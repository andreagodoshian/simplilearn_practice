import os

goodFile = r"C:\Users\glass\OneDrive\Documents\Coding Class\2021\SimpliLearn_practice\testing.txt"
print("Does this even exist?", os.path.exists(goodFile))

#open(goodFile)
#this is a normal result:
#<_io.TextIOWrapper name='C:\\Users\\glass\\OneDrive\\Documents\\Coding Class\\2021\\SimpliLearn_practice\\testing.txt' mode='r' encoding='cp1252'>

#for example:
print("\nPrinting (goodFile) as-is will produce this:\n", goodFile)

openForReal = open(goodFile, 'r')
readForReal = openForReal.read()

print("\nThis should actually open the file:\n", readForReal)

print("\nIf you're opening this way, don't forget to close 🥰")

openForReal.close()

#Credit: https://www.youtube.com/watch?v=Yv9q8PZWT48

#And

#Credit: https://www.youtube.com/watch?v=rNmF991BSTE