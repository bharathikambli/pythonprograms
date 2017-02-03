import pickle


my_list = [1,2,3,4,5]
my_dict = {'name':'bharathi'}
my_str = 'asm tech'
f = open('newfile.txt','w')
pickle.dump(my_list,f)
pickle.dump(my_dict,f)
f.close() 

