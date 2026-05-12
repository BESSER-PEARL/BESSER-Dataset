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







class consulta_ventas_UseCase:

    pass


class consulta_caja_UseCase:

    pass


class consulta_producto_UseCase:

    pass


class due_o_Actor:

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





class inscripcion:

    def __init__(self, pago: Real, fecha: str, Cliente_inscripcion_169: "Cliente1" = None):
        self.pago = pago
        self.fecha = fecha
        self.Cliente_inscripcion_169 = Cliente_inscripcion_169
        
        pass
    @property
    def pago(self):
        return self.__pago
    @pago.setter
    def pago(self, pago: Real):
        self.__pago = pago

    @property
    def fecha(self):
        return self.__fecha
    @fecha.setter
    def fecha(self, fecha: str):
        self.__fecha = fecha

    @property
    def Cliente_inscripcion_169(self):
        return self.__Cliente_inscripcion_169
    @Cliente_inscripcion_169.setter
    def Cliente_inscripcion_169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_inscripcion__Cliente_inscripcion_169", None)
        self.__Cliente_inscripcion_169 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Cliente_inscripcion_068"):
                opp_val = getattr(old_value, "Cliente_inscripcion_068", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Cliente_inscripcion_068"):
                opp_val = getattr(value, "Cliente_inscripcion_068", None)
                if opp_val is None:
                    setattr(value, "Cliente_inscripcion_068", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Instructor:

    def __init__(self, Nombre: str, asistencia63: set["Asistencia"] = None):
        self.Nombre = Nombre
        self.asistencia63 = asistencia63 if asistencia63 is not None else set()
        
        pass
    @property
    def Nombre(self):
        return self.__Nombre
    @Nombre.setter
    def Nombre(self, Nombre: str):
        self.__Nombre = Nombre

    @property
    def asistencia63(self):
        return self.__asistencia63
    @asistencia63.setter
    def asistencia63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Instructor__asistencia63", None)
        self.__asistencia63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "instructor62"):
                    opp_val = getattr(item, "instructor62", None)
                    
                    if opp_val == self:
                        setattr(item, "instructor62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "instructor62"):
                    opp_val = getattr(item, "instructor62", None)
                    
                    setattr(item, "instructor62", self)
                    



class Clase:

    def __init__(self, Nombre: str, Asistencia: str, asistencia65: set["Asistencia"] = None):
        self.Nombre = Nombre
        self.Asistencia = Asistencia
        self.asistencia65 = asistencia65 if asistencia65 is not None else set()
        
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
    def asistencia65(self):
        return self.__asistencia65
    @asistencia65.setter
    def asistencia65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Clase__asistencia65", None)
        self.__asistencia65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "clase64"):
                    opp_val = getattr(item, "clase64", None)
                    
                    if opp_val == self:
                        setattr(item, "clase64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "clase64"):
                    opp_val = getattr(item, "clase64", None)
                    
                    setattr(item, "clase64", self)
                    



class Asistencia:

    def __init__(self, Ingreso: str, Sucursal: str, cliente61: "Cliente1" = None, instructor62: "Instructor" = None, clase64: "Clase" = None):
        self.Ingreso = Ingreso
        self.Sucursal = Sucursal
        self.cliente61 = cliente61
        self.instructor62 = instructor62
        self.clase64 = clase64
        
        pass
    @property
    def Ingreso(self):
        return self.__Ingreso
    @Ingreso.setter
    def Ingreso(self, Ingreso: str):
        self.__Ingreso = Ingreso

    @property
    def Sucursal(self):
        return self.__Sucursal
    @Sucursal.setter
    def Sucursal(self, Sucursal: str):
        self.__Sucursal = Sucursal

    @property
    def instructor62(self):
        return self.__instructor62
    @instructor62.setter
    def instructor62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Asistencia__instructor62", None)
        self.__instructor62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "asistencia63"):
                opp_val = getattr(old_value, "asistencia63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "asistencia63"):
                opp_val = getattr(value, "asistencia63", None)
                if opp_val is None:
                    setattr(value, "asistencia63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cliente61(self):
        return self.__cliente61
    @cliente61.setter
    def cliente61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Asistencia__cliente61", None)
        self.__cliente61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "asistencia60"):
                opp_val = getattr(old_value, "asistencia60", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "asistencia60"):
                opp_val = getattr(value, "asistencia60", None)
                if opp_val is None:
                    setattr(value, "asistencia60", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def clase64(self):
        return self.__clase64
    @clase64.setter
    def clase64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Asistencia__clase64", None)
        self.__clase64 = value
        
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



class Cliente1:

    def __init__(self, Nombre: str, Apellido: str, DNI: str, Fecha_de_Nac: str, Telefono: str, Email: str, asistencia60: set["Asistencia"] = None, Cliente_inscripcion_068: set["inscripcion"] = None):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.DNI = DNI
        self.Fecha_de_Nac = Fecha_de_Nac
        self.Telefono = Telefono
        self.Email = Email
        self.asistencia60 = asistencia60 if asistencia60 is not None else set()
        self.Cliente_inscripcion_068 = Cliente_inscripcion_068 if Cliente_inscripcion_068 is not None else set()
        
        pass
    @property
    def Fecha_de_Nac(self):
        return self.__Fecha_de_Nac
    @Fecha_de_Nac.setter
    def Fecha_de_Nac(self, Fecha_de_Nac: str):
        self.__Fecha_de_Nac = Fecha_de_Nac

    @property
    def Nombre(self):
        return self.__Nombre
    @Nombre.setter
    def Nombre(self, Nombre: str):
        self.__Nombre = Nombre

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def DNI(self):
        return self.__DNI
    @DNI.setter
    def DNI(self, DNI: str):
        self.__DNI = DNI

    @property
    def Telefono(self):
        return self.__Telefono
    @Telefono.setter
    def Telefono(self, Telefono: str):
        self.__Telefono = Telefono

    @property
    def Apellido(self):
        return self.__Apellido
    @Apellido.setter
    def Apellido(self, Apellido: str):
        self.__Apellido = Apellido

    @property
    def asistencia60(self):
        return self.__asistencia60
    @asistencia60.setter
    def asistencia60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cliente1__asistencia60", None)
        self.__asistencia60 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cliente61"):
                    opp_val = getattr(item, "cliente61", None)
                    
                    if opp_val == self:
                        setattr(item, "cliente61", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cliente61"):
                    opp_val = getattr(item, "cliente61", None)
                    
                    setattr(item, "cliente61", self)
                    

    @property
    def Cliente_inscripcion_068(self):
        return self.__Cliente_inscripcion_068
    @Cliente_inscripcion_068.setter
    def Cliente_inscripcion_068(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cliente1__Cliente_inscripcion_068", None)
        self.__Cliente_inscripcion_068 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Cliente_inscripcion_169"):
                    opp_val = getattr(item, "Cliente_inscripcion_169", None)
                    
                    if opp_val == self:
                        setattr(item, "Cliente_inscripcion_169", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Cliente_inscripcion_169"):
                    opp_val = getattr(item, "Cliente_inscripcion_169", None)
                    
                    setattr(item, "Cliente_inscripcion_169", self)
                    



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

    def __init__(self, Dinero_Inicio: real, Arqueo: Real, Fecha: str, moto_final: Real, supervisor51: "Supervisor" = None, ventas53: set["Ventas"] = None, jornada57: set["Jornada"] = None):
        self.Dinero_Inicio = Dinero_Inicio
        self.Arqueo = Arqueo
        self.Fecha = Fecha
        self.moto_final = moto_final
        self.supervisor51 = supervisor51
        self.ventas53 = ventas53 if ventas53 is not None else set()
        self.jornada57 = jornada57 if jornada57 is not None else set()
        
        pass
    @property
    def Arqueo(self):
        return self.__Arqueo
    @Arqueo.setter
    def Arqueo(self, Arqueo: Real):
        self.__Arqueo = Arqueo

    @property
    def Fecha(self):
        return self.__Fecha
    @Fecha.setter
    def Fecha(self, Fecha: str):
        self.__Fecha = Fecha

    @property
    def Dinero_Inicio(self):
        return self.__Dinero_Inicio
    @Dinero_Inicio.setter
    def Dinero_Inicio(self, Dinero_Inicio: real):
        self.__Dinero_Inicio = Dinero_Inicio

    @property
    def moto_final(self):
        return self.__moto_final
    @moto_final.setter
    def moto_final(self, moto_final: Real):
        self.__moto_final = moto_final

    @property
    def jornada57(self):
        return self.__jornada57
    @jornada57.setter
    def jornada57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Caja__jornada57", None)
        self.__jornada57 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "caja56"):
                    opp_val = getattr(item, "caja56", None)
                    
                    if opp_val == self:
                        setattr(item, "caja56", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "caja56"):
                    opp_val = getattr(item, "caja56", None)
                    
                    setattr(item, "caja56", self)
                    

    @property
    def supervisor51(self):
        return self.__supervisor51
    @supervisor51.setter
    def supervisor51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Caja__supervisor51", None)
        self.__supervisor51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caja50"):
                opp_val = getattr(old_value, "caja50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caja50"):
                opp_val = getattr(value, "caja50", None)
                if opp_val is None:
                    setattr(value, "caja50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ventas53(self):
        return self.__ventas53
    @ventas53.setter
    def ventas53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Caja__ventas53", None)
        self.__ventas53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "caja52"):
                    opp_val = getattr(item, "caja52", None)
                    
                    if opp_val == self:
                        setattr(item, "caja52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "caja52"):
                    opp_val = getattr(item, "caja52", None)
                    
                    setattr(item, "caja52", self)
                    



class Jornada:

    def __init__(self, Stock: str, Dinero_en_caja: real, Arqueo: real, producto47: set["Producto"] = None, supervisor48: "Supervisor" = None, caja56: "Caja" = None):
        self.Stock = Stock
        self.Dinero_en_caja = Dinero_en_caja
        self.Arqueo = Arqueo
        self.producto47 = producto47 if producto47 is not None else set()
        self.supervisor48 = supervisor48
        self.caja56 = caja56
        
        pass
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
    def Arqueo(self):
        return self.__Arqueo
    @Arqueo.setter
    def Arqueo(self, Arqueo: real):
        self.__Arqueo = Arqueo

    @property
    def caja56(self):
        return self.__caja56
    @caja56.setter
    def caja56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Jornada__caja56", None)
        self.__caja56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jornada57"):
                opp_val = getattr(old_value, "jornada57", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jornada57"):
                opp_val = getattr(value, "jornada57", None)
                if opp_val is None:
                    setattr(value, "jornada57", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def supervisor48(self):
        return self.__supervisor48
    @supervisor48.setter
    def supervisor48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Jornada__supervisor48", None)
        self.__supervisor48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jornada49"):
                opp_val = getattr(old_value, "jornada49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jornada49"):
                opp_val = getattr(value, "jornada49", None)
                if opp_val is None:
                    setattr(value, "jornada49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def producto47(self):
        return self.__producto47
    @producto47.setter
    def producto47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Jornada__producto47", None)
        self.__producto47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jornada46"):
                    opp_val = getattr(item, "jornada46", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jornada46"):
                    opp_val = getattr(item, "jornada46", None)
                    
                    if opp_val is None:
                        setattr(item, "jornada46", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Ventas:

    def __init__(self, Cantidad: str, Producto: str, Monto: real, Fecha: str, caja52: "Caja" = None, producto55: "Producto" = None):
        self.Cantidad = Cantidad
        self.Producto = Producto
        self.Monto = Monto
        self.Fecha = Fecha
        self.caja52 = caja52
        self.producto55 = producto55
        
        pass
    @property
    def Fecha(self):
        return self.__Fecha
    @Fecha.setter
    def Fecha(self, Fecha: str):
        self.__Fecha = Fecha

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
    def Cantidad(self):
        return self.__Cantidad
    @Cantidad.setter
    def Cantidad(self, Cantidad: str):
        self.__Cantidad = Cantidad

    @property
    def caja52(self):
        return self.__caja52
    @caja52.setter
    def caja52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ventas__caja52", None)
        self.__caja52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ventas53"):
                opp_val = getattr(old_value, "ventas53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ventas53"):
                opp_val = getattr(value, "ventas53", None)
                if opp_val is None:
                    setattr(value, "ventas53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def producto55(self):
        return self.__producto55
    @producto55.setter
    def producto55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ventas__producto55", None)
        self.__producto55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ventas54"):
                opp_val = getattr(old_value, "ventas54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ventas54"):
                opp_val = getattr(value, "ventas54", None)
                if opp_val is None:
                    setattr(value, "ventas54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Supervisor:

    def __init__(self, Clave: str, jornada49: set["Jornada"] = None, caja50: set["Caja"] = None):
        self.Clave = Clave
        self.jornada49 = jornada49 if jornada49 is not None else set()
        self.caja50 = caja50 if caja50 is not None else set()
        
        pass
    @property
    def Clave(self):
        return self.__Clave
    @Clave.setter
    def Clave(self, Clave: str):
        self.__Clave = Clave

    @property
    def caja50(self):
        return self.__caja50
    @caja50.setter
    def caja50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Supervisor__caja50", None)
        self.__caja50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "supervisor51"):
                    opp_val = getattr(item, "supervisor51", None)
                    
                    if opp_val == self:
                        setattr(item, "supervisor51", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "supervisor51"):
                    opp_val = getattr(item, "supervisor51", None)
                    
                    setattr(item, "supervisor51", self)
                    

    @property
    def jornada49(self):
        return self.__jornada49
    @jornada49.setter
    def jornada49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Supervisor__jornada49", None)
        self.__jornada49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "supervisor48"):
                    opp_val = getattr(item, "supervisor48", None)
                    
                    if opp_val == self:
                        setattr(item, "supervisor48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "supervisor48"):
                    opp_val = getattr(item, "supervisor48", None)
                    
                    setattr(item, "supervisor48", self)
                    



class Producto:

    def __init__(self, Stock: str, Precio: real, Modo_de_venta: str, jornada46: set["Jornada"] = None, ventas54: set["Ventas"] = None):
        self.Stock = Stock
        self.Precio = Precio
        self.Modo_de_venta = Modo_de_venta
        self.jornada46 = jornada46 if jornada46 is not None else set()
        self.ventas54 = ventas54 if ventas54 is not None else set()
        
        pass
    @property
    def Modo_de_venta(self):
        return self.__Modo_de_venta
    @Modo_de_venta.setter
    def Modo_de_venta(self, Modo_de_venta: str):
        self.__Modo_de_venta = Modo_de_venta

    @property
    def Stock(self):
        return self.__Stock
    @Stock.setter
    def Stock(self, Stock: str):
        self.__Stock = Stock

    @property
    def Precio(self):
        return self.__Precio
    @Precio.setter
    def Precio(self, Precio: real):
        self.__Precio = Precio

    @property
    def ventas54(self):
        return self.__ventas54
    @ventas54.setter
    def ventas54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Producto__ventas54", None)
        self.__ventas54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "producto55"):
                    opp_val = getattr(item, "producto55", None)
                    
                    if opp_val == self:
                        setattr(item, "producto55", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "producto55"):
                    opp_val = getattr(item, "producto55", None)
                    
                    setattr(item, "producto55", self)
                    

    @property
    def jornada46(self):
        return self.__jornada46
    @jornada46.setter
    def jornada46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Producto__jornada46", None)
        self.__jornada46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "producto47"):
                    opp_val = getattr(item, "producto47", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "producto47"):
                    opp_val = getattr(item, "producto47", None)
                    
                    if opp_val is None:
                        setattr(item, "producto47", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Detalle:

    def __init__(self, Cantidad: str, Precio: real, Producto: str, pedido41: "Pedido" = None, articulo67: set["Articulo2"] = None):
        self.Cantidad = Cantidad
        self.Precio = Precio
        self.Producto = Producto
        self.pedido41 = pedido41
        self.articulo67 = articulo67 if articulo67 is not None else set()
        
        pass
    @property
    def Producto(self):
        return self.__Producto
    @Producto.setter
    def Producto(self, Producto: str):
        self.__Producto = Producto

    @property
    def Precio(self):
        return self.__Precio
    @Precio.setter
    def Precio(self, Precio: real):
        self.__Precio = Precio

    @property
    def Cantidad(self):
        return self.__Cantidad
    @Cantidad.setter
    def Cantidad(self, Cantidad: str):
        self.__Cantidad = Cantidad

    @property
    def articulo67(self):
        return self.__articulo67
    @articulo67.setter
    def articulo67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Detalle__articulo67", None)
        self.__articulo67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "detalle66"):
                    opp_val = getattr(item, "detalle66", None)
                    
                    if opp_val == self:
                        setattr(item, "detalle66", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "detalle66"):
                    opp_val = getattr(item, "detalle66", None)
                    
                    setattr(item, "detalle66", self)
                    

    @property
    def pedido41(self):
        return self.__pedido41
    @pedido41.setter
    def pedido41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Detalle__pedido41", None)
        self.__pedido41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "detalle40"):
                opp_val = getattr(old_value, "detalle40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "detalle40"):
                opp_val = getattr(value, "detalle40", None)
                if opp_val is None:
                    setattr(value, "detalle40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Envio:

    def __init__(self, Fecha: str, Codigo: str, cliente33: "Cliente" = None, pedido45: "Pedido" = None, articulo59: set["Articulo2"] = None):
        self.Fecha = Fecha
        self.Codigo = Codigo
        self.cliente33 = cliente33
        self.pedido45 = pedido45
        self.articulo59 = articulo59 if articulo59 is not None else set()
        
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

    @property
    def articulo59(self):
        return self.__articulo59
    @articulo59.setter
    def articulo59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Envio__articulo59", None)
        self.__articulo59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "envio58"):
                    opp_val = getattr(item, "envio58", None)
                    
                    if opp_val == self:
                        setattr(item, "envio58", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "envio58"):
                    opp_val = getattr(item, "envio58", None)
                    
                    setattr(item, "envio58", self)
                    

    @property
    def pedido45(self):
        return self.__pedido45
    @pedido45.setter
    def pedido45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Envio__pedido45", None)
        self.__pedido45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "envio44"):
                opp_val = getattr(old_value, "envio44", None)
                if opp_val == self:
                    setattr(old_value, "envio44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "envio44"):
                opp_val = getattr(value, "envio44", None)
                setattr(value, "envio44", self)



class Consulta:

    def __init__(self, Fecha: str, Producto: str, articulo35: "Articulo2" = None, cliente43: "Cliente" = None):
        self.Fecha = Fecha
        self.Producto = Producto
        self.articulo35 = articulo35
        self.cliente43 = cliente43
        
        pass
    @property
    def Fecha(self):
        return self.__Fecha
    @Fecha.setter
    def Fecha(self, Fecha: str):
        self.__Fecha = Fecha

    @property
    def Producto(self):
        return self.__Producto
    @Producto.setter
    def Producto(self, Producto: str):
        self.__Producto = Producto

    @property
    def cliente43(self):
        return self.__cliente43
    @cliente43.setter
    def cliente43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Consulta__cliente43", None)
        self.__cliente43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "consulta42"):
                opp_val = getattr(old_value, "consulta42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "consulta42"):
                opp_val = getattr(value, "consulta42", None)
                if opp_val is None:
                    setattr(value, "consulta42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def articulo35(self):
        return self.__articulo35
    @articulo35.setter
    def articulo35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Consulta__articulo35", None)
        self.__articulo35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "consulta34"):
                opp_val = getattr(old_value, "consulta34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "consulta34"):
                opp_val = getattr(value, "consulta34", None)
                if opp_val is None:
                    setattr(value, "consulta34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Pedido:

    def __init__(self, Numero: str, Fecha: str, cliente39: "Cliente" = None, detalle40: set["Detalle"] = None, envio44: "Envio" = None):
        self.Numero = Numero
        self.Fecha = Fecha
        self.cliente39 = cliente39
        self.detalle40 = detalle40 if detalle40 is not None else set()
        self.envio44 = envio44
        
        pass
    @property
    def Fecha(self):
        return self.__Fecha
    @Fecha.setter
    def Fecha(self, Fecha: str):
        self.__Fecha = Fecha

    @property
    def Numero(self):
        return self.__Numero
    @Numero.setter
    def Numero(self, Numero: str):
        self.__Numero = Numero

    @property
    def detalle40(self):
        return self.__detalle40
    @detalle40.setter
    def detalle40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pedido__detalle40", None)
        self.__detalle40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pedido41"):
                    opp_val = getattr(item, "pedido41", None)
                    
                    if opp_val == self:
                        setattr(item, "pedido41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pedido41"):
                    opp_val = getattr(item, "pedido41", None)
                    
                    setattr(item, "pedido41", self)
                    

    @property
    def envio44(self):
        return self.__envio44
    @envio44.setter
    def envio44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pedido__envio44", None)
        self.__envio44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pedido45"):
                opp_val = getattr(old_value, "pedido45", None)
                if opp_val == self:
                    setattr(old_value, "pedido45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pedido45"):
                opp_val = getattr(value, "pedido45", None)
                setattr(value, "pedido45", self)

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
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pedido38"):
                opp_val = getattr(value, "pedido38", None)
                if opp_val is None:
                    setattr(value, "pedido38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Cliente:

    def __init__(self, Nombre: str, Apellido: str, Direccion: str, Email: str, envio32: "Envio" = None, Articulo_Cliente_137: set["Articulo2"] = None, pedido38: set["Pedido"] = None, consulta42: set["Consulta"] = None):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Direccion = Direccion
        self.Email = Email
        self.envio32 = envio32
        self.Articulo_Cliente_137 = Articulo_Cliente_137 if Articulo_Cliente_137 is not None else set()
        self.pedido38 = pedido38 if pedido38 is not None else set()
        self.consulta42 = consulta42 if consulta42 is not None else set()
        
        pass
    @property
    def Direccion(self):
        return self.__Direccion
    @Direccion.setter
    def Direccion(self, Direccion: str):
        self.__Direccion = Direccion

    @property
    def Apellido(self):
        return self.__Apellido
    @Apellido.setter
    def Apellido(self, Apellido: str):
        self.__Apellido = Apellido

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
    def consulta42(self):
        return self.__consulta42
    @consulta42.setter
    def consulta42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cliente__consulta42", None)
        self.__consulta42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cliente43"):
                    opp_val = getattr(item, "cliente43", None)
                    
                    if opp_val == self:
                        setattr(item, "cliente43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cliente43"):
                    opp_val = getattr(item, "cliente43", None)
                    
                    setattr(item, "cliente43", self)
                    

    @property
    def pedido38(self):
        return self.__pedido38
    @pedido38.setter
    def pedido38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cliente__pedido38", None)
        self.__pedido38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cliente39"):
                    opp_val = getattr(item, "cliente39", None)
                    
                    if opp_val == self:
                        setattr(item, "cliente39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cliente39"):
                    opp_val = getattr(item, "cliente39", None)
                    
                    setattr(item, "cliente39", self)
                    

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

    def __init__(self, Descripci_n: str, Precio: real, Nombre: str, consulta34: set["Consulta"] = None, Articulo_Cliente_036: set["Cliente"] = None, envio58: "Envio" = None, detalle66: "Detalle" = None):
        self.Descripci_n = Descripci_n
        self.Precio = Precio
        self.Nombre = Nombre
        self.consulta34 = consulta34 if consulta34 is not None else set()
        self.Articulo_Cliente_036 = Articulo_Cliente_036 if Articulo_Cliente_036 is not None else set()
        self.envio58 = envio58
        self.detalle66 = detalle66
        
        pass
    @property
    def Descripci_n(self):
        return self.__Descripci_n
    @Descripci_n.setter
    def Descripci_n(self, Descripci_n: str):
        self.__Descripci_n = Descripci_n

    @property
    def Nombre(self):
        return self.__Nombre
    @Nombre.setter
    def Nombre(self, Nombre: str):
        self.__Nombre = Nombre

    @property
    def Precio(self):
        return self.__Precio
    @Precio.setter
    def Precio(self, Precio: real):
        self.__Precio = Precio

    @property
    def envio58(self):
        return self.__envio58
    @envio58.setter
    def envio58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Articulo2__envio58", None)
        self.__envio58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "articulo59"):
                opp_val = getattr(old_value, "articulo59", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "articulo59"):
                opp_val = getattr(value, "articulo59", None)
                if opp_val is None:
                    setattr(value, "articulo59", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def detalle66(self):
        return self.__detalle66
    @detalle66.setter
    def detalle66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Articulo2__detalle66", None)
        self.__detalle66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "articulo67"):
                opp_val = getattr(old_value, "articulo67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "articulo67"):
                opp_val = getattr(value, "articulo67", None)
                if opp_val is None:
                    setattr(value, "articulo67", set([self]))
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
                    
                    if opp_val == self:
                        setattr(item, "articulo35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "articulo35"):
                    opp_val = getattr(item, "articulo35", None)
                    
                    setattr(item, "articulo35", self)
                    

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
