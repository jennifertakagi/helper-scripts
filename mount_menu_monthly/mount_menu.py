import random
import csv

FILE_INPUT = "menu.csv"
FILE_OUTPUT = "menu_monthly.csv"

def transformList(fields, lower = False):
  """Transforms fields on a list, splitted by ','

    Args:
      fields (str): The file location of the spreadsheet
      lower (bool): A flag used to transform the field on lowercase
        (default is False)

    Returns:
      list: a list of the fields
  """

  result_list = []
  splitted_fields = fields.split(',')

  for field in splitted_fields:
    if (field.strip()):
      if (lower):
        result_list.append(field.lower())
      else:
        result_list.append(field)

  return result_list


def readDataFromCSV():
  """Reads the data from CSV file and storage it into a list"""

  data_list = []

  with open(FILE_INPUT, mode="r") as csv_read:
    file_reader = csv.reader(csv_read, delimiter=",")

    for field in file_reader:
      clean_data = field and field[0] and field[0].strip()
      data_list.append(clean_data)
    
    random.shuffle(data_list)

    mountTwoMealsList(data_list)

def mountTwoMealsList(data_list):
  list_by_two = []
  menu_length = len(data_list) // 2

  for index in range(menu_length):
    list_by_two.append(data_list[index: index + 2])
    index = index + 2

  writeCSVFile(list_by_two)


def writeCSVFile(list_by_two):
  """Writes a data list in a CSV file,

    Args:
      list_by_two (list): The data list with two
  """

  with open(FILE_OUTPUT, 'w', newline='') as csv_write:
    writer = csv.writer(csv_write)

    for food_day in list_by_two:
      writer.writerow([food_day[0], food_day[1]])


readDataFromCSV()
