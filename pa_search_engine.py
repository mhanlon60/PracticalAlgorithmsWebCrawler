# -*- coding: utf-8 -*-

"""
Module: 
pa2022_search_engine

About:
Implements functions used by a directory search engine

SOME FUNCTIONS OR THEIR SKELETONS HAVE BEEN PROVIDED
HOWEVER, YOU ARE FREE TO MAKE ANY CHANGES YOU WANT IN THIS FILE
AS LONG AS IT REMAINS COMPATIBLE WITH main.py and tester.py
"""

# %% ---------------------------------------------------------------------------
# Required Imports
# ------------------------------------------------------------------------------
import string
from timeit import default_timer as timer
import os


# %%----------------------------------------------------------------------------
def dict_to_file(di, fi):
    with open(fi, "w") as f:
        for key, value in di.items():
            f.write("%s:%s\n" % (key, value))


# %%----------------------------------------------------------------------------
def print_result(result):
    """
    Print result (all docs with non-zero weights)
    """
    print("# Search Results:")
    count = 0
    for val in result:
        if val[1] > 0:
            print(val[0])
            count += 1
    print(count, " results returned")


# %%----------------------------------------------------------------------------
def crawl_folder(folder
                 , forward_index
                 , invert_index
                 , term_freq
                 , inv_doc_freq
                 , doc_rank
                 ):
    """"
    Crawls a given folder, and runs the indexer on each file
    """

    total_docs = 0
    for file in os.scandir(folder):
        if file.is_file():
            total_docs += 1
            index_file(file.name, file.path, forward_index, invert_index, term_freq, doc_rank)

    # with invert_index calculated, we can calculate the inv_doc_freq of each unique word
    # where inv_doc_freq = number of documents with the word / total number of documents
    for word in invert_index.keys():
        inv_doc_freq[word] = len(invert_index[word]) / total_docs


# %%----------------------------------------------------------------------------
def sanitize_word(word):
    """
    Removes all non ascii characters from a given word
    """
    newword = word.encode('ascii', 'ignore')
    return newword


# %%----------------------------------------------------------------------------
def parse_line(line):
    """    
    Parses a given line, 
    removes whitespaces, splits into list of sanitize words
    Uses sanitize_word()
    
    HINT: Consider using the "strip()" and "split()" function here
    
    """
    list_of_words = line.split()
    for word in list_of_words:
        word = word.strip()
        word = sanitize_word(word)
    return (list_of_words)


# %%----------------------------------------------------------------------------
def index_file(filename
               , filepath
               , forward_index
               , invert_index
               , term_freq
               , doc_rank
               ):
    """    
    Given a file, indexes it by calculating its:
        forward_index
        term_freq
        doc_rank
    and updates the global invert_index
    """
    start = timer()
    number_of_occurences = {}
    files_for_words = []
    with open(filepath, 'r', encoding="utf-8-sig") as f:
        file_words = []
        total_word_num = 0
        for line in f:
            for word in line:
                total_word_num += 1
            list_of_words = parse_line(line)
            forward_index = calculate_forward_index(list_of_words, filename, forward_index, file_words)
            number_of_occurences = calculate_term_freq(list_of_words, number_of_occurences, file_words)
        invert_index = calculate_first_invert_index(forward_index, invert_index, filename)
        for key in number_of_occurences.keys():
            # term_frequency
            freq = number_of_occurences[key] / total_word_num
            term_freq[key] = freq

    end = timer()
    print("Time taken to index file: ", filename, " = ", end - start)


# %%----------------------------------------------------------------------------

def calculate_term_freq(list_of_words, number_of_occurences, file_words):
    for word in list_of_words:
        if word not in number_of_occurences:
            number_of_occurences[word] = 1
        elif word in number_of_occurences:
            number_of_occurences[word] += 1
    return number_of_occurences


def calculate_first_invert_index(forward_index_dict, invert_index_dict, filename):
    # Inverted Index
    for value in forward_index_dict[filename]:
        if value not in invert_index_dict:
            invert_index_dict[value] = [filename]
        elif value in invert_index_dict and filename not in invert_index_dict[value]:
            invert_index_dict[value] = invert_index_dict[value]+[filename]

    return invert_index_dict

def calculate_next_invert_index(forward_index_dict, files_for_words, invert_index_dict, filename):
    # Inverted Index
    for value in forward_index_dict.values():
        for word in value:
            if filename not in files_for_words:
                files_for_words.append(filename)
            invert_index_dict[word] = files_for_words

    return invert_index_dict

def calculate_forward_index(list_of_words, file_name, forward_index_dict, file_words):
    for word in list_of_words:
        file_words.append(word)

    forward_index_dict[file_name] = file_words
    return forward_index_dict


def search(search_phrase
           , forward_index
           , invert_index
           , term_freq
           , inv_doc_freq
           , doc_rank
           ):
    """    
    For every document, you can take the product of TF and IDF 
    for term of the query, and calculate their cumulative product. 
    Then you multiply this value with that documents document-rank 
    to arrive at a final weight for a given query, for every document. 
    """

    words = parse_line(search_phrase)
    result = {}
    sorted_result = ""
    # <YOUR-CODE-HERE>

    return (sorted_result)
