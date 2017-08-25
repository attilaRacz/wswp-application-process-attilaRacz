import psycopg2
import database

connect_str = "dbname='raczattila' user='attila' host='localhost' password='Palmapalma12'"
connection = psycopg2.connect(connect_str)


def plain_text(text):
    return str(text).replace(',', '').replace("'", '').replace('(', '').replace(')', '').replace('[', '').replace(']', '')


def mentor_names():
    cursor = connection.cursor()
    cursor.execute("SELECT first_name, last_name FROM mentors;")
    rows = cursor.fetchall()
    print("\nMentor names:\n")
    for row in rows:
        print(plain_text(row))
    print('\n')
    cursor.close()


def nicks_from_miskolc():
    cursor = connection.cursor()
    cursor.execute("SELECT nick_name FROM mentors WHERE city='Miskolc';")
    print("\nNicknames of mentors from Miskolc:\n")
    rows = cursor.fetchall()
    for row in rows:
        print(plain_text(row))
    print('\n')
    cursor.close()


def carol_full_name():
    cursor = connection.cursor()
    cursor.execute("SELECT CONCAT (first_name, ' ', last_name) FROM applicants AS full_name WHERE first_name='Carol';")
    print("\nCarol's full name:\n")
    rows = cursor.fetchall()
    for row in rows:
        print(plain_text(row))
    print('\n')
    cursor.close()


def carol_full_name():
    cursor = connection.cursor()
    cursor.execute("SELECT CONCAT (first_name, ' ', last_name), '-', phone_number FROM applicants AS full_name WHERE first_name='Carol';")
    print("\nCarol's full name and phone number:\n")
    rows = cursor.fetchall()
    for row in rows:
        print(plain_text(row))
    print('\n')
    cursor.close()


def owner_of_the_hat():
    cursor = connection.cursor()
    cursor.execute("SELECT CONCAT (first_name, ' ', last_name), '-', phone_number FROM applicants AS full_name WHERE email LIKE '%@adipiscingenimmi.edu';")
    print("\nThe hat belongs to:\n")
    rows = cursor.fetchall()
    for row in rows:
        print(plain_text(row))
    print('\n')
    cursor.close()


def new_applicant():
    cursor = connection.cursor()
    cursor.execute("INSERT INTO applicants (first_name, last_name, phone_number, email, application_code) VALUES (%s, %s, %s, %s, %s);", ("Markus", "Schaffarzyk", "003620/725-2666", "djnovus@groovecoverage.com", 54823))
    cursor.execute("SELECT * FROM applicants WHERE application_code=54823;")
    print("\nNew applicant:\n")
    rows = cursor.fetchall()
    for row in rows:
        print(plain_text(row))
    print('\n')
    cursor.close()


def phone_num_changed():
    cursor = connection.cursor()
    cursor.execute("UPDATE applicants SET phone_number='003670/223-7459' WHERE first_name='Jemima' AND last_name='Foreman';")
    cursor.execute("SELECT * FROM applicants WHERE first_name='Jemima' AND last_name='Foreman';")
    print("\nPhone number have changed:\n")
    rows = cursor.fetchall()
    for row in rows:
        print(plain_text(row))
    print('\n')
    cursor.close()


def delete_applicants():
    cursor = connection.cursor()
    cursor.execute("DELETE FROM applicants WHERE email LIKE '%@mauriseu.net';")
    print("\nApplicants removed\n")
    cursor.close()


def show_applicants():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM applicants")
    print("\nApplicants:\n")
    rows = cursor.fetchall()
    for row in rows:
        print(plain_text(row))
    print('\n')
    cursor.close()


def show_mentors():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM mentors")
    print("\nMentors:\n")
    rows = cursor.fetchall()
    for row in rows:
        print(plain_text(row))
    print('\n')
    cursor.close()
