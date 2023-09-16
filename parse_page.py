import requests
from bs4 import BeautifulSoup


def parse_page():
    with open('urls.txt', 'r') as f:
        urls = f.read().split()

    cookies = {
        'TAUnique': '%1%enc%3AjZbvR9B%2B2WF8wLdiMYOYyYMikW%2Fz7rJ1dV1KdbpZORM2jHwltRJPGQ%3D%3D',
        'TADCID': 'O35K3sxSu89pd91-ABQCCKy0j55CTpGVsECjuwJMq3hBUTMSZp3sd8GmoDkaJc0J96v8MTEu2d_XsorYZS7tBQqE4p08nVh4e5c',
        'TASameSite': '1',
        'TASSK': 'enc%3AALh47%2Fhvsk%2By0BcgsCVVnM69TZoS%2Bn3PY4PcZgolgcgv9yT%2BC8QfmIxJRdrIv4bA6PsBSKd6Bi4%2Bv9YzW7uLC6WRnRFMlHQ0bkCAzZMPT%2FkLF3WY4HkT5iCMPcBRPxywMQ%3D%3D',
        'ServerPool': 'B',
        'PMC': 'V2*MS.23*MD.20230916*LD.20230916',
        'TART': '%1%enc%3AfMC3YjGDmMnjnbfxLWhrcgmJbFgJjKLM6gBx0iUDFlgIZ%2FPnNHrVAs9um05HU%2BB8yx9HjuV9fk0%3D',
        'TATravelInfo': 'V2*A.2*MG.-1*HP.2*FL.3*RS.1',
        'TASID': '7AC14CBB57CD4EB0A5ABEE67B5E9FDA3',
        '_abck': '2AED00A27A92B7F2688FD11C0439F7ED~-1~YAAQoANJF6tr5YaKAQAANSOCngriqil00Nm8mP2wBWc3eg8D/aftOpnu6BeUmsH3O2RMa9+EQs8/CtY6+RudGheG4k6JnkEVfJ7iXcltpYFTL1vfh7vAGT5XmqpukiUaXZJAKWCQcg6lkDiE/1SOEZZsmcPqrLq2LWhaH+ipdnkF2xw21FiRmDSCzua6+nXNaxQ0kfDaobEUlWXjTsuWizeKvXw1wKrR8qL0zVSTcU6EnsjCCeMOIrPg1IcYd0V8BARrTZEXNVg7gxm1yIiQYjpfJIg+5htyPSFx8h4p0zjgcsywug9FGtyDjFjVYKh2JB37ksRjFHaG7P1fFj34HmzkT0U1lUYDkMbg+8GypsRI/a9YO2Ul29e7kSiZehr9nQ==~-1~-1~-1',
        'bm_sz': '1C51CD5505CECD634DD1C5BAA0F05487~YAAQoANJF6xr5YaKAQAANSOCnhVpVMlfU95tyWvpa82uqJ7Cpg9C+oAu1OvEm/MvBKllDIpHp7GLSHRzXgB1Q006NvewPpba5EWEoRsQYUemVvgB960aeWQzb2rxkbCvCuLoiQcpW/r9e3h14Etz48tfLtpE20Y7vsMggqKajayQUKKAff8rUYIH8E3hYCNhj9hNeGux2sgnuW4Zkp8gyf/I1CRXMyBq9x4Bn5NpjTmTKyTgQAV0OdtpYq0ojc3GvyMGIImlg51xQVlASzpHc3WNPzMJVb7vCR6zeNzHSVkhBUcr5lwv8A==~3551539~4474418',
        'PAC': 'ADoaQH_lY-C2FVtdrtabmS7jRUaGScsySoIUAVDVq9LPU-kPmQ-1IyEqBL1fhIs5KJmsGe0h4yE0ngu5OaAwtDzh4Nvq7LA6uoGWMf3fdYhLlApCUzbGmoFL62Q2oTXwQ1SOlBK1Jt8gojNwxe2Dln19NKgB-vHK2D2q7XyBtGgh_f0nrn3AE5wc81VHXF1cjjKjs1G1cYZfI3bK8CrpzrNkBQeuvizbi2lmWzN2eNR8p0wXZamh6yogdWSM74h-xr9dod07RpgrI1fKPspw7FNnw36D8ir70R7TrskxJ0bMtfNNID9W31vVgUEchvRF4J15cfjTEj3RuWSdkDX6boNjzpekvHQxFGdnODBXVEJP',
        'VRMCID': '%1%V1*id.13091*llp.%2FFindRestaurants%3Fgeo%3D187479%26establishmentTypes%3D10591%252C9909%252C9900%252C11776%252C16556%252C9901%26priceTypes%3D10953%252C10955%252C10954%26broadened%3Dfalse*e.1695481245809',
        'TATrkConsent': 'eyJvdXQiOiIiLCJpbiI6IkFMTCJ9',
        '_ga': 'GA1.1.689492702.1694876447',
        '_pbjs_userid_consent_data': '3524755945110770',
        '_li_dcdm_c': '.tripadvisor.com',
        '_lc2_fpi': 'b140173de591--01haf84cy8mdcqt7hj91agc5hb',
        'pbjs_sharedId': '75697411-cfed-4aa8-8cc9-6d746e4e89e3',
        'TAAUTHEAT': 'Pp8bd_w-uH2N7eEtABQCobW21V9oR1-Dg22GNw6BiDgYUa6Xz704oRtei7MM-bMAmYj8t8rcKy-1X2a9j2J9J4OmWKhLf-fbis8iew22ueNhAoxfDQQuFID72Nxq5jJ0p5BCD3XONXgBDpuTa6ilYJ3pNdzBVGOCBXa5wk23rnh0WRgs8GotP1UwWcUEPtQ-0LvWRoyqUa9n4TgtTem95o5v13pSEambQv0A',
        '__vt': 'YVGDlBCcSlHZFYjKABQCCQPEFUluRFmojcP0P3EgGige8VgaCZKCDhJCeCZNnojcumMPVqzxKsy88oHDWl9TlVgpa9USMJ7CcotkAa0fn3K67-ruYaniTv58IOAhbGIQ7dkPtLP4cLsspVHmvewCKF2UeOJHeTawNuseRPRWOoTceBF92_1KL0rxMOeCsn-xa0Eg60jaSU3lHMkkxx6mpPIDhaN8-Ov3lAzgdmr-8zEDHb5GUSslSqOReKtmp14ZXQ',
        'G_AUTH2_MIGRATION': 'informational',
        'TAReturnTo': '%1%%2FRestaurant_Review-g562820-d23759392-Reviews-Fiore_Italianissimo-Playa_de_las_Americas_Arona_Tenerife_Canary_Islands.html',
        'roybatty': 'TNI1625!AN64Db8mJpj6K0tSgopAsuTBRLf5fgXQZAkPUIQpIKso%2BJTN%2BtC1hIp1LVxF%2BtVHZjat%2FIQfn64mkZ9j1bkihdsGTCeJrNhfXub%2B6DrGXTLC1EQtN0KN3J%2F671GrvkJuk1Y8m9wM2qV4b0lKPtf3epgLcVg1FLc%2B2ZlVP6lzTLnh%2C1',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Sat+Sep+16+2023+18%3A01%3A21+GMT%2B0300+(%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202209.1.0&isIABGlobal=false&hosts=&consentId=8DD7DC3022D0E1F9CB1FF3FB7B28CE59&interactionCount=0&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false',
        'SRT': '%1%enc%3AfMC3YjGDmMnjnbfxLWhrcgmJbFgJjKLM6gBx0iUDFlgIZ%2FPnNHrVAs9um05HU%2BB8yx9HjuV9fk0%3D',
        '_ga_QX0Q50ZC9P': 'GS1.1.1694876447.1.1.1694876481.26.0.0',
        'TASession': '%1%V2ID.7AC14CBB57CD4EB0A5ABEE67B5E9FDA3*SQ.8*PR.40185%7C*LS.PageMoniker*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.8DD7DC3022D0E1F9CB1FF3FB7B28CE59*LF.en*FA.1*DF.0*TRA.false*LD.23759392*EAU.%27',
        'TAUD': 'LA-1694876451981-1*RDD-1-2023_09_16*LG-29949-2.1.F.*LD-29950-.....',
        'datadome': '5RPb4Libtq0BBOAEujapRpcZ-u~Jb_Y4~xn7xNPp~ih~Ojk-byaajtjPppzh1UThLmnk5-OR5rsYE5QNgWsXecFyxWvUpeAavwI5iH-KRUD7aZOATPONKHGz_JYSapi_',
    }

    headers = {
        'authority': 'www.tripadvisor.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        # 'cookie': 'TAUnique=%1%enc%3AjZbvR9B%2B2WF8wLdiMYOYyYMikW%2Fz7rJ1dV1KdbpZORM2jHwltRJPGQ%3D%3D; TADCID=O35K3sxSu89pd91-ABQCCKy0j55CTpGVsECjuwJMq3hBUTMSZp3sd8GmoDkaJc0J96v8MTEu2d_XsorYZS7tBQqE4p08nVh4e5c; TASameSite=1; TASSK=enc%3AALh47%2Fhvsk%2By0BcgsCVVnM69TZoS%2Bn3PY4PcZgolgcgv9yT%2BC8QfmIxJRdrIv4bA6PsBSKd6Bi4%2Bv9YzW7uLC6WRnRFMlHQ0bkCAzZMPT%2FkLF3WY4HkT5iCMPcBRPxywMQ%3D%3D; ServerPool=B; PMC=V2*MS.23*MD.20230916*LD.20230916; TART=%1%enc%3AfMC3YjGDmMnjnbfxLWhrcgmJbFgJjKLM6gBx0iUDFlgIZ%2FPnNHrVAs9um05HU%2BB8yx9HjuV9fk0%3D; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RS.1; TASID=7AC14CBB57CD4EB0A5ABEE67B5E9FDA3; _abck=2AED00A27A92B7F2688FD11C0439F7ED~-1~YAAQoANJF6tr5YaKAQAANSOCngriqil00Nm8mP2wBWc3eg8D/aftOpnu6BeUmsH3O2RMa9+EQs8/CtY6+RudGheG4k6JnkEVfJ7iXcltpYFTL1vfh7vAGT5XmqpukiUaXZJAKWCQcg6lkDiE/1SOEZZsmcPqrLq2LWhaH+ipdnkF2xw21FiRmDSCzua6+nXNaxQ0kfDaobEUlWXjTsuWizeKvXw1wKrR8qL0zVSTcU6EnsjCCeMOIrPg1IcYd0V8BARrTZEXNVg7gxm1yIiQYjpfJIg+5htyPSFx8h4p0zjgcsywug9FGtyDjFjVYKh2JB37ksRjFHaG7P1fFj34HmzkT0U1lUYDkMbg+8GypsRI/a9YO2Ul29e7kSiZehr9nQ==~-1~-1~-1; bm_sz=1C51CD5505CECD634DD1C5BAA0F05487~YAAQoANJF6xr5YaKAQAANSOCnhVpVMlfU95tyWvpa82uqJ7Cpg9C+oAu1OvEm/MvBKllDIpHp7GLSHRzXgB1Q006NvewPpba5EWEoRsQYUemVvgB960aeWQzb2rxkbCvCuLoiQcpW/r9e3h14Etz48tfLtpE20Y7vsMggqKajayQUKKAff8rUYIH8E3hYCNhj9hNeGux2sgnuW4Zkp8gyf/I1CRXMyBq9x4Bn5NpjTmTKyTgQAV0OdtpYq0ojc3GvyMGIImlg51xQVlASzpHc3WNPzMJVb7vCR6zeNzHSVkhBUcr5lwv8A==~3551539~4474418; PAC=ADoaQH_lY-C2FVtdrtabmS7jRUaGScsySoIUAVDVq9LPU-kPmQ-1IyEqBL1fhIs5KJmsGe0h4yE0ngu5OaAwtDzh4Nvq7LA6uoGWMf3fdYhLlApCUzbGmoFL62Q2oTXwQ1SOlBK1Jt8gojNwxe2Dln19NKgB-vHK2D2q7XyBtGgh_f0nrn3AE5wc81VHXF1cjjKjs1G1cYZfI3bK8CrpzrNkBQeuvizbi2lmWzN2eNR8p0wXZamh6yogdWSM74h-xr9dod07RpgrI1fKPspw7FNnw36D8ir70R7TrskxJ0bMtfNNID9W31vVgUEchvRF4J15cfjTEj3RuWSdkDX6boNjzpekvHQxFGdnODBXVEJP; VRMCID=%1%V1*id.13091*llp.%2FFindRestaurants%3Fgeo%3D187479%26establishmentTypes%3D10591%252C9909%252C9900%252C11776%252C16556%252C9901%26priceTypes%3D10953%252C10955%252C10954%26broadened%3Dfalse*e.1695481245809; TATrkConsent=eyJvdXQiOiIiLCJpbiI6IkFMTCJ9; _ga=GA1.1.689492702.1694876447; _pbjs_userid_consent_data=3524755945110770; _li_dcdm_c=.tripadvisor.com; _lc2_fpi=b140173de591--01haf84cy8mdcqt7hj91agc5hb; pbjs_sharedId=75697411-cfed-4aa8-8cc9-6d746e4e89e3; TAAUTHEAT=Pp8bd_w-uH2N7eEtABQCobW21V9oR1-Dg22GNw6BiDgYUa6Xz704oRtei7MM-bMAmYj8t8rcKy-1X2a9j2J9J4OmWKhLf-fbis8iew22ueNhAoxfDQQuFID72Nxq5jJ0p5BCD3XONXgBDpuTa6ilYJ3pNdzBVGOCBXa5wk23rnh0WRgs8GotP1UwWcUEPtQ-0LvWRoyqUa9n4TgtTem95o5v13pSEambQv0A; __vt=YVGDlBCcSlHZFYjKABQCCQPEFUluRFmojcP0P3EgGige8VgaCZKCDhJCeCZNnojcumMPVqzxKsy88oHDWl9TlVgpa9USMJ7CcotkAa0fn3K67-ruYaniTv58IOAhbGIQ7dkPtLP4cLsspVHmvewCKF2UeOJHeTawNuseRPRWOoTceBF92_1KL0rxMOeCsn-xa0Eg60jaSU3lHMkkxx6mpPIDhaN8-Ov3lAzgdmr-8zEDHb5GUSslSqOReKtmp14ZXQ; G_AUTH2_MIGRATION=informational; TAReturnTo=%1%%2FRestaurant_Review-g562820-d23759392-Reviews-Fiore_Italianissimo-Playa_de_las_Americas_Arona_Tenerife_Canary_Islands.html; roybatty=TNI1625!AN64Db8mJpj6K0tSgopAsuTBRLf5fgXQZAkPUIQpIKso%2BJTN%2BtC1hIp1LVxF%2BtVHZjat%2FIQfn64mkZ9j1bkihdsGTCeJrNhfXub%2B6DrGXTLC1EQtN0KN3J%2F671GrvkJuk1Y8m9wM2qV4b0lKPtf3epgLcVg1FLc%2B2ZlVP6lzTLnh%2C1; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Sep+16+2023+18%3A01%3A21+GMT%2B0300+(%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202209.1.0&isIABGlobal=false&hosts=&consentId=8DD7DC3022D0E1F9CB1FF3FB7B28CE59&interactionCount=0&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false; SRT=%1%enc%3AfMC3YjGDmMnjnbfxLWhrcgmJbFgJjKLM6gBx0iUDFlgIZ%2FPnNHrVAs9um05HU%2BB8yx9HjuV9fk0%3D; _ga_QX0Q50ZC9P=GS1.1.1694876447.1.1.1694876481.26.0.0; TASession=%1%V2ID.7AC14CBB57CD4EB0A5ABEE67B5E9FDA3*SQ.8*PR.40185%7C*LS.PageMoniker*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.8DD7DC3022D0E1F9CB1FF3FB7B28CE59*LF.en*FA.1*DF.0*TRA.false*LD.23759392*EAU.%27; TAUD=LA-1694876451981-1*RDD-1-2023_09_16*LG-29949-2.1.F.*LD-29950-.....; datadome=5RPb4Libtq0BBOAEujapRpcZ-u~Jb_Y4~xn7xNPp~ih~Ojk-byaajtjPppzh1UThLmnk5-OR5rsYE5QNgWsXecFyxWvUpeAavwI5iH-KRUD7aZOATPONKHGz_JYSapi_',
        'referer': 'https://www.tripadvisor.com/FindRestaurants?geo=187479&offset=0&establishmentTypes=10591%2C9909%2C9900%2C11776%2C16556%2C9901&priceTypes=10953%2C10955%2C10954&broadened=false',
        'sec-ch-device-memory': '8',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-full-version-list': '"Chromium";v="116.0.5845.188", "Not)A;Brand";v="24.0.0.0", "Google Chrome";v="116.0.5845.188"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }
    for url in urls:
        response = requests.get(
            url,
            cookies=cookies,
            headers=headers,
        )
        soup = BeautifulSoup(response.content, 'lxml')
        name = soup.find('h1', class_='HjBfq').text
        text = soup.find_all("a", class_='AYHFM')
        address = text[1].text
        links = soup.find_all('span', class_='DsyBj cNFrA')
        telephone = links[2].text
        website = text[3].text


        print(website)


parse_page()
