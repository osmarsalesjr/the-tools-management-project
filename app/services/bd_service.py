
from dao.operacoes_banco_de_dados import (
    conectar_banco_de_dados,
    desconectar_banco_de_dados,
    recuperar_todas_as_pecas,
    recuperar_caixas,
    recuperar_caixas_com_pecas,
    recuperar_ou_criar_caixa_para_nova_peca,
    recuperar_peca_por_id,
    remover_peca,
    recuperar_todas_as_cores,
    recuperar_cor_por_id,
    salvar_peca,
    recuperar_caixas_por_status,
    recuperar_pecas_por_status,
    atualizar_peca,
)


def main() -> None:
    pass


def conectar_servico_banco_de_dados() -> None:
    conectar_banco_de_dados()


def desconectar_servico_banco_de_dados() -> None:
    desconectar_banco_de_dados()


def guardar_peca(peca: dict) -> dict:
    return salvar_peca(peca)


def alterar_cadastro_peca(peca: dict) -> None:
    atualizar_peca(peca)


def buscar_todas_as_pecas() -> list[dict]:
    return recuperar_todas_as_pecas()


def buscar_pecas_por_status(status: str) -> list[dict]:
    return recuperar_pecas_por_status(status)


def buscar_caixas_com_pecas() -> list[dict]:
    return recuperar_caixas_com_pecas()


def buscar_todas_as_caixas() -> list[dict]:
    return recuperar_caixas()


def buscar_caixas_com_pecas_por_status(esta_fechada: int) -> list[dict]:

    return recuperar_caixas_por_status(esta_fechada)


def buscar_ou_criar_caixa_para_nova_peca() -> dict:
    return recuperar_ou_criar_caixa_para_nova_peca()


def buscar_peca_por_id(id: int) -> dict:
    return recuperar_peca_por_id(id)


def excluir_peca(peca: dict) -> None:
    remover_peca(peca)


def buscar_cor_por_id(id: int) -> dict:
    return recuperar_cor_por_id(id)


def buscar_cores() -> list[dict]:
    return recuperar_todas_as_cores()


if __name__ == "__main__":
    main()
