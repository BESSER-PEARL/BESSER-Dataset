from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class AbstractConection:

    pass
class FSmachine_ReasonConnection(AbstractConection):

    def __init__(self, reason: str):
        self.reason = reason
        
        pass
    @property
    def reason(self):
        return self.__reason

    @reason.setter
    def reason(self, reason: str):
        self.__reason = reason


class AbstractObject:

    pass
class FSmachine_State(AbstractObject):

    def __init__(self, description: str, data: str):
        self.description = description
        self.data = data
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data


class FSmachine_TimeConnection(AbstractConection):

    def __init__(self, when: str):
        self.when = when
        
        pass
    @property
    def when(self):
        return self.__when

    @when.setter
    def when(self, when: str):
        self.__when = when


class FSmachine_AbstractObject:

    def __init__(self, name: str, active: bool, AbstractObject: "FSmachine_Root" = None, prev: "FSmachine_AbstractConection" = None, objects: "FSmachine_Root" = None, next: "FSmachine_AbstractConection" = None, AbstractObject10: "FSmachine_AbstractConection" = None, AbstractObject12: "FSmachine_AbstractConection" = None):
        self.name = name
        self.active = active
        self.AbstractObject = AbstractObject
        self.prev = prev
        self.objects = objects
        self.next = next
        self.AbstractObject10 = AbstractObject10
        self.AbstractObject12 = AbstractObject12
        
        pass
    @property
    def active(self):
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def objects(self):
        return self.__objects

    @objects.setter
    def objects(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSmachine_AbstractObject__objects", None)
        self.__objects = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Root"):
                opp_val = getattr(old_value, "Root", None)
                if opp_val == self:
                    setattr(old_value, "Root", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Root"):
                opp_val = getattr(value, "Root", None)
                setattr(value, "Root", self)

    @property
    def AbstractObject(self):
        return self.__AbstractObject

    @AbstractObject.setter
    def AbstractObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSmachine_AbstractObject__AbstractObject", None)
        self.__AbstractObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent"):
                opp_val = getattr(old_value, "parent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent"):
                opp_val = getattr(value, "parent", None)
                if opp_val is None:
                    setattr(value, "parent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSmachine_AbstractObject__next", None)
        self.__next = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractConection4"):
                opp_val = getattr(old_value, "AbstractConection4", None)
                if opp_val == self:
                    setattr(old_value, "AbstractConection4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractConection4"):
                opp_val = getattr(value, "AbstractConection4", None)
                setattr(value, "AbstractConection4", self)

    @property
    def AbstractObject12(self):
        return self.__AbstractObject12

    @AbstractObject12.setter
    def AbstractObject12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSmachine_AbstractObject__AbstractObject12", None)
        self.__AbstractObject12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conParent"):
                opp_val = getattr(old_value, "conParent", None)
                if opp_val == self:
                    setattr(old_value, "conParent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conParent"):
                opp_val = getattr(value, "conParent", None)
                setattr(value, "conParent", self)

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSmachine_AbstractObject__prev", None)
        self.__prev = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractConection6"):
                opp_val = getattr(old_value, "AbstractConection6", None)
                if opp_val == self:
                    setattr(old_value, "AbstractConection6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractConection6"):
                opp_val = getattr(value, "AbstractConection6", None)
                setattr(value, "AbstractConection6", self)

    @property
    def AbstractObject10(self):
        return self.__AbstractObject10

    @AbstractObject10.setter
    def AbstractObject10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSmachine_AbstractObject__AbstractObject10", None)
        self.__AbstractObject10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conChild"):
                opp_val = getattr(old_value, "conChild", None)
                if opp_val == self:
                    setattr(old_value, "conChild", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conChild"):
                opp_val = getattr(value, "conChild", None)
                setattr(value, "conChild", self)

    def makeMeActive(self):
        # TODO: Implement makeMeActive method
        pass

    def checkStatussen(self) :
        # TODO: Implement checkStatussen method
        pass

class FSmachine_Root:

    def __init__(self, FSmachineName: str, par: set["FSmachine_AbstractConection"] = None, parent: set["FSmachine_AbstractObject"] = None, Root: "FSmachine_AbstractObject" = None, Root8: "FSmachine_AbstractConection" = None):
        self.FSmachineName = FSmachineName
        self.par = par if par is not None else set()
        self.parent = parent if parent is not None else set()
        self.Root = Root
        self.Root8 = Root8
        
        pass
    @property
    def FSmachineName(self):
        return self.__FSmachineName

    @FSmachineName.setter
    def FSmachineName(self, FSmachineName: str):
        self.__FSmachineName = FSmachineName


    @property
    def Root8(self):
        return self.__Root8

    @Root8.setter
    def Root8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSmachine_Root__Root8", None)
        self.__Root8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connections"):
                opp_val = getattr(old_value, "connections", None)
                if opp_val == self:
                    setattr(old_value, "connections", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connections"):
                opp_val = getattr(value, "connections", None)
                setattr(value, "connections", self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSmachine_Root__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractObject"):
                    opp_val = getattr(item, "AbstractObject", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractObject"):
                    opp_val = getattr(item, "AbstractObject", None)
                    
                    setattr(item, "AbstractObject", self)
                    

    @property
    def Root(self):
        return self.__Root

    @Root.setter
    def Root(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSmachine_Root__Root", None)
        self.__Root = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "objects"):
                opp_val = getattr(old_value, "objects", None)
                if opp_val == self:
                    setattr(old_value, "objects", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "objects"):
                opp_val = getattr(value, "objects", None)
                setattr(value, "objects", self)

    @property
    def par(self):
        return self.__par

    @par.setter
    def par(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSmachine_Root__par", None)
        self.__par = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractConection"):
                    opp_val = getattr(item, "AbstractConection", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractConection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractConection"):
                    opp_val = getattr(item, "AbstractConection", None)
                    
                    setattr(item, "AbstractConection", self)
                    

class FSmachine_AbstractConection:

    def __init__(self, name: str, AbstractConection: "FSmachine_Root" = None, AbstractConection6: "FSmachine_AbstractObject" = None, AbstractConection4: "FSmachine_AbstractObject" = None, connections: "FSmachine_Root" = None, conChild: "FSmachine_AbstractObject" = None, conParent: "FSmachine_AbstractObject" = None):
        self.name = name
        self.AbstractConection = AbstractConection
        self.AbstractConection6 = AbstractConection6
        self.AbstractConection4 = AbstractConection4
        self.connections = connections
        self.conChild = conChild
        self.conParent = conParent
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def conParent(self):
        return self.__conParent

    @conParent.setter
    def conParent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSmachine_AbstractConection__conParent", None)
        self.__conParent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractObject12"):
                opp_val = getattr(old_value, "AbstractObject12", None)
                if opp_val == self:
                    setattr(old_value, "AbstractObject12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractObject12"):
                opp_val = getattr(value, "AbstractObject12", None)
                setattr(value, "AbstractObject12", self)

    @property
    def conChild(self):
        return self.__conChild

    @conChild.setter
    def conChild(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSmachine_AbstractConection__conChild", None)
        self.__conChild = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractObject10"):
                opp_val = getattr(old_value, "AbstractObject10", None)
                if opp_val == self:
                    setattr(old_value, "AbstractObject10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractObject10"):
                opp_val = getattr(value, "AbstractObject10", None)
                setattr(value, "AbstractObject10", self)

    @property
    def AbstractConection6(self):
        return self.__AbstractConection6

    @AbstractConection6.setter
    def AbstractConection6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSmachine_AbstractConection__AbstractConection6", None)
        self.__AbstractConection6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "prev"):
                opp_val = getattr(old_value, "prev", None)
                if opp_val == self:
                    setattr(old_value, "prev", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "prev"):
                opp_val = getattr(value, "prev", None)
                setattr(value, "prev", self)

    @property
    def AbstractConection4(self):
        return self.__AbstractConection4

    @AbstractConection4.setter
    def AbstractConection4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSmachine_AbstractConection__AbstractConection4", None)
        self.__AbstractConection4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "next"):
                opp_val = getattr(old_value, "next", None)
                if opp_val == self:
                    setattr(old_value, "next", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "next"):
                opp_val = getattr(value, "next", None)
                setattr(value, "next", self)

    @property
    def AbstractConection(self):
        return self.__AbstractConection

    @AbstractConection.setter
    def AbstractConection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSmachine_AbstractConection__AbstractConection", None)
        self.__AbstractConection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "par"):
                opp_val = getattr(old_value, "par", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "par"):
                opp_val = getattr(value, "par", None)
                if opp_val is None:
                    setattr(value, "par", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def connections(self):
        return self.__connections

    @connections.setter
    def connections(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSmachine_AbstractConection__connections", None)
        self.__connections = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Root8"):
                opp_val = getattr(old_value, "Root8", None)
                if opp_val == self:
                    setattr(old_value, "Root8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Root8"):
                opp_val = getattr(value, "Root8", None)
                setattr(value, "Root8", self)
