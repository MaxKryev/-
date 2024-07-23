from typing import Tuple


class IncorrectInputException(Exception):
    pass


def validation_operator(string: str) -> str:
    operator_counter = 0
    operator = None
    for elem in string:
        if elem in ['+', '/', '-', '*']:
            operator_counter += 1
            operator = elem
    if operator_counter == 0:
        raise IncorrectInputException('throws Exception //т.к. строка не является математической операцией')
    elif operator_counter != 1:
        raise IncorrectInputException('throws Exception //т.к. формат математической операции не удовлетворяет заданию - два операнда и один оператор (+, -, /, *)')
    return operator


def validation_operands(string: str, operator: str) -> tuple[str, str]:
    operands_list = string.split(' ' + operator + ' ')
    if len(operands_list) != 2:
        raise IncorrectInputException('throws Exception операнды')
    for operand in operands_list:
        if not (operand.isdigit() and 0 < int(operand) < 11):
            raise IncorrectInputException('throws Exception число')
    return operands_list[0], operands_list[1]


def main(input: str) -> None:
    operator = validation_operator(input)
    operand_1, operand_2 = validation_operands(input, operator)

    if operator == '+':
        result = int(operand_1) + int(operand_2)
    elif operator == '-':
        result = int(operand_1) - int(operand_2)
    elif operator == '*':
        result = int(operand_1) * int(operand_2)
    elif operator == '/':
        result = int(operand_1) // int(operand_2)
    print(str(result))


example = input()
main(example)
