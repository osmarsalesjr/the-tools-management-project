
from utilitarios.constantes import (
    STATUS_APROVADO,
    STATUS_REPROVADO,
    MOTIVO_REPROVADO_POR_COMPRIMENTO,
    MOTIVO_REPROVADO_POR_COR,
    MOTIVO_REPROVADO_POR_PESO
)

def main() -> None:
    pass


def validar_peca(peca: dict, cor: dict) -> dict:

    if peca is None:
        return peca

    peso = peca["peso"]
    cor = cor["nome"]
    comprimento = peca["comprimento"]
    motivos_reprovacao = []

    if peso < 95 or peso > 105:
        motivos_reprovacao.append(MOTIVO_REPROVADO_POR_PESO)

    if cor.casefold() != "azul".casefold() and cor.casefold() != "verde".casefold():
        motivos_reprovacao.append(MOTIVO_REPROVADO_POR_COR)

    if comprimento < 10 or comprimento > 20:
        motivos_reprovacao.append(MOTIVO_REPROVADO_POR_COMPRIMENTO)

    if len(motivos_reprovacao) == 0:
        peca["status"] = STATUS_APROVADO
    else:
        peca["status"] = STATUS_REPROVADO
        peca["motivos_reprovacao"] = motivos_reprovacao

    return peca


if __name__ == "__main__":
    main()
