from os.path import exists
from csv_file import creating
from writing_file import writing_scv
from writing_file import writing_txt


path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    creating()

writing_scv()
writing_txt()