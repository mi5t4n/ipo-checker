#! /usr/bin/python

import time
import asyncio
import argparse
import requests
import inquirer
import traceback

from typing import Union
from yachalk import chalk

base_url = "https://iporesult.cdsc.com.np"


def cli():
    parser = argparse.ArgumentParser(description="IPO Checker for a list.")
    parser.add_argument(
        "--file", type=str, help="Name of the pattern file.", default="list.txt"
    )
    args = parser.parse_args()

    run_ipo_checker(args)


def run_ipo_checker(args):
    company = get_company()

    if not company:
        print(chalk.red("Failed to fetch companies."))

        return

    start = time.time()
    results = bulk_check(args, company)
    end = time.time()

    print("\n")

    if results:
        print(chalk.green(f"Alloted:\t{results.count(True)}"))
        print(chalk.red(f"Not Alloted:\t{results.count(False)}"))
        print(chalk.yellow(f"Invalid BOID:\t{results.count(None)}"))

    print(chalk.bold(f"Time elapsed:\t{(end - start):.2f}s"))


def bulk_check(args, company):
    file = open(args.file, "r")

    try:
        loop = asyncio.get_event_loop()

        all_groups = asyncio.gather(
            *[check_ipo(company, investor) for investor in file]
        )
        results = loop.run_until_complete(all_groups)

        loop.close()

        return results

    except Exception:
        print(traceback.format_exc(limit=1, chain=False))

        print(chalk.red("Failed to check IPOs."))

        return False


def get_company():
    companies = {}
    url = base_url + "/result/companyShares/fileUploaded"

    try:
        response = requests.get(url)

        body = response.json()

        if not body["success"]:
            return False

        for company in body["body"]:
            companies[company["name"]] = company["id"]

        companies = sorted(companies.items(), key=lambda x: x[1], reverse=True)

        questions = [
            inquirer.List(
                "company", message="Select the company?", choices=companies
            )
        ]

        answers = inquirer.prompt(questions)

        return answers["company"]

    except Exception:
        print(traceback.format_exc(limit=1, chain=False))

        return False


async def check_ipo(company: int, investor: str) -> Union[bool, None]:
    data = investor.strip().split(",")
    response = check_result(company, data[0])

    if not (response and response.ok):
        return None

    body = response.json()
    message = f"[{data[1].strip()}] :: {body['message']}"

    if body["success"]:
        print(chalk.green(message))

        return True

    print(chalk.red(message))

    return False


def check_result(company: int, boid: str) -> requests.Response:
    url = base_url + "/result/result/check"

    headers = {
        "Origin": base_url,
        "Referer": base_url,
        "Content-Type": "application/json",
    }

    payload = {"boid": str(boid), "companyShareId": str(company)}

    return requests.post(url, headers=headers, json=payload)


if __name__ == "__main__":
    cli()
