import random
from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
      return render(request, "HANGMAN/home.html")  # render a home page with a button

# WORDS = ["apple", "banana", "mango", "strawberry", "orange", "grape", "peach", "cherry", "litchi", "guava", "pineapple", "kiwi", "avocado" ]

WORDS = [
    {"word": "apple", "clue": "Keeps the doctor away"},
    {"word": "banana", "clue": "A yellow fruit loved by monkeys"},
    {"word": "mango", "clue": "Known as the king of fruits"},
    {"word": "strawberry", "clue": "A red fruit with seeds on the outside"},
    {"word": "orange", "clue": "A citrus fruit rich in Vitamin C"},
    {"word": "grape", "clue": "Tiny fruit often used to make wine"},
    {"word": "peach", "clue": "A fruit with fuzzy skin"},
    {"word": "cherry", "clue": "Small red fruit often on top of cakes"},
    {"word": "litchi", "clue": "Sweet tropical fruit with rough skin"},
    {"word": "guava", "clue": "Fruit high in Vitamin C, with edible seeds"},
    {"word": "pineapple", "clue": "Spiky fruit, grows in tropical regions"},
    {"word": "kiwi", "clue": "Brown outside, green inside with black seeds"},
    {"word": "avocado", "clue": "Green creamy fruit, used in guacamole"}
]

def start_game(request):
    chosen = random.choice(WORDS)   # pick random word + clue
    word = chosen["word"].lower()
    clue = chosen["clue"]

    request.session["word"] = word  # save word
    request.session["clue"] = clue  # save clue
    request.session["guessed"] = []  
    request.session["attempts"] = len(word) + 3
    return redirect("play_game")
def quit_game(request):
    wins = request.session.get("wins", 0)  # total wins so far

    # Clear only the game state, keep win count
    request.session.pop("word", None)
    request.session.pop("clue", None)
    request.session.pop("guessed", None)
    request.session.pop("attempts", None)

    return render(request, "HANGMAN/quit.html", {"wins": wins})

def reset_wins(request):
    request.session['wins'] = 0
    return redirect('play_game')

def play_game(request):
    word = request.session.get("word")             # the secret word
    if not word:
        # user has not started a game (or game was cleared) — redirect to start
        return redirect("start_game")   # or redirect('home') 

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
        request.session["wins"] = request.session.get("wins", 0) + 1
    elif attempts <= 0:
        message = f"Game Over! The word was '{word}'."
        
    context = {
    "display_word": display_word,
    "attempts": attempts,
    "guessed": guessed,
    "message": message,
    "clue": request.session.get("clue", "No clue available")  # add clue here
}
    return render(request, "hangman/game.html", context)
