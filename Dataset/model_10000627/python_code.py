from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class HomePage:

    def __init__(self, __status: str, __friendStatus: str, likeorunlike: bool, user3: "User" = None):
        self.__status = __status
        self.__friendStatus = __friendStatus
        self.likeorunlike = likeorunlike
        self.user3 = user3
        
        pass
    @property
    def __status(self):
        return self.____status
    @__status.setter
    def __status(self, __status: str):
        self.____status = __status

    @property
    def likeorunlike(self):
        return self.__likeorunlike
    @likeorunlike.setter
    def likeorunlike(self, likeorunlike: bool):
        self.__likeorunlike = likeorunlike

    @property
    def __friendStatus(self):
        return self.____friendStatus
    @__friendStatus.setter
    def __friendStatus(self, __friendStatus: str):
        self.____friendStatus = __friendStatus

    @property
    def user3(self):
        return self.__user3
    @user3.setter
    def user3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HomePage__user3", None)
        self.__user3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "homePage2"):
                opp_val = getattr(old_value, "homePage2", None)
                if opp_val == self:
                    setattr(old_value, "homePage2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "homePage2"):
                opp_val = getattr(value, "homePage2", None)
                setattr(value, "homePage2", self)



class Photos:

    def __init__(self, __photos: str, user7: "User" = None):
        self.__photos = __photos
        self.user7 = user7
        
        pass
    @property
    def __photos(self):
        return self.____photos
    @__photos.setter
    def __photos(self, __photos: str):
        self.____photos = __photos

    @property
    def user7(self):
        return self.__user7
    @user7.setter
    def user7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Photos__user7", None)
        self.__user7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "photos6"):
                opp_val = getattr(old_value, "photos6", None)
                if opp_val == self:
                    setattr(old_value, "photos6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "photos6"):
                opp_val = getattr(value, "photos6", None)
                setattr(value, "photos6", self)



class Message:

    def __init__(self, sender: str, message: str, reciver: str, user5: "User" = None):
        self.sender = sender
        self.message = message
        self.reciver = reciver
        self.user5 = user5
        
        pass
    @property
    def message(self):
        return self.__message
    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def sender(self):
        return self.__sender
    @sender.setter
    def sender(self, sender: str):
        self.__sender = sender

    @property
    def reciver(self):
        return self.__reciver
    @reciver.setter
    def reciver(self, reciver: str):
        self.__reciver = reciver

    @property
    def user5(self):
        return self.__user5
    @user5.setter
    def user5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Message__user5", None)
        self.__user5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "message4"):
                opp_val = getattr(old_value, "message4", None)
                if opp_val == self:
                    setattr(old_value, "message4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "message4"):
                opp_val = getattr(value, "message4", None)
                setattr(value, "message4", self)



class Friend:

    def __init__(self, friend____: str, acceptornot: bool, user1: "User" = None):
        self.friend____ = friend____
        self.acceptornot = acceptornot
        self.user1 = user1
        
        pass
    @property
    def friend____(self):
        return self.__friend____
    @friend____.setter
    def friend____(self, friend____: str):
        self.__friend____ = friend____

    @property
    def acceptornot(self):
        return self.__acceptornot
    @acceptornot.setter
    def acceptornot(self, acceptornot: bool):
        self.__acceptornot = acceptornot

    @property
    def user1(self):
        return self.__user1
    @user1.setter
    def user1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Friend__user1", None)
        self.__user1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "friend0"):
                opp_val = getattr(old_value, "friend0", None)
                if opp_val == self:
                    setattr(old_value, "friend0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "friend0"):
                opp_val = getattr(value, "friend0", None)
                setattr(value, "friend0", self)



class User:

    def __init__(self, _F: Friend, __M: Message, _P: Photos, message4: "Message" = None, photos6: "Photos" = None, friend0: "Friend" = None, homePage2: "HomePage" = None):
        self._F = _F
        self.__M = __M
        self._P = _P
        self.message4 = message4
        self.photos6 = photos6
        self.friend0 = friend0
        self.homePage2 = homePage2
        
        pass
    @property
    def __M(self):
        return self.____M
    @__M.setter
    def __M(self, __M: Message):
        self.____M = __M

    @property
    def _F(self):
        return self.___F
    @_F.setter
    def _F(self, _F: Friend):
        self.___F = _F

    @property
    def _P(self):
        return self.___P
    @_P.setter
    def _P(self, _P: Photos):
        self.___P = _P

    @property
    def friend0(self):
        return self.__friend0
    @friend0.setter
    def friend0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__friend0", None)
        self.__friend0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user1"):
                opp_val = getattr(old_value, "user1", None)
                if opp_val == self:
                    setattr(old_value, "user1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user1"):
                opp_val = getattr(value, "user1", None)
                setattr(value, "user1", self)

    @property
    def homePage2(self):
        return self.__homePage2
    @homePage2.setter
    def homePage2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__homePage2", None)
        self.__homePage2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user3"):
                opp_val = getattr(old_value, "user3", None)
                if opp_val == self:
                    setattr(old_value, "user3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user3"):
                opp_val = getattr(value, "user3", None)
                setattr(value, "user3", self)

    @property
    def message4(self):
        return self.__message4
    @message4.setter
    def message4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__message4", None)
        self.__message4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user5"):
                opp_val = getattr(old_value, "user5", None)
                if opp_val == self:
                    setattr(old_value, "user5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user5"):
                opp_val = getattr(value, "user5", None)
                setattr(value, "user5", self)

    @property
    def photos6(self):
        return self.__photos6
    @photos6.setter
    def photos6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__photos6", None)
        self.__photos6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user7"):
                opp_val = getattr(old_value, "user7", None)
                if opp_val == self:
                    setattr(old_value, "user7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user7"):
                opp_val = getattr(value, "user7", None)
                setattr(value, "user7", self)



class Account:

    def __init__(self, name: str, email: str, password: str, entity: str):
        self.name = name
        self.email = email
        self.password = password
        self.entity = entity
        
        pass
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def entity(self):
        return self.__entity
    @entity.setter
    def entity(self, entity: str):
        self.__entity = entity

