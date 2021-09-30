from todos_app.config.MySQLConnection import connectToMySQL

class Todo:
    def __init__( self, todo_id, todo, completed, username ):
        self.todo_id = todo_id
        self.todo = todo
        self.completed = completed
        self.username = username
    
    @classmethod
    def get_todos_from_user( cls, username ):
        query = "SELECT * FROM todos WHERE username=%(username)s"
        data = {
            "username" : username
        }
        results = connectToMySQL( "todos_db" ).query_db( query, data )
        todos = []
        for todo in results:
            todos.append( Todo( todo['todo_id'], todo['todo'], todo['completed'], todo['username'] ) )
        
        return todos