'''
BCBGSO Basic Python workshop 3/23/2018
Exercise 3

@author urmi
'''
#1. Given a number, find its factorial i.e. n*n-1*n-2*...*1. Hint: use loop.
n=5
#Don't change this
#Thanks Yuan Wang, BCB for the dict code
geneticCode = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
              "UCU":"S", "UCC":"s", "UCA":"S", "UCG":"S",
              "UAU":"Y", "UAC":"Y", "UAG":"STOP",
              "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
              "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
              "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
              "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
              "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
              "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
              "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
              "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
              "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
              "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
              "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
              "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
              "GGU":"G", "GGC":"G", "GGA":"G", }

'''
Above "geneticCode" is a dict which maps an RNA codon to an amino acid letter. Same from excercise 2.
'''

dnaCodons=['ATG','TTT','TTG','CTC','ATT','ATG','GTA','TAC','TAA','TAG','CAT','CAC','CAA','AAC','AAG','GAT','TGC','TGA','TGG','CGA','AGC','AGG','GGG']

#2. dnaCodons is a list of valid codons. Using a for loop iterate over this list and print corresponding amino acid.
#Hint: The dict geneticCode is defined for RNA codons you will have to first convert the given DNA codons to RNA codons. To this replace all 'T' with 'U'.
#You may want to use str.replace() function

#3. If you did step 1 correctly you will notice two "STOP" in your amino acid sequence. Biologically, the "Stop" codons mark te end of a peptide.
#Use an if condition to skip printing of the "Stop" codon. Can you do the same using a continue statement?
#Hint: the codons that will result in a stop codon are "UAG" and "UGA".

'''
*Bonus Question
Open Reading Frame (ORF): An ORF is defined as the sequence which has the ability to be translated into a protein. An ORF start with a start codon i.e "ATG" and
ends with any of the stop codons i.e. "TAG" or "TGA". Where a codon is defined as sub-sequence of length 3 in a given sequence. To keep things simple we scan in
only one direction  and in only one frame (don't worry if you don't know these terms) to find the possible ORF. e.g. in the sequence AAATTTATGAGCTTTCATCATTAGGGTTTG
the ORF has the codons are ATG AGC TTT CAT CAT i.e. three letters taken at a time starting from the start codon till the stop codon is reached (not printed). 
'''
dnaSeq='AAATTTATGAGCTTTCATCATTAGGGTTTG'
#4. Given a DNA sequence can you find the ORF using the above defination.
flag=False
for i in range(0,len(dnaSeq)-3,3):
    t=dnaSeq[i:i+3]
    if t == "TAG" or t=="TGA":
        break
    if t == "ATG" or flag == True:
        flag=True
        print geneticCode[t.replace('T','U')]
