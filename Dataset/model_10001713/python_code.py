from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Manager:

    def __init__(self, name: str, password: str, menu28: "Menu" = None):
        self.name = name
        self.password = password
        self.menu28 = menu28
        
        pass
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
    def menu28(self):
        return self.__menu28
    @menu28.setter
    def menu28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Manager__menu28", None)
        self.__menu28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "manager29"):
                opp_val = getattr(old_value, "manager29", None)
                if opp_val == self:
                    setattr(old_value, "manager29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "manager29"):
                opp_val = getattr(value, "manager29", None)
                setattr(value, "manager29", self)



class Drink:

    def __init__(self, name: str, price: str, quantity: int, sales_Line_Item17: "Sales_Line_Item" = None):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.sales_Line_Item17 = sales_Line_Item17
        
        pass
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: str):
        self.__price = price

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def sales_Line_Item17(self):
        return self.__sales_Line_Item17
    @sales_Line_Item17.setter
    def sales_Line_Item17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Drink__sales_Line_Item17", None)
        self.__sales_Line_Item17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drink16"):
                opp_val = getattr(old_value, "drink16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drink16"):
                opp_val = getattr(value, "drink16", None)
                if opp_val is None:
                    setattr(value, "drink16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Order:

    def __init__(self, customer: str, foodName: str, foodPrice: int, drinkName: str, drinkPrice: int, payment13: "Payment" = None):
        self.customer = customer
        self.foodName = foodName
        self.foodPrice = foodPrice
        self.drinkName = drinkName
        self.drinkPrice = drinkPrice
        self.payment13 = payment13
        
        pass
    @property
    def foodPrice(self):
        return self.__foodPrice
    @foodPrice.setter
    def foodPrice(self, foodPrice: int):
        self.__foodPrice = foodPrice

    @property
    def foodName(self):
        return self.__foodName
    @foodName.setter
    def foodName(self, foodName: str):
        self.__foodName = foodName

    @property
    def drinkPrice(self):
        return self.__drinkPrice
    @drinkPrice.setter
    def drinkPrice(self, drinkPrice: int):
        self.__drinkPrice = drinkPrice

    @property
    def customer(self):
        return self.__customer
    @customer.setter
    def customer(self, customer: str):
        self.__customer = customer

    @property
    def drinkName(self):
        return self.__drinkName
    @drinkName.setter
    def drinkName(self, drinkName: str):
        self.__drinkName = drinkName

    @property
    def payment13(self):
        return self.__payment13
    @payment13.setter
    def payment13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__payment13", None)
        self.__payment13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order12"):
                opp_val = getattr(old_value, "order12", None)
                if opp_val == self:
                    setattr(old_value, "order12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order12"):
                opp_val = getattr(value, "order12", None)
                setattr(value, "order12", self)



class Food:

    def __init__(self, name: str, price: str, quantity: int, attribute: str, sales_Line_Item15: "Sales_Line_Item" = None):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.attribute = attribute
        self.sales_Line_Item15 = sales_Line_Item15
        
        pass
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: str):
        self.__price = price

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sales_Line_Item15(self):
        return self.__sales_Line_Item15
    @sales_Line_Item15.setter
    def sales_Line_Item15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Food__sales_Line_Item15", None)
        self.__sales_Line_Item15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "food14"):
                opp_val = getattr(old_value, "food14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "food14"):
                opp_val = getattr(value, "food14", None)
                if opp_val is None:
                    setattr(value, "food14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class customerDatabase:

    def __init__(self, customerName: str, paymentHistory: str, SUID: int, creditCardNum: int, card20: set["Card"] = None):
        self.customerName = customerName
        self.paymentHistory = paymentHistory
        self.SUID = SUID
        self.creditCardNum = creditCardNum
        self.card20 = card20 if card20 is not None else set()
        
        pass
    @property
    def paymentHistory(self):
        return self.__paymentHistory
    @paymentHistory.setter
    def paymentHistory(self, paymentHistory: str):
        self.__paymentHistory = paymentHistory

    @property
    def creditCardNum(self):
        return self.__creditCardNum
    @creditCardNum.setter
    def creditCardNum(self, creditCardNum: int):
        self.__creditCardNum = creditCardNum

    @property
    def customerName(self):
        return self.__customerName
    @customerName.setter
    def customerName(self, customerName: str):
        self.__customerName = customerName

    @property
    def SUID(self):
        return self.__SUID
    @SUID.setter
    def SUID(self, SUID: int):
        self.__SUID = SUID

    @property
    def card20(self):
        return self.__card20
    @card20.setter
    def card20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_customerDatabase__card20", None)
        self.__card20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customerDatabase21"):
                    opp_val = getattr(item, "customerDatabase21", None)
                    
                    if opp_val == self:
                        setattr(item, "customerDatabase21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customerDatabase21"):
                    opp_val = getattr(item, "customerDatabase21", None)
                    
                    setattr(item, "customerDatabase21", self)
                    



class Payment:

    def __init__(self, amount: str, sale9: "Sale" = None, order12: "Order" = None, sUID25: set["SUID"] = None):
        self.amount = amount
        self.sale9 = sale9
        self.order12 = order12
        self.sUID25 = sUID25 if sUID25 is not None else set()
        
        pass
    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: str):
        self.__amount = amount

    @property
    def sale9(self):
        return self.__sale9
    @sale9.setter
    def sale9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__sale9", None)
        self.__sale9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment8"):
                opp_val = getattr(old_value, "payment8", None)
                if opp_val == self:
                    setattr(old_value, "payment8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment8"):
                opp_val = getattr(value, "payment8", None)
                setattr(value, "payment8", self)

    @property
    def order12(self):
        return self.__order12
    @order12.setter
    def order12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__order12", None)
        self.__order12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment13"):
                opp_val = getattr(old_value, "payment13", None)
                if opp_val == self:
                    setattr(old_value, "payment13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment13"):
                opp_val = getattr(value, "payment13", None)
                setattr(value, "payment13", self)

    @property
    def sUID25(self):
        return self.__sUID25
    @sUID25.setter
    def sUID25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__sUID25", None)
        self.__sUID25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "payment24"):
                    opp_val = getattr(item, "payment24", None)
                    
                    if opp_val == self:
                        setattr(item, "payment24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "payment24"):
                    opp_val = getattr(item, "payment24", None)
                    
                    setattr(item, "payment24", self)
                    



class SUID:

    def __init__(self, ID: int, studentName: str, suFOODBal: str, card22: "Card" = None, payment24: "Payment" = None):
        self.ID = ID
        self.studentName = studentName
        self.suFOODBal = suFOODBal
        self.card22 = card22
        self.payment24 = payment24
        
        pass
    @property
    def suFOODBal(self):
        return self.__suFOODBal
    @suFOODBal.setter
    def suFOODBal(self, suFOODBal: str):
        self.__suFOODBal = suFOODBal

    @property
    def studentName(self):
        return self.__studentName
    @studentName.setter
    def studentName(self, studentName: str):
        self.__studentName = studentName

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def payment24(self):
        return self.__payment24
    @payment24.setter
    def payment24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SUID__payment24", None)
        self.__payment24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sUID25"):
                opp_val = getattr(old_value, "sUID25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sUID25"):
                opp_val = getattr(value, "sUID25", None)
                if opp_val is None:
                    setattr(value, "sUID25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def card22(self):
        return self.__card22
    @card22.setter
    def card22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SUID__card22", None)
        self.__card22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sUID23"):
                opp_val = getattr(old_value, "sUID23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sUID23"):
                opp_val = getattr(value, "sUID23", None)
                if opp_val is None:
                    setattr(value, "sUID23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Card:

    def __init__(self, isCredit: bool, isDebit: bool, cardNumber: int, cardholderName: str, cardSN: int, customerDatabase21: "customerDatabase" = None, sUID23: set["SUID"] = None):
        self.isCredit = isCredit
        self.isDebit = isDebit
        self.cardNumber = cardNumber
        self.cardholderName = cardholderName
        self.cardSN = cardSN
        self.customerDatabase21 = customerDatabase21
        self.sUID23 = sUID23 if sUID23 is not None else set()
        
        pass
    @property
    def isDebit(self):
        return self.__isDebit
    @isDebit.setter
    def isDebit(self, isDebit: bool):
        self.__isDebit = isDebit

    @property
    def isCredit(self):
        return self.__isCredit
    @isCredit.setter
    def isCredit(self, isCredit: bool):
        self.__isCredit = isCredit

    @property
    def cardNumber(self):
        return self.__cardNumber
    @cardNumber.setter
    def cardNumber(self, cardNumber: int):
        self.__cardNumber = cardNumber

    @property
    def cardSN(self):
        return self.__cardSN
    @cardSN.setter
    def cardSN(self, cardSN: int):
        self.__cardSN = cardSN

    @property
    def cardholderName(self):
        return self.__cardholderName
    @cardholderName.setter
    def cardholderName(self, cardholderName: str):
        self.__cardholderName = cardholderName

    @property
    def customerDatabase21(self):
        return self.__customerDatabase21
    @customerDatabase21.setter
    def customerDatabase21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__customerDatabase21", None)
        self.__customerDatabase21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card20"):
                opp_val = getattr(old_value, "card20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card20"):
                opp_val = getattr(value, "card20", None)
                if opp_val is None:
                    setattr(value, "card20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sUID23(self):
        return self.__sUID23
    @sUID23.setter
    def sUID23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__sUID23", None)
        self.__sUID23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "card22"):
                    opp_val = getattr(item, "card22", None)
                    
                    if opp_val == self:
                        setattr(item, "card22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "card22"):
                    opp_val = getattr(item, "card22", None)
                    
                    setattr(item, "card22", self)
                    



class CardReader:

    def __init__(self, attribute: str, sale19: "Sale" = None):
        self.attribute = attribute
        self.sale19 = sale19
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def sale19(self):
        return self.__sale19
    @sale19.setter
    def sale19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CardReader__sale19", None)
        self.__sale19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cardReader18"):
                opp_val = getattr(old_value, "cardReader18", None)
                if opp_val == self:
                    setattr(old_value, "cardReader18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cardReader18"):
                opp_val = getattr(value, "cardReader18", None)
                setattr(value, "cardReader18", self)



class Register:

    def __init__(self, attribute: str, store0: "Store" = None, sale6: "Sale" = None):
        self.attribute = attribute
        self.store0 = store0
        self.sale6 = sale6
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def sale6(self):
        return self.__sale6
    @sale6.setter
    def sale6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Register__sale6", None)
        self.__sale6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "register7"):
                opp_val = getattr(old_value, "register7", None)
                if opp_val == self:
                    setattr(old_value, "register7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "register7"):
                opp_val = getattr(value, "register7", None)
                setattr(value, "register7", self)

    @property
    def store0(self):
        return self.__store0
    @store0.setter
    def store0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Register__store0", None)
        self.__store0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "register1"):
                opp_val = getattr(old_value, "register1", None)
                if opp_val == self:
                    setattr(old_value, "register1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "register1"):
                opp_val = getattr(value, "register1", None)
                setattr(value, "register1", self)



class Sale:

    def __init__(self, Date: str, Time: str, isComplete: bool, register7: "Register" = None, payment8: "Payment" = None, sales_Line_Item10: set["Sales_Line_Item"] = None, cardReader18: "CardReader" = None):
        self.Date = Date
        self.Time = Time
        self.isComplete = isComplete
        self.register7 = register7
        self.payment8 = payment8
        self.sales_Line_Item10 = sales_Line_Item10 if sales_Line_Item10 is not None else set()
        self.cardReader18 = cardReader18
        
        pass
    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: str):
        self.__Date = Date

    @property
    def Time(self):
        return self.__Time
    @Time.setter
    def Time(self, Time: str):
        self.__Time = Time

    @property
    def isComplete(self):
        return self.__isComplete
    @isComplete.setter
    def isComplete(self, isComplete: bool):
        self.__isComplete = isComplete

    @property
    def sales_Line_Item10(self):
        return self.__sales_Line_Item10
    @sales_Line_Item10.setter
    def sales_Line_Item10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sale__sales_Line_Item10", None)
        self.__sales_Line_Item10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sale11"):
                    opp_val = getattr(item, "sale11", None)
                    
                    if opp_val == self:
                        setattr(item, "sale11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sale11"):
                    opp_val = getattr(item, "sale11", None)
                    
                    setattr(item, "sale11", self)
                    

    @property
    def register7(self):
        return self.__register7
    @register7.setter
    def register7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sale__register7", None)
        self.__register7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sale6"):
                opp_val = getattr(old_value, "sale6", None)
                if opp_val == self:
                    setattr(old_value, "sale6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sale6"):
                opp_val = getattr(value, "sale6", None)
                setattr(value, "sale6", self)

    @property
    def payment8(self):
        return self.__payment8
    @payment8.setter
    def payment8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sale__payment8", None)
        self.__payment8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sale9"):
                opp_val = getattr(old_value, "sale9", None)
                if opp_val == self:
                    setattr(old_value, "sale9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sale9"):
                opp_val = getattr(value, "sale9", None)
                setattr(value, "sale9", self)

    @property
    def cardReader18(self):
        return self.__cardReader18
    @cardReader18.setter
    def cardReader18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sale__cardReader18", None)
        self.__cardReader18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sale19"):
                opp_val = getattr(old_value, "sale19", None)
                if opp_val == self:
                    setattr(old_value, "sale19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sale19"):
                opp_val = getattr(value, "sale19", None)
                setattr(value, "sale19", self)



class Sales_Line_Item:

    def __init__(self, Quantity: int, sale11: "Sale" = None, food14: set["Food"] = None, drink16: set["Drink"] = None, product27: "Product" = None):
        self.Quantity = Quantity
        self.sale11 = sale11
        self.food14 = food14 if food14 is not None else set()
        self.drink16 = drink16 if drink16 is not None else set()
        self.product27 = product27
        
        pass
    @property
    def Quantity(self):
        return self.__Quantity
    @Quantity.setter
    def Quantity(self, Quantity: int):
        self.__Quantity = Quantity

    @property
    def food14(self):
        return self.__food14
    @food14.setter
    def food14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sales_Line_Item__food14", None)
        self.__food14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sales_Line_Item15"):
                    opp_val = getattr(item, "sales_Line_Item15", None)
                    
                    if opp_val == self:
                        setattr(item, "sales_Line_Item15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sales_Line_Item15"):
                    opp_val = getattr(item, "sales_Line_Item15", None)
                    
                    setattr(item, "sales_Line_Item15", self)
                    

    @property
    def product27(self):
        return self.__product27
    @product27.setter
    def product27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sales_Line_Item__product27", None)
        self.__product27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sales_Line_Item26"):
                opp_val = getattr(old_value, "sales_Line_Item26", None)
                if opp_val == self:
                    setattr(old_value, "sales_Line_Item26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sales_Line_Item26"):
                opp_val = getattr(value, "sales_Line_Item26", None)
                setattr(value, "sales_Line_Item26", self)

    @property
    def sale11(self):
        return self.__sale11
    @sale11.setter
    def sale11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sales_Line_Item__sale11", None)
        self.__sale11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sales_Line_Item10"):
                opp_val = getattr(old_value, "sales_Line_Item10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sales_Line_Item10"):
                opp_val = getattr(value, "sales_Line_Item10", None)
                if opp_val is None:
                    setattr(value, "sales_Line_Item10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def drink16(self):
        return self.__drink16
    @drink16.setter
    def drink16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sales_Line_Item__drink16", None)
        self.__drink16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sales_Line_Item17"):
                    opp_val = getattr(item, "sales_Line_Item17", None)
                    
                    if opp_val == self:
                        setattr(item, "sales_Line_Item17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sales_Line_Item17"):
                    opp_val = getattr(item, "sales_Line_Item17", None)
                    
                    setattr(item, "sales_Line_Item17", self)
                    



class Product:

    def __init__(self, name: str, description: str, itemID: int, price: str, menu5: "Menu" = None, sales_Line_Item26: "Sales_Line_Item" = None):
        self.name = name
        self.description = description
        self.itemID = itemID
        self.price = price
        self.menu5 = menu5
        self.sales_Line_Item26 = sales_Line_Item26
        
        pass
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: str):
        self.__price = price

    @property
    def itemID(self):
        return self.__itemID
    @itemID.setter
    def itemID(self, itemID: int):
        self.__itemID = itemID

    @property
    def menu5(self):
        return self.__menu5
    @menu5.setter
    def menu5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__menu5", None)
        self.__menu5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product4"):
                opp_val = getattr(old_value, "product4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product4"):
                opp_val = getattr(value, "product4", None)
                if opp_val is None:
                    setattr(value, "product4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sales_Line_Item26(self):
        return self.__sales_Line_Item26
    @sales_Line_Item26.setter
    def sales_Line_Item26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__sales_Line_Item26", None)
        self.__sales_Line_Item26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product27"):
                opp_val = getattr(old_value, "product27", None)
                if opp_val == self:
                    setattr(old_value, "product27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product27"):
                opp_val = getattr(value, "product27", None)
                setattr(value, "product27", self)



class Menu:

    def __init__(self, _attr: str, store3: "Store" = None, product4: set["Product"] = None, manager29: "Manager" = None):
        self._attr = _attr
        self.store3 = store3
        self.product4 = product4 if product4 is not None else set()
        self.manager29 = manager29
        
        pass
    @property
    def _attr(self):
        return self.___attr
    @_attr.setter
    def _attr(self, _attr: str):
        self.___attr = _attr

    @property
    def manager29(self):
        return self.__manager29
    @manager29.setter
    def manager29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Menu__manager29", None)
        self.__manager29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "menu28"):
                opp_val = getattr(old_value, "menu28", None)
                if opp_val == self:
                    setattr(old_value, "menu28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "menu28"):
                opp_val = getattr(value, "menu28", None)
                setattr(value, "menu28", self)

    @property
    def store3(self):
        return self.__store3
    @store3.setter
    def store3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Menu__store3", None)
        self.__store3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "menu2"):
                opp_val = getattr(old_value, "menu2", None)
                if opp_val == self:
                    setattr(old_value, "menu2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "menu2"):
                opp_val = getattr(value, "menu2", None)
                setattr(value, "menu2", self)

    @property
    def product4(self):
        return self.__product4
    @product4.setter
    def product4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Menu__product4", None)
        self.__product4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "menu5"):
                    opp_val = getattr(item, "menu5", None)
                    
                    if opp_val == self:
                        setattr(item, "menu5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "menu5"):
                    opp_val = getattr(item, "menu5", None)
                    
                    setattr(item, "menu5", self)
                    



class Store:

    def __init__(self, Address: str, Name: str, register1: "Register" = None, menu2: "Menu" = None):
        self.Address = Address
        self.Name = Name
        self.register1 = register1
        self.menu2 = menu2
        
        pass
    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def menu2(self):
        return self.__menu2
    @menu2.setter
    def menu2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Store__menu2", None)
        self.__menu2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "store3"):
                opp_val = getattr(old_value, "store3", None)
                if opp_val == self:
                    setattr(old_value, "store3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "store3"):
                opp_val = getattr(value, "store3", None)
                setattr(value, "store3", self)

    @property
    def register1(self):
        return self.__register1
    @register1.setter
    def register1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Store__register1", None)
        self.__register1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "store0"):
                opp_val = getattr(old_value, "store0", None)
                if opp_val == self:
                    setattr(old_value, "store0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "store0"):
                opp_val = getattr(value, "store0", None)
                setattr(value, "store0", self)

