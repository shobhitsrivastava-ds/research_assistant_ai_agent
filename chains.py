from pydantic import BaseModel
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from llm import llm
from prompts import writer_prompt, critic_prompt
from tools import search_tool

class CritiqueResult(BaseModel):
    critique: str
    verdict: bool

critic_parser= PydanticOutputParser(
    pydantic_object= CritiqueResult
)

research_chain = RunnablePassthrough.assign(
    search_result=RunnableLambda(lambda x: search_tool.invoke(x["question"]))
)

writer_chain= (
    RunnablePassthrough() | writer_prompt | llm
)

critic_chain= (
    RunnablePassthrough() | critic_prompt | llm | critic_parser
)