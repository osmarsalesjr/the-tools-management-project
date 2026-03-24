APPROVED_STATUS = "APROVADO"
TOOL_ADDED_TO_BOX_SUCCESSFULLY_OUTPUT_TEXT = "Peça foi adicionada a uma caixa."


def main() -> None:
    pass


def add_tool_to_box(boxes: list[list[dict]], new_tool: dict) -> None:

    status = str(new_tool["status"])

    if status.casefold() != APPROVED_STATUS.casefold():
        return


    if len(boxes) == 0:
        new_box = [new_tool]
        boxes.append(new_box)
        print(TOOL_ADDED_TO_BOX_SUCCESSFULLY_OUTPUT_TEXT)
        return
    
    is_new_tool_added = False

    for box in boxes:
        if len(box) >= 10:
            continue
        else:
            box.append(new_tool)
            is_new_tool_added = True
            print(TOOL_ADDED_TO_BOX_SUCCESSFULLY_OUTPUT_TEXT)
    
    if is_new_tool_added is False:
        new_box = [new_tool]
        boxes.append(new_box)
        print(TOOL_ADDED_TO_BOX_SUCCESSFULLY_OUTPUT_TEXT)


if __name__ == "__main__":
    main()
