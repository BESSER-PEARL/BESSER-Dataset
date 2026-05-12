from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class login_or_sign_in_page_UseCase:

    pass


class Bank_Actor:

    pass


class Authentication_Service_or_identity_provider_Actor:

    pass


class Credit__shop_credit_card_or_PayPal_payments_UseCase:

    pass


class User_authentication_cookie__UseCase:

    pass


class Credit_payment_service_Actor:

    pass


class Customer_authentication_UseCase:

    pass


class UseCase_UseCase:

    pass


class Save_items_for_later_UseCase:

    pass


class Add_items_to_shopping_cart_UseCase:

    pass


class View_recommended_items_UseCase:

    pass


class Browse_catalogue_UseCase:

    pass


class Search_for_items_UseCase:

    pass


class PayPal_Mastercard_etc_UseCase:

    pass


class Move_items_into_basket_UseCase:

    pass


class View_Items_UseCase:

    pass


class Payment_UseCase:

    pass


class Checkout_UseCase:

    pass


class Points_and_Special_Offers_UseCase:

    pass


class Authentication_UseCase:

    pass


class Register_UseCase:

    pass


class Login_UseCase:

    pass


class Customer_Actor:

    pass





class str:

    pass


class Online_Shopping_Order:

    def __init__(self, Placed_Date: str, Contents: Online_Shopping_Order_Item, order_Item46: "Online_Shopping_Order_Item" = None, card_Payment43: "Online_Shopping_Card_Payment" = None, paypal_Payment45: "Online_Shopping_Paypal_Payment" = None):
        self.Placed_Date = Placed_Date
        self.Contents = Contents
        self.order_Item46 = order_Item46
        self.card_Payment43 = card_Payment43
        self.paypal_Payment45 = paypal_Payment45
        
        pass
    @property
    def Contents(self):
        return self.__Contents
    @Contents.setter
    def Contents(self, Contents: Online_Shopping_Order_Item):
        self.__Contents = Contents

    @property
    def Placed_Date(self):
        return self.__Placed_Date
    @Placed_Date.setter
    def Placed_Date(self, Placed_Date: str):
        self.__Placed_Date = Placed_Date

    @property
    def card_Payment43(self):
        return self.__card_Payment43
    @card_Payment43.setter
    def card_Payment43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Order__card_Payment43", None)
        self.__card_Payment43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order42"):
                opp_val = getattr(old_value, "order42", None)
                if opp_val == self:
                    setattr(old_value, "order42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order42"):
                opp_val = getattr(value, "order42", None)
                setattr(value, "order42", self)

    @property
    def paypal_Payment45(self):
        return self.__paypal_Payment45
    @paypal_Payment45.setter
    def paypal_Payment45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Order__paypal_Payment45", None)
        self.__paypal_Payment45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order44"):
                opp_val = getattr(old_value, "order44", None)
                if opp_val == self:
                    setattr(old_value, "order44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order44"):
                opp_val = getattr(value, "order44", None)
                setattr(value, "order44", self)

    @property
    def order_Item46(self):
        return self.__order_Item46
    @order_Item46.setter
    def order_Item46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Order__order_Item46", None)
        self.__order_Item46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Order47"):
                opp_val = getattr(old_value, "Order47", None)
                if opp_val == self:
                    setattr(old_value, "Order47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Order47"):
                opp_val = getattr(value, "Order47", None)
                setattr(value, "Order47", self)



class Online_Shopping_Points___Special_Offers:

    def __init__(self, Discount: int, customer_Account29: "Online_Shopping_Customer_Account" = None):
        self.Discount = Discount
        self.customer_Account29 = customer_Account29
        
        pass
    @property
    def Discount(self):
        return self.__Discount
    @Discount.setter
    def Discount(self, Discount: int):
        self.__Discount = Discount

    @property
    def customer_Account29(self):
        return self.__customer_Account29
    @customer_Account29.setter
    def customer_Account29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Points___Special_Offers__customer_Account29", None)
        self.__customer_Account29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "points___Special_Offers28"):
                opp_val = getattr(old_value, "points___Special_Offers28", None)
                if opp_val == self:
                    setattr(old_value, "points___Special_Offers28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "points___Special_Offers28"):
                opp_val = getattr(value, "points___Special_Offers28", None)
                setattr(value, "points___Special_Offers28", self)



class Online_Shopping_Order_Item:

    def __init__(self, Product_ID: str, Quantity: int, SubTotal: str, Order47: "Online_Shopping_Order" = None):
        self.Product_ID = Product_ID
        self.Quantity = Quantity
        self.SubTotal = SubTotal
        self.Order47 = Order47
        
        pass
    @property
    def Product_ID(self):
        return self.__Product_ID
    @Product_ID.setter
    def Product_ID(self, Product_ID: str):
        self.__Product_ID = Product_ID

    @property
    def Quantity(self):
        return self.__Quantity
    @Quantity.setter
    def Quantity(self, Quantity: int):
        self.__Quantity = Quantity

    @property
    def SubTotal(self):
        return self.__SubTotal
    @SubTotal.setter
    def SubTotal(self, SubTotal: str):
        self.__SubTotal = SubTotal

    @property
    def Order47(self):
        return self.__Order47
    @Order47.setter
    def Order47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Order_Item__Order47", None)
        self.__Order47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order_Item46"):
                opp_val = getattr(old_value, "order_Item46", None)
                if opp_val == self:
                    setattr(old_value, "order_Item46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order_Item46"):
                opp_val = getattr(value, "order_Item46", None)
                setattr(value, "order_Item46", self)



class Online_Shopping_Shopping_Cart_Item:

    def __init__(self, Price: int, Quantity: str, shopping_Cart35: "Online_Shopping_Shopping_Cart" = None):
        self.Price = Price
        self.Quantity = Quantity
        self.shopping_Cart35 = shopping_Cart35
        
        pass
    @property
    def Quantity(self):
        return self.__Quantity
    @Quantity.setter
    def Quantity(self, Quantity: str):
        self.__Quantity = Quantity

    @property
    def Price(self):
        return self.__Price
    @Price.setter
    def Price(self, Price: int):
        self.__Price = Price

    @property
    def shopping_Cart35(self):
        return self.__shopping_Cart35
    @shopping_Cart35.setter
    def shopping_Cart35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Shopping_Cart_Item__shopping_Cart35", None)
        self.__shopping_Cart35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shopping_Cart_Item34"):
                opp_val = getattr(old_value, "shopping_Cart_Item34", None)
                if opp_val == self:
                    setattr(old_value, "shopping_Cart_Item34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shopping_Cart_Item34"):
                opp_val = getattr(value, "shopping_Cart_Item34", None)
                setattr(value, "shopping_Cart_Item34", self)



class Online_Shopping_Customer_Account:

    def __init__(self, Username: str, Password: str, points___Special_Offers28: "Online_Shopping_Points___Special_Offers" = None, item30: "Online_Shopping_Item" = None):
        self.Username = Username
        self.Password = Password
        self.points___Special_Offers28 = points___Special_Offers28
        self.item30 = item30
        
        pass
    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def Username(self):
        return self.__Username
    @Username.setter
    def Username(self, Username: str):
        self.__Username = Username

    @property
    def points___Special_Offers28(self):
        return self.__points___Special_Offers28
    @points___Special_Offers28.setter
    def points___Special_Offers28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Customer_Account__points___Special_Offers28", None)
        self.__points___Special_Offers28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer_Account29"):
                opp_val = getattr(old_value, "customer_Account29", None)
                if opp_val == self:
                    setattr(old_value, "customer_Account29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer_Account29"):
                opp_val = getattr(value, "customer_Account29", None)
                setattr(value, "customer_Account29", self)

    @property
    def item30(self):
        return self.__item30
    @item30.setter
    def item30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Customer_Account__item30", None)
        self.__item30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer_Account31"):
                opp_val = getattr(old_value, "customer_Account31", None)
                if opp_val == self:
                    setattr(old_value, "customer_Account31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer_Account31"):
                opp_val = getattr(value, "customer_Account31", None)
                setattr(value, "customer_Account31", self)



class Online_Shopping_Shopping_Cart:

    def __init__(self, Is_Empty: bool, Contents: Online_Shopping_Shopping_Cart_Item, item33: "Online_Shopping_Item" = None, shopping_Cart_Item34: "Online_Shopping_Shopping_Cart_Item" = None, checkout36: "Online_Shopping_Checkout" = None):
        self.Is_Empty = Is_Empty
        self.Contents = Contents
        self.item33 = item33
        self.shopping_Cart_Item34 = shopping_Cart_Item34
        self.checkout36 = checkout36
        
        pass
    @property
    def Is_Empty(self):
        return self.__Is_Empty
    @Is_Empty.setter
    def Is_Empty(self, Is_Empty: bool):
        self.__Is_Empty = Is_Empty

    @property
    def Contents(self):
        return self.__Contents
    @Contents.setter
    def Contents(self, Contents: Online_Shopping_Shopping_Cart_Item):
        self.__Contents = Contents

    @property
    def checkout36(self):
        return self.__checkout36
    @checkout36.setter
    def checkout36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Shopping_Cart__checkout36", None)
        self.__checkout36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shopping_Cart37"):
                opp_val = getattr(old_value, "shopping_Cart37", None)
                if opp_val == self:
                    setattr(old_value, "shopping_Cart37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shopping_Cart37"):
                opp_val = getattr(value, "shopping_Cart37", None)
                setattr(value, "shopping_Cart37", self)

    @property
    def item33(self):
        return self.__item33
    @item33.setter
    def item33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Shopping_Cart__item33", None)
        self.__item33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shopping_Cart32"):
                opp_val = getattr(old_value, "shopping_Cart32", None)
                if opp_val == self:
                    setattr(old_value, "shopping_Cart32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shopping_Cart32"):
                opp_val = getattr(value, "shopping_Cart32", None)
                setattr(value, "shopping_Cart32", self)

    @property
    def shopping_Cart_Item34(self):
        return self.__shopping_Cart_Item34
    @shopping_Cart_Item34.setter
    def shopping_Cart_Item34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Shopping_Cart__shopping_Cart_Item34", None)
        self.__shopping_Cart_Item34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shopping_Cart35"):
                opp_val = getattr(old_value, "shopping_Cart35", None)
                if opp_val == self:
                    setattr(old_value, "shopping_Cart35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shopping_Cart35"):
                opp_val = getattr(value, "shopping_Cart35", None)
                setattr(value, "shopping_Cart35", self)



class Online_Shopping_Item:

    def __init__(self, Name: str, Product_ID: str, Description: str, Price: int, customer_Account31: "Online_Shopping_Customer_Account" = None, shopping_Cart32: "Online_Shopping_Shopping_Cart" = None):
        self.Name = Name
        self.Product_ID = Product_ID
        self.Description = Description
        self.Price = Price
        self.customer_Account31 = customer_Account31
        self.shopping_Cart32 = shopping_Cart32
        
        pass
    @property
    def Price(self):
        return self.__Price
    @Price.setter
    def Price(self, Price: int):
        self.__Price = Price

    @property
    def Description(self):
        return self.__Description
    @Description.setter
    def Description(self, Description: str):
        self.__Description = Description

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Product_ID(self):
        return self.__Product_ID
    @Product_ID.setter
    def Product_ID(self, Product_ID: str):
        self.__Product_ID = Product_ID

    @property
    def customer_Account31(self):
        return self.__customer_Account31
    @customer_Account31.setter
    def customer_Account31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Item__customer_Account31", None)
        self.__customer_Account31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "item30"):
                opp_val = getattr(old_value, "item30", None)
                if opp_val == self:
                    setattr(old_value, "item30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "item30"):
                opp_val = getattr(value, "item30", None)
                setattr(value, "item30", self)

    @property
    def shopping_Cart32(self):
        return self.__shopping_Cart32
    @shopping_Cart32.setter
    def shopping_Cart32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Item__shopping_Cart32", None)
        self.__shopping_Cart32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "item33"):
                opp_val = getattr(old_value, "item33", None)
                if opp_val == self:
                    setattr(old_value, "item33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "item33"):
                opp_val = getattr(value, "item33", None)
                setattr(value, "item33", self)



class Online_Shopping_Checkout:

    def __init__(self, Billing_Address: str, Delivery_Address: str, Phone_Number: int, Email_Address: str, shopping_Cart37: "Online_Shopping_Shopping_Cart" = None, card_Payment38: "Online_Shopping_Card_Payment" = None, paypal_Payment40: "Online_Shopping_Paypal_Payment" = None):
        self.Billing_Address = Billing_Address
        self.Delivery_Address = Delivery_Address
        self.Phone_Number = Phone_Number
        self.Email_Address = Email_Address
        self.shopping_Cart37 = shopping_Cart37
        self.card_Payment38 = card_Payment38
        self.paypal_Payment40 = paypal_Payment40
        
        pass
    @property
    def Email_Address(self):
        return self.__Email_Address
    @Email_Address.setter
    def Email_Address(self, Email_Address: str):
        self.__Email_Address = Email_Address

    @property
    def Delivery_Address(self):
        return self.__Delivery_Address
    @Delivery_Address.setter
    def Delivery_Address(self, Delivery_Address: str):
        self.__Delivery_Address = Delivery_Address

    @property
    def Billing_Address(self):
        return self.__Billing_Address
    @Billing_Address.setter
    def Billing_Address(self, Billing_Address: str):
        self.__Billing_Address = Billing_Address

    @property
    def Phone_Number(self):
        return self.__Phone_Number
    @Phone_Number.setter
    def Phone_Number(self, Phone_Number: int):
        self.__Phone_Number = Phone_Number

    @property
    def shopping_Cart37(self):
        return self.__shopping_Cart37
    @shopping_Cart37.setter
    def shopping_Cart37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Checkout__shopping_Cart37", None)
        self.__shopping_Cart37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "checkout36"):
                opp_val = getattr(old_value, "checkout36", None)
                if opp_val == self:
                    setattr(old_value, "checkout36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "checkout36"):
                opp_val = getattr(value, "checkout36", None)
                setattr(value, "checkout36", self)

    @property
    def paypal_Payment40(self):
        return self.__paypal_Payment40
    @paypal_Payment40.setter
    def paypal_Payment40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Checkout__paypal_Payment40", None)
        self.__paypal_Payment40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "checkout41"):
                opp_val = getattr(old_value, "checkout41", None)
                if opp_val == self:
                    setattr(old_value, "checkout41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "checkout41"):
                opp_val = getattr(value, "checkout41", None)
                setattr(value, "checkout41", self)

    @property
    def card_Payment38(self):
        return self.__card_Payment38
    @card_Payment38.setter
    def card_Payment38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Checkout__card_Payment38", None)
        self.__card_Payment38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "checkout39"):
                opp_val = getattr(old_value, "checkout39", None)
                if opp_val == self:
                    setattr(old_value, "checkout39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "checkout39"):
                opp_val = getattr(value, "checkout39", None)
                setattr(value, "checkout39", self)



class Online_Shopping_Paypal_Payment:

    def __init__(self, Username: str, Password: str, checkout41: "Online_Shopping_Checkout" = None, order44: "Online_Shopping_Order" = None):
        self.Username = Username
        self.Password = Password
        self.checkout41 = checkout41
        self.order44 = order44
        
        pass
    @property
    def Username(self):
        return self.__Username
    @Username.setter
    def Username(self, Username: str):
        self.__Username = Username

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def order44(self):
        return self.__order44
    @order44.setter
    def order44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Paypal_Payment__order44", None)
        self.__order44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "paypal_Payment45"):
                opp_val = getattr(old_value, "paypal_Payment45", None)
                if opp_val == self:
                    setattr(old_value, "paypal_Payment45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "paypal_Payment45"):
                opp_val = getattr(value, "paypal_Payment45", None)
                setattr(value, "paypal_Payment45", self)

    @property
    def checkout41(self):
        return self.__checkout41
    @checkout41.setter
    def checkout41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Paypal_Payment__checkout41", None)
        self.__checkout41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "paypal_Payment40"):
                opp_val = getattr(old_value, "paypal_Payment40", None)
                if opp_val == self:
                    setattr(old_value, "paypal_Payment40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "paypal_Payment40"):
                opp_val = getattr(value, "paypal_Payment40", None)
                setattr(value, "paypal_Payment40", self)



class Online_Shopping_Card_Payment:

    def __init__(self, Card_Holder_Name: str, Valid_Date: str, Card_Number: int, CVS_Number: int, checkout39: "Online_Shopping_Checkout" = None, order42: "Online_Shopping_Order" = None):
        self.Card_Holder_Name = Card_Holder_Name
        self.Valid_Date = Valid_Date
        self.Card_Number = Card_Number
        self.CVS_Number = CVS_Number
        self.checkout39 = checkout39
        self.order42 = order42
        
        pass
    @property
    def Card_Number(self):
        return self.__Card_Number
    @Card_Number.setter
    def Card_Number(self, Card_Number: int):
        self.__Card_Number = Card_Number

    @property
    def Card_Holder_Name(self):
        return self.__Card_Holder_Name
    @Card_Holder_Name.setter
    def Card_Holder_Name(self, Card_Holder_Name: str):
        self.__Card_Holder_Name = Card_Holder_Name

    @property
    def Valid_Date(self):
        return self.__Valid_Date
    @Valid_Date.setter
    def Valid_Date(self, Valid_Date: str):
        self.__Valid_Date = Valid_Date

    @property
    def CVS_Number(self):
        return self.__CVS_Number
    @CVS_Number.setter
    def CVS_Number(self, CVS_Number: int):
        self.__CVS_Number = CVS_Number

    @property
    def checkout39(self):
        return self.__checkout39
    @checkout39.setter
    def checkout39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Card_Payment__checkout39", None)
        self.__checkout39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card_Payment38"):
                opp_val = getattr(old_value, "card_Payment38", None)
                if opp_val == self:
                    setattr(old_value, "card_Payment38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card_Payment38"):
                opp_val = getattr(value, "card_Payment38", None)
                setattr(value, "card_Payment38", self)

    @property
    def order42(self):
        return self.__order42
    @order42.setter
    def order42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Card_Payment__order42", None)
        self.__order42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card_Payment43"):
                opp_val = getattr(old_value, "card_Payment43", None)
                if opp_val == self:
                    setattr(old_value, "card_Payment43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card_Payment43"):
                opp_val = getattr(value, "card_Payment43", None)
                setattr(value, "card_Payment43", self)



class Customer_Actor2:

    pass


class Payment_UseCase1:

    pass


class Customer_Actor1:

    pass


class Checkout_UseCase1:

    pass


class View_Items_UseCase1:

    pass
