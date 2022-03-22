# mini_sap_system
A mini sap system software that calculates the weighted grade, letter grade and the general average of the class of the students who are given laboratory, homework, midterm and final exams in the dictionary.


!!!DATA!!!

In this case, the format of our data must be as below;

input_dict = {'student1': {'lab': [100, 100, 0, 100, 80, 60, 80, 90, 100, 10], 'homework': [100, 20, 0, 75, 80], 'midterm': 60, 'final': 80},
'student2': {'lab': [100, 100, 0, 100, 80, 60, 80, 90, 20, 10], 'homework': [100, 0, 0, 75, 80], 'midterm': 50, 'final': 30},
'student3': {'lab': [0, 0, 0, 100, 80, 60, 80, 90, 20, 10], 'homework': [0, 0, 0, 100, 0], 'midterm': 50, 'final': 20},
'student4': {'lab': [0, 100, 100, 100, 80, 60, 80, 90, 20, 10], 'homework': [0, 0, 100, 75, 80], 'midterm': 50, 'final': 90},
'student5': {'lab': [0, 100, 100, 100, 80, 60, 80, 90, 20, 10], 'homework': [0, 100, 100, 75, 80], 'midterm': 100, 'final': 100},
'student6': {'lab': [0, 100, 100, 100, 80, 60, 80, 90, 20, 10], 'homework': [100, 0, 0, 75, 80], 'midterm': 25, 'final': 40},
'student7': {'lab': [0, 100, 0, 100, 80, 50, 80, 90, 50, 10], 'homework': [100, 100, 50, 75, 80], 'midterm': 75, 'final': 50},
'student8': {'lab': [54, 68, 82, 94, 55, 22, 100, 88, 75, 92], 'homework': [42, 33, 68, 75, 82], 'midterm': 62, 'final': 82}}

Otherwise, you might get an error.
