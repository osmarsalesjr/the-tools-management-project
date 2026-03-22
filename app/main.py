from tools_operations import create_tool

MENU_INPUT_TEXT = "\nDigite a opção desejada: "
MENU_INVALID_OPTION_OUTPUT_TEXT = "Opção inválida!"

APPLICATION_ENDED_OUTPUT_TEXT = "Programa encerrado pelo usuário.\n"
PAUSE_INPUT_TEXT = "Pressione ENTER para continuar..."

def main():

    tools = []
    boxes = []

    while(True):

        show_menu()
        option = input(MENU_INPUT_TEXT)

        match option:
            case "0":
                print(APPLICATION_ENDED_OUTPUT_TEXT)
                break
            case "1":
                add_tool(tools, boxes)
            case "2":
                list_tools(tools)
            case _:
                print(MENU_INVALID_OPTION_OUTPUT_TEXT)

def pause():
    input(PAUSE_INPUT_TEXT)

def show_menu():
    print("\n")
    print((">" * 20) + " Menu " + ("<" * 20))
    print("1. Cadastrar nova peça")
    print("2. Listar peças aprovadas/reprovadas")
    print("3. Remover peça cadastrada")
    print("4. Listar caixas fechadas")
    print("5. Gerar relatório final")
    print("0. Sair")

def add_tool(tools:list, boxes: list):
    new_tool = create_tool(tools)
    tools.append(new_tool)

def remove_tool():
    pass

def list_tools(tools: list):
    print("\n")
    print((">" * 30) + " Peças " + ("<" * 30))

    for tool in tools:
        print(("_" * 60) + "\n")
        print(f"| ID: {tool["id"]} | PESO: {tool["weight"]} | COR: {tool["color"]} | COMPRIMENTO: {tool["length"]} |")
        print(f"| STATUS: {tool["status"]}")

        failed_reasons = list(tool["failed_reasons"])
        if len(failed_reasons) != 0:
            reasons = "\n| ".join(failed_reasons)
            print(f"| Motivos da Reprovação:\n| {reasons}")
        print(("_" * 60) + "\n")
        

def list_closed_boxes():
    pass

def create_final_report():
    pass

if __name__ == "__main__":
    main()