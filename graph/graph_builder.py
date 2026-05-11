from langgraph.graph import StateGraph, END

from graph.state import AgentState
from graph.nodes import summarize_node


def build_graph():

    workflow = StateGraph(AgentState)

    workflow.add_node("summarizer", summarize_node)

    workflow.set_entry_point("summarizer")

    workflow.add_edge("summarizer", END)

    return workflow.compile()