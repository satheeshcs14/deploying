from flask import Flask



app = Flask(__name__)



@app.route("/new" , methods =['GET'])
def get():
    return("back to fire ")
        
    
    
    
    
if __name__ =="__main__":
    app.run(host="127.0.2.1",   port=8000)
