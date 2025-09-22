import random
import string
from create_sentence import create_sentence
from verb import Verb, create_verb
from template import Template, create_template
from subject import Subject, create_subject
from determiner import Determiner, create_determiner
from conjugate import conjugate
from object import Object, create_object
from add_delimiter import add_delimiter

def add_variance(sentence, delimiter = " "):
    # random word will have first letter capitalized
    sentence = sentence.split(delimiter)
    random_word = random.choice(sentence)
    random_word_index = sentence.index(random_word)
    sentence[random_word_index] = random_word.capitalize()
    
    # random word will have a symbol appended
    random_word = random.choice(sentence)
    random_word_index = sentence.index(random_word)
    sentence[random_word_index] += random.choice(string.punctuation)
    
    #  random word will have an int appended
    random_word = random.choice(sentence)
    random_word_index = sentence.index(random_word)
    sentence[random_word_index] += str(random.randint(0, 100))
    
    return(delimiter.join(sentence))


