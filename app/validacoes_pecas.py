STATUS_APROVADO = "APROVADO"
STATUS_REPROVADO = "REPROVADO"

MOTIVO_REPROVADO_POR_PESO = "PESO DA PEÇA NÃO SEGUE OS PADRÕES DE QUALIDADE."
MOTIVO_REPROVADO_POR_COR = "COR DA PEÇA NÃO SEGUE OS PADRÕES DE QUALIDADE."
MOTIVO_REPROVADO_POR_COMPRIMENTO = "COMPRIMENTO DA PEÇA NÃO SEGUE OS PADRÕES DE QUALIDADE."


def main() -> None:
    pass


def verificar_peca_existe_por_id(pecas: list[dict], id: int) -> bool:

    if pecas is None or len(pecas) == 0:
        return False

    pecas_ids = [peca["id"] for peca in pecas if peca["id"] == id]

    if len(pecas_ids) != 0:
        return True
    
    return False


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
