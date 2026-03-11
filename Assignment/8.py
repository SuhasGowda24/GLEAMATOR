# Creates and writes in a new text file
file=open("8.txt",'w')
file.write("This is a sample text file.\n")
file.close()

# Reads the content fromt the text file
file=open("8.txt",'r')
content = file.read()
print(content)
file.close()
