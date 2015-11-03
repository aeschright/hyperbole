#!/usr/bin/env python3

import random
import re

baskervilles = open('sources/pg2852.txt')
baskervilles_chapters = re.split("\n\nChapter [0-9]+\.\s[a-zA-Z .]+\n\n", str(baskervilles.read()))
baskervilles_chapters.pop(0) # removing everything before the start of the first chapter

pride = open('sources/pg1342.txt')
pride_chapters = re.split("\n\nChapter [0-9]+\s*\n\n", str(pride.read()))
pride_chapters.pop(0) # removing everything before the start of the first chapter

dunwich = open('sources/pg50133.txt')
dunwich_chapters = re.split("\n\n[0-9]+\n\n", str(dunwich.read()))
dunwich_chapters.pop(0) # removing everything before the start of the first chapter

source_chapters = [baskervilles_chapters, pride_chapters, dunwich_chapters]

a_new_novel = "Chapter 1\n\n"
a_new_novel += random.choice(source_chapters)[0]

# randomly pick 10 chapters
for i in range(10):
	chapter_number = str(i+2)
	chapter_title = "Chapter " + chapter_number + "\n\n"
	selected_source = random.choice(source_chapters)
	chapter_index = random.randint(1, len(selected_source) - 2)
	chapter = selected_source[chapter_index]
	a_new_novel += chapter_title + chapter + "\n\n"

a_new_novel += "Chapter 12\n\n"
a_new_novel += random.choice(source_chapters)[-1]

with open('novel.txt', 'w') as f:
	f.write(a_new_novel)
