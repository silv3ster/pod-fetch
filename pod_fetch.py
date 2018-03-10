from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime

PB_HOMEPAGE = "https://www.pinkbike.com"
PHOTO_PREFIX = "https://www.pinkbike.com/photo/"
POD_DIR = "pods/"

def find_pod_url(soup):
    for a in soup.find_all('a', href=True):
        if PHOTO_PREFIX in str(a):
            url = a['href']
            if len(url) == len(PHOTO_PREFIX) + 9:
                return url

def get_pod_img(url):
    pod_num = url[len(PHOTO_PREFIX):-1]
    soup = BeautifulSoup(urlopen(url), 'html.parser')
    img_src = "http://ep1.pinkbike.org/p6pb" + pod_num + "/p0pb" + pod_num + ".jpg"
    pic = urlopen(img_src).read()
    write_to_file(pic)

def write_to_file(bin):
    fname = POD_DIR + "pb_pod_" + datetime.date.today().strftime("%Y%m%d") + ".jpg"
    with open(fname, 'bw') as f:
        f.write(bin)
        print("PoD saved to " + fname)

def main():
    print("Fetching today's PoD...")
    pod_url = find_pod_url(BeautifulSoup(urlopen(PB_HOMEPAGE), 'html.parser'))
    get_pod_img(pod_url)

if __name__ == "__main__":
    main()
    