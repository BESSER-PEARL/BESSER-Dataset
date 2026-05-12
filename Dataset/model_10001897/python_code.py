from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class _Actor:

    pass


class Actor_Actor:

    pass


class Dependencias_Actor:

    pass


class Proveedores_Actor:

    pass


class Juridico_Actor:

    pass


class Natural_Actor:

    pass


class Cliente_Actor:

    pass





class Clasificar_Producto_external:

    pass


class Entregar_Productos_external:

    pass


class Resivir_ordenes_de_suministros_external:

    pass


class Registrar_proveedores_external:

    pass


class Recibir_productos_o_pedidos_external:

    pass


class Brindar_consultoria_external:

    pass


class impuesto:

    def __init__(self, setPorcentaje: float, producto56: "producto" = None):
        self.setPorcentaje = setPorcentaje
        self.producto56 = producto56
        
        pass
    @property
    def setPorcentaje(self):
        return self.__setPorcentaje
    @setPorcentaje.setter
    def setPorcentaje(self, setPorcentaje: float):
        self.__setPorcentaje = setPorcentaje

    @property
    def producto56(self):
        return self.__producto56
    @producto56.setter
    def producto56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_impuesto__producto56", None)
        self.__producto56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "impuesto57"):
                opp_val = getattr(old_value, "impuesto57", None)
                if opp_val == self:
                    setattr(old_value, "impuesto57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "impuesto57"):
                opp_val = getattr(value, "impuesto57", None)
                setattr(value, "impuesto57", self)



class producto:

    def __init__(self, setCodigo: str, setNombre: str, setPrecio: float, setCantidad: int, impuesto57: "impuesto" = None, venta54: "venta" = None):
        self.setCodigo = setCodigo
        self.setNombre = setNombre
        self.setPrecio = setPrecio
        self.setCantidad = setCantidad
        self.impuesto57 = impuesto57
        self.venta54 = venta54
        
        pass
    @property
    def setCantidad(self):
        return self.__setCantidad
    @setCantidad.setter
    def setCantidad(self, setCantidad: int):
        self.__setCantidad = setCantidad

    @property
    def setCodigo(self):
        return self.__setCodigo
    @setCodigo.setter
    def setCodigo(self, setCodigo: str):
        self.__setCodigo = setCodigo

    @property
    def setPrecio(self):
        return self.__setPrecio
    @setPrecio.setter
    def setPrecio(self, setPrecio: float):
        self.__setPrecio = setPrecio

    @property
    def setNombre(self):
        return self.__setNombre
    @setNombre.setter
    def setNombre(self, setNombre: str):
        self.__setNombre = setNombre

    @property
    def impuesto57(self):
        return self.__impuesto57
    @impuesto57.setter
    def impuesto57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_producto__impuesto57", None)
        self.__impuesto57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "producto56"):
                opp_val = getattr(old_value, "producto56", None)
                if opp_val == self:
                    setattr(old_value, "producto56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "producto56"):
                opp_val = getattr(value, "producto56", None)
                setattr(value, "producto56", self)

    @property
    def venta54(self):
        return self.__venta54
    @venta54.setter
    def venta54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_producto__venta54", None)
        self.__venta54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "producto55"):
                opp_val = getattr(old_value, "producto55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "producto55"):
                opp_val = getattr(value, "producto55", None)
                if opp_val is None:
                    setattr(value, "producto55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class venta:

    def __init__(self, Setcodigo: str, setFecha: str, producto55: set["producto"] = None):
        self.Setcodigo = Setcodigo
        self.setFecha = setFecha
        self.producto55 = producto55 if producto55 is not None else set()
        
        pass
    @property
    def setFecha(self):
        return self.__setFecha
    @setFecha.setter
    def setFecha(self, setFecha: str):
        self.__setFecha = setFecha

    @property
    def Setcodigo(self):
        return self.__Setcodigo
    @Setcodigo.setter
    def Setcodigo(self, Setcodigo: str):
        self.__Setcodigo = Setcodigo

    @property
    def producto55(self):
        return self.__producto55
    @producto55.setter
    def producto55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_venta__producto55", None)
        self.__producto55 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "venta54"):
                    opp_val = getattr(item, "venta54", None)
                    
                    if opp_val == self:
                        setattr(item, "venta54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "venta54"):
                    opp_val = getattr(item, "venta54", None)
                    
                    setattr(item, "venta54", self)
                    



class JavaApplication2:

    pass


class Cacular:

    pass


class Servidor_Intel_Node:

    pass


class Pedidos1:

    def __init__(self, codigo: str, fecha: str, empresa48: "Empresa" = None, compa_ia51: set["Compa_ia"] = None):
        self.codigo = codigo
        self.fecha = fecha
        self.empresa48 = empresa48
        self.compa_ia51 = compa_ia51 if compa_ia51 is not None else set()
        
        pass
    @property
    def fecha(self):
        return self.__fecha
    @fecha.setter
    def fecha(self, fecha: str):
        self.__fecha = fecha

    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, codigo: str):
        self.__codigo = codigo

    @property
    def compa_ia51(self):
        return self.__compa_ia51
    @compa_ia51.setter
    def compa_ia51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pedidos1__compa_ia51", None)
        self.__compa_ia51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pedidos50"):
                    opp_val = getattr(item, "pedidos50", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pedidos50"):
                    opp_val = getattr(item, "pedidos50", None)
                    
                    if opp_val is None:
                        setattr(item, "pedidos50", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def empresa48(self):
        return self.__empresa48
    @empresa48.setter
    def empresa48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pedidos1__empresa48", None)
        self.__empresa48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pedidos49"):
                opp_val = getattr(old_value, "pedidos49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pedidos49"):
                opp_val = getattr(value, "pedidos49", None)
                if opp_val is None:
                    setattr(value, "pedidos49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Pago:

    def __init__(self, Codigo: str, Fecha: str, facturas45: set["Facturas"] = None):
        self.Codigo = Codigo
        self.Fecha = Fecha
        self.facturas45 = facturas45 if facturas45 is not None else set()
        
        pass
    @property
    def Codigo(self):
        return self.__Codigo
    @Codigo.setter
    def Codigo(self, Codigo: str):
        self.__Codigo = Codigo

    @property
    def Fecha(self):
        return self.__Fecha
    @Fecha.setter
    def Fecha(self, Fecha: str):
        self.__Fecha = Fecha

    @property
    def facturas45(self):
        return self.__facturas45
    @facturas45.setter
    def facturas45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pago__facturas45", None)
        self.__facturas45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cancela44"):
                    opp_val = getattr(item, "cancela44", None)
                    
                    if opp_val == self:
                        setattr(item, "cancela44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cancela44"):
                    opp_val = getattr(item, "cancela44", None)
                    
                    setattr(item, "cancela44", self)
                    



class ventas:

    def __init__(self, fechadeventas: str, valordeventa: str, comerciales42: "Comerciales" = None):
        self.fechadeventas = fechadeventas
        self.valordeventa = valordeventa
        self.comerciales42 = comerciales42
        
        pass
    @property
    def fechadeventas(self):
        return self.__fechadeventas
    @fechadeventas.setter
    def fechadeventas(self, fechadeventas: str):
        self.__fechadeventas = fechadeventas

    @property
    def valordeventa(self):
        return self.__valordeventa
    @valordeventa.setter
    def valordeventa(self, valordeventa: str):
        self.__valordeventa = valordeventa

    @property
    def comerciales42(self):
        return self.__comerciales42
    @comerciales42.setter
    def comerciales42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ventas__comerciales42", None)
        self.__comerciales42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ventas43"):
                opp_val = getattr(old_value, "ventas43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ventas43"):
                opp_val = getattr(value, "ventas43", None)
                if opp_val is None:
                    setattr(value, "ventas43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Compa_ia:

    def __init__(self, codigo: str, zona: str, comerciales40: set["Comerciales"] = None, facturas47: set["Facturas"] = None, pedidos50: set["Pedidos1"] = None):
        self.codigo = codigo
        self.zona = zona
        self.comerciales40 = comerciales40 if comerciales40 is not None else set()
        self.facturas47 = facturas47 if facturas47 is not None else set()
        self.pedidos50 = pedidos50 if pedidos50 is not None else set()
        
        pass
    @property
    def zona(self):
        return self.__zona
    @zona.setter
    def zona(self, zona: str):
        self.__zona = zona

    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, codigo: str):
        self.__codigo = codigo

    @property
    def pedidos50(self):
        return self.__pedidos50
    @pedidos50.setter
    def pedidos50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Compa_ia__pedidos50", None)
        self.__pedidos50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "compa_ia51"):
                    opp_val = getattr(item, "compa_ia51", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "compa_ia51"):
                    opp_val = getattr(item, "compa_ia51", None)
                    
                    if opp_val is None:
                        setattr(item, "compa_ia51", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def comerciales40(self):
        return self.__comerciales40
    @comerciales40.setter
    def comerciales40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Compa_ia__comerciales40", None)
        self.__comerciales40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "compa_ia41"):
                    opp_val = getattr(item, "compa_ia41", None)
                    
                    if opp_val == self:
                        setattr(item, "compa_ia41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "compa_ia41"):
                    opp_val = getattr(item, "compa_ia41", None)
                    
                    setattr(item, "compa_ia41", self)
                    

    @property
    def facturas47(self):
        return self.__facturas47
    @facturas47.setter
    def facturas47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Compa_ia__facturas47", None)
        self.__facturas47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "compa_ia46"):
                    opp_val = getattr(item, "compa_ia46", None)
                    
                    if opp_val == self:
                        setattr(item, "compa_ia46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "compa_ia46"):
                    opp_val = getattr(item, "compa_ia46", None)
                    
                    setattr(item, "compa_ia46", self)
                    



class CuentaBanco:

    def __init__(self, nombreBanco: str, numeroCuenta: str, tipoCuenta: str):
        self.nombreBanco = nombreBanco
        self.numeroCuenta = numeroCuenta
        self.tipoCuenta = tipoCuenta
        
        pass
    @property
    def numeroCuenta(self):
        return self.__numeroCuenta
    @numeroCuenta.setter
    def numeroCuenta(self, numeroCuenta: str):
        self.__numeroCuenta = numeroCuenta

    @property
    def nombreBanco(self):
        return self.__nombreBanco
    @nombreBanco.setter
    def nombreBanco(self, nombreBanco: str):
        self.__nombreBanco = nombreBanco

    @property
    def tipoCuenta(self):
        return self.__tipoCuenta
    @tipoCuenta.setter
    def tipoCuenta(self, tipoCuenta: str):
        self.__tipoCuenta = tipoCuenta



class TransferenciaCompa_ia:

    def __init__(self, numerodecuenta: str):
        self.numerodecuenta = numerodecuenta
        
        pass
    @property
    def numerodecuenta(self):
        return self.__numerodecuenta
    @numerodecuenta.setter
    def numerodecuenta(self, numerodecuenta: str):
        self.__numerodecuenta = numerodecuenta



class Imformes:

    pass


class Empresa:

    def __init__(self, codigo: str, nombre: str, ubicacion: str, gastos33: set["Presupuesto"] = None, facturas39: set["Facturas"] = None, pedidos49: set["Pedidos1"] = None):
        self.codigo = codigo
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.gastos33 = gastos33 if gastos33 is not None else set()
        self.facturas39 = facturas39 if facturas39 is not None else set()
        self.pedidos49 = pedidos49 if pedidos49 is not None else set()
        
        pass
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, codigo: str):
        self.__codigo = codigo

    @property
    def ubicacion(self):
        return self.__ubicacion
    @ubicacion.setter
    def ubicacion(self, ubicacion: str):
        self.__ubicacion = ubicacion

    @property
    def gastos33(self):
        return self.__gastos33
    @gastos33.setter
    def gastos33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Empresa__gastos33", None)
        self.__gastos33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "empresa32"):
                    opp_val = getattr(item, "empresa32", None)
                    
                    if opp_val == self:
                        setattr(item, "empresa32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "empresa32"):
                    opp_val = getattr(item, "empresa32", None)
                    
                    setattr(item, "empresa32", self)
                    

    @property
    def facturas39(self):
        return self.__facturas39
    @facturas39.setter
    def facturas39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Empresa__facturas39", None)
        self.__facturas39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "empresa38"):
                    opp_val = getattr(item, "empresa38", None)
                    
                    if opp_val == self:
                        setattr(item, "empresa38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "empresa38"):
                    opp_val = getattr(item, "empresa38", None)
                    
                    setattr(item, "empresa38", self)
                    

    @property
    def pedidos49(self):
        return self.__pedidos49
    @pedidos49.setter
    def pedidos49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Empresa__pedidos49", None)
        self.__pedidos49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "empresa48"):
                    opp_val = getattr(item, "empresa48", None)
                    
                    if opp_val == self:
                        setattr(item, "empresa48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "empresa48"):
                    opp_val = getattr(item, "empresa48", None)
                    
                    setattr(item, "empresa48", self)
                    



class Comerciales:

    def __init__(self, Id: str, Nombre: str, Zona: str, gastos31: "Presupuesto" = None, facturas34: "Facturas" = None, ingresos37: set["Imformes"] = None, compa_ia41: "Compa_ia" = None, ventas43: set["ventas"] = None):
        self.Id = Id
        self.Nombre = Nombre
        self.Zona = Zona
        self.gastos31 = gastos31
        self.facturas34 = facturas34
        self.ingresos37 = ingresos37 if ingresos37 is not None else set()
        self.compa_ia41 = compa_ia41
        self.ventas43 = ventas43 if ventas43 is not None else set()
        
        pass
    @property
    def Zona(self):
        return self.__Zona
    @Zona.setter
    def Zona(self, Zona: str):
        self.__Zona = Zona

    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: str):
        self.__Id = Id

    @property
    def Nombre(self):
        return self.__Nombre
    @Nombre.setter
    def Nombre(self, Nombre: str):
        self.__Nombre = Nombre

    @property
    def ingresos37(self):
        return self.__ingresos37
    @ingresos37.setter
    def ingresos37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Comerciales__ingresos37", None)
        self.__ingresos37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "comerciales36"):
                    opp_val = getattr(item, "comerciales36", None)
                    
                    if opp_val == self:
                        setattr(item, "comerciales36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "comerciales36"):
                    opp_val = getattr(item, "comerciales36", None)
                    
                    setattr(item, "comerciales36", self)
                    

    @property
    def gastos31(self):
        return self.__gastos31
    @gastos31.setter
    def gastos31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Comerciales__gastos31", None)
        self.__gastos31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "comerciales30"):
                opp_val = getattr(old_value, "comerciales30", None)
                if opp_val == self:
                    setattr(old_value, "comerciales30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "comerciales30"):
                opp_val = getattr(value, "comerciales30", None)
                setattr(value, "comerciales30", self)

    @property
    def ventas43(self):
        return self.__ventas43
    @ventas43.setter
    def ventas43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Comerciales__ventas43", None)
        self.__ventas43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "comerciales42"):
                    opp_val = getattr(item, "comerciales42", None)
                    
                    if opp_val == self:
                        setattr(item, "comerciales42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "comerciales42"):
                    opp_val = getattr(item, "comerciales42", None)
                    
                    setattr(item, "comerciales42", self)
                    

    @property
    def facturas34(self):
        return self.__facturas34
    @facturas34.setter
    def facturas34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Comerciales__facturas34", None)
        self.__facturas34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "comerciales35"):
                opp_val = getattr(old_value, "comerciales35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "comerciales35"):
                opp_val = getattr(value, "comerciales35", None)
                if opp_val is None:
                    setattr(value, "comerciales35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def compa_ia41(self):
        return self.__compa_ia41
    @compa_ia41.setter
    def compa_ia41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Comerciales__compa_ia41", None)
        self.__compa_ia41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "comerciales40"):
                opp_val = getattr(old_value, "comerciales40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "comerciales40"):
                opp_val = getattr(value, "comerciales40", None)
                if opp_val is None:
                    setattr(value, "comerciales40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Facturas:

    def __init__(self, codigo: str, nombre: str, nif: str, direccionPostal: str, comerciales35: set["Comerciales"] = None, empresa38: "Empresa" = None, cancela44: "Pago" = None, compa_ia46: "Compa_ia" = None):
        self.codigo = codigo
        self.nombre = nombre
        self.nif = nif
        self.direccionPostal = direccionPostal
        self.comerciales35 = comerciales35 if comerciales35 is not None else set()
        self.empresa38 = empresa38
        self.cancela44 = cancela44
        self.compa_ia46 = compa_ia46
        
        pass
    @property
    def nif(self):
        return self.__nif
    @nif.setter
    def nif(self, nif: str):
        self.__nif = nif

    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, codigo: str):
        self.__codigo = codigo

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def direccionPostal(self):
        return self.__direccionPostal
    @direccionPostal.setter
    def direccionPostal(self, direccionPostal: str):
        self.__direccionPostal = direccionPostal

    @property
    def cancela44(self):
        return self.__cancela44
    @cancela44.setter
    def cancela44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Facturas__cancela44", None)
        self.__cancela44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "facturas45"):
                opp_val = getattr(old_value, "facturas45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "facturas45"):
                opp_val = getattr(value, "facturas45", None)
                if opp_val is None:
                    setattr(value, "facturas45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def comerciales35(self):
        return self.__comerciales35
    @comerciales35.setter
    def comerciales35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Facturas__comerciales35", None)
        self.__comerciales35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "facturas34"):
                    opp_val = getattr(item, "facturas34", None)
                    
                    if opp_val == self:
                        setattr(item, "facturas34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "facturas34"):
                    opp_val = getattr(item, "facturas34", None)
                    
                    setattr(item, "facturas34", self)
                    

    @property
    def empresa38(self):
        return self.__empresa38
    @empresa38.setter
    def empresa38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Facturas__empresa38", None)
        self.__empresa38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "facturas39"):
                opp_val = getattr(old_value, "facturas39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "facturas39"):
                opp_val = getattr(value, "facturas39", None)
                if opp_val is None:
                    setattr(value, "facturas39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def compa_ia46(self):
        return self.__compa_ia46
    @compa_ia46.setter
    def compa_ia46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Facturas__compa_ia46", None)
        self.__compa_ia46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "facturas47"):
                opp_val = getattr(old_value, "facturas47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "facturas47"):
                opp_val = getattr(value, "facturas47", None)
                if opp_val is None:
                    setattr(value, "facturas47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Presupuesto:

    pass


class Pedidos:

    def __init__(self, Codigo: str, Fecha: str, proveedores17: "Proveedores" = None):
        self.Codigo = Codigo
        self.Fecha = Fecha
        self.proveedores17 = proveedores17
        
        pass
    @property
    def Codigo(self):
        return self.__Codigo
    @Codigo.setter
    def Codigo(self, Codigo: str):
        self.__Codigo = Codigo

    @property
    def Fecha(self):
        return self.__Fecha
    @Fecha.setter
    def Fecha(self, Fecha: str):
        self.__Fecha = Fecha

    @property
    def proveedores17(self):
        return self.__proveedores17
    @proveedores17.setter
    def proveedores17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pedidos__proveedores17", None)
        self.__proveedores17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pedidos16"):
                opp_val = getattr(old_value, "pedidos16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pedidos16"):
                opp_val = getattr(value, "pedidos16", None)
                if opp_val is None:
                    setattr(value, "pedidos16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Dependencia:

    def __init__(self, Codigo: str, Nombre: str, Responsable: str, solicitud_suministro24: set["Solicitud_suministro"] = None):
        self.Codigo = Codigo
        self.Nombre = Nombre
        self.Responsable = Responsable
        self.solicitud_suministro24 = solicitud_suministro24 if solicitud_suministro24 is not None else set()
        
        pass
    @property
    def Responsable(self):
        return self.__Responsable
    @Responsable.setter
    def Responsable(self, Responsable: str):
        self.__Responsable = Responsable

    @property
    def Nombre(self):
        return self.__Nombre
    @Nombre.setter
    def Nombre(self, Nombre: str):
        self.__Nombre = Nombre

    @property
    def Codigo(self):
        return self.__Codigo
    @Codigo.setter
    def Codigo(self, Codigo: str):
        self.__Codigo = Codigo

    @property
    def solicitud_suministro24(self):
        return self.__solicitud_suministro24
    @solicitud_suministro24.setter
    def solicitud_suministro24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dependencia__solicitud_suministro24", None)
        self.__solicitud_suministro24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dependencia25"):
                    opp_val = getattr(item, "dependencia25", None)
                    
                    if opp_val == self:
                        setattr(item, "dependencia25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dependencia25"):
                    opp_val = getattr(item, "dependencia25", None)
                    
                    setattr(item, "dependencia25", self)
                    



class Proveedores:

    def __init__(self, Nit: str, RazonSocial: str, Direccion: str, Telefono: str, ordenes_Perdidos14: set["Ordenes_Perdidos"] = None, pedidos16: set["Pedidos"] = None, factura27: set["Factura"] = None):
        self.Nit = Nit
        self.RazonSocial = RazonSocial
        self.Direccion = Direccion
        self.Telefono = Telefono
        self.ordenes_Perdidos14 = ordenes_Perdidos14 if ordenes_Perdidos14 is not None else set()
        self.pedidos16 = pedidos16 if pedidos16 is not None else set()
        self.factura27 = factura27 if factura27 is not None else set()
        
        pass
    @property
    def Nit(self):
        return self.__Nit
    @Nit.setter
    def Nit(self, Nit: str):
        self.__Nit = Nit

    @property
    def Telefono(self):
        return self.__Telefono
    @Telefono.setter
    def Telefono(self, Telefono: str):
        self.__Telefono = Telefono

    @property
    def RazonSocial(self):
        return self.__RazonSocial
    @RazonSocial.setter
    def RazonSocial(self, RazonSocial: str):
        self.__RazonSocial = RazonSocial

    @property
    def Direccion(self):
        return self.__Direccion
    @Direccion.setter
    def Direccion(self, Direccion: str):
        self.__Direccion = Direccion

    @property
    def ordenes_Perdidos14(self):
        return self.__ordenes_Perdidos14
    @ordenes_Perdidos14.setter
    def ordenes_Perdidos14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Proveedores__ordenes_Perdidos14", None)
        self.__ordenes_Perdidos14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "proveedores15"):
                    opp_val = getattr(item, "proveedores15", None)
                    
                    if opp_val == self:
                        setattr(item, "proveedores15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "proveedores15"):
                    opp_val = getattr(item, "proveedores15", None)
                    
                    setattr(item, "proveedores15", self)
                    

    @property
    def factura27(self):
        return self.__factura27
    @factura27.setter
    def factura27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Proveedores__factura27", None)
        self.__factura27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "proveedores26"):
                    opp_val = getattr(item, "proveedores26", None)
                    
                    if opp_val == self:
                        setattr(item, "proveedores26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "proveedores26"):
                    opp_val = getattr(item, "proveedores26", None)
                    
                    setattr(item, "proveedores26", self)
                    

    @property
    def pedidos16(self):
        return self.__pedidos16
    @pedidos16.setter
    def pedidos16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Proveedores__pedidos16", None)
        self.__pedidos16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "proveedores17"):
                    opp_val = getattr(item, "proveedores17", None)
                    
                    if opp_val == self:
                        setattr(item, "proveedores17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "proveedores17"):
                    opp_val = getattr(item, "proveedores17", None)
                    
                    setattr(item, "proveedores17", self)
                    



class Elementos:

    def __init__(self, Referencia: str, Clasificacion: str, ordenes_Perdidos19: set["Ordenes_Perdidos"] = None, solicitud_suministro21: set["Solicitud_suministro"] = None, factura28: set["Factura"] = None):
        self.Referencia = Referencia
        self.Clasificacion = Clasificacion
        self.ordenes_Perdidos19 = ordenes_Perdidos19 if ordenes_Perdidos19 is not None else set()
        self.solicitud_suministro21 = solicitud_suministro21 if solicitud_suministro21 is not None else set()
        self.factura28 = factura28 if factura28 is not None else set()
        
        pass
    @property
    def Referencia(self):
        return self.__Referencia
    @Referencia.setter
    def Referencia(self, Referencia: str):
        self.__Referencia = Referencia

    @property
    def Clasificacion(self):
        return self.__Clasificacion
    @Clasificacion.setter
    def Clasificacion(self, Clasificacion: str):
        self.__Clasificacion = Clasificacion

    @property
    def solicitud_suministro21(self):
        return self.__solicitud_suministro21
    @solicitud_suministro21.setter
    def solicitud_suministro21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elementos__solicitud_suministro21", None)
        self.__solicitud_suministro21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "elementos20"):
                    opp_val = getattr(item, "elementos20", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "elementos20"):
                    opp_val = getattr(item, "elementos20", None)
                    
                    if opp_val is None:
                        setattr(item, "elementos20", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def ordenes_Perdidos19(self):
        return self.__ordenes_Perdidos19
    @ordenes_Perdidos19.setter
    def ordenes_Perdidos19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elementos__ordenes_Perdidos19", None)
        self.__ordenes_Perdidos19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "elementos18"):
                    opp_val = getattr(item, "elementos18", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "elementos18"):
                    opp_val = getattr(item, "elementos18", None)
                    
                    if opp_val is None:
                        setattr(item, "elementos18", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def factura28(self):
        return self.__factura28
    @factura28.setter
    def factura28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elementos__factura28", None)
        self.__factura28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "elementos29"):
                    opp_val = getattr(item, "elementos29", None)
                    
                    if opp_val == self:
                        setattr(item, "elementos29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "elementos29"):
                    opp_val = getattr(item, "elementos29", None)
                    
                    setattr(item, "elementos29", self)
                    



class Solicitud_suministro:

    def __init__(self, Codigo: str, Fecha: str, elementos20: set["Elementos"] = None, ordenes_Perdidos22: "Ordenes_Perdidos" = None, dependencia25: "Dependencia" = None):
        self.Codigo = Codigo
        self.Fecha = Fecha
        self.elementos20 = elementos20 if elementos20 is not None else set()
        self.ordenes_Perdidos22 = ordenes_Perdidos22
        self.dependencia25 = dependencia25
        
        pass
    @property
    def Fecha(self):
        return self.__Fecha
    @Fecha.setter
    def Fecha(self, Fecha: str):
        self.__Fecha = Fecha

    @property
    def Codigo(self):
        return self.__Codigo
    @Codigo.setter
    def Codigo(self, Codigo: str):
        self.__Codigo = Codigo

    @property
    def elementos20(self):
        return self.__elementos20
    @elementos20.setter
    def elementos20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Solicitud_suministro__elementos20", None)
        self.__elementos20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "solicitud_suministro21"):
                    opp_val = getattr(item, "solicitud_suministro21", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "solicitud_suministro21"):
                    opp_val = getattr(item, "solicitud_suministro21", None)
                    
                    if opp_val is None:
                        setattr(item, "solicitud_suministro21", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def ordenes_Perdidos22(self):
        return self.__ordenes_Perdidos22
    @ordenes_Perdidos22.setter
    def ordenes_Perdidos22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Solicitud_suministro__ordenes_Perdidos22", None)
        self.__ordenes_Perdidos22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "solicitud_suministro23"):
                opp_val = getattr(old_value, "solicitud_suministro23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "solicitud_suministro23"):
                opp_val = getattr(value, "solicitud_suministro23", None)
                if opp_val is None:
                    setattr(value, "solicitud_suministro23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dependencia25(self):
        return self.__dependencia25
    @dependencia25.setter
    def dependencia25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Solicitud_suministro__dependencia25", None)
        self.__dependencia25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "solicitud_suministro24"):
                opp_val = getattr(old_value, "solicitud_suministro24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "solicitud_suministro24"):
                opp_val = getattr(value, "solicitud_suministro24", None)
                if opp_val is None:
                    setattr(value, "solicitud_suministro24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Ordenes_Perdidos:

    def __init__(self, Codigo: str, Fecha: str, proveedores15: "Proveedores" = None, elementos18: set["Elementos"] = None, solicitud_suministro23: set["Solicitud_suministro"] = None):
        self.Codigo = Codigo
        self.Fecha = Fecha
        self.proveedores15 = proveedores15
        self.elementos18 = elementos18 if elementos18 is not None else set()
        self.solicitud_suministro23 = solicitud_suministro23 if solicitud_suministro23 is not None else set()
        
        pass
    @property
    def Codigo(self):
        return self.__Codigo
    @Codigo.setter
    def Codigo(self, Codigo: str):
        self.__Codigo = Codigo

    @property
    def Fecha(self):
        return self.__Fecha
    @Fecha.setter
    def Fecha(self, Fecha: str):
        self.__Fecha = Fecha

    @property
    def solicitud_suministro23(self):
        return self.__solicitud_suministro23
    @solicitud_suministro23.setter
    def solicitud_suministro23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ordenes_Perdidos__solicitud_suministro23", None)
        self.__solicitud_suministro23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ordenes_Perdidos22"):
                    opp_val = getattr(item, "ordenes_Perdidos22", None)
                    
                    if opp_val == self:
                        setattr(item, "ordenes_Perdidos22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ordenes_Perdidos22"):
                    opp_val = getattr(item, "ordenes_Perdidos22", None)
                    
                    setattr(item, "ordenes_Perdidos22", self)
                    

    @property
    def elementos18(self):
        return self.__elementos18
    @elementos18.setter
    def elementos18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ordenes_Perdidos__elementos18", None)
        self.__elementos18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ordenes_Perdidos19"):
                    opp_val = getattr(item, "ordenes_Perdidos19", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ordenes_Perdidos19"):
                    opp_val = getattr(item, "ordenes_Perdidos19", None)
                    
                    if opp_val is None:
                        setattr(item, "ordenes_Perdidos19", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def proveedores15(self):
        return self.__proveedores15
    @proveedores15.setter
    def proveedores15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ordenes_Perdidos__proveedores15", None)
        self.__proveedores15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ordenes_Perdidos14"):
                opp_val = getattr(old_value, "ordenes_Perdidos14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ordenes_Perdidos14"):
                opp_val = getattr(value, "ordenes_Perdidos14", None)
                if opp_val is None:
                    setattr(value, "ordenes_Perdidos14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Sistema_Web_Movil___Receccion_de_pedidos_Component:

    pass


class Departamento_de_inventarios_y_Suminsitros_Component:

    pass


class Millenium_Component:

    pass
