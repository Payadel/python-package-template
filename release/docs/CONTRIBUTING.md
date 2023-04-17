## Development environment setup

To set up a development environment, please follow these steps:

1. Clone the repo

   ```sh
   git clone https://github.com/USER_NAME/REPO
   ```

2.install `poetry`:

```shell
python -m pip install poetry
poetry install
```

3. install python requirements:

```shell
pip install -r requirements
```

4. Run `tox` to ensure everything is ok:

```shell
tox
```