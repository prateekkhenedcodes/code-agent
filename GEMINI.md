# GEMINI.md

## Project Status

**State:** Functional.

This project is a proof-of-concept demonstrating a CLI AI assistant and a simple calculator. The core functionalities are working.

## Project Overview

This project contains two primary command-line applications:
1.  **AI Code Assistant:** A CLI tool that sends user prompts to the Gemini API and streams the response.
2.  **Calculator:** A simple CLI expression evaluator.

The project is written in Python and structured as follows:

-   `main.py`: The entry point for the AI assistant. It uses the `gemini-2.0-flash-001` model.
-   `calculator/`: Contains the calculator application (`main.py`), its core logic (`pkg/calculator.py`), and a comprehensive test suite (`tests.py`).
-   `functions/`: Contains helper functions for file system operations with built-in security checks.
    - `get_file_content.py`: Reads and returns the content of a specified file.
    - `get_files_info.py`: Lists files in the specified directory along with their sizes.
    - `run_python.py`: Executes a Python file and returns the output.
    - `write_file_content.py`: Writes content to a file.
-   `config.py`: A configuration file, currently used to define `MAX_CHARS` for file reading and `WORKING_DIR` for the AI assistant.
-   `pyproject.toml`: Defines project metadata and dependencies.
-   `prompts.py`: Contains the system prompt for the AI assistant.
-   `call_function.py`: Maps function calls from the Gemini API to the actual Python functions.
-   `tests.py`: A script to run some tests for the `functions` modules.

## Building and Running

### Dependencies

The project uses [uv](https://github.com/astral-sh/uv) for package management. The dependencies are defined in `pyproject.toml`.

To install the dependencies, run:
```bash
uv pip install -r requirements.txt
```

You can generate the `requirements.txt` file from `pyproject.toml` with the following command:
```bash
uv pip freeze > requirements.txt
```

### Running the AI Code Assistant

To run the AI code assistant, you need a Gemini API key from [Google AI Studio](https://aistudio.google.com/).

1.  Create a `.env` file in the root of the project:
    ```
    GEMINI_API_KEY="YOUR_API_KEY"
    ```
2.  Run the assistant from the command line:
    ```bash
    python main.py "Your prompt here"
    ```
    Use the `--verbose` flag for more details on API usage.

### Running the Calculator

To run the calculator, execute the `main.py` file in the `calculator` directory:
```bash
python calculator/main.py "3 + 5"
```

## Development Conventions

### Testing

The project uses the `unittest` framework for the calculator.

-   **Calculator Tests:** The calculator tests are in `calculator/tests.py` and are fully functional. They can be run directly:
    ```bash
    python calculator/tests.py
    ```
-   **Root Tests:** The `tests.py` file in the root directory is a simple script to test the `functions` modules.

**TODO:** It is recommended to use a test runner like `pytest` to automatically discover and run all tests.

### Code Style

The project does not currently enforce a specific code style.
**TODO:** It is recommended to use a code formatter like `black` to ensure a consistent style.

### Contribution Guidelines

There are no contribution guidelines at the moment.
**TODO:** It is recommended to create a `CONTRIBUTING.md` file with instructions for contributors.
