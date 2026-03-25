from operacoes_pecas import criar_peca
from operacoes_caixas import adicionar_peca_a_caixa, criar_caixas_com_lista_de_pecas
from massa_dados_testes import pegar_lista_pecas

TEXTO_ENTRADA_MENU_PRINCIPAL = "\nDigite a opção desejada: "
TEXTO_SAIDA_ALERTA_OPCAO_INVALIDA = "Opção inválida!"

TEXTO_SAIDA_PROGRAMA_ENCERRADO = "Programa encerrado pelo usuário.\n"
TEXTO_SAIDA_PAUSA_PROGRAMA = "Pressione ENTER para continuar..."

TEXTO_SAIDA_PECA_ADICIONADA_COM_SUCESSO = "\nPeça cadastrada com sucesso!"

TEXTO_SAIDA_NUMERO_CAIXAS_ENCONTRADAS = "QUANTIDADE DE CAIXAS ENCONTRADAS: "
TEXTO_SAIDA_NAO_HA_CAIXAS_CRIADAS = "\nNão há caixas criadas."
TEXTO_SAIDA_NAO_PECAS_CADASTRADAS = "\nNão há peças cadastradas."


def main() -> None:

    # pecas = [] comecar lista com zerada
    pecas = pegar_lista_pecas()
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
                nova_peca = adicionar_peca(pecas)
                adicionar_peca_a_caixa(caixas, nova_peca)
                pause()
            case "2":
                desenhar_titulo("Peças", 40)
                listar_pecas(pecas)
                pause()
            case "6":
                listar_todas_as_caixas(caixas)
                pause()
            case _:
                print(TEXTO_SAIDA_ALERTA_OPCAO_INVALIDA)


def pause() -> None:
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


def adicionar_peca(pecas: list[dict]) -> dict:
    nova_peca = criar_peca(pecas)
    pecas.append(nova_peca)

    print(TEXTO_SAIDA_PECA_ADICIONADA_COM_SUCESSO)
    return nova_peca


def remover_peca():
    pass


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


def listar_caixas_fechadas() -> None:
    pass


def listar_todas_as_caixas(caixas: list[dict]) -> None:

    caixas_size = len(caixas)

    if caixas_size == 0:
        print(TEXTO_SAIDA_NAO_HA_CAIXAS_CRIADAS)
        return

    desenhar_titulo("Caixas", 40)
    for i in range(caixas_size):
        desenhar_titulo(f"Caixa {i + 1}", 30)
        status = "CAIXA FECHADA" if caixas[i]["esta_fechada"] else "CAIXA ABERTA"
        print(status)
        desenhar_titulo("Peças")
        listar_pecas(caixas[i]["pecas"])
    
    print(TEXTO_SAIDA_NUMERO_CAIXAS_ENCONTRADAS + f"{caixas_size}")


def imprimir_relatorio_final():
    pass


def desenhar_titulo(titulo: str, multiplicador: int = 20) -> None:
    print((">" * multiplicador) + f" {titulo.upper()} " + ("<" * multiplicador))


if __name__ == "__main__":
    main()
