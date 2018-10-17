name = input( "Enter name: ")
print("Name is ", name)
age = int(input("Enter age of the person: "))
willreachhundredby = 100.0 - age + 2018
strToPrint = ("%s will reach hundred years in %d" % ( name, willreachhundredby ) )
howmanyprints = int ( input( "How many times do you want to see above message: "))
print(howmanyprints * ( strToPrint + "\n" ) )