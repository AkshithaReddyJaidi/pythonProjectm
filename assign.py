1.
# given list
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# sorting by using sort method
ages.sort()
print("The Sorted List is : ", end='')
''' printing the sorted list'''
print(ages)

# finding min and max value
min_value = ages[0]
max_value = ages[-1]
''' printing the minimum and maximum values in list'''
print("The Minimum value is : " + str(min_value))
print("The Maximum value is : " + str(max_value))

# adding min and max values to list using append and printing the modified list
ages.append(min_value)
ages.append(max_value)
print("The Modified list : ", end='')
print(ages)

# finding the median age
# using len method we are checking whether  the length is even or odd accordingly we are finding the median
if len(ages) % 2 != 0:
    median = ages[len(ages) // 2]
else:
    median = (ages[len(ages) // 2] + ages[(len(ages) // 2) - 1]) / 2
print("The Median value is : " + str(median))

# finding average age by total sum of ages/ no of ages and printing the result
average_age = sum(ages) // len(ages)
print("The Average age is : " + str(average_age))

# finding range of ages by picking maximum and minimum from ages and we perform maximum-minimum and printing the result
range_of_age = max(ages) - min(ages)
print("The Range of ages is : " + str(range_of_age))

#creating dog dictionary
# first we create empty dictionary and then we assign key and values to the dog dictionary and print them
dog=dict()
dog["Name"]="Rocky"
dog["Color"]="White"
dog["Breed"]="Husky"
dog["legs"]=4
dog["Age"]=5
print("Dog dictionary is : ",dog)
print()

#creating student dictionary
#first we create student dictionary and then assign keys and values to thatand print them
student=dict()
student["first_name"]="Akshitha"
student["last_name"]="Akki"
student["Gender"]="Female"
student["Age"]=22
student["Martal status"]="single"
student["Skills"]=["python","Java","AWS"]
student["Country"]="India"
student["City"]="Nizamabad"
student["Address"]="street number 1"
print("Student dictionary is : ",student)
print()

# we are finding the length of the student dictionary by len method
print("The length of student dictionary is : ",str(len(student)));

#we are finding values of student skills
print("The student skills are : ",end='')
print(student["Skills"])
# we are finding datatype of students by using type method
print("Types of student skills is : ",type(student["Skills"]))

#modifying student skills by using append method which will add these values inside the skills
student["Skills"].append("Problem solving")
student["Skills"].append("Analytical skills")
print("The modified student skills are : ",student["Skills"])

#we are using keys and values method to retrive dictionary keys as list and printing them
dog_keys=list(dog.keys())
print("The dog dictionary keys are : ",dog_keys)
student_keys=list(student.keys())
print("The student dictionary keys are : ",student_keys)
dog_values=list(dog.values())
print("The dog dictionary values are : ",dog_values)
student_values=list(student.values())
print("The student dictionary values are : ",student_values)

#creating tuples for brothers and sisters and we are printing them
sisters=("Akkis","Aka")
brothers=("Broth1","Broth2","Broth3","Broth4","Broth5")
print("The brothers are : ",brothers)
print("The sisters are : ",sisters)

#joining brothers and sisters tuples to siblings using + and printing the length of siblings using len method
siblings=brothers+sisters
print("The siblings are : ",siblings)
print("The number of siblings are : ",len(siblings))
#we are modifying siblings tuple by adding father name and mother name and printing the updated tuple
family_members=("father","mother")+siblings
print("The family members are : ",family_members)
#given list of it companies
it_companies={"Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"}
A={19,22,24,20,25,26}
B={19,22,20,25,26,24,28,27}
age=[22,19,24,25,26,24,25,24]
print("length of it_companies : ",len(it_companies))

#we are ising add method to add twitter to it_companies and print them
it_companies.add("Twitter")
print("The it_companies after adding twitter :",it_companies)

#we are inserting multiple it companies to it_companies and printing them
companies=["NCR","Wipro","TCS"]
it_companies.update(companies)
print("The it_companies after adding multiple companies :",it_companies)

#we are using remove method for removing one company
it_companies.remove("Twitter")
print("The it_companies after removing one company : ",it_companies)
''' 2 e '''
#Difference between remove and discard method
#The remove() method will raise an error if the specified item does not exist, and the discard() method will not raise error.

#we are joining A and B using union method
C=A.union(B)
print("Joining A and B gives :",C)

#we are finding A intersection B using intersection method
I=A.intersection(B)
print("Intersection of A and B is:",I)

#we are checking is A subset of B using issubset method and printing using if block if it is true or false
check=A.issubset(B)
if check:
    print("A is subset of B")
else:
    print("A is not a subset of B")

#we are checking  A and B are disjoint sets using isdisjoint method
check1=A.isdisjoint(B)
if check1:
    print("A and B are disjoint sets")
else:
    print("A and B are not disjoint sets")

#we are joining A with B and B with A using union method and printing them
A_join_B=A.union(B)
B_join_A=B.union(A)
print("A join B is :",A_join_B)
print("B join A is :",B_join_A)

#we are calculating symmetric difference between A and B using symmetric_difference method
D=A.symmetric_difference(B)
print("symmetric difference between A and B is :",D)

#we are deleting all the sets using clera method
it_companies.clear()
A.clear()
B.clear()

#we are converting ages list to set using set method and calculating the length of set and list and printing the greatest length
age_set=set(age)
print("length of ages list is : ",len(age))
print("length of ages set is :",len(age_set))
print("length of ages list is greater than the ages set")

#area of circle
#Given radius of circle 30 meters
r=30
#assigned variable name to  "_area_of_circle"
_area_of_circle=3.17*(r**2)
 #printing the stored value in variabale
print("The area of circle :",_area_of_circle)
#circumference of circle
#assigned value to "_circum_of_circle"
_circum_of_circle=2*3.17*r
#printing the value
print("The circumference of circle :",_circum_of_circle)

#area of circle for user input
#taking the user input using input method
n=int(input())
#assigned the result to"area"
area=3.17*(n**2)
#printing the value
print("The Area of circle with user input :",area)


# given string to the variable a
A="I am a teacher and I love to inspire and teach people"
# split the given string using split method
B=A.split()
# used set to remove duplicates
set1=set(B)
# used len to count number of words
count=len(set1)
# printing the value
print(count)
#tab escape
# declaring a string to the txt variable and using \t for spaces and \nfor next line
txt = "Name\tAge\tCountry\tCity\nAsabench\t250\tFinland\tHelsinki"
#print the requried output
print(txt)

#assigned variable radius
radius=10
#assigned area of circle formula
area=3.14 * radius ** 2
#print the output using string format using format method
print("The area of circle with radius {} is {} meters square".format(radius,area))


#we take no of stdents through keyboard
n=int(input("Enter number of student's weight to be calculated"))
weights_in_lbs=[]
weights_in_kg=[]
#appending the elements into the list and printing lbs in list
for i in range(n):
    weights_in_lbs.append(int(input("weight {} \n".format(i+1))))
print(weights_in_lbs)
#converting lbs to kilogram with exactly 2 decimal places &printing that in another list
for i in range(len(weights_in_lbs)):
    lbs=0.45359237 #1lbs= 0.45359237kg
    temp=round(weights_in_lbs[i]*lbs,2)
    weights_in_kg.append(temp)
    temp=0
print(weights_in_kg)