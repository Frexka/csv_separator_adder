import os

# your path to the target folder, e.g.: r'C:\Users\user\Documents\csv_files'
target_folder = r'C:\Users\user\Documents\csv_files'

# Change the current working directory to the target folder
os.chdir(target_folder)

# specify the input and output file names
input_file = 'f1_drivers.csv'
output_file = os.path.join(target_folder, 'f1_drivers_with_semicolons.csv')

# specify the separator to be added, escape the separator if needed, add newline character
separator = '\;\n'

# add more encodings if needed
encodings = ['utf-8', 'latin-1', 'cp1252']

lines = None
for encoding in encodings:
    try:
        with open(input_file, 'r', encoding=encoding) as file:
            lines = file.readlines()
        break  # break the loop if file reading is successful
    except UnicodeDecodeError:
        continue

if lines is not None:
    modified_lines = [line.rstrip('\n') + separator for line in lines]  # add separator

    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(modified_lines)
else:
    print("Unable to read the file with any of the specified encodings.")
