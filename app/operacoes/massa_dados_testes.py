
from utilitarios.validacoes import (
    STATUS_APROVADO,
    STATUS_REPROVADO,
    MOTIVO_REPROVADO_POR_PESO,
    MOTIVO_REPROVADO_POR_COR,
    MOTIVO_REPROVADO_POR_COMPRIMENTO,
)

lista_de_pecas = [
    # ======================
    # APROVADAS
    # ======================
    {"peso": 100, "cor_id": 4, "comprimento": 15, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 100, "cor_id": 6, "comprimento": 15, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 98, "cor_id": 4, "comprimento": 12, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 102, "cor_id": 6, "comprimento": 18, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 95, "cor_id": 4, "comprimento": 10, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 105, "cor_id": 6, "comprimento": 20, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 99, "cor_id": 4, "comprimento": 14, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 101, "cor_id": 6, "comprimento": 16, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 100, "cor_id": 4, "comprimento": 17, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 97, "cor_id": 6, "comprimento": 13, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 103, "cor_id": 4, "comprimento": 19, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 96, "cor_id": 6, "comprimento": 11, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 100, "cor_id": 4, "comprimento": 15, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 104, "cor_id": 6, "comprimento": 20, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 95, "cor_id": 4, "comprimento": 12, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 105, "cor_id": 6, "comprimento": 18, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 98, "cor_id": 4, "comprimento": 16, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 101, "cor_id": 6, "comprimento": 14, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 100, "cor_id": 4, "comprimento": 15, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 99, "cor_id": 6, "comprimento": 17, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 102, "cor_id": 4, "comprimento": 18, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 97, "cor_id": 6, "comprimento": 13, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 100, "cor_id": 4, "comprimento": 15, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 103, "cor_id": 6, "comprimento": 19, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 96, "cor_id": 4, "comprimento": 11, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 104, "cor_id": 6, "comprimento": 20, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 98, "cor_id": 4, "comprimento": 14, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 101, "cor_id": 6, "comprimento": 16, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 100, "cor_id": 4, "comprimento": 15, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 97, "cor_id": 6, "comprimento": 13, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 102, "cor_id": 4, "comprimento": 18, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 99, "cor_id": 6, "comprimento": 17, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 100, "cor_id": 4, "comprimento": 15, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 103, "cor_id": 6, "comprimento": 19, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 96, "cor_id": 4, "comprimento": 11, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 104, "cor_id": 6, "comprimento": 20, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 98, "cor_id": 4, "comprimento": 14, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 101, "cor_id": 6, "comprimento": 16, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 100, "cor_id": 4, "comprimento": 15, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 97, "cor_id": 6, "comprimento": 13, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 102, "cor_id": 4, "comprimento": 18, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 99, "cor_id": 6, "comprimento": 17, "status": STATUS_APROVADO, "motivos_reprovacao": []},
    {"peso": 100, "cor_id": 4, "comprimento": 15, "status": STATUS_APROVADO, "motivos_reprovacao": []},

    # ======================
    # REPROVADAS (exemplos)
    # ======================
    {"peso": 80, "cor_id": 4, "comprimento": 15, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_PESO]},
    {"peso": 80, "cor_id": 6, "comprimento": 15, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_PESO]},
    {"peso": 110, "cor_id": 4, "comprimento": 15, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_PESO]},
    {"peso": 110, "cor_id": 6, "comprimento": 15, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_PESO]},

    {"peso": 100, "cor_id": 3, "comprimento": 15, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_COR]},
    {"peso": 100, "cor_id": 1, "comprimento": 15, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_COR]},
    {"peso": 100, "cor_id": 2, "comprimento": 15, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_COR]},
    {"peso": 100, "cor_id": 5, "comprimento": 15, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_COR]},
    {"peso": 100, "cor_id": 11, "comprimento": 15, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_COR]},

    {"peso": 100, "cor_id": 4, "comprimento": 5, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_COMPRIMENTO]},
    {"peso": 100, "cor_id": 6, "comprimento": 5, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_COMPRIMENTO]},

    {"peso": 50, "cor_id": 11, "comprimento": 30, "status": STATUS_REPROVADO, "motivos_reprovacao": [MOTIVO_REPROVADO_POR_PESO, MOTIVO_REPROVADO_POR_COR, MOTIVO_REPROVADO_POR_COMPRIMENTO]},
]

def main() -> None:
    pass


def pegar_massa_lista_pecas() -> list[dict]:
    global lista_de_pecas

    return lista_de_pecas


if __name__ == "__main__":
    main()
