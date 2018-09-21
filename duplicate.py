#list of names for array
duplicate = []

#adding the ability to input 5 entries into the array
for n in range(0,5):
    name = input("Enter how many names you want: ")
    duplicate.append(name)

#function to remove the names that get repeated in the array
def remove(duplicate):
    final_list = []
    for name in duplicate:
        if name not in final_list:
            final_list.append(name)
    return final_list

print(remove(duplicate))