from TimeStatsProfiler import *
from memory_profiler import profile as memoryProfile
from FileHelper import *

class Duplicate:


    def __isDuplicate(self,name,secondNameList):

        isDuplicate = False

        for eachName in secondNameList:
            if eachName == name:
                isDuplicate=True
                break

        return isDuplicate

    @timeStatsProfiler
    @memoryProfile
    def getDuplicateItems(self,firstNameList,secondNameList):

        duplicateItemList = []

        for eachName in firstNameList:
            if self.__isDuplicate(eachName,secondNameList):
                duplicateItemList.append(eachName)

        print(duplicateItemList)



if __name__ == '__main__':

    fileHelper = FileHelper()
    firstNameList = fileHelper.getNameList("FirstNameList.json")
    secondNameList = fileHelper.getNameList("SecondNameList.json")

    duplicate = Duplicate()
    duplicate.getDuplicateItems(firstNameList,secondNameList)

