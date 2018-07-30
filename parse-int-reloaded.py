def parse_int(string):
    int_list = string.split()
    print('int_list:', int_list)
    number = ''
    
    ones_dict = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    teens_dict = {
        'ten': 10,
        'eleven': 11,
        'twelve': 12,
        'thirteen': 13,
        'fourteen': 14,
        'fifteen': 15,
        'sixteen': 16,
        'seventeen': 17,
        'eighteen': 18,
        'nineteen': 19
    }
    tens_dict = {
        'twenty': 20,
        'thirty': 30,
        'forty': 40,
        'fifty': 50,
        'sixty': 60,
        'seventy': 70,
        'eighty': 80,
        'ninety': 90
    }
    others_dict = {
        'hundred': '00',
        'thousand': '000',
        'million': '000000'
    }

    def lookup(num_string):
        if '-' in num_string:
            a, b = num_string.split('-')
            return str(tens_dict[a])[0] + str(ones_dict[b])
        try:
            return str(ones_dict[num_string])
        except:
            pass
        try:
            return str(teens_dict[num_string])
        except:
            pass
        try:
            return str(tens_dict[num_string])
        except:
            pass
        try:
            return others_dict[num_string]
        except:
            pass
        return ''

    last = ''
    for each in int_list:
        print('last', last)
        print('each', each)
        print('lookup(each):', lookup(each))
        if last == 'hundred':
            if '-' in each or each in teens_dict:
                number = number[:-2]
            elif each == 'thousand':
                pass
            elif each == 'and':
                pass
            else:
                number = number[:-1]
        if last == 'thousand':
            if '-' in each:
                number = number[:-2]
            elif each == 'and':
                pass
            else:
                number = number[:-1]
        if each == 'hundred' and len(number) > 3:
            number = number[:-3] + lookup(last) + '00'
        else: 
            number = number + lookup(each)
        if each != 'and':
            last = each
        print('number:', number)
        
    print('final number:', number)

    return int(number)
