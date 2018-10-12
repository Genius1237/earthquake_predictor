# An overly complex Earthquake Predictor

One needs to be prepared to know what will happen if an earthquake striked his home.

We have a solution for this, a website hosted on Azure that will tell you what will exactly happen.

The website has an UI powered by map engine like Bing Maps or OpenStreetMap. The user selects a location on the map and inputs the magnitude of the would be earthquake. 

# The Model
A model, trained on historical data of earthquakes, takes in the location and magnitude and predicts the following facts for an earthquake striking at that location
1. Number of Deaths
2. Number of Missing Persons
3. Number of Injuries
4. Nuber of Houses destroyed and damaged
5. Damage Costs
6. Chance of a Tsunami

# End-User usability
Using the death count outputted by the model, a heatmap is developed and overlayed on top of a map, thus providing an indicator for how dangerous each area is. People can determine how dangerous an area is before deciding to live there, thus providing an ahead of time disaster warning.
