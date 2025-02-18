# Homework 1 results

Your name: 

## Part 1
Paste the results of your queries for each question given in the README below:

1.
|    id | track_title          |
|------:|:---------------------|
| 22344 | Outburst             |
| 66084 | Got My Modem Working |
| 66096 | Mistress Song        |
2.
| track_explicit   |
|:-----------------|
| Radio-Safe       |
| Radio-Unsafe     |
| Adults-Only      |
3.
|    id | track_title   |
|------:|:--------------|
| 62460 | Siesta        |
4.
|   COUNT(*) |
|-----------:|
|        453 |
5.
|   COUNT(*) | track_language_code   |
|-----------:|:----------------------|
|          4 | de                    |
|          4 | ru                    |
6.
|   COUNT(*) |
|-----------:|
|         34 |
7.
|   #_of_distinct_album | artist_name          |
|----------------------:|:---------------------|
|                     6 | U Can Unlearn Guitar |
|                     6 | Ars Sonor            |
|                     5 | Disco Missile        |
8.
|    id | track_title   | artist_name   |
|------:|:--------------|:--------------|
| 76008 | JessicaBD     | Cody Goss     |

## Part 2

- Execution time before optimization:

Mean time: 0.142 [seconds/query]

Best time: 0.027 [seconds/query]


- Execution time after optimization:

Mean time: 0.128 [seconds/query]

Best time   : 0.025 [seconds/query]


- Briefly describe how you optimized for this query:

I try to use a multi-column index

- Did you try anything other approaches?  How did they compare to your final answer?

I try to use a single-column index:

cursor.execute("CREATE INDEX idx_artist_id ON track(artist_id);")

cursor.execute("CREATE INDEX idx_album_id ON track(album_id);")

cursor.execute("CREATE INDEX idx_album_listens ON album(album_listens);")

almost the same with a little higher mean time
