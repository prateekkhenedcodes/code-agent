from functions.get_files_info import get_files_info

def test():
    # Test case 1
    print("Result for current directory:")
    result1 = get_files_info("calculator", ".")
    print(result1)
    
    # Test case 2  
    print("Result for 'pkg' directory:")
    result2 = get_files_info("calculator", "pkg")
    print(result2)
    
    # Test case 3
    print("Result for '/bin' directory:")
    result3 = get_files_info("calculator", "/bin")
    print(result3)
    
    # Test case 4
    print("Result for '../' directory:")
    result4 = get_files_info("calculator", "../")
    print(result4)

if __name__ == "__main__":
    test()