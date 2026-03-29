
from operacoes.operacoes_banco_de_dados import (
    conectar_banco_de_dados,
    desconectar_banco_de_dados,
    recuperar_todas_as_pecas,
    recuperar_caixas_com_pecas,
    recuperar_peca_por_id,
    remover_peca,
)


def main() -> None:
    pass


def conectar_servico_banco_de_dados() -> None:
    conectar_banco_de_dados()


def desconectar_servico_banco_de_dados() -> None:
    desconectar_banco_de_dados()


def buscar_todas_as_pecas() -> list[dict]:
    return recuperar_todas_as_pecas()


def buscar_caixas_com_pecas() -> list[dict]:
    return recuperar_caixas_com_pecas()


def buscar_caixas_fechadas_com_pecas() -> list[dict]:

    caixas = recuperar_caixas_com_pecas()
    caixas_fechadas = [caixa for caixa in caixas if caixa["esta_fechada"]]
    
    return caixas_fechadas


def buscar_peca_por_id(id: int) -> dict:
    return recuperar_peca_por_id(id)


def excluir_peca(peca: dict) -> None:
    remover_peca(peca)

if __name__ == "__main__":
    main()
