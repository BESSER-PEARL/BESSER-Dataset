from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class caninos3:

    def __init__(self, nombre: str, raza: str, edad: str, peso: str, altura: str, observaciones: str, veterinaria_caninos4_115: set["veterinaria3"] = None):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.altura = altura
        self.observaciones = observaciones
        self.veterinaria_caninos4_115 = veterinaria_caninos4_115 if veterinaria_caninos4_115 is not None else set()
        
        pass
    @property
    def altura(self):
        return self.__altura
    @altura.setter
    def altura(self, altura: str):
        self.__altura = altura

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def peso(self):
        return self.__peso
    @peso.setter
    def peso(self, peso: str):
        self.__peso = peso

    @property
    def raza(self):
        return self.__raza
    @raza.setter
    def raza(self, raza: str):
        self.__raza = raza

    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, edad: str):
        self.__edad = edad

    @property
    def observaciones(self):
        return self.__observaciones
    @observaciones.setter
    def observaciones(self, observaciones: str):
        self.__observaciones = observaciones

    @property
    def veterinaria_caninos4_115(self):
        return self.__veterinaria_caninos4_115
    @veterinaria_caninos4_115.setter
    def veterinaria_caninos4_115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caninos3__veterinaria_caninos4_115", None)
        self.__veterinaria_caninos4_115 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "caninos14"):
                    opp_val = getattr(item, "caninos14", None)
                    
                    if opp_val == self:
                        setattr(item, "caninos14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "caninos14"):
                    opp_val = getattr(item, "caninos14", None)
                    
                    setattr(item, "caninos14", self)
                    



class veterinaria3:

    def __init__(self, _attr: str, caninos14: "caninos3" = None):
        self._attr = _attr
        self.caninos14 = caninos14
        
        pass
    @property
    def _attr(self):
        return self.___attr
    @_attr.setter
    def _attr(self, _attr: str):
        self.___attr = _attr

    @property
    def caninos14(self):
        return self.__caninos14
    @caninos14.setter
    def caninos14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_veterinaria3__caninos14", None)
        self.__caninos14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "veterinaria_caninos4_115"):
                opp_val = getattr(old_value, "veterinaria_caninos4_115", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "veterinaria_caninos4_115"):
                opp_val = getattr(value, "veterinaria_caninos4_115", None)
                if opp_val is None:
                    setattr(value, "veterinaria_caninos4_115", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class caninos2:

    def __init__(self, nombre: str, raza: str, edad: str, peso: str, altura: str, observaciones: str, veterinaria_caninos3_113: set["veterinaria2"] = None):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.altura = altura
        self.observaciones = observaciones
        self.veterinaria_caninos3_113 = veterinaria_caninos3_113 if veterinaria_caninos3_113 is not None else set()
        
        pass
    @property
    def raza(self):
        return self.__raza
    @raza.setter
    def raza(self, raza: str):
        self.__raza = raza

    @property
    def altura(self):
        return self.__altura
    @altura.setter
    def altura(self, altura: str):
        self.__altura = altura

    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, edad: str):
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def peso(self):
        return self.__peso
    @peso.setter
    def peso(self, peso: str):
        self.__peso = peso

    @property
    def observaciones(self):
        return self.__observaciones
    @observaciones.setter
    def observaciones(self, observaciones: str):
        self.__observaciones = observaciones

    @property
    def veterinaria_caninos3_113(self):
        return self.__veterinaria_caninos3_113
    @veterinaria_caninos3_113.setter
    def veterinaria_caninos3_113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caninos2__veterinaria_caninos3_113", None)
        self.__veterinaria_caninos3_113 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "caninos12"):
                    opp_val = getattr(item, "caninos12", None)
                    
                    if opp_val == self:
                        setattr(item, "caninos12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "caninos12"):
                    opp_val = getattr(item, "caninos12", None)
                    
                    setattr(item, "caninos12", self)
                    



class veterinaria2:

    def __init__(self, _: str, caninos12: "caninos2" = None):
        self._ = _
        self.caninos12 = caninos12
        
        pass
    @property
    def _(self):
        return self.___
    @_.setter
    def _(self, _: str):
        self.___ = _

    @property
    def caninos12(self):
        return self.__caninos12
    @caninos12.setter
    def caninos12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_veterinaria2__caninos12", None)
        self.__caninos12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "veterinaria_caninos3_113"):
                opp_val = getattr(old_value, "veterinaria_caninos3_113", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "veterinaria_caninos3_113"):
                opp_val = getattr(value, "veterinaria_caninos3_113", None)
                if opp_val is None:
                    setattr(value, "veterinaria_caninos3_113", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class caninos1:

    def __init__(self, nombre: str, raza: str, edad: str, peso: str, altura: str, obsercaciones: str, veterinaria_caninos_111: set["veterinaria1"] = None):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.altura = altura
        self.obsercaciones = obsercaciones
        self.veterinaria_caninos_111 = veterinaria_caninos_111 if veterinaria_caninos_111 is not None else set()
        
        pass
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def obsercaciones(self):
        return self.__obsercaciones
    @obsercaciones.setter
    def obsercaciones(self, obsercaciones: str):
        self.__obsercaciones = obsercaciones

    @property
    def raza(self):
        return self.__raza
    @raza.setter
    def raza(self, raza: str):
        self.__raza = raza

    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, edad: str):
        self.__edad = edad

    @property
    def altura(self):
        return self.__altura
    @altura.setter
    def altura(self, altura: str):
        self.__altura = altura

    @property
    def peso(self):
        return self.__peso
    @peso.setter
    def peso(self, peso: str):
        self.__peso = peso

    @property
    def veterinaria_caninos_111(self):
        return self.__veterinaria_caninos_111
    @veterinaria_caninos_111.setter
    def veterinaria_caninos_111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caninos1__veterinaria_caninos_111", None)
        self.__veterinaria_caninos_111 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "caninos10"):
                    opp_val = getattr(item, "caninos10", None)
                    
                    if opp_val == self:
                        setattr(item, "caninos10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "caninos10"):
                    opp_val = getattr(item, "caninos10", None)
                    
                    setattr(item, "caninos10", self)
                    



class veterinaria1:

    pass


class caninos:

    def __init__(self, nombre: str, raza: str, edad: str, peso: str, altura: str, observaciones: str, veterinaria_caninos2_19: set["veterinaria"] = None):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.altura = altura
        self.observaciones = observaciones
        self.veterinaria_caninos2_19 = veterinaria_caninos2_19 if veterinaria_caninos2_19 is not None else set()
        
        pass
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def peso(self):
        return self.__peso
    @peso.setter
    def peso(self, peso: str):
        self.__peso = peso

    @property
    def raza(self):
        return self.__raza
    @raza.setter
    def raza(self, raza: str):
        self.__raza = raza

    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, edad: str):
        self.__edad = edad

    @property
    def observaciones(self):
        return self.__observaciones
    @observaciones.setter
    def observaciones(self, observaciones: str):
        self.__observaciones = observaciones

    @property
    def altura(self):
        return self.__altura
    @altura.setter
    def altura(self, altura: str):
        self.__altura = altura

    @property
    def veterinaria_caninos2_19(self):
        return self.__veterinaria_caninos2_19
    @veterinaria_caninos2_19.setter
    def veterinaria_caninos2_19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caninos__veterinaria_caninos2_19", None)
        self.__veterinaria_caninos2_19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Caninos8"):
                    opp_val = getattr(item, "Caninos8", None)
                    
                    if opp_val == self:
                        setattr(item, "Caninos8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Caninos8"):
                    opp_val = getattr(item, "Caninos8", None)
                    
                    setattr(item, "Caninos8", self)
                    



class veterinaria:

    pass


class _1:

    pass


class producto:

    def __init__(self, cantidadVendida: str, precioVenta: str, PAPELERIA: str, SUPERMERCADO: str, DROGUERIA: str, IVA_PAPELERIA: str, IVA_SUPERMERCADO: str, IVA_DROGUERIA: str, nombre: str, tipo: str, cantidadBodega: str, cantidadMinima: str, tienda0: "Tienda" = None, tienda2: "Tienda" = None, tienda4: "Tienda" = None, tienda6: "Tienda" = None):
        self.cantidadVendida = cantidadVendida
        self.precioVenta = precioVenta
        self.PAPELERIA = PAPELERIA
        self.SUPERMERCADO = SUPERMERCADO
        self.DROGUERIA = DROGUERIA
        self.IVA_PAPELERIA = IVA_PAPELERIA
        self.IVA_SUPERMERCADO = IVA_SUPERMERCADO
        self.IVA_DROGUERIA = IVA_DROGUERIA
        self.nombre = nombre
        self.tipo = tipo
        self.cantidadBodega = cantidadBodega
        self.cantidadMinima = cantidadMinima
        self.tienda0 = tienda0
        self.tienda2 = tienda2
        self.tienda4 = tienda4
        self.tienda6 = tienda6
        
        pass
    @property
    def IVA_PAPELERIA(self):
        return self.__IVA_PAPELERIA
    @IVA_PAPELERIA.setter
    def IVA_PAPELERIA(self, IVA_PAPELERIA: str):
        self.__IVA_PAPELERIA = IVA_PAPELERIA

    @property
    def DROGUERIA(self):
        return self.__DROGUERIA
    @DROGUERIA.setter
    def DROGUERIA(self, DROGUERIA: str):
        self.__DROGUERIA = DROGUERIA

    @property
    def PAPELERIA(self):
        return self.__PAPELERIA
    @PAPELERIA.setter
    def PAPELERIA(self, PAPELERIA: str):
        self.__PAPELERIA = PAPELERIA

    @property
    def SUPERMERCADO(self):
        return self.__SUPERMERCADO
    @SUPERMERCADO.setter
    def SUPERMERCADO(self, SUPERMERCADO: str):
        self.__SUPERMERCADO = SUPERMERCADO

    @property
    def cantidadMinima(self):
        return self.__cantidadMinima
    @cantidadMinima.setter
    def cantidadMinima(self, cantidadMinima: str):
        self.__cantidadMinima = cantidadMinima

    @property
    def IVA_SUPERMERCADO(self):
        return self.__IVA_SUPERMERCADO
    @IVA_SUPERMERCADO.setter
    def IVA_SUPERMERCADO(self, IVA_SUPERMERCADO: str):
        self.__IVA_SUPERMERCADO = IVA_SUPERMERCADO

    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self, tipo: str):
        self.__tipo = tipo

    @property
    def IVA_DROGUERIA(self):
        return self.__IVA_DROGUERIA
    @IVA_DROGUERIA.setter
    def IVA_DROGUERIA(self, IVA_DROGUERIA: str):
        self.__IVA_DROGUERIA = IVA_DROGUERIA

    @property
    def precioVenta(self):
        return self.__precioVenta
    @precioVenta.setter
    def precioVenta(self, precioVenta: str):
        self.__precioVenta = precioVenta

    @property
    def cantidadVendida(self):
        return self.__cantidadVendida
    @cantidadVendida.setter
    def cantidadVendida(self, cantidadVendida: str):
        self.__cantidadVendida = cantidadVendida

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def cantidadBodega(self):
        return self.__cantidadBodega
    @cantidadBodega.setter
    def cantidadBodega(self, cantidadBodega: str):
        self.__cantidadBodega = cantidadBodega

    @property
    def tienda6(self):
        return self.__tienda6
    @tienda6.setter
    def tienda6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_producto__tienda6", None)
        self.__tienda6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "producto47"):
                opp_val = getattr(old_value, "producto47", None)
                if opp_val == self:
                    setattr(old_value, "producto47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "producto47"):
                opp_val = getattr(value, "producto47", None)
                setattr(value, "producto47", self)

    @property
    def tienda2(self):
        return self.__tienda2
    @tienda2.setter
    def tienda2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_producto__tienda2", None)
        self.__tienda2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "producto33"):
                opp_val = getattr(old_value, "producto33", None)
                if opp_val == self:
                    setattr(old_value, "producto33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "producto33"):
                opp_val = getattr(value, "producto33", None)
                setattr(value, "producto33", self)

    @property
    def tienda0(self):
        return self.__tienda0
    @tienda0.setter
    def tienda0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_producto__tienda0", None)
        self.__tienda0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "producto21"):
                opp_val = getattr(old_value, "producto21", None)
                if opp_val == self:
                    setattr(old_value, "producto21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "producto21"):
                opp_val = getattr(value, "producto21", None)
                setattr(value, "producto21", self)

    @property
    def tienda4(self):
        return self.__tienda4
    @tienda4.setter
    def tienda4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_producto__tienda4", None)
        self.__tienda4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "producto15"):
                opp_val = getattr(old_value, "producto15", None)
                if opp_val == self:
                    setattr(old_value, "producto15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "producto15"):
                opp_val = getattr(value, "producto15", None)
                setattr(value, "producto15", self)



class Tienda:

    def __init__(self, Tienda: str, getProducto1: str, getProducto2: str, getProducto3: str, getProducto4: str, producto21: "producto" = None, producto33: "producto" = None, producto15: "producto" = None, producto47: "producto" = None):
        self.Tienda = Tienda
        self.getProducto1 = getProducto1
        self.getProducto2 = getProducto2
        self.getProducto3 = getProducto3
        self.getProducto4 = getProducto4
        self.producto21 = producto21
        self.producto33 = producto33
        self.producto15 = producto15
        self.producto47 = producto47
        
        pass
    @property
    def getProducto3(self):
        return self.__getProducto3
    @getProducto3.setter
    def getProducto3(self, getProducto3: str):
        self.__getProducto3 = getProducto3

    @property
    def getProducto4(self):
        return self.__getProducto4
    @getProducto4.setter
    def getProducto4(self, getProducto4: str):
        self.__getProducto4 = getProducto4

    @property
    def getProducto2(self):
        return self.__getProducto2
    @getProducto2.setter
    def getProducto2(self, getProducto2: str):
        self.__getProducto2 = getProducto2

    @property
    def Tienda(self):
        return self.__Tienda
    @Tienda.setter
    def Tienda(self, Tienda: str):
        self.__Tienda = Tienda

    @property
    def getProducto1(self):
        return self.__getProducto1
    @getProducto1.setter
    def getProducto1(self, getProducto1: str):
        self.__getProducto1 = getProducto1

    @property
    def producto33(self):
        return self.__producto33
    @producto33.setter
    def producto33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Tienda__producto33", None)
        self.__producto33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tienda2"):
                opp_val = getattr(old_value, "tienda2", None)
                if opp_val == self:
                    setattr(old_value, "tienda2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tienda2"):
                opp_val = getattr(value, "tienda2", None)
                setattr(value, "tienda2", self)

    @property
    def producto21(self):
        return self.__producto21
    @producto21.setter
    def producto21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Tienda__producto21", None)
        self.__producto21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tienda0"):
                opp_val = getattr(old_value, "tienda0", None)
                if opp_val == self:
                    setattr(old_value, "tienda0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tienda0"):
                opp_val = getattr(value, "tienda0", None)
                setattr(value, "tienda0", self)

    @property
    def producto15(self):
        return self.__producto15
    @producto15.setter
    def producto15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Tienda__producto15", None)
        self.__producto15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tienda4"):
                opp_val = getattr(old_value, "tienda4", None)
                if opp_val == self:
                    setattr(old_value, "tienda4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tienda4"):
                opp_val = getattr(value, "tienda4", None)
                setattr(value, "tienda4", self)

    @property
    def producto47(self):
        return self.__producto47
    @producto47.setter
    def producto47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Tienda__producto47", None)
        self.__producto47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tienda6"):
                opp_val = getattr(old_value, "tienda6", None)
                if opp_val == self:
                    setattr(old_value, "tienda6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tienda6"):
                opp_val = getattr(value, "tienda6", None)
                setattr(value, "tienda6", self)

