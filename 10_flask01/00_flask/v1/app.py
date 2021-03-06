# Clyde 'Thluffy' Sinclair
# SoftDev -- Rona Ed.
# Oct 2020

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()

"""
Notes and Predicted Behavior:
- Very similar to app.py in 09
- Nothing printed into the terminal
- "No hablo queso!" will appear on the resulting homepage.
"""
