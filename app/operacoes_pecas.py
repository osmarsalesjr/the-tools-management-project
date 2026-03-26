from validacoes_pecas import processar_validacao_peca

TEXTO_ENTRADA_PESO_PECA = "\nDigite o peso em gramas (g) da peça: "
TEXTO_ENTRADA_COR_PECA = "\nEscolha o número da cor da peça: "
TEXTO_ENTRADA_COMPRIMENTO_PECA = "\nDigite o comprimento em centímetro (cm) da peça: "

TEXTO_SAIDA_ALERTA_COR_PECA_NAO_ENCONTRADA = (
    "A número da cor escolhida não foi encontrada. Tente novamente."
)

TEXTO_SAIDA_ERRO_VALOR_DEVE_SER_NUMERICO = "Erro! O valor deve ser numérico."
TEXTO_SAIDA_ERRO_GENERICO = "Erro inesperado! Tente novamente."

ids_pecas_disponiveis = []


def main() -> None:
    pass


def gerar_id_peca(pecas: list[dict]) -> int:
    global ids_pecas_disponiveis

    numero_pecas = len(pecas)

    if numero_pecas <= 0:
        return 1

    numero_ids_pecas_disponiveis = len(ids_pecas_disponiveis)

    if numero_ids_pecas_disponiveis != 0:
        ids_pecas_disponiveis.sort(reverse=True)
        return ids_pecas_disponiveis.pop()

    return buscar_maior_id_peca(pecas) + 1


def receber_numero_inteiro(texto_entrada: str) -> int:
    while True:
        try:
            id = int(input(texto_entrada))
            return id
        except ValueError:
            print(TEXTO_SAIDA_ERRO_VALOR_DEVE_SER_NUMERICO)
        except Exception:
            print(TEXTO_SAIDA_ERRO_GENERICO)


def criar_peca(pecas: list[dict]) -> dict:
    id = gerar_id_peca(pecas)
    peso = receber_numero_inteiro(TEXTO_ENTRADA_PESO_PECA)
    cor = receber_cor_peca()
    comprimento = receber_numero_inteiro(TEXTO_ENTRADA_COMPRIMENTO_PECA)

    peca = {
        "id": id,
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento,
        "status": "",
        "motivos_reprovacao": [],
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


def buscar_cor_por_id(id_cor: int, cores: list[dict]) -> str | None:

    cores_map = {cor["id"]: cor["nome"] for cor in cores}
    return cores_map.get(id_cor)


def buscar_peca_por_id(id_peca: int, pecas: list[dict]) -> dict | None:

    pecas_map = {peca["id"]: peca for peca in pecas}
    return pecas_map.get(id_peca)


def buscar_maior_id_peca(pecas: list[dict]) -> int:

    ultimo_id_peca_maior = max([peca["id"] for peca in pecas])
    return ultimo_id_peca_maior


def atualizar_ids_pecas_disponiveis(id_peca_disponivel: int) -> None:
    global ids_pecas_disponiveis

    ids_pecas_disponiveis.append(id_peca_disponivel)
    print(f"O ID {id_peca_disponivel} foi liberado para cadastro de nova peça.")


if __name__ == "__main__":
    main()
