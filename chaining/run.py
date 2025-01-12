#!/usr/bin/env python
# coding: utf-8

# Chaining technique adapted from https://github.com/anthropics/anthropic-cookbook/blob/main/patterns/agents/basic_workflows.ipynb

from typing import List

from llm import LLM
from tool import Tool


def read_file(path_to_file: str) -> str:
    with open(path_to_file) as f:
        return f.read()

def write_file(path_to_file: str, content: str) -> None:
    with open(path_to_file, "w") as f:
        f.write(content)
    return f"content written to {path_to_file}"


# Create Tool instance and get specification
read_tool = Tool.from_function(read_file)
write_tool = Tool.from_function(write_file)

llm = LLM(model="qwen2.5")

def chain(input: str, prompts: List[str]) -> str:
    """Chain multiple LLM calls sequentially, passing results between steps."""
    result = input
    for prompt in prompts:
        print(prompt)
        full_prompt = f"{prompt}\nInput: {result}"
        result = llm.ask(full_prompt, tools=[read_tool, write_tool])
    return result

if __name__ == "__main__":
    chain("embed.py",
               ["Read the content of the file whose name is in the Input.",
               "Add comments and annotations to the code in the Input.",
                "Save the code in the Input as commented.py"])
    print(read_file("commented.py"))

