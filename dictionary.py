#### Dictionary Questions ####
##############################

# dict1={1:10, 2:20}
# dic2={3:30,4:40}
# dic3={5:50,6:60}
# dict1.update(dic2)
# dict1.update(dic3)
# print(dict1)

##############################

# a=input("Enter the keys :")
# dict1={"name":"Raju", "marks":56}
# if a in dict1:
#     print("Key already exist in the dictionary :")
# else:
#     print("Key not exist in the dictionary :")

##############################

# my_dict = {
#     'data1':100,
#     'data2': -54,
#     'data3': 247
#     } 
# c=0
# for i in my_dict.values():
#     c+=i
# print(c)

##############################

# Dic= {
#     1: 'NAVGURUKUL',
#     2: 'IN',  
#     3:{    
#             'A' : 'WELCOME',
#             'B' : 'To',
#             'C' : 'DHARAMSALA'
#         }
#     }
# del Dic[3]['A']
# print(Dic)

###############################

# list1=["one","two","three","four","five"]
# list2=[1,2,3,4,5]
# a={}
# for i in range (len(list1)):
#     a[list1[i]]=list2[i]
# print(a)

###############################

# dic={
#     "ball":"red",
#     "bat":4,
#     "wickets":8,
#     "ball":"green",
#     "bat":3
#     }
# print(dic)

################################

# a=[
#      {"first":"1"}, 
#      {"second": "2"}, 
#      {"third": "1"}, 
#      {"four": "5"}, 
#      {"five":"5"}, 
#      {"six":"9"},
#      {"seven":"7"}
# ]
# b=[]
# for i in a:
#     for j in i.values():
#         if j not in b:
#             b.append(j)
# print(b)

##################################

# a=int(input("Enter the students name and values :"))
# b={}
# for i in range (a):
#     c=input("Enter the name :")
#     d=int(input("Enter the students marks :"))
#     b[c]=(d)
# print(b)

####################################

# a="MISSISSIPPI"
# b={}
# for i in a:
#     d=a.count(i)
#     b[i]=(d)
# print(b)

######################################

# dict1 =  {
#    'Alex': ['subj1', 'subj2', 'subj3'], 
#    'David': ['subj1', 'subj2']}
# b=0
# for i in dict1.values():
#     for j in i:
#         b+=1
# print("Total count = ",b)

######################################

# my_dict = {
#     'a':500, 
#     'b':58, 
#     'c':560,
#     'd':40, 
#     'e':100, 
#     'f':20
#     }
# a=[]
# for i in my_dict.values():
#     a.append(i)
#     a.sort()
# print(a[3:])

########################################

# a=int(input("Enter the number :"))
# b={}
# for i in range (a):
#     c=int(input())
#     b[c]=(c*c)
# print(b)

################################

# details={
#     "name":"Shanti",
#     "age":12,
#     "email":"shanti@navgurukul.org",
#     }
# print(details["name"])
# print(details["email"])
# print(details["age"])

#################################

# dict1={1:2,2:3,3:4,4:5}
# sum=0
# for i in dict1.values():    
#     sum=sum+i
# print(sum) 

#################################

# c=dict()
# for i in range(1,16):
#     c[i]=i*i
# print(c)


###################################

# my_dict = {
#     'a':50, 
#     'b':58,
#     'c': 56,
#     'd':40,
#     'e':100, 
#     'f':20
#     } 
# b=sorted(my_dict.values())
# s=b[-3:]
# s.reverse() 
# print(s)
# a=[]
# for i in s:
#     for j, k in zip(my_dict.values(),my_dict.keys()):
#         if i == j :
#             a.append(k)                      
# print(a)

##################################

# a={'bijender':45,'deepak':60,"param":20,"anjili":30,"roshini":50}
# d={}
# for i,j in zip(a.values(),a.keys()):
#     d[i]=j
# list1=[]
# for i in d:
#     list1.append(i)
# list1.sort()
# a=[]
# d2={}
# for j in list1:
#     for i,k in zip(d.values(),d.keys()):
#         if j==k:
#             d2[i]=j
# print("Assending order :",d2)
# a={'bijender':45,'deepak':60,"param":20,"anjili":30,"roshini":50}
# d={}
# for i,j in zip(a.values(),a.keys()):
#     d[i]=j
# list1=[]
# for i in d:
#     list1.append(i)
# list1.sort(reverse=True)
# a=[]
# d2={}
# for j in list1:
#     for i,k in zip(d.values(),d.keys()):
#         if j==k:
#             d2[i]=j
# print("Dessending order :",d2)




# d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'b': 3, 'a': 2}
# d2 = {}
# list1=[]
# list2=[]
# for key,value in d1.items():
#     print(value)
#     if key not in list1:
#         list1.append(key)
#     if value not in list2:
#         list2.append(value)
# list2.insert(0,1)
# print(list1)
# print(list2)
# for i in range (len(list1)):
#     d2[list1[i]]=list2[i]
# print(d2)


###########################################
#### w3recourse dictionary questions ######
###############################
#### add sum of all values ####

# a=int(input())
# b=0
# c={}
# for i in range (a):
#     e=input()
#     d=int(input())
#     c[e]=d
# for j in c.values():
#     b+=j
# print(b)

#################################
#### multiples of all values ####

# a=int(input())
# b=1
# c={}
# for i in range (a):
#     e=input()
#     d=int(input())
#     c[e]=d
# for j in c.values():
#     b*=j
# print(b)

########################################
#### remove the key from dictionary ####

# a={"tus":56,"dh":67,"k":3}
# print(a)
# a.pop("tus")
# print(a)

#########################################################
#### find minimum and maximum value from dictionary #####

# a={"a":45,"f":34,"e":35,"b":2}
# b=[]
# for i in a.values():
#     b.append(i)
#     b.sort()
# print("minimum value of dictionary : ",b[0])
# print("maximum value of dictionary : ",b[-1])

##############################################################
#### combine two dictionary adding values for common keys.####

# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# D3 ={}
# for i,j in zip(d1,d2):
#     if i == j:
#         D3[i] = d1[i]+d2[j]
#     else:
#         D3[i] = d1[i]
#         D3[j] = d2[j]
# print(D3)

##############################################
#### find 3 highest value from dictionary ####

# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
# b=0
# c=[]
# l = []
# for i in my_dict.values():
#     c.append(i)
# for j in c:
#     l.append(max(c))
#     c.remove(max(c))
# print(l)

###############################################
#### remove the spaces from the dictionary ####

# a= {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# c={}
# for i in a:
#     b=i.replace(' ','')
#     for j in a.values():
#         c[b]=j
# print(c)

##############################
#### find 3 maximum value ####

# a= {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# b=0
# c=[]
# l = []
# for i in a.values():
#     c.append(i)
# for j in c:
#     l.append(max(c))
#     c.remove(max(c))
# print(l)

######################################################
#### find the key, value and item in a dictionary.####

# a = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# b=0
# print("key","value","count")
# for i,j in zip(a.keys(),a.values()):
#     b+=1
#     print(i,"  ",j,"  ",b)

##################################################################
#### Write a Python program to print a dictionary line by line.####

# a={'Aex':{'class':'V',
#         'rolld_id':2},
#         'Puja':{'class':'V',
#         'roll_id':3}}
# for i in a:
#     print(i)
#     for j in a[i]:
#         print(j,':',a[i][j])

####################################################################
#### count number of items in a dictionary value that is a list.####

# dic =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# c=0
# for i in dic.values():
#     for j in range (len(i)):
#         c+=1
# print(c)

########################################################
##### replace dictionary values with their average.#####

# def average(a):
#     for d in a:
#         n1 = d.pop('V')
#         n2 = d.pop('VI')
#         d['V+VI'] = (n1 + n2)/2
#     return a
# student_details= [
#   {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
#   {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
#   {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
# ]
# print(average(student_details))

##############################################
#### match key values in two dictionaries.####

# x = {'key1': 1, 'key2': 3, 'key3': 2}
# y = {'key1': 1, 'key2': 2}
# for i,j in zip(x,y):
#     if i==j:
#         if x[i]==y[j]:
#             print(i,':',x[i],"is present in both x and y")

###############################################################
#### Access the fifth value of each key from the dictionary.####

# a={'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
#  'y':   [21, 22, 23, 24, 25, 26, 27, 28, 29],
#  'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
# print(a)
# for i in a.values():
#     if 15 in i:
#         print(15)
#     elif 25 in i :
#         print(25)  
#     elif 35 in i :
#         print(35) 
# for j in a.values():
#     print(j)
        
#########################################################
#### filter a dictionary based on values.marks > 170 ####

# a={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# b={}
# for i,j in zip (a.keys(),a.values()):
#     if j>170:
#         b[i]=j
# print(b)
        
#########################################################
#### convert a given dictionary into a list of lists ####

# a={'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# b=[]
# for i,j in zip (a.keys(),a.values()):
#     b.append([i,j])
# print(b)

# a={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# b=[]
# for i,j in zip (a.keys(),a.values()):
#     b.append([i,j])
# print(b)

########################################################################################
##### get the total length of all values of a given dictionary with string values. #####

# a={'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
# b=0
# for i in a.values():
#     for j in i:
#         b+=1
# print(b)

################################################################
#### create a key-value list pairings in a given dictionary.####

# a={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
# b={}
# for i,j in zip(a.keys(),a.values()):
#     for k in j:
#         b[i]=k
# print([b])
