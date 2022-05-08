import csv
import pandas
# STRIP_TEXT= "\n"
# # data = []
# temperature = []
# with open("weather_data.csv", mode="r") as weather_data:
#     data = csv.reader(weather_data)
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
# print(temperature)


# for i in temp_data:
#     data.append(i.strip(STRIP_TEXT))    
#Reading csv data
data = pandas.read_csv("weather_data.csv")

#converting data to python data types
data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

average_temp = data["temp"].mean()
print(average_temp)

max_temp = data["temp"].max()
print(max_temp)

#Reading from rows
print(data[data.day == "Monday"])
print(data[data.temp == max_temp])

monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
fahrenheit = monday_temp*(9/5) + 32
print(fahrenheit)

#Create a datafrane from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

student_data = pandas.DataFrame(data_dict)
print(student_data)
student_data.to_csv("student_data.csv")