#!/usr/bin/env python3
import logging
import random

logging.basicConfig(level=logging.INFO)


def main():
    logging.info("загадано рандомное число от 0 до 100:")
    number1 = random.randint(0, 100)
    for i in range(3):
        logging.info("введите ваше число:")
        number2 = int(input())
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

