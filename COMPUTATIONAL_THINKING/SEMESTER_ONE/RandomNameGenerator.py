# Importing Random Module
import random

#Initializing CONSTANT VALUES
FILE_FIRSTNAMES = "firstNames.txt"
FILE_LASTNAMES = "lastNames.txt"
FILE_FULLNAMES = "fullNames.txt"
REQUIRED_SIZE = 4000#this is the required size of the list' content.
is_file_Read = False#Checking, if file been read and the correct flow of program.

#Open 'FILE_FIRSTNAMES' and 'FILE_LASTNAMES' files in 'r' read-only mode.
#Using 'with' statement for better resource managements
try: #Checking for Exception
    with open(FILE_FIRSTNAMES,'r') as file:
        #Getting clean line from eachline Ignoring Whitespace charactor
        first_names_List = [each_line.strip() for each_line in file.readlines()]
        #Shuffle list content Before Trimming
        random.shuffle(first_names_List)
        #Trim 'LASTNAME_CONTENT' LIST UPTO REQUIRED_SIZE
        FIRSTNAME_LIST = first_names_List[:REQUIRED_SIZE]
        #setting 'True' if file been read successfully
        is_file_Read = True
# Accepting exception if file not found
except FileNotFoundError as Error:
    # Displaying Error Information
    print(f"Error : File {Error.filename} is Missing !")

if is_file_Read:#Proceeding if 'FILE_FIRSTNAME' file been read 
    is_file_Read = False#Setting it to default
    try: #Checking for Exception
        with open(FILE_LASTNAMES,'r') as file:
           #Getting clean line from eachline Ignoring Whitespace charactor
           last_names_List = [each_line.strip() for each_line in file.readlines()]
           #Shuffle list content Before Trimming
           random.shuffle(last_names_List)
           #Trim 'LASTNAME_CONTENT' LIST UPTO REQUIRED_SIZE
           LASTNAME_LIST = last_names_List[:REQUIRED_SIZE]
           #setting 'True' if file been read successfully
           is_file_Read = True
    # Accepting exception if file not found
    except FileNotFoundError as Error:
        # Displaying Error Information
        print(f"Error : File {Error.filename} is Missing !")

if is_file_Read:#Proceeding if both files been read 
    #open 'FILE_FULLNAMES' file in write mode to write shuffled Names in it
    with open(FILE_FULLNAMES,'w') as file:
        max_length=0;# to store the length of name
        longest_name_at_indx = -1;
        longest_name = "";
        #Generating shuffled full names using loop
        for indx in range(REQUIRED_SIZE):
         #Formating full name using string Interpolation
         full_name = f"{random.choice(FIRSTNAME_LIST)} {random.choice(LASTNAME_LIST)}"
         #checking for longest name passed into the list
         if max_length<len(full_name):#checking length
            max_length = len(full_name)#re-initializing max_length
            longest_name = full_name;
            longest_name_at_indx = (indx);#storing index of longest name
         #Writing random name generated, into 'FILE_FULLNAMES' file
         #prefixing each name with an index
         file.writelines(f"{indx+1}. {full_name}\n")
    #printing success message
    print("\nFile Successfully created !\n")
    #As index starts from 1 within the generated list,
    #adding 1 to locate right position of the name in file
    longest_name_at_indx+=1;
    #print longest name, generated within list
    print(f"The longest name generated : '{longest_name}' at index = {longest_name_at_indx}\n")