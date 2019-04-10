from TimeStatsProfiler import *
from memory_profiler import profile as memoryProfile
from FileHelper import *

class DuplicateUpdated:


    def __isDuplicate(self, name, firstNameListDict):

        isDuplicate = False

        if firstNameListDict and \
                name in firstNameListDict:
            isDuplicate = True

        return isDuplicate

    @timeStatsProfiler
    @memoryProfile
    def getDuplicateItems(self, firstNameList, secondNameList):

        firstNameListDict = {}
        duplicateItemList = []

        # Populate firstName list dict
        for eachName in firstNameList:
            firstNameListDict[eachName] = 1

        for eachName in secondNameList:

            if self.__isDuplicate(eachName, firstNameListDict):
                duplicateItemList.append(eachName)

        print(duplicateItemList)


if __name__ == '__main__':

    fileHelper = FileHelper()
    firstNameList = fileHelper.getNameList("FirstNameList.json")
    secondNameList = fileHelper.getNameList("SecondNameList.json")

    duplicate = DuplicateUpdated()
    duplicate.getDuplicateItems(firstNameList, secondNameList)
