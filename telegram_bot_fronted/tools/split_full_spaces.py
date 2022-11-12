def split_spaces_and_jump(chain:str):
    array = []
    temp = ''
    for i in range(len(chain)):
        if chain[i] != ' ' and chain[i] != '\n':
            temp += chain[i]
        else:
            if temp != '':
                array.append(temp)
            temp = ''
    if temp != '':
        array.append(temp)
    return array