from mcp import ClientSession
from mcp.client.sse import sse_client

async def run():
    async with sse_client(url="http://localhost:9000/sse") as streams:
        async with ClientSession(*streams) as session:
            await session.initialize()
            tools = await session.list_tools()
            print('*' * 10)
            print(tools)
            print('*' * 10)
            result = await session.call_tool("get_arxiv_papers", arguments={"query": "attention is all you need"})
            print(result.content[0].text)

if __name__ == "__main__":
    import asyncio
    asyncio.run(run())