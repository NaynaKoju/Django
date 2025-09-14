import random
from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
      return render(request, "HANGMAN/home.html")  # render a home page with a button

WORDS = ["apple", "banana", "mango", "strawberry", "orange", "grape", "peach", "cherry", "litchi", "guava", "pineapple", "kiwi", "avocado" ]

def start_game(request):
    # initialize game state
    word = random.choice(WORDS).lower() #picks a random word
    request.session["word"] = word #save word in session
    request.session["guessed"] = []  # empty list to store guessed letters
    request.session["attempts"] = len(word) + 3 #number of extra attempts to player
    return redirect("play_game")

def play_game(request):
    word = request.session.get("word")             # the secret word
    guessed = request.session.get("guessed", [])    # guessed letters
    attempts = request.session.get("attempts", 0)   # remaining tries
    message = ""

#handling guesses: if user submits a post request it reads the guessed letter
    if request.method == "POST":
        guess = request.POST.get("guess", "").lower()

        if guess and guess.isalpha() and len(guess) == 1:
            if guess in guessed:
                message = f"You already guessed '{guess}'."
            elif guess in word:
                guessed.append(guess)
                message = f"Good guess! '{guess}' is in the word."
            else:
                guessed.append(guess)
                attempts -= 1
                message = f"Oops! '{guess}' is not in the word."
#updating the session again
        request.session["guessed"] = guessed
        request.session["attempts"] = attempts

    # Build word display
    display_word = " ".join([c if c in guessed else "_" for c in word])

    # Check game over
    if "_" not in display_word:
        message = "Congratulations! You guessed the word!"
    elif attempts <= 0:
        message = f"Game Over! The word was '{word}'."

    context = {
        "display_word": display_word,
        "attempts": attempts,
        "guessed": guessed,
        "message": message,
    }
    return render(request, "hangman/game.html", context)
