from pymongo import *
import os
import sys

fileName = sys.argv[1] #file where data is written
eventNum = sys.argv[2] #retrieve data from  for specific eventNum

file = open(fileName, 'w')

client = MongoClient('localhost',27017)

db = client.accelDatabase

for data in db.accelDatabase.find({"eventNum": int(eventNum)}):
		file.write(data["accel"])
		file.write("\n")
