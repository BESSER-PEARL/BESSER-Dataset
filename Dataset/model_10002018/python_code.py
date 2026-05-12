from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Actor_Actor:

    pass


class Responsable_Inventario_Actor:

    pass


class Contabilidad_y_tesorer_a_Actor:

    pass


class Dependencias_Actor:

    pass


class Proveedores_Actor:

    pass


class Jur_dica_Actor:

    pass


class Natural_Actor:

    pass


class Cliente_Actor:

    pass





class Entregar_productos_external:

    pass


class Recibir_ordenes_de_suministros_external:

    pass


class Registrar_proveedores_external:

    pass


class Brindar_consultor_as_external:

    pass


class Pedidos:

    def __init__(self, codigo: str, fecha: str, proveedor18: "Proveedor" = None):
        self.codigo = codigo
        self.fecha = fecha
        self.proveedor18 = proveedor18
        
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
    def proveedor18(self):
        return self.__proveedor18
    @proveedor18.setter
    def proveedor18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pedidos__proveedor18", None)
        self.__proveedor18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pedidos19"):
                opp_val = getattr(old_value, "pedidos19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pedidos19"):
                opp_val = getattr(value, "pedidos19", None)
                if opp_val is None:
                    setattr(value, "pedidos19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class SolicitudSuministro:

    def __init__(self, codigo: str, fecha: str, ordenesPedidos22: "OrdenesPedidos" = None, elementos25: set["Elementos"] = None, dependencias27: "Dependencias" = None):
        self.codigo = codigo
        self.fecha = fecha
        self.ordenesPedidos22 = ordenesPedidos22
        self.elementos25 = elementos25 if elementos25 is not None else set()
        self.dependencias27 = dependencias27
        
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
    def elementos25(self):
        return self.__elementos25
    @elementos25.setter
    def elementos25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SolicitudSuministro__elementos25", None)
        self.__elementos25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "solicitudSuministro24"):
                    opp_val = getattr(item, "solicitudSuministro24", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "solicitudSuministro24"):
                    opp_val = getattr(item, "solicitudSuministro24", None)
                    
                    if opp_val is None:
                        setattr(item, "solicitudSuministro24", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def dependencias27(self):
        return self.__dependencias27
    @dependencias27.setter
    def dependencias27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SolicitudSuministro__dependencias27", None)
        self.__dependencias27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "solicitudSuministro26"):
                opp_val = getattr(old_value, "solicitudSuministro26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "solicitudSuministro26"):
                opp_val = getattr(value, "solicitudSuministro26", None)
                if opp_val is None:
                    setattr(value, "solicitudSuministro26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ordenesPedidos22(self):
        return self.__ordenesPedidos22
    @ordenesPedidos22.setter
    def ordenesPedidos22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SolicitudSuministro__ordenesPedidos22", None)
        self.__ordenesPedidos22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "solicitudSuministro23"):
                opp_val = getattr(old_value, "solicitudSuministro23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "solicitudSuministro23"):
                opp_val = getattr(value, "solicitudSuministro23", None)
                if opp_val is None:
                    setattr(value, "solicitudSuministro23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Factura:

    def __init__(self, codigo: str, fecha: str, proveedor28: "Proveedor" = None, elementos31: set["Elementos"] = None):
        self.codigo = codigo
        self.fecha = fecha
        self.proveedor28 = proveedor28
        self.elementos31 = elementos31 if elementos31 is not None else set()
        
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
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "factura29"):
                opp_val = getattr(value, "factura29", None)
                if opp_val is None:
                    setattr(value, "factura29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def elementos31(self):
        return self.__elementos31
    @elementos31.setter
    def elementos31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Factura__elementos31", None)
        self.__elementos31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "factura30"):
                    opp_val = getattr(item, "factura30", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "factura30"):
                    opp_val = getattr(item, "factura30", None)
                    
                    if opp_val is None:
                        setattr(item, "factura30", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Proveedor:

    def __init__(self, nit: str, razonSocial: str, direccion: str, telefonos: str, ordenesPedidos16: set["OrdenesPedidos"] = None, pedidos19: set["Pedidos"] = None, factura29: set["Factura"] = None):
        self.nit = nit
        self.razonSocial = razonSocial
        self.direccion = direccion
        self.telefonos = telefonos
        self.ordenesPedidos16 = ordenesPedidos16 if ordenesPedidos16 is not None else set()
        self.pedidos19 = pedidos19 if pedidos19 is not None else set()
        self.factura29 = factura29 if factura29 is not None else set()
        
        pass
    @property
    def telefonos(self):
        return self.__telefonos
    @telefonos.setter
    def telefonos(self, telefonos: str):
        self.__telefonos = telefonos

    @property
    def razonSocial(self):
        return self.__razonSocial
    @razonSocial.setter
    def razonSocial(self, razonSocial: str):
        self.__razonSocial = razonSocial

    @property
    def nit(self):
        return self.__nit
    @nit.setter
    def nit(self, nit: str):
        self.__nit = nit

    @property
    def direccion(self):
        return self.__direccion
    @direccion.setter
    def direccion(self, direccion: str):
        self.__direccion = direccion

    @property
    def pedidos19(self):
        return self.__pedidos19
    @pedidos19.setter
    def pedidos19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Proveedor__pedidos19", None)
        self.__pedidos19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "proveedor18"):
                    opp_val = getattr(item, "proveedor18", None)
                    
                    if opp_val == self:
                        setattr(item, "proveedor18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "proveedor18"):
                    opp_val = getattr(item, "proveedor18", None)
                    
                    setattr(item, "proveedor18", self)
                    

    @property
    def factura29(self):
        return self.__factura29
    @factura29.setter
    def factura29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Proveedor__factura29", None)
        self.__factura29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "proveedor28"):
                    opp_val = getattr(item, "proveedor28", None)
                    
                    if opp_val == self:
                        setattr(item, "proveedor28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "proveedor28"):
                    opp_val = getattr(item, "proveedor28", None)
                    
                    setattr(item, "proveedor28", self)
                    

    @property
    def ordenesPedidos16(self):
        return self.__ordenesPedidos16
    @ordenesPedidos16.setter
    def ordenesPedidos16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Proveedor__ordenesPedidos16", None)
        self.__ordenesPedidos16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "proveedor17"):
                    opp_val = getattr(item, "proveedor17", None)
                    
                    if opp_val == self:
                        setattr(item, "proveedor17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "proveedor17"):
                    opp_val = getattr(item, "proveedor17", None)
                    
                    setattr(item, "proveedor17", self)
                    



class Dependencias:

    def __init__(self, codigo: str, nombre: str, responsable: str, solicitudSuministro26: set["SolicitudSuministro"] = None):
        self.codigo = codigo
        self.nombre = nombre
        self.responsable = responsable
        self.solicitudSuministro26 = solicitudSuministro26 if solicitudSuministro26 is not None else set()
        
        pass
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
    def responsable(self):
        return self.__responsable
    @responsable.setter
    def responsable(self, responsable: str):
        self.__responsable = responsable

    @property
    def solicitudSuministro26(self):
        return self.__solicitudSuministro26
    @solicitudSuministro26.setter
    def solicitudSuministro26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dependencias__solicitudSuministro26", None)
        self.__solicitudSuministro26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dependencias27"):
                    opp_val = getattr(item, "dependencias27", None)
                    
                    if opp_val == self:
                        setattr(item, "dependencias27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dependencias27"):
                    opp_val = getattr(item, "dependencias27", None)
                    
                    setattr(item, "dependencias27", self)
                    



class Elementos:

    def __init__(self, referencia: str, clasificacion: str, ordenesPedidos20: set["OrdenesPedidos"] = None, solicitudSuministro24: set["SolicitudSuministro"] = None, factura30: set["Factura"] = None):
        self.referencia = referencia
        self.clasificacion = clasificacion
        self.ordenesPedidos20 = ordenesPedidos20 if ordenesPedidos20 is not None else set()
        self.solicitudSuministro24 = solicitudSuministro24 if solicitudSuministro24 is not None else set()
        self.factura30 = factura30 if factura30 is not None else set()
        
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
    def factura30(self):
        return self.__factura30
    @factura30.setter
    def factura30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elementos__factura30", None)
        self.__factura30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "elementos31"):
                    opp_val = getattr(item, "elementos31", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "elementos31"):
                    opp_val = getattr(item, "elementos31", None)
                    
                    if opp_val is None:
                        setattr(item, "elementos31", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def solicitudSuministro24(self):
        return self.__solicitudSuministro24
    @solicitudSuministro24.setter
    def solicitudSuministro24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elementos__solicitudSuministro24", None)
        self.__solicitudSuministro24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "elementos25"):
                    opp_val = getattr(item, "elementos25", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "elementos25"):
                    opp_val = getattr(item, "elementos25", None)
                    
                    if opp_val is None:
                        setattr(item, "elementos25", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def ordenesPedidos20(self):
        return self.__ordenesPedidos20
    @ordenesPedidos20.setter
    def ordenesPedidos20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elementos__ordenesPedidos20", None)
        self.__ordenesPedidos20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "elementos21"):
                    opp_val = getattr(item, "elementos21", None)
                    
                    if opp_val == self:
                        setattr(item, "elementos21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "elementos21"):
                    opp_val = getattr(item, "elementos21", None)
                    
                    setattr(item, "elementos21", self)
                    



class OrdenesPedidos:

    def __init__(self, codigo: str, fecha: str, proveedor17: "Proveedor" = None, elementos21: "Elementos" = None, solicitudSuministro23: set["SolicitudSuministro"] = None):
        self.codigo = codigo
        self.fecha = fecha
        self.proveedor17 = proveedor17
        self.elementos21 = elementos21
        self.solicitudSuministro23 = solicitudSuministro23 if solicitudSuministro23 is not None else set()
        
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
    def solicitudSuministro23(self):
        return self.__solicitudSuministro23
    @solicitudSuministro23.setter
    def solicitudSuministro23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrdenesPedidos__solicitudSuministro23", None)
        self.__solicitudSuministro23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ordenesPedidos22"):
                    opp_val = getattr(item, "ordenesPedidos22", None)
                    
                    if opp_val == self:
                        setattr(item, "ordenesPedidos22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ordenesPedidos22"):
                    opp_val = getattr(item, "ordenesPedidos22", None)
                    
                    setattr(item, "ordenesPedidos22", self)
                    

    @property
    def proveedor17(self):
        return self.__proveedor17
    @proveedor17.setter
    def proveedor17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrdenesPedidos__proveedor17", None)
        self.__proveedor17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ordenesPedidos16"):
                opp_val = getattr(old_value, "ordenesPedidos16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ordenesPedidos16"):
                opp_val = getattr(value, "ordenesPedidos16", None)
                if opp_val is None:
                    setattr(value, "ordenesPedidos16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def elementos21(self):
        return self.__elementos21
    @elementos21.setter
    def elementos21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrdenesPedidos__elementos21", None)
        self.__elementos21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ordenesPedidos20"):
                opp_val = getattr(old_value, "ordenesPedidos20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ordenesPedidos20"):
                opp_val = getattr(value, "ordenesPedidos20", None)
                if opp_val is None:
                    setattr(value, "ordenesPedidos20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Sistema_WEB_M_vil___Recepci_n_de_pedidos_Component:

    pass


class Deoartamento_de_inventarios_y_suministros_DIS_Component:

    pass


class Millenium_Component1:

    pass


class Millenium_Component:

    pass


class Generar_ordenes_de_pedido_external:

    pass


class Clasificar_producto_external:

    pass


class Recibir_productos_o_pedidos_external:

    pass
