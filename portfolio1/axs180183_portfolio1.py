import re
import pickle
import sys

#This is the person class which contains 5 class variables as seen below
class Person:
    last = ''
    first = ''
    mi = ''
    id = ''
    phone = ''


    #the init constructor initilalizes a person object with the respective values from parameters
    def __init__(self,last_name,first_name,middle_initials, id_num, phone_num):
        #print(last_name,first_name)
        self.last = last_name
        self.first = first_name
        self.mi = middle_initials
        self.id = id_num
        self.phone = phone_num

    #the display function prints and displays each variable of a particular perosn object
    def display(self):
        print(f"Employee id: {self.id}\n        {self.first} {self.mi} {self.last}\n        {self.phone}")


#this function handles the processing of the input file and creating the dictionary of people
def process_csv(filename):
    file = open(filename)
    file.readline()
    #the line below helps split each line of input into a seperate element in an array
    file = file.read().split('\n')
    people = {}
    #The below processing is done for each line/person
    for person in file:

        #The variables are split on a ','
        person_arr = person.split(',')
        
        #Below, each variable is processed seperately and modified if necessary
        last_name = person_arr[0].capitalize()
        first_name = person_arr[1].capitalize()
        middle_initial = person_arr[2]
        if middle_initial != '':
            middle_initial = middle_initial.upper()
        else:
            middle_initial = 'X'   # This 

        id_num = person_arr[3]
        #Here, the id is modified if necessary, using regex the user is prompted to re-enter the id
        while re.match('^[A-Z][A-Z][0-9][0-9][0-9][0-9]$', id_num, flags=re.IGNORECASE) == None:
            print(f'ID Invalid: {id_num}')
            print('ID is two letters followed by 4 digits')
            id_num = input('Please enter a valid id: ')
        
        phone_num = person_arr[4]
        ##Here, the phone number is modified if necessary, using regex the user is prompted to re-enter the id
        while re.match('^[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]$', phone_num) == None:
            print(f'Phone {phone_num} is invalid')
            print('Enter phone number in form 123-456-7890')
            phone_num = input('Enter phone number: ')
        #Below, all person objects are put into a dictionary unless there is a duplicate 
        if id_num in people:
            print('This ID {id_num} already exists in the dictionary! Please use another ID for this person')
            return None
        else:
            people[id_num] = Person(last_name,first_name,middle_initial,id_num.upper(),phone_num)

    return people


if __name__ == "__main__":
    path = ''
    #this checks for the file path as a sys arg
    if len(sys.argv) <2:
        print('Please provide the path to the data file as a system arg')
    else:
        path = sys.argv[1]
        people = process_csv(path)

        #Below the code handles dumping the dictionary into a pickle file, loading from it again and printing the person objects
        if people !=None:
            pickle.dump(people, open('people.p','wb'))
            new_people = pickle.load(open('people.p', 'rb'))
            print()
            print('Employee List: ')
            print()
            for person in new_people:
                new_people[person].display()
                print()
