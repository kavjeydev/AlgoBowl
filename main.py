
file = open("test.txt", "r")
file_content = file.read().split("\n")

num_courses_required = int(file_content[0]) # first like of input file is # courses required

prerequisites_to_class = {}

# key is classID, values are prerequisite IDs, dictionary holds this information
for i in range(1, num_courses_required + 1):
    prerequisites_to_class[i] = (file_content[i].split(" ")[1:])


print(prerequisites_to_class)