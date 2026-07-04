print('<==== D I C T I O N A R Y ====>')
'''
- Stores data in key value pair
- They are unordered, mutable(changeable) & don’t allow duplicate keys

'''

info={
  #   'key':'value',
'name':'Laraib',
'course':['AI','ML','DS'],
'topic':('Dict','set','list','tuple'),
'age':20
}

info["lastname"]="Fatima"
print(info)

# nested dictionary
student={
    "name":"Ali",
    "age":29,
    "grades":{
        "AI":"A",
        "DS":"B",
        "PF":"C+"
    }
}
print(student["grades"])
print(student["grades"]["DS"]) #B

print(student.keys()) # dict_keys(['name', 'age', 'grades'])
print(student.values()) # dict_values(['Ali', 29, {'AI': 'A', 'DS': 'B', 'PF': 'C+'}])


print(list(student.keys()))

print(student.items()) # dict_items([('name', 'Ali'), ('age', 29), ('grades', {'AI': 'A', 'DS': 'B', 'PF': 'C+'})])

print(list(student.items()))

pairs=list(student.items())
print(pairs[1])

# to get dict value we hv 2 ways:
print(student.get("n")) # return None
# print(student["n"]) # returns an error

stu_updated={"city":"Karachi"}
student.update(stu_updated)
print(student)


print("<=== S E T ===>")

# Set is the collection of the unordered items.
# Each element in the set must be unique & immutable.
# sets can have int,float,string, & tuple bcz they are immutable
# list & dictionary is not included bcz they are mutable
# sets are mutable elements inside sets are immutable
# sets values are immuatable nd hashable if we try to mutate it it disrupts the set
set={1,2,2,3,"hello","world",5}
print(set)
print(len(set)) # ignores duplicated items


coll={} # dictionary
print(type(coll))

# collection=set() # empty set syntax

s={1,2,2,3,"hello","world",5}
s.add(4)
s.add((8,9))
# .add(['a','d']) # TypeError: unhashable type: 'list'
# s.clear()
s.remove('hello')
s.pop() # removes random val.
print(s)

set1={1,2,3}
set2={2,3,4}
union=set1.union(set2) # {12,3,4}
intersect=set1.intersection(set2) #{2,3}
print("union -> ",union)
print("intersection ->",intersect)


# ====================================================================================================

print("<==== Let‘s Practice ====>")

# Store following word meanings in a python dictionary 
dict={
    "cat":"a small animal",
    "table":["a piece of furniture","list of facts & figures"]
}
print(dict)

# WAP to enter marks of 3 subjects from the user and store them in a dictionary.
#  Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
marks={}

s1=int(input("Enter marks in s1: "))
marks.update({'s1':s1})
s2=int(input("Enter marks in s2: "))
marks.update({'s2':s2})

s3=int(input("Enter marks in s3: "))
marks.update({'s3':s3})

print(marks)



# You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.

subjects={'python','java','C++','python','javascript','java','python','java','C++','C' }
print(len(subjects))


# Figure out a way to store 9 & 9.0 as separate values in the set. (You can take help of built-in data types)

values={9,9.0} # this will consider both same and just shows {9}
print(values) 


values={("float",9.0),("int",9)}
print(values)
