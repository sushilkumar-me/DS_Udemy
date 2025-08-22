import logging

logging.basicConfig(level=logging.DEBUG, filename="log.log", filemode="w", 
                    format="%(asctime)s - %(levelname)s - %(message)s")

x = 2
logging.debug(f"The value of x is {x}")