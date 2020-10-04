import json
from pyorbital.orbital import Orbital
import datetime
import time
import requests

# Python program to read
# json file
class Dataset:
    def __init__(self):
        self.line1=""
        self.filename="static/Data/Satellites.json"
        self.name1=""
        self.name=""
        self.tle1=""
        self.tle2=""
    # Opening JSON file

    def load_satellite(self):
        f = open(self.filename)

        # returns JSON object as
        # a dictionary
        data = json.load(f)

        # Iterating through the json
        # list
        x=[]
        for i in data["Satellites"]:
            link = i["url"]
            f = requests.get(link)
            x.append(f.split("\n"))

        f.close()
        return x

    def checksum(self):
        """Calculate checksum for the current TLE."""
        check = 0
        for char in self.line1[:-1]:
            if char.isdigit():
                check += int(char)
            if char == "-":
                check += 1
        return (check-1)%10

    def create_txt(self):
        f=open('static/Data/parser.txt','w')
        for i in range(len(self.name1)):
            self.name=self.name1[i]
            self.line1 =self.tle1[i]
            self.line2 =self.tle2[i]

            dayssince = time.strftime("%y%j.00000000")
            dayssince = dayssince[0:1] + '0' * (15 - len(dayssince)) + dayssince[2:]
            self.line1 = self.line1[0:18] + dayssince + self.line1[32:-1]
            self.line1 = self.line1 + str(self.checksum())
            f.writelines(self.name+'\n')
            f.writelines(self.line1+'\n')
            f.writelines(self.line2+'\n')
        f.close()

    def orbitpos(file_name,names,date):
        orbit=[]
        cont=0
        for nam in names:
            try:
                orb = Orbital(nam, file_name)
                orbit.append([nam,orb.get_lonlatalt(date),orb.get_position(date)])
                        #altitudine in km da terra  #pos normalizata r_sat/r_terra
            except:
                cont+=1
                print(nam,cont)

        return orbit
    

    def run(self):
        x=self.load_satellite()

        currentlines = []
        count = 0

        # Strips the newline character
        for line in x:
            if line == '\n':
                pass
            elif count == 0:
                NOME = line
                count += 1
            elif count == 1:
                TL1 = line
                count += 1

            else:
                TL2 = line
                count = 0
                currentlines.append([TL1[2:8], NOME, TL1, TL2])

        currentlines.sort()
        prev = ''
        newlines= []
        for currentline in currentlines:
            if prev == currentline[0]:
                pass
            else:
                newlines.append(currentline)
            prev = currentline[0]

        name = []
        tle1 = []
        tle2 = []
        for d in newlines:
            for di in d:
                temp = d[di]
                name.append(temp[1])
                tle1.append(temp[2])
                tle2.append(temp[3])

        self.create_txt(name, tle1, tle2)

        return self.orbitpos('static/Data/parser.txt',name, datetime.datetime.utcnow())


D=Dataset()
print(D.run())
'''
xs=[]
ys=[]
zs=[]
us=[]
vs=[]
ws=[]
for ai in a:
    xs.append(ai[2][0][0])
    ys.append(ai[2][0][1])
    zs.append(ai[2][0][2])
    us.append(ai[2][1][0])
    vs.append(ai[2][1][1])
    ws.append(ai[2][1][2])
'''



