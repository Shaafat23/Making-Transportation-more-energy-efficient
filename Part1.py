import csv 

def read_data(data_filename):
  """
  should return two dictionaries (i.e. a tuple with two elements, 
  each of them a dictionary).

  1) A dictionary mapping each UHF geographic IDs to a lists of measurement tuples.
  2) A dictionary mapping each date (as a string) to a list of measurement tuples.
  """ 
  UHFdict = {}
  Datedict = {}
  with open(data_filename, "r", encoding='utf-8-sig') as csvfile:
      reader = csv.DictReader(csvfile, fieldnames = ["UHF id", "Geo Description", "Date", "pm2.5"])

      for row in reader:
          UHF = int(row["UHF id"])
          date = str(row["Date"])
          rowli = []
          rowli.append(int(row["UHF id"]))
          rowli.append(row["Geo Description"])
          rowli.append(row["Date"])
          rowli.append(float(row["pm2.5"]))
          rows = tuple(rowli)
          if UHF not in UHFdict:
              newUHF = [rows]
              UHFdict[UHF] = newUHF
          if rows not in UHFdict[UHF]:
              UHFdict[UHF].append(rows)
  with open(data_filename, "r", encoding='utf-8-sig') as csvfile:
     reader = csv.DictReader(csvfile, fieldnames = ["UHF id", "Geo Description", "Date", "pm2.5"])

     for row in reader:
          UHF = int(row["UHF id"])
          date = str(row["Date"])
          rowli = []
          rowli.append(int(row["UHF id"]))
          rowli.append(row["Geo Description"])
          rowli.append(row["Date"])
          rowli.append(float(row["pm2.5"]))
          rows = tuple(rowli)
          if date not in Datedict:
              newdate = [rows]
              Datedict[date] = newdate
          if rows not in Datedict[date]:
              Datedict[date].append(rows)
  read_data_tup = (UHFdict, Datedict)
  return read_data_tup


def measurement_to_string(measurement):
  """
  format a single measurement tuple as a string. For example: 
  "6/1/09 UHF 205 Sunset Park 11.45 mcg/m^3"
  """
  msli = []
  msli.append(measurement[2])
  msli.append(measurement[0])
  msli.append(measurement[1])
  msli.append(measurement[3])
  measure = "{} UHF {} {} {} mcg/m^3".format(msli[0], msli[1], msli[2], msli[3])

  return measure  


def read_uhf(uhf_filename):
  """
  should return two dictionaries: 
  1) A dictionary mapping each zip code to a list of UHF geographic IDs 
  2) A dictionary mapping each borough name to a list of UHF geographic IDs.
  """
  zipid = {}
  boroughid = {}
  with open(uhf_filename, "r") as csvfile:
      read = csv.reader(csvfile, delimiter= ",")
      for row in read:
          ids = int(row[2])
          zipcodes = row[3:]
          zipcodesints = []
          for item in zipcodes:
              zipcodesints.append(int(item))
          for x in range(0, len(zipcodesints)):
              zips = zipcodesints[x]
              if zips not in zipid:
                  zipid[zips] = [ids]
              else:
                  zipid[zips].append(ids)
  with open(uhf_filename, "r") as csvfile:
    read = csv.reader(csvfile, delimiter= ",")
    Bronxids = []
    Brooklynids = []
    Manhattanids = []
    Queensids = []
    Statenids = []
    boroughlist = []
    for row in read:
        ids = row[2]
        borough = row[0]
        if borough not in boroughlist:
          boroughlist.append(borough)
        if len(boroughlist) == 1 and ids not in Bronxids:
          Bronxids.append(int(ids))
        elif len(boroughlist) == 2 and ids not in Brooklynids:
          Brooklynids.append(int(ids))
        elif len(boroughlist) == 3 and ids not in Manhattanids:
          Manhattanids.append(int(ids))
        elif len(boroughlist) == 4 and ids not in Queensids:
          Queensids.append(int(ids))
        elif len(boroughlist) == 5 and ids not in Statenids:
          Statenids.append(int(ids))

        if len(boroughlist) == 1 and ids not in boroughid:
          boroughid[borough] = Bronxids
        elif len(boroughlist) == 2 and ids not in boroughid:
          boroughid[borough] = Brooklynids
        elif len(boroughlist) == 3 and ids not in boroughid:
          boroughid[borough] = Manhattanids
        elif len(boroughlist) == 4 and ids not in boroughid:
          boroughid[borough] = Queensids
        elif len(boroughlist) == 5 and ids not in boroughid:
          boroughid[borough] = Statenids
  read_uhf_tup = (zipid, boroughid)  
  return read_uhf_tup 


def main():

  data_filename = "air_quality.csv"
  uhf_filename = "uhf.csv"
  read_read_data = read_data(data_filename)
  read_uhfdata = read_uhf(uhf_filename)
  done = False
  while done == False:
    request = input("Would you like to search by zip code, UHF id, borough, or date?\nIf you are done searching, type 'done.'\n")
    if request == "zip code":
      zip_code_dict = read_uhfdata[0]
      search = int(input("Please enter the zip code:\n"))
      print("The results are:")
      if search in zip_code_dict:
        id = zip_code_dict[search]
        for x in id:
          id_list = []
          id_list.append(x)
          UHFdictionary = read_read_data[0]
          for i in id_list:
            measurement = UHFdictionary[i]
            for item in measurement:
              print(measurement_to_string(item))

    elif request == "UHF id":
      UHFdictionary = read_read_data[0]
      search = int(input("Please enter the UHF id:\n"))
      print("The results are:")
      if search in UHFdictionary:
          measurement = UHFdictionary[search]
          for item in measurement:
              print(measurement_to_string(item))

    elif request == "date":
      datedictionary = read_read_data[1]
      search = input("Note that if the month or day is a single digit, there is no need to add a zero in front of it.\nPlease enter the date in mm/dd/yyyy format:\n")
      print("The results are:")
      if search in datedictionary:
          measurement = datedictionary[search]
          for item in measurement:
              print(measurement_to_string(item))

    elif request == "borough":
      boroughdict = read_uhfdata[1]
      search = input("Please enter the borough name:\n")
      print("The results are:")
      if search in boroughdict:
        borough = boroughdict[search]
        for x in borough:
          id_list = []
          id_list.append(x)
          UHFdictionary = read_read_data[0]
          for i in id_list:
            measurement = UHFdictionary[i]
            for item in measurement:
              print(measurement_to_string(item))

    elif request == "done":
      done = True
      print("Thanks for searching!")

if __name__ == "__main__": 
  main()