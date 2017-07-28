def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data=f.readline()
        return (data.strip().split(','))
    except IOError as ioerr:
        print('File error:'+ str(ioerr))
        return(None)

james=get_coach_data('james2.txt')
julie=get_coach_data('julie2.txt')
mikey=get_coach_data('mikey2.txt')
sarah=get_coach_data('sarah2.txt')

(james_name, james_dob)=james.pop(0), james.pop(0)
(julie_name, julie_dob)=julie.pop(0), julie.pop(0)
(mikey_name, mikey_dob)=mikey.pop(0), mikey.pop(0)
(sarah_name, sarah_dob)=sarah.pop(0), sarah.pop(0)

print(james_name + "'s fastest times are: "+ str(sorted(set([sanitize(t) for t in james]))[0:3]))
print(julie_name + "'s fastest times are: "+ str(sorted(set([sanitize(t) for t in julie]))[0:3]))
print(mikey_name + "'s fastest times are: "+ str(sorted(set([sanitize(t) for t in mikey]))[0:3]))
print(sarah_name + "'s fastest times are: "+ str(sorted(set([sanitize(t) for t in sarah]))[0:3]))
