import requests
from bs4 import BeautifulSoup
def list_meme():
    url = 'http://apimeme.com'
    response = requests.get(url=url)
    # Превращаем HTML-код в объект BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    options = soup.find_all('option')
    mems = [option.get('value') for option in options]
    return mems

def generate_meme(top_text, bottom_text, meme):

    url = f'http://apimeme.com/meme?meme={meme}&top={top_text}&bottom={bottom_text}'

    response = requests.get(url=url)

    if response.status_code == 200:
        with open('meme.png', 'wb') as img_file:
            img_file.write(response.content)
    else:
        print(f"Request failed with status code {response.status_code}")


def main():
    print (list_meme())

if __name__ == '__main__':
    main()
