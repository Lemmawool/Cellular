def cellular_automaton(string, pattern, generations):
    i = 0
    l = len(string)
    plist = find_pattern(pattern)
    #print plist
    while i < generations:
        string_list = break_string(string, l)
        numlist = strlist2numlist(string_list, l)
        string = numlist2string(numlist, plist, l)
        i += 1
    return string
    
def find_pattern(p):
    bin_list = [128, 64, 32, 16, 8, 4, 2, 1]
    plist = []
    i = 0
    while p > 0:
        if bin_list[i] <= p:
            p -= bin_list[i]
            plist.append(bin_list[i])
        i += 1
        if i == 8:
            break
    return plist

def string2number(string, l):
    str_list = ['...', '..x', '.x.', '.xx', 'x..', 'x.x', 'xx.', 'xxx']
    num_list = [1, 2, 4, 8, 16, 32, 64, 128]
    i = 0
    while i < 8:
        if (str_list[i] == string):
            return num_list[i]
        i += 1

def break_string(string, l):
    string_list = ['...']*l
    if l==2:
        string_list[0] = '.' + string[0] + string[1]
        return string_list
    if l==1:
        string_list[0] = '..' + string[0]
        return string_list
    string_list[0] = string[l-1] + string[0] + string[1]
    string_list[l-1] = string[l-2] + string[l-1] + string[0]
    if l==3:
        string_list[l-2] = string[0] + string[1] + string[2]
        return string_list
    i = 1
    while i < (l-1):
        string_list[i] = string[i-1] + string[i] + string[i + 1]
        i += 1  
    return string_list
    
def strlist2numlist(strlist, l):
    i = 0
    numlist = []
    while i < l:
        numlist.append(string2number(strlist[i], l))
        i +=1
    return numlist

def numlist2string(numlist, plist, l):
    newstr = ''
    i=0
    while i < l:
        if numlist[i] in plist:
            newstr += 'x'
        else:
            newstr += '.'
        i += 1
    return newstr
    
def s2n_test():
    print string2number('...')
    print string2number('..x')
    print string2number('.x.')
    print string2number('.xx')
    print string2number('x..')
    print string2number('x.x')
    print string2number('xx.')
    print string2number('xxx')

#plist = find_pattern(69)
#print plist
#numlist = strlist2numlist(['...','..x', '.x.', '.xx', 'x..', 'x.x', 'xx.', 'xxx'])
#print numlist2string(numlist, plist)
#s2n_test()
def testHarness():
    print cellular_automaton('.x.x.x.x.', 17, 2)
    #>>> xxxxxxx..
    print cellular_automaton('.x.x.x.x.', 249, 3)
    #>>> .x..x.x.x
    print cellular_automaton('...x....', 125, 1)
    #>>> xx.xxxxx
    print cellular_automaton('...x....', 125, 2)
    #>>> .xxx....
    print cellular_automaton('...x....', 125, 3)
    #>>> .x.xxxxx
    print cellular_automaton('...x....', 125, 4)
    #>>> xxxx...x
    print cellular_automaton('...x....', 125, 5)
    #>>> ...xxx.x
    print cellular_automaton('...x....', 125, 6)
    #>>> xx.x.xxx
    print cellular_automaton('...x....', 125, 7)
    #>>> .xxxxx..
    print cellular_automaton('...x....', 125, 8)
    #>>> .x...xxx
    print cellular_automaton('...x....', 125, 9)
    #>>> xxxx.x.x
    print cellular_automaton('...x....', 125, 10)
    #>>> ...xxxxx
    print cellular_automaton('.x.', 248, 2)
    #>>> 'x..'
    return

testHarness()
