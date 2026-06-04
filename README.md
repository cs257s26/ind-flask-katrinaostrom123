# README

Individual Flask project.

Type "/game" after the URL to play the game

http://127.0.0.1/game 

Type "/leaderboard/animal_name" after the URL to get the leaderboard for a certain animal name, fill in "animal_name" with the common species name, like coyote.

http://127.0.0.1/leaderboard/Coyote 


To copy data into database:

`\copy mammals_table FROM 'mammals.csv' DELIMITER ',' CSV`


**Describe the process by which you decided how to represent your data in your database. Include why you selected the number of tables you did, how you decided what data to include and exclude, why you selected the datatypes you did, and what the primary keys are.**

I used `double precision` for my longitude and lattitude, as the length of those numbers could greatly vary, `timestamp` to represent the time, `int` to represent each entry's ID, and `text` to represent my strings of text. I only needed to select a single table, and I removed all the columns whose data didn't get used in any of the 3 user stories. The first column, id, is acts as the primary key as each entry is assigned a unique id. 

**Explain how each of your queries represents a user story. What does the query do, and how does this match all or part of a user story?**

Leaderboard User Story:

My `get_leaderboard(connection, animalSearched: str) -> list:` function makes a query to get the top 10 users that submitted sightings of a certain animal, and the amount of sightings they logged. This is all I needed for the Leaderboard user story. 

Game User Story:

I used two queries to fulfil this user story. 
My `def get_random_location(connection) -> str:` gets a random location from the table and returns it. My `get_top5Animals(connection, location: str) -> list:` function then uses that location to return a list of the most common 5 animals that are found in that location. It matches all of the Game user story.
 
