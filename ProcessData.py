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

    student_id = makeID(first, last, idNum)
    output = last + "," + first + "," + student_id + "\n"
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


if __name__ == '__main__':
  main()
