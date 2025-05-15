# themes.py  –  Banco de questões HABILITA
# -------------------------------------------------
# 100 questões de Direito Civil  +  60 de Registros Públicos (Lei 6.015/73)
# Cada bloco contém exactly 10 questões.

THEMES = {
parte_geral": {"title":"Parte Geral","questions":[
        {"enunciado":"O negócio jurídico celebrado por absolutamente incapaz é...","alternativas":["nulo","anulável","inexistente","eficaz mediante confirmação"],"resposta":"nulo","comentario":"Art. 166 I CC."},
        {"enunciado":"A personalidade civil da pessoa começa...","alternativas":["com a concepção","com o nascimento com vida","com o registro civil","com a maioridade"],"resposta":"com o nascimento com vida","comentario":"Art. 2º CC."},
        {"enunciado":"Os atos jurídicos lícitos que não contiverem indicação de termo...","alternativas":["são imediatamente exigíveis","são anuláveis","são nulos","dependem de homologação"],"resposta":"são imediatamente exigíveis","comentario":"Art. 132 CC."},
        {"enunciado":"São absolutamente incapazes de exercer pessoalmente os atos da vida civil:","alternativas":["os menores de 16 anos","os ébrios habituais","os viciados em tóxico","os pródigos"],"resposta":"os menores de 16 anos","comentario":"Art. 3º CC."},
        {"enunciado":"A anulabilidade do negócio jurídico por erro material prescreve em...","alternativas":["quatro anos","dois anos","três anos","dez anos"],"resposta":"quatro anos","comentario":"Art. 178 §9º CC."},
        {"enunciado":"O domicílio necessário do incapaz é...","alternativas":["o domicílio dos pais ou tutor","o lugar onde ele se encontrar","a sede do cartório","o domicílio escolhido por seu representante"],"resposta":"o domicílio dos pais ou tutor","comentario":"Art. 76 I CC."},
        {"enunciado":"O prazo decadencial para anular testamento por vício de vontade é de...","alternativas":["1 ano","2 anos","4 anos","5 anos"],"resposta":"2 anos","comentario":"Art. 178 §9º VII CC."},
        {"enunciado":"A regra de interpretação estrita aplica-se aos negócios jurídicos...","alternativas":["benéficos","oneroso bilaterais","comutativos","aleatórios"],"resposta":"benéficos","comentario":"Art. 114 CC."},
        {"enunciado":"Presume-se comorientes quando...","alternativas":["duas pessoas falecem na mesma ocasião sem prova de premoriente","não há sucessão entre elas","falecem em locais diferentes","o juiz assim declara"],"resposta":"duas pessoas falecem na mesma ocasião sem prova de premoriente","comentario":"Art. 8º CC."},
        {"enunciado":"Convalesce o negócio jurídico anulável...","alternativas":["pela confirmação pelas partes","pelo decurso do prazo","pela dação em pagamento","por sentença"],"resposta":"pela confirmação pelas partes","comentario":"Art. 172 CC."}
    ]},
    "coisas": {"title":"Direitos Reais (Coisas)","questions":[
        {"enunciado":"A acessão natural ocorre pelo(a)...","alternativas":["Aluvião","Construção ou plantação","Adjacência","Usucapião"],"resposta":"Aluvião","comentario":"Art. 1.250 CC."},
        {"enunciado":"É o prazo mínimo da usucapião extraordinária:","alternativas":["5 anos","10 anos","15 anos","20 anos"],"resposta":"15 anos","comentario":"Art. 1.238 caput."},
        {"enunciado":"Servidão é direito real...","alternativas":["sobre coisa própria","sobre coisa alheia","personalíssimo","intransmissível"],"resposta":"sobre coisa alheia","comentario":"Art. 1.378."},
        {"enunciado":"Possuidor de boa‑fé tem direito a...","alternativas":["retenção por benfeitorias úteis","indenização sem retenção","retirar todas as acessões","nada"],"resposta":"retenção por benfeitorias úteis","comentario":"Art. 1.219."},
        {"enunciado":"O direito de construir até certo limite vertical é chamado de...","alternativas":["Superfície","Enfiteuse","Condomínio edilício","Servidão de passagem"],"resposta":"Superfície","comentario":"Art. 1.369."},
        {"enunciado":"Penhor rural recai sobre...","alternativas":["direitos creditórios","veículos","bens móveis agrícolas","imóvel urbano"],"resposta":"bens móveis agrícolas","comentario":"Art. 1.438."},
        {"enunciado":"A perda da posse se verifica, entre outras hipóteses, pela...","alternativas":["constituição de usufruto","tradição voluntária","mera intenção de abandonar","ação reivindicatória"],"resposta":"tradição voluntária","comentario":"Art. 1.223 II."},
        {"enunciado":"Condomínio geral presume‑se...","alternativas":["dividido","indiviso","pro diviso","clausulado"],"resposta":"indiviso","comentario":"Art. 1.314."},
        {"enunciado":"A desapropriação indireta gera ao particular o direito a...","alternativas":["retrocesso","indenização","benfeitorias","lucros cessantes"],"resposta":"indenização","comentario":"Súm. 345 STF."},
        {"enunciado":"A enfiteuse foi extinta pelo CC/2002, porém respeitou...","alternativas":["novas inscrições","os contratos em vigor","qualquer transmissão futura","todas as utilizações"],"resposta":"os contratos em vigor","comentario":"Art. 2.038."}
    ]},
    "familia": {"title":"Família","questions":[
        {"enunciado":"É correto afirmar que a união estável gera...","alternativas":["direito sucessório idêntico ao casamento desde 2017 (STF)","comunhão universal obrigatória de bens","regime obrigatório de separação de bens","regime supletivo de comunhão parcial de bens"],"resposta":"regime supletivo de comunhão parcial de bens","comentario":"Art. 1.725 CC."},
        {"enunciado":"A separação de fato há mais de 2 anos é causa...","alternativas":["terminativa do casamento","excludente da obrigação alimentar","facultativa de divórcio","automática de dissolução"],"resposta":"facultativa de divórcio","comentario":"Art. 226 §6º CF."},
        {"enunciado":"São efeitos pessoais do casamento, exceto...","alternativas":["fidelidade","nome","coabitação","partilha de bens"],"resposta":"partilha de bens","comentario":"Partilha é efeito patrimonial."},
        {"enunciado":"Adotante deve ser, no mínimo, ___ anos mais velho que o adotando.","alternativas":["14","16","18","20"],"resposta":"16","comentario":"Art. 42 §3º ECA."},
        {"enunciado":"O poder familiar é suspenso, EXCETO...","alternativas":["em condenação superior a dois anos","abandono","maus‑tratos","desamparo"],"resposta":"desamparo","comentario":"Art. 1.637 CC."},
        {"enunciado":"Os alimentos gravídicos cessam...","alternativas":["com o nascimento com vida","com a concepção","após 6 meses","são definitivos"],"resposta":"com o nascimento com vida","comentario":"Lei 11.804/08 art. 6º."},
        {"enunciado":"O pacto antenupcial deve ser feito por...","alternativas":["instrumento particular","escritura pública","contrato verbal","procuração"],"resposta":"escritura pública","comentario":"Art. 1.653."},
        {"enunciado":"A guarda compartilhada é regra, salvo...","alternativas":["quando um dos pais viaja","se houver acordo ambos","se um dos genitores declarar que não deseja","se houver perigo ao menor"],"resposta":"se houver perigo ao menor","comentario":"Art. 1.584 §2º."},
        {"enunciado":"A tutela se dá a quem...","alternativas":["tiver mais de 18 anos","for parente consanguíneo","tiver idoneidade","todas anteriores"],"resposta":"todas anteriores","comentario":"Arts. 1.728-1.732."},
        {"enunciado":"Companheiros herdam do outro quando...","alternativas":["não existirem descendentes nem ascendentes","sempre","só se houver pacto","em separação total"],"resposta":"não existirem descendentes nem ascendentes","comentario":"Art. 1.790 revogado, aplica-se Art. 1.829."}
    ]},
    "sucessoes": {"title":"Sucessões","questions":[
        {"enunciado":"A legítima dos herdeiros necessários corresponde a...","alternativas":["1/3 da herança","metade da herança","2/3 da herança","quota fixada pelo testador"],"resposta":"metade da herança","comentario":"Art. 1.846 CC."},
        {"enunciado":"O herdeiro que renuncia...","alternativas":["pode representar seu ascendente","é excluído da sucessão","pode voltar atrás","herda a meação"],"resposta":"é excluído da sucessão","comentario":"Art. 1.811 CC."},
        {"enunciado":"O testamento público deve ser lavrado...","alternativas":["em cartório","em qualquer papel","em juízo","em nota particular"],"resposta":"em cartório","comentario":"Art. 1.864 CC."},
        {"enunciado":"O cônjuge sobrevivente é herdeiro necessário quando...","alternativas":["casado em regime de separação obrigatória","casado em comunhão parcial com bens particulares","sempre","casado em regime de participação final"],"resposta":"sempre","comentario":"Art. 1.845 CC."},
        {"enunciado":"Direito de representação ocorre na linha...","alternativas":["reta ascendente","reta descendente e colateral segundo grau","reta descendente","colateral até quarto grau"],"resposta":"reta descendente","comentario":"Art. 1.851 CC."},
        {"enunciado":"São excluídos da sucessão, por indignidade, EXCETO...","alternativas":["autor de homicídio doloso contra o autor da herança","acusação caluniosa","ato de cooperação em homicídio","injúria simples"],"resposta":"injúria simples","comentario":"Art. 1.814 CC."},
        {"enunciado":"O inventariante deve prestar as primeiras declarações em...","alternativas":["20 dias","30 dias","10 dias","15 dias"],"resposta":"20 dias","comentario":"Art. 619 CPC."},
        {"enunciado":"O legado de coisa certa existente em condomínio...","alternativas":["se reduz proporcionalmente","assegura preferência na divisão","é ineficaz","se converte em dinheiro"],"resposta":"assegura preferência na divisão","comentario":"Art. 1.911 CC."},
        {"enunciado":"Codicilo é ato revogável de última vontade que...","alternativas":["exige testemunhas","dispensa forma solene","só pode dispor de bens imóveis","não tem eficácia"],"resposta":"dispensa forma solene","comentario":"Art. 1.881 CC."},
        {"enunciado":"A colação é obrigatória para...","alternativas":["herdeiros necessários","testamenteiros","legatários","herdeiros facultativos"],"resposta":"herdeiros necessários","comentario":"Art. 2.002 CC."}
    ]},
    # === DIREITO OBRIGAÇÕES & CONTRATOS ===
    "obrigacoes": {"title":"Obrigações","questions":[
        {"enunciado":"A mora ex persona exige...","alternativas":["constituição em mora","prazo certo","intimação judicial","protesto cambial"],"resposta":"constituição em mora","comentario":"Art. 397 CC."},
        {"enunciado":"Na obrigação alternativa, a escolha pertence...","alternativas":["ao devedor, se o contrário não resultar da obrigação","sempre ao credor","ao juiz","solidariamente"],"resposta":"ao devedor, se o contrário não resultar da obrigação","comentario":"Art. 252 CC."},
        {"enunciado":"Ação de adimplemento da obrigação de pagar soma em dinheiro prescreve em...","alternativas":["3 anos","5 anos","10 anos","2 anos"],"resposta":"5 anos","comentario":"Art. 206 §5º I CC."},
        {"enunciado":"A cláusula penal pode ser...","alternativas":["cumulativa com perdas e danos","substituta das perdas e danos","sem limite","executada parcialmente"],"resposta":"substituta das perdas e danos","comentario":"Art. 416 CC."},
        {"enunciado":"Novação só se opera quando...","alternativas":["há animus novandi","há mera modificação acessória","o credor exigir","o devedor quiser"],"resposta":"há animus novandi","comentario":"Art. 360 CC."},
        {"enunciado":"Confusão extingue a obrigação porque...","alternativas":["credor e devedor se unem na mesma pessoa","há remissão","há novação","se torna impossível"],"resposta":"credor e devedor se unem na mesma pessoa","comentario":"Art. 381 CC."},
        {"enunciado":"Na obrigação indivisível não há...","alternativas":["cumprimento parcial liberatório","solidariedade","quota pro rata","benefício de divisão"],"resposta":"cumprimento parcial liberatório","comentario":"Art. 258 CC."},
        {"enunciado":"O pagamento com sub-rogação transfere...","alternativas":["os direitos do credor ao terceiro pagante","a dívida para outro devedor","a obrigação para o juiz","nada altera"],"resposta":"os direitos do credor ao terceiro pagante","comentario":"Art. 346 CC."},
        {"enunciado":"A imputação do pagamento, se o devedor não declara e o credor não aceita, far-se-á...","alternativas":["pela dívida mais onerosa","pela dívida mais antiga","pro rata","por decisão judicial"],"resposta":"pela dívida mais onerosa","comentario":"Art. 354 CC."},
        {"enunciado":"O devedor poderá consignar judicialmente a prestação quando...","alternativas":["o credor sem justa causa recusar receber","houver dúvida de quem seja o credor","o credor for incapaz","todas estão corretas"],"resposta":"todas estão corretas","comentario":"Art. 335 CC."}
    ]},
    "contratos": {"title":"Contratos","questions":[
        {"enunciado":"Contrato unilateral é aquele em que...","alternativas":["apenas uma parte assume obrigações","há troca de prestações equivalentes","gera direitos para ambas as partes","é intuito personae"],"resposta":"apenas uma parte assume obrigações","comentario":"Art. 541 CC."},
        {"enunciado":"No contrato de compra e venda, os riscos da coisa correm por conta do comprador a partir...","alternativas":["da tradição","do acordo de vontades","do pagamento","do registro"],"resposta":"da tradição","comentario":"Art. 492 CC."},
        {"enunciado":"A doação é considerada..., salvo quando...","alternativas":["contrato gratuito","contrato oneroso","contrato bilateral","contrato aleatório"],"resposta":"contrato gratuito","comentario":"Art. 538 CC."},
        {"enunciado":"No contrato estimatório, se a coisa perecer por fato do devedor...","alternativas":["ele deve pagar o preço estimado","extingue-se a obrigação","cabem perdas e danos ao credor","se rescinde de pleno direito"],"resposta":"ele deve pagar o preço estimado","comentario":"Art. 534 CC."},
        {"enunciado":"Locação de imóvel urbano residencial regula-se por...","alternativas":["Lei 8.245/91","Código Civil","CDC","CLT"],"resposta":"Lei 8.245/91","comentario":"Lei de Locações."},
        {"enunciado":"No contrato de mandato, o mandatário...","alternativas":["pode substabelecer salvo proibição","não pode cobrar despesas","não responde por dolo","é remunerado sempre"],"resposta":"pode substabelecer salvo proibição","comentario":"Art. 653 CC."},
        {"enunciado":"Contrato aleatório é aquele em que...","alternativas":["a prestação depende de evento incerto","não há risco","ambas as prestações são certas","é intuito personae"],"resposta":"a prestação depende de evento incerto","comentario":"Art. 458 CC."},
        {"enunciado":"No contrato de comodato, o comodatário responde...","alternativas":["pelo uso indevido","por caso fortuito","por força maior","apenas por dolo"],"resposta":"pelo uso indevido","comentario":"Art. 581 CC."},
        {"enunciado":"A compra e venda entre ascendente e descendente depende...","alternativas":["do consentimento dos demais descendentes e cônjuge","de escritura pública","de alvará judicial","de pacto antenupcial"],"resposta":"do consentimento dos demais descendentes e cônjuge","comentario":"Art. 496 CC."},
        {"enunciado":"No contrato de seguro, o prêmio é","alternativas":["o valor pago pelo segurado","a indenização","o risco","a franquia"],"resposta":"o valor pago pelo segurado","comentario":"Conceito básico de seguro."}
    ]},
    # === REGISTROS PÚBLICOS (60 QUESTÕES) ===
    "rp_titulo_i": {"title":"Registros Públicos – Título I (Disposições Gerais)","questions":[
        {"enunciado":"A Lei 6.015/73 visa assegurar autenticidade, segurança e ____ dos atos jurídicos.","alternativas":["legitimidade","publicidade","eficácia","validade"],"resposta":"eficácia","comentario":"Art. 1º caput."},
        {"enunciado":"Qual destes NÃO é um dos quatro registros públicos previstos no §1º do art. 1º?","alternativas":["Registro civil de pessoas naturais","Registro de títulos e documentos","Registro de protesto de títulos","Registro de imóveis"],"resposta":"Registro de protesto de títulos","comentario":"Art. 1º §1º."},
        {"enunciado":"Os registros serão escriturados, publicizados e conservados em meio _____, segundo §3º do art. 1º.","alternativas":["escrito","eletrônico","mecânico","analógico"],"resposta":"eletrônico","comentario":"Art. 1º §3º."},
        {"enunciado":"É vedado às serventias recusar a recepção de documentos eletrônicos que sigam padrões CNJ.","alternativas":["Verdadeiro","Falso"],"resposta":"Verdadeiro","comentario":"Art. 1º §4º."},
        {"enunciado":"Os livros podem ter largura máxima de ____ metros (art. 3º §1º).","alternativas":["0,25","0,30","0,35","0,40"],"resposta":"0,40","comentario":"Art. 3º §1º."},
        {"enunciado":"No registro de imóveis, esgotado um livro, o número é mantido acrescido de letras sucessivas.","alternativas":["Verdadeiro","Falso"],"resposta":"Verdadeiro","comentario":"Art. 6º."},
        {"enunciado":"O registro civil de pessoas naturais funciona todos os dias, sem exceção.","alternativas":["Verdadeiro","Falso"],"resposta":"Verdadeiro","comentario":"Art. 8º parágrafo único."},
        {"enunciado":"É nulo o registro lavrado fora das horas regulamentares, implicando responsabilidade do oficial.","alternativas":["Verdadeiro","Falso"],"resposta":"Verdadeiro","comentario":"Art. 9º caput."},
        {"enunciado":"A certidão será lavrada em até ____ dias, salvo disposição especial (art. 19).","alternativas":["2","3","5","7"],"resposta":"5","comentario":"Art. 19 caput."},
        {"enunciado":"Os emolumentos pelo ato do registro são pagos pelo interessado (art. 14).","alternativas":["Verdadeiro","Falso"],"resposta":"Verdadeiro","comentario":"Art. 14 caput."}
    ]},
    "rp_titulo_ii": {"title":"Registros Públicos – Título II (Pessoas Naturais)","questions":[
        {"enunciado":"Quais fatos NÃO são registrados no RCPN, segundo art. 29?","alternativas":["Nascimentos","Interdições","Hipoteca","Óbitos"],"resposta":"Hipoteca","comentario":"Art. 29."},
        {"enunciado":"O prazo ordinário para registro de nascimento é de ___ dias (art. 50).","alternativas":["5","10","15","30"],"resposta":"15","comentario":"Art. 50."},
        {"enunciado":"No registro tardio, o assento é feito no lugar de residência do interessado (art. 46).","alternativas":["Verdadeiro","Falso"],"resposta":"Verdadeiro","comentario":"Art. 46."},
        {"enunciado":"Os mapas trimestrais de nascimentos são remetidos ao IBGE nos primeiros ___ dias do trimestre seguinte (art. 49).","alternativas":["5","8","10","15"],"resposta":"8","comentario":"Art. 49."},
        {"enunciado":"A certidão de nascimento e a de óbito são gratuitas (art. 30).","alternativas":["Verdadeiro","Falso"],"resposta":"Verdadeiro","comentario":"Art. 30."},
        {"enunciado":"Qual item NÃO integra obrigatoriamente o assento de nascimento (art. 54)?","alternativas":["Hora do nascimento","Naturalidade do registrando","Profissão dos avós","Número da Declaração de Nascido Vivo"],"resposta":"Profissão dos avós","comentario":"Art. 54."},
        {"enunciado":"A opção pela naturalidade da mãe foi introduzida pelo §4º do art. 54 em que ano?","alternativas":["2017","2020","2022","2009"],"resposta":"2017","comentario":"Lei 13.484/2017."},
        {"enunciado":"A pessoa maior pode alterar prenome imotivadamente uma única vez no cartório (art. 56).","alternativas":["Verdadeiro","Falso"],"resposta":"Verdadeiro","comentario":"Art. 56 caput."},
        {"enunciado":"As certidões devem mencionar eventuais averbações correlatas, salvo exceções (art. 21).","alternativas":["Verdadeiro","Falso"],"resposta":"Verdadeiro","comentario":"Art. 21."},
        {"enunciado":"A declaração de nascimento deve ser feita preferencialmente por pai ou mãe; na falta, o prazo prorroga-se por ___ dias (art. 52).","alternativas":["30","45","60","90"],"resposta":"45","comentario":"Art. 52 §2º."}
    ]},
    "rp_titulo_iii": {"title":"Registros Públicos – Título III (Pessoas Jurídicas)","questions":[
        {"enunciado":"Compete ao RCPJ registrar sociedades simples e associações civis.","alternativas":["Verdadeiro","Falso"],"resposta":"Verdadeiro","comentario":"Art. 114."},
        {"enunciado":"O requerimento de inscrição deve ser assinado por ___ dos fundadores (art. 115).","alternativas":["1/3","maioria","todos","qualquer um"],"resposta":"todos","comentario":"Art. 115."},
        {"enunciado":"A alteração de estatuto social exige publicação e arquivamento no prazo de ___ dias (art. 118).","alternativas":["15","30","60","90"],"resposta":"30","comentario":"Art. 118."},
        {"enunciado":"As sociedades terão número de ordem cronológica sem recomeço em cada livro.","alternativas":["Verdadeiro","Falso"],"resposta":"Verdadeiro","comentario":"Art. 120."},
        {"enunciado":"O cancelamento da inscrição da PJ deve ser averbado mediante requerimento ou sentença.","alternativas":["Verdadeiro","Falso"],"resposta":"Verdadeiro","comentario":"Art. 121."},
        {"enunciado":"Documentos de sociedades estrangeiras devem vir autenticados por consulado (art. 122).","alternativas":["Verdadeiro","Falso"],"resposta":"Verdadeiro","comentario":"Art. 122."},
        {"enunciado":"Cabe recurso da decisão do oficial ao Juiz no prazo de ___ dias (art. 127).","alternativas":["5","8","10","15"],"resposta":"5","comentario":"Art. 127."},
        {"enunciado":"A verbação do encerramento de liquidação deve conter quórum de aprovação do balanço.","alternativas":["Verdadeiro","Falso"],"resposta":"Verdadeiro","comentario":"Art. 124."},
        {"enunciado":"O índice alfabético dos registros de pessoas jurídicas é obrigatório (art. 126).","alternativas":["Verdadeiro","Falso"],"resposta":"Verdadeiro","comentario":"Art. 126."},
        {"enunciado":"A publicação dos atos é dispensada para associações sem fins econômicos.","alternativas":["Verdadeiro","Falso"],"resposta":"Falso","comentario":"Art. 118."}
    ]},
    "rp_titulo_iv": {"title":"Registros Públicos – Título IV (Títulos e Documentos)","questions":[
        {"enunciado":"O RTD tem efeito de dar publicidade e garantir a ____ dos documentos.","alternativas":["autoria","autenticidade","eficácia","legalidade"],"resposta":"autenticidade","comentario":"Art. 127 caput."},
        {"enunciado":"Contratos de locação devem ser registrados no RTD para valer contra terceiros.","alternativas":["Verdadeiro","Falso"],"resposta":"Verdadeiro","comentario":"Art. 129 VII."},
        {"enunciado":"O protesto de documento particular pode ser registrado no RTD.","alternativas":["Verdadeiro","Falso"],```}]}]}
   }
