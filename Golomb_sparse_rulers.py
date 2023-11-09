#MATH2920 Miniproject Sparse Rulers Template File

#import files here
import itertools, math
#Part 1
#Q1(a) # take as input a list representing a sparse ruler and return its reach and order, respectively.
def reach(myruler):
    return myruler[-1]



def order(myruler):
    return len(myruler)



#Q1(b)
def isitaruler(mylist):

    if mylist[0] != 0:
        return False

    for i in range(len(mylist)-1):
        if mylist[i] >= mylist[i+1] or not isinstance(mylist[i], int):
            return False

    if not isinstance(mylist[i+1], int):
        return False

    return True








# #Q1(c) returns a list of all sparse rulers of reach nand order k

def sparsenkrulers(n,k):
    listofrulers = []
    listofcombinations = list(itertools.combinations(list(range(1,n)), k-2))
    for i in range(len(listofcombinations)) :

        removedcombination = list(listofcombinations.pop(0))
        removedcombination.insert(0,0)
        removedcombination.append(n)
        listofrulers.append(removedcombination)
        listofrulers.append(removedcombination)

    return listofrulers




# #Q1(d)  takes as input a list representing a sparse ruler of reach N and returns True if it is complete and False otherwise
def ismyrulercomplete(myruler):
    hitcount = 0
    listofdifferences = []
    for i in range(len(myruler)):
        for j in range(i+1,len(myruler)):
            listofdifferences.append(myruler[j]-myruler[i])



    for k in range(1, myruler[-1] + 1):
        for number in listofdifferences:
            if k == number:
                hitcount = hitcount + 1
                break

    if hitcount == myruler[-1] :
        return True
    else:
        return False




# #Part 2
# #Q2(a) takes as input a list representing a sparse ruler of reach N and returns True if it is Golomb and False otherwise.
def ismyrulergolomb(myruler):
    hitcount = 0
    listofdifferences = []
    for i in range(len(myruler)):
        for j in range(i+1,len(myruler)):
            listofdifferences.append(myruler[j]-myruler[i])

    for k in listofdifferences :


        if listofdifferences.count(k) == 1 :
            hitcount = hitcount +1

    if hitcount == len(listofdifferences):
        return True
    else:
        return False



# #Q2(b) i
def listofgolombrulers(n):
    listofgolombrulers = []
    listofrulers = []
    for i in range(1,n) :

        listofcombinations = list(itertools.combinations(list(range(1,n)),i))

        for j in range(len(listofcombinations)) :

            removedcombination = list(listofcombinations.pop(0))
            removedcombination.insert(0,0)
            removedcombination.append(n)

            listofrulers.append(removedcombination)



    for k in range(len(listofrulers)):
        listofdifferences = []
        removedruler = list(listofrulers.pop(0))
        for i in range(len(removedruler)):
            for j in range(i+1,len(removedruler)):
                listofdifferences.append(removedruler[j]-removedruler[i])
        hitcount = 0
        for k in listofdifferences :


            if listofdifferences.count(k) == 1 :
                hitcount = hitcount +1

        if hitcount == len(listofdifferences):
            listofgolombrulers.append(removedruler)



    return listofgolombrulers






#Q2 b ii
# function to find complete rulers

def listofcompleterulers(n):
    completerulers = []
    listofrulers = []
    for i in range(1,n) :

        listofcombinations = list(itertools.combinations(list(range(1,n)),i))

        for j in range(len(listofcombinations)) :

            removedcombination = list(listofcombinations.pop(0))
            removedcombination.insert(0,0)
            removedcombination.append(n)

            listofrulers.append(removedcombination)



    for k in range(len(listofrulers)):
        listofdifferences = []
        removedruler = list(listofrulers.pop(0))
        for i in range(len(removedruler)):
            for j in range(i+1,len(removedruler)):
                listofdifferences.append(removedruler[j]-removedruler[i])
        hitcount = 0
        for k in range(1,n+1) :


            if listofdifferences.count(k) > 0 :
                hitcount = hitcount +1

        if hitcount == n:
            completerulers.append(removedruler)



    return completerulers






# #Comment: My function finds golomb rulers as desired. what i have found is that this programme isnt very efficient as I have nested for loops 3 times. It takes < 5 seconds to run for n < 15.
#           However for n > 20 it takes well over a minute to compute the list of golomb rulers. (in fact i am not patient enough to have even waited for results for n > 20 as it is proving to take ages. As i type this i hae been running the function for n = 20 for around 4 minutes and i have still no result )
# for n = 4 found 2 golomb rulers
# for n = 5 found 4 golomb rulers
# for n = 6 found 6 golomb rulers
# for n = 7 found 12 golomb rulers.


# #Q2(c)
def ErdosTuran(m):
    sparseruler = [0]
    for k in range(1,m):
        mark = 2*m*k + ((k**2)%m)
        sparseruler.append(mark)

    return sparseruler

#Comment: testing the erdos turan generator of sparse rulers. I am going to check if the rulers produced are golomb by putting them into my function ismyrulergolomb(my ruler)
#Below are the rulers produced from the ErdosTuran, after which i check if these rulers are golomb.
# What i realised is that when the argument m = prime number in the ErdosTuran function it will produce a golomb ruler. and If m isnt prime then the ruler produced isnt golomb.
# see evidence commented below.

#ErdosTuran(3)
# Out[83]: [0, 7, 13]
# ismyrulergolomb([0, 7, 13])
# Out[92]: True

# ErdosTuran(4)
# Out[84]: [0, 9, 16, 25]
# ismyrulergolomb([0, 9, 16, 25])
# Out[93]: False

# ErdosTuran(5)
# Out[85]: [0, 11, 24, 34, 41]
# ismyrulergolomb([0, 11, 24, 34, 41])
# Out[94]: True

# ErdosTuran(6)
# Out[86]: [0, 13, 28, 39, 52, 61]
# ismyrulergolomb([0, 13, 28, 39, 52, 61])
# Out[95]: False

# ErdosTuran(7)
# Out[87]: [0, 15, 32, 44, 58, 74, 85]
# ismyrulergolomb([0, 15, 32, 44, 58, 74, 85])
# Out[96]: True

# ErdosTuran(8)
# Out[88]: [0, 17, 36, 49, 64, 81, 100, 113]
# ismyrulergolomb([0, 17, 36, 49, 64, 81, 100, 113])
# Out[97]: False

# ErdosTuran(9)
# Out[89]: [0, 19, 40, 54, 79, 97, 108, 130, 145]
# ismyrulergolomb([0, 19, 40, 54, 79, 97, 108, 130, 145])
# Out[99]: False

# ErdosTuran(10)
# Out[90]: [0, 21, 44, 69, 86, 105, 126, 149, 164, 181]
# ismyrulergolomb([0, 21, 44, 69, 86, 105, 126, 149, 164, 181])
# Out[100]: False

# ErdosTuran(11)
# Out[91]: [0, 23, 48, 75, 93, 113, 135, 159, 185, 202, 221]
# ismyrulergolomb([0, 23, 48, 75, 93, 113, 135, 159, 185, 202, 221])
# Out[101]: True




#Part 3
# Using the Rusza lindstram construction to buikd golomb rulers. These rulers will have P-1 markings.
# p is a prime number , g is a primitive root of p, and s is coprime to p-1
# Given a prime number p, the task is to find its primitive root under modulo p. The primitive root of a prime number p is an integer g between[1, p-1] such that the values of g^x(mod p) where x is in the range[0, n-2] are different. ref (https://www.geeksforgeeks.org/primitive-root-of-a-prime-number-n-modulo-n/)

def ruszalindstrom(p,g,s) :
    golombruler = []
    for k in range(p-1) :
        mark = ((p*s*k)+(p-1)*(g**k))%(p*(p-1))
        golombruler.append(mark)
    # the sequence produced at this stage is not a golomb ruler, or a ruler of any sort for that matter as the markings arent in ascending order. so used the sort function to get them in ascending order.
    golombruler.sort()
    # finally the ruler produced at this stage needs to be renormalized (start at 0) so whatever the difference between mark 1 and 0 is must be subtracted from every subsequent mark also.

    difference = golombruler[0]
    for i in range(len(golombruler)) :
        golombruler[i] = golombruler[i] - difference
    return golombruler

# using p = 13 , g = 2 , and s = 5 produces the ruler [0, 8, 15, 17, 18, 62, 81, 85, 115, 131, 136, 142]
# double checked thus in my is my ruler golomb function and oit returned true so the construction i coded works.
# Something new to me in this coonstruction is the idea of a primitive root g. I am going to write code to find the primitive root of p and also number s which is coprime to p-1.

def primitiveroot(p) : # p is prime

    for g in range(2,p) :
        listofmodvalues = [] #for the number i to be a primitive root it must have all g^x (mod p) for g in range [1,p-1]  and x in range [1,p-2]
        for x in range(p-1) :

            listofmodvalues.append((g**x)%p)
            # if the values are repeated then it isnt primitive root, if the values are unique then it is.
        hitcount = 0
        for element in listofmodvalues:
            if listofmodvalues.count(element) == 1 :
                hitcount = hitcount +1
        if hitcount == len(listofmodvalues) :
            return g
        # returns the smallest primitive root of prime number inserted as the argument.



def coprime(p) : # finding smallest coprime number to p-1
    for i in range(2,p):
        if math.gcd(p-1,i)==1 :
            return i



# now i thought i would look into what different golomb rulers look like for rusza-lindstram construction. To produce each ruler i will use prime numbers from 7 - 31 inclusive. Also using smallest copirme number to p-1 and smallest primitive root of the prime number also. I will call the functions i have created.
# g and s found using primitive root function and coprime function respectively.

# ruszalindstrom(7,3,5)     returns : [0, 5, 9, 31, 32, 34]   (58.9% complete)
# ruszalindstrom(11,2,3)    returns : [0, 17, 35, 43, 58, 59, 62, 64, 71, 96]    (54.2% complete)
# ruszalindstrom(13,2,5)    returns : [0, 8, 15, 17, 18, 62, 81, 85, 115, 131, 136, 142]    (54.2% complete)
# ruszalindstrom(17,3,3)    returns : [0, 14, 37, 39, 43, 61, 92, 97, 118, 127, 130, 137, 138, 200, 244, 259]    (54.1% complete)
# ruszalindstrom(19,2,5)    returns : [0, 6, 13, 58, 73, 75, 119, 141, 218, 221, 226, 230, 250, 251, 261, 277, 300, 314]    (51.6% complete)
# ruszalindstrom(23,5,3)    returns : [0, 62, 104, 136, 157, 160, 190, 209, 217, 218, 257, 325, 329, 335, 340, 342, 360, 376, 405, 419, 431, 469]    (51.0% complete)

# the reach of these rulers begins to get large as the prime number used gets bigger. Out of curiosity I will use prime number 97 for one try and see if it runs.
# ruszalindstrom(97,5,5) copying the result of this seems pointless however the reach of this ruler is 9085. it was 49.8% complete.


#i thought i would look int how close the rulers are to being complete by making a list of the distances it cannot measure directly. and see how close to optimal the rulers produces bu the ruszalindstrom construction are.
# this function returns a proportion of how many lenghts can be measured over the reach of the ruler
def howcomplete(ruler) :
    listofdifferences = []
    missingdistances = []
    for i in range(len(ruler)):
        for j in range(i+1,len(ruler)):
            listofdifferences.append(ruler[j]-ruler[i])
    for j in range(ruler[-1]) :

        if listofdifferences.count(j) == 0 :
            missingdistances.append(j)
    return len(missingdistances)/ruler[-1]

# this is how i was able to give a 'percentage competeness' to each of the rusza lindstrom rulers above. What i noticed is that as the length and size of prime number chosen increased the 'completeness' of the ruler decreases.
# ruszalindstrom(191,19,3)   50.2% complete. so as it seems the rusza lindstrom method produces roughly 50 percent complete rulers which is quite remarkable as this ruler has reach of 36061, only requires 190 markings to measure half of all the distances up to 36061.
