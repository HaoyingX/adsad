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
Mean time: 0.080 [seconds/query]
Best time: 0.016 [seconds/query]
- Execution time after optimization:
Mean time: 0.070 [seconds/query]
Best time   : 0.013 [seconds/query]
- Briefly describe how you optimized for this query:
artist.id is indexed as it is appended to GROUP BY and JOIN ON.
album.id is indexed as it is appended to JOIN.
album_listens is index as it is used to fliter the rows. 
- Did you try anything other approaches?  How did they compare to your final answer?
I also tried indexing track(album_id) and track(artist_id) additionally, but the final answer didn't change. Specifically, the indexing of artist.id critically speeded up the query, then the indexing of either album.id or track.album_id had the second effects on time improvement. 
