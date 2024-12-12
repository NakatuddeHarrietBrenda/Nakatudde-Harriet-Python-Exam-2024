#i)
studentName = input('\nEnter the Student Name:\t')
studentNumber = input('Enter the Student Number:\t')
Programing = int(input('Enter Programing marks:\t'))
dataScience = int(input('Enter Data Science marks:\t'))
computeApplications =int(input('Enter Computer applications marks:\t'))
averageMark = float((Programing + dataScience + computeApplications) / 3) # For calculating the average mark

print(f'\n{studentName}, of student number {studentNumber} has average marks of {averageMark:.3}') #Printing the average mark


# ii)
milesDriven = int(input('\nEnter the number of miles driven:\t'))
gallonsOfGasUsed = int(input('Enter the gallons used:\t'))
MPG = int(milesDriven / gallonsOfGasUsed) #calculating the MPG
print(f'\nThe car that drove {milesDriven} miles and used {gallonsOfGasUsed} gallons of gas has MPG of {MPG}')

#iii)
for odd in range(1, 101):
    # Checking if the number is odd
    if odd % 2 != 0:
        print(odd)
#
def evenNumber():
    for odd in range (2,2,100):
        print(odd)
evenNumber()

