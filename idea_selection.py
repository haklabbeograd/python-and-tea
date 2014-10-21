import os
import sys

persons = []
ideas = []
votes = []

data_filename = sys.argv[1]

def save():
    print 'saving to', data_filename
    f = open(data_filename, 'w+')
    f.write(str( (persons, ideas, votes) ))
    f.close()

def load():
    if os.path.exists(data_filename):
        print 'loading', data_filename
        global persons, ideas, votes
        f = open(data_filename, 'r')
        (persons, ideas, votes) = eval(f.read())
        f.close()

def manage_persons():
    while True:
        cmd = raw_input('persons> ')
        if cmd in ['a', 'add']:
            persons.append(raw_input('unesi ime: '))
        elif cmd in ['d', 'del']:
            persons.remove(raw_input('unesi ime: '))
        elif cmd in ['p', 'print']:
            for ime in persons:
                print ime
        elif cmd in ['q', 'quit']:
            break
        elif cmd in ['l', 'load']:
            load()
        elif cmd in ['s', 'save']:
            save()

def main():
    print 'hello everybody! how are you doing today?!'
    while True:
        cmd = raw_input('> ')
        if cmd in ['p', 'persons']:
            manage_persons()
        elif cmd in ['i', 'ideas']:
            manage_ideas()
        elif cmd in ['v', 'votes']:
            manage_votes()
        elif cmd in ['q', 'quit']:
            break
        elif cmd in ['l', 'load']:
            load()
        elif cmd in ['s', 'save']:
            save()

load()
main()
if raw_input('do you want to save data? ').lower() in ['y', 'yes']:
    save()

