from validacoes_pecas import processar_validacao_peca

TEXTO_ENTRADA_PESO_PECA = "\nDigite o peso em gramas (g) da peça: "
TEXTO_ENTRADA_COR_PECA = "\nEscolha o número da cor da peça: "
TEXTO_ENTRADA_COMPRIMENTO_PECA = "\nDigite o comprimento em centímetro (cm) da peça: "

TEXTO_SAIDA_ALERTA_COR_PECA_NAO_ENCONTRADA = (
    "A número da cor escolhida não foi encontrada. Tente novamente."
)

TEXTO_SAIDA_ERRO_VALOR_DEVE_SER_NUMERICO = "Erro! O valor deve ser numérico."
TEXTO_SAIDA_ERRO_GENERICO = "Erro inesperado! Tente novamente."

pecas_ids_disponiveis = []


def main() -> None:
    pass


def receber_numero_inteiro(texto_entrada: str) -> int:
    while True:
        try:
            id = int(input(texto_entrada))
            return id
        except ValueError:
            print(TEXTO_SAIDA_ERRO_VALOR_DEVE_SER_NUMERICO)
        except Exception:
            print(TEXTO_SAIDA_ERRO_GENERICO)


def criar_peca_validada(peso: int, cor: str, comprimento: int) -> dict:
    peca = {
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento,
        "status": "",
        "motivos_reprovacao": [],
        "caixa_id": None
    }

    return processar_validacao_peca(peca) 


def receber_cor_peca() -> str:

    cores = [
        {"id": 1, "nome": "Preto"},
        {"id": 2, "nome": "Branco"},
        {"id": 3, "nome": "Vermelho"},
        {"id": 4, "nome": "Azul"},
        {"id": 5, "nome": "Amarelo"},
        {"id": 6, "nome": "Verde"},
        {"id": 7, "nome": "Marrom"},
        {"id": 8, "nome": "Laranja"},
        {"id": 9, "nome": "Rosa"},
        {"id": 10, "nome": "Cinza"},
        {"id": 11, "nome": "Roxo"},
        {"id": 12, "nome": "Dourado"},
        {"id": 13, "nome": "Prata"},
        {"id": 14, "nome": "Bege"},
    ]

    while True:
        try:
            imprimir_cores(cores)
            cor_id = int(input(TEXTO_ENTRADA_COR_PECA))
            cor = buscar_cor_por_id(cor_id, cores)

            if cor is None:
                print(TEXTO_SAIDA_ALERTA_COR_PECA_NAO_ENCONTRADA)
            else:
                return cor.upper()
        except ValueError:
            print(TEXTO_SAIDA_ERRO_VALOR_DEVE_SER_NUMERICO)
        except Exception:
            print(TEXTO_SAIDA_ERRO_GENERICO)


def imprimir_cores(cores: list[dict]) -> None:

    print((">" * 10) + " Cores " + ("<" * 10))
    for cor in cores:
        print(f"{cor["id"]}. {cor["nome"]}")


def buscar_cor_por_id(cor_id: int, cores: list[dict]) -> str | None:

    cores_map = {cor["id"]: cor["nome"] for cor in cores}
    return cores_map.get(cor_id)


if __name__ == "__main__":
    main()
