from flask import Flask



app = Flask(__name__)



@app.route("/new" , methods =['GET'])
def get():
    return("back to fire ")
        
    
    
    
mode = "dev" 
mode = "pro"
 
    
   
if __name__=="__main__":
    from waitress import serve                #    waitress is the serve useing for WSGI(web serve gateway interface )
    
    if mode =="dev":                          #         dev           or                  "pro"

        app.run(host="127.0.0.1",port=8000 ,debug=True)

    else:

        serve(app , host ="127.0.0.1", port=8000 )  
