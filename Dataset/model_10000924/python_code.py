from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Evento:

    def __init__(self, Cod_partido: str, Cod_jugador: str, Cod_TipodeEvento: str, jugador11: "Jugador" = None, partido12: "Partido" = None, tipoDeEvento15: "TipoDeEvento" = None):
        self.Cod_partido = Cod_partido
        self.Cod_jugador = Cod_jugador
        self.Cod_TipodeEvento = Cod_TipodeEvento
        self.jugador11 = jugador11
        self.partido12 = partido12
        self.tipoDeEvento15 = tipoDeEvento15
        
        pass
    @property
    def Cod_partido(self):
        return self.__Cod_partido
    @Cod_partido.setter
    def Cod_partido(self, Cod_partido: str):
        self.__Cod_partido = Cod_partido

    @property
    def Cod_TipodeEvento(self):
        return self.__Cod_TipodeEvento
    @Cod_TipodeEvento.setter
    def Cod_TipodeEvento(self, Cod_TipodeEvento: str):
        self.__Cod_TipodeEvento = Cod_TipodeEvento

    @property
    def Cod_jugador(self):
        return self.__Cod_jugador
    @Cod_jugador.setter
    def Cod_jugador(self, Cod_jugador: str):
        self.__Cod_jugador = Cod_jugador

    @property
    def jugador11(self):
        return self.__jugador11
    @jugador11.setter
    def jugador11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Evento__jugador11", None)
        self.__jugador11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "evento10"):
                opp_val = getattr(old_value, "evento10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "evento10"):
                opp_val = getattr(value, "evento10", None)
                if opp_val is None:
                    setattr(value, "evento10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def partido12(self):
        return self.__partido12
    @partido12.setter
    def partido12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Evento__partido12", None)
        self.__partido12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "evento13"):
                opp_val = getattr(old_value, "evento13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "evento13"):
                opp_val = getattr(value, "evento13", None)
                if opp_val is None:
                    setattr(value, "evento13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tipoDeEvento15(self):
        return self.__tipoDeEvento15
    @tipoDeEvento15.setter
    def tipoDeEvento15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Evento__tipoDeEvento15", None)
        self.__tipoDeEvento15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "evento14"):
                opp_val = getattr(old_value, "evento14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "evento14"):
                opp_val = getattr(value, "evento14", None)
                if opp_val is None:
                    setattr(value, "evento14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Partido:

    def __init__(self, Cod_partido: str, Fecha: str, Hora: str, Local: str, Visita: str, GolLocal: str, GolVisita: str, Ganador: str, Cod_liga: str, estadio4: "Estadio" = None, equipo6: "Equipo" = None, equipo9: "Equipo" = None, evento13: set["Evento"] = None, liga25: "Liga" = None):
        self.Cod_partido = Cod_partido
        self.Fecha = Fecha
        self.Hora = Hora
        self.Local = Local
        self.Visita = Visita
        self.GolLocal = GolLocal
        self.GolVisita = GolVisita
        self.Ganador = Ganador
        self.Cod_liga = Cod_liga
        self.estadio4 = estadio4
        self.equipo6 = equipo6
        self.equipo9 = equipo9
        self.evento13 = evento13 if evento13 is not None else set()
        self.liga25 = liga25
        
        pass
    @property
    def Local(self):
        return self.__Local
    @Local.setter
    def Local(self, Local: str):
        self.__Local = Local

    @property
    def GolVisita(self):
        return self.__GolVisita
    @GolVisita.setter
    def GolVisita(self, GolVisita: str):
        self.__GolVisita = GolVisita

    @property
    def Cod_partido(self):
        return self.__Cod_partido
    @Cod_partido.setter
    def Cod_partido(self, Cod_partido: str):
        self.__Cod_partido = Cod_partido

    @property
    def Visita(self):
        return self.__Visita
    @Visita.setter
    def Visita(self, Visita: str):
        self.__Visita = Visita

    @property
    def Ganador(self):
        return self.__Ganador
    @Ganador.setter
    def Ganador(self, Ganador: str):
        self.__Ganador = Ganador

    @property
    def Hora(self):
        return self.__Hora
    @Hora.setter
    def Hora(self, Hora: str):
        self.__Hora = Hora

    @property
    def GolLocal(self):
        return self.__GolLocal
    @GolLocal.setter
    def GolLocal(self, GolLocal: str):
        self.__GolLocal = GolLocal

    @property
    def Cod_liga(self):
        return self.__Cod_liga
    @Cod_liga.setter
    def Cod_liga(self, Cod_liga: str):
        self.__Cod_liga = Cod_liga

    @property
    def Fecha(self):
        return self.__Fecha
    @Fecha.setter
    def Fecha(self, Fecha: str):
        self.__Fecha = Fecha

    @property
    def liga25(self):
        return self.__liga25
    @liga25.setter
    def liga25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Partido__liga25", None)
        self.__liga25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "partido24"):
                opp_val = getattr(old_value, "partido24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "partido24"):
                opp_val = getattr(value, "partido24", None)
                if opp_val is None:
                    setattr(value, "partido24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def estadio4(self):
        return self.__estadio4
    @estadio4.setter
    def estadio4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Partido__estadio4", None)
        self.__estadio4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "partido5"):
                opp_val = getattr(old_value, "partido5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "partido5"):
                opp_val = getattr(value, "partido5", None)
                if opp_val is None:
                    setattr(value, "partido5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def equipo6(self):
        return self.__equipo6
    @equipo6.setter
    def equipo6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Partido__equipo6", None)
        self.__equipo6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "partido7"):
                opp_val = getattr(old_value, "partido7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "partido7"):
                opp_val = getattr(value, "partido7", None)
                if opp_val is None:
                    setattr(value, "partido7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def equipo9(self):
        return self.__equipo9
    @equipo9.setter
    def equipo9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Partido__equipo9", None)
        self.__equipo9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "partido8"):
                opp_val = getattr(old_value, "partido8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "partido8"):
                opp_val = getattr(value, "partido8", None)
                if opp_val is None:
                    setattr(value, "partido8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def evento13(self):
        return self.__evento13
    @evento13.setter
    def evento13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Partido__evento13", None)
        self.__evento13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "partido12"):
                    opp_val = getattr(item, "partido12", None)
                    
                    if opp_val == self:
                        setattr(item, "partido12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "partido12"):
                    opp_val = getattr(item, "partido12", None)
                    
                    setattr(item, "partido12", self)
                    



class Arbitro:

    def __init__(self, Cod_Arbitro: str, Partidos: str, Cod_persona: str, persona17: "Persona" = None):
        self.Cod_Arbitro = Cod_Arbitro
        self.Partidos = Partidos
        self.Cod_persona = Cod_persona
        self.persona17 = persona17
        
        pass
    @property
    def Partidos(self):
        return self.__Partidos
    @Partidos.setter
    def Partidos(self, Partidos: str):
        self.__Partidos = Partidos

    @property
    def Cod_Arbitro(self):
        return self.__Cod_Arbitro
    @Cod_Arbitro.setter
    def Cod_Arbitro(self, Cod_Arbitro: str):
        self.__Cod_Arbitro = Cod_Arbitro

    @property
    def Cod_persona(self):
        return self.__Cod_persona
    @Cod_persona.setter
    def Cod_persona(self, Cod_persona: str):
        self.__Cod_persona = Cod_persona

    @property
    def persona17(self):
        return self.__persona17
    @persona17.setter
    def persona17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arbitro__persona17", None)
        self.__persona17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arbitro16"):
                opp_val = getattr(old_value, "arbitro16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arbitro16"):
                opp_val = getattr(value, "arbitro16", None)
                if opp_val is None:
                    setattr(value, "arbitro16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Entrenador:

    def __init__(self, Cod_Entrenador: str, Titulos: str, Cod_persona: str, equipo0: "Equipo" = None, persona21: "Persona" = None):
        self.Cod_Entrenador = Cod_Entrenador
        self.Titulos = Titulos
        self.Cod_persona = Cod_persona
        self.equipo0 = equipo0
        self.persona21 = persona21
        
        pass
    @property
    def Cod_persona(self):
        return self.__Cod_persona
    @Cod_persona.setter
    def Cod_persona(self, Cod_persona: str):
        self.__Cod_persona = Cod_persona

    @property
    def Cod_Entrenador(self):
        return self.__Cod_Entrenador
    @Cod_Entrenador.setter
    def Cod_Entrenador(self, Cod_Entrenador: str):
        self.__Cod_Entrenador = Cod_Entrenador

    @property
    def Titulos(self):
        return self.__Titulos
    @Titulos.setter
    def Titulos(self, Titulos: str):
        self.__Titulos = Titulos

    @property
    def persona21(self):
        return self.__persona21
    @persona21.setter
    def persona21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Entrenador__persona21", None)
        self.__persona21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entrenador20"):
                opp_val = getattr(old_value, "entrenador20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entrenador20"):
                opp_val = getattr(value, "entrenador20", None)
                if opp_val is None:
                    setattr(value, "entrenador20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def equipo0(self):
        return self.__equipo0
    @equipo0.setter
    def equipo0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Entrenador__equipo0", None)
        self.__equipo0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entrenador1"):
                opp_val = getattr(old_value, "entrenador1", None)
                if opp_val == self:
                    setattr(old_value, "entrenador1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entrenador1"):
                opp_val = getattr(value, "entrenador1", None)
                setattr(value, "entrenador1", self)



class Jugador:

    def __init__(self, Cod_jugador: str, Dorsal: str, Posicion: str, Altura: str, Peso: str, Titulos: str, Cod_equipo: str, Cod_persona: str, equipo2: "Equipo" = None, evento10: set["Evento"] = None, persona19: "Persona" = None, lesion22: set["Lesion"] = None):
        self.Cod_jugador = Cod_jugador
        self.Dorsal = Dorsal
        self.Posicion = Posicion
        self.Altura = Altura
        self.Peso = Peso
        self.Titulos = Titulos
        self.Cod_equipo = Cod_equipo
        self.Cod_persona = Cod_persona
        self.equipo2 = equipo2
        self.evento10 = evento10 if evento10 is not None else set()
        self.persona19 = persona19
        self.lesion22 = lesion22 if lesion22 is not None else set()
        
        pass
    @property
    def Altura(self):
        return self.__Altura
    @Altura.setter
    def Altura(self, Altura: str):
        self.__Altura = Altura

    @property
    def Posicion(self):
        return self.__Posicion
    @Posicion.setter
    def Posicion(self, Posicion: str):
        self.__Posicion = Posicion

    @property
    def Cod_equipo(self):
        return self.__Cod_equipo
    @Cod_equipo.setter
    def Cod_equipo(self, Cod_equipo: str):
        self.__Cod_equipo = Cod_equipo

    @property
    def Peso(self):
        return self.__Peso
    @Peso.setter
    def Peso(self, Peso: str):
        self.__Peso = Peso

    @property
    def Titulos(self):
        return self.__Titulos
    @Titulos.setter
    def Titulos(self, Titulos: str):
        self.__Titulos = Titulos

    @property
    def Dorsal(self):
        return self.__Dorsal
    @Dorsal.setter
    def Dorsal(self, Dorsal: str):
        self.__Dorsal = Dorsal

    @property
    def Cod_jugador(self):
        return self.__Cod_jugador
    @Cod_jugador.setter
    def Cod_jugador(self, Cod_jugador: str):
        self.__Cod_jugador = Cod_jugador

    @property
    def Cod_persona(self):
        return self.__Cod_persona
    @Cod_persona.setter
    def Cod_persona(self, Cod_persona: str):
        self.__Cod_persona = Cod_persona

    @property
    def equipo2(self):
        return self.__equipo2
    @equipo2.setter
    def equipo2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Jugador__equipo2", None)
        self.__equipo2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jugador3"):
                opp_val = getattr(old_value, "jugador3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jugador3"):
                opp_val = getattr(value, "jugador3", None)
                if opp_val is None:
                    setattr(value, "jugador3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lesion22(self):
        return self.__lesion22
    @lesion22.setter
    def lesion22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Jugador__lesion22", None)
        self.__lesion22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jugador23"):
                    opp_val = getattr(item, "jugador23", None)
                    
                    if opp_val == self:
                        setattr(item, "jugador23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jugador23"):
                    opp_val = getattr(item, "jugador23", None)
                    
                    setattr(item, "jugador23", self)
                    

    @property
    def evento10(self):
        return self.__evento10
    @evento10.setter
    def evento10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Jugador__evento10", None)
        self.__evento10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jugador11"):
                    opp_val = getattr(item, "jugador11", None)
                    
                    if opp_val == self:
                        setattr(item, "jugador11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jugador11"):
                    opp_val = getattr(item, "jugador11", None)
                    
                    setattr(item, "jugador11", self)
                    

    @property
    def persona19(self):
        return self.__persona19
    @persona19.setter
    def persona19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Jugador__persona19", None)
        self.__persona19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jugador18"):
                opp_val = getattr(old_value, "jugador18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jugador18"):
                opp_val = getattr(value, "jugador18", None)
                if opp_val is None:
                    setattr(value, "jugador18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Equipo:

    def __init__(self, Cod_equipo: str, Nombre: str, F_fundacion: str, Ciudad: str, Titulos: str, Cod_Entrenador: str, entrenador1: "Entrenador" = None, jugador3: set["Jugador"] = None, partido7: set["Partido"] = None, partido8: set["Partido"] = None):
        self.Cod_equipo = Cod_equipo
        self.Nombre = Nombre
        self.F_fundacion = F_fundacion
        self.Ciudad = Ciudad
        self.Titulos = Titulos
        self.Cod_Entrenador = Cod_Entrenador
        self.entrenador1 = entrenador1
        self.jugador3 = jugador3 if jugador3 is not None else set()
        self.partido7 = partido7 if partido7 is not None else set()
        self.partido8 = partido8 if partido8 is not None else set()
        
        pass
    @property
    def F_fundacion(self):
        return self.__F_fundacion
    @F_fundacion.setter
    def F_fundacion(self, F_fundacion: str):
        self.__F_fundacion = F_fundacion

    @property
    def Titulos(self):
        return self.__Titulos
    @Titulos.setter
    def Titulos(self, Titulos: str):
        self.__Titulos = Titulos

    @property
    def Cod_equipo(self):
        return self.__Cod_equipo
    @Cod_equipo.setter
    def Cod_equipo(self, Cod_equipo: str):
        self.__Cod_equipo = Cod_equipo

    @property
    def Cod_Entrenador(self):
        return self.__Cod_Entrenador
    @Cod_Entrenador.setter
    def Cod_Entrenador(self, Cod_Entrenador: str):
        self.__Cod_Entrenador = Cod_Entrenador

    @property
    def Nombre(self):
        return self.__Nombre
    @Nombre.setter
    def Nombre(self, Nombre: str):
        self.__Nombre = Nombre

    @property
    def Ciudad(self):
        return self.__Ciudad
    @Ciudad.setter
    def Ciudad(self, Ciudad: str):
        self.__Ciudad = Ciudad

    @property
    def entrenador1(self):
        return self.__entrenador1
    @entrenador1.setter
    def entrenador1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Equipo__entrenador1", None)
        self.__entrenador1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "equipo0"):
                opp_val = getattr(old_value, "equipo0", None)
                if opp_val == self:
                    setattr(old_value, "equipo0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "equipo0"):
                opp_val = getattr(value, "equipo0", None)
                setattr(value, "equipo0", self)

    @property
    def partido8(self):
        return self.__partido8
    @partido8.setter
    def partido8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Equipo__partido8", None)
        self.__partido8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "equipo9"):
                    opp_val = getattr(item, "equipo9", None)
                    
                    if opp_val == self:
                        setattr(item, "equipo9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "equipo9"):
                    opp_val = getattr(item, "equipo9", None)
                    
                    setattr(item, "equipo9", self)
                    

    @property
    def partido7(self):
        return self.__partido7
    @partido7.setter
    def partido7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Equipo__partido7", None)
        self.__partido7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "equipo6"):
                    opp_val = getattr(item, "equipo6", None)
                    
                    if opp_val == self:
                        setattr(item, "equipo6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "equipo6"):
                    opp_val = getattr(item, "equipo6", None)
                    
                    setattr(item, "equipo6", self)
                    

    @property
    def jugador3(self):
        return self.__jugador3
    @jugador3.setter
    def jugador3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Equipo__jugador3", None)
        self.__jugador3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "equipo2"):
                    opp_val = getattr(item, "equipo2", None)
                    
                    if opp_val == self:
                        setattr(item, "equipo2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "equipo2"):
                    opp_val = getattr(item, "equipo2", None)
                    
                    setattr(item, "equipo2", self)
                    



class Estadio:

    def __init__(self, Cod_Estadio: str, Nombre: str, Ubicacion: str, Capacidad: str, Terreno: str, Ubicacion1: str, Cod_equipo: str, partido5: set["Partido"] = None):
        self.Cod_Estadio = Cod_Estadio
        self.Nombre = Nombre
        self.Ubicacion = Ubicacion
        self.Capacidad = Capacidad
        self.Terreno = Terreno
        self.Ubicacion1 = Ubicacion1
        self.Cod_equipo = Cod_equipo
        self.partido5 = partido5 if partido5 is not None else set()
        
        pass
    @property
    def Ubicacion(self):
        return self.__Ubicacion
    @Ubicacion.setter
    def Ubicacion(self, Ubicacion: str):
        self.__Ubicacion = Ubicacion

    @property
    def Terreno(self):
        return self.__Terreno
    @Terreno.setter
    def Terreno(self, Terreno: str):
        self.__Terreno = Terreno

    @property
    def Capacidad(self):
        return self.__Capacidad
    @Capacidad.setter
    def Capacidad(self, Capacidad: str):
        self.__Capacidad = Capacidad

    @property
    def Cod_equipo(self):
        return self.__Cod_equipo
    @Cod_equipo.setter
    def Cod_equipo(self, Cod_equipo: str):
        self.__Cod_equipo = Cod_equipo

    @property
    def Cod_Estadio(self):
        return self.__Cod_Estadio
    @Cod_Estadio.setter
    def Cod_Estadio(self, Cod_Estadio: str):
        self.__Cod_Estadio = Cod_Estadio

    @property
    def Ubicacion1(self):
        return self.__Ubicacion1
    @Ubicacion1.setter
    def Ubicacion1(self, Ubicacion1: str):
        self.__Ubicacion1 = Ubicacion1

    @property
    def Nombre(self):
        return self.__Nombre
    @Nombre.setter
    def Nombre(self, Nombre: str):
        self.__Nombre = Nombre

    @property
    def partido5(self):
        return self.__partido5
    @partido5.setter
    def partido5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Estadio__partido5", None)
        self.__partido5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "estadio4"):
                    opp_val = getattr(item, "estadio4", None)
                    
                    if opp_val == self:
                        setattr(item, "estadio4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "estadio4"):
                    opp_val = getattr(item, "estadio4", None)
                    
                    setattr(item, "estadio4", self)
                    



class Persona:

    def __init__(self, Cod_persona: str, Nombre: str, Apellido: str, NombreCorto: str, FechaNacimiento: str, Nacionalidad: str, arbitro16: set["Arbitro"] = None, jugador18: set["Jugador"] = None, entrenador20: set["Entrenador"] = None):
        self.Cod_persona = Cod_persona
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.NombreCorto = NombreCorto
        self.FechaNacimiento = FechaNacimiento
        self.Nacionalidad = Nacionalidad
        self.arbitro16 = arbitro16 if arbitro16 is not None else set()
        self.jugador18 = jugador18 if jugador18 is not None else set()
        self.entrenador20 = entrenador20 if entrenador20 is not None else set()
        
        pass
    @property
    def NombreCorto(self):
        return self.__NombreCorto
    @NombreCorto.setter
    def NombreCorto(self, NombreCorto: str):
        self.__NombreCorto = NombreCorto

    @property
    def Cod_persona(self):
        return self.__Cod_persona
    @Cod_persona.setter
    def Cod_persona(self, Cod_persona: str):
        self.__Cod_persona = Cod_persona

    @property
    def Apellido(self):
        return self.__Apellido
    @Apellido.setter
    def Apellido(self, Apellido: str):
        self.__Apellido = Apellido

    @property
    def Nacionalidad(self):
        return self.__Nacionalidad
    @Nacionalidad.setter
    def Nacionalidad(self, Nacionalidad: str):
        self.__Nacionalidad = Nacionalidad

    @property
    def FechaNacimiento(self):
        return self.__FechaNacimiento
    @FechaNacimiento.setter
    def FechaNacimiento(self, FechaNacimiento: str):
        self.__FechaNacimiento = FechaNacimiento

    @property
    def Nombre(self):
        return self.__Nombre
    @Nombre.setter
    def Nombre(self, Nombre: str):
        self.__Nombre = Nombre

    @property
    def jugador18(self):
        return self.__jugador18
    @jugador18.setter
    def jugador18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Persona__jugador18", None)
        self.__jugador18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "persona19"):
                    opp_val = getattr(item, "persona19", None)
                    
                    if opp_val == self:
                        setattr(item, "persona19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "persona19"):
                    opp_val = getattr(item, "persona19", None)
                    
                    setattr(item, "persona19", self)
                    

    @property
    def entrenador20(self):
        return self.__entrenador20
    @entrenador20.setter
    def entrenador20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Persona__entrenador20", None)
        self.__entrenador20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "persona21"):
                    opp_val = getattr(item, "persona21", None)
                    
                    if opp_val == self:
                        setattr(item, "persona21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "persona21"):
                    opp_val = getattr(item, "persona21", None)
                    
                    setattr(item, "persona21", self)
                    

    @property
    def arbitro16(self):
        return self.__arbitro16
    @arbitro16.setter
    def arbitro16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Persona__arbitro16", None)
        self.__arbitro16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "persona17"):
                    opp_val = getattr(item, "persona17", None)
                    
                    if opp_val == self:
                        setattr(item, "persona17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "persona17"):
                    opp_val = getattr(item, "persona17", None)
                    
                    setattr(item, "persona17", self)
                    



class Clasificacion:

    def __init__(self, Cod_Equipo: str, Posicion: str, JJ: str, JP: str, JE: str, JG: str, GF: str, GC: str, DG: str, Puntos: str, liga27: set["Liga"] = None):
        self.Cod_Equipo = Cod_Equipo
        self.Posicion = Posicion
        self.JJ = JJ
        self.JP = JP
        self.JE = JE
        self.JG = JG
        self.GF = GF
        self.GC = GC
        self.DG = DG
        self.Puntos = Puntos
        self.liga27 = liga27 if liga27 is not None else set()
        
        pass
    @property
    def JE(self):
        return self.__JE
    @JE.setter
    def JE(self, JE: str):
        self.__JE = JE

    @property
    def JG(self):
        return self.__JG
    @JG.setter
    def JG(self, JG: str):
        self.__JG = JG

    @property
    def Posicion(self):
        return self.__Posicion
    @Posicion.setter
    def Posicion(self, Posicion: str):
        self.__Posicion = Posicion

    @property
    def GC(self):
        return self.__GC
    @GC.setter
    def GC(self, GC: str):
        self.__GC = GC

    @property
    def Cod_Equipo(self):
        return self.__Cod_Equipo
    @Cod_Equipo.setter
    def Cod_Equipo(self, Cod_Equipo: str):
        self.__Cod_Equipo = Cod_Equipo

    @property
    def Puntos(self):
        return self.__Puntos
    @Puntos.setter
    def Puntos(self, Puntos: str):
        self.__Puntos = Puntos

    @property
    def GF(self):
        return self.__GF
    @GF.setter
    def GF(self, GF: str):
        self.__GF = GF

    @property
    def JJ(self):
        return self.__JJ
    @JJ.setter
    def JJ(self, JJ: str):
        self.__JJ = JJ

    @property
    def DG(self):
        return self.__DG
    @DG.setter
    def DG(self, DG: str):
        self.__DG = DG

    @property
    def JP(self):
        return self.__JP
    @JP.setter
    def JP(self, JP: str):
        self.__JP = JP

    @property
    def liga27(self):
        return self.__liga27
    @liga27.setter
    def liga27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Clasificacion__liga27", None)
        self.__liga27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "clasificacion26"):
                    opp_val = getattr(item, "clasificacion26", None)
                    
                    if opp_val == self:
                        setattr(item, "clasificacion26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "clasificacion26"):
                    opp_val = getattr(item, "clasificacion26", None)
                    
                    setattr(item, "clasificacion26", self)
                    



class Liga:

    def __init__(self, Cod_liga: str, Nombre: str, Num_equipos: str, Superior: str, Inferior: str, Cod_Clasificacion: str, partido24: set["Partido"] = None, clasificacion26: "Clasificacion" = None):
        self.Cod_liga = Cod_liga
        self.Nombre = Nombre
        self.Num_equipos = Num_equipos
        self.Superior = Superior
        self.Inferior = Inferior
        self.Cod_Clasificacion = Cod_Clasificacion
        self.partido24 = partido24 if partido24 is not None else set()
        self.clasificacion26 = clasificacion26
        
        pass
    @property
    def Nombre(self):
        return self.__Nombre
    @Nombre.setter
    def Nombre(self, Nombre: str):
        self.__Nombre = Nombre

    @property
    def Inferior(self):
        return self.__Inferior
    @Inferior.setter
    def Inferior(self, Inferior: str):
        self.__Inferior = Inferior

    @property
    def Cod_Clasificacion(self):
        return self.__Cod_Clasificacion
    @Cod_Clasificacion.setter
    def Cod_Clasificacion(self, Cod_Clasificacion: str):
        self.__Cod_Clasificacion = Cod_Clasificacion

    @property
    def Num_equipos(self):
        return self.__Num_equipos
    @Num_equipos.setter
    def Num_equipos(self, Num_equipos: str):
        self.__Num_equipos = Num_equipos

    @property
    def Superior(self):
        return self.__Superior
    @Superior.setter
    def Superior(self, Superior: str):
        self.__Superior = Superior

    @property
    def Cod_liga(self):
        return self.__Cod_liga
    @Cod_liga.setter
    def Cod_liga(self, Cod_liga: str):
        self.__Cod_liga = Cod_liga

    @property
    def partido24(self):
        return self.__partido24
    @partido24.setter
    def partido24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Liga__partido24", None)
        self.__partido24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "liga25"):
                    opp_val = getattr(item, "liga25", None)
                    
                    if opp_val == self:
                        setattr(item, "liga25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "liga25"):
                    opp_val = getattr(item, "liga25", None)
                    
                    setattr(item, "liga25", self)
                    

    @property
    def clasificacion26(self):
        return self.__clasificacion26
    @clasificacion26.setter
    def clasificacion26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Liga__clasificacion26", None)
        self.__clasificacion26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "liga27"):
                opp_val = getattr(old_value, "liga27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "liga27"):
                opp_val = getattr(value, "liga27", None)
                if opp_val is None:
                    setattr(value, "liga27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Lesion:

    def __init__(self, Cod_jugador: str, FechaLesion: str, TiempoLesion: str, Condicion: str, jugador23: "Jugador" = None):
        self.Cod_jugador = Cod_jugador
        self.FechaLesion = FechaLesion
        self.TiempoLesion = TiempoLesion
        self.Condicion = Condicion
        self.jugador23 = jugador23
        
        pass
    @property
    def Condicion(self):
        return self.__Condicion
    @Condicion.setter
    def Condicion(self, Condicion: str):
        self.__Condicion = Condicion

    @property
    def Cod_jugador(self):
        return self.__Cod_jugador
    @Cod_jugador.setter
    def Cod_jugador(self, Cod_jugador: str):
        self.__Cod_jugador = Cod_jugador

    @property
    def FechaLesion(self):
        return self.__FechaLesion
    @FechaLesion.setter
    def FechaLesion(self, FechaLesion: str):
        self.__FechaLesion = FechaLesion

    @property
    def TiempoLesion(self):
        return self.__TiempoLesion
    @TiempoLesion.setter
    def TiempoLesion(self, TiempoLesion: str):
        self.__TiempoLesion = TiempoLesion

    @property
    def jugador23(self):
        return self.__jugador23
    @jugador23.setter
    def jugador23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Lesion__jugador23", None)
        self.__jugador23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lesion22"):
                opp_val = getattr(old_value, "lesion22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lesion22"):
                opp_val = getattr(value, "lesion22", None)
                if opp_val is None:
                    setattr(value, "lesion22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class TipoDeEvento:

    def __init__(self, Cod_TipodeEvento: str, Evento: str, evento14: set["Evento"] = None):
        self.Cod_TipodeEvento = Cod_TipodeEvento
        self.Evento = Evento
        self.evento14 = evento14 if evento14 is not None else set()
        
        pass
    @property
    def Evento(self):
        return self.__Evento
    @Evento.setter
    def Evento(self, Evento: str):
        self.__Evento = Evento

    @property
    def Cod_TipodeEvento(self):
        return self.__Cod_TipodeEvento
    @Cod_TipodeEvento.setter
    def Cod_TipodeEvento(self, Cod_TipodeEvento: str):
        self.__Cod_TipodeEvento = Cod_TipodeEvento

    @property
    def evento14(self):
        return self.__evento14
    @evento14.setter
    def evento14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TipoDeEvento__evento14", None)
        self.__evento14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tipoDeEvento15"):
                    opp_val = getattr(item, "tipoDeEvento15", None)
                    
                    if opp_val == self:
                        setattr(item, "tipoDeEvento15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tipoDeEvento15"):
                    opp_val = getattr(item, "tipoDeEvento15", None)
                    
                    setattr(item, "tipoDeEvento15", self)
                    

