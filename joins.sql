/*
Let's say we have these tables:
*/

CREATE TABLE author (
  id serial PRIMARY KEY,
  name varchar
);

CREATE TABLE tweet (
  id serial PRIMARY KEY,
  tweet varchar(140),
  author_id integer
);





/*
And the following data:

author table:

id |    name
----+-------------
 1 | airportyh
 2 | phamous2day
 3 | scrumlord

tweet table:

id |                                               tweet                                                | author_id
----+----------------------------------------------------------------------------------------------------+-----------
 1 | Nobody could implement quicksort quick enough and so bubblesort won.                               |         1
 3 | Covering data structures in an intro class, righteous!!! Thanks @cs50  https://study.cs50.net/     |         2
 4 | NTS: study these data structures - hash table, linked lists, binary tree, graph traversal, sorting |         2
 2 | Forgetting is a feature. http://revisionisthistory.com/episodes/04-carlos-doesnt-remember          |         1
 5 | We become aware of the void as we fill it.                                                         |

*/

-- A cartesian product join:

select
  author.name, tweet.tweet
from
  author, tweet;







/*
The above query will give you all combinations of author and tweet, regardless of whether they are related or not. Meaning that if you had m authors and n tweets, it will return m times n rows. So 15 rows total:


name     |                                               tweet
-------------+----------------------------------------------------------------------------------------------------
airportyh   | Nobody could implement quicksort quick enough and so bubblesort won.
airportyh   | Covering data structures in an intro class, righteous!!! Thanks @cs50  https://study.cs50.net/
airportyh   | NTS: study these data structures - hash table, linked lists, binary tree, graph traversal, sorting
airportyh   | Forgetting is a feature. http://revisionisthistory.com/episodes/04-carlos-doesnt-remember
airportyh   | We become aware of the void as we fill it.
phamous2day | Nobody could implement quicksort quick enough and so bubblesort won.
phamous2day | Covering data structures in an intro class, righteous!!! Thanks @cs50  https://study.cs50.net/
phamous2day | NTS: study these data structures - hash table, linked lists, binary tree, graph traversal, sorting
phamous2day | Forgetting is a feature. http://revisionisthistory.com/episodes/04-carlos-doesnt-remember
phamous2day | We become aware of the void as we fill it.
scrumlord   | Nobody could implement quicksort quick enough and so bubblesort won.
scrumlord   | Covering data structures in an intro class, righteous!!! Thanks @cs50  https://study.cs50.net/
scrumlord   | NTS: study these data structures - hash table, linked lists, binary tree, graph traversal, sorting
scrumlord   | Forgetting is a feature. http://revisionisthistory.com/episodes/04-carlos-doesnt-remember
scrumlord   | We become aware of the void as we fill it.
(15 rows)

*/

/*

Inner Join:

An inner join filters the results of the cartesian product join
and returns only the rows from that join which match the conditions

*/

select
  author.name, tweet.tweet
from
  author, tweet
where
  author.id = tweet.author_id;

-- or equivalently:

select
  *
from
  author
inner join
  tweet on author.id = tweet.author_id;

/*

name     |                                               tweet
-------------+----------------------------------------------------------------------------------------------------
airportyh   | Nobody could implement quicksort quick enough and so bubblesort won.
phamous2day | Covering data structures in an intro class, righteous!!! Thanks @cs50  https://study.cs50.net/
phamous2day | NTS: study these data structures - hash table, linked lists, binary tree, graph traversal, sorting
airportyh   | Forgetting is a feature. http://revisionisthistory.com/episodes/04-carlos-doesnt-remember
(4 rows)

*/

/*

LEFT OUTER JOIN
a left outer join will include every row in the table on the left in the results regardless of whether that row matched the join condition. If the right side of the join is not there, all the values in the resulting columns that have to come from the right side are NULL.

*/

select
	author.name, tweet.tweet
from
	author
left outer join
  tweet on author.id = tweet.author_id;

/*

name     |                                               tweet
-------------+----------------------------------------------------------------------------------------------------
airportyh   | Nobody could implement quicksort quick enough and so bubblesort won.
phamous2day | Covering data structures in an intro class, righteous!!! Thanks @cs50  https://study.cs50.net/
phamous2day | NTS: study these data structures - hash table, linked lists, binary tree, graph traversal, sorting
airportyh   | Forgetting is a feature. http://revisionisthistory.com/episodes/04-carlos-doesnt-remember
scrumlord   |
(5 rows)

*/

/*

RIGHT OUTER JOIN

is the inverse of LEFT OUTER JOIN. Every row for the table on the right will be included.

*/

select
	author.name, tweet.tweet
from
	author
right outer join
  tweet on author.id = tweet.author_id;

/*

name     |                                               tweet
-------------+----------------------------------------------------------------------------------------------------
airportyh   | Nobody could implement quicksort quick enough and so bubblesort won.
phamous2day | Covering data structures in an intro class, righteous!!! Thanks @cs50  https://study.cs50.net/
phamous2day | NTS: study these data structures - hash table, linked lists, binary tree, graph traversal, sorting
airportyh   | Forgetting is a feature. http://revisionisthistory.com/episodes/04-carlos-doesnt-remember
         | We become aware of the void as we fill it.
(5 rows)
*/

-- full outer join

select
	author.name, tweet.tweet
from
	author
full outer join
  tweet on author.id = tweet.author_id;

/*

name     |                                               tweet
-------------+----------------------------------------------------------------------------------------------------
airportyh   | Nobody could implement quicksort quick enough and so bubblesort won.
phamous2day | Covering data structures in an intro class, righteous!!! Thanks @cs50  https://study.cs50.net/
phamous2day | NTS: study these data structures - hash table, linked lists, binary tree, graph traversal, sorting
airportyh   | Forgetting is a feature. http://revisionisthistory.com/episodes/04-carlos-doesnt-remember
         | We become aware of the void as we fill it.
scrumlord   |
(6 rows)

*/

/*

Why is outer join useful?
It is useful for tallying the many side of a one-to-many or a many-to-many association using aggregation.

This query counts how many tweets each author has posted, and also how many total characters each author has authored.
*/

select
	author.id,
	author.name,
  sum(case when tweet.id is NULL then 0 else 1 end) as tweet_count,
	sum(char_length(tweet.tweet)) as character_count
from
	author
full outer join
  tweet on author.id = tweet.author_id
group by
  author.id;

/*

id |    name     | character_count | tweet_count
----+-------------+-----------------+-------------
   |             |              42 |           1
 2 | phamous2day |             193 |           2
 1 | airportyh   |             157 |           2
 3 | scrumlord   |                 |           0
(4 rows)

*/

-- How did that work? Check out this query:

select
	author.id,
	author.name,
  case when tweet.id is NULL then 0 else 1 end as tweet_count,
	char_length(tweet.tweet) as character_count,
  tweet.tweet
from
	author
full outer join
  tweet on author.id = tweet.author_id;

/*

It returns:

id |    name     | tweet_count | character_count |                                               tweet
----+-------------+-------------+-----------------+----------------------------------------------------------------------------------------------------
 1 | airportyh   |           1 |              68 | Nobody could implement quicksort quick enough and so bubblesort won.
 2 | phamous2day |           1 |              95 | Covering data structures in an intro class, righteous!!! Thanks @cs50  https://study.cs50.net/
 2 | phamous2day |           1 |              98 | NTS: study these data structures - hash table, linked lists, binary tree, graph traversal, sorting
 1 | airportyh   |           1 |              89 | Forgetting is a feature. http://revisionisthistory.com/episodes/04-carlos-doesnt-remember
   |             |           1 |              42 | We become aware of the void as we fill it.
 3 | scrumlord   |           0 |                 |
(6 rows)

Tweet count is either a 1 or a 0, because each row can represent an individual tweet - although the tweet could also be absent in the case that that user has never posted a tweet. So we use the case statement:

case when tweet.id is NULL then 0 else 1 end

to return a 0 if there isn't a tweet and 1 if there is.

character_count is the character length of the tweet and we got that by calling the char_length() function. Once we have this query, we can apply the sum() function to aggregate the character_count and the tweet_count in combination with group by author.id, and that's how we got the previous SQL statement.

*/
