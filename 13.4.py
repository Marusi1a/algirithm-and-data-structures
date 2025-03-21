def convert_to_base_p(number: str, base: str) -> str:
    decimal = int(number)
    p = int(base)
    if decimal == 0:
        return "0"

    stack = []
    while decimal > 0:
        d = decimal % p
        decimal = decimal // p
        if d < 10:
            stack.append(str(d))
        else:
            stack.append(f"[{d}]")

    # Збираємо результат у зворотному порядку
    result = "".join(reversed(stack))
    return result


if __name__ == '__main__':
    num = input().strip()
    base = input().strip()
    res = convert_to_base_p(num, base)
    print(res)
