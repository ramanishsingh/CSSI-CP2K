from cssi_cp2k.classes import EACH

class PROGRAM_RUN_INFO:

  def __init__(self,errorLog=[],changeLog=[],location=""):

    self.__errorLog  = errorLog
    self.__changeLog = changeLog
    self.__location  = "{}/PROGRAM_RUN_INFO".format(location)
    #PROGRAM_RUN_INFO subsections
    self.__EACH      = EACH.EACH(errorLog=self.__errorLog,changeLog=self.__changeLog,
                         location=self.__location)

  @property
  def errorLog(self):
    return self.__errorLog

  @property
  def changeLog(self):
    return self.__changeLog

  @property
  def location(self):
    return self.__location

  @property
  def EACH(self):
    return self.__EACH
