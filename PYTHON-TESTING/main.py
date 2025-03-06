import time
from datetime import datetime


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
        print(f'Test datetime: {timestamp}\nLine count: {line_cnt}\nExecution Time: {end_time - start_time:.6f} seconds\n')
        return line_cnt
        

def count_words(file_name):
    '''
    file_name (string): the name of the file containing 
    
    Returns: number of valid words.
    '''
    start_time = time.time()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    word_cnt = 0
    with open(file_name, 'r') as f:
        for line in f:
            word_cnt +=  len(line.strip().split())
        end_time = time.time()
        print(f'Test datetime: {timestamp}\nWord count: {word_cnt}\nExecution Time: {end_time - start_time:.6f} seconds\n')
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
        print(f'Test datetime: {timestamp}\nSpace count: {space_cnt}\nExecution Time: {end_time - start_time:.6f} seconds\n')
        return space_cnt

def get_file_content(file_name):
    '''
    file_name (string): the name of the file containing 
    
    Returns: contents in string
    '''
    start_time = time.time()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_name, 'r') as f:
        content = " ".join(line.strip() for line in f if line.strip())
        end_time = time.time()
        print(f'Test datetime: {timestamp}\nContent: {content}\nExecution Time: {end_time - start_time:.6f} seconds\n')
        return content


class UserManger(object):
    def __init__(self):
        pass