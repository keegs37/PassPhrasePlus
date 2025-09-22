import argparse
from create_sentence import create_sentence
from verb import Verb, create_verb
from template import Template, create_template
from subject import Subject, create_subject
from determiner import Determiner, create_determiner
from conjugate import conjugate
from object import Object, create_object
from add_delimiter import add_delimiter
from add_variance import add_variance

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", type=int, help="Number of passphrases to generate")
    parser.add_argument("-d", type=str, help="Passphrase words will be separated by your chosen delimiter")
    parser.add_argument("-r", action="store_true", help="the output will have: 1. The first character of a random word capitalized, 2. A random word appended with a special character, and  3. A random word appended with a random number.")
    args = parser.parse_args()
    
    if args.n:
        for i in range(args.n):
            sentence = create_sentence()
            delimiter = " "
            if args.d:
                delimiter = args.d
                sentence = add_delimiter(sentence,args.d)
            if args.r:
                sentence = add_variance(sentence, delimiter)
            print(sentence)
    else:
        for i in range(5):
            sentence = create_sentence()
            delimiter = " "
            if args.d:
                delimiter = args.d
                sentence = add_delimiter(sentence,args.d)
            if args.r:
                sentence = add_variance(sentence, delimiter)
            print(sentence) 

if __name__ == "__main__":
    main()
