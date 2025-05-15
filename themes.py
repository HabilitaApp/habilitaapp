# themes.py – Versão compacta para TESTE (3 questões por tema)
# ------------------------------------------------------------------
# 12 temas × 3 níveis:
#   • Iniciante  → 3 questões objetivas (para testes rápidos)
#   • Intermediário → 1 prompt discursivo
#   • Avançado → 1 prompt parecer/minuta
# ------------------------------------------------------------------
# OBS: Após validação do fluxo, basta substituir cada lista "iniciante"
#      por 10 questões completas (ou mais) mantendo a mesma estrutura.
# ------------------------------------------------------------------

THEMES = {
    # ==========================================================
    # 1. DIREITO CIVIL (6 temas)
    # ==========================================================

    "parte_geral": {
        "title": "Parte Geral",
        "iniciante": [
            {"enunciado": "O negócio jurídico celebrado por absolutamente incapaz é...", "alternativas": ["nulo", "anulável", "inexistente", "eficaz mediante confirmação"], "resposta": "nulo", "comentario": "Art. 166 I CC."},
            {"enunciado": "A personalidade civil da pessoa começa...", "alternativas": ["concepção", "nascimento com vida", "registro civil", "maioridade"], "resposta": "nascimento com vida", "comentario": "Art. 2º CC."},
            {"enunciado": "São absolutamente incapazes: ___", "alternativas": ["menores de 16", "menores de 18", "maiores interditos", "pródigos"], "resposta": "menores de 16", "comentario": "Art. 3º CC."}
        ],
        "intermediario": {
            "enunciado": "Explique (80‑120 palavras) a função social do contrato conforme arts. 421‑422 CC.",
            "comentario": "Conceito + efeito na interpretação dos negócios." },
        "avancado": {
            "enunciado": "Parecer (≥200 palavras) sobre nulidade de cláusula abusiva em contrato de adesão sob a ótica da boa‑fé objetiva.",
            "comentario": "Incluir fundamentos legais e orientação prática." }
    },

    "coisas": {
        "title": "Direitos Reais (Coisas)",
        "iniciante": [
            {"enunciado": "Prazo mínimo da usucapião extraordinária é...", "alternativas": ["5", "10", "15", "20"], "resposta": "15", "comentario": "Art. 1.238."},
            {"enunciado": "Servidão é direito real sobre coisa...", "alternativas": ["própria", "alheia"], "resposta": "alheia", "comentario": "Art. 1.378."},
            {"enunciado": "Possuidor de boa‑fé pode reter benfeitorias...", "alternativas": ["necessárias", "úteis", "voluptuárias"], "resposta": "úteis", "comentario": "Art. 1.219."}
        ],
        "intermediario": {"enunciado": "Diferencie posse direta e indireta (80‑100 palavras).", "comentario": "Arts. 1.196‑1.197."},
        "avancado": {"enunciado": "Elabore minuta de sentença concedendo usucapião extraordinária (≥200 palavras).", "comentario": "Citar art. 1.238 e requisitos."}
    },

    "familia": {
        "title": "Família",
        "iniciante": [
            {"enunciado": "União estável gera regime supletivo de...", "alternativas": ["separação", "comunhão parcial", "universal"], "resposta": "comunhão parcial", "comentario": "Art. 1.725."},
            {"enunciado": "Alimentos gravídicos cessam com...", "alternativas": ["concepção", "nascimento", "6 meses"], "resposta": "nascimento", "comentario": "Lei 11.804/08."},
            {"enunciado": "Idade mínima de diferença para adoção: ___ anos.", "alternativas": ["14", "16", "18"], "resposta": "16", "comentario": "Art. 42 §3º ECA."}
        ],
        "intermediario": {"enunciado": "Explique, em 100 palavras, quando se aplica guarda compartilhada obrigatória.", "comentario": "Art. 1.584 CC."},
        "avancado": {"enunciado": "Redija parecer sobre possibilidade de alteração de nome do filho menor (≥200 palavras).", "comentario": "Art. 56 LRP + interesse do menor."}
    },

    "sucessoes": {
        "title": "Sucessões",
        "iniciante": [
            {"enunciado": "Legítima corresponde a ___ da herança.", "alternativas": ["1/3", "1/2", "2/3"], "resposta": "1/2", "comentario": "Art. 1.846."},
            {"enunciado": "Herdeiro que renuncia é...", "alternativas": ["excluído", "representado", "colacionado"], "resposta": "excluído", "comentario": "Art. 1.811."},
            {"enunciado": "Testamento público é lavrado em...", "alternativas": ["cartório", "particular", "juízo"], "resposta": "cartório", "comentario": "Art. 1.864."}
        ],
        "intermediario": {"enunciado": "Em 100 palavras, conceitue indignidade e cite hipótese do art. 1.814.", "comentario": "Citar homicídio doloso ou calúnia."},
        "avancado": {"enunciado": "Parecer (≥200 palavras) sobre direito de representação na sucessão colateral.", "comentario": "Explicar inexistência art. 1.851."}
    },

    "obrigacoes": {
        "title": "Obrigações",
        "iniciante": [
            {"enunciado": "Mora ex persona exige...", "alternativas": ["notificação", "prazo certo"], "resposta": "notificação", "comentario": "Art. 397."},
            {"enunciado": "Na obrigação alternativa, a escolha pertence...", "alternativas": ["devedor", "credor"], "resposta": "devedor", "comentario": "Art. 252."},
            {"enunciado": "Confusão extingue a obrigação quando...", "alternativas": ["cédula única", "credor = devedor"], "resposta": "credor = devedor", "comentario": "Art. 381."}
        ],
        "intermediario": {"enunciado": "Explique cláusula penal compensatória (80‑120 palavras).", "comentario": "Art. 416."},
        "avancado": {"enunciado": "Redija parecer sobre possibilidade de revisão contratual por onerosidade excessiva (≥200 palavras).", "comentario": "Art. 478."}
    },

    "contratos": {
        "title": "Contratos",
        "iniciante": [
            {"enunciado": "Contrato unilateral é aquele em que...", "alternativas": ["1 parte assume obrigação", "ambas partes"], "resposta": "1 parte assume obrigação", "comentario": "Art. 541."},
            {"enunciado": "Locação de imóvel urbano residencial: lei...", "alternativas": ["8.245/91", "10.406/02"], "resposta": "8.245/91", "comentario": "Lei de Locações."},
            {"enunciado": "Compra e venda entre ascendente e descendente depende...", "alternativas": ["consentimento", "escritura"], "resposta": "consentimento", "comentario": "Art. 496."}
        ],
        "intermediario": {"enunciado": "Conceitue contrato aleatório e dê exemplo (80‑120 palavras).", "comentario": "Art. 458."},
        "avancado": {"enunciado": "Elabore minuta de contrato estimatório (≥200 palavras) com cláusula de responsabilidade.", "comentario": "Art. 534."}
    },

    # ==========================================================
    # 2. REGISTROS PÚBLICOS (6 Títulos)
    # ==========================================================

    "rp_titulo_i": {
        "title": "RP – Título I (Disposições Gerais)",
        "iniciante": [
            {"enunciado": "Lei 6.015/73 visa autenticidade, segurança e...", "alternativas": ["eficácia", "legitimidade"], "resposta": "eficácia", "comentario": "Art. 1º."},
            {"enunciado": "Registro de protesto NÃO consta no art. 1º §1º.", "alternativas": ["Verdadeiro", "Falso"], "resposta": "Verdadeiro", "comentario": "Art. 1º."},
            {"enunciado": "Livros podem ter até ___ m de largura", "alternatives": ["0,40", "0,30"], "resposta": "0,40", "comentario": "Art. 3º §1º."}
        ],
        "intermediario": {"enunciado": "Explique finalidade do Livro 2 – Matrícula (80‑100 palavras).", "comentario": "Art. 176."},
        "avancado": {"enunciado": "Minute despacho para abertura de matrícula após usucapião extrajudicial (≥200 palavras).", "comentario": "Art. 216‑A."}
    },

    "rp_titulo_ii": {
        "title": "RP – Título II (Pessoas Naturais)",
        "iniciante": [
            {"enunciado": "Prazo ordinário de registro de nascimento: ___ dias", "alternativas": ["15", "30"], "resposta": "15", "comentario": "Art. 50."},
            {"enunciado": "Registro tardio faz‑se no domicílio do interessado.", "alternativas": ["V", "F"], "resposta": "V", "comentario": "Art. 46."},
            {"enunciado": "Mapas trimestrais de nascimentos são enviados ao IBGE em ___ dias", "alternativas": ["8", "15"], "resposta": "8", "comentario": "Art. 49."}
        ],
        "intermediario": {"enunciado": "Em 100 palavras, aponte documentos exigidos para registro tardio de nascimento.", "comentario": "Art. 46."},
        "avancado": {"enunciado": "Elabore minuta de decisão que determina averbação de alteração de prenome de maior de idade (≥200 palavras).", "comentario": "Art. 56."}
    },

    "rp_titulo_iii": {
        "title": "RP – Título III (Pessoas Jurídicas)",
        "iniciante": [
            {"enunciado": "RCPJ registra sociedades ___", "alternativas": ["simples", "anônimas"], "resposta": "simples", "comentario": "Art. 114."},
            {"enunciado": "Alteração estatutária deve ser arquivada em ___ dias", "alternativas": ["30", "60"], "resposta": "30", "comentario": "Art. 118."},
            {"enunciado": "Recurso ao juiz contra o oficial: prazo ___ dias", "alternativas": ["5", "15"], "resposta": "5", "comentario": "Art. 127."}
        ],
        "intermediario": {"enunciado": "Explique (80‑100 palavras) a publicidade dos atos de PJ no RCPJ.", "comentario": "Art. 118."},
        "avancado": {"enunciado": "Redija despacho deferindo registro de associação estrangeira (≥200 palavras).", "comentario": "Art. 122."}
    },

    "rp_titulo_iv": {
        "title": "RP – Título IV (Títulos e Documentos)",
        "iniciante": [
            {"enunciado": "RTD garante ___ dos documentos", "alternativas": ["autenticidade", "validade"], "resposta": "autenticidade", "comentario": "Art. 127."},
            {"enunciado": "Locação registrada no RTD vale contra terceiros.", "alternativas": ["V", "F"], "resposta": "V", "comentario": "Art. 129 VII."},
            {"enunciado": "Documento estrangeiro precisa de ___", "alternativas": ["tradução juramentada", "apenas carimbo"], "resposta": "tradução juramentada", "comentario": "Art. 132."}
        ],
        "intermediario": {"enunciado": "Explique efeito erga omnes do registro de cessão de crédito (80‑100 palavras).", "comentario": "Art. 129 VIII."},
        "avancado": {"enunciado": "Minute ato de registro de contrato de locação com cláusula de vigência (≥200 palavras).", "comentario": "Art. 129 VII."}
    },

    "rp_titulo_v": {
        "title": "RP – Título V (Registro de Imóveis)",
        "iniciante": [
            {"enunciado": "A matrícula individualiza o imóvel: art. ___", "alternativas": ["176", "167"], "resposta": "176", "comentario": "Art. 176."},
            {"enunciado": "Prenotação vigora por ___ dias", "alternativas": ["30", "60"], "resposta": "30", "comentario": "Art. 205."},
            {"enunciado": "Usucapião extrajudicial está no art. ___", "alternativas": ["216‑A", "225"], "resposta": "216‑A", "comentario": "Art. 216‑A."}
        ],
        "intermediario": {"enunciado": "Descreva (80‑120 palavras) etapas da averbação de georreferenciamento.", "comentario": "Art. 176 §3º."},
        "avancado": {"enunciado": "Parecer (≥200 palavras) sobre dúvida suscitada pelo oficial em registro de hipoteca.", "comentario": "Art. 198."}
    },

    "rp_titulo_vi": {
        "title": "RP – Título VI (Disposições Finais)",
        "iniciante": [
            {"enunciado": "Livros só saem do cartório com autorização ___", "alternativas": ["judicial", "do oficial"], "resposta": "judicial", "comentario": "Art. 22."},
            {"enunciado": "Oficial responde civilmente por atos próprios e de prepostos.", "alternativas": ["V", "F"], "resposta": "V", "comentario": "Art. 28."},
            {"enunciado": "Multa por recusa injusta de registro: ___ salário mínimo", "alternativas": ["um", "dez"], "resposta": "um", "comentario": "Art. 47 §1º."}
        ],
        "intermediario": {"enunciado": "Explique correição permanente dos livros (80‑100 palavras).", "comentario": "Art. 48."},
        "avancado": {"enunciado": "Redija decisão impondo multa a oficial que recusa registro sem fundamento (≥200 palavras).", "comentario": "Art. 47."}
    }
