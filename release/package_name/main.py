import logging
import sys

import inject
from on_rails import Result, def_result
from package_name.configs import Configs, load_configs_from_yaml
from package_name.inputs import Inputs, get_inputs
from package_name.logger import create_logger
from run import run
from sqlalchemy.orm import Session


def main():
    """
    The main function is the entry point for this program.
    """
    res = startup() \
        .on_success(lambda: run()) \
        .on_success_tee(lambda result: print(result)) \
        .on_fail_tee(lambda result: print(repr(result)))

    sys.exit(0 if res.success else res.code())


@def_result()
def startup() -> Result:
    """
    The startup function is called by the main function to configure the application.
    It loads configuration from a YAML file, creates a logger, and configures dependency injection.
    """
    configs = load_configs_from_yaml('configs.yaml').on_fail_break_function().value
    inputs = get_inputs().on_fail_break_function().value
    logger = create_logger(configs.log).on_fail_break_function().value

    inject.configure(lambda binder: injector_configs(binder, configs, logger, inputs))
    return Result.ok()


def injector_configs(binder, configs: Configs, logger: logging.Logger, inputs: Inputs):
    """
    The injector_configs function is a helper function that binds the Configs and logging.Logger objects to the injector
    so that they can be injected into other classes. This allows us to use these objects in our code without having to
    pass them around as parameters.
    """
    binder.bind(Configs, configs) \
        .bind(logging.Logger, logger) \
        .bind(Inputs, inputs)


if __name__ == '__main__':
    main()
