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

james_data={}
james_data['Name']=james.pop(0)
james_data['DOB']=james.pop(0)
james_data['Times']=james

print(james_data['Name']+"'s fastest times are: "+
      str(sorted(set([sanitize(t) for t in james_data['Times']]))[0:3]))
