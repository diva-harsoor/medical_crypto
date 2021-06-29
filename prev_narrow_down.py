import json
import os
import re

directory = 'medical_app_toolkit\\cryptoguard_results'

output_file = open('old_output.txt', 'a')

count = 0

def print_result(my_count, my_item):
	output_file.write(str(my_count))
	output_file.write(". ")
	output_file.write("{")
	output_file.write("")
	output_file.write("Message: ")
	output_file.write(my_item['Message'])
	output_file.write("\n\t")
	output_file.write("Description: ")
	output_file.write(my_item['Description'])
	output_file.write("\n\t")
	output_file.write("_FullPath: ")
	output_file.write(my_item['_FullPath'])
	output_file.write("\n\t")
	output_file.write("_Id: ")
	output_file.write(my_item['_Id'])
	output_file.write("}")
	output_file.write('\n')

count = 0
for filename in os.listdir(directory):
    fullpath = os.path.join(directory, filename)
    if os.path.isfile(fullpath):
        with open(fullpath) as file:
            data = json.load(file)
            path_to_match = data['Target']['FullPath']
            path_to_match = re.match(r'.*?(?=\.)', path_to_match)
            if (path_to_match):
            	path_to_match = path_to_match.group()
            	for item in data['Issues']:
            		substring = re.search(r'(?<=\/).*?(?=\/)', item['_FullPath'])
            		if (substring):
            			substring = substring.group()
            			if (path_to_match == substring):
            				count += 1
            				print_result(count, item)


output_file.close()