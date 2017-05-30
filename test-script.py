
my_name='steve'
#print my_name

my_age=43
#print my_age




############ Lists

my_family=['Steve', 'Effy', 'Antia']
#for member in my_family: print member

parents=['Dinos','Antonia']
siblings=['Elizabeth','Maria']

extended_family=[]
extended_family.extend(my_family)
#for member in extended_family: print member

extended_family.extend(parents)
#for member in extended_family: print member

extended_family.extend(siblings)
#for member in extended_family: print member

extended_family.insert(0,'Steve\'s Family')
#for member in extended_family: print member

extended_family.insert(4,'Dinos\'s Family')
#for member in extended_family: print member




############ String Formatting

sentence = "%s has a daughter. Her name is %s"
steve = ("steve", "antia")
#print (sentence % steve)
dino = ("dino", "elizabeth")
#print (sentence % dino)


number=4.54
#print number

number='%i'%(4.54)
#print number

number='%f'%(4.54)
#print number

number='%e'%(4.54)
#print number

number='%x'%(15)
#print number




############ Conditions

a=20
b=10

#if(a>b):
#    print ("%i is greater than %i" % (a,b)) 
#else:
#    print ("%i is greater than %i" % (b,a)) 



############ Loops
a=0
while a<10:
        print a
        a=a+1

week =['Mon','Tus','Wed','Thu','Fri','Sat','Sun']
for item in week:
    if item == 'Sat':
        print 'Weekend '     
    print item




