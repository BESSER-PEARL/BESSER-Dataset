from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Effect:

    pass
class dsl_PersistentEffect(Effect):

    def __init__(self, periodCount: int, durations: str, ranges: str, dsl_PersistentEffect: set["dsl_Effect"] = None):
        self.periodCount = periodCount
        self.durations = durations
        self.ranges = ranges
        self.dsl_PersistentEffect = dsl_PersistentEffect if dsl_PersistentEffect is not None else set()
        
    @property
    def ranges(self) -> str:
        return self.__ranges

    @ranges.setter
    def ranges(self, ranges: str):
        self.__ranges = ranges

    @property
    def durations(self) -> str:
        return self.__durations

    @durations.setter
    def durations(self, durations: str):
        self.__durations = durations

    @property
    def periodCount(self) -> int:
        return self.__periodCount

    @periodCount.setter
    def periodCount(self, periodCount: int):
        self.__periodCount = periodCount

    @property
    def dsl_PersistentEffect(self):
        return self.__dsl_PersistentEffect

    @dsl_PersistentEffect.setter
    def dsl_PersistentEffect(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_PersistentEffect__dsl_PersistentEffect", None)
        self.__dsl_PersistentEffect = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_Effect47"):
                    opp_val = getattr(item, "dsl_Effect47", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_Effect47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_Effect47"):
                    opp_val = getattr(item, "dsl_Effect47", None)
                    
                    setattr(item, "dsl_Effect47", self)
                    

class dsl_LauncherEffect(Effect):

    pass
class dsl_DamageEffect(Effect):

    def __init__(self, amount: int):
        self.amount = amount
        
    @property
    def amount(self) -> int:
        return self.__amount

    @amount.setter
    def amount(self, amount: int):
        self.__amount = amount

class dsl_Color:

    def __init__(self, r: int, g: int, b: int, a: int, dsl_Color: "dsl_ParticleActor" = None, dsl_Color19: "dsl_ParticleActor" = None):
        self.r = r
        self.g = g
        self.b = b
        self.a = a
        self.dsl_Color = dsl_Color
        self.dsl_Color19 = dsl_Color19
        
    @property
    def b(self) -> int:
        return self.__b

    @b.setter
    def b(self, b: int):
        self.__b = b

    @property
    def r(self) -> int:
        return self.__r

    @r.setter
    def r(self, r: int):
        self.__r = r

    @property
    def a(self) -> int:
        return self.__a

    @a.setter
    def a(self, a: int):
        self.__a = a

    @property
    def g(self) -> int:
        return self.__g

    @g.setter
    def g(self, g: int):
        self.__g = g

    @property
    def dsl_Color19(self):
        return self.__dsl_Color19

    @dsl_Color19.setter
    def dsl_Color19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Color__dsl_Color19", None)
        self.__dsl_Color19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ParticleActor18"):
                opp_val = getattr(old_value, "dsl_ParticleActor18", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ParticleActor18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ParticleActor18"):
                opp_val = getattr(value, "dsl_ParticleActor18", None)
                setattr(value, "dsl_ParticleActor18", self)

    @property
    def dsl_Color(self):
        return self.__dsl_Color

    @dsl_Color.setter
    def dsl_Color(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Color__dsl_Color", None)
        self.__dsl_Color = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ParticleActor"):
                opp_val = getattr(old_value, "dsl_ParticleActor", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ParticleActor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ParticleActor"):
                opp_val = getattr(value, "dsl_ParticleActor", None)
                setattr(value, "dsl_ParticleActor", self)

class dsl_UnitWeaponLink:

    pass
class dsl_Turrent:

    def __init__(self, name: str, speed: int, idleSpeed: int, onIdle: str, boneName: str, dsl_Turrent: "dsl_Model" = None, dsl_Turrent39: "dsl_UnitWeaponLink" = None):
        self.name = name
        self.speed = speed
        self.idleSpeed = idleSpeed
        self.onIdle = onIdle
        self.boneName = boneName
        self.dsl_Turrent = dsl_Turrent
        self.dsl_Turrent39 = dsl_Turrent39
        
    @property
    def onIdle(self) -> str:
        return self.__onIdle

    @onIdle.setter
    def onIdle(self, onIdle: str):
        self.__onIdle = onIdle

    @property
    def speed(self) -> int:
        return self.__speed

    @speed.setter
    def speed(self, speed: int):
        self.__speed = speed

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def idleSpeed(self) -> int:
        return self.__idleSpeed

    @idleSpeed.setter
    def idleSpeed(self, idleSpeed: int):
        self.__idleSpeed = idleSpeed

    @property
    def boneName(self) -> str:
        return self.__boneName

    @boneName.setter
    def boneName(self, boneName: str):
        self.__boneName = boneName

    @property
    def dsl_Turrent39(self):
        return self.__dsl_Turrent39

    @dsl_Turrent39.setter
    def dsl_Turrent39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Turrent__dsl_Turrent39", None)
        self.__dsl_Turrent39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_UnitWeaponLink38"):
                opp_val = getattr(old_value, "dsl_UnitWeaponLink38", None)
                if opp_val == self:
                    setattr(old_value, "dsl_UnitWeaponLink38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_UnitWeaponLink38"):
                opp_val = getattr(value, "dsl_UnitWeaponLink38", None)
                setattr(value, "dsl_UnitWeaponLink38", self)

    @property
    def dsl_Turrent(self):
        return self.__dsl_Turrent

    @dsl_Turrent.setter
    def dsl_Turrent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Turrent__dsl_Turrent", None)
        self.__dsl_Turrent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Model12"):
                opp_val = getattr(old_value, "dsl_Model12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Model12"):
                opp_val = getattr(value, "dsl_Model12", None)
                if opp_val is None:
                    setattr(value, "dsl_Model12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dsl_Effect:

    def __init__(self, name: str, dsl_Effect: "dsl_Model" = None, dsl_Effect47: "dsl_PersistentEffect" = None, dsl_Effect49: "dsl_LauncherEffect" = None, dsl_Effect42: "dsl_Weapon" = None):
        self.name = name
        self.dsl_Effect = dsl_Effect
        self.dsl_Effect47 = dsl_Effect47
        self.dsl_Effect49 = dsl_Effect49
        self.dsl_Effect42 = dsl_Effect42
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_Effect49(self):
        return self.__dsl_Effect49

    @dsl_Effect49.setter
    def dsl_Effect49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Effect__dsl_Effect49", None)
        self.__dsl_Effect49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_LauncherEffect"):
                opp_val = getattr(old_value, "dsl_LauncherEffect", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_LauncherEffect"):
                opp_val = getattr(value, "dsl_LauncherEffect", None)
                if opp_val is None:
                    setattr(value, "dsl_LauncherEffect", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_Effect(self):
        return self.__dsl_Effect

    @dsl_Effect.setter
    def dsl_Effect(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Effect__dsl_Effect", None)
        self.__dsl_Effect = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Model10"):
                opp_val = getattr(old_value, "dsl_Model10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Model10"):
                opp_val = getattr(value, "dsl_Model10", None)
                if opp_val is None:
                    setattr(value, "dsl_Model10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_Effect42(self):
        return self.__dsl_Effect42

    @dsl_Effect42.setter
    def dsl_Effect42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Effect__dsl_Effect42", None)
        self.__dsl_Effect42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Weapon41"):
                opp_val = getattr(old_value, "dsl_Weapon41", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Weapon41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Weapon41"):
                opp_val = getattr(value, "dsl_Weapon41", None)
                setattr(value, "dsl_Weapon41", self)

    @property
    def dsl_Effect47(self):
        return self.__dsl_Effect47

    @dsl_Effect47.setter
    def dsl_Effect47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Effect__dsl_Effect47", None)
        self.__dsl_Effect47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_PersistentEffect"):
                opp_val = getattr(old_value, "dsl_PersistentEffect", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_PersistentEffect"):
                opp_val = getattr(value, "dsl_PersistentEffect", None)
                if opp_val is None:
                    setattr(value, "dsl_PersistentEffect", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dsl_Actor:

    def __init__(self, name: str, dsl_Actor: "dsl_Model" = None, dsl_Actor22: "dsl_ActorList" = None, dsl_Actor33: "dsl_Unit" = None, dsl_Actor58: "dsl_Projectile" = None, dsl_Actor45: "dsl_Weapon" = None):
        self.name = name
        self.dsl_Actor = dsl_Actor
        self.dsl_Actor22 = dsl_Actor22
        self.dsl_Actor33 = dsl_Actor33
        self.dsl_Actor58 = dsl_Actor58
        self.dsl_Actor45 = dsl_Actor45
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_Actor45(self):
        return self.__dsl_Actor45

    @dsl_Actor45.setter
    def dsl_Actor45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Actor__dsl_Actor45", None)
        self.__dsl_Actor45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Weapon44"):
                opp_val = getattr(old_value, "dsl_Weapon44", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Weapon44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Weapon44"):
                opp_val = getattr(value, "dsl_Weapon44", None)
                setattr(value, "dsl_Weapon44", self)

    @property
    def dsl_Actor(self):
        return self.__dsl_Actor

    @dsl_Actor.setter
    def dsl_Actor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Actor__dsl_Actor", None)
        self.__dsl_Actor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Model8"):
                opp_val = getattr(old_value, "dsl_Model8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Model8"):
                opp_val = getattr(value, "dsl_Model8", None)
                if opp_val is None:
                    setattr(value, "dsl_Model8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_Actor33(self):
        return self.__dsl_Actor33

    @dsl_Actor33.setter
    def dsl_Actor33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Actor__dsl_Actor33", None)
        self.__dsl_Actor33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Unit32"):
                opp_val = getattr(old_value, "dsl_Unit32", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Unit32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Unit32"):
                opp_val = getattr(value, "dsl_Unit32", None)
                setattr(value, "dsl_Unit32", self)

    @property
    def dsl_Actor22(self):
        return self.__dsl_Actor22

    @dsl_Actor22.setter
    def dsl_Actor22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Actor__dsl_Actor22", None)
        self.__dsl_Actor22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ActorList21"):
                opp_val = getattr(old_value, "dsl_ActorList21", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ActorList21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ActorList21"):
                opp_val = getattr(value, "dsl_ActorList21", None)
                setattr(value, "dsl_ActorList21", self)

    @property
    def dsl_Actor58(self):
        return self.__dsl_Actor58

    @dsl_Actor58.setter
    def dsl_Actor58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Actor__dsl_Actor58", None)
        self.__dsl_Actor58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Projectile57"):
                opp_val = getattr(old_value, "dsl_Projectile57", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Projectile57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Projectile57"):
                opp_val = getattr(value, "dsl_Projectile57", None)
                setattr(value, "dsl_Projectile57", self)

class dsl_Mover:

    def __init__(self, name: str, pathfindingMode: str, heightmap: str, standingMode: str, dsl_Mover: "dsl_Model" = None, dsl_Mover28: "dsl_Unit" = None, dsl_Mover55: "dsl_Projectile" = None):
        self.name = name
        self.pathfindingMode = pathfindingMode
        self.heightmap = heightmap
        self.standingMode = standingMode
        self.dsl_Mover = dsl_Mover
        self.dsl_Mover28 = dsl_Mover28
        self.dsl_Mover55 = dsl_Mover55
        
    @property
    def pathfindingMode(self) -> str:
        return self.__pathfindingMode

    @pathfindingMode.setter
    def pathfindingMode(self, pathfindingMode: str):
        self.__pathfindingMode = pathfindingMode

    @property
    def standingMode(self) -> str:
        return self.__standingMode

    @standingMode.setter
    def standingMode(self, standingMode: str):
        self.__standingMode = standingMode

    @property
    def heightmap(self) -> str:
        return self.__heightmap

    @heightmap.setter
    def heightmap(self, heightmap: str):
        self.__heightmap = heightmap

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_Mover28(self):
        return self.__dsl_Mover28

    @dsl_Mover28.setter
    def dsl_Mover28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Mover__dsl_Mover28", None)
        self.__dsl_Mover28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Unit27"):
                opp_val = getattr(old_value, "dsl_Unit27", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Unit27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Unit27"):
                opp_val = getattr(value, "dsl_Unit27", None)
                setattr(value, "dsl_Unit27", self)

    @property
    def dsl_Mover(self):
        return self.__dsl_Mover

    @dsl_Mover.setter
    def dsl_Mover(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Mover__dsl_Mover", None)
        self.__dsl_Mover = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Model6"):
                opp_val = getattr(old_value, "dsl_Model6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Model6"):
                opp_val = getattr(value, "dsl_Model6", None)
                if opp_val is None:
                    setattr(value, "dsl_Model6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_Mover55(self):
        return self.__dsl_Mover55

    @dsl_Mover55.setter
    def dsl_Mover55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Mover__dsl_Mover55", None)
        self.__dsl_Mover55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Projectile54"):
                opp_val = getattr(old_value, "dsl_Projectile54", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Projectile54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Projectile54"):
                opp_val = getattr(value, "dsl_Projectile54", None)
                setattr(value, "dsl_Projectile54", self)

class dsl_ActorList:

    def __init__(self, trigger: str, dsl_ActorList: "dsl_ModelActor" = None, dsl_ActorList21: "dsl_Actor" = None):
        self.trigger = trigger
        self.dsl_ActorList = dsl_ActorList
        self.dsl_ActorList21 = dsl_ActorList21
        
    @property
    def trigger(self) -> str:
        return self.__trigger

    @trigger.setter
    def trigger(self, trigger: str):
        self.__trigger = trigger

    @property
    def dsl_ActorList(self):
        return self.__dsl_ActorList

    @dsl_ActorList.setter
    def dsl_ActorList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ActorList__dsl_ActorList", None)
        self.__dsl_ActorList = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ModelActor"):
                opp_val = getattr(old_value, "dsl_ModelActor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ModelActor"):
                opp_val = getattr(value, "dsl_ModelActor", None)
                if opp_val is None:
                    setattr(value, "dsl_ModelActor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_ActorList21(self):
        return self.__dsl_ActorList21

    @dsl_ActorList21.setter
    def dsl_ActorList21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ActorList__dsl_ActorList21", None)
        self.__dsl_ActorList21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Actor22"):
                opp_val = getattr(old_value, "dsl_Actor22", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Actor22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Actor22"):
                opp_val = getattr(value, "dsl_Actor22", None)
                setattr(value, "dsl_Actor22", self)

class Actor:

    pass
class dsl_ParticleActor(Actor):

    def __init__(self, spritePath: str, nbCol: int, nbRow: int, add: str, emissionBone: str, directionBone: str, maxCount: int, perSecond: int, duration: int, startSize: str, endSize: str, minLife: str, maxLife: str, startVariation: str, dsl_ParticleActor: "dsl_Color" = None, dsl_ParticleActor18: "dsl_Color" = None):
        self.spritePath = spritePath
        self.nbCol = nbCol
        self.nbRow = nbRow
        self.add = add
        self.emissionBone = emissionBone
        self.directionBone = directionBone
        self.maxCount = maxCount
        self.perSecond = perSecond
        self.duration = duration
        self.startSize = startSize
        self.endSize = endSize
        self.minLife = minLife
        self.maxLife = maxLife
        self.startVariation = startVariation
        self.dsl_ParticleActor = dsl_ParticleActor
        self.dsl_ParticleActor18 = dsl_ParticleActor18
        
    @property
    def emissionBone(self) -> str:
        return self.__emissionBone

    @emissionBone.setter
    def emissionBone(self, emissionBone: str):
        self.__emissionBone = emissionBone

    @property
    def spritePath(self) -> str:
        return self.__spritePath

    @spritePath.setter
    def spritePath(self, spritePath: str):
        self.__spritePath = spritePath

    @property
    def perSecond(self) -> int:
        return self.__perSecond

    @perSecond.setter
    def perSecond(self, perSecond: int):
        self.__perSecond = perSecond

    @property
    def startSize(self) -> str:
        return self.__startSize

    @startSize.setter
    def startSize(self, startSize: str):
        self.__startSize = startSize

    @property
    def nbRow(self) -> int:
        return self.__nbRow

    @nbRow.setter
    def nbRow(self, nbRow: int):
        self.__nbRow = nbRow

    @property
    def directionBone(self) -> str:
        return self.__directionBone

    @directionBone.setter
    def directionBone(self, directionBone: str):
        self.__directionBone = directionBone

    @property
    def maxLife(self) -> str:
        return self.__maxLife

    @maxLife.setter
    def maxLife(self, maxLife: str):
        self.__maxLife = maxLife

    @property
    def maxCount(self) -> int:
        return self.__maxCount

    @maxCount.setter
    def maxCount(self, maxCount: int):
        self.__maxCount = maxCount

    @property
    def minLife(self) -> str:
        return self.__minLife

    @minLife.setter
    def minLife(self, minLife: str):
        self.__minLife = minLife

    @property
    def endSize(self) -> str:
        return self.__endSize

    @endSize.setter
    def endSize(self, endSize: str):
        self.__endSize = endSize

    @property
    def nbCol(self) -> int:
        return self.__nbCol

    @nbCol.setter
    def nbCol(self, nbCol: int):
        self.__nbCol = nbCol

    @property
    def add(self) -> str:
        return self.__add

    @add.setter
    def add(self, add: str):
        self.__add = add

    @property
    def startVariation(self) -> str:
        return self.__startVariation

    @startVariation.setter
    def startVariation(self, startVariation: str):
        self.__startVariation = startVariation

    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration

    @property
    def dsl_ParticleActor18(self):
        return self.__dsl_ParticleActor18

    @dsl_ParticleActor18.setter
    def dsl_ParticleActor18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ParticleActor__dsl_ParticleActor18", None)
        self.__dsl_ParticleActor18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Color19"):
                opp_val = getattr(old_value, "dsl_Color19", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Color19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Color19"):
                opp_val = getattr(value, "dsl_Color19", None)
                setattr(value, "dsl_Color19", self)

    @property
    def dsl_ParticleActor(self):
        return self.__dsl_ParticleActor

    @dsl_ParticleActor.setter
    def dsl_ParticleActor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ParticleActor__dsl_ParticleActor", None)
        self.__dsl_ParticleActor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Color"):
                opp_val = getattr(old_value, "dsl_Color", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Color", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Color"):
                opp_val = getattr(value, "dsl_Color", None)
                setattr(value, "dsl_Color", self)

class dsl_AnimtationActor(Actor):

    def __init__(self, animName: str, speed: str, cycle: str):
        self.animName = animName
        self.speed = speed
        self.cycle = cycle
        
    @property
    def speed(self) -> str:
        return self.__speed

    @speed.setter
    def speed(self, speed: str):
        self.__speed = speed

    @property
    def animName(self) -> str:
        return self.__animName

    @animName.setter
    def animName(self, animName: str):
        self.__animName = animName

    @property
    def cycle(self) -> str:
        return self.__cycle

    @cycle.setter
    def cycle(self, cycle: str):
        self.__cycle = cycle

class dsl_ModelActor(Actor):

    def __init__(self, modelPath: str, scale: int, dsl_ModelActor: set["dsl_ActorList"] = None):
        self.modelPath = modelPath
        self.scale = scale
        self.dsl_ModelActor = dsl_ModelActor if dsl_ModelActor is not None else set()
        
    @property
    def modelPath(self) -> str:
        return self.__modelPath

    @modelPath.setter
    def modelPath(self, modelPath: str):
        self.__modelPath = modelPath

    @property
    def scale(self) -> int:
        return self.__scale

    @scale.setter
    def scale(self, scale: int):
        self.__scale = scale

    @property
    def dsl_ModelActor(self):
        return self.__dsl_ModelActor

    @dsl_ModelActor.setter
    def dsl_ModelActor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ModelActor__dsl_ModelActor", None)
        self.__dsl_ModelActor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_ActorList"):
                    opp_val = getattr(item, "dsl_ActorList", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_ActorList", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_ActorList"):
                    opp_val = getattr(item, "dsl_ActorList", None)
                    
                    setattr(item, "dsl_ActorList", self)
                    

class dsl_Projectile:

    def __init__(self, name: str, speed: int, mass: int, precision: str, dsl_Projectile: "dsl_Model" = None, dsl_Projectile52: "dsl_LauncherEffect" = None, dsl_Projectile54: "dsl_Mover" = None, dsl_Projectile57: "dsl_Actor" = None):
        self.name = name
        self.speed = speed
        self.mass = mass
        self.precision = precision
        self.dsl_Projectile = dsl_Projectile
        self.dsl_Projectile52 = dsl_Projectile52
        self.dsl_Projectile54 = dsl_Projectile54
        self.dsl_Projectile57 = dsl_Projectile57
        
    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

    @property
    def speed(self) -> int:
        return self.__speed

    @speed.setter
    def speed(self, speed: int):
        self.__speed = speed

    @property
    def mass(self) -> int:
        return self.__mass

    @mass.setter
    def mass(self, mass: int):
        self.__mass = mass

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_Projectile54(self):
        return self.__dsl_Projectile54

    @dsl_Projectile54.setter
    def dsl_Projectile54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Projectile__dsl_Projectile54", None)
        self.__dsl_Projectile54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Mover55"):
                opp_val = getattr(old_value, "dsl_Mover55", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Mover55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Mover55"):
                opp_val = getattr(value, "dsl_Mover55", None)
                setattr(value, "dsl_Mover55", self)

    @property
    def dsl_Projectile(self):
        return self.__dsl_Projectile

    @dsl_Projectile.setter
    def dsl_Projectile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Projectile__dsl_Projectile", None)
        self.__dsl_Projectile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Model14"):
                opp_val = getattr(old_value, "dsl_Model14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Model14"):
                opp_val = getattr(value, "dsl_Model14", None)
                if opp_val is None:
                    setattr(value, "dsl_Model14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_Projectile52(self):
        return self.__dsl_Projectile52

    @dsl_Projectile52.setter
    def dsl_Projectile52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Projectile__dsl_Projectile52", None)
        self.__dsl_Projectile52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_LauncherEffect51"):
                opp_val = getattr(old_value, "dsl_LauncherEffect51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_LauncherEffect51"):
                opp_val = getattr(value, "dsl_LauncherEffect51", None)
                if opp_val is None:
                    setattr(value, "dsl_LauncherEffect51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_Projectile57(self):
        return self.__dsl_Projectile57

    @dsl_Projectile57.setter
    def dsl_Projectile57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Projectile__dsl_Projectile57", None)
        self.__dsl_Projectile57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Actor58"):
                opp_val = getattr(old_value, "dsl_Actor58", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Actor58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Actor58"):
                opp_val = getattr(value, "dsl_Actor58", None)
                setattr(value, "dsl_Actor58", self)

class dsl_Race:

    def __init__(self, name: str, dsl_Race: "dsl_Model" = None, dsl_Race25: "dsl_Unit" = None):
        self.name = name
        self.dsl_Race = dsl_Race
        self.dsl_Race25 = dsl_Race25
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_Race25(self):
        return self.__dsl_Race25

    @dsl_Race25.setter
    def dsl_Race25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Race__dsl_Race25", None)
        self.__dsl_Race25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Unit24"):
                opp_val = getattr(old_value, "dsl_Unit24", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Unit24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Unit24"):
                opp_val = getattr(value, "dsl_Unit24", None)
                setattr(value, "dsl_Unit24", self)

    @property
    def dsl_Race(self):
        return self.__dsl_Race

    @dsl_Race.setter
    def dsl_Race(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Race__dsl_Race", None)
        self.__dsl_Race = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Model4"):
                opp_val = getattr(old_value, "dsl_Model4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Model4"):
                opp_val = getattr(value, "dsl_Model4", None)
                if opp_val is None:
                    setattr(value, "dsl_Model4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dsl_Unit:

    def __init__(self, name: str, uIName: str, radius: str, separationRadius: str, speed: str, mass: str, maxHealth: int, sight: int, dsl_Unit: "dsl_Model" = None, dsl_Unit24: "dsl_Race" = None, dsl_Unit27: "dsl_Mover" = None, dsl_Unit30: set["dsl_UnitWeaponLink"] = None, dsl_Unit32: "dsl_Actor" = None):
        self.name = name
        self.uIName = uIName
        self.radius = radius
        self.separationRadius = separationRadius
        self.speed = speed
        self.mass = mass
        self.maxHealth = maxHealth
        self.sight = sight
        self.dsl_Unit = dsl_Unit
        self.dsl_Unit24 = dsl_Unit24
        self.dsl_Unit27 = dsl_Unit27
        self.dsl_Unit30 = dsl_Unit30 if dsl_Unit30 is not None else set()
        self.dsl_Unit32 = dsl_Unit32
        
    @property
    def speed(self) -> str:
        return self.__speed

    @speed.setter
    def speed(self, speed: str):
        self.__speed = speed

    @property
    def separationRadius(self) -> str:
        return self.__separationRadius

    @separationRadius.setter
    def separationRadius(self, separationRadius: str):
        self.__separationRadius = separationRadius

    @property
    def uIName(self) -> str:
        return self.__uIName

    @uIName.setter
    def uIName(self, uIName: str):
        self.__uIName = uIName

    @property
    def mass(self) -> str:
        return self.__mass

    @mass.setter
    def mass(self, mass: str):
        self.__mass = mass

    @property
    def maxHealth(self) -> int:
        return self.__maxHealth

    @maxHealth.setter
    def maxHealth(self, maxHealth: int):
        self.__maxHealth = maxHealth

    @property
    def sight(self) -> int:
        return self.__sight

    @sight.setter
    def sight(self, sight: int):
        self.__sight = sight

    @property
    def radius(self) -> str:
        return self.__radius

    @radius.setter
    def radius(self, radius: str):
        self.__radius = radius

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_Unit24(self):
        return self.__dsl_Unit24

    @dsl_Unit24.setter
    def dsl_Unit24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Unit__dsl_Unit24", None)
        self.__dsl_Unit24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Race25"):
                opp_val = getattr(old_value, "dsl_Race25", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Race25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Race25"):
                opp_val = getattr(value, "dsl_Race25", None)
                setattr(value, "dsl_Race25", self)

    @property
    def dsl_Unit27(self):
        return self.__dsl_Unit27

    @dsl_Unit27.setter
    def dsl_Unit27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Unit__dsl_Unit27", None)
        self.__dsl_Unit27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Mover28"):
                opp_val = getattr(old_value, "dsl_Mover28", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Mover28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Mover28"):
                opp_val = getattr(value, "dsl_Mover28", None)
                setattr(value, "dsl_Mover28", self)

    @property
    def dsl_Unit30(self):
        return self.__dsl_Unit30

    @dsl_Unit30.setter
    def dsl_Unit30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Unit__dsl_Unit30", None)
        self.__dsl_Unit30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_UnitWeaponLink"):
                    opp_val = getattr(item, "dsl_UnitWeaponLink", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_UnitWeaponLink", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_UnitWeaponLink"):
                    opp_val = getattr(item, "dsl_UnitWeaponLink", None)
                    
                    setattr(item, "dsl_UnitWeaponLink", self)
                    

    @property
    def dsl_Unit(self):
        return self.__dsl_Unit

    @dsl_Unit.setter
    def dsl_Unit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Unit__dsl_Unit", None)
        self.__dsl_Unit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Model2"):
                opp_val = getattr(old_value, "dsl_Model2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Model2"):
                opp_val = getattr(value, "dsl_Model2", None)
                if opp_val is None:
                    setattr(value, "dsl_Model2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_Unit32(self):
        return self.__dsl_Unit32

    @dsl_Unit32.setter
    def dsl_Unit32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Unit__dsl_Unit32", None)
        self.__dsl_Unit32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Actor33"):
                opp_val = getattr(old_value, "dsl_Actor33", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Actor33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Actor33"):
                opp_val = getattr(value, "dsl_Actor33", None)
                setattr(value, "dsl_Actor33", self)

class dsl_Weapon:

    def __init__(self, name: str, uIName: str, range: str, scanRange: int, period: int, sourceBone: str, directionBone: str, dsl_Weapon: "dsl_Model" = None, dsl_Weapon36: "dsl_UnitWeaponLink" = None, dsl_Weapon41: "dsl_Effect" = None, dsl_Weapon44: "dsl_Actor" = None):
        self.name = name
        self.uIName = uIName
        self.range = range
        self.scanRange = scanRange
        self.period = period
        self.sourceBone = sourceBone
        self.directionBone = directionBone
        self.dsl_Weapon = dsl_Weapon
        self.dsl_Weapon36 = dsl_Weapon36
        self.dsl_Weapon41 = dsl_Weapon41
        self.dsl_Weapon44 = dsl_Weapon44
        
    @property
    def range(self) -> str:
        return self.__range

    @range.setter
    def range(self, range: str):
        self.__range = range

    @property
    def scanRange(self) -> int:
        return self.__scanRange

    @scanRange.setter
    def scanRange(self, scanRange: int):
        self.__scanRange = scanRange

    @property
    def sourceBone(self) -> str:
        return self.__sourceBone

    @sourceBone.setter
    def sourceBone(self, sourceBone: str):
        self.__sourceBone = sourceBone

    @property
    def uIName(self) -> str:
        return self.__uIName

    @uIName.setter
    def uIName(self, uIName: str):
        self.__uIName = uIName

    @property
    def directionBone(self) -> str:
        return self.__directionBone

    @directionBone.setter
    def directionBone(self, directionBone: str):
        self.__directionBone = directionBone

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def period(self) -> int:
        return self.__period

    @period.setter
    def period(self, period: int):
        self.__period = period

    @property
    def dsl_Weapon(self):
        return self.__dsl_Weapon

    @dsl_Weapon.setter
    def dsl_Weapon(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Weapon__dsl_Weapon", None)
        self.__dsl_Weapon = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Model"):
                opp_val = getattr(old_value, "dsl_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Model"):
                opp_val = getattr(value, "dsl_Model", None)
                if opp_val is None:
                    setattr(value, "dsl_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_Weapon36(self):
        return self.__dsl_Weapon36

    @dsl_Weapon36.setter
    def dsl_Weapon36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Weapon__dsl_Weapon36", None)
        self.__dsl_Weapon36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_UnitWeaponLink35"):
                opp_val = getattr(old_value, "dsl_UnitWeaponLink35", None)
                if opp_val == self:
                    setattr(old_value, "dsl_UnitWeaponLink35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_UnitWeaponLink35"):
                opp_val = getattr(value, "dsl_UnitWeaponLink35", None)
                setattr(value, "dsl_UnitWeaponLink35", self)

    @property
    def dsl_Weapon44(self):
        return self.__dsl_Weapon44

    @dsl_Weapon44.setter
    def dsl_Weapon44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Weapon__dsl_Weapon44", None)
        self.__dsl_Weapon44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Actor45"):
                opp_val = getattr(old_value, "dsl_Actor45", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Actor45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Actor45"):
                opp_val = getattr(value, "dsl_Actor45", None)
                setattr(value, "dsl_Actor45", self)

    @property
    def dsl_Weapon41(self):
        return self.__dsl_Weapon41

    @dsl_Weapon41.setter
    def dsl_Weapon41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Weapon__dsl_Weapon41", None)
        self.__dsl_Weapon41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Effect42"):
                opp_val = getattr(old_value, "dsl_Effect42", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Effect42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Effect42"):
                opp_val = getattr(value, "dsl_Effect42", None)
                setattr(value, "dsl_Effect42", self)

class dsl_Model:

    pass