# Clyde 'Thluffy' Sinclair
# SoftDev -- Rona Ed.
# Oct 2020

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()

"""
Notes and Predicted Behavior:
- Since v3, "if __name__ == "__main__":" has been added.
- The program will still print "about to print __name__..." before printing "__main__" to the terminal.
- "No hablo queso!" will still be on the homepage.
- "app.debug = True" will put flask app into debug mode
- Allows simultaneous running and importing without unexpected side effects.
"""
