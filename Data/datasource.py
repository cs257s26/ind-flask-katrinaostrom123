import psycopg2 as ps
from . import psqlConfig as config


def connect():
    """Establishes a connection to the database with the following credentials:
        user - username, which is also the name of the database
        password - the password for this database on perlman

    Returns: a database connection.

    Note: exits if a connection cannot be established.
    """
    try:
        connection = ps.connect(database=config.database, user=config.user, password=config.password, host="localhost")
    except Exception as e:
        print("Connection error: ", e)
        exit()
    return connection

def get_leaderboard(connection, animalSearched: str) -> list:
    """Retrieves top 10 users that logged that animal

    Args:
        connection (psycopg2.connection) - the connection to the database
        animalSearched (str) - the animal we are searching for

    Returns:
        list - a list of all instances of usernames and amount they logged a certain animal.
    """
    try:
        cursor = connection.cursor()
        query = """
            SELECT observer, COUNT(*) AS frequency
            FROM mammals_table
            WHERE common_name = %s
            GROUP BY observer
            ORDER BY COUNT(*) DESC
            LIMIT 10;
        """
        cursor.execute(query, (animalSearched,))
        return cursor.fetchall()

    except Exception as e:
        print ("Something went wrong when executing the query: ", e)
        return None


def get_random_location(connection) -> str:
    """Retrieves a random location

    Args:
        connection (psycopg2.connection) - the connection to the database

    Returns:
        string - a random location
    """
    try:
        cursor = connection.cursor()
        query = """
            SELECT place_guess
            FROM mammals_table
            ORDER BY RANDOM()
            LIMIT 1;
        """
        cursor.execute(query)
        return cursor.fetchall()

    except Exception as e:
        print ("Something went wrong when executing the query: ", e)
        return None

def get_top5Animals(connection, location: str) -> list:
    """Gets the top 5 animals at a location

    Args:
        connection (psycopg2.connection) - the connection to the database
        location (str) - the location we are looking at


    Returns:
        list - the top 5 animals that are found there
    """

    try:
        cursor = connection.cursor()
        query = """
            SELECT common_name, COUNT(*) AS frequency
            FROM mammals_table
            WHERE place_guess = %s
            GROUP BY common_name
            ORDER BY COUNT(*) DESC
            LIMIT 5;
        """
        cursor.execute(query, (location,))
        return cursor.fetchall()

    except Exception as e:
        print ("Something went wrong when executing the query: ", e)
        return None


def main():
    # Connect to the database
    connection = connect()

    # Execute a simple query: which users submitted the most Coyote entries?
    results = get_leaderboard(connection, "Coyote")
    
    if results is not None:
        print("Query results: ")
        for item in results:
            print(item)

    # Disconnect from database
    connection.close()

if __name__ == '__main__':
    main()
