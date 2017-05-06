# Project 3: Simple Content indexer

## Part one - Indexer

We are going to build a simple file content indexer.

Often, we want to find things quickly but doing a brute for search takes too long.

If we have many files running grep may take too long to be pratical. So we want to frontload
some of the work.

Google doesn't search the entire web everytime you search for something.
Google periodically searches the web, and builds an index of that data.

When you request it looks through the index, and gives you the results.

We can build a very simple version of that.

This is a good exercise because we can really push the work to the data structures. The code
is really about building the best data structures, and then leveraging this.

In this example we are going to build an indexer capable of indexing a few text files.

The heart of the indexer is to build a dictionary (hash) of words that map to files. Our
end goal is that we can enter keywords and quickly find the files that have those words in it.

Where we can go from a word to a list of files

Ex:

```python
{'witch'}['harrypotter.txt','salemtrials.txt']
```

A hash lookup of 'witch' is O(1) where a search for the word through every file is O(N) and there
could be millions of words.

The steps are

* Search a directory for a list of .txt files

* For each text file found, open and read, parsing the words out

* Each word becomes a key in the dictionary/hash, and the value is an array of files that word is found in




```python

import os
for file in os.listdir("/mydir"):
    if file.endswith(".txt"):
        print(os.path.join("/mydir", file))


```

## Part two - search

Search the index for a word and show all the files that contain that word.



## part three - and/or/not search


