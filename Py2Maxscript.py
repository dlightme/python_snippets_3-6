import  sys
import MaxPlus


def returnstuff(x):
	return x**2
  
def main():
	""" Main entry point of the app """
	print "Debug Python: Def Main: Hello 3ds Max!"
	print sys.argv
	a = returnstuff(4)
	MaxPlus.Core.EvalMAXScript("format \"Maxscript print from python: %\n\"(x) ") 	#! escape characters!
	
	


if __name__ == "__main__":
	""" This is executed when run from the command line """
	main()