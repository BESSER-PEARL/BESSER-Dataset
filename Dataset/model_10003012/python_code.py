from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Product:

    def __init__(self, id: int, name: str, description: str):
        self.id = id
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

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id



class Order:

    def __init__(self, number: int, ordered: date, shipped: bool, shipTo: str, total: float, status: str, payment9: "Payment" = None, account7: "Account" = None):
        self.number = number
        self.ordered = ordered
        self.shipped = shipped
        self.shipTo = shipTo
        self.total = total
        self.status = status
        self.payment9 = payment9
        self.account7 = account7
        
        pass
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
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def shipTo(self):
        return self.__shipTo
    @shipTo.setter
    def shipTo(self, shipTo: str):
        self.__shipTo = shipTo

    @property
    def account7(self):
        return self.__account7
    @account7.setter
    def account7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__account7", None)
        self.__account7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order6"):
                opp_val = getattr(old_value, "order6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order6"):
                opp_val = getattr(value, "order6", None)
                if opp_val is None:
                    setattr(value, "order6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def payment9(self):
        return self.__payment9
    @payment9.setter
    def payment9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__payment9", None)
        self.__payment9 = value
        
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



class Cliente:

    def __init__(self, Nombre: str, email: str, Contacto: int, Direcci_n: str, shoppingCart2: "Carro_de_Compras" = None):
        self.Nombre = Nombre
        self.email = email
        self.Contacto = Contacto
        self.Direcci_n = Direcci_n
        self.shoppingCart2 = shoppingCart2
        
        pass
    @property
    def Direcci_n(self):
        return self.__Direcci_n
    @Direcci_n.setter
    def Direcci_n(self, Direcci_n: str):
        self.__Direcci_n = Direcci_n

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def Contacto(self):
        return self.__Contacto
    @Contacto.setter
    def Contacto(self, Contacto: int):
        self.__Contacto = Contacto

    @property
    def Nombre(self):
        return self.__Nombre
    @Nombre.setter
    def Nombre(self, Nombre: str):
        self.__Nombre = Nombre

    @property
    def shoppingCart2(self):
        return self.__shoppingCart2
    @shoppingCart2.setter
    def shoppingCart2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cliente__shoppingCart2", None)
        self.__shoppingCart2 = value
        
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



class Account:

    def __init__(self, billingAddress: str, open: date, closed: date, isClosed: bool, p0: set["Payment"] = None, cart4: "Carro_de_Compras" = None, order6: set["Order"] = None):
        self.billingAddress = billingAddress
        self.open = open
        self.closed = closed
        self.isClosed = isClosed
        self.p0 = p0 if p0 is not None else set()
        self.cart4 = cart4
        self.order6 = order6 if order6 is not None else set()
        
        pass
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
    def p0(self):
        return self.__p0
    @p0.setter
    def p0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__p0", None)
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
    def cart4(self):
        return self.__cart4
    @cart4.setter
    def cart4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__cart4", None)
        self.__cart4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account5"):
                opp_val = getattr(old_value, "account5", None)
                if opp_val == self:
                    setattr(old_value, "account5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account5"):
                opp_val = getattr(value, "account5", None)
                setattr(value, "account5", self)

    @property
    def order6(self):
        return self.__order6
    @order6.setter
    def order6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__order6", None)
        self.__order6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "account7"):
                    opp_val = getattr(item, "account7", None)
                    
                    if opp_val == self:
                        setattr(item, "account7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "account7"):
                    opp_val = getattr(item, "account7", None)
                    
                    setattr(item, "account7", self)
                    



class Carro_de_Compras:

    def __init__(self, IdCarro: int, Producto: str, Precio: int, Cantidad: int, webUser3: "Cliente" = None, account5: "Account" = None):
        self.IdCarro = IdCarro
        self.Producto = Producto
        self.Precio = Precio
        self.Cantidad = Cantidad
        self.webUser3 = webUser3
        self.account5 = account5
        
        pass
    @property
    def Precio(self):
        return self.__Precio
    @Precio.setter
    def Precio(self, Precio: int):
        self.__Precio = Precio

    @property
    def Producto(self):
        return self.__Producto
    @Producto.setter
    def Producto(self, Producto: str):
        self.__Producto = Producto

    @property
    def IdCarro(self):
        return self.__IdCarro
    @IdCarro.setter
    def IdCarro(self, IdCarro: int):
        self.__IdCarro = IdCarro

    @property
    def Cantidad(self):
        return self.__Cantidad
    @Cantidad.setter
    def Cantidad(self, Cantidad: int):
        self.__Cantidad = Cantidad

    @property
    def webUser3(self):
        return self.__webUser3
    @webUser3.setter
    def webUser3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Carro_de_Compras__webUser3", None)
        self.__webUser3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shoppingCart2"):
                opp_val = getattr(old_value, "shoppingCart2", None)
                if opp_val == self:
                    setattr(old_value, "shoppingCart2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shoppingCart2"):
                opp_val = getattr(value, "shoppingCart2", None)
                setattr(value, "shoppingCart2", self)

    @property
    def account5(self):
        return self.__account5
    @account5.setter
    def account5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Carro_de_Compras__account5", None)
        self.__account5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cart4"):
                opp_val = getattr(old_value, "cart4", None)
                if opp_val == self:
                    setattr(old_value, "cart4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cart4"):
                opp_val = getattr(value, "cart4", None)
                setattr(value, "cart4", self)



class Payment:

    def __init__(self, paidDate: date, total: float, details: str, order8: "Order" = None, acc1: "Account" = None):
        self.paidDate = paidDate
        self.total = total
        self.details = details
        self.order8 = order8
        self.acc1 = acc1
        
        pass
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
    def paidDate(self):
        return self.__paidDate
    @paidDate.setter
    def paidDate(self, paidDate: date):
        self.__paidDate = paidDate

    @property
    def order8(self):
        return self.__order8
    @order8.setter
    def order8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__order8", None)
        self.__order8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment9"):
                opp_val = getattr(old_value, "payment9", None)
                if opp_val == self:
                    setattr(old_value, "payment9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment9"):
                opp_val = getattr(value, "payment9", None)
                setattr(value, "payment9", self)

    @property
    def acc1(self):
        return self.__acc1
    @acc1.setter
    def acc1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__acc1", None)
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

