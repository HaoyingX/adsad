#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# USAGE:
#   python lab1_part1.py music_small.db

import sys
import sqlite3


# The database file should be given as the first argument on the command line
# Please do not hard code the database file!
db_file = sys.argv[1]

# We connect to the database using 
with sqlite3.connect(db_file) as conn:
    # This query counts the number of artists who became active in 1990
    year = (1990,)
    for row in conn.execute('SELECT count(*) FROM artist WHERE artist_active_year_begin=?', year):
        # Since there is no grouping here, the aggregation is over all rows
        # and there will only be one output row from the query, which we can
        # print as follows:
        print('Tracks from {}: {}'.format(year[0], row[0]))
        
        # The [0] bits here tell us to pull the first column out of the 'year' tuple
        # and query results, respectively.

    # ADD YOUR CODE STARTING HERE
    import pandas as pd

    def format(query):
        # Execute the query and load the result into a DataFrame
        df = pd.read_sql_query(query, conn)
        # Convert the DataFrame to a Markdown-formatted string
        markdown_table = df.to_markdown(index=False)
        print(markdown_table)


    
    # implement your solution to q1
    query_1 = """ 
              SELECT id, track_title 
              FROM track 
              WHERE track_lyricist LIKE 'W%'
              """
    format(query_1)
    
    print('---')
    
    # Question 2
    print('Question 2:')
    
    # implement your solution to q2
    query_2 = """
              SELECT DISTINCT(track_explicit) 
              FROM track 
              WHERE track_explicit IS NOT NULL
              """        
    format(query_2)
    
    print('---')
    
    # Question 3
    print('Question 3:')
    
    # implement your solution to q3
    query_3 = """
              SELECT id,track_title 
              FROM track 
              Order by track_listens DESC 
              LIMIT 1
              """
    format(query_3)
        
    print('---')
    
    # Question 4
    print('Question 4:')
    
    # implement your solution to q4
    query_4 = """
              SELECT  COUNT(*)
              FROM artist 
              WHERE artist_related_projects IS NOT NULL
              """
    format(query_4)
        
    print('---')
    
    # Question 5
    print('Question 5:')
    
    # implement your solution to q5
    query_5 = """
              SELECT COUNT(*),track_language_code 
              FROM track WHERE track_language_code IS NOT NULL 
              GROUP BY track_language_code 
              HAVING COUNT(*) = 4
              """
    format(query_5)
        
    print('---')
    
    # Question 6
    print('Question 6:')
    
    # implement your solution to q6
    query_6 = """
              SELECT COUNT(*) 
              FROM track 
              JOIN artist 
              ON track.artist_id = artist.id  
              WHERE artist_active_year_begin >= 1990 
                AND artist_active_year_end <= 1999 
                AND artist_active_year_end >= artist_active_year_begin
              """
    format(query_6)
    
    print('---')
    
    # Question 7
    print('Question 7:')
    
    # implement your solution to q7
    query_7 = """
              SELECT COUNT(DISTINCT(album_producer)) AS "#_of_distinct_album",artist_name 
              FROM album 
              JOIN track 
              ON album.id = track.album_id 
              JOIN artist 
              ON artist.id = track.artist_id 
              WHERE album_producer IS NOT NULL 
              GROUP BY artist_name 
              ORDER BY "#_of_distinct_album" DESC 
              LIMIT 3
              """
    format(query_7)
    
    print('---')
    
    # Question 8
    print('Question 8:')
    
    # implement your solution to q8
    query_8 = """
              SELECT track.id, track_title, artist_name 
              FROM track 
              JOIN artist 
              ON track.artist_id = artist.id 
              JOIN album 
              ON track.album_id = album.id 
              ORDER BY ABS(track_listens-album_listens) DESC 
              LIMIT 1
              """
    format(query_8)
    print('---')
