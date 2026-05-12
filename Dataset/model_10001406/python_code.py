from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Starea_comenzii(Enum):
    pass
class StatusulUtilizatorilor(Enum):
    pass

############################################
# Definition of Classes
############################################










class Produse:

    def __init__(self, name: str, description: str, elemente_de_linie12: set["LineItem"] = None):
        self.name = name
        self.description = description
        self.elemente_de_linie12 = elemente_de_linie12 if elemente_de_linie12 is not None else set()
        
        pass
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
    def elemente_de_linie12(self):
        return self.__elemente_de_linie12
    @elemente_de_linie12.setter
    def elemente_de_linie12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Produse__elemente_de_linie12", None)
        self.__elemente_de_linie12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "product13"):
                    opp_val = getattr(item, "product13", None)
                    
                    if opp_val == self:
                        setattr(item, "product13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "product13"):
                    opp_val = getattr(item, "product13", None)
                    
                    setattr(item, "product13", self)
                    



class LineItem:

    def __init__(self, quantity: int, price: float, sc11: "Cosul_de_cumparaturi" = None, product13: "Produse" = None, order15: "Ordin" = None):
        self.quantity = quantity
        self.price = price
        self.sc11 = sc11
        self.product13 = product13
        self.order15 = order15
        
        pass
    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def product13(self):
        return self.__product13
    @product13.setter
    def product13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LineItem__product13", None)
        self.__product13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elemente_de_linie12"):
                opp_val = getattr(old_value, "elemente_de_linie12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elemente_de_linie12"):
                opp_val = getattr(value, "elemente_de_linie12", None)
                if opp_val is None:
                    setattr(value, "elemente_de_linie12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def order15(self):
        return self.__order15
    @order15.setter
    def order15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LineItem__order15", None)
        self.__order15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "articole14"):
                opp_val = getattr(old_value, "articole14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "articole14"):
                opp_val = getattr(value, "articole14", None)
                if opp_val is None:
                    setattr(value, "articole14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sc11(self):
        return self.__sc11
    @sc11.setter
    def sc11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LineItem__sc11", None)
        self.__sc11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "articole10"):
                opp_val = getattr(old_value, "articole10", None)
                if opp_val == self:
                    setattr(old_value, "articole10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "articole10"):
                opp_val = getattr(value, "articole10", None)
                setattr(value, "articole10", self)



class Ordin:

    def __init__(self, number: int, ordered: date, shipped: bool, shipTo: str, total: float, status: Starea_comenzii, articole14: set["LineItem"] = None, cont17: "cont" = None, payment19: "Plata" = None):
        self.number = number
        self.ordered = ordered
        self.shipped = shipped
        self.shipTo = shipTo
        self.total = total
        self.status = status
        self.articole14 = articole14 if articole14 is not None else set()
        self.cont17 = cont17
        self.payment19 = payment19
        
        pass
    @property
    def ordered(self):
        return self.__ordered
    @ordered.setter
    def ordered(self, ordered: date):
        self.__ordered = ordered

    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, total: float):
        self.__total = total

    @property
    def shipTo(self):
        return self.__shipTo
    @shipTo.setter
    def shipTo(self, shipTo: str):
        self.__shipTo = shipTo

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: Starea_comenzii):
        self.__status = status

    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def shipped(self):
        return self.__shipped
    @shipped.setter
    def shipped(self, shipped: bool):
        self.__shipped = shipped

    @property
    def articole14(self):
        return self.__articole14
    @articole14.setter
    def articole14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ordin__articole14", None)
        self.__articole14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "order15"):
                    opp_val = getattr(item, "order15", None)
                    
                    if opp_val == self:
                        setattr(item, "order15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "order15"):
                    opp_val = getattr(item, "order15", None)
                    
                    setattr(item, "order15", self)
                    

    @property
    def payment19(self):
        return self.__payment19
    @payment19.setter
    def payment19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ordin__payment19", None)
        self.__payment19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ordin18"):
                opp_val = getattr(old_value, "ordin18", None)
                if opp_val == self:
                    setattr(old_value, "ordin18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ordin18"):
                opp_val = getattr(value, "ordin18", None)
                setattr(value, "ordin18", self)

    @property
    def cont17(self):
        return self.__cont17
    @cont17.setter
    def cont17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ordin__cont17", None)
        self.__cont17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ordin16"):
                opp_val = getattr(old_value, "ordin16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ordin16"):
                opp_val = getattr(value, "ordin16", None)
                if opp_val is None:
                    setattr(value, "ordin16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class WebUser:

    def __init__(self, login: str, password: str, state: StatusulUtilizatorilor, client4: "client" = None, Cosul_de_cumparaturi2: "Cosul_de_cumparaturi" = None):
        self.login = login
        self.password = password
        self.state = state
        self.client4 = client4
        self.Cosul_de_cumparaturi2 = Cosul_de_cumparaturi2
        
        pass
    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, state: StatusulUtilizatorilor):
        self.__state = state

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
    def client4(self):
        return self.__client4
    @client4.setter
    def client4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WebUser__client4", None)
        self.__client4 = value
        
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
    def Cosul_de_cumparaturi2(self):
        return self.__Cosul_de_cumparaturi2
    @Cosul_de_cumparaturi2.setter
    def Cosul_de_cumparaturi2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WebUser__Cosul_de_cumparaturi2", None)
        self.__Cosul_de_cumparaturi2 = value
        
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



class cont:

    def __init__(self, billingAddress: str, open: date, closed: date, isClosed: bool, client7: "client" = None, cart8: "Cosul_de_cumparaturi" = None, ordin16: set["Ordin"] = None, p0: set["Plata"] = None):
        self.billingAddress = billingAddress
        self.open = open
        self.closed = closed
        self.isClosed = isClosed
        self.client7 = client7
        self.cart8 = cart8
        self.ordin16 = ordin16 if ordin16 is not None else set()
        self.p0 = p0 if p0 is not None else set()
        
        pass
    @property
    def open(self):
        return self.__open
    @open.setter
    def open(self, open: date):
        self.__open = open

    @property
    def billingAddress(self):
        return self.__billingAddress
    @billingAddress.setter
    def billingAddress(self, billingAddress: str):
        self.__billingAddress = billingAddress

    @property
    def closed(self):
        return self.__closed
    @closed.setter
    def closed(self, closed: date):
        self.__closed = closed

    @property
    def isClosed(self):
        return self.__isClosed
    @isClosed.setter
    def isClosed(self, isClosed: bool):
        self.__isClosed = isClosed

    @property
    def cart8(self):
        return self.__cart8
    @cart8.setter
    def cart8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cont__cart8", None)
        self.__cart8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cont9"):
                opp_val = getattr(old_value, "cont9", None)
                if opp_val == self:
                    setattr(old_value, "cont9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cont9"):
                opp_val = getattr(value, "cont9", None)
                setattr(value, "cont9", self)

    @property
    def client7(self):
        return self.__client7
    @client7.setter
    def client7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cont__client7", None)
        self.__client7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cont6"):
                opp_val = getattr(old_value, "cont6", None)
                if opp_val == self:
                    setattr(old_value, "cont6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cont6"):
                opp_val = getattr(value, "cont6", None)
                setattr(value, "cont6", self)

    @property
    def p0(self):
        return self.__p0
    @p0.setter
    def p0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cont__p0", None)
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
    def ordin16(self):
        return self.__ordin16
    @ordin16.setter
    def ordin16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cont__ordin16", None)
        self.__ordin16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cont17"):
                    opp_val = getattr(item, "cont17", None)
                    
                    if opp_val == self:
                        setattr(item, "cont17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cont17"):
                    opp_val = getattr(item, "cont17", None)
                    
                    setattr(item, "cont17", self)
                    



class Cosul_de_cumparaturi:

    def __init__(self, creationDate: date, webUser3: "WebUser" = None, cont9: "cont" = None, articole10: "LineItem" = None):
        self.creationDate = creationDate
        self.webUser3 = webUser3
        self.cont9 = cont9
        self.articole10 = articole10
        
        pass
    @property
    def creationDate(self):
        return self.__creationDate
    @creationDate.setter
    def creationDate(self, creationDate: date):
        self.__creationDate = creationDate

    @property
    def articole10(self):
        return self.__articole10
    @articole10.setter
    def articole10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cosul_de_cumparaturi__articole10", None)
        self.__articole10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sc11"):
                opp_val = getattr(old_value, "sc11", None)
                if opp_val == self:
                    setattr(old_value, "sc11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sc11"):
                opp_val = getattr(value, "sc11", None)
                setattr(value, "sc11", self)

    @property
    def webUser3(self):
        return self.__webUser3
    @webUser3.setter
    def webUser3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cosul_de_cumparaturi__webUser3", None)
        self.__webUser3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Cosul_de_cumparaturi2"):
                opp_val = getattr(old_value, "Cosul_de_cumparaturi2", None)
                if opp_val == self:
                    setattr(old_value, "Cosul_de_cumparaturi2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Cosul_de_cumparaturi2"):
                opp_val = getattr(value, "Cosul_de_cumparaturi2", None)
                setattr(value, "Cosul_de_cumparaturi2", self)

    @property
    def cont9(self):
        return self.__cont9
    @cont9.setter
    def cont9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cosul_de_cumparaturi__cont9", None)
        self.__cont9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cart8"):
                opp_val = getattr(old_value, "cart8", None)
                if opp_val == self:
                    setattr(old_value, "cart8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cart8"):
                opp_val = getattr(value, "cart8", None)
                setattr(value, "cart8", self)



class Plata:

    def __init__(self, paidDate: date, total: float, details: str, ordin18: "Ordin" = None, acc1: "cont" = None):
        self.paidDate = paidDate
        self.total = total
        self.details = details
        self.ordin18 = ordin18
        self.acc1 = acc1
        
        pass
    @property
    def paidDate(self):
        return self.__paidDate
    @paidDate.setter
    def paidDate(self, paidDate: date):
        self.__paidDate = paidDate

    @property
    def details(self):
        return self.__details
    @details.setter
    def details(self, details: str):
        self.__details = details

    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, total: float):
        self.__total = total

    @property
    def acc1(self):
        return self.__acc1
    @acc1.setter
    def acc1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Plata__acc1", None)
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

    @property
    def ordin18(self):
        return self.__ordin18
    @ordin18.setter
    def ordin18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Plata__ordin18", None)
        self.__ordin18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment19"):
                opp_val = getattr(old_value, "payment19", None)
                if opp_val == self:
                    setattr(old_value, "payment19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment19"):
                opp_val = getattr(value, "payment19", None)
                setattr(value, "payment19", self)



class client:

    def __init__(self, address: str, phone: str, email: str, webUser5: "WebUser" = None, cont6: "cont" = None):
        self.address = address
        self.phone = phone
        self.email = email
        self.webUser5 = webUser5
        self.cont6 = cont6
        
        pass
    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def cont6(self):
        return self.__cont6
    @cont6.setter
    def cont6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_client__cont6", None)
        self.__cont6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "client7"):
                opp_val = getattr(old_value, "client7", None)
                if opp_val == self:
                    setattr(old_value, "client7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "client7"):
                opp_val = getattr(value, "client7", None)
                setattr(value, "client7", self)

    @property
    def webUser5(self):
        return self.__webUser5
    @webUser5.setter
    def webUser5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_client__webUser5", None)
        self.__webUser5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "client4"):
                opp_val = getattr(old_value, "client4", None)
                if opp_val == self:
                    setattr(old_value, "client4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "client4"):
                opp_val = getattr(value, "client4", None)
                setattr(value, "client4", self)

