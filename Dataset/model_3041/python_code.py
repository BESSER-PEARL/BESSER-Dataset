from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class actions_Parameter:

    pass
class actions_Participant:

    pass
class actions_Distribution:

    def __init__(self, datapoint: float, density: float, id: int, version: int, actions_Distribution: "actions_AtomicActionResult" = None, actions_Distribution12: "actions_AtomicActionResult" = None, actions_Distribution15: "actions_AtomicActionResult" = None):
        self.datapoint = datapoint
        self.density = density
        self.id = id
        self.version = version
        self.actions_Distribution = actions_Distribution
        self.actions_Distribution12 = actions_Distribution12
        self.actions_Distribution15 = actions_Distribution15
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def version(self) -> int:
        return self.__version

    @version.setter
    def version(self, version: int):
        self.__version = version

    @property
    def density(self) -> float:
        return self.__density

    @density.setter
    def density(self, density: float):
        self.__density = density

    @property
    def datapoint(self) -> float:
        return self.__datapoint

    @datapoint.setter
    def datapoint(self, datapoint: float):
        self.__datapoint = datapoint

    @property
    def actions_Distribution(self):
        return self.__actions_Distribution

    @actions_Distribution.setter
    def actions_Distribution(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_actions_Distribution__actions_Distribution", None)
        self.__actions_Distribution = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "actions_AtomicActionResult9"):
                opp_val = getattr(old_value, "actions_AtomicActionResult9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "actions_AtomicActionResult9"):
                opp_val = getattr(value, "actions_AtomicActionResult9", None)
                if opp_val is None:
                    setattr(value, "actions_AtomicActionResult9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def actions_Distribution12(self):
        return self.__actions_Distribution12

    @actions_Distribution12.setter
    def actions_Distribution12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_actions_Distribution__actions_Distribution12", None)
        self.__actions_Distribution12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "actions_AtomicActionResult11"):
                opp_val = getattr(old_value, "actions_AtomicActionResult11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "actions_AtomicActionResult11"):
                opp_val = getattr(value, "actions_AtomicActionResult11", None)
                if opp_val is None:
                    setattr(value, "actions_AtomicActionResult11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def actions_Distribution15(self):
        return self.__actions_Distribution15

    @actions_Distribution15.setter
    def actions_Distribution15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_actions_Distribution__actions_Distribution15", None)
        self.__actions_Distribution15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "actions_AtomicActionResult14"):
                opp_val = getattr(old_value, "actions_AtomicActionResult14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "actions_AtomicActionResult14"):
                opp_val = getattr(value, "actions_AtomicActionResult14", None)
                if opp_val is None:
                    setattr(value, "actions_AtomicActionResult14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ActionResult:

    pass
class actions_ActionsCollection:

    def __init__(self, ns: str, id: int, version: int, actions_ActionsCollection: set["actions_Action"] = None, actions_ActionsCollection19: set["actions_Participant"] = None, actions_ActionsCollection21: set["actions_Parameter"] = None):
        self.ns = ns
        self.id = id
        self.version = version
        self.actions_ActionsCollection = actions_ActionsCollection if actions_ActionsCollection is not None else set()
        self.actions_ActionsCollection19 = actions_ActionsCollection19 if actions_ActionsCollection19 is not None else set()
        self.actions_ActionsCollection21 = actions_ActionsCollection21 if actions_ActionsCollection21 is not None else set()
        
    @property
    def ns(self) -> str:
        return self.__ns

    @ns.setter
    def ns(self, ns: str):
        self.__ns = ns

    @property
    def version(self) -> int:
        return self.__version

    @version.setter
    def version(self, version: int):
        self.__version = version

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def actions_ActionsCollection21(self):
        return self.__actions_ActionsCollection21

    @actions_ActionsCollection21.setter
    def actions_ActionsCollection21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_actions_ActionsCollection__actions_ActionsCollection21", None)
        self.__actions_ActionsCollection21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "actions_Parameter"):
                    opp_val = getattr(item, "actions_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "actions_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "actions_Parameter"):
                    opp_val = getattr(item, "actions_Parameter", None)
                    
                    setattr(item, "actions_Parameter", self)
                    

    @property
    def actions_ActionsCollection19(self):
        return self.__actions_ActionsCollection19

    @actions_ActionsCollection19.setter
    def actions_ActionsCollection19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_actions_ActionsCollection__actions_ActionsCollection19", None)
        self.__actions_ActionsCollection19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "actions_Participant"):
                    opp_val = getattr(item, "actions_Participant", None)
                    
                    if opp_val == self:
                        setattr(item, "actions_Participant", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "actions_Participant"):
                    opp_val = getattr(item, "actions_Participant", None)
                    
                    setattr(item, "actions_Participant", self)
                    

    @property
    def actions_ActionsCollection(self):
        return self.__actions_ActionsCollection

    @actions_ActionsCollection.setter
    def actions_ActionsCollection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_actions_ActionsCollection__actions_ActionsCollection", None)
        self.__actions_ActionsCollection = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "actions_Action17"):
                    opp_val = getattr(item, "actions_Action17", None)
                    
                    if opp_val == self:
                        setattr(item, "actions_Action17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "actions_Action17"):
                    opp_val = getattr(item, "actions_Action17", None)
                    
                    setattr(item, "actions_Action17", self)
                    

class actions_AtomicActionResult(ActionResult):

    def __init__(self, hasDensity: float, actions_AtomicActionResult: "actions_AtomicAction" = None, actions_AtomicActionResult9: set["actions_Distribution"] = None, actions_AtomicActionResult11: set["actions_Distribution"] = None, actions_AtomicActionResult14: set["actions_Distribution"] = None):
        self.hasDensity = hasDensity
        self.actions_AtomicActionResult = actions_AtomicActionResult
        self.actions_AtomicActionResult9 = actions_AtomicActionResult9 if actions_AtomicActionResult9 is not None else set()
        self.actions_AtomicActionResult11 = actions_AtomicActionResult11 if actions_AtomicActionResult11 is not None else set()
        self.actions_AtomicActionResult14 = actions_AtomicActionResult14 if actions_AtomicActionResult14 is not None else set()
        
    @property
    def hasDensity(self) -> float:
        return self.__hasDensity

    @hasDensity.setter
    def hasDensity(self, hasDensity: float):
        self.__hasDensity = hasDensity

    @property
    def actions_AtomicActionResult(self):
        return self.__actions_AtomicActionResult

    @actions_AtomicActionResult.setter
    def actions_AtomicActionResult(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_actions_AtomicActionResult__actions_AtomicActionResult", None)
        self.__actions_AtomicActionResult = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "actions_AtomicAction"):
                opp_val = getattr(old_value, "actions_AtomicAction", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "actions_AtomicAction"):
                opp_val = getattr(value, "actions_AtomicAction", None)
                if opp_val is None:
                    setattr(value, "actions_AtomicAction", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def actions_AtomicActionResult9(self):
        return self.__actions_AtomicActionResult9

    @actions_AtomicActionResult9.setter
    def actions_AtomicActionResult9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_actions_AtomicActionResult__actions_AtomicActionResult9", None)
        self.__actions_AtomicActionResult9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "actions_Distribution"):
                    opp_val = getattr(item, "actions_Distribution", None)
                    
                    if opp_val == self:
                        setattr(item, "actions_Distribution", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "actions_Distribution"):
                    opp_val = getattr(item, "actions_Distribution", None)
                    
                    setattr(item, "actions_Distribution", self)
                    

    @property
    def actions_AtomicActionResult11(self):
        return self.__actions_AtomicActionResult11

    @actions_AtomicActionResult11.setter
    def actions_AtomicActionResult11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_actions_AtomicActionResult__actions_AtomicActionResult11", None)
        self.__actions_AtomicActionResult11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "actions_Distribution12"):
                    opp_val = getattr(item, "actions_Distribution12", None)
                    
                    if opp_val == self:
                        setattr(item, "actions_Distribution12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "actions_Distribution12"):
                    opp_val = getattr(item, "actions_Distribution12", None)
                    
                    setattr(item, "actions_Distribution12", self)
                    

    @property
    def actions_AtomicActionResult14(self):
        return self.__actions_AtomicActionResult14

    @actions_AtomicActionResult14.setter
    def actions_AtomicActionResult14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_actions_AtomicActionResult__actions_AtomicActionResult14", None)
        self.__actions_AtomicActionResult14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "actions_Distribution15"):
                    opp_val = getattr(item, "actions_Distribution15", None)
                    
                    if opp_val == self:
                        setattr(item, "actions_Distribution15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "actions_Distribution15"):
                    opp_val = getattr(item, "actions_Distribution15", None)
                    
                    setattr(item, "actions_Distribution15", self)
                    

class AtomicProcess:

    pass
class Action:

    pass
class actions_AtomicAction(AtomicProcess, Action):

    pass
class actions_Role:

    pass
class Process:

    pass
class actions_Action(Process):

    pass
class actions_Expression:

    pass
class actions_Condition:

    pass
class actions_ActionResult:

    def __init__(self, id: int, version: int, actions_ActionResult: set["actions_Condition"] = None, actions_ActionResult4: set["actions_Expression"] = None, actions_ActionResult6: set["actions_Expression"] = None):
        self.id = id
        self.version = version
        self.actions_ActionResult = actions_ActionResult if actions_ActionResult is not None else set()
        self.actions_ActionResult4 = actions_ActionResult4 if actions_ActionResult4 is not None else set()
        self.actions_ActionResult6 = actions_ActionResult6 if actions_ActionResult6 is not None else set()
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def version(self) -> int:
        return self.__version

    @version.setter
    def version(self, version: int):
        self.__version = version

    @property
    def actions_ActionResult6(self):
        return self.__actions_ActionResult6

    @actions_ActionResult6.setter
    def actions_ActionResult6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_actions_ActionResult__actions_ActionResult6", None)
        self.__actions_ActionResult6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "actions_Expression7"):
                    opp_val = getattr(item, "actions_Expression7", None)
                    
                    if opp_val == self:
                        setattr(item, "actions_Expression7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "actions_Expression7"):
                    opp_val = getattr(item, "actions_Expression7", None)
                    
                    setattr(item, "actions_Expression7", self)
                    

    @property
    def actions_ActionResult4(self):
        return self.__actions_ActionResult4

    @actions_ActionResult4.setter
    def actions_ActionResult4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_actions_ActionResult__actions_ActionResult4", None)
        self.__actions_ActionResult4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "actions_Expression"):
                    opp_val = getattr(item, "actions_Expression", None)
                    
                    if opp_val == self:
                        setattr(item, "actions_Expression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "actions_Expression"):
                    opp_val = getattr(item, "actions_Expression", None)
                    
                    setattr(item, "actions_Expression", self)
                    

    @property
    def actions_ActionResult(self):
        return self.__actions_ActionResult

    @actions_ActionResult.setter
    def actions_ActionResult(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_actions_ActionResult__actions_ActionResult", None)
        self.__actions_ActionResult = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "actions_Condition"):
                    opp_val = getattr(item, "actions_Condition", None)
                    
                    if opp_val == self:
                        setattr(item, "actions_Condition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "actions_Condition"):
                    opp_val = getattr(item, "actions_Condition", None)
                    
                    setattr(item, "actions_Condition", self)
                    

class CompositeProcess:

    pass
class actions_CompositeAction(CompositeProcess, Action):

    pass