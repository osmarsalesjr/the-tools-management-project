from validacoes_pecas import verificar_peca_existe_por_id, processar_validacao_peca

TEXTO_ENTRADA_ID_PECA = "\nDigite a identificação numérica da peça: "
TEXTO_SAIDA_ALERTA_ID_PECA_JA_EXISTE = "A identificação da peça digitada já está cadastrada."

TEXTO_ENTRADA_PESO_PECA = "\nDigite o peso em gramas (g) da peça: "
TEXTO_ENTRADA_COR_PECA = "\nEscolha o número da cor da peça: "
TEXTO_ENTRADA_COMPRIMENTO_PECA = "\nDigite o comprimento em centímetro (cm) da peça: "

TEXTO_SAIDA_ALERTA_COR_PECA_NAO_ENCONTRADA = (
    "A número da cor escolhida não foi encontrada. Tente novamente."
)

TEXTO_SAIDA_ERRO_VALOR_DEVE_SER_NUMERICO = "Erro! O valor deve ser numérico."
TEXTO_SAIDA_ERRO_GENERICO = "Erro inesperado! Tente novamente."

ids_pecas_disponiveis = [1]
houve_peca_excluida = False

def main() -> None:
    pass

def gerar_id_peca(pecas: list[dict]) -> int:
    global ids_pecas_disponiveis

    numero_pecas = len(pecas)
    numero_ids_pecas_disponiveis = len(ids_pecas_disponiveis)

    if (
        (numero_ids_pecas_disponiveis != 0 and numero_pecas <= 0)
        or (numero_ids_pecas_disponiveis != 0 and numero_pecas > 0 and houve_peca_excluida)
    ):
        return ids_pecas_disponiveis.pop()
    
    ultima_peca_cadastrada = pecas[numero_pecas - 1]
    return ultima_peca_cadastrada["id"] + 1
    

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
    print(f"ID GERADO = {id}")
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


def receber_id_peca(pecas: list[dict]) -> int:

    while True:
        id = receber_numero_inteiro(TEXTO_ENTRADA_ID_PECA)

        if verificar_peca_existe_por_id(pecas, id):
            print(TEXTO_SAIDA_ALERTA_ID_PECA_JA_EXISTE)
        else:
            return id


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


def buscar_cor_por_id(id_cor: int, cores: list[dict]) -> str:

    cores_map = {cor["id"]: cor["nome"] for cor in cores}
    return cores_map.get(id_cor)


if __name__ == "__main__":
    main()
