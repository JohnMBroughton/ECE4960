#!/usr/bin/env python3
import time
from datetime import datetime
import mercury

reader = mercury.Reader("tmr:///dev/ttyUSB0", baudrate=115200)
reader.set_region("NA3")
reader.set_read_plan([1], "GEN2", bank=["user"], read_power=1900)

def PrintModel():
	print(reader.get_model())
	print(reader.get_supported_regions())

def GetCUID():
	FoundTags = reader.read()
	for Tag in FoundTags:
		print(Tag.user_mem_data)
		return Tag.user_mem_data
