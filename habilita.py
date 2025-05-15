import streamlit as st

from typing import Dict, List

from io import BytesIO

import uuid, datetime



from fpdf import FPDF  # ✔️ 100% Pure‑Python (evita problemas de compilação)

import qrcode

from PIL import Image



# -----------------------------------------------------------------

#  HABILITA – Pré‑ENAC  |  app.py   (v2 – sem ReportLab)

# -----------------------------------------------------------------

# • Streamlit + emissão de certificados PDF/QR usando fpdf2 (pure Python)

# • Questões estão em  themes.py

# -----------------------------------------------------------------



from themes import THEMES



# ---------------- CONFIG ----------------

USERS: Dict[str, str] = {"demo@habilita.app": "senha123"}

THRESHOLD = 0.7  # 70 %

VERIFY_URL = "https://habilita.app/verify/"



# ---------------- PDF ----------------



def cert_pdf(email: str, tema: str, pct: float) -> BytesIO:

    """Gera certificado (A4) em PDF via fpdf2 e retorna buffer."""

    cert_id = str(uuid.uuid4())

    pdf = FPDF("P", "mm", "A4")

    pdf.add_page()

    pdf.set_font("Helvetica", "B", 20)

    pdf.cell(0, 15, "CERTIFICADO HABILITA", align="C", ln=1)

    pdf.ln(5)

    pdf.set_font("Helvetica", size=12)

    pdf.multi_cell(0, 8,

        txt=f"Certificamos que {email} concluiu \"{tema}\" com {pct*100:.0f}% de acertos.",

        align="C")

    pdf.ln(2)

    pdf.cell(0, 8, f"Emitido em {datetime.date.today():%d/%m/%Y} | ID {cert_id}", align="C", ln=1)



    # QR‑Code

    qr_img = qrcode.make(f"{VERIFY_URL}{cert_id}")

    buf_qr = BytesIO(); qr_img.save(buf_qr); buf_qr.seek(0)

    pdf.image(buf_qr, x=(210-40)/2, y=pdf.get_y()+4, w=40)



    out = BytesIO(pdf.output())

    out.seek(0)

    return out



# -------------- STATE --------------



def init_state():

    if "auth" not in st.session_state:

        st.session_state.update({

            "auth": False,

            "email": "",

            "scores": {k: 0.0 for k in THEMES},

            "certs": {k: False for k in THEMES},

        })



# -------------- UI --------------



def login():

    st.title("🔐 Login – HABILITA (Pré‑ENAC)")

    st.markdown("**74/100** questões do ENAC são de Direito Civil e Notarial/Registral.")

    e = st.text_input("E‑mail"); p = st.text_input("Senha", type="password")

    if st.button("Entrar") and USERS.get(e) == p:

        st.session_state.update({"auth": True, "email": e}); st.experimental_rerun()





def quiz(key: str):

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

            st.success(f"🎉 {pct*100:.0f}% – certificado disponível!")

            pdf = cert_pdf(st.session_state["email"], tema["title"], pct)

            st.download_button("📄 Baixar PDF", data=pdf, file_name=f"cert_{key}.pdf")

        else:

            st.warning(f"{pct*100:.0f}% – mínimo 70 %.")

        with st.expander("Gabarito comentado"):

            for i, q in enumerate(tema["questions"], 1):

                st.write(f"**{i}.** {q['resposta']} — {q['comentario']}")





def painel():

    st.title("📊 Painel de Desempenho")

    for k, v in THEMES.items():

        pct = st.session_state["scores"][k] * 100

        st.write(f"- **{v['title']}** — {'✅' if st.session_state['certs'][k] else f'{pct:.0f}%'}")



# -------------- MAIN --------------



def main():

    st.set_page_config(page_title="HABILITA – ENAC", layout="centered")

    init_state()

    if not st.session_state["auth"]:

        login(); return



    choice = st.sidebar.radio("Menu", ("Painel", "Nova Avaliação", "Sair"))

    if choice == "Painel":

        painel()

    elif choice == "Nova Avaliação":

        k = st.selectbox("Tema", list(THEMES.keys()), format_func=lambda k: THEMES[k]['title'])

        quiz(k)

    else:

        st.session_state.clear(); st.experimental_rerun()



if __name__ == "__main__":

    main()
