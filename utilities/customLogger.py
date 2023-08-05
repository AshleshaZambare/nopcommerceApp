import logging


class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger(__name__)
        file_handler = logging.FileHandler(".\\Logs\\test_logging.log")
        Formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(Formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.DEBUG)
        return logger
