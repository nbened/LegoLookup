import requests
from bs4 import BeautifulSoup

def get_part_price(part_id,color):
    colors = {
        "white":1,
        "tan":2,
        "yellow":3,
        "orange":4,
        "red":5,
        "green":6,
        "blue":7,
        "brown":8,
        "light gray":9,
        "dark gray":10,
        "black":11
    }

    url = f'https://www.bricklink.com/catalogPG.asp?P={part_id}&colorID={colors[color]}'
    print(f"Sourcing part from url: {url}")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    td_element = soup.find('td', text='Avg Price:')
    price_element = td_element.find_next('b')
    average_price = price_element.text.split('$')[1]
    return {'part_id': part_id, 'average_price': float(average_price)}

