# GEMINI.md

## Project Overview

This project is a command-line AI code assistant that uses the Gemini API. It allows users to interact with the Gemini large language model from their terminal. The project also includes a simple command-line calculator application.

The project is written in Python and uses the `google-genai` library to interact with the Gemini API. It is structured into three main parts:

*   **AI Code Assistant:** The main entry point for the AI assistant is `main.py`. It takes a user prompt as a command-line argument and prints the response from the AI model.
*   **Calculator:** The calculator is a separate application located in the `calculator` directory. It can evaluate mathematical expressions from the command line.
*   **Helper Functions:** The `functions` directory contains helper functions for reading file content and getting file information.

## Building and Running

### Dependencies

The project uses [uv](https://github.com/astral-sh/uv) for package management. The dependencies are listed in the `pyproject.toml` file and locked in `uv.lock`.

To install the dependencies, run the following command:

```bash
uv pip install -r requirements.txt
```

**TODO:** Create a `requirements.txt` file from `pyproject.toml`.

### Running the AI Code Assistant

To run the AI code assistant, you need to have a Gemini API key. You can get one from the [Google AI Studio](https://aistudio.google.com/).

Once you have your API key, create a `.env` file in the root of the project and add the following line:

```
GEMINI_API_KEY="YOUR_API_KEY"
```

Then, you can run the AI assistant from the command line:

```bash
python main.py "Your prompt here"
```

You can also use the `--verbose` flag to get more information about the API usage:

```bash
python main.py "Your prompt here" --verbose
```

### Running the Calculator

To run the calculator, you can execute the `main.py` file in the `calculator` directory:

```bash
python calculator/main.py "3 + 5"
```

## Development Conventions

### Testing

The project uses the `unittest` framework for testing. The tests for the calculator are located in `calculator/tests.py`. The tests for the helper functions are in `tests.py`.

To run the tests, you can execute the test files directly:

```bash
python calculator/tests.py
python tests.py
```

**TODO:** It is recommended to use a test runner like `pytest` to automatically discover and run all tests.

### Code Style

The project does not currently enforce a specific code style. It is recommended to use a code formatter like `black` to ensure a consistent style.

### Contribution Guidelines

There are no contribution guidelines at the moment. It is recommended to create a `CONTRIBUTING.md` file with instructions for contributors.
