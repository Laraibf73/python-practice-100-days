'''
File Input/Output 
types of Files:
   - Text File: Data is stored in a form of character format (.txt, .log, .docx etc)
   - Binary File:In 0's & 1's format (.mp4, .png etc.)
'''


f=open("demo.txt",'r')
data=f.read()
print(data)
print(type(data))
f.close()

#Space after first line bcz after first line there is '\n' which we can't see. After both line there is a space bcz pointer reaches at the end and there is notthing to be outputed.
f=open("demo.txt",'r')
data=f.read()
print(data)

line1=f.readline() # reads one line at a time.
print(line1)

line2=f.readline()
print(line2)
f.close()



'''
Writing to a file
Modes:
'w': (overwrites in a file) writes and truncates
'a': (modifies a file) write & adds in the end of a file {appends}
'''
f=open("demo.txt",'w')
data=f.write("I will learn pycharm")
f.close()

f=open("demo.txt",'a')
data=f.write("\nAfter it I will be learning ML")
f.close()

f=open("sample.txt",'a')
data=f.write("If file doesn't exist it will automatically creates a new file.")
f.close()

# 'r+' read+overwrite -> No truncate (ptr starts)
# 'w+' read+overwrite -> truncates
#'a+'  read+ append   -> No truncate (ptr ends)

# Now If we and to read & write in a file. (reads & appends at the start of a file.)
f=open("demo.txt",'r+')
f.write("abc")
print(f.read()) # s is a Sample File. {as the stram cusrsor is after abc that's why output is from s...}
f.close()



# Now If we and to read & write in a file. (reads & truncates  a file {wipe out}.)
f=open("demo.txt",'w+')
print(f.read()) #empty
f.write("abc")
f.close()


f=open("demo.txt",'a+')
print(f.read())
f.write("abc")
f.close()



# With syntax : No nned to write close() bcz it is done automatically.
with open('demo.txt','r') as f:
   data=f.read()
   print(data)

with open('demo.txt','w') as f:
   f.write("THis will vanishes previous text.")



#Deleting a file we have to import a module(built-in lib)
import os
os.remove("sample.txt")


# Lets Practice
'''
Create a new file “practice.txt” using python. Add the following data in it:
WAF that replace all occurrences of “java” with “python” in above file.
Search if the word “learning” exists in the file or not.
'''

def  create_file():    
      with open("practice.txt",'w') as f:
         f.write("Hi everyone\nwe are learning File I/O\nusing Java.")
         f.write("\nI like programming in Java")
   
def replace_find_word():
      with open("practice.txt",'r') as f:
         data=f.read()
         new_data=data.replace('Java', 'Python')
         print(new_data)
         if(new_data.find("learning")!=-1):
            print("Found!")
         else:
            print("Not Found!")
  
      with open("practice.txt",'w') as f:
         f.write(new_data)
  
create_file()
replace_find_word()


#WAF to find in which line of the file does the word “learning”occur first.Print -1 if word not found.
def find_word_lineno():
   word='learning'
   data=True
   lineno=1
   with open("practice.txt",'r') as f:
      while data:
         data=f.readline()
         if word in data:
            return lineno
         lineno+=1
   return -1

print(find_word_lineno())

#From a file containing numbers separated by comma, print the count of even numbers.
count=0
with open("practice1.txt",'r') as f:
   data=f.read()
   num=data.split(",")
   print(num) 
   for val in num:
      if(int(val)%2==0):
         count+=1
   print(count)
      

      
      







'''
In Python, file input and output (I/O) is performed using the built-in open() function, which creates a file object to read,
 write, or append data. The most efficient and safe practice is to use the with statement, which automatically closes the file
  after operations are complete to prevent data corruption.
  Core File ModesWhen opening a file, you must specify a mode depending on the task:

  Mode      Action             Behavior
  'r'       Read (Default)     Opens a file for reading; throws an error if it does not exist.
  'w'       Write              Overwrites existing content or creates a new file.
  'a'       Append             Adds new content to the end without modifying existing data.
  'b'       Binary             Handles non-text files like images or executables (e.g., 'rb', 'wb').
'''