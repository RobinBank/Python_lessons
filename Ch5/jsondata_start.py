# 
# Example file for parsing and processing JSON
#
import urllib.request 
import json

def printResults(data):
  # Use the json module to load the string data into a dictionary
  theJSON = json.loads(data)

  
  # now we can access the contents of the JSON like any other Python object

  # if "title" in theJSON["metadata"]:
  #     print(theJSON["metadata"]["title"])
  #     print(theJSON["metadata"]["api"])
  # output the number of events, plus the magnitude and each event name  
  # if "count" in theJSON["metadata"]:
  #     print("Total number of eventthe:" +str(theJSON["metadata"]["count"]))
  # for i in theJSON["features"]:
  #      print("Place : " +str(i["properties"]["place"]))
  #      print("Event : " +str(i["properties"]["type"]))
  #      print("The magnatitude of the event : " +str(i["properties"]["mag"]))
  #      print("--------------\n")

  
    # for each event, print the place where it occurred


  # print the events that only have a magnitude greater than 4
  # for i in theJSON["features"]:
  #   mag = (i["properties"]["mag"])
  #   if mag >= 5:
  #      print("Place : " +str(i["properties"]["place"]))
  #      print("Event : " +str(i["properties"]["type"]))
  #      print("The magnatitude of the event : " +str(i["properties"]["mag"]))
  #      print("--------------\n")

  # print only the events where at least 1 person reported feeling something

  for i in theJSON["features"]:
    feltsomething = (i["properties"]["felt"])
    if feltsomething != None:
      if feltsomething != "null":
        if feltsomething > 0:
            print("Place : " +str(i["properties"]["place"]))
            print("Event : " +str(i["properties"]["type"]))
            print("The magnatitude of the event : " +str(i["properties"]["mag"]))
            print("Felt something : " +str(i["properties"]["felt"]))
            print("--------------\n")
  
def main():
  # define a variable to hold the source URL
  # In this case we'll use the free data feed from the USGS
  # This feed lists all earthquakes for the last day larger than Mag 2.5
  urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

  # Open the URL and read the data
  webUrl = urllib.request.urlopen(urlData)
  print ("result code: " + str(webUrl.getcode()))
  
  if (webUrl.getcode() == 200):
    data = webUrl.read().decode("utf-8")
    printResults(data)

  else:
        print("Received an error from server, cannot retrieve results " +
              str(webUrl.getcode()))


if __name__ == "__main__":
  main()
