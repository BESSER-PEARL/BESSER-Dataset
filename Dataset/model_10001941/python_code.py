from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Contabilidad_y_Tesorer_a_Actor:

    pass


class Responsable_inventariorio_Actor:

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


class Recibir_productos_o_pedidos_external:

    pass


class Registrar_Proveedores_external:

    pass


class Brindar_consultor_a_external:

    pass


class ServidorBD_Node:

    pass


class ServidoWeb_Node:

    pass


class Persistencia_Factura_Component:

    pass


class logicaPresentacion_Factura_Component:

    pass


class Servidor_Intel_i9_Node:

    pass


class Pedidos:

    def __init__(self, codigo: str, fecha: str, proveedor20: "Proveedor" = None):
        self.codigo = codigo
        self.fecha = fecha
        self.proveedor20 = proveedor20
        
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
    def proveedor20(self):
        return self.__proveedor20
    @proveedor20.setter
    def proveedor20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pedidos__proveedor20", None)
        self.__proveedor20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pedidos21"):
                opp_val = getattr(old_value, "pedidos21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pedidos21"):
                opp_val = getattr(value, "pedidos21", None)
                if opp_val is None:
                    setattr(value, "pedidos21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Dependencia:

    def __init__(self, codgio: str, nombre: str, reponsable: str, solicitudSuministro28: set["SolicitudSuministro"] = None):
        self.codgio = codgio
        self.nombre = nombre
        self.reponsable = reponsable
        self.solicitudSuministro28 = solicitudSuministro28 if solicitudSuministro28 is not None else set()
        
        pass
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def reponsable(self):
        return self.__reponsable
    @reponsable.setter
    def reponsable(self, reponsable: str):
        self.__reponsable = reponsable

    @property
    def codgio(self):
        return self.__codgio
    @codgio.setter
    def codgio(self, codgio: str):
        self.__codgio = codgio

    @property
    def solicitudSuministro28(self):
        return self.__solicitudSuministro28
    @solicitudSuministro28.setter
    def solicitudSuministro28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dependencia__solicitudSuministro28", None)
        self.__solicitudSuministro28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dependencia29"):
                    opp_val = getattr(item, "dependencia29", None)
                    
                    if opp_val == self:
                        setattr(item, "dependencia29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dependencia29"):
                    opp_val = getattr(item, "dependencia29", None)
                    
                    setattr(item, "dependencia29", self)
                    



class SolicitudSuministro:

    def __init__(self, solicitud: str, fecha: str, elementos24: "Elementos" = None, _rdenesPedido27: "_rdenesPedido" = None, dependencia29: "Dependencia" = None):
        self.solicitud = solicitud
        self.fecha = fecha
        self.elementos24 = elementos24
        self._rdenesPedido27 = _rdenesPedido27
        self.dependencia29 = dependencia29
        
        pass
    @property
    def solicitud(self):
        return self.__solicitud
    @solicitud.setter
    def solicitud(self, solicitud: str):
        self.__solicitud = solicitud

    @property
    def fecha(self):
        return self.__fecha
    @fecha.setter
    def fecha(self, fecha: str):
        self.__fecha = fecha

    @property
    def _rdenesPedido27(self):
        return self.___rdenesPedido27
    @_rdenesPedido27.setter
    def _rdenesPedido27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SolicitudSuministro___rdenesPedido27", None)
        self.___rdenesPedido27 = value
        
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
    def dependencia29(self):
        return self.__dependencia29
    @dependencia29.setter
    def dependencia29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SolicitudSuministro__dependencia29", None)
        self.__dependencia29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "solicitudSuministro28"):
                opp_val = getattr(old_value, "solicitudSuministro28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "solicitudSuministro28"):
                opp_val = getattr(value, "solicitudSuministro28", None)
                if opp_val is None:
                    setattr(value, "solicitudSuministro28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def elementos24(self):
        return self.__elementos24
    @elementos24.setter
    def elementos24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SolicitudSuministro__elementos24", None)
        self.__elementos24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "solicitudSuministro25"):
                opp_val = getattr(old_value, "solicitudSuministro25", None)
                if opp_val == self:
                    setattr(old_value, "solicitudSuministro25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "solicitudSuministro25"):
                opp_val = getattr(value, "solicitudSuministro25", None)
                setattr(value, "solicitudSuministro25", self)



class Factura:

    def __init__(self, fecha: str, codigo: str, proveedor30: "Proveedor" = None, elementos33: set["Elementos"] = None):
        self.fecha = fecha
        self.codigo = codigo
        self.proveedor30 = proveedor30
        self.elementos33 = elementos33 if elementos33 is not None else set()
        
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
    def elementos33(self):
        return self.__elementos33
    @elementos33.setter
    def elementos33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Factura__elementos33", None)
        self.__elementos33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "factura32"):
                    opp_val = getattr(item, "factura32", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "factura32"):
                    opp_val = getattr(item, "factura32", None)
                    
                    if opp_val is None:
                        setattr(item, "factura32", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def proveedor30(self):
        return self.__proveedor30
    @proveedor30.setter
    def proveedor30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Factura__proveedor30", None)
        self.__proveedor30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "factura31"):
                opp_val = getattr(old_value, "factura31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "factura31"):
                opp_val = getattr(value, "factura31", None)
                if opp_val is None:
                    setattr(value, "factura31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Elementos:

    def __init__(self, referencia: str, clasificacion: str, _rdenesPedido22: set["_rdenesPedido"] = None, solicitudSuministro25: "SolicitudSuministro" = None, factura32: set["Factura"] = None):
        self.referencia = referencia
        self.clasificacion = clasificacion
        self._rdenesPedido22 = _rdenesPedido22 if _rdenesPedido22 is not None else set()
        self.solicitudSuministro25 = solicitudSuministro25
        self.factura32 = factura32 if factura32 is not None else set()
        
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
    def _rdenesPedido22(self):
        return self.___rdenesPedido22
    @_rdenesPedido22.setter
    def _rdenesPedido22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elementos___rdenesPedido22", None)
        self.___rdenesPedido22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "elementos23"):
                    opp_val = getattr(item, "elementos23", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "elementos23"):
                    opp_val = getattr(item, "elementos23", None)
                    
                    if opp_val is None:
                        setattr(item, "elementos23", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def solicitudSuministro25(self):
        return self.__solicitudSuministro25
    @solicitudSuministro25.setter
    def solicitudSuministro25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elementos__solicitudSuministro25", None)
        self.__solicitudSuministro25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elementos24"):
                opp_val = getattr(old_value, "elementos24", None)
                if opp_val == self:
                    setattr(old_value, "elementos24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elementos24"):
                opp_val = getattr(value, "elementos24", None)
                setattr(value, "elementos24", self)

    @property
    def factura32(self):
        return self.__factura32
    @factura32.setter
    def factura32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elementos__factura32", None)
        self.__factura32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "elementos33"):
                    opp_val = getattr(item, "elementos33", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "elementos33"):
                    opp_val = getattr(item, "elementos33", None)
                    
                    if opp_val is None:
                        setattr(item, "elementos33", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class _rdenesPedido:

    def __init__(self, codigo: str, fecha: str, proveedor18: "Proveedor" = None, elementos23: set["Elementos"] = None, solicitudSuministro26: set["SolicitudSuministro"] = None):
        self.codigo = codigo
        self.fecha = fecha
        self.proveedor18 = proveedor18
        self.elementos23 = elementos23 if elementos23 is not None else set()
        self.solicitudSuministro26 = solicitudSuministro26 if solicitudSuministro26 is not None else set()
        
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
    def solicitudSuministro26(self):
        return self.__solicitudSuministro26
    @solicitudSuministro26.setter
    def solicitudSuministro26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__rdenesPedido__solicitudSuministro26", None)
        self.__solicitudSuministro26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "_rdenesPedido27"):
                    opp_val = getattr(item, "_rdenesPedido27", None)
                    
                    if opp_val == self:
                        setattr(item, "_rdenesPedido27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "_rdenesPedido27"):
                    opp_val = getattr(item, "_rdenesPedido27", None)
                    
                    setattr(item, "_rdenesPedido27", self)
                    

    @property
    def proveedor18(self):
        return self.__proveedor18
    @proveedor18.setter
    def proveedor18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__rdenesPedido__proveedor18", None)
        self.__proveedor18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "_rdenesPedido19"):
                opp_val = getattr(old_value, "_rdenesPedido19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "_rdenesPedido19"):
                opp_val = getattr(value, "_rdenesPedido19", None)
                if opp_val is None:
                    setattr(value, "_rdenesPedido19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def elementos23(self):
        return self.__elementos23
    @elementos23.setter
    def elementos23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__rdenesPedido__elementos23", None)
        self.__elementos23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "_rdenesPedido22"):
                    opp_val = getattr(item, "_rdenesPedido22", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "_rdenesPedido22"):
                    opp_val = getattr(item, "_rdenesPedido22", None)
                    
                    if opp_val is None:
                        setattr(item, "_rdenesPedido22", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Proveedor:

    def __init__(self, nit: str, razonSocial: str, direccion: str, telefono: str, _rdenesPedido19: set["_rdenesPedido"] = None, pedidos21: set["Pedidos"] = None, factura31: set["Factura"] = None):
        self.nit = nit
        self.razonSocial = razonSocial
        self.direccion = direccion
        self.telefono = telefono
        self._rdenesPedido19 = _rdenesPedido19 if _rdenesPedido19 is not None else set()
        self.pedidos21 = pedidos21 if pedidos21 is not None else set()
        self.factura31 = factura31 if factura31 is not None else set()
        
        pass
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
    def telefono(self):
        return self.__telefono
    @telefono.setter
    def telefono(self, telefono: str):
        self.__telefono = telefono

    @property
    def pedidos21(self):
        return self.__pedidos21
    @pedidos21.setter
    def pedidos21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Proveedor__pedidos21", None)
        self.__pedidos21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "proveedor20"):
                    opp_val = getattr(item, "proveedor20", None)
                    
                    if opp_val == self:
                        setattr(item, "proveedor20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "proveedor20"):
                    opp_val = getattr(item, "proveedor20", None)
                    
                    setattr(item, "proveedor20", self)
                    

    @property
    def _rdenesPedido19(self):
        return self.___rdenesPedido19
    @_rdenesPedido19.setter
    def _rdenesPedido19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Proveedor___rdenesPedido19", None)
        self.___rdenesPedido19 = value if value is not None else set()
        
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
    def factura31(self):
        return self.__factura31
    @factura31.setter
    def factura31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Proveedor__factura31", None)
        self.__factura31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "proveedor30"):
                    opp_val = getattr(item, "proveedor30", None)
                    
                    if opp_val == self:
                        setattr(item, "proveedor30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "proveedor30"):
                    opp_val = getattr(item, "proveedor30", None)
                    
                    setattr(item, "proveedor30", self)
                    



class Sistema_WEB_Movil___Recepci_n_de_pedidos_Component:

    pass


class Departamento_de_Inventarios_y_Suministros_DIS_Component:

    pass


class Millenium_S_A_Component:

    pass
