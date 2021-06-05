import re
import json
file = open("Testy_Patokhimia.txt", 'r', encoding="utf8")

row = file.readlines()

questions = []

question = ""
options = []

# re.match(r'^\d+\.', line):

prev_line = ""

for line in row:
    if re.match(r'^test ', line):
        count = len(questions) + 1
        question = str(count) + ". " + line[5:]
    elif re.match(r'^.\) ', line):
        otvet = line[3:]
        options.append(otvet)

    if re.match(r'^Г\) ', line):
        questions.append(
            {
                "question": question,
                "options": options,
                "correct": 0
            }
        )
        question = ""
        options = []

#print(json.dumps(questions, indent=4))
#print(questions)

with open('Testy_Patokhimia.json', 'w') as outfile:
    json.dump(questions, outfile)
