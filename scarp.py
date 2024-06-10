import os
import requests
import re
from bs4 import BeautifulSoup as parser

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
        return self.scrape(url)

    def dump_video_reactions(self, video_id):
        url = f"https://m.facebook.com/browse/reactions/?id={video_id}"
        return self.scrape(url)

    def scrape(self, url):
        session = requests.Session()
        response = session.get(url, cookies={'cookie': self.token})
        soup = parser(response.text, 'html.parser')
        users = []
        for user in soup.find_all('a', href=True):
            uid_match = re.search(r'id=(\d+)', user['href'])
            if uid_match:
                uid = uid_match.group(1)
                name = user.get_text()
                users.append((uid, name))
            if len(users) >= 100:
                break
        return users

    def save_cookies(self, cookies):
        with open('cookies.txt', 'w') as file:
            file.write(cookies)

class Menu:
    def __init__(self, dump):
        self.dump = dump
        self.run_menu()

    def run_menu(self):
        while True:
            self.clear_screen()
            print("Select an option:")
            print("1. Dump Post Likes")
            print("2. Dump Video Reactions")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                post_id = input("Enter post ID: ")
                users = self.dump.dump_post_likes(post_id)
                print("Found Users:")
                for uid, name in users:
                    print(f"UID: {uid}, Name: {name}")
                input("Press Enter to continue...")
            elif choice == '2':
                video_id = input("Enter video ID: ")
                users = self.dump.dump_video_reactions(video_id)
                print("Found Users:")
                for uid, name in users:
                    print(f"UID: {uid}, Name: {name}")
                input("Press Enter to continue...")
            elif choice == '3':
                break
            else:
                print("Invalid choice. Try again.")

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    login = Login()
    dump = Dump(login.token)
    menu = Menu(dump)
