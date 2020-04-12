import requests

proxies = {"http": 'http://127.0.0.1:8080', "https": 'http://127.0.0.1:8080'}

url = 'http://api.ipstack.com/check?access_key=188a74277248ac005c6b1d4b640e30ff'
# url = 'https://baidu.com'

rep = requests.get(url, proxies=proxies, timeout=5, verify=False)
print(rep.text)

# rep = requests.post(url, json={}, proxies=proxies, verify=False)
# print(rep.text)

# import aiohttp
# import asyncio
# import ssl
# import certifi

# sslcontext = ssl.create_default_context(cafile=certifi.where())

# async def fetch(session, url):
#     async with session.get(url, ssl=sslcontext) as response:
#         return await response.read()

# async def main():
#     async with aiohttp.ClientSession() as session:
#         async with session.request('CONNECT', 'https://zhuanlan.zhihu.com/p/30422195', data=None, ssl=sslcontext) as response:
#             body = await response.read()
#             return body

# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     print(loop.run_until_complete(main()))
#     print(loop.run_until_complete(main()))