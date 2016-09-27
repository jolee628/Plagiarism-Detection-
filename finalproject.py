#
#
# fianlproject.py
#
# name: Joseph Lee
# email: leejoseph628@gmail.com
#
# partner name: Clement Ho Kei Lee
# partner email: clelee@bu.edu


import math


class TextModel:
    def __init__(self, model_name):       
        self.name = model_name                #define the name of the model
        self.words = ({})                     #dictionary for words
        self.word_lengths = ({})              #dictionary for unique words
        self.stems = ({})                     #dictionary for the stem of a word
        self.sentence_lengths = ({})          #dictionary for unique sentence lengths
        self.syllable = ({})                  #dictionary for number of syllables
        self.readability = ({})               #dictionary for unique readability score
        self.word_count = ({})                #dictionary for word count

# Task 2
    def __str__(self):
        '''Return a string representation of the TextModel'''
        s = 'text model name: ' + self.name + '\n'                              #string for Model Name
        s += '  number of words: ' + str(len(self.words)) + '\n'                #string for number of words
    
   
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'   #string for number of word lengths
        s += '  number of stems: ' + str(len(self.stems)) + '\n'                  #string for number of stems
        
        s += '  number of sentence length: ' + str(len(self.sentence_lengths)) + '\n'   #string for number of sentence length
        
        s += '  readability range for grade: ' + str(int( ((0.39 * (len(self.word_count))/(cal_sentence(self.sentence_lengths))) \
                                                          + (11.8 * (sum(self.syllable))/(len(self.word_count))) - (15.59)))) + '\n' #string for readability grade range
        
        s += '  total words: ' + str(len(self.word_count)) + '\n'   #string for total words

        s += '  total syllable: ' + str(sum(self.syllable)) + '\n'   #string for total syllables

        s += '  total sentence: ' + str(cal_sentence(self.sentence_lengths)) + '\n'  #string for total sentence
        return s  
  
    def __repr__(self):
        '''This will return a string of itself so it can be used in shell'''
        return str(self)       # calls our __str__

# Task 4

    def add_string(self, s):
        """Analyzes the string txt and adds its pieces
       to all of the dictionaries in this text model.
        """
        count_split = s.split()                                     #split the sentence into strings
        count = 0                                                   #initiate the count to be 0
        lst = ['Dr.', 'Ms.', 'Jr.', 'Mrs.', 'Mr.', 'Miss.']         #a list of words that won't be split
        for x in count_split:
            if x in lst:
                count += 1
            elif x[-1] in '.!?':
                count += 1
                if count in self.sentence_lengths:
                    self.sentence_lengths[count] += 1
                    count = 0
                else:
                    self.sentence_lengths[count] = 1
                    count = 0
            else:
                count += 1

        first_split = s.split()                                     #split the words again
        word_count = 0
        syllable_count = 0
        readability_count = 0
        another_list = ['Dr.', 'Ms.', 'Jr.', 'Mrs.', 'Mr.', 'Miss.']  
        for b in first_split:
            if b in another_list:
                word_count += 1
                syllable_count += change(changing(b))
            elif b[-1] in '.!?':
                word_count += 1
                syllable_count += change(changing(b))
                readability_count = int(((0.39 * (word_count)) + (11.8 * (syllable_count)/(word_count)) - (15.59))) # This is the formula for calculating the readability score for 
                                                                                                                    # each unique sentence
                
                if readability_count in self.readability:
                    self.readability[readability_count] += 1
                    word_count = 0
                    syllable_count = 0
                    readability_count = 0
                    
                else:
                    self.readability[readability_count] = 1
                    word_count = 0
                    syllable_count = 0
                    readability_count = 0

            else:
                word_count += 1
                syllable_count += change(changing(b))
                    
                
      
        words = clean_txt(s)  # cleaning the file with the clean txt function
        words = words.lower() # turn the words into lower cases
        words = words.split() # spliting the string into seperate words
        wordlist = [len(i) for i in words] 
        stems = [stem(x) for x in words]
        num_syllable = [change(changing(a))for a in words]
        
    # Code for word count
        self.word_count = words


     # Code for updating the syllables
        self.syllable = num_syllable

        

    # Code for updating the words dictionary.
        for w in words:
            if w not in self.words:
                self.words[w] = 1
            else:
                self.words[w] += 1
                
        # Maybe write Return code for each dictionary UPDATE
    

    # Add code to update other feature dictionaries.
    
        for q in wordlist:
            if q not in self.word_lengths:
                self.word_lengths[q] = 1
      
            else:

                self.word_lengths[q] += 1
    
    ### update the stems dictionary###
        for z in stems:
            if z in self.stems:
                self.stems[z] += 1
            else:
              	self.stems[z] = 1


        


#Task 5
    def add_file(self, filename):
        '''This function should read a file and create a dictionary with keys leading
        to each independent word along with the word's possible followup words.'''
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        
        text = f.read()

        self.add_string(text)
        self.save_model()
        
        f.close()


# Part II Task 1

    def save_model(self):
        """A function that demonstrates how to save a
           Python dictionary to a file.
        """

        f = open(str(self.name) + '_' + 'words', 'w')
        f.write(str(self.words))
        f.close()

        f = open(str(self.name) + '_' + 'word_lengths', 'w')
        f.write(str(self.word_lengths))
        f.close()
        
        f = open(str(self.name) + '_' + 'stems', 'w')
        f.write(str(self.stems))
        f.close()
        
        f = open(str(self.name) + '_' + 'sentence_lengths', 'w')
        f.write(str(self.sentence_lengths))
        f.close()

        f = open(str(self.name) + '_' + 'syllable', 'w')
        f.write(str(self.syllable))
        f.close()
                                                                 
                                                                 
        f = open(str(self.name) + '_' + 'readability', 'w')
        f.write(str(self.readability))
        f.close()                                                         

# Part II Task 2

    def read_model(self):
        """ A function that demonstrates how to read a
            Python dictionary from a file.
        """

        f = open(str(self.name) + '_' + 'words', 'r')    # Open for reading.
        words_str = f.read()           # Read in a string that represents a dict.
        f.close()

        self.words = dict(eval(words_str))      # Convert the string to a dictionary.

        f = open(str(self.name) + '_' + 'word_lengths', 'r')    # Open for reading.
        word_lengths_str = f.read()           # Read in a string that represents a dict.
        f.close()

        self.word_lengths = dict(eval(word_lengths_str))
        
        f = open(str(self.name) + '_' + 'stems', 'r')    # Open for reading.
        stems_str = f.read()           # Read in a string that represents a dict.
        f.close()

        self.stems = dict(eval(stems_str))
        
        f = open(str(self.name) + '_' + 'sentence_lengths', 'r')    # Open for reading.
        sentence_lengths_str = f.read()           # Read in a string that represents a dict.
        f.close()

        self.sentence_lengths = dict(eval(sentence_lengths_str))

        f = open(str(self.name) + '_' + 'syllable', 'r')    # Open for reading.
        syllable_str = f.read()           # Read in a string that represents a dict.
        f.close()

        self.syllable = dict(eval(syllable_str))
                                                                 
                                                                 
        f = open(str(self.name) + '_' + 'readability', 'r')    # Open for reading.
        readability_str = f.read()           # Read in a string that represents a dict.
        f.close()

        self.readability = dict(eval(readability_str))

    def similarity_scores(self, other):
        """ analyzing the text files and returning a score according
            to their similarity
        """
        total_scores = [0]*5    

        words_scores = compare_dictionaries(other.words, self.words)
        word_lengths_scores = compare_dictionaries(other.word_lengths, self.word_lengths)
        stems_scores = compare_dictionaries(other.stems, self.stems)
        sentence_lengths_scores = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
        readability_scores = compare_dictionaries(other.readability, self.readability)

        total_scores[0] = words_scores 
        total_scores[1] = word_lengths_scores 
        total_scores[2] = stems_scores 
        total_scores[3] = sentence_lengths_scores 
        total_scores[4] = readability_scores
  
        return total_scores
#classify

    def classify(self, source1, source2):
    
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        
        print(scores1)
        print(scores2)
        
        words_weight = 0.3
        word_lengths_weight = 0.15
        stems_weight =0.15
        sentnece_lengths_weight =0.2
        readability_weight = 0.2   
        
        
        weighted_sum1 = scores1[0] * words_weight + scores1[1] * word_lengths_weight + scores1[2] * stems_weight + scores1[3] * sentnece_lengths_weight + \
                        scores1[4] * readability_weight
        
        weighted_sum2 = scores2[0] * words_weight + scores2[1] * word_lengths_weight + scores2[2] * stems_weight + scores2[3] * sentnece_lengths_weight + \
                        scores2[4] * readability_weight
          
        print(weighted_sum1)
        print(weighted_sum2)
        print()
        
        if weighted_sum1 > weighted_sum2:
          
          print(self.name, 'is more likely to have come from', source1.name)
        
        else:
          
          print(self.name, 'is more likely to have come from', source2.name)

# Task 3-----not included in class

def clean_txt(txt):
  '''takes in a string of text and returns a string of clean words'''
  
  txt = txt.replace('.', '')
  txt = txt.replace('?', '')
  txt = txt.replace(',', '')
  txt = txt.replace('!', '')
  txt = txt.replace('"', '') # remove open quotations
  txt = txt.replace('"', '') # remove close quotations
  txt = txt.replace(':', '')
  txt = txt.replace(';', '')
  txt = txt.replace('(', '')
  txt = txt.replace(')', '')
  
  
  return txt


def run_test():
  '''takes in a test file and reads and run the class model
  '''
 
  model= TextModel('A. Poor Righter')
  model.add_string("The partiers love the pizza party.")
  print(model)
  print(model.words)
  print()
  print(model.stems)
  
                                                          
  


 
def change_y(list_words):
    """ if the last character of a word is 'y', change it to "i"
    """

    for x in range(len(list_words)):



        if list_words[x][-1] =='y':

            list_words[x] = list_words[x][:-1] + 'i'

    return list_words



def stem(s):
    """takes in a word and returns the stem of that word
    """

    if s[-3:] == 'ing':
        if len(s) == 4:
            s = s
        else:
            if s[-4] == s[-5]:
                s = s[:-3]
            else:
                s = s[:-3]
    elif s[-1] =='y':        #change y in the last character into i for later stemming purpose
        s = s[:-1] + 'i'
    elif s[-3:] == 'est':
        if len(s) <= 5:
            s=s
        elif s[-4] == s[-5]:
            s = s[:-2]
        else:
            s= s[:-3]
    elif s[-2:] == 'ed':
        s = s[:-2]
    elif s[-2:] == 'en':
        s = s[:-2]
    elif s[-2:] == 'es':
        if s[-3] == s[-4]:
            s = s[:-2]
        else:
            s = s[:-2]
    elif s[-3:] == 'ers':
        s = s[:-3]
    elif s[-2:] == 'er':
        s = s[:-2]
    elif s[-1] == 's':
        s = s[:-1]
    return s

  
  
def changing(word):
    """take in a string of words and return a list of
       words that contain 'aeiou'
    """
    return [x for x in range(len(word)) if word[x] in 'aeiou']
  

def change(listword_index):
    """take in a word and return a list of
       the numbers of syllables in that word
    """
  
    syll = 0

    for x in range(len(listword_index)):

        if listword_index[x] == listword_index[-1] and listword_index[x]-1 == listword_index[x-1]:

            syll == syll
            
        elif listword_index[x] == listword_index[-1]:

            syll += 1
        
        else:

            if x != -1 and listword_index[x] + 1 == listword_index[x + 1]:
            
            
                syll += 1
            
            elif x != -1 and listword_index[x]-1 == listword_index[x-1]:
                syll == syll

            else:

                syll +=1

    return syll
                

  
# Part IV

def compare_dictionaries(d1, d2):
    '''This will compare the dictionary 1 and dictionary 2
       and return a score for comparing each item in the dictionaries.
    '''
    score = 0
    total_d1 = sum(d1.values())
    log_sim_score = 0
    no_match = 0
  
    for x in d2.keys():
        if x in d1.keys():
            probability = math.log(d1[x] / total_d1) * d2[x]
            log_sim_score += probability
        else:

            no_match += d2[x] * math.log((0.5/total_d1))
  
    score = log_sim_score + no_match
  
    return score


def cal_sentence(d1):
    '''take in a dictionary and return the sum of the values in each key.'''

    total_value = 0

    for x in d1.keys():
        total_value += d1[x] 

    
    return total_value

                                                                
                                                                 
def test():
    """ compare mystery to source1 and source 2 and see which file is mystery closer to """
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)    
                                     

def test_with_text(file1, file2, file3):
    """ compare mystery to source1 and source 2 and see which file is mystery closer to """
    source1 = TextModel(file1)
    source1.add_file(file1)
    


    source2 = TextModel(file2)
    source2.add_file(file2)
 


    mystery = TextModel(file3)
    mystery.add_file(file3)
 


    mystery.classify(source1, source2)

    print()
    print(source1)
    print(source2)
    print(mystery)
                                     
   


