from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class restapp_model_Card:

    def __init__(self, id: int, sellDate: date, totalValue: float, discount: int, totalValueWithDiscount: float, payedValue: float, change: float, restapp_model_Card: "PhysicalCard" = None):
        self.id = id
        self.sellDate = sellDate
        self.totalValue = totalValue
        self.discount = discount
        self.totalValueWithDiscount = totalValueWithDiscount
        self.payedValue = payedValue
        self.change = change
        self.restapp_model_Card = restapp_model_Card
        
    @property
    def totalValue(self) -> float:
        return self.__totalValue

    @totalValue.setter
    def totalValue(self, totalValue: float):
        self.__totalValue = totalValue

    @property
    def payedValue(self) -> float:
        return self.__payedValue

    @payedValue.setter
    def payedValue(self, payedValue: float):
        self.__payedValue = payedValue

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def discount(self) -> int:
        return self.__discount

    @discount.setter
    def discount(self, discount: int):
        self.__discount = discount

    @property
    def totalValueWithDiscount(self) -> float:
        return self.__totalValueWithDiscount

    @totalValueWithDiscount.setter
    def totalValueWithDiscount(self, totalValueWithDiscount: float):
        self.__totalValueWithDiscount = totalValueWithDiscount

    @property
    def change(self) -> float:
        return self.__change

    @change.setter
    def change(self, change: float):
        self.__change = change

    @property
    def sellDate(self) -> date:
        return self.__sellDate

    @sellDate.setter
    def sellDate(self, sellDate: date):
        self.__sellDate = sellDate

    @property
    def restapp_model_Card(self):
        return self.__restapp_model_Card

    @restapp_model_Card.setter
    def restapp_model_Card(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_restapp_model_Card__restapp_model_Card", None)
        self.__restapp_model_Card = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhysicalCard"):
                opp_val = getattr(old_value, "PhysicalCard", None)
                if opp_val == self:
                    setattr(old_value, "PhysicalCard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhysicalCard"):
                opp_val = getattr(value, "PhysicalCard", None)
                setattr(value, "PhysicalCard", self)

class restapp_model_PhysicalCard:

    def __init__(self, id: int, number: int, status: int):
        self.id = id
        self.number = number
        self.status = status
        
    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def status(self) -> int:
        return self.__status

    @status.setter
    def status(self, status: int):
        self.__status = status

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

class Purchase:

    pass
class Card:

    pass
class restapp_model_ProductsCard:

    def __init__(self, id: int, date: date, restapp_model_ProductsCard: "Product" = None, restapp_model_ProductsCard14: "Card" = None, restapp_model_ProductsCard16: "User" = None):
        self.id = id
        self.date = date
        self.restapp_model_ProductsCard = restapp_model_ProductsCard
        self.restapp_model_ProductsCard14 = restapp_model_ProductsCard14
        self.restapp_model_ProductsCard16 = restapp_model_ProductsCard16
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def restapp_model_ProductsCard14(self):
        return self.__restapp_model_ProductsCard14

    @restapp_model_ProductsCard14.setter
    def restapp_model_ProductsCard14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_restapp_model_ProductsCard__restapp_model_ProductsCard14", None)
        self.__restapp_model_ProductsCard14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Card"):
                opp_val = getattr(old_value, "Card", None)
                if opp_val == self:
                    setattr(old_value, "Card", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Card"):
                opp_val = getattr(value, "Card", None)
                setattr(value, "Card", self)

    @property
    def restapp_model_ProductsCard(self):
        return self.__restapp_model_ProductsCard

    @restapp_model_ProductsCard.setter
    def restapp_model_ProductsCard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_restapp_model_ProductsCard__restapp_model_ProductsCard", None)
        self.__restapp_model_ProductsCard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Product12"):
                opp_val = getattr(old_value, "Product12", None)
                if opp_val == self:
                    setattr(old_value, "Product12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Product12"):
                opp_val = getattr(value, "Product12", None)
                setattr(value, "Product12", self)

    @property
    def restapp_model_ProductsCard16(self):
        return self.__restapp_model_ProductsCard16

    @restapp_model_ProductsCard16.setter
    def restapp_model_ProductsCard16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_restapp_model_ProductsCard__restapp_model_ProductsCard16", None)
        self.__restapp_model_ProductsCard16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "User17"):
                opp_val = getattr(old_value, "User17", None)
                if opp_val == self:
                    setattr(old_value, "User17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "User17"):
                opp_val = getattr(value, "User17", None)
                setattr(value, "User17", self)

class PhysicalCard:

    pass
class Category:

    pass
class restapp_model_Product:

    def __init__(self, id: int, name: str, description: str, stock: int, status: int, restapp_model_Product: "Category" = None):
        self.id = id
        self.name = name
        self.description = description
        self.stock = stock
        self.status = status
        self.restapp_model_Product = restapp_model_Product
        
    @property
    def status(self) -> int:
        return self.__status

    @status.setter
    def status(self, status: int):
        self.__status = status

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def stock(self) -> int:
        return self.__stock

    @stock.setter
    def stock(self, stock: int):
        self.__stock = stock

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def restapp_model_Product(self):
        return self.__restapp_model_Product

    @restapp_model_Product.setter
    def restapp_model_Product(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_restapp_model_Product__restapp_model_Product", None)
        self.__restapp_model_Product = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Category"):
                opp_val = getattr(old_value, "Category", None)
                if opp_val == self:
                    setattr(old_value, "Category", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Category"):
                opp_val = getattr(value, "Category", None)
                setattr(value, "Category", self)

class restapp_model_ProductsPurchase:

    def __init__(self, quantity: int, unityValue: float, unityDiscount: int, unityValueWithDiscount: float, restapp_model_ProductsPurchase: "Purchase" = None, restapp_model_ProductsPurchase8: "Product" = None):
        self.quantity = quantity
        self.unityValue = unityValue
        self.unityDiscount = unityDiscount
        self.unityValueWithDiscount = unityValueWithDiscount
        self.restapp_model_ProductsPurchase = restapp_model_ProductsPurchase
        self.restapp_model_ProductsPurchase8 = restapp_model_ProductsPurchase8
        
    @property
    def unityDiscount(self) -> int:
        return self.__unityDiscount

    @unityDiscount.setter
    def unityDiscount(self, unityDiscount: int):
        self.__unityDiscount = unityDiscount

    @property
    def unityValue(self) -> float:
        return self.__unityValue

    @unityValue.setter
    def unityValue(self, unityValue: float):
        self.__unityValue = unityValue

    @property
    def unityValueWithDiscount(self) -> float:
        return self.__unityValueWithDiscount

    @unityValueWithDiscount.setter
    def unityValueWithDiscount(self, unityValueWithDiscount: float):
        self.__unityValueWithDiscount = unityValueWithDiscount

    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def restapp_model_ProductsPurchase(self):
        return self.__restapp_model_ProductsPurchase

    @restapp_model_ProductsPurchase.setter
    def restapp_model_ProductsPurchase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_restapp_model_ProductsPurchase__restapp_model_ProductsPurchase", None)
        self.__restapp_model_ProductsPurchase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Purchase"):
                opp_val = getattr(old_value, "Purchase", None)
                if opp_val == self:
                    setattr(old_value, "Purchase", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Purchase"):
                opp_val = getattr(value, "Purchase", None)
                setattr(value, "Purchase", self)

    @property
    def restapp_model_ProductsPurchase8(self):
        return self.__restapp_model_ProductsPurchase8

    @restapp_model_ProductsPurchase8.setter
    def restapp_model_ProductsPurchase8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_restapp_model_ProductsPurchase__restapp_model_ProductsPurchase8", None)
        self.__restapp_model_ProductsPurchase8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Product9"):
                opp_val = getattr(old_value, "Product9", None)
                if opp_val == self:
                    setattr(old_value, "Product9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Product9"):
                opp_val = getattr(value, "Product9", None)
                setattr(value, "Product9", self)

class restapp_model_Provider:

    def __init__(self, id: int, name: str, phone: str, CNPJ: str, Address: str, contact: str):
        self.id = id
        self.name = name
        self.phone = phone
        self.CNPJ = CNPJ
        self.Address = Address
        self.contact = contact
        
    @property
    def phone(self) -> str:
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def contact(self) -> str:
        return self.__contact

    @contact.setter
    def contact(self, contact: str):
        self.__contact = contact

    @property
    def CNPJ(self) -> str:
        return self.__CNPJ

    @CNPJ.setter
    def CNPJ(self, CNPJ: str):
        self.__CNPJ = CNPJ

    @property
    def Address(self) -> str:
        return self.__Address

    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

class User:

    pass
class Provider:

    pass
class restapp_model_Purchase:

    def __init__(self, id: int, date: date, totalValue: float, discount: int, totalWithDiscount: float, restapp_model_Purchase: "Provider" = None, restapp_model_Purchase5: "User" = None):
        self.id = id
        self.date = date
        self.totalValue = totalValue
        self.discount = discount
        self.totalWithDiscount = totalWithDiscount
        self.restapp_model_Purchase = restapp_model_Purchase
        self.restapp_model_Purchase5 = restapp_model_Purchase5
        
    @property
    def totalWithDiscount(self) -> float:
        return self.__totalWithDiscount

    @totalWithDiscount.setter
    def totalWithDiscount(self, totalWithDiscount: float):
        self.__totalWithDiscount = totalWithDiscount

    @property
    def totalValue(self) -> float:
        return self.__totalValue

    @totalValue.setter
    def totalValue(self, totalValue: float):
        self.__totalValue = totalValue

    @property
    def discount(self) -> int:
        return self.__discount

    @discount.setter
    def discount(self, discount: int):
        self.__discount = discount

    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def restapp_model_Purchase5(self):
        return self.__restapp_model_Purchase5

    @restapp_model_Purchase5.setter
    def restapp_model_Purchase5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_restapp_model_Purchase__restapp_model_Purchase5", None)
        self.__restapp_model_Purchase5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "User"):
                opp_val = getattr(old_value, "User", None)
                if opp_val == self:
                    setattr(old_value, "User", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "User"):
                opp_val = getattr(value, "User", None)
                setattr(value, "User", self)

    @property
    def restapp_model_Purchase(self):
        return self.__restapp_model_Purchase

    @restapp_model_Purchase.setter
    def restapp_model_Purchase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_restapp_model_Purchase__restapp_model_Purchase", None)
        self.__restapp_model_Purchase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Provider"):
                opp_val = getattr(old_value, "Provider", None)
                if opp_val == self:
                    setattr(old_value, "Provider", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Provider"):
                opp_val = getattr(value, "Provider", None)
                setattr(value, "Provider", self)

class Product:

    pass
class restapp_model_Price:

    def __init__(self, id: int, value: float, date: date, restapp_model_Price: set["Product"] = None):
        self.id = id
        self.value = value
        self.date = date
        self.restapp_model_Price = restapp_model_Price if restapp_model_Price is not None else set()
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def restapp_model_Price(self):
        return self.__restapp_model_Price

    @restapp_model_Price.setter
    def restapp_model_Price(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_restapp_model_Price__restapp_model_Price", None)
        self.__restapp_model_Price = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Product"):
                    opp_val = getattr(item, "Product", None)
                    
                    if opp_val == self:
                        setattr(item, "Product", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Product"):
                    opp_val = getattr(item, "Product", None)
                    
                    setattr(item, "Product", self)
                    

class restapp_model_Category:

    def __init__(self, id: int, name: str, description: str, status: int):
        self.id = id
        self.name = name
        self.description = description
        self.status = status
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def status(self) -> int:
        return self.__status

    @status.setter
    def status(self, status: int):
        self.__status = status

class Employee:

    pass
class restapp_model_User:

    def __init__(self, id: int, user: str, password: str, status: int, restapp_model_User: "Employee" = None):
        self.id = id
        self.user = user
        self.password = password
        self.status = status
        self.restapp_model_User = restapp_model_User
        
    @property
    def status(self) -> int:
        return self.__status

    @status.setter
    def status(self, status: int):
        self.__status = status

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def user(self) -> str:
        return self.__user

    @user.setter
    def user(self, user: str):
        self.__user = user

    @property
    def restapp_model_User(self):
        return self.__restapp_model_User

    @restapp_model_User.setter
    def restapp_model_User(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_restapp_model_User__restapp_model_User", None)
        self.__restapp_model_User = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Employee"):
                opp_val = getattr(old_value, "Employee", None)
                if opp_val == self:
                    setattr(old_value, "Employee", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employee"):
                opp_val = getattr(value, "Employee", None)
                setattr(value, "Employee", self)

class restapp_model_Employee:

    def __init__(self, id: int, name: str, rg: str, cpf: str, address: str, zipcode: str, phone: str, mobile: str, working: bool, contracted: date, fired: date, salary: float, comission: float, status: int):
        self.id = id
        self.name = name
        self.rg = rg
        self.cpf = cpf
        self.address = address
        self.zipcode = zipcode
        self.phone = phone
        self.mobile = mobile
        self.working = working
        self.contracted = contracted
        self.fired = fired
        self.salary = salary
        self.comission = comission
        self.status = status
        
    @property
    def fired(self) -> date:
        return self.__fired

    @fired.setter
    def fired(self, fired: date):
        self.__fired = fired

    @property
    def phone(self) -> str:
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def zipcode(self) -> str:
        return self.__zipcode

    @zipcode.setter
    def zipcode(self, zipcode: str):
        self.__zipcode = zipcode

    @property
    def comission(self) -> float:
        return self.__comission

    @comission.setter
    def comission(self, comission: float):
        self.__comission = comission

    @property
    def status(self) -> int:
        return self.__status

    @status.setter
    def status(self, status: int):
        self.__status = status

    @property
    def mobile(self) -> str:
        return self.__mobile

    @mobile.setter
    def mobile(self, mobile: str):
        self.__mobile = mobile

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def contracted(self) -> date:
        return self.__contracted

    @contracted.setter
    def contracted(self, contracted: date):
        self.__contracted = contracted

    @property
    def working(self) -> bool:
        return self.__working

    @working.setter
    def working(self, working: bool):
        self.__working = working

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def salary(self) -> float:
        return self.__salary

    @salary.setter
    def salary(self, salary: float):
        self.__salary = salary

    @property
    def rg(self) -> str:
        return self.__rg

    @rg.setter
    def rg(self, rg: str):
        self.__rg = rg

    @property
    def cpf(self) -> str:
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address
