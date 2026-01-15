from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class di_View(ABC):

    def __init__(self, context: str, definition: str, id: str, sourceConnector: str, targetConnector: str, di_View: "di_DocumentRoot" = None, di_View23: set["di_Style"] = None, di_View26: set["di_Node"] = None):
        self.context = context
        self.definition = definition
        self.id = id
        self.sourceConnector = sourceConnector
        self.targetConnector = targetConnector
        self.di_View = di_View
        self.di_View23 = di_View23 if di_View23 is not None else set()
        self.di_View26 = di_View26 if di_View26 is not None else set()
        
    @property
    def targetConnector(self) -> str:
        return self.__targetConnector

    @targetConnector.setter
    def targetConnector(self, targetConnector: str):
        self.__targetConnector = targetConnector

    @property
    def definition(self) -> str:
        return self.__definition

    @definition.setter
    def definition(self, definition: str):
        self.__definition = definition

    @property
    def context(self) -> str:
        return self.__context

    @context.setter
    def context(self, context: str):
        self.__context = context

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def sourceConnector(self) -> str:
        return self.__sourceConnector

    @sourceConnector.setter
    def sourceConnector(self, sourceConnector: str):
        self.__sourceConnector = sourceConnector

    @property
    def di_View(self):
        return self.__di_View

    @di_View.setter
    def di_View(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_View__di_View", None)
        self.__di_View = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_DocumentRoot14"):
                opp_val = getattr(old_value, "di_DocumentRoot14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_DocumentRoot14"):
                opp_val = getattr(value, "di_DocumentRoot14", None)
                if opp_val is None:
                    setattr(value, "di_DocumentRoot14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def di_View26(self):
        return self.__di_View26

    @di_View26.setter
    def di_View26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_View__di_View26", None)
        self.__di_View26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_Node27"):
                    opp_val = getattr(item, "di_Node27", None)
                    
                    if opp_val == self:
                        setattr(item, "di_Node27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_Node27"):
                    opp_val = getattr(item, "di_Node27", None)
                    
                    setattr(item, "di_Node27", self)
                    

    @property
    def di_View23(self):
        return self.__di_View23

    @di_View23.setter
    def di_View23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_View__di_View23", None)
        self.__di_View23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_Style24"):
                    opp_val = getattr(item, "di_Style24", None)
                    
                    if opp_val == self:
                        setattr(item, "di_Style24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_Style24"):
                    opp_val = getattr(item, "di_Style24", None)
                    
                    setattr(item, "di_Style24", self)
                    

class di_EStringToStringMapEntry:

    pass
class di_DocumentRoot:

    def __init__(self, mixed: str, di_DocumentRoot16: set["di_Diagram"] = None, di_DocumentRoot19: set["di_Node"] = None, di_DocumentRoot21: set["di_Style"] = None, di_DocumentRoot: set["di_EStringToStringMapEntry"] = None, di_DocumentRoot5: set["di_EStringToStringMapEntry"] = None, di_DocumentRoot8: set["di_Bendpoint"] = None, di_DocumentRoot11: set["di_Connector"] = None, di_DocumentRoot14: set["di_View"] = None):
        self.mixed = mixed
        self.di_DocumentRoot16 = di_DocumentRoot16 if di_DocumentRoot16 is not None else set()
        self.di_DocumentRoot19 = di_DocumentRoot19 if di_DocumentRoot19 is not None else set()
        self.di_DocumentRoot21 = di_DocumentRoot21 if di_DocumentRoot21 is not None else set()
        self.di_DocumentRoot = di_DocumentRoot if di_DocumentRoot is not None else set()
        self.di_DocumentRoot5 = di_DocumentRoot5 if di_DocumentRoot5 is not None else set()
        self.di_DocumentRoot8 = di_DocumentRoot8 if di_DocumentRoot8 is not None else set()
        self.di_DocumentRoot11 = di_DocumentRoot11 if di_DocumentRoot11 is not None else set()
        self.di_DocumentRoot14 = di_DocumentRoot14 if di_DocumentRoot14 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def di_DocumentRoot5(self):
        return self.__di_DocumentRoot5

    @di_DocumentRoot5.setter
    def di_DocumentRoot5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DocumentRoot__di_DocumentRoot5", None)
        self.__di_DocumentRoot5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_EStringToStringMapEntry6"):
                    opp_val = getattr(item, "di_EStringToStringMapEntry6", None)
                    
                    if opp_val == self:
                        setattr(item, "di_EStringToStringMapEntry6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_EStringToStringMapEntry6"):
                    opp_val = getattr(item, "di_EStringToStringMapEntry6", None)
                    
                    setattr(item, "di_EStringToStringMapEntry6", self)
                    

    @property
    def di_DocumentRoot14(self):
        return self.__di_DocumentRoot14

    @di_DocumentRoot14.setter
    def di_DocumentRoot14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DocumentRoot__di_DocumentRoot14", None)
        self.__di_DocumentRoot14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_View"):
                    opp_val = getattr(item, "di_View", None)
                    
                    if opp_val == self:
                        setattr(item, "di_View", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_View"):
                    opp_val = getattr(item, "di_View", None)
                    
                    setattr(item, "di_View", self)
                    

    @property
    def di_DocumentRoot19(self):
        return self.__di_DocumentRoot19

    @di_DocumentRoot19.setter
    def di_DocumentRoot19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DocumentRoot__di_DocumentRoot19", None)
        self.__di_DocumentRoot19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_Node"):
                    opp_val = getattr(item, "di_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "di_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_Node"):
                    opp_val = getattr(item, "di_Node", None)
                    
                    setattr(item, "di_Node", self)
                    

    @property
    def di_DocumentRoot16(self):
        return self.__di_DocumentRoot16

    @di_DocumentRoot16.setter
    def di_DocumentRoot16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DocumentRoot__di_DocumentRoot16", None)
        self.__di_DocumentRoot16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_Diagram17"):
                    opp_val = getattr(item, "di_Diagram17", None)
                    
                    if opp_val == self:
                        setattr(item, "di_Diagram17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_Diagram17"):
                    opp_val = getattr(item, "di_Diagram17", None)
                    
                    setattr(item, "di_Diagram17", self)
                    

    @property
    def di_DocumentRoot8(self):
        return self.__di_DocumentRoot8

    @di_DocumentRoot8.setter
    def di_DocumentRoot8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DocumentRoot__di_DocumentRoot8", None)
        self.__di_DocumentRoot8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_Bendpoint9"):
                    opp_val = getattr(item, "di_Bendpoint9", None)
                    
                    if opp_val == self:
                        setattr(item, "di_Bendpoint9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_Bendpoint9"):
                    opp_val = getattr(item, "di_Bendpoint9", None)
                    
                    setattr(item, "di_Bendpoint9", self)
                    

    @property
    def di_DocumentRoot11(self):
        return self.__di_DocumentRoot11

    @di_DocumentRoot11.setter
    def di_DocumentRoot11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DocumentRoot__di_DocumentRoot11", None)
        self.__di_DocumentRoot11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_Connector12"):
                    opp_val = getattr(item, "di_Connector12", None)
                    
                    if opp_val == self:
                        setattr(item, "di_Connector12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_Connector12"):
                    opp_val = getattr(item, "di_Connector12", None)
                    
                    setattr(item, "di_Connector12", self)
                    

    @property
    def di_DocumentRoot21(self):
        return self.__di_DocumentRoot21

    @di_DocumentRoot21.setter
    def di_DocumentRoot21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DocumentRoot__di_DocumentRoot21", None)
        self.__di_DocumentRoot21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_Style"):
                    opp_val = getattr(item, "di_Style", None)
                    
                    if opp_val == self:
                        setattr(item, "di_Style", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_Style"):
                    opp_val = getattr(item, "di_Style", None)
                    
                    setattr(item, "di_Style", self)
                    

    @property
    def di_DocumentRoot(self):
        return self.__di_DocumentRoot

    @di_DocumentRoot.setter
    def di_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DocumentRoot__di_DocumentRoot", None)
        self.__di_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_EStringToStringMapEntry"):
                    opp_val = getattr(item, "di_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "di_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_EStringToStringMapEntry"):
                    opp_val = getattr(item, "di_EStringToStringMapEntry", None)
                    
                    setattr(item, "di_EStringToStringMapEntry", self)
                    

class di_Style:

    def __init__(self, name: str, value: str, di_Style: "di_DocumentRoot" = None, di_Style24: "di_View" = None):
        self.name = name
        self.value = value
        self.di_Style = di_Style
        self.di_Style24 = di_Style24
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def di_Style24(self):
        return self.__di_Style24

    @di_Style24.setter
    def di_Style24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Style__di_Style24", None)
        self.__di_Style24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_View23"):
                opp_val = getattr(old_value, "di_View23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_View23"):
                opp_val = getattr(value, "di_View23", None)
                if opp_val is None:
                    setattr(value, "di_View23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def di_Style(self):
        return self.__di_Style

    @di_Style.setter
    def di_Style(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Style__di_Style", None)
        self.__di_Style = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_DocumentRoot21"):
                opp_val = getattr(old_value, "di_DocumentRoot21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_DocumentRoot21"):
                opp_val = getattr(value, "di_DocumentRoot21", None)
                if opp_val is None:
                    setattr(value, "di_DocumentRoot21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class View:

    pass
class di_Node(View):

    pass
class di_Connector(View):

    def __init__(self, source: str, target: str, di_Connector2: "di_Diagram" = None, di_Connector: set["di_Bendpoint"] = None, di_Connector12: "di_DocumentRoot" = None):
        self.source = source
        self.target = target
        self.di_Connector2 = di_Connector2
        self.di_Connector = di_Connector if di_Connector is not None else set()
        self.di_Connector12 = di_Connector12
        
    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target

    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def di_Connector2(self):
        return self.__di_Connector2

    @di_Connector2.setter
    def di_Connector2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Connector__di_Connector2", None)
        self.__di_Connector2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_Diagram"):
                opp_val = getattr(old_value, "di_Diagram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_Diagram"):
                opp_val = getattr(value, "di_Diagram", None)
                if opp_val is None:
                    setattr(value, "di_Diagram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def di_Connector12(self):
        return self.__di_Connector12

    @di_Connector12.setter
    def di_Connector12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Connector__di_Connector12", None)
        self.__di_Connector12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_DocumentRoot11"):
                opp_val = getattr(old_value, "di_DocumentRoot11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_DocumentRoot11"):
                opp_val = getattr(value, "di_DocumentRoot11", None)
                if opp_val is None:
                    setattr(value, "di_DocumentRoot11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def di_Connector(self):
        return self.__di_Connector

    @di_Connector.setter
    def di_Connector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Connector__di_Connector", None)
        self.__di_Connector = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_Bendpoint"):
                    opp_val = getattr(item, "di_Bendpoint", None)
                    
                    if opp_val == self:
                        setattr(item, "di_Bendpoint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_Bendpoint"):
                    opp_val = getattr(item, "di_Bendpoint", None)
                    
                    setattr(item, "di_Bendpoint", self)
                    

class di_Bendpoint:

    def __init__(self, sourceX: str, sourceY: str, targetX: str, targetY: str, di_Bendpoint: "di_Connector" = None, di_Bendpoint9: "di_DocumentRoot" = None):
        self.sourceX = sourceX
        self.sourceY = sourceY
        self.targetX = targetX
        self.targetY = targetY
        self.di_Bendpoint = di_Bendpoint
        self.di_Bendpoint9 = di_Bendpoint9
        
    @property
    def sourceX(self) -> str:
        return self.__sourceX

    @sourceX.setter
    def sourceX(self, sourceX: str):
        self.__sourceX = sourceX

    @property
    def sourceY(self) -> str:
        return self.__sourceY

    @sourceY.setter
    def sourceY(self, sourceY: str):
        self.__sourceY = sourceY

    @property
    def targetY(self) -> str:
        return self.__targetY

    @targetY.setter
    def targetY(self, targetY: str):
        self.__targetY = targetY

    @property
    def targetX(self) -> str:
        return self.__targetX

    @targetX.setter
    def targetX(self, targetX: str):
        self.__targetX = targetX

    @property
    def di_Bendpoint(self):
        return self.__di_Bendpoint

    @di_Bendpoint.setter
    def di_Bendpoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Bendpoint__di_Bendpoint", None)
        self.__di_Bendpoint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_Connector"):
                opp_val = getattr(old_value, "di_Connector", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_Connector"):
                opp_val = getattr(value, "di_Connector", None)
                if opp_val is None:
                    setattr(value, "di_Connector", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def di_Bendpoint9(self):
        return self.__di_Bendpoint9

    @di_Bendpoint9.setter
    def di_Bendpoint9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Bendpoint__di_Bendpoint9", None)
        self.__di_Bendpoint9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_DocumentRoot8"):
                opp_val = getattr(old_value, "di_DocumentRoot8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_DocumentRoot8"):
                opp_val = getattr(value, "di_DocumentRoot8", None)
                if opp_val is None:
                    setattr(value, "di_DocumentRoot8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class di_Diagram(View):

    pass