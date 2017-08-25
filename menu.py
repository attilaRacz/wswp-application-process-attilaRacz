import psycopg2
import database
import actions

connect_str = "dbname='raczattila' user='attila' host='localhost' password='Palmapalma12'"
connection = psycopg2.connect(connect_str)
connection.autocommit = True
cursor = connection.cursor()

menu = {}
menu['1'] = "Mentor names"
menu['2'] = "Mentor nicknames from Miskolc"
menu['3'] = "Carol's full name and phone number"
menu['4'] = "The other girl's full name and phone number"
menu['5'] = "New applicant"
menu['6'] = "Phone number changed"
menu['7'] = "Delete applicants"
menu['8'] = "Show mentors"
menu['9'] = "Show applicants"
menu['q'] = "Exit"
while True:
    options = sorted(menu.keys())
    for entry in options:
        print(entry, menu[entry])

    selection = input("Please Select:")
    if selection == '1':
        database.main(actions.mentor_names())
    elif selection == '2':
        database.main(actions.nicks_from_miskolc())
    elif selection == '3':
        database.main(actions.carol_full_name())
    elif selection == '4':
        database.main(actions.owner_of_the_hat())
    elif selection == '5':
        database.main(actions.new_applicant())
    elif selection == '6':
        database.main(actions.phone_num_changed())
    elif selection == '7':
        database.main(actions.delete_applicants())
    elif selection == '8':
        database.main(actions.show_mentors())
    elif selection == '9':
        database.main(actions.show_applicants())
    elif selection == 'q':
        break
    else:
        print("Unknown Option Selected!")
