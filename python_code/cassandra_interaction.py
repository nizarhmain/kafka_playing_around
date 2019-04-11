# check this link http://datastax.github.io/python-driver/getting_started.html

from cassandra.cluster import Cluster

cluster = Cluster(['172.40.0.9'])

session = cluster.connect('cycling')

print(session)

# dynamic query example
# it doesnt add the same query if the data is identical, wouldnt happen if we had a UUID but meh fuck it

data = {
     'race_year': 2016,
     'race_name':'Tour of Japan - Stage 4 - Minami > Shinshu',
     'cyclist_name':'Benjamin PRADES',
     'rank':1
}

session.execute(
    """
    INSERT INTO cycling.rank_by_year_and_name 
        (race_year, race_name, cyclist_name, rank) 
        VALUES (%(race_year)s, %(race_name)s, %(cyclist_name)s, %(rank)s)   
    """,
    data
)



# INSERT INTO cycling.rank_by_year_and_name (race_year, race_name, cyclist_name, rank) 
#    VALUES (2015, 'Tour of Japan - Stage 4 - Minami > Shinshu', 'Benjamin PRADES', 1);
# INSERT INTO cycling.rank_by_year_and_name (race_year, race_name, cyclist_name, rank) 
#    VALUES (2015, 'Tour of Japan - Stage 4 - Minami > Shinshu', 'Adam PHELAN', 2);
# INSERT INTO cycling.rank_by_year_and_name (race_year, race_name, cyclist_name, rank) 
#    VALUES (2015, 'Tour of Japan - Stage 4 - Minami > Shinshu', 'Thomas LEBAS', 3);
# INSERT INTO cycling.rank_by_year_and_name (race_year, race_name, cyclist_name, rank) 
#    VALUES (2015, 'Giro d''Italia - Stage 11 - Forli > Imola', 'Ilnur ZAKARIN', 1);
# INSERT INTO cycling.rank_by_year_and_name (race_year, race_name, cyclist_name, rank) 
#    VALUES (2015, 'Giro d''Italia - Stage 11 - Forli > Imola', 'Carlos BETANCUR', 2);
# INSERT INTO cycling.rank_by_year_and_name (race_year, race_name, cyclist_name, rank) 
#    VALUES (2014, '4th Tour of Beijing', 'Phillippe GILBERT', 1);
# INSERT INTO cycling.rank_by_year_and_name (race_year, race_name, cyclist_name, rank)  
#    VALUES (2014, '4th Tour of Beijing', 'Daniel MARTIN', 2);
# INSERT INTO cycling.rank_by_year_and_name (race_year, race_name, cyclist_name, rank)  
#    VALUES (2014, '4th Tour of Beijing', 'Johan Esteban CHAVES', 3);





# CREATE KEYSPACE blog
#     WITH REPLICATION = { 
#      'class' : 'SimpleStrategy', 
#      'replication_factor' : 1 
#     };


# CREATE TABLE IF NOT EXISTS "kc_events" (
#     event_id1 TEXT, 
#     event_id2 TEXT, 
#     event_ts TIMEUUID, 
#     event_data1 TEXT, 
#     event_data2 TEXT, 
# PRIMARY KEY ((event_id1, event_id2)));