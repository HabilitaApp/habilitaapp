# -*- coding: utf-8 -*-
"""
app.py – HABILITA (versão compacta de teste)
==================================================
Fluxo: Login → Seleção de Tema → Nível (Iniciante/Intermediário/Avançado)
Certificado PDF + QR emitido quando pontuação ≥ 70 %.
Esta versão compacta usa 3 questões por tema para facilitar deploy.
"""

import streamlit as st
from typing import Dict, List
from io import BytesIO
import uuid, datetime

from fpdf import FPDF           # biblioteca 100 % Python
import qrcode
from PIL import Image

# -------------------------------------------------
# Importa banco de questões estruturado por nível
# -------------------------------------------------
from themes import THEMES        # themes.py deve estar no mesmo diretório

# ---------------- CONFIG ----------------
USERS: Dict[str, str] = {"demo@habilita.app": "senha123"}
THRESHOLD = 0.7  # 70 %
VERIFY_URL = "https://habilita.app/verify/"  # placeholder

# ---------------- PDF ----------------

def _latin(txt: str) -> str:
    """Converte caracteres não compatíveis com core-font para latin‑1."""
    return txt.replace("–", "-").replace("—", "-").encode("latin-1", "ignore").decode("latin-1")


def make_pdf(email: str, tema: str, nivel: str, pct: float) -> BytesIO:
    cert_id = str(uuid.uuid4())
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 20)
    pdf.cell(0, 12, _latin("CERTIFICADO HABILITA"), ln=1, align="C")

    pdf.set_font("Helvetica", size=12)
    pdf.multi_cell(0, 8, _latin(f"{email} concluiu '{tema}' – nível {nivel} – com {pct*100:.0f}% de acertos."), align="C")
    pdf.cell(0, 7, _latin(f"Emitido em {datetime.date.today():%d/%m/%Y} | ID {cert_id}"), ln=1, align="C")

    qr = qrcode.make(f"{VERIFY_URL}{cert_id}")
    buf = BytesIO(); qr.save(buf); buf.seek(0)
    pdf.image(buf, x=(210-40)/2, y=pdf.get_y()+4, w=40)

    out = BytesIO(pdf.output())
    out.seek(0)
    return out

# ---------------- STATE ----------------

def init_state():
    if "auth" not in st.session_state:
        st.session_state.update({
            "auth": False,
            "email": "",
            "scores": {},   # {(tema, nivel): pct}
            "certs":  {},
        })

# ---------------- UI ----------------

def login():
    st.title("HABILITA – Pré‑ENAC (teste)")
    e = st.text_input("E‑mail"); p = st.text_input("Senha", type="password")
    if st.button("Entrar") and USERS.get(e) == p:
        st.session_state.update({"auth": True, "email": e}); st.experimental_rerun()

# ---------- avaliação automática simples ----------

def score_obj(questions: List[Dict], answers: List[str]) -> float:
    return sum(a == q["resposta"] for a, q in zip(answers, questions)) / len(questions)

def score_text(text: str, min_words: int) -> float:
    return 1.0 if len(text.split()) >= min_words else 0.5

# ---------- fluxo de nível ----------

def handle_result(tema_key: str, nivel: str, pct: float):
    key = (tema_key, nivel)
    st.session_state["scores"][key] = pct
    if pct >= THRESHOLD:
        st.session_state["certs"][key] = True
        st.success(f"Aprovado com {pct*100:.0f}%!")
        pdf = make_pdf(st.session_state["email"], THEMES[tema_key]['title'], nivel, pct)
        st.download_button("📄 Baixar Certificado", pdf, file_name=f"cert_{tema_key}_{nivel}.pdf")
    else:
        st.warning(f"{pct*100:.0f}% – necessário 70 %.")


def run_iniciante(tema_key: str):
    qs = THEMES[tema_key]["iniciante"]
    resp = [st.radio(q["enunciado"], q["alternativas"], key=f"{tema_key}_{i}") for i, q in enumerate(qs)]
    if st.button("Enviar (Iniciante)"):
        pct = score_obj(qs, resp)
        handle_result(tema_key, "Iniciante", pct)
        with st.expander("Gabarito"):
            for i, q in enumerate(qs, 1):
                st.write(f"{i}. {q['resposta']} – {q['comentario']}")


def run_intermediario(tema_key: str):
    prompt = THEMES[tema_key]["intermediario"]["enunciado"]
    st.write(prompt)
    text = st.text_area("Resposta (80‑120 palavras)")
    if st.button("Enviar (Intermediário)"):
        pct = score_text(text, 80)
        handle_result(tema_key, "Intermediário", pct)


def run_avancado(tema_key: str):
    prompt = THEMES[tema_key]["avancado"]["enunciado"]
    st.write(prompt)
    text = st.text_area("Resposta (≥200 palavras)", height=250)
    if st.button("Enviar (Avançado)"):
        pct = score_text(text, 200)
        handle_result(tema_key, "Avançado", pct)

# -------------- painel --------------

def painel():
    st.title("Painel de Desempenho")
    for tkey, tval in THEMES.items():
        st.subheader(tval["title"])
        for nivel in ("Iniciante", "Intermediário", "Avançado"):
            k = (tkey, nivel)
            pct = st.session_state["scores"].get(k, 0) * 100
            label = "✅" if st.session_state["certs"].get(k) else f"{pct:.0f}%"
            st.write(f"{nivel}: {label}")

# -------------- main --------------

def main():
    st.set_page_config(page_title="HABILITA – ENAC (teste)")
    init_state()
    if not st.session_state["auth"]:
        login(); return

    choice = st.sidebar.radio("Menu", ("Painel", "Nova Avaliação", "Sair"))
    if choice == "Painel":
        painel()
    elif choice == "Nova Avaliação":
        tema_key = st.selectbox("Tema", THEMES.keys(), format_func=lambda k: THEMES[k]['title'])
        nivel = st.radio("Nível", ("Iniciante", "Intermediário", "Avançado"))
        if nivel == "Iniciante":
            run_iniciante(tema_key)
        elif nivel == "Intermediário":
            run_intermediario(tema_key)
        else:
            run_avancado(tema_key)
    else:
        st.session_state.clear(); st.experimental_rerun()

if __name__ == "__main__":
    main()
