import pandas as pd
import numpy as np
import os

input_dict = {'student1': {'lab': [100, 100, 0, 100, 80, 60, 80, 90, 100, 10], 'homework': [100, 20, 0, 75, 80], 'midterm': 60, 'final': 80},
'student2': {'lab': [100, 100, 0, 100, 80, 60, 80, 90, 20, 10], 'homework': [100, 0, 0, 75, 80], 'midterm': 50, 'final': 30},
'student3': {'lab': [0, 0, 0, 100, 80, 60, 80, 90, 20, 10], 'homework': [0, 0, 0, 100, 0], 'midterm': 50, 'final': 20},
'student4': {'lab': [0, 100, 100, 100, 80, 60, 80, 90, 20, 10], 'homework': [0, 0, 100, 75, 80], 'midterm': 50, 'final': 90},
'student5': {'lab': [0, 100, 100, 100, 80, 60, 80, 90, 20, 10], 'homework': [0, 100, 100, 75, 80], 'midterm': 100, 'final': 100},
'student6': {'lab': [0, 100, 100, 100, 80, 60, 80, 90, 20, 10], 'homework': [100, 0, 0, 75, 80], 'midterm': 25, 'final': 40},
'student7': {'lab': [0, 100, 0, 100, 80, 50, 80, 90, 50, 10], 'homework': [100, 100, 50, 75, 80], 'midterm': 75, 'final': 50},
'student8': {'lab': [54, 68, 82, 94, 55, 22, 100, 88, 75, 92], 'homework': [42, 33, 68, 75, 82], 'midterm': 62, 'final': 82}}

class Student_grades:
    
    def __init__(self, input_):
        self.input_ = input_
        self.df = pd.DataFrame(self.input_)
        self.number_of_students = len(self.df.columns)
        
    @staticmethod
    def clearConsole():
        command = 'clear'
        if os.name in ('nt', 'dos'):
            command = 'cls'
        os.system(command)
    
    def split_students(self):
        global student_list
        student_list = []
        for i in self.df.columns:
            student_list.append(pd.DataFrame(self.df[i]))
        return student_list
        
    
    def labs_and_homeworks(self):
        global result_labs, result_homeworks
        result_labs = []
        result_homeworks = []
        for i in range(self.number_of_students):
            student_lab = student_list[i].iloc[0]
            student_homework = student_list[i].iloc[1]
            
            for labs in student_lab:
                labs.sort(reverse=True)
                for p in range(3):
                    labs.pop()
                result1 = sum(labs) / len(labs)
                result_labs.append(result1)
            
            for homeworks in student_homework:
                homeworks.sort(reverse=True)
                homeworks.pop()
                result2 = sum(homeworks) / len(homeworks)
                result_homeworks.append(result2)
    
    def midterms_and_finals(self):
        global midterms_list, finals_list
        midterms_list = []
        finals_list = []
        for i in range(self.number_of_students):
            student_midterms = student_list[i].iloc[2]
            student_finals = student_list[i].iloc[3]
            
            for midterm in student_midterms:
                midterms_list.append(midterm)
            for final in student_finals:
                finals_list.append(final)
    
    def grade_point_students(self):
        global grade_point_of_students
        grade_point_of_students = []
        for i in range(self.number_of_students):
            grade_point = (result_labs[i] * 20 + result_homeworks[i] * 15 + midterms_list[i] * 25 + finals_list[i] * 40) / 100
            grade_point_of_students.append(grade_point)
        
    def calculate_avg_grade_points(self):
        global avg_grade_points
        avg_grade_points = sum(grade_point_of_students) / len(grade_point_of_students)
        
    def listed_avg_grade_points(self):
        global list_of_points
        list_of_points = []
        for i in grade_point_of_students:
            if(i >= avg_grade_points*1.25 and i <= 100):
                grade = 'AA'
                list_of_points.append(grade)
            elif(i >= avg_grade_points*1.1 and i < avg_grade_points*1.25):
                grade = 'BA'
                list_of_points.append(grade)
            elif(i >= avg_grade_points and i < avg_grade_points*1.1):
                grade = 'BB'
                list_of_points.append(grade)
            elif(i >= avg_grade_points*0.75 and i < avg_grade_points):
                grade = 'CB'
                list_of_points.append(grade)
            elif(i >= avg_grade_points*0.5 and i < avg_grade_points*0.75):
                grade = 'CC'
                list_of_points.append(grade)
            elif(i >= 0 and i < avg_grade_points*0.5):
                grade = 'F'
                list_of_points.append(grade)
                
    def show(self):
        for i in range(self.number_of_students):
            print(f"While the class average of this course was {avg_grade_points}, student {self.df.columns[i]} got a '{list_of_points[i]}' letter grade with a weighted grade of {grade_point_of_students[i]}.")
    
    def exe(self):
        self.clearConsole()
        self.split_students()
        self.labs_and_homeworks()
        self.midterms_and_finals()
        self.grade_point_students()
        self.calculate_avg_grade_points()
        self.listed_avg_grade_points()
        self.show()
        
ex = Student_grades(input_dict)
ex.exe()