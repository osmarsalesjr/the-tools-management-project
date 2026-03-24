APPROVED_STATUS = "APROVADO"
FAILED_STATUS = "REPROVADO"

FAILED_WEIGHT_REASON = "PESO DA PEÇA NÃO SEGUE OS PADRÕES DE QUALIDADE."
FAILED_COLOR_REASON = "COR DA PEÇA NÃO SEGUE OS PADRÕES DE QUALIDADE."
FAILED_LENGTH_REASON = "COMPRIMENTO DA PEÇA NÃO SEGUE OS PADRÕES DE QUALIDADE."


def main() -> None:
    pass


def id_exists(tools: list[dict], id: int) -> bool:

    if tools is None or len(tools) == 0:
        return False

    tools_ids = [tool["id"] for tool in tools if tool["id"] == id]

    if len(tools_ids) != 0:
        return True
    
    return False


def process_tool_validation(tool: dict) -> dict:

    if tool is None:
        return tool

    weight = tool["weight"]
    color = str(tool["color"])
    length = tool["length"]
    failed_reasons = []

    if weight < 95 or weight > 105:
        failed_reasons.append(FAILED_WEIGHT_REASON)

    if color.casefold() != "azul".casefold() and color.casefold() != "verde".casefold():
        failed_reasons.append(FAILED_COLOR_REASON)

    if length < 10 or length > 20:
        failed_reasons.append(FAILED_LENGTH_REASON)

    if len(failed_reasons) == 0:
        tool["status"] = APPROVED_STATUS
    else:
        tool["status"] = FAILED_STATUS
        tool["failed_reasons"] = failed_reasons
    
    return tool


if __name__ == "__main__":
    main()
