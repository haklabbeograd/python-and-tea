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

def manage(collection_name, parse_f=str, cmd_f=None):
    coll = globals()[collection_name]
    while True:
        cmd = raw_input(collection_name+'> ')
        if cmd_f:
            if cmd_f(cmd, coll):
                continue
        if cmd in ['a', 'add']:
            coll.append(parse_f(raw_input('unesi: ')))
        elif cmd in ['d', 'del']:
            coll.remove(parse_f(raw_input('unesi: ')))
        elif cmd in ['p', 'print']:
            for s in coll:
                print s
        elif cmd in ['q', 'quit']:
            break
        elif cmd in ['l', 'load']:
            load()
        elif cmd in ['s', 'save']:
            save()
        elif cmd in ['h', 'help']:
            print 'commands: add del print quit load save help'

def handle_votes_cmds(cmd, coll):
    if cmd in ['a', 'add']:
        for person in persons:
            for idea in ideas:
                coll.append((person, idea, raw_input('unesi za %s, %s: ' % (person, idea))))
        return True
    elif cmd in ['d', 'del']:
        coll[:] = []
        print 'votes are empty!'
        return True
    elif cmd in ['p', 'print']:
        d = {}
        for person, idea, score in coll:
            if idea not in d: d[idea] = 0
            d[idea] += int(score)
        for idea, total_score in sorted(d.items(), key=lambda pair: -pair[1]):
            print idea, ':', total_score
        return True
    else:
        return False

def main():
    print 'hello everybody! how are you doing today?!'
    print 'for help enter help or h'
    while True:
        cmd = raw_input('> ')
        if cmd in ['p', 'persons']:
            manage('persons')
        elif cmd in ['i', 'ideas']:
            manage('ideas')
        elif cmd in ['v', 'votes']:
            manage('votes', parse_f=lambda s: tuple(s.split()),
                   cmd_f=handle_votes_cmds)
        elif cmd in ['q', 'quit']:
            break
        elif cmd in ['l', 'load']:
            load()
        elif cmd in ['s', 'save']:
            save()
        elif cmd in ['h', 'help']:
            print 'commands: persons ideas votes quit load save help'

load()
try:
    main()
finally:
    if raw_input('do you want to save data? ').lower() in ['y', 'yes']:
        save()

'''
{
    'dule': [('ulepsavanje ovoga programa', 5),...]
}

[('dule', 'ulepsavanje ovoga programa', 5),...]
'''
