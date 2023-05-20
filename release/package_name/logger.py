import logging

from on_rails import Result, def_result
from pydantic import BaseModel


class StreamConfig(BaseModel):
    disable = False
    level = 'info'
    format = '[%(levelname)s] %(message)s'


class FileConfig(BaseModel):
    disable = True
    level = 'debug'
    file_name = 'app.log'
    format = '%(asctime)s [%(levelname)s] %(message)s'


class LogConfigs(BaseModel):
    stream: StreamConfig
    file: FileConfig


@def_result()
def create_logger(log_configs: LogConfigs) -> Result:
    _logger = logging.getLogger()
    _logger.setLevel(logging.DEBUG)

    if not log_configs.file.disable:
        file_handler = logging.FileHandler(log_configs.file.file_name)
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
