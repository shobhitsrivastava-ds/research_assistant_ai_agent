from pydantic import BaseModel
from typing import List

class AgentState(BaseModel):
    question: str
    research_notes: List[str]
    draft: str
    critique: str
    is_good: bool
    iteration: int