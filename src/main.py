from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from enum import Enum
import uvicorn
import random

tag_meta_data = [
    {
        "name": "Ping",
        "description": "This will ping the BE server to check the server connectivity.",
    },
    {
        "name": "Rock, Paper, Scissors",
        "description": "This will play Rock, Paper, Scissors with the BE server.",
    },
]

# Instantiating the application
app = FastAPI(title="FastAPI", version="v1.0.0")

# Adding CORS.
origins = [
    "http://localhost:4200",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route used to check the server connectivity.
@app.get("/", tags=["Ping"], description="Route used to check the server connectivity.")
async def root():
    return {"message": "Hello World"}


# Options available for the game.
class Options(str, Enum):
    rock = "rock"
    paper = "paper"
    scissors = "scissors"


# Route used to play Rock, Paper, Scissors with the computer.
@app.get(
    "/play-rps/users_choice/{users_choice}",
    tags=["Rock, Paper, Scissors"],
    description="Route used to play Rock, Paper, Scissors with the computer.",
)
async def play(users_choice: Options):
    options = ["rock", "paper", "scissors"]
    message = "Computer wins!"
    computers_choice = random.choice(options)
    if users_choice == Options.rock and computers_choice == Options.scissors:
        message = "You win!"
    elif users_choice == Options.scissors and computers_choice == Options.paper:
        message = "You win!"
    elif users_choice == Options.paper and computers_choice == Options.rock:
        message = "You win!"

    return {
        "usersChoice": users_choice,
        "computersChoice": computers_choice,
        "message": message,
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", reload=True)
