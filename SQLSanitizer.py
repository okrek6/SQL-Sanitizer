import os
import re

def display_ascii_art():
	print(r"""
 _____      _____  _____ _       _____  ___   _   _ _____ _____ _____ ______ ___________ 
|_   _|    /  ___||  _  | |     /  ___|/ _ \ | \ | |_   _|_   _|_   _|___  /|  ___| ___ \
  | |______\ `--. | | | | |     \ `--./ /_\ \|  \| | | |   | |   | |    / / | |__ | |_/ /
  | |______|`--. \| | | | |      `--. \  _  || . ` | | |   | |   | |   / /  |  __||    / 
  | |      /\__/ /\ \/' / |____ /\__/ / | | || |\  |_| |_  | |  _| |_./ /___| |___| |\ \ 
  \_/      \____/  \_/\_\_____/ \____/\_| |_/\_| \_/\___/  \_/  \___/\_____/\____/\_| \_|
    
	""")

import os

def get_directory():
	while True:
		directory = input("Please enter the directory containing T-SQL files: ")
		if os.path.isdir(directory):
			return directory
		else:
			print("The provided directory does not exist. Please try again.")

def is_tsql_file(filename: str) -> bool:
	if not filename:
		return False
	return filename.endswith('.sql')

def add_n_to_string_literals(content: str):
	# Pattern to match string literals not prefixed with N
	pattern = r"(?<!N)('[^']*')"
	matches = re.findall(pattern, content)
	modified_content = re.sub(pattern, r"N\1", content)
	return modified_content, matches

def change_varchar_to_nvarchar(content: str):
    # Pattern to match VARCHAR not prefixed with N
    pattern = r"(?<!N)VARCHAR\b"
    matches = re.findall(pattern, content)
    modified_content = re.sub(pattern, "NVARCHAR", content)
    return modified_content, matches

def change_char_to_nchar(content: str):
    # Pattern to match CHAR not prefixed with N
    pattern = r"(?<!N)CHAR\b"
    matches = re.findall(pattern, content)
    modified_content = re.sub(pattern, "NCHAR", content)
    return modified_content, matches

def process_file(filepath: str):
	"""
	Process the file located at the given filepath.
	Args:
		filepath (str): The path to the file to be processed.
	Returns:
		None
	Raises:
		FileNotFoundError: If the file does not exist.
	"""
	with open(filepath, 'r') as file:
		content = file.read()

	content, string_literals = add_n_to_string_literals(content)
	print("Added 'N' to string literals at:", string_literals)
	if input("Do you want to continue? (y/n): ").lower() != 'y':
		return

	content, varchars = change_varchar_to_nvarchar(content)
	print("Changed VARCHAR to NVARCHAR at:", varchars)
	if input("Do you want to continue? (y/n): ").lower() != 'y':
		return

	content, chars = change_char_to_nchar(content)
	print("Changed CHAR to NCHAR at:", chars)
	if input("Do you want to continue? (y/n): ").lower() != 'y':
		return

	output_path = os.path.join(os.path.expanduser('~'), 'Downloads', os.path.basename(filepath))
	with open(output_path, 'w') as file:
		file.write(content)
	print(f"Modified file saved to: {output_path}")

def main():
	display_ascii_art()
	directory = get_directory()

	for filename in os.listdir(directory):
		filepath = os.path.join(directory, filename)
		if is_tsql_file(filename):
			process_file(filepath)
		else:
			print(f"Skipping non-T-SQL file: {filename}")

	print("All files processed. Exiting.")

if __name__ == "__main__":
	main()

