from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Provides:

    pass
class sql_SqlProvides(Provides):

    def __init__(self, url: str, user: str, password: str, driver: str, storedProcedure: str, maxIdle: str, minIdle: str, maxActive: str, maxWait: str, timeBetweenEvictionRunsMillis: str, metadata: str):
        self.url = url
        self.user = user
        self.password = password
        self.driver = driver
        self.storedProcedure = storedProcedure
        self.maxIdle = maxIdle
        self.minIdle = minIdle
        self.maxActive = maxActive
        self.maxWait = maxWait
        self.timeBetweenEvictionRunsMillis = timeBetweenEvictionRunsMillis
        self.metadata = metadata
        
        pass
    @property
    def maxWait(self):
        return self.__maxWait

    @maxWait.setter
    def maxWait(self, maxWait: str):
        self.__maxWait = maxWait


    @property
    def timeBetweenEvictionRunsMillis(self):
        return self.__timeBetweenEvictionRunsMillis

    @timeBetweenEvictionRunsMillis.setter
    def timeBetweenEvictionRunsMillis(self, timeBetweenEvictionRunsMillis: str):
        self.__timeBetweenEvictionRunsMillis = timeBetweenEvictionRunsMillis


    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user: str):
        self.__user = user


    @property
    def minIdle(self):
        return self.__minIdle

    @minIdle.setter
    def minIdle(self, minIdle: str):
        self.__minIdle = minIdle


    @property
    def metadata(self):
        return self.__metadata

    @metadata.setter
    def metadata(self, metadata: str):
        self.__metadata = metadata


    @property
    def maxIdle(self):
        return self.__maxIdle

    @maxIdle.setter
    def maxIdle(self, maxIdle: str):
        self.__maxIdle = maxIdle


    @property
    def storedProcedure(self):
        return self.__storedProcedure

    @storedProcedure.setter
    def storedProcedure(self, storedProcedure: str):
        self.__storedProcedure = storedProcedure


    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url


    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password


    @property
    def driver(self):
        return self.__driver

    @driver.setter
    def driver(self, driver: str):
        self.__driver = driver


    @property
    def maxActive(self):
        return self.__maxActive

    @maxActive.setter
    def maxActive(self, maxActive: str):
        self.__maxActive = maxActive

