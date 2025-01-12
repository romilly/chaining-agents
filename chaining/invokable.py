from abc import ABC, abstractmethod
from typing import Dict, Optional


class Invokable(ABC):
    def __init__(self, data: Optional[Dict]=None):
        if data is None:
            data = {"messages": []}
        self.data = data

    @abstractmethod
    def invoke(self, data: Optional[Dict], tools: Optional[Dict]) -> Dict:
        pass

    def ask(self, prompt: str, data=None, tools=None) -> str:
        if data is not None:
            self.data = data
        self.data["messages"].append({"role": "user", "content": prompt})
        self.invoke(self.data, tools)
        return self.data['messages'][-1]['content']





