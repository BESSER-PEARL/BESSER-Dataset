from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class ProyectoNuevo_Actor:

    pass


class Calcular_Actor:

    pass


class Responsable_Inventario_Actor:

    pass


class Contabilidad_y_Tesorer_a_Actor:

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





class Revisi_n_de_factura_external:

    pass


class Clasificar_producto_external:

    pass


class Entegar_productos_external:

    pass


class Recibir_ordenes_de_suministro_external:

    pass


class Registrar_proveedores_external:

    pass


class Recibir_productos_o_pedidos_external:

    pass


class Brindar_consultoria_external:

    pass


class Impuesto:

    pass


class Producto:

    pass


class Venta:

    pass


class Principal:

    pass


class NuevoProyecto:

    pass


class Calcular:

    pass


class ConcretBuilderBicicletaDoble:

    pass


class ConcretBuilderBicicletaMasculina:

    pass


class ConcretBuilderBicicletaFemenina:

    pass


class ConcretBuilderBicicletaInfantil:

    pass


class _a__BicicletaBuilder:

    pass


class Director:

    def __init__(self, bicicletaBuilder: _a__BicicletaBuilder, void_construirBicicleta: str):
        self.bicicletaBuilder = bicicletaBuilder
        self.void_construirBicicleta = void_construirBicicleta
        
        pass
    @property
    def void_construirBicicleta(self):
        return self.__void_construirBicicleta
    @void_construirBicicleta.setter
    def void_construirBicicleta(self, void_construirBicicleta: str):
        self.__void_construirBicicleta = void_construirBicicleta

    @property
    def bicicletaBuilder(self):
        return self.__bicicletaBuilder
    @bicicletaBuilder.setter
    def bicicletaBuilder(self, bicicletaBuilder: _a__BicicletaBuilder):
        self.__bicicletaBuilder = bicicletaBuilder



class Servidor_intel_I8_Node:

    pass


class Autores:

    def __init__(self, fechaCreaci_n: str, fechamodificaci_n: str, fechaEliminaci_n: str, documentos33: set["Documentos"] = None):
        self.fechaCreaci_n = fechaCreaci_n
        self.fechamodificaci_n = fechamodificaci_n
        self.fechaEliminaci_n = fechaEliminaci_n
        self.documentos33 = documentos33 if documentos33 is not None else set()
        
        pass
    @property
    def fechamodificaci_n(self):
        return self.__fechamodificaci_n
    @fechamodificaci_n.setter
    def fechamodificaci_n(self, fechamodificaci_n: str):
        self.__fechamodificaci_n = fechamodificaci_n

    @property
    def fechaEliminaci_n(self):
        return self.__fechaEliminaci_n
    @fechaEliminaci_n.setter
    def fechaEliminaci_n(self, fechaEliminaci_n: str):
        self.__fechaEliminaci_n = fechaEliminaci_n

    @property
    def fechaCreaci_n(self):
        return self.__fechaCreaci_n
    @fechaCreaci_n.setter
    def fechaCreaci_n(self, fechaCreaci_n: str):
        self.__fechaCreaci_n = fechaCreaci_n

    @property
    def documentos33(self):
        return self.__documentos33
    @documentos33.setter
    def documentos33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Autores__documentos33", None)
        self.__documentos33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "autores232"):
                    opp_val = getattr(item, "autores232", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "autores232"):
                    opp_val = getattr(item, "autores232", None)
                    
                    if opp_val is None:
                        setattr(item, "autores232", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Editoriales:

    def __init__(self, direcci_nEmail: str, direcci_nF_sica: str, n_meroTel_fono: str, personaContacto: str, documentos39: set["Documentos"] = None):
        self.direcci_nEmail = direcci_nEmail
        self.direcci_nF_sica = direcci_nF_sica
        self.n_meroTel_fono = n_meroTel_fono
        self.personaContacto = personaContacto
        self.documentos39 = documentos39 if documentos39 is not None else set()
        
        pass
    @property
    def n_meroTel_fono(self):
        return self.__n_meroTel_fono
    @n_meroTel_fono.setter
    def n_meroTel_fono(self, n_meroTel_fono: str):
        self.__n_meroTel_fono = n_meroTel_fono

    @property
    def direcci_nEmail(self):
        return self.__direcci_nEmail
    @direcci_nEmail.setter
    def direcci_nEmail(self, direcci_nEmail: str):
        self.__direcci_nEmail = direcci_nEmail

    @property
    def direcci_nF_sica(self):
        return self.__direcci_nF_sica
    @direcci_nF_sica.setter
    def direcci_nF_sica(self, direcci_nF_sica: str):
        self.__direcci_nF_sica = direcci_nF_sica

    @property
    def personaContacto(self):
        return self.__personaContacto
    @personaContacto.setter
    def personaContacto(self, personaContacto: str):
        self.__personaContacto = personaContacto

    @property
    def documentos39(self):
        return self.__documentos39
    @documentos39.setter
    def documentos39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Editoriales__documentos39", None)
        self.__documentos39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "editoriales38"):
                    opp_val = getattr(item, "editoriales38", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "editoriales38"):
                    opp_val = getattr(item, "editoriales38", None)
                    
                    if opp_val is None:
                        setattr(item, "editoriales38", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class ArticulosCient_ficos:

    def __init__(self, SSN: str, documentos37: set["Documentos"] = None):
        self.SSN = SSN
        self.documentos37 = documentos37 if documentos37 is not None else set()
        
        pass
    @property
    def SSN(self):
        return self.__SSN
    @SSN.setter
    def SSN(self, SSN: str):
        self.__SSN = SSN

    @property
    def documentos37(self):
        return self.__documentos37
    @documentos37.setter
    def documentos37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ArticulosCient_ficos__documentos37", None)
        self.__documentos37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "articulosCient_ficos36"):
                    opp_val = getattr(item, "articulosCient_ficos36", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "articulosCient_ficos36"):
                    opp_val = getattr(item, "articulosCient_ficos36", None)
                    
                    if opp_val is None:
                        setattr(item, "articulosCient_ficos36", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Ponencias:

    def __init__(self, nombreCongreso: str, documentos41: set["Documentos"] = None):
        self.nombreCongreso = nombreCongreso
        self.documentos41 = documentos41 if documentos41 is not None else set()
        
        pass
    @property
    def nombreCongreso(self):
        return self.__nombreCongreso
    @nombreCongreso.setter
    def nombreCongreso(self, nombreCongreso: str):
        self.__nombreCongreso = nombreCongreso

    @property
    def documentos41(self):
        return self.__documentos41
    @documentos41.setter
    def documentos41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ponencias__documentos41", None)
        self.__documentos41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ponencias40"):
                    opp_val = getattr(item, "ponencias40", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ponencias40"):
                    opp_val = getattr(item, "ponencias40", None)
                    
                    if opp_val is None:
                        setattr(item, "ponencias40", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Libros:

    def __init__(self, n_meroP_ginas: str, documentos35: set["Documentos"] = None):
        self.n_meroP_ginas = n_meroP_ginas
        self.documentos35 = documentos35 if documentos35 is not None else set()
        
        pass
    @property
    def n_meroP_ginas(self):
        return self.__n_meroP_ginas
    @n_meroP_ginas.setter
    def n_meroP_ginas(self, n_meroP_ginas: str):
        self.__n_meroP_ginas = n_meroP_ginas

    @property
    def documentos35(self):
        return self.__documentos35
    @documentos35.setter
    def documentos35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Libros__documentos35", None)
        self.__documentos35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libros34"):
                    opp_val = getattr(item, "libros34", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libros34"):
                    opp_val = getattr(item, "libros34", None)
                    
                    if opp_val is None:
                        setattr(item, "libros34", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Documentos:

    def __init__(self, titulo: str, fechaPublicaci_n: str, autores: str, ISBN: str, mesPublicaci_n: str, d_a: str, editorial: str, fechaCreaci_n: str, autores232: set["Autores"] = None, libros34: set["Libros"] = None, articulosCient_ficos36: set["ArticulosCient_ficos"] = None, editoriales38: set["Editoriales"] = None, ponencias40: set["Ponencias"] = None):
        self.titulo = titulo
        self.fechaPublicaci_n = fechaPublicaci_n
        self.autores = autores
        self.ISBN = ISBN
        self.mesPublicaci_n = mesPublicaci_n
        self.d_a = d_a
        self.editorial = editorial
        self.fechaCreaci_n = fechaCreaci_n
        self.autores232 = autores232 if autores232 is not None else set()
        self.libros34 = libros34 if libros34 is not None else set()
        self.articulosCient_ficos36 = articulosCient_ficos36 if articulosCient_ficos36 is not None else set()
        self.editoriales38 = editoriales38 if editoriales38 is not None else set()
        self.ponencias40 = ponencias40 if ponencias40 is not None else set()
        
        pass
    @property
    def editorial(self):
        return self.__editorial
    @editorial.setter
    def editorial(self, editorial: str):
        self.__editorial = editorial

    @property
    def fechaPublicaci_n(self):
        return self.__fechaPublicaci_n
    @fechaPublicaci_n.setter
    def fechaPublicaci_n(self, fechaPublicaci_n: str):
        self.__fechaPublicaci_n = fechaPublicaci_n

    @property
    def fechaCreaci_n(self):
        return self.__fechaCreaci_n
    @fechaCreaci_n.setter
    def fechaCreaci_n(self, fechaCreaci_n: str):
        self.__fechaCreaci_n = fechaCreaci_n

    @property
    def titulo(self):
        return self.__titulo
    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo

    @property
    def d_a(self):
        return self.__d_a
    @d_a.setter
    def d_a(self, d_a: str):
        self.__d_a = d_a

    @property
    def ISBN(self):
        return self.__ISBN
    @ISBN.setter
    def ISBN(self, ISBN: str):
        self.__ISBN = ISBN

    @property
    def autores(self):
        return self.__autores
    @autores.setter
    def autores(self, autores: str):
        self.__autores = autores

    @property
    def mesPublicaci_n(self):
        return self.__mesPublicaci_n
    @mesPublicaci_n.setter
    def mesPublicaci_n(self, mesPublicaci_n: str):
        self.__mesPublicaci_n = mesPublicaci_n

    @property
    def autores232(self):
        return self.__autores232
    @autores232.setter
    def autores232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Documentos__autores232", None)
        self.__autores232 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "documentos33"):
                    opp_val = getattr(item, "documentos33", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "documentos33"):
                    opp_val = getattr(item, "documentos33", None)
                    
                    if opp_val is None:
                        setattr(item, "documentos33", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def libros34(self):
        return self.__libros34
    @libros34.setter
    def libros34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Documentos__libros34", None)
        self.__libros34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "documentos35"):
                    opp_val = getattr(item, "documentos35", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "documentos35"):
                    opp_val = getattr(item, "documentos35", None)
                    
                    if opp_val is None:
                        setattr(item, "documentos35", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def articulosCient_ficos36(self):
        return self.__articulosCient_ficos36
    @articulosCient_ficos36.setter
    def articulosCient_ficos36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Documentos__articulosCient_ficos36", None)
        self.__articulosCient_ficos36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "documentos37"):
                    opp_val = getattr(item, "documentos37", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "documentos37"):
                    opp_val = getattr(item, "documentos37", None)
                    
                    if opp_val is None:
                        setattr(item, "documentos37", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def editoriales38(self):
        return self.__editoriales38
    @editoriales38.setter
    def editoriales38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Documentos__editoriales38", None)
        self.__editoriales38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "documentos39"):
                    opp_val = getattr(item, "documentos39", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "documentos39"):
                    opp_val = getattr(item, "documentos39", None)
                    
                    if opp_val is None:
                        setattr(item, "documentos39", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def ponencias40(self):
        return self.__ponencias40
    @ponencias40.setter
    def ponencias40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Documentos__ponencias40", None)
        self.__ponencias40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "documentos41"):
                    opp_val = getattr(item, "documentos41", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "documentos41"):
                    opp_val = getattr(item, "documentos41", None)
                    
                    if opp_val is None:
                        setattr(item, "documentos41", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Dependencia:

    def __init__(self, codigo: str, nombre: str, responsable: str, solicitudSuministro26: set["SolicitudSuministro"] = None):
        self.codigo = codigo
        self.nombre = nombre
        self.responsable = responsable
        self.solicitudSuministro26 = solicitudSuministro26 if solicitudSuministro26 is not None else set()
        
        pass
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
        old_value = getattr(self, f"_Dependencia__solicitudSuministro26", None)
        self.__solicitudSuministro26 = value if value is not None else set()
        
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
                    



class SolicitudSuministro:

    def __init__(self, codigo: str, fecha: str, elementos22: set["Elementos"] = None, ordenesPedidos25: "OrdenesPedido" = None, dependencia27: "Dependencia" = None):
        self.codigo = codigo
        self.fecha = fecha
        self.elementos22 = elementos22 if elementos22 is not None else set()
        self.ordenesPedidos25 = ordenesPedidos25
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
        old_value = getattr(self, f"_SolicitudSuministro__dependencia27", None)
        self.__dependencia27 = value
        
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
    def elementos22(self):
        return self.__elementos22
    @elementos22.setter
    def elementos22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SolicitudSuministro__elementos22", None)
        self.__elementos22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "solicitudSuministro23"):
                    opp_val = getattr(item, "solicitudSuministro23", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "solicitudSuministro23"):
                    opp_val = getattr(item, "solicitudSuministro23", None)
                    
                    if opp_val is None:
                        setattr(item, "solicitudSuministro23", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def ordenesPedidos25(self):
        return self.__ordenesPedidos25
    @ordenesPedidos25.setter
    def ordenesPedidos25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SolicitudSuministro__ordenesPedidos25", None)
        self.__ordenesPedidos25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "solicitudSuministro24"):
                opp_val = getattr(old_value, "solicitudSuministro24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "solicitudSuministro24"):
                opp_val = getattr(value, "solicitudSuministro24", None)
                if opp_val is None:
                    setattr(value, "solicitudSuministro24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Factura:

    def __init__(self, codigo: str, fecha: str, elementos31: set["Elementos"] = None, proveedor29: "Proveedor" = None):
        self.codigo = codigo
        self.fecha = fecha
        self.elementos31 = elementos31 if elementos31 is not None else set()
        self.proveedor29 = proveedor29
        
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
                    

    @property
    def proveedor29(self):
        return self.__proveedor29
    @proveedor29.setter
    def proveedor29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Factura__proveedor29", None)
        self.__proveedor29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "factura28"):
                opp_val = getattr(old_value, "factura28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "factura28"):
                opp_val = getattr(value, "factura28", None)
                if opp_val is None:
                    setattr(value, "factura28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Elementos:

    def __init__(self, referencia: str, clasificaci_n: str, ordenesPedido21: set["OrdenesPedido"] = None, solicitudSuministro23: set["SolicitudSuministro"] = None, factura30: set["Factura"] = None):
        self.referencia = referencia
        self.clasificaci_n = clasificaci_n
        self.ordenesPedido21 = ordenesPedido21 if ordenesPedido21 is not None else set()
        self.solicitudSuministro23 = solicitudSuministro23 if solicitudSuministro23 is not None else set()
        self.factura30 = factura30 if factura30 is not None else set()
        
        pass
    @property
    def referencia(self):
        return self.__referencia
    @referencia.setter
    def referencia(self, referencia: str):
        self.__referencia = referencia

    @property
    def clasificaci_n(self):
        return self.__clasificaci_n
    @clasificaci_n.setter
    def clasificaci_n(self, clasificaci_n: str):
        self.__clasificaci_n = clasificaci_n

    @property
    def ordenesPedido21(self):
        return self.__ordenesPedido21
    @ordenesPedido21.setter
    def ordenesPedido21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elementos__ordenesPedido21", None)
        self.__ordenesPedido21 = value if value is not None else set()
        
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
    def solicitudSuministro23(self):
        return self.__solicitudSuministro23
    @solicitudSuministro23.setter
    def solicitudSuministro23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elementos__solicitudSuministro23", None)
        self.__solicitudSuministro23 = value if value is not None else set()
        
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
                    



class Proveedor:

    def __init__(self, nit: str, razonSocial: str, direcci_n: str, tel_fonos: str, ordenesPedido16: set["OrdenesPedido"] = None, pedidos19: set["Pedidos"] = None, factura28: set["Factura"] = None):
        self.nit = nit
        self.razonSocial = razonSocial
        self.direcci_n = direcci_n
        self.tel_fonos = tel_fonos
        self.ordenesPedido16 = ordenesPedido16 if ordenesPedido16 is not None else set()
        self.pedidos19 = pedidos19 if pedidos19 is not None else set()
        self.factura28 = factura28 if factura28 is not None else set()
        
        pass
    @property
    def tel_fonos(self):
        return self.__tel_fonos
    @tel_fonos.setter
    def tel_fonos(self, tel_fonos: str):
        self.__tel_fonos = tel_fonos

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
    def direcci_n(self):
        return self.__direcci_n
    @direcci_n.setter
    def direcci_n(self, direcci_n: str):
        self.__direcci_n = direcci_n

    @property
    def factura28(self):
        return self.__factura28
    @factura28.setter
    def factura28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Proveedor__factura28", None)
        self.__factura28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "proveedor29"):
                    opp_val = getattr(item, "proveedor29", None)
                    
                    if opp_val == self:
                        setattr(item, "proveedor29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "proveedor29"):
                    opp_val = getattr(item, "proveedor29", None)
                    
                    setattr(item, "proveedor29", self)
                    

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
    def ordenesPedido16(self):
        return self.__ordenesPedido16
    @ordenesPedido16.setter
    def ordenesPedido16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Proveedor__ordenesPedido16", None)
        self.__ordenesPedido16 = value if value is not None else set()
        
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
                    



class OrdenesPedido:

    def __init__(self, codigo: str, fecha: str, proveedor17: "Proveedor" = None, elementos20: set["Elementos"] = None, solicitudSuministro24: set["SolicitudSuministro"] = None):
        self.codigo = codigo
        self.fecha = fecha
        self.proveedor17 = proveedor17
        self.elementos20 = elementos20 if elementos20 is not None else set()
        self.solicitudSuministro24 = solicitudSuministro24 if solicitudSuministro24 is not None else set()
        
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
        old_value = getattr(self, f"_OrdenesPedido__elementos20", None)
        self.__elementos20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ordenesPedido21"):
                    opp_val = getattr(item, "ordenesPedido21", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ordenesPedido21"):
                    opp_val = getattr(item, "ordenesPedido21", None)
                    
                    if opp_val is None:
                        setattr(item, "ordenesPedido21", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def solicitudSuministro24(self):
        return self.__solicitudSuministro24
    @solicitudSuministro24.setter
    def solicitudSuministro24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrdenesPedido__solicitudSuministro24", None)
        self.__solicitudSuministro24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ordenesPedidos25"):
                    opp_val = getattr(item, "ordenesPedidos25", None)
                    
                    if opp_val == self:
                        setattr(item, "ordenesPedidos25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ordenesPedidos25"):
                    opp_val = getattr(item, "ordenesPedidos25", None)
                    
                    setattr(item, "ordenesPedidos25", self)
                    

    @property
    def proveedor17(self):
        return self.__proveedor17
    @proveedor17.setter
    def proveedor17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrdenesPedido__proveedor17", None)
        self.__proveedor17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ordenesPedido16"):
                opp_val = getattr(old_value, "ordenesPedido16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ordenesPedido16"):
                opp_val = getattr(value, "ordenesPedido16", None)
                if opp_val is None:
                    setattr(value, "ordenesPedido16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Sistema_WEB_M_vil_Recepci_n_de_pedidos_Component:

    pass


class Departamento_de_Inventarios_y_Suministros_DIS_Component:

    pass


class Milenium_Component:

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

