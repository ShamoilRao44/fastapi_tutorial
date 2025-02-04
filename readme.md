lesson 8:
 -imported Base model from pydantic.
 -created class Post which extends BaseModel and defined schema for create_post method by declaring title as string, content as string, published as bool defaulting to true, and rating to optional int oterwise None.
 -changed create_post methods parameter to accept a object of type Post and store it in argument named post, returned different values of this object.
---------------------------------------------------------------------------------------------------------

lesson 9;
 - changed path for creting post from createpost to posts, following the naming convetion.
 - made an array of dictionaies to store the new post being created by api and set two default posts.
 - returned my_posts in get post api.
--------------------------------------------------------------------------------------------------------

lesson 10:
 - in create_post function first convert the incoming request model to dictionary,
 - import randrange from random library and use it assign a random integer between 3 to 1million to the id key of podt dictionary.
 -append this post dictionary to my posts list.
 return this dictionary as aresponse of create post api
---------------------------------------------------------------------------------------------------------

lesson 11:
- make a new path operation @app.get("/posts/{id}")
- the function will use this path parameter id to fetch a particular post.
- make a function findpost which will traverse the my-posts list in ordre to find post.
- if we dont spcify id:int in method parameter the default  type of path parameter will be string but since our id parameter in each dictionary of my posts list is int we have to convert id  into integer.
- import httpexception from fastapi in order to raise an htp exceptin when a post is not found
- import status from fstapi to assign proper status codes to exception and  responses, this class stores all the diferent status codes so we dont have to remember what is for what.
- if a new api lets say @app.get("/posts/latest") is to be defined thei should be defined above this @app.get("/posts/{id}") api because otherwise python will the frist api and hence latest would be taken as path parmaeter {id}. which will then generate error because latest cant be converted to int.
---------------------------------------------------------------------------------------------------------

lesson 12:
- write api for deleting a post with path paramter id.
- we give a status code parameter in decorator in order to change the default status code which is 200 OK, which should not be returned in case of a delete api
---------------------------------------------------------------------------------------------------------

lesson 13:
- write api for updating a post using http put method.
- take id and updated post as path parameters.
- find the index of post with given id.
- convert incoming post in dict.
- set id parameter of this dict to incoming id because in incoming post there won't be a id parameter.
- replace post at index with this new dict
---------------------------------------------------------------------------------------------------------

lesson 14:
- restructure code by making a folder named app and first make a file in it named "__init__.py" which will make thisfolder a python package.
- now move yor mai file in app folder.
- the command for running the main should now be "uvicorn app.main:app --reload".
---------------------------------------------------------------------------------------------------------

lesson 17:
-install psycopg2
-import psycopg2 and realdictcursor from psycopg2.extras.
-use try and except block for connecting to database.
-realdictcursor is used so that the returned values form databse is mapped withh column name and not
just the values
-analyze code changes to understand how queries are being run.
-we directly do not put input parmeters in queries but rather use %s to safeguard from SQL injection attacks.
---------------------------------------------------------------------------------------------------------

lesson 18:
-install sqlalchemy, which is a ORM(object relational mapper). an ORM is an interface between backend code and database. it give built in languge functions(python methods in our case) to interactt with database. It makes the use of a database driver like psycopg2, in order to interact with database though.
---------------------------------------------------------------------------------------------------------

lesson 19:
-added ceated_at attribute i post class of model.py.
-used sqlalchemy in get all posts
---------------------------------------------------------------------------------------------------------

lesson 20:
-create post changed to use sqlalchemy. 
-here **post.model_dump() is used to convert incoming post variable first into a dictionary and then ** is going to convert it into like this models.Post(title = post.title, content = post.content and so on).
-refresh funtion is used as an equivalent of returning* statement of sql in order to return new created entries.
---------------------------------------------------------------------------------------------------------