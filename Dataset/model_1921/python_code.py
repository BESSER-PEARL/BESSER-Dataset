from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class AdminInterface:

    pass
class model_AdminController(AdminInterface):

    def __init__(self, model_AdminController52: "model_DatabaseInterface" = None, model_AdminController55: "model_RoomExpert" = None, model_AdminController: "model_UserExpert" = None, model_AdminController46: "model_ExpenseExpert" = None, model_AdminController49: "model_PromotionExpert" = None):
        self.model_AdminController52 = model_AdminController52
        self.model_AdminController55 = model_AdminController55
        self.model_AdminController = model_AdminController
        self.model_AdminController46 = model_AdminController46
        self.model_AdminController49 = model_AdminController49
        
        pass
    @property
    def model_AdminController49(self):
        return self.__model_AdminController49

    @model_AdminController49.setter
    def model_AdminController49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AdminController__model_AdminController49", None)
        self.__model_AdminController49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_PromotionExpert50"):
                opp_val = getattr(old_value, "model_PromotionExpert50", None)
                if opp_val == self:
                    setattr(old_value, "model_PromotionExpert50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_PromotionExpert50"):
                opp_val = getattr(value, "model_PromotionExpert50", None)
                setattr(value, "model_PromotionExpert50", self)

    @property
    def model_AdminController55(self):
        return self.__model_AdminController55

    @model_AdminController55.setter
    def model_AdminController55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AdminController__model_AdminController55", None)
        self.__model_AdminController55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_RoomExpert56"):
                opp_val = getattr(old_value, "model_RoomExpert56", None)
                if opp_val == self:
                    setattr(old_value, "model_RoomExpert56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_RoomExpert56"):
                opp_val = getattr(value, "model_RoomExpert56", None)
                setattr(value, "model_RoomExpert56", self)

    @property
    def model_AdminController(self):
        return self.__model_AdminController

    @model_AdminController.setter
    def model_AdminController(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AdminController__model_AdminController", None)
        self.__model_AdminController = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_UserExpert44"):
                opp_val = getattr(old_value, "model_UserExpert44", None)
                if opp_val == self:
                    setattr(old_value, "model_UserExpert44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_UserExpert44"):
                opp_val = getattr(value, "model_UserExpert44", None)
                setattr(value, "model_UserExpert44", self)

    @property
    def model_AdminController46(self):
        return self.__model_AdminController46

    @model_AdminController46.setter
    def model_AdminController46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AdminController__model_AdminController46", None)
        self.__model_AdminController46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ExpenseExpert47"):
                opp_val = getattr(old_value, "model_ExpenseExpert47", None)
                if opp_val == self:
                    setattr(old_value, "model_ExpenseExpert47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ExpenseExpert47"):
                opp_val = getattr(value, "model_ExpenseExpert47", None)
                setattr(value, "model_ExpenseExpert47", self)

    @property
    def model_AdminController52(self):
        return self.__model_AdminController52

    @model_AdminController52.setter
    def model_AdminController52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AdminController__model_AdminController52", None)
        self.__model_AdminController52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DatabaseInterface53"):
                opp_val = getattr(old_value, "model_DatabaseInterface53", None)
                if opp_val == self:
                    setattr(old_value, "model_DatabaseInterface53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DatabaseInterface53"):
                opp_val = getattr(value, "model_DatabaseInterface53", None)
                setattr(value, "model_DatabaseInterface53", self)

    def AdminController(self, model_userExpert, model_promotionExpert, model_roomExpert, model_expenseExpert):
        # TODO: Implement AdminController method
        pass

class DatabaseInterface:

    pass
class model_MSAccessDB(DatabaseInterface):

    def __init__(self):
        
        pass
    def closeConnection(self):
        # TODO: Implement closeConnection method
        pass

    def openConnection(self) :
        # TODO: Implement openConnection method
        pass

class ReceptionistInterface:

    pass
class BookingController:

    pass
class model_ReceptionistController(BookingController, ReceptionistInterface):

    def __init__(self, model_ReceptionistController: "model_UserExpert" = None):
        self.model_ReceptionistController = model_ReceptionistController
        
        pass
    @property
    def model_ReceptionistController(self):
        return self.__model_ReceptionistController

    @model_ReceptionistController.setter
    def model_ReceptionistController(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ReceptionistController__model_ReceptionistController", None)
        self.__model_ReceptionistController = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_UserExpert58"):
                opp_val = getattr(old_value, "model_UserExpert58", None)
                if opp_val == self:
                    setattr(old_value, "model_UserExpert58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_UserExpert58"):
                opp_val = getattr(value, "model_UserExpert58", None)
                setattr(value, "model_UserExpert58", self)

    def ReceptionistController(self, model_roomExpert, model_receiptExpert, model_promotionExpert, model_expenseExpert, model_userExpert, model_bookingExpert):
        # TODO: Implement ReceptionistController method
        pass

class model_ReceiptExpert:

    def __init__(self, model_ReceiptExpert: "model_DatabaseInterface" = None, model_ReceiptExpert42: "model_BookingController" = None):
        self.model_ReceiptExpert = model_ReceiptExpert
        self.model_ReceiptExpert42 = model_ReceiptExpert42
        
        pass
    @property
    def model_ReceiptExpert(self):
        return self.__model_ReceiptExpert

    @model_ReceiptExpert.setter
    def model_ReceiptExpert(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ReceiptExpert__model_ReceiptExpert", None)
        self.__model_ReceiptExpert = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DatabaseInterface25"):
                opp_val = getattr(old_value, "model_DatabaseInterface25", None)
                if opp_val == self:
                    setattr(old_value, "model_DatabaseInterface25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DatabaseInterface25"):
                opp_val = getattr(value, "model_DatabaseInterface25", None)
                setattr(value, "model_DatabaseInterface25", self)

    @property
    def model_ReceiptExpert42(self):
        return self.__model_ReceiptExpert42

    @model_ReceiptExpert42.setter
    def model_ReceiptExpert42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ReceiptExpert__model_ReceiptExpert42", None)
        self.__model_ReceiptExpert42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_BookingController41"):
                opp_val = getattr(old_value, "model_BookingController41", None)
                if opp_val == self:
                    setattr(old_value, "model_BookingController41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_BookingController41"):
                opp_val = getattr(value, "model_BookingController41", None)
                setattr(value, "model_BookingController41", self)

    def getReceipt(self, model_ID) :
        # TODO: Implement getReceipt method
        pass

    def updateReceipt(self, model_receipt) :
        # TODO: Implement updateReceipt method
        pass

    def combine(self, model_receiptList) :
        # TODO: Implement combine method
        pass

    def ReceiptExpert(self, model_database):
        # TODO: Implement ReceiptExpert method
        pass

    def getAllReceipt(self) :
        # TODO: Implement getAllReceipt method
        pass

    def addReceipt(self, model_receipt) :
        # TODO: Implement addReceipt method
        pass

    def removeReceipt(self, model_receipt) :
        # TODO: Implement removeReceipt method
        pass

class CustomerInterface:

    pass
class model_BookingController(CustomerInterface):

    def __init__(self, model_BookingController: "model_RoomExpert" = None, model_BookingController29: "model_BookingExpert" = None, model_BookingController32: "model_PromotionExpert" = None, model_BookingController35: "model_DatabaseInterface" = None, model_BookingController38: "model_ExpenseExpert" = None, model_BookingController41: "model_ReceiptExpert" = None):
        self.model_BookingController = model_BookingController
        self.model_BookingController29 = model_BookingController29
        self.model_BookingController32 = model_BookingController32
        self.model_BookingController35 = model_BookingController35
        self.model_BookingController38 = model_BookingController38
        self.model_BookingController41 = model_BookingController41
        
        pass
    @property
    def model_BookingController29(self):
        return self.__model_BookingController29

    @model_BookingController29.setter
    def model_BookingController29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_BookingController__model_BookingController29", None)
        self.__model_BookingController29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_BookingExpert30"):
                opp_val = getattr(old_value, "model_BookingExpert30", None)
                if opp_val == self:
                    setattr(old_value, "model_BookingExpert30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_BookingExpert30"):
                opp_val = getattr(value, "model_BookingExpert30", None)
                setattr(value, "model_BookingExpert30", self)

    @property
    def model_BookingController38(self):
        return self.__model_BookingController38

    @model_BookingController38.setter
    def model_BookingController38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_BookingController__model_BookingController38", None)
        self.__model_BookingController38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ExpenseExpert39"):
                opp_val = getattr(old_value, "model_ExpenseExpert39", None)
                if opp_val == self:
                    setattr(old_value, "model_ExpenseExpert39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ExpenseExpert39"):
                opp_val = getattr(value, "model_ExpenseExpert39", None)
                setattr(value, "model_ExpenseExpert39", self)

    @property
    def model_BookingController32(self):
        return self.__model_BookingController32

    @model_BookingController32.setter
    def model_BookingController32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_BookingController__model_BookingController32", None)
        self.__model_BookingController32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_PromotionExpert33"):
                opp_val = getattr(old_value, "model_PromotionExpert33", None)
                if opp_val == self:
                    setattr(old_value, "model_PromotionExpert33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_PromotionExpert33"):
                opp_val = getattr(value, "model_PromotionExpert33", None)
                setattr(value, "model_PromotionExpert33", self)

    @property
    def model_BookingController35(self):
        return self.__model_BookingController35

    @model_BookingController35.setter
    def model_BookingController35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_BookingController__model_BookingController35", None)
        self.__model_BookingController35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DatabaseInterface36"):
                opp_val = getattr(old_value, "model_DatabaseInterface36", None)
                if opp_val == self:
                    setattr(old_value, "model_DatabaseInterface36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DatabaseInterface36"):
                opp_val = getattr(value, "model_DatabaseInterface36", None)
                setattr(value, "model_DatabaseInterface36", self)

    @property
    def model_BookingController41(self):
        return self.__model_BookingController41

    @model_BookingController41.setter
    def model_BookingController41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_BookingController__model_BookingController41", None)
        self.__model_BookingController41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ReceiptExpert42"):
                opp_val = getattr(old_value, "model_ReceiptExpert42", None)
                if opp_val == self:
                    setattr(old_value, "model_ReceiptExpert42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ReceiptExpert42"):
                opp_val = getattr(value, "model_ReceiptExpert42", None)
                setattr(value, "model_ReceiptExpert42", self)

    @property
    def model_BookingController(self):
        return self.__model_BookingController

    @model_BookingController.setter
    def model_BookingController(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_BookingController__model_BookingController", None)
        self.__model_BookingController = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_RoomExpert27"):
                opp_val = getattr(old_value, "model_RoomExpert27", None)
                if opp_val == self:
                    setattr(old_value, "model_RoomExpert27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_RoomExpert27"):
                opp_val = getattr(value, "model_RoomExpert27", None)
                setattr(value, "model_RoomExpert27", self)

    def BookingController(self, model_receiptExpert, model_roomExpert, model_bookingExpert, model_expenseExpert, model_promotionExpert):
        # TODO: Implement BookingController method
        pass

class model_Payment:

    def __init__(self):
        
        pass
    def makePayment(self, model_amount, model_customer) :
        # TODO: Implement makePayment method
        pass

    def isCreditCardValid(self, model_customer) :
        # TODO: Implement isCreditCardValid method
        pass

class model_EmailSender:

    def __init__(self):
        
        pass
    def send(self, model_booking) :
        # TODO: Implement send method
        pass

class model_UserExpert:

    def __init__(self, model_UserExpert58: "model_ReceptionistController" = None, model_UserExpert44: "model_AdminController" = None, model_UserExpert: "model_DatabaseInterface" = None):
        self.model_UserExpert58 = model_UserExpert58
        self.model_UserExpert44 = model_UserExpert44
        self.model_UserExpert = model_UserExpert
        
        pass
    @property
    def model_UserExpert58(self):
        return self.__model_UserExpert58

    @model_UserExpert58.setter
    def model_UserExpert58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_UserExpert__model_UserExpert58", None)
        self.__model_UserExpert58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ReceptionistController"):
                opp_val = getattr(old_value, "model_ReceptionistController", None)
                if opp_val == self:
                    setattr(old_value, "model_ReceptionistController", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ReceptionistController"):
                opp_val = getattr(value, "model_ReceptionistController", None)
                setattr(value, "model_ReceptionistController", self)

    @property
    def model_UserExpert(self):
        return self.__model_UserExpert

    @model_UserExpert.setter
    def model_UserExpert(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_UserExpert__model_UserExpert", None)
        self.__model_UserExpert = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DatabaseInterface19"):
                opp_val = getattr(old_value, "model_DatabaseInterface19", None)
                if opp_val == self:
                    setattr(old_value, "model_DatabaseInterface19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DatabaseInterface19"):
                opp_val = getattr(value, "model_DatabaseInterface19", None)
                setattr(value, "model_DatabaseInterface19", self)

    @property
    def model_UserExpert44(self):
        return self.__model_UserExpert44

    @model_UserExpert44.setter
    def model_UserExpert44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_UserExpert__model_UserExpert44", None)
        self.__model_UserExpert44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_AdminController"):
                opp_val = getattr(old_value, "model_AdminController", None)
                if opp_val == self:
                    setattr(old_value, "model_AdminController", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_AdminController"):
                opp_val = getattr(value, "model_AdminController", None)
                setattr(value, "model_AdminController", self)

    def removeUser(self, model_ID) :
        # TODO: Implement removeUser method
        pass

    def getUser(self, model_ID) :
        # TODO: Implement getUser method
        pass

    def getAllUsers(self) :
        # TODO: Implement getAllUsers method
        pass

    def addUser(self, model_user) :
        # TODO: Implement addUser method
        pass

    def updateUser(self, model_user) :
        # TODO: Implement updateUser method
        pass

    def UserExpert(self, model_database):
        # TODO: Implement UserExpert method
        pass

    def login(self, model_password, model_name) :
        # TODO: Implement login method
        pass

class model_BookingExpert:

    def __init__(self, model_BookingExpert: "model_DatabaseInterface" = None, model_BookingExpert30: "model_BookingController" = None):
        self.model_BookingExpert = model_BookingExpert
        self.model_BookingExpert30 = model_BookingExpert30
        
        pass
    @property
    def model_BookingExpert30(self):
        return self.__model_BookingExpert30

    @model_BookingExpert30.setter
    def model_BookingExpert30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_BookingExpert__model_BookingExpert30", None)
        self.__model_BookingExpert30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_BookingController29"):
                opp_val = getattr(old_value, "model_BookingController29", None)
                if opp_val == self:
                    setattr(old_value, "model_BookingController29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_BookingController29"):
                opp_val = getattr(value, "model_BookingController29", None)
                setattr(value, "model_BookingController29", self)

    @property
    def model_BookingExpert(self):
        return self.__model_BookingExpert

    @model_BookingExpert.setter
    def model_BookingExpert(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_BookingExpert__model_BookingExpert", None)
        self.__model_BookingExpert = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DatabaseInterface23"):
                opp_val = getattr(old_value, "model_DatabaseInterface23", None)
                if opp_val == self:
                    setattr(old_value, "model_DatabaseInterface23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DatabaseInterface23"):
                opp_val = getattr(value, "model_DatabaseInterface23", None)
                setattr(value, "model_DatabaseInterface23", self)

    def getAllBookings(self, model_dateTo, model_surname, model_dateFrom) :
        # TODO: Implement getAllBookings method
        pass

    def updateBooking(self, model_booking) :
        # TODO: Implement updateBooking method
        pass

    def checkOut(self, model_booking) :
        # TODO: Implement checkOut method
        pass

    def removeBooking(self, model_booking) :
        # TODO: Implement removeBooking method
        pass

    def checkIn(self, model_rooms, model_booking) :
        # TODO: Implement checkIn method
        pass

    def getBooking(self, model_ID) :
        # TODO: Implement getBooking method
        pass

    def BookingExpert(self, model_database):
        # TODO: Implement BookingExpert method
        pass

    def addBooking(self, model_booking) :
        # TODO: Implement addBooking method
        pass

class model_PromotionExpert:

    def __init__(self, model_PromotionExpert50: "model_AdminController" = None, model_PromotionExpert: "model_DatabaseInterface" = None, model_PromotionExpert33: "model_BookingController" = None):
        self.model_PromotionExpert50 = model_PromotionExpert50
        self.model_PromotionExpert = model_PromotionExpert
        self.model_PromotionExpert33 = model_PromotionExpert33
        
        pass
    @property
    def model_PromotionExpert(self):
        return self.__model_PromotionExpert

    @model_PromotionExpert.setter
    def model_PromotionExpert(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PromotionExpert__model_PromotionExpert", None)
        self.__model_PromotionExpert = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DatabaseInterface21"):
                opp_val = getattr(old_value, "model_DatabaseInterface21", None)
                if opp_val == self:
                    setattr(old_value, "model_DatabaseInterface21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DatabaseInterface21"):
                opp_val = getattr(value, "model_DatabaseInterface21", None)
                setattr(value, "model_DatabaseInterface21", self)

    @property
    def model_PromotionExpert33(self):
        return self.__model_PromotionExpert33

    @model_PromotionExpert33.setter
    def model_PromotionExpert33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PromotionExpert__model_PromotionExpert33", None)
        self.__model_PromotionExpert33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_BookingController32"):
                opp_val = getattr(old_value, "model_BookingController32", None)
                if opp_val == self:
                    setattr(old_value, "model_BookingController32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_BookingController32"):
                opp_val = getattr(value, "model_BookingController32", None)
                setattr(value, "model_BookingController32", self)

    @property
    def model_PromotionExpert50(self):
        return self.__model_PromotionExpert50

    @model_PromotionExpert50.setter
    def model_PromotionExpert50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PromotionExpert__model_PromotionExpert50", None)
        self.__model_PromotionExpert50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_AdminController49"):
                opp_val = getattr(old_value, "model_AdminController49", None)
                if opp_val == self:
                    setattr(old_value, "model_AdminController49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_AdminController49"):
                opp_val = getattr(value, "model_AdminController49", None)
                setattr(value, "model_AdminController49", self)

    def updatePromotion(self, model_promotion) :
        # TODO: Implement updatePromotion method
        pass

    def getPromotion(self, model_promotionCode) :
        # TODO: Implement getPromotion method
        pass

    def getAllPromotions(self) :
        # TODO: Implement getAllPromotions method
        pass

    def PromotionExpert(self, model_database):
        # TODO: Implement PromotionExpert method
        pass

    def removePromotion(self, model_code) :
        # TODO: Implement removePromotion method
        pass

    def addPromotion(self, model_promotion) :
        # TODO: Implement addPromotion method
        pass

class model_ExpenseExpert:

    def __init__(self, model_ExpenseExpert47: "model_AdminController" = None, model_ExpenseExpert: "model_DatabaseInterface" = None, model_ExpenseExpert39: "model_BookingController" = None):
        self.model_ExpenseExpert47 = model_ExpenseExpert47
        self.model_ExpenseExpert = model_ExpenseExpert
        self.model_ExpenseExpert39 = model_ExpenseExpert39
        
        pass
    @property
    def model_ExpenseExpert39(self):
        return self.__model_ExpenseExpert39

    @model_ExpenseExpert39.setter
    def model_ExpenseExpert39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ExpenseExpert__model_ExpenseExpert39", None)
        self.__model_ExpenseExpert39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_BookingController38"):
                opp_val = getattr(old_value, "model_BookingController38", None)
                if opp_val == self:
                    setattr(old_value, "model_BookingController38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_BookingController38"):
                opp_val = getattr(value, "model_BookingController38", None)
                setattr(value, "model_BookingController38", self)

    @property
    def model_ExpenseExpert(self):
        return self.__model_ExpenseExpert

    @model_ExpenseExpert.setter
    def model_ExpenseExpert(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ExpenseExpert__model_ExpenseExpert", None)
        self.__model_ExpenseExpert = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DatabaseInterface17"):
                opp_val = getattr(old_value, "model_DatabaseInterface17", None)
                if opp_val == self:
                    setattr(old_value, "model_DatabaseInterface17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DatabaseInterface17"):
                opp_val = getattr(value, "model_DatabaseInterface17", None)
                setattr(value, "model_DatabaseInterface17", self)

    @property
    def model_ExpenseExpert47(self):
        return self.__model_ExpenseExpert47

    @model_ExpenseExpert47.setter
    def model_ExpenseExpert47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ExpenseExpert__model_ExpenseExpert47", None)
        self.__model_ExpenseExpert47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_AdminController46"):
                opp_val = getattr(old_value, "model_AdminController46", None)
                if opp_val == self:
                    setattr(old_value, "model_AdminController46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_AdminController46"):
                opp_val = getattr(value, "model_AdminController46", None)
                setattr(value, "model_AdminController46", self)

    def removeExpense(self, model_ID) :
        # TODO: Implement removeExpense method
        pass

    def updateExpense(self, model_expense) :
        # TODO: Implement updateExpense method
        pass

    def ExpenseExpert(self, model_database):
        # TODO: Implement ExpenseExpert method
        pass

    def addExpense(self, model_expense) :
        # TODO: Implement addExpense method
        pass

    def getExpense(self, model_ID) :
        # TODO: Implement getExpense method
        pass

    def getAllExpense(self, model_receiptID) :
        # TODO: Implement getAllExpense method
        pass

class model_DatabaseInterface(ABC):

    def __init__(self, model_DatabaseInterface: "model_RoomExpert" = None, model_DatabaseInterface23: "model_BookingExpert" = None, model_DatabaseInterface53: "model_AdminController" = None, model_DatabaseInterface19: "model_UserExpert" = None, model_DatabaseInterface21: "model_PromotionExpert" = None, model_DatabaseInterface17: "model_ExpenseExpert" = None, model_DatabaseInterface25: "model_ReceiptExpert" = None, model_DatabaseInterface36: "model_BookingController" = None):
        self.model_DatabaseInterface = model_DatabaseInterface
        self.model_DatabaseInterface23 = model_DatabaseInterface23
        self.model_DatabaseInterface53 = model_DatabaseInterface53
        self.model_DatabaseInterface19 = model_DatabaseInterface19
        self.model_DatabaseInterface21 = model_DatabaseInterface21
        self.model_DatabaseInterface17 = model_DatabaseInterface17
        self.model_DatabaseInterface25 = model_DatabaseInterface25
        self.model_DatabaseInterface36 = model_DatabaseInterface36
        
        pass
    @property
    def model_DatabaseInterface17(self):
        return self.__model_DatabaseInterface17

    @model_DatabaseInterface17.setter
    def model_DatabaseInterface17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DatabaseInterface__model_DatabaseInterface17", None)
        self.__model_DatabaseInterface17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ExpenseExpert"):
                opp_val = getattr(old_value, "model_ExpenseExpert", None)
                if opp_val == self:
                    setattr(old_value, "model_ExpenseExpert", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ExpenseExpert"):
                opp_val = getattr(value, "model_ExpenseExpert", None)
                setattr(value, "model_ExpenseExpert", self)

    @property
    def model_DatabaseInterface(self):
        return self.__model_DatabaseInterface

    @model_DatabaseInterface.setter
    def model_DatabaseInterface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DatabaseInterface__model_DatabaseInterface", None)
        self.__model_DatabaseInterface = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_RoomExpert"):
                opp_val = getattr(old_value, "model_RoomExpert", None)
                if opp_val == self:
                    setattr(old_value, "model_RoomExpert", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_RoomExpert"):
                opp_val = getattr(value, "model_RoomExpert", None)
                setattr(value, "model_RoomExpert", self)

    @property
    def model_DatabaseInterface53(self):
        return self.__model_DatabaseInterface53

    @model_DatabaseInterface53.setter
    def model_DatabaseInterface53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DatabaseInterface__model_DatabaseInterface53", None)
        self.__model_DatabaseInterface53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_AdminController52"):
                opp_val = getattr(old_value, "model_AdminController52", None)
                if opp_val == self:
                    setattr(old_value, "model_AdminController52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_AdminController52"):
                opp_val = getattr(value, "model_AdminController52", None)
                setattr(value, "model_AdminController52", self)

    @property
    def model_DatabaseInterface19(self):
        return self.__model_DatabaseInterface19

    @model_DatabaseInterface19.setter
    def model_DatabaseInterface19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DatabaseInterface__model_DatabaseInterface19", None)
        self.__model_DatabaseInterface19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_UserExpert"):
                opp_val = getattr(old_value, "model_UserExpert", None)
                if opp_val == self:
                    setattr(old_value, "model_UserExpert", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_UserExpert"):
                opp_val = getattr(value, "model_UserExpert", None)
                setattr(value, "model_UserExpert", self)

    @property
    def model_DatabaseInterface36(self):
        return self.__model_DatabaseInterface36

    @model_DatabaseInterface36.setter
    def model_DatabaseInterface36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DatabaseInterface__model_DatabaseInterface36", None)
        self.__model_DatabaseInterface36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_BookingController35"):
                opp_val = getattr(old_value, "model_BookingController35", None)
                if opp_val == self:
                    setattr(old_value, "model_BookingController35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_BookingController35"):
                opp_val = getattr(value, "model_BookingController35", None)
                setattr(value, "model_BookingController35", self)

    @property
    def model_DatabaseInterface23(self):
        return self.__model_DatabaseInterface23

    @model_DatabaseInterface23.setter
    def model_DatabaseInterface23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DatabaseInterface__model_DatabaseInterface23", None)
        self.__model_DatabaseInterface23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_BookingExpert"):
                opp_val = getattr(old_value, "model_BookingExpert", None)
                if opp_val == self:
                    setattr(old_value, "model_BookingExpert", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_BookingExpert"):
                opp_val = getattr(value, "model_BookingExpert", None)
                setattr(value, "model_BookingExpert", self)

    @property
    def model_DatabaseInterface25(self):
        return self.__model_DatabaseInterface25

    @model_DatabaseInterface25.setter
    def model_DatabaseInterface25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DatabaseInterface__model_DatabaseInterface25", None)
        self.__model_DatabaseInterface25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ReceiptExpert"):
                opp_val = getattr(old_value, "model_ReceiptExpert", None)
                if opp_val == self:
                    setattr(old_value, "model_ReceiptExpert", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ReceiptExpert"):
                opp_val = getattr(value, "model_ReceiptExpert", None)
                setattr(value, "model_ReceiptExpert", self)

    @property
    def model_DatabaseInterface21(self):
        return self.__model_DatabaseInterface21

    @model_DatabaseInterface21.setter
    def model_DatabaseInterface21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DatabaseInterface__model_DatabaseInterface21", None)
        self.__model_DatabaseInterface21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_PromotionExpert"):
                opp_val = getattr(old_value, "model_PromotionExpert", None)
                if opp_val == self:
                    setattr(old_value, "model_PromotionExpert", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_PromotionExpert"):
                opp_val = getattr(value, "model_PromotionExpert", None)
                setattr(value, "model_PromotionExpert", self)

    def query(self, model_query) :
        # TODO: Implement query method
        pass

    def send(self, model_query) :
        # TODO: Implement send method
        pass

class model_RoomExpert:

    def __init__(self, model_RoomExpert: "model_DatabaseInterface" = None, model_RoomExpert56: "model_AdminController" = None, model_RoomExpert27: "model_BookingController" = None):
        self.model_RoomExpert = model_RoomExpert
        self.model_RoomExpert56 = model_RoomExpert56
        self.model_RoomExpert27 = model_RoomExpert27
        
        pass
    @property
    def model_RoomExpert27(self):
        return self.__model_RoomExpert27

    @model_RoomExpert27.setter
    def model_RoomExpert27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_RoomExpert__model_RoomExpert27", None)
        self.__model_RoomExpert27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_BookingController"):
                opp_val = getattr(old_value, "model_BookingController", None)
                if opp_val == self:
                    setattr(old_value, "model_BookingController", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_BookingController"):
                opp_val = getattr(value, "model_BookingController", None)
                setattr(value, "model_BookingController", self)

    @property
    def model_RoomExpert(self):
        return self.__model_RoomExpert

    @model_RoomExpert.setter
    def model_RoomExpert(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_RoomExpert__model_RoomExpert", None)
        self.__model_RoomExpert = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DatabaseInterface"):
                opp_val = getattr(old_value, "model_DatabaseInterface", None)
                if opp_val == self:
                    setattr(old_value, "model_DatabaseInterface", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DatabaseInterface"):
                opp_val = getattr(value, "model_DatabaseInterface", None)
                setattr(value, "model_DatabaseInterface", self)

    @property
    def model_RoomExpert56(self):
        return self.__model_RoomExpert56

    @model_RoomExpert56.setter
    def model_RoomExpert56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_RoomExpert__model_RoomExpert56", None)
        self.__model_RoomExpert56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_AdminController55"):
                opp_val = getattr(old_value, "model_AdminController55", None)
                if opp_val == self:
                    setattr(old_value, "model_AdminController55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_AdminController55"):
                opp_val = getattr(value, "model_AdminController55", None)
                setattr(value, "model_AdminController55", self)

    def RoomExpert(self, model_database):
        # TODO: Implement RoomExpert method
        pass

    def getAllRooms(self) :
        # TODO: Implement getAllRooms method
        pass

    def getAvailableRoomTypes(self, model_numberOfGuests, model_to, model_from_, model_numberOfRooms) :
        # TODO: Implement getAvailableRoomTypes method
        pass

    def updateRoom(self, model_room) :
        # TODO: Implement updateRoom method
        pass

    def addRoom(self, model_room) :
        # TODO: Implement addRoom method
        pass

    def removeRoom(self, model_room) :
        # TODO: Implement removeRoom method
        pass

    def getRoom(self, model_roomNumber) :
        # TODO: Implement getRoom method
        pass

    def getUnoccupiedRooms(self) :
        # TODO: Implement getUnoccupiedRooms method
        pass

class model_Promotion:

    def __init__(self, code: str, description: str, percentage: str, validFrom: date, validTo: date, roomType: str, expirationDate: date):
        self.code = code
        self.description = description
        self.percentage = percentage
        self.validFrom = validFrom
        self.validTo = validTo
        self.roomType = roomType
        self.expirationDate = expirationDate
        
        pass
    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code


    @property
    def validTo(self):
        return self.__validTo

    @validTo.setter
    def validTo(self, validTo: date):
        self.__validTo = validTo


    @property
    def expirationDate(self):
        return self.__expirationDate

    @expirationDate.setter
    def expirationDate(self, expirationDate: date):
        self.__expirationDate = expirationDate


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def validFrom(self):
        return self.__validFrom

    @validFrom.setter
    def validFrom(self, validFrom: date):
        self.__validFrom = validFrom


    @property
    def roomType(self):
        return self.__roomType

    @roomType.setter
    def roomType(self, roomType: str):
        self.__roomType = roomType


    @property
    def percentage(self):
        return self.__percentage

    @percentage.setter
    def percentage(self, percentage: str):
        self.__percentage = percentage


    def calculateDiscount(self, model_room) :
        # TODO: Implement calculateDiscount method
        pass

    def Promotion(self, model_expirationDate, model_vaildFrom, model_roomType, model_percentage, model_vaildTo, model_code, model_description):
        # TODO: Implement Promotion method
        pass

class model_User:

    def __init__(self, firstName: str, surname: str, password: str, id: str, receptionist: str, administrator: str):
        self.firstName = firstName
        self.surname = surname
        self.password = password
        self.id = id
        self.receptionist = receptionist
        self.administrator = administrator
        
        pass
    @property
    def administrator(self):
        return self.__administrator

    @administrator.setter
    def administrator(self, administrator: str):
        self.__administrator = administrator


    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname: str):
        self.__surname = surname


    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password


    @property
    def firstName(self):
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName


    @property
    def receptionist(self):
        return self.__receptionist

    @receptionist.setter
    def receptionist(self, receptionist: str):
        self.__receptionist = receptionist


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    def User(self, model_receptionist, model_surname, model_administrator, model_id, model_password, model_firstName):
        # TODO: Implement User method
        pass

class model_AdminInterface(ABC):

    def __init__(self):
        
        pass
    def viewRooms(self) :
        # TODO: Implement viewRooms method
        pass

    def createExpense(self, model_expense) :
        # TODO: Implement createExpense method
        pass

    def viewUsers(self) :
        # TODO: Implement viewUsers method
        pass

    def updateRoom(self, model_room) :
        # TODO: Implement updateRoom method
        pass

    def viewExpenses(self) :
        # TODO: Implement viewExpenses method
        pass

    def removeRoom(self, model_room) :
        # TODO: Implement removeRoom method
        pass

    def viewPromotions(self) :
        # TODO: Implement viewPromotions method
        pass

    def updatePromotion(self, model_promotion) :
        # TODO: Implement updatePromotion method
        pass

    def removeUser(self, model_user) :
        # TODO: Implement removeUser method
        pass

    def createPromotion(self, model_promotion) :
        # TODO: Implement createPromotion method
        pass

    def removeExpense(self, model_expense) :
        # TODO: Implement removeExpense method
        pass

    def AdminController(self, model_userExpert, model_promotionExpert, model_expenseExpert, model_roomExpert):
        # TODO: Implement AdminController method
        pass

    def login(self, model_name, model_password) :
        # TODO: Implement login method
        pass

    def createUser(self, model_user) :
        # TODO: Implement createUser method
        pass

    def createRoom(self, model_room) :
        # TODO: Implement createRoom method
        pass

    def updateUser(self, model_user) :
        # TODO: Implement updateUser method
        pass

    def updateExpense(self, model_expense) :
        # TODO: Implement updateExpense method
        pass

    def removePromotion(self, model_promotion) :
        # TODO: Implement removePromotion method
        pass

class model_Booking:

    def __init__(self, fromDate: date, toDate: date, wishes: str, promotion: str, roomTypes: str, checkedIn: str, id: int, model_Booking: "model_Customer" = None, model_Booking10: "model_Receipt" = None, model_Booking13: set["model_Room"] = None):
        self.fromDate = fromDate
        self.toDate = toDate
        self.wishes = wishes
        self.promotion = promotion
        self.roomTypes = roomTypes
        self.checkedIn = checkedIn
        self.id = id
        self.model_Booking = model_Booking
        self.model_Booking10 = model_Booking10
        self.model_Booking13 = model_Booking13 if model_Booking13 is not None else set()
        
        pass
    @property
    def wishes(self):
        return self.__wishes

    @wishes.setter
    def wishes(self, wishes: str):
        self.__wishes = wishes


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id


    @property
    def toDate(self):
        return self.__toDate

    @toDate.setter
    def toDate(self, toDate: date):
        self.__toDate = toDate


    @property
    def fromDate(self):
        return self.__fromDate

    @fromDate.setter
    def fromDate(self, fromDate: date):
        self.__fromDate = fromDate


    @property
    def checkedIn(self):
        return self.__checkedIn

    @checkedIn.setter
    def checkedIn(self, checkedIn: str):
        self.__checkedIn = checkedIn


    @property
    def roomTypes(self):
        return self.__roomTypes

    @roomTypes.setter
    def roomTypes(self, roomTypes: str):
        self.__roomTypes = roomTypes


    @property
    def promotion(self):
        return self.__promotion

    @promotion.setter
    def promotion(self, promotion: str):
        self.__promotion = promotion


    @property
    def model_Booking10(self):
        return self.__model_Booking10

    @model_Booking10.setter
    def model_Booking10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Booking__model_Booking10", None)
        self.__model_Booking10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Receipt11"):
                opp_val = getattr(old_value, "model_Receipt11", None)
                if opp_val == self:
                    setattr(old_value, "model_Receipt11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Receipt11"):
                opp_val = getattr(value, "model_Receipt11", None)
                setattr(value, "model_Receipt11", self)

    @property
    def model_Booking13(self):
        return self.__model_Booking13

    @model_Booking13.setter
    def model_Booking13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Booking__model_Booking13", None)
        self.__model_Booking13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Room14"):
                    opp_val = getattr(item, "model_Room14", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Room14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Room14"):
                    opp_val = getattr(item, "model_Room14", None)
                    
                    setattr(item, "model_Room14", self)
                    

    @property
    def model_Booking(self):
        return self.__model_Booking

    @model_Booking.setter
    def model_Booking(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Booking__model_Booking", None)
        self.__model_Booking = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Customer"):
                opp_val = getattr(old_value, "model_Customer", None)
                if opp_val == self:
                    setattr(old_value, "model_Customer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Customer"):
                opp_val = getattr(value, "model_Customer", None)
                setattr(value, "model_Customer", self)

    def Booking(self, model_roomTypes, model_rooms, model_promotionCode, model_id, model_customer, model_receipt, model_fromDate, model_toDate, model_wishes):
        # TODO: Implement Booking method
        pass

class model_ReceptionistInterface(ABC):

    def __init__(self):
        
        pass
    def checkOut(self, model_booking) :
        # TODO: Implement checkOut method
        pass

    def getBooking(self, model_bookingNumber) :
        # TODO: Implement getBooking method
        pass

    def createResident(self, model_firstName, model_passportNumber, model_surname) :
        # TODO: Implement createResident method
        pass

    def viewAllBookings(self, model_dateTo, model_dateFrom, model_surname) :
        # TODO: Implement viewAllBookings method
        pass

    def viewUnOccupiedRooms(self) :
        # TODO: Implement viewUnOccupiedRooms method
        pass

    def login(self, model_name, model_password) :
        # TODO: Implement login method
        pass

    def checkIn(self, model_booking, model_rooms) :
        # TODO: Implement checkIn method
        pass

    def removeBooking(self, model_booking) :
        # TODO: Implement removeBooking method
        pass

class model_Customer:

    def __init__(self, firstName: str, surname: str, email: str, adress: str, ccNumber: str, ccv: str, expiringMonth: str, expiringYear: str, model_Customer: "model_Booking" = None):
        self.firstName = firstName
        self.surname = surname
        self.email = email
        self.adress = adress
        self.ccNumber = ccNumber
        self.ccv = ccv
        self.expiringMonth = expiringMonth
        self.expiringYear = expiringYear
        self.model_Customer = model_Customer
        
        pass
    @property
    def expiringYear(self):
        return self.__expiringYear

    @expiringYear.setter
    def expiringYear(self, expiringYear: str):
        self.__expiringYear = expiringYear


    @property
    def ccNumber(self):
        return self.__ccNumber

    @ccNumber.setter
    def ccNumber(self, ccNumber: str):
        self.__ccNumber = ccNumber


    @property
    def expiringMonth(self):
        return self.__expiringMonth

    @expiringMonth.setter
    def expiringMonth(self, expiringMonth: str):
        self.__expiringMonth = expiringMonth


    @property
    def firstName(self):
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName


    @property
    def ccv(self):
        return self.__ccv

    @ccv.setter
    def ccv(self, ccv: str):
        self.__ccv = ccv


    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email


    @property
    def adress(self):
        return self.__adress

    @adress.setter
    def adress(self, adress: str):
        self.__adress = adress


    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname: str):
        self.__surname = surname


    @property
    def model_Customer(self):
        return self.__model_Customer

    @model_Customer.setter
    def model_Customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Customer__model_Customer", None)
        self.__model_Customer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Booking"):
                opp_val = getattr(old_value, "model_Booking", None)
                if opp_val == self:
                    setattr(old_value, "model_Booking", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Booking"):
                opp_val = getattr(value, "model_Booking", None)
                setattr(value, "model_Booking", self)

    def Customer(self, model_ccv, model_email, model_ccExpiringMonth, model_address, model_surname, model_ccNumber, model_ccExpiringYear, model_firstName):
        # TODO: Implement Customer method
        pass

class model_Resident:

    def __init__(self, firstName: str, surname: str, id: str, model_Resident: "model_Room" = None):
        self.firstName = firstName
        self.surname = surname
        self.id = id
        self.model_Resident = model_Resident
        
        pass
    @property
    def firstName(self):
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName


    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname: str):
        self.__surname = surname


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def model_Resident(self):
        return self.__model_Resident

    @model_Resident.setter
    def model_Resident(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Resident__model_Resident", None)
        self.__model_Resident = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Room4"):
                opp_val = getattr(old_value, "model_Room4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Room4"):
                opp_val = getattr(value, "model_Room4", None)
                if opp_val is None:
                    setattr(value, "model_Room4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def Resident(self, model_id, model_surname, model_firstName):
        # TODO: Implement Resident method
        pass

class model_Receipt:

    def __init__(self, totalCost: float, Date: date, id: int, model_Receipt: "model_Room" = None, model_Receipt6: set["model_Expense"] = None, model_Receipt11: "model_Booking" = None):
        self.totalCost = totalCost
        self.Date = Date
        self.id = id
        self.model_Receipt = model_Receipt
        self.model_Receipt6 = model_Receipt6 if model_Receipt6 is not None else set()
        self.model_Receipt11 = model_Receipt11
        
        pass
    @property
    def Date(self):
        return self.__Date

    @Date.setter
    def Date(self, Date: date):
        self.__Date = Date


    @property
    def totalCost(self):
        return self.__totalCost

    @totalCost.setter
    def totalCost(self, totalCost: float):
        self.__totalCost = totalCost


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id


    @property
    def model_Receipt(self):
        return self.__model_Receipt

    @model_Receipt.setter
    def model_Receipt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Receipt__model_Receipt", None)
        self.__model_Receipt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Room2"):
                opp_val = getattr(old_value, "model_Room2", None)
                if opp_val == self:
                    setattr(old_value, "model_Room2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Room2"):
                opp_val = getattr(value, "model_Room2", None)
                setattr(value, "model_Room2", self)

    @property
    def model_Receipt11(self):
        return self.__model_Receipt11

    @model_Receipt11.setter
    def model_Receipt11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Receipt__model_Receipt11", None)
        self.__model_Receipt11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Booking10"):
                opp_val = getattr(old_value, "model_Booking10", None)
                if opp_val == self:
                    setattr(old_value, "model_Booking10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Booking10"):
                opp_val = getattr(value, "model_Booking10", None)
                setattr(value, "model_Booking10", self)

    @property
    def model_Receipt6(self):
        return self.__model_Receipt6

    @model_Receipt6.setter
    def model_Receipt6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Receipt__model_Receipt6", None)
        self.__model_Receipt6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Expense7"):
                    opp_val = getattr(item, "model_Expense7", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Expense7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Expense7"):
                    opp_val = getattr(item, "model_Expense7", None)
                    
                    setattr(item, "model_Expense7", self)
                    

    def removeExpense(self, model_expense) :
        # TODO: Implement removeExpense method
        pass

    def addExpense(self, model_expense) :
        # TODO: Implement addExpense method
        pass

    def Receipt(self, model_id, model_expenses, model_date):
        # TODO: Implement Receipt method
        pass

    def getAllExpenses(self) :
        # TODO: Implement getAllExpenses method
        pass

class model_Expense:

    def __init__(self, price: float, name: str, description: str, date: date, id: int, fixed: bool, receiptId: int, model_Expense: "model_Room" = None, model_Expense7: "model_Receipt" = None):
        self.price = price
        self.name = name
        self.description = description
        self.date = date
        self.id = id
        self.fixed = fixed
        self.receiptId = receiptId
        self.model_Expense = model_Expense
        self.model_Expense7 = model_Expense7
        
        pass
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price


    @property
    def receiptId(self):
        return self.__receiptId

    @receiptId.setter
    def receiptId(self, receiptId: int):
        self.__receiptId = receiptId


    @property
    def fixed(self):
        return self.__fixed

    @fixed.setter
    def fixed(self, fixed: bool):
        self.__fixed = fixed


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id


    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def model_Expense(self):
        return self.__model_Expense

    @model_Expense.setter
    def model_Expense(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Expense__model_Expense", None)
        self.__model_Expense = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Room"):
                opp_val = getattr(old_value, "model_Room", None)
                if opp_val == self:
                    setattr(old_value, "model_Room", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Room"):
                opp_val = getattr(value, "model_Room", None)
                setattr(value, "model_Room", self)

    @property
    def model_Expense7(self):
        return self.__model_Expense7

    @model_Expense7.setter
    def model_Expense7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Expense__model_Expense7", None)
        self.__model_Expense7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Receipt6"):
                opp_val = getattr(old_value, "model_Receipt6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Receipt6"):
                opp_val = getattr(value, "model_Receipt6", None)
                if opp_val is None:
                    setattr(value, "model_Receipt6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def Expense(self, model_id, model_name, model_receiptID, model_isFixed, model_description, model_price, model_date):
        # TODO: Implement Expense method
        pass

class model_Room:

    def __init__(self, number: str, description: str, clean: str, type: str, beds: str, status: str, model_Room: "model_Expense" = None, model_Room2: "model_Receipt" = None, model_Room4: set["model_Resident"] = None, model_Room14: "model_Booking" = None):
        self.number = number
        self.description = description
        self.clean = clean
        self.type = type
        self.beds = beds
        self.status = status
        self.model_Room = model_Room
        self.model_Room2 = model_Room2
        self.model_Room4 = model_Room4 if model_Room4 is not None else set()
        self.model_Room14 = model_Room14
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number


    @property
    def beds(self):
        return self.__beds

    @beds.setter
    def beds(self, beds: str):
        self.__beds = beds


    @property
    def clean(self):
        return self.__clean

    @clean.setter
    def clean(self, clean: str):
        self.__clean = clean


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status


    @property
    def model_Room14(self):
        return self.__model_Room14

    @model_Room14.setter
    def model_Room14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Room__model_Room14", None)
        self.__model_Room14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Booking13"):
                opp_val = getattr(old_value, "model_Booking13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Booking13"):
                opp_val = getattr(value, "model_Booking13", None)
                if opp_val is None:
                    setattr(value, "model_Booking13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Room4(self):
        return self.__model_Room4

    @model_Room4.setter
    def model_Room4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Room__model_Room4", None)
        self.__model_Room4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Resident"):
                    opp_val = getattr(item, "model_Resident", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Resident", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Resident"):
                    opp_val = getattr(item, "model_Resident", None)
                    
                    setattr(item, "model_Resident", self)
                    

    @property
    def model_Room(self):
        return self.__model_Room

    @model_Room.setter
    def model_Room(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Room__model_Room", None)
        self.__model_Room = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Expense"):
                opp_val = getattr(old_value, "model_Expense", None)
                if opp_val == self:
                    setattr(old_value, "model_Expense", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Expense"):
                opp_val = getattr(value, "model_Expense", None)
                setattr(value, "model_Expense", self)

    @property
    def model_Room2(self):
        return self.__model_Room2

    @model_Room2.setter
    def model_Room2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Room__model_Room2", None)
        self.__model_Room2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Receipt"):
                opp_val = getattr(old_value, "model_Receipt", None)
                if opp_val == self:
                    setattr(old_value, "model_Receipt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Receipt"):
                opp_val = getattr(value, "model_Receipt", None)
                setattr(value, "model_Receipt", self)

    def Room(self, model_status, model_beds, model_description, model_price, model_number, model_receipt, model_type):
        # TODO: Implement Room method
        pass

class model_CustomerInterface(ABC):

    def __init__(self):
        
        pass
    def createBooking(self, model_toDate, model_customer, model_receipt, model_roomTypes, model_wishes, model_promotion, model_fromDate) :
        # TODO: Implement createBooking method
        pass

    def searchRooms(self, model_dateFrom, model_numberOfRooms, model_dateTo, model_numberOfGuests) :
        # TODO: Implement searchRooms method
        pass

    def pay(self, model_customer, model_receipt) :
        # TODO: Implement pay method
        pass

    def createCustomer(self, model_firstName, model_email, model_ccv, model_ccNumber, model_surname, model_expiringMonth, model_expriningYear, model_address) :
        # TODO: Implement createCustomer method
        pass

    def validateCard(self, model_customer) :
        # TODO: Implement validateCard method
        pass

class model_BankInterface(ABC):

    pass
class model_Admin:

    pass
class model_Customers:

    pass
class model_Receptionist:

    pass
class model_HotelComponent:

    pass
class model_BankComponent:

    pass