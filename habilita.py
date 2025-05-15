import streamlit as st
from typing import Dict, List
from io import BytesIO
import uuid, datetime

from fpdf import FPDF            # pure‑python PDF
import qrcode
from PIL import Image

"""
HABILITA – Pré‑ENAC (v3)
====================================================
Níveis de desafio:
• Iniciante  → questões objetivas (1ª fase)
• Intermediário → discursiva curta (2ª fase / prova escrita)
• Avançado → parecer/minuta (2ª fase avançada)
Certificado emitido por Tema **e** Nível (>=70 % ou avaliação manual ✅).
====================================================
"""

from themes import THEMES        # themes.py possui estrutura por nível

USERS: Dict[str, str] = {"demo@habilita.app": "senha123"}
THRESHOLD = 0.7
VERIFY_URL = "https://habilita.app/verify/"

# ---------------- PDF helper ----------------

def _sanitize(txt: str) -> str:
    return txt.replace("–", "-").replace("—", "-").encode("latin-1", "ignore").decode("latin-1")

def make_pdf(email: str, tema: str, nivel: str, pct: float) -> BytesIO:
    cid = str(uuid.uuid4())
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 20)
    pdf.cell(0, 12, _sanitize("CERTIFICADO HABILITA"), ln=1, align="C")
    pdf.set_font("Helvetica", size=12)
    pdf.multi_cell(0, 8, _sanitize(f"{email} concluiu '{tema}' – nível {nivel} – com {pct*100:.0f}% de aproveitamento."), align="C")
    pdf.cell(0, 7, _sanitize(f"{datetime.date.today():%d/%m/%Y}  |  ID {cid}"), ln=1, align="C")
    qr = qrcode.make(f"{VERIFY_URL}{cid}"); buf=BytesIO(); qr.save(buf); buf.seek(0)
    pdf.image(buf, x=(210-40)/2, y=pdf.get_y()+4, w=40)
    out = BytesIO(pdf.output()); out.seek(0); return out

# ---------------- state ----------------

def init_state():
    if "auth" not in st.session_state:
        st.session_state.update({
            "auth": False,
            "email": "",
            "scores": {},       # key = (tema,nivel)
            "certs":  {},
        })

# -------------- ui helpers --------------

def login():
    st.title("🔐 HABILITA – Pré‑ENAC")
    e = st.text_input("E‑mail"); p = st.text_input("Senha", type="password")
    if st.button("Entrar") and USERS.get(e) == p:
        st.session_state.update({"auth": True, "email": e}); st.experimental_rerun()

# ---------- evaluation placeholders ----------

def auto_score_objective(questions: List[Dict], answers: List[str]) -> float:
    hits = sum(a==q["resposta"] for a,q in zip(answers, questions))
    return hits/len(questions)

def auto_score_discursiva(text:str) -> float:
    """placeholder – simples length check"""
    return 1.0 if len(text.split())>=80 else 0.6

def auto_score_parecer(text:str) -> float:
    return 1.0 if len(text.split())>=200 else 0.5

# ---------- quiz by level ----------

def run_iniciante(tema_key:str):
    data = THEMES[tema_key]["iniciante"]
    ans=[st.radio(q["enunciado"],q["alternativas"],key=f"{tema_key}_ini_{i}") for i,q in enumerate(data)]
    if st.button("Enviar (Iniciante)"):
        pct=auto_score_objective(data,ans); handle_result(tema_key,"Iniciante",pct)
        with st.expander("Gabarito"):
            for i,q in enumerate(data,1):
                st.write(f"{i}. {q['resposta']} – {q['comentario']}")

def run_discursiva(tema_key:str):
    text=st.text_area("Redija sua resposta (mín. 80 palavras)")
    if st.button("Enviar (Intermediário)"):
        pct=auto_score_discursiva(text)
        handle_result(tema_key,"Intermediário",pct)

def run_parecer(tema_key:str):
    text=st.text_area("Elabore o parecer/minuta (mín. 200 palavras)", height=300)
    if st.button("Enviar (Avançado)"):
        pct=auto_score_parecer(text)
        handle_result(tema_key,"Avançado",pct)

# ---------- result + cert ----------

def handle_result(tema_key:str,nivel:str,pct:float):
    key=(tema_key,nivel)
    st.session_state["scores"][key]=pct
    if pct>=THRESHOLD:
        st.session_state["certs"][key]=True
        st.success(f"Aprovado com {pct*100:.0f}%!")
        pdf=make_pdf(st.session_state["email"],THEMES[tema_key]['title'],nivel,pct)
        st.download_button("📄 Baixar Certificado",pdf,file_name=f"cert_{tema_key}_{nivel}.pdf")
    else:
        st.warning(f"{pct*100:.0f}% – necessário 70%")

# ---------- dashboard ----------

def panel():
    st.title("📊 Painel")
    for tema_key,tema in THEMES.items():
        st.subheader(tema['title'])
        for nivel in ("Iniciante","Intermediário","Avançado"):
            key=(tema_key,nivel)
            pct=st.session_state["scores"].get(key,0)*100
            label="✅" if st.session_state["certs"].get(key,False) else f"{pct:.0f}%"
            st.write(f"{nivel}: {label}")

# ---------- main ----------

def main():
    st.set_page_config(page_title="HABILITA – ENAC",layout="centered")
    init_state()
    if not st.session_state["auth"]:
        login(); return

    choice=st.sidebar.radio("Menu",("Painel","Nova Avaliação","Sair"))
    if choice=="Painel":
        panel()
    elif choice=="Nova Avaliação":
        tema_key=st.selectbox("Tema",list(THEMES.keys()),format_func=lambda k:THEMES[k]['title'])
        nivel=st.radio("Escolha o nível",("Iniciante","Intermediário","Avançado"))
        if nivel=="Iniciante":
            run_iniciante(tema_key)
        elif nivel=="Intermediário":
            run_discursiva(tema_key)
        else:
            run_parecer(tema_key)
    else:
        st.session_state.clear(); st.experimental_rerun()

if __name__=="__main__":
    main()
