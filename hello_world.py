import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 7 attempts to guess the correct number.")
    
    # 컴퓨터가 랜덤 숫자를 생성
    secret_number = random.randint(1, 100)
    attempts = 7

    while attempts > 0:
        try:
            # 사용자 입력 받기
            guess = int(input(f"You have {attempts} attempts remaining. Make a guess: "))

            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue

            # 추측한 숫자와 정답 비교
            if guess == secret_number:
                print(f"Congratulations! You guessed the number {secret_number} correctly!")
                break
            elif guess < secret_number:
                print("Too low. Try again!")
            else:
                print("Too high. Try again!")
            
            # 시도 횟수 줄이기
            attempts -= 1
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    # 게임 종료 메시지
    if attempts == 0:
        print(f"Game over! The correct number was {secret_number}. Better luck next time!")

# 게임 실행
if __name__ == "__main__":
    number_guessing_game()