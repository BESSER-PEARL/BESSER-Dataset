from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Profile:

    def __init__(self, f_Name: str, l_Name: str, user_Name: str, password: str):
        self.f_Name = f_Name
        self.l_Name = l_Name
        self.user_Name = user_Name
        self.password = password
        
        pass
    @property
    def f_Name(self):
        return self.__f_Name
    @f_Name.setter
    def f_Name(self, f_Name: str):
        self.__f_Name = f_Name

    @property
    def user_Name(self):
        return self.__user_Name
    @user_Name.setter
    def user_Name(self, user_Name: str):
        self.__user_Name = user_Name

    @property
    def l_Name(self):
        return self.__l_Name
    @l_Name.setter
    def l_Name(self, l_Name: str):
        self.__l_Name = l_Name

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password



class Mail:

    def __init__(self, emailID: str, sendTo: str, sendBy: str, subject: str, admin9: "Admin" = None):
        self.emailID = emailID
        self.sendTo = sendTo
        self.sendBy = sendBy
        self.subject = subject
        self.admin9 = admin9
        
        pass
    @property
    def sendTo(self):
        return self.__sendTo
    @sendTo.setter
    def sendTo(self, sendTo: str):
        self.__sendTo = sendTo

    @property
    def sendBy(self):
        return self.__sendBy
    @sendBy.setter
    def sendBy(self, sendBy: str):
        self.__sendBy = sendBy

    @property
    def emailID(self):
        return self.__emailID
    @emailID.setter
    def emailID(self, emailID: str):
        self.__emailID = emailID

    @property
    def subject(self):
        return self.__subject
    @subject.setter
    def subject(self, subject: str):
        self.__subject = subject

    @property
    def admin9(self):
        return self.__admin9
    @admin9.setter
    def admin9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Mail__admin9", None)
        self.__admin9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mail8"):
                opp_val = getattr(old_value, "mail8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mail8"):
                opp_val = getattr(value, "mail8", None)
                if opp_val is None:
                    setattr(value, "mail8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Payment:

    def __init__(self, amount: int, cardType: str, cardNumber: int, issuerName: str, expiryDate: str, superAdmin1: set["Manager"] = None, volunteer3: set["Volunteer"] = None, admin5: set["Admin"] = None, normal_user7: set["Normal_user"] = None):
        self.amount = amount
        self.cardType = cardType
        self.cardNumber = cardNumber
        self.issuerName = issuerName
        self.expiryDate = expiryDate
        self.superAdmin1 = superAdmin1 if superAdmin1 is not None else set()
        self.volunteer3 = volunteer3 if volunteer3 is not None else set()
        self.admin5 = admin5 if admin5 is not None else set()
        self.normal_user7 = normal_user7 if normal_user7 is not None else set()
        
        pass
    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: int):
        self.__amount = amount

    @property
    def cardType(self):
        return self.__cardType
    @cardType.setter
    def cardType(self, cardType: str):
        self.__cardType = cardType

    @property
    def expiryDate(self):
        return self.__expiryDate
    @expiryDate.setter
    def expiryDate(self, expiryDate: str):
        self.__expiryDate = expiryDate

    @property
    def issuerName(self):
        return self.__issuerName
    @issuerName.setter
    def issuerName(self, issuerName: str):
        self.__issuerName = issuerName

    @property
    def cardNumber(self):
        return self.__cardNumber
    @cardNumber.setter
    def cardNumber(self, cardNumber: int):
        self.__cardNumber = cardNumber

    @property
    def superAdmin1(self):
        return self.__superAdmin1
    @superAdmin1.setter
    def superAdmin1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__superAdmin1", None)
        self.__superAdmin1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "payment0"):
                    opp_val = getattr(item, "payment0", None)
                    
                    if opp_val == self:
                        setattr(item, "payment0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "payment0"):
                    opp_val = getattr(item, "payment0", None)
                    
                    setattr(item, "payment0", self)
                    

    @property
    def admin5(self):
        return self.__admin5
    @admin5.setter
    def admin5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__admin5", None)
        self.__admin5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "payment4"):
                    opp_val = getattr(item, "payment4", None)
                    
                    if opp_val == self:
                        setattr(item, "payment4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "payment4"):
                    opp_val = getattr(item, "payment4", None)
                    
                    setattr(item, "payment4", self)
                    

    @property
    def normal_user7(self):
        return self.__normal_user7
    @normal_user7.setter
    def normal_user7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__normal_user7", None)
        self.__normal_user7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "payment26"):
                    opp_val = getattr(item, "payment26", None)
                    
                    if opp_val == self:
                        setattr(item, "payment26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "payment26"):
                    opp_val = getattr(item, "payment26", None)
                    
                    setattr(item, "payment26", self)
                    

    @property
    def volunteer3(self):
        return self.__volunteer3
    @volunteer3.setter
    def volunteer3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__volunteer3", None)
        self.__volunteer3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "payment2"):
                    opp_val = getattr(item, "payment2", None)
                    
                    if opp_val == self:
                        setattr(item, "payment2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "payment2"):
                    opp_val = getattr(item, "payment2", None)
                    
                    setattr(item, "payment2", self)
                    



class Logout:

    pass


class Login:

    def __init__(self, userID: Profile, loggedinTime: str, loggedoutTime: str):
        self.userID = userID
        self.loggedinTime = loggedinTime
        self.loggedoutTime = loggedoutTime
        
        pass
    @property
    def userID(self):
        return self.__userID
    @userID.setter
    def userID(self, userID: Profile):
        self.__userID = userID

    @property
    def loggedoutTime(self):
        return self.__loggedoutTime
    @loggedoutTime.setter
    def loggedoutTime(self, loggedoutTime: str):
        self.__loggedoutTime = loggedoutTime

    @property
    def loggedinTime(self):
        return self.__loggedinTime
    @loggedinTime.setter
    def loggedinTime(self, loggedinTime: str):
        self.__loggedinTime = loggedinTime



class Calender_Event:

    def __init__(self, category: str, date: str, time: str, description: str, eventType: str, participantAmount: str, volunteer: Volunteer, nomarlUser: Normal_user, admin: Admin):
        self.category = category
        self.date = date
        self.time = time
        self.description = description
        self.eventType = eventType
        self.participantAmount = participantAmount
        self.volunteer = volunteer
        self.nomarlUser = nomarlUser
        self.admin = admin
        
        pass
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def admin(self):
        return self.__admin
    @admin.setter
    def admin(self, admin: Admin):
        self.__admin = admin

    @property
    def nomarlUser(self):
        return self.__nomarlUser
    @nomarlUser.setter
    def nomarlUser(self, nomarlUser: Normal_user):
        self.__nomarlUser = nomarlUser

    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: str):
        self.__time = time

    @property
    def eventType(self):
        return self.__eventType
    @eventType.setter
    def eventType(self, eventType: str):
        self.__eventType = eventType

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def participantAmount(self):
        return self.__participantAmount
    @participantAmount.setter
    def participantAmount(self, participantAmount: str):
        self.__participantAmount = participantAmount

    @property
    def volunteer(self):
        return self.__volunteer
    @volunteer.setter
    def volunteer(self, volunteer: Volunteer):
        self.__volunteer = volunteer

    @property
    def category(self):
        return self.__category
    @category.setter
    def category(self, category: str):
        self.__category = category



class Volunteer:

    def __init__(self, userID: int, userName: str, password: str, payment2: "Payment" = None):
        self.userID = userID
        self.userName = userName
        self.password = password
        self.payment2 = payment2
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def userName(self):
        return self.__userName
    @userName.setter
    def userName(self, userName: str):
        self.__userName = userName

    @property
    def userID(self):
        return self.__userID
    @userID.setter
    def userID(self, userID: int):
        self.__userID = userID

    @property
    def payment2(self):
        return self.__payment2
    @payment2.setter
    def payment2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Volunteer__payment2", None)
        self.__payment2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "volunteer3"):
                opp_val = getattr(old_value, "volunteer3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "volunteer3"):
                opp_val = getattr(value, "volunteer3", None)
                if opp_val is None:
                    setattr(value, "volunteer3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Admin:

    def __init__(self, userID: int, userName: str, password: str, payment4: "Payment" = None, mail8: set["Mail"] = None):
        self.userID = userID
        self.userName = userName
        self.password = password
        self.payment4 = payment4
        self.mail8 = mail8 if mail8 is not None else set()
        
        pass
    @property
    def userID(self):
        return self.__userID
    @userID.setter
    def userID(self, userID: int):
        self.__userID = userID

    @property
    def userName(self):
        return self.__userName
    @userName.setter
    def userName(self, userName: str):
        self.__userName = userName

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def mail8(self):
        return self.__mail8
    @mail8.setter
    def mail8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__mail8", None)
        self.__mail8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "admin9"):
                    opp_val = getattr(item, "admin9", None)
                    
                    if opp_val == self:
                        setattr(item, "admin9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "admin9"):
                    opp_val = getattr(item, "admin9", None)
                    
                    setattr(item, "admin9", self)
                    

    @property
    def payment4(self):
        return self.__payment4
    @payment4.setter
    def payment4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__payment4", None)
        self.__payment4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "admin5"):
                opp_val = getattr(old_value, "admin5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "admin5"):
                opp_val = getattr(value, "admin5", None)
                if opp_val is None:
                    setattr(value, "admin5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Normal_user:

    def __init__(self, userID: int, userName: str, password: str, payment26: "Payment" = None):
        self.userID = userID
        self.userName = userName
        self.password = password
        self.payment26 = payment26
        
        pass
    @property
    def userName(self):
        return self.__userName
    @userName.setter
    def userName(self, userName: str):
        self.__userName = userName

    @property
    def userID(self):
        return self.__userID
    @userID.setter
    def userID(self, userID: int):
        self.__userID = userID

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def payment26(self):
        return self.__payment26
    @payment26.setter
    def payment26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Normal_user__payment26", None)
        self.__payment26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "normal_user7"):
                opp_val = getattr(old_value, "normal_user7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "normal_user7"):
                opp_val = getattr(value, "normal_user7", None)
                if opp_val is None:
                    setattr(value, "normal_user7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class void:

    pass


class Manager:

    def __init__(self, userID: int, userName: str, password: str, payment0: "Payment" = None):
        self.userID = userID
        self.userName = userName
        self.password = password
        self.payment0 = payment0
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def userName(self):
        return self.__userName
    @userName.setter
    def userName(self, userName: str):
        self.__userName = userName

    @property
    def userID(self):
        return self.__userID
    @userID.setter
    def userID(self, userID: int):
        self.__userID = userID

    @property
    def payment0(self):
        return self.__payment0
    @payment0.setter
    def payment0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Manager__payment0", None)
        self.__payment0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "superAdmin1"):
                opp_val = getattr(old_value, "superAdmin1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "superAdmin1"):
                opp_val = getattr(value, "superAdmin1", None)
                if opp_val is None:
                    setattr(value, "superAdmin1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

