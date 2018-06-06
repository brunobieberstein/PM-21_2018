import random

def get_input():
    while True:
        eingabe = input('Wie viele Leute sind in dem Raum? ')
        try:
            n = int(eingabe)
            return n
            break
        except ValueError:
            print('Bitte Zahl eingeben.')

def choices(seq, k):
    result = []
    for n in range(k):
        result.append(random.choice(seq))
    return result

def calculate_likelihood_for_2_out_of_n(n):
    count_trials_with_people_with_same_birthday = 0
    trials = 10000
    for trial in range(trials):
        birthdays = set(choices(range(365), k=n))
        if len(birthdays) < n:
            count_trials_with_people_with_same_birthday += 1
    return count_trials_with_people_with_same_birthday / trials

n = get_input()
print('Die Wahrscheinlichkeit, dass mindestens zwei Leute am gleichen Tag Geburtstag haben beträgt:',calculate_likelihood_for_2_out_of_n(n))
