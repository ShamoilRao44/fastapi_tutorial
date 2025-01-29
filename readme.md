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

