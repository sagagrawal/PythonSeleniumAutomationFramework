from utilities.Log import Log

log = Log("logs.txt")


def test_log_runner():
    log.debug("This is a debug log")
    log.critical("this is a CRITICAL log")
    log.info("this is a information log")
    log.warning("warning log")
    log.error("error log")
    log.change_logging_level()
