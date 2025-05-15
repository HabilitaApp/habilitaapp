# themes.py  –  Banco de questões HABILITA
# -------------------------------------------------
# Cada item contém "enunciado", "alternativas", "resposta", "comentario"
# Coloque aqui as 100 questões de Direito Civil + 60 de Registros Públicos.
# Abaixo apresento UM exemplo por bloco para você copiar o padrão.
# -------------------------------------------------

THEMES = {
    "parte_geral": {
        "title": "Parte Geral",
        "questions": [
            {
                "enunciado": "O negócio jurídico celebrado por absolutamente incapaz é...",
                "alternativas": ["nulo", "anulável", "inexistente", "eficaz mediante confirmação"],
                "resposta": "nulo",
                "comentario": "Art. 166 I CC."
            },
            # … mais 9 perguntas …
        ]
    },

    "coisas": {
        "title": "Direitos Reais (Coisas)",
        "questions": [
            {
                "enunciado": "A acessão natural ocorre pelo(a)...",
                "alternativas": ["Aluvião", "Construção ou plantação", "Adjacência", "Usucapião"],
                "resposta": "Aluvião",
                "comentario": "Art. 1.250 CC."
            },
            # … mais 9 perguntas …
        ]
    },

    # --- adicione família, sucessões, obrigações, contratos ---

    "rp_titulo_i": {
        "title": "RP – Título I (Disposições Gerais)",
        "questions": [
            {
                "enunciado": "A Lei 6.015/73 visa assegurar autenticidade, segurança e ____ dos atos jurídicos.",
                "alternativas": ["legitimidade", "publicidade", "eficácia", "validade"],
                "resposta": "eficácia",
                "comentario": "Art. 1º caput."
            },
            # … mais 9 perguntas …
        ]
    },

    # --- rp_titulo_ii  … rp_titulo_vi (cada um com 10 perguntas) ---
}
