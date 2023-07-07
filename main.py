# # Option 1
#
# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)
#
#
# # Option 2
#
# import csv
#
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1].isdigit():
#             temperatures.append(int(row[1]))
#     print(temperatures)
#
#
# # Option 3
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data["Temperature"])
# data_dict = data.to_dict()
# print(data_dict)
#
#
# # Average temperature
# # Option 1
# temperature = data["Temperature"].to_list()
# print(sum(temperature)/len(temperature))
#
# # Option 2
# print(data["Temperature"].mean())
#
# # Get dat in columns
# # Maximum Temperature
# # Option 1
# print(data["Temperature"].max())
#
# # Option 2
# print(data.Temperature.max())
#
# # Get data in rows
# print(data[data.Day == "Monday"])
# print(data[data.Temperature == data.Temperature.max()])
#
# # Specific column in specific row
# monday = data[data.Day == "Monday"]
# print(monday.Condition)
# print(monday.Temperature)
# # Convert Temperature from Celsius to Fahrenheit
# print(monday.Temperature * 9 / 5 + 32)
#
#
# # Create a dataframe from scratch
# data_dictionary = {
#     "students": ["Amy", "James", "Angela", "Paul", "Sean", "Julie"],
#     "scores": [23, 63, 45, 93, 53, 87]
# }
#
# student_data = pandas.DataFrame(data_dictionary)
# student_data.to_csv("student_data.csv")

import pandas
# Read data from Central Park Squirrel Census
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

squirrel_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

squirrels_count = pandas.DataFrame(squirrel_dict)
squirrels_count.to_csv("squirrel_count.csv")


