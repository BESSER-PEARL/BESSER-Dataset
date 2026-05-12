from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Users:

    def __init__(self, ID: int, name: str, average_star: int, review_count: int, date_joined: date):
        self.ID = ID
        self.name = name
        self.average_star = average_star
        self.review_count = review_count
        self.date_joined = date_joined
        
        pass
    @property
    def date_joined(self):
        return self.__date_joined
    @date_joined.setter
    def date_joined(self, date_joined: date):
        self.__date_joined = date_joined

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def average_star(self):
        return self.__average_star
    @average_star.setter
    def average_star(self, average_star: int):
        self.__average_star = average_star

    @property
    def review_count(self):
        return self.__review_count
    @review_count.setter
    def review_count(self, review_count: int):
        self.__review_count = review_count

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID



class Reviews:

    def __init__(self, ID: int, business_id: int, user_id: int, date: date, text: str, rating: int):
        self.ID = ID
        self.business_id = business_id
        self.user_id = user_id
        self.date = date
        self.text = text
        self.rating = rating
        
        pass
    @property
    def text(self):
        return self.__text
    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def business_id(self):
        return self.__business_id
    @business_id.setter
    def business_id(self, business_id: int):
        self.__business_id = business_id

    @property
    def rating(self):
        return self.__rating
    @rating.setter
    def rating(self, rating: int):
        self.__rating = rating

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def user_id(self):
        return self.__user_id
    @user_id.setter
    def user_id(self, user_id: int):
        self.__user_id = user_id



class Places:

    def __init__(self, ID: int, address: str, opening_times: date, review_count: int, place_id: str, wifi: str, plugs: str, music: str):
        self.ID = ID
        self.address = address
        self.opening_times = opening_times
        self.review_count = review_count
        self.place_id = place_id
        self.wifi = wifi
        self.plugs = plugs
        self.music = music
        
        pass
    @property
    def opening_times(self):
        return self.__opening_times
    @opening_times.setter
    def opening_times(self, opening_times: date):
        self.__opening_times = opening_times

    @property
    def review_count(self):
        return self.__review_count
    @review_count.setter
    def review_count(self, review_count: int):
        self.__review_count = review_count

    @property
    def music(self):
        return self.__music
    @music.setter
    def music(self, music: str):
        self.__music = music

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def place_id(self):
        return self.__place_id
    @place_id.setter
    def place_id(self, place_id: str):
        self.__place_id = place_id

    @property
    def wifi(self):
        return self.__wifi
    @wifi.setter
    def wifi(self, wifi: str):
        self.__wifi = wifi

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def plugs(self):
        return self.__plugs
    @plugs.setter
    def plugs(self, plugs: str):
        self.__plugs = plugs

