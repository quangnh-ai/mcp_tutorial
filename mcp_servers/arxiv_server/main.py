from mcp.server.fastmcp import FastMCP
from tools import get_arxiv_papers

mcp = FastMCP(name="Arxiv")

mcp.add_tool(
    fn=get_arxiv_papers,
    name="get_arxiv_papers",
    description="Get arxiv papers based on a query",
)

if __name__ == "__main__":
    mcp.run(transport="sse")