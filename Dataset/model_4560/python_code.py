from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class platoon_PlatooningSystem:

    pass
class platoon_JoiningPosition:

    pass
class platoon_FrontGap:

    def __init__(self, actualGapSize: int, platoon_FrontGap: "platoon_JoiningVehicle" = None, platoon_FrontGap34: "platoon_PlatoonVehicle" = None):
        self.actualGapSize = actualGapSize
        self.platoon_FrontGap = platoon_FrontGap
        self.platoon_FrontGap34 = platoon_FrontGap34
        
    @property
    def actualGapSize(self) -> int:
        return self.__actualGapSize

    @actualGapSize.setter
    def actualGapSize(self, actualGapSize: int):
        self.__actualGapSize = actualGapSize

    @property
    def platoon_FrontGap34(self):
        return self.__platoon_FrontGap34

    @platoon_FrontGap34.setter
    def platoon_FrontGap34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_platoon_FrontGap__platoon_FrontGap34", None)
        self.__platoon_FrontGap34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "platoon_PlatoonVehicle33"):
                opp_val = getattr(old_value, "platoon_PlatoonVehicle33", None)
                if opp_val == self:
                    setattr(old_value, "platoon_PlatoonVehicle33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "platoon_PlatoonVehicle33"):
                opp_val = getattr(value, "platoon_PlatoonVehicle33", None)
                setattr(value, "platoon_PlatoonVehicle33", self)

    @property
    def platoon_FrontGap(self):
        return self.__platoon_FrontGap

    @platoon_FrontGap.setter
    def platoon_FrontGap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_platoon_FrontGap__platoon_FrontGap", None)
        self.__platoon_FrontGap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "platoon_JoiningVehicle"):
                opp_val = getattr(old_value, "platoon_JoiningVehicle", None)
                if opp_val == self:
                    setattr(old_value, "platoon_JoiningVehicle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "platoon_JoiningVehicle"):
                opp_val = getattr(value, "platoon_JoiningVehicle", None)
                setattr(value, "platoon_JoiningVehicle", self)

class Vehicle:

    pass
class platoon_JoiningVehicle(Vehicle):

    pass
class platoon_Vehicle(ABC):

    def __init__(self, id: int, platoon_Vehicle20: "platoon_JoinPlatoonCoord" = None, platoon_Vehicle23: "platoon_JoinPlatoonCoord" = None, platoon_Vehicle26: "platoon_JoinPlatoonCoord" = None, platoon_Vehicle41: "platoon_PlatooningSystem" = None, platoon_Vehicle: "platoon_Vehicle" = None, platoon_Vehicle10: "platoon_Vehicle" = None, platoon_Vehicle14: "platoon_Vehicle" = None, platoon_Vehicle12: "platoon_Vehicle" = None, platoon_Vehicle16: "platoon_JoinPlatoonCoord" = None):
        self.id = id
        self.platoon_Vehicle20 = platoon_Vehicle20
        self.platoon_Vehicle23 = platoon_Vehicle23
        self.platoon_Vehicle26 = platoon_Vehicle26
        self.platoon_Vehicle41 = platoon_Vehicle41
        self.platoon_Vehicle = platoon_Vehicle
        self.platoon_Vehicle10 = platoon_Vehicle10
        self.platoon_Vehicle14 = platoon_Vehicle14
        self.platoon_Vehicle12 = platoon_Vehicle12
        self.platoon_Vehicle16 = platoon_Vehicle16
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def platoon_Vehicle41(self):
        return self.__platoon_Vehicle41

    @platoon_Vehicle41.setter
    def platoon_Vehicle41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_platoon_Vehicle__platoon_Vehicle41", None)
        self.__platoon_Vehicle41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "platoon_PlatooningSystem"):
                opp_val = getattr(old_value, "platoon_PlatooningSystem", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "platoon_PlatooningSystem"):
                opp_val = getattr(value, "platoon_PlatooningSystem", None)
                if opp_val is None:
                    setattr(value, "platoon_PlatooningSystem", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def platoon_Vehicle26(self):
        return self.__platoon_Vehicle26

    @platoon_Vehicle26.setter
    def platoon_Vehicle26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_platoon_Vehicle__platoon_Vehicle26", None)
        self.__platoon_Vehicle26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "platoon_JoinPlatoonCoord25"):
                opp_val = getattr(old_value, "platoon_JoinPlatoonCoord25", None)
                if opp_val == self:
                    setattr(old_value, "platoon_JoinPlatoonCoord25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "platoon_JoinPlatoonCoord25"):
                opp_val = getattr(value, "platoon_JoinPlatoonCoord25", None)
                setattr(value, "platoon_JoinPlatoonCoord25", self)

    @property
    def platoon_Vehicle(self):
        return self.__platoon_Vehicle

    @platoon_Vehicle.setter
    def platoon_Vehicle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_platoon_Vehicle__platoon_Vehicle", None)
        self.__platoon_Vehicle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "platoon_Vehicle10"):
                opp_val = getattr(old_value, "platoon_Vehicle10", None)
                if opp_val == self:
                    setattr(old_value, "platoon_Vehicle10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "platoon_Vehicle10"):
                opp_val = getattr(value, "platoon_Vehicle10", None)
                setattr(value, "platoon_Vehicle10", self)

    @property
    def platoon_Vehicle20(self):
        return self.__platoon_Vehicle20

    @platoon_Vehicle20.setter
    def platoon_Vehicle20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_platoon_Vehicle__platoon_Vehicle20", None)
        self.__platoon_Vehicle20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "platoon_JoinPlatoonCoord19"):
                opp_val = getattr(old_value, "platoon_JoinPlatoonCoord19", None)
                if opp_val == self:
                    setattr(old_value, "platoon_JoinPlatoonCoord19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "platoon_JoinPlatoonCoord19"):
                opp_val = getattr(value, "platoon_JoinPlatoonCoord19", None)
                setattr(value, "platoon_JoinPlatoonCoord19", self)

    @property
    def platoon_Vehicle14(self):
        return self.__platoon_Vehicle14

    @platoon_Vehicle14.setter
    def platoon_Vehicle14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_platoon_Vehicle__platoon_Vehicle14", None)
        self.__platoon_Vehicle14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "platoon_Vehicle12"):
                opp_val = getattr(old_value, "platoon_Vehicle12", None)
                if opp_val == self:
                    setattr(old_value, "platoon_Vehicle12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "platoon_Vehicle12"):
                opp_val = getattr(value, "platoon_Vehicle12", None)
                setattr(value, "platoon_Vehicle12", self)

    @property
    def platoon_Vehicle23(self):
        return self.__platoon_Vehicle23

    @platoon_Vehicle23.setter
    def platoon_Vehicle23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_platoon_Vehicle__platoon_Vehicle23", None)
        self.__platoon_Vehicle23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "platoon_JoinPlatoonCoord22"):
                opp_val = getattr(old_value, "platoon_JoinPlatoonCoord22", None)
                if opp_val == self:
                    setattr(old_value, "platoon_JoinPlatoonCoord22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "platoon_JoinPlatoonCoord22"):
                opp_val = getattr(value, "platoon_JoinPlatoonCoord22", None)
                setattr(value, "platoon_JoinPlatoonCoord22", self)

    @property
    def platoon_Vehicle10(self):
        return self.__platoon_Vehicle10

    @platoon_Vehicle10.setter
    def platoon_Vehicle10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_platoon_Vehicle__platoon_Vehicle10", None)
        self.__platoon_Vehicle10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "platoon_Vehicle"):
                opp_val = getattr(old_value, "platoon_Vehicle", None)
                if opp_val == self:
                    setattr(old_value, "platoon_Vehicle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "platoon_Vehicle"):
                opp_val = getattr(value, "platoon_Vehicle", None)
                setattr(value, "platoon_Vehicle", self)

    @property
    def platoon_Vehicle12(self):
        return self.__platoon_Vehicle12

    @platoon_Vehicle12.setter
    def platoon_Vehicle12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_platoon_Vehicle__platoon_Vehicle12", None)
        self.__platoon_Vehicle12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "platoon_Vehicle14"):
                opp_val = getattr(old_value, "platoon_Vehicle14", None)
                if opp_val == self:
                    setattr(old_value, "platoon_Vehicle14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "platoon_Vehicle14"):
                opp_val = getattr(value, "platoon_Vehicle14", None)
                setattr(value, "platoon_Vehicle14", self)

    @property
    def platoon_Vehicle16(self):
        return self.__platoon_Vehicle16

    @platoon_Vehicle16.setter
    def platoon_Vehicle16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_platoon_Vehicle__platoon_Vehicle16", None)
        self.__platoon_Vehicle16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "platoon_JoinPlatoonCoord17"):
                opp_val = getattr(old_value, "platoon_JoinPlatoonCoord17", None)
                if opp_val == self:
                    setattr(old_value, "platoon_JoinPlatoonCoord17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "platoon_JoinPlatoonCoord17"):
                opp_val = getattr(value, "platoon_JoinPlatoonCoord17", None)
                setattr(value, "platoon_JoinPlatoonCoord17", self)

class platoon_JoinPlatoonCoord:

    pass
class platoon_PlatoonVehicle(Vehicle):

    def __init__(self, position: int, platoon_PlatoonVehicle: "platoon_Platoon" = None, platoon_PlatoonVehicle3: "platoon_Platoon" = None, PlatoonVehicle: "platoon_Platoon" = None, PlatoonVehicle29: "platoon_JoiningVehicle" = None, platoon_PlatoonVehicle33: "platoon_FrontGap" = None, platoon_PlatoonVehicle36: "platoon_JoiningPosition" = None, wantsToJoin: "platoon_JoiningVehicle" = None, members: "platoon_Platoon" = None):
        self.position = position
        self.platoon_PlatoonVehicle = platoon_PlatoonVehicle
        self.platoon_PlatoonVehicle3 = platoon_PlatoonVehicle3
        self.PlatoonVehicle = PlatoonVehicle
        self.PlatoonVehicle29 = PlatoonVehicle29
        self.platoon_PlatoonVehicle33 = platoon_PlatoonVehicle33
        self.platoon_PlatoonVehicle36 = platoon_PlatoonVehicle36
        self.wantsToJoin = wantsToJoin
        self.members = members
        
    @property
    def position(self) -> int:
        return self.__position

    @position.setter
    def position(self, position: int):
        self.__position = position

    @property
    def members(self):
        return self.__members

    @members.setter
    def members(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_platoon_PlatoonVehicle__members", None)
        self.__members = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Platoon"):
                opp_val = getattr(old_value, "Platoon", None)
                if opp_val == self:
                    setattr(old_value, "Platoon", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Platoon"):
                opp_val = getattr(value, "Platoon", None)
                setattr(value, "Platoon", self)

    @property
    def platoon_PlatoonVehicle3(self):
        return self.__platoon_PlatoonVehicle3

    @platoon_PlatoonVehicle3.setter
    def platoon_PlatoonVehicle3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_platoon_PlatoonVehicle__platoon_PlatoonVehicle3", None)
        self.__platoon_PlatoonVehicle3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "platoon_Platoon2"):
                opp_val = getattr(old_value, "platoon_Platoon2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "platoon_Platoon2"):
                opp_val = getattr(value, "platoon_Platoon2", None)
                if opp_val is None:
                    setattr(value, "platoon_Platoon2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def platoon_PlatoonVehicle33(self):
        return self.__platoon_PlatoonVehicle33

    @platoon_PlatoonVehicle33.setter
    def platoon_PlatoonVehicle33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_platoon_PlatoonVehicle__platoon_PlatoonVehicle33", None)
        self.__platoon_PlatoonVehicle33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "platoon_FrontGap34"):
                opp_val = getattr(old_value, "platoon_FrontGap34", None)
                if opp_val == self:
                    setattr(old_value, "platoon_FrontGap34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "platoon_FrontGap34"):
                opp_val = getattr(value, "platoon_FrontGap34", None)
                setattr(value, "platoon_FrontGap34", self)

    @property
    def PlatoonVehicle(self):
        return self.__PlatoonVehicle

    @PlatoonVehicle.setter
    def PlatoonVehicle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_platoon_PlatoonVehicle__PlatoonVehicle", None)
        self.__PlatoonVehicle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "platoon"):
                opp_val = getattr(old_value, "platoon", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "platoon"):
                opp_val = getattr(value, "platoon", None)
                if opp_val is None:
                    setattr(value, "platoon", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def platoon_PlatoonVehicle36(self):
        return self.__platoon_PlatoonVehicle36

    @platoon_PlatoonVehicle36.setter
    def platoon_PlatoonVehicle36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_platoon_PlatoonVehicle__platoon_PlatoonVehicle36", None)
        self.__platoon_PlatoonVehicle36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "platoon_JoiningPosition37"):
                opp_val = getattr(old_value, "platoon_JoiningPosition37", None)
                if opp_val == self:
                    setattr(old_value, "platoon_JoiningPosition37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "platoon_JoiningPosition37"):
                opp_val = getattr(value, "platoon_JoiningPosition37", None)
                setattr(value, "platoon_JoiningPosition37", self)

    @property
    def platoon_PlatoonVehicle(self):
        return self.__platoon_PlatoonVehicle

    @platoon_PlatoonVehicle.setter
    def platoon_PlatoonVehicle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_platoon_PlatoonVehicle__platoon_PlatoonVehicle", None)
        self.__platoon_PlatoonVehicle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "platoon_Platoon"):
                opp_val = getattr(old_value, "platoon_Platoon", None)
                if opp_val == self:
                    setattr(old_value, "platoon_Platoon", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "platoon_Platoon"):
                opp_val = getattr(value, "platoon_Platoon", None)
                setattr(value, "platoon_Platoon", self)

    @property
    def wantsToJoin(self):
        return self.__wantsToJoin

    @wantsToJoin.setter
    def wantsToJoin(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_platoon_PlatoonVehicle__wantsToJoin", None)
        self.__wantsToJoin = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JoiningVehicle"):
                opp_val = getattr(old_value, "JoiningVehicle", None)
                if opp_val == self:
                    setattr(old_value, "JoiningVehicle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JoiningVehicle"):
                opp_val = getattr(value, "JoiningVehicle", None)
                setattr(value, "JoiningVehicle", self)

    @property
    def PlatoonVehicle29(self):
        return self.__PlatoonVehicle29

    @PlatoonVehicle29.setter
    def PlatoonVehicle29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_platoon_PlatoonVehicle__PlatoonVehicle29", None)
        self.__PlatoonVehicle29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "joiningRequest"):
                opp_val = getattr(old_value, "joiningRequest", None)
                if opp_val == self:
                    setattr(old_value, "joiningRequest", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "joiningRequest"):
                opp_val = getattr(value, "joiningRequest", None)
                setattr(value, "joiningRequest", self)

class platoon_Platoon:

    def __init__(self, length: int, desiredGapSize: int, platoon_Platoon: "platoon_PlatoonVehicle" = None, platoon_Platoon2: set["platoon_PlatoonVehicle"] = None, platoon_Platoon6: "platoon_Platoon" = None, platoon_Platoon4: "platoon_Platoon" = None, platoon_Platoon8: "platoon_JoinPlatoonCoord" = None, platoon: set["platoon_PlatoonVehicle"] = None, Platoon: "platoon_PlatoonVehicle" = None, platoon_Platoon44: "platoon_PlatooningSystem" = None):
        self.length = length
        self.desiredGapSize = desiredGapSize
        self.platoon_Platoon = platoon_Platoon
        self.platoon_Platoon2 = platoon_Platoon2 if platoon_Platoon2 is not None else set()
        self.platoon_Platoon6 = platoon_Platoon6
        self.platoon_Platoon4 = platoon_Platoon4
        self.platoon_Platoon8 = platoon_Platoon8
        self.platoon = platoon if platoon is not None else set()
        self.Platoon = Platoon
        self.platoon_Platoon44 = platoon_Platoon44
        
    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

    @property
    def desiredGapSize(self) -> int:
        return self.__desiredGapSize

    @desiredGapSize.setter
    def desiredGapSize(self, desiredGapSize: int):
        self.__desiredGapSize = desiredGapSize

    @property
    def platoon_Platoon8(self):
        return self.__platoon_Platoon8

    @platoon_Platoon8.setter
    def platoon_Platoon8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_platoon_Platoon__platoon_Platoon8", None)
        self.__platoon_Platoon8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "platoon_JoinPlatoonCoord"):
                opp_val = getattr(old_value, "platoon_JoinPlatoonCoord", None)
                if opp_val == self:
                    setattr(old_value, "platoon_JoinPlatoonCoord", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "platoon_JoinPlatoonCoord"):
                opp_val = getattr(value, "platoon_JoinPlatoonCoord", None)
                setattr(value, "platoon_JoinPlatoonCoord", self)

    @property
    def Platoon(self):
        return self.__Platoon

    @Platoon.setter
    def Platoon(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_platoon_Platoon__Platoon", None)
        self.__Platoon = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "members"):
                opp_val = getattr(old_value, "members", None)
                if opp_val == self:
                    setattr(old_value, "members", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "members"):
                opp_val = getattr(value, "members", None)
                setattr(value, "members", self)

    @property
    def platoon_Platoon2(self):
        return self.__platoon_Platoon2

    @platoon_Platoon2.setter
    def platoon_Platoon2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_platoon_Platoon__platoon_Platoon2", None)
        self.__platoon_Platoon2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "platoon_PlatoonVehicle3"):
                    opp_val = getattr(item, "platoon_PlatoonVehicle3", None)
                    
                    if opp_val == self:
                        setattr(item, "platoon_PlatoonVehicle3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "platoon_PlatoonVehicle3"):
                    opp_val = getattr(item, "platoon_PlatoonVehicle3", None)
                    
                    setattr(item, "platoon_PlatoonVehicle3", self)
                    

    @property
    def platoon_Platoon44(self):
        return self.__platoon_Platoon44

    @platoon_Platoon44.setter
    def platoon_Platoon44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_platoon_Platoon__platoon_Platoon44", None)
        self.__platoon_Platoon44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "platoon_PlatooningSystem43"):
                opp_val = getattr(old_value, "platoon_PlatooningSystem43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "platoon_PlatooningSystem43"):
                opp_val = getattr(value, "platoon_PlatooningSystem43", None)
                if opp_val is None:
                    setattr(value, "platoon_PlatooningSystem43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def platoon_Platoon6(self):
        return self.__platoon_Platoon6

    @platoon_Platoon6.setter
    def platoon_Platoon6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_platoon_Platoon__platoon_Platoon6", None)
        self.__platoon_Platoon6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "platoon_Platoon4"):
                opp_val = getattr(old_value, "platoon_Platoon4", None)
                if opp_val == self:
                    setattr(old_value, "platoon_Platoon4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "platoon_Platoon4"):
                opp_val = getattr(value, "platoon_Platoon4", None)
                setattr(value, "platoon_Platoon4", self)

    @property
    def platoon(self):
        return self.__platoon

    @platoon.setter
    def platoon(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_platoon_Platoon__platoon", None)
        self.__platoon = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PlatoonVehicle"):
                    opp_val = getattr(item, "PlatoonVehicle", None)
                    
                    if opp_val == self:
                        setattr(item, "PlatoonVehicle", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PlatoonVehicle"):
                    opp_val = getattr(item, "PlatoonVehicle", None)
                    
                    setattr(item, "PlatoonVehicle", self)
                    

    @property
    def platoon_Platoon(self):
        return self.__platoon_Platoon

    @platoon_Platoon.setter
    def platoon_Platoon(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_platoon_Platoon__platoon_Platoon", None)
        self.__platoon_Platoon = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "platoon_PlatoonVehicle"):
                opp_val = getattr(old_value, "platoon_PlatoonVehicle", None)
                if opp_val == self:
                    setattr(old_value, "platoon_PlatoonVehicle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "platoon_PlatoonVehicle"):
                opp_val = getattr(value, "platoon_PlatoonVehicle", None)
                setattr(value, "platoon_PlatoonVehicle", self)

    @property
    def platoon_Platoon4(self):
        return self.__platoon_Platoon4

    @platoon_Platoon4.setter
    def platoon_Platoon4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_platoon_Platoon__platoon_Platoon4", None)
        self.__platoon_Platoon4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "platoon_Platoon6"):
                opp_val = getattr(old_value, "platoon_Platoon6", None)
                if opp_val == self:
                    setattr(old_value, "platoon_Platoon6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "platoon_Platoon6"):
                opp_val = getattr(value, "platoon_Platoon6", None)
                setattr(value, "platoon_Platoon6", self)
