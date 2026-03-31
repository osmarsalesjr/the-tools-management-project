
from flask import (
    Flask,
    render_template,
    request
)
from datetime import datetime, timezone
from math import ceil


from services.bd_service import (
    conectar_servico_banco_de_dados,
    desconectar_servico_banco_de_dados,
    buscar_todas_as_pecas,
    buscar_todas_as_caixas,
    buscar_caixas_com_pecas,
    buscar_caixas_com_pecas_por_status,
    buscar_ou_criar_caixa_para_nova_peca,
    buscar_peca_por_id,
    excluir_peca,
    buscar_cor_por_id,
    buscar_cores,
    guardar_peca,
    buscar_pecas_por_status,
    alterar_cadastro_peca,

)

from utilitarios.constantes import (
    LIMITE_ITENS_POR_PAGINA,
    STATUS_APROVADO,
    STATUS_REPROVADO
)

from utilitarios.pecas_utils import criar_peca
from utilitarios.validacoes import validar_peca

app = Flask(__name__)


### Abre uma nova conexão com banco de dados para cada requisição
@app.before_request
def inicializar_conexao_banco_de_dados():
    conectar_servico_banco_de_dados()


### Fecha conexão com banco de dados
@app.teardown_appcontext
def fechar_conexao_banco_de_dados(error=None):
    desconectar_servico_banco_de_dados()


### Configura data atual para pagina base.html
@app.context_processor
def inject_now():
    return {'now': datetime.now(timezone.utc)}


### Configura rotas padrões para pagina inicial da aplicação
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/cadastrar-peca')
def cadastrar_peca():

    cores = buscar_cores()

    return render_template(
        'cadastrar_peca.html',
        cores=cores
    )


@app.post('/pecas')
def adicionar_peca():

    dados = request.get_json()

    peso = dados.get('peso')
    comprimento = dados.get('comprimento')
    cor = buscar_cor_por_id(dados.get('cor_id'))

    if cor is None:
        return 'Cor selecionada não encontrada.', 404

    peca = criar_peca(peso, cor["id"], comprimento)
    peca = validar_peca(peca, cor)

    if peca["status"].casefold() == STATUS_APROVADO.casefold():
        caixa = buscar_ou_criar_caixa_para_nova_peca()
        peca["caixa_id"] = caixa.get("id")

    peca = guardar_peca(peca)
    return '', 201, {'Location': f'/peca/{peca["id"]}'}


@app.get('/pecas/<int:peca_id>')
def detalhar_peca(peca_id: int):

    peca = buscar_peca_por_id(peca_id)

    if peca is None:
        return 'Peça não encontrada.', 404
    
    return render_template(
        'detalhar_peca.html',
        peca=peca
    )


@app.route('/alterar-peca/<int:peca_id>')
def alterar_peca(peca_id: int):

    peca = buscar_peca_por_id(peca_id)

    if peca is None:
        return 'Peça não encontrada.', 404

    cores = buscar_cores()

    return render_template(
        'alterar_peca.html',
        cores=cores,
        peca=peca
    )


@app.put('/pecas/<int:peca_id>')
def atualizar_peca(peca_id: int):

    peca = buscar_peca_por_id(peca_id)

    if peca is None:
        return 'Peça não encontrada.', 404

    dados = request.get_json()

    peca["peso"] = dados.get('peso')
    peca["comprimento"] = dados.get('comprimento')
    cor = buscar_cor_por_id(dados.get('cor_id'))

    if cor is None:
        return 'Cor selecionada não encontrada.', 404

    peca["cor_id"] = cor["id"]
    peca = validar_peca(peca, cor)

    if peca["status"].casefold() == STATUS_REPROVADO.casefold():
        peca["caixa_id"] = None
    
    if (
        peca["status"].casefold() == STATUS_APROVADO.casefold()
        and peca["caixa_id"] is None
    ):
        caixa = buscar_ou_criar_caixa_para_nova_peca()
        peca["caixa_id"] = caixa.get("id")

    peca = alterar_cadastro_peca(peca)
    return '', 204


@app.delete('/pecas/<int:peca_id>')
def deletar_peca(peca_id: int):

    peca = buscar_peca_por_id(peca_id)

    if peca is None:
        return 'Peça não encontrada.', 404
    
    excluir_peca(peca)
    return '', 204


@app.get('/remover-peca')
def listar_pecas_para_remocao():
    pagina = request.args.get('pagina', 1, type=int)

    pecas = buscar_todas_as_pecas()
    total_pecas = len(pecas)

    total_paginas = max(1, ceil(total_pecas / LIMITE_ITENS_POR_PAGINA))
    pagina = max(1, min(pagina, total_paginas))

    offset = (pagina - 1) * LIMITE_ITENS_POR_PAGINA
    pecas_pagina = pecas[offset : offset + LIMITE_ITENS_POR_PAGINA]

    return render_template(
        'listar_pecas_para_remocao.html',
        pecas=pecas,
        pecas_pagina=pecas_pagina,
        pagina_atual=pagina,
        total_paginas=total_paginas,
        offset=offset,
    )


@app.get('/pecas')
def listar_pecas():

    pagina = request.args.get('pagina', 1, type=int)

    pecas = buscar_todas_as_pecas()
    total_pecas = len(pecas)

    total_paginas = max(1, ceil(total_pecas / LIMITE_ITENS_POR_PAGINA))
    pagina = max(1, min(pagina, total_paginas))

    offset = (pagina - 1) * LIMITE_ITENS_POR_PAGINA
    pecas_pagina = pecas[offset : offset + LIMITE_ITENS_POR_PAGINA]

    return render_template(
        'listar_pecas.html',
        pecas=pecas,
        pecas_pagina=pecas_pagina,
        pagina_atual=pagina,
        total_paginas=total_paginas,
        offset=offset,
    )


@app.get('/caixas-fechadas')
def listar_caixas_fechadas():

    pagina = request.args.get('pagina', 1, type=int)

    caixas = buscar_caixas_com_pecas_por_status(int(True))
    total_caixas = len(caixas)

    total_paginas = max(1, ceil(total_caixas / LIMITE_ITENS_POR_PAGINA))
    pagina = max(1, min(pagina, total_paginas))

    offset = (pagina - 1) * LIMITE_ITENS_POR_PAGINA
    caixas_pagina = caixas[offset : offset + LIMITE_ITENS_POR_PAGINA]

    return render_template(
        'listar_caixas.html',
        caixas=caixas,
        caixas_pagina=caixas_pagina,
        pagina_atual=pagina,
        total_paginas=total_paginas,
    )


@app.get('/caixas')
def listar_todas_caixas():

    pagina = request.args.get('pagina', 1, type=int)

    caixas = buscar_caixas_com_pecas()
    total_caixas = len(caixas)

    total_paginas = max(1, ceil(total_caixas / LIMITE_ITENS_POR_PAGINA))
    pagina = max(1, min(pagina, total_paginas))

    offset = (pagina - 1) * LIMITE_ITENS_POR_PAGINA
    caixas_pagina = caixas[offset : offset + LIMITE_ITENS_POR_PAGINA]

    return render_template(
        'listar_caixas.html',
        caixas=caixas,
        caixas_pagina=caixas_pagina,
        pagina_atual=pagina,
        total_paginas=total_paginas,
    )


@app.route('/gerar-relatorio')
def gerar_relatorio():

    pecas_aprovadas = buscar_pecas_por_status(STATUS_APROVADO)
    pecas_reprovadas = buscar_pecas_por_status(STATUS_REPROVADO)

    caixas = buscar_todas_as_caixas()
    quantidade_caixas_fechadas = 0
    quantidade_caixas_abertas = 0

    for caixa in caixas:
        
        if caixa["esta_fechada"] is True:
            quantidade_caixas_fechadas += 1
            continue
        quantidade_caixas_abertas += 1

    return render_template(
        'relatorio_geral.html',
        pecas_aprovadas=pecas_aprovadas,
        pecas_reprovadas=pecas_reprovadas,
        quantidade_caixas_abertas=quantidade_caixas_abertas,
        quantidade_caixas_fechadas=quantidade_caixas_fechadas,
        total_caixas_utilizadas = quantidade_caixas_fechadas + quantidade_caixas_abertas
    )


if __name__ == "__main__":
    app.run(debug=True)