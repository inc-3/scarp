import os
import requests
import re
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor

class Login:
    def __init__(self):
        self.token = ""
        self.cookies = self.load_cookies()
        if self.cookies:
            self.validate_cookies()
        else:
            self.get_new_cookies()

    def load_cookies(self):
        try:
            with open('cookies.txt', 'r') as file:
                cookies = file.read().strip()
            return cookies
        except FileNotFoundError:
            return None

    def save_cookies(self, cookies):
        with open('cookies.txt', 'w') as file:
            file.write(cookies)

    def validate_cookies(self):
        response = requests.get('https://mbasic.facebook.com/profile.php', cookies={'cookie': self.cookies})
        if 'mbasic_logout_button' in response.text:
            self.token = self.cookies
        else:
            self.get_new_cookies()

    def get_new_cookies(self):
        self.cookies = input("Enter your Facebook cookies: ")
        self.save_cookies(self.cookies)
        self.validate_cookies()

class Dump:
    def __init__(self, token):
        self.token = token

    def dump_post_likes(self, post_id):
        url = f"https://mbasic.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier={post_id}"
        self.scrape(url)

    def scrape(self, url):
        session = requests.Session()
        response = session.get(url, cookies={'cookie': self.token})
        soup = parser(response.text, 'html.parser')
        for user in soup.find_all('a', href=True):
            user_id = re.search(r'id=(\d+)', user['href'])
            if user_id:
                print(f"Found UID: {user_id.group(1)}")

    def save_cookies(self, cookies):
        with open('cookies.txt', 'w') as file:
            file.write(cookies)

class Menu:
    def __init__(self, dump):
        self.dump = dump
        self.show_menu()

    def show_menu(self):
        print("Select an option:")
        print("1. Dump Post Likes")
        choice = input("Enter your choice: ")
        self.handle_choice(choice)

    def handle_choice(self, choice):
        if choice == '1':
            post_id = input("Enter post ID: ")
            self.dump.dump_post_likes(post_id)
        else:
            print("Invalid choice. Try again.")
            self.show_menu()

if __name__ == "__main__":
    login = Login()
    dump = Dump(login.token)
    menu = Menu(dump)
