# by Kami Bigdely
# Inline method.
# TODO: Refactor this program to improve its readability.

LEGAL_DRINKING_AGE = 18
class Person:
    def __init__(self, my_age):
        self.age = my_age
        
def enter_night_club(individual):
    if older_than_18_year_old(individual.age):
        print("Allowed to enter.")
    else:
        print("Entrance of minors is denied.")

def older_than_18_year_old(age):
    return age > LEGAL_DRINKING_AGE
    
    
person = Person(17.9)
enter_night_club(person)
        
