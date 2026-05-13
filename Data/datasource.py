import psycopg2 as ps
import psqlConfig as config


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
    """Retrieves all users that logged that animal

    Args:
        connection (psycopg2.connection) - the connection to the database
        animalSearched (str) - the animal we are searching for

    Returns:
        list - a list of all instances of usernames that logged a certain animal.
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

main()
