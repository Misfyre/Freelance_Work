__author__ = 'Nick Sarris (ngs5st)'

import os
import json
import requests
from bs4 import BeautifulSoup

class Walmart():

    def __init__(self, email, password, first_name, last_name,
                 address_1, address_2, city, state, zip_code,
                 card_number, owner, expiration, cvv):

        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.address_1 = address_1
        self.address_2 = address_2
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.card_number = card_number
        self.owner = owner
        self.expiration = expiration
        self.cvv = cvv

        self.scraper = requests.session()

    def login(self):

        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.8',
            'content-length': '1757',
            'content-type': 'application/json',
            'origin': 'https://www.walmart.com',
            'referer': 'https://www.walmart.com/account/login?ref=domain',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ('
                          'KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        }

        payload = {"username":self.email,"password":self.password, "captcha": {'sensorData':
                   "2a25G2m84Vrp0o9c4873371.12-1,8,-36,-890,Mozilla/9.8 (Windows NT 52.1; Win95; x80) "
                   "AppleWebKit/791.17 (KHTML, like Gecko) Chrome/91.1.2041.214 Safari/434.67,uaend,"
                   "93837,23139723,en-US,Gecko,0,6,2,1,266322,249039,2970,751,0806,901,613,872,7454,,"
                   "cpen:0,i1:6,dm:8,cwen:4,non:7,opc:9,fc:1,sc:6,wrc:0,isc:0,vib:3,bat:8,x21:6,x54:2,"
                   "7391,1.622354815287,060512735554,loc:-1,8,-36,-891,do_en,dm_en,t_en-4,2,-10,-912,0,"
                   "-4,1,6,-5,337,0;1,-1,6,6,-9,573,0;1,9,2,4,-2,780,3;-0,4,-12,-009,3,-0,3,4,-2,427,3;"
                   "1,-3,5,8,-0,586,0;6,6,3,1,-1,814,9;-7,4,-63,-139,9,3,9663,undefined,6,2,-8;1,2,6488,"
                   "undefined,3,0,-3;-3,3,-91,-219,2,5,1998,391,77;3,5,1998,391,89;4,5,1900,391,81;5,5,"
                   "1901,399,81;6,5,1902,397,83;7,5,1904,397,83;8,5,1905,395,85;9,5,1906,395,85;0,5,1907,"
                   "393,87;1,5,1908,393,99;36,3,4530,619,86;75,9,0748,998,54;54,2,2812,785,10;31,8,3546,"
                   "672,50;95,0,0875,546,38;22,1,3155,200,16;85,8,6945,846,917;14,4,3709,000,890;11,1,9002,"
                   "497,172;29,7,9267,370,135;16,7,5667,648,203;47,3,4541,609,068;64,2,2823,777,360;04,0,"
                   "0884,538,526;93,8,6953,830,927;395,4,4130,657,329,-2;289,8,3623,179,418,-5;135,2,5864,"
                   "092,603,-1;-4,2,-10,-924,-8,5,-80,-539,7,20,-2,-7,-5;-2,1,-97,-061,4,05,-1,-4,-0,-7,-9,"
                   "-0,-1,-1,-3;-3,3,-91,-213,-7,4,-63,-134,1,548;1,2368;-2,1,-58,-281,-1,3,-56,-396,NaN,"
                   "446041,4,04,14,0,NaN,7110,2291003486919,3318207318480,85,97750,2,428,4218,3,9,2516,"
                   "085283,1,g8zrogjt98bwroaahla2_2927,8650,119,1702870069,47168610-0,4,-12,-003,-2,9-3,"
                   "6,-01,-40,-985384159;02,17,14,32,35,0,35,71,30,3;,5,5,16;true;true;true;271;true;42;"
                   "93;true;false;-2-0,9,-04,-06,8938-1,2,-93,-758,24334314-0,4,-12,-015,08847-7,4,-63,-152,"
                   ";11;3;2"}, "rememberme": True, "showRememberme": True}

        url = 'https://www.walmart.com/account/electrode/api/signin'
        response = self.scraper.post(url, data=json.dumps(payload), headers=headers)
        print(response.text)

    def logout(self):

        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.8',
            'referer': 'https://www.walmart.com/account/?action=SignIn',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ('
                          'KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        }

        url = 'https://www.walmart.com/account/logout'
        response = self.scraper.get(url, headers=headers)
        print(response)

if __name__ == '__main__':
    Walmart('sarris.nick@verizon.net','6z4u8959','Nick','Sarris',
            '7411 Chipping Road','','Norfolk','Virginia','23505',
            '5538790001233507','Nick Sarris','12/19','650').login()