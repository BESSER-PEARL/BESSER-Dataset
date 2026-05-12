from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Historico:

    def __init__(self, numeroPartidosPerdidos: int, numeroPartidosGanados: int, numeroPartidosJugados: int, porcentajeApuestasEnFavor: str, equipo13: "Equipo" = None, partido14: set["Partido"] = None):
        self.numeroPartidosPerdidos = numeroPartidosPerdidos
        self.numeroPartidosGanados = numeroPartidosGanados
        self.numeroPartidosJugados = numeroPartidosJugados
        self.porcentajeApuestasEnFavor = porcentajeApuestasEnFavor
        self.equipo13 = equipo13
        self.partido14 = partido14 if partido14 is not None else set()
        
        pass
    @property
    def numeroPartidosGanados(self):
        return self.__numeroPartidosGanados
    @numeroPartidosGanados.setter
    def numeroPartidosGanados(self, numeroPartidosGanados: int):
        self.__numeroPartidosGanados = numeroPartidosGanados

    @property
    def numeroPartidosPerdidos(self):
        return self.__numeroPartidosPerdidos
    @numeroPartidosPerdidos.setter
    def numeroPartidosPerdidos(self, numeroPartidosPerdidos: int):
        self.__numeroPartidosPerdidos = numeroPartidosPerdidos

    @property
    def porcentajeApuestasEnFavor(self):
        return self.__porcentajeApuestasEnFavor
    @porcentajeApuestasEnFavor.setter
    def porcentajeApuestasEnFavor(self, porcentajeApuestasEnFavor: str):
        self.__porcentajeApuestasEnFavor = porcentajeApuestasEnFavor

    @property
    def numeroPartidosJugados(self):
        return self.__numeroPartidosJugados
    @numeroPartidosJugados.setter
    def numeroPartidosJugados(self, numeroPartidosJugados: int):
        self.__numeroPartidosJugados = numeroPartidosJugados

    @property
    def partido14(self):
        return self.__partido14
    @partido14.setter
    def partido14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Historico__partido14", None)
        self.__partido14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "historico15"):
                    opp_val = getattr(item, "historico15", None)
                    
                    if opp_val == self:
                        setattr(item, "historico15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "historico15"):
                    opp_val = getattr(item, "historico15", None)
                    
                    setattr(item, "historico15", self)
                    

    @property
    def equipo13(self):
        return self.__equipo13
    @equipo13.setter
    def equipo13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Historico__equipo13", None)
        self.__equipo13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "historico12"):
                opp_val = getattr(old_value, "historico12", None)
                if opp_val == self:
                    setattr(old_value, "historico12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "historico12"):
                opp_val = getattr(value, "historico12", None)
                setattr(value, "historico12", self)



class Equipo:

    def __init__(self, nombre: str, jugadores: str, porcentajeFavoritismo: str, partido9: "Partido" = None, partido11: "Partido" = None, historico12: "Historico" = None):
        self.nombre = nombre
        self.jugadores = jugadores
        self.porcentajeFavoritismo = porcentajeFavoritismo
        self.partido9 = partido9
        self.partido11 = partido11
        self.historico12 = historico12
        
        pass
    @property
    def jugadores(self):
        return self.__jugadores
    @jugadores.setter
    def jugadores(self, jugadores: str):
        self.__jugadores = jugadores

    @property
    def porcentajeFavoritismo(self):
        return self.__porcentajeFavoritismo
    @porcentajeFavoritismo.setter
    def porcentajeFavoritismo(self, porcentajeFavoritismo: str):
        self.__porcentajeFavoritismo = porcentajeFavoritismo

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def historico12(self):
        return self.__historico12
    @historico12.setter
    def historico12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Equipo__historico12", None)
        self.__historico12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "equipo13"):
                opp_val = getattr(old_value, "equipo13", None)
                if opp_val == self:
                    setattr(old_value, "equipo13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "equipo13"):
                opp_val = getattr(value, "equipo13", None)
                setattr(value, "equipo13", self)

    @property
    def partido9(self):
        return self.__partido9
    @partido9.setter
    def partido9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Equipo__partido9", None)
        self.__partido9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eq_18"):
                opp_val = getattr(old_value, "eq_18", None)
                if opp_val == self:
                    setattr(old_value, "eq_18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eq_18"):
                opp_val = getattr(value, "eq_18", None)
                setattr(value, "eq_18", self)

    @property
    def partido11(self):
        return self.__partido11
    @partido11.setter
    def partido11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Equipo__partido11", None)
        self.__partido11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eq_210"):
                opp_val = getattr(old_value, "eq_210", None)
                if opp_val == self:
                    setattr(old_value, "eq_210", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eq_210"):
                opp_val = getattr(value, "eq_210", None)
                setattr(value, "eq_210", self)



class Marcador:

    def __init__(self, nombreEquipoGanador: str, numeroGolesEquipo1: int, numeroGolesEquipo2: int, partido17: "Partido" = None):
        self.nombreEquipoGanador = nombreEquipoGanador
        self.numeroGolesEquipo1 = numeroGolesEquipo1
        self.numeroGolesEquipo2 = numeroGolesEquipo2
        self.partido17 = partido17
        
        pass
    @property
    def nombreEquipoGanador(self):
        return self.__nombreEquipoGanador
    @nombreEquipoGanador.setter
    def nombreEquipoGanador(self, nombreEquipoGanador: str):
        self.__nombreEquipoGanador = nombreEquipoGanador

    @property
    def numeroGolesEquipo2(self):
        return self.__numeroGolesEquipo2
    @numeroGolesEquipo2.setter
    def numeroGolesEquipo2(self, numeroGolesEquipo2: int):
        self.__numeroGolesEquipo2 = numeroGolesEquipo2

    @property
    def numeroGolesEquipo1(self):
        return self.__numeroGolesEquipo1
    @numeroGolesEquipo1.setter
    def numeroGolesEquipo1(self, numeroGolesEquipo1: int):
        self.__numeroGolesEquipo1 = numeroGolesEquipo1

    @property
    def partido17(self):
        return self.__partido17
    @partido17.setter
    def partido17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Marcador__partido17", None)
        self.__partido17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "marcador16"):
                opp_val = getattr(old_value, "marcador16", None)
                if opp_val == self:
                    setattr(old_value, "marcador16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "marcador16"):
                opp_val = getattr(value, "marcador16", None)
                setattr(value, "marcador16", self)



class ApuestaEquipoGanador:

    def __init__(self, nombreEquipoGnador: str):
        self.nombreEquipoGnador = nombreEquipoGnador
        
        pass
    @property
    def nombreEquipoGnador(self):
        return self.__nombreEquipoGnador
    @nombreEquipoGnador.setter
    def nombreEquipoGnador(self, nombreEquipoGnador: str):
        self.__nombreEquipoGnador = nombreEquipoGnador



class ApuestaMarcadorEspecifico:

    def __init__(self, nombreEquipoGanador: str, porcentajeAciertoMarcador: str, numeroGolesEquipo1: int, numeroGolesEquipo2: int):
        self.nombreEquipoGanador = nombreEquipoGanador
        self.porcentajeAciertoMarcador = porcentajeAciertoMarcador
        self.numeroGolesEquipo1 = numeroGolesEquipo1
        self.numeroGolesEquipo2 = numeroGolesEquipo2
        
        pass
    @property
    def porcentajeAciertoMarcador(self):
        return self.__porcentajeAciertoMarcador
    @porcentajeAciertoMarcador.setter
    def porcentajeAciertoMarcador(self, porcentajeAciertoMarcador: str):
        self.__porcentajeAciertoMarcador = porcentajeAciertoMarcador

    @property
    def nombreEquipoGanador(self):
        return self.__nombreEquipoGanador
    @nombreEquipoGanador.setter
    def nombreEquipoGanador(self, nombreEquipoGanador: str):
        self.__nombreEquipoGanador = nombreEquipoGanador

    @property
    def numeroGolesEquipo2(self):
        return self.__numeroGolesEquipo2
    @numeroGolesEquipo2.setter
    def numeroGolesEquipo2(self, numeroGolesEquipo2: int):
        self.__numeroGolesEquipo2 = numeroGolesEquipo2

    @property
    def numeroGolesEquipo1(self):
        return self.__numeroGolesEquipo1
    @numeroGolesEquipo1.setter
    def numeroGolesEquipo1(self, numeroGolesEquipo1: int):
        self.__numeroGolesEquipo1 = numeroGolesEquipo1



class Partido:

    def __init__(self, numeroApuestas: str, idPartido: str, apuesta7: set["Apuesta"] = None, eq_18: "Equipo" = None, eq_210: "Equipo" = None, historico15: "Historico" = None, marcador16: "Marcador" = None, sistemaApuesta21: "SistemaApuesta" = None):
        self.numeroApuestas = numeroApuestas
        self.idPartido = idPartido
        self.apuesta7 = apuesta7 if apuesta7 is not None else set()
        self.eq_18 = eq_18
        self.eq_210 = eq_210
        self.historico15 = historico15
        self.marcador16 = marcador16
        self.sistemaApuesta21 = sistemaApuesta21
        
        pass
    @property
    def idPartido(self):
        return self.__idPartido
    @idPartido.setter
    def idPartido(self, idPartido: str):
        self.__idPartido = idPartido

    @property
    def numeroApuestas(self):
        return self.__numeroApuestas
    @numeroApuestas.setter
    def numeroApuestas(self, numeroApuestas: str):
        self.__numeroApuestas = numeroApuestas

    @property
    def apuesta7(self):
        return self.__apuesta7
    @apuesta7.setter
    def apuesta7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Partido__apuesta7", None)
        self.__apuesta7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "partido6"):
                    opp_val = getattr(item, "partido6", None)
                    
                    if opp_val == self:
                        setattr(item, "partido6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "partido6"):
                    opp_val = getattr(item, "partido6", None)
                    
                    setattr(item, "partido6", self)
                    

    @property
    def sistemaApuesta21(self):
        return self.__sistemaApuesta21
    @sistemaApuesta21.setter
    def sistemaApuesta21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Partido__sistemaApuesta21", None)
        self.__sistemaApuesta21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "partido20"):
                opp_val = getattr(old_value, "partido20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "partido20"):
                opp_val = getattr(value, "partido20", None)
                if opp_val is None:
                    setattr(value, "partido20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eq_210(self):
        return self.__eq_210
    @eq_210.setter
    def eq_210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Partido__eq_210", None)
        self.__eq_210 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "partido11"):
                opp_val = getattr(old_value, "partido11", None)
                if opp_val == self:
                    setattr(old_value, "partido11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "partido11"):
                opp_val = getattr(value, "partido11", None)
                setattr(value, "partido11", self)

    @property
    def historico15(self):
        return self.__historico15
    @historico15.setter
    def historico15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Partido__historico15", None)
        self.__historico15 = value
        
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

    @property
    def eq_18(self):
        return self.__eq_18
    @eq_18.setter
    def eq_18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Partido__eq_18", None)
        self.__eq_18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "partido9"):
                opp_val = getattr(old_value, "partido9", None)
                if opp_val == self:
                    setattr(old_value, "partido9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "partido9"):
                opp_val = getattr(value, "partido9", None)
                setattr(value, "partido9", self)

    @property
    def marcador16(self):
        return self.__marcador16
    @marcador16.setter
    def marcador16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Partido__marcador16", None)
        self.__marcador16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "partido17"):
                opp_val = getattr(old_value, "partido17", None)
                if opp_val == self:
                    setattr(old_value, "partido17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "partido17"):
                opp_val = getattr(value, "partido17", None)
                setattr(value, "partido17", self)



class Apuesta:

    def __init__(self, valorApuesta: str, porcentajeGanancia: str, id: str, usuario5: "Usuario" = None, partido6: "Partido" = None, sistemaApuesta19: "SistemaApuesta" = None):
        self.valorApuesta = valorApuesta
        self.porcentajeGanancia = porcentajeGanancia
        self.id = id
        self.usuario5 = usuario5
        self.partido6 = partido6
        self.sistemaApuesta19 = sistemaApuesta19
        
        pass
    @property
    def porcentajeGanancia(self):
        return self.__porcentajeGanancia
    @porcentajeGanancia.setter
    def porcentajeGanancia(self, porcentajeGanancia: str):
        self.__porcentajeGanancia = porcentajeGanancia

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def valorApuesta(self):
        return self.__valorApuesta
    @valorApuesta.setter
    def valorApuesta(self, valorApuesta: str):
        self.__valorApuesta = valorApuesta

    @property
    def usuario5(self):
        return self.__usuario5
    @usuario5.setter
    def usuario5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Apuesta__usuario5", None)
        self.__usuario5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "apuesta4"):
                opp_val = getattr(old_value, "apuesta4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "apuesta4"):
                opp_val = getattr(value, "apuesta4", None)
                if opp_val is None:
                    setattr(value, "apuesta4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sistemaApuesta19(self):
        return self.__sistemaApuesta19
    @sistemaApuesta19.setter
    def sistemaApuesta19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Apuesta__sistemaApuesta19", None)
        self.__sistemaApuesta19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "apuesta18"):
                opp_val = getattr(old_value, "apuesta18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "apuesta18"):
                opp_val = getattr(value, "apuesta18", None)
                if opp_val is None:
                    setattr(value, "apuesta18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def partido6(self):
        return self.__partido6
    @partido6.setter
    def partido6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Apuesta__partido6", None)
        self.__partido6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "apuesta7"):
                opp_val = getattr(old_value, "apuesta7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "apuesta7"):
                opp_val = getattr(value, "apuesta7", None)
                if opp_val is None:
                    setattr(value, "apuesta7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Usuario:

    def __init__(self, userName: str, passWord: str, sistemaApuesta1: "SistemaApuesta" = None, tarjeta2: set["Tarjeta"] = None, apuesta4: set["Apuesta"] = None):
        self.userName = userName
        self.passWord = passWord
        self.sistemaApuesta1 = sistemaApuesta1
        self.tarjeta2 = tarjeta2 if tarjeta2 is not None else set()
        self.apuesta4 = apuesta4 if apuesta4 is not None else set()
        
        pass
    @property
    def userName(self):
        return self.__userName
    @userName.setter
    def userName(self, userName: str):
        self.__userName = userName

    @property
    def passWord(self):
        return self.__passWord
    @passWord.setter
    def passWord(self, passWord: str):
        self.__passWord = passWord

    @property
    def sistemaApuesta1(self):
        return self.__sistemaApuesta1
    @sistemaApuesta1.setter
    def sistemaApuesta1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Usuario__sistemaApuesta1", None)
        self.__sistemaApuesta1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usuario0"):
                opp_val = getattr(old_value, "usuario0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usuario0"):
                opp_val = getattr(value, "usuario0", None)
                if opp_val is None:
                    setattr(value, "usuario0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def apuesta4(self):
        return self.__apuesta4
    @apuesta4.setter
    def apuesta4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Usuario__apuesta4", None)
        self.__apuesta4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "usuario5"):
                    opp_val = getattr(item, "usuario5", None)
                    
                    if opp_val == self:
                        setattr(item, "usuario5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "usuario5"):
                    opp_val = getattr(item, "usuario5", None)
                    
                    setattr(item, "usuario5", self)
                    

    @property
    def tarjeta2(self):
        return self.__tarjeta2
    @tarjeta2.setter
    def tarjeta2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Usuario__tarjeta2", None)
        self.__tarjeta2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "usuario3"):
                    opp_val = getattr(item, "usuario3", None)
                    
                    if opp_val == self:
                        setattr(item, "usuario3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "usuario3"):
                    opp_val = getattr(item, "usuario3", None)
                    
                    setattr(item, "usuario3", self)
                    



class Tarjeta:

    def __init__(self, numeroTarje: int, codigoSeguridad: int, usuario3: "Usuario" = None):
        self.numeroTarje = numeroTarje
        self.codigoSeguridad = codigoSeguridad
        self.usuario3 = usuario3
        
        pass
    @property
    def codigoSeguridad(self):
        return self.__codigoSeguridad
    @codigoSeguridad.setter
    def codigoSeguridad(self, codigoSeguridad: int):
        self.__codigoSeguridad = codigoSeguridad

    @property
    def numeroTarje(self):
        return self.__numeroTarje
    @numeroTarje.setter
    def numeroTarje(self, numeroTarje: int):
        self.__numeroTarje = numeroTarje

    @property
    def usuario3(self):
        return self.__usuario3
    @usuario3.setter
    def usuario3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Tarjeta__usuario3", None)
        self.__usuario3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tarjeta2"):
                opp_val = getattr(old_value, "tarjeta2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tarjeta2"):
                opp_val = getattr(value, "tarjeta2", None)
                if opp_val is None:
                    setattr(value, "tarjeta2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class SistemaApuesta:

    pass
