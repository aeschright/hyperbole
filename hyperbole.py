#!/usr/bin/env python3

baskervilles = open('sources/pg2852.txt')
pride = open('sources/pg1342.txt')
dunwich = open('sources/pg50133.txt')

with open('novel.txt', 'w') as f:
	f.write(baskervilles.read())
	f.write(pride.read())
	f.write(dunwich.read())
