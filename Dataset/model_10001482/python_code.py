from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class BenannteEinrichtung:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name



class Deck:

    def __init__(self, sektion: str, fahrtWunsch: bool, toDelete3: set["Kabine"] = None, toDelete5: set["Kabine"] = None, toDelete7: set["TurboliftSchacht"] = None):
        self.sektion = sektion
        self.fahrtWunsch = fahrtWunsch
        self.toDelete3 = toDelete3 if toDelete3 is not None else set()
        self.toDelete5 = toDelete5 if toDelete5 is not None else set()
        self.toDelete7 = toDelete7 if toDelete7 is not None else set()
        
        pass
    @property
    def sektion(self):
        return self.__sektion
    @sektion.setter
    def sektion(self, sektion: str):
        self.__sektion = sektion

    @property
    def fahrtWunsch(self):
        return self.__fahrtWunsch
    @fahrtWunsch.setter
    def fahrtWunsch(self, fahrtWunsch: bool):
        self.__fahrtWunsch = fahrtWunsch

    @property
    def toDelete3(self):
        return self.__toDelete3
    @toDelete3.setter
    def toDelete3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__toDelete3", None)
        self.__toDelete3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "position2"):
                    opp_val = getattr(item, "position2", None)
                    
                    if opp_val == self:
                        setattr(item, "position2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "position2"):
                    opp_val = getattr(item, "position2", None)
                    
                    setattr(item, "position2", self)
                    

    @property
    def toDelete5(self):
        return self.__toDelete5
    @toDelete5.setter
    def toDelete5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__toDelete5", None)
        self.__toDelete5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fahrtziele4"):
                    opp_val = getattr(item, "fahrtziele4", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fahrtziele4"):
                    opp_val = getattr(item, "fahrtziele4", None)
                    
                    if opp_val is None:
                        setattr(item, "fahrtziele4", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def toDelete7(self):
        return self.__toDelete7
    @toDelete7.setter
    def toDelete7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__toDelete7", None)
        self.__toDelete7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "decks6"):
                    opp_val = getattr(item, "decks6", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "decks6"):
                    opp_val = getattr(item, "decks6", None)
                    
                    if opp_val is None:
                        setattr(item, "decks6", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Kabine:

    def __init__(self, tuerZustand: bool, position2: "Deck" = None, fahrtziele4: set["Deck"] = None, toDelete15: "TurboliftSchacht" = None):
        self.tuerZustand = tuerZustand
        self.position2 = position2
        self.fahrtziele4 = fahrtziele4 if fahrtziele4 is not None else set()
        self.toDelete15 = toDelete15
        
        pass
    @property
    def tuerZustand(self):
        return self.__tuerZustand
    @tuerZustand.setter
    def tuerZustand(self, tuerZustand: bool):
        self.__tuerZustand = tuerZustand

    @property
    def fahrtziele4(self):
        return self.__fahrtziele4
    @fahrtziele4.setter
    def fahrtziele4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kabine__fahrtziele4", None)
        self.__fahrtziele4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "toDelete5"):
                    opp_val = getattr(item, "toDelete5", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "toDelete5"):
                    opp_val = getattr(item, "toDelete5", None)
                    
                    if opp_val is None:
                        setattr(item, "toDelete5", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def toDelete15(self):
        return self.__toDelete15
    @toDelete15.setter
    def toDelete15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kabine__toDelete15", None)
        self.__toDelete15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kabine14"):
                opp_val = getattr(old_value, "kabine14", None)
                if opp_val == self:
                    setattr(old_value, "kabine14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kabine14"):
                opp_val = getattr(value, "kabine14", None)
                setattr(value, "kabine14", self)

    @property
    def position2(self):
        return self.__position2
    @position2.setter
    def position2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kabine__position2", None)
        self.__position2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "toDelete3"):
                opp_val = getattr(old_value, "toDelete3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "toDelete3"):
                opp_val = getattr(value, "toDelete3", None)
                if opp_val is None:
                    setattr(value, "toDelete3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Antrieb:

    def __init__(self, aNTRIEBSART: str, toDelete13: "TurboliftSchacht" = None):
        self.aNTRIEBSART = aNTRIEBSART
        self.toDelete13 = toDelete13
        
        pass
    @property
    def aNTRIEBSART(self):
        return self.__aNTRIEBSART
    @aNTRIEBSART.setter
    def aNTRIEBSART(self, aNTRIEBSART: str):
        self.__aNTRIEBSART = aNTRIEBSART

    @property
    def toDelete13(self):
        return self.__toDelete13
    @toDelete13.setter
    def toDelete13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Antrieb__toDelete13", None)
        self.__toDelete13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "antrieb12"):
                opp_val = getattr(old_value, "antrieb12", None)
                if opp_val == self:
                    setattr(old_value, "antrieb12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "antrieb12"):
                opp_val = getattr(value, "antrieb12", None)
                setattr(value, "antrieb12", self)



class TurboliftSchacht:

    def __init__(self, vertikal: bool, toDelete1: "Steuerung" = None, decks6: set["Deck"] = None, toDelete9: "TurboliftSystem" = None, antrieb12: "Antrieb" = None, kabine14: "Kabine" = None):
        self.vertikal = vertikal
        self.toDelete1 = toDelete1
        self.decks6 = decks6 if decks6 is not None else set()
        self.toDelete9 = toDelete9
        self.antrieb12 = antrieb12
        self.kabine14 = kabine14
        
        pass
    @property
    def vertikal(self):
        return self.__vertikal
    @vertikal.setter
    def vertikal(self, vertikal: bool):
        self.__vertikal = vertikal

    @property
    def antrieb12(self):
        return self.__antrieb12
    @antrieb12.setter
    def antrieb12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TurboliftSchacht__antrieb12", None)
        self.__antrieb12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "toDelete13"):
                opp_val = getattr(old_value, "toDelete13", None)
                if opp_val == self:
                    setattr(old_value, "toDelete13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "toDelete13"):
                opp_val = getattr(value, "toDelete13", None)
                setattr(value, "toDelete13", self)

    @property
    def kabine14(self):
        return self.__kabine14
    @kabine14.setter
    def kabine14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TurboliftSchacht__kabine14", None)
        self.__kabine14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "toDelete15"):
                opp_val = getattr(old_value, "toDelete15", None)
                if opp_val == self:
                    setattr(old_value, "toDelete15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "toDelete15"):
                opp_val = getattr(value, "toDelete15", None)
                setattr(value, "toDelete15", self)

    @property
    def toDelete1(self):
        return self.__toDelete1
    @toDelete1.setter
    def toDelete1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TurboliftSchacht__toDelete1", None)
        self.__toDelete1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "turboliftSchaechte0"):
                opp_val = getattr(old_value, "turboliftSchaechte0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "turboliftSchaechte0"):
                opp_val = getattr(value, "turboliftSchaechte0", None)
                if opp_val is None:
                    setattr(value, "turboliftSchaechte0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def decks6(self):
        return self.__decks6
    @decks6.setter
    def decks6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TurboliftSchacht__decks6", None)
        self.__decks6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "toDelete7"):
                    opp_val = getattr(item, "toDelete7", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "toDelete7"):
                    opp_val = getattr(item, "toDelete7", None)
                    
                    if opp_val is None:
                        setattr(item, "toDelete7", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def toDelete9(self):
        return self.__toDelete9
    @toDelete9.setter
    def toDelete9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TurboliftSchacht__toDelete9", None)
        self.__toDelete9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "turboliftSchaechte8"):
                opp_val = getattr(old_value, "turboliftSchaechte8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "turboliftSchaechte8"):
                opp_val = getattr(value, "turboliftSchaechte8", None)
                if opp_val is None:
                    setattr(value, "turboliftSchaechte8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Steuerung:

    pass


class TurboliftSystem:

    def __init__(self, alarmStufe: int, turboliftSchaechte8: set["TurboliftSchacht"] = None, steuerung10: "Steuerung" = None):
        self.alarmStufe = alarmStufe
        self.turboliftSchaechte8 = turboliftSchaechte8 if turboliftSchaechte8 is not None else set()
        self.steuerung10 = steuerung10
        
        pass
    @property
    def alarmStufe(self):
        return self.__alarmStufe
    @alarmStufe.setter
    def alarmStufe(self, alarmStufe: int):
        self.__alarmStufe = alarmStufe

    @property
    def turboliftSchaechte8(self):
        return self.__turboliftSchaechte8
    @turboliftSchaechte8.setter
    def turboliftSchaechte8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TurboliftSystem__turboliftSchaechte8", None)
        self.__turboliftSchaechte8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "toDelete9"):
                    opp_val = getattr(item, "toDelete9", None)
                    
                    if opp_val == self:
                        setattr(item, "toDelete9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "toDelete9"):
                    opp_val = getattr(item, "toDelete9", None)
                    
                    setattr(item, "toDelete9", self)
                    

    @property
    def steuerung10(self):
        return self.__steuerung10
    @steuerung10.setter
    def steuerung10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TurboliftSystem__steuerung10", None)
        self.__steuerung10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "toDelete11"):
                opp_val = getattr(old_value, "toDelete11", None)
                if opp_val == self:
                    setattr(old_value, "toDelete11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "toDelete11"):
                opp_val = getattr(value, "toDelete11", None)
                setattr(value, "toDelete11", self)

