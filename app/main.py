from tools_operations import create_tool
from boxes_operations import add_tool_to_box

MENU_INPUT_TEXT = "\nDigite a opção desejada: "
MENU_INVALID_OPTION_OUTPUT_TEXT = "Opção inválida!"

APPLICATION_ENDED_OUTPUT_TEXT = "Programa encerrado pelo usuário.\n"
PAUSE_INPUT_TEXT = "Pressione ENTER para continuar..."

TOOL_ADDED_SUCCESSFULLY_OUTPUT_TEXT = "\nPeça cadastrada com sucesso!"

N_BOXES_FOUND_OUTPUT_TEXT = "QUANTIDADE DE CAIXAS ENCONTRADAS: "

NO_BOXES_CREATED_OUTPUT_TEXT = "\nNão há caixas criadas."
NO_TOOLS_CREATED_OUTPUT_TEXT = "\nNão há peças cadastradas."


def main() -> None:

    tools = []
    boxes = []

    while True:

        show_menu()
        option = input(MENU_INPUT_TEXT)

        match option:
            case "0":
                print(APPLICATION_ENDED_OUTPUT_TEXT)
                break
            case "1":
                new_tool = add_tool(tools)
                add_tool_to_box(boxes, new_tool)
                pause()
            case "2":
                draw_title("Peças", 40)
                list_tools(tools)
                pause()
            case "6":
                list_all_boxes(boxes)
                pause()
            case _:
                print(MENU_INVALID_OPTION_OUTPUT_TEXT)


def pause() -> None:
    input(PAUSE_INPUT_TEXT)


def show_menu() -> None:

    draw_title("Menu", 50)
    print("1. Cadastrar nova peça")
    print("2. Listar peças aprovadas/reprovadas")
    print("3. Remover peça cadastrada")
    print("4. Listar caixas fechadas")
    print("5. Gerar relatório final")
    print("6. Listar todas as caixas")
    print("0. Sair")


def add_tool(tools: list[dict]) -> dict:
    new_tool = create_tool(tools)
    tools.append(new_tool)

    print(TOOL_ADDED_SUCCESSFULLY_OUTPUT_TEXT)

    return new_tool


def remove_tool():
    pass


def list_tools(tools: list[dict]) -> None:

    if len(tools) == 0:
        print(NO_TOOLS_CREATED_OUTPUT_TEXT)
        return

    for tool in tools:
        print(("_" * 60))
        print(
            f"| ID: {tool["id"]} | PESO: {tool["weight"]}g | COR: {tool["color"]} | COMPRIMENTO: {tool["length"]} cm |"
        )
        print(f"| STATUS: {tool["status"]}")

        failed_reasons = list(tool["failed_reasons"])

        if len(failed_reasons) != 0:
            reasons = "\n| ".join(failed_reasons)
            print(f"| MOTIVOS DA REPROVAÇÃO:\n| {reasons}")
        print(("_" * 60))


def list_closed_boxes() -> None:
    pass


def list_all_boxes(boxes: list[list[dict]]) -> None:

    boxes_size = len(boxes)

    if boxes_size == 0:
        print(NO_BOXES_CREATED_OUTPUT_TEXT)
        return

    draw_title("Caixas", 40)
    for i in range(boxes_size):
        draw_title(f"Caixa {i + 1}", 30)
        draw_title("Peças")
        list_tools(boxes[i])
    
    print(N_BOXES_FOUND_OUTPUT_TEXT + f"{boxes_size}")


def create_final_report():
    pass


def draw_title(title: str, times: int = 20) -> None:
    print((">" * times) + f" {title.upper()} " + ("<" * times))


if __name__ == "__main__":
    main()
