import csv
import urllib

PopulationAndDensity = "http://boxnumbertwo.com/PittsburghData/Population_and_Density.csv"

fhand = urllib.urlopen(PopulationAndDensity)

# Making a dictionary for every column

neighborhood= dict()
population1940 = dict()
population1950 = dict()
population1960 = dict()
population1970 = dict()
population1980 = dict()
population1990 = dict()
population2000 = dict()
population2010 = dict()

## reading from the reader 

try:
	reader = csv.reader(fhand)
	next(reader, None)  # skip the headers
	##adding values in the dictinory 
	for row in reader:
	    key = row[0]
            neighborhood[key] = row[0]  ## assign the first column to neighborhood dictionary and get rid of the "comma"
            population1940[key] = int(row[2].replace(',',''))  ## assign the third column to population1940 dictionary
            population1950[key] = int(row[3].replace(',',''))  ## assign the fourth column to population1950 dictionary
            population1960[key] = int(row[4].replace(',',''))  ## assign the fifth column to population1960 dictionary
            population1970[key] = int(row[5].replace(',',''))  ## assign the sixth column to population1970 dictionary
            population1980[key] = int(row[6].replace(',',''))  ## assign the seventh column to population1980 dictionary
            population1990[key] = int(row[7].replace(',',''))  ## assign the eighth column to population1949 dictionary
            population2000[key] = int(row[8].replace(',',''))  ## assign the ninth column to population2000 dictionary
            population2010[key] = int(row[9].replace(',',''))  ## assign the tenth column to population2010 dictionary
finally:
	fhand.close()

### find the differecne  by looping through every dictionary by its [neighborhood] index

print "Difference between 1940 - 1950: "  
difference = 0
for key in neighborhood:
   difference +=  population1950[key] - population1940[key]   

print difference

print "Difference between 1950 - 1960: "

difference = 0
for key in neighborhood:
   difference +=  population1960[key] - population1950[key]
   
print difference


print "Difference between 1960 - 1970: "

difference = 0
for key in neighborhood:
   difference +=  population1970[key] - population1960[key]

print difference

print "Difference between 1970 - 1980: "

difference = 0
for key in neighborhood:
   difference +=  population1980[key] - population1970[key]

print difference

print "Difference between 1980 - 1990: "
difference = 0
for key in neighborhood:
   difference +=  population1990[key] - population1980[key]
   
print difference

print "Difference between 1990 - 2000: "

difference = 0
for key in neighborhood:
   difference +=  population2000[key] - population1990[key]

print difference

print "Difference between 2000 - 2010: "

difference = 0
for key in neighborhood:
   difference +=  population2010[key] - population2000[key]
   
print difference

print"\n"
 #########################################################
print "#########################################################"
print "\n"

### find the differecne  by looping through every dictionary by its [neighborhood] index


print "#Difference between 1940 - 1950 for Mount Washington: "

difference = population1950['Mount Washington'] - population1940['Mount Washington']

print difference 

print "#Difference between 1950 - 1960 for Mount Washington: "

difference = population1960['Mount Washington'] - population1950['Mount Washington']

print difference 

print "#Difference between 1960 - 1970 for Mount Washington: "

difference = population1970['Mount Washington'] - population1960['Mount Washington']

print difference 

print "#Difference between 1970 - 1980 for Mount Washington: "

difference = population1980['Mount Washington'] - population1970['Mount Washington']

print difference 

print "#Difference between 1980 - 1990 for Mount Washington: "

difference = population1990['Mount Washington'] - population1980['Mount Washington']

print difference 

print "#Difference between 1990 - 2000 for Mount Washington: "

difference = population2000['Mount Washington'] - population1990['Mount Washington']

print difference 

print "#Difference between 2000 - 2010 for Mount Washington: "

difference = population2010['Mount Washington'] - population2000['Mount Washington']

print difference 
 
 
print"\n"
 #########################################################
print "#########################################################"
print "\n"
 
### find the differecne  by looping through every dictionary by its [neighborhood] index



print "#Difference between 1940 - 1950 for North Oakland: "

difference = population1950['North Oakland'] - population1940['North Oakland']

print difference 

print "#Difference between 1950 - 1960 for North Oakland: "

difference = population1960['North Oakland'] - population1950['North Oakland']

print difference 

print "#Difference between 1960 - 1970 for North Oakland: "

difference = population1970['North Oakland'] - population1960['North Oakland']

print difference 

print "#Difference between 1970 - 1980 for North Oakland: "

difference = population1980['North Oakland'] - population1970['North Oakland']

print difference 

print "#Difference between 1980 - 1990 for North Oakland: "

difference = population1990['North Oakland'] - population1980['North Oakland']

print difference 

print "#Difference between 1990 - 2000 for North Oakland: "

difference = population2000['North Oakland'] - population1990['North Oakland']

print difference 

print "#Difference between 2000 - 2010 for North Oakland: "

difference = population2010['North Oakland'] - population2000['North Oakland']

print difference 


print"\n"
 #########################################################
print "#########################################################"
print "\n"

### find the differecne  by looping through every dictionary by its [neighborhood] index


print "#Difference between 1940 - 1950 for Shadyside: "

difference = population1950['Shadyside'] - population1940['Shadyside']

print difference 

print "#Difference between 1950 - 1960 for Shadyside: "

difference = population1960['Shadyside'] - population1950['Shadyside']

print difference 
print "#Difference between 1960 - 1970 for Shadyside: "

difference = population1970['Shadyside'] - population1960['Shadyside']

print difference 
print "#Difference between 1970 - 1980 for Shadyside: "

difference = population1980['Shadyside'] - population1970['Shadyside']

print difference 
print "#Difference between 1980 - 1990 for Shadyside: "

difference = population1990['Shadyside'] - population1980['Shadyside']

print difference 
print "#Difference between 1990 - 2000 for Shadyside: "

difference = population2000['Shadyside'] - population1990['Shadyside']

print difference 
print "#Difference between 2000 - 2010 for Shadyside: "

difference = population2010['Shadyside'] - population2000['Shadyside']

print difference 



print"\n"
 #########################################################
print "#########################################################"
print "\n"



### finding the Worst and the Best 

print "Difference between 2010 - 1940: "
totalDiff20101940 = dict()  ### making a dictinoary to save the differernce between 2010 and 1940
difference = 0
### looping through the column by its [neighborhood] index  
for key in neighborhood:  
   totalDiff20101940[key] =  population2010[key] - population1940[key] 

### USE THIS TO SORT, Returns a list (array) ###
totalDiff20101940 = sorted(totalDiff20101940.items(), key=lambda x:x[1])

print "Top 10 - Worst"

print totalDiff20101940[-90:-79]   ### print the top 10 worst


print "Top 10 - Best"

print totalDiff20101940[79:90]   ### print the top 10 best

#Results

#Difference between 1940 - 1950:  5148
#Difference between 1950 - 1960:  -61563
#Difference between 1960 - 1970:  -95088
#Difference between 1970 - 1980:  -96216
#Difference between 1980 - 1990:  -54059
#Difference between 1990 - 2000:  -36352
#Difference between 2000 - 2010:  -27823


#Difference between 1940 - 1950 for Mount Washington:  -953
#Difference between 1950 - 1960 for Mount Washington:  -1645
#Difference between 1960 - 1970 for Mount Washington:  -2628
#Difference between 1970 - 1980 for Mount Washington:  -2992
#Difference between 1980 - 1990 for Mount Washington:  -1095
#Difference between 1990 - 2000 for Mount Washington:  -822
#Difference between 2000 - 2010 for Mount Washington:  -1079


#Difference between 1940 - 1950 for North Oakland:  1936
#Difference between 1950 - 1960 for North Oakland:  -610
#Difference between 1960 - 1970 for North Oakland:  1213
#Difference between 1970 - 1980 for North Oakland:  42
#Difference between 1980 - 1990 for North Oakland:  2128
#Difference between 1990 - 2000 for North Oakland:  -979
#Difference between 2000 - 2010 for North Oakland:  694


#Difference between 1940 - 1950 for Shadyside:  1599
#Difference between 1950 - 1960 for Shadyside:  -1102
#Difference between 1960 - 1970 for Shadyside:  -2329
#Difference between 1970 - 1980 for Shadyside:  -1903
#Difference between 1980 - 1990 for Shadyside:  -560
#Difference between 1990 - 2000 for Shadyside:  369
#Difference between 2000 - 2010 for Shadyside:  161



#Top 10 - Worst

#  ('South Side Flats', -15879)
#  ('Middle Hill', -15322)
#  ('Crawford-Roberts', -14789)
#  ('Bloomfield', -12266)
#  ('Larimer', -11610)
#  ('Mount Washington', -11214)
#  ('East Allegheny', -10835)
#  ('Homewood South', -10678)
#  ('South Side Slopes', -10660)
#  ('Perry South', -10521)
#  ('Homewood North', -10319)
#Top 10 - Best
#  ('Stanton Heights', -9)
#  ('Bon Air', -6)
#  ('Swisshelm Park', 23)
#  ('Oakwood', 290)
#  ('New Homestead', 301)
#  ('Northview Heights', 552)
#  ('Westwood', 618)
#  ('Squirrel Hill North', 928)
#  ('Windgap', 1151)
#  ('Banksville', 2930)
#  ('North Oakland', 4424)
	