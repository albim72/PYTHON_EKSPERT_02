import asyncio

async def function_async():
    for i in range(5):
        print("kod dostępu A:")
        print(5834589458)
    return 0

loop = asyncio.get_event_loop()
loop.run_until_complete(function_async())

print("_________________________________________")

async def function_a2():
    for i in range(100000):
        if i%50000 == 0:
            print("kod dostępu B:")
            print(976842)
            await asyncio.sleep(0.01)
    return 0

async def function_b2():
    print("\n druga opcja ABC\n")
    return 0

async def main():
    f1 = loop.create_task(function_a2())
    f2 = loop.create_task(function_b2())
    await asyncio.wait([f1,f2])

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
