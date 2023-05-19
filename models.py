import requests
from bs4 import BeautifulSoup


class Part(object):

    def __init__(self, part_id, color, qty):

        # initialize unique variables
        self.price = 0
        self.total_cost = 0
        self.url = ''

        # set rest of them
        self.part_id = part_id
        self.color = color
        self.qty = int(qty)


    def get_part_price(self, part_id, color):
        colors = {
            "white": 1,
            "tan": 2,
            "yellow": 3,
            "orange": 4,
            "red": 5,
            "green": 6,
            "blue": 7,
            "brown": 8,
            "light gray": 9,
            "dark gray": 10,
            "black": 11,
            "clear": 12,
            "clear brown": 13,
            "clear dark blue":14,
            "clear blue":15,
            "clear neon green":16,
            "clear red":17,
            "clear neon orange": 18,
            "clear yellow": 19,
            "clear green": 20,
            "pink": 23,
            "purple": 24
        }
        if color in colors.keys():
            url = f'https://www.bricklink.com/catalogPG.asp?P={part_id}&colorID={colors[color]}'
            self.url = url
            print(f"Sourcing part from url: {url}")

            headers = {
                'User-Agent': f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3029.110 Safari/537.3'
                # 'X-Forwarded-For': '1.1.1.1'
            }
            response = requests.get(url, headers=headers)
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')
            td_element = soup.find('td', text='Avg Price:')

            try:
                price_element = td_element.find_next('b')
                average_price = price_element.text.split('$')[1]
                self.price = average_price
                self.total_cost = int(self.qty)*float(self.price)
            except AttributeError:
                print(f'\nThe piece of {self.part_id} not found or you are rate limited.')
        else:
            print(f'\nThe color "{color}" of {self.part_id} not found or you are rate limited.')

        print(f"Price of ${self.price} retrieved for {self.color} {self.part_id}. {self.qty} costs ${int(self.qty)*float(self.price)}")

class Build(object):

    def __init__(self,name,parts,build_cost):
        self.total_parts = 0

        self.name = name
        self.parts = parts
        self.build_cost = build_cost

    def count_total_pieces(self):
        total_parts = 0
        for part in self.parts:
            total_parts+=part.qty
        self.total_parts = total_parts
