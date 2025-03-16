import re
import os
import sys
import time
from datetime import datetime
import argparse

# Detect if running on macOS or Linux
python_cmd = "python3" if sys.platform == "darwin" else "python"

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
    # start_time = time.time()
    # timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line_cnt = 0
    with open(file_name, 'r') as f:
        for line in f:
            if line.strip():  # we don't count empty line, this help check if an line is empty
                line_cnt += 1
    # end_time = time.time()
   #     print(f'Test datetime: {timestamp}\nLine count: {line_cnt}\nExecution Time: {end_time - start_time:.6f} seconds\n')
    return line_cnt
        

def count_words(file_name):
    '''
    file_name (string): the name of the file containing 
    
    Returns: number of valid words.
    '''
    # start_time = time.time()
    # timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    word_cnt = 0
    special_character = r'[^a-zA-Z0-9]'

    with open(file_name, 'r') as f:
        for line in f:
            for word in line.strip().split():
                clean_word = re.sub(special_character, '', word)
                if clean_word:
                    word_cnt += 1

    # end_time = time.time()
    # print(f'Test datetime: {timestamp}\nWord count: {word_cnt}\nExecution Time: {end_time - start_time:.6f} seconds\n')
    return word_cnt
        

def count_spaces(file_name):
    '''
    file_name (string): the name of the file containing 
    
    Returns: number of valid spaces.
    '''
    # start_time = time.time()
    # timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    space_cnt = 0
    with open(file_name, 'r') as f:
        for line in f:
            for word in line.strip(): 
                if word.isspace():
                    space_cnt += 1

    # end_time = time.time()
    #  print(f'Test datetime: {timestamp}\nSpace count: {space_cnt}\nExecution Time: {end_time - start_time:.6f} seconds\n')
    return space_cnt

def get_file_content(file_name):
    '''
    file_name (string): the name of the file containing 
    
    Returns: contents in string
    '''
    # start_time = time.time()
    # timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # special_character_pattern = r'^[^a-zA-Z0-9\s]+|[^a-zA-Z0-9\s]+$'  # remove special character at the beginning and end (optional)

    with open(file_name, 'r') as f:
        content = " ".join(line.strip() for line in f if line.strip())
        # content = re.sub(special_character_pattern, '', content)
    
    # end_time = time.time()
    # print(f'Test datetime: {timestamp}\nContent: {content}\nExecution Time: {end_time - start_time:.6f} seconds\n')
    return content
    
def count_specific_words(file_name, words):
    '''
    file_name (string): the name of the file containing 
    words (list): list of specific words to be checked in the file

    Returns(dictionary): word as key, count of word as value
    '''
    # start_time = time.time()
    # timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    special_character = r'[^a-zA-Z0-9]'
    word_cnt_dict = {word:0 for word in words} # create dict for word to be checked
    word_mapping = {word.lower(): word for word in words} 

    with open(file_name, 'r') as f:
        for line in f:
            for w in line.lower().strip().split():
                clean_word = re.sub(special_character, '', w)
                if clean_word in word_mapping:
                    original_word = word_mapping[w]
                    word_cnt_dict[original_word] += 1

    # end_time = time.time()
    return word_cnt_dict


def analyze_file(file_name, words=None):
    '''
    file_name (string): the name of the file containing 
    words (list): list of words to be checked occurances

    Returns: line count, word count, space count, and file content
    '''
    if not os.path.isfile(file_name):
        print(f"Error: File '{file_name}' not found.")

    start_time = time.time()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # analyze function
    line_count = count_lines(file_name)
    word_count = count_words(file_name)
    space_count = count_spaces(file_name)
    content = get_file_content(file_name)
    


    print(f'\nDatetime: {timestamp}')
    print(f'\nAnalyzing file: {file_name}')
    print(f'Line count: {line_count}\nWord count: {word_count}\nSpace count: {space_count}')
    print(f'File content: \n{content}')    


    if words and len(words) > 0:
        word_occurrences = count_specific_words(file_name, words)
        for word in words:
            print(f"Occurances of {word}: {word_occurrences[word]}")

    end_time = time.time()
    print(f'Execution Time: {end_time - start_time:.6f} seconds\n')

# if __name__ == "__main__":
#     if len(sys.argv) < 2:  # Check if exactly one argument is provided
#         print("Please provide at least one file name\nUsage: python analyze_file.py <file_name> <file_name> ... <file_name>")
#         sys.exit(1)

#     for file_name in sys.argv[1:]:  # Get the file name from the command-line argument
#         analyze_file(file_name)


def main():
    '''
    Using argparse to implement CLI feature
    '''
    parser = argparse.ArgumentParser(description="Analyze text files and display statistics")

    # add sub-command and description of available commands
    subparsers = parser.add_subparsers(dest="command",
                                       title="Available Commands",
                                       description="Select one of the following commands:")
    
    analyze_parser = subparsers.add_parser("analyze",
                                            help="Analyze file and display: count lines, words, spaces, content and specific word count\nRun `python3 mvp.py analyze --help` for more details")
    
    analyze_parser.add_argument("files", nargs="+", help="File path(s) to be analyzed")
    analyze_parser.add_argument("-w", "--word", nargs="+", help="Count specific words occurrences within the file")

    args = parser.parse_args()

    if len(sys.argv) < 1 or args.command is None:
        print("\n🚨 Error: Missing command.\n")
        print(f"Usage: {python_cmd} mvp.py analyze <file1> <file2> ... [-w <word1> <word2> ...]")
        print(f"Run `{python_cmd} mvp.py --help` for more details.\n")
        sys.exit(1)

    if args.command == "analyze":
        word_list = args.word if args.word else [] # create a word list for arguments
        for file in args.files:
            analyze_file(file, word_list)



if __name__ == "__main__":
    main()