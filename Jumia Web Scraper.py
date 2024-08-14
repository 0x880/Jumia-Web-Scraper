import requests as req
import re
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

s = req.session()
S = '\033[2;36m'
B = "\033[1;90m"

class Scraper:
    def __init__(self, domain, country):
        self.inp = input(f"Enter Name of Product : ")
        self.n = 1
        self.domain = domain
        self.country = country
        self.results = []
        self.scrap()

    def format_response(self, response, regex_pattern):
        nam = re.findall(regex_pattern['name'], response)
        con = re.findall(regex_pattern['price'], response)
        ur = re.findall(regex_pattern['url'], response)
        disc = re.findall(regex_pattern['disco'], response)
        rate_co = re.findall(regex_pattern['rate_count'], response)
        rate_va = re.findall(regex_pattern['rate_value'], response)
        for product_name, product_price, product_link, product_disc, rate_count, rate_value in zip(
            nam, con, ur, disc, rate_co, rate_va
        ):
            rep_link = f"https://www.jumia.{self.domain}/{self.country}/ {product_link}"
            format_link = "".join(rep_link.split())
            result = {
                "Discription": product_name,
                "Price": product_price,
                "Discount": product_disc,
                "Num of Rating": rate_count,
                "Rating Value": f"{rate_value} / 5",
                "Product Link": format_link,
            }
            self.results.append(result)
            print(
                f"""Discription : {product_name}
Price : {product_price}
Discount : {product_disc}
Number of Rating : {rate_count}
Rating Value : {rate_value} / 5
Product Link : {format_link}
============================
""")

    def process_page(self, page):
        url = f"https://www.jumia.{self.domain}/{self.country}/catalog/?q={self.inp}&page={page}"
        response = s.get(url).text
        regex_pattern = {
            "name": r'class="name">([^<]+)',
            "price": r'rawPrice":"([^"]+)',
            "url": r'class="core" href="/([^"]+)',
            "disco": r'discount":"([^"]+)',
            "rate_count": r'totalRatings":([^}]+)',
            "rate_value": r'rating":{"average":([^,]+)',
        }
        self.format_response(response, regex_pattern)

    def scrap(self):
        url = f"https://www.jumia.{self.domain}/{self.country}/catalog/?q={self.inp}"
        response = s.get(url).text
        try:
            la = response.split('&amp;page=')[5].split('#')[0]
            las = int(la)
            regex_pattern = {
                "name": r'class="name">([^<]+)',
                "price": r'rawPrice":"([^"]+)',
                "url": r'class="core" href="/([^"]+)',
                "disco": r'discount":"([^"]+)',
                "rate_count": r'totalRatings":([^}]+)',
                "rate_value": r'rating":{"average":([^,]+)',
            }
            self.format_response(response, regex_pattern)
            with ThreadPoolExecutor(max_workers=20) as executor:
                futures = [
                    executor.submit(self.process_page, page)
                    for page in range(2, las + 1)
                ]
                for future in futures:
                    future.result()
        except:
            print("Error Search\nTrying Method Number 2....")
            regex_pattern = {
                "name": r'class="name">([^<]+)',
                "price": r'class="prc">([^<]+)',
                "url": r'class="core" href="/([^"]+)',
                "disco": r'discount":"([^"]+)',
                "rate_count": r'totalRatings":([^}]+)',
                "rate_value": r'rating":{"average":([^,]+)',
            }
            self.format_response(response, regex_pattern)

        df = pd.DataFrame(self.results)
        file_name = f"Scraping Jumia [{self.inp}].xlsx"
        df.to_excel(file_name, index=False)
        print("Scrapped Finished Done ✅")


def main():
    print(S + f"""Welcome To Jumia Web Scraper
=======================
                 """)
    nap = input(
        f"""{S}[1]  EG{B}YPT
 ——•——•——•——•——•——•——
{S}[2]  ALGE{B}RIA
——•——•——•——•——•——•——
{S}[3]  GHA{B}NA
——•——•——•——•——•——•——
{S}[4]  SEN{B}EGAL
——•——•——•——•——•——•——
{S}[5]  NIG{B}ERIA
——•——•——•——•——•——•——
{S}[6]  MOR{B}OCCO
{B}====================================
{S}[~] Cho{B}ose ====> """
    )
    print("====================================")

    if nap == "1":
        scraper = Scraper("com.eg", "ar")
    elif nap == "2":
        scraper = Scraper("dz", "ar")
    elif nap == "3":
        scraper = Scraper("com.gh", "")
    elif nap == "4":
        scraper = Scraper("sn", "")
    elif nap == "5":
        scraper = Scraper("com.ng", "")
    elif nap == "6":
        scraper = Scraper("ma", "ar")


if __name__ == "__main__":
    main()
