from verb import Verb, create_verb
from template import Template, create_template
from subject import Subject, create_subject
from determiner import Determiner, create_determiner
from conjugate import conjugate
from object import Object, create_object

def create_sentence():
    verb = create_verb()
    template = create_template()
    subject = create_subject()
    verb_phrase = conjugate(verb, template, subject)
    object = create_object()
    determiner = create_determiner(object)

    if determiner.compatibility == "plural_count":
        object.object += "s"
        
    string = f"{verb_phrase} {determiner.determiner} {object.object}"
    return string

