"""hash tables (dictionaries in python) are good at lookups, inserts and deletes as well as 
avoiding duplicates, mapping one data to another (example: cashing)"""
voted = dict()

def check_voter(name):
    if name in voted:
        print("kick them out!")
    else:
        voted[name] = True
        print("Let them vote!")

check_voter("sami")
check_voter('Aida')
check_voter("sami")
check_voter("Naomi")
check_voter("Aida")