
import os, sys, re
def getScriptPath():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

def linesplit(inline):
		values = re.split(r'(,+?)(?=(?:[^"]*"[^"]*")*[^"]*\Z)', inline) 
		nocomma = list(set(values))
		try:
			nocomma.remove(',')
		except:
			pass			
		return nocomma

class gads:
	
	def __init__(self, filename):
		self.myfile =filename
		self.parsedarray=[]
		self.fullfile=[]
		
	def parsefile(self):
		fqfn = getScriptPath() + "\\" + self.myfile
		num_lines = sum(1 for line in open(fqfn))
		f = open(fqfn, "r")
		self.fullfile=f.read().splitlines()
		f.close()
		for i in range(0, len(self.fullfile)):
			self.parsedarray.append(linesplit(self.fullfile[i]))
			

print "Something with this code doesn't work right. \n"
print "I can import the file: gads.t20070101.csv"
print "I can read it into a list of lines \n" 
print "here is line 1 without any CSV splitting \n"
g = gads("gads.t20070101.csv")
g.parsefile()
print g.fullfile[1] 
print "\n \n here is the same line after being split by csv. It's a 2D array so you can access individual terms with g.parsedarray[line][field] or the whole line with g.parsedarray[line] \n"
print g.parsedarray[1] 
print "\n \n as you can see, for some reason when it is being split, the numbers get randomly shuffled around within the line."
print "it's random per line too, so I can't just re-map which fields are where."


		
		
	