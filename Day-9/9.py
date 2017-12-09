import sys, re

tests = {
    '{}': 1,
    '{{{}}}': 6,
    '{{},{}}': 5,
    '{{{},{},{{}}}}': 16,
    '{<a>,<a>,<a>,<a>}': 1,
    '{{<ab>},{<ab>},{<ab>},{<ab>}}': 9,
    '{{<!!>},{<!!>},{<!!>},{<!!>}}': 9,
    '{{<a!>},{<a!>},{<a!>},{<ab>}}': 3
}

def score(s):
    s = re.sub('!.', '', s)
    sc = rubbish = level = rubbish_chars = 0
    for ch in s:
        if not rubbish:
            level += (ch == '{')
            rubbish += (ch == '<')
            sc += (ch == '}') * level
            level -= (ch == '}')
        else:
            rubbish -= (ch == '>')
            rubbish_chars += (ch != '>')
    return sc, rubbish_chars

print('Test results: {:s}'.format('pass' if all(score(x[0])[0] == x[1] for x in tests.items()) else 'fail'))
print('Part 1: {:d}\nPart 2: {:d}'.format(*score(sys.stdin.read())))
