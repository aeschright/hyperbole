#!/usr/bin/env python3

baskervilles = open('sources/pg2852.txt')
pride = open('sources/pg1342.txt')
dunwich = open('sources/pg50133.txt')

a_new_novel = str(baskervilles.read()) + str(pride.read()) + str(dunwich.read())

with open('novel.txt', 'w') as f:
	f.write(a_new_novel)
