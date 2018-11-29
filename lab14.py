#!/usr/bin/env python3
# Lab 14 - Christopher Piwarski
# Written 29 November 2018
# Python version 3
# Developed with Sublime Text 3.1.1 Build 3176 and Mac OS X Terminal

################################################################################
# Problem 1
# Process the Green Eggs and Ham poem to count the distinct words. Print out
# how many distinct words there are, and their frequency. Print out the most
# commonly occuring word in the book.
################################################################################

# import statements
import urllib.request


# declare variables
wordCount = {}
filename = 'eggs.txt'

# process file
try:
    # open file
    with open(filename, 'r') as eggFile:

        # read in a line and count the words
        for line in eggFile:
            sentence = line
            print(sentence)

        # for each line, remove dashes

        eggFile.close()
except IOError:
    print('IO Error detected. File Operation Failed.')
finally:
    print('File Reading Sequence Completed.')


totalWords = 0
mostCommon = ''

# print out results
print('There are %d words in %s' % (totalWords, filename))
print('The most commonly occuring word is %s' % mostCommon)



################################################################################
# Problem 2
# Retrieve the headlines from CSU News from the website HTML.
################################################################################

# declare variables
website = 'https://www2.calstate.edu/csu-system/news'