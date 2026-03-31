
def main() -> None:
    pass


def criar_peca(peso: int, cor_id: int, comprimento: int) -> dict:
    peca = {
        "peso": peso,
        "cor_id": cor_id,
        "comprimento": comprimento,
        "status": "",
        "motivos_reprovacao": [],
        "caixa_id": None
    }

    return peca


if __name__ == "__main__":
    main()
