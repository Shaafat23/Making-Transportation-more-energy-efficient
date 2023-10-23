from Part1 import read_data
from Part1 import measurement_to_string
from Part1 import read_uhf

uhf_filename = "uhf.csv"
data_filename = "air_quality.csv"
read_uhfdata = read_uhf(uhf_filename)
read_read_data = read_data(data_filename)
zip_code_dict = read_uhfdata[0]
UHF_dict = read_read_data[0]
Date_dict = read_read_data[1]

#Q1 Which UHF id had the worst pollution in 2012.
pollution_list = []
UHFpollutiondict = {}
search_key = "/12"

for i in Date_dict.keys():
    if search_key in i:
        pollution_list.append(Date_dict[i])
pollution = []
for item in pollution_list:
    for d in item:
        pollution.append(d[3])
        UHFpollutiondict[d[0]] = d[3]


hipollutionUHF = max(UHFpollutiondict, key= UHFpollutiondict.get)
highestpollution = UHFpollutiondict[hipollutionUHF]
print("The UHF id that had the worst pollution in 2012 was:", hipollutionUHF, "at", highestpollution, "mcg/m^3.\n") 


#Q2 What was the average air polution in Queens in 2016 and in 2020.
Borough_dict = read_uhfdata[1]
blist = []
QueensUHF = []
allpollution = []
pollutiondata16 = []
pollutiondata20 = []
search_borough = "Queens"


for b in Borough_dict:
  blist.append(b)
for i in Borough_dict.keys():
    if search_borough in i:
        QueensUHF.append(Borough_dict[i])
for item in QueensUHF:
    for x in item:
        allpollution.append(UHF_dict[x])
for items in allpollution:
    for n in items:
        if "12/1/16" in n:
            pollutiondata16.append(n[3])
        if "12/1/20" in n:
            pollutiondata20.append(n[3])
        if "6/1/20" in n:
            pollutiondata20.append(n[3])

totalpollution16 = sum(pollutiondata16)
average16 = totalpollution16/len(pollutiondata16)
totalpollution20 = sum(pollutiondata20)
average20 = totalpollution20/len(pollutiondata20)
print("The average air pollution in Queens in 2016 was", average16,"\nThe average air pollution in Queens in 2020 was", average20)
