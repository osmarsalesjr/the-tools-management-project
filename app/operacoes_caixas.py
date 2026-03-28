from operacoes_banco_de_dados import (
    recuperar_todas_as_caixas,
    criar_caixa
)

STATUS_APROVADO = "APROVADO"


def main() -> None:
    pass


def adicionar_peca_a_caixa(caixas: list[dict], nova_peca: dict) -> None:

    status = str(nova_peca["status"])

    if status.casefold() != STATUS_APROVADO.casefold():
        return

    if len(caixas) == 0:
        nova_caixa = criar_nova_caixa(nova_peca)
        caixas.append(nova_caixa)
        print("Peça foi adicionada a uma caixa.")
        return

    peca_esta_encaixada = False

    for caixa in caixas:
        esta_fechada = caixa["esta_fechada"]

        if esta_fechada:
            continue

        caixa["pecas"].append(nova_peca)
        peca_esta_encaixada = True
        numero_pecas = len(caixa["pecas"])

        if numero_pecas >= 10:
            caixa["esta_fechada"] = True
        break

    if peca_esta_encaixada is False:
        nova_caixa = criar_nova_caixa(nova_peca)
        caixas.append(nova_caixa)

    print("Peça foi adicionada a uma caixa.")


def buscar_caixa_para_nova_peca() -> dict | None:
    
    caixas = recuperar_todas_as_caixas()

    if len(caixas) == 0:
        return criar_caixa()

    caixa_para_nova_peca_encontrada = False

    for caixa in caixas:
        esta_fechada = caixa["esta_fechada"]

        if esta_fechada:
            continue

        return caixa

    if caixa_para_nova_peca_encontrada is False:
        return criar_caixa()

    print("Peça foi adicionada a uma caixa.")


def criar_nova_caixa(nova_peca: dict) -> dict:
    return {"esta_fechada": False, "pecas": [nova_peca]}


def criar_caixas_com_lista_de_pecas(pecas: list[dict], caixas: list[dict]) -> None:

    for peca in pecas:
        adicionar_peca_a_caixa(caixas, peca)


def remover_peca_de_caixa(peca_removida: dict, caixas: list[dict]) -> None:

    for caixa in caixas:

        if peca_removida in caixa["pecas"]:
            caixa["pecas"].remove(peca_removida)
            esta_fechada = caixa["esta_fechada"]
            caixa["esta_fechada"] = False if esta_fechada else False

            print(
                f"Peça de ID {peca_removida["id"]} foi removida da caixa em que estava localizada."
            )
            return


if __name__ == "__main__":
    main()
