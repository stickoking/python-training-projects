import pandas
TITLE = "Primary Fur Color"
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray = len(data[data[TITLE] == "Gray"])
red = len(data[data[TITLE] == "Cinnamon"])
black = len(data[data[TITLE] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray, red, black]
}

squirrel_data = pandas.DataFrame(data_dict)
print(squirrel_data)
squirrel_data.to_csv("squirrel_data.csv")
