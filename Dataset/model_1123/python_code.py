from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class uppaallite_TransitionType:

    def __init__(self, sync: str, assignment: str, guard: str, cost: str, uppaallite_TransitionType: "uppaallite_LocationType" = None, uppaallite_TransitionType7: "uppaallite_LocationType" = None, transition: "uppaallite_TemplateType" = None, TransitionType: "uppaallite_TemplateType" = None):
        self.sync = sync
        self.assignment = assignment
        self.guard = guard
        self.cost = cost
        self.uppaallite_TransitionType = uppaallite_TransitionType
        self.uppaallite_TransitionType7 = uppaallite_TransitionType7
        self.transition = transition
        self.TransitionType = TransitionType
        
    @property
    def guard(self) -> str:
        return self.__guard

    @guard.setter
    def guard(self, guard: str):
        self.__guard = guard

    @property
    def assignment(self) -> str:
        return self.__assignment

    @assignment.setter
    def assignment(self, assignment: str):
        self.__assignment = assignment

    @property
    def sync(self) -> str:
        return self.__sync

    @sync.setter
    def sync(self, sync: str):
        self.__sync = sync

    @property
    def cost(self) -> str:
        return self.__cost

    @cost.setter
    def cost(self, cost: str):
        self.__cost = cost

    @property
    def uppaallite_TransitionType7(self):
        return self.__uppaallite_TransitionType7

    @uppaallite_TransitionType7.setter
    def uppaallite_TransitionType7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaallite_TransitionType__uppaallite_TransitionType7", None)
        self.__uppaallite_TransitionType7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uppaallite_LocationType8"):
                opp_val = getattr(old_value, "uppaallite_LocationType8", None)
                if opp_val == self:
                    setattr(old_value, "uppaallite_LocationType8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uppaallite_LocationType8"):
                opp_val = getattr(value, "uppaallite_LocationType8", None)
                setattr(value, "uppaallite_LocationType8", self)

    @property
    def uppaallite_TransitionType(self):
        return self.__uppaallite_TransitionType

    @uppaallite_TransitionType.setter
    def uppaallite_TransitionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaallite_TransitionType__uppaallite_TransitionType", None)
        self.__uppaallite_TransitionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uppaallite_LocationType"):
                opp_val = getattr(old_value, "uppaallite_LocationType", None)
                if opp_val == self:
                    setattr(old_value, "uppaallite_LocationType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uppaallite_LocationType"):
                opp_val = getattr(value, "uppaallite_LocationType", None)
                setattr(value, "uppaallite_LocationType", self)

    @property
    def TransitionType(self):
        return self.__TransitionType

    @TransitionType.setter
    def TransitionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaallite_TransitionType__TransitionType", None)
        self.__TransitionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "container3"):
                opp_val = getattr(old_value, "container3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "container3"):
                opp_val = getattr(value, "container3", None)
                if opp_val is None:
                    setattr(value, "container3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def transition(self):
        return self.__transition

    @transition.setter
    def transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaallite_TransitionType__transition", None)
        self.__transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TemplateType10"):
                opp_val = getattr(old_value, "TemplateType10", None)
                if opp_val == self:
                    setattr(old_value, "TemplateType10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TemplateType10"):
                opp_val = getattr(value, "TemplateType10", None)
                setattr(value, "TemplateType10", self)

class uppaallite_LocationType:

    def __init__(self, y: int, name: str, urgent: bool, committed: bool, initial: bool, id: str, invariant: str, cost: str, x: int, uppaallite_LocationType: "uppaallite_TransitionType" = None, uppaallite_LocationType8: "uppaallite_TransitionType" = None, LocationType: "uppaallite_TemplateType" = None, location: "uppaallite_TemplateType" = None):
        self.y = y
        self.name = name
        self.urgent = urgent
        self.committed = committed
        self.initial = initial
        self.id = id
        self.invariant = invariant
        self.cost = cost
        self.x = x
        self.uppaallite_LocationType = uppaallite_LocationType
        self.uppaallite_LocationType8 = uppaallite_LocationType8
        self.LocationType = LocationType
        self.location = location
        
    @property
    def invariant(self) -> str:
        return self.__invariant

    @invariant.setter
    def invariant(self, invariant: str):
        self.__invariant = invariant

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def urgent(self) -> bool:
        return self.__urgent

    @urgent.setter
    def urgent(self, urgent: bool):
        self.__urgent = urgent

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cost(self) -> str:
        return self.__cost

    @cost.setter
    def cost(self, cost: str):
        self.__cost = cost

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def committed(self) -> bool:
        return self.__committed

    @committed.setter
    def committed(self, committed: bool):
        self.__committed = committed

    @property
    def initial(self) -> bool:
        return self.__initial

    @initial.setter
    def initial(self, initial: bool):
        self.__initial = initial

    @property
    def LocationType(self):
        return self.__LocationType

    @LocationType.setter
    def LocationType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaallite_LocationType__LocationType", None)
        self.__LocationType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "container"):
                opp_val = getattr(old_value, "container", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "container"):
                opp_val = getattr(value, "container", None)
                if opp_val is None:
                    setattr(value, "container", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uppaallite_LocationType8(self):
        return self.__uppaallite_LocationType8

    @uppaallite_LocationType8.setter
    def uppaallite_LocationType8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaallite_LocationType__uppaallite_LocationType8", None)
        self.__uppaallite_LocationType8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uppaallite_TransitionType7"):
                opp_val = getattr(old_value, "uppaallite_TransitionType7", None)
                if opp_val == self:
                    setattr(old_value, "uppaallite_TransitionType7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uppaallite_TransitionType7"):
                opp_val = getattr(value, "uppaallite_TransitionType7", None)
                setattr(value, "uppaallite_TransitionType7", self)

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaallite_LocationType__location", None)
        self.__location = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TemplateType"):
                opp_val = getattr(old_value, "TemplateType", None)
                if opp_val == self:
                    setattr(old_value, "TemplateType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TemplateType"):
                opp_val = getattr(value, "TemplateType", None)
                setattr(value, "TemplateType", self)

    @property
    def uppaallite_LocationType(self):
        return self.__uppaallite_LocationType

    @uppaallite_LocationType.setter
    def uppaallite_LocationType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaallite_LocationType__uppaallite_LocationType", None)
        self.__uppaallite_LocationType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uppaallite_TransitionType"):
                opp_val = getattr(old_value, "uppaallite_TransitionType", None)
                if opp_val == self:
                    setattr(old_value, "uppaallite_TransitionType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uppaallite_TransitionType"):
                opp_val = getattr(value, "uppaallite_TransitionType", None)
                setattr(value, "uppaallite_TransitionType", self)

class uppaallite_TemplateType:

    def __init__(self, name: str, declaration: str, uppaallite_TemplateType: "uppaallite_UppaalDiagram" = None, TemplateType10: "uppaallite_TransitionType" = None, container: set["uppaallite_LocationType"] = None, container3: set["uppaallite_TransitionType"] = None, TemplateType: "uppaallite_LocationType" = None):
        self.name = name
        self.declaration = declaration
        self.uppaallite_TemplateType = uppaallite_TemplateType
        self.TemplateType10 = TemplateType10
        self.container = container if container is not None else set()
        self.container3 = container3 if container3 is not None else set()
        self.TemplateType = TemplateType
        
    @property
    def declaration(self) -> str:
        return self.__declaration

    @declaration.setter
    def declaration(self, declaration: str):
        self.__declaration = declaration

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def TemplateType10(self):
        return self.__TemplateType10

    @TemplateType10.setter
    def TemplateType10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaallite_TemplateType__TemplateType10", None)
        self.__TemplateType10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transition"):
                opp_val = getattr(old_value, "transition", None)
                if opp_val == self:
                    setattr(old_value, "transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transition"):
                opp_val = getattr(value, "transition", None)
                setattr(value, "transition", self)

    @property
    def container3(self):
        return self.__container3

    @container3.setter
    def container3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaallite_TemplateType__container3", None)
        self.__container3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TransitionType"):
                    opp_val = getattr(item, "TransitionType", None)
                    
                    if opp_val == self:
                        setattr(item, "TransitionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TransitionType"):
                    opp_val = getattr(item, "TransitionType", None)
                    
                    setattr(item, "TransitionType", self)
                    

    @property
    def TemplateType(self):
        return self.__TemplateType

    @TemplateType.setter
    def TemplateType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaallite_TemplateType__TemplateType", None)
        self.__TemplateType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "location"):
                opp_val = getattr(old_value, "location", None)
                if opp_val == self:
                    setattr(old_value, "location", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "location"):
                opp_val = getattr(value, "location", None)
                setattr(value, "location", self)

    @property
    def uppaallite_TemplateType(self):
        return self.__uppaallite_TemplateType

    @uppaallite_TemplateType.setter
    def uppaallite_TemplateType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaallite_TemplateType__uppaallite_TemplateType", None)
        self.__uppaallite_TemplateType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uppaallite_UppaalDiagram"):
                opp_val = getattr(old_value, "uppaallite_UppaalDiagram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uppaallite_UppaalDiagram"):
                opp_val = getattr(value, "uppaallite_UppaalDiagram", None)
                if opp_val is None:
                    setattr(value, "uppaallite_UppaalDiagram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def container(self):
        return self.__container

    @container.setter
    def container(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaallite_TemplateType__container", None)
        self.__container = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LocationType"):
                    opp_val = getattr(item, "LocationType", None)
                    
                    if opp_val == self:
                        setattr(item, "LocationType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LocationType"):
                    opp_val = getattr(item, "LocationType", None)
                    
                    setattr(item, "LocationType", self)
                    

class uppaallite_UppaalDiagram:

    def __init__(self, declaration: str, resourceWeightDeclaration: str, uppaallite_UppaalDiagram: set["uppaallite_TemplateType"] = None):
        self.declaration = declaration
        self.resourceWeightDeclaration = resourceWeightDeclaration
        self.uppaallite_UppaalDiagram = uppaallite_UppaalDiagram if uppaallite_UppaalDiagram is not None else set()
        
    @property
    def declaration(self) -> str:
        return self.__declaration

    @declaration.setter
    def declaration(self, declaration: str):
        self.__declaration = declaration

    @property
    def resourceWeightDeclaration(self) -> str:
        return self.__resourceWeightDeclaration

    @resourceWeightDeclaration.setter
    def resourceWeightDeclaration(self, resourceWeightDeclaration: str):
        self.__resourceWeightDeclaration = resourceWeightDeclaration

    @property
    def uppaallite_UppaalDiagram(self):
        return self.__uppaallite_UppaalDiagram

    @uppaallite_UppaalDiagram.setter
    def uppaallite_UppaalDiagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uppaallite_UppaalDiagram__uppaallite_UppaalDiagram", None)
        self.__uppaallite_UppaalDiagram = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uppaallite_TemplateType"):
                    opp_val = getattr(item, "uppaallite_TemplateType", None)
                    
                    if opp_val == self:
                        setattr(item, "uppaallite_TemplateType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uppaallite_TemplateType"):
                    opp_val = getattr(item, "uppaallite_TemplateType", None)
                    
                    setattr(item, "uppaallite_TemplateType", self)
                    
