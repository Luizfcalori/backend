from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def get_surebets():
    return [
        {
            "team1": "Palmeiras",
            "odd1": 2.1,
            "team2": "Time B",
            "odd2": 2.2,
            "profit": 5.4
        },
        {
            "team1": "Time C",
            "odd1": 1.95,
            "team2": "Time D",
            "odd2": 2.05,
            "profit": 2.3
        }
    ]

