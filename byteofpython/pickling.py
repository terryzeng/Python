#Filename: pickling.py

import cPickle as p

shoplistfile = 'shoplist.data'

shoplist = ['apple', 'mango', 'carrot']

#Write to the file
f = file(shoplistfile, 'w')
p.dump(shoplist, f)
f.close()

del shoplist

#Read back from the storage
f = file(shoplistfile)
storedlist = p.load(f)
print storedlist
