from operacoes_pecas import (
    criar_peca,
    receber_numero_inteiro,
    receber_cor_peca,
    buscar_peca_por_id,
    atualizar_ids_pecas_disponiveis,
)

from operacoes_caixas import (
    criar_caixas_com_lista_de_pecas,
    buscar_caixa_para_nova_peca,
    remover_peca_de_caixa,
)

from operacoes_banco_de_dados import (
    conectar_banco_de_dados,
    salvar_peca,
    recuperar_todas_as_pecas,
    recuperar_peca_por_id,
    remover_peca
)

from massa_dados_testes import (
    pegar_lista_pecas
)

TEXTO_ENTRADA_PESO_PECA = "\nDigite o peso em gramas (g) da peça: "
TEXTO_ENTRADA_COMPRIMENTO_PECA = "\nDigite o comprimento em centímetro (cm) da peça: "

TEXTO_ENTRADA_MENU_PRINCIPAL = "\nDigite a opção desejada: "
TEXTO_ENTRADA_ID_PECA_A_REMOVER = (
    "\nDigite a identificação numérica da peça a ser removida: "
)

TEXTO_SAIDA_ALERTA_OPCAO_INVALIDA = "Opção inválida!"

TEXTO_SAIDA_PROGRAMA_ENCERRADO = "Programa encerrado pelo usuário.\n"
TEXTO_SAIDA_PAUSA_PROGRAMA = "Pressione ENTER para continuar..."

TEXTO_SAIDA_PECA_ADICIONADA_COM_SUCESSO = (
    "\nPeça cadastrada com sucesso! Identificação da peça: "
)
TEXTO_SAIDA_ALERTA_PECA_NAO_ENCONTRADA = "\nO id da peça digitado não existe!"
TEXTO_SAIDA_PECA_REMOVIDA_COM_SUCESSO = "\nPeça removida com sucesso!"

TEXTO_SAIDA_NUMERO_CAIXAS_ENCONTRADAS = "QUANTIDADE DE CAIXAS ENCONTRADAS: "
TEXTO_SAIDA_NAO_HA_CAIXAS_CRIADAS = "\nNão há caixas criadas."
TEXTO_SAIDA_NAO_PECAS_CADASTRADAS = "\nNão há peças cadastradas."

STATUS_APROVADO = "APROVADO"

def main() -> None:

    conectar_banco_de_dados()

    # pecas = [] comecar lista com zerada
    # pecas = pegar_lista_pecas()

    pecas = []
    caixas = []

    # atualizar lista de caixas com massa de testes
    criar_caixas_com_lista_de_pecas(pecas, caixas)

    while True:

        imprimir_menu()
        option = input(TEXTO_ENTRADA_MENU_PRINCIPAL)

        match option:
            case "0":
                print(TEXTO_SAIDA_PROGRAMA_ENCERRADO)
                break
            case "1":
                adicionar_peca()
                pausar()
            case "2":
                pecas = recuperar_todas_as_pecas()
                desenhar_titulo("Peças", 40)
                listar_pecas(pecas)
                pausar()
            case "3":
                pecas = recuperar_todas_as_pecas()
                excluir_peca(pecas)
                pausar()
            case "4":
                listar_caixas_fechadas(caixas)
                pausar()
            case "6":
                listar_caixas(caixas)
                pausar()
            case _:
                print(TEXTO_SAIDA_ALERTA_OPCAO_INVALIDA)


def pausar() -> None:
    input(TEXTO_SAIDA_PAUSA_PROGRAMA)


def imprimir_menu() -> None:

    desenhar_titulo("Menu", 50)
    print("1. Cadastrar nova peça")
    print("2. Listar peças aprovadas/reprovadas")
    print("3. Remover peça cadastrada")
    print("4. Listar caixas fechadas")
    print("5. Gerar relatório final")
    print("6. Listar todas as caixas")
    print("0. Sair")


def adicionar_peca() -> dict:

    peso = receber_numero_inteiro(TEXTO_ENTRADA_PESO_PECA)
    cor = receber_cor_peca()
    comprimento = receber_numero_inteiro(TEXTO_ENTRADA_COMPRIMENTO_PECA)

    peca = criar_peca(peso, cor, comprimento)

    if peca["status"].casefold() == STATUS_APROVADO.casefold():
        caixa = buscar_caixa_para_nova_peca()
        caixa_id = caixa.get("id")
        peca["caixa_id"] = caixa_id

    peca_salva = salvar_peca(peca)
    print(TEXTO_SAIDA_PECA_ADICIONADA_COM_SUCESSO + f"{peca_salva["id"]}.")



def excluir_peca(pecas: list[dict]):

    while True:
        listar_pecas(pecas)
        id_peca = receber_numero_inteiro(TEXTO_ENTRADA_ID_PECA_A_REMOVER)

        peca_encontrada = recuperar_peca_por_id(id_peca)
        if peca_encontrada is not None:
            break
        else:
            print(TEXTO_SAIDA_ALERTA_PECA_NAO_ENCONTRADA)
            pausar()

    remover_peca(peca_encontrada.get("id"))
    print(TEXTO_SAIDA_PECA_REMOVIDA_COM_SUCESSO)


def listar_pecas(pecas: list[dict]) -> None:

    if len(pecas) == 0:
        print(TEXTO_SAIDA_NAO_PECAS_CADASTRADAS)
        return

    for peca in pecas:
        print(("_" * 60))
        print(
            f"| ID: {peca["id"]} | PESO: {peca["peso"]}g | COR: {peca["cor"]} | COMPRIMENTO: {peca["comprimento"]} cm |"
        )
        print(f"| STATUS: {peca["status"]}")

        motivos_reprovacao = list(peca["motivos_reprovacao"])

        if len(motivos_reprovacao) != 0:
            motivos = "\n| ".join(motivos_reprovacao)
            print(f"| MOTIVOS DA REPROVAÇÃO:\n| {motivos}")
        print(("_" * 60))


def listar_caixas_fechadas(caixas: list[dict]) -> None:
    caixas_fechadas = caixas_fechadas = [
        caixa for caixa in caixas if caixa["esta_fechada"]
    ]
    listar_caixas(caixas_fechadas)


def listar_caixas(caixas: list[dict]) -> None:

    caixas_size = len(caixas)

    if caixas_size == 0:
        print(TEXTO_SAIDA_NAO_HA_CAIXAS_CRIADAS)
        return

    desenhar_titulo("Caixas", 40)
    for i in range(caixas_size):
        status = "CAIXA FECHADA" if caixas[i]["esta_fechada"] else "CAIXA ABERTA"
        desenhar_titulo(f"{status}", 30)
        desenhar_titulo("Peças")
        listar_pecas(caixas[i]["pecas"])

    print(TEXTO_SAIDA_NUMERO_CAIXAS_ENCONTRADAS + f"{caixas_size}")


def imprimir_relatorio_final():
    pass


def desenhar_titulo(titulo: str, multiplicador: int = 20) -> None:
    print((">" * multiplicador) + f" {titulo.upper()} " + ("<" * multiplicador))


""" def adicionar_peca(pecas: list[dict]) -> dict:
    nova_peca = criar_peca(pecas)
    pecas.append(nova_peca)

    print(TEXTO_SAIDA_PECA_ADICIONADA_COM_SUCESSO + f"{nova_peca["id"]}.")
    return nova_peca
 
def remover_peca(pecas: list[dict]):

    while True:
        listar_pecas(pecas)
        id_peca = receber_numero_inteiro(TEXTO_ENTRADA_ID_PECA_A_REMOVER)

        peca_encontrada = buscar_peca_por_id(id_peca, pecas)
        if peca_encontrada is not None:
            break
        else:
            print(TEXTO_SAIDA_ALERTA_PECA_NAO_ENCONTRADA)
            pausar()

    pecas.remove(peca_encontrada)
    print(TEXTO_SAIDA_PECA_REMOVIDA_COM_SUCESSO)

    return peca_encontrada """

if __name__ == "__main__":
    main()
