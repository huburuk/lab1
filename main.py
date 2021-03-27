#!/usr/bin/env python3
import logging
import random

logging.basicConfig(level=logging.INFO)


def main():
    logging.info("загадано рандомное число от 0 до 100")
    number1 = random.randint(0, 100)
    for counter in range(3):
        while True:
            try:
                number2 = int(input("введите ваше число:"))
                break
            except ValueError:
                logging.info("Ошибка!")   
        if number1 > number2 or number1 < number2:
            logging.info("вы не угадали")
            if counter == 2:
                logging.info("Попытки кончились(")
                break
            if number2 < number1:
                logging.info("ваше число меньше нужного, повторите попытку...")
            elif number2 > number1:
                logging.info("ваше число больше нужного, повторите попытку...")
        else:
            logging.info("Вы угадали))")
            break


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logging.error("Ошибка!")
