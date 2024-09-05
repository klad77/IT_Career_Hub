import unittest
import os
import json
from io import StringIO


def write_to_file(file_name, data):
    try:
        with open(file_name, 'w') as f:
            json.dump(data, f)
    except TypeError as err:
        raise err


def read_from_file(file_name):
    try:
        with open(file_name, 'r') as f:
            return json.load(f)
    except FileNotFoundError as err:
        raise err
    except TypeError as err:
        raise err


class TestFileOperations(unittest.TestCase):

    def setUp(self):
        self.file_name = "test_file.json"
        self.test_data = {
            "pk": 4,
            "title": "Test Title",
            "author": "Test Author",
            "published_date": "2024-06-23",
            "publisher": 6,
            "price": 9.99,
            "discounted_price": 3.56,
            "is_bestseller": True,
            "is_banned": False,
            "genres": [1, 2, 3]
        }

    def test_write_and_read_file(self):
        # Write test data to file
        write_to_file(self.file_name, self.test_data)

        # Read the data back
        result_data = read_from_file(self.file_name)

    def test_write_and_read_empty_file(self):
        # Write an empty dictionary to the file
        empty_data = {}
        write_to_file(self.file_name, empty_data)

        # Read the data back
        result_data = read_from_file(self.file_name)

        # Verify that the data read from the file is an empty dictionary
        self.assertEqual(result_data, {})

    def test_read_nonexistent_file(self):
        # Attempt to read from a nonexistent file should raise FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            read_from_file("nonexistent_file.json")

    def test_write_bad_data_into_file(self):
        # Attempt to write non-serializable data to file should raise TypeError
        bad_data = {"data": StringIO("This is not JSON serializable")}
        with self.assertRaises(TypeError):
            write_to_file(self.file_name, bad_data)

    def tearDown(self):
        # Clean up the file after the test, if it exists
        if os.path.exists(self.file_name):
            os.remove(self.file_name)


if __name__ == '__main__':
    unittest.main()
