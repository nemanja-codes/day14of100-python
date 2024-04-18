from art import logo
from art import vs
from replit import clear
from game_data import data
from random import randint

def get_random_account():
  """Get data from random account"""
  return randint(0, len(data) - 1)

def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  print(f"{name}, a {description}, from {country}")

def check_answer(guess, a_followers, b_followers):
  """Check answer and return True if correct, False if wrong"""
  return (guess == "a" and a_followers > b_followers) or (guess == "b" and b_followers > a_followers)

def game():
  print(logo)
  score = 0
  account_a = data[get_random_account()]
  account_b = data[get_random_account()]
  game_should_continue = True
  while game_should_continue:
    if account_a == account_b:
       account_b = data[get_random_account()]
      
    num_of_followers_a = account_a["follower_count"]
    num_of_followers_b = account_b["follower_count"]
    print("Compare A: ", end="")
    format_data(account_a)
    print(vs)
    print("Against B: ", end="")
    format_data(account_b)
    guess = input("Who has more followers? Type 'A' or 'B':  ").lower()

    if check_answer(guess, num_of_followers_a, num_of_followers_b):
      score += 1
      account_a = account_b
      account_b = data[get_random_account()]
      clear()
      print(logo)
      print(f"You are right! Current score: {score}")
    else:
      game_should_continue = False
      clear()
      print(logo)
      print(f"Sorry, that's wrong. Final score: {score}")


game()
