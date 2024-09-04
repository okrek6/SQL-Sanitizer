import unittest
from unittest.mock import patch
from typing import Any  # Add this line
from SQLSanitizer import process_file

class TestProcessFile(unittest.TestCase):
	@patch('builtins.input', side_effect=['y', 'y', 'n'])
	@patch('builtins.open', create=True)
	def test_process_file(self, mock_open: Any, mock_input: Any):
		# Test case 1: Valid file path
		mock_open.return_value.__enter__.return_value.read.return_value = "SELECT * FROM Customers WHERE Country = 'USA'"
		process_file('/path/to/file.sql')
		mock_open.assert_called_once_with('/path/to/file.sql', 'r')
		mock_open.return_value.__enter__.return_value.write.assert_called_once_with("SELECT * FROM Customers WHERE Country = N'USA'")

		# Test case 2: Empty file content
		mock_open.return_value.__enter__.return_value.read.return_value = ""
		process_file('/path/to/empty_file.sql')
		mock_open.return_value.__enter__.return_value.write.assert_not_called()

		# Test case 3: User chooses not to continue after adding 'N' to string literals
		mock_open.return_value.__enter__.return_value.read.return_value = "SELECT * FROM Customers WHERE Country = 'USA'"
		process_file('/path/to/file.sql')
		mock_open.return_value.__enter__.return_value.write.assert_not_called()

if __name__ == '__main__':
	unittest.main()