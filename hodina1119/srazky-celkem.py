import urllib.request

url = "https://voskh.cz/envirotyden/index.php?lokalita=kutnahora"

# otevreni komunikace s webovym serverem, stezeni odpoedi ue serveru
odpoved = urllib.request.urlopen(url)

pocet_dnu = 0
srazky_celkem = 0

radek = odpoved.readline()                #CTU PRVNMI RADEK
while bool(radek):          
  text_radku = radek.decode("utf-8")
  srazky = float(text_radku)
  if srazky >= 0:
   pocet_dnu += 1
   srazky_celkem += srazky
  radek = odpoved.readline()             # ctu druhy radek
odpoved.close()

print(srazky_celkem / pocet_dnu)