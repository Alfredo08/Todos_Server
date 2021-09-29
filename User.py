from MySQLConnection import connectToMySQL

class User:
    def __init__( self, username, password ):
        self.username = username
        self.password = password
    
    @classmethod
    def get_all_users( cls ):
        query = "SELECT * FROM users;"
        results = connectToMySQL( "todos_db" ).query_db( query )
        return results
