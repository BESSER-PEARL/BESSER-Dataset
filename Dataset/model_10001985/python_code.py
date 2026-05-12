from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Dependencias_Actor:

    pass


class Proveedores_Actor:

    pass


class Juridico_Actor:

    pass


class Natural_Actor:

    pass


class Clientes_Actor:

    pass





class Entregar_los_pedidos_external:

    pass


class Recivir_ordenes_de_suministro_external:

    pass


class Recibir_productos_external:

    pass


class Registrar_proveedores_external:

    pass


class Class4:

    pass


class Impuesto:

    def __init__(self, Porcentae: float, CalcularImpuesto: float, venta50: "Venta" = None, producto52: "Producto" = None):
        self.Porcentae = Porcentae
        self.CalcularImpuesto = CalcularImpuesto
        self.venta50 = venta50
        self.producto52 = producto52
        
        pass
    @property
    def Porcentae(self):
        return self.__Porcentae
    @Porcentae.setter
    def Porcentae(self, Porcentae: float):
        self.__Porcentae = Porcentae

    @property
    def CalcularImpuesto(self):
        return self.__CalcularImpuesto
    @CalcularImpuesto.setter
    def CalcularImpuesto(self, CalcularImpuesto: float):
        self.__CalcularImpuesto = CalcularImpuesto

    @property
    def producto52(self):
        return self.__producto52
    @producto52.setter
    def producto52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Impuesto__producto52", None)
        self.__producto52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "impuesto53"):
                opp_val = getattr(old_value, "impuesto53", None)
                if opp_val == self:
                    setattr(old_value, "impuesto53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "impuesto53"):
                opp_val = getattr(value, "impuesto53", None)
                setattr(value, "impuesto53", self)

    @property
    def venta50(self):
        return self.__venta50
    @venta50.setter
    def venta50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Impuesto__venta50", None)
        self.__venta50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "impuesto51"):
                opp_val = getattr(old_value, "impuesto51", None)
                if opp_val == self:
                    setattr(old_value, "impuesto51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "impuesto51"):
                opp_val = getattr(value, "impuesto51", None)
                setattr(value, "impuesto51", self)



class Producto:

    def __init__(self, Codigo: int, Nombre: str, Precio: int, Cantidad: int, CalcularCosto: int, venta48: "Venta" = None, impuesto53: "Impuesto" = None):
        self.Codigo = Codigo
        self.Nombre = Nombre
        self.Precio = Precio
        self.Cantidad = Cantidad
        self.CalcularCosto = CalcularCosto
        self.venta48 = venta48
        self.impuesto53 = impuesto53
        
        pass
    @property
    def Codigo(self):
        return self.__Codigo
    @Codigo.setter
    def Codigo(self, Codigo: int):
        self.__Codigo = Codigo

    @property
    def Nombre(self):
        return self.__Nombre
    @Nombre.setter
    def Nombre(self, Nombre: str):
        self.__Nombre = Nombre

    @property
    def CalcularCosto(self):
        return self.__CalcularCosto
    @CalcularCosto.setter
    def CalcularCosto(self, CalcularCosto: int):
        self.__CalcularCosto = CalcularCosto

    @property
    def Precio(self):
        return self.__Precio
    @Precio.setter
    def Precio(self, Precio: int):
        self.__Precio = Precio

    @property
    def Cantidad(self):
        return self.__Cantidad
    @Cantidad.setter
    def Cantidad(self, Cantidad: int):
        self.__Cantidad = Cantidad

    @property
    def venta48(self):
        return self.__venta48
    @venta48.setter
    def venta48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Producto__venta48", None)
        self.__venta48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "producto49"):
                opp_val = getattr(old_value, "producto49", None)
                if opp_val == self:
                    setattr(old_value, "producto49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "producto49"):
                opp_val = getattr(value, "producto49", None)
                setattr(value, "producto49", self)

    @property
    def impuesto53(self):
        return self.__impuesto53
    @impuesto53.setter
    def impuesto53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Producto__impuesto53", None)
        self.__impuesto53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "producto52"):
                opp_val = getattr(old_value, "producto52", None)
                if opp_val == self:
                    setattr(old_value, "producto52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "producto52"):
                opp_val = getattr(value, "producto52", None)
                setattr(value, "producto52", self)



class Venta:

    def __init__(self, Codigo: int, Fecha: str, RealizarVenta: str, producto49: "Producto" = None, impuesto51: "Impuesto" = None):
        self.Codigo = Codigo
        self.Fecha = Fecha
        self.RealizarVenta = RealizarVenta
        self.producto49 = producto49
        self.impuesto51 = impuesto51
        
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
    def Codigo(self, Codigo: int):
        self.__Codigo = Codigo

    @property
    def RealizarVenta(self):
        return self.__RealizarVenta
    @RealizarVenta.setter
    def RealizarVenta(self, RealizarVenta: str):
        self.__RealizarVenta = RealizarVenta

    @property
    def impuesto51(self):
        return self.__impuesto51
    @impuesto51.setter
    def impuesto51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Venta__impuesto51", None)
        self.__impuesto51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "venta50"):
                opp_val = getattr(old_value, "venta50", None)
                if opp_val == self:
                    setattr(old_value, "venta50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "venta50"):
                opp_val = getattr(value, "venta50", None)
                setattr(value, "venta50", self)

    @property
    def producto49(self):
        return self.__producto49
    @producto49.setter
    def producto49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Venta__producto49", None)
        self.__producto49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "venta48"):
                opp_val = getattr(old_value, "venta48", None)
                if opp_val == self:
                    setattr(old_value, "venta48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "venta48"):
                opp_val = getattr(value, "venta48", None)
                setattr(value, "venta48", self)



class Javaaplication:

    pass


class Calcular:

    pass


class Servidor_BD_Node:

    pass


class LogicaPresentacion___Factura_Component:

    pass


class Servidor_WEB_Node:

    pass


class Persistencia___Factura_Component:

    pass


class Servidor_Intel__Node:

    pass


class Programa:

    def __init__(self, Codigo: int, Nombre: str, pemsum_Universitario45: "Pemsum_Universitario" = None):
        self.Codigo = Codigo
        self.Nombre = Nombre
        self.pemsum_Universitario45 = pemsum_Universitario45
        
        pass
    @property
    def Codigo(self):
        return self.__Codigo
    @Codigo.setter
    def Codigo(self, Codigo: int):
        self.__Codigo = Codigo

    @property
    def Nombre(self):
        return self.__Nombre
    @Nombre.setter
    def Nombre(self, Nombre: str):
        self.__Nombre = Nombre

    @property
    def pemsum_Universitario45(self):
        return self.__pemsum_Universitario45
    @pemsum_Universitario45.setter
    def pemsum_Universitario45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Programa__pemsum_Universitario45", None)
        self.__pemsum_Universitario45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "programa44"):
                opp_val = getattr(old_value, "programa44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "programa44"):
                opp_val = getattr(value, "programa44", None)
                if opp_val is None:
                    setattr(value, "programa44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Creditos:

    def __init__(self, Numeros: int, materias30: "Materias" = None, asignacion_de_creditos42: set["asignacion_de_creditos"] = None):
        self.Numeros = Numeros
        self.materias30 = materias30
        self.asignacion_de_creditos42 = asignacion_de_creditos42 if asignacion_de_creditos42 is not None else set()
        
        pass
    @property
    def Numeros(self):
        return self.__Numeros
    @Numeros.setter
    def Numeros(self, Numeros: int):
        self.__Numeros = Numeros

    @property
    def asignacion_de_creditos42(self):
        return self.__asignacion_de_creditos42
    @asignacion_de_creditos42.setter
    def asignacion_de_creditos42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Creditos__asignacion_de_creditos42", None)
        self.__asignacion_de_creditos42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "creditos43"):
                    opp_val = getattr(item, "creditos43", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "creditos43"):
                    opp_val = getattr(item, "creditos43", None)
                    
                    if opp_val is None:
                        setattr(item, "creditos43", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def materias30(self):
        return self.__materias30
    @materias30.setter
    def materias30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Creditos__materias30", None)
        self.__materias30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "creditos31"):
                opp_val = getattr(old_value, "creditos31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "creditos31"):
                opp_val = getattr(value, "creditos31", None)
                if opp_val is None:
                    setattr(value, "creditos31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Areas_del_Conocimiento:

    def __init__(self, NombreArea: str, Departamentos: str, pemsum_Universitario37: "Pemsum_Universitario" = None, asignacion_de_creditos39: set["asignacion_de_creditos"] = None):
        self.NombreArea = NombreArea
        self.Departamentos = Departamentos
        self.pemsum_Universitario37 = pemsum_Universitario37
        self.asignacion_de_creditos39 = asignacion_de_creditos39 if asignacion_de_creditos39 is not None else set()
        
        pass
    @property
    def Departamentos(self):
        return self.__Departamentos
    @Departamentos.setter
    def Departamentos(self, Departamentos: str):
        self.__Departamentos = Departamentos

    @property
    def NombreArea(self):
        return self.__NombreArea
    @NombreArea.setter
    def NombreArea(self, NombreArea: str):
        self.__NombreArea = NombreArea

    @property
    def pemsum_Universitario37(self):
        return self.__pemsum_Universitario37
    @pemsum_Universitario37.setter
    def pemsum_Universitario37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Areas_del_Conocimiento__pemsum_Universitario37", None)
        self.__pemsum_Universitario37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "areas_del_Conocimiento36"):
                opp_val = getattr(old_value, "areas_del_Conocimiento36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "areas_del_Conocimiento36"):
                opp_val = getattr(value, "areas_del_Conocimiento36", None)
                if opp_val is None:
                    setattr(value, "areas_del_Conocimiento36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def asignacion_de_creditos39(self):
        return self.__asignacion_de_creditos39
    @asignacion_de_creditos39.setter
    def asignacion_de_creditos39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Areas_del_Conocimiento__asignacion_de_creditos39", None)
        self.__asignacion_de_creditos39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "areas_del_Conocimiento38"):
                    opp_val = getattr(item, "areas_del_Conocimiento38", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "areas_del_Conocimiento38"):
                    opp_val = getattr(item, "areas_del_Conocimiento38", None)
                    
                    if opp_val is None:
                        setattr(item, "areas_del_Conocimiento38", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class asignacion_de_creditos:

    def __init__(self, Cod_Materia: int, areas_del_Conocimiento38: set["Areas_del_Conocimiento"] = None, departamento40: "Departamento" = None, creditos43: set["Creditos"] = None):
        self.Cod_Materia = Cod_Materia
        self.areas_del_Conocimiento38 = areas_del_Conocimiento38 if areas_del_Conocimiento38 is not None else set()
        self.departamento40 = departamento40
        self.creditos43 = creditos43 if creditos43 is not None else set()
        
        pass
    @property
    def Cod_Materia(self):
        return self.__Cod_Materia
    @Cod_Materia.setter
    def Cod_Materia(self, Cod_Materia: int):
        self.__Cod_Materia = Cod_Materia

    @property
    def creditos43(self):
        return self.__creditos43
    @creditos43.setter
    def creditos43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asignacion_de_creditos__creditos43", None)
        self.__creditos43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "asignacion_de_creditos42"):
                    opp_val = getattr(item, "asignacion_de_creditos42", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "asignacion_de_creditos42"):
                    opp_val = getattr(item, "asignacion_de_creditos42", None)
                    
                    if opp_val is None:
                        setattr(item, "asignacion_de_creditos42", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def departamento40(self):
        return self.__departamento40
    @departamento40.setter
    def departamento40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asignacion_de_creditos__departamento40", None)
        self.__departamento40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "asignacion_de_creditos41"):
                opp_val = getattr(old_value, "asignacion_de_creditos41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "asignacion_de_creditos41"):
                opp_val = getattr(value, "asignacion_de_creditos41", None)
                if opp_val is None:
                    setattr(value, "asignacion_de_creditos41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def areas_del_Conocimiento38(self):
        return self.__areas_del_Conocimiento38
    @areas_del_Conocimiento38.setter
    def areas_del_Conocimiento38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asignacion_de_creditos__areas_del_Conocimiento38", None)
        self.__areas_del_Conocimiento38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "asignacion_de_creditos39"):
                    opp_val = getattr(item, "asignacion_de_creditos39", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "asignacion_de_creditos39"):
                    opp_val = getattr(item, "asignacion_de_creditos39", None)
                    
                    if opp_val is None:
                        setattr(item, "asignacion_de_creditos39", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Horas_de_clase:

    def __init__(self, CreditosMateria: str, TipoCreditos: str, materias33: "Materias" = None):
        self.CreditosMateria = CreditosMateria
        self.TipoCreditos = TipoCreditos
        self.materias33 = materias33
        
        pass
    @property
    def CreditosMateria(self):
        return self.__CreditosMateria
    @CreditosMateria.setter
    def CreditosMateria(self, CreditosMateria: str):
        self.__CreditosMateria = CreditosMateria

    @property
    def TipoCreditos(self):
        return self.__TipoCreditos
    @TipoCreditos.setter
    def TipoCreditos(self, TipoCreditos: str):
        self.__TipoCreditos = TipoCreditos

    @property
    def materias33(self):
        return self.__materias33
    @materias33.setter
    def materias33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Horas_de_clase__materias33", None)
        self.__materias33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "horas_de_clase32"):
                opp_val = getattr(old_value, "horas_de_clase32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "horas_de_clase32"):
                opp_val = getattr(value, "horas_de_clase32", None)
                if opp_val is None:
                    setattr(value, "horas_de_clase32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Profesor:

    def __init__(self, ID: int, Nombre: str, Apellido: str, Area: str, materias28: set["Materias"] = None):
        self.ID = ID
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Area = Area
        self.materias28 = materias28 if materias28 is not None else set()
        
        pass
    @property
    def Nombre(self):
        return self.__Nombre
    @Nombre.setter
    def Nombre(self, Nombre: str):
        self.__Nombre = Nombre

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def Apellido(self):
        return self.__Apellido
    @Apellido.setter
    def Apellido(self, Apellido: str):
        self.__Apellido = Apellido

    @property
    def Area(self):
        return self.__Area
    @Area.setter
    def Area(self, Area: str):
        self.__Area = Area

    @property
    def materias28(self):
        return self.__materias28
    @materias28.setter
    def materias28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Profesor__materias28", None)
        self.__materias28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "profesores29"):
                    opp_val = getattr(item, "profesores29", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "profesores29"):
                    opp_val = getattr(item, "profesores29", None)
                    
                    if opp_val is None:
                        setattr(item, "profesores29", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Departamento:

    def __init__(self, ID_Profesores: int, pemsum_Universitario35: "Pemsum_Universitario" = None, asignacion_de_creditos41: set["asignacion_de_creditos"] = None):
        self.ID_Profesores = ID_Profesores
        self.pemsum_Universitario35 = pemsum_Universitario35
        self.asignacion_de_creditos41 = asignacion_de_creditos41 if asignacion_de_creditos41 is not None else set()
        
        pass
    @property
    def ID_Profesores(self):
        return self.__ID_Profesores
    @ID_Profesores.setter
    def ID_Profesores(self, ID_Profesores: int):
        self.__ID_Profesores = ID_Profesores

    @property
    def pemsum_Universitario35(self):
        return self.__pemsum_Universitario35
    @pemsum_Universitario35.setter
    def pemsum_Universitario35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Departamento__pemsum_Universitario35", None)
        self.__pemsum_Universitario35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "departamento34"):
                opp_val = getattr(old_value, "departamento34", None)
                if opp_val == self:
                    setattr(old_value, "departamento34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "departamento34"):
                opp_val = getattr(value, "departamento34", None)
                setattr(value, "departamento34", self)

    @property
    def asignacion_de_creditos41(self):
        return self.__asignacion_de_creditos41
    @asignacion_de_creditos41.setter
    def asignacion_de_creditos41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Departamento__asignacion_de_creditos41", None)
        self.__asignacion_de_creditos41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "departamento40"):
                    opp_val = getattr(item, "departamento40", None)
                    
                    if opp_val == self:
                        setattr(item, "departamento40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "departamento40"):
                    opp_val = getattr(item, "departamento40", None)
                    
                    setattr(item, "departamento40", self)
                    



class Materias:

    def __init__(self, Codigo: int, Tipo: str, Creditos: int, Nombre: str, pemsum_Universitario26: "Pemsum_Universitario" = None, profesores29: set["Profesor"] = None, creditos31: set["Creditos"] = None, horas_de_clase32: set["Horas_de_clase"] = None):
        self.Codigo = Codigo
        self.Tipo = Tipo
        self.Creditos = Creditos
        self.Nombre = Nombre
        self.pemsum_Universitario26 = pemsum_Universitario26
        self.profesores29 = profesores29 if profesores29 is not None else set()
        self.creditos31 = creditos31 if creditos31 is not None else set()
        self.horas_de_clase32 = horas_de_clase32 if horas_de_clase32 is not None else set()
        
        pass
    @property
    def Codigo(self):
        return self.__Codigo
    @Codigo.setter
    def Codigo(self, Codigo: int):
        self.__Codigo = Codigo

    @property
    def Tipo(self):
        return self.__Tipo
    @Tipo.setter
    def Tipo(self, Tipo: str):
        self.__Tipo = Tipo

    @property
    def Nombre(self):
        return self.__Nombre
    @Nombre.setter
    def Nombre(self, Nombre: str):
        self.__Nombre = Nombre

    @property
    def Creditos(self):
        return self.__Creditos
    @Creditos.setter
    def Creditos(self, Creditos: int):
        self.__Creditos = Creditos

    @property
    def horas_de_clase32(self):
        return self.__horas_de_clase32
    @horas_de_clase32.setter
    def horas_de_clase32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Materias__horas_de_clase32", None)
        self.__horas_de_clase32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "materias33"):
                    opp_val = getattr(item, "materias33", None)
                    
                    if opp_val == self:
                        setattr(item, "materias33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "materias33"):
                    opp_val = getattr(item, "materias33", None)
                    
                    setattr(item, "materias33", self)
                    

    @property
    def creditos31(self):
        return self.__creditos31
    @creditos31.setter
    def creditos31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Materias__creditos31", None)
        self.__creditos31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "materias30"):
                    opp_val = getattr(item, "materias30", None)
                    
                    if opp_val == self:
                        setattr(item, "materias30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "materias30"):
                    opp_val = getattr(item, "materias30", None)
                    
                    setattr(item, "materias30", self)
                    

    @property
    def profesores29(self):
        return self.__profesores29
    @profesores29.setter
    def profesores29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Materias__profesores29", None)
        self.__profesores29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "materias28"):
                    opp_val = getattr(item, "materias28", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "materias28"):
                    opp_val = getattr(item, "materias28", None)
                    
                    if opp_val is None:
                        setattr(item, "materias28", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def pemsum_Universitario26(self):
        return self.__pemsum_Universitario26
    @pemsum_Universitario26.setter
    def pemsum_Universitario26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Materias__pemsum_Universitario26", None)
        self.__pemsum_Universitario26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "materias27"):
                opp_val = getattr(old_value, "materias27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "materias27"):
                opp_val = getattr(value, "materias27", None)
                if opp_val is None:
                    setattr(value, "materias27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Pemsum_Universitario:

    def __init__(self, Materias: str, Programa: str, materias27: set["Materias"] = None, departamento34: "Departamento" = None, areas_del_Conocimiento36: set["Areas_del_Conocimiento"] = None, programa44: set["Programa"] = None):
        self.Materias = Materias
        self.Programa = Programa
        self.materias27 = materias27 if materias27 is not None else set()
        self.departamento34 = departamento34
        self.areas_del_Conocimiento36 = areas_del_Conocimiento36 if areas_del_Conocimiento36 is not None else set()
        self.programa44 = programa44 if programa44 is not None else set()
        
        pass
    @property
    def Materias(self):
        return self.__Materias
    @Materias.setter
    def Materias(self, Materias: str):
        self.__Materias = Materias

    @property
    def Programa(self):
        return self.__Programa
    @Programa.setter
    def Programa(self, Programa: str):
        self.__Programa = Programa

    @property
    def materias27(self):
        return self.__materias27
    @materias27.setter
    def materias27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pemsum_Universitario__materias27", None)
        self.__materias27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pemsum_Universitario26"):
                    opp_val = getattr(item, "pemsum_Universitario26", None)
                    
                    if opp_val == self:
                        setattr(item, "pemsum_Universitario26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pemsum_Universitario26"):
                    opp_val = getattr(item, "pemsum_Universitario26", None)
                    
                    setattr(item, "pemsum_Universitario26", self)
                    

    @property
    def programa44(self):
        return self.__programa44
    @programa44.setter
    def programa44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pemsum_Universitario__programa44", None)
        self.__programa44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pemsum_Universitario45"):
                    opp_val = getattr(item, "pemsum_Universitario45", None)
                    
                    if opp_val == self:
                        setattr(item, "pemsum_Universitario45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pemsum_Universitario45"):
                    opp_val = getattr(item, "pemsum_Universitario45", None)
                    
                    setattr(item, "pemsum_Universitario45", self)
                    

    @property
    def areas_del_Conocimiento36(self):
        return self.__areas_del_Conocimiento36
    @areas_del_Conocimiento36.setter
    def areas_del_Conocimiento36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pemsum_Universitario__areas_del_Conocimiento36", None)
        self.__areas_del_Conocimiento36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pemsum_Universitario37"):
                    opp_val = getattr(item, "pemsum_Universitario37", None)
                    
                    if opp_val == self:
                        setattr(item, "pemsum_Universitario37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pemsum_Universitario37"):
                    opp_val = getattr(item, "pemsum_Universitario37", None)
                    
                    setattr(item, "pemsum_Universitario37", self)
                    

    @property
    def departamento34(self):
        return self.__departamento34
    @departamento34.setter
    def departamento34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pemsum_Universitario__departamento34", None)
        self.__departamento34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pemsum_Universitario35"):
                opp_val = getattr(old_value, "pemsum_Universitario35", None)
                if opp_val == self:
                    setattr(old_value, "pemsum_Universitario35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pemsum_Universitario35"):
                opp_val = getattr(value, "pemsum_Universitario35", None)
                setattr(value, "pemsum_Universitario35", self)



class Pedidos:

    def __init__(self, Codigo: str, Fecha: str, proveedor12: "Proveedor" = None):
        self.Codigo = Codigo
        self.Fecha = Fecha
        self.proveedor12 = proveedor12
        
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
    def proveedor12(self):
        return self.__proveedor12
    @proveedor12.setter
    def proveedor12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pedidos__proveedor12", None)
        self.__proveedor12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pedidos13"):
                opp_val = getattr(old_value, "pedidos13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pedidos13"):
                opp_val = getattr(value, "pedidos13", None)
                if opp_val is None:
                    setattr(value, "pedidos13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Proveedor:

    def __init__(self, Nit: str, Razonsocial: str, Direccion: str, Telefonos: str, factura23: set["Factura"] = None, ordenesPedidos10: set["OrdenesPedidos"] = None, pedidos13: set["Pedidos"] = None):
        self.Nit = Nit
        self.Razonsocial = Razonsocial
        self.Direccion = Direccion
        self.Telefonos = Telefonos
        self.factura23 = factura23 if factura23 is not None else set()
        self.ordenesPedidos10 = ordenesPedidos10 if ordenesPedidos10 is not None else set()
        self.pedidos13 = pedidos13 if pedidos13 is not None else set()
        
        pass
    @property
    def Nit(self):
        return self.__Nit
    @Nit.setter
    def Nit(self, Nit: str):
        self.__Nit = Nit

    @property
    def Razonsocial(self):
        return self.__Razonsocial
    @Razonsocial.setter
    def Razonsocial(self, Razonsocial: str):
        self.__Razonsocial = Razonsocial

    @property
    def Direccion(self):
        return self.__Direccion
    @Direccion.setter
    def Direccion(self, Direccion: str):
        self.__Direccion = Direccion

    @property
    def Telefonos(self):
        return self.__Telefonos
    @Telefonos.setter
    def Telefonos(self, Telefonos: str):
        self.__Telefonos = Telefonos

    @property
    def pedidos13(self):
        return self.__pedidos13
    @pedidos13.setter
    def pedidos13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Proveedor__pedidos13", None)
        self.__pedidos13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "proveedor12"):
                    opp_val = getattr(item, "proveedor12", None)
                    
                    if opp_val == self:
                        setattr(item, "proveedor12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "proveedor12"):
                    opp_val = getattr(item, "proveedor12", None)
                    
                    setattr(item, "proveedor12", self)
                    

    @property
    def factura23(self):
        return self.__factura23
    @factura23.setter
    def factura23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Proveedor__factura23", None)
        self.__factura23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "proveedor22"):
                    opp_val = getattr(item, "proveedor22", None)
                    
                    if opp_val == self:
                        setattr(item, "proveedor22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "proveedor22"):
                    opp_val = getattr(item, "proveedor22", None)
                    
                    setattr(item, "proveedor22", self)
                    

    @property
    def ordenesPedidos10(self):
        return self.__ordenesPedidos10
    @ordenesPedidos10.setter
    def ordenesPedidos10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Proveedor__ordenesPedidos10", None)
        self.__ordenesPedidos10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "proveedor11"):
                    opp_val = getattr(item, "proveedor11", None)
                    
                    if opp_val == self:
                        setattr(item, "proveedor11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "proveedor11"):
                    opp_val = getattr(item, "proveedor11", None)
                    
                    setattr(item, "proveedor11", self)
                    



class SolicitudSuministro:

    def __init__(self, Codigo: str, Fecha: str, eLementos16: set["ELementos"] = None, ordenesPedidos18: "OrdenesPedidos" = None, dependencia21: "Dependencia" = None):
        self.Codigo = Codigo
        self.Fecha = Fecha
        self.eLementos16 = eLementos16 if eLementos16 is not None else set()
        self.ordenesPedidos18 = ordenesPedidos18
        self.dependencia21 = dependencia21
        
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
    def dependencia21(self):
        return self.__dependencia21
    @dependencia21.setter
    def dependencia21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SolicitudSuministro__dependencia21", None)
        self.__dependencia21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "solicitudSuministro20"):
                opp_val = getattr(old_value, "solicitudSuministro20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "solicitudSuministro20"):
                opp_val = getattr(value, "solicitudSuministro20", None)
                if opp_val is None:
                    setattr(value, "solicitudSuministro20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ordenesPedidos18(self):
        return self.__ordenesPedidos18
    @ordenesPedidos18.setter
    def ordenesPedidos18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SolicitudSuministro__ordenesPedidos18", None)
        self.__ordenesPedidos18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "solicitudSuministro19"):
                opp_val = getattr(old_value, "solicitudSuministro19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "solicitudSuministro19"):
                opp_val = getattr(value, "solicitudSuministro19", None)
                if opp_val is None:
                    setattr(value, "solicitudSuministro19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eLementos16(self):
        return self.__eLementos16
    @eLementos16.setter
    def eLementos16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SolicitudSuministro__eLementos16", None)
        self.__eLementos16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "solicitudSuministro17"):
                    opp_val = getattr(item, "solicitudSuministro17", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "solicitudSuministro17"):
                    opp_val = getattr(item, "solicitudSuministro17", None)
                    
                    if opp_val is None:
                        setattr(item, "solicitudSuministro17", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Dependencia:

    def __init__(self, Codigo: str, Nombre: str, Responsable: str, solicitudSuministro20: set["SolicitudSuministro"] = None):
        self.Codigo = Codigo
        self.Nombre = Nombre
        self.Responsable = Responsable
        self.solicitudSuministro20 = solicitudSuministro20 if solicitudSuministro20 is not None else set()
        
        pass
    @property
    def Codigo(self):
        return self.__Codigo
    @Codigo.setter
    def Codigo(self, Codigo: str):
        self.__Codigo = Codigo

    @property
    def Nombre(self):
        return self.__Nombre
    @Nombre.setter
    def Nombre(self, Nombre: str):
        self.__Nombre = Nombre

    @property
    def Responsable(self):
        return self.__Responsable
    @Responsable.setter
    def Responsable(self, Responsable: str):
        self.__Responsable = Responsable

    @property
    def solicitudSuministro20(self):
        return self.__solicitudSuministro20
    @solicitudSuministro20.setter
    def solicitudSuministro20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dependencia__solicitudSuministro20", None)
        self.__solicitudSuministro20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dependencia21"):
                    opp_val = getattr(item, "dependencia21", None)
                    
                    if opp_val == self:
                        setattr(item, "dependencia21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dependencia21"):
                    opp_val = getattr(item, "dependencia21", None)
                    
                    setattr(item, "dependencia21", self)
                    



class ELementos:

    def __init__(self, REferencia: str, Clasificacion: str, ordenesPedidos15: set["OrdenesPedidos"] = None, solicitudSuministro17: set["SolicitudSuministro"] = None, factura25: set["Factura"] = None):
        self.REferencia = REferencia
        self.Clasificacion = Clasificacion
        self.ordenesPedidos15 = ordenesPedidos15 if ordenesPedidos15 is not None else set()
        self.solicitudSuministro17 = solicitudSuministro17 if solicitudSuministro17 is not None else set()
        self.factura25 = factura25 if factura25 is not None else set()
        
        pass
    @property
    def REferencia(self):
        return self.__REferencia
    @REferencia.setter
    def REferencia(self, REferencia: str):
        self.__REferencia = REferencia

    @property
    def Clasificacion(self):
        return self.__Clasificacion
    @Clasificacion.setter
    def Clasificacion(self, Clasificacion: str):
        self.__Clasificacion = Clasificacion

    @property
    def factura25(self):
        return self.__factura25
    @factura25.setter
    def factura25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ELementos__factura25", None)
        self.__factura25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eLementos24"):
                    opp_val = getattr(item, "eLementos24", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eLementos24"):
                    opp_val = getattr(item, "eLementos24", None)
                    
                    if opp_val is None:
                        setattr(item, "eLementos24", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def solicitudSuministro17(self):
        return self.__solicitudSuministro17
    @solicitudSuministro17.setter
    def solicitudSuministro17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ELementos__solicitudSuministro17", None)
        self.__solicitudSuministro17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eLementos16"):
                    opp_val = getattr(item, "eLementos16", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eLementos16"):
                    opp_val = getattr(item, "eLementos16", None)
                    
                    if opp_val is None:
                        setattr(item, "eLementos16", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def ordenesPedidos15(self):
        return self.__ordenesPedidos15
    @ordenesPedidos15.setter
    def ordenesPedidos15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ELementos__ordenesPedidos15", None)
        self.__ordenesPedidos15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eLementos14"):
                    opp_val = getattr(item, "eLementos14", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eLementos14"):
                    opp_val = getattr(item, "eLementos14", None)
                    
                    if opp_val is None:
                        setattr(item, "eLementos14", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class OrdenesPedidos:

    def __init__(self, Fecha: str, Codigo: str, eLementos14: set["ELementos"] = None, solicitudSuministro19: set["SolicitudSuministro"] = None, proveedor11: "Proveedor" = None):
        self.Fecha = Fecha
        self.Codigo = Codigo
        self.eLementos14 = eLementos14 if eLementos14 is not None else set()
        self.solicitudSuministro19 = solicitudSuministro19 if solicitudSuministro19 is not None else set()
        self.proveedor11 = proveedor11
        
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
    def solicitudSuministro19(self):
        return self.__solicitudSuministro19
    @solicitudSuministro19.setter
    def solicitudSuministro19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrdenesPedidos__solicitudSuministro19", None)
        self.__solicitudSuministro19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ordenesPedidos18"):
                    opp_val = getattr(item, "ordenesPedidos18", None)
                    
                    if opp_val == self:
                        setattr(item, "ordenesPedidos18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ordenesPedidos18"):
                    opp_val = getattr(item, "ordenesPedidos18", None)
                    
                    setattr(item, "ordenesPedidos18", self)
                    

    @property
    def eLementos14(self):
        return self.__eLementos14
    @eLementos14.setter
    def eLementos14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrdenesPedidos__eLementos14", None)
        self.__eLementos14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ordenesPedidos15"):
                    opp_val = getattr(item, "ordenesPedidos15", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ordenesPedidos15"):
                    opp_val = getattr(item, "ordenesPedidos15", None)
                    
                    if opp_val is None:
                        setattr(item, "ordenesPedidos15", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def proveedor11(self):
        return self.__proveedor11
    @proveedor11.setter
    def proveedor11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrdenesPedidos__proveedor11", None)
        self.__proveedor11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ordenesPedidos10"):
                opp_val = getattr(old_value, "ordenesPedidos10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ordenesPedidos10"):
                opp_val = getattr(value, "ordenesPedidos10", None)
                if opp_val is None:
                    setattr(value, "ordenesPedidos10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Component_Component:

    pass


class Departamento_de_inventarios_y_suministros___DIS_Component:

    pass


class Millenium_S_A_Component:

    pass


class Brindar_Consultoria_external:

    pass
