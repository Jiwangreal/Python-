import asyncio
import aiohttp
import blog_spider

##协程：在超级循环里可以跑的函数，就是在异步IO中执行async_craw函数
async def async_craw(url):
    print("craw url: ", url)
    ##async with创建对象
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            ##resp.text()获取结果
            result = await resp.text()
            print(f"craw url: {url}, {len(result)}")

##超级循环
loop = asyncio.get_event_loop()

##使用协程函数定义一个list
tasks = [
    loop.create_task(async_craw(url))
    for url in blog_spider.urls]

import time

start = time.time()
##等待tasks完成
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print("use time seconds: ", end - start)
