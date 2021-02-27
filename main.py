import logging

logging.basicConfig(level=logging.INFO)


def main():
    logging.info("hello world")
    def sum(term1, term2):
        return term1 + term2
    logging.info(sum(3, 4))


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
