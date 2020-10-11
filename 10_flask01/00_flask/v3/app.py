# Clyde 'Thluffy' Sinclair
# SoftDev -- Rona Ed.
# Oct 2020

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.debug = True
app.run()

"""
Notes and Predicted Behavior:
- Since v2, a debug statement has been added.
- The program will still print "about to print __name__..." before printing "__main__" to the terminal.
- "No hablo queso!" will still be on the homepage.
- "app.debug = True" will put flask app into debug mode
"""
