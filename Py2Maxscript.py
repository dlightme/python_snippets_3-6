import  sys
import MaxPlus


def returnstuff(x):
	return x**2
  
def main():
	""" Main entry point of the app """
	print "Py2Maxscript: Def Main: Hello 3ds Max!"
	print sys.argv
	if len(sys.argv) < 1:
		print sys.argv[1]
		
	foo  = returnstuff(4)
	
	MaxPlus.Core.EvalMAXScript("fooStr = \"this is string from Py2Maxscript\"") # This declares a new variable in maxscript, which is how you can pass things over to max.
	MaxPlus.Core.EvalMAXScript("format \"Py2Maxscript: Print from python Using the var moo declared in Maxscript2py: %\n\"(moo) ") 	#! escape characters!
	
	
	


if __name__ == "__main__":
	""" This is executed when run from the command line """
	main()