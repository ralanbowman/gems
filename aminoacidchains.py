###FOR FURTHER INSTRUCTIONS PLEASE REFER TO alternateresidues.py SAMPLE FILE
#SAMPLE COMMAND :
# python aminoacidchains.py -libs "gmml/dat/CurrentParams/leaprc.ff12SB_2014-04-24/amino12.lib","gmml/dat/CurrentParams/leaprc.ff12SB_2014-04-24/aminont12.lib","gmml/dat/CurrentParams/leaprc.ff12SB_2014-04-24/aminoct12.lib" -pdb "gmml/example/pdb/1Z7E.pdb"

import gmml
import sys

temp = gmml.PdbPreprocessor()
libs = gmml.string_vector()

for i, arg in enumerate(sys.argv):	
    if arg == '-libs':                       
		arguments = sys.argv[i+1].split(',')
		for argument in arguments:
			libs.push_back(argument)
    elif arg == '-pdb':
		pdb = sys.argv[i+1]

pdbfile = gmml.PdbFile(pdb)

temp.ExtractAminoAcidChains(pdbfile)

chain_terminations = temp.GetChainTerminations()

for x in xrange(0, chain_terminations.size()):
        chain_terminations[x].Print()


###UPDATING AMINO ACID CHAINS###
chain_terminations[0].SetSelectedNTermination(gmml.NH3)
chain_terminations[0].SetSelectedCTermination(gmml.NHCH3)
print "The Updated chain terminations:"
for x in xrange(0, chain_terminations.size()):
        chain_terminations[x].Print()

temp.UpdateAminoAcidChains(pdbfile, libs, chain_terminations)

pdbfile.Write('aminoacidchain-update.pdb')
