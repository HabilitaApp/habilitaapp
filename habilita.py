import streamlit as st

from typing import Dict, List

from io import BytesIO

import uuid, datetime



from fpdf import FPDF          # biblioteca 100 % Python (já na requirements)

import qrcode

from PIL import Image



# -------------------------------------------------

#  HABILITA – Pré-ENAC   (app.py)

#  • lógica Streamlit

#  • emissão de PDF com QR via fpdf2

#  • importa QUESTÕES do arquivo themes.py

# -------------------------------------------------



from themes import THEMES      #  << precisa do arquivo themes.py irmão



USERS       : Dict[str, str] = {"demo@habilita.app": "senha123"}

THRESHOLD   : float           = 0.7          # ≥70 % para certificar

VERIFY_URL  : str             = "https://habilita.app/verify/"  # placeholder



# ---------- PDF gerado via fpdf2 ----------

def make_certificate(email: str, topic: str, pct: float) -> BytesIO:

    cert_id = str(uuid.uuid4())

    pdf = FPDF(orientation="P", unit="mm", format="A4")

    pdf.add_page()

    pdf.set_font("Helvetica", "B", 20)

    pdf.cell(0, 15, "CERTIFICADO HABILITA", ln=1, align="C")

    pdf.set_font("Helvetica", size=12)

    pdf.multi_cell(

        0, 8,

        txt=f"Certificamos que {email} concluiu “{topic}” "

            f"com {pct*100:.0f}% de acertos.",

        align="C"

    )

    pdf.cell(0, 8,

             f"Emitido em {datetime.date.today():%d/%m/%Y}  |  ID {cert_id}",

             ln=1, align="C")



    # QR-Code central

    qr_img = qrcode.make(f"{VERIFY_URL}{cert_id}")

    buf = BytesIO(); qr_img.save(buf); buf.seek(0)

    pdf.image(buf, x=(210-40)/2, y=pdf.get_y()+4, w=40)



    out = BytesIO(pdf.output())      # devolve PDF binário

    out.seek(0)

    return out



# ---------- estado ----------

def init_state():

    if "auth" not in st.session_state:

        st.session_state.update({

            "auth": False,

            "email": "",

            "scores": {k: 0.0 for k in THEMES},

            "certs":  {k: False for k in THEMES},

        })



# ---------- UI ----------

def login():

    st.title("🔐 Login – HABILITA (Pré-ENAC)")

    st.markdown("**74/100** questões do ENAC tratam de Direito Civil e Notarial/Registral.")

    e = st.text_input("E-mail")

    p = st.text_input("Senha", type="password")

    if st.button("Entrar") and USERS.get(e) == p:

        st.session_state.update({"auth": True, "email": e})

        st.experimental_rerun()



def run_quiz(key: str):

    tema = THEMES[key]

    st.header(tema["title"])

    answers: List[str] = [

        st.radio(q["enunciado"], q["alternativas"], key=f"{key}_{i}")

        for i, q in enumerate(tema["questions"])

    ]

    if st.button("Enviar respostas"):

        hits = sum(a == q["resposta"] for a, q in zip(answers, tema["questions"]))

        pct  = hits / len(tema["questions"])

        st.session_state["scores"][key] = pct

        if pct >= THRESHOLD:

            st.session_state["certs"][key] = True

            st.success(f"🎉 {pct*100:.0f}% – certificado liberado!")

            pdf = make_certificate(st.session_state["email"], tema["title"], pct)

            st.download_button("📄 Baixar PDF", pdf, file_name=f"cert_{key}.pdf")

        else:

            st.warning(f"{pct*100:.0f}% – mínimo 70 %.")

        with st.expander("Gabarito comentado"):

            for i, q in enumerate(tema["questions"], 1):

                st.write(f"**{i}.** {q['resposta']} — {q['comentario']}")



def dashboard():

    st.title("📊 Painel")

    for k, v in THEMES.items():

        pct = st.session_state["scores"][k] * 100

        tag = "✅ Certificado" if st.session_state["certs"][k] else f"{pct:.0f}%"

        st.write(f"- **{v['title']}** — {tag}")



# ---------- main ----------

def main():

    st.set_page_config(page_title="HABILITA – ENAC", layout="centered")

    init_state()

    if not st.session_state["auth"]:

        login(); return



    choice = st.sidebar.radio("Menu", ("Painel", "Nova Avaliação", "Sair"))

    if choice == "Painel":

        dashboard()

    elif choice == "Nova Avaliação":

        key = st.selectbox("Tema", THEMES.keys(), format_func=lambda k: THEMES[k]['title'])

        run_quiz(key)

    else:

        st.session_state.clear(); st.experimental_rerun()



if __name__ == "__main__":

    main()

