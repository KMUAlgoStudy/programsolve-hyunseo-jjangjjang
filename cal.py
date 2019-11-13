eval_str = input()
eval_list = []
oper = ['(',')','^','*','/','+','-']


def eval_split(eStr):
    eList = []
    idx = 0
    while eStr != '':
        print('hi : ' + eStr)
        if idx == len(eStr):
            eList.append(eStr[:])
            break
        if eStr[idx] in oper:
            eList.append(eStr[:idx])
            eList.append(eStr[idx])
            eStr = eStr[idx+1:]
            idx = 0
        else:
            idx += 1

    while '' in eList:
        eList.remove('')

    return eList

op_func = {
    '^':lambda a,b : int(a)^int(b),
    '*':lambda a,b : int(a)*int(b),
    '/':lambda a,b : int(a)/int(b),
    '+':lambda a,b : int(a)+int(b),
    '-':lambda a,b : int(a)-int(b),

}


def calc(eList):
    if '(' in eList:
        open_idx = eList.index('(')
        close_idx = len(eList) - list(reversed(eList)).index(')')
        eList = eList[:open_idx] + [calc(eList[open_idx + 1:close_idx-1])] + eList[close_idx+1:]

    for op in oper:
        while op in eList:
            idx = eList.index(op)
            result = op_func[op](eList[idx - 1], eList[idx + 1])
            eList = eList[:idx-1] + [str(result)] + eList[idx +2:]

    return int(eList[0])


eval_list = eval_split(eval_str)
#eval_list = ['2','*','(','1','+','1',')']
print(eval_list)
re = calc(eval_list)
print(re)
