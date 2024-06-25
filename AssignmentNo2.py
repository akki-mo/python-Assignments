import json

def json_to_dict(json_file):
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
    except Exception as e:
        print("An error occurred:", e)


json_file = 'data.json'
result_dict = json_to_dict(json_file)
if result_dict:
    print("JSON file converted to Python dictionary successfully:")
    print(result_dict)
