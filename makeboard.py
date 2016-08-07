#!/usr/bin/env python
# vim: tabstop=4 softtabstop=4 shiftwidth=4 smarttab expandtab:

import sqlite3

class startinggame:
	def setup (self):
		print "creating table of countries"
		with sqlite3.connect('pandemic.db') as conn:
	            	cursor = conn.cursor()
	            	tobedone = 'DROP TABLE if exists countries;'
	            	cursor.execute( tobedone )
			conn.commit()
			tobedone = '''CREATE TABLE countries(
			"Name",
			"NoConnect",
			"Co1",
			"Co2",
			"Co3",		
			"Co4",
			"Co5",
			"Co6");'''
			cursor.execute( tobedone )
			conn.commit()
		
	def setupboard (self,board):
		boardfile = open(board,'r') 
		for line in boardfile:
			with sqlite3.connect('pandemic.db') as conn:
			        cursor = conn.cursor()
		            	tobedone = """INSERT INTO countries (Name,NoConnect,Co1,Co2,Co3,Co4,Co5,Co6) VALUES (%s);""" % (line)
		            	cursor.execute( tobedone )
				conn.commit()

	def setupresearch (self):
		with sqlite3.connect('pandemic.db') as conn:
			        cursor = conn.cursor()
		            	tobedone = """ALTER TABLE countries ADD COLUMN research;"""
		            	cursor.execute( tobedone )
				conn.commit()
				tobedone = """UPDATE countries SET research = 0 WHERE name is 'Atlanta'""";
		            	cursor.execute( tobedone )
				conn.commit()

