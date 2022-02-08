import requests as r
import os


def main():
    url_ipv4 = r'https://api.ipify.org'
    req_ipv4 = r.request("GET", url_ipv4).text
    stream = os.popen("ifconfig")
    output = stream.readlines(0)[1]

    print(
        f"""
my public ipv4 is: '{req_ipv4}'
my private ip is: '{output.split(" ")[9]}'
        """)


if __name__ == '__main__':
    main()
