# UTF-8 Validation
## Description
This repository contains the solution for the "UTF-8 Validation" project in the Algorithm curriculum at Holberton School. The project aims to determine if a given data set represents a valid UTF-8 encoding.

## Getting Started
To run the code, you will need an editor like vi, vim, or emacs. The code is written in Python and will be interpreted/compiled on Ubuntu 14.04 LTS using Python 3 (version 3.4.3).

## Requirements
- All Python files should end with a new line.
- The first line of all Python files should be exactly #!/usr/bin/python3.
- The code should follow the PEP 8 style (version 1.7.x) for consistency and readability.
- All files must be executable.
## Usage
### Task: UTF-8 Validation
The main objective of this project is to implement a method, validUTF8(data), that checks whether a given data set represents a valid UTF-8 encoding. The method should return True if the data is valid UTF-8, and False otherwise.

## Constraints:

- A character in UTF-8 can be 1 to 4 bytes long.
- The data set can contain multiple characters.
- The data will be represented by a list of integers.
- Each integer represents 1 byte of data, and we only need to handle the 8 least significant bits of each integer.
## Example Usage:
``
python
Copy code
data = [65]
print(validUTF8(data))  # Output: True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # Output: True

data = [229, 65, 127, 256]
print(validUTF8(data))  # Output: False``
## Additional Resources
For further understanding of UTF-8 encoding and Unicode, you can refer to the following resources:

- UTF-8
- Characters, Symbols, and the Unicode Miracle
## About the Author
This project was written by, **Ugwuanyi Afam** a  student at the ALX SE program🚀