import json
import os
import re

directory = 'medical_app_toolkit\\cryptoguard_results'

json_output_file = open('json_output.txt', 'a')

matched_array = []

def formatted_write(count, item):
	json_output_file.write(str(count))
	json_output_file.write(". ")
	json_output_file.write("Message: ")
	json_output_file.write(str(item["Message"]))
	json_output_file.write("\n\t")
	json_output_file.write("Description: ")
	json_output_file.write(str(item["Description"]))
	json_output_file.write("\n\t")
	json_output_file.write("RuleNumber: ")
	json_output_file.write(str(item["RuleNumber"]))
	json_output_file.write("\n\t")
	json_output_file.write("RuleDesc: ")
	json_output_file.write(str(item["RuleDesc"]))
	json_output_file.write("\n\t")
	json_output_file.write("CWEId: ")
	json_output_file.write(str(item["CWEId"]))
	json_output_file.write("\n\t")
	json_output_file.write("Severity: ")
	json_output_file.write(str(item["Severity"]))
	json_output_file.write("\n\t")
	json_output_file.write("_FullPath: ")
	json_output_file.write(str(item["_FullPath"]))
	json_output_file.write("\n\t")
	json_output_file.write("_MatchingIds: ")
	json_output_file.write(str(item["_MatchingIds"]))
	json_output_file.write("\n")


def match_with_duplicates(cryptoguard_file):
	data = json.load(cryptoguard_file)
	path_to_match = data['Target']['FullPath']
	path_to_match = re.sub(r'\.', '/', path_to_match)
	path_to_match = re.search(r'/.*?(/)', path_to_match)
	if path_to_match:
		path_to_match = path_to_match.group()
		for item in data['Issues']:
			substring = re.search(r'(?<=/).*', item['_FullPath'])
			if (substring):
				substring = substring.group()
				substring = re.search(r'/.*?(/)', substring)
				if (substring):
					substring = substring.group()
					if (path_to_match == substring):
						matched_array.append(item)


def find_matches(original):
	matching_ids = []
	my_matched_array = matched_array.copy()
	for item in my_matched_array:
		if original["Message"] == item["Message"]:
			if original["Description"] == item["Description"]:
				if original["_FullPath"] == item["_FullPath"]:
					matching_ids.append(item["_Id"])
					matched_array.remove(item)
	if (matching_ids):
		my_original = dict(original)
		my_original["_MatchingIds"] = matching_ids
		return my_original
	else:
		return original

def get_unique():
	unique_objects = []
	for item in matched_array:
		unique_object = find_matches(item)
		unique_objects.append(unique_object)
	return unique_objects

count = 0
for filename in os.listdir(directory):
	fullpath = os.path.join(directory, filename)
	if os.path.isfile(fullpath):
		with open(fullpath) as file:
			match_with_duplicates(file)
			unique = get_unique()
			for item in unique:
				count += 1
				formatted_write(count, item)
