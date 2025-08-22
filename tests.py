from functions.run_python import run_python_file

print("--- Running test: calculator/main.py ---")
print(run_python_file("calculator", "main.py"))
print("\n--- Running test: calculator/main.py with args ---")
print(run_python_file("calculator", "main.py", ["3 + 5"]))
print("\n--- Running test: calculator/tests.py ---")
print(run_python_file("calculator", "tests.py"))
print("\n--- Running test: ../main.py (error case) ---")
print(run_python_file("calculator", "../main.py"))
print("\n--- Running test: nonexistent.py (error case) ---")
print(run_python_file("calculator", "nonexistent.py"))

