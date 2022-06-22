import datetime 
import pdb
import sys
import os
from time import strftime



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

    # reset daily progress if we are on a new day
    if get_last_save() != datetime.datetime.now().strftime("%A") and len(ppl) > 0:

        for name in ppl:
            clear_daily_progress(name)


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
        # automate the clearing of data when new day comes around
        # make document day method
        set_day(datetime.datetime.now().strftime("%A"))
        sys.exit()



def person_menu(ppl):
    date = datetime.datetime.now()
    #get person data
    idx = int(input("Enter the your person's index: "))
    person = ppl[idx - 1]
    #labels
    nut_categories = ["Calories", "Protein", "Carbohydrates", "Fat", "Sugar Limit", "Saturated Fat Limit"]
    # for totals
    person_data = get_data(person)
    # for daily
    person_data_day = get_data_day(person)
    


    # display that person's information

    # some totals
    print("-" * 40)
    print("|{0:^38s}|".format("Daily Macro Goals"))
    print("|{0:^38s}|".format('(' + person + ')'))
    draw_chart(nut_categories, person_data)
    
    
    
    # display some more options

    while True:    


        # daily progress
        print("-" * 40)
        print("|{0:^38s}|".format("Daily Progress"))
        print("|{0:^38s}|".format('(' + date.strftime("%A") + ')')) # the day of the week
        print("| {0:^37s}|".format(str(date)[0:11]))

        print('-' * 40)
        for i in range(len(person_data_day)):
            print("|    {0:<19} : {1:^12s}| ---{2:.2f}%".format(nut_categories[i], person_data_day[i] + '/' + person_data[i], (float(person_data_day[i]) / float(person_data[i]))* 100))
        print('-' * 40)
    
    # display some more options

    

        print("More options...\nAdd Meal Entry (1)\nReset day (2)\nBack (3)")

        option = int(input("ENTER: "))

        if option == 1:
            add_meal(person)

            # for totals
            person_data = get_data(person)
            # for daily
            person_data_day = get_data_day(person)

        elif option == 2:
            clear_daily_progress(person)
            pass
        elif option == 3:
            display_ppl(ppl)
            return
        else:
            print("Please enter an option between 1 and 5")
            option = input("ENTER: ")

def cur_day_menu(person):




    pass


def draw_chart(labels, data):

    print("-" * 40)
    for i in range(len(data)):
        print("|    {0:<19} : {1:^12s}|".format(labels[i], data[i]))

    print("-" * 40, end='\n')



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
    out_file.write('satfat = ' + str(lim_satfat) + '\n')

    out_file.write('calories_day = ' + '0' + '\n' )
    out_file.write('protein_day = ' + '0' + '\n' )
    out_file.write('carbs_day = ' + '0' + '\n')
    out_file.write('fat_day = ' + '0' + '\n')
    out_file.write('sugar_day = ' + '0' + '\n')
    out_file.write('satfat_day = ' + '0' + '\n\n')
    out_file.close()

def add_meal(person):


    # gather data from user 
    print('---Enter the nutritional value of your meal---')
    print("\namout of...")
    calories = input("Calories: ")
    protein = input("Protein: ")
    carbs = input("Carbs: ")
    fat = input("Fat: ")
    sugar = input("Sugar: ")
    satfat = input("Saturated Fat: ")

    data = [calories, protein, carbs, fat, sugar, satfat]

    #Write to file
    set_data_day(person, data)



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

def get_data_day(person):

    data = []

    out_file = open('data.txt', 'r')
    lines = out_file.readlines()

    for i in range(len(lines)):
        line = lines[i].split()

        if len(line) > 0 and line[2].rstrip('\n') == person:
            i += 7
            for j in range(6):
                data.append(lines[i].split()[2])
                i += 1
            return data




def set_data_day(person, data):


    # read from file
    out_file = open('data.txt', 'r')
    lines = out_file.readlines()
    out_file.close()

    for i in range(len(lines)):
        line = lines[i].split()

        if len(line) > 0 and line[2].rstrip('\n') == person:
            i += 7
            for j in range(6):
                line = lines[i].split()
                line[2] = str(int(line[2]) + int(data[j])) + '\n'
                lines[i] = " ".join(line)

                i += 1
            break
    
    # write to file
    out_file = open('data.txt','w')
    out_file.write("".join(lines))
    out_file.close()

def clear_daily_progress(person):
    out_file = open('data.txt','r')
    lines = out_file.readlines()
    out_file.close()

    for i in range(len(lines)):
        line = lines[i].split()

        if len(line) > 0 and line[2] == person:
            i += 7
            for j in range(6):
                line = lines[i].split()
                line[2] = '0' +'\n'
                lines[i] = " ".join(line)
                i += 1
            break


    #write to file
    out_file = open('data.txt', 'w')
    out_file.write("".join(lines))
    out_file.close()


def get_last_save():
    out_file = open('data.txt', 'r')
    lines = out_file.readlines()
    out_file.close()

    for line in lines:

        if len(line.split()) == 1 and line != "\n":
            return "".join(line)
    return 'garbage'


def set_day(day):

    # read data
    out_file = open('data.txt', 'r')
    lines = out_file.readlines()
    out_file.close()
    lines[len(lines) - 1] = day

    # write data
    out_file = open('data.txt', 'w')
    out_file.write("".join(lines))
    out_file.close()


if __name__ == "__main__":
    main()