'''
This is a sample flask application demoing how model 
modularization improves the ability to use and deploy 
trained models.
'''

# Importing dependencies
from flask import Flask
import pandas as pd
from sklearn.neighbors import NearestNeighbors

# Reading in file
file = pd.read_csv('games.csv')

# Creating Flask application
app = Flask(__name__)

# Creating the home route
@app.route("/")
def home():
    return "<h1>Hello World!</h1>"

# Creating an api route usin the model
@app.route("/api/<X>")

def api(X):
        
    neigh = NearestNeighbors(n_neighbors=3)
    neigh.fit(file.iloc[:,3:10])
    
    game = file.iloc[int(X)][3:10]
    print()
    print()
    print()
    print()
    print(X)
    print()
    print()
    print()
    print()
    closest_neighbor = neigh.kneighbors(game.to_numpy().reshape(1, -1))
    
    s = file.iloc[closest_neighbor[1][0][1],:3]
    df = pd.DataFrame(s)
    
    
    # Return the prediction to the user
    return df.to_html()
    
# Running the app
if __name__ == '__main__':
    app.run(debug=True)