STATUS_APROVADO = "APROVADO"
STATUS_REPROVADO = "REPROVADO"

MOTIVO_REPROVADO_POR_PESO = "PESO DA PEÇA NÃO SEGUE OS PADRÕES DE QUALIDADE."
MOTIVO_REPROVADO_POR_COR = "COR DA PEÇA NÃO SEGUE OS PADRÕES DE QUALIDADE."
MOTIVO_REPROVADO_POR_COMPRIMENTO = (
    "COMPRIMENTO DA PEÇA NÃO SEGUE OS PADRÕES DE QUALIDADE."
)


def main() -> None:
    pass


def processar_validacao_peca(peca: dict) -> dict:

    if peca is None:
        return peca

    peso = peca["peso"]
    cor = str(peca["cor"])
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
