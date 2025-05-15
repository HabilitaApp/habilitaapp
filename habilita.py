import streamlit as st
from typing import Dict, List
from io import BytesIO
import uuid, datetime

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import qrcode
from PIL import Image

# -----------------------------------------------------------------
#  HABILITA – Pré-ENAC  |  app.py
# -----------------------------------------------------------------
# • Lógica Streamlit + emissão de certificados PDF/QR
# • O dicionário com todas as questões fica em  themes.py
#   (mesmo diretório).  →  from themes import THEMES
# -----------------------------------------------------------------

from themes import THEMES  # ✓ 100 questões de Civil + 60 de Registros

# ---------------- CONFIG ----------------
USERS: Dict[str, str] = {"demo@habilita.app": "senha123"}
THRESHOLD: float       = 0.7  # ≥ 70 % para certificar
VERIFY_URL: str        = "https://habilita.app/verify/"  # TODO endpoint real

# ---------------- PDF ----------------

def cert_pdf(email: str, tema: str, pct: float) -> BytesIO:
    """Gera certificado A4 em PDF com QR-Code de verificação."""
    buf = BytesIO(); cert_id = str(uuid.uuid4())
    c = canvas.Canvas(buf, pagesize=A4); W, H = A4

    c.setFont("Helvetica-Bold", 22)
    c.drawCentredString(W / 2, H - 90, "CERTIFICADO HABILITA")
    c.setFont("Helvetica", 12)
    c.drawCentredString(W / 2, H - 120,
                        f"{email} concluiu \"{tema}\" com {pct*100:.0f}% de acertos.")
    c.drawCentredString(W / 2, H - 140,
                        f"Emitido em {datetime.date.today():%d/%m/%Y} | ID {cert_id}")

    qr_img = qrcode.make(f"{VERIFY_URL}{cert_id}")
    qr_buf = BytesIO(); qr_img.save(qr_buf); qr_buf.seek(0)
    c.drawInlineImage(Image.open(qr_buf), (W - 110) / 2, H - 280, 110, 110)

    c.showPage(); c.save(); buf.seek(0)
    return buf

# -------------- STATE --------------

def init_state() -> None:
    if "auth" not in st.session_state:
        st.session_state.update({
            "auth": False,
            "email": "",
            "scores": {k: 0.0 for k in THEMES},
            "certs": {k: False for k in THEMES},
        })

# -------------- UI --------------

def login() -> None:
    st.title("🔐 Login – HABILITA (Pré-ENAC)")
    st.markdown("**74/100** questões do ENAC são de Direito Civil e Notarial/Registral.")
    e = st.text_input("E-mail"); p = st.text_input("Senha", type="password")
    if st.button("Entrar") and USERS.get(e) == p:
        st.session_state.update({"auth": True, "email": e}); st.experimental_rerun()


def quiz(key: str) -> None:
    tema = THEMES[key]
    st.header(tema["title"])
    answers: List[str] = [
        st.radio(q["enunciado"], q["alternativas"], key=f"{key}_{i}")
        for i, q in enumerate(tema["questions"])
    ]
    if st.button("Enviar respostas"):
        correct = sum(a == q["resposta"] for a, q in zip(answers, tema["questions"]))
        pct = correct / len(tema["questions"])
        st.session_state["scores"][key] = pct
        if pct >= THRESHOLD:
            st.session_state["certs"][key] = True
            st.success(f"👏 {pct*100:.0f}% – certificado liberado!")
            pdf = cert_pdf(st.session_state["email"], tema["title"], pct)
            st.download_button("📄 Baixar PDF", data=pdf, file_name=f"cert_{key}.pdf")
        else:
            st.warning(f"{pct*100:.0f}% – mínimo {THRESHOLD*100:.0f}%.")
        with st.expander("Gabarito comentado"):
            for i, q in enumerate(tema["questions"], 1):
                st.write(f"**{i}.** {q['resposta']} — {q['comentario']}")


def painel() -> None:
    st.title("📊 Painel de Desempenho")
    for k, v in THEMES.items():
        pct = st.session_state["scores"][k] * 100
        label = "✅ Certificado" if st.session_state["certs"][k] else f"{pct:.0f}%"
        st.write(f"- **{v['title']}** — {label}")

# -------------- MAIN --------------

def main() -> None:
    st.set_page_config(page_title="HABILITA – ENAC", layout="centered")
    init_state()
    if not st.session_state["auth"]:
        login(); return

    st.sidebar.title("HABILITA")
    choice = st.sidebar.radio("Menu", ("Painel", "Nova Avaliação", "Sair"))

    if choice == "Painel":
        painel()
    elif choice == "Nova Avaliação":
        key = st.selectbox("Selecione o tema", list(THEMES.keys()), format_func=lambda k: THEMES[k]['title'])
        quiz(key)
    else:  # Sair
        st.session_state.clear(); st.experimental_rerun()

if __name__ == "__main__":
    main()
