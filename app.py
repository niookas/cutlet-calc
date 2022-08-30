from flask import Flask, render_template, request
import os
from bs4 import BeautifulSoup
import requests
from html.parser import HTMLParser

source = requests.get('https://www.medbank.lt/lt/verslui/kasdienes-paslaugos/valiutos-keitimas')
soup = BeautifulSoup(source.content, features="html.parser")
usd_table = soup.find('div',"custom-content--table custom-content--table---mobile currency-calculator---USD" )
usd_rate = usd_table.find('p', "custom-content--paragraph currency-calculator---sell").text.replace(",", ".")

def delivery(city):
    if city == "ABILENE":	
        return 1575
    elif city == "ADELANTO":	
        return 1505
    elif city == "ALBANY":	
        return 1010
    elif city == "ALBUQUERQUE":	
        return 1725
    elif city == "ALTOONA":	
        return 1140
    elif city == "AMARILLO":	
        return 1625
    elif city == "ANCHORAGE":	
        return 3400
    elif city == "ANDREWS":	
        return 1575
    elif city == "ANTELOPE":	
        return 1650
    elif city == "APPLETON":	
        return 1300
    elif city == "ATLANTA":	
        return 975
    elif city == "AUGUSTA":	
        return 990
    elif city == "AUSTIN":	
        return 1425
    elif city == "BAKERSFIELD":	
        return 1520
    elif city == "BALTIMORE":	
        return 1010
    elif city == "BATON_ROUGE":	
        return 1125
    elif city == "BILLINGS":	
        return 2000
    elif city == "BIRMINGHAM":	
        return 1120
    elif city == "BISMARCK":	
        return 1850
    elif city == "BOISE":	
        return 1950
    elif city == "BUFFALO":	
        return 1225
    elif city == "CANDIA":	
        return 1080
    elif city == "CARTERSVILLE":	
        return 1025
    elif city == "CASPER":	
        return 1825
    elif city == "CHAMBERSBURG":	
        return 1055
    elif city == "CHARLESTON_Hurricane":	
        return 1240
    elif city == "CHICAGO":	
        return 1140
    elif city == "CHINA_GROVE":	
        return 1000
    elif city == "CICERO":	
        return 825
    elif city == "CLEVELAND":	
        return 1225
    elif city == "COLORADO_SPRINGS":	
        return 1500
    elif city == "COLUMBIA_MO":	
        return 1325
    elif city == "COLUMBIA_SC":	
        return 930
    elif city == "COLUMBUS":	
        return 1150
    elif city == "CONCORD":	
        return 1030
    elif city == "CORPUS_CHRISTI":	
        return 1425
    elif city == "CRASHEDTOYS_ATLANTA":	
        return 1000
    elif city == "CRASHEDTOYS_DALLAS":	
        return 1425
    elif city == "CRASHEDTOYS_EAST_BETHEL":	
        return 1335
    elif city == "CRASHEDTOYS_ELDRIDGE":	
        return 1350
    elif city == "CRASHEDTOYS_MINNEAPOLIS":	
        return 1370
    elif city == "CRASHEDTOYS_SACRAMENTO":	
        return 1700
    elif city == "DALLAS":	
        return 1425
    elif city == "DANVILLE":	
        return 1125
    elif city == "DAVENPORT":	
        return 1350
    elif city == "DAYTON":	
        return 1160
    elif city == "DENVER":	
        return 1425
    elif city == "DES_MOINES":	
        return 1350
    elif city == "DETROIT":	
        return 1300
    elif city == "DOTHAN":	
        return 1075
    elif city == "DYER":	
        return 1110
    elif city == "EARLINGTON":	
        return 1210
    elif city == "EL_PASO":	
        return 1625
    elif city == "EUGENE":	
        return 1990
    elif city == "EXETER":	
        return 1080
    elif city == "FAIRBURN":	
        return 975
    elif city == "FAYETTEVILLE":	
        return 1425
    elif city == "FLINT":	
        return 1300
    elif city == "FORT_WAYNE":	
        return 1080
    elif city == "FREDERICKSBURG":	
        return 1125
    elif city == "FREETOWN":	
        return 1080
    elif city == "FRESNO":	
        return 1595
    elif city == "FT._PIERCE":	
        return 1060
    elif city == "FT_WORTH":	
        return 1425
    elif city == "GASTONIA":	
        return 1030
    elif city == "GLASSBORO":	
        return 930
    elif city == "GRAHAM":	
        return 1975
    elif city == "HAMMOND":	
        return 1110
    elif city == "HAMPTON":	
        return 1055
    elif city == "HARRISBURG":	
        return 980
    elif city == "HARTFORD":	
        return 955
    elif city == "HARTFORD_SPRINGFIELD":	
        return 955
    elif city == "HAYWARD_DESERT_VIEW":	
        return 1630
    elif city == "HAYWARD":	
        return 1630
    elif city == "HELENA":	
        return 2000
    elif city == "HONOLULU":	
        return 3835
    elif city == "HOUSTON":	
        return 1275
    elif city == "INDIANAPOLIS":	
        return 1080
    elif city == "IONIA":	
        return 1275
    elif city == "JACKSON":	
        return 1245
    elif city == "JACKSONVILLE":	
        return 925
    elif city == "KANSAS_CITY":	
        return 1375
    elif city == "KINCHELOE":	
        return 1700
    elif city == "KNOXVILLE":	
        return 1090
    elif city == "LANSING":	
        return 1275
    elif city == "LAS_VEGAS":	
        return 1595
    elif city == "LEXINGTON":	
        return 1200
    elif city == "LINCOLN":	
        return 1370
    elif city == "LITTLE_ROCK":	
        return 1275
    elif city == "LONG_BEACH":	
        return 1470
    elif city == "LONG_ISLAND":	
        return 990
    elif city == "LONGVIEW":	
        return 1325
    elif city == "LOS_ANGELES":	
        return 1470
    elif city == "LOUISVILLE":	
        return 1200
    elif city == "LUFKIN":	
        return 1425
    elif city == "LUMBERTON":	
        return 1060
    elif city == "LYMAN":	
        return 1125
    elif city == "MACON":	
        return 990
    elif city == "MADISON":	
        return 1275
    elif city == "MARTINEZ":	
        return 1630
    elif city == "MCALLEN":	
        return 1625
    elif city == "MEBANE":	
        return 1030
    elif city == "MEMPHIS":	
        return 1155
    elif city == "MIAMI":	
        return 1090
    elif city == "MILWAUKEE":	
        return 1225
    elif city == "MINNEAPOLIS":	
        return 1370
    elif city == "MOBILE":	
        return 1075
    elif city == "MOCKSVILLE":	
        return 1030
    elif city == "MONTGOMERY":	
        return 1075
    elif city == "NASHVILLE":	
        return 1120
    elif city == "NEW_ORLEANS":	
        return 1125
    elif city == "NEWBURGH/Marlbo":	
        return 940
    elif city == "NORTH_BOSTON":	
        return 1080
    elif city == "NORTH_CHARLESTON":	
        return 925
    elif city == "NORTH_SEATTLE":	
        return 2000
    elif city == "OCALA":	
        return 1020
    elif city == "OGDEN":	
        return 1600
    elif city == "OKLAHOMA_CITY":	
        return 1425
    elif city == "ORLANDO":	
        return 1020
    elif city == "PASCO":	
        return 2000
    elif city == "PEORIA":	
        return 1175
    elif city == "PHILADELPHIA":	
        return 915
    elif city == "PHOENIX":	
        return 1595
    elif city == "PITTSBURGH":	
        return 1140
    elif city == "PORTLAND":	
        return 1950
    elif city == "PUNTA_GORDA":	
        return 1095
    elif city == "RALEIGH":	
        return 1000
    elif city == "RANCHO_CUCAMONGA":	
        return 1520
    elif city == "REDDING":	
        return 1850
    elif city == "RENO":	
        return 1800
    elif city == "RICHMOND":	
        return 1055
    elif city == "ROCHESTER":	
        return 1140
    elif city == "SACRAMENTO":	
        return 1700
    elif city == "SALT_LAKE_CITY":	
        return 1825
    elif city == "SAN_ANTONIO":	
        return 1625
    elif city == "SAVANNAH":	
        return 865
    elif city == "SCRANTON":	
        return 1010
    elif city == "SEAFORD":	
        return 1010
    elif city == "SHREVEPORT":	
        return 1275
    elif city == "SIKESTON":	
        return 1325
    elif city == "SACRAMENTO":	
        return 1740
    elif city == "SOMERVILLE":	
        return 870
    elif city == "SOUTH_BOSTON":	
        return 1080
    elif city == "SOUTHERN_ILLINOIS":	
        return 1175
    elif city == "SPARTANBURG":	
        return 975
    elif city == "SPOKANE":	
        return 2075
    elif city == "SPRINGFIELD":	
        return 1325
    elif city == "ST_CLOUD":	
        return 1425
    elif city == "ST_LOUIS":	
        return 1135
    elif city == "SUN_VALLEY":	
        return 1500
    elif city == "SYRACUSE":	
        return 1055
    elif city == "TALLAHASSEE":	
        return 1060
    elif city == "TAMPA_SOUTH":	
        return 1050
    elif city == "TANNER":	
        return 1090
    elif city == "TIFTON":	
        return 990
    elif city == "TRENTON":	
        return 890
    elif city == "TUCSON":	
        return 1680
    elif city == "TULSA":	
        return 1425
    elif city == "VALLEJO":	
        return 1625
    elif city == "VAN_NUYS":	
        return 1520
    elif city == "WACO":	
        return 1425
    elif city == "WALTON":	
        return 1175
    elif city == "WASHINGTON":	
        return 1030
    elif city == "WEST_PALM_BEACH":	
        return 1090
    elif city == "WEST_WARREN":	
        return 1080
    elif city == "WHEELING":	
        return 1140
    elif city == "WICHITA":	
        return 1450
    elif city == "YORK_HAVEN":	
        return 1010
    elif city == "Vilnius": 
        return 1250.00
    elif city == "Kaunas": 
        return 800.0
    elif city == "Siauliai":
        return 1050.0
    elif city == "Sakiai":
        return 1350.0




def bidding_fees(bid):
    if bid >= 15000.00:
        return (bid * 0.07)
    elif bid >= 10000.00  and bid <= 14999.99:
        return 800.0
    elif bid >= 7500.00 and bid <= 9999.99:
        return 775.00
    elif bid >= 6000.00 and bid <= 7499.99:
        return 750.00
    elif bid >= 5000.00 and bid <= 5999.99:
        return 725.00
    elif bid >= 4500.00 and bid <= 4999.99:
        return 700.00
    elif bid >= 4000.00 and bid <= 4499.99:
        return 675.00
    elif bid >= 3500.00 and bid <= 3999.99:
        return 650.00
    elif bid >= 3000.00 and bid <= 3499.99:
        return 600.00
    elif bid >= 2500.00 and bid <= 2999.99:
        return 500.00
    elif bid >= 2400.00 and bid <= 2499.99:
        return 480.00
    elif bid >= 2000.00 and bid <= 2399.99:
        return 470.00
    elif bid >= 1800.00 and bid <= 1999.99:
        return 440.00
    elif bid >= 1700.00 and bid <= 1799.99:
        return 420.00
    elif bid >= 1600.00 and bid <= 1699.99:
        return 410.00
    elif bid >= 1600.00 and bid <= 1699.99:
        return 410.00
    elif bid >= 1500 and bid <= 1599.99:
        return 390.00
    elif bid >= 1400.00 and bid <= 1499.99:
        return 380.00
    elif bid >= 1300.00 and bid <= 1399.99:
        return 365.00
    elif bid >= 1200.00 and bid <= 1299.99:
        return 3500.00
    elif bid >= 1000.00 and bid <= 1199.99:
        return 325.00
    elif bid >= 900.00 and bid <= 999.99:
        return 275.00
    elif bid >= 800.00 and bid <= 899.99:
        return 250.00
    elif bid >= 700.00 and bid <= 799.99:
        return 230.00
    elif bid >= 600.00 and bid <= 699.99:
        return 210.00
    elif bid >= 500.00 and bid <= 599.99:
        return 185.00
    elif bid >= 400.00 and bid <= 499.99:
        return 160.00
    elif bid >= 200.00 and bid <= 399.99:
        return 120.00
    elif bid >= 0.00 and bid <= 199.99:
        return 80.00
    

def virtual_fees(bid):
    if bid >= 8000.00:
        return 129.00
    elif bid >= 6000 and bid <= 7999.99:
        return 119.00
    elif bid >= 4000 and bid <= 5999.99:
        return 99.00
    elif bid >= 2000.00 and bid <= 3999.99:
        return 89.00
    elif bid >= 1500.00 and bid <= 1999.99:
        return 79.00
    elif bid >= 1000.00 and bid <= 1499.99:
        return 69.00
    elif bid >= 500.00 and bid <= 999.99:
        return 49.00
    elif bid >= 100.00 and bid <= 499.99:
        return 39.00
    elif bid >= 0.00 and bid <= 99.99:
        return 0.00

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])

def calculate():
    gate_fee = 79
    krova_fee = 310
    kotlet_fee = 500
    env_fee = 10
    rate = float(usd_rate)
    total = ''
    city = None
    dom_ship = ''
    auct_fees = None
    eur = None
    import_fee = None
    sub_total = None
    bid = None

    if request.method == 'POST' and 'bid' in request.form:
        bid = round(float(request.form.get('bid')))
        city = request.form.get('city')
        total = round(bid + bidding_fees(bid) + virtual_fees(bid) + gate_fee + env_fee + delivery(city))
        dom_ship = delivery(city)
        auct_fees = round(bidding_fees(bid) + virtual_fees(bid) + gate_fee + env_fee)
        eur = round(total / rate + kotlet_fee + krova_fee)
        import_fee = round(((eur) / 100) * 31)
        sub_total = eur + import_fee
    return render_template("index.html", eur = eur, bid = bid, import_fee = import_fee, sub_total = sub_total, kotlet_fee = kotlet_fee, krova_fee = krova_fee,total = total, rate=rate, city=city, dom_ship = dom_ship, auct_fees = auct_fees)
 
if __name__ == "__main__":
    app.run(debug=True)