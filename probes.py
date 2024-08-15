import sys
import requests


def urls(out_files):
    urls2= sys.stdin.read().splitlines()
    good_url = []
    bad_url = []
    for url in urls2:
        try:
            response = requests.head(url)
            if response.status_code==200:
                good_url.append(url)

        except requests.exceptions.MissingSchema:
            bad_url.append(url)
            continue
        except requests.exceptions.ConnectionError:
            bad_url.append(url)
            continue
    with open(out_files , 'w') as file:
        file.write('\n'.join(good_url))

    print(f"Saved urls {out_files}")

out_files = 'filteredd_urls.txt'
urls(out_files)