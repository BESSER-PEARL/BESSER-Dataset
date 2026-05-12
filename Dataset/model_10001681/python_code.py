from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Enumeration(Enum):
    pass

############################################
# Definition of Classes
############################################







class Consultar_producto_UseCase:

    pass


class Ver_consultas_sin_responder_UseCase:

    pass


class Enviar_producto_UseCase:

    pass


class Publicar_producto_UseCase:

    pass


class Responder_consultas_UseCase:

    pass


class Comprador_Actor:

    pass


class Vendedor_Actor:

    pass


class Registrar_venta_UseCase:

    pass


class Vender_producto_UseCase:

    pass


class Listar_stock_UseCase:

    pass


class Registrar_cierre_de_caja_UseCase:

    pass


class Registrar_inicio_de_caja_UseCase:

    pass


class Registrar_datos_del_producto_UseCase:

    pass


class Supervisor_Actor:

    pass


class Consultar_inscripci_n_a_otra_clase_UseCase:

    pass


class Inscribir_a_una_clase_UseCase:

    pass


class Consultar_asistencia_historica_UseCase:

    pass


class Renovar_inscripci_n_UseCase:

    pass


class Registrar_datos_de_la_clase_a_la_que_asistir__el_cliente_UseCase:

    pass


class Registrar_datos_de_clientes_UseCase:

    pass


class Cliente_Actor:

    pass


class Instructor_Actor:

    pass


class Realizar_pedido_UseCase:

    pass


class Realizar_consulta_UseCase:

    pass





class Instructor:

    def __init__(self, Nombre: str, asistencia65: set["Asistencia"] = None):
        self.Nombre = Nombre
        self.asistencia65 = asistencia65 if asistencia65 is not None else set()
        
        pass
    @property
    def Nombre(self):
        return self.__Nombre
    @Nombre.setter
    def Nombre(self, Nombre: str):
        self.__Nombre = Nombre

    @property
    def asistencia65(self):
        return self.__asistencia65
    @asistencia65.setter
    def asistencia65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Instructor__asistencia65", None)
        self.__asistencia65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "instructor64"):
                    opp_val = getattr(item, "instructor64", None)
                    
                    if opp_val == self:
                        setattr(item, "instructor64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "instructor64"):
                    opp_val = getattr(item, "instructor64", None)
                    
                    setattr(item, "instructor64", self)
                    



class Clase:

    def __init__(self, Nombre: str, Asistencia: str, asistencia67: "Asistencia" = None):
        self.Nombre = Nombre
        self.Asistencia = Asistencia
        self.asistencia67 = asistencia67
        
        pass
    @property
    def Nombre(self):
        return self.__Nombre
    @Nombre.setter
    def Nombre(self, Nombre: str):
        self.__Nombre = Nombre

    @property
    def Asistencia(self):
        return self.__Asistencia
    @Asistencia.setter
    def Asistencia(self, Asistencia: str):
        self.__Asistencia = Asistencia

    @property
    def asistencia67(self):
        return self.__asistencia67
    @asistencia67.setter
    def asistencia67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Clase__asistencia67", None)
        self.__asistencia67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "clase66"):
                opp_val = getattr(old_value, "clase66", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "clase66"):
                opp_val = getattr(value, "clase66", None)
                if opp_val is None:
                    setattr(value, "clase66", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Asistencia:

    def __init__(self, Ingreso: str, Sucursal: str, cliente63: set["Cliente1"] = None, instructor64: "Instructor" = None, clase66: set["Clase"] = None):
        self.Ingreso = Ingreso
        self.Sucursal = Sucursal
        self.cliente63 = cliente63 if cliente63 is not None else set()
        self.instructor64 = instructor64
        self.clase66 = clase66 if clase66 is not None else set()
        
        pass
    @property
    def Sucursal(self):
        return self.__Sucursal
    @Sucursal.setter
    def Sucursal(self, Sucursal: str):
        self.__Sucursal = Sucursal

    @property
    def Ingreso(self):
        return self.__Ingreso
    @Ingreso.setter
    def Ingreso(self, Ingreso: str):
        self.__Ingreso = Ingreso

    @property
    def cliente63(self):
        return self.__cliente63
    @cliente63.setter
    def cliente63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Asistencia__cliente63", None)
        self.__cliente63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "asistencia62"):
                    opp_val = getattr(item, "asistencia62", None)
                    
                    if opp_val == self:
                        setattr(item, "asistencia62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "asistencia62"):
                    opp_val = getattr(item, "asistencia62", None)
                    
                    setattr(item, "asistencia62", self)
                    

    @property
    def instructor64(self):
        return self.__instructor64
    @instructor64.setter
    def instructor64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Asistencia__instructor64", None)
        self.__instructor64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "asistencia65"):
                opp_val = getattr(old_value, "asistencia65", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "asistencia65"):
                opp_val = getattr(value, "asistencia65", None)
                if opp_val is None:
                    setattr(value, "asistencia65", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def clase66(self):
        return self.__clase66
    @clase66.setter
    def clase66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Asistencia__clase66", None)
        self.__clase66 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "asistencia67"):
                    opp_val = getattr(item, "asistencia67", None)
                    
                    if opp_val == self:
                        setattr(item, "asistencia67", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "asistencia67"):
                    opp_val = getattr(item, "asistencia67", None)
                    
                    setattr(item, "asistencia67", self)
                    



class Cliente1:

    def __init__(self, Apellido: str, DNI: str, Fecha_de_Nac: str, Telefono: str, Email: str, Nombre: str, asistencia62: "Asistencia" = None):
        self.Apellido = Apellido
        self.DNI = DNI
        self.Fecha_de_Nac = Fecha_de_Nac
        self.Telefono = Telefono
        self.Email = Email
        self.Nombre = Nombre
        self.asistencia62 = asistencia62
        
        pass
    @property
    def Nombre(self):
        return self.__Nombre
    @Nombre.setter
    def Nombre(self, Nombre: str):
        self.__Nombre = Nombre

    @property
    def Fecha_de_Nac(self):
        return self.__Fecha_de_Nac
    @Fecha_de_Nac.setter
    def Fecha_de_Nac(self, Fecha_de_Nac: str):
        self.__Fecha_de_Nac = Fecha_de_Nac

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def Telefono(self):
        return self.__Telefono
    @Telefono.setter
    def Telefono(self, Telefono: str):
        self.__Telefono = Telefono

    @property
    def DNI(self):
        return self.__DNI
    @DNI.setter
    def DNI(self, DNI: str):
        self.__DNI = DNI

    @property
    def Apellido(self):
        return self.__Apellido
    @Apellido.setter
    def Apellido(self, Apellido: str):
        self.__Apellido = Apellido

    @property
    def asistencia62(self):
        return self.__asistencia62
    @asistencia62.setter
    def asistencia62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cliente1__asistencia62", None)
        self.__asistencia62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cliente63"):
                opp_val = getattr(old_value, "cliente63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cliente63"):
                opp_val = getattr(value, "cliente63", None)
                if opp_val is None:
                    setattr(value, "cliente63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class usario:

    def __init__(self, nombre: str):
        self.nombre = nombre
        
        pass
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre



class Caja:

    def __init__(self, Dinero_Inicio: real, Arqueo: Real, Fecha: str, supervisor53: "Supervisor" = None, ventas55: set["Ventas"] = None, jornada59: set["Jornada"] = None):
        self.Dinero_Inicio = Dinero_Inicio
        self.Arqueo = Arqueo
        self.Fecha = Fecha
        self.supervisor53 = supervisor53
        self.ventas55 = ventas55 if ventas55 is not None else set()
        self.jornada59 = jornada59 if jornada59 is not None else set()
        
        pass
    @property
    def Arqueo(self):
        return self.__Arqueo
    @Arqueo.setter
    def Arqueo(self, Arqueo: Real):
        self.__Arqueo = Arqueo

    @property
    def Dinero_Inicio(self):
        return self.__Dinero_Inicio
    @Dinero_Inicio.setter
    def Dinero_Inicio(self, Dinero_Inicio: real):
        self.__Dinero_Inicio = Dinero_Inicio

    @property
    def Fecha(self):
        return self.__Fecha
    @Fecha.setter
    def Fecha(self, Fecha: str):
        self.__Fecha = Fecha

    @property
    def supervisor53(self):
        return self.__supervisor53
    @supervisor53.setter
    def supervisor53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Caja__supervisor53", None)
        self.__supervisor53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caja52"):
                opp_val = getattr(old_value, "caja52", None)
                if opp_val == self:
                    setattr(old_value, "caja52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caja52"):
                opp_val = getattr(value, "caja52", None)
                setattr(value, "caja52", self)

    @property
    def ventas55(self):
        return self.__ventas55
    @ventas55.setter
    def ventas55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Caja__ventas55", None)
        self.__ventas55 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "caja54"):
                    opp_val = getattr(item, "caja54", None)
                    
                    if opp_val == self:
                        setattr(item, "caja54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "caja54"):
                    opp_val = getattr(item, "caja54", None)
                    
                    setattr(item, "caja54", self)
                    

    @property
    def jornada59(self):
        return self.__jornada59
    @jornada59.setter
    def jornada59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Caja__jornada59", None)
        self.__jornada59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "caja58"):
                    opp_val = getattr(item, "caja58", None)
                    
                    if opp_val == self:
                        setattr(item, "caja58", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "caja58"):
                    opp_val = getattr(item, "caja58", None)
                    
                    setattr(item, "caja58", self)
                    



class Jornada:

    def __init__(self, Stock: str, Dinero_en_caja: real, Arqueo: real, producto49: set["Producto"] = None, supervisor50: "Supervisor" = None, caja58: "Caja" = None):
        self.Stock = Stock
        self.Dinero_en_caja = Dinero_en_caja
        self.Arqueo = Arqueo
        self.producto49 = producto49 if producto49 is not None else set()
        self.supervisor50 = supervisor50
        self.caja58 = caja58
        
        pass
    @property
    def Arqueo(self):
        return self.__Arqueo
    @Arqueo.setter
    def Arqueo(self, Arqueo: real):
        self.__Arqueo = Arqueo

    @property
    def Stock(self):
        return self.__Stock
    @Stock.setter
    def Stock(self, Stock: str):
        self.__Stock = Stock

    @property
    def Dinero_en_caja(self):
        return self.__Dinero_en_caja
    @Dinero_en_caja.setter
    def Dinero_en_caja(self, Dinero_en_caja: real):
        self.__Dinero_en_caja = Dinero_en_caja

    @property
    def caja58(self):
        return self.__caja58
    @caja58.setter
    def caja58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Jornada__caja58", None)
        self.__caja58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jornada59"):
                opp_val = getattr(old_value, "jornada59", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jornada59"):
                opp_val = getattr(value, "jornada59", None)
                if opp_val is None:
                    setattr(value, "jornada59", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def supervisor50(self):
        return self.__supervisor50
    @supervisor50.setter
    def supervisor50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Jornada__supervisor50", None)
        self.__supervisor50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jornada51"):
                opp_val = getattr(old_value, "jornada51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jornada51"):
                opp_val = getattr(value, "jornada51", None)
                if opp_val is None:
                    setattr(value, "jornada51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def producto49(self):
        return self.__producto49
    @producto49.setter
    def producto49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Jornada__producto49", None)
        self.__producto49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jornada48"):
                    opp_val = getattr(item, "jornada48", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jornada48"):
                    opp_val = getattr(item, "jornada48", None)
                    
                    if opp_val is None:
                        setattr(item, "jornada48", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Ventas:

    def __init__(self, Cantidad: str, Producto: str, Monto: real, Fecha: str, caja54: "Caja" = None, producto57: set["Producto"] = None):
        self.Cantidad = Cantidad
        self.Producto = Producto
        self.Monto = Monto
        self.Fecha = Fecha
        self.caja54 = caja54
        self.producto57 = producto57 if producto57 is not None else set()
        
        pass
    @property
    def Fecha(self):
        return self.__Fecha
    @Fecha.setter
    def Fecha(self, Fecha: str):
        self.__Fecha = Fecha

    @property
    def Cantidad(self):
        return self.__Cantidad
    @Cantidad.setter
    def Cantidad(self, Cantidad: str):
        self.__Cantidad = Cantidad

    @property
    def Producto(self):
        return self.__Producto
    @Producto.setter
    def Producto(self, Producto: str):
        self.__Producto = Producto

    @property
    def Monto(self):
        return self.__Monto
    @Monto.setter
    def Monto(self, Monto: real):
        self.__Monto = Monto

    @property
    def producto57(self):
        return self.__producto57
    @producto57.setter
    def producto57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ventas__producto57", None)
        self.__producto57 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ventas56"):
                    opp_val = getattr(item, "ventas56", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ventas56"):
                    opp_val = getattr(item, "ventas56", None)
                    
                    if opp_val is None:
                        setattr(item, "ventas56", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def caja54(self):
        return self.__caja54
    @caja54.setter
    def caja54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ventas__caja54", None)
        self.__caja54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ventas55"):
                opp_val = getattr(old_value, "ventas55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ventas55"):
                opp_val = getattr(value, "ventas55", None)
                if opp_val is None:
                    setattr(value, "ventas55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Supervisor:

    def __init__(self, Clave: str, jornada51: set["Jornada"] = None, caja52: "Caja" = None):
        self.Clave = Clave
        self.jornada51 = jornada51 if jornada51 is not None else set()
        self.caja52 = caja52
        
        pass
    @property
    def Clave(self):
        return self.__Clave
    @Clave.setter
    def Clave(self, Clave: str):
        self.__Clave = Clave

    @property
    def jornada51(self):
        return self.__jornada51
    @jornada51.setter
    def jornada51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Supervisor__jornada51", None)
        self.__jornada51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "supervisor50"):
                    opp_val = getattr(item, "supervisor50", None)
                    
                    if opp_val == self:
                        setattr(item, "supervisor50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "supervisor50"):
                    opp_val = getattr(item, "supervisor50", None)
                    
                    setattr(item, "supervisor50", self)
                    

    @property
    def caja52(self):
        return self.__caja52
    @caja52.setter
    def caja52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Supervisor__caja52", None)
        self.__caja52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "supervisor53"):
                opp_val = getattr(old_value, "supervisor53", None)
                if opp_val == self:
                    setattr(old_value, "supervisor53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "supervisor53"):
                opp_val = getattr(value, "supervisor53", None)
                setattr(value, "supervisor53", self)



class Producto:

    def __init__(self, Stock: str, Precio: real, Modo_de_venta: str, jornada48: set["Jornada"] = None, ventas56: set["Ventas"] = None):
        self.Stock = Stock
        self.Precio = Precio
        self.Modo_de_venta = Modo_de_venta
        self.jornada48 = jornada48 if jornada48 is not None else set()
        self.ventas56 = ventas56 if ventas56 is not None else set()
        
        pass
    @property
    def Modo_de_venta(self):
        return self.__Modo_de_venta
    @Modo_de_venta.setter
    def Modo_de_venta(self, Modo_de_venta: str):
        self.__Modo_de_venta = Modo_de_venta

    @property
    def Precio(self):
        return self.__Precio
    @Precio.setter
    def Precio(self, Precio: real):
        self.__Precio = Precio

    @property
    def Stock(self):
        return self.__Stock
    @Stock.setter
    def Stock(self, Stock: str):
        self.__Stock = Stock

    @property
    def jornada48(self):
        return self.__jornada48
    @jornada48.setter
    def jornada48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Producto__jornada48", None)
        self.__jornada48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "producto49"):
                    opp_val = getattr(item, "producto49", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "producto49"):
                    opp_val = getattr(item, "producto49", None)
                    
                    if opp_val is None:
                        setattr(item, "producto49", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def ventas56(self):
        return self.__ventas56
    @ventas56.setter
    def ventas56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Producto__ventas56", None)
        self.__ventas56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "producto57"):
                    opp_val = getattr(item, "producto57", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "producto57"):
                    opp_val = getattr(item, "producto57", None)
                    
                    if opp_val is None:
                        setattr(item, "producto57", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Detalle:

    def __init__(self, Cantidad: str, Precio: real, Producto: str, pedido43: "Pedido" = None):
        self.Cantidad = Cantidad
        self.Precio = Precio
        self.Producto = Producto
        self.pedido43 = pedido43
        
        pass
    @property
    def Producto(self):
        return self.__Producto
    @Producto.setter
    def Producto(self, Producto: str):
        self.__Producto = Producto

    @property
    def Cantidad(self):
        return self.__Cantidad
    @Cantidad.setter
    def Cantidad(self, Cantidad: str):
        self.__Cantidad = Cantidad

    @property
    def Precio(self):
        return self.__Precio
    @Precio.setter
    def Precio(self, Precio: real):
        self.__Precio = Precio

    @property
    def pedido43(self):
        return self.__pedido43
    @pedido43.setter
    def pedido43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Detalle__pedido43", None)
        self.__pedido43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "detalle42"):
                opp_val = getattr(old_value, "detalle42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "detalle42"):
                opp_val = getattr(value, "detalle42", None)
                if opp_val is None:
                    setattr(value, "detalle42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Envio:

    def __init__(self, Fecha: str, Codigo: str, cliente41: "Cliente" = None, pedido47: "Pedido" = None, articulo61: set["Articulo2"] = None, cliente33: "Cliente" = None):
        self.Fecha = Fecha
        self.Codigo = Codigo
        self.cliente41 = cliente41
        self.pedido47 = pedido47
        self.articulo61 = articulo61 if articulo61 is not None else set()
        self.cliente33 = cliente33
        
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
    def pedido47(self):
        return self.__pedido47
    @pedido47.setter
    def pedido47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Envio__pedido47", None)
        self.__pedido47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "envio46"):
                opp_val = getattr(old_value, "envio46", None)
                if opp_val == self:
                    setattr(old_value, "envio46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "envio46"):
                opp_val = getattr(value, "envio46", None)
                setattr(value, "envio46", self)

    @property
    def articulo61(self):
        return self.__articulo61
    @articulo61.setter
    def articulo61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Envio__articulo61", None)
        self.__articulo61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "envio60"):
                    opp_val = getattr(item, "envio60", None)
                    
                    if opp_val == self:
                        setattr(item, "envio60", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "envio60"):
                    opp_val = getattr(item, "envio60", None)
                    
                    setattr(item, "envio60", self)
                    

    @property
    def cliente41(self):
        return self.__cliente41
    @cliente41.setter
    def cliente41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Envio__cliente41", None)
        self.__cliente41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "envio40"):
                opp_val = getattr(old_value, "envio40", None)
                if opp_val == self:
                    setattr(old_value, "envio40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "envio40"):
                opp_val = getattr(value, "envio40", None)
                setattr(value, "envio40", self)

    @property
    def cliente33(self):
        return self.__cliente33
    @cliente33.setter
    def cliente33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Envio__cliente33", None)
        self.__cliente33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "envio32"):
                opp_val = getattr(old_value, "envio32", None)
                if opp_val == self:
                    setattr(old_value, "envio32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "envio32"):
                opp_val = getattr(value, "envio32", None)
                setattr(value, "envio32", self)



class Consulta:

    def __init__(self, Fecha: str, Producto: str, cliente45: "Cliente" = None, articulo35: set["Articulo2"] = None):
        self.Fecha = Fecha
        self.Producto = Producto
        self.cliente45 = cliente45
        self.articulo35 = articulo35 if articulo35 is not None else set()
        
        pass
    @property
    def Producto(self):
        return self.__Producto
    @Producto.setter
    def Producto(self, Producto: str):
        self.__Producto = Producto

    @property
    def Fecha(self):
        return self.__Fecha
    @Fecha.setter
    def Fecha(self, Fecha: str):
        self.__Fecha = Fecha

    @property
    def cliente45(self):
        return self.__cliente45
    @cliente45.setter
    def cliente45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Consulta__cliente45", None)
        self.__cliente45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "consulta44"):
                opp_val = getattr(old_value, "consulta44", None)
                if opp_val == self:
                    setattr(old_value, "consulta44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "consulta44"):
                opp_val = getattr(value, "consulta44", None)
                setattr(value, "consulta44", self)

    @property
    def articulo35(self):
        return self.__articulo35
    @articulo35.setter
    def articulo35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Consulta__articulo35", None)
        self.__articulo35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "consulta34"):
                    opp_val = getattr(item, "consulta34", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "consulta34"):
                    opp_val = getattr(item, "consulta34", None)
                    
                    if opp_val is None:
                        setattr(item, "consulta34", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Pedido:

    def __init__(self, Numero: str, Fecha: str, detalle42: set["Detalle"] = None, envio46: "Envio" = None, cliente39: "Cliente" = None):
        self.Numero = Numero
        self.Fecha = Fecha
        self.detalle42 = detalle42 if detalle42 is not None else set()
        self.envio46 = envio46
        self.cliente39 = cliente39
        
        pass
    @property
    def Numero(self):
        return self.__Numero
    @Numero.setter
    def Numero(self, Numero: str):
        self.__Numero = Numero

    @property
    def Fecha(self):
        return self.__Fecha
    @Fecha.setter
    def Fecha(self, Fecha: str):
        self.__Fecha = Fecha

    @property
    def detalle42(self):
        return self.__detalle42
    @detalle42.setter
    def detalle42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pedido__detalle42", None)
        self.__detalle42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pedido43"):
                    opp_val = getattr(item, "pedido43", None)
                    
                    if opp_val == self:
                        setattr(item, "pedido43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pedido43"):
                    opp_val = getattr(item, "pedido43", None)
                    
                    setattr(item, "pedido43", self)
                    

    @property
    def cliente39(self):
        return self.__cliente39
    @cliente39.setter
    def cliente39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pedido__cliente39", None)
        self.__cliente39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pedido38"):
                opp_val = getattr(old_value, "pedido38", None)
                if opp_val == self:
                    setattr(old_value, "pedido38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pedido38"):
                opp_val = getattr(value, "pedido38", None)
                setattr(value, "pedido38", self)

    @property
    def envio46(self):
        return self.__envio46
    @envio46.setter
    def envio46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pedido__envio46", None)
        self.__envio46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pedido47"):
                opp_val = getattr(old_value, "pedido47", None)
                if opp_val == self:
                    setattr(old_value, "pedido47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pedido47"):
                opp_val = getattr(value, "pedido47", None)
                setattr(value, "pedido47", self)



class Cliente:

    def __init__(self, Nombre: str, Apellido: str, Direccion: str, Email: str, envio40: "Envio" = None, consulta44: "Consulta" = None, envio32: "Envio" = None, Articulo_Cliente_137: set["Articulo2"] = None, pedido38: "Pedido" = None):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Direccion = Direccion
        self.Email = Email
        self.envio40 = envio40
        self.consulta44 = consulta44
        self.envio32 = envio32
        self.Articulo_Cliente_137 = Articulo_Cliente_137 if Articulo_Cliente_137 is not None else set()
        self.pedido38 = pedido38
        
        pass
    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def Nombre(self):
        return self.__Nombre
    @Nombre.setter
    def Nombre(self, Nombre: str):
        self.__Nombre = Nombre

    @property
    def Apellido(self):
        return self.__Apellido
    @Apellido.setter
    def Apellido(self, Apellido: str):
        self.__Apellido = Apellido

    @property
    def Direccion(self):
        return self.__Direccion
    @Direccion.setter
    def Direccion(self, Direccion: str):
        self.__Direccion = Direccion

    @property
    def envio40(self):
        return self.__envio40
    @envio40.setter
    def envio40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cliente__envio40", None)
        self.__envio40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cliente41"):
                opp_val = getattr(old_value, "cliente41", None)
                if opp_val == self:
                    setattr(old_value, "cliente41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cliente41"):
                opp_val = getattr(value, "cliente41", None)
                setattr(value, "cliente41", self)

    @property
    def pedido38(self):
        return self.__pedido38
    @pedido38.setter
    def pedido38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cliente__pedido38", None)
        self.__pedido38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cliente39"):
                opp_val = getattr(old_value, "cliente39", None)
                if opp_val == self:
                    setattr(old_value, "cliente39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cliente39"):
                opp_val = getattr(value, "cliente39", None)
                setattr(value, "cliente39", self)

    @property
    def consulta44(self):
        return self.__consulta44
    @consulta44.setter
    def consulta44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cliente__consulta44", None)
        self.__consulta44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cliente45"):
                opp_val = getattr(old_value, "cliente45", None)
                if opp_val == self:
                    setattr(old_value, "cliente45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cliente45"):
                opp_val = getattr(value, "cliente45", None)
                setattr(value, "cliente45", self)

    @property
    def envio32(self):
        return self.__envio32
    @envio32.setter
    def envio32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cliente__envio32", None)
        self.__envio32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cliente33"):
                opp_val = getattr(old_value, "cliente33", None)
                if opp_val == self:
                    setattr(old_value, "cliente33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cliente33"):
                opp_val = getattr(value, "cliente33", None)
                setattr(value, "cliente33", self)

    @property
    def Articulo_Cliente_137(self):
        return self.__Articulo_Cliente_137
    @Articulo_Cliente_137.setter
    def Articulo_Cliente_137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cliente__Articulo_Cliente_137", None)
        self.__Articulo_Cliente_137 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Articulo_Cliente_036"):
                    opp_val = getattr(item, "Articulo_Cliente_036", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Articulo_Cliente_036"):
                    opp_val = getattr(item, "Articulo_Cliente_036", None)
                    
                    if opp_val is None:
                        setattr(item, "Articulo_Cliente_036", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class real:

    pass


class Real:

    pass


class Articulo2:

    def __init__(self, Nombre: str, Descripci_n: str, Precio: real, envio60: "Envio" = None, consulta34: set["Consulta"] = None, Articulo_Cliente_036: set["Cliente"] = None):
        self.Nombre = Nombre
        self.Descripci_n = Descripci_n
        self.Precio = Precio
        self.envio60 = envio60
        self.consulta34 = consulta34 if consulta34 is not None else set()
        self.Articulo_Cliente_036 = Articulo_Cliente_036 if Articulo_Cliente_036 is not None else set()
        
        pass
    @property
    def Nombre(self):
        return self.__Nombre
    @Nombre.setter
    def Nombre(self, Nombre: str):
        self.__Nombre = Nombre

    @property
    def Descripci_n(self):
        return self.__Descripci_n
    @Descripci_n.setter
    def Descripci_n(self, Descripci_n: str):
        self.__Descripci_n = Descripci_n

    @property
    def Precio(self):
        return self.__Precio
    @Precio.setter
    def Precio(self, Precio: real):
        self.__Precio = Precio

    @property
    def envio60(self):
        return self.__envio60
    @envio60.setter
    def envio60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Articulo2__envio60", None)
        self.__envio60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "articulo61"):
                opp_val = getattr(old_value, "articulo61", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "articulo61"):
                opp_val = getattr(value, "articulo61", None)
                if opp_val is None:
                    setattr(value, "articulo61", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def consulta34(self):
        return self.__consulta34
    @consulta34.setter
    def consulta34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Articulo2__consulta34", None)
        self.__consulta34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "articulo35"):
                    opp_val = getattr(item, "articulo35", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "articulo35"):
                    opp_val = getattr(item, "articulo35", None)
                    
                    if opp_val is None:
                        setattr(item, "articulo35", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def Articulo_Cliente_036(self):
        return self.__Articulo_Cliente_036
    @Articulo_Cliente_036.setter
    def Articulo_Cliente_036(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Articulo2__Articulo_Cliente_036", None)
        self.__Articulo_Cliente_036 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Articulo_Cliente_137"):
                    opp_val = getattr(item, "Articulo_Cliente_137", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Articulo_Cliente_137"):
                    opp_val = getattr(item, "Articulo_Cliente_137", None)
                    
                    if opp_val is None:
                        setattr(item, "Articulo_Cliente_137", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class T:

    pass


class Articulo1:

    pass


class Articulo:

    def __init__(self, Nombre: str):
        self.Nombre = Nombre
        
        pass
    @property
    def Nombre(self):
        return self.__Nombre
    @Nombre.setter
    def Nombre(self, Nombre: str):
        self.__Nombre = Nombre



class Vendedor_Actor1:

    pass
