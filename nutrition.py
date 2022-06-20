
import pdb
import sys
import os


# program that tracks daily nutrition and eventually weight and such

# Personal Macros
'''
PER...

DAY:
Calories = 3,204
Protein = 78 - (195) - 274 
Carbs = 342 - (427) - 598
Fat = 73 - (91) - 127
Sugar < 85
Saturated Fat < 36

MEAL:
Calories = 1,068
Protein = 65
Carbs = 143
Fat = 31
Sugar < 29
Saturated Fat < 12

'''

def main():

    ppl = get_names()

    print("\n- Nutrition Tracker -")

    while True:
        
        display_ppl(ppl)
        main_menu(ppl)
        

def display_ppl(ppl):


    print('-' * 40)

    if len(ppl) == 0:
        print("<There are no people registered in the system>")
        register_person(ppl)
        display_ppl(ppl)
        return

    print("|    People regestered in system       |")
    print('-' * 40)

    i = 1
    for name in ppl:
        print("|    {0} : {1:<30s}|".format(i, name))
        i+= 1
    
    print('-' * 40)


    pass




def main_menu(ppl):

    # user options = select person || exit
    print('Options...\nAdd Person (1)\nGoto Person (2)\nClear Person info (3)\nClear all data (4)\nExit (5)')
    option = int(input("ENTER: "))
    while int(option) < 1 or int(option) > 5:
        print("Please enter an option between 1 and 5")
        option = input("ENTER: ")

    if option == 1:
        register_person(ppl)

    elif option == 2:
        #this is the afforementioned sub menu
        person_menu(ppl)
       
    elif option == 3:
        #clear person info
        pass

    elif option == 4:
        wipe_all_data(ppl)

    elif option == 5:
        sys.exit()



def person_menu(ppl):
    #get person data
    idx = int(input("Enter the your person's index: "))
    person = ppl[idx - 1]
    person_data = get_data(person)
    nut_categories = ["Calories", "Protein", "Carbohydrates", "Fat", "Sugar Limit", "Saturated Fat Limit"]


    # display that person's information
    print("-" * 40)
    print("|            Macronutrients            |")
    print("-" * 40)
    for i in range(len(person_data)): 
        print("|    {0:<19} : {1:^12s}|".format(nut_categories[i], person_data[i]))
    print("-" * 40, end='\n\n')

    # display some more options
    

        
def register_person(ppl):

    # gather data from user 
    print('Please enter a person into the system...')
    name = str(input("Name: "))
    print("Please enter that person's daily nutritional goals...")
    calories = int(input("Calories: "))
    protein = int(input("Protein: "))
    carbs = int(input("Carbs: "))
    fat = int(input("Fat: "))
    lim_sugar = int(input("Sugar limit: "))
    lim_satfat = int(input("Saturated Fat limit: "))
    ppl.append(name)

    # write to file
    out_file = open('data.txt', 'a')
    out_file.write('name = ' + name + '\n')
    out_file.write('calories = ' + str(calories) + '\n')
    out_file.write('protein = ' + str(protein) + '\n')
    out_file.write('carbs = ' + str(carbs) + '\n')
    out_file.write('fat = ' + str(fat) + '\n')
    out_file.write('sugar = ' + str(lim_sugar) + '\n')
    out_file.write('satfat = ' + str(lim_satfat) + '\n\n')
    out_file.close()

    


def wipe_all_data(ppl):
    out_file = open('data.txt', 'w')
    out_file.close
    print('\nData cleared')
    ppl.clear()
    display_ppl(ppl)


def get_names():
    out_file = open('data.txt', 'r')
    names = []

    if os.stat("data.txt").st_size == 0:
        return names

    else:

        text = out_file.readlines()
        for line in text:
            line = line.split()
            if len(line) > 0 and line[0] == 'name':
                names.append(line[2])
        
    out_file.close()
    return names
    
def get_data(person):

    data = []

    out_file = open('data.txt', 'r')
    lines = out_file.readlines()

    for i in range(len(lines)):
        line = lines[i].split()

        if len(line) > 0 and line[2].rstrip('\n') == person:
            i += 1
            for j in range(6):
                data.append(lines[i].split()[2])
                i += 1
            return data
    
   






if __name__ == "__main__":
    main()