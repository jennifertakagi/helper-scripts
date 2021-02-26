import json
import csv

FILE_INPUT = "drinks.csv"
FILE_OUTPUT = "cleared_drinks.json"

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
  """Reads the data from CSV file and storage the fields:
      [name, category, image, ingredients, measurements_ingredients,
      instructions, glass_type, drink_type] into a list
  """

  data_list = []

  with open(FILE_INPUT, mode="r") as csv_read:
    file_reader = csv.reader(csv_read, delimiter=",")

    for field in file_reader:
      if (field[0] != "strDrink"):
        data_list.append({
          "name": field[0],
          "category": field[1],
          "image": field[2],
          "ingredients": transformList(field[3], True),
          "measurements_ingredients": transformList(field[4]),
          "instructions": field[5],
          "glass_type": field[6],
          "drink_type": field[7]
        })
    
    writeJSONFile(data_list)


def writeJSONFile(data_list):
  """Writes a data list in a JSON file,
      also write '[' on start, ']' on final,
      and ',' between each collection

    Args:
      data_list (list): The data list
  """

  with open(FILE_OUTPUT, 'wt') as csv_write:
    for result in data_list:
      if result == data_list[0]:
        csv_write.write('[')

      json.dump(result, csv_write, sort_keys = True, indent = 4,
               ensure_ascii = False)
      
      if result == data_list[-1]:
        csv_write.write(']')

      if result != data_list[-1]:
        csv_write.write(',')


readDataFromCSV()
