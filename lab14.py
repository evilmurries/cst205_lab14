# Lab 14 - Christopher Piwarski
# Written 29 November 2018
# Python version 3.7.1
# Developed with Sublime Text 3.1.1 Build 3176 and Mac OS X Terminal

###############################################################################
# Problem 1
# Process the Green Eggs and Ham poem to count the distinct words. Print out
# how many distinct words there are, and their frequency. Print out the most
# commonly occuring word in the book.
###############################################################################

def problem1():
  # declare variables
    wordCount = {}
    filename = 'eggs.txt'


    print('trying file open...')
    # process file
    try:
      # open file
        with open(filename, 'r') as eggFile:
            print('opened file')

            # read in a line and count the words
            for line in eggFile:
                # remove dashes and lower case sentence
                sentence = line.replace('-', ' ')
                sentenceLower = sentence.lower()
                sentenceList = sentenceLower.split()
                for word in sentenceList:
                    if word in wordCount.keys():
                        wordCount[word] += 1
                    else:
                        wordCount[word] = 1

        eggFile.close()
    except IOError:
        print('\nIO Error detected. File Operation Failed.')
    finally:
        print('\nFile Reading Sequence Finished: Problem 1')

    # determine word count and most common word
    mostCommon = 'eggs'
    totalWords = 0
    for word in wordCount.keys():
        totalWords += 1
        if wordCount[word] > wordCount[mostCommon]:
            mostCommon = word

  # print out results
    print('There are %d words in %s' % (totalWords, filename))
    print('The most commonly occuring word is %s' % mostCommon)



###############################################################################
# Problem 2
# Retrieve the headlines from CSU News from the website HTML.
###############################################################################

def problem2():

    # declare variables
    filename = 'foothill_news.html'

    try:
        # open file
        with open(filename, 'r') as newsFile:
        newsFile.close()
    except IOError:
        print('\nIO Error Detected Problem 2. File Operation Failed')
    finally
        print('\nFile Reading Sequence Finished: Problem 2')

if __name__ == '__main__':
  problem1()
  problem2()

