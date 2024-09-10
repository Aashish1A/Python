     # File Handling
     
##Readind a File
     
##f=open('fun.txt',"r")
##text=f.read()
##print(text)
##f.close()
 
#Writing to a file

##f=open("fun.txt","w")
##f.write("Hello world")
##f.close()

# Append a file

##f=open("fun.txt","a")
##f.write("Python is a fun")
##f.close()

# readlines meethod

##f=open("fun.txt","r")
##while True:
##    line=f.readline()
##    if not line:
##        break
##    print(line)

# WAP to copy a content to one file to another.

""" with open('fun.txt',"r") as firstfile,open("fix.txt","w") as secondfile:
    for line in firstfile:
        secondfile.write(line)
print("file copied") """

# WAP to append a file with content of another file.

"""file1=input("enter the file to be opened for append :")
file2=input("enter the file name to be appended :")
fa=open("fun.txt","a")
fr=open("fix.txt","r")
for line in fr.readlines():
        fa.write(line)
fr.close()
fa.close()
print("file appended") """

# Wap a program to read a file in reverse order.

""" f1=open("fun.txt","w")
with open("fix.txt","r") as myfile:
    data=myfile.read()
data_1=data[::-1]
f1.write(data_1)
f1.close() """

# WAP to count number of lines in a file,no of words and count the frequency of each word.

""" with open("fix.txt","r" ) as f:
    lines=len(f.readlines())
    print("Total number of line: ",lines)

no_of_words = 0
with open("fix.txt","r" ) as file:
    data=file.read()
    lines=data.split()
    no_of_words += len(lines)
    print("total no words: ",no_of_words)

fr=open("fix.txt","r")
wordcount={}
for word in fr.read().split():
    if word not in wordcount:
        wordcount[word]=1
    else:
        wordcount[word] +=1
for k,v in wordcount.items():
    print(k,v)
fr.close() """

#
          

