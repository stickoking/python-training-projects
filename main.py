import random
import pandas

name = ['Alex', 'Bet', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

students_scores = {students: random.randint(1, 100) for students in name}

print(students_scores)

passed_students = {passed: score for(passed, score) in students_scores.items() if score >= 60}

print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

word_char_count = {word: len(word) for word in sentence.split()}

print(word_char_count)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: round((temperature_c * (9/5) + 32), 2) for (day, temperature_c) in weather_c.items()}

print(weather_f)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)

print(student_data_frame)

#Looping through data frame
for(index, row) in student_data_frame.iterrows():
    print(row.student)
