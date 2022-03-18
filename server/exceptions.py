class DatabaseError(Exception):
    ''' Raised for errors regarding the database conneciton '''
    
    def __init__(self):
        self.message = "Unable to connect to the database. Check the server.py file config settings and try again."
        super().__init__(self.message)
    pass

