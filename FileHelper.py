import json

class FileHelper:

    def getNameList(self,filePath):

        with open(filePath) as json_file:
            data = json.load(json_file)
            #print(data)

            return data

