#CSV for python
#  "LU",86.25,"11/4/19,98","2:19PM",+4.0625
#my magic regex: (,+?)(?=(?:[^"]*"[^"]*")*[^"]*\Z)
import re

class mycsv:
	def __init__(self, instring):
		 self.line = instring
		 self.nocomma = None
	def split(mycsv):
		values = re.split(r'(,+?)(?=(?:[^"]*"[^"]*")*[^"]*\Z)', mycsv.line) 
		nocomma = list(set(values))
		try:
			nocomma.remove(',')
		except:
			pass			
		return nocomma
		

