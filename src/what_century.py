def whatCentury(year):
    int_year = int(year)
    cent_block = int(int_year/100)
    if year[0] == '1':
        return str(cent_block + 1) + 'th'
    elif year[1] == '0':
        if year[1:] == '000':
            return str(cent_block) + 'th'
        return str(cent_block + 1) + 'st'
    elif year[1] == '0':
        return str(cent_block + 1) + 'st'
    elif year[1] == '1':
        return str(cent_block + 1) + 'nd'
    elif year[1] == '2':
        return str(cent_block + 1) + 'rd'
    else:
        return str(cent_block + 1) + 'th'