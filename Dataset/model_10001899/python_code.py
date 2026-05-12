from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Responsable_Inventario_Actor:

    pass


class Contabilidad_y_Tesoreria_Actor:

    pass


class Dependencia_Actor:

    pass


class Proveedores_Actor:

    pass


class Juridica_Actor:

    pass


class Natural_Actor:

    pass


class Cliente_Actor:

    pass





class Clasificar_Producto_external:

    pass


class Entregar_productos_external:

    pass


class ServidorWEB_Node:

    pass


class LogicaPresentacion_Factura_Component:

    pass


class Persistencia_Factura_Component:

    pass


class Servidor_intel_I8_Node:

    pass


class Elementos:

    def __init__(self, referencia: str, clasificacion: str, ordenes_Pedidos18: set["Ordenes_Pedidos"] = None, solicitud_Suministros21: set["Solicitud_Suministros"] = None, factura27: set["Factura"] = None):
        self.referencia = referencia
        self.clasificacion = clasificacion
        self.ordenes_Pedidos18 = ordenes_Pedidos18 if ordenes_Pedidos18 is not None else set()
        self.solicitud_Suministros21 = solicitud_Suministros21 if solicitud_Suministros21 is not None else set()
        self.factura27 = factura27 if factura27 is not None else set()
        
        pass
    @property
    def referencia(self):
        return self.__referencia
    @referencia.setter
    def referencia(self, referencia: str):
        self.__referencia = referencia

    @property
    def clasificacion(self):
        return self.__clasificacion
    @clasificacion.setter
    def clasificacion(self, clasificacion: str):
        self.__clasificacion = clasificacion

    @property
    def ordenes_Pedidos18(self):
        return self.__ordenes_Pedidos18
    @ordenes_Pedidos18.setter
    def ordenes_Pedidos18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elementos__ordenes_Pedidos18", None)
        self.__ordenes_Pedidos18 = value if value is not None else set()
        
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
    def factura27(self):
        return self.__factura27
    @factura27.setter
    def factura27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elementos__factura27", None)
        self.__factura27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "elementos26"):
                    opp_val = getattr(item, "elementos26", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "elementos26"):
                    opp_val = getattr(item, "elementos26", None)
                    
                    if opp_val is None:
                        setattr(item, "elementos26", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def solicitud_Suministros21(self):
        return self.__solicitud_Suministros21
    @solicitud_Suministros21.setter
    def solicitud_Suministros21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elementos__solicitud_Suministros21", None)
        self.__solicitud_Suministros21 = value if value is not None else set()
        
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
                    



class Pedidos:

    def __init__(self, codigo: str, fecha: str, proveedor16: "Proveedor" = None):
        self.codigo = codigo
        self.fecha = fecha
        self.proveedor16 = proveedor16
        
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
    def proveedor16(self):
        return self.__proveedor16
    @proveedor16.setter
    def proveedor16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pedidos__proveedor16", None)
        self.__proveedor16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pedidos17"):
                opp_val = getattr(old_value, "pedidos17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pedidos17"):
                opp_val = getattr(value, "pedidos17", None)
                if opp_val is None:
                    setattr(value, "pedidos17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Solicitud_Suministros:

    def __init__(self, codigo: str, fecha: str, elementos20: set["Elementos"] = None, ordenes_Pedidos23: "Ordenes_Pedidos" = None, dependencia24: "Dependencia" = None):
        self.codigo = codigo
        self.fecha = fecha
        self.elementos20 = elementos20 if elementos20 is not None else set()
        self.ordenes_Pedidos23 = ordenes_Pedidos23
        self.dependencia24 = dependencia24
        
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
    def dependencia24(self):
        return self.__dependencia24
    @dependencia24.setter
    def dependencia24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Solicitud_Suministros__dependencia24", None)
        self.__dependencia24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "solicitud_Suministros25"):
                opp_val = getattr(old_value, "solicitud_Suministros25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "solicitud_Suministros25"):
                opp_val = getattr(value, "solicitud_Suministros25", None)
                if opp_val is None:
                    setattr(value, "solicitud_Suministros25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def elementos20(self):
        return self.__elementos20
    @elementos20.setter
    def elementos20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Solicitud_Suministros__elementos20", None)
        self.__elementos20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "solicitud_Suministros21"):
                    opp_val = getattr(item, "solicitud_Suministros21", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "solicitud_Suministros21"):
                    opp_val = getattr(item, "solicitud_Suministros21", None)
                    
                    if opp_val is None:
                        setattr(item, "solicitud_Suministros21", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def ordenes_Pedidos23(self):
        return self.__ordenes_Pedidos23
    @ordenes_Pedidos23.setter
    def ordenes_Pedidos23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Solicitud_Suministros__ordenes_Pedidos23", None)
        self.__ordenes_Pedidos23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "solicitud_Suministros22"):
                opp_val = getattr(old_value, "solicitud_Suministros22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "solicitud_Suministros22"):
                opp_val = getattr(value, "solicitud_Suministros22", None)
                if opp_val is None:
                    setattr(value, "solicitud_Suministros22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Factura:

    def __init__(self, codigo: str, fecha: str, elementos26: set["Elementos"] = None, proveedor28: "Proveedor" = None):
        self.codigo = codigo
        self.fecha = fecha
        self.elementos26 = elementos26 if elementos26 is not None else set()
        self.proveedor28 = proveedor28
        
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
    def elementos26(self):
        return self.__elementos26
    @elementos26.setter
    def elementos26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Factura__elementos26", None)
        self.__elementos26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "factura27"):
                    opp_val = getattr(item, "factura27", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "factura27"):
                    opp_val = getattr(item, "factura27", None)
                    
                    if opp_val is None:
                        setattr(item, "factura27", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def proveedor28(self):
        return self.__proveedor28
    @proveedor28.setter
    def proveedor28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Factura__proveedor28", None)
        self.__proveedor28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "factura29"):
                opp_val = getattr(old_value, "factura29", None)
                if opp_val == self:
                    setattr(old_value, "factura29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "factura29"):
                opp_val = getattr(value, "factura29", None)
                setattr(value, "factura29", self)



class Dependencia:

    def __init__(self, codigo: str, nombre: str, responsable: str, solicitud_Suministros25: set["Solicitud_Suministros"] = None):
        self.codigo = codigo
        self.nombre = nombre
        self.responsable = responsable
        self.solicitud_Suministros25 = solicitud_Suministros25 if solicitud_Suministros25 is not None else set()
        
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
    def responsable(self):
        return self.__responsable
    @responsable.setter
    def responsable(self, responsable: str):
        self.__responsable = responsable

    @property
    def solicitud_Suministros25(self):
        return self.__solicitud_Suministros25
    @solicitud_Suministros25.setter
    def solicitud_Suministros25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dependencia__solicitud_Suministros25", None)
        self.__solicitud_Suministros25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dependencia24"):
                    opp_val = getattr(item, "dependencia24", None)
                    
                    if opp_val == self:
                        setattr(item, "dependencia24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dependencia24"):
                    opp_val = getattr(item, "dependencia24", None)
                    
                    setattr(item, "dependencia24", self)
                    



class Proveedor:

    def __init__(self, nit: str, razonSocial: str, direccion: str, telefonos: str, ordenes_Pedidos14: set["Ordenes_Pedidos"] = None, pedidos17: set["Pedidos"] = None, factura29: "Factura" = None):
        self.nit = nit
        self.razonSocial = razonSocial
        self.direccion = direccion
        self.telefonos = telefonos
        self.ordenes_Pedidos14 = ordenes_Pedidos14 if ordenes_Pedidos14 is not None else set()
        self.pedidos17 = pedidos17 if pedidos17 is not None else set()
        self.factura29 = factura29
        
        pass
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
    def telefonos(self, telefonos: str):
        self.__telefonos = telefonos

    @property
    def direccion(self):
        return self.__direccion
    @direccion.setter
    def direccion(self, direccion: str):
        self.__direccion = direccion

    @property
    def nit(self):
        return self.__nit
    @nit.setter
    def nit(self, nit: str):
        self.__nit = nit

    @property
    def pedidos17(self):
        return self.__pedidos17
    @pedidos17.setter
    def pedidos17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Proveedor__pedidos17", None)
        self.__pedidos17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "proveedor16"):
                    opp_val = getattr(item, "proveedor16", None)
                    
                    if opp_val == self:
                        setattr(item, "proveedor16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "proveedor16"):
                    opp_val = getattr(item, "proveedor16", None)
                    
                    setattr(item, "proveedor16", self)
                    

    @property
    def factura29(self):
        return self.__factura29
    @factura29.setter
    def factura29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Proveedor__factura29", None)
        self.__factura29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "proveedor28"):
                opp_val = getattr(old_value, "proveedor28", None)
                if opp_val == self:
                    setattr(old_value, "proveedor28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "proveedor28"):
                opp_val = getattr(value, "proveedor28", None)
                setattr(value, "proveedor28", self)

    @property
    def ordenes_Pedidos14(self):
        return self.__ordenes_Pedidos14
    @ordenes_Pedidos14.setter
    def ordenes_Pedidos14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Proveedor__ordenes_Pedidos14", None)
        self.__ordenes_Pedidos14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "proveedor15"):
                    opp_val = getattr(item, "proveedor15", None)
                    
                    if opp_val == self:
                        setattr(item, "proveedor15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "proveedor15"):
                    opp_val = getattr(item, "proveedor15", None)
                    
                    setattr(item, "proveedor15", self)
                    



class Ordenes_Pedidos:

    def __init__(self, codigo: str, fecha: str, proveedor15: "Proveedor" = None, elementos19: set["Elementos"] = None, solicitud_Suministros22: set["Solicitud_Suministros"] = None):
        self.codigo = codigo
        self.fecha = fecha
        self.proveedor15 = proveedor15
        self.elementos19 = elementos19 if elementos19 is not None else set()
        self.solicitud_Suministros22 = solicitud_Suministros22 if solicitud_Suministros22 is not None else set()
        
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
    def elementos19(self):
        return self.__elementos19
    @elementos19.setter
    def elementos19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ordenes_Pedidos__elementos19", None)
        self.__elementos19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ordenes_Pedidos18"):
                    opp_val = getattr(item, "ordenes_Pedidos18", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ordenes_Pedidos18"):
                    opp_val = getattr(item, "ordenes_Pedidos18", None)
                    
                    if opp_val is None:
                        setattr(item, "ordenes_Pedidos18", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def proveedor15(self):
        return self.__proveedor15
    @proveedor15.setter
    def proveedor15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ordenes_Pedidos__proveedor15", None)
        self.__proveedor15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ordenes_Pedidos14"):
                opp_val = getattr(old_value, "ordenes_Pedidos14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ordenes_Pedidos14"):
                opp_val = getattr(value, "ordenes_Pedidos14", None)
                if opp_val is None:
                    setattr(value, "ordenes_Pedidos14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def solicitud_Suministros22(self):
        return self.__solicitud_Suministros22
    @solicitud_Suministros22.setter
    def solicitud_Suministros22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ordenes_Pedidos__solicitud_Suministros22", None)
        self.__solicitud_Suministros22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ordenes_Pedidos23"):
                    opp_val = getattr(item, "ordenes_Pedidos23", None)
                    
                    if opp_val == self:
                        setattr(item, "ordenes_Pedidos23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ordenes_Pedidos23"):
                    opp_val = getattr(item, "ordenes_Pedidos23", None)
                    
                    setattr(item, "ordenes_Pedidos23", self)
                    



class Sistema_WEB_Movil___Recepcion_de_Pedidos_Component:

    pass


class Departamento_de_Inventarios_y_Suministros_DIS_Component:

    pass


class Millenium_Component:

    pass


class Recibir_productos_o_pedidos_external:

    pass


class Registrar_proveedores_external:

    pass


class Recibir_ordenes_de_suministro_external:

    pass


class Brindar_consultoria_external:

    pass


class ServidorBSD_Node:

    pass
