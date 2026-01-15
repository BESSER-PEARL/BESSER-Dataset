from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class error3_Bazbar:

    def __init__(self, b: str, error3_Bazbar: "error3_RecursiveComponen" = None):
        self.b = b
        self.error3_Bazbar = error3_Bazbar
        
    @property
    def b(self) -> str:
        return self.__b

    @b.setter
    def b(self, b: str):
        self.__b = b

    @property
    def error3_Bazbar(self):
        return self.__error3_Bazbar

    @error3_Bazbar.setter
    def error3_Bazbar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_error3_Bazbar__error3_Bazbar", None)
        self.__error3_Bazbar = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "error3_RecursiveComponen20"):
                opp_val = getattr(old_value, "error3_RecursiveComponen20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "error3_RecursiveComponen20"):
                opp_val = getattr(value, "error3_RecursiveComponen20", None)
                if opp_val is None:
                    setattr(value, "error3_RecursiveComponen20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AbstractComponent:

    pass
class error3_RecursiveComponen(AbstractComponent):

    pass
class error3_NestedComponent(AbstractComponent):

    pass
class error3_Level2(AbstractComponent):

    pass
class error3_AbstractComponent:

    def __init__(self, name: str, error3_AbstractComponent: set["error3_Required"] = None, error3_AbstractComponent14: set["error3_Provided"] = None):
        self.name = name
        self.error3_AbstractComponent = error3_AbstractComponent if error3_AbstractComponent is not None else set()
        self.error3_AbstractComponent14 = error3_AbstractComponent14 if error3_AbstractComponent14 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def error3_AbstractComponent(self):
        return self.__error3_AbstractComponent

    @error3_AbstractComponent.setter
    def error3_AbstractComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_error3_AbstractComponent__error3_AbstractComponent", None)
        self.__error3_AbstractComponent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "error3_Required12"):
                    opp_val = getattr(item, "error3_Required12", None)
                    
                    if opp_val == self:
                        setattr(item, "error3_Required12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "error3_Required12"):
                    opp_val = getattr(item, "error3_Required12", None)
                    
                    setattr(item, "error3_Required12", self)
                    

    @property
    def error3_AbstractComponent14(self):
        return self.__error3_AbstractComponent14

    @error3_AbstractComponent14.setter
    def error3_AbstractComponent14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_error3_AbstractComponent__error3_AbstractComponent14", None)
        self.__error3_AbstractComponent14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "error3_Provided15"):
                    opp_val = getattr(item, "error3_Provided15", None)
                    
                    if opp_val == self:
                        setattr(item, "error3_Provided15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "error3_Provided15"):
                    opp_val = getattr(item, "error3_Provided15", None)
                    
                    setattr(item, "error3_Provided15", self)
                    

class error3_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class error3_Provided:

    def __init__(self, ip: str, error3_Provided: "error3_Binding" = None, error3_Provided15: "error3_AbstractComponent" = None):
        self.ip = ip
        self.error3_Provided = error3_Provided
        self.error3_Provided15 = error3_Provided15
        
    @property
    def ip(self) -> str:
        return self.__ip

    @ip.setter
    def ip(self, ip: str):
        self.__ip = ip

    @property
    def error3_Provided15(self):
        return self.__error3_Provided15

    @error3_Provided15.setter
    def error3_Provided15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_error3_Provided__error3_Provided15", None)
        self.__error3_Provided15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "error3_AbstractComponent14"):
                opp_val = getattr(old_value, "error3_AbstractComponent14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "error3_AbstractComponent14"):
                opp_val = getattr(value, "error3_AbstractComponent14", None)
                if opp_val is None:
                    setattr(value, "error3_AbstractComponent14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def error3_Provided(self):
        return self.__error3_Provided

    @error3_Provided.setter
    def error3_Provided(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_error3_Provided__error3_Provided", None)
        self.__error3_Provided = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "error3_Binding10"):
                opp_val = getattr(old_value, "error3_Binding10", None)
                if opp_val == self:
                    setattr(old_value, "error3_Binding10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "error3_Binding10"):
                opp_val = getattr(value, "error3_Binding10", None)
                setattr(value, "error3_Binding10", self)

class error3_Binding:

    def __init__(self, type: str, error3_Binding: "error3_Required" = None, error3_Binding7: "error3_Required" = None, error3_Binding10: "error3_Provided" = None):
        self.type = type
        self.error3_Binding = error3_Binding
        self.error3_Binding7 = error3_Binding7
        self.error3_Binding10 = error3_Binding10
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def error3_Binding7(self):
        return self.__error3_Binding7

    @error3_Binding7.setter
    def error3_Binding7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_error3_Binding__error3_Binding7", None)
        self.__error3_Binding7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "error3_Required8"):
                opp_val = getattr(old_value, "error3_Required8", None)
                if opp_val == self:
                    setattr(old_value, "error3_Required8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "error3_Required8"):
                opp_val = getattr(value, "error3_Required8", None)
                setattr(value, "error3_Required8", self)

    @property
    def error3_Binding(self):
        return self.__error3_Binding

    @error3_Binding.setter
    def error3_Binding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_error3_Binding__error3_Binding", None)
        self.__error3_Binding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "error3_Required"):
                opp_val = getattr(old_value, "error3_Required", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "error3_Required"):
                opp_val = getattr(value, "error3_Required", None)
                if opp_val is None:
                    setattr(value, "error3_Required", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def error3_Binding10(self):
        return self.__error3_Binding10

    @error3_Binding10.setter
    def error3_Binding10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_error3_Binding__error3_Binding10", None)
        self.__error3_Binding10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "error3_Provided"):
                opp_val = getattr(old_value, "error3_Provided", None)
                if opp_val == self:
                    setattr(old_value, "error3_Provided", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "error3_Provided"):
                opp_val = getattr(value, "error3_Provided", None)
                setattr(value, "error3_Provided", self)

class error3_Required:

    def __init__(self, ir: str, error3_Required: set["error3_Binding"] = None, error3_Required8: "error3_Binding" = None, error3_Required12: "error3_AbstractComponent" = None):
        self.ir = ir
        self.error3_Required = error3_Required if error3_Required is not None else set()
        self.error3_Required8 = error3_Required8
        self.error3_Required12 = error3_Required12
        
    @property
    def ir(self) -> str:
        return self.__ir

    @ir.setter
    def ir(self, ir: str):
        self.__ir = ir

    @property
    def error3_Required(self):
        return self.__error3_Required

    @error3_Required.setter
    def error3_Required(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_error3_Required__error3_Required", None)
        self.__error3_Required = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "error3_Binding"):
                    opp_val = getattr(item, "error3_Binding", None)
                    
                    if opp_val == self:
                        setattr(item, "error3_Binding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "error3_Binding"):
                    opp_val = getattr(item, "error3_Binding", None)
                    
                    setattr(item, "error3_Binding", self)
                    

    @property
    def error3_Required8(self):
        return self.__error3_Required8

    @error3_Required8.setter
    def error3_Required8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_error3_Required__error3_Required8", None)
        self.__error3_Required8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "error3_Binding7"):
                opp_val = getattr(old_value, "error3_Binding7", None)
                if opp_val == self:
                    setattr(old_value, "error3_Binding7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "error3_Binding7"):
                opp_val = getattr(value, "error3_Binding7", None)
                setattr(value, "error3_Binding7", self)

    @property
    def error3_Required12(self):
        return self.__error3_Required12

    @error3_Required12.setter
    def error3_Required12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_error3_Required__error3_Required12", None)
        self.__error3_Required12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "error3_AbstractComponent"):
                opp_val = getattr(old_value, "error3_AbstractComponent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "error3_AbstractComponent"):
                opp_val = getattr(value, "error3_AbstractComponent", None)
                if opp_val is None:
                    setattr(value, "error3_AbstractComponent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class NamedElement:

    pass
class error3_RelatedTo(NamedElement):

    def __init__(self, since: str, RelatedTo: "error3_Thing" = None, relations: "error3_Thing" = None, error3_RelatedTo: "error3_Thing" = None):
        self.since = since
        self.RelatedTo = RelatedTo
        self.relations = relations
        self.error3_RelatedTo = error3_RelatedTo
        
    @property
    def since(self) -> str:
        return self.__since

    @since.setter
    def since(self, since: str):
        self.__since = since

    @property
    def RelatedTo(self):
        return self.__RelatedTo

    @RelatedTo.setter
    def RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_error3_RelatedTo__RelatedTo", None)
        self.__RelatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fromThing"):
                opp_val = getattr(old_value, "fromThing", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fromThing"):
                opp_val = getattr(value, "fromThing", None)
                if opp_val is None:
                    setattr(value, "fromThing", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def relations(self):
        return self.__relations

    @relations.setter
    def relations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_error3_RelatedTo__relations", None)
        self.__relations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Thing"):
                opp_val = getattr(old_value, "Thing", None)
                if opp_val == self:
                    setattr(old_value, "Thing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Thing"):
                opp_val = getattr(value, "Thing", None)
                setattr(value, "Thing", self)

    @property
    def error3_RelatedTo(self):
        return self.__error3_RelatedTo

    @error3_RelatedTo.setter
    def error3_RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_error3_RelatedTo__error3_RelatedTo", None)
        self.__error3_RelatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "error3_Thing4"):
                opp_val = getattr(old_value, "error3_Thing4", None)
                if opp_val == self:
                    setattr(old_value, "error3_Thing4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "error3_Thing4"):
                opp_val = getattr(value, "error3_Thing4", None)
                setattr(value, "error3_Thing4", self)

class error3_Thing(NamedElement):

    def __init__(self, id: int, error3_Thing: "error3_World" = None, Thing: "error3_RelatedTo" = None, error3_Thing4: "error3_RelatedTo" = None, fromThing: set["error3_RelatedTo"] = None):
        self.id = id
        self.error3_Thing = error3_Thing
        self.Thing = Thing
        self.error3_Thing4 = error3_Thing4
        self.fromThing = fromThing if fromThing is not None else set()
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def error3_Thing4(self):
        return self.__error3_Thing4

    @error3_Thing4.setter
    def error3_Thing4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_error3_Thing__error3_Thing4", None)
        self.__error3_Thing4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "error3_RelatedTo"):
                opp_val = getattr(old_value, "error3_RelatedTo", None)
                if opp_val == self:
                    setattr(old_value, "error3_RelatedTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "error3_RelatedTo"):
                opp_val = getattr(value, "error3_RelatedTo", None)
                setattr(value, "error3_RelatedTo", self)

    @property
    def error3_Thing(self):
        return self.__error3_Thing

    @error3_Thing.setter
    def error3_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_error3_Thing__error3_Thing", None)
        self.__error3_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "error3_World"):
                opp_val = getattr(old_value, "error3_World", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "error3_World"):
                opp_val = getattr(value, "error3_World", None)
                if opp_val is None:
                    setattr(value, "error3_World", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Thing(self):
        return self.__Thing

    @Thing.setter
    def Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_error3_Thing__Thing", None)
        self.__Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relations"):
                opp_val = getattr(old_value, "relations", None)
                if opp_val == self:
                    setattr(old_value, "relations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relations"):
                opp_val = getattr(value, "relations", None)
                setattr(value, "relations", self)

    @property
    def fromThing(self):
        return self.__fromThing

    @fromThing.setter
    def fromThing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_error3_Thing__fromThing", None)
        self.__fromThing = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RelatedTo"):
                    opp_val = getattr(item, "RelatedTo", None)
                    
                    if opp_val == self:
                        setattr(item, "RelatedTo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RelatedTo"):
                    opp_val = getattr(item, "RelatedTo", None)
                    
                    setattr(item, "RelatedTo", self)
                    

class error3_World:

    pass