#Number Guessing Game:
from art import logo
from random import randint

# Allow the player to submit a guess for a number between 1 and 100.
# If they run out of turns, provide feedback to the player. 

def random_number():
  return randint(1,100)

def check_answer(guess, number_to_guess, attempts):
  if guess > number_to_guess:
    print("Too high")
    return attempts - 1
  elif guess < number_to_guess:
    print("Too low")
    return attempts - 1
  else:
    print(f"You got it! The answer was {number_to_guess}")
    attempts = 0
    return attempts




def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  number_to_guess = random_number()
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if difficulty == "easy":
    attempts = 10
  else:
    attempts = 5
  print(number_to_guess)
  while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    attempts = check_answer(guess, number_to_guess, attempts)
    if attempts == 0 and guess != number_to_guess:
      print("You run out of guesses. You lose!.")
      return
    elif guess != number_to_guess:
      print("Guess again.")

game()