# Semester Project for CS39AA
## Author: Brady
## Semester: Fall 2023

I always enjoy working with data as far removed from useful real-world applications as possible. So I find myself asking the question, can we use pokedex entries to predict the typing of a pokemon? I'll be using [this dataset](https://www.kaggle.com/datasets/cristobalmitchell/pokedex/data) created by Cristobal Mitchell that contains a large variety of information on pokemon up to Pokemon Sword and Shield. 

I find this idea very interesting as pokedex entries aren't long but tend to contain pretty important key words that I believe will be good indicators of typing. Pokemon also tend to have multiple types (up to two), so this becomes a more interesting problem as we're now predicting the values of two separate columns and we can't have duplicates! 

Some will be easy, like Bulbasaur mentioning that it has a plant like bulb on its back, but I doubt all will be that straightforward. 

My plan will revolve around starting with distilbert-uncased and seeing how well it performs with some basic fine tuning. If I have the time I'd like to compare its performance to other models as well! 