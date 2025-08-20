# AI Code Assistant

This project is a command-line AI code assistant powered by the Gemini API. It allows you to ask coding questions and get answers directly in your terminal.

## Getting Started

### Prerequisites

*   Python 3.12 or higher
*   An API key for the Gemini API. You can get one from [Google AI Studio](https://aistudio.google.com/).

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/prateekkhenedcodes/aiagent.git
    cd aiagent
    ```

2.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    **Note:** A `requirements.txt` file needs to be generated from the `pyproject.toml` file.

3.  Create a `.env` file and add your Gemini API key:
    ```
    GEMINI_API_KEY="YOUR_API_KEY"
    ```

### Usage

To use the AI assistant, run the following command:

```bash
python main.py "Your question here"
```

For example:

```bash
python main.py "How do I create a virtual environment in Python?"
```

## Calculator

This project also includes a simple command-line calculator.

To use the calculator, run the following command:

```bash
python calculator/main.py "2 + 2 * 2"
```

The calculator will print the result in a formatted box.
