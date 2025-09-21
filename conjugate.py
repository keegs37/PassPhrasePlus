from verb import Verb, create_verb
from template import Template, create_template
from subject import Subject, create_subject

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
    elif template.tense == "past" and template.aspect == "continuous":
        conjugated_pharse = template.pattern
        conjugated_pharse = conjugated_pharse.replace("[Subject]", subject.subject)
        conjugated_pharse = conjugated_pharse.replace("[Gerund]", verb.gerund)
        if subject.number == "singular":
            conjugated_pharse = conjugated_pharse.replace("was/were", "was")
        if subject.number == "plural":
            conjugated_pharse = conjugated_pharse.replace("was/were", "were")
        return conjugated_pharse
    elif template.tense == "future" and template.aspect == "continuous":
        conjugated_pharse = template.pattern
        conjugated_pharse = conjugated_pharse.replace("[Subject]", subject.subject)
        conjugated_pharse = conjugated_pharse.replace("[Gerund]", verb.gerund)
        return conjugated_pharse
    elif template.tense == "present" and template.aspect == "perfect":
       conjugated_pharse = template.pattern
       conjugated_pharse = conjugated_pharse.replace("[Subject]", subject.subject)
       conjugated_pharse = conjugated_pharse.replace("[PastParticiple]", verb.past)
       if subject.number == "singular":
            conjugated_pharse = conjugated_pharse.replace("have/has", "has")
       if subject.number == "plural":
            conjugated_pharse = conjugated_pharse.replace("have/has", "have")
       return conjugated_pharse
    elif (template.tense == "past" or template.tense == "future") and template.aspect == "perfect":
       conjugated_pharse = template.pattern
       conjugated_pharse = conjugated_pharse.replace("[Subject]", subject.subject)
       conjugated_pharse = conjugated_pharse.replace("[PastParticiple]", verb.past)
       return conjugated_pharse
    
verb = create_verb()
template = create_template()
subject = create_subject()

print(conjugate(verb, template, subject))