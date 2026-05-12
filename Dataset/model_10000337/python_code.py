from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class UserState(Enum):
    pass

############################################
# Definition of Classes
############################################










class lugar:

    def __init__(self, Id_lugar: int, nombre: int, attribute: str, webUser1: "Consulta" = None, items2: "venta" = None):
        self.Id_lugar = Id_lugar
        self.nombre = nombre
        self.attribute = attribute
        self.webUser1 = webUser1
        self.items2 = items2
        
        pass
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: int):
        self.__nombre = nombre

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def Id_lugar(self):
        return self.__Id_lugar
    @Id_lugar.setter
    def Id_lugar(self, Id_lugar: int):
        self.__Id_lugar = Id_lugar

    @property
    def webUser1(self):
        return self.__webUser1
    @webUser1.setter
    def webUser1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lugar__webUser1", None)
        self.__webUser1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shoppingCart0"):
                opp_val = getattr(old_value, "shoppingCart0", None)
                if opp_val == self:
                    setattr(old_value, "shoppingCart0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shoppingCart0"):
                opp_val = getattr(value, "shoppingCart0", None)
                setattr(value, "shoppingCart0", self)

    @property
    def items2(self):
        return self.__items2
    @items2.setter
    def items2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lugar__items2", None)
        self.__items2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sc3"):
                opp_val = getattr(old_value, "sc3", None)
                if opp_val == self:
                    setattr(old_value, "sc3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sc3"):
                opp_val = getattr(value, "sc3", None)
                setattr(value, "sc3", self)



class cliente:

    def __init__(self, paidDate: date, total: float, details: str, order6: "producto" = None):
        self.paidDate = paidDate
        self.total = total
        self.details = details
        self.order6 = order6
        
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
    def order6(self):
        return self.__order6
    @order6.setter
    def order6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cliente__order6", None)
        self.__order6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment7"):
                opp_val = getattr(old_value, "payment7", None)
                if opp_val == self:
                    setattr(old_value, "payment7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment7"):
                opp_val = getattr(value, "payment7", None)
                setattr(value, "payment7", self)



class Empleado:

    def __init__(self, address: str, phone: str, email: str):
        self.address = address
        self.phone = phone
        self.email = email
        
        pass
    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

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



class provvedor:

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        
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



class venta:

    def __init__(self, quantity: int, price: float, sc3: "lugar" = None, order5: "producto" = None):
        self.quantity = quantity
        self.price = price
        self.sc3 = sc3
        self.order5 = order5
        
        pass
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def order5(self):
        return self.__order5
    @order5.setter
    def order5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_venta__order5", None)
        self.__order5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "items4"):
                opp_val = getattr(old_value, "items4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "items4"):
                opp_val = getattr(value, "items4", None)
                if opp_val is None:
                    setattr(value, "items4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sc3(self):
        return self.__sc3
    @sc3.setter
    def sc3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_venta__sc3", None)
        self.__sc3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "items2"):
                opp_val = getattr(old_value, "items2", None)
                if opp_val == self:
                    setattr(old_value, "items2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "items2"):
                opp_val = getattr(value, "items2", None)
                setattr(value, "items2", self)



class producto:

    def __init__(self, number: int, ordered: date, shipped: bool, shipTo: str, total: float, status: str, items4: set["venta"] = None, payment7: "cliente" = None):
        self.number = number
        self.ordered = ordered
        self.shipped = shipped
        self.shipTo = shipTo
        self.total = total
        self.status = status
        self.items4 = items4 if items4 is not None else set()
        self.payment7 = payment7
        
        pass
    @property
    def shipTo(self):
        return self.__shipTo
    @shipTo.setter
    def shipTo(self, shipTo: str):
        self.__shipTo = shipTo

    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, total: float):
        self.__total = total

    @property
    def shipped(self):
        return self.__shipped
    @shipped.setter
    def shipped(self, shipped: bool):
        self.__shipped = shipped

    @property
    def ordered(self):
        return self.__ordered
    @ordered.setter
    def ordered(self, ordered: date):
        self.__ordered = ordered

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def items4(self):
        return self.__items4
    @items4.setter
    def items4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_producto__items4", None)
        self.__items4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "order5"):
                    opp_val = getattr(item, "order5", None)
                    
                    if opp_val == self:
                        setattr(item, "order5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "order5"):
                    opp_val = getattr(item, "order5", None)
                    
                    setattr(item, "order5", self)
                    

    @property
    def payment7(self):
        return self.__payment7
    @payment7.setter
    def payment7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_producto__payment7", None)
        self.__payment7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order6"):
                opp_val = getattr(old_value, "order6", None)
                if opp_val == self:
                    setattr(old_value, "order6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order6"):
                opp_val = getattr(value, "order6", None)
                setattr(value, "order6", self)



class Consulta:

    def __init__(self, Administrador: int, nombre: str, telefono: int, mail: int, shoppingCart0: "lugar" = None):
        self.Administrador = Administrador
        self.nombre = nombre
        self.telefono = telefono
        self.mail = mail
        self.shoppingCart0 = shoppingCart0
        
        pass
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def Administrador(self):
        return self.__Administrador
    @Administrador.setter
    def Administrador(self, Administrador: int):
        self.__Administrador = Administrador

    @property
    def mail(self):
        return self.__mail
    @mail.setter
    def mail(self, mail: int):
        self.__mail = mail

    @property
    def telefono(self):
        return self.__telefono
    @telefono.setter
    def telefono(self, telefono: int):
        self.__telefono = telefono

    @property
    def shoppingCart0(self):
        return self.__shoppingCart0
    @shoppingCart0.setter
    def shoppingCart0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Consulta__shoppingCart0", None)
        self.__shoppingCart0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webUser1"):
                opp_val = getattr(old_value, "webUser1", None)
                if opp_val == self:
                    setattr(old_value, "webUser1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webUser1"):
                opp_val = getattr(value, "webUser1", None)
                setattr(value, "webUser1", self)

