

import pickle


# Functions provided by pickle
# 1. pickle.dump()
# 2. pickle.dumps()
# 3. pickle.load()
# 4. pickle.loads()

# def storeData():
# 	child1 = {'key' : 'World', 'value' : 'World'}
# 	child2 = {1 : 'One', 2 : 'Two'}

# 	parent_dict = {}
# 	parent_dict['first'] = child1
# 	parent_dict['second'] = child2
	
# 	picklefile = open('examplePickle', 'wb')
	
# 	# source, destination
# 	pickle.dump(parent_dict, picklefile)					
# 	picklefile.close()



# def storeData():

# 	child1 = {'key' : 'World', 'value' : 'World'}
# 	child2 = {1 : 'One', 2 : 'Two'}

# 	parent_dict = {}
# 	parent_dict['first'] = child1
# 	parent_dict['second'] = child2
    
# 	b = pickle.dumps(parent_dict)	
# 	print(b)
# 	print(type(b)) 
# 	parent_slice = (2,34,5)
# 	b = pickle.dumps(parent_slice)	
# 	print(b)
# 	print(type(b)) 



# def loadData():
# 	pickle_file = open('examplePickle', 'rb')	
# 	parent_dict = pickle.load(pickle_file)
# 	for keys in parent_dict:
# 		print(keys, '=>', parent_dict[keys])
# 	pickle_file.close()


# def loadData():

# 	parent_slice = (2,34,5)
# 	b = pickle.dumps(parent_slice)
# 	value  = pickle.loads(b)
# 	print(value)






class Person:
	def __init__(self,name, age):
		self.name = name
		self.age = age
	def print_person(self):
		print('Hello ' + self.name)

# j = Person("James",20)
# jfile = open("james.pickle",'wb')
# pickle.dump(j,jfile)
# jfile.close()


jfile =  open("james.pickle",'rb')
j = pickle.load(jfile)
j.print_person()

# storeData()
# loadData()
