import logging

logging.basicConfig(level=logging.INFO)


def main():
    logging.info("введите число a:")
    a = input()
    logging.info("введите число b:")
    b = input()
    if a > b:
        logging.info("вы тупой")
        return 0
    logging.info("загадайте рандомное число от a до b:")
    number1 = input()
    if number1 > b or number1 < a:
        logging.info("введите другое число:")
        number1 = input()
        if number1 > b or number1 < a:
            logging.info("вы тупой")
            return 0
    for i in range(3):
        logging.info("введите ваше число:")
        number2 = input()
        if (number1 > number2) or (number1 < number2):
            logging.info("вы не угадали")
            if i == 2:
                logging.info("Попытки кончились(")
                return 0
            if number2 < number1:
                logging.info("ваше число меньше нужного, повторите попытку...")
            elif number2 > number1:
                logging.info("ваше число больше нужного, повторите попытку...")
        else:
            logging.info("Вы угадали))")
            return 0


if __name__ == '__main__':
    main()

