from mitmproxy import http, ctx
from mitmproxy.script import concurrent
import typing

from proxy.base import LocalProxy

# This scripts demonstrates how mitmproxy can switch to a second/different upstream proxy
# in upstream proxy mode.
#
# Usage: mitmdump -U http://default-upstream-proxy.local:8080/ -s change_upstream_proxy.py
#
# If you want to change the target server, you should modify flow.request.host and flow.request.port

local_proxy = LocalProxy()


ctx.log.info(f'proxy address count is : {local_proxy.count()}')


def proxy_address(flow: http.HTTPFlow) -> typing.Tuple[str, int]:
    # Poor man's loadbalancing: route every second domain through the alternative proxy.
    global local_proxy
    address = local_proxy.get()
    ctx.log.info(f'proxy address is: {address}')
    return address.split(':')


def request(flow: http.HTTPFlow) -> None:
    if flow.request.method == "CONNECT":
        # If the decision is done by domain, one could also modify the server address here.
        # We do it after CONNECT here to have the request data available as well.
        return

    address = proxy_address(flow)
    if flow.live and address:
        flow.live.change_upstream_proxy_server(address)


# def response(flow):
#     ctx.log.info(f'{flow.response.status_code}')


def error(flow):
    ctx.log.error(f'{flow.error}')
    ctx.log.info(f'{flow.server_conn.address}')
    global local_proxy
    local_proxy.delete(':'.join(flow.server_conn.address))
