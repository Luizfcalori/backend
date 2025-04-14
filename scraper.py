from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def get_betano_odds():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    url = "https://br.betano.com/sport/futebol/brasil/serie-a/17908/"
    driver.get(url)
    time.sleep(5)

    matches = []
    try:
        events = driver.find_elements(By.CLASS_NAME, "event")
        for event in events:
            teams = event.find_elements(By.CLASS_NAME, "participant__name")
            odds = event.find_elements(By.CLASS_NAME, "odd__value")
            if len(teams) == 2 and len(odds) >= 2:
                team1, team2 = teams[0].text, teams[1].text
                odd1, odd2 = float(odds[0].text.replace(',', '.')), float(odds[1].text.replace(',', '.'))
                matches.append({
                    "team1": team1,
                    "team2": team2,
                    "odd1": odd1,
                    "odd2": odd2
                })
    except Exception as e:
        print("Erro:", e)
    driver.quit()
    return matches