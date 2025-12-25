from langchain_core.tools import Tool

from tavily import TavilyClient

tavily= TavilyClient()

def web_search(query: str) -> str:
    result= tavily.search(query= query, max_results= 5)

    return str(result)

search_tool= Tool(
    name= "web_Search",
    func= web_search,
    description="Search the web for up-to-date factual information"
)