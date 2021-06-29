import json
import os
import re

directory = 'medical_app_toolkit\\cryptoguard_results'

output_file = open('output.txt', 'a')

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

for filename in os.listdir(directory):
	fullpath = os.path.join(directory, filename)
	if os.path.isfile(fullpath):
		with open(fullpath) as file:
			data = json.load(file)
			path_to_match = data['Target']['FullPath']
			path_to_match = re.sub(r'\.', '/', path_to_match)
			path_to_match = re.search(r"/.*?(/)", path_to_match)
			#print(path_to_match.group())
			# path_to_match = re.match(r"^([^.]+)", path_to_match)
			if path_to_match:
				path_to_match = path_to_match.group()
				# print(path_to_match)
				for item in data['Issues']:
					substring = re.search(r"(?<=/).*", item['_FullPath'])
					#print(substring)
					#print("hello")
					if (substring):
						substring = substring.group()
						#print(substring)
						should_match = re.search(r"/.*?(/)", substring)
						#print(substring)
						if (should_match):
							should_match = should_match.group()
							# print(should_match)
							if (path_to_match == should_match):
								count += 1
								print_result(count, item)
					#should_match = re.search(r"(?<=/).*?(?=/)", item['_FullPath'])
					#if (should_match):
					#	should_match = should_match.group()
					#	if (path_to_match == should_match):
					#		count += 1
							# print_result(count, item)

output_file.close()