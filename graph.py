from langgraph.graph import StateGraph, END
from const import MAX_ITERS
from state import AgentState
from nodes import research_node, critic_node, writer_node

graph= StateGraph(AgentState)
graph.add_node("research", research_node)
graph.add_node("write", writer_node)
graph.add_node("critic", critic_node)

graph.set_entry_point("research")
graph.add_edge("research", "write")
graph.add_edge("write", "critic")

def should_continue(state: AgentState):
    if state["is_good"]:
        return END
    if state["iteration"] >= MAX_ITERS:
        return END
    return "research"

graph.add_conditional_edges(
    "critic",
    should_continue
)

app= graph.compile()