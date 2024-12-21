def calculate_positive_feedback(ratings):
    positive_feedback_count = sum(1 for rating in ratings if rating >= 4)
    if len(ratings) == 0:
        return 0
    else:
        positive= (positive_feedback_count / len(ratings)) * 100
        return positive
ratings = [5, 4, 3, 5, 2, 4, 1, 5]
positive= calculate_positive_feedback(ratings)
print(f"Positive Feedback: {positive}%")
