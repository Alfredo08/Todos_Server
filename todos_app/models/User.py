from flask import flash
from todos_app.config.MySQLConnection import connectToMySQL
from todos_app.models.Todo import Todo

class User:
    def __init__( self, username, password ):
        self.username = username
        self.password = password
        self.todos = []
    
    def printInfo( self ):
        print(f"username: {self.username} password: {self.password} ")

    @classmethod
    def get_all_users( cls, flag = False ):
        query = "SELECT * FROM users;"
        results = connectToMySQL( "todos_db" ).query_db( query )
        
        if flag == True:
            return results
        else:
            users = []
            for user in results:
                users.append( User( user['username'], user['password']) )
            
            return users
    
    @classmethod
    def add_user( cls, newUser ):
        query = "INSERT INTO users(username,password) VALUES(%(username)s, %(password)s);"
        data = {
            "username" : newUser.username,
            "password" : newUser.password
        }
        result = connectToMySQL( "todos_db" ).query_db( query, data )
        return result
    
    @classmethod
    def delete_user( cls, username ):
        query = "DELETE FROM users WHERE username=%(username)s"
        data = {
            "username": username
        }
        result = connectToMySQL( "todos_db" ).query_db( query, data )
        print( result )
        return( result )
    
    @classmethod
    def get_user_to_validate( cls, username ):
        query = "SELECT * FROM users WHERE username=%(username)s;"
        data = {
            "username" : username
        }
        result = connectToMySQL( "todos_db" ).query_db( query, data )

        return result
    
    @classmethod
    def get_all_users_with_todos( cls ):
        query = "SELECT * FROM users JOIN todos ON users.username = todos.username;"
        results = connectToMySQL( "todos_db" ).query_db( query )
        users = []
        for row in results:
            index = findUserInArray( users, row['username'] )
            if index == -1:
                newUser = User( row['username'], row['password'] )
                newUser.todos.append( Todo( row['todo_id'], row['todo'], row['completed'], row['username'] ))
                users.append( newUser )
            else:
                users[index].todos.append( Todo( row['todo_id'], row['todo'], row['completed'], row['username'] ))
        return users

    @staticmethod
    def validate_user_password( username, password ):
        isValid = True
        if len( username ) < 5:
            flash( "Username must be at least 5 characters long" )
            isValid = False 
        if len( password ) < 5:
            flash( "Password must be at least 5 characters long")
            isValid = False
        return isValid

def findUserInArray( users, username ):
    for i in range(0, len(users), 1 ):
        if users[i].username == username:
            return i
    return -1


