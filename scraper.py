import asyncio
from pyppeteer import launch

async def scrape_betano():
    browser = await launch(headless=True, args=['--no-sandbox'])
    page = await browser.newPage()
    await page.goto('https://www.betano.com.br/sport/futebol/brasil/serie-a/')

    await page.waitForSelector('div.eventRow')  # espera carregar os eventos
    events = await page.querySelectorAll('div.eventRow')

    odds = []

    for event in events[:5]:  # limita só pros 5 primeiros
        teams = await event.JJeval('div.competitor', '(els) => els.map(e => e.innerText)')
        event_odds = await event.JJeval('div.odds', '(els) => els.map(e => e.innerText)')
        odds.append({
            'teams': teams,
            'odds': event_odds
        })

    await browser.close()
    return odds

if __name__ == "__main__":
    results = asyncio.get_event_loop().run_until_complete(scrape_betano())
    for r in results:
        print(r)

