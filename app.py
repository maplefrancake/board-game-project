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




# # Sea Gun's app

# # Importing the required libraries
# import numpy as np
# from sklearn.neighbors import NearestNeighbors

# # Function to calculate the nearest neighbor logic
# def nearest_neighbor(data):
#     # Create a NearestNeighbors object and fit the data
#     nbrs = NearestNeighbors(n_neighbors=2).fit(data)

#     # Calculate the distances and indices of the nearest neighbors
#     distances, indices = nbrs.kneighbors(data)

#     # For demonstration purposes, let's assume we want to find the second nearest neighbor
#     nearest_index = indices[:, 1]
#     nearest_neighbor = data[nearest_index]

#     return nearest_neighbor

# # Main function
# def main():
#     # Example data (replace with your actual dataset)
#     data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

#     # Generate table using nearest neighbor logic
#     table = []
#     for row in data:
#         nearest_neighbor_row = nearest_neighbor(data)
#         table.append(list(row) + list(nearest_neighbor_row))

#     # Print the generated table
#     for row in table:
#         print(row)

# # Entry point of the application
# if __name__ == "__main__":
#     main()
















