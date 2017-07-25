import pickle
import nester
man = []
new_man = []
other = []
new_other = []

try:        
        data = open("sketch.txt")

        for each_line in data:
                try:
                        (role,line_spoken)=each_line.split(':',1)
                        line_spoken=line_spoken.strip()
                        if role == 'Man':
                                man.append(line_spoken)
                        elif role == 'Other Man':
                                other.append(line_spoken)
                        #print(role,end='')
                        #print(' said:',end='')
                        #print(line_spoken,end='')
                except ValueError:
                        pass

        data.close()
except IOError:
        print('The data file is missing.')

try:
        with open('man_data.txt','wb') as man_file, open('other_data.txt','wb') as other_file:
                pickle.dump(man,man_file)
                pickle.dump(other,other_file)
        with open('man_data.txt','rb') as man_file, open('other_data.txt','rb') as other_file:
                new_man = pickle.load(man_file)
                new_other = pickle.load(other_file)                
except IOError as err:
        print('File error:'+str(err))
except pickle.PickleError as perr:
        print('Pickling error:'+ str(perr))

nester.print_lol(new_man)
print("==============================================")
nester.print_lol(new_other)

