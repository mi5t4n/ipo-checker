#! /usr/bin/python

import argparse
import requests
from yachalk import chalk

def run_ipo_checker(args):
    file = open(args.file, "r")
    for line in file:
        data = line.strip().split(",")
        response = make_request(args.company, data[0])

        if 200 != response.status_code:
            continue

        body = response.json()

        if (body['success']):
            print(chalk.green( "[" + data[1].strip() + "]" + " :: " + body['message']))
        else:
            print(chalk.red( "[" + data[1].strip() + "]" + " :: " + body['message']))

def make_request(company, boid):
    url = "https://iporesult.cdsc.com.np/result/result/check";

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
        "Origin": "https://iporesult.cdsc.com.np",
        "Referer": "https://iporesult.cdsc.com.np/",
        "Content-Type":"application/json",
    }

    payload = {
        "boid": str(boid),
        "companyShareId": str(company)
    }

    return requests.post(url, json=payload);

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='IPO Checker for a list.')
    parser.add_argument('--company', type=str, required=True, help='Company ID')
    parser.add_argument('--file', type=str, required=True,
                        help='Name of the pattern file.')
    args = parser.parse_args()

    run_ipo_checker(args)
