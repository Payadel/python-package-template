from typing import Optional

import requests
from requests import Session


class Proxy:
    host: str
    port: int

    def __init__(self, proxy_host: str, proxy_port: int):
        self.host = proxy_host
        self.port = proxy_port


def get_request_session(proxy: Optional[Proxy] = None) -> Session:
    # Create a session and configure the proxy
    request_session = requests.session()
    if proxy:
        request_session.proxies = {
            'http': f'socks5h://{proxy.host}:{proxy.port}',
            'https': f'socks5h://{proxy.host}:{proxy.port}'
        }
    return request_session
