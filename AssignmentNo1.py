import csv

def extract_columns(input_file, output_file, columns):
    try:
        with open(input_file, 'r', newline='') as infile:
            reader = csv.reader(infile)
            extracted_data = []
            for row in reader:
                extracted_row = [row[col] for col in columns]
                extracted_data.append(extracted_row)

        with open(output_file, 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(extracted_data)

        print("Extraction successful. Output written to", output_file)

    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except Exception as e:
        print("An error occurred:", e)


input_file = 'akinput.csv'
output_file = 'amoutput.csv'
columns_to_extract = [0, 2, 3]
extract_columns(input_file, output_file, columns_to_extract)
