from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Responsable_inventario_Actor:

    pass


class Contabilidad_y_tesoreria_Actor:

    pass


class Dependencias_Actor:

    pass


class Proveedores_Actor:

    pass


class Juridica_Actor:

    pass


class Natural_Actor:

    pass


class Cliente_Actor:

    pass





class Revisi_n_de_factura_external:

    pass


class Clasificar_producto_external:

    pass


class Entregar_productos_external:

    pass


class Recibir_ordenes_de_suministros_external:

    pass


class Registrar_proveedores_external:

    pass


class Recibir_productos_o_pedidos_external:

    pass


class Brindar_Consultorias_external:

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



class dependencia:

    def __init__(self, codigo: str, nombre: str, responsable: str, solicitudSuministros26: set["SolicitudSuministros"] = None):
        self.codigo = codigo
        self.nombre = nombre
        self.responsable = responsable
        self.solicitudSuministros26 = solicitudSuministros26 if solicitudSuministros26 is not None else set()
        
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
    def solicitudSuministros26(self):
        return self.__solicitudSuministros26
    @solicitudSuministros26.setter
    def solicitudSuministros26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dependencia__solicitudSuministros26", None)
        self.__solicitudSuministros26 = value if value is not None else set()
        
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
                    



class SolicitudSuministros:

    def __init__(self, codigo: str, fecha: str, elementos22: set["Elementos"] = None, ordenesPedidos24: "OrdenesPedidos" = None, dependencia27: "dependencia" = None):
        self.codigo = codigo
        self.fecha = fecha
        self.elementos22 = elementos22 if elementos22 is not None else set()
        self.ordenesPedidos24 = ordenesPedidos24
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
    def ordenesPedidos24(self):
        return self.__ordenesPedidos24
    @ordenesPedidos24.setter
    def ordenesPedidos24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SolicitudSuministros__ordenesPedidos24", None)
        self.__ordenesPedidos24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "solicitudSuministros25"):
                opp_val = getattr(old_value, "solicitudSuministros25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "solicitudSuministros25"):
                opp_val = getattr(value, "solicitudSuministros25", None)
                if opp_val is None:
                    setattr(value, "solicitudSuministros25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dependencia27(self):
        return self.__dependencia27
    @dependencia27.setter
    def dependencia27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SolicitudSuministros__dependencia27", None)
        self.__dependencia27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "solicitudSuministros26"):
                opp_val = getattr(old_value, "solicitudSuministros26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "solicitudSuministros26"):
                opp_val = getattr(value, "solicitudSuministros26", None)
                if opp_val is None:
                    setattr(value, "solicitudSuministros26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def elementos22(self):
        return self.__elementos22
    @elementos22.setter
    def elementos22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SolicitudSuministros__elementos22", None)
        self.__elementos22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "solicitudSuministros23"):
                    opp_val = getattr(item, "solicitudSuministros23", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "solicitudSuministros23"):
                    opp_val = getattr(item, "solicitudSuministros23", None)
                    
                    if opp_val is None:
                        setattr(item, "solicitudSuministros23", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Elementos:

    def __init__(self, referencia: str, clasificacion: str, ordenesPedidos21: set["OrdenesPedidos"] = None, solicitudSuministros23: set["SolicitudSuministros"] = None, factura31: set["Factura"] = None):
        self.referencia = referencia
        self.clasificacion = clasificacion
        self.ordenesPedidos21 = ordenesPedidos21 if ordenesPedidos21 is not None else set()
        self.solicitudSuministros23 = solicitudSuministros23 if solicitudSuministros23 is not None else set()
        self.factura31 = factura31 if factura31 is not None else set()
        
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
    def factura31(self):
        return self.__factura31
    @factura31.setter
    def factura31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elementos__factura31", None)
        self.__factura31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "elementos30"):
                    opp_val = getattr(item, "elementos30", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "elementos30"):
                    opp_val = getattr(item, "elementos30", None)
                    
                    if opp_val is None:
                        setattr(item, "elementos30", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def ordenesPedidos21(self):
        return self.__ordenesPedidos21
    @ordenesPedidos21.setter
    def ordenesPedidos21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elementos__ordenesPedidos21", None)
        self.__ordenesPedidos21 = value if value is not None else set()
        
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
    def solicitudSuministros23(self):
        return self.__solicitudSuministros23
    @solicitudSuministros23.setter
    def solicitudSuministros23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elementos__solicitudSuministros23", None)
        self.__solicitudSuministros23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "elementos22"):
                    opp_val = getattr(item, "elementos22", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "elementos22"):
                    opp_val = getattr(item, "elementos22", None)
                    
                    if opp_val is None:
                        setattr(item, "elementos22", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Factura:

    def __init__(self, codigo: str, fecha: str, proveedor28: "Proveedor" = None, elementos30: set["Elementos"] = None):
        self.codigo = codigo
        self.fecha = fecha
        self.proveedor28 = proveedor28
        self.elementos30 = elementos30 if elementos30 is not None else set()
        
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
    def elementos30(self):
        return self.__elementos30
    @elementos30.setter
    def elementos30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Factura__elementos30", None)
        self.__elementos30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "factura31"):
                    opp_val = getattr(item, "factura31", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "factura31"):
                    opp_val = getattr(item, "factura31", None)
                    
                    if opp_val is None:
                        setattr(item, "factura31", set([self]))
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



class Proveedor:

    def __init__(self, nit: str, nombre: str, direccion: str, telefono: str, pedidos19: set["Pedidos"] = None, factura29: set["Factura"] = None, ordenesPedidos16: set["OrdenesPedidos"] = None):
        self.nit = nit
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.pedidos19 = pedidos19 if pedidos19 is not None else set()
        self.factura29 = factura29 if factura29 is not None else set()
        self.ordenesPedidos16 = ordenesPedidos16 if ordenesPedidos16 is not None else set()
        
        pass
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
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def telefono(self):
        return self.__telefono
    @telefono.setter
    def telefono(self, telefono: str):
        self.__telefono = telefono

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
                    



class OrdenesPedidos:

    def __init__(self, codigo: str, fecha: str, elementos20: set["Elementos"] = None, solicitudSuministros25: set["SolicitudSuministros"] = None, proveedor17: "Proveedor" = None):
        self.codigo = codigo
        self.fecha = fecha
        self.elementos20 = elementos20 if elementos20 is not None else set()
        self.solicitudSuministros25 = solicitudSuministros25 if solicitudSuministros25 is not None else set()
        self.proveedor17 = proveedor17
        
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
    def elementos20(self):
        return self.__elementos20
    @elementos20.setter
    def elementos20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrdenesPedidos__elementos20", None)
        self.__elementos20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ordenesPedidos21"):
                    opp_val = getattr(item, "ordenesPedidos21", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ordenesPedidos21"):
                    opp_val = getattr(item, "ordenesPedidos21", None)
                    
                    if opp_val is None:
                        setattr(item, "ordenesPedidos21", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def solicitudSuministros25(self):
        return self.__solicitudSuministros25
    @solicitudSuministros25.setter
    def solicitudSuministros25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrdenesPedidos__solicitudSuministros25", None)
        self.__solicitudSuministros25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ordenesPedidos24"):
                    opp_val = getattr(item, "ordenesPedidos24", None)
                    
                    if opp_val == self:
                        setattr(item, "ordenesPedidos24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ordenesPedidos24"):
                    opp_val = getattr(item, "ordenesPedidos24", None)
                    
                    setattr(item, "ordenesPedidos24", self)
                    

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



class Sistema_Web_Movil___Reccepci_n_de_pedidos_Component:

    pass


class Departamento_de_Inventarios_y_Suministros_Dis_Component:

    pass


class Millenium_Component:

    pass
