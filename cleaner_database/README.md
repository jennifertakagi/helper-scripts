# Database Cleaner

> This script was made to clean a CSV dataset and generate a JSON file with all the data I needed to storage on my database

---

# :pushpin: Table of Contents

* [Features](#rocket-features)
* [Getting Started](#runner-getting-started)


# :rocket: Features

* The dataset was taken from Kaggle: https://www.kaggle.com/ai-first/cocktail-ingredients
* The script will get the specific fields: `name, category, image, ingredients, measurements_ingredients, instructions, glass_type, drink_type`
* The fields ingredients and measurements_ingredients are strings, they'll be transform into list split by ','
* It will be generated a JSON file named `cleared_drinks.JSON`

# :runner: Getting Started

Run the following command in **api and client** folder start the application in a development environment:

```python3 clear_database.py```
