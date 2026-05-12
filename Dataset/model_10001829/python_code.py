from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class int(Enum):
    pass

############################################
# Definition of Classes
############################################










class Reporte:

    pass


class Tipo_mascota:

    def __init__(self, Nombre_Tipo: str, id_Tipo_Mascota: int, mascotas16: set["Mascotas"] = None):
        self.Nombre_Tipo = Nombre_Tipo
        self.id_Tipo_Mascota = id_Tipo_Mascota
        self.mascotas16 = mascotas16 if mascotas16 is not None else set()
        
        pass
    @property
    def Nombre_Tipo(self):
        return self.__Nombre_Tipo
    @Nombre_Tipo.setter
    def Nombre_Tipo(self, Nombre_Tipo: str):
        self.__Nombre_Tipo = Nombre_Tipo

    @property
    def id_Tipo_Mascota(self):
        return self.__id_Tipo_Mascota
    @id_Tipo_Mascota.setter
    def id_Tipo_Mascota(self, id_Tipo_Mascota: int):
        self.__id_Tipo_Mascota = id_Tipo_Mascota

    @property
    def mascotas16(self):
        return self.__mascotas16
    @mascotas16.setter
    def mascotas16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Tipo_mascota__mascotas16", None)
        self.__mascotas16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tipo_mascota217"):
                    opp_val = getattr(item, "tipo_mascota217", None)
                    
                    if opp_val == self:
                        setattr(item, "tipo_mascota217", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tipo_mascota217"):
                    opp_val = getattr(item, "tipo_mascota217", None)
                    
                    setattr(item, "tipo_mascota217", self)
                    



class Estados:

    def __init__(self, Nombre_estados: str, id_estados: int, mascotas7: "Mascotas" = None):
        self.Nombre_estados = Nombre_estados
        self.id_estados = id_estados
        self.mascotas7 = mascotas7
        
        pass
    @property
    def id_estados(self):
        return self.__id_estados
    @id_estados.setter
    def id_estados(self, id_estados: int):
        self.__id_estados = id_estados

    @property
    def Nombre_estados(self):
        return self.__Nombre_estados
    @Nombre_estados.setter
    def Nombre_estados(self, Nombre_estados: str):
        self.__Nombre_estados = Nombre_estados

    @property
    def mascotas7(self):
        return self.__mascotas7
    @mascotas7.setter
    def mascotas7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Estados__mascotas7", None)
        self.__mascotas7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "estados6"):
                opp_val = getattr(old_value, "estados6", None)
                if opp_val == self:
                    setattr(old_value, "estados6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "estados6"):
                opp_val = getattr(value, "estados6", None)
                setattr(value, "estados6", self)



class Insumos:

    def __init__(self, Nombre_insumo: str, Id_insumo: int, servicios3: "Servicios" = None):
        self.Nombre_insumo = Nombre_insumo
        self.Id_insumo = Id_insumo
        self.servicios3 = servicios3
        
        pass
    @property
    def Id_insumo(self):
        return self.__Id_insumo
    @Id_insumo.setter
    def Id_insumo(self, Id_insumo: int):
        self.__Id_insumo = Id_insumo

    @property
    def Nombre_insumo(self):
        return self.__Nombre_insumo
    @Nombre_insumo.setter
    def Nombre_insumo(self, Nombre_insumo: str):
        self.__Nombre_insumo = Nombre_insumo

    @property
    def servicios3(self):
        return self.__servicios3
    @servicios3.setter
    def servicios3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Insumos__servicios3", None)
        self.__servicios3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "insumos2"):
                opp_val = getattr(old_value, "insumos2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "insumos2"):
                opp_val = getattr(value, "insumos2", None)
                if opp_val is None:
                    setattr(value, "insumos2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Profesionales:

    def __init__(self, Nombre_profesional: str, id_profesional: int, servicios5: "Servicios" = None):
        self.Nombre_profesional = Nombre_profesional
        self.id_profesional = id_profesional
        self.servicios5 = servicios5
        
        pass
    @property
    def Nombre_profesional(self):
        return self.__Nombre_profesional
    @Nombre_profesional.setter
    def Nombre_profesional(self, Nombre_profesional: str):
        self.__Nombre_profesional = Nombre_profesional

    @property
    def id_profesional(self):
        return self.__id_profesional
    @id_profesional.setter
    def id_profesional(self, id_profesional: int):
        self.__id_profesional = id_profesional

    @property
    def servicios5(self):
        return self.__servicios5
    @servicios5.setter
    def servicios5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Profesionales__servicios5", None)
        self.__servicios5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profesionales4"):
                opp_val = getattr(old_value, "profesionales4", None)
                if opp_val == self:
                    setattr(old_value, "profesionales4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profesionales4"):
                opp_val = getattr(value, "profesionales4", None)
                setattr(value, "profesionales4", self)



class Auxiliar:

    def __init__(self, Nombre_auxiliar: str, Id_auxiliar: str, registro18: set["Registro"] = None):
        self.Nombre_auxiliar = Nombre_auxiliar
        self.Id_auxiliar = Id_auxiliar
        self.registro18 = registro18 if registro18 is not None else set()
        
        pass
    @property
    def Nombre_auxiliar(self):
        return self.__Nombre_auxiliar
    @Nombre_auxiliar.setter
    def Nombre_auxiliar(self, Nombre_auxiliar: str):
        self.__Nombre_auxiliar = Nombre_auxiliar

    @property
    def Id_auxiliar(self):
        return self.__Id_auxiliar
    @Id_auxiliar.setter
    def Id_auxiliar(self, Id_auxiliar: str):
        self.__Id_auxiliar = Id_auxiliar

    @property
    def registro18(self):
        return self.__registro18
    @registro18.setter
    def registro18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Auxiliar__registro18", None)
        self.__registro18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "auxiliar19"):
                    opp_val = getattr(item, "auxiliar19", None)
                    
                    if opp_val == self:
                        setattr(item, "auxiliar19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "auxiliar19"):
                    opp_val = getattr(item, "auxiliar19", None)
                    
                    setattr(item, "auxiliar19", self)
                    



class Guacales:

    def __init__(self, Id_guacal: int, mascotas9: "Mascotas" = None):
        self.Id_guacal = Id_guacal
        self.mascotas9 = mascotas9
        
        pass
    @property
    def Id_guacal(self):
        return self.__Id_guacal
    @Id_guacal.setter
    def Id_guacal(self, Id_guacal: int):
        self.__Id_guacal = Id_guacal

    @property
    def mascotas9(self):
        return self.__mascotas9
    @mascotas9.setter
    def mascotas9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Guacales__mascotas9", None)
        self.__mascotas9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "guacales8"):
                opp_val = getattr(old_value, "guacales8", None)
                if opp_val == self:
                    setattr(old_value, "guacales8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "guacales8"):
                opp_val = getattr(value, "guacales8", None)
                setattr(value, "guacales8", self)



class Cliente:

    def __init__(self, C_dula: str, Tel_fono: int, mascotas14: set["Mascotas"] = None, registro12: set["Registro"] = None):
        self.C_dula = C_dula
        self.Tel_fono = Tel_fono
        self.mascotas14 = mascotas14 if mascotas14 is not None else set()
        self.registro12 = registro12 if registro12 is not None else set()
        
        pass
    @property
    def C_dula(self):
        return self.__C_dula
    @C_dula.setter
    def C_dula(self, C_dula: str):
        self.__C_dula = C_dula

    @property
    def Tel_fono(self):
        return self.__Tel_fono
    @Tel_fono.setter
    def Tel_fono(self, Tel_fono: int):
        self.__Tel_fono = Tel_fono

    @property
    def mascotas14(self):
        return self.__mascotas14
    @mascotas14.setter
    def mascotas14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cliente__mascotas14", None)
        self.__mascotas14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cliente15"):
                    opp_val = getattr(item, "cliente15", None)
                    
                    if opp_val == self:
                        setattr(item, "cliente15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cliente15"):
                    opp_val = getattr(item, "cliente15", None)
                    
                    setattr(item, "cliente15", self)
                    

    @property
    def registro12(self):
        return self.__registro12
    @registro12.setter
    def registro12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cliente__registro12", None)
        self.__registro12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cliente13"):
                    opp_val = getattr(item, "cliente13", None)
                    
                    if opp_val == self:
                        setattr(item, "cliente13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cliente13"):
                    opp_val = getattr(item, "cliente13", None)
                    
                    setattr(item, "cliente13", self)
                    



class Registro:

    def __init__(self, Hora_entrada: str, Hora_salida: str, Tipo_Mascota: Tipo_mascota, Cliente: Cliente, Auxiliar: Auxiliar, auxiliar19: "Auxiliar" = None, mascotas11: "Mascotas" = None, cliente13: "Cliente" = None):
        self.Hora_entrada = Hora_entrada
        self.Hora_salida = Hora_salida
        self.Tipo_Mascota = Tipo_Mascota
        self.Cliente = Cliente
        self.Auxiliar = Auxiliar
        self.auxiliar19 = auxiliar19
        self.mascotas11 = mascotas11
        self.cliente13 = cliente13
        
        pass
    @property
    def Tipo_Mascota(self):
        return self.__Tipo_Mascota
    @Tipo_Mascota.setter
    def Tipo_Mascota(self, Tipo_Mascota: Tipo_mascota):
        self.__Tipo_Mascota = Tipo_Mascota

    @property
    def Auxiliar(self):
        return self.__Auxiliar
    @Auxiliar.setter
    def Auxiliar(self, Auxiliar: Auxiliar):
        self.__Auxiliar = Auxiliar

    @property
    def Hora_entrada(self):
        return self.__Hora_entrada
    @Hora_entrada.setter
    def Hora_entrada(self, Hora_entrada: str):
        self.__Hora_entrada = Hora_entrada

    @property
    def Hora_salida(self):
        return self.__Hora_salida
    @Hora_salida.setter
    def Hora_salida(self, Hora_salida: str):
        self.__Hora_salida = Hora_salida

    @property
    def Cliente(self):
        return self.__Cliente
    @Cliente.setter
    def Cliente(self, Cliente: Cliente):
        self.__Cliente = Cliente

    @property
    def auxiliar19(self):
        return self.__auxiliar19
    @auxiliar19.setter
    def auxiliar19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Registro__auxiliar19", None)
        self.__auxiliar19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "registro18"):
                opp_val = getattr(old_value, "registro18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "registro18"):
                opp_val = getattr(value, "registro18", None)
                if opp_val is None:
                    setattr(value, "registro18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mascotas11(self):
        return self.__mascotas11
    @mascotas11.setter
    def mascotas11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Registro__mascotas11", None)
        self.__mascotas11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "registro10"):
                opp_val = getattr(old_value, "registro10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "registro10"):
                opp_val = getattr(value, "registro10", None)
                if opp_val is None:
                    setattr(value, "registro10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cliente13(self):
        return self.__cliente13
    @cliente13.setter
    def cliente13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Registro__cliente13", None)
        self.__cliente13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "registro12"):
                opp_val = getattr(old_value, "registro12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "registro12"):
                opp_val = getattr(value, "registro12", None)
                if opp_val is None:
                    setattr(value, "registro12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Mascotas:

    def __init__(self, Id_mascota: int, tipo_mascota: Tipo_mascota, cliente15: "Cliente" = None, tipo_mascota217: "Tipo_mascota" = None, reporte21: set["Reporte"] = None, servicios1: set["Servicios"] = None, estados6: "Estados" = None, guacales8: "Guacales" = None, registro10: set["Registro"] = None):
        self.Id_mascota = Id_mascota
        self.tipo_mascota = tipo_mascota
        self.cliente15 = cliente15
        self.tipo_mascota217 = tipo_mascota217
        self.reporte21 = reporte21 if reporte21 is not None else set()
        self.servicios1 = servicios1 if servicios1 is not None else set()
        self.estados6 = estados6
        self.guacales8 = guacales8
        self.registro10 = registro10 if registro10 is not None else set()
        
        pass
    @property
    def tipo_mascota(self):
        return self.__tipo_mascota
    @tipo_mascota.setter
    def tipo_mascota(self, tipo_mascota: Tipo_mascota):
        self.__tipo_mascota = tipo_mascota

    @property
    def Id_mascota(self):
        return self.__Id_mascota
    @Id_mascota.setter
    def Id_mascota(self, Id_mascota: int):
        self.__Id_mascota = Id_mascota

    @property
    def cliente15(self):
        return self.__cliente15
    @cliente15.setter
    def cliente15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Mascotas__cliente15", None)
        self.__cliente15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mascotas14"):
                opp_val = getattr(old_value, "mascotas14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mascotas14"):
                opp_val = getattr(value, "mascotas14", None)
                if opp_val is None:
                    setattr(value, "mascotas14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def estados6(self):
        return self.__estados6
    @estados6.setter
    def estados6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Mascotas__estados6", None)
        self.__estados6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mascotas7"):
                opp_val = getattr(old_value, "mascotas7", None)
                if opp_val == self:
                    setattr(old_value, "mascotas7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mascotas7"):
                opp_val = getattr(value, "mascotas7", None)
                setattr(value, "mascotas7", self)

    @property
    def tipo_mascota217(self):
        return self.__tipo_mascota217
    @tipo_mascota217.setter
    def tipo_mascota217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Mascotas__tipo_mascota217", None)
        self.__tipo_mascota217 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mascotas16"):
                opp_val = getattr(old_value, "mascotas16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mascotas16"):
                opp_val = getattr(value, "mascotas16", None)
                if opp_val is None:
                    setattr(value, "mascotas16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def registro10(self):
        return self.__registro10
    @registro10.setter
    def registro10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Mascotas__registro10", None)
        self.__registro10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mascotas11"):
                    opp_val = getattr(item, "mascotas11", None)
                    
                    if opp_val == self:
                        setattr(item, "mascotas11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mascotas11"):
                    opp_val = getattr(item, "mascotas11", None)
                    
                    setattr(item, "mascotas11", self)
                    

    @property
    def reporte21(self):
        return self.__reporte21
    @reporte21.setter
    def reporte21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Mascotas__reporte21", None)
        self.__reporte21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mascotas20"):
                    opp_val = getattr(item, "mascotas20", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mascotas20"):
                    opp_val = getattr(item, "mascotas20", None)
                    
                    if opp_val is None:
                        setattr(item, "mascotas20", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def servicios1(self):
        return self.__servicios1
    @servicios1.setter
    def servicios1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Mascotas__servicios1", None)
        self.__servicios1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mascotas0"):
                    opp_val = getattr(item, "mascotas0", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mascotas0"):
                    opp_val = getattr(item, "mascotas0", None)
                    
                    if opp_val is None:
                        setattr(item, "mascotas0", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def guacales8(self):
        return self.__guacales8
    @guacales8.setter
    def guacales8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Mascotas__guacales8", None)
        self.__guacales8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mascotas9"):
                opp_val = getattr(old_value, "mascotas9", None)
                if opp_val == self:
                    setattr(old_value, "mascotas9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mascotas9"):
                opp_val = getattr(value, "mascotas9", None)
                setattr(value, "mascotas9", self)



class Servicios:

    def __init__(self, id_servicio: int, Nombre_servicio: str, Tiempo: int, Valor: int, Profesional: Profesionales, Insumos: Insumos, reporte23: set["Reporte"] = None, mascotas0: set["Mascotas"] = None, insumos2: set["Insumos"] = None, profesionales4: "Profesionales" = None):
        self.id_servicio = id_servicio
        self.Nombre_servicio = Nombre_servicio
        self.Tiempo = Tiempo
        self.Valor = Valor
        self.Profesional = Profesional
        self.Insumos = Insumos
        self.reporte23 = reporte23 if reporte23 is not None else set()
        self.mascotas0 = mascotas0 if mascotas0 is not None else set()
        self.insumos2 = insumos2 if insumos2 is not None else set()
        self.profesionales4 = profesionales4
        
        pass
    @property
    def Valor(self):
        return self.__Valor
    @Valor.setter
    def Valor(self, Valor: int):
        self.__Valor = Valor

    @property
    def Tiempo(self):
        return self.__Tiempo
    @Tiempo.setter
    def Tiempo(self, Tiempo: int):
        self.__Tiempo = Tiempo

    @property
    def Insumos(self):
        return self.__Insumos
    @Insumos.setter
    def Insumos(self, Insumos: Insumos):
        self.__Insumos = Insumos

    @property
    def Profesional(self):
        return self.__Profesional
    @Profesional.setter
    def Profesional(self, Profesional: Profesionales):
        self.__Profesional = Profesional

    @property
    def id_servicio(self):
        return self.__id_servicio
    @id_servicio.setter
    def id_servicio(self, id_servicio: int):
        self.__id_servicio = id_servicio

    @property
    def Nombre_servicio(self):
        return self.__Nombre_servicio
    @Nombre_servicio.setter
    def Nombre_servicio(self, Nombre_servicio: str):
        self.__Nombre_servicio = Nombre_servicio

    @property
    def reporte23(self):
        return self.__reporte23
    @reporte23.setter
    def reporte23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Servicios__reporte23", None)
        self.__reporte23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "servicios22"):
                    opp_val = getattr(item, "servicios22", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "servicios22"):
                    opp_val = getattr(item, "servicios22", None)
                    
                    if opp_val is None:
                        setattr(item, "servicios22", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def insumos2(self):
        return self.__insumos2
    @insumos2.setter
    def insumos2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Servicios__insumos2", None)
        self.__insumos2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "servicios3"):
                    opp_val = getattr(item, "servicios3", None)
                    
                    if opp_val == self:
                        setattr(item, "servicios3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "servicios3"):
                    opp_val = getattr(item, "servicios3", None)
                    
                    setattr(item, "servicios3", self)
                    

    @property
    def mascotas0(self):
        return self.__mascotas0
    @mascotas0.setter
    def mascotas0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Servicios__mascotas0", None)
        self.__mascotas0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "servicios1"):
                    opp_val = getattr(item, "servicios1", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "servicios1"):
                    opp_val = getattr(item, "servicios1", None)
                    
                    if opp_val is None:
                        setattr(item, "servicios1", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def profesionales4(self):
        return self.__profesionales4
    @profesionales4.setter
    def profesionales4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Servicios__profesionales4", None)
        self.__profesionales4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "servicios5"):
                opp_val = getattr(old_value, "servicios5", None)
                if opp_val == self:
                    setattr(old_value, "servicios5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "servicios5"):
                opp_val = getattr(value, "servicios5", None)
                setattr(value, "servicios5", self)

