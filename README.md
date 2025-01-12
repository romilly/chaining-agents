# Chaining Agents

A lightweight implementation showing how to build AI agents by adapting patterns from Anthropic's cookbook to work with smaller, locally-running language models.

## Overview

This project demonstrates how to create simple but effective AI agents using local LLMs. It includes a complete implementation of:
- A flexible Tool system for function specifications
- An LLM wrapper for model interaction
- A simple chaining mechanism for sequential operations

The example application automatically adds documentation and type hints to Python code.

## Requirements

- Python 3.10 or higher
- Ollama (for running local LLMs)

## Installation

1. First, install Ollama for your operating system:
   - Linux: Follow instructions at [Ollama Installation](https://github.com/ollama/ollama)
   - MacOS/Windows: Currently untested, but should work following Ollama's installation guidelines

2. Clone this repository:
   ```bash
   git clone https://github.com/romilly/chaining-agents.git
   cd chaining-agents
   ```

3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/MacOS
   # or
   .\venv\Scripts\activate  # On Windows
   ```

4. Install the required Python package:
   ```bash
   pip install -r requirements.txt
   ```

5. Pull the required model:
   ```bash
   ollama pull qwen2.5
   ```

## Usage

Under Linux, you can run the example by:
```bash
cd chaining
chmod a+x run.py
./run.py
```

This will process a sample Python file, adding comprehensive documentation and type hints,
printing out the new file and saving it as `commented.py`.

For other operating systems, you should be able to run:
```bash
python run.py
```

## Example

Input Python file:
```python
import ollama

def embed(text):
    try:
        embedding = ollama.embeddings(
        model='nomic-embed-text',
        prompt=text
        )
        result = embedding['embedding']
    except Exception:
        print(f"Could not embed text: {text}")
        result = None
    return result
```

After processing, you get:
```python
import ollama  # Import the necessary library

def embed(text: str) -> any:
    """
    Function to embed a given text into an embedding vector.

    Parameters:
        text (str): The input text to be embedded.

    Returns:
        Any: The resulting embedding or None if an error occurs.
    """
    try:
        # Attempt to get the embedding for the provided text using the 'nomic-embed-text' model
        embedding = ollama.embeddings(
            model='nomic-embed-text',  # Specify the model name
            prompt=text  # Provide the input text as a prompt
        )

        # Extract the actual embedding vector from the response
        result = embedding['embedding']
    except Exception:
        # If an error occurs during the process, print an error message and return None
        print(f"Could not embed text: {text}")
        result = None

    # Return the resulting embedding or None if an error occurred
    return result
```

## Contributing

Contributions are welcome! Here are some ways you can contribute:

1. **Testing on Different Platforms**: Help verify and document the setup process for Windows and MacOS.
2. **Testing with Different Models**: Try the code with other local LLMs and report your findings.
3. **Bug Reports**: If you find a bug, please open an issue with:
   - A clear description of the problem
   - Steps to reproduce
   - Expected vs actual behavior
   - Your operating system and Python version
4. **Feature Requests**: Open an issue to suggest new features or improvements.
5. **Code Contributions**: Submit pull requests for:
   - Bug fixes
   - New features
   - Documentation improvements
   - Additional examples

Please:
- Write clear, descriptive commit messages
- Follow the existing code style
- Add/update tests if relevant
- Update documentation as needed

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Based on patterns from [Anthropic's Cookbook](https://github.com/anthropics/anthropic-cookbook)
- Uses [Ollama](https://github.com/ollama/ollama) for local LLM deployment
