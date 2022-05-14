import datetime
class User():
     def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.registered_on = datetime.datetime.now()
        
class Quotes():
    '''
    Defining Quote objects
    '''
    def __init__(self, quote, author, permalink):
        self.quote = quote
        self.author  = author
        self.permalink = permalink
        