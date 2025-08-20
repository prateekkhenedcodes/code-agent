# GEMINI.md

## Project Status

**State:** Functional with some issues.

This project is a proof-of-concept demonstrating a CLI AI assistant and a simple calculator. The core functionalities are working. However, there are known issues:
- The root `tests.py` is broken and references a non-existent module.
- The `gemini` file in the root is an unnecessary HTML redirect and should be removed.
- The project lacks automated testing, a consistent code style, and contribution guidelines.

## Project Overview

This project contains two primary command-line applications:
1.  **AI Code Assistant:** A CLI tool that sends user prompts to the Gemini API and streams the response.
2.  **Calculator:** A simple CLI expression evaluator.

The project is written in Python and structured as follows:

-   `main.py`: The entry point for the AI assistant. It uses the `gemini-2.0-flash-001` model.
-   `calculator/`: Contains the calculator application (`main.py`), its core logic (`pkg/calculator.py`), and a comprehensive test suite (`tests.py`).
-   `functions/`: Contains helper functions for file system operations with built-in security checks.
-   `config.py`: A configuration file, currently used to define `MAX_CHARS` for file reading.
-   `pyproject.toml`: Defines project metadata and dependencies.

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

The project uses the `unittest` framework.

-   **Calculator Tests:** The calculator tests are in `calculator/tests.py` and are fully functional. They can be run directly:
    ```bash
    python calculator/tests.py
    ```
-   **Root Tests:** The `tests.py` file in the root directory is **broken** as it tries to import a non-existent module (`functions.write_file_content`).

**TODO:** It is recommended to use a test runner like `pytest` to automatically discover and run all tests.

### Code Style

The project does not currently enforce a specific code style.
**TODO:** It is recommended to use a code formatter like `black` to ensure a consistent style.

### Contribution Guidelines

There are no contribution guidelines at the moment.
**TODO:** It is recommended to create a `CONTRIBUTING.md` file with instructions for contributors.