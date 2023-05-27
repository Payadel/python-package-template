import os.path

import yaml
from on_rails import Result, def_result
from on_rails.ResultDetails.Success.WarningDetail import WarningDetail
from package_name.logger import LogConfigs
from pydantic import BaseModel


class ProxyConfigs(BaseModel):
    disable = False
    host = '127.0.0.1'
    port = 9050


class Configs(BaseModel):
    log: LogConfigs
    proxy: ProxyConfigs


@def_result()
def load_configs_from_yaml(file_path: str) -> Result[Configs]:
    """
    Loads the configs from a yaml file.

    :param file_path: str: Specify the file path of the configs
    :return: A result with value Configs
    """
    if not os.path.isfile(file_path):
        return Result.ok(Configs(), WarningDetail(f"Can not find config file in {file_path}"))

    with open(file_path, "r") as file:
        config_data = yaml.safe_load(file)

    configs = Configs(**config_data)
    return Result.ok(configs)
