# Пріоритет операторів
PRIORITY = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}

# Функція визначення необхідності дужок
def need_brackets(current_op: str, inner_op: str, is_right: bool) -> bool:
    if inner_op == '':
        return False
    if PRIORITY[current_op] < PRIORITY[inner_op]:
        return False
    if PRIORITY[current_op] > PRIORITY[inner_op]:
        return True
    # Операції з однаковим пріоритетом, враховуємо асоціативність
    return is_right and current_op in '-/'

# Функція перетворення префіксного виразу на інфіксний
def to_infix(sequence: str) -> str:
    stack = []
    operators = "+-*/"

    # Рухаємося з кінця виразу до початку
    for token in reversed(sequence):
        if token in operators:
            # Дістаємо два операнди зі стеку
            left_expr, left_op = stack.pop()
            right_expr, right_op = stack.pop()

            # Додаємо дужки, якщо потрібно
            if need_brackets(token, left_op, False):
                left_expr = f"({left_expr})"
            if need_brackets(token, right_op, True):
                right_expr = f"({right_expr})"

            # Формуємо інфіксний вираз
            expression = f"{left_expr}{token}{right_expr}"
            stack.append((expression, token))
        else:
            # Якщо це операнд, додаємо його в стек без оператора
            stack.append((token, ''))

    # Повертаємо результат
    return stack.pop()[0]

# Головна частина програми
if __name__ == '__main__':
    seq = input().strip()
    print(to_infix(seq))
