#What is the most common species and ability1?
with open("pokemon_data.csv", "r") as file: #opening the file in read mode
    contents = file.read() #reading the contents of the file
    lines = contents.splitlines() #splitting the contents by lines
     #splitting the lines by commas and saving them to a list of columns for my sanity
    columns = [line.split(",") for line in lines] 


header = columns[0] #grabs the column names

speciesIndex = header.index("species") #finds which index the species column is in
ability1Index = header.index("ability1") #finds which index the ability1 column is in

 
species = [row[speciesIndex]for row in columns[1:]] #creates the list of species by using the speciesIndex but excludes the header
ability1 = [row[ability1Index] for row in columns[1:] ] #creates the list of ability1 by using the ability1Index but excludes the header

#counting the instances of each species and ability1
speciesCount = {}
ability1Count = {}
#looping through the species and ability1 lists to count the instances of each
for i in species:
    if i in speciesCount:
          speciesCount[i] += 1 #if the species is already in the dictionary, add 1 to the count
    else:
        speciesCount[i] = 1 #else the species is not in the dictionary, add the species to the dictionary and set the count to 1

for k in ability1:
        if k in ability1Count:
            ability1Count[k] += 1 #if the ability1 is already in the dictionary, add 1 to the count
        else:
             ability1Count[k] = 1 #else the ability1 is not in the dictionary, add the ability1 to the dictionary and set the count to 1

#finding the most common species and ability1
commonSpecies = max(speciesCount, key=speciesCount.get)
commonAbility1 = max(ability1Count, key=ability1Count.get)
#printing the most common species and ability1
print("The most common species is: ", commonSpecies)
print("The most common ability1 is: ", commonAbility1)
