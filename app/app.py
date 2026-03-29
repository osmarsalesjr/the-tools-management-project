
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
    buscar_caixas_com_pecas,
    buscar_caixas_fechadas_com_pecas,
    buscar_peca_por_id,
    excluir_peca,

)

app = Flask(__name__)
LIMITE_ITENS_POR_PAGINA = 20


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


@app.route('/cadastrar_peca')
def cadastrar_peca():
    pass


@app.delete('/pecas/<int:peca_id>')
def deletar_peca(peca_id: int):

    peca = buscar_peca_por_id(peca_id)

    if peca is None:
        return '', 404
    
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

    caixas = buscar_caixas_fechadas_com_pecas()
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
    pass


if __name__ == "__main__":
    app.run(debug=True)