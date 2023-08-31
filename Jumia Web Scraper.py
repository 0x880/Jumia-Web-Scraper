import requests as s
import re
import pandas as pd

S = '\033[2;36m'
B = "\033[1;90m"

class EG:
    def __init__(self):
        self.inp = input(B+"Enter Name of Product: "+S)
        self.n = 0
        self.results = []
        self.scrap()

    def format(self, r):
        nam = re.findall(r'data-name="([^"]+)', r)
        con = re.findall(r'class="prc">([^<]+)', r)
        ur = re.findall(r'class="core" href="/ar/([^"]+)', r)
        for name, pri, link in zip(nam, con, ur):
            result = {
                'Description': name,
                'Price': pri,
                'Link of Product': f'https://www.jumia.com.eg/ar/{link}'
            }
            self.results.append(result)

    def format1(self, r):
        nam = re.findall(r'class="name">([^<]+)', r)
        con = re.findall(r'class="old">([^<]+)', r)
        ur = re.findall(r'class="core" href="/ar/([^"]+)', r)
        for name, pri, link in zip(nam, con, ur):
            result = {
                'Description': name,
                'Price': pri,
                'Link of Product': f'https://www.jumia.com.eg/ar/{link}'
            }
            self.results.append(result)

    def scrap(self):
        url = f"https://www.jumia.com.eg/ar/catalog/?q={self.inp}"
        r = s.get(url).text
        try:
            la = r.split('&amp;page=')[5].split('#')[0]
            las = int(la)
            self.format(r)
            for i in range(las):
                self.n = 1
                url1 = f"https://www.jumia.com.eg/ar/catalog/?q={self.inp}&page={self.n}"
                r = s.get(url1).text
                self.format(r)
                
        except:
            print("Error Search\nTrying Method Number 2....")
            self.format1(r)

        df = pd.DataFrame(self.results)

        file_name = f"Scraping Jumia EG 🇪🇬 [{self.inp}].xlsx"
        df.to_excel(file_name, index=False)
        print("Scrapped Finished Done ✅")


class DZ:
	def __init__(self):
		self.inp = input(B+"Enter Name of Product: "+S)
		self.n = 0
		self.results = []
		self.scrap()
		
	def format(self,r):
		nam = re.findall(r'data-name="([^"]+)',r)
		con = re.findall(r'class="prc">([^<]+)',r)
		ur = re.findall(r'class="core" href="/([^"]+)',r)
		for name, pri, link in zip(nam, con, ur):
			result = {
                'Description': name,
                'Price': pri,
                'Link of Product': f'https://www.jumia.dz/{link}',
			}
			self.results.append(result)
	def format1(self,r):
		nam = re.findall(r'class="name">([^<]+)', r)
		con = re.findall(r'class="old">([^<]+)', r)
		ur = re.findall(r'class="core" href="/([^"]+)',r)
		for name, pri, link in zip(nam, con, ur):
		  result = {
                'Description': name,
                'Price': pri,
                'Link of Product': f'https://www.jumia.dz/{link}',
		  }
		  self.results.append(result)
		  
	def scrap(self):
	       url = f"https://www.jumia.dz/catalog/?q={self.inp}"
	       r = s.get(url).text

	       try:
	                la = r.split('&amp;page=')[5].split('#')[0]
	                las = int(la)
	                self.format(r)
	                for i in range(las):
	                    self.n += 1
	                    url1 = f"https://www.jumia.dz/catalog/?q={self.inp}&page={self.n}"
	                    r = s.get(url1).text
	                    self.format(r)
	       except:
	                print("Error Search\nTrying Method Number 2....")
	                self.format1(r)
	       df = pd.DataFrame(self.results)
	       file_name = f"Scraping Jumia DZ 🇩🇿 [{self.inp}].xlsx"
	       df.to_excel(file_name, index=False)
	       print("Scrapped Finished Done ✅")

class GH:
    def __init__(self):
        self.inp = input(B+"Enter Name of Product: "+S)
        self.n = 0
        self.results = []
        self.scrap()

    def format(self, r):
        nam = re.findall(r'class="name">([^<]+)',r)
        con = re.findall(r'class="prc">([^<]+)', r)
        ur = re.findall(r'class="core" href="/([^"]+)', r)
        
        for name, pri, link in zip(nam, con, ur):
            result = {
                'Description': name,
                'Price': pri,
                'Link of Product': f'https://www.jumia.com.gh/{link}'
            }
            self.results.append(result)
            
    def format1(self, r):
        nam = re.findall(r'class="name">([^<]+)', r)
        con = re.findall(r'class="old">([^<]+)', r)
        ur = re.findall(r'class="core" href="/([^"]+)', r)
        for name, pri, link in zip(nam, con, ur):
            result = {
                'Description': name,
                'Price': pri,
                'Link of Product': f'https://www.jumia.com.gh/{link}'
            }
            self.results.append(result)
            
    def scrap(self):

        url = f"https://www.jumia.com.gh/catalog/?q={self.inp}"
        r = s.get(url).text
        #print(r)

        try:
                la = r.split('&amp;page=')[5].split('#')[0]
                las = int(la)
                self.format(r)
                for i in range(las):
                    self.n += 1
                    url1 = f"https://www.jumia.com.gh/catalog/?q={self.inp}&page={self.n}"
                    r = s.get(url1).text
                    #print(r)
                    self.format(r)

        except:
                print("Error Search\nTrying Method Number 2....")
                self.format1(r)
        df = pd.DataFrame(self.results)

        file_name = f"Scraping Jumia GH 🇬🇭 [{self.inp}].xlsx"
        df.to_excel(file_name, index=False)
        print("Scrapped Finished Done ✅")


class SN:
    def __init__(self):
        self.inp = input(B+"Enter Name of Product: "+S)
        self.n = 0
        self.results = []
        self.scrap()

    def format(self, r):
        nam = re.findall(r'class="name">([^<]+)',r)
        con = re.findall(r'class="prc">([^<]+)', r)
        ur = re.findall(r'class="core" href="/([^"]+)', r)
        for name, pri, link in zip(nam, con, ur):
            result = {
                'Description': name,
                'Price': pri,
                'Link of Product': f'https://www.jumia.sn/{link}'
            }
            self.results.append(result)
            
    def format1(self, r):
        nam = re.findall(r'class="name">([^<]+)', r)
        con = re.findall(r'class="old">([^<]+)', r)
        ur = re.findall(r'class="core" href="/([^"]+)', r)
        for name, pri, linkr in zip(nam, con, ur):
            result = {
                'Description': name,
                'Price': pri,
                'Link of Product': f'https://www.jumia.sn/{link}'
            }
            self.results.append(result)
            
    def scrap(self):
        url = f"https://www.jumia.sn/catalog/?q={self.inp}"
        r = s.get(url).text
        #print(r)

        try:
                la = r.split('&amp;page=')[5].split('#')[0]
                las = int(la)
                self.format(r)
                for i in range(las):
                    self.n += 1
                    url1 = f"https://www.jumia.sn/catalog/?q={self.inp}&page={self.n}"
                    r = s.get(url1).text
                    #print(r)
                    self.format(r)
                    
        except:
                print("Error Search\nTrying Method Number 2....")
                self.format1(r)
        df = pd.DataFrame(self.results)
        file_name = f"Scraping Jumia SEN 🇸🇳 [{self.inp}].xlsx"
        df.to_excel(file_name, index=False)
        print("Scrapped Finished Done ✅")
        
        
class NG:
    def __init__(self):
        self.inp = input(B+"Enter Name of Product: "+S)
        self.n = 0
        self.results = []
        self.scrap()

    def format(self, r):
        nam = re.findall(r'class="name">([^<]+)',r)
        con = re.findall(r'class="prc">([^<]+)', r)
        ur = re.findall(r'class="core" href="/([^"]+)', r)
        for name, pri, link in zip(nam, con, ur):
            result = {
                'Description': name,
                'Price': pri,
                'Link of Product': f'https://www.jumia.com.ng/{link}'
            }
            self.results.append(result)
            
    def format1(self, r):
        nam = re.findall(r'class="name">([^<]+)', r)
        con = re.findall(r'class="old">([^<]+)', r)
        ur = re.findall(r'class="core" href="/([^"]+)', r)
        for name, pri, link in zip(nam, con, ur):
            result = {
                'Description': name,
                'Price': pri,
                'Link of Product': f'https://www.jumia.com.ng/{link}'
            }
            self.results.append(result)
            
    def scrap(self):

        url = f"https://www.jumia.com.ng/catalog/?q={self.inp}"
        r = s.get(url).text
        #print(r)

        try:
                la = r.split('&amp;page=')[5].split('#')[0]
                las = int(la)
                self.format(r)
                for i in range(las):
                    self.n += 1
                    url1 = f"https://www.jumia.com.ng/catalog/?q={self.inp}&page={self.n}"
                    r = s.get(url1).text
                    #print(r)
                    self.format(r)
                    
        except:
                print("Error Search\nTrying Method Number 2....")
                self.format1(r)
                
        df = pd.DataFrame(self.results)
        file_name = f"Scraping Jumia NG 🇳🇬 [{self.inp}].xlsx"
        df.to_excel(file_name, index=False)               
        print("Scrapped Finished Done ✅")
                        
class MR:
    def __init__(self):
        self.inp = input(B+"Enter Name of Product: "+S)
        self.n = 0
        self.results = []
        self.scrap()

    def format(self, r):
        nam = re.findall(r'class="name">([^<]+)',r)
        con = re.findall(r'class="prc">([^<]+)', r)
        ur = re.findall(r'class="core" href="/([^"]+)', r)
        for name, pri, link in zip(nam, con, ur):
            result = {
                'Description': name,
                'Price': pri,
                'Link of Product': f'https://www.jumia.ma/{link}'
            }
            self.results.append(result)
            
    def format1(self, r):
        nam = re.findall(r'class="name">([^<]+)', r)
        con = re.findall(r'class="old">([^<]+)', r)
        ur = re.findall(r'class="core" href="/([^"]+)', r)
        for name, pri, link in zip(nam, con, ur):
            result = {
                'Description ': name,
                'Price': pri,
                'Link of Product': f'https://www.jumia.ma/{link}'
            }
            self.results.append(result)
            
    def scrap(self):

        url = f"https://www.jumia.ma/catalog/?q={self.inp}"
        r = s.get(url).text
        #print(r)

        try:
                la = r.split('&amp;page=')[5].split('#')[0]
                las = int(la)
                self.format(r)
                for i in range(las):
                    self.n += 1
                    url1 = f"https://www.jumia.ma/catalog/?q={self.inp}&page={self.n}"
                    r = s.get(url1).text
                    #print(r)
                    self.format(r)
                    
        except:
                print("Error Search\nTrying Method Number 2....")
                #print(r)
                self.format1(r)             
                   
        df = pd.DataFrame(self.results)
        file_name = f"Scraping Jumia MAR 🇲🇦 [{self.inp}].xlsx"
        df.to_excel(file_name, index=False)
        print("Scrapped Finished Done ✅")
class Scraper():
 print(S+f"""				Jumia Scraper {B}By @J2_N2
				=======================
				             """)
 nap = input(f"""{S}[1]  EG{B}YPT
 ——•——•——•——•——•——•——
{S}[2]  ALGE{B}RIA
——•——•——•——•——•——•——
{S}[3]  GHA{B}N
——•——•——•——•——•——•——
{S}[4]  SEN{B}EGAL
——•——•——•——•——•——•——
{S}[5]  NIG{B}ERIA
——•——•——•——•——•——•——
{S}[6]  MOR{B}OCCO
{B}====================================
{S}[~] Cho{B}ose ====> """)
 print('====================================')

 if nap == '1':
 	EG()
 if nap == '2':
 	DZ()
 if nap == '3':
 	GH()
 if nap == '4':
 	SN()
 if nap == '5':
 	NG()
 if nap == '6':
 	MR()
if __name__ == "__main__":
	Scraper()
