import asyncio
import aiohttp
import blog_spider

##Э�̣��ڳ���ѭ��������ܵĺ������������첽IO��ִ��async_craw����
async def async_craw(url):
    print("craw url: ", url)
    ##async with��������
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            ##resp.text()��ȡ���
            result = await resp.text()
            print(f"craw url: {url}, {len(result)}")

##����ѭ��
loop = asyncio.get_event_loop()

##ʹ��Э�̺�������һ��list
tasks = [
    loop.create_task(async_craw(url))
    for url in blog_spider.urls]

import time

start = time.time()
##�ȴ�tasks���
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print("use time seconds: ", end - start)
