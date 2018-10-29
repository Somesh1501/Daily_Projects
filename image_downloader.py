from bs4 import BeautifulSoup
import requests
import argparse

parser = argparse.ArgumentParser()
url = input('Enter Url\n')
hdr = {
  "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"
}
content = requests.get(url, headers=hdr)
soup = BeautifulSoup(content.text, 'html.parser')
count = 0
for link in soup.find_all('img'):
    if link.get('src'):
        file_name = str(link.get('src')).split('/')[-1]
        if file_name.endswith('.jpg'):
            image_link = (link.get('src')).replace('350', '1920')
            response = requests.get(image_link, headers=hdr)
            size = response.headers.get('Content-length')
            with open('/home/ironman/Pictures/new_Wallpapers/{}'.format(file_name), 'wb') as f:
                f.write(response.content)
            print(count, 'Downloading', file_name, 'Of Size:', size, sep='\t')
            count += 1
    else:
        file_name = link.get('data-lazy-src').split('/')[-1]
        if file_name.endswith('.jpg'):
            image_link = link.get('data-lazy-src')
            response = requests.get(image_link, headers=hdr)
            size = response.headers.get('Content-length')
            with open('/home/ironman/Pictures/new_Wallpapers/{}'.format(file_name), 'wb') as f:
                f.write(response.content)
                print(count, 'Downloading', file_name, 'Of Size:', size, sep='\t')

            count += 1
