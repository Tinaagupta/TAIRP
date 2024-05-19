import random
import time

def main():
    questions = [
        {
            'id': 1,
            'question': 'What is the capital of India?',
            'options': ['A. New Delhi', 'B. Mumbai', 'C. Bhopal', 'D. Chandigarh'],
            'answer': 'A'
        },
        {
            'id': 2,
            'question': 'A leap year has how many days?',
            'options': ['A. 367', 'B. 365 ', 'C. 366', 'D. 364'],
            'answer': 'C'
        },
        {
            'id': 3,
            'question': 'Which planet in the solar system is known as the “Red Planet”?',
            'options': ['A. Venus', 'B. Earth ', 'C. Jupiter', 'D. Mars'],
            'answer': 'D'
            },
        {
            'id': 4,
            'question': 'How many continents are there in the world?',
            'options': ['A. Six', 'B. Seven ', 'C. Five', 'D. Eight'],
            'answer': 'B'
        }
    ]
    
    score = 0
    start_time = time.time()
    
    for question in random.sample(questions, k=len(questions)):
        print(question['question'])
        for option in question['options']:
            print(option)
        
        user_answer = input("Enter your answer (A, B, C, or D): ").upper()
        if user_answer == question['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, the correct answer is {question['answer']}.")
        
        print()
    
    end_time = time.time()
    total_time = round(end_time - start_time, 2)
    
    print(f"Quiz completed! Your score is {score}/{len(questions)} in {total_time} seconds.")

if __name__ == "__main__":
    main()
