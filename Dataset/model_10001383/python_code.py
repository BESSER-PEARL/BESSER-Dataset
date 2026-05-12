from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Online_Shopping_Or(Enum):
    pass
class Integer(Enum):
    pass

############################################
# Definition of Classes
############################################







class bank__Actor:

    pass


class credit_card__shop_card__PayPal_UseCase:

    pass


class Online_customer_Actor:

    pass


class Payment_UseCase:

    pass


class Authentication_or_service_or_identity_provider_Actor:

    pass


class Credit_payment_service_Actor:

    pass


class user_authentication_cookie_UseCase:

    pass


class Log_in__sign_in_page_UseCase:

    pass


class Customer_authentication__UseCase:

    pass


class Checkout_UseCase:

    pass


class save_items_for_later_in_wish_list_UseCase:

    pass


class add_items_to_shopping_cart_UseCase:

    pass


class view_recommended_items_UseCase:

    pass


class browse_catalogue_UseCase:

    pass


class Search_for_items_UseCase:

    pass


class View_items_UseCase:

    pass


class Choose_items_UseCase:

    pass


class PayPal__Mastercard__etc__UseCase:

    pass


class payment_UseCase:

    pass


class special_offers_UseCase:

    pass


class claim_some_points_UseCase:

    pass


class make_a_purchase_UseCase:

    pass


class view_items_UseCase:

    pass


class Authentication_UseCase:

    pass


class Login_UseCase:

    pass


class register_UseCase:

    pass


class Customer_Actor:

    pass





class Online_Shopping_Orderitem:

    def __init__(self, Quantity: int, ProductID: str, Sub_Total: str, order54: "Online_Shopping_Order" = None):
        self.Quantity = Quantity
        self.ProductID = ProductID
        self.Sub_Total = Sub_Total
        self.order54 = order54
        
        pass
    @property
    def Sub_Total(self):
        return self.__Sub_Total
    @Sub_Total.setter
    def Sub_Total(self, Sub_Total: str):
        self.__Sub_Total = Sub_Total

    @property
    def ProductID(self):
        return self.__ProductID
    @ProductID.setter
    def ProductID(self, ProductID: str):
        self.__ProductID = ProductID

    @property
    def Quantity(self):
        return self.__Quantity
    @Quantity.setter
    def Quantity(self, Quantity: int):
        self.__Quantity = Quantity

    @property
    def order54(self):
        return self.__order54
    @order54.setter
    def order54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Orderitem__order54", None)
        self.__order54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderitem55"):
                opp_val = getattr(old_value, "orderitem55", None)
                if opp_val == self:
                    setattr(old_value, "orderitem55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderitem55"):
                opp_val = getattr(value, "orderitem55", None)
                setattr(value, "orderitem55", self)



class Online_Shopping_Customer:

    def __init__(self, Username: str, Password: str, Address: str, Age: int, special_offers32: "Online_Shopping_Special_offers" = None, customer_points36: "Online_Shopping_Customer_points" = None, item38: "Online_Shopping_Item" = None):
        self.Username = Username
        self.Password = Password
        self.Address = Address
        self.Age = Age
        self.special_offers32 = special_offers32
        self.customer_points36 = customer_points36
        self.item38 = item38
        
        pass
    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def Age(self):
        return self.__Age
    @Age.setter
    def Age(self, Age: int):
        self.__Age = Age

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
    def item38(self):
        return self.__item38
    @item38.setter
    def item38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Customer__item38", None)
        self.__item38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer39"):
                opp_val = getattr(old_value, "customer39", None)
                if opp_val == self:
                    setattr(old_value, "customer39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer39"):
                opp_val = getattr(value, "customer39", None)
                setattr(value, "customer39", self)

    @property
    def special_offers32(self):
        return self.__special_offers32
    @special_offers32.setter
    def special_offers32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Customer__special_offers32", None)
        self.__special_offers32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer33"):
                opp_val = getattr(old_value, "customer33", None)
                if opp_val == self:
                    setattr(old_value, "customer33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer33"):
                opp_val = getattr(value, "customer33", None)
                setattr(value, "customer33", self)

    @property
    def customer_points36(self):
        return self.__customer_points36
    @customer_points36.setter
    def customer_points36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Customer__customer_points36", None)
        self.__customer_points36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer37"):
                opp_val = getattr(old_value, "customer37", None)
                if opp_val == self:
                    setattr(old_value, "customer37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer37"):
                opp_val = getattr(value, "customer37", None)
                setattr(value, "customer37", self)



class Online_Shopping_Customer_points:

    def __init__(self, Balance: Integer, customer37: "Online_Shopping_Customer" = None):
        self.Balance = Balance
        self.customer37 = customer37
        
        pass
    @property
    def Balance(self):
        return self.__Balance
    @Balance.setter
    def Balance(self, Balance: Integer):
        self.__Balance = Balance

    @property
    def customer37(self):
        return self.__customer37
    @customer37.setter
    def customer37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Customer_points__customer37", None)
        self.__customer37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer_points36"):
                opp_val = getattr(old_value, "customer_points36", None)
                if opp_val == self:
                    setattr(old_value, "customer_points36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer_points36"):
                opp_val = getattr(value, "customer_points36", None)
                setattr(value, "customer_points36", self)



class Online_Shopping_Special_offers:

    def __init__(self, Price: str, Discount: int, customer33: "Online_Shopping_Customer" = None, basketItem34: "Online_Shopping_BasketItem" = None):
        self.Price = Price
        self.Discount = Discount
        self.customer33 = customer33
        self.basketItem34 = basketItem34
        
        pass
    @property
    def Discount(self):
        return self.__Discount
    @Discount.setter
    def Discount(self, Discount: int):
        self.__Discount = Discount

    @property
    def Price(self):
        return self.__Price
    @Price.setter
    def Price(self, Price: str):
        self.__Price = Price

    @property
    def basketItem34(self):
        return self.__basketItem34
    @basketItem34.setter
    def basketItem34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Special_offers__basketItem34", None)
        self.__basketItem34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "special_offers35"):
                opp_val = getattr(old_value, "special_offers35", None)
                if opp_val == self:
                    setattr(old_value, "special_offers35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "special_offers35"):
                opp_val = getattr(value, "special_offers35", None)
                setattr(value, "special_offers35", self)

    @property
    def customer33(self):
        return self.__customer33
    @customer33.setter
    def customer33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Special_offers__customer33", None)
        self.__customer33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "special_offers32"):
                opp_val = getattr(old_value, "special_offers32", None)
                if opp_val == self:
                    setattr(old_value, "special_offers32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "special_offers32"):
                opp_val = getattr(value, "special_offers32", None)
                setattr(value, "special_offers32", self)



class Online_Shopping_Orderstate:

    def __init__(self, attribute: str):
        self.attribute = attribute
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute



class Online_Shopping_Order:

    def __init__(self, Placed_Date: int, State: str, Contents: Online_Shopping_Orderitem, card_payment51: "Online_Shopping_Card_payment" = None, payPal_payment53: "Online_Shopping_PayPal_payment" = None, orderitem55: "Online_Shopping_Orderitem" = None):
        self.Placed_Date = Placed_Date
        self.State = State
        self.Contents = Contents
        self.card_payment51 = card_payment51
        self.payPal_payment53 = payPal_payment53
        self.orderitem55 = orderitem55
        
        pass
    @property
    def State(self):
        return self.__State
    @State.setter
    def State(self, State: str):
        self.__State = State

    @property
    def Contents(self):
        return self.__Contents
    @Contents.setter
    def Contents(self, Contents: Online_Shopping_Orderitem):
        self.__Contents = Contents

    @property
    def Placed_Date(self):
        return self.__Placed_Date
    @Placed_Date.setter
    def Placed_Date(self, Placed_Date: int):
        self.__Placed_Date = Placed_Date

    @property
    def card_payment51(self):
        return self.__card_payment51
    @card_payment51.setter
    def card_payment51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Order__card_payment51", None)
        self.__card_payment51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderitem50"):
                opp_val = getattr(old_value, "orderitem50", None)
                if opp_val == self:
                    setattr(old_value, "orderitem50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderitem50"):
                opp_val = getattr(value, "orderitem50", None)
                setattr(value, "orderitem50", self)

    @property
    def payPal_payment53(self):
        return self.__payPal_payment53
    @payPal_payment53.setter
    def payPal_payment53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Order__payPal_payment53", None)
        self.__payPal_payment53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderitem52"):
                opp_val = getattr(old_value, "orderitem52", None)
                if opp_val == self:
                    setattr(old_value, "orderitem52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderitem52"):
                opp_val = getattr(value, "orderitem52", None)
                setattr(value, "orderitem52", self)

    @property
    def orderitem55(self):
        return self.__orderitem55
    @orderitem55.setter
    def orderitem55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Order__orderitem55", None)
        self.__orderitem55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order54"):
                opp_val = getattr(old_value, "order54", None)
                if opp_val == self:
                    setattr(old_value, "order54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order54"):
                opp_val = getattr(value, "order54", None)
                setattr(value, "order54", self)



class Online_Shopping_BasketItem:

    def __init__(self, Quantity: int, ProductID: str, special_offers35: "Online_Shopping_Special_offers" = None, basket43: "Online_Shopping_Basket" = None):
        self.Quantity = Quantity
        self.ProductID = ProductID
        self.special_offers35 = special_offers35
        self.basket43 = basket43
        
        pass
    @property
    def Quantity(self):
        return self.__Quantity
    @Quantity.setter
    def Quantity(self, Quantity: int):
        self.__Quantity = Quantity

    @property
    def ProductID(self):
        return self.__ProductID
    @ProductID.setter
    def ProductID(self, ProductID: str):
        self.__ProductID = ProductID

    @property
    def special_offers35(self):
        return self.__special_offers35
    @special_offers35.setter
    def special_offers35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_BasketItem__special_offers35", None)
        self.__special_offers35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basketItem34"):
                opp_val = getattr(old_value, "basketItem34", None)
                if opp_val == self:
                    setattr(old_value, "basketItem34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basketItem34"):
                opp_val = getattr(value, "basketItem34", None)
                setattr(value, "basketItem34", self)

    @property
    def basket43(self):
        return self.__basket43
    @basket43.setter
    def basket43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_BasketItem__basket43", None)
        self.__basket43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basketItem42"):
                opp_val = getattr(old_value, "basketItem42", None)
                if opp_val == self:
                    setattr(old_value, "basketItem42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basketItem42"):
                opp_val = getattr(value, "basketItem42", None)
                setattr(value, "basketItem42", self)



class Online_Shopping_Basket:

    def __init__(self, IsEmpty: bool, attribute: str, Contents: Online_Shopping_BasketItem, item41: "Online_Shopping_Item" = None, basketItem42: "Online_Shopping_BasketItem" = None, checkout44: "Online_Shopping_Checkout" = None):
        self.IsEmpty = IsEmpty
        self.attribute = attribute
        self.Contents = Contents
        self.item41 = item41
        self.basketItem42 = basketItem42
        self.checkout44 = checkout44
        
        pass
    @property
    def IsEmpty(self):
        return self.__IsEmpty
    @IsEmpty.setter
    def IsEmpty(self, IsEmpty: bool):
        self.__IsEmpty = IsEmpty

    @property
    def Contents(self):
        return self.__Contents
    @Contents.setter
    def Contents(self, Contents: Online_Shopping_BasketItem):
        self.__Contents = Contents

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def basketItem42(self):
        return self.__basketItem42
    @basketItem42.setter
    def basketItem42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Basket__basketItem42", None)
        self.__basketItem42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basket43"):
                opp_val = getattr(old_value, "basket43", None)
                if opp_val == self:
                    setattr(old_value, "basket43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basket43"):
                opp_val = getattr(value, "basket43", None)
                setattr(value, "basket43", self)

    @property
    def item41(self):
        return self.__item41
    @item41.setter
    def item41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Basket__item41", None)
        self.__item41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basket40"):
                opp_val = getattr(old_value, "basket40", None)
                if opp_val == self:
                    setattr(old_value, "basket40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basket40"):
                opp_val = getattr(value, "basket40", None)
                setattr(value, "basket40", self)

    @property
    def checkout44(self):
        return self.__checkout44
    @checkout44.setter
    def checkout44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Basket__checkout44", None)
        self.__checkout44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basket45"):
                opp_val = getattr(old_value, "basket45", None)
                if opp_val == self:
                    setattr(old_value, "basket45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basket45"):
                opp_val = getattr(value, "basket45", None)
                setattr(value, "basket45", self)



class Online_Shopping_Checkout:

    def __init__(self, Billing_address: str, Checkout_address: str, Phone_number: int, Email_address: str, basket45: "Online_Shopping_Basket" = None, payPal_payment46: "Online_Shopping_PayPal_payment" = None, card_payment48: "Online_Shopping_Card_payment" = None):
        self.Billing_address = Billing_address
        self.Checkout_address = Checkout_address
        self.Phone_number = Phone_number
        self.Email_address = Email_address
        self.basket45 = basket45
        self.payPal_payment46 = payPal_payment46
        self.card_payment48 = card_payment48
        
        pass
    @property
    def Billing_address(self):
        return self.__Billing_address
    @Billing_address.setter
    def Billing_address(self, Billing_address: str):
        self.__Billing_address = Billing_address

    @property
    def Checkout_address(self):
        return self.__Checkout_address
    @Checkout_address.setter
    def Checkout_address(self, Checkout_address: str):
        self.__Checkout_address = Checkout_address

    @property
    def Email_address(self):
        return self.__Email_address
    @Email_address.setter
    def Email_address(self, Email_address: str):
        self.__Email_address = Email_address

    @property
    def Phone_number(self):
        return self.__Phone_number
    @Phone_number.setter
    def Phone_number(self, Phone_number: int):
        self.__Phone_number = Phone_number

    @property
    def card_payment48(self):
        return self.__card_payment48
    @card_payment48.setter
    def card_payment48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Checkout__card_payment48", None)
        self.__card_payment48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "checkout49"):
                opp_val = getattr(old_value, "checkout49", None)
                if opp_val == self:
                    setattr(old_value, "checkout49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "checkout49"):
                opp_val = getattr(value, "checkout49", None)
                setattr(value, "checkout49", self)

    @property
    def basket45(self):
        return self.__basket45
    @basket45.setter
    def basket45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Checkout__basket45", None)
        self.__basket45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "checkout44"):
                opp_val = getattr(old_value, "checkout44", None)
                if opp_val == self:
                    setattr(old_value, "checkout44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "checkout44"):
                opp_val = getattr(value, "checkout44", None)
                setattr(value, "checkout44", self)

    @property
    def payPal_payment46(self):
        return self.__payPal_payment46
    @payPal_payment46.setter
    def payPal_payment46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Checkout__payPal_payment46", None)
        self.__payPal_payment46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "checkout47"):
                opp_val = getattr(old_value, "checkout47", None)
                if opp_val == self:
                    setattr(old_value, "checkout47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "checkout47"):
                opp_val = getattr(value, "checkout47", None)
                setattr(value, "checkout47", self)



class Online_Shopping_Item:

    def __init__(self, ProductID: str, Name: str, Description: str, Price: int, customer39: "Online_Shopping_Customer" = None, basket40: "Online_Shopping_Basket" = None):
        self.ProductID = ProductID
        self.Name = Name
        self.Description = Description
        self.Price = Price
        self.customer39 = customer39
        self.basket40 = basket40
        
        pass
    @property
    def ProductID(self):
        return self.__ProductID
    @ProductID.setter
    def ProductID(self, ProductID: str):
        self.__ProductID = ProductID

    @property
    def Description(self):
        return self.__Description
    @Description.setter
    def Description(self, Description: str):
        self.__Description = Description

    @property
    def Price(self):
        return self.__Price
    @Price.setter
    def Price(self, Price: int):
        self.__Price = Price

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def basket40(self):
        return self.__basket40
    @basket40.setter
    def basket40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Item__basket40", None)
        self.__basket40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "item41"):
                opp_val = getattr(old_value, "item41", None)
                if opp_val == self:
                    setattr(old_value, "item41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "item41"):
                opp_val = getattr(value, "item41", None)
                setattr(value, "item41", self)

    @property
    def customer39(self):
        return self.__customer39
    @customer39.setter
    def customer39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Item__customer39", None)
        self.__customer39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "item38"):
                opp_val = getattr(old_value, "item38", None)
                if opp_val == self:
                    setattr(old_value, "item38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "item38"):
                opp_val = getattr(value, "item38", None)
                setattr(value, "item38", self)



class Online_Shopping_PayPal_payment:

    def __init__(self, Username: str, attribute: str, Password: str, checkout47: "Online_Shopping_Checkout" = None, orderitem52: "Online_Shopping_Order" = None):
        self.Username = Username
        self.attribute = attribute
        self.Password = Password
        self.checkout47 = checkout47
        self.orderitem52 = orderitem52
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

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
    def orderitem52(self):
        return self.__orderitem52
    @orderitem52.setter
    def orderitem52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_PayPal_payment__orderitem52", None)
        self.__orderitem52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payPal_payment53"):
                opp_val = getattr(old_value, "payPal_payment53", None)
                if opp_val == self:
                    setattr(old_value, "payPal_payment53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payPal_payment53"):
                opp_val = getattr(value, "payPal_payment53", None)
                setattr(value, "payPal_payment53", self)

    @property
    def checkout47(self):
        return self.__checkout47
    @checkout47.setter
    def checkout47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_PayPal_payment__checkout47", None)
        self.__checkout47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payPal_payment46"):
                opp_val = getattr(old_value, "payPal_payment46", None)
                if opp_val == self:
                    setattr(old_value, "payPal_payment46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payPal_payment46"):
                opp_val = getattr(value, "payPal_payment46", None)
                setattr(value, "payPal_payment46", self)



class Online_Shopping_Card_payment:

    def __init__(self, payment_type: str, Card_number: int, Cardholder_name: str, Valid_date: int, CVS_number: int, checkout49: "Online_Shopping_Checkout" = None, orderitem50: "Online_Shopping_Order" = None):
        self.payment_type = payment_type
        self.Card_number = Card_number
        self.Cardholder_name = Cardholder_name
        self.Valid_date = Valid_date
        self.CVS_number = CVS_number
        self.checkout49 = checkout49
        self.orderitem50 = orderitem50
        
        pass
    @property
    def CVS_number(self):
        return self.__CVS_number
    @CVS_number.setter
    def CVS_number(self, CVS_number: int):
        self.__CVS_number = CVS_number

    @property
    def Card_number(self):
        return self.__Card_number
    @Card_number.setter
    def Card_number(self, Card_number: int):
        self.__Card_number = Card_number

    @property
    def payment_type(self):
        return self.__payment_type
    @payment_type.setter
    def payment_type(self, payment_type: str):
        self.__payment_type = payment_type

    @property
    def Valid_date(self):
        return self.__Valid_date
    @Valid_date.setter
    def Valid_date(self, Valid_date: int):
        self.__Valid_date = Valid_date

    @property
    def Cardholder_name(self):
        return self.__Cardholder_name
    @Cardholder_name.setter
    def Cardholder_name(self, Cardholder_name: str):
        self.__Cardholder_name = Cardholder_name

    @property
    def checkout49(self):
        return self.__checkout49
    @checkout49.setter
    def checkout49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Card_payment__checkout49", None)
        self.__checkout49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card_payment48"):
                opp_val = getattr(old_value, "card_payment48", None)
                if opp_val == self:
                    setattr(old_value, "card_payment48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card_payment48"):
                opp_val = getattr(value, "card_payment48", None)
                setattr(value, "card_payment48", self)

    @property
    def orderitem50(self):
        return self.__orderitem50
    @orderitem50.setter
    def orderitem50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Online_Shopping_Card_payment__orderitem50", None)
        self.__orderitem50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card_payment51"):
                opp_val = getattr(old_value, "card_payment51", None)
                if opp_val == self:
                    setattr(old_value, "card_payment51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card_payment51"):
                opp_val = getattr(value, "card_payment51", None)
                setattr(value, "card_payment51", self)



class _unnamed:

    pass


class Customer_Actor1:

    pass


class Checkout_UseCase1:

    pass
