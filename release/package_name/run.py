import logging

import inject


def run() -> None:
    say_hellp()


@inject.autoparams()
def say_hellp(logger: logging.Logger):
    logger.info("Injector works!")
