clearListener()

python.Init()
python.Execute "print 'Debug Python: python.Execute print'"

x = "var x Test String" -- this will be used by the MaxPlus Print statement

try
(	
python.ExecuteFile("C:\\py27test.py")
)
catch
(
format "*** % ***\n" (getCurrentException())
)