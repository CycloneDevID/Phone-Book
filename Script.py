import csv
import os
import platform

myfile = 'D:/Programming/Hacktoberfest/2021/Phone-Book/Contacts.csv'

def main_menu():
    print(f"{'='*10}Phone Book{'='*10}")
    print('A simple program to save and manage contact lists in the phone book.\n')
    print(f"{'='*10}Main Menu{'='*10}")
    print('[1] Show Contact')
    print('[2] Add Contact')
    print('[3] Update Contact')
    print('[4] Search Contact')
    print('[5] Delete Contact')
    print('[0] Exit')

    selected_number = str(input('\nInput number to select menu: '))
    if selected_number == '1':
        show_contact()
    elif selected_number == '2':
        add_contact()
    elif selected_number == '3':
        pass
    elif selected_number == '4':
        pass
    elif selected_number == '5':
        pass
    elif selected_number == '0':
        pass
    else:
        print('\nUnknown command.\n')

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def back_to_main_menu():
    input('\nPress enter to return to the main menu...')
    clear_screen()
    main_menu()

def add_contact_to_temporary():
    contact = []
    with open(myfile, mode='r', encoding='UTF-8', newline='\n') as my_csv_file:
        file = csv.DictReader(my_csv_file)
        for data in file:
            contact.append(data)
    
    return contact

def show_contact_from_temporary():
    tmp_contact = add_contact_to_temporary()

    if not tmp_contact:
        print('No contact yet.')
    else:
        field = list(tmp_contact[0].keys())
        print(f"No\t{field[0]}\t\t{field[1]}")
        for i in range(len(tmp_contact)):
            print(f"{i+1}\t{tmp_contact[i]['Name']}\t{tmp_contact[i]['Contact']}")

def show_contact():
    clear_screen()

    print(f"{'='*10}Show Contact{'='*10}")
    show_contact_from_temporary()

    back_to_main_menu()

def add_contact():
    clear_screen()

    print(f"{'='*10}Add Contact{'='*10}")
    name = str(input('Name \t: '))
    contact = str(input('Contact : '))
    
    add = str(input('\nadd to contact list? [y/n]: '))

    if add.lower() == 'y':
        with open(myfile, mode='a', encoding='UTF-8', newline='\n') as my_file_csv:
            fieldnames = ['Name','Contact']
            file = csv.DictWriter(my_file_csv, fieldnames=fieldnames)
            file.writerow({'Name':name,'Contact':contact})
            print('\ncontact added successfully.')
        back_to_main_menu()
    elif add.lower() == 't':
        print('\ncontact not added.')
        back_to_main_menu()
    else:
        print('\nUnknown command.')
        back_to_main_menu()

if __name__ == '__main__':
    main_menu()