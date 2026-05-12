from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Actor_Actor:

    pass


class Dependencia_Actor:

    pass


class Proveedores_Actor:

    pass


class Juridica_Actor:

    pass


class Natural_Actor:

    pass


class Departamento_de_contabilidad_y_tesoreria_Actor:

    pass





class Clasificar_Producto_external:

    pass


class Generar_ordenes_de_pedidos_external:

    pass


class Recibir_ordenes_de_suministro_external:

    pass


class Recibir_productos_y_pedidos_external:

    pass


class Registrar_proveedores_external:

    pass


class Servidor_intel_i8_Node:

    pass


class _reasConocimiento:

    pass


class Departamento:

    pass


class Profesores:

    pass


class Sistema_desplegable:

    def __init__(self, codigo: str):
        self.codigo = codigo
        
        pass
    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, codigo: str):
        self.__codigo = codigo



class Sistema_Electrico:

    def __init__(self, codigo: str):
        self.codigo = codigo
        
        pass
    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, codigo: str):
        self.__codigo = codigo



class PlanosTerreno:

    def __init__(self, Ublicacion: str):
        self.Ublicacion = Ublicacion
        
        pass
    @property
    def Ublicacion(self):
        return self.__Ublicacion
    @Ublicacion.setter
    def Ublicacion(self, Ublicacion: str):
        self.__Ublicacion = Ublicacion



class Ejecuci_n:

    def __init__(self, codigo: str):
        self.codigo = codigo
        
        pass
    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, codigo: str):
        self.__codigo = codigo



class Encargos:

    def __init__(self, codigo: str, detalles: str, comprador42: "Comprador" = None, obras45: set["Obras"] = None):
        self.codigo = codigo
        self.detalles = detalles
        self.comprador42 = comprador42
        self.obras45 = obras45 if obras45 is not None else set()
        
        pass
    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, codigo: str):
        self.__codigo = codigo

    @property
    def detalles(self):
        return self.__detalles
    @detalles.setter
    def detalles(self, detalles: str):
        self.__detalles = detalles

    @property
    def obras45(self):
        return self.__obras45
    @obras45.setter
    def obras45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Encargos__obras45", None)
        self.__obras45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "encargos44"):
                    opp_val = getattr(item, "encargos44", None)
                    
                    if opp_val == self:
                        setattr(item, "encargos44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "encargos44"):
                    opp_val = getattr(item, "encargos44", None)
                    
                    setattr(item, "encargos44", self)
                    

    @property
    def comprador42(self):
        return self.__comprador42
    @comprador42.setter
    def comprador42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Encargos__comprador42", None)
        self.__comprador42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "encargos43"):
                opp_val = getattr(old_value, "encargos43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "encargos43"):
                opp_val = getattr(value, "encargos43", None)
                if opp_val is None:
                    setattr(value, "encargos43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class facturas_pagos_:

    def __init__(self, codigo: str, total: str, pagoNomina: int, obras32: "Obras" = None, trabajadores40: set["Trabajadores"] = None):
        self.codigo = codigo
        self.total = total
        self.pagoNomina = pagoNomina
        self.obras32 = obras32
        self.trabajadores40 = trabajadores40 if trabajadores40 is not None else set()
        
        pass
    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, total: str):
        self.__total = total

    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, codigo: str):
        self.__codigo = codigo

    @property
    def pagoNomina(self):
        return self.__pagoNomina
    @pagoNomina.setter
    def pagoNomina(self, pagoNomina: int):
        self.__pagoNomina = pagoNomina

    @property
    def obras32(self):
        return self.__obras32
    @obras32.setter
    def obras32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_facturas_pagos___obras32", None)
        self.__obras32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "factura33"):
                opp_val = getattr(old_value, "factura33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "factura33"):
                opp_val = getattr(value, "factura33", None)
                if opp_val is None:
                    setattr(value, "factura33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def trabajadores40(self):
        return self.__trabajadores40
    @trabajadores40.setter
    def trabajadores40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_facturas_pagos___trabajadores40", None)
        self.__trabajadores40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "factura41"):
                    opp_val = getattr(item, "factura41", None)
                    
                    if opp_val == self:
                        setattr(item, "factura41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "factura41"):
                    opp_val = getattr(item, "factura41", None)
                    
                    setattr(item, "factura41", self)
                    



class Comprador:

    def __init__(self, identificacion: str, Nombre: str, telefono: str, encargos43: set["Encargos"] = None):
        self.identificacion = identificacion
        self.Nombre = Nombre
        self.telefono = telefono
        self.encargos43 = encargos43 if encargos43 is not None else set()
        
        pass
    @property
    def telefono(self):
        return self.__telefono
    @telefono.setter
    def telefono(self, telefono: str):
        self.__telefono = telefono

    @property
    def identificacion(self):
        return self.__identificacion
    @identificacion.setter
    def identificacion(self, identificacion: str):
        self.__identificacion = identificacion

    @property
    def Nombre(self):
        return self.__Nombre
    @Nombre.setter
    def Nombre(self, Nombre: str):
        self.__Nombre = Nombre

    @property
    def encargos43(self):
        return self.__encargos43
    @encargos43.setter
    def encargos43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Comprador__encargos43", None)
        self.__encargos43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "comprador42"):
                    opp_val = getattr(item, "comprador42", None)
                    
                    if opp_val == self:
                        setattr(item, "comprador42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "comprador42"):
                    opp_val = getattr(item, "comprador42", None)
                    
                    setattr(item, "comprador42", self)
                    



class Historial_trabajadores:

    def __init__(self, codigo: str, TrabajoAntiguo: str, horasTrabajadas: str, trabajadores31: "Trabajadores" = None):
        self.codigo = codigo
        self.TrabajoAntiguo = TrabajoAntiguo
        self.horasTrabajadas = horasTrabajadas
        self.trabajadores31 = trabajadores31
        
        pass
    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, codigo: str):
        self.__codigo = codigo

    @property
    def horasTrabajadas(self):
        return self.__horasTrabajadas
    @horasTrabajadas.setter
    def horasTrabajadas(self, horasTrabajadas: str):
        self.__horasTrabajadas = horasTrabajadas

    @property
    def TrabajoAntiguo(self):
        return self.__TrabajoAntiguo
    @TrabajoAntiguo.setter
    def TrabajoAntiguo(self, TrabajoAntiguo: str):
        self.__TrabajoAntiguo = TrabajoAntiguo

    @property
    def trabajadores31(self):
        return self.__trabajadores31
    @trabajadores31.setter
    def trabajadores31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Historial_trabajadores__trabajadores31", None)
        self.__trabajadores31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "his_trabajores30"):
                opp_val = getattr(old_value, "his_trabajores30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "his_trabajores30"):
                opp_val = getattr(value, "his_trabajores30", None)
                if opp_val is None:
                    setattr(value, "his_trabajores30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Trabajadores:

    def __init__(self, identificacion: str, nombre: str, Telefono: int, his_trabajores30: set["Historial_trabajadores"] = None, obras36: "Obras" = None, factura41: "facturas_pagos_" = None):
        self.identificacion = identificacion
        self.nombre = nombre
        self.Telefono = Telefono
        self.his_trabajores30 = his_trabajores30 if his_trabajores30 is not None else set()
        self.obras36 = obras36
        self.factura41 = factura41
        
        pass
    @property
    def Telefono(self):
        return self.__Telefono
    @Telefono.setter
    def Telefono(self, Telefono: int):
        self.__Telefono = Telefono

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def identificacion(self):
        return self.__identificacion
    @identificacion.setter
    def identificacion(self, identificacion: str):
        self.__identificacion = identificacion

    @property
    def obras36(self):
        return self.__obras36
    @obras36.setter
    def obras36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Trabajadores__obras36", None)
        self.__obras36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trabajadores37"):
                opp_val = getattr(old_value, "trabajadores37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trabajadores37"):
                opp_val = getattr(value, "trabajadores37", None)
                if opp_val is None:
                    setattr(value, "trabajadores37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def his_trabajores30(self):
        return self.__his_trabajores30
    @his_trabajores30.setter
    def his_trabajores30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Trabajadores__his_trabajores30", None)
        self.__his_trabajores30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trabajadores31"):
                    opp_val = getattr(item, "trabajadores31", None)
                    
                    if opp_val == self:
                        setattr(item, "trabajadores31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trabajadores31"):
                    opp_val = getattr(item, "trabajadores31", None)
                    
                    setattr(item, "trabajadores31", self)
                    

    @property
    def factura41(self):
        return self.__factura41
    @factura41.setter
    def factura41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Trabajadores__factura41", None)
        self.__factura41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trabajadores40"):
                opp_val = getattr(old_value, "trabajadores40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trabajadores40"):
                opp_val = getattr(value, "trabajadores40", None)
                if opp_val is None:
                    setattr(value, "trabajadores40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Permisos:

    def __init__(self, Codigo: str, Estado: str, Fecha: str, planos38: "Planos" = None):
        self.Codigo = Codigo
        self.Estado = Estado
        self.Fecha = Fecha
        self.planos38 = planos38
        
        pass
    @property
    def Estado(self):
        return self.__Estado
    @Estado.setter
    def Estado(self, Estado: str):
        self.__Estado = Estado

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
    def planos38(self):
        return self.__planos38
    @planos38.setter
    def planos38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Permisos__planos38", None)
        self.__planos38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "permisos39"):
                opp_val = getattr(old_value, "permisos39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "permisos39"):
                opp_val = getattr(value, "permisos39", None)
                if opp_val is None:
                    setattr(value, "permisos39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Planos:

    def __init__(self, Codigo: str, Escala: str, Fecha: str, obras34: "Obras" = None, permisos39: set["Permisos"] = None):
        self.Codigo = Codigo
        self.Escala = Escala
        self.Fecha = Fecha
        self.obras34 = obras34
        self.permisos39 = permisos39 if permisos39 is not None else set()
        
        pass
    @property
    def Escala(self):
        return self.__Escala
    @Escala.setter
    def Escala(self, Escala: str):
        self.__Escala = Escala

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
    def obras34(self):
        return self.__obras34
    @obras34.setter
    def obras34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Planos__obras34", None)
        self.__obras34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "planos35"):
                opp_val = getattr(old_value, "planos35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "planos35"):
                opp_val = getattr(value, "planos35", None)
                if opp_val is None:
                    setattr(value, "planos35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def permisos39(self):
        return self.__permisos39
    @permisos39.setter
    def permisos39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Planos__permisos39", None)
        self.__permisos39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "planos38"):
                    opp_val = getattr(item, "planos38", None)
                    
                    if opp_val == self:
                        setattr(item, "planos38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "planos38"):
                    opp_val = getattr(item, "planos38", None)
                    
                    setattr(item, "planos38", self)
                    



class Obras:

    def __init__(self, codigo: str, direccion: str, encargos44: "Encargos" = None, factura33: set["facturas_pagos_"] = None, planos35: set["Planos"] = None, trabajadores37: set["Trabajadores"] = None):
        self.codigo = codigo
        self.direccion = direccion
        self.encargos44 = encargos44
        self.factura33 = factura33 if factura33 is not None else set()
        self.planos35 = planos35 if planos35 is not None else set()
        self.trabajadores37 = trabajadores37 if trabajadores37 is not None else set()
        
        pass
    @property
    def direccion(self):
        return self.__direccion
    @direccion.setter
    def direccion(self, direccion: str):
        self.__direccion = direccion

    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, codigo: str):
        self.__codigo = codigo

    @property
    def planos35(self):
        return self.__planos35
    @planos35.setter
    def planos35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Obras__planos35", None)
        self.__planos35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "obras34"):
                    opp_val = getattr(item, "obras34", None)
                    
                    if opp_val == self:
                        setattr(item, "obras34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "obras34"):
                    opp_val = getattr(item, "obras34", None)
                    
                    setattr(item, "obras34", self)
                    

    @property
    def factura33(self):
        return self.__factura33
    @factura33.setter
    def factura33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Obras__factura33", None)
        self.__factura33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "obras32"):
                    opp_val = getattr(item, "obras32", None)
                    
                    if opp_val == self:
                        setattr(item, "obras32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "obras32"):
                    opp_val = getattr(item, "obras32", None)
                    
                    setattr(item, "obras32", self)
                    

    @property
    def encargos44(self):
        return self.__encargos44
    @encargos44.setter
    def encargos44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Obras__encargos44", None)
        self.__encargos44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "obras45"):
                opp_val = getattr(old_value, "obras45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "obras45"):
                opp_val = getattr(value, "obras45", None)
                if opp_val is None:
                    setattr(value, "obras45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def trabajadores37(self):
        return self.__trabajadores37
    @trabajadores37.setter
    def trabajadores37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Obras__trabajadores37", None)
        self.__trabajadores37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "obras36"):
                    opp_val = getattr(item, "obras36", None)
                    
                    if opp_val == self:
                        setattr(item, "obras36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "obras36"):
                    opp_val = getattr(item, "obras36", None)
                    
                    setattr(item, "obras36", self)
                    



class Pedidos:

    def __init__(self, codigo: str, fecha: str, proveedores17: "Proveedores" = None):
        self.codigo = codigo
        self.fecha = fecha
        self.proveedores17 = proveedores17
        
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



class SolucitudSuministro:

    def __init__(self, codigo: str, fecha: str, elementos20: set["Elementos"] = None, ordenesPedido23: "OrdenesPedido" = None, dependencia27: "Dependencia" = None):
        self.codigo = codigo
        self.fecha = fecha
        self.elementos20 = elementos20 if elementos20 is not None else set()
        self.ordenesPedido23 = ordenesPedido23
        self.dependencia27 = dependencia27
        
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
    def dependencia27(self):
        return self.__dependencia27
    @dependencia27.setter
    def dependencia27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SolucitudSuministro__dependencia27", None)
        self.__dependencia27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "solucitudSuministro26"):
                opp_val = getattr(old_value, "solucitudSuministro26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "solucitudSuministro26"):
                opp_val = getattr(value, "solucitudSuministro26", None)
                if opp_val is None:
                    setattr(value, "solucitudSuministro26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ordenesPedido23(self):
        return self.__ordenesPedido23
    @ordenesPedido23.setter
    def ordenesPedido23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SolucitudSuministro__ordenesPedido23", None)
        self.__ordenesPedido23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "solucitudSuministro22"):
                opp_val = getattr(old_value, "solucitudSuministro22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "solucitudSuministro22"):
                opp_val = getattr(value, "solucitudSuministro22", None)
                if opp_val is None:
                    setattr(value, "solucitudSuministro22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def elementos20(self):
        return self.__elementos20
    @elementos20.setter
    def elementos20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SolucitudSuministro__elementos20", None)
        self.__elementos20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "solucitudSuministro21"):
                    opp_val = getattr(item, "solucitudSuministro21", None)
                    
                    if opp_val == self:
                        setattr(item, "solucitudSuministro21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "solucitudSuministro21"):
                    opp_val = getattr(item, "solucitudSuministro21", None)
                    
                    setattr(item, "solucitudSuministro21", self)
                    



class Factura:

    def __init__(self, codigo: str, fecha: str, proveedores25: "Proveedores" = None, elementos29: set["Elementos"] = None):
        self.codigo = codigo
        self.fecha = fecha
        self.proveedores25 = proveedores25
        self.elementos29 = elementos29 if elementos29 is not None else set()
        
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
    def elementos29(self):
        return self.__elementos29
    @elementos29.setter
    def elementos29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Factura__elementos29", None)
        self.__elementos29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "factura28"):
                    opp_val = getattr(item, "factura28", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "factura28"):
                    opp_val = getattr(item, "factura28", None)
                    
                    if opp_val is None:
                        setattr(item, "factura28", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def proveedores25(self):
        return self.__proveedores25
    @proveedores25.setter
    def proveedores25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Factura__proveedores25", None)
        self.__proveedores25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "factura24"):
                opp_val = getattr(old_value, "factura24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "factura24"):
                opp_val = getattr(value, "factura24", None)
                if opp_val is None:
                    setattr(value, "factura24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Dependencia:

    def __init__(self, codigo: str, nombre: str, responsable: str, solucitudSuministro26: set["SolucitudSuministro"] = None):
        self.codigo = codigo
        self.nombre = nombre
        self.responsable = responsable
        self.solucitudSuministro26 = solucitudSuministro26 if solucitudSuministro26 is not None else set()
        
        pass
    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, codigo: str):
        self.__codigo = codigo

    @property
    def responsable(self):
        return self.__responsable
    @responsable.setter
    def responsable(self, responsable: str):
        self.__responsable = responsable

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def solucitudSuministro26(self):
        return self.__solucitudSuministro26
    @solucitudSuministro26.setter
    def solucitudSuministro26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dependencia__solucitudSuministro26", None)
        self.__solucitudSuministro26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dependencia27"):
                    opp_val = getattr(item, "dependencia27", None)
                    
                    if opp_val == self:
                        setattr(item, "dependencia27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dependencia27"):
                    opp_val = getattr(item, "dependencia27", None)
                    
                    setattr(item, "dependencia27", self)
                    



class Proveedores:

    def __init__(self, nit: str, razonSocial: str, direccion: str, telefonos: int, ordenesPedido14: set["OrdenesPedido"] = None, pedidos16: set["Pedidos"] = None, factura24: set["Factura"] = None):
        self.nit = nit
        self.razonSocial = razonSocial
        self.direccion = direccion
        self.telefonos = telefonos
        self.ordenesPedido14 = ordenesPedido14 if ordenesPedido14 is not None else set()
        self.pedidos16 = pedidos16 if pedidos16 is not None else set()
        self.factura24 = factura24 if factura24 is not None else set()
        
        pass
    @property
    def direccion(self):
        return self.__direccion
    @direccion.setter
    def direccion(self, direccion: str):
        self.__direccion = direccion

    @property
    def razonSocial(self):
        return self.__razonSocial
    @razonSocial.setter
    def razonSocial(self, razonSocial: str):
        self.__razonSocial = razonSocial

    @property
    def telefonos(self):
        return self.__telefonos
    @telefonos.setter
    def telefonos(self, telefonos: int):
        self.__telefonos = telefonos

    @property
    def nit(self):
        return self.__nit
    @nit.setter
    def nit(self, nit: str):
        self.__nit = nit

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
                    

    @property
    def factura24(self):
        return self.__factura24
    @factura24.setter
    def factura24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Proveedores__factura24", None)
        self.__factura24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "proveedores25"):
                    opp_val = getattr(item, "proveedores25", None)
                    
                    if opp_val == self:
                        setattr(item, "proveedores25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "proveedores25"):
                    opp_val = getattr(item, "proveedores25", None)
                    
                    setattr(item, "proveedores25", self)
                    

    @property
    def ordenesPedido14(self):
        return self.__ordenesPedido14
    @ordenesPedido14.setter
    def ordenesPedido14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Proveedores__ordenesPedido14", None)
        self.__ordenesPedido14 = value if value is not None else set()
        
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
                    



class Elementos:

    def __init__(self, referencia: str, clasificacion: str, ordenesPedido18: set["OrdenesPedido"] = None, solucitudSuministro21: "SolucitudSuministro" = None, factura28: set["Factura"] = None):
        self.referencia = referencia
        self.clasificacion = clasificacion
        self.ordenesPedido18 = ordenesPedido18 if ordenesPedido18 is not None else set()
        self.solucitudSuministro21 = solucitudSuministro21
        self.factura28 = factura28 if factura28 is not None else set()
        
        pass
    @property
    def clasificacion(self):
        return self.__clasificacion
    @clasificacion.setter
    def clasificacion(self, clasificacion: str):
        self.__clasificacion = clasificacion

    @property
    def referencia(self):
        return self.__referencia
    @referencia.setter
    def referencia(self, referencia: str):
        self.__referencia = referencia

    @property
    def solucitudSuministro21(self):
        return self.__solucitudSuministro21
    @solucitudSuministro21.setter
    def solucitudSuministro21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elementos__solucitudSuministro21", None)
        self.__solucitudSuministro21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elementos20"):
                opp_val = getattr(old_value, "elementos20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elementos20"):
                opp_val = getattr(value, "elementos20", None)
                if opp_val is None:
                    setattr(value, "elementos20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ordenesPedido18(self):
        return self.__ordenesPedido18
    @ordenesPedido18.setter
    def ordenesPedido18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elementos__ordenesPedido18", None)
        self.__ordenesPedido18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "elementos19"):
                    opp_val = getattr(item, "elementos19", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "elementos19"):
                    opp_val = getattr(item, "elementos19", None)
                    
                    if opp_val is None:
                        setattr(item, "elementos19", set([self]))
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
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "elementos29"):
                    opp_val = getattr(item, "elementos29", None)
                    
                    if opp_val is None:
                        setattr(item, "elementos29", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class OrdenesPedido:

    def __init__(self, codigo: str, fecha: str, proveedores15: "Proveedores" = None, elementos19: set["Elementos"] = None, solucitudSuministro22: set["SolucitudSuministro"] = None):
        self.codigo = codigo
        self.fecha = fecha
        self.proveedores15 = proveedores15
        self.elementos19 = elementos19 if elementos19 is not None else set()
        self.solucitudSuministro22 = solucitudSuministro22 if solucitudSuministro22 is not None else set()
        
        pass
    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, codigo: str):
        self.__codigo = codigo

    @property
    def fecha(self):
        return self.__fecha
    @fecha.setter
    def fecha(self, fecha: str):
        self.__fecha = fecha

    @property
    def proveedores15(self):
        return self.__proveedores15
    @proveedores15.setter
    def proveedores15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrdenesPedido__proveedores15", None)
        self.__proveedores15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ordenesPedido14"):
                opp_val = getattr(old_value, "ordenesPedido14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ordenesPedido14"):
                opp_val = getattr(value, "ordenesPedido14", None)
                if opp_val is None:
                    setattr(value, "ordenesPedido14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def elementos19(self):
        return self.__elementos19
    @elementos19.setter
    def elementos19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrdenesPedido__elementos19", None)
        self.__elementos19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ordenesPedido18"):
                    opp_val = getattr(item, "ordenesPedido18", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ordenesPedido18"):
                    opp_val = getattr(item, "ordenesPedido18", None)
                    
                    if opp_val is None:
                        setattr(item, "ordenesPedido18", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def solucitudSuministro22(self):
        return self.__solucitudSuministro22
    @solucitudSuministro22.setter
    def solucitudSuministro22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrdenesPedido__solucitudSuministro22", None)
        self.__solucitudSuministro22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ordenesPedido23"):
                    opp_val = getattr(item, "ordenesPedido23", None)
                    
                    if opp_val == self:
                        setattr(item, "ordenesPedido23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ordenesPedido23"):
                    opp_val = getattr(item, "ordenesPedido23", None)
                    
                    setattr(item, "ordenesPedido23", self)
                    



class Sistema_WEB_Movil___Recceci_n_de_pedidos_Component:

    pass


class Departamento_de_Inventarios_y_Suministros___Dis_Component:

    pass


class Mileninum_Component:

    pass


class Brinda_consultoria_external:

    pass
