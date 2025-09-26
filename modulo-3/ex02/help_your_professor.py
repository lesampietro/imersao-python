def average(data: dict[str, int]) -> float:
    """Receives a dictionary with names and grades, returns the average grade of all students"""
    if not data.values():
        return 0
    grades = []
    for value in data.values():
        if value is None:
            return 0
        grades.append(value)
    average_grade = sum(grades) / len(grades)
    if average_grade == 0:
        return 0
    return average_grade


# if __name__ == "__main__":
#     class_3A = {"marine": 0,"jean": 15,"coline": 8,"luc": 9}
#     print(average(class_3A))
#     class_3B = {"quentin": 0,"julie": 0,"marc": 0,"stephanie": 0}
#     print(average(class_3B))
#     class_3C = {}
#     print(average(class_3C))
