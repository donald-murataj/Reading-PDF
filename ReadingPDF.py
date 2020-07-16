import os
import PyPDF2 as p2
import re
import pprint
import json

PDF = open("practice_exam.pdf", "rb")
pdfread = p2.PdfFileReader(PDF)

# Extracting First Page
x = pdfread.getPage(0)
question_num = 1
letters = ['A.', 'B.', 'C.', 'D.', 'E.', 'F.']

all_lines = x.extractText().splitlines()
line_num = 0
# Retrieve questions and answers in one blob
question_arr = []
while line_num < len(all_lines):
    line = all_lines[line_num].strip()
    if f"{question_num}." in line:
        question_text = ""
        question_num += 1
        next_line = all_lines[line_num].strip()

        while f"{question_num}." not in next_line and line_num < len(all_lines):
            question_text += next_line + " "
            line_num += 1
            if line_num >= len(all_lines):
                continue

            next_line = all_lines[line_num].strip()
        question_arr.append(question_text.strip())
        continue

    line_num += 1

question_json = {}
for question in question_arr:
    all_matches = re.split(" [ABCDEFG]. ", question)

    question_text = all_matches[0]
    question_answers = all_matches[1:]

    question_json[question_text] = question_answers

print(json.dumps(question_json, indent=4))
