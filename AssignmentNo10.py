def open_file(file_path):
    try:
        with open(file_path, 'r') as file:
            print("File content:")
            print(file.read())
    except FileNotFoundError:
        print("Error: File not found. Please provide a valid file path.")
    except Exception as e:
        print("An error occurred:", e)


file_path = 'demo.txt'  
open_file(file_path)
