 import asyncio

t = (6, 4, 2)
result = sum (t)

async def fir():
    print (t[0])
    await asyncio.sleep(5)
    print (result) 

async def sec():
    print (t[1])
    await asyncio.sleep(3)
    print (t[2])

loop = asyncio.get_event_loop()
tasks = [loop.create_task(fir()), loop.create_task(sec())]
wait_here = asyncio.wait(tasks)
loop.run_until_complete(wait_here)
loop.close()


import time 
import asyncio 

start = time.time() 


def tic():
    return 'at %1.1f seconds' % (time.time() - start) 


async def gr1():# it waits for 4 sec, but we don't want to stick around...
    print('gr1 started work: {}'.format(tic()))
    await asyncio.sleep(4)
    print('gr1 ended work: {}'.format(tic())) 


async def gr2(): 
# it waits for 4 sec, but we don't want to stick around... 
    print('gr2 started work: {}'.format(tic())) 
    await asyncio.sleep(4) 
    print('gr2 Ended work: {}'.format(tic())) 


async def gr3(): 
    print("Let's do some stuff while the coroutines are blocked, {}".format(tic()))
    await asyncio.sleep(1)
    print('doing...')
    await asyncio.sleep(3) 
    print("Done!") 


ioloop = asyncio.get_event_loop() 
tasks = [ 
ioloop.create_task(gr1()), 
ioloop.create_task(gr2()), 
ioloop.create_task(gr3()) 
] 
ioloop.run_until_complete(asyncio.wait(tasks)) 
ioloop.close()


# import random 
# from time import sleep 
# import asyncio 


# def task(pid):
#     """Synchronous non-deterministic task.""" 
#     sleep(random.randint(0,2) * 2) 
#     print('Task %s done' % pid) 


# async def task_coro(pid): 
#     """Coroutine non-deterministic task"""
#     await asyncio.sleep(random.randint(0,2) * 2) 
#     print('Task %s done' % pid) 


# def synchronous(): 
#     for i in range(1, 10):
#         task(i) 


# async def asynchronous(): 
#     tasks = [asyncio.ensure_future(task_coro(i)) for i in range(1, 10)] 
#     await asyncio.wait(tasks) 


# print('Synchronous:')
# synchronous() 

# ioloop = asyncio.get_event_loop()
# print('Asynchronous:') 
# ioloop.run_until_complete(asynchronous()) 
# ioloop.close()


# import time 
# import random 
# import asyncio 
# import aiohttp 

# URL = 'https://api.github.com/events' 
# MAX_CLIENTS = 3 


# async def fetch_async(pid):
#     start = time.time()
#     sleepy_time = random.randint(2, 5)
#     print('Fetch async process {} started, sleeping for {} seconds'.format(pid, sleepy_time))
    
#     await asyncio.sleep(sleepy_time)

#     response = await aiohttp.request('GET', URL)
#     datetime = response.headers.get('Date')
    
#     response.close()
#     return 'Process {}: {}, took: {:.2f} seconds'.format(pid, datetime, time.time() - start) 


# async def asynchronous():
#     start = time.time()
#     futures = [fetch_async(i) for i in range(1, MAX_CLIENTS + 1)]
#     for i, future in enumerate(asyncio.as_completed(futures)):
#         result = await future
#         print('{} {}'.format("»" * (i + 1), result))
        
#         print("Process took: {:.2f} seconds".format(time.time() - start)) 


# ioloop = asyncio.get_event_loop() 
# ioloop.run_until_complete(asynchronous()) 
# ioloop.close()
