import uvicorn
from fastapi import FastAPI
from typing import List, Union

import config
from utils.format import Format
from mtypes import *
from functions import _get_local_address

_format = Format()

APP = FastAPI()


class Server:
    def __init__(self, config: dict, **kwargs: object) -> None:

        if config is None:
            raise ValueError("Config is required")

        self._host: str = ""
        self._port: Union[str, int] = ""

        self.__configurate__(config=config)
        if kwargs is None:
            kwargs = {}

    def __configurate__(self, config: dict) -> None:
        local_address = _get_local_address()
        self.host = config.get("host", local_address[0])
        self.port = config.get("port", local_address[1])

    @property
    def host(self) -> str:
        return self._host

    @host.setter
    def host(self, value: str) -> None:
        @_format.host
        def setter(value: str) -> None:
            self._host = value

        if not isinstance(value, str):
            raise ValueError("Host must be a string")
        else:
            setter(value)

    @property
    def port(self) -> Union[str, int]:
        return self._port

    @port.setter
    def port(self, value: Union[str, int]) -> None:
        @_format.port
        def setter(value: Union[str, int]) -> None:
            self._port = value

        if not isinstance(value, str) and not isinstance(value, int):
            raise ValueError("Port must be a string or int")
        else:
            setter(value)

    def run(self) -> None:
        if self.host is None or self.port is None:
            raise ValueError("Host and Port are required")

        uvicorn.run(APP, host=self.host, port=int(self.port))

    @staticmethod
    @APP.get("/")
    async def index():
        return {"message": "Hello World"}
