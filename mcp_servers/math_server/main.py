from mcp.server.fastmcp import FastMCP

from tools.math import subtract, add, multiply, divide
from prompts import prompt_dummy, prompt_greeting

mcp = FastMCP("math")

mcp.add_tool(fn=subtract, name="subtract", description="Subtract two numbers")
mcp.add_tool(fn=add, name="add", description="Add two numbers")
mcp.add_tool(fn=multiply, name="multiply", description="Multiply two numbers")
mcp.add_tool(fn=divide, name="divide", description="Divide two numbers")

mcp.add_prompt(fn=prompt_dummy, name="dummy", description="A dummy prompt")
mcp.add_prompt(fn=prompt_greeting, name="greeting", description="A greeting prompt")

if __name__ == "__main__":
    mcp.run(transport='sse')
