with open ("ak.txt","r") as f:
    data = f.read()
    print(data)

with open ("ak.txt","w") as f:
    data = f.write("I am Aashish kumar and i am good student")
    print(data)

with open ("ak.txt","a") as f:
    data = f.write("\nI am very happy to told that this college is very good .")
    print(data)
