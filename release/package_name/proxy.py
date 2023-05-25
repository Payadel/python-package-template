# Set the proxy information
import requests

proxy_host = '127.0.0.1'  # The Tor proxy IP address
proxy_port = 9050  # The Tor proxy port (default is usually 9050)

# Create a session and configure the proxy
request_session = requests.session()
request_session.proxies = {
    'http': f'socks5h://{proxy_host}:{proxy_port}',
    'https': f'socks5h://{proxy_host}:{proxy_port}'
}
