def make_readable(seconds):
    minutes = seconds/60
    seconds_remainder = seconds%60
    hours = minutes/60
    minutes_remainder = minutes%60
    if hours<10:
        hours = '0' + str(hours)
    else:
        hours = str(hours)
    if minutes_remainder<10:
        minutes = '0' + str(minutes_remainder)
    else:
        minutes = str(minutes_remainder)
    if seconds_remainder<10:
        seconds = '0' + str(seconds_remainder)
    else:
        seconds = str(seconds_remainder)
    return hours+":"+minutes+":"+seconds