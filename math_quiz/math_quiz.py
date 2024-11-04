import random

def get_random_integer(min_value, max_value):
    """
    Generate a random integer within a specified range.
    
    Parameters:
        min_value (int): The minimum value of the range.
        max_value (int): The maximum value of the range.
    
    Returns:
        int: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)

def get_random_operator():
    """
    Choose a random operator for the math problem.
    
    Returns:
        str: A random operator, either '+', '-', or '*'.
    """
    return random.choice(['+', '-', '*'])

def generate_problem_and_solution(num1, num2, operator):
    """
    Create a math problem and calculate its correct answer based on the given operator.
    
    Parameters:
        num1 (int): The first number in the problem.
        num2 (int): The second number in the problem.
        operator (str): The operator, which is either '+', '-', or '*'.
    
    Returns:
        tuple: A tuple containing the problem as a string and the correct answer as an integer.
    """
    problem = f"{num1} {operator} {num2}"
    
    # Calculate the answer based on the operator
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    
    return problem, answer

def math_quiz():
    """
    Start the math quiz game, present math problems, and track the user's score.
    """
    score = 0
    total_questions = 3  # Set a fixed number of questions for the game

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Generate random numbers and operator for the problem
        num1 = get_random_integer(1, 10)
        num2 = get_random_integer(1, 10)
        operator = get_random_operator()

        # Generate the math problem and its solution
        problem, correct_answer = generate_problem_and_solution(num1, num2, operator)

        # Display the problem to the user
        print(f"\nQuestion: {problem}")
        
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            raise ValueError(f"expected type int, got type {type(user_answer).__name__}instead.")
            continue

        # Check the user's answer
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
