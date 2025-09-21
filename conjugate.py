from verb import Verb, create_verb
from template import Template, create_template
from subject import Subject, create_subject
"""
Tense,Aspect,Pattern

x past,simple,[Subject] [Past]
x future,simple,[Subject] will [Verb_Base]
present,continuous,[Subject] am/are/is [Gerund]
past,continuous,[Subject] was/were [Gerund]
future,continuous,[Subject] will be [Gerund]
present,perfect,[Subject] have/has [PastParticiple]
past,perfect,[Subject] had [PastParticiple]
future,perfect,[Subject] will have [PastParticiple]
"""
def conjugate(verb, template, subject):
    if template.tense == "past" and template.aspect == "simple":
       conjugated_pharse = template.pattern
       conjugated_pharse = conjugated_pharse.replace("[Subject]", subject.subject)
       conjugated_pharse = conjugated_pharse.replace("[Past]", verb.past)
       return conjugated_pharse
    elif template.tense == "future" and template.aspect == "simple":
        conjugated_pharse = template.pattern
        conjugated_pharse = conjugated_pharse.replace("[Subject]", subject.subject)
        conjugated_pharse = conjugated_pharse.replace("[Verb_Base]", verb.verb_base)
        return conjugated_pharse
    elif template.tense == "present" and template.aspect == "continuous":
        conjugated_pharse = template.pattern
        conjugated_pharse = conjugated_pharse.replace("[Subject]", subject.subject)
        conjugated_pharse = conjugated_pharse.replace("[Gerund]", verb.gerund)
        if subject.person == "1" and subject.number == "singular":
            conjugated_pharse = conjugated_pharse.replace("am/are/is", "am")
        if subject.person == "1" and subject.number == "plural":
            conjugated_pharse = conjugated_pharse.replace("am/are/is", "are")
        if subject.person == "3" and subject.number == "singular":
            conjugated_pharse = conjugated_pharse.replace("am/are/is", "is")
        if subject.person == "3" and subject.number == "plural":
            conjugated_pharse = conjugated_pharse.replace("am/are/is", "are")
        if subject.person == "2" and subject.number == "singular":
            conjugated_pharse = conjugated_pharse.replace("am/are/is", "are")
        return conjugated_pharse
    
verb = create_verb()
template = create_template()
subject = create_subject()

print(conjugate(verb, template, subject))