import csv

## define a function to create the doi_text string containing the contents of the file
def create_doi():
    doi_text = open("doi.txt", 'r')
    doi = ''

    ## run through doi.txt and concatenate to string doi
    for line in doi_text:
        doi += line
    doi_text.close()
    return doi

## define a function to create the gadsby_text string containing the contents of the file
def create_gadsby():
    gadsby_text = open("gadsby_text.txt", 'r')
    gadsby = ''

    ## run through gadsby_text.txt and concatenate to string gadsby
    for line in gadsby_text:
        gadsby += line
    gadsby_text.close()
    return gadsby

## define a function to count the frequency of appearance for each character in the file
def char_freq(file):
    print("Type '1' if you want to count all ASCII characters.")
    print("Type '2' if you want to count only alpha-numeric characters.")
    count_type = input("Enter your selection: ")

    ## define the ascii_counter dictionary
    ascii_counter = {}
    ## run through the file and count unique characters in ascii_counter dictionary
    if count_type == '1':
        for char in file:
            if char not in ascii_counter:
                ascii_counter[char] = 1
            else:
                ascii_counter[char] += 1
        print("Frequency analysis of alpha-numeric characters: \n")
        print(ascii_counter)
        print("\n\n")

    ## define the alpha_counter dictionary
    alpha_counter = {}
    ## run through the file and count unique alpha-numeric characters in alpha_counter dictionary
    if count_type == '2':
        for char in file:
            if ord(char) > 47 and ord(char) < 123:
                if char not in alpha_counter:
                    alpha_counter[char] = 1
                else:
                    alpha_counter[char] += 1
        print("Frequency analysis of ASCII characters: \n")
        print(alpha_counter)
        print("\n\n")

    ## Ask user if they want to export the counts to a spreadsheet
    user_choice = input("Enter '1' if you would like to export this data to a .csv file: ")

    if user_choice == '1':
        print("\n")
        print("Please note that the .csv file will be named output.csv and will be overwritten")
        print("if this program is run again before you change the name of the file.")

        # Function to print the counts to a spreadsheet
        with open('output.csv', 'w+') as output:
            writer = csv.writer(output)
            if count_type == '1':
                for key, value in ascii_counter.items():
                    writer.writerow([key, value])
            if count_type == '2':
                for key, value in alpha_counter.items():
                    writer.writerow([key, value])

## User menu
print("Welcome to my frequency analysis program.")
print("Type '1' if you would like to perform frequency analysis for doi.txt.")
print("Type '2' if you would like to perform frequency analysis for gadsby_text.txt.")
print("Type '3' if you would like to perform frequency analysis for crypto.")
choice = input("Enter your selection: ")

## Create the strings to save the output of the functions
gadsby_text = ''
doi_text = ''
gadsby_text = create_gadsby()
doi_text = create_doi()

## Create a variable for ciphertext to decrypt
# crypto = '''RFDRG WQPMW AOPSW VOHWR ZGKRR WQOCO OIWAM DGKIF GJPJS DLPAR
# DGKCA GHRZO QGARZ RZODO PFRZO UPDGV RZOHO OCRZO FOWTP LSGLC
# GADGK FHPSS GFRZO UPTZJ GPFUG VDGKF LPFDG KZPYO PTLZO UKSOP
# LPSOA UPFPR WQOVG FUWAA OFGFP QGYWO DORPS SPFGK AUDGK RWQOC
# OOIWA MWTWM AGFOU JWFUT PFOAG RSPRO PUGMU GOTAG RLZOL CWRTH
# PRLZU OOFUG AGRVF ORGYO FIPTT WAMJW FRZUP DTQPA PSGAO QOPTK
# FOTRW QOQPA PSGAO LZWQO TRZOZ GKFPA UJOLP KTOGV RZWTQ PAPSG
# AOTKV VOFTP IPFPS DEWAM VOPFR ZPRAG GRZOF LFOPR KFOOA UKFOT
# PVOPF GVRWQ OFKAA WAMGK RQWRL ZPSJG QRZOR WQOCO OIOFX RFDRG'''


crypto = "MUST CHANGE MEETING LOCATION FROM BRIDGE TO UNDERPASS SINCE ENEMY AGENTS ARE BELIEVED TO HAVE BEEN ASSIGNED TO WATCH BRIDGE STOP MEETING TIME UNCHANGED XX"



## if user wants to perform frequency analysis for doi.txt
if choice == '1':
    print("FREQUENCY ANALYSIS FOR doi.txt\n\n")
    char_freq(doi_text)

## if user wants to perform frequency analysis for gadsby_text.txt
elif choice == '2':
    print("FREQUENCY ANALYSIS FOR gadsby_text.txt\n\n")
    char_freq(gadsby_text)

## if user wants to perform frequency analysis for crypto
elif choice == '3':
    print("FREQUENCY ANALYSIS FOR crypto.\n\n")
    char_freq(crypto)




