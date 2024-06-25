def count_lines_words_characters(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = 0
            num_characters = 0
            for line in lines:
                words = line.split()
                num_words += len(words)
                num_characters += len(line)
        
        print("Number of lines:", num_lines)
        print("Number of words:", num_words)
        print("Number of characters:", num_characters)

    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except Exception as e:
        print("An error occurred:", e)


file_path = 'sample.txt'  
count_lines_words_characters(file_path)
