import json

url = input("What is the url? ")

fileName = input("Name of file with JSON object: ")

print(url + " " + fileName)

file = open(fileName)

with open(fileName) as file:
    jsonPayload = json.load(file)

print(jsonPayload)