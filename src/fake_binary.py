def fake_bin(x):
    return_me = ''
    for char in x:
        if int(char) < 5:
            return_me += '0'
        else:
            return_me += '1'
    return return_me