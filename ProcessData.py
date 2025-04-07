#ProcessData.py
#Name:Alex Hernandez Lopez
#Date:4/6/25
#Assignment:Lab 8

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  for line in inFile:
    data = line.split()
    first = data[0]
    last = data[1]
    idNum = data[3]
    major = data[6]
    year = data[5]

    student_id = makeID(first, last, idNum)
    major_year = majorYear(major, year)
    output = last + "," + first + "," + student_id + "," + major_year + "\n"
    outFile.write(output)

  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

def makeID(first, last, idNum):
  while len(last) < 5:
    last = last + "X"

  idLen = len(idNum)
  id = first[0] + last + idNum[idLen - 3: ]

  return id

def majorYear(major, year):
  major = major[ :3]
  
  year = year.upper()
  if year == "FRESHMAN":
    year = "FR"
  elif year == "SOPHOMORE":
    year = "SO"
  elif year == "JUNIOR":
    year = "JR"
  elif year == "SENIOR":
    year = "SR"
  
  major_year = major + "-" + year
  return major_year

if __name__ == '__main__':
  main()
