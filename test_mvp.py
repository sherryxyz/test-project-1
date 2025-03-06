import pytest
from mvp import count_lines, count_words, count_spaces, get_file_content

file1 = 'test_folder/file1.txt'
file2 = 'test_folder/file2.txt'
file3 = 'test_folder/file3.txt'
file4 = 'test_folder/file4.txt'

@pytest.mark.parametrize("file_name, expected_word_count", [
      (file1, 0),
      (file2, 37),
      (file3, 19),
      (file4, 0),
])

def test_count_words(file_name, expected_word_count):
    assert count_words(file_name) == expected_word_count



@pytest.mark.parametrize("file_name, expected_line_count", [
      (file1, 0),
      (file2, 3),
      (file3, 4),
      (file4, 4),
])

def test_count_lines(file_name, expected_line_count):
    assert count_lines(file_name) == expected_line_count


@pytest.mark.parametrize("file_name, expected_space_count", [
      (file1, 0),
      (file2, 34),
      (file3, 16),
      (file4, 0),
])

def test_count_spaces(file_name, expected_space_count):
    assert count_spaces(file_name) == expected_space_count