import re


def get_logs(file):
    with open(file, 'r', encoding='utf-8') as logs:
        RE_PARCER = re.compile(r'^(.[^\s]+)\W+(\[\w+.+\])\s\"([A-Z]+)\s(\/[^\"]+)\"\s(\d+)\s(\d+)')
        for i in logs.readlines():
            match = re.search(RE_PARCER, i)
            print(list[match[1], match[2], match[3], match[4], match[5], match[6]])


run = get_logs('nginx_logs.txt')
