from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Bill_Details(Enum):
    pass
class Booking_Status(Enum):
    pass

############################################
# Definition of Classes
############################################










class FeedBack:

    def __init__(self, Rating: str, FeedBackMessage: str, Items10: set["CheckOut_Entity"] = None):
        self.Rating = Rating
        self.FeedBackMessage = FeedBackMessage
        self.Items10 = Items10 if Items10 is not None else set()
        
        pass
    @property
    def FeedBackMessage(self):
        return self.__FeedBackMessage
    @FeedBackMessage.setter
    def FeedBackMessage(self, FeedBackMessage: str):
        self.__FeedBackMessage = FeedBackMessage

    @property
    def Rating(self):
        return self.__Rating
    @Rating.setter
    def Rating(self, Rating: str):
        self.__Rating = Rating

    @property
    def Items10(self):
        return self.__Items10
    @Items10.setter
    def Items10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FeedBack__Items10", None)
        self.__Items10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Feed_Back11"):
                    opp_val = getattr(item, "Feed_Back11", None)
                    
                    if opp_val == self:
                        setattr(item, "Feed_Back11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Feed_Back11"):
                    opp_val = getattr(item, "Feed_Back11", None)
                    
                    setattr(item, "Feed_Back11", self)
                    



class CheckOut_Entity:

    def __init__(self, ItemisedBillDetails: Bill_Details, price: float, sc9: "PostStay_Entity" = None, Feed_Back11: "FeedBack" = None, order13: "StayIn_Entity" = None, p0: set["Payment"] = None):
        self.ItemisedBillDetails = ItemisedBillDetails
        self.price = price
        self.sc9 = sc9
        self.Feed_Back11 = Feed_Back11
        self.order13 = order13
        self.p0 = p0 if p0 is not None else set()
        
        pass
    @property
    def ItemisedBillDetails(self):
        return self.__ItemisedBillDetails
    @ItemisedBillDetails.setter
    def ItemisedBillDetails(self, ItemisedBillDetails: Bill_Details):
        self.__ItemisedBillDetails = ItemisedBillDetails

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def sc9(self):
        return self.__sc9
    @sc9.setter
    def sc9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CheckOut_Entity__sc9", None)
        self.__sc9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "undefined8"):
                opp_val = getattr(old_value, "undefined8", None)
                if opp_val == self:
                    setattr(old_value, "undefined8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "undefined8"):
                opp_val = getattr(value, "undefined8", None)
                setattr(value, "undefined8", self)

    @property
    def p0(self):
        return self.__p0
    @p0.setter
    def p0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CheckOut_Entity__p0", None)
        self.__p0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "acc1"):
                    opp_val = getattr(item, "acc1", None)
                    
                    if opp_val == self:
                        setattr(item, "acc1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "acc1"):
                    opp_val = getattr(item, "acc1", None)
                    
                    setattr(item, "acc1", self)
                    

    @property
    def Feed_Back11(self):
        return self.__Feed_Back11
    @Feed_Back11.setter
    def Feed_Back11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CheckOut_Entity__Feed_Back11", None)
        self.__Feed_Back11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Items10"):
                opp_val = getattr(old_value, "Items10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Items10"):
                opp_val = getattr(value, "Items10", None)
                if opp_val is None:
                    setattr(value, "Items10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def order13(self):
        return self.__order13
    @order13.setter
    def order13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CheckOut_Entity__order13", None)
        self.__order13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "items12"):
                opp_val = getattr(old_value, "items12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "items12"):
                opp_val = getattr(value, "items12", None)
                if opp_val is None:
                    setattr(value, "items12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class StayIn_Entity:

    def __init__(self, EntertainMentList: str, oodList: str, InPremisesList: str, promotionsList: str, placeOfInterest: float, status: Booking_Status, items12: set["CheckOut_Entity"] = None, undefined15: "CheckIn_Entity" = None, payment17: "Payment" = None):
        self.EntertainMentList = EntertainMentList
        self.oodList = oodList
        self.InPremisesList = InPremisesList
        self.promotionsList = promotionsList
        self.placeOfInterest = placeOfInterest
        self.status = status
        self.items12 = items12 if items12 is not None else set()
        self.undefined15 = undefined15
        self.payment17 = payment17
        
        pass
    @property
    def EntertainMentList(self):
        return self.__EntertainMentList
    @EntertainMentList.setter
    def EntertainMentList(self, EntertainMentList: str):
        self.__EntertainMentList = EntertainMentList

    @property
    def promotionsList(self):
        return self.__promotionsList
    @promotionsList.setter
    def promotionsList(self, promotionsList: str):
        self.__promotionsList = promotionsList

    @property
    def placeOfInterest(self):
        return self.__placeOfInterest
    @placeOfInterest.setter
    def placeOfInterest(self, placeOfInterest: float):
        self.__placeOfInterest = placeOfInterest

    @property
    def oodList(self):
        return self.__oodList
    @oodList.setter
    def oodList(self, oodList: str):
        self.__oodList = oodList

    @property
    def InPremisesList(self):
        return self.__InPremisesList
    @InPremisesList.setter
    def InPremisesList(self, InPremisesList: str):
        self.__InPremisesList = InPremisesList

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: Booking_Status):
        self.__status = status

    @property
    def undefined15(self):
        return self.__undefined15
    @undefined15.setter
    def undefined15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StayIn_Entity__undefined15", None)
        self.__undefined15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order14"):
                opp_val = getattr(old_value, "order14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order14"):
                opp_val = getattr(value, "order14", None)
                if opp_val is None:
                    setattr(value, "order14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def payment17(self):
        return self.__payment17
    @payment17.setter
    def payment17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StayIn_Entity__payment17", None)
        self.__payment17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order16"):
                opp_val = getattr(old_value, "order16", None)
                if opp_val == self:
                    setattr(old_value, "order16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order16"):
                opp_val = getattr(value, "order16", None)
                setattr(value, "order16", self)

    @property
    def items12(self):
        return self.__items12
    @items12.setter
    def items12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StayIn_Entity__items12", None)
        self.__items12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "order13"):
                    opp_val = getattr(item, "order13", None)
                    
                    if opp_val == self:
                        setattr(item, "order13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "order13"):
                    opp_val = getattr(item, "order13", None)
                    
                    setattr(item, "order13", self)
                    



class User_Entity:

    def __init__(self, login: str, password: str, City: str, Email: str, Start_Resedentz2: "PostStay_Entity" = None, Booking4: "Booking_Entity" = None):
        self.login = login
        self.password = password
        self.City = City
        self.Email = Email
        self.Start_Resedentz2 = Start_Resedentz2
        self.Booking4 = Booking4
        
        pass
    @property
    def login(self):
        return self.__login
    @login.setter
    def login(self, login: str):
        self.__login = login

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def City(self):
        return self.__City
    @City.setter
    def City(self, City: str):
        self.__City = City

    @property
    def Booking4(self):
        return self.__Booking4
    @Booking4.setter
    def Booking4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User_Entity__Booking4", None)
        self.__Booking4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webUser5"):
                opp_val = getattr(old_value, "webUser5", None)
                if opp_val == self:
                    setattr(old_value, "webUser5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webUser5"):
                opp_val = getattr(value, "webUser5", None)
                setattr(value, "webUser5", self)

    @property
    def Start_Resedentz2(self):
        return self.__Start_Resedentz2
    @Start_Resedentz2.setter
    def Start_Resedentz2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User_Entity__Start_Resedentz2", None)
        self.__Start_Resedentz2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webUser3"):
                opp_val = getattr(old_value, "webUser3", None)
                if opp_val == self:
                    setattr(old_value, "webUser3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webUser3"):
                opp_val = getattr(value, "webUser3", None)
                setattr(value, "webUser3", self)



class CheckIn_Entity:

    def __init__(self, PickUpAddress: str, paymentMode: str, CheckInStatus: str, QRCode: str, MobileKey: str, undefined6: "PostStay_Entity" = None, order14: set["StayIn_Entity"] = None):
        self.PickUpAddress = PickUpAddress
        self.paymentMode = paymentMode
        self.CheckInStatus = CheckInStatus
        self.QRCode = QRCode
        self.MobileKey = MobileKey
        self.undefined6 = undefined6
        self.order14 = order14 if order14 is not None else set()
        
        pass
    @property
    def MobileKey(self):
        return self.__MobileKey
    @MobileKey.setter
    def MobileKey(self, MobileKey: str):
        self.__MobileKey = MobileKey

    @property
    def PickUpAddress(self):
        return self.__PickUpAddress
    @PickUpAddress.setter
    def PickUpAddress(self, PickUpAddress: str):
        self.__PickUpAddress = PickUpAddress

    @property
    def CheckInStatus(self):
        return self.__CheckInStatus
    @CheckInStatus.setter
    def CheckInStatus(self, CheckInStatus: str):
        self.__CheckInStatus = CheckInStatus

    @property
    def QRCode(self):
        return self.__QRCode
    @QRCode.setter
    def QRCode(self, QRCode: str):
        self.__QRCode = QRCode

    @property
    def paymentMode(self):
        return self.__paymentMode
    @paymentMode.setter
    def paymentMode(self, paymentMode: str):
        self.__paymentMode = paymentMode

    @property
    def undefined6(self):
        return self.__undefined6
    @undefined6.setter
    def undefined6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CheckIn_Entity__undefined6", None)
        self.__undefined6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "undefined7"):
                opp_val = getattr(old_value, "undefined7", None)
                if opp_val == self:
                    setattr(old_value, "undefined7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "undefined7"):
                opp_val = getattr(value, "undefined7", None)
                setattr(value, "undefined7", self)

    @property
    def order14(self):
        return self.__order14
    @order14.setter
    def order14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CheckIn_Entity__order14", None)
        self.__order14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "undefined15"):
                    opp_val = getattr(item, "undefined15", None)
                    
                    if opp_val == self:
                        setattr(item, "undefined15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "undefined15"):
                    opp_val = getattr(item, "undefined15", None)
                    
                    setattr(item, "undefined15", self)
                    



class PostStay_Entity:

    def __init__(self, ThanksMessage: str, DiscountPoints: str, PromotionPoints: str, webUser3: "User_Entity" = None, undefined7: "CheckIn_Entity" = None, undefined8: "CheckOut_Entity" = None):
        self.ThanksMessage = ThanksMessage
        self.DiscountPoints = DiscountPoints
        self.PromotionPoints = PromotionPoints
        self.webUser3 = webUser3
        self.undefined7 = undefined7
        self.undefined8 = undefined8
        
        pass
    @property
    def DiscountPoints(self):
        return self.__DiscountPoints
    @DiscountPoints.setter
    def DiscountPoints(self, DiscountPoints: str):
        self.__DiscountPoints = DiscountPoints

    @property
    def ThanksMessage(self):
        return self.__ThanksMessage
    @ThanksMessage.setter
    def ThanksMessage(self, ThanksMessage: str):
        self.__ThanksMessage = ThanksMessage

    @property
    def PromotionPoints(self):
        return self.__PromotionPoints
    @PromotionPoints.setter
    def PromotionPoints(self, PromotionPoints: str):
        self.__PromotionPoints = PromotionPoints

    @property
    def webUser3(self):
        return self.__webUser3
    @webUser3.setter
    def webUser3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PostStay_Entity__webUser3", None)
        self.__webUser3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Start_Resedentz2"):
                opp_val = getattr(old_value, "Start_Resedentz2", None)
                if opp_val == self:
                    setattr(old_value, "Start_Resedentz2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Start_Resedentz2"):
                opp_val = getattr(value, "Start_Resedentz2", None)
                setattr(value, "Start_Resedentz2", self)

    @property
    def undefined8(self):
        return self.__undefined8
    @undefined8.setter
    def undefined8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PostStay_Entity__undefined8", None)
        self.__undefined8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sc9"):
                opp_val = getattr(old_value, "sc9", None)
                if opp_val == self:
                    setattr(old_value, "sc9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sc9"):
                opp_val = getattr(value, "sc9", None)
                setattr(value, "sc9", self)

    @property
    def undefined7(self):
        return self.__undefined7
    @undefined7.setter
    def undefined7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PostStay_Entity__undefined7", None)
        self.__undefined7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "undefined6"):
                opp_val = getattr(old_value, "undefined6", None)
                if opp_val == self:
                    setattr(old_value, "undefined6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "undefined6"):
                opp_val = getattr(value, "undefined6", None)
                setattr(value, "undefined6", self)



class Payment:

    def __init__(self, paidDate: date, total: float, details: str, order16: "StayIn_Entity" = None, acc1: "CheckOut_Entity" = None):
        self.paidDate = paidDate
        self.total = total
        self.details = details
        self.order16 = order16
        self.acc1 = acc1
        
        pass
    @property
    def paidDate(self):
        return self.__paidDate
    @paidDate.setter
    def paidDate(self, paidDate: date):
        self.__paidDate = paidDate

    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, total: float):
        self.__total = total

    @property
    def details(self):
        return self.__details
    @details.setter
    def details(self, details: str):
        self.__details = details

    @property
    def order16(self):
        return self.__order16
    @order16.setter
    def order16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__order16", None)
        self.__order16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment17"):
                opp_val = getattr(old_value, "payment17", None)
                if opp_val == self:
                    setattr(old_value, "payment17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment17"):
                opp_val = getattr(value, "payment17", None)
                setattr(value, "payment17", self)

    @property
    def acc1(self):
        return self.__acc1
    @acc1.setter
    def acc1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__acc1", None)
        self.__acc1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p0"):
                opp_val = getattr(old_value, "p0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p0"):
                opp_val = getattr(value, "p0", None)
                if opp_val is None:
                    setattr(value, "p0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Booking_Entity:

    def __init__(self, address: str, phone: str, email: str, CheckInDate: date, NoOfDays: int, webUser5: "User_Entity" = None):
        self.address = address
        self.phone = phone
        self.email = email
        self.CheckInDate = CheckInDate
        self.NoOfDays = NoOfDays
        self.webUser5 = webUser5
        
        pass
    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def NoOfDays(self):
        return self.__NoOfDays
    @NoOfDays.setter
    def NoOfDays(self, NoOfDays: int):
        self.__NoOfDays = NoOfDays

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def CheckInDate(self):
        return self.__CheckInDate
    @CheckInDate.setter
    def CheckInDate(self, CheckInDate: date):
        self.__CheckInDate = CheckInDate

    @property
    def webUser5(self):
        return self.__webUser5
    @webUser5.setter
    def webUser5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Booking_Entity__webUser5", None)
        self.__webUser5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Booking4"):
                opp_val = getattr(old_value, "Booking4", None)
                if opp_val == self:
                    setattr(old_value, "Booking4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Booking4"):
                opp_val = getattr(value, "Booking4", None)
                setattr(value, "Booking4", self)

