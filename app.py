from flask import Flask
from waitress import serve                       #    waitress is the serve useing for WSGI(web serve gateway interface )


app = Flask(__name__)



@app.route("/new" , methods =['GET'])
def get():
    return("back to fire ")
        
    
    
    
mode = "dev" 
mode = "pro"
 
    
   
if __name__=="__main__":
     serve(app , host ="127.0.0.1", port=8000 )  
