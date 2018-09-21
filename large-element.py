#list of numbers 
number_list = []

#loop to add input entry to the array, 5 in total
#range can be modified according to needs
for a in range(0,5):
    number = int(input("Enter number: "))
    number_list.append(number)

#function to calculate the largest number in the array
def largest(number_list):
    max = number_list[0]
    for a in range(1,len(number_list)):
        if number_list[a] > max:
            max = number_list[a]
    return max
    
#giving the function a value        
Ans = largest(number_list)

print("Largest number in given array is: ", Ans)