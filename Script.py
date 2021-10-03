import csv

file = 'Contacts.csv'

def show_menu():
    print(f"{'='*10}Phone Book{'='*10}")
    print('[1] Show Contact')
    print('[2] Add Contact')
    print('[3] Update Contact')
    print('[4] Search Contact')
    print('[5] Delete Contact')
    print('[0] Exit')

    selected_number = str(input('\nInput number to select menu: '))
    if selected_number == '1':
        pass
    elif selected_number == '2':
        pass
    elif selected_number == '3':
        pass
    elif selected_number == '4':
        pass
    elif selected_number == '5':
        pass
    elif selected_number == '0':
        pass
    else:
        print('\nUnknown command\n')

if __name__ == '__main__':
    show_menu()


