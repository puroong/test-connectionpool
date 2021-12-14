import logging
import requests

logging.basicConfig(level=logging.DEBUG)
logging.getLogger("requests.packages.urllib3.connectionpool").setLevel(logging.DEBUG)

if __name__ == "__main__":
    session = requests.Session()
    r = session.get('https://www.google.com')
    print(session.headers)
    print(r.headers)
    print('Done')