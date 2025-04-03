from mcp.server.fastmcp import FastMCP
from tools import get_wikipedia_summary

mcp = FastMCP(name="Wikipedia")

mcp.add_tool(
    fn=get_wikipedia_summary,
    name="get_wikipedia_summary",
    description="Get Wikipedia summary based on a query",
)

if __name__ == "__main__":
    mcp.run(transport="sse")