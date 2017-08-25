import psycopg2
import actions


def main(function):
    connect_str = "dbname='raczattila' user='attila' host='localhost' password='Palmapalma12'"
    connection = psycopg2.connect(connect_str)
    connection.autocommit = True
    try:
        function

    except psycopg2.DatabaseError as exception:
        print(exception)

    finally:
        if connection:
            connection.close()

if __name__ == "__main__":
    main()
