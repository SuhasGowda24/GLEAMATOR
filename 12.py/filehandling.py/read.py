# Main Modes
r=open("data.txt",'r')
print(r.read())
r.close()

r=open("data.txt",'w')
r.write("Hello World") #It will overwrite the existing data in the data.txt file
r.close()

r=open("data.txt",'a')
r.write(" whats up") #It will append the data to the existing data in the data.txt file
r.close()

file=open("data2.txt",'x')
file.write("This is a new file")
# file.close()
with open("data.txt",'r') as file: # to close automatically after the block of code is executed
    r=file.read()
    print(r)
    
    
