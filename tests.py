from functions.get_file_content import get_file_content

def test():
    # Test case 1
    result1 = get_file_content("calculator", "main.py")
    print(result1)
    
    # Test case 2  
    result2 = get_file_content("calculator", "pkg/calculator.py")
    print(result2)
    
    # Test case 3
    result3 = get_file_content("calculator", "/bin/cat")
    print(result3)
    
    # Test case 4
    result4 = get_file_content("calculator", "pkg/does_not_exist.py")
    print(result4)

if __name__ == "__main__":
    test()