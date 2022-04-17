import logging
import os

loggers = {}


def _init_logger(name="WDM", formatter='[%(name)s] - %(message)s', level=None):
    """Initialize the logger."""
    if not loggers.get(name):
        _logger = logging.getLogger(name)

        handler = logging.StreamHandler()
        formatter = logging.Formatter(formatter)
        handler.setFormatter(formatter)
        _logger.addHandler(handler)
        _logger.setLevel(level)
        loggers[name] = _logger
    else:
        loggers.get(name).handlers[0].setFormatter(logging.Formatter(formatter))


def log(text, name="WDM", formatter='[%(name)s] - %(message)s'):
    """Emitting the log message."""
    log_level = int(os.getenv('WDM_LOG_LEVEL', logging.INFO))

    if os.getenv('WDM_LOG', '') != '0':
        _init_logger(name, formatter, log_level)
        loggers.get(name).log(log_level, text)
