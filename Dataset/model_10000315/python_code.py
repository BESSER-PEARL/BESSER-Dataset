from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Alumni:

    def __init__(self, _F: Friend, __M: Message, Report: Message, homePage6: "HomePage" = None, message8: "Message" = None, account11: "Account" = None, admin16: "Admin" = None):
        self._F = _F
        self.__M = __M
        self.Report = Report
        self.homePage6 = homePage6
        self.message8 = message8
        self.account11 = account11
        self.admin16 = admin16
        
        pass
    @property
    def Report(self):
        return self.__Report
    @Report.setter
    def Report(self, Report: Message):
        self.__Report = Report

    @property
    def _F(self):
        return self.___F
    @_F.setter
    def _F(self, _F: Friend):
        self.___F = _F

    @property
    def __M(self):
        return self.____M
    @__M.setter
    def __M(self, __M: Message):
        self.____M = __M

    @property
    def homePage6(self):
        return self.__homePage6
    @homePage6.setter
    def homePage6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Alumni__homePage6", None)
        self.__homePage6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alumni7"):
                opp_val = getattr(old_value, "alumni7", None)
                if opp_val == self:
                    setattr(old_value, "alumni7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alumni7"):
                opp_val = getattr(value, "alumni7", None)
                setattr(value, "alumni7", self)

    @property
    def message8(self):
        return self.__message8
    @message8.setter
    def message8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Alumni__message8", None)
        self.__message8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alumni9"):
                opp_val = getattr(old_value, "alumni9", None)
                if opp_val == self:
                    setattr(old_value, "alumni9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alumni9"):
                opp_val = getattr(value, "alumni9", None)
                setattr(value, "alumni9", self)

    @property
    def admin16(self):
        return self.__admin16
    @admin16.setter
    def admin16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Alumni__admin16", None)
        self.__admin16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alumni17"):
                opp_val = getattr(old_value, "alumni17", None)
                if opp_val == self:
                    setattr(old_value, "alumni17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alumni17"):
                opp_val = getattr(value, "alumni17", None)
                setattr(value, "alumni17", self)

    @property
    def account11(self):
        return self.__account11
    @account11.setter
    def account11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Alumni__account11", None)
        self.__account11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alumni10"):
                opp_val = getattr(old_value, "alumni10", None)
                if opp_val == self:
                    setattr(old_value, "alumni10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alumni10"):
                opp_val = getattr(value, "alumni10", None)
                setattr(value, "alumni10", self)



class Admin:

    pass


class HomePage:

    def __init__(self, __friendpost: HomePage, user3: "Student" = None, alumni7: "Alumni" = None, admin18: "Admin" = None):
        self.__friendpost = __friendpost
        self.user3 = user3
        self.alumni7 = alumni7
        self.admin18 = admin18
        
        pass
    @property
    def __friendpost(self):
        return self.____friendpost
    @__friendpost.setter
    def __friendpost(self, __friendpost: HomePage):
        self.____friendpost = __friendpost

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

    @property
    def alumni7(self):
        return self.__alumni7
    @alumni7.setter
    def alumni7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HomePage__alumni7", None)
        self.__alumni7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "homePage6"):
                opp_val = getattr(old_value, "homePage6", None)
                if opp_val == self:
                    setattr(old_value, "homePage6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "homePage6"):
                opp_val = getattr(value, "homePage6", None)
                setattr(value, "homePage6", self)

    @property
    def admin18(self):
        return self.__admin18
    @admin18.setter
    def admin18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HomePage__admin18", None)
        self.__admin18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "homePage19"):
                opp_val = getattr(old_value, "homePage19", None)
                if opp_val == self:
                    setattr(old_value, "homePage19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "homePage19"):
                opp_val = getattr(value, "homePage19", None)
                setattr(value, "homePage19", self)



class Message:

    def __init__(self, sender: str, message: str, reciver: str, user5: "Student" = None, alumni9: "Alumni" = None, admin20: "Admin" = None):
        self.sender = sender
        self.message = message
        self.reciver = reciver
        self.user5 = user5
        self.alumni9 = alumni9
        self.admin20 = admin20
        
        pass
    @property
    def sender(self):
        return self.__sender
    @sender.setter
    def sender(self, sender: str):
        self.__sender = sender

    @property
    def message(self):
        return self.__message
    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def reciver(self):
        return self.__reciver
    @reciver.setter
    def reciver(self, reciver: str):
        self.__reciver = reciver

    @property
    def alumni9(self):
        return self.__alumni9
    @alumni9.setter
    def alumni9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Message__alumni9", None)
        self.__alumni9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "message8"):
                opp_val = getattr(old_value, "message8", None)
                if opp_val == self:
                    setattr(old_value, "message8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "message8"):
                opp_val = getattr(value, "message8", None)
                setattr(value, "message8", self)

    @property
    def admin20(self):
        return self.__admin20
    @admin20.setter
    def admin20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Message__admin20", None)
        self.__admin20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "message21"):
                opp_val = getattr(old_value, "message21", None)
                if opp_val == self:
                    setattr(old_value, "message21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "message21"):
                opp_val = getattr(value, "message21", None)
                setattr(value, "message21", self)

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

    def __init__(self, friend____: str, acceptornot: bool, user1: "Student" = None):
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



class Student:

    def __init__(self, _F: Friend, __M: Message, Report: Message, friend0: "Friend" = None, homePage2: "HomePage" = None, message4: "Message" = None, admin12: "Admin" = None):
        self._F = _F
        self.__M = __M
        self.Report = Report
        self.friend0 = friend0
        self.homePage2 = homePage2
        self.message4 = message4
        self.admin12 = admin12
        
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
    def Report(self):
        return self.__Report
    @Report.setter
    def Report(self, Report: Message):
        self.__Report = Report

    @property
    def admin12(self):
        return self.__admin12
    @admin12.setter
    def admin12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Student__admin12", None)
        self.__admin12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "student13"):
                opp_val = getattr(old_value, "student13", None)
                if opp_val == self:
                    setattr(old_value, "student13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "student13"):
                opp_val = getattr(value, "student13", None)
                setattr(value, "student13", self)

    @property
    def friend0(self):
        return self.__friend0
    @friend0.setter
    def friend0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Student__friend0", None)
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
        old_value = getattr(self, f"_Student__homePage2", None)
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
        old_value = getattr(self, f"_Student__message4", None)
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



class Account:

    def __init__(self, name: str, email: str, password: str, Department: str, class1: str, Branch: str, alumni10: "Alumni" = None, admin14: "Admin" = None):
        self.name = name
        self.email = email
        self.password = password
        self.Department = Department
        self.class1 = class1
        self.Branch = Branch
        self.alumni10 = alumni10
        self.admin14 = admin14
        
        pass
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def class1(self):
        return self.__class1
    @class1.setter
    def class1(self, class1: str):
        self.__class = class1

    @property
    def Department(self):
        return self.__Department
    @Department.setter
    def Department(self, Department: str):
        self.__Department = Department

    @property
    def Branch(self):
        return self.__Branch
    @Branch.setter
    def Branch(self, Branch: str):
        self.__Branch = Branch

    @property
    def alumni10(self):
        return self.__alumni10
    @alumni10.setter
    def alumni10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__alumni10", None)
        self.__alumni10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account11"):
                opp_val = getattr(old_value, "account11", None)
                if opp_val == self:
                    setattr(old_value, "account11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account11"):
                opp_val = getattr(value, "account11", None)
                setattr(value, "account11", self)

    @property
    def admin14(self):
        return self.__admin14
    @admin14.setter
    def admin14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__admin14", None)
        self.__admin14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account15"):
                opp_val = getattr(old_value, "account15", None)
                if opp_val == self:
                    setattr(old_value, "account15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account15"):
                opp_val = getattr(value, "account15", None)
                setattr(value, "account15", self)

