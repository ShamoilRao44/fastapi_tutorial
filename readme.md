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