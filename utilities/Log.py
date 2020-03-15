import inspect
import logging

"""
This is a wrapper helper class for capturing logging during tests run 
"""


class Log:

    def __init__(self, filename="runLogs.txt"):
        logger_name = inspect.stack()[1][3]
        self.logger = logging.getLogger(logger_name)

        self.file_handler = logging.FileHandler(filename)

        self.file_handler.setFormatter(logging.Formatter("%(asctime)s\t|\t%(levelname)s\t|\t%(name)s | %(message)s"))

        self.logger.addHandler(self.file_handler)

        self.logger.setLevel(logging.DEBUG)

    """
        Use this method when it is required to change logging level of a Test Run.
        Level Parameter expects a string of the level you wanna set. Level is by default set to Debug
    """
    def change_logging_level(self, level='debug'):
        level.lower()

        if level == 'debug':
            self.logger.setLevel(logging.DEBUG)
        elif level == 'info':
            self.logger.setLevel(logging.INFO)
        elif level == 'warning':
            self.logger.setLevel(logging.WARNING)
        elif level == 'error':
            self.logger.setLevel(logging.ERROR)
        elif level == 'critical':
            self.logger.setLevel(logging.CRITICAL)
        else:
            self.logger.error(f"Invalid parameter for level was passed to change_logging_level method: {level}")

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.file_handler.setFormatter(logging.Formatter("%(asctime)s\t|\t%(levelname)s|\t%(name)s | %(message)s"))
        self.logger.addHandler(self.file_handler)

        self.logger.critical(message)

        self.file_handler.setFormatter(logging.Formatter("%(asctime)s\t|\t%(levelname)s\t|\t%(name)s | %(message)s"))
        self.logger.addHandler(self.file_handler)




