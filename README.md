# board-game-project

URL to dataset: [board games](https://www.kaggle.com/datasets/threnjen/board-games-database-from-boardgamegeek?select=themes.csv)

Proposal: [Google Doc](https://docs.google.com/document/d/1HYuqws4Yuvrw-bJypp_IPAaHstGVPFo72bovL7_qUS0/edit)

## Summary

For the final project, we decided to look at board game data and determine what would make a successful board game with machine learning. At the start, we asked ourselves "what makes a board game successful?". A couple of ideas popped out first: 1) we can look at the average rating of a game to see how the general population feels about a game, and 2) we can determine the success of a game for a group of people, since some people prefer certain types of games over others. We decided to do some exploratory data analysis first and decide on the best model afterwards.

After doing some EDA, we decided to pursue both, as both provided intriguing results from our inital models. We first did a Nearest Neighbors model to determine what games are similar to an inputted game in order to give a recommendation. We found that this model worked fairly well, but with only 20,000 rows, we could not give incredibly accurate/similar results for every type of game. From here, we decided to move onto a Logistic Regression model to determine the success of a game based on the average rating. With the Logistic Regression model, we defined a 'good' game as one with an average rating of at least 6.5. Those with a lesser average rating were defined as 'bad'. We decided on 6.5 because it was close to the mean and median average rating across the entire data set (6.42 and 6.45, respectively). We were able to accurately predict whether a game would be 'good' or 'bad' around 83% of the time with this model. Finally, we created a Neural Network to predict the classification of a 'good' or 'bad' game. With some tweaks, we were able to increase the accuracy of this model to 93.05%.
