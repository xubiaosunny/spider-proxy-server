from mitmproxy import http, ctx
from mitmproxy.script import concurrent
import typing

# This scripts demonstrates how mitmproxy can switch to a second/different upstream proxy
# in upstream proxy mode.
#
# Usage: mitmdump -U http://default-upstream-proxy.local:8080/ -s change_upstream_proxy.py
#
# If you want to change the target server, you should modify flow.request.host and flow.request.port


def proxy_address(flow: http.HTTPFlow) -> typing.Tuple[str, int]:
    # Poor man's loadbalancing: route every second domain through the alternative proxy.
    ctx.log.info(f'----proxy')
    return ("108.61.178.121", 20003)


def request(flow: http.HTTPFlow) -> None:
    if flow.request.method == "CONNECT":
        # If the decision is done by domain, one could also modify the server address here.
        # We do it after CONNECT here to have the request data available as well.
        return
    address = proxy_address(flow)
    if flow.live:
        flow.live.change_upstream_proxy_server(address)


def response(flow):
    ctx.log.info(f'{flow.response.status_code}')


def error(flow):
    ctx.log.error(f'{flow.error}')
    ctx.log.info(f'{flow.server_conn.address}')
