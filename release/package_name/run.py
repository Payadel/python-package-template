import logging

import inject

from package_name.inputs import Inputs


def run() -> None:
    say_hellp()


@inject.autoparams()
def say_hellp(logger: logging.Logger, inputs: Inputs):
    logger.info(f"Hello {inputs.name}!")
