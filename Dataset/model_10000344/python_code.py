from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Licor:

    def __init__(self, name: str, description: str, lineItems12: set["ItemOrden"] = None):
        self.name = name
        self.description = description
        self.lineItems12 = lineItems12 if lineItems12 is not None else set()
        
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
    def lineItems12(self):
        return self.__lineItems12
    @lineItems12.setter
    def lineItems12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Licor__lineItems12", None)
        self.__lineItems12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Producto13"):
                    opp_val = getattr(item, "Producto13", None)
                    
                    if opp_val == self:
                        setattr(item, "Producto13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Producto13"):
                    opp_val = getattr(item, "Producto13", None)
                    
                    setattr(item, "Producto13", self)
                    



class ItemOrden:

    def __init__(self, quantity: int, price: float, sc11: "Venta" = None, Producto13: "Licor" = None, order15: "Orden" = None):
        self.quantity = quantity
        self.price = price
        self.sc11 = sc11
        self.Producto13 = Producto13
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
    def Producto13(self):
        return self.__Producto13
    @Producto13.setter
    def Producto13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ItemOrden__Producto13", None)
        self.__Producto13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lineItems12"):
                opp_val = getattr(old_value, "lineItems12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lineItems12"):
                opp_val = getattr(value, "lineItems12", None)
                if opp_val is None:
                    setattr(value, "lineItems12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sc11(self):
        return self.__sc11
    @sc11.setter
    def sc11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ItemOrden__sc11", None)
        self.__sc11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "items10"):
                opp_val = getattr(old_value, "items10", None)
                if opp_val == self:
                    setattr(old_value, "items10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "items10"):
                opp_val = getattr(value, "items10", None)
                setattr(value, "items10", self)

    @property
    def order15(self):
        return self.__order15
    @order15.setter
    def order15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ItemOrden__order15", None)
        self.__order15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "items14"):
                opp_val = getattr(old_value, "items14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "items14"):
                opp_val = getattr(value, "items14", None)
                if opp_val is None:
                    setattr(value, "items14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Orden:

    def __init__(self, number: int, ordered: date, shipped: bool, shipTo: str, total: float, status: str, payment19: "Pago" = None, items14: set["ItemOrden"] = None, Cuenta17: "Cuenta" = None):
        self.number = number
        self.ordered = ordered
        self.shipped = shipped
        self.shipTo = shipTo
        self.total = total
        self.status = status
        self.payment19 = payment19
        self.items14 = items14 if items14 is not None else set()
        self.Cuenta17 = Cuenta17
        
        pass
    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, total: float):
        self.__total = total

    @property
    def ordered(self):
        return self.__ordered
    @ordered.setter
    def ordered(self, ordered: date):
        self.__ordered = ordered

    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def shipped(self):
        return self.__shipped
    @shipped.setter
    def shipped(self, shipped: bool):
        self.__shipped = shipped

    @property
    def shipTo(self):
        return self.__shipTo
    @shipTo.setter
    def shipTo(self, shipTo: str):
        self.__shipTo = shipTo

    @property
    def items14(self):
        return self.__items14
    @items14.setter
    def items14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Orden__items14", None)
        self.__items14 = value if value is not None else set()
        
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
    def Cuenta17(self):
        return self.__Cuenta17
    @Cuenta17.setter
    def Cuenta17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Orden__Cuenta17", None)
        self.__Cuenta17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Orden16"):
                opp_val = getattr(old_value, "Orden16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Orden16"):
                opp_val = getattr(value, "Orden16", None)
                if opp_val is None:
                    setattr(value, "Orden16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def payment19(self):
        return self.__payment19
    @payment19.setter
    def payment19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Orden__payment19", None)
        self.__payment19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Orden18"):
                opp_val = getattr(old_value, "Orden18", None)
                if opp_val == self:
                    setattr(old_value, "Orden18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Orden18"):
                opp_val = getattr(value, "Orden18", None)
                setattr(value, "Orden18", self)



class Login:

    def __init__(self, login: str, password: str, state: str, Venta2: "Venta" = None, Vendedor4: "Vendedor" = None):
        self.login = login
        self.password = password
        self.state = state
        self.Venta2 = Venta2
        self.Vendedor4 = Vendedor4
        
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
    def state(self):
        return self.__state
    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def Vendedor4(self):
        return self.__Vendedor4
    @Vendedor4.setter
    def Vendedor4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Login__Vendedor4", None)
        self.__Vendedor4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UsuarioWeb5"):
                opp_val = getattr(old_value, "UsuarioWeb5", None)
                if opp_val == self:
                    setattr(old_value, "UsuarioWeb5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UsuarioWeb5"):
                opp_val = getattr(value, "UsuarioWeb5", None)
                setattr(value, "UsuarioWeb5", self)

    @property
    def Venta2(self):
        return self.__Venta2
    @Venta2.setter
    def Venta2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Login__Venta2", None)
        self.__Venta2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UsuarioWeb3"):
                opp_val = getattr(old_value, "UsuarioWeb3", None)
                if opp_val == self:
                    setattr(old_value, "UsuarioWeb3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UsuarioWeb3"):
                opp_val = getattr(value, "UsuarioWeb3", None)
                setattr(value, "UsuarioWeb3", self)



class Cuenta:

    def __init__(self, billingAddress: str, open: date, closed: date, isClosed: bool, p0: set["Pago"] = None, Vendedor7: "Vendedor" = None, cart8: "Venta" = None, Orden16: set["Orden"] = None):
        self.billingAddress = billingAddress
        self.open = open
        self.closed = closed
        self.isClosed = isClosed
        self.p0 = p0 if p0 is not None else set()
        self.Vendedor7 = Vendedor7
        self.cart8 = cart8
        self.Orden16 = Orden16 if Orden16 is not None else set()
        
        pass
    @property
    def isClosed(self):
        return self.__isClosed
    @isClosed.setter
    def isClosed(self, isClosed: bool):
        self.__isClosed = isClosed

    @property
    def closed(self):
        return self.__closed
    @closed.setter
    def closed(self, closed: date):
        self.__closed = closed

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
    def cart8(self):
        return self.__cart8
    @cart8.setter
    def cart8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cuenta__cart8", None)
        self.__cart8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Cuenta9"):
                opp_val = getattr(old_value, "Cuenta9", None)
                if opp_val == self:
                    setattr(old_value, "Cuenta9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Cuenta9"):
                opp_val = getattr(value, "Cuenta9", None)
                setattr(value, "Cuenta9", self)

    @property
    def p0(self):
        return self.__p0
    @p0.setter
    def p0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cuenta__p0", None)
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
    def Vendedor7(self):
        return self.__Vendedor7
    @Vendedor7.setter
    def Vendedor7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cuenta__Vendedor7", None)
        self.__Vendedor7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Cuenta6"):
                opp_val = getattr(old_value, "Cuenta6", None)
                if opp_val == self:
                    setattr(old_value, "Cuenta6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Cuenta6"):
                opp_val = getattr(value, "Cuenta6", None)
                setattr(value, "Cuenta6", self)

    @property
    def Orden16(self):
        return self.__Orden16
    @Orden16.setter
    def Orden16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cuenta__Orden16", None)
        self.__Orden16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Cuenta17"):
                    opp_val = getattr(item, "Cuenta17", None)
                    
                    if opp_val == self:
                        setattr(item, "Cuenta17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Cuenta17"):
                    opp_val = getattr(item, "Cuenta17", None)
                    
                    setattr(item, "Cuenta17", self)
                    



class Venta:

    def __init__(self, creationDate: date, UsuarioWeb3: "Login" = None, Cuenta9: "Cuenta" = None, items10: "ItemOrden" = None):
        self.creationDate = creationDate
        self.UsuarioWeb3 = UsuarioWeb3
        self.Cuenta9 = Cuenta9
        self.items10 = items10
        
        pass
    @property
    def creationDate(self):
        return self.__creationDate
    @creationDate.setter
    def creationDate(self, creationDate: date):
        self.__creationDate = creationDate

    @property
    def items10(self):
        return self.__items10
    @items10.setter
    def items10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Venta__items10", None)
        self.__items10 = value
        
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
    def UsuarioWeb3(self):
        return self.__UsuarioWeb3
    @UsuarioWeb3.setter
    def UsuarioWeb3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Venta__UsuarioWeb3", None)
        self.__UsuarioWeb3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Venta2"):
                opp_val = getattr(old_value, "Venta2", None)
                if opp_val == self:
                    setattr(old_value, "Venta2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Venta2"):
                opp_val = getattr(value, "Venta2", None)
                setattr(value, "Venta2", self)

    @property
    def Cuenta9(self):
        return self.__Cuenta9
    @Cuenta9.setter
    def Cuenta9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Venta__Cuenta9", None)
        self.__Cuenta9 = value
        
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



class Pago:

    def __init__(self, paidDate: date, total: float, details: str, Orden18: "Orden" = None, acc1: "Cuenta" = None):
        self.paidDate = paidDate
        self.total = total
        self.details = details
        self.Orden18 = Orden18
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
    def acc1(self):
        return self.__acc1
    @acc1.setter
    def acc1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pago__acc1", None)
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
    def Orden18(self):
        return self.__Orden18
    @Orden18.setter
    def Orden18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pago__Orden18", None)
        self.__Orden18 = value
        
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



class Vendedor:

    def __init__(self, address: str, phone: str, email: str, UsuarioWeb5: "Login" = None, Cuenta6: "Cuenta" = None):
        self.address = address
        self.phone = phone
        self.email = email
        self.UsuarioWeb5 = UsuarioWeb5
        self.Cuenta6 = Cuenta6
        
        pass
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
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def UsuarioWeb5(self):
        return self.__UsuarioWeb5
    @UsuarioWeb5.setter
    def UsuarioWeb5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Vendedor__UsuarioWeb5", None)
        self.__UsuarioWeb5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vendedor4"):
                opp_val = getattr(old_value, "Vendedor4", None)
                if opp_val == self:
                    setattr(old_value, "Vendedor4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vendedor4"):
                opp_val = getattr(value, "Vendedor4", None)
                setattr(value, "Vendedor4", self)

    @property
    def Cuenta6(self):
        return self.__Cuenta6
    @Cuenta6.setter
    def Cuenta6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Vendedor__Cuenta6", None)
        self.__Cuenta6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vendedor7"):
                opp_val = getattr(old_value, "Vendedor7", None)
                if opp_val == self:
                    setattr(old_value, "Vendedor7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vendedor7"):
                opp_val = getattr(value, "Vendedor7", None)
                setattr(value, "Vendedor7", self)

