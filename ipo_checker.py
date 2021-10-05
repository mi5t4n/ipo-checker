#! /usr/bin/python

import argparse
import requests
from yachalk import chalk
import inquirer

base_url = "https://iporesult.cdsc.com.np"

def run_ipo_checker(args):
    company = get_company()

    bulk_check(args, company)


def bulk_check(args, company):
    file = open(args.file, "r")
    for line in file:
        data = line.strip().split(",")
        response = check_single_ipo(company, data[0])

        if 200 != response.status_code:
            continue

        body = response.json()

        if (body['success']):
            print(chalk.green( "[" + data[1].strip() + "]" + " :: " + body['message']))
        else:
            print(chalk.red( "[" + data[1].strip() + "]" + " :: " + body['message']))

def get_company():
    url = base_url + "/result/companyShares/fileUploaded"

    response = requests.get(url)

    body = response.json()

    if not body['success'] :
        return False

    companies = {}
    for company in body['body']:
        companies[company['name']] = company['id']

    companies = sorted(companies.items(), key=lambda x: x[1], reverse=True)

    questions=[
        inquirer.List("company", message = "Select the company?", choices=companies)
    ]

    answers = inquirer.prompt(questions)

    return answers['company']

def check_single_ipo(company, boid):
    url = base_url + "/result/result/check";

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
        "Origin": base_url,
        "Referer": base_url,
        "Content-Type":"application/json",
    }

    payload = {
        "boid": str(boid),
        "companyShareId": str(company)
    }

    return requests.post(url, json=payload);

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='IPO Checker for a list.')
    parser.add_argument('--file', type=str, required=True,
                        help='Name of the pattern file.')
    args = parser.parse_args()

    run_ipo_checker(args)
