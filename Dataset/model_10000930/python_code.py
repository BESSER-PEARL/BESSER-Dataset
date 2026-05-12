from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Mail:

    def __init__(self, emailID: str, sendTo: str, sendBy: str, subject: str, superAdmin7: "SuperAdmin" = None, admin9: "Admin" = None):
        self.emailID = emailID
        self.sendTo = sendTo
        self.sendBy = sendBy
        self.subject = subject
        self.superAdmin7 = superAdmin7
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
    def subject(self):
        return self.__subject
    @subject.setter
    def subject(self, subject: str):
        self.__subject = subject

    @property
    def emailID(self):
        return self.__emailID
    @emailID.setter
    def emailID(self, emailID: str):
        self.__emailID = emailID

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

    @property
    def superAdmin7(self):
        return self.__superAdmin7
    @superAdmin7.setter
    def superAdmin7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Mail__superAdmin7", None)
        self.__superAdmin7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mail6"):
                opp_val = getattr(old_value, "mail6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mail6"):
                opp_val = getattr(value, "mail6", None)
                if opp_val is None:
                    setattr(value, "mail6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Payment:

    def __init__(self, amount: int, cardType: str, cardNumber: int, issuerName: str, expiryDate: str, superAdmin1: set["SuperAdmin"] = None, volunteer3: set["Volunteer"] = None, admin5: set["Admin"] = None):
        self.amount = amount
        self.cardType = cardType
        self.cardNumber = cardNumber
        self.issuerName = issuerName
        self.expiryDate = expiryDate
        self.superAdmin1 = superAdmin1 if superAdmin1 is not None else set()
        self.volunteer3 = volunteer3 if volunteer3 is not None else set()
        self.admin5 = admin5 if admin5 is not None else set()
        
        pass
    @property
    def issuerName(self):
        return self.__issuerName
    @issuerName.setter
    def issuerName(self, issuerName: str):
        self.__issuerName = issuerName

    @property
    def expiryDate(self):
        return self.__expiryDate
    @expiryDate.setter
    def expiryDate(self, expiryDate: str):
        self.__expiryDate = expiryDate

    @property
    def cardNumber(self):
        return self.__cardNumber
    @cardNumber.setter
    def cardNumber(self, cardNumber: int):
        self.__cardNumber = cardNumber

    @property
    def cardType(self):
        return self.__cardType
    @cardType.setter
    def cardType(self, cardType: str):
        self.__cardType = cardType

    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: int):
        self.__amount = amount

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



class Volunteer:

    def __init__(self, userID: int, userName: str, password: str, payment2: "Payment" = None):
        self.userID = userID
        self.userName = userName
        self.password = password
        self.payment2 = payment2
        
        pass
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
    def userName(self):
        return self.__userName
    @userName.setter
    def userName(self, userName: str):
        self.__userName = userName

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



class void:

    pass


class SuperAdmin:

    def __init__(self, userID: int, userName: str, password: str, payment0: "Payment" = None, mail6: set["Mail"] = None):
        self.userID = userID
        self.userName = userName
        self.password = password
        self.payment0 = payment0
        self.mail6 = mail6 if mail6 is not None else set()
        
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
    def mail6(self):
        return self.__mail6
    @mail6.setter
    def mail6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SuperAdmin__mail6", None)
        self.__mail6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "superAdmin7"):
                    opp_val = getattr(item, "superAdmin7", None)
                    
                    if opp_val == self:
                        setattr(item, "superAdmin7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "superAdmin7"):
                    opp_val = getattr(item, "superAdmin7", None)
                    
                    setattr(item, "superAdmin7", self)
                    

    @property
    def payment0(self):
        return self.__payment0
    @payment0.setter
    def payment0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SuperAdmin__payment0", None)
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



class Profile:

    def __init__(self, l_Name: str, user_Name: str, password: str, f_Name: str):
        self.l_Name = l_Name
        self.user_Name = user_Name
        self.password = password
        self.f_Name = f_Name
        
        pass
    @property
    def f_Name(self):
        return self.__f_Name
    @f_Name.setter
    def f_Name(self, f_Name: str):
        self.__f_Name = f_Name

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

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

