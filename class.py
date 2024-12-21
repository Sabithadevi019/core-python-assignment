def calculate_averages(students):
    averages = {}
    for name, marks in students.items():
        averages[name] = sum(marks) / len(marks)
    return averages
def find_top_performer(averages):
    return max(averages, key=averages.get)
students = {
    "John": [85, 78, 92],
    "Alice": [88, 79, 95],
    "Bob": [70, 75, 80]
}
averages = calculate_averages(students)
print("Average Marks:", averages)
top_performer = find_top_performer(averages)
print("Top Performer:", top_performer)
