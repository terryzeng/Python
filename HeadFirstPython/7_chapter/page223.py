import pickle
#from athletelist import AthleteList

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)

class AthleteList(list):
    def __init__(self,a_name,a_bob=None,a_times=[]):
        list.__init__([])
        self.name=a_name
        self.bob=a_bob
        self.extend(a_times)
    def top3(self):
        return (sorted(set([sanitize(t) for t in self]))[0:3])
    
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data=f.readline()
        templ=data.strip().split(',')
        return (AthleteList(templ.pop(0),templ.pop(0),templ))
    except IOError as ioerr:
        print('File error:'+ str(ioerr))
        return(None)

def put_to_store(file_list):
    all_athletes={}
    for each_file in files_list:
        ath=get_coach_data(each_file)
        all_athletes[ath.name]=ath
    try:
        with open('athletes.pickle','wb') as athf:
            pickle.dump(all_athletes,athf)
    except IOError as ioerr:
            print('File error(put_and_store):'+str(ioerr))
    return(all_athletes)

def get_from_store():
    all_athletes={}
    try:
        with open('athletes.pickle','rb') as athf:
            all_athletes=pickle.load(athf)
    except IOError as ioerr:
            print('File error(get_from_store):'+str(ioerr))
    return(all_athletes)

the_files=['sarah.txt','james.txt','mikey.txt','julie.txt']
data=put_to_store(the_files)
for each_athlete in data:
    print(data[each_athlete].name + ' ' + data[each_athlete].dob)

dato_copy=get_from_store()
for each_athlete in data_copy:
    print(data_copy[each_athlete].name + ' ' + data_copy[each_athlete].dob)
