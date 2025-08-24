# AI Code Assistant & Calculator

Welcome to the AI Code Assistant. This project provides two command-line tools: an AI-powered code assistant using the Gemini API and a simple expression evaluator.

## Features

-   **AI Code Assistant:**
    -   Get help with your coding questions directly from your terminal.
    -   Powered by the Gemini API.
    -   Can list files, read file contents, execute Python files, and write files.
-   **Calculator:**
    -   A simple command-line calculator that evaluates mathematical expressions.
    -   Supports addition, subtraction, multiplication, and division.
    -   Handles operator precedence.

## Project Structure

```
├── calculator
│   ├── main.py
│   ├── pkg
│   │   ├── calculator.py
│   │   └── render.py
│   └── tests.py
├── functions
│   ├── get_file_content.py
│   ├── get_files_info.py
│   ├── run_python.py
│   └── write_file_content.py
├── main.py
├── call_function.py
├── prompts.py
├── config.py
├── pyproject.toml
├── requirements.txt
└── README.md
```

-   `main.py`: The entry point for the AI code assistant.
-   `calculator/`: The directory for the calculator application.
-   `functions/`: Helper functions for file system operations.
-   `prompts.py`: The system prompt for the AI assistant.
-   `config.py`: Configuration for the project.
-   `call_function.py`: Maps API calls to Python functions.

## Getting Started

### Prerequisites

-   Python 3.12 or higher
-   A Gemini API key from [Google AI Studio](https://aistudio.google.com/).

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/prateekkhenedcodes/aiagent.git
    cd aiagent
    ```

2.  **Install the dependencies:**

    The project uses `uv` for package management. The dependencies are defined in `pyproject.toml`.

    ```bash
    uv pip install -r requirements.txt
    ```

    You can generate the `requirements.txt` file from `pyproject.toml` with the following command:

    ```bash
    uv pip freeze > requirements.txt
    ```

3.  **Set up your API key:**

    Create a `.env` file in the root of the project and add your Gemini API key:

    ```
    GEMINI_API_KEY="YOUR_API_KEY"
    ```

## Usage

### AI Code Assistant

To ask the AI assistant a question, run the following command:

```bash
uv run main.py "Your question here"
```

For example:

```bash
uv run main.py "How do I create a virtual environment in Python?"
```

Use the `--verbose` flag for more details on API usage.


## Testing

The project uses the `unittest` framework for the calculator.

-   **Calculator Tests:** The calculator tests are in `calculator/tests.py` and are fully functional. They can be run directly:

    ```bash
    python calculator/tests.py
    ```

-   **Root Tests:** The `tests.py` file in the root directory is a simple script to test the `functions` modules.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
