import logging
import pytest

class LogGen:
    # logging.basicConfig(filename=".//Logs//.automation.logs",
    #                     format ='%(asctime)s: %(levelname)s: %(message)s',
    #                     datefmt='%Y-%m-%d %H:%M:%S%P')
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\logs\\automation.log",
                            filemode='a',
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S%p',
                            force=True)

        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

