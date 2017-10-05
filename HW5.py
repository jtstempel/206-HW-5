#The basic outline of this problem is to read the file,
#look for integers using the re.findall(), looking for a regular
#expression of '[0-9]+' and then converting the extracted strings 
#to integers and summing up the integers.

import re

my_final_sum = 0
my_file = open('Actual_Data.txt', 'r')

for my_line in my_file:
	find_all = re.findall('[0-9]+', my_line)			#the type of find_all is a list, I need it to be an integer
	
	for my_item in find_all:
		my_final_sum = my_final_sum + int(my_item)
	
print(my_final_sum)
