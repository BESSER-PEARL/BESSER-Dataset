from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Calcular_Actor:

    pass


class Clientes_Actor:

    pass


class Cliente2_Actor:

    pass


class Responsable_de_inventario_Actor:

    pass


class Contabilidad_y_Tesoreria_Actor:

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





class Clasificar_producto_external:

    pass


class Entregar_productos_external:

    pass


class Recibir_ordenes_de_suministro_external:

    pass


class Recibir_productos_o_pedidos_external:

    pass


class Registrar_proveedores_external:

    pass


class Brindar_consultorias_external:

    pass


class Principal:

    pass


class Impuesto:

    def __init__(self, porcentaje: float, producto38: "Producto" = None):
        self.porcentaje = porcentaje
        self.producto38 = producto38
        
        pass
    @property
    def porcentaje(self):
        return self.__porcentaje
    @porcentaje.setter
    def porcentaje(self, porcentaje: float):
        self.__porcentaje = porcentaje

    @property
    def producto38(self):
        return self.__producto38
    @producto38.setter
    def producto38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Impuesto__producto38", None)
        self.__producto38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "impuesto39"):
                opp_val = getattr(old_value, "impuesto39", None)
                if opp_val == self:
                    setattr(old_value, "impuesto39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "impuesto39"):
                opp_val = getattr(value, "impuesto39", None)
                setattr(value, "impuesto39", self)



class Producto:

    def __init__(self, cantidad: int, codigo: int, nombre: str, precio: float, venta36: set["Venta"] = None, impuesto39: "Impuesto" = None):
        self.cantidad = cantidad
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.venta36 = venta36 if venta36 is not None else set()
        self.impuesto39 = impuesto39
        
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
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def precio(self):
        return self.__precio
    @precio.setter
    def precio(self, precio: float):
        self.__precio = precio

    @property
    def cantidad(self):
        return self.__cantidad
    @cantidad.setter
    def cantidad(self, cantidad: int):
        self.__cantidad = cantidad

    @property
    def venta36(self):
        return self.__venta36
    @venta36.setter
    def venta36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Producto__venta36", None)
        self.__venta36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "producto37"):
                    opp_val = getattr(item, "producto37", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "producto37"):
                    opp_val = getattr(item, "producto37", None)
                    
                    if opp_val is None:
                        setattr(item, "producto37", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def impuesto39(self):
        return self.__impuesto39
    @impuesto39.setter
    def impuesto39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Producto__impuesto39", None)
        self.__impuesto39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "producto38"):
                opp_val = getattr(old_value, "producto38", None)
                if opp_val == self:
                    setattr(old_value, "producto38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "producto38"):
                opp_val = getattr(value, "producto38", None)
                setattr(value, "producto38", self)



class Venta:

    def __init__(self, codigo: int, fecha: str, producto37: set["Producto"] = None, principal40: "Principal" = None):
        self.codigo = codigo
        self.fecha = fecha
        self.producto37 = producto37 if producto37 is not None else set()
        self.principal40 = principal40
        
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
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def producto37(self):
        return self.__producto37
    @producto37.setter
    def producto37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Venta__producto37", None)
        self.__producto37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "venta36"):
                    opp_val = getattr(item, "venta36", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "venta36"):
                    opp_val = getattr(item, "venta36", None)
                    
                    if opp_val is None:
                        setattr(item, "venta36", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def principal40(self):
        return self.__principal40
    @principal40.setter
    def principal40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Venta__principal40", None)
        self.__principal40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "venta41"):
                opp_val = getattr(old_value, "venta41", None)
                if opp_val == self:
                    setattr(old_value, "venta41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "venta41"):
                opp_val = getattr(value, "venta41", None)
                setattr(value, "venta41", self)



class Clientes:

    pass


class Calcular:

    pass


class ServidorBD_Node:

    pass


class ServidorWEB_Node:

    pass


class persistenciaFactura_Component:

    pass


class logicaPresentacionFactura_Component:

    pass


class Servidor_Intel_i8_Node:

    pass


class EmpresasFiliales:

    def __init__(self, codigo: int, razonSocial: str, trabajador33: set["Trabajador"] = None):
        self.codigo = codigo
        self.razonSocial = razonSocial
        self.trabajador33 = trabajador33 if trabajador33 is not None else set()
        
        pass
    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def razonSocial(self):
        return self.__razonSocial
    @razonSocial.setter
    def razonSocial(self, razonSocial: str):
        self.__razonSocial = razonSocial

    @property
    def trabajador33(self):
        return self.__trabajador33
    @trabajador33.setter
    def trabajador33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmpresasFiliales__trabajador33", None)
        self.__trabajador33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "empresasFiliales32"):
                    opp_val = getattr(item, "empresasFiliales32", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "empresasFiliales32"):
                    opp_val = getattr(item, "empresasFiliales32", None)
                    
                    if opp_val is None:
                        setattr(item, "empresasFiliales32", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class VentaCalzado:

    def __init__(self, codigo: int, razonSocial: str, NroTrabajadoresBase: int, EquipoDirectivo: str, PteEquipoDirectivo: str):
        self.codigo = codigo
        self.razonSocial = razonSocial
        self.NroTrabajadoresBase = NroTrabajadoresBase
        self.EquipoDirectivo = EquipoDirectivo
        self.PteEquipoDirectivo = PteEquipoDirectivo
        
        pass
    @property
    def PteEquipoDirectivo(self):
        return self.__PteEquipoDirectivo
    @PteEquipoDirectivo.setter
    def PteEquipoDirectivo(self, PteEquipoDirectivo: str):
        self.__PteEquipoDirectivo = PteEquipoDirectivo

    @property
    def EquipoDirectivo(self):
        return self.__EquipoDirectivo
    @EquipoDirectivo.setter
    def EquipoDirectivo(self, EquipoDirectivo: str):
        self.__EquipoDirectivo = EquipoDirectivo

    @property
    def NroTrabajadoresBase(self):
        return self.__NroTrabajadoresBase
    @NroTrabajadoresBase.setter
    def NroTrabajadoresBase(self, NroTrabajadoresBase: int):
        self.__NroTrabajadoresBase = NroTrabajadoresBase

    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def razonSocial(self):
        return self.__razonSocial
    @razonSocial.setter
    def razonSocial(self, razonSocial: str):
        self.__razonSocial = razonSocial



class Distribucion:

    def __init__(self, codigo: int, razonSocial: str, NroTrabajadoresBase: int, EquipoDirectivo: str, PteEquipoDirectivo: str):
        self.codigo = codigo
        self.razonSocial = razonSocial
        self.NroTrabajadoresBase = NroTrabajadoresBase
        self.EquipoDirectivo = EquipoDirectivo
        self.PteEquipoDirectivo = PteEquipoDirectivo
        
        pass
    @property
    def PteEquipoDirectivo(self):
        return self.__PteEquipoDirectivo
    @PteEquipoDirectivo.setter
    def PteEquipoDirectivo(self, PteEquipoDirectivo: str):
        self.__PteEquipoDirectivo = PteEquipoDirectivo

    @property
    def NroTrabajadoresBase(self):
        return self.__NroTrabajadoresBase
    @NroTrabajadoresBase.setter
    def NroTrabajadoresBase(self, NroTrabajadoresBase: int):
        self.__NroTrabajadoresBase = NroTrabajadoresBase

    @property
    def razonSocial(self):
        return self.__razonSocial
    @razonSocial.setter
    def razonSocial(self, razonSocial: str):
        self.__razonSocial = razonSocial

    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def EquipoDirectivo(self):
        return self.__EquipoDirectivo
    @EquipoDirectivo.setter
    def EquipoDirectivo(self, EquipoDirectivo: str):
        self.__EquipoDirectivo = EquipoDirectivo



class Fabricacion:

    def __init__(self, codigo: int, razonSocial: str, NroTrabajadoresBase: int, EquipoDirectivo: str, PteEquipoDirectivo: str):
        self.codigo = codigo
        self.razonSocial = razonSocial
        self.NroTrabajadoresBase = NroTrabajadoresBase
        self.EquipoDirectivo = EquipoDirectivo
        self.PteEquipoDirectivo = PteEquipoDirectivo
        
        pass
    @property
    def NroTrabajadoresBase(self):
        return self.__NroTrabajadoresBase
    @NroTrabajadoresBase.setter
    def NroTrabajadoresBase(self, NroTrabajadoresBase: int):
        self.__NroTrabajadoresBase = NroTrabajadoresBase

    @property
    def razonSocial(self):
        return self.__razonSocial
    @razonSocial.setter
    def razonSocial(self, razonSocial: str):
        self.__razonSocial = razonSocial

    @property
    def EquipoDirectivo(self):
        return self.__EquipoDirectivo
    @EquipoDirectivo.setter
    def EquipoDirectivo(self, EquipoDirectivo: str):
        self.__EquipoDirectivo = EquipoDirectivo

    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def PteEquipoDirectivo(self):
        return self.__PteEquipoDirectivo
    @PteEquipoDirectivo.setter
    def PteEquipoDirectivo(self, PteEquipoDirectivo: str):
        self.__PteEquipoDirectivo = PteEquipoDirectivo



class Informe:

    def __init__(self, codigo: int, nombreTrabajador: str, FilialesTrabajados: str, mesesTrabajadosFiliales: int, HrsExtrasFiliales: str, HrsTrabajadas: int, trabajador31: set["Trabajador"] = None):
        self.codigo = codigo
        self.nombreTrabajador = nombreTrabajador
        self.FilialesTrabajados = FilialesTrabajados
        self.mesesTrabajadosFiliales = mesesTrabajadosFiliales
        self.HrsExtrasFiliales = HrsExtrasFiliales
        self.HrsTrabajadas = HrsTrabajadas
        self.trabajador31 = trabajador31 if trabajador31 is not None else set()
        
        pass
    @property
    def nombreTrabajador(self):
        return self.__nombreTrabajador
    @nombreTrabajador.setter
    def nombreTrabajador(self, nombreTrabajador: str):
        self.__nombreTrabajador = nombreTrabajador

    @property
    def FilialesTrabajados(self):
        return self.__FilialesTrabajados
    @FilialesTrabajados.setter
    def FilialesTrabajados(self, FilialesTrabajados: str):
        self.__FilialesTrabajados = FilialesTrabajados

    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def mesesTrabajadosFiliales(self):
        return self.__mesesTrabajadosFiliales
    @mesesTrabajadosFiliales.setter
    def mesesTrabajadosFiliales(self, mesesTrabajadosFiliales: int):
        self.__mesesTrabajadosFiliales = mesesTrabajadosFiliales

    @property
    def HrsTrabajadas(self):
        return self.__HrsTrabajadas
    @HrsTrabajadas.setter
    def HrsTrabajadas(self, HrsTrabajadas: int):
        self.__HrsTrabajadas = HrsTrabajadas

    @property
    def HrsExtrasFiliales(self):
        return self.__HrsExtrasFiliales
    @HrsExtrasFiliales.setter
    def HrsExtrasFiliales(self, HrsExtrasFiliales: str):
        self.__HrsExtrasFiliales = HrsExtrasFiliales

    @property
    def trabajador31(self):
        return self.__trabajador31
    @trabajador31.setter
    def trabajador31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Informe__trabajador31", None)
        self.__trabajador31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "informe30"):
                    opp_val = getattr(item, "informe30", None)
                    
                    if opp_val == self:
                        setattr(item, "informe30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "informe30"):
                    opp_val = getattr(item, "informe30", None)
                    
                    setattr(item, "informe30", self)
                    



class Pedidos:

    def __init__(self, codigo: str, fecha: str, proveedor17: "Proveedor" = None):
        self.codigo = codigo
        self.fecha = fecha
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
    def proveedor17(self):
        return self.__proveedor17
    @proveedor17.setter
    def proveedor17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pedidos__proveedor17", None)
        self.__proveedor17 = value
        
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



class Trabajador:

    def __init__(self, DNI: int, nombre: str, HrsTrabajadasMes: int, Sueldo: int, informe30: "Informe" = None, empresasFiliales32: set["EmpresasFiliales"] = None):
        self.DNI = DNI
        self.nombre = nombre
        self.HrsTrabajadasMes = HrsTrabajadasMes
        self.Sueldo = Sueldo
        self.informe30 = informe30
        self.empresasFiliales32 = empresasFiliales32 if empresasFiliales32 is not None else set()
        
        pass
    @property
    def Sueldo(self):
        return self.__Sueldo
    @Sueldo.setter
    def Sueldo(self, Sueldo: int):
        self.__Sueldo = Sueldo

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def HrsTrabajadasMes(self):
        return self.__HrsTrabajadasMes
    @HrsTrabajadasMes.setter
    def HrsTrabajadasMes(self, HrsTrabajadasMes: int):
        self.__HrsTrabajadasMes = HrsTrabajadasMes

    @property
    def DNI(self):
        return self.__DNI
    @DNI.setter
    def DNI(self, DNI: int):
        self.__DNI = DNI

    @property
    def informe30(self):
        return self.__informe30
    @informe30.setter
    def informe30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Trabajador__informe30", None)
        self.__informe30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trabajador31"):
                opp_val = getattr(old_value, "trabajador31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trabajador31"):
                opp_val = getattr(value, "trabajador31", None)
                if opp_val is None:
                    setattr(value, "trabajador31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def empresasFiliales32(self):
        return self.__empresasFiliales32
    @empresasFiliales32.setter
    def empresasFiliales32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Trabajador__empresasFiliales32", None)
        self.__empresasFiliales32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trabajador33"):
                    opp_val = getattr(item, "trabajador33", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trabajador33"):
                    opp_val = getattr(item, "trabajador33", None)
                    
                    if opp_val is None:
                        setattr(item, "trabajador33", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Dependencia:

    def __init__(self, codigo: str, nombre: str, responsable: str, solicitudSuministro25: "SolicitudSuministro" = None):
        self.codigo = codigo
        self.nombre = nombre
        self.responsable = responsable
        self.solicitudSuministro25 = solicitudSuministro25
        
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
    def solicitudSuministro25(self):
        return self.__solicitudSuministro25
    @solicitudSuministro25.setter
    def solicitudSuministro25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dependencia__solicitudSuministro25", None)
        self.__solicitudSuministro25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dependencia24"):
                opp_val = getattr(old_value, "dependencia24", None)
                if opp_val == self:
                    setattr(old_value, "dependencia24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dependencia24"):
                opp_val = getattr(value, "dependencia24", None)
                setattr(value, "dependencia24", self)



class SolicitudSuministro:

    def __init__(self, codigo: str, fecha: str, dependencia24: "Dependencia" = None, elementos20: set["Elementos"] = None, ordenesPedidos22: "OrdenesPedidos" = None):
        self.codigo = codigo
        self.fecha = fecha
        self.dependencia24 = dependencia24
        self.elementos20 = elementos20 if elementos20 is not None else set()
        self.ordenesPedidos22 = ordenesPedidos22
        
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
        old_value = getattr(self, f"_SolicitudSuministro__dependencia24", None)
        self.__dependencia24 = value
        
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

    @property
    def elementos20(self):
        return self.__elementos20
    @elementos20.setter
    def elementos20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SolicitudSuministro__elementos20", None)
        self.__elementos20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "solicitudSuministro21"):
                    opp_val = getattr(item, "solicitudSuministro21", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "solicitudSuministro21"):
                    opp_val = getattr(item, "solicitudSuministro21", None)
                    
                    if opp_val is None:
                        setattr(item, "solicitudSuministro21", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Factura:

    def __init__(self, codigo: str, fecha: str, proveedor27: "Proveedor" = None, elementos28: set["Elementos"] = None):
        self.codigo = codigo
        self.fecha = fecha
        self.proveedor27 = proveedor27
        self.elementos28 = elementos28 if elementos28 is not None else set()
        
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
    def proveedor27(self):
        return self.__proveedor27
    @proveedor27.setter
    def proveedor27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Factura__proveedor27", None)
        self.__proveedor27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "factura26"):
                opp_val = getattr(old_value, "factura26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "factura26"):
                opp_val = getattr(value, "factura26", None)
                if opp_val is None:
                    setattr(value, "factura26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def elementos28(self):
        return self.__elementos28
    @elementos28.setter
    def elementos28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Factura__elementos28", None)
        self.__elementos28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "factura29"):
                    opp_val = getattr(item, "factura29", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "factura29"):
                    opp_val = getattr(item, "factura29", None)
                    
                    if opp_val is None:
                        setattr(item, "factura29", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Elementos:

    def __init__(self, referencia: str, clasificacion: str, factura29: set["Factura"] = None, ordenesPedidos19: set["OrdenesPedidos"] = None, solicitudSuministro21: set["SolicitudSuministro"] = None):
        self.referencia = referencia
        self.clasificacion = clasificacion
        self.factura29 = factura29 if factura29 is not None else set()
        self.ordenesPedidos19 = ordenesPedidos19 if ordenesPedidos19 is not None else set()
        self.solicitudSuministro21 = solicitudSuministro21 if solicitudSuministro21 is not None else set()
        
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
    def ordenesPedidos19(self):
        return self.__ordenesPedidos19
    @ordenesPedidos19.setter
    def ordenesPedidos19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elementos__ordenesPedidos19", None)
        self.__ordenesPedidos19 = value if value is not None else set()
        
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
    def solicitudSuministro21(self):
        return self.__solicitudSuministro21
    @solicitudSuministro21.setter
    def solicitudSuministro21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elementos__solicitudSuministro21", None)
        self.__solicitudSuministro21 = value if value is not None else set()
        
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
    def factura29(self):
        return self.__factura29
    @factura29.setter
    def factura29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elementos__factura29", None)
        self.__factura29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "elementos28"):
                    opp_val = getattr(item, "elementos28", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "elementos28"):
                    opp_val = getattr(item, "elementos28", None)
                    
                    if opp_val is None:
                        setattr(item, "elementos28", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Proveedor:

    def __init__(self, nit: str, razonSocial: str, direccion: str, telefono: str, factura26: set["Factura"] = None, ordenesPedidos14: set["OrdenesPedidos"] = None, pedidos16: set["Pedidos"] = None):
        self.nit = nit
        self.razonSocial = razonSocial
        self.direccion = direccion
        self.telefono = telefono
        self.factura26 = factura26 if factura26 is not None else set()
        self.ordenesPedidos14 = ordenesPedidos14 if ordenesPedidos14 is not None else set()
        self.pedidos16 = pedidos16 if pedidos16 is not None else set()
        
        pass
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
    def nit(self):
        return self.__nit
    @nit.setter
    def nit(self, nit: str):
        self.__nit = nit

    @property
    def razonSocial(self):
        return self.__razonSocial
    @razonSocial.setter
    def razonSocial(self, razonSocial: str):
        self.__razonSocial = razonSocial

    @property
    def pedidos16(self):
        return self.__pedidos16
    @pedidos16.setter
    def pedidos16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Proveedor__pedidos16", None)
        self.__pedidos16 = value if value is not None else set()
        
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
                    

    @property
    def factura26(self):
        return self.__factura26
    @factura26.setter
    def factura26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Proveedor__factura26", None)
        self.__factura26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "proveedor27"):
                    opp_val = getattr(item, "proveedor27", None)
                    
                    if opp_val == self:
                        setattr(item, "proveedor27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "proveedor27"):
                    opp_val = getattr(item, "proveedor27", None)
                    
                    setattr(item, "proveedor27", self)
                    

    @property
    def ordenesPedidos14(self):
        return self.__ordenesPedidos14
    @ordenesPedidos14.setter
    def ordenesPedidos14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Proveedor__ordenesPedidos14", None)
        self.__ordenesPedidos14 = value if value is not None else set()
        
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
                    



class OrdenesPedidos:

    def __init__(self, codigo: str, fecha: str, proveedor15: "Proveedor" = None, elementos18: set["Elementos"] = None, solicitudSuministro23: set["SolicitudSuministro"] = None):
        self.codigo = codigo
        self.fecha = fecha
        self.proveedor15 = proveedor15
        self.elementos18 = elementos18 if elementos18 is not None else set()
        self.solicitudSuministro23 = solicitudSuministro23 if solicitudSuministro23 is not None else set()
        
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
    def proveedor15(self):
        return self.__proveedor15
    @proveedor15.setter
    def proveedor15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrdenesPedidos__proveedor15", None)
        self.__proveedor15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ordenesPedidos14"):
                opp_val = getattr(old_value, "ordenesPedidos14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ordenesPedidos14"):
                opp_val = getattr(value, "ordenesPedidos14", None)
                if opp_val is None:
                    setattr(value, "ordenesPedidos14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def elementos18(self):
        return self.__elementos18
    @elementos18.setter
    def elementos18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrdenesPedidos__elementos18", None)
        self.__elementos18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ordenesPedidos19"):
                    opp_val = getattr(item, "ordenesPedidos19", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ordenesPedidos19"):
                    opp_val = getattr(item, "ordenesPedidos19", None)
                    
                    if opp_val is None:
                        setattr(item, "ordenesPedidos19", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Servicio_WEB_Movil___Recepcion_de_pedidos_Component:

    pass


class Departamento_de_Inventario_y_Suministros_DIS_Component:

    pass


class Millenium_Component:

    pass
