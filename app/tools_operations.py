from tools_validations import id_exists, process_tool_validation

TOOL_ID_INPUT_TEXT = "\nDigite a identificação numérica da peça: "
TOOL_ID_EXISTS_OUTPUT_TEXT = "A identificação da peça digitada já está cadastrada."

TOOL_WEIGHT_INPUT_TEXT = "\nDigite o peso em gramas (g) da peça: "
TOOL_COLOR_INPUT_TEXT = "\nEscolha o número da cor da peça: "
TOOL_COLOR_NOT_FOUND_OUTPUT_TEXT = (
    "A número da cor escolhida não foi encontrada. Tente novamente."
)
TOOL_LENGTH_INPUT_TEXT = "\nDigite o comprimento em centímetro (cm) da peça: "

TOOL_INT_VALUE_ERROR_EXCEPTION_OUTPUT_TEXT = "Erro! O valor deve ser numérico."
TOOL_EXCEPTION_OUTPUT_TEXT = "Erro inesperado! Tente novamente."


def main() -> None:
    pass


def int_input(input_text: str) -> int:
    while True:
        try:
            id = int(input(input_text))
            return id
        except ValueError:
            print(TOOL_INT_VALUE_ERROR_EXCEPTION_OUTPUT_TEXT)
        except Exception:
            print(TOOL_EXCEPTION_OUTPUT_TEXT)


def create_tool(tools: list[dict]) -> dict:
    id = id_input(tools)
    weight = int_input(TOOL_WEIGHT_INPUT_TEXT)
    color = color_input()
    length = int_input(TOOL_LENGTH_INPUT_TEXT)

    tool = {
        "id": id,
        "weight": weight,
        "color": color,
        "length": length,
        "status": "",
        "failed_reasons": [],
    }

    return process_tool_validation(tool)


def id_input(tools: list[dict]) -> int:

    while True:
        id = int_input(TOOL_ID_INPUT_TEXT)

        if id_exists(tools, id):
            print(TOOL_ID_EXISTS_OUTPUT_TEXT)
        else:
            return id


def color_input() -> str:

    colors = [
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
            show_colors(colors)
            color_id = int(input(TOOL_COLOR_INPUT_TEXT))
            color = get_color(color_id, colors)

            if color is None:
                print(TOOL_COLOR_NOT_FOUND_OUTPUT_TEXT)
            else:
                return color.upper()
        except ValueError:
            print(TOOL_INT_VALUE_ERROR_EXCEPTION_OUTPUT_TEXT)
        except Exception:
            print(TOOL_EXCEPTION_OUTPUT_TEXT)


def show_colors(colors: list[dict]) -> None:

    print((">" * 10) + " Cores " + ("<" * 10))
    for color in colors:
        print(f"{color["id"]}. {color["nome"]}")


def get_color(color_id: int, colors: list[dict]) -> str:

    colors_map = {color["id"]: color["nome"] for color in colors}
    return colors_map.get(color_id)


if __name__ == "__main__":
    main()
