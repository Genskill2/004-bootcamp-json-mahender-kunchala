import json
from math import sqrt

# Load journal function
def load_journal(filename):
    fObj = open(filename)
    data = json.load(fObj)
    return data

# compute_phi funtion
def compute_phi(filename, event):
    lst = load_journal(filename)
    n11 = n00 = n10 = n01 = n1_plus = n0_plus  = nplus_1 = nplus_0 = 0
    for d in lst:
        if event in d['events'] and d['squirrel'] == True:
            n11 += 1
        if event not in d['events'] and d['squirrel'] == False:
            n00 += 1
        if event in d['events'] and d['squirrel'] == False:
            n10 += 1
        if event not in d['events'] and d['squirrel'] == True:
            n01 += 1
        if event in d['events']:
            n1_plus += 1
        if event not in d['events']:
            n0_plus += 1
        if d['squirrel'] is True:
            nplus_1 += 1
        if d['squirrel'] is False:
            nplus_0 += 1
    #Calculating correlation between the given event and squirrel event     
    corr = (n11 * n00 - n10 * n01) / sqrt(n1_plus * n0_plus * nplus_1 * nplus_0)
    return corr   


#compute_correlations function
def compute_correlations(filename):
    data = load_journal(filename)
    corr_d = dict()
    unique = []
    #Creating a list of unique events
    for d in data:
        for i in d['events']:
            if i not in unique:
                unique.append(i)
    #Calculating corr relation for every unique event in the list to squirrel event and adding them to a dictionary as key, value pairs           
    for event in unique:
        corr_d[event] = compute_phi("journal.json", event)

    return corr_d

#diagnose function       
def diagnose(filename):
    
    d = compute_correlations(filename)
    max_value = -100
    event_max = None
    event_min = None
    min_value = 100
    for key, value in d.items():
        if value > max_value:
            max_value = value
            event_max = key
        if value < min_value:
            min_value = value
            event_min = key
    return event_max, event_min


'''I would recommend Scott not to eat peanuts and to brush daily because those events are most highly positively and most highly negatively correlated with the squirrel event.'''
