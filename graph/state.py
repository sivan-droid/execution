from typing import TypedDict


class AgentState(TypedDict):
    input_text: str
    summary: str