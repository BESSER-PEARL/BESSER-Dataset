from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Jugador:

    def __init__(self, nombre: str, apellidos: str, telefono: int, nif: str, equipo7: "Equipo" = None, fechaNacimiento8: "Fecha" = None):
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.nif = nif
        self.equipo7 = equipo7
        self.fechaNacimiento8 = fechaNacimiento8
        
        pass
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def apellidos(self):
        return self.__apellidos
    @apellidos.setter
    def apellidos(self, apellidos: str):
        self.__apellidos = apellidos

    @property
    def telefono(self):
        return self.__telefono
    @telefono.setter
    def telefono(self, telefono: int):
        self.__telefono = telefono

    @property
    def nif(self):
        return self.__nif
    @nif.setter
    def nif(self, nif: str):
        self.__nif = nif

    @property
    def equipo7(self):
        return self.__equipo7
    @equipo7.setter
    def equipo7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Jugador__equipo7", None)
        self.__equipo7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jugador6"):
                opp_val = getattr(old_value, "jugador6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jugador6"):
                opp_val = getattr(value, "jugador6", None)
                if opp_val is None:
                    setattr(value, "jugador6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fechaNacimiento8(self):
        return self.__fechaNacimiento8
    @fechaNacimiento8.setter
    def fechaNacimiento8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Jugador__fechaNacimiento8", None)
        self.__fechaNacimiento8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jugador9"):
                opp_val = getattr(old_value, "jugador9", None)
                if opp_val == self:
                    setattr(old_value, "jugador9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jugador9"):
                opp_val = getattr(value, "jugador9", None)
                setattr(value, "jugador9", self)



class Equipo:

    def __init__(self, nombre: str, partido5: "Partido" = None, jugador6: set["Jugador"] = None):
        self.nombre = nombre
        self.partido5 = partido5
        self.jugador6 = jugador6 if jugador6 is not None else set()
        
        pass
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def jugador6(self):
        return self.__jugador6
    @jugador6.setter
    def jugador6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Equipo__jugador6", None)
        self.__jugador6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "equipo7"):
                    opp_val = getattr(item, "equipo7", None)
                    
                    if opp_val == self:
                        setattr(item, "equipo7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "equipo7"):
                    opp_val = getattr(item, "equipo7", None)
                    
                    setattr(item, "equipo7", self)
                    

    @property
    def partido5(self):
        return self.__partido5
    @partido5.setter
    def partido5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Equipo__partido5", None)
        self.__partido5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "equipo4"):
                opp_val = getattr(old_value, "equipo4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "equipo4"):
                opp_val = getattr(value, "equipo4", None)
                if opp_val is None:
                    setattr(value, "equipo4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Marcador:

    def __init__(self, equipo1: int, equipo2: int, tiempoSet: int, partido3: "Partido" = None):
        self.equipo1 = equipo1
        self.equipo2 = equipo2
        self.tiempoSet = tiempoSet
        self.partido3 = partido3
        
        pass
    @property
    def equipo2(self):
        return self.__equipo2
    @equipo2.setter
    def equipo2(self, equipo2: int):
        self.__equipo2 = equipo2

    @property
    def tiempoSet(self):
        return self.__tiempoSet
    @tiempoSet.setter
    def tiempoSet(self, tiempoSet: int):
        self.__tiempoSet = tiempoSet

    @property
    def equipo1(self):
        return self.__equipo1
    @equipo1.setter
    def equipo1(self, equipo1: int):
        self.__equipo1 = equipo1

    @property
    def partido3(self):
        return self.__partido3
    @partido3.setter
    def partido3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Marcador__partido3", None)
        self.__partido3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "marcador2"):
                opp_val = getattr(old_value, "marcador2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "marcador2"):
                opp_val = getattr(value, "marcador2", None)
                if opp_val is None:
                    setattr(value, "marcador2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Partido:

    def __init__(self, id: int, ronda: str, marcador2: set["Marcador"] = None, equipo4: set["Equipo"] = None, torneo15: "Torneo" = None):
        self.id = id
        self.ronda = ronda
        self.marcador2 = marcador2 if marcador2 is not None else set()
        self.equipo4 = equipo4 if equipo4 is not None else set()
        self.torneo15 = torneo15
        
        pass
    @property
    def ronda(self):
        return self.__ronda
    @ronda.setter
    def ronda(self, ronda: str):
        self.__ronda = ronda

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def marcador2(self):
        return self.__marcador2
    @marcador2.setter
    def marcador2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Partido__marcador2", None)
        self.__marcador2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "partido3"):
                    opp_val = getattr(item, "partido3", None)
                    
                    if opp_val == self:
                        setattr(item, "partido3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "partido3"):
                    opp_val = getattr(item, "partido3", None)
                    
                    setattr(item, "partido3", self)
                    

    @property
    def equipo4(self):
        return self.__equipo4
    @equipo4.setter
    def equipo4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Partido__equipo4", None)
        self.__equipo4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "partido5"):
                    opp_val = getattr(item, "partido5", None)
                    
                    if opp_val == self:
                        setattr(item, "partido5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "partido5"):
                    opp_val = getattr(item, "partido5", None)
                    
                    setattr(item, "partido5", self)
                    

    @property
    def torneo15(self):
        return self.__torneo15
    @torneo15.setter
    def torneo15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Partido__torneo15", None)
        self.__torneo15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "partido14"):
                opp_val = getattr(old_value, "partido14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "partido14"):
                opp_val = getattr(value, "partido14", None)
                if opp_val is None:
                    setattr(value, "partido14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Fecha:

    def __init__(self, anio: int, mes: int, dia: int, jugador9: "Jugador" = None, torneo11: "Torneo" = None, torneo13: "Torneo" = None):
        self.anio = anio
        self.mes = mes
        self.dia = dia
        self.jugador9 = jugador9
        self.torneo11 = torneo11
        self.torneo13 = torneo13
        
        pass
    @property
    def mes(self):
        return self.__mes
    @mes.setter
    def mes(self, mes: int):
        self.__mes = mes

    @property
    def dia(self):
        return self.__dia
    @dia.setter
    def dia(self, dia: int):
        self.__dia = dia

    @property
    def anio(self):
        return self.__anio
    @anio.setter
    def anio(self, anio: int):
        self.__anio = anio

    @property
    def jugador9(self):
        return self.__jugador9
    @jugador9.setter
    def jugador9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Fecha__jugador9", None)
        self.__jugador9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fechaNacimiento8"):
                opp_val = getattr(old_value, "fechaNacimiento8", None)
                if opp_val == self:
                    setattr(old_value, "fechaNacimiento8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fechaNacimiento8"):
                opp_val = getattr(value, "fechaNacimiento8", None)
                setattr(value, "fechaNacimiento8", self)

    @property
    def torneo11(self):
        return self.__torneo11
    @torneo11.setter
    def torneo11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Fecha__torneo11", None)
        self.__torneo11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fechaInicio10"):
                opp_val = getattr(old_value, "fechaInicio10", None)
                if opp_val == self:
                    setattr(old_value, "fechaInicio10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fechaInicio10"):
                opp_val = getattr(value, "fechaInicio10", None)
                setattr(value, "fechaInicio10", self)

    @property
    def torneo13(self):
        return self.__torneo13
    @torneo13.setter
    def torneo13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Fecha__torneo13", None)
        self.__torneo13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fechaFin12"):
                opp_val = getattr(old_value, "fechaFin12", None)
                if opp_val == self:
                    setattr(old_value, "fechaFin12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fechaFin12"):
                opp_val = getattr(value, "fechaFin12", None)
                setattr(value, "fechaFin12", self)



class Premio:

    def __init__(self, Puesto: int, Dinero: int, Puntos: int, torneo1: "Torneo" = None):
        self.Puesto = Puesto
        self.Dinero = Dinero
        self.Puntos = Puntos
        self.torneo1 = torneo1
        
        pass
    @property
    def Puesto(self):
        return self.__Puesto
    @Puesto.setter
    def Puesto(self, Puesto: int):
        self.__Puesto = Puesto

    @property
    def Puntos(self):
        return self.__Puntos
    @Puntos.setter
    def Puntos(self, Puntos: int):
        self.__Puntos = Puntos

    @property
    def Dinero(self):
        return self.__Dinero
    @Dinero.setter
    def Dinero(self, Dinero: int):
        self.__Dinero = Dinero

    @property
    def torneo1(self):
        return self.__torneo1
    @torneo1.setter
    def torneo1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Premio__torneo1", None)
        self.__torneo1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "premio0"):
                opp_val = getattr(old_value, "premio0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "premio0"):
                opp_val = getattr(value, "premio0", None)
                if opp_val is None:
                    setattr(value, "premio0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Torneo:

    def __init__(self, Nombre: str, Pais: str, premio0: set["Premio"] = None, fechaInicio10: "Fecha" = None, fechaFin12: "Fecha" = None, partido14: set["Partido"] = None):
        self.Nombre = Nombre
        self.Pais = Pais
        self.premio0 = premio0 if premio0 is not None else set()
        self.fechaInicio10 = fechaInicio10
        self.fechaFin12 = fechaFin12
        self.partido14 = partido14 if partido14 is not None else set()
        
        pass
    @property
    def Nombre(self):
        return self.__Nombre
    @Nombre.setter
    def Nombre(self, Nombre: str):
        self.__Nombre = Nombre

    @property
    def Pais(self):
        return self.__Pais
    @Pais.setter
    def Pais(self, Pais: str):
        self.__Pais = Pais

    @property
    def partido14(self):
        return self.__partido14
    @partido14.setter
    def partido14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Torneo__partido14", None)
        self.__partido14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "torneo15"):
                    opp_val = getattr(item, "torneo15", None)
                    
                    if opp_val == self:
                        setattr(item, "torneo15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "torneo15"):
                    opp_val = getattr(item, "torneo15", None)
                    
                    setattr(item, "torneo15", self)
                    

    @property
    def fechaInicio10(self):
        return self.__fechaInicio10
    @fechaInicio10.setter
    def fechaInicio10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Torneo__fechaInicio10", None)
        self.__fechaInicio10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "torneo11"):
                opp_val = getattr(old_value, "torneo11", None)
                if opp_val == self:
                    setattr(old_value, "torneo11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "torneo11"):
                opp_val = getattr(value, "torneo11", None)
                setattr(value, "torneo11", self)

    @property
    def fechaFin12(self):
        return self.__fechaFin12
    @fechaFin12.setter
    def fechaFin12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Torneo__fechaFin12", None)
        self.__fechaFin12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "torneo13"):
                opp_val = getattr(old_value, "torneo13", None)
                if opp_val == self:
                    setattr(old_value, "torneo13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "torneo13"):
                opp_val = getattr(value, "torneo13", None)
                setattr(value, "torneo13", self)

    @property
    def premio0(self):
        return self.__premio0
    @premio0.setter
    def premio0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Torneo__premio0", None)
        self.__premio0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "torneo1"):
                    opp_val = getattr(item, "torneo1", None)
                    
                    if opp_val == self:
                        setattr(item, "torneo1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "torneo1"):
                    opp_val = getattr(item, "torneo1", None)
                    
                    setattr(item, "torneo1", self)
                    

