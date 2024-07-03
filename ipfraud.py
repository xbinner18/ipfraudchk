import requests
from bs4 import BeautifulSoup as bs


def database(ip):
    try:
        base_url = f"https://scamalytics.com/ip/{ip}"  
        r = requests.get(base_url).text
        soup = bs(r, features="html.parser")
        score = soup.find('div', class_="score").get_text().strip("Fraud Score:")
        risk = soup.find('div', class_="panel_title high_risk").get_text()
        # k = soup.findAll('td')
        
        data = {}
        data["ip"] = ip
        data["score"] = score
        data["risk"] = risk
        """data["host"] = k[0].get_text()
        data["asn"] = k[1].get_text()
        data["isp"] = k[2].get_text()
        data["org"] = k[3].get_text()
        data["ctype"] = k[4].get_text()
        data["country"] = k[5].get_text()
        data["code"] = k[6].get_text()
        data["region"] = k[7].get_text()
        data["city"] = k[8].get_text()
        data["zip"] = k[9].get_text()
        data["latitude"] = k[12].get_text()
        data["longitude"] = k[13].get_text()
        data["vpn"] = k[15].get_text()
        data["tor"] = k[16].get_text()
        data["server"] = k[17].get_text()
        data["pproxy"] = k[18].get_text()
        data["wproxy"] = k[19].get_text()
        data["robot"] = k[20].get_text()"""
        return data
    except Exception as e:
        return {"status":False,"error":e}
