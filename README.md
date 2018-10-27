# An overly complex Earthquake Badness Predictor

One needs to be prepared to know how bad of an earthquake would strike his home.

We have a solution for this, a website hosted on Azure that will tell you what will exactly happen.

The website has an UI powered by map engine like Bing Maps or OpenStreetMap. The user selects a location on the map and the website shows a badness score(with respect to earthquakes) for for that place

The website is at https://104.211.89.243/ (Temporarily allow the SSL certificate)

![The Website](https://github.com/Genius1237/earthquake_predictor/raw/master/Screenshot%20from%202018-10-27%2020-27-17.png)

# The Model
The model is trained on data of earthquakes from 1955 onwards obtained from https://www.kaggle.com/usgs/earthquake-database.
Using a machine learning model and the inverse square law, we assign a score to every location on the map. The model makes use of the magnitude data from the earthquakes from the past.

# End-User usability
Using the badness factor outputted by the model, a heatmap is developed and overlayed on top of a map, thus providing an indicator for how dangerous each area is. People can determine how dangerous an area is before deciding to live there, thus providing an ahead of time disaster warning.
