import requests,re,os
os.system('clear')
print("Ambil Proxy Disini > https://linkduit.net/OSIcx")
proxyss = raw_input("Proxy > ")

http_proxy = "http://"+proxyss
https_proxy = "http://"+proxyss
ftp_proxy = "http://"+proxyss

proxyDict = {
	      "http"  : http_proxy,
	      "https" : https_proxy,
	      "ftp"   : ftp_proxy
	     }

print proxyDict

def xhamster():
    os.system('clear')
    r = requests.get("https://xhamster.com", proxies=proxyDict)
    cari_judul = re.findall('alt=".*?"', r.text)
    cari_durasi = re.findall('duration">.*?<', r.text)
    cari_link = re.findall('https://xhamster.com/videos/.*?"', r.text)
    cjcount = 1
    cdcount = 0
    clcount = 0
    for _ in cari_link:
	 cdcount += 1
    print "    Total Video 0-{}".format(cdcount)
    print "=======================)>"
    pilih = input("Pilih > ")
    if pilih == 0:
        phasil = cari_link[3]
        rcl = phasil.replace('"', '')
        res = requests.get(rcl, proxies=proxyDict)
        bkphsl = res.text.replace("\\", "")
        bkphsl1 = re.findall('"480p":"https:.*?"', bkphsl)[0]
        rbkphsl = bkphsl1.replace('"480p":"', '')
	rbkphsl2 - rbkphsl.replace('"', '')
	os.system('clear')
	print "Copy Link Dibawah | Buka Di Browser"
	print ""
        os.system('termux-open-url '+rbkphsl2)
	os.sys.exit()
    elif pilih == 1:
        phasil = cari_link[4]
        rcl = phasil.replace('"', '')
        res = requests.get(rcl, proxies=proxyDict)
        bkphsl = res.text.replace("\\", "")
        bkphsl1 = re.findall('"480p":"https:.*?"', bkphsl)[0]
        rbkphsl = bkphsl1.replace('"480p":"', '')
        rbkphsl2 = rbkphsl.replace('"', '')
        os.system('clear')
        print "Copy Link Dibawah | Buka Di Browser"
	print ""
	os.system('termux-open-url '+rbkphsl2)
	os.sys.exit()
    elif pilih == 2:
        phasil = cari_link[5]
        rcl = phasil.replace('"', '')
        res = requests.get(rcl, proxies=proxyDict)
        bkphsl = res.text.replace("\\", "")
        bkphsl1 = re.findall('"480p":"https:.*?"', bkphsl)[0]
        rbkphsl = bkphsl1.replace('"480p":"', '')
        rbkphsl2 = rbkphsl.replace('"', '')
	os.system('clear')
        print "Copy Link Dibawah | Buka Di Browser"
        print ""
	os.system('termux-open-url '+rbkphsl2)
	os.sys.exit()
    phasil = cari_link[pilih]
    rcl = phasil.replace('"', '')
    res = requests.get(rcl, proxies=proxyDict)
    bkphsl = res.text.replace("\\", "")
    bkphsl1 = re.findall('"480p":"https:.*?"', bkphsl)[0]
    rbkphsl = bkphsl1.replace('"480p":"', '')
    rbkphsl2 = rbkphsl.replace('"', '')
    os.system('clear')
    print "Copy Link Dibawah | Buka Di Browser"
    print ""
    os.system('termux-open-url '+rbkphsl2)
    os.sys.exit()

if __name__ == "__main__":
    xhamster()
