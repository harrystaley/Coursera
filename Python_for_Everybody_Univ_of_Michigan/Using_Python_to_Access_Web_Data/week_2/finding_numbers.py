"""
Find and sum all  numbers in a file using regex.
"""
import re


def read_text_file():
    """
    Prompts the user for a filename and if not given uses sample_data.txt.

    :return: the lines read in from the text file.
    """
    file_name = input('Enter file name: ')
    if len(file_name) < 1:
        print('No file was provided using sample_data.txt to test')
        file_name = 'sample_data.txt'
    with open(file_name, 'r') as f:
        text = f.read()
    return text


def sum_numbers_from_file():
    """
    Read in a text file and sum all numbers.
    :return: The sum of all numbers output to the terminal.
    """
    text = read_text_file()
    pattern = '[0-9]+'
    numbers = re.findall(pattern, text)
    try:
        # convert the list of strings into int.
        numbers = list(map(int, numbers))
    except:
        print("check the pattern of your regular expression.")
    print(f"Sum of all numbers in the file:\n{sum(numbers)}")


if __name__ == '__main__':
    sum_numbers_from_file()