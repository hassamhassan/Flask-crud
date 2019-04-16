**Requirements:**

    Python 3.7
    XAMPP
    All the packages written in requirements.txt
    
**SETUP:**

    -> Install Python from https://www.python.org/downloads/
    
    -> Install requirements.txt using following command:
           pip install -r requirements.txt
    
    -> Install XAMPP from https://www.apachefriends.org/index.html
    
    -> Open XAMPP Control Panel and start Apache and MySQL services
    
    -> Now go to following url Create a new Database named 'my_db':
           http://localhost/phpmyadmin/
        
    -> Now open Command Prompt and navigate to projects root directory
    
    -> Execute following Commands: (make sure to change username & password
                                    in database URI in config.py)
           python manage.py db init
           python manage.py db migrate
           python manage.py db upgrade
        
    -> Now open up PyCharm and run routes.py file
    

**Usage:**
  
    -> Now it is time to explore the add user api call:
    
    Add Users(POST):
        127.0.0.1:5000/api/users 
        Example POST data: 
            username:hassam
            password:123456
            
    BOOK CRUD API END POINTS: (Authentication header {username, passowrd})
        -> 127.0.0.1:5000/api/book
            METHOD1: GET(Returns all books)
            METHOD2: POST(Create a new book)
            
            Example data:
                {"title": "The age of stones"}
           
        -> 127.0.0.1:5000/api/book/2    
            METHOD1: GET(Get a book)
            METHOD2: PUT(Update a new book)
            METHOD3: DELETE(Delete a new book)
        
                 
            
    
                      
    
    
    
    
    
    
    