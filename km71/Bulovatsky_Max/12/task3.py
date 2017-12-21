def count(list,i,counter):
	if i < len(list):
	    m = findGroup(list,i,0,1)
	    if counter < m[0]:
	        counter = m[0]
	    return count(list,i + 1,counter)
	else:
	    return counter    


def findGroup(list,i,indicator,k):
    if i < len(list) - 1 and list[i] == list[i + 1]:
        k = k + 1        
        return findGroup(list,i + 1,indicator,k)
    else :
        return k,indicator


list = input("please write a list ").split()
print(count(list,0,0))
input()
