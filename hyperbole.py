#!/usr/bin/env python3

import re

baskervilles = open('sources/pg2852.txt')
baskervilles_chapters = re.split("\nChapter [0-9]+\.\s[a-zA-Z.\s]+\n", str(baskervilles.read()))

pride = open('sources/pg1342.txt')
pride_chapters = re.split("\nChapter [0-9]+\s*\n", str(pride.read()))

dunwich = open('sources/pg50133.txt')
dunwich_chapters = re.split("\n[0-9]+\n", str(dunwich.read()))

a_new_novel = baskervilles_chapters[1] + pride_chapters[1] + dunwich_chapters[1]

with open('novel.txt', 'w') as f:
	f.write(a_new_novel)
