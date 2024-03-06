##### opening a file #####
text_file = open('file_directory/file_name.txt', encoding='utf-8')

##### closing a file #####
text_file.close()

### OR ###
with open('file_name.txt', encoding='utf-8') as text_file:
    text_file.read()

######## MODES ########
#append mode
text_file = open('file_directory/file_name.txt', mode='a', encoding='utf-8')

#write mode
text_file = open('file_directory/file_name.txt', mode='w' encoding='utf-8')

#### READING A FILE ####
# Lets say the text_file.txt contains the following sentence:
# The door swung open to reveal pink giraffes and red elephants.

text_file = open('text_file.txt', encoding='utf-8')
print(text_file.read())
# => The door swung open to reveal pink giraffes and red elephants.

#### WRITING TO A FILE ####
#Writing to a file
with open('log_file.txt', mode='w', encoding='utf-8') as log_file:
    log_file.write('Log 1')

with open('log_file.txt', mode='a', encoding='utf-8') as log_file:
    log_file.write('Log 2')