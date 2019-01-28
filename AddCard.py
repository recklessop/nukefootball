#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
import os
import time
import base64
import pickledb

reader = SimpleMFRC522.SimpleMFRC522()

db = pickledb.load('example.db', False)

while True:
	try:
        	id, text = reader.read()
	        id = str(id)
		print(id)
	        print(text)

	        key = db.get(id)
		if key:
			print("Card Already In Database ... Updating Card")
	                random_bytes = os.urandom(16)
	                text = base64.b64encode(random_bytes).decode('utf-8')
        	        print("Now place your tag to write")
                	reader.write(text)
			if db.set(id, text):
				print("Card and DB Updated")

		else:

		        Add = raw_input("Add to Database? ")

			if Add == 'y':
		                random_bytes = os.urandom(16)
		                text = base64.b64encode(random_bytes).decode('utf-8')
		                print("Now place your tag to write")
		                reader.write(text)

				db.set(id, text)
	        		print("Added to DB")
				db.dump()

	        #id, text = reader.read()
	        #print(id)
	        #key2 = db.get(id)
		#print(key2)
		time.sleep(2)
		print("Keys In Database:")
		cards = db.getall()
		for card in cards:
			key = db.get(card)
			print 'card: {0} Key {1}'.format(card, key)
	finally:
        	GPIO.cleanup()


