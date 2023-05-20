import logging

import inject
from on_rails import Result, def_result

from configs import Configs, load_configs_from_yaml
from logger import create_logger
from run import run


def main():
    """
    The main function is the entry point for this program.
    """
    startup() \
        .on_success(lambda: run()) \
        .on_success_tee(lambda result: print(result)) \
        .on_fail_tee(lambda result: print(repr(result)))


@def_result()
def startup() -> Result:
    """
    The startup function is called by the main function to configure the application.
    It loads configuration from a YAML file, creates a logger, and configures dependency injection.
    """
    configs = load_configs_from_yaml('configs.yaml').on_fail_break_function().value
    logger = create_logger(configs.log).on_fail_break_function().value

    inject.configure(lambda binder: injector_configs(binder, configs, logger))
    return Result.ok()


def injector_configs(binder, configs: Configs, logger: logging.Logger):
    """
    The injector_configs function is a helper function that binds the Configs and logging.Logger objects to the injector
    so that they can be injected into other classes. This allows us to use these objects in our code without having to
    pass them around as parameters.
    """
    binder.bind(Configs, configs)
    binder.bind(logging.Logger, logger)


if __name__ == '__main__':
    main()
