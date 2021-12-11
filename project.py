import csv
with open('height-weight.csv', newline='') as fileObject:
    reader=csv.reader(fileObject)
    file_data=list(reader)
    
    
file_data.pop(0)


new_data=[]
for i in range(len(file_data)):
    n_num=file_data[i][2]
    new_data.append(float(n_num))
    
    
numberOfValues=len(new_data)
total=0
for eachValue in new_data:
    total += eachValue
    
mean=total/numberOfValues
if numberOfValues % 2 == 0: 
    #getting the first number 
    median1 = float(new_data[numberOfValues//2])
    #getting the second number 
    median2 = float(new_data[numberOfValues//2 - 1])
    #getting mean of those numbers 
    median = (median1 + median2)/2 
    
else: 
    median = new_data[numberOfValues/2]


print("Mean of the given weight values is: " +str(mean))
print("Meadian of the given weight values is: " +str(median))

    