import os
import re
import sys
import json

import requests

def get_f1s_and_s1s_from_cik(cik):
    forms = []
    for file in os.listdir('forms_idx'):
        filepath = os.path.join('forms_idx', file)
        with open(filepath, 'r', encoding='latin-1') as f:
            for line in f.readlines():
                if re.search(f" {cik} ", line) and (line.startswith("F-1 ") or line.startswith("S-1 ")):
                    forms.append(line[line.strip().rfind(" ")::].strip())
    return forms

def get_tickers_json():
    if os.path.exists("company_tickers.json"):
        tickers_json = {}
        with open("company_tickers.json", "r") as f:
            tickers_json = json.loads(f.read())
        return tickers_json
    print("Downloading company_tickers.json...")
    response = requests.get("https://www.sec.gov/files/company_tickers.json")
    with open("company_tickers.json", "w") as f:
        f.write(response.text)
    return json.loads(response.text)

def get_dict_tickers():
    tickers_json = get_tickers_json()
    dict_tickers = {}
    for _, ticker in tickers_json.items():
        dict_tickers[ticker["ticker"]] = ticker["cik_str"]
    return dict_tickers

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 get_forms_urls.py <cik/ticker>")
        sys.exit(1)
    quiet = False
    if "-q" in sys.argv:
        quiet = True
        sys.argv.remove("-q")
    ticker = sys.argv[1]
    if ticker.isnumeric():
        cik = ticker
    else:
        dict_tickers = get_dict_tickers()
        cik = dict_tickers[sys.argv[1].upper()]
    if not quiet:
        print(f"Starting search for F-1s and S-1s for company {cik=}")

    forms = get_f1s_and_s1s_from_cik(cik)
    if not quiet:
        print("Found the following F-1s and S-1s:")
    for path in forms:
        print(f"https://www.sec.gov/Archives/{path}")


