import re
import os
import sys
import time
from datetime import datetime


# def ensure_path_exists(file_name):
#     # Get the directory of the file path
#     dir_path = os.path.dirname(file_name)

#     # Check if the directory exists
#     if not os.path.exists(dir_path):
#         print(f"Directory '{dir_path}' does not exist.")
#         return False
    
#     print(f"Directory '{dir_path}' does exists")
#     return True


def count_lines(file_name):
    '''
    file_name (string): the name of the file containing 
    
    Returns: number of valid lines.
    '''
    start_time = time.time()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line_cnt = 0
    with open(file_name, 'r') as f:
        for line in f:
            if line.strip():  # we don't count empty line, this help check if an line is empty
                line_cnt += 1
        end_time = time.time()
   #     print(f'Test datetime: {timestamp}\nLine count: {line_cnt}\nExecution Time: {end_time - start_time:.6f} seconds\n')
        return line_cnt
        

def count_words(file_name):
    '''
    file_name (string): the name of the file containing 
    
    Returns: number of valid words.
    '''
    start_time = time.time()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    word_cnt = 0
    special_character = r'[^a-zA-Z0-9]'

    with open(file_name, 'r') as f:
        for line in f:
            for word in line.strip().split():
                clean_word = re.sub(special_character, '', word)
                if clean_word:
                    word_cnt += 1
        end_time = time.time()
      #  print(f'Test datetime: {timestamp}\nWord count: {word_cnt}\nExecution Time: {end_time - start_time:.6f} seconds\n')
        return word_cnt
        

def count_spaces(file_name):
    '''
    file_name (string): the name of the file containing 
    
    Returns: number of valid spaces.
    '''
    start_time = time.time()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    space_cnt = 0
    with open(file_name, 'r') as f:
        for line in f:
            for word in line.strip(): 
                if word.isspace():
                    space_cnt += 1
        end_time = time.time()
      #  print(f'Test datetime: {timestamp}\nSpace count: {space_cnt}\nExecution Time: {end_time - start_time:.6f} seconds\n')
        return space_cnt

def get_file_content(file_name):
    '''
    file_name (string): the name of the file containing 
    
    Returns: contents in string
    '''
    start_time = time.time()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # special_character_pattern = r'^[^a-zA-Z0-9\s]+|[^a-zA-Z0-9\s]+$'  # remove special character at the beginning and end (optional)

    with open(file_name, 'r') as f:
        content = " ".join(line.strip() for line in f if line.strip())
        # content = re.sub(special_character_pattern, '', content)
        end_time = time.time()
       # print(f'Test datetime: {timestamp}\nContent: {content}\nExecution Time: {end_time - start_time:.6f} seconds\n')
        return content


# ensure_path_exists('/Users/xueyingzheng/Desktop/python/project1/test_folder/file3.txt')

def analyze_file(file_name):
    '''
    file_name (string): the name of the file containing 
    
    Returns: line count, word count, space count, and file content
    '''
    start_time = time.time()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line_count = count_lines(file_name)
    word_count = count_words(file_name)
    space_count = count_spaces(file_name)
    content = get_file_content(file_name)
    end_time = time.time()


    print(f'\nDatetime: {timestamp}')
    print(f'Line count: {line_count}\nWord count: {word_count}\nSpace count: {space_count}')
    print(f'File content: \n{content}')
    print(f'Execution Time: {end_time - start_time:.6f} seconds\n')


if __name__ == "__main__":
    if len(sys.argv) != 2:  # Check if exactly one argument is provided
        print("Usage: python analyze_file.py <file_name>")
        sys.exit(1)

    file_name = sys.argv[1]  # Get the file name from the command-line argument
    analyze_file(file_name)