from dataclasses import dataclass
from typing import Callable, List, Type, Optional, Dict, Any, Union
import inspect


@dataclass
class Parameter:
    name: str
    type: Type
    optional: bool

    def _get_type_string(self) -> str:
        """Convert Python types to JSON schema type strings."""
        type_map = {
            int: "integer",
            float: "number",
            str: "string",
            bool: "boolean",
            list: "array",
            dict: "object"
        }
        # Get the base type (handles Optional types)
        base_type = getattr(self.type, "__origin__", self.type)
        if base_type in (Optional, Union):
            # Get the first non-None type argument
            types = [t for t in self.type.__args__ if t != type(None)]
            if types:
                base_type = types[0]

        return type_map.get(base_type, "string")


@dataclass
class Tool:
    name: str
    function: Callable
    description: str
    parameters: List[Parameter]

    def to_spec(self) -> Dict[str, Any]:
        """Extract an Ollama-style function specification from the Tool."""
        # Build properties dictionary
        properties = {}
        required = []

        for param in self.parameters:
            properties[param.name] = {
                "type": param._get_type_string()
            }

            if not param.optional:
                required.append(param.name)

        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": {
                    "type": "object",
                    "properties": properties,
                    "required": required
                }
            }
        }

    @classmethod
    def from_function(cls, func: Callable) -> 'Tool':
        """Create a tool from a Python function."""

        # Get the docstring and extract first line
        doc = inspect.getdoc(func) or ""
        description = doc.split('\n')[0].strip()

        # Get function signature and parameters
        signature = inspect.signature(func)
        parameters = []

        for name, param in signature.parameters.items():
            # Check if parameter is optional (has default value)
            optional = param.default is not param.empty

            # Get parameter type, use Any if not specified
            param_type = param.annotation if param.annotation is not param.empty else type(None)

            # Create Parameter object
            parameters.append(Parameter(
                name=name,
                type=param_type,
                optional=optional
            ))

        return cls(
            name=func.__name__,
            function=func,
            description=description,
            parameters=parameters
        )