# store a short DNA seq in the variable my_dna
my_dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
# now print the DNA seq
print (my_dna)

# calculate DNA length
dna_length = len (my_dna)

# print length amount
print ("The length of the DNA sequence is " + str(dna_length) + " base pairs.")

# replacement of argument characters
print (my_dna.replace ("ATG" , "AUG"))

#EXTRACTING PART OF A STRING = print positions _ TO _
print ("The first 10 bases are " + str(my_dna[0:10]) + ".")

# assign the first base variable
first_base = my_dna[0]
print ("The first base is " + str(first_base) + ".")

#assign the first codon read variable
first_codon = my_dna[0:3]
print ("The first codon is " + str(first_codon) + ".")


#substring - counting the number of times some pattern occurs in your sequence
#this uses the COUNT method

#count the DNA bases
adenine_count = my_dna.count ('A')
thymine_count = my_dna.count ("T")
guanine_count = my_dna.count ("G")
cytosine_count = my_dna.count ("C")
#an additional test
CpG_count = my_dna.count ('CG')

#now print the COUNTS
print ("Adenines: " + str(adenine_count))
print ("Thymines: " + str(thymine_count))
print ("Guanines: " + str(guanine_count))
print ("Cytosines: " + str(cytosine_count))
print ("CpG islands: " + str(CpG_count))


#FIND method to located where they are
print (str(my_dna.find ("GA") ) )
#display the number
print ("The position of GA is " + (str(my_dna.find ("GA"))))

#calculating a substring occurence
at_content = (adenine_count + thymine_count) / dna_length
print ("AT content is " + str(at_content))
#DIDN't WORK #DIDNT'T WORK #DIDNT'T WORK #DIDNT'T WORK #DIDNT'T WORK #DIDNT'T WORK #DIDNT'T WORK 


# replace A with T, T with A, C with G, G with C, NEED TO USE UPPER COMMAND
# i.e. define the complementary sequence

replacement1 = my_dna.replace('A', 't')
replacement2 = replacement1.replace('T', 'a')
replacement3 = replacement2.replace('C', 'g')
replacement4 = replacement3.replace('G', 'c')
# convert it to uppercase
# assign new variable
replacement5 = (replacement4.upper())

# display the complementary sequence
print ("The complementary sequence is " + str(replacement5))


# using FIND for restriction enzymes, ex: EcoRI cuts GAATTC
frag1_length = my_dna.find("GAATTC") + 1
#the + 1 is because the enzyme cuts between G and A which adds one position
frag2_length = dna_length - frag1_length
#print the lengths of fragments
print ("Results from EcoRI cutting:")
print ("The length of fragment 1 is " + str(frag1_length) + " bases")
print ("The length of fragment 2 is " + str(frag2_length) + " bases")



