from todos_app.config.MySQLConnection import connectToMySQL

class User:
    def __init__( self, username, password ):
        self.username = username
        self.password = password
    
    def printInfo( self ):
        print(f"username: {self.username} password: {self.password} ")

    @classmethod
    def get_all_users( cls ):
        query = "SELECT * FROM users;"
        results = connectToMySQL( "todos_db" ).query_db( query )

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
        return( result )