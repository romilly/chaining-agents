from typing import Dict, Optional
from ollama import chat

from invokable import Invokable
from tool import Tool


class LLM(Invokable):
    def __init__(self, model: str = "llama3.1"):
        super().__init__()
        self._model = model

    def invoke(self, data: Optional[Dict[str, Tool]], tools) -> Optional[Dict]:
        args = {"messages": data["messages"]}
        td = {}
        if tools:
            args["tools"] = [tool.to_spec() for tool in tools]
            for tool in tools:
                td[tool.name] = tool
        result = chat(self._model, **args)
        message = result["message"]
        if "tool_calls" in message:
            for tool in message["tool_calls"]:
                name = tool["function"]["name"]
                function = td.get(name).function
                args = tool["function"]["arguments"]
                result = function(**args)
                message = {
                    "role": "tool",
                    "content": result
                }
        data["messages"].append(message)
        return data


