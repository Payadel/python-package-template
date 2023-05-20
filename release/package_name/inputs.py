import argparse

from on_rails import def_result, Result


class Inputs:
    name: str

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')


@def_result()
def get_inputs() -> Result[Inputs]:
    """
    The get_inputs function parses the command line arguments and returns an Inputs object.

    :return: An object of type inputs
    """
    parser = argparse.ArgumentParser(description='Python CLI App')
    parser.add_argument('name', type=str, help='Name')
    args = parser.parse_args()

    return Result.ok(Inputs(**vars(args)))
