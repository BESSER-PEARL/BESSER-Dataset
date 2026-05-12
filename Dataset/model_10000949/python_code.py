from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Search_pet_accessories_UseCase:

    pass


class Create_new_administrators_UseCase:

    pass


class Logging_into_program_UseCase:

    pass


class Register_pets__physical_characteristics_UseCase:

    pass


class Make_requests_to_administrator_UseCase:

    pass


class Register_pet_types_UseCase:

    pass


class Send_mail_to_lost_pet_owners_UseCase:

    pass


class Match_lost_pet_cases_UseCase:

    pass


class Create_reports_UseCase:

    pass


class System_Actor:

    pass


class Check_black_list_requests_UseCase:

    pass


class Search_pet_s_UseCase:

    pass


class Register_as_a_pro_care_association_UseCase:

    pass


class Edit_pet_information_UseCase:

    pass


class Edit_user_information_UseCase:

    pass


class Edit_information_UseCase:

    pass


class Register_a_pet_UseCase:

    pass


class Report_a_person_to_the_blacklist_UseCase:

    pass


class Register_as_an_adopter_UseCase:

    pass


class Registering_UseCase:

    pass


class Search_UseCase:

    pass


class Logging_into_web_UseCase:

    pass


class Administrator_Actor:

    pass


class User_Actor:

    pass





class Medeina:

    def __init__(self, attribute: str, blackList_User_: User):
        self.attribute = attribute
        self.blackList_User_ = blackList_User_
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def blackList_User_(self):
        return self.__blackList_User_
    @blackList_User_.setter
    def blackList_User_(self, blackList_User_: User):
        self.__blackList_User_ = blackList_User_



class Organization:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name



class User:

    def __init__(self, name: str, lastName: str):
        self.name = name
        self.lastName = lastName
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def lastName(self):
        return self.__lastName
    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName



class Pet:

    def __init__(self, type: str, breed: str, name: str, chipID: str, color: str, picture: str, phone: str, email: str, stray: bool, place: str, date: date, reward: int, notes: str, state: str):
        self.type = type
        self.breed = breed
        self.name = name
        self.chipID = chipID
        self.color = color
        self.picture = picture
        self.phone = phone
        self.email = email
        self.stray = stray
        self.place = place
        self.date = date
        self.reward = reward
        self.notes = notes
        self.state = state
        
        pass
    @property
    def chipID(self):
        return self.__chipID
    @chipID.setter
    def chipID(self, chipID: str):
        self.__chipID = chipID

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def picture(self):
        return self.__picture
    @picture.setter
    def picture(self, picture: str):
        self.__picture = picture

    @property
    def notes(self):
        return self.__notes
    @notes.setter
    def notes(self, notes: str):
        self.__notes = notes

    @property
    def stray(self):
        return self.__stray
    @stray.setter
    def stray(self, stray: bool):
        self.__stray = stray

    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def place(self):
        return self.__place
    @place.setter
    def place(self, place: str):
        self.__place = place

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def reward(self):
        return self.__reward
    @reward.setter
    def reward(self, reward: int):
        self.__reward = reward

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def breed(self):
        return self.__breed
    @breed.setter
    def breed(self, breed: str):
        self.__breed = breed

