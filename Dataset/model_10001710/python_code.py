from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Web_Login:

    def __init__(self, login_id: str, password: str, verification: Customer, customer0: "Customer" = None, cart2: "Cart" = None):
        self.login_id = login_id
        self.password = password
        self.verification = verification
        self.customer0 = customer0
        self.cart2 = cart2
        
        pass
    @property
    def login_id(self):
        return self.__login_id
    @login_id.setter
    def login_id(self, login_id: str):
        self.__login_id = login_id

    @property
    def verification(self):
        return self.__verification
    @verification.setter
    def verification(self, verification: Customer):
        self.__verification = verification

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def cart2(self):
        return self.__cart2
    @cart2.setter
    def cart2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Web_Login__cart2", None)
        self.__cart2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "web_Login3"):
                opp_val = getattr(old_value, "web_Login3", None)
                if opp_val == self:
                    setattr(old_value, "web_Login3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "web_Login3"):
                opp_val = getattr(value, "web_Login3", None)
                setattr(value, "web_Login3", self)

    @property
    def customer0(self):
        return self.__customer0
    @customer0.setter
    def customer0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Web_Login__customer0", None)
        self.__customer0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "web_Login1"):
                opp_val = getattr(old_value, "web_Login1", None)
                if opp_val == self:
                    setattr(old_value, "web_Login1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "web_Login1"):
                opp_val = getattr(value, "web_Login1", None)
                setattr(value, "web_Login1", self)



class Payment_Verification:

    def __init__(self, txn_id: str, status: str, payment13: "Payment" = None, account16: "Account" = None, customer20: "Customer" = None):
        self.txn_id = txn_id
        self.status = status
        self.payment13 = payment13
        self.account16 = account16
        self.customer20 = customer20
        
        pass
    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def txn_id(self):
        return self.__txn_id
    @txn_id.setter
    def txn_id(self, txn_id: str):
        self.__txn_id = txn_id

    @property
    def customer20(self):
        return self.__customer20
    @customer20.setter
    def customer20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment_Verification__customer20", None)
        self.__customer20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment_Verification21"):
                opp_val = getattr(old_value, "payment_Verification21", None)
                if opp_val == self:
                    setattr(old_value, "payment_Verification21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment_Verification21"):
                opp_val = getattr(value, "payment_Verification21", None)
                setattr(value, "payment_Verification21", self)

    @property
    def payment13(self):
        return self.__payment13
    @payment13.setter
    def payment13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment_Verification__payment13", None)
        self.__payment13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment_Verification12"):
                opp_val = getattr(old_value, "payment_Verification12", None)
                if opp_val == self:
                    setattr(old_value, "payment_Verification12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment_Verification12"):
                opp_val = getattr(value, "payment_Verification12", None)
                setattr(value, "payment_Verification12", self)

    @property
    def account16(self):
        return self.__account16
    @account16.setter
    def account16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment_Verification__account16", None)
        self.__account16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment_Verification17"):
                opp_val = getattr(old_value, "payment_Verification17", None)
                if opp_val == self:
                    setattr(old_value, "payment_Verification17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment_Verification17"):
                opp_val = getattr(value, "payment_Verification17", None)
                setattr(value, "payment_Verification17", self)



class catalog:

    def __init__(self, category: str, name: str, product6: "Product" = None):
        self.category = category
        self.name = name
        self.product6 = product6
        
        pass
    @property
    def category(self):
        return self.__category
    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def product6(self):
        return self.__product6
    @product6.setter
    def product6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_catalog__product6", None)
        self.__product6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "catalog7"):
                opp_val = getattr(old_value, "catalog7", None)
                if opp_val == self:
                    setattr(old_value, "catalog7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "catalog7"):
                opp_val = getattr(value, "catalog7", None)
                setattr(value, "catalog7", self)



class Cart:

    def __init__(self, Id: str, items: int, web_Login3: "Web_Login" = None, order18: "Order" = None, product22: "Product" = None):
        self.Id = Id
        self.items = items
        self.web_Login3 = web_Login3
        self.order18 = order18
        self.product22 = product22
        
        pass
    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: str):
        self.__Id = Id

    @property
    def items(self):
        return self.__items
    @items.setter
    def items(self, items: int):
        self.__items = items

    @property
    def web_Login3(self):
        return self.__web_Login3
    @web_Login3.setter
    def web_Login3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cart__web_Login3", None)
        self.__web_Login3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cart2"):
                opp_val = getattr(old_value, "cart2", None)
                if opp_val == self:
                    setattr(old_value, "cart2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cart2"):
                opp_val = getattr(value, "cart2", None)
                setattr(value, "cart2", self)

    @property
    def order18(self):
        return self.__order18
    @order18.setter
    def order18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cart__order18", None)
        self.__order18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cart19"):
                opp_val = getattr(old_value, "cart19", None)
                if opp_val == self:
                    setattr(old_value, "cart19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cart19"):
                opp_val = getattr(value, "cart19", None)
                setattr(value, "cart19", self)

    @property
    def product22(self):
        return self.__product22
    @product22.setter
    def product22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cart__product22", None)
        self.__product22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cart23"):
                opp_val = getattr(old_value, "cart23", None)
                if opp_val == self:
                    setattr(old_value, "cart23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cart23"):
                opp_val = getattr(value, "cart23", None)
                setattr(value, "cart23", self)



class Product:

    def __init__(self, Category: str, name: str, price: str, attribute: str, catalog7: "catalog" = None, order8: "Order" = None, cart23: "Cart" = None):
        self.Category = Category
        self.name = name
        self.price = price
        self.attribute = attribute
        self.catalog7 = catalog7
        self.order8 = order8
        self.cart23 = cart23
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: str):
        self.__price = price

    @property
    def Category(self):
        return self.__Category
    @Category.setter
    def Category(self, Category: str):
        self.__Category = Category

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def catalog7(self):
        return self.__catalog7
    @catalog7.setter
    def catalog7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__catalog7", None)
        self.__catalog7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product6"):
                opp_val = getattr(old_value, "product6", None)
                if opp_val == self:
                    setattr(old_value, "product6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product6"):
                opp_val = getattr(value, "product6", None)
                setattr(value, "product6", self)

    @property
    def cart23(self):
        return self.__cart23
    @cart23.setter
    def cart23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__cart23", None)
        self.__cart23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product22"):
                opp_val = getattr(old_value, "product22", None)
                if opp_val == self:
                    setattr(old_value, "product22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product22"):
                opp_val = getattr(value, "product22", None)
                setattr(value, "product22", self)

    @property
    def order8(self):
        return self.__order8
    @order8.setter
    def order8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__order8", None)
        self.__order8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product9"):
                opp_val = getattr(old_value, "product9", None)
                if opp_val == self:
                    setattr(old_value, "product9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product9"):
                opp_val = getattr(value, "product9", None)
                setattr(value, "product9", self)



class Order:

    def __init__(self, items: str, ordered: str, shipped: str, address: str, status: str, t: str, product9: "Product" = None, payment10: "Payment" = None, account15: "Account" = None, cart19: "Cart" = None):
        self.items = items
        self.ordered = ordered
        self.shipped = shipped
        self.address = address
        self.status = status
        self.t = t
        self.product9 = product9
        self.payment10 = payment10
        self.account15 = account15
        self.cart19 = cart19
        
        pass
    @property
    def shipped(self):
        return self.__shipped
    @shipped.setter
    def shipped(self, shipped: str):
        self.__shipped = shipped

    @property
    def t(self):
        return self.__t
    @t.setter
    def t(self, t: str):
        self.__t = t

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def items(self):
        return self.__items
    @items.setter
    def items(self, items: str):
        self.__items = items

    @property
    def ordered(self):
        return self.__ordered
    @ordered.setter
    def ordered(self, ordered: str):
        self.__ordered = ordered

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def product9(self):
        return self.__product9
    @product9.setter
    def product9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__product9", None)
        self.__product9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order8"):
                opp_val = getattr(old_value, "order8", None)
                if opp_val == self:
                    setattr(old_value, "order8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order8"):
                opp_val = getattr(value, "order8", None)
                setattr(value, "order8", self)

    @property
    def account15(self):
        return self.__account15
    @account15.setter
    def account15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__account15", None)
        self.__account15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order14"):
                opp_val = getattr(old_value, "order14", None)
                if opp_val == self:
                    setattr(old_value, "order14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order14"):
                opp_val = getattr(value, "order14", None)
                setattr(value, "order14", self)

    @property
    def payment10(self):
        return self.__payment10
    @payment10.setter
    def payment10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__payment10", None)
        self.__payment10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order11"):
                opp_val = getattr(old_value, "order11", None)
                if opp_val == self:
                    setattr(old_value, "order11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order11"):
                opp_val = getattr(value, "order11", None)
                setattr(value, "order11", self)

    @property
    def cart19(self):
        return self.__cart19
    @cart19.setter
    def cart19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__cart19", None)
        self.__cart19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order18"):
                opp_val = getattr(old_value, "order18", None)
                if opp_val == self:
                    setattr(old_value, "order18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order18"):
                opp_val = getattr(value, "order18", None)
                setattr(value, "order18", self)



class Payment:

    def __init__(self, txn_id: str, paid: str, total: str, Details: str, order11: "Order" = None, payment_Verification12: "Payment_Verification" = None):
        self.txn_id = txn_id
        self.paid = paid
        self.total = total
        self.Details = Details
        self.order11 = order11
        self.payment_Verification12 = payment_Verification12
        
        pass
    @property
    def txn_id(self):
        return self.__txn_id
    @txn_id.setter
    def txn_id(self, txn_id: str):
        self.__txn_id = txn_id

    @property
    def Details(self):
        return self.__Details
    @Details.setter
    def Details(self, Details: str):
        self.__Details = Details

    @property
    def paid(self):
        return self.__paid
    @paid.setter
    def paid(self, paid: str):
        self.__paid = paid

    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, total: str):
        self.__total = total

    @property
    def order11(self):
        return self.__order11
    @order11.setter
    def order11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__order11", None)
        self.__order11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment10"):
                opp_val = getattr(old_value, "payment10", None)
                if opp_val == self:
                    setattr(old_value, "payment10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment10"):
                opp_val = getattr(value, "payment10", None)
                setattr(value, "payment10", self)

    @property
    def payment_Verification12(self):
        return self.__payment_Verification12
    @payment_Verification12.setter
    def payment_Verification12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__payment_Verification12", None)
        self.__payment_Verification12 = value
        
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



class Account:

    def __init__(self, id: str, billing_address: str, open: str, customer5: "Customer" = None, order14: "Order" = None, payment_Verification17: "Payment_Verification" = None):
        self.id = id
        self.billing_address = billing_address
        self.open = open
        self.customer5 = customer5
        self.order14 = order14
        self.payment_Verification17 = payment_Verification17
        
        pass
    @property
    def open(self):
        return self.__open
    @open.setter
    def open(self, open: str):
        self.__open = open

    @property
    def billing_address(self):
        return self.__billing_address
    @billing_address.setter
    def billing_address(self, billing_address: str):
        self.__billing_address = billing_address

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def customer5(self):
        return self.__customer5
    @customer5.setter
    def customer5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__customer5", None)
        self.__customer5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account4"):
                opp_val = getattr(old_value, "account4", None)
                if opp_val == self:
                    setattr(old_value, "account4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account4"):
                opp_val = getattr(value, "account4", None)
                setattr(value, "account4", self)

    @property
    def order14(self):
        return self.__order14
    @order14.setter
    def order14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__order14", None)
        self.__order14 = value
        
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

    @property
    def payment_Verification17(self):
        return self.__payment_Verification17
    @payment_Verification17.setter
    def payment_Verification17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__payment_Verification17", None)
        self.__payment_Verification17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account16"):
                opp_val = getattr(old_value, "account16", None)
                if opp_val == self:
                    setattr(old_value, "account16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account16"):
                opp_val = getattr(value, "account16", None)
                setattr(value, "account16", self)



class Customer:

    def __init__(self, id_: str, address: str, phone: int, email: str, web_Login1: "Web_Login" = None, account4: "Account" = None, payment_Verification21: "Payment_Verification" = None):
        self.id_ = id_
        self.address = address
        self.phone = phone
        self.email = email
        self.web_Login1 = web_Login1
        self.account4 = account4
        self.payment_Verification21 = payment_Verification21
        
        pass
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: int):
        self.__phone = phone

    @property
    def id_(self):
        return self.__id_
    @id_.setter
    def id_(self, id_: str):
        self.__id_ = id_

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def web_Login1(self):
        return self.__web_Login1
    @web_Login1.setter
    def web_Login1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__web_Login1", None)
        self.__web_Login1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer0"):
                opp_val = getattr(old_value, "customer0", None)
                if opp_val == self:
                    setattr(old_value, "customer0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer0"):
                opp_val = getattr(value, "customer0", None)
                setattr(value, "customer0", self)

    @property
    def account4(self):
        return self.__account4
    @account4.setter
    def account4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__account4", None)
        self.__account4 = value
        
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
    def payment_Verification21(self):
        return self.__payment_Verification21
    @payment_Verification21.setter
    def payment_Verification21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__payment_Verification21", None)
        self.__payment_Verification21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer20"):
                opp_val = getattr(old_value, "customer20", None)
                if opp_val == self:
                    setattr(old_value, "customer20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer20"):
                opp_val = getattr(value, "customer20", None)
                setattr(value, "customer20", self)

