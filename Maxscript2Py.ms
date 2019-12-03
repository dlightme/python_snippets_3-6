clearListener()

python.Init()
python.Execute "print 'Debug Python: python.Execute print'"

moo = "var x Test String" -- this will be used by the MaxPlus Print statement

filename = "C:\\Users\\rockhunter\\Documents\\GitHub\\python_snippets_3-6\\Py2Maxscript.py" + " var1"

try
(	
python.ExecuteFile("C:\\Users\\rockhunter\\Documents\\GitHub\\python_snippets_3-6\\Py2Maxscript.py")
)
catch
(
format "*** % ***\n" (getCurrentException())
)

print "Maxscript Print :" + fooStr