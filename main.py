from fastapi import FastAPI
from scraper import get_betano_odds
from surebet import find_surebets

app = FastAPI()

@app.get("/surebets")
def get_surebets():
    games = get_betano_odds()
    return find_surebets(games)