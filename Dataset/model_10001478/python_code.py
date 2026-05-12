from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Online_Order_and_CC_processing_Actor:

    pass


class Customer_Actor:

    pass





class chefTicket:

    pass


class Store_POS_System:

    def __init__(self, print: str, chefTicket29: "chefTicket" = None):
        self.print = print
        self.chefTicket29 = chefTicket29
        
        pass
    @property
    def print(self):
        return self.__print
    @print.setter
    def print(self, print: str):
        self.__print = print

    @property
    def chefTicket29(self):
        return self.__chefTicket29
    @chefTicket29.setter
    def chefTicket29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Store_POS_System__chefTicket29", None)
        self.__chefTicket29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "store_POS_System8"):
                opp_val = getattr(old_value, "store_POS_System8", None)
                if opp_val == self:
                    setattr(old_value, "store_POS_System8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "store_POS_System8"):
                opp_val = getattr(value, "store_POS_System8", None)
                setattr(value, "store_POS_System8", self)



class deleteOrder:

    pass


class viewOrder:

    pass


class updatePayment:

    def __init__(self, paymentInformation: str, customer5: "Customer" = None):
        self.paymentInformation = paymentInformation
        self.customer5 = customer5
        
        pass
    @property
    def paymentInformation(self):
        return self.__paymentInformation
    @paymentInformation.setter
    def paymentInformation(self, paymentInformation: str):
        self.__paymentInformation = paymentInformation

    @property
    def customer5(self):
        return self.__customer5
    @customer5.setter
    def customer5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_updatePayment__customer5", None)
        self.__customer5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "updatePayment24"):
                opp_val = getattr(old_value, "updatePayment24", None)
                if opp_val == self:
                    setattr(old_value, "updatePayment24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "updatePayment24"):
                opp_val = getattr(value, "updatePayment24", None)
                setattr(value, "updatePayment24", self)



class createOrder:

    def __init__(self, orderedItems: str, customer3: "Customer" = None):
        self.orderedItems = orderedItems
        self.customer3 = customer3
        
        pass
    @property
    def orderedItems(self):
        return self.__orderedItems
    @orderedItems.setter
    def orderedItems(self, orderedItems: str):
        self.__orderedItems = orderedItems

    @property
    def customer3(self):
        return self.__customer3
    @customer3.setter
    def customer3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_createOrder__customer3", None)
        self.__customer3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "createOrder22"):
                opp_val = getattr(old_value, "createOrder22", None)
                if opp_val == self:
                    setattr(old_value, "createOrder22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "createOrder22"):
                opp_val = getattr(value, "createOrder22", None)
                setattr(value, "createOrder22", self)



class Online_Order_and_CC_Processing:

    def __init__(self, order: str, payment: str, paymentApproved: bool, customer1: "Customer" = None, chefTicket210: "chefTicket" = None):
        self.order = order
        self.payment = payment
        self.paymentApproved = paymentApproved
        self.customer1 = customer1
        self.chefTicket210 = chefTicket210
        
        pass
    @property
    def payment(self):
        return self.__payment
    @payment.setter
    def payment(self, payment: str):
        self.__payment = payment

    @property
    def paymentApproved(self):
        return self.__paymentApproved
    @paymentApproved.setter
    def paymentApproved(self, paymentApproved: bool):
        self.__paymentApproved = paymentApproved

    @property
    def order(self):
        return self.__order
    @order.setter
    def order(self, order: str):
        self.__order = order

    @property
    def customer1(self):
        return self.__customer1
    @customer1.setter
    def customer1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Order_and_CC_Processing__customer1", None)
        self.__customer1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Online_Order_and_CC_Processing0"):
                opp_val = getattr(old_value, "Online_Order_and_CC_Processing0", None)
                if opp_val == self:
                    setattr(old_value, "Online_Order_and_CC_Processing0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Online_Order_and_CC_Processing0"):
                opp_val = getattr(value, "Online_Order_and_CC_Processing0", None)
                setattr(value, "Online_Order_and_CC_Processing0", self)

    @property
    def chefTicket210(self):
        return self.__chefTicket210
    @chefTicket210.setter
    def chefTicket210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Order_and_CC_Processing__chefTicket210", None)
        self.__chefTicket210 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "online_Order_and_CC_Processing11"):
                opp_val = getattr(old_value, "online_Order_and_CC_Processing11", None)
                if opp_val == self:
                    setattr(old_value, "online_Order_and_CC_Processing11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "online_Order_and_CC_Processing11"):
                opp_val = getattr(value, "online_Order_and_CC_Processing11", None)
                setattr(value, "online_Order_and_CC_Processing11", self)



class Customer:

    def __init__(self, name: str, location: str, Online_Order_and_CC_Processing0: "Online_Order_and_CC_Processing" = None, createOrder22: "createOrder" = None, updatePayment24: "updatePayment" = None, deleteOrder26: "deleteOrder" = None):
        self.name = name
        self.location = location
        self.Online_Order_and_CC_Processing0 = Online_Order_and_CC_Processing0
        self.createOrder22 = createOrder22
        self.updatePayment24 = updatePayment24
        self.deleteOrder26 = deleteOrder26
        
        pass
    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def createOrder22(self):
        return self.__createOrder22
    @createOrder22.setter
    def createOrder22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__createOrder22", None)
        self.__createOrder22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer3"):
                opp_val = getattr(old_value, "customer3", None)
                if opp_val == self:
                    setattr(old_value, "customer3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer3"):
                opp_val = getattr(value, "customer3", None)
                setattr(value, "customer3", self)

    @property
    def updatePayment24(self):
        return self.__updatePayment24
    @updatePayment24.setter
    def updatePayment24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__updatePayment24", None)
        self.__updatePayment24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer5"):
                opp_val = getattr(old_value, "customer5", None)
                if opp_val == self:
                    setattr(old_value, "customer5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer5"):
                opp_val = getattr(value, "customer5", None)
                setattr(value, "customer5", self)

    @property
    def Online_Order_and_CC_Processing0(self):
        return self.__Online_Order_and_CC_Processing0
    @Online_Order_and_CC_Processing0.setter
    def Online_Order_and_CC_Processing0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__Online_Order_and_CC_Processing0", None)
        self.__Online_Order_and_CC_Processing0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer1"):
                opp_val = getattr(old_value, "customer1", None)
                if opp_val == self:
                    setattr(old_value, "customer1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer1"):
                opp_val = getattr(value, "customer1", None)
                setattr(value, "customer1", self)

    @property
    def deleteOrder26(self):
        return self.__deleteOrder26
    @deleteOrder26.setter
    def deleteOrder26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__deleteOrder26", None)
        self.__deleteOrder26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer7"):
                opp_val = getattr(old_value, "customer7", None)
                if opp_val == self:
                    setattr(old_value, "customer7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer7"):
                opp_val = getattr(value, "customer7", None)
                setattr(value, "customer7", self)

