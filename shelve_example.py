import shelve
import pickle

# Creating a shelve

shfile = shelve.open("shelf_file")
my_new_list =['Hello', 'Python','Shelve','item']
shfile['new_list']= my_new_list
shfile['new_list1']= my_new_list

shfile.close()

# print(type(shfile))



# # # Retrieving data from shelve

var = shelve.open("shelf_file")
print(var['new_list'])
print(var['new_list1'])

var.close()







# Updating a shelve

# var = shelve.open("shelf_file", writeback = True)	
# var['new_list'].append("Second item" )
# print(var['new_list'])
# var.close()





# Shelve with pickle

var = shelve.open("shelf_file", writeback = False)	
child1 = {1 : 'One', 2 : 'Two'}
child2 = {3 : 'Three', 4 : 'Four'}
parent_dict = {}
parent_dict['first'] = child1
parent_dict['second'] = child2

b = pickle.dumps(parent_dict)	
var['pickle_values'] =  b
print(var['pickle_values'])
pickled_item =  pickle.loads(var['pickle_values'])
print(pickled_item)
var.close()