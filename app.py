# Importing dependencies
from flask import Flask, render_template, request
import pandas as pd
from sklearn.neighbors import NearestNeighbors

# Reading in file
file = pd.read_csv('./Resources/games_scaled.csv')
file1 = pd.read_csv('./Resources/games.csv')

# Creating Flask application
app = Flask(__name__)

# Creating the home route
@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        search_query = request.form.get("search_query")
        neigh = NearestNeighbors(n_neighbors=6)
        neigh.fit(file.iloc[:, 3:39])

        # Perform a search based on the given query
        search_results = file[file["Name"].str.contains(search_query, case=False)]

        # If no search results are found, return an appropriate message
        if search_results.empty:
            return "No matching results found."

        game = search_results.iloc[0, 3:39]

        closest_neighbor = neigh.kneighbors(game.to_numpy().reshape(1, -1))

        columns_to_return = [0, 1, 2, 3, 4, 5, 40, 41, 42, 43, 44, 45, 46, 47]
        
        i = closest_neighbor[1][0]

        selected_columns = file1.iloc[i, columns_to_return]

        # Render the HTML template and pass the selected columns as a parameter
        return render_template("index.html", result=selected_columns.to_html())
    else:
        # Render the HTML template and pass the selected columns as a parameter
        return render_template("index.html", result="")

# Running the app
if __name__ == '__main__':
    app.run(debug=True)