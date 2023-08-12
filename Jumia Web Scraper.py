import requests as s
import re
from time import sleep

S = '\033[2;36m'
B = "\033[1;90m"

class EG:
    n = 1
    def __init__(self):
        self.inp = input("Enter Name of Product: ")
        self.scrap()

    def format(self, r):
        nam = re.findall(r'data-name="([^"]+)', r)
        con = re.findall(r'class="prc">([^<]+)', r)
        ur = re.findall(r'class="core" href="/ar/([^"]+)', r)
        for name, url, ur in zip(nam, con, ur):
            print("Description:", name, '\nPrice:', url, '\nLink of Product: https://www.jumia.com.eg/ar/' + ur, end='\n==============================================\n')
            open(f"Scraping Jumia EG 🇪🇬 [{self.inp}].txt","a").write(f'Discription : {name}\nPrice : {url}\nLink of Product : https://www.jumia.com.eg/ar/{ur}\n==============================================\n')

    def format1(self, r):
        nam = re.findall(r'class="name">([^<]+)', r)
        con = re.findall(r'class="old">([^<]+)', r)
        ur = re.findall(r'class="core" href="/ar/([^"]+)', r)
        for name, url, ur in zip(nam, con, ur):
            print("Description:", name, '\nPrice:', url, '\nLink of Product: https://www.jumia.com.eg/ar/' + ur, end='\n==============================================\n')
            open(f"Scraping Jumia EG 🇪🇬 [{self.inp}].txt","a").write(f'Discription : {name}\nPrice : {url}\nLink of Product : https://www.jumia.com.eg/ar/{ur}\n==============================================\n')

    def scrap(self):
        #global inp
        url = f"https://www.jumia.com.eg/ar/catalog/?q={self.inp}"
        r = s.get(url).text
        try:
                la = r.split('&amp;page=')[5].split('#')[0]
                las = int(la)
                self.format(r)
                for i in range(las):
                    self.n += 1
                    url1 = f"https://www.jumia.com.eg/ar/catalog/?q={self.inp}&page={self.n}"
                    r = s.get(url1).text
                    self.format(r)
        except:
                print("Error Search\nTrying Method Number 2....")
                self.format1(r)


class DZ:
	def __init__(self):
		self.inp = input("Enter Name of Product : ")
		self.scrap(self)
		
	def format(self,r):
		nam = re.findall(r'data-name="([^"]+)',r)
		con = re.findall(r'class="prc">([^<]+)',r)
		ur = re.findall(r'class="core" href="/([^"]+)',r)
		for name, url, ur in zip(nam, con, ur):
			print("Discription : ",name,'\nPrice : ',url, '\nLink of Product : https://www.jumia.dz/'+ur,end='\n==============================================\n')
			open(f"Scraping Jumia DZ 🇩🇿 [{self.inp}].txt","a").write(f'Discription : {name}\nPrice : {url}\nLink of Product : https://www.jumia.dz/{ur}\n==============================================\n')
			
	def format1(self,r):
		nam = re.findall(r'class="name">([^<]+)', r)
		con = re.findall(r'class="old">([^<]+)', r)
		ur = re.findall(r'class="core" href="/([^"]+)',r)
		for name, url, ur in zip(nam, con, ur):
		  print("Discription : ",name,'\nPrice : ',url, '\nLink of Product : https://www.jumia.dz/'+ur,end='\n==============================================\n')
		  open(f"Scraping Jumia DZ 🇩🇿 [{self.inp}].txt","a").write(f'Discription : {name}\nPrice : {url}\nLink of Product : https://www.jumia.dz/{ur}\n==============================================\n')
	def scrap(self,r):
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
	                

class GH:
    n = 1
    def __init__(self):
        self.inp = input("Enter Name of Product: ")
        self.scrap()

    def format(self, r):
        nam = re.findall(r'class="name">([^<]+)',r)
        con = re.findall(r'class="prc">([^<]+)', r)
        ur = re.findall(r'class="core" href="/([^"]+)', r)
        for name, url, ur in zip(nam, con, ur):
            print("Discription : ",name,'\nPrice : ',url, '\nLink of Product : https://www.jumia.com.gh/'+ur,end='\n==============================================\n')
            open(f"Scraping Jumia GH 🇬🇭 [{self.inp}].txt","a").write(f'Discription : {name}\nPrice : {url}\nLink of Product : https://www.jumia.com.gh/{ur}\n==============================================\n')

    def format1(self, r):
        nam = re.findall(r'class="name">([^<]+)', r)
        con = re.findall(r'class="old">([^<]+)', r)
        ur = re.findall(r'class="core" href="/([^"]+)', r)
        for name, url, ur in zip(nam, con, ur):
            print("Discription : ",name,'\nPrice : ',url, '\nLink of Product : https://www.jumia.com.gh/'+ur,end='\n==============================================\n')
            open(f"Scraping Jumia GH 🇬🇭 [{self.inp}].txt","a").write(f'Discription : {name}\nPrice : {url}\nLink of Product : https://www.jumia.com.gh/{ur}\n==============================================\n')

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
                


class SN:
    n = 1
    def __init__(self):
        self.inp = input("Enter Name of Product: ")
        self.scrap()

    def format(self, r):
        nam = re.findall(r'class="name">([^<]+)',r)
        con = re.findall(r'class="prc">([^<]+)', r)
        ur = re.findall(r'class="core" href="/([^"]+)', r)
        for name, url, ur in zip(nam, con, ur):
            print("Discription : ",name,'\nPrice : ',url, '\nLink of Product : https://www.jumia.sn/'+ur,end='\n==============================================\n')
            open(f"Scraping Jumia SN 🇸🇳 [{self.inp}].txt","a").write(f'Discription : {name}\nPrice : {url}\nLink of Product : https://www.jumia.sn/{ur}\n==============================================\n')

    def format1(self, r):
        nam = re.findall(r'class="name">([^<]+)', r)
        con = re.findall(r'class="old">([^<]+)', r)
        ur = re.findall(r'class="core" href="/([^"]+)', r)
        for name, url, ur in zip(nam, con, ur):
            print("Discription : ",name,'\nPrice : ',url, '\nLink of Product : https://www.jumia.sn/'+ur,end='\n==============================================\n')
            open(f"Scraping Jumia SN 🇸🇳 [{self.inp}].txt","a").write(f'Discription : {name}\nPrice : {url}\nLink of Product : https://www.jumia.sn/{ur}\n==============================================\n')

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
                
class NG:
    n = 1
    def __init__(self):
        self.inp = input("Enter Name of Product: ")
        self.scrap()

    def format(self, r):
        nam = re.findall(r'class="name">([^<]+)',r)
        con = re.findall(r'class="prc">([^<]+)', r)
        ur = re.findall(r'class="core" href="/([^"]+)', r)
        for name, url, ur in zip(nam, con, ur):
            print("Discription : ",name,'\nPrice : ',url, '\nLink of Product : https://www.jumia.com.ng/'+ur,end='\n==============================================\n')
            open(f"Scraping Jumia NG 🇳🇬 [{self.inp}].txt","a").write(f'Discription : {name}\nPrice : {url}\nLink of Product : https://www.jumia.com.ng/{ur}\n==============================================\n')

    def format1(self, r):
        nam = re.findall(r'class="name">([^<]+)', r)
        con = re.findall(r'class="old">([^<]+)', r)
        ur = re.findall(r'class="core" href="/([^"]+)', r)
        for name, url, ur in zip(nam, con, ur):
            print("Discription : ",name,'\nPrice : ',url, '\nLink of Product : https://www.jumia.com.ng/'+ur,end='\n==============================================\n')
            open(f"Scraping Jumia NG 🇳🇬  [{self.inp}].txt","a").write(f'Discription : {name}\nPrice : {url}\nLink of Product : https://www.jumia.com.ng/{ur}\n==============================================\n')

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
                
class MR:
    n = 1
    def __init__(self):
        self.inp = input("Enter Name of Product: ")
        self.scrap()

    def format(self, r):
        nam = re.findall(r'class="name">([^<]+)',r)
        con = re.findall(r'class="prc">([^<]+)', r)
        ur = re.findall(r'class="core" href="/([^"]+)', r)
        for name, url, ur in zip(nam, con, ur):
            print("Discription : ",name,'\nPrice : ',url, '\nLink of Product : https://www.jumia.ma/'+ur,end='\n==============================================\n')
            open(f"Scraping Jumia MAR 🇲🇦 [{self.inp}].txt","a").write(f'Discription : {name}\nPrice : {url}\nLink of Product : https://www.jumia.ma/{ur}\n==============================================\n')

    def format1(self, r):
        nam = re.findall(r'class="name">([^<]+)', r)
        con = re.findall(r'class="old">([^<]+)', r)
        ur = re.findall(r'class="core" href="/([^"]+)', r)
        for name, url, ur in zip(nam, con, ur):
            print("Discription : ",name,'\nPrice : ',url, '\nLink of Product : https://www.jumia.ma/'+ur,end='\n==============================================\n')
            open(f"Scraping Jumia MAR 🇲🇦 [{self.inp}].txt","a").write(f'Discription : {name}\nPrice : {url}\nLink of Product : https://www.jumia.ma/{ur}\n==============================================\n')

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
                                
class Scraper():
 print(S+f"""				Jumia Scraper {B}By @J2_N2
				=======================
				             """)
 nap = input(f"""{S}[1]  EG{B}YPT
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