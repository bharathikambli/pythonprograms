#Task-5
===============================================
print "==Reverse of given input=="
def reverse(string): 
    begin = 0 
    end = len(string) - 1 
    strlist = [i for i in string] 
    while(begin < end): 
        temp = strlist[begin] 
        strlist[begin] = strlist[end] 
        strlist[end] = temp 
        begin += 1 
        end -= 1 
    return ''.join(strlist)

print reverse('flash')

#Task-6
==============================================
print "===Reverse of Given List==="
def reverse(d):
    return a[::-1]

d = ["ASM" "Technologies" "ltd"]#using list
print d
print "reverse of given list is :",reverse(d)
