from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class genmymodelreverse_java_util_logging_Logger:

    pass


class model_Supervisor:

    pass


class model_Operator:

    pass


class model_Director:

    pass


class model_CallCenterEmployee:

    def __init__(self, LOGGER: genmymodelreverse_java_util_logging_Logger, name: str, employeeType: str, callsAnswered: int):
        self.LOGGER = LOGGER
        self.name = name
        self.employeeType = employeeType
        self.callsAnswered = callsAnswered
        
        pass
    @property
    def employeeType(self):
        return self.__employeeType
    @employeeType.setter
    def employeeType(self, employeeType: str):
        self.__employeeType = employeeType

    @property
    def callsAnswered(self):
        return self.__callsAnswered
    @callsAnswered.setter
    def callsAnswered(self, callsAnswered: int):
        self.__callsAnswered = callsAnswered

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def LOGGER(self):
        return self.__LOGGER
    @LOGGER.setter
    def LOGGER(self, LOGGER: genmymodelreverse_java_util_logging_Logger):
        self.__LOGGER = LOGGER



class model_T:

    pass


class model_Call:

    def __init__(self, number: int, MIN: int, MAX: int, LOGGER: genmymodelreverse_java_util_logging_Logger):
        self.number = number
        self.MIN = MIN
        self.MAX = MAX
        self.LOGGER = LOGGER
        
        pass
    @property
    def MIN(self):
        return self.__MIN
    @MIN.setter
    def MIN(self, MIN: int):
        self.__MIN = MIN

    @property
    def LOGGER(self):
        return self.__LOGGER
    @LOGGER.setter
    def LOGGER(self, LOGGER: genmymodelreverse_java_util_logging_Logger):
        self.__LOGGER = LOGGER

    @property
    def MAX(self):
        return self.__MAX
    @MAX.setter
    def MAX(self, MAX: int):
        self.__MAX = MAX

    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number: int):
        self.__number = number

