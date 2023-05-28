import logging

import inject as inject
from on_rails import Result, def_result, try_func
from pydantic import BaseModel

from package_name.utility import get_formatted_datetime


class StreamConfig(BaseModel):
    """ Stream configs model for logger """
    disable = False
    level = 'info'
    format = '[%(levelname)s] %(message)s'


class FileConfig(BaseModel):
    """ File configs model for logger """
    disable = True
    level = 'debug'
    file_name = 'app'
    format = '%(asctime)s [%(levelname)s] %(message)s'


class LogConfigs(BaseModel):
    """ Configs model for logger """
    stream: StreamConfig
    file: FileConfig


@def_result()
def create_logger(log_configs: LogConfigs) -> Result:
    """
    The create_logger function is responsible for creating a logger object that can be used to log messages.
    The function takes in a LogConfigs object, which contains the configuration information needed to create the logger.
    The function returns either an error or the created logger.
    """
    _logger = logging.getLogger()
    _logger.setLevel(logging.DEBUG)

    if not log_configs.file.disable:
        file_name = f"{log_configs.file.file_name}-{get_formatted_datetime()}.log"
        file_handler = logging.FileHandler(file_name)
        file_handler.setLevel(_get_set_level(log_configs.file.level))
        file_formatter = logging.Formatter(log_configs.file.format)
        file_handler.setFormatter(file_formatter)
        _logger.addHandler(file_handler)

    if not log_configs.stream.disable:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(_get_set_level(log_configs.stream.level))
        stream_formatter = logging.Formatter(log_configs.stream.format)
        stream_handler.setFormatter(stream_formatter)
        _logger.addHandler(stream_handler)

    return Result.ok(_logger)


def _get_set_level(level: str):
    level = level.upper()

    match level:
        case 'CRITICAL':
            return logging.CRITICAL
        case 'FATAL':
            return logging.FATAL
        case 'ERROR':
            return logging.ERROR
        case 'WARNING':
            return logging.WARNING
        case 'WARN':
            return logging.WARN
        case 'INFO':
            return logging.INFO
        case 'DEBUG':
            return logging.DEBUG
        case 'NOTSET':
            return logging.NOTSET
        case _:
            return logging.NOTSET


class ColorfulConsole:
    # ANSI escape sequences for different colors
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'

    @staticmethod
    def error(text):
        ColorfulConsole._print(ColorfulConsole.RED, text)

    @staticmethod
    def success(text):
        ColorfulConsole._print(ColorfulConsole.GREEN, text)

    @staticmethod
    def warning(text):
        ColorfulConsole._print(ColorfulConsole.YELLOW, text)

    @staticmethod
    def info(text):
        ColorfulConsole._print(ColorfulConsole.BLUE, text)

    @staticmethod
    def _print(color_code, text: str):
        print(color_code + text + ColorfulConsole.RESET)


def log_result(result: Result) -> None:
    """
    Logs the result of an operation.
    """
    inject_result = try_func(lambda: inject.instance(logging.Logger))
    if not inject_result.success or not inject_result.value:
        logger = ColorfulConsole()
    else:
        logger = inject_result.value

    if result.success:
        if result.detail or result.value:
            logger.info(str(result))
        else:
            logger.info("The operation was completed successfully.")
    else:
        if not result.detail:
            logger.error(repr(result))
        # elif result.detail.is_instance_of(MetaTraderDetail):
        #     logger.error(str(result))  # Expected errors no need detail like stacktrace, etc
        else:
            logger.error(repr(result))  # Unexpected error
