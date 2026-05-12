from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class int(Enum):
    pass

############################################
# Definition of Classes
############################################










class Booking:

    def __init__(self, booking_Id: str, type: int, name: str, contact: str, date: str, reservedTables: str, is_in3: "RMS" = None):
        self.booking_Id = booking_Id
        self.type = type
        self.name = name
        self.contact = contact
        self.date = date
        self.reservedTables = reservedTables
        self.is_in3 = is_in3
        
        pass
    @property
    def booking_Id(self):
        return self.__booking_Id
    @booking_Id.setter
    def booking_Id(self, booking_Id: str):
        self.__booking_Id = booking_Id

    @property
    def contact(self):
        return self.__contact
    @contact.setter
    def contact(self, contact: str):
        self.__contact = contact

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: int):
        self.__type = type

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def reservedTables(self):
        return self.__reservedTables
    @reservedTables.setter
    def reservedTables(self, reservedTables: str):
        self.__reservedTables = reservedTables

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def is_in3(self):
        return self.__is_in3
    @is_in3.setter
    def is_in3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Booking__is_in3", None)
        self.__is_in3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "has2"):
                opp_val = getattr(old_value, "has2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "has2"):
                opp_val = getattr(value, "has2", None)
                if opp_val is None:
                    setattr(value, "has2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Report:

    def __init__(self, orders: str, totalSales: str, profit: str, generates4: "RMS" = None):
        self.orders = orders
        self.totalSales = totalSales
        self.profit = profit
        self.generates4 = generates4
        
        pass
    @property
    def orders(self):
        return self.__orders
    @orders.setter
    def orders(self, orders: str):
        self.__orders = orders

    @property
    def totalSales(self):
        return self.__totalSales
    @totalSales.setter
    def totalSales(self, totalSales: str):
        self.__totalSales = totalSales

    @property
    def profit(self):
        return self.__profit
    @profit.setter
    def profit(self, profit: str):
        self.__profit = profit

    @property
    def generates4(self):
        return self.__generates4
    @generates4.setter
    def generates4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Report__generates4", None)
        self.__generates4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "is_generated_by5"):
                opp_val = getattr(old_value, "is_generated_by5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "is_generated_by5"):
                opp_val = getattr(value, "is_generated_by5", None)
                if opp_val is None:
                    setattr(value, "is_generated_by5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class RMS:

    def __init__(self, bookings: str, has2: set["Booking"] = None, is_generated_by5: set["Report"] = None):
        self.bookings = bookings
        self.has2 = has2 if has2 is not None else set()
        self.is_generated_by5 = is_generated_by5 if is_generated_by5 is not None else set()
        
        pass
    @property
    def bookings(self):
        return self.__bookings
    @bookings.setter
    def bookings(self, bookings: str):
        self.__bookings = bookings

    @property
    def has2(self):
        return self.__has2
    @has2.setter
    def has2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RMS__has2", None)
        self.__has2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "is_in3"):
                    opp_val = getattr(item, "is_in3", None)
                    
                    if opp_val == self:
                        setattr(item, "is_in3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "is_in3"):
                    opp_val = getattr(item, "is_in3", None)
                    
                    setattr(item, "is_in3", self)
                    

    @property
    def is_generated_by5(self):
        return self.__is_generated_by5
    @is_generated_by5.setter
    def is_generated_by5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RMS__is_generated_by5", None)
        self.__is_generated_by5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "generates4"):
                    opp_val = getattr(item, "generates4", None)
                    
                    if opp_val == self:
                        setattr(item, "generates4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "generates4"):
                    opp_val = getattr(item, "generates4", None)
                    
                    setattr(item, "generates4", self)
                    



class Vegetariano:

    def __init__(self, tipoDieta: str):
        self.tipoDieta = tipoDieta
        
        pass
    @property
    def tipoDieta(self):
        return self.__tipoDieta
    @tipoDieta.setter
    def tipoDieta(self, tipoDieta: str):
        self.__tipoDieta = tipoDieta



class Class2:

    pass


class Class:

    pass


class Alimento:

    def __init__(self, alimento_Id: str, nombre: str, precio: str, refrigeraci_n: bool, compuesta_por1: set["Orden"] = None):
        self.alimento_Id = alimento_Id
        self.nombre = nombre
        self.precio = precio
        self.refrigeraci_n = refrigeraci_n
        self.compuesta_por1 = compuesta_por1 if compuesta_por1 is not None else set()
        
        pass
    @property
    def refrigeraci_n(self):
        return self.__refrigeraci_n
    @refrigeraci_n.setter
    def refrigeraci_n(self, refrigeraci_n: bool):
        self.__refrigeraci_n = refrigeraci_n

    @property
    def alimento_Id(self):
        return self.__alimento_Id
    @alimento_Id.setter
    def alimento_Id(self, alimento_Id: str):
        self.__alimento_Id = alimento_Id

    @property
    def precio(self):
        return self.__precio
    @precio.setter
    def precio(self, precio: str):
        self.__precio = precio

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def compuesta_por1(self):
        return self.__compuesta_por1
    @compuesta_por1.setter
    def compuesta_por1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Alimento__compuesta_por1", None)
        self.__compuesta_por1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "incluido_en0"):
                    opp_val = getattr(item, "incluido_en0", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "incluido_en0"):
                    opp_val = getattr(item, "incluido_en0", None)
                    
                    if opp_val is None:
                        setattr(item, "incluido_en0", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Orden:

    def __init__(self, orden_Id: str, numComensales: int, fecha: str, mesa: int, preparada: bool, servida: bool, pagada: bool, incluido_en0: set["Alimento"] = None):
        self.orden_Id = orden_Id
        self.numComensales = numComensales
        self.fecha = fecha
        self.mesa = mesa
        self.preparada = preparada
        self.servida = servida
        self.pagada = pagada
        self.incluido_en0 = incluido_en0 if incluido_en0 is not None else set()
        
        pass
    @property
    def pagada(self):
        return self.__pagada
    @pagada.setter
    def pagada(self, pagada: bool):
        self.__pagada = pagada

    @property
    def fecha(self):
        return self.__fecha
    @fecha.setter
    def fecha(self, fecha: str):
        self.__fecha = fecha

    @property
    def servida(self):
        return self.__servida
    @servida.setter
    def servida(self, servida: bool):
        self.__servida = servida

    @property
    def numComensales(self):
        return self.__numComensales
    @numComensales.setter
    def numComensales(self, numComensales: int):
        self.__numComensales = numComensales

    @property
    def orden_Id(self):
        return self.__orden_Id
    @orden_Id.setter
    def orden_Id(self, orden_Id: str):
        self.__orden_Id = orden_Id

    @property
    def preparada(self):
        return self.__preparada
    @preparada.setter
    def preparada(self, preparada: bool):
        self.__preparada = preparada

    @property
    def mesa(self):
        return self.__mesa
    @mesa.setter
    def mesa(self, mesa: int):
        self.__mesa = mesa

    @property
    def incluido_en0(self):
        return self.__incluido_en0
    @incluido_en0.setter
    def incluido_en0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Orden__incluido_en0", None)
        self.__incluido_en0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "compuesta_por1"):
                    opp_val = getattr(item, "compuesta_por1", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "compuesta_por1"):
                    opp_val = getattr(item, "compuesta_por1", None)
                    
                    if opp_val is None:
                        setattr(item, "compuesta_por1", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

