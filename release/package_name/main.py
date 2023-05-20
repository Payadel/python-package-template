import logging

import inject
from on_rails import Result, def_result

from configs import Configs, load_configs_from_yaml
from logger import create_logger
from run import run


def main():
    startup() \
        .on_success(lambda: run()) \
        .on_success_tee(lambda result: print(result)) \
        .on_fail_tee(lambda result: print(repr(result)))


@def_result()
def startup() -> Result:
    configs = load_configs_from_yaml('configs.yaml').on_fail_break_function().value
    logger = create_logger(configs.log).on_fail_break_function().value

    inject.configure(lambda binder: injector_configs(binder, configs, logger))
    return Result.ok()


def injector_configs(binder, configs: Configs, logger: logging.Logger):
    binder.bind(Configs, configs)
    binder.bind(logging.Logger, logger)


if __name__ == '__main__':
    main()
