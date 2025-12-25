from state import AgentState
from chains import research_chain, writer_chain, critic_chain

def research_node(state: AgentState) -> AgentState:
    result = research_chain.invoke(state)

    return AgentState(
        question= state["question"],
        research_notes= state["research_notes"] + [result["search_result"]],
        draft= state["draft"],
        critique= state["critique"],
        is_good= state["is_good"],
        iteration= state["iteration"]
    )


def writer_node(state: AgentState) -> AgentState:
    draft= writer_chain.invoke(state)

    return AgentState(
        question=  state["question"],
        research_notes=  state["research_notes"],
        draft= draft.content,
        critique= state["critique"],
        is_good= state["is_good"],
        iteration= state["iteration"]
    )

def critic_node(state: AgentState) ->AgentState:
    result= critic_chain.invoke(state)

    return AgentState(
        question= state["question"],
        research_notes=  state["research_notes"],
        draft=  state["draft"],
        critique= result.critique,
        is_good=  result.verdict,
        iteration= state["iteration"]+1
    )