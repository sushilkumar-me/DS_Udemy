import logging

logging.basicConfig(level=logging.DEBUG, filename="log.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")

try:
    1/0
except ZeroDivisionError as e:
    logging.exception("ZeroDivisionError")