from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Volunteer_Forms:

    def __init__(self, userID: int, userName: str, password: str):
        self.userID = userID
        self.userName = userName
        self.password = password
        
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



class Mail:

    def __init__(self, emailID: str, sendTo: str, sendBy: str, subject: str, superAdmin19: "Executive_Director" = None, admin21: "Admin" = None):
        self.emailID = emailID
        self.sendTo = sendTo
        self.sendBy = sendBy
        self.subject = subject
        self.superAdmin19 = superAdmin19
        self.admin21 = admin21
        
        pass
    @property
    def sendTo(self):
        return self.__sendTo
    @sendTo.setter
    def sendTo(self, sendTo: str):
        self.__sendTo = sendTo

    @property
    def emailID(self):
        return self.__emailID
    @emailID.setter
    def emailID(self, emailID: str):
        self.__emailID = emailID

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
    def admin21(self):
        return self.__admin21
    @admin21.setter
    def admin21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Mail__admin21", None)
        self.__admin21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mail20"):
                opp_val = getattr(old_value, "mail20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mail20"):
                opp_val = getattr(value, "mail20", None)
                if opp_val is None:
                    setattr(value, "mail20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def superAdmin19(self):
        return self.__superAdmin19
    @superAdmin19.setter
    def superAdmin19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Mail__superAdmin19", None)
        self.__superAdmin19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mail18"):
                opp_val = getattr(old_value, "mail18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mail18"):
                opp_val = getattr(value, "mail18", None)
                if opp_val is None:
                    setattr(value, "mail18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Donations:

    def __init__(self, amount: int, cardType: str, cardNumber: int, issuerName: str, expirationDate: int, superAdmin11: set["Executive_Director"] = None, volunteer13: set["Volunteer"] = None, admin15: set["Admin"] = None, normal_user17: set["Normal_user"] = None):
        self.amount = amount
        self.cardType = cardType
        self.cardNumber = cardNumber
        self.issuerName = issuerName
        self.expirationDate = expirationDate
        self.superAdmin11 = superAdmin11 if superAdmin11 is not None else set()
        self.volunteer13 = volunteer13 if volunteer13 is not None else set()
        self.admin15 = admin15 if admin15 is not None else set()
        self.normal_user17 = normal_user17 if normal_user17 is not None else set()
        
        pass
    @property
    def cardType(self):
        return self.__cardType
    @cardType.setter
    def cardType(self, cardType: str):
        self.__cardType = cardType

    @property
    def issuerName(self):
        return self.__issuerName
    @issuerName.setter
    def issuerName(self, issuerName: str):
        self.__issuerName = issuerName

    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: int):
        self.__amount = amount

    @property
    def expirationDate(self):
        return self.__expirationDate
    @expirationDate.setter
    def expirationDate(self, expirationDate: int):
        self.__expirationDate = expirationDate

    @property
    def cardNumber(self):
        return self.__cardNumber
    @cardNumber.setter
    def cardNumber(self, cardNumber: int):
        self.__cardNumber = cardNumber

    @property
    def superAdmin11(self):
        return self.__superAdmin11
    @superAdmin11.setter
    def superAdmin11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Donations__superAdmin11", None)
        self.__superAdmin11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "payment10"):
                    opp_val = getattr(item, "payment10", None)
                    
                    if opp_val == self:
                        setattr(item, "payment10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "payment10"):
                    opp_val = getattr(item, "payment10", None)
                    
                    setattr(item, "payment10", self)
                    

    @property
    def volunteer13(self):
        return self.__volunteer13
    @volunteer13.setter
    def volunteer13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Donations__volunteer13", None)
        self.__volunteer13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "payment12"):
                    opp_val = getattr(item, "payment12", None)
                    
                    if opp_val == self:
                        setattr(item, "payment12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "payment12"):
                    opp_val = getattr(item, "payment12", None)
                    
                    setattr(item, "payment12", self)
                    

    @property
    def admin15(self):
        return self.__admin15
    @admin15.setter
    def admin15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Donations__admin15", None)
        self.__admin15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "donation14"):
                    opp_val = getattr(item, "donation14", None)
                    
                    if opp_val == self:
                        setattr(item, "donation14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "donation14"):
                    opp_val = getattr(item, "donation14", None)
                    
                    setattr(item, "donation14", self)
                    

    @property
    def normal_user17(self):
        return self.__normal_user17
    @normal_user17.setter
    def normal_user17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Donations__normal_user17", None)
        self.__normal_user17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "donation216"):
                    opp_val = getattr(item, "donation216", None)
                    
                    if opp_val == self:
                        setattr(item, "donation216", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "donation216"):
                    opp_val = getattr(item, "donation216", None)
                    
                    setattr(item, "donation216", self)
                    



class Logout:

    pass


class Attendance:

    def __init__(self, attendanceID: int, checkInTime: str, checkOutTime: str, profile9: "Profile" = None):
        self.attendanceID = attendanceID
        self.checkInTime = checkInTime
        self.checkOutTime = checkOutTime
        self.profile9 = profile9
        
        pass
    @property
    def checkInTime(self):
        return self.__checkInTime
    @checkInTime.setter
    def checkInTime(self, checkInTime: str):
        self.__checkInTime = checkInTime

    @property
    def attendanceID(self):
        return self.__attendanceID
    @attendanceID.setter
    def attendanceID(self, attendanceID: int):
        self.__attendanceID = attendanceID

    @property
    def checkOutTime(self):
        return self.__checkOutTime
    @checkOutTime.setter
    def checkOutTime(self, checkOutTime: str):
        self.__checkOutTime = checkOutTime

    @property
    def profile9(self):
        return self.__profile9
    @profile9.setter
    def profile9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Attendance__profile9", None)
        self.__profile9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Track_Attendance8"):
                opp_val = getattr(old_value, "Track_Attendance8", None)
                if opp_val == self:
                    setattr(old_value, "Track_Attendance8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Track_Attendance8"):
                opp_val = getattr(value, "Track_Attendance8", None)
                setattr(value, "Track_Attendance8", self)



class System_Login:

    def __init__(self, userID: Profile, loggedinTime: str, loggedoutTime: str):
        self.userID = userID
        self.loggedinTime = loggedinTime
        self.loggedoutTime = loggedoutTime
        
        pass
    @property
    def loggedinTime(self):
        return self.__loggedinTime
    @loggedinTime.setter
    def loggedinTime(self, loggedinTime: str):
        self.__loggedinTime = loggedinTime

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



class Calender_Event:

    def __init__(self, category: str, date: str, time: str, description: str, eventType: str, participantAmount: str, volunteer: Volunteer, nomarlUser: Normal_user, admin: Admin, Add_Edit_View1: set["Volunteer"] = None, Add_Edit_View3: set["Admin"] = None, Add_Edit_View5: "Normal_user" = None, Add_Edit_Vew7: set["Executive_Director"] = None):
        self.category = category
        self.date = date
        self.time = time
        self.description = description
        self.eventType = eventType
        self.participantAmount = participantAmount
        self.volunteer = volunteer
        self.nomarlUser = nomarlUser
        self.admin = admin
        self.Add_Edit_View1 = Add_Edit_View1 if Add_Edit_View1 is not None else set()
        self.Add_Edit_View3 = Add_Edit_View3 if Add_Edit_View3 is not None else set()
        self.Add_Edit_View5 = Add_Edit_View5
        self.Add_Edit_Vew7 = Add_Edit_Vew7 if Add_Edit_Vew7 is not None else set()
        
        pass
    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: str):
        self.__time = time

    @property
    def admin(self):
        return self.__admin
    @admin.setter
    def admin(self, admin: Admin):
        self.__admin = admin

    @property
    def category(self):
        return self.__category
    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def eventType(self):
        return self.__eventType
    @eventType.setter
    def eventType(self, eventType: str):
        self.__eventType = eventType

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def volunteer(self):
        return self.__volunteer
    @volunteer.setter
    def volunteer(self, volunteer: Volunteer):
        self.__volunteer = volunteer

    @property
    def participantAmount(self):
        return self.__participantAmount
    @participantAmount.setter
    def participantAmount(self, participantAmount: str):
        self.__participantAmount = participantAmount

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def nomarlUser(self):
        return self.__nomarlUser
    @nomarlUser.setter
    def nomarlUser(self, nomarlUser: Normal_user):
        self.__nomarlUser = nomarlUser

    @property
    def Add_Edit_Vew7(self):
        return self.__Add_Edit_Vew7
    @Add_Edit_Vew7.setter
    def Add_Edit_Vew7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Calender_Event__Add_Edit_Vew7", None)
        self.__Add_Edit_Vew7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "calender_Event6"):
                    opp_val = getattr(item, "calender_Event6", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "calender_Event6"):
                    opp_val = getattr(item, "calender_Event6", None)
                    
                    if opp_val is None:
                        setattr(item, "calender_Event6", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def Add_Edit_View1(self):
        return self.__Add_Edit_View1
    @Add_Edit_View1.setter
    def Add_Edit_View1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Calender_Event__Add_Edit_View1", None)
        self.__Add_Edit_View1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "calender_Event0"):
                    opp_val = getattr(item, "calender_Event0", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "calender_Event0"):
                    opp_val = getattr(item, "calender_Event0", None)
                    
                    if opp_val is None:
                        setattr(item, "calender_Event0", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def Add_Edit_View3(self):
        return self.__Add_Edit_View3
    @Add_Edit_View3.setter
    def Add_Edit_View3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Calender_Event__Add_Edit_View3", None)
        self.__Add_Edit_View3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "calender_Event2"):
                    opp_val = getattr(item, "calender_Event2", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "calender_Event2"):
                    opp_val = getattr(item, "calender_Event2", None)
                    
                    if opp_val is None:
                        setattr(item, "calender_Event2", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def Add_Edit_View5(self):
        return self.__Add_Edit_View5
    @Add_Edit_View5.setter
    def Add_Edit_View5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Calender_Event__Add_Edit_View5", None)
        self.__Add_Edit_View5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "calender_Event4"):
                opp_val = getattr(old_value, "calender_Event4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "calender_Event4"):
                opp_val = getattr(value, "calender_Event4", None)
                if opp_val is None:
                    setattr(value, "calender_Event4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Volunteer:

    def __init__(self, userID: int, userName: str, password: str, calender_Event0: set["Calender_Event"] = None, payment12: "Donations" = None):
        self.userID = userID
        self.userName = userName
        self.password = password
        self.calender_Event0 = calender_Event0 if calender_Event0 is not None else set()
        self.payment12 = payment12
        
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
    def calender_Event0(self):
        return self.__calender_Event0
    @calender_Event0.setter
    def calender_Event0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Volunteer__calender_Event0", None)
        self.__calender_Event0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Add_Edit_View1"):
                    opp_val = getattr(item, "Add_Edit_View1", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Add_Edit_View1"):
                    opp_val = getattr(item, "Add_Edit_View1", None)
                    
                    if opp_val is None:
                        setattr(item, "Add_Edit_View1", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def payment12(self):
        return self.__payment12
    @payment12.setter
    def payment12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Volunteer__payment12", None)
        self.__payment12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "volunteer13"):
                opp_val = getattr(old_value, "volunteer13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "volunteer13"):
                opp_val = getattr(value, "volunteer13", None)
                if opp_val is None:
                    setattr(value, "volunteer13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Admin:

    def __init__(self, password: str, userID: int, userName: str, calender_Event2: set["Calender_Event"] = None, donation14: "Donations" = None, mail20: set["Mail"] = None):
        self.password = password
        self.userID = userID
        self.userName = userName
        self.calender_Event2 = calender_Event2 if calender_Event2 is not None else set()
        self.donation14 = donation14
        self.mail20 = mail20 if mail20 is not None else set()
        
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
    def donation14(self):
        return self.__donation14
    @donation14.setter
    def donation14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__donation14", None)
        self.__donation14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "admin15"):
                opp_val = getattr(old_value, "admin15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "admin15"):
                opp_val = getattr(value, "admin15", None)
                if opp_val is None:
                    setattr(value, "admin15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mail20(self):
        return self.__mail20
    @mail20.setter
    def mail20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__mail20", None)
        self.__mail20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "admin21"):
                    opp_val = getattr(item, "admin21", None)
                    
                    if opp_val == self:
                        setattr(item, "admin21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "admin21"):
                    opp_val = getattr(item, "admin21", None)
                    
                    setattr(item, "admin21", self)
                    

    @property
    def calender_Event2(self):
        return self.__calender_Event2
    @calender_Event2.setter
    def calender_Event2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__calender_Event2", None)
        self.__calender_Event2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Add_Edit_View3"):
                    opp_val = getattr(item, "Add_Edit_View3", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Add_Edit_View3"):
                    opp_val = getattr(item, "Add_Edit_View3", None)
                    
                    if opp_val is None:
                        setattr(item, "Add_Edit_View3", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Normal_user:

    def __init__(self, userID: int, userName: str, password: str, calender_Event4: set["Calender_Event"] = None, donation216: "Donations" = None):
        self.userID = userID
        self.userName = userName
        self.password = password
        self.calender_Event4 = calender_Event4 if calender_Event4 is not None else set()
        self.donation216 = donation216
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

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
    def calender_Event4(self):
        return self.__calender_Event4
    @calender_Event4.setter
    def calender_Event4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Normal_user__calender_Event4", None)
        self.__calender_Event4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Add_Edit_View5"):
                    opp_val = getattr(item, "Add_Edit_View5", None)
                    
                    if opp_val == self:
                        setattr(item, "Add_Edit_View5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Add_Edit_View5"):
                    opp_val = getattr(item, "Add_Edit_View5", None)
                    
                    setattr(item, "Add_Edit_View5", self)
                    

    @property
    def donation216(self):
        return self.__donation216
    @donation216.setter
    def donation216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Normal_user__donation216", None)
        self.__donation216 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "normal_user17"):
                opp_val = getattr(old_value, "normal_user17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "normal_user17"):
                opp_val = getattr(value, "normal_user17", None)
                if opp_val is None:
                    setattr(value, "normal_user17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class void:

    pass


class Executive_Director:

    def __init__(self, userID: int, userName: str, password: str, calender_Event6: set["Calender_Event"] = None, payment10: "Donations" = None, mail18: set["Mail"] = None):
        self.userID = userID
        self.userName = userName
        self.password = password
        self.calender_Event6 = calender_Event6 if calender_Event6 is not None else set()
        self.payment10 = payment10
        self.mail18 = mail18 if mail18 is not None else set()
        
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
    def calender_Event6(self):
        return self.__calender_Event6
    @calender_Event6.setter
    def calender_Event6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Executive_Director__calender_Event6", None)
        self.__calender_Event6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Add_Edit_Vew7"):
                    opp_val = getattr(item, "Add_Edit_Vew7", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Add_Edit_Vew7"):
                    opp_val = getattr(item, "Add_Edit_Vew7", None)
                    
                    if opp_val is None:
                        setattr(item, "Add_Edit_Vew7", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def mail18(self):
        return self.__mail18
    @mail18.setter
    def mail18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Executive_Director__mail18", None)
        self.__mail18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "superAdmin19"):
                    opp_val = getattr(item, "superAdmin19", None)
                    
                    if opp_val == self:
                        setattr(item, "superAdmin19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "superAdmin19"):
                    opp_val = getattr(item, "superAdmin19", None)
                    
                    setattr(item, "superAdmin19", self)
                    

    @property
    def payment10(self):
        return self.__payment10
    @payment10.setter
    def payment10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Executive_Director__payment10", None)
        self.__payment10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "superAdmin11"):
                opp_val = getattr(old_value, "superAdmin11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "superAdmin11"):
                opp_val = getattr(value, "superAdmin11", None)
                if opp_val is None:
                    setattr(value, "superAdmin11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Profile:

    def __init__(self, first_Name: str, last_Name: str, user_Name: str, password: str, phone_Number: int, Track_Attendance8: "Attendance" = None):
        self.first_Name = first_Name
        self.last_Name = last_Name
        self.user_Name = user_Name
        self.password = password
        self.phone_Number = phone_Number
        self.Track_Attendance8 = Track_Attendance8
        
        pass
    @property
    def user_Name(self):
        return self.__user_Name
    @user_Name.setter
    def user_Name(self, user_Name: str):
        self.__user_Name = user_Name

    @property
    def phone_Number(self):
        return self.__phone_Number
    @phone_Number.setter
    def phone_Number(self, phone_Number: int):
        self.__phone_Number = phone_Number

    @property
    def first_Name(self):
        return self.__first_Name
    @first_Name.setter
    def first_Name(self, first_Name: str):
        self.__first_Name = first_Name

    @property
    def last_Name(self):
        return self.__last_Name
    @last_Name.setter
    def last_Name(self, last_Name: str):
        self.__last_Name = last_Name

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def Track_Attendance8(self):
        return self.__Track_Attendance8
    @Track_Attendance8.setter
    def Track_Attendance8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Profile__Track_Attendance8", None)
        self.__Track_Attendance8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile9"):
                opp_val = getattr(old_value, "profile9", None)
                if opp_val == self:
                    setattr(old_value, "profile9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile9"):
                opp_val = getattr(value, "profile9", None)
                setattr(value, "profile9", self)

