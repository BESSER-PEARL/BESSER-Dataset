from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Entrega_producto:

    def __init__(self, Email_confirmaci_n: str, Agradecimiento: str, lineItems12: set["Lineamiento"] = None):
        self.Email_confirmaci_n = Email_confirmaci_n
        self.Agradecimiento = Agradecimiento
        self.lineItems12 = lineItems12 if lineItems12 is not None else set()
        
        pass
    @property
    def Agradecimiento(self):
        return self.__Agradecimiento
    @Agradecimiento.setter
    def Agradecimiento(self, Agradecimiento: str):
        self.__Agradecimiento = Agradecimiento

    @property
    def Email_confirmaci_n(self):
        return self.__Email_confirmaci_n
    @Email_confirmaci_n.setter
    def Email_confirmaci_n(self, Email_confirmaci_n: str):
        self.__Email_confirmaci_n = Email_confirmaci_n

    @property
    def lineItems12(self):
        return self.__lineItems12
    @lineItems12.setter
    def lineItems12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Entrega_producto__lineItems12", None)
        self.__lineItems12 = value if value is not None else set()
        
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
                    



class Lineamiento:

    def __init__(self, Cantidad: int, Costo: float, account9: "Toma_de_pedido" = None, sc11: "ShoppingCart" = None, product13: "Entrega_producto" = None, order15: "Order" = None):
        self.Cantidad = Cantidad
        self.Costo = Costo
        self.account9 = account9
        self.sc11 = sc11
        self.product13 = product13
        self.order15 = order15
        
        pass
    @property
    def Cantidad(self):
        return self.__Cantidad
    @Cantidad.setter
    def Cantidad(self, Cantidad: int):
        self.__Cantidad = Cantidad

    @property
    def Costo(self):
        return self.__Costo
    @Costo.setter
    def Costo(self, Costo: float):
        self.__Costo = Costo

    @property
    def order15(self):
        return self.__order15
    @order15.setter
    def order15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Lineamiento__order15", None)
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

    @property
    def sc11(self):
        return self.__sc11
    @sc11.setter
    def sc11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Lineamiento__sc11", None)
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
    def product13(self):
        return self.__product13
    @product13.setter
    def product13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Lineamiento__product13", None)
        self.__product13 = value
        
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
    def account9(self):
        return self.__account9
    @account9.setter
    def account9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Lineamiento__account9", None)
        self.__account9 = value
        
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



class Order:

    def __init__(self, number: int, ordered: date, total: float, status: str, payment19: "Pago" = None, items14: set["Lineamiento"] = None, account17: "Toma_de_pedido" = None):
        self.number = number
        self.ordered = ordered
        self.total = total
        self.status = status
        self.payment19 = payment19
        self.items14 = items14 if items14 is not None else set()
        self.account17 = account17
        
        pass
    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

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
    def number(self):
        return self.__number
    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def items14(self):
        return self.__items14
    @items14.setter
    def items14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__items14", None)
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
    def payment19(self):
        return self.__payment19
    @payment19.setter
    def payment19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__payment19", None)
        self.__payment19 = value
        
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

    @property
    def account17(self):
        return self.__account17
    @account17.setter
    def account17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__account17", None)
        self.__account17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order16"):
                opp_val = getattr(old_value, "order16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order16"):
                opp_val = getattr(value, "order16", None)
                if opp_val is None:
                    setattr(value, "order16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class WebADM:

    def __init__(self, login: str, password: str, state: str, shoppingCart2: "ShoppingCart" = None, customer4: "Cliente" = None):
        self.login = login
        self.password = password
        self.state = state
        self.shoppingCart2 = shoppingCart2
        self.customer4 = customer4
        
        pass
    @property
    def login(self):
        return self.__login
    @login.setter
    def login(self, login: str):
        self.__login = login

    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def shoppingCart2(self):
        return self.__shoppingCart2
    @shoppingCart2.setter
    def shoppingCart2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WebADM__shoppingCart2", None)
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

    @property
    def customer4(self):
        return self.__customer4
    @customer4.setter
    def customer4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WebADM__customer4", None)
        self.__customer4 = value
        
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



class Toma_de_pedido:

    def __init__(self, Tipo_de_elemnto: str, Despacho: date, p0: set["Pago"] = None, customer7: "Cliente" = None, cart8: "Lineamiento" = None, order16: set["Order"] = None):
        self.Tipo_de_elemnto = Tipo_de_elemnto
        self.Despacho = Despacho
        self.p0 = p0 if p0 is not None else set()
        self.customer7 = customer7
        self.cart8 = cart8
        self.order16 = order16 if order16 is not None else set()
        
        pass
    @property
    def Despacho(self):
        return self.__Despacho
    @Despacho.setter
    def Despacho(self, Despacho: date):
        self.__Despacho = Despacho

    @property
    def Tipo_de_elemnto(self):
        return self.__Tipo_de_elemnto
    @Tipo_de_elemnto.setter
    def Tipo_de_elemnto(self, Tipo_de_elemnto: str):
        self.__Tipo_de_elemnto = Tipo_de_elemnto

    @property
    def customer7(self):
        return self.__customer7
    @customer7.setter
    def customer7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Toma_de_pedido__customer7", None)
        self.__customer7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account6"):
                opp_val = getattr(old_value, "account6", None)
                if opp_val == self:
                    setattr(old_value, "account6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account6"):
                opp_val = getattr(value, "account6", None)
                setattr(value, "account6", self)

    @property
    def p0(self):
        return self.__p0
    @p0.setter
    def p0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Toma_de_pedido__p0", None)
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
    def cart8(self):
        return self.__cart8
    @cart8.setter
    def cart8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Toma_de_pedido__cart8", None)
        self.__cart8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account9"):
                opp_val = getattr(old_value, "account9", None)
                if opp_val == self:
                    setattr(old_value, "account9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account9"):
                opp_val = getattr(value, "account9", None)
                setattr(value, "account9", self)

    @property
    def order16(self):
        return self.__order16
    @order16.setter
    def order16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Toma_de_pedido__order16", None)
        self.__order16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "account17"):
                    opp_val = getattr(item, "account17", None)
                    
                    if opp_val == self:
                        setattr(item, "account17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "account17"):
                    opp_val = getattr(item, "account17", None)
                    
                    setattr(item, "account17", self)
                    



class ShoppingCart:

    def __init__(self, creationDate: date, webUser3: "WebADM" = None, items10: "Lineamiento" = None):
        self.creationDate = creationDate
        self.webUser3 = webUser3
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
        old_value = getattr(self, f"_ShoppingCart__items10", None)
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
    def webUser3(self):
        return self.__webUser3
    @webUser3.setter
    def webUser3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__webUser3", None)
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



class Pago:

    def __init__(self, Contra_entrega: date, PSI: float, order18: "Order" = None, acc1: "Toma_de_pedido" = None):
        self.Contra_entrega = Contra_entrega
        self.PSI = PSI
        self.order18 = order18
        self.acc1 = acc1
        
        pass
    @property
    def PSI(self):
        return self.__PSI
    @PSI.setter
    def PSI(self, PSI: float):
        self.__PSI = PSI

    @property
    def Contra_entrega(self):
        return self.__Contra_entrega
    @Contra_entrega.setter
    def Contra_entrega(self, Contra_entrega: date):
        self.__Contra_entrega = Contra_entrega

    @property
    def order18(self):
        return self.__order18
    @order18.setter
    def order18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pago__order18", None)
        self.__order18 = value
        
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



class Cliente:

    def __init__(self, Asunto: str, Ciudad: str, Nombre: str, webUser5: "WebADM" = None, account6: "Toma_de_pedido" = None):
        self.Asunto = Asunto
        self.Ciudad = Ciudad
        self.Nombre = Nombre
        self.webUser5 = webUser5
        self.account6 = account6
        
        pass
    @property
    def Asunto(self):
        return self.__Asunto
    @Asunto.setter
    def Asunto(self, Asunto: str):
        self.__Asunto = Asunto

    @property
    def Nombre(self):
        return self.__Nombre
    @Nombre.setter
    def Nombre(self, Nombre: str):
        self.__Nombre = Nombre

    @property
    def Ciudad(self):
        return self.__Ciudad
    @Ciudad.setter
    def Ciudad(self, Ciudad: str):
        self.__Ciudad = Ciudad

    @property
    def account6(self):
        return self.__account6
    @account6.setter
    def account6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cliente__account6", None)
        self.__account6 = value
        
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

    @property
    def webUser5(self):
        return self.__webUser5
    @webUser5.setter
    def webUser5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cliente__webUser5", None)
        self.__webUser5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer4"):
                opp_val = getattr(old_value, "customer4", None)
                if opp_val == self:
                    setattr(old_value, "customer4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer4"):
                opp_val = getattr(value, "customer4", None)
                setattr(value, "customer4", self)

