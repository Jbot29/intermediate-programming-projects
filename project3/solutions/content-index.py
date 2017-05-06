import os
import string

stop_words = ['a','an','and','i']

def recursive_find(current_path):
    """recursive find all files and return a list of file names"""
    files = []
    
    for name in os.listdir(current_path):
        path = os.path.join(current_path, name)
        
        if os.path.isdir(path):
            files.extend(recursive_find(path))
        else:
            files.append(path)

    return files

def read_data(filename):
    with open(filename,"r") as f:
        return f.read()

def strip_punctuation(token):
    """strip out punctuation from a toke"""
    return ''.join(ch for ch in token if ch not in string.punctuation)

def index_file(filename):
    """Index one file return a cleaned array of words"""
    words = []
    file_data = read_data(filename)

    file_data = file_data.replace('\n', ' ').replace('\r', '').lower()
    
    tokens = file_data.split(' ')

    for token in tokens:
        if token == "":
            continue

        token_strip = strip_punctuation(token)
        
        if token_strip not in stop_words:
            words.append(token_strip)

    return set(words)


def index_all_files(file_list):
    """go through the list of files and add a file's words to the index"""
    index = {}
    
    for file in file_list:
        add_to_index(index_file(file),file,index)
        
    return index

def add_to_index(words,filename,index):
    """takes a set of words for a filename and adds it to the index"""
    for word in words:
        if index.has_key(word):
            index[word].append(filename)
        else:
            index[word] = [filename]

    return index

def find_files_with(index,keywords):
    """takes a list of keywords, and return a list of files with those keywords"""
    files = []
    
    for keyword in keywords:
        if index.has_key(keyword):
            files.extend(index[keyword])

    return set(files)


print find_files_with(index_all_files(recursive_find('.')),["return"])



        

