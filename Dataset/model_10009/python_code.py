from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Nombramiento(Enum):
    medioTiempo = "medioTiempo"
    tiempoCompleto = "tiempoCompleto"


############################################
# Definition of Classes
############################################

class itculiacan_Universidad:

    pass
class itculiacan_Profesor:

    def __init__(self, clave: int, nombre: str, numeroMaterias: int, nombramiento: str, Profesor: "itculiacan_Grupo" = None, profesor: set["itculiacan_Grupo"] = None, itculiacan_Profesor: "itculiacan_Universidad" = None):
        self.clave = clave
        self.nombre = nombre
        self.numeroMaterias = numeroMaterias
        self.nombramiento = nombramiento
        self.Profesor = Profesor
        self.profesor = profesor if profesor is not None else set()
        self.itculiacan_Profesor = itculiacan_Profesor
        
        pass
    @property
    def nombramiento(self):
        return self.__nombramiento

    @nombramiento.setter
    def nombramiento(self, nombramiento: str):
        self.__nombramiento = nombramiento


    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre


    @property
    def numeroMaterias(self):
        return self.__numeroMaterias

    @numeroMaterias.setter
    def numeroMaterias(self, numeroMaterias: int):
        self.__numeroMaterias = numeroMaterias


    @property
    def clave(self):
        return self.__clave

    @clave.setter
    def clave(self, clave: int):
        self.__clave = clave


    @property
    def profesor(self):
        return self.__profesor

    @profesor.setter
    def profesor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itculiacan_Profesor__profesor", None)
        self.__profesor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Grupo21"):
                    opp_val = getattr(item, "Grupo21", None)
                    
                    if opp_val == self:
                        setattr(item, "Grupo21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Grupo21"):
                    opp_val = getattr(item, "Grupo21", None)
                    
                    setattr(item, "Grupo21", self)
                    

    @property
    def itculiacan_Profesor(self):
        return self.__itculiacan_Profesor

    @itculiacan_Profesor.setter
    def itculiacan_Profesor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itculiacan_Profesor__itculiacan_Profesor", None)
        self.__itculiacan_Profesor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "itculiacan_Universidad"):
                opp_val = getattr(old_value, "itculiacan_Universidad", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "itculiacan_Universidad"):
                opp_val = getattr(value, "itculiacan_Universidad", None)
                if opp_val is None:
                    setattr(value, "itculiacan_Universidad", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Profesor(self):
        return self.__Profesor

    @Profesor.setter
    def Profesor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itculiacan_Profesor__Profesor", None)
        self.__Profesor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "grupos10"):
                opp_val = getattr(old_value, "grupos10", None)
                if opp_val == self:
                    setattr(old_value, "grupos10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "grupos10"):
                opp_val = getattr(value, "grupos10", None)
                setattr(value, "grupos10", self)

class itculiacan_Materia:

    def __init__(self, clave: int, nombre: str, Materia: "itculiacan_Grupo" = None, materia: set["itculiacan_Grupo"] = None, materias: set["itculiacan_PlanEstudio"] = None, Materia25: "itculiacan_PlanEstudio" = None, itculiacan_Materia: "itculiacan_Universidad" = None):
        self.clave = clave
        self.nombre = nombre
        self.Materia = Materia
        self.materia = materia if materia is not None else set()
        self.materias = materias if materias is not None else set()
        self.Materia25 = Materia25
        self.itculiacan_Materia = itculiacan_Materia
        
        pass
    @property
    def clave(self):
        return self.__clave

    @clave.setter
    def clave(self, clave: int):
        self.__clave = clave


    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre


    @property
    def Materia(self):
        return self.__Materia

    @Materia.setter
    def Materia(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itculiacan_Materia__Materia", None)
        self.__Materia = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "grupos8"):
                opp_val = getattr(old_value, "grupos8", None)
                if opp_val == self:
                    setattr(old_value, "grupos8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "grupos8"):
                opp_val = getattr(value, "grupos8", None)
                setattr(value, "grupos8", self)

    @property
    def itculiacan_Materia(self):
        return self.__itculiacan_Materia

    @itculiacan_Materia.setter
    def itculiacan_Materia(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itculiacan_Materia__itculiacan_Materia", None)
        self.__itculiacan_Materia = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "itculiacan_Universidad36"):
                opp_val = getattr(old_value, "itculiacan_Universidad36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "itculiacan_Universidad36"):
                opp_val = getattr(value, "itculiacan_Universidad36", None)
                if opp_val is None:
                    setattr(value, "itculiacan_Universidad36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Materia25(self):
        return self.__Materia25

    @Materia25.setter
    def Materia25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itculiacan_Materia__Materia25", None)
        self.__Materia25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "planesEstudio"):
                opp_val = getattr(old_value, "planesEstudio", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "planesEstudio"):
                opp_val = getattr(value, "planesEstudio", None)
                if opp_val is None:
                    setattr(value, "planesEstudio", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def materia(self):
        return self.__materia

    @materia.setter
    def materia(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itculiacan_Materia__materia", None)
        self.__materia = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Grupo17"):
                    opp_val = getattr(item, "Grupo17", None)
                    
                    if opp_val == self:
                        setattr(item, "Grupo17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Grupo17"):
                    opp_val = getattr(item, "Grupo17", None)
                    
                    setattr(item, "Grupo17", self)
                    

    @property
    def materias(self):
        return self.__materias

    @materias.setter
    def materias(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itculiacan_Materia__materias", None)
        self.__materias = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PlanEstudio19"):
                    opp_val = getattr(item, "PlanEstudio19", None)
                    
                    if opp_val == self:
                        setattr(item, "PlanEstudio19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PlanEstudio19"):
                    opp_val = getattr(item, "PlanEstudio19", None)
                    
                    setattr(item, "PlanEstudio19", self)
                    

class itculiacan_Aula:

    def __init__(self, clave: int, capacidad: int, Aula: "itculiacan_Grupo" = None, aula: set["itculiacan_Grupo"] = None, itculiacan_Aula: "itculiacan_Universidad" = None):
        self.clave = clave
        self.capacidad = capacidad
        self.Aula = Aula
        self.aula = aula if aula is not None else set()
        self.itculiacan_Aula = itculiacan_Aula
        
        pass
    @property
    def capacidad(self):
        return self.__capacidad

    @capacidad.setter
    def capacidad(self, capacidad: int):
        self.__capacidad = capacidad


    @property
    def clave(self):
        return self.__clave

    @clave.setter
    def clave(self, clave: int):
        self.__clave = clave


    @property
    def Aula(self):
        return self.__Aula

    @Aula.setter
    def Aula(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itculiacan_Aula__Aula", None)
        self.__Aula = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "grupos"):
                opp_val = getattr(old_value, "grupos", None)
                if opp_val == self:
                    setattr(old_value, "grupos", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "grupos"):
                opp_val = getattr(value, "grupos", None)
                setattr(value, "grupos", self)

    @property
    def itculiacan_Aula(self):
        return self.__itculiacan_Aula

    @itculiacan_Aula.setter
    def itculiacan_Aula(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itculiacan_Aula__itculiacan_Aula", None)
        self.__itculiacan_Aula = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "itculiacan_Universidad28"):
                opp_val = getattr(old_value, "itculiacan_Universidad28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "itculiacan_Universidad28"):
                opp_val = getattr(value, "itculiacan_Universidad28", None)
                if opp_val is None:
                    setattr(value, "itculiacan_Universidad28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aula(self):
        return self.__aula

    @aula.setter
    def aula(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itculiacan_Aula__aula", None)
        self.__aula = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Grupo15"):
                    opp_val = getattr(item, "Grupo15", None)
                    
                    if opp_val == self:
                        setattr(item, "Grupo15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Grupo15"):
                    opp_val = getattr(item, "Grupo15", None)
                    
                    setattr(item, "Grupo15", self)
                    

class itculiacan_Grupo:

    def __init__(self, clave: int, Grupo: "itculiacan_Alumno" = None, grupos: "itculiacan_Aula" = None, grupos8: "itculiacan_Materia" = None, grupos10: "itculiacan_Profesor" = None, grupos12: set["itculiacan_Alumno"] = None, Grupo15: "itculiacan_Aula" = None, Grupo17: "itculiacan_Materia" = None, Grupo21: "itculiacan_Profesor" = None, itculiacan_Grupo: "itculiacan_Universidad" = None):
        self.clave = clave
        self.Grupo = Grupo
        self.grupos = grupos
        self.grupos8 = grupos8
        self.grupos10 = grupos10
        self.grupos12 = grupos12 if grupos12 is not None else set()
        self.Grupo15 = Grupo15
        self.Grupo17 = Grupo17
        self.Grupo21 = Grupo21
        self.itculiacan_Grupo = itculiacan_Grupo
        
        pass
    @property
    def clave(self):
        return self.__clave

    @clave.setter
    def clave(self, clave: int):
        self.__clave = clave


    @property
    def Grupo21(self):
        return self.__Grupo21

    @Grupo21.setter
    def Grupo21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itculiacan_Grupo__Grupo21", None)
        self.__Grupo21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profesor"):
                opp_val = getattr(old_value, "profesor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profesor"):
                opp_val = getattr(value, "profesor", None)
                if opp_val is None:
                    setattr(value, "profesor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def grupos8(self):
        return self.__grupos8

    @grupos8.setter
    def grupos8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itculiacan_Grupo__grupos8", None)
        self.__grupos8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Materia"):
                opp_val = getattr(old_value, "Materia", None)
                if opp_val == self:
                    setattr(old_value, "Materia", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Materia"):
                opp_val = getattr(value, "Materia", None)
                setattr(value, "Materia", self)

    @property
    def grupos(self):
        return self.__grupos

    @grupos.setter
    def grupos(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itculiacan_Grupo__grupos", None)
        self.__grupos = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Aula"):
                opp_val = getattr(old_value, "Aula", None)
                if opp_val == self:
                    setattr(old_value, "Aula", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Aula"):
                opp_val = getattr(value, "Aula", None)
                setattr(value, "Aula", self)

    @property
    def Grupo(self):
        return self.__Grupo

    @Grupo.setter
    def Grupo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itculiacan_Grupo__Grupo", None)
        self.__Grupo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alumnos4"):
                opp_val = getattr(old_value, "alumnos4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alumnos4"):
                opp_val = getattr(value, "alumnos4", None)
                if opp_val is None:
                    setattr(value, "alumnos4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Grupo15(self):
        return self.__Grupo15

    @Grupo15.setter
    def Grupo15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itculiacan_Grupo__Grupo15", None)
        self.__Grupo15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aula"):
                opp_val = getattr(old_value, "aula", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aula"):
                opp_val = getattr(value, "aula", None)
                if opp_val is None:
                    setattr(value, "aula", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Grupo17(self):
        return self.__Grupo17

    @Grupo17.setter
    def Grupo17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itculiacan_Grupo__Grupo17", None)
        self.__Grupo17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "materia"):
                opp_val = getattr(old_value, "materia", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "materia"):
                opp_val = getattr(value, "materia", None)
                if opp_val is None:
                    setattr(value, "materia", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def itculiacan_Grupo(self):
        return self.__itculiacan_Grupo

    @itculiacan_Grupo.setter
    def itculiacan_Grupo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itculiacan_Grupo__itculiacan_Grupo", None)
        self.__itculiacan_Grupo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "itculiacan_Universidad38"):
                opp_val = getattr(old_value, "itculiacan_Universidad38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "itculiacan_Universidad38"):
                opp_val = getattr(value, "itculiacan_Universidad38", None)
                if opp_val is None:
                    setattr(value, "itculiacan_Universidad38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def grupos10(self):
        return self.__grupos10

    @grupos10.setter
    def grupos10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itculiacan_Grupo__grupos10", None)
        self.__grupos10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Profesor"):
                opp_val = getattr(old_value, "Profesor", None)
                if opp_val == self:
                    setattr(old_value, "Profesor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Profesor"):
                opp_val = getattr(value, "Profesor", None)
                setattr(value, "Profesor", self)

    @property
    def grupos12(self):
        return self.__grupos12

    @grupos12.setter
    def grupos12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itculiacan_Grupo__grupos12", None)
        self.__grupos12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Alumno13"):
                    opp_val = getattr(item, "Alumno13", None)
                    
                    if opp_val == self:
                        setattr(item, "Alumno13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Alumno13"):
                    opp_val = getattr(item, "Alumno13", None)
                    
                    setattr(item, "Alumno13", self)
                    

class itculiacan_PlanEstudio:

    def __init__(self, clave: int, nombre: str, PlanEstudio: "itculiacan_Alumno" = None, PlanEstudio19: "itculiacan_Materia" = None, cursa: set["itculiacan_Alumno"] = None, planesEstudio: set["itculiacan_Materia"] = None, itculiacan_PlanEstudio: "itculiacan_Universidad" = None):
        self.clave = clave
        self.nombre = nombre
        self.PlanEstudio = PlanEstudio
        self.PlanEstudio19 = PlanEstudio19
        self.cursa = cursa if cursa is not None else set()
        self.planesEstudio = planesEstudio if planesEstudio is not None else set()
        self.itculiacan_PlanEstudio = itculiacan_PlanEstudio
        
        pass
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre


    @property
    def clave(self):
        return self.__clave

    @clave.setter
    def clave(self, clave: int):
        self.__clave = clave


    @property
    def itculiacan_PlanEstudio(self):
        return self.__itculiacan_PlanEstudio

    @itculiacan_PlanEstudio.setter
    def itculiacan_PlanEstudio(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itculiacan_PlanEstudio__itculiacan_PlanEstudio", None)
        self.__itculiacan_PlanEstudio = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "itculiacan_Universidad30"):
                opp_val = getattr(old_value, "itculiacan_Universidad30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "itculiacan_Universidad30"):
                opp_val = getattr(value, "itculiacan_Universidad30", None)
                if opp_val is None:
                    setattr(value, "itculiacan_Universidad30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PlanEstudio19(self):
        return self.__PlanEstudio19

    @PlanEstudio19.setter
    def PlanEstudio19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itculiacan_PlanEstudio__PlanEstudio19", None)
        self.__PlanEstudio19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "materias"):
                opp_val = getattr(old_value, "materias", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "materias"):
                opp_val = getattr(value, "materias", None)
                if opp_val is None:
                    setattr(value, "materias", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PlanEstudio(self):
        return self.__PlanEstudio

    @PlanEstudio.setter
    def PlanEstudio(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itculiacan_PlanEstudio__PlanEstudio", None)
        self.__PlanEstudio = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alumnos2"):
                opp_val = getattr(old_value, "alumnos2", None)
                if opp_val == self:
                    setattr(old_value, "alumnos2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alumnos2"):
                opp_val = getattr(value, "alumnos2", None)
                setattr(value, "alumnos2", self)

    @property
    def cursa(self):
        return self.__cursa

    @cursa.setter
    def cursa(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itculiacan_PlanEstudio__cursa", None)
        self.__cursa = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Alumno23"):
                    opp_val = getattr(item, "Alumno23", None)
                    
                    if opp_val == self:
                        setattr(item, "Alumno23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Alumno23"):
                    opp_val = getattr(item, "Alumno23", None)
                    
                    setattr(item, "Alumno23", self)
                    

    @property
    def planesEstudio(self):
        return self.__planesEstudio

    @planesEstudio.setter
    def planesEstudio(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itculiacan_PlanEstudio__planesEstudio", None)
        self.__planesEstudio = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Materia25"):
                    opp_val = getattr(item, "Materia25", None)
                    
                    if opp_val == self:
                        setattr(item, "Materia25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Materia25"):
                    opp_val = getattr(item, "Materia25", None)
                    
                    setattr(item, "Materia25", self)
                    

class itculiacan_Generacion:

    def __init__(self, fechaInicio: date, fechaFin: date, Generacion: "itculiacan_Alumno" = None, generacion: set["itculiacan_Alumno"] = None, itculiacan_Generacion: "itculiacan_Universidad" = None):
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.Generacion = Generacion
        self.generacion = generacion if generacion is not None else set()
        self.itculiacan_Generacion = itculiacan_Generacion
        
        pass
    @property
    def fechaFin(self):
        return self.__fechaFin

    @fechaFin.setter
    def fechaFin(self, fechaFin: date):
        self.__fechaFin = fechaFin


    @property
    def fechaInicio(self):
        return self.__fechaInicio

    @fechaInicio.setter
    def fechaInicio(self, fechaInicio: date):
        self.__fechaInicio = fechaInicio


    @property
    def itculiacan_Generacion(self):
        return self.__itculiacan_Generacion

    @itculiacan_Generacion.setter
    def itculiacan_Generacion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itculiacan_Generacion__itculiacan_Generacion", None)
        self.__itculiacan_Generacion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "itculiacan_Universidad34"):
                opp_val = getattr(old_value, "itculiacan_Universidad34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "itculiacan_Universidad34"):
                opp_val = getattr(value, "itculiacan_Universidad34", None)
                if opp_val is None:
                    setattr(value, "itculiacan_Universidad34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Generacion(self):
        return self.__Generacion

    @Generacion.setter
    def Generacion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itculiacan_Generacion__Generacion", None)
        self.__Generacion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alumnos"):
                opp_val = getattr(old_value, "alumnos", None)
                if opp_val == self:
                    setattr(old_value, "alumnos", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alumnos"):
                opp_val = getattr(value, "alumnos", None)
                setattr(value, "alumnos", self)

    @property
    def generacion(self):
        return self.__generacion

    @generacion.setter
    def generacion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itculiacan_Generacion__generacion", None)
        self.__generacion = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Alumno"):
                    opp_val = getattr(item, "Alumno", None)
                    
                    if opp_val == self:
                        setattr(item, "Alumno", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Alumno"):
                    opp_val = getattr(item, "Alumno", None)
                    
                    setattr(item, "Alumno", self)
                    

class itculiacan_Alumno:

    def __init__(self, nombre: str, numeroControl: int, alumnos: "itculiacan_Generacion" = None, alumnos2: "itculiacan_PlanEstudio" = None, alumnos4: set["itculiacan_Grupo"] = None, Alumno: "itculiacan_Generacion" = None, Alumno13: "itculiacan_Grupo" = None, Alumno23: "itculiacan_PlanEstudio" = None, itculiacan_Alumno: "itculiacan_Universidad" = None):
        self.nombre = nombre
        self.numeroControl = numeroControl
        self.alumnos = alumnos
        self.alumnos2 = alumnos2
        self.alumnos4 = alumnos4 if alumnos4 is not None else set()
        self.Alumno = Alumno
        self.Alumno13 = Alumno13
        self.Alumno23 = Alumno23
        self.itculiacan_Alumno = itculiacan_Alumno
        
        pass
    @property
    def numeroControl(self):
        return self.__numeroControl

    @numeroControl.setter
    def numeroControl(self, numeroControl: int):
        self.__numeroControl = numeroControl


    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre


    @property
    def alumnos2(self):
        return self.__alumnos2

    @alumnos2.setter
    def alumnos2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itculiacan_Alumno__alumnos2", None)
        self.__alumnos2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PlanEstudio"):
                opp_val = getattr(old_value, "PlanEstudio", None)
                if opp_val == self:
                    setattr(old_value, "PlanEstudio", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PlanEstudio"):
                opp_val = getattr(value, "PlanEstudio", None)
                setattr(value, "PlanEstudio", self)

    @property
    def Alumno(self):
        return self.__Alumno

    @Alumno.setter
    def Alumno(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itculiacan_Alumno__Alumno", None)
        self.__Alumno = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generacion"):
                opp_val = getattr(old_value, "generacion", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generacion"):
                opp_val = getattr(value, "generacion", None)
                if opp_val is None:
                    setattr(value, "generacion", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def alumnos(self):
        return self.__alumnos

    @alumnos.setter
    def alumnos(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itculiacan_Alumno__alumnos", None)
        self.__alumnos = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Generacion"):
                opp_val = getattr(old_value, "Generacion", None)
                if opp_val == self:
                    setattr(old_value, "Generacion", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Generacion"):
                opp_val = getattr(value, "Generacion", None)
                setattr(value, "Generacion", self)

    @property
    def Alumno23(self):
        return self.__Alumno23

    @Alumno23.setter
    def Alumno23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itculiacan_Alumno__Alumno23", None)
        self.__Alumno23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cursa"):
                opp_val = getattr(old_value, "cursa", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cursa"):
                opp_val = getattr(value, "cursa", None)
                if opp_val is None:
                    setattr(value, "cursa", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Alumno13(self):
        return self.__Alumno13

    @Alumno13.setter
    def Alumno13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itculiacan_Alumno__Alumno13", None)
        self.__Alumno13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "grupos12"):
                opp_val = getattr(old_value, "grupos12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "grupos12"):
                opp_val = getattr(value, "grupos12", None)
                if opp_val is None:
                    setattr(value, "grupos12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def alumnos4(self):
        return self.__alumnos4

    @alumnos4.setter
    def alumnos4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itculiacan_Alumno__alumnos4", None)
        self.__alumnos4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Grupo"):
                    opp_val = getattr(item, "Grupo", None)
                    
                    if opp_val == self:
                        setattr(item, "Grupo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Grupo"):
                    opp_val = getattr(item, "Grupo", None)
                    
                    setattr(item, "Grupo", self)
                    

    @property
    def itculiacan_Alumno(self):
        return self.__itculiacan_Alumno

    @itculiacan_Alumno.setter
    def itculiacan_Alumno(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itculiacan_Alumno__itculiacan_Alumno", None)
        self.__itculiacan_Alumno = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "itculiacan_Universidad32"):
                opp_val = getattr(old_value, "itculiacan_Universidad32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "itculiacan_Universidad32"):
                opp_val = getattr(value, "itculiacan_Universidad32", None)
                if opp_val is None:
                    setattr(value, "itculiacan_Universidad32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
