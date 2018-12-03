# Lab 14 - Christopher Piwarski
# Written 29 November 2018
# Python version 3.7.1
# Developed with Sublime Text 3.1.1 Build 3176 and Mac OS X Terminal
# Assignment help sourced where used

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

    print('Problem 1:')
    # process file
    try:
      # open file
        with open(filename, 'r') as eggFile:
            print('opened ' + filename)

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
        print('\nIO Error Detected Problem 1. File Operation Failed.')
        raise SystemExit
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
    print('Full word count:')
    for key in wordCount:
        print('%s: %d' % (key, wordCount[key]), end='  ')
    print('\nThere are %d words in %s' % (totalWords, filename))
    print('The most commonly occuring word is \'%s\' with %d occurances' \
        % (mostCommon, wordCount[mostCommon]))



###############################################################################
# Problem 2
# Retrieve the headlines from CSU News from the website HTML.
###############################################################################

def problem2():

    # import statements
    import re

    # declare variables
    filename = 'foothill_news.html'

    # help with regex
    # https://stackoverflow.com/questions/7167279/regex-select-all-
    # text-between-tags
    # originally tried using variations on '<h3>.*</h3>' before using 
    # help sourced above.
    regex = re.compile(r'<h3>(.*?)</h3>')

    print('\nProblem 2:')
    # read file
    try:
        with open(filename, 'r') as newsFile:
            print('opened ' + filename)
            newsText = newsFile.read()
        newsFile.close()
    except IOError:
        print('\nIO Error Detected Problem 2. File Operation Failed')
        raise SystemExit
    finally:
        print('\nFile Reading Sequence Finished: Problem 2')

    # process file
    headlines = regex.findall(newsText)

    # print results
    print('*** Foothill Breaking News! ***')
    for line in headlines:
        print('> ' + line)

# Main function to run the script
if __name__ == '__main__':
  problem1()
  problem2()

