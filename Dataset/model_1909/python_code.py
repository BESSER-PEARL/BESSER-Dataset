from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class myDsl_PostgreSQL:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class myDsl_Spring:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class myDsl_ReactInformation:

    def __init__(self, name: str, myDsl_ReactInformation: "myDsl_ReactInfo" = None):
        self.name = name
        self.myDsl_ReactInformation = myDsl_ReactInformation
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_ReactInformation(self):
        return self.__myDsl_ReactInformation

    @myDsl_ReactInformation.setter
    def myDsl_ReactInformation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ReactInformation__myDsl_ReactInformation", None)
        self.__myDsl_ReactInformation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ReactInfo"):
                opp_val = getattr(old_value, "myDsl_ReactInfo", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ReactInfo"):
                opp_val = getattr(value, "myDsl_ReactInfo", None)
                if opp_val is None:
                    setattr(value, "myDsl_ReactInfo", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_ReactInfo:

    pass
class myDsl_ReactLibrary:

    def __init__(self, name: str, myDsl_ReactLibrary: "myDsl_ReactLibraries" = None):
        self.name = name
        self.myDsl_ReactLibrary = myDsl_ReactLibrary
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_ReactLibrary(self):
        return self.__myDsl_ReactLibrary

    @myDsl_ReactLibrary.setter
    def myDsl_ReactLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ReactLibrary__myDsl_ReactLibrary", None)
        self.__myDsl_ReactLibrary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ReactLibraries"):
                opp_val = getattr(old_value, "myDsl_ReactLibraries", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ReactLibraries"):
                opp_val = getattr(value, "myDsl_ReactLibraries", None)
                if opp_val is None:
                    setattr(value, "myDsl_ReactLibraries", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_ReactLibraries:

    pass
class myDsl_ReactServicesType:

    def __init__(self, name: str, myDsl_ReactServicesType: "myDsl_ReactServicesRelation" = None):
        self.name = name
        self.myDsl_ReactServicesType = myDsl_ReactServicesType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_ReactServicesType(self):
        return self.__myDsl_ReactServicesType

    @myDsl_ReactServicesType.setter
    def myDsl_ReactServicesType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ReactServicesType__myDsl_ReactServicesType", None)
        self.__myDsl_ReactServicesType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ReactServicesRelation116"):
                opp_val = getattr(old_value, "myDsl_ReactServicesRelation116", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ReactServicesRelation116"):
                opp_val = getattr(value, "myDsl_ReactServicesRelation116", None)
                if opp_val is None:
                    setattr(value, "myDsl_ReactServicesRelation116", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_AmazonWebServices:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class myDsl_ReactActionsContent:

    pass
class myDsl_ReactActions:

    pass
class myDsl_ReactCoreFunctions:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class myDsl_Props:

    def __init__(self, name: str, componentclass: str):
        self.name = name
        self.componentclass = componentclass
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def componentclass(self) -> str:
        return self.__componentclass

    @componentclass.setter
    def componentclass(self, componentclass: str):
        self.__componentclass = componentclass

class myDsl_CoreFunctionsDeclaration:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class myDsl_State:

    def __init__(self, name: str, componentclass: str):
        self.name = name
        self.componentclass = componentclass
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def componentclass(self) -> str:
        return self.__componentclass

    @componentclass.setter
    def componentclass(self, componentclass: str):
        self.__componentclass = componentclass

class myDsl_ReactConstructor:

    pass
class myDsl_ReactServicesRelation:

    def __init__(self, name: str, myDsl_ReactServicesRelation: "myDsl_ReactActionsContent" = None, myDsl_ReactServicesRelation116: set["myDsl_ReactServicesType"] = None):
        self.name = name
        self.myDsl_ReactServicesRelation = myDsl_ReactServicesRelation
        self.myDsl_ReactServicesRelation116 = myDsl_ReactServicesRelation116 if myDsl_ReactServicesRelation116 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_ReactServicesRelation116(self):
        return self.__myDsl_ReactServicesRelation116

    @myDsl_ReactServicesRelation116.setter
    def myDsl_ReactServicesRelation116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ReactServicesRelation__myDsl_ReactServicesRelation116", None)
        self.__myDsl_ReactServicesRelation116 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_ReactServicesType"):
                    opp_val = getattr(item, "myDsl_ReactServicesType", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_ReactServicesType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_ReactServicesType"):
                    opp_val = getattr(item, "myDsl_ReactServicesType", None)
                    
                    setattr(item, "myDsl_ReactServicesType", self)
                    

    @property
    def myDsl_ReactServicesRelation(self):
        return self.__myDsl_ReactServicesRelation

    @myDsl_ReactServicesRelation.setter
    def myDsl_ReactServicesRelation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ReactServicesRelation__myDsl_ReactServicesRelation", None)
        self.__myDsl_ReactServicesRelation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ReactActionsContent114"):
                opp_val = getattr(old_value, "myDsl_ReactActionsContent114", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ReactActionsContent114"):
                opp_val = getattr(value, "myDsl_ReactActionsContent114", None)
                if opp_val is None:
                    setattr(value, "myDsl_ReactActionsContent114", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_UIContent:

    def __init__(self, name: str, myDsl_UIContent: "myDsl_ComponentsUI" = None, myDsl_UIContent103: set["myDsl_ComponentClass"] = None):
        self.name = name
        self.myDsl_UIContent = myDsl_UIContent
        self.myDsl_UIContent103 = myDsl_UIContent103 if myDsl_UIContent103 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_UIContent(self):
        return self.__myDsl_UIContent

    @myDsl_UIContent.setter
    def myDsl_UIContent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_UIContent__myDsl_UIContent", None)
        self.__myDsl_UIContent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ComponentsUI101"):
                opp_val = getattr(old_value, "myDsl_ComponentsUI101", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ComponentsUI101"):
                opp_val = getattr(value, "myDsl_ComponentsUI101", None)
                if opp_val is None:
                    setattr(value, "myDsl_ComponentsUI101", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_UIContent103(self):
        return self.__myDsl_UIContent103

    @myDsl_UIContent103.setter
    def myDsl_UIContent103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_UIContent__myDsl_UIContent103", None)
        self.__myDsl_UIContent103 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_ComponentClass104"):
                    opp_val = getattr(item, "myDsl_ComponentClass104", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_ComponentClass104", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_ComponentClass104"):
                    opp_val = getattr(item, "myDsl_ComponentClass104", None)
                    
                    setattr(item, "myDsl_ComponentClass104", self)
                    

class myDsl_ComponentClass:

    pass
class myDsl_LogicStructure:

    def __init__(self, name: str, myDsl_LogicStructure: "myDsl_LogicContent" = None, myDsl_LogicStructure99: set["myDsl_ComponentClass"] = None):
        self.name = name
        self.myDsl_LogicStructure = myDsl_LogicStructure
        self.myDsl_LogicStructure99 = myDsl_LogicStructure99 if myDsl_LogicStructure99 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_LogicStructure99(self):
        return self.__myDsl_LogicStructure99

    @myDsl_LogicStructure99.setter
    def myDsl_LogicStructure99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_LogicStructure__myDsl_LogicStructure99", None)
        self.__myDsl_LogicStructure99 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_ComponentClass"):
                    opp_val = getattr(item, "myDsl_ComponentClass", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_ComponentClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_ComponentClass"):
                    opp_val = getattr(item, "myDsl_ComponentClass", None)
                    
                    setattr(item, "myDsl_ComponentClass", self)
                    

    @property
    def myDsl_LogicStructure(self):
        return self.__myDsl_LogicStructure

    @myDsl_LogicStructure.setter
    def myDsl_LogicStructure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_LogicStructure__myDsl_LogicStructure", None)
        self.__myDsl_LogicStructure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_LogicContent97"):
                opp_val = getattr(old_value, "myDsl_LogicContent97", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_LogicContent97"):
                opp_val = getattr(value, "myDsl_LogicContent97", None)
                if opp_val is None:
                    setattr(value, "myDsl_LogicContent97", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_ReactFunctions:

    def __init__(self, lifecycleclass: str, renderclass: str, myDsl_ReactFunctions: set["myDsl_EObject"] = None):
        self.lifecycleclass = lifecycleclass
        self.renderclass = renderclass
        self.myDsl_ReactFunctions = myDsl_ReactFunctions if myDsl_ReactFunctions is not None else set()
        
    @property
    def renderclass(self) -> str:
        return self.__renderclass

    @renderclass.setter
    def renderclass(self, renderclass: str):
        self.__renderclass = renderclass

    @property
    def lifecycleclass(self) -> str:
        return self.__lifecycleclass

    @lifecycleclass.setter
    def lifecycleclass(self, lifecycleclass: str):
        self.__lifecycleclass = lifecycleclass

    @property
    def myDsl_ReactFunctions(self):
        return self.__myDsl_ReactFunctions

    @myDsl_ReactFunctions.setter
    def myDsl_ReactFunctions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ReactFunctions__myDsl_ReactFunctions", None)
        self.__myDsl_ReactFunctions = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_EObject109"):
                    opp_val = getattr(item, "myDsl_EObject109", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_EObject109", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_EObject109"):
                    opp_val = getattr(item, "myDsl_EObject109", None)
                    
                    setattr(item, "myDsl_EObject109", self)
                    

class myDsl_ComponentsUI:

    def __init__(self, name: str, myDsl_ComponentsUI: "myDsl_ReactComponents" = None, myDsl_ComponentsUI101: set["myDsl_UIContent"] = None):
        self.name = name
        self.myDsl_ComponentsUI = myDsl_ComponentsUI
        self.myDsl_ComponentsUI101 = myDsl_ComponentsUI101 if myDsl_ComponentsUI101 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_ComponentsUI(self):
        return self.__myDsl_ComponentsUI

    @myDsl_ComponentsUI.setter
    def myDsl_ComponentsUI(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ComponentsUI__myDsl_ComponentsUI", None)
        self.__myDsl_ComponentsUI = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ReactComponents93"):
                opp_val = getattr(old_value, "myDsl_ReactComponents93", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ReactComponents93"):
                opp_val = getattr(value, "myDsl_ReactComponents93", None)
                if opp_val is None:
                    setattr(value, "myDsl_ReactComponents93", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_ComponentsUI101(self):
        return self.__myDsl_ComponentsUI101

    @myDsl_ComponentsUI101.setter
    def myDsl_ComponentsUI101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ComponentsUI__myDsl_ComponentsUI101", None)
        self.__myDsl_ComponentsUI101 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_UIContent"):
                    opp_val = getattr(item, "myDsl_UIContent", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_UIContent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_UIContent"):
                    opp_val = getattr(item, "myDsl_UIContent", None)
                    
                    setattr(item, "myDsl_UIContent", self)
                    

class myDsl_ComponentsLogic:

    def __init__(self, name: str, myDsl_ComponentsLogic95: set["myDsl_LogicContent"] = None, myDsl_ComponentsLogic: "myDsl_ReactComponents" = None):
        self.name = name
        self.myDsl_ComponentsLogic95 = myDsl_ComponentsLogic95 if myDsl_ComponentsLogic95 is not None else set()
        self.myDsl_ComponentsLogic = myDsl_ComponentsLogic
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_ComponentsLogic95(self):
        return self.__myDsl_ComponentsLogic95

    @myDsl_ComponentsLogic95.setter
    def myDsl_ComponentsLogic95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ComponentsLogic__myDsl_ComponentsLogic95", None)
        self.__myDsl_ComponentsLogic95 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_LogicContent"):
                    opp_val = getattr(item, "myDsl_LogicContent", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_LogicContent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_LogicContent"):
                    opp_val = getattr(item, "myDsl_LogicContent", None)
                    
                    setattr(item, "myDsl_LogicContent", self)
                    

    @property
    def myDsl_ComponentsLogic(self):
        return self.__myDsl_ComponentsLogic

    @myDsl_ComponentsLogic.setter
    def myDsl_ComponentsLogic(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ComponentsLogic__myDsl_ComponentsLogic", None)
        self.__myDsl_ComponentsLogic = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ReactComponents"):
                opp_val = getattr(old_value, "myDsl_ReactComponents", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ReactComponents"):
                opp_val = getattr(value, "myDsl_ReactComponents", None)
                if opp_val is None:
                    setattr(value, "myDsl_ReactComponents", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_ReactComponents:

    pass
class myDsl_DOMConfigurations:

    def __init__(self, elements: str, name: str, myDsl_DOMConfigurations: "myDsl_ReactConfigurations" = None):
        self.elements = elements
        self.name = name
        self.myDsl_DOMConfigurations = myDsl_DOMConfigurations
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def elements(self) -> str:
        return self.__elements

    @elements.setter
    def elements(self, elements: str):
        self.__elements = elements

    @property
    def myDsl_DOMConfigurations(self):
        return self.__myDsl_DOMConfigurations

    @myDsl_DOMConfigurations.setter
    def myDsl_DOMConfigurations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_DOMConfigurations__myDsl_DOMConfigurations", None)
        self.__myDsl_DOMConfigurations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ReactConfigurations90"):
                opp_val = getattr(old_value, "myDsl_ReactConfigurations90", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ReactConfigurations90"):
                opp_val = getattr(value, "myDsl_ReactConfigurations90", None)
                if opp_val is None:
                    setattr(value, "myDsl_ReactConfigurations90", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_PackageVersion:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class myDsl_PackageName:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class myDsl_LogicContent:

    def __init__(self, name: str, myDsl_LogicContent: "myDsl_ComponentsLogic" = None, myDsl_LogicContent97: set["myDsl_LogicStructure"] = None):
        self.name = name
        self.myDsl_LogicContent = myDsl_LogicContent
        self.myDsl_LogicContent97 = myDsl_LogicContent97 if myDsl_LogicContent97 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_LogicContent97(self):
        return self.__myDsl_LogicContent97

    @myDsl_LogicContent97.setter
    def myDsl_LogicContent97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_LogicContent__myDsl_LogicContent97", None)
        self.__myDsl_LogicContent97 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_LogicStructure"):
                    opp_val = getattr(item, "myDsl_LogicStructure", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_LogicStructure", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_LogicStructure"):
                    opp_val = getattr(item, "myDsl_LogicStructure", None)
                    
                    setattr(item, "myDsl_LogicStructure", self)
                    

    @property
    def myDsl_LogicContent(self):
        return self.__myDsl_LogicContent

    @myDsl_LogicContent.setter
    def myDsl_LogicContent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_LogicContent__myDsl_LogicContent", None)
        self.__myDsl_LogicContent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ComponentsLogic95"):
                opp_val = getattr(old_value, "myDsl_ComponentsLogic95", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ComponentsLogic95"):
                opp_val = getattr(value, "myDsl_ComponentsLogic95", None)
                if opp_val is None:
                    setattr(value, "myDsl_ComponentsLogic95", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_ReactDependenciesSubRules:

    pass
class myDsl_ReactDependenciesRules:

    def __init__(self, name: str, myDsl_ReactDependenciesRules: "myDsl_ReactDependencies" = None, myDsl_ReactDependenciesRules83: set["myDsl_ReactDependenciesSubRules"] = None):
        self.name = name
        self.myDsl_ReactDependenciesRules = myDsl_ReactDependenciesRules
        self.myDsl_ReactDependenciesRules83 = myDsl_ReactDependenciesRules83 if myDsl_ReactDependenciesRules83 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_ReactDependenciesRules83(self):
        return self.__myDsl_ReactDependenciesRules83

    @myDsl_ReactDependenciesRules83.setter
    def myDsl_ReactDependenciesRules83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ReactDependenciesRules__myDsl_ReactDependenciesRules83", None)
        self.__myDsl_ReactDependenciesRules83 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_ReactDependenciesSubRules"):
                    opp_val = getattr(item, "myDsl_ReactDependenciesSubRules", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_ReactDependenciesSubRules", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_ReactDependenciesSubRules"):
                    opp_val = getattr(item, "myDsl_ReactDependenciesSubRules", None)
                    
                    setattr(item, "myDsl_ReactDependenciesSubRules", self)
                    

    @property
    def myDsl_ReactDependenciesRules(self):
        return self.__myDsl_ReactDependenciesRules

    @myDsl_ReactDependenciesRules.setter
    def myDsl_ReactDependenciesRules(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ReactDependenciesRules__myDsl_ReactDependenciesRules", None)
        self.__myDsl_ReactDependenciesRules = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ReactDependencies81"):
                opp_val = getattr(old_value, "myDsl_ReactDependencies81", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ReactDependencies81"):
                opp_val = getattr(value, "myDsl_ReactDependencies81", None)
                if opp_val is None:
                    setattr(value, "myDsl_ReactDependencies81", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_ReactConfigurations:

    def __init__(self, name: str, myDsl_ReactConfigurations: "myDsl_ReactConfiguration" = None, myDsl_ReactConfigurations90: set["myDsl_DOMConfigurations"] = None):
        self.name = name
        self.myDsl_ReactConfigurations = myDsl_ReactConfigurations
        self.myDsl_ReactConfigurations90 = myDsl_ReactConfigurations90 if myDsl_ReactConfigurations90 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_ReactConfigurations(self):
        return self.__myDsl_ReactConfigurations

    @myDsl_ReactConfigurations.setter
    def myDsl_ReactConfigurations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ReactConfigurations__myDsl_ReactConfigurations", None)
        self.__myDsl_ReactConfigurations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ReactConfiguration79"):
                opp_val = getattr(old_value, "myDsl_ReactConfiguration79", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ReactConfiguration79"):
                opp_val = getattr(value, "myDsl_ReactConfiguration79", None)
                if opp_val is None:
                    setattr(value, "myDsl_ReactConfiguration79", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_ReactConfigurations90(self):
        return self.__myDsl_ReactConfigurations90

    @myDsl_ReactConfigurations90.setter
    def myDsl_ReactConfigurations90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ReactConfigurations__myDsl_ReactConfigurations90", None)
        self.__myDsl_ReactConfigurations90 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_DOMConfigurations"):
                    opp_val = getattr(item, "myDsl_DOMConfigurations", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_DOMConfigurations", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_DOMConfigurations"):
                    opp_val = getattr(item, "myDsl_DOMConfigurations", None)
                    
                    setattr(item, "myDsl_DOMConfigurations", self)
                    

class myDsl_ReactDependencies:

    pass
class myDsl_ReactConfiguration:

    pass
class myDsl_SingleDependencies:

    pass
class myDsl_ReactModules:

    pass
class myDsl_React:

    def __init__(self, name: str, myDsl_React: set["myDsl_ReactModules"] = None):
        self.name = name
        self.myDsl_React = myDsl_React if myDsl_React is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_React(self):
        return self.__myDsl_React

    @myDsl_React.setter
    def myDsl_React(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_React__myDsl_React", None)
        self.__myDsl_React = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_ReactModules"):
                    opp_val = getattr(item, "myDsl_ReactModules", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_ReactModules", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_ReactModules"):
                    opp_val = getattr(item, "myDsl_ReactModules", None)
                    
                    setattr(item, "myDsl_ReactModules", self)
                    

class myDsl_Technologies:

    pass
class myDsl_Technology:

    def __init__(self, name: str, myDsl_Technology: set["myDsl_Technologies"] = None):
        self.name = name
        self.myDsl_Technology = myDsl_Technology if myDsl_Technology is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Technology(self):
        return self.__myDsl_Technology

    @myDsl_Technology.setter
    def myDsl_Technology(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Technology__myDsl_Technology", None)
        self.__myDsl_Technology = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Technologies"):
                    opp_val = getattr(item, "myDsl_Technologies", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Technologies", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Technologies"):
                    opp_val = getattr(item, "myDsl_Technologies", None)
                    
                    setattr(item, "myDsl_Technologies", self)
                    

class myDsl_NTiersRelations:

    def __init__(self, name: str, myDsl_NTiersRelations: "myDsl_NTierSource" = None, myDsl_NTiersRelations66: "myDsl_NTierTarget" = None):
        self.name = name
        self.myDsl_NTiersRelations = myDsl_NTiersRelations
        self.myDsl_NTiersRelations66 = myDsl_NTiersRelations66
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_NTiersRelations(self):
        return self.__myDsl_NTiersRelations

    @myDsl_NTiersRelations.setter
    def myDsl_NTiersRelations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_NTiersRelations__myDsl_NTiersRelations", None)
        self.__myDsl_NTiersRelations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_NTierSource63"):
                opp_val = getattr(old_value, "myDsl_NTierSource63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_NTierSource63"):
                opp_val = getattr(value, "myDsl_NTierSource63", None)
                if opp_val is None:
                    setattr(value, "myDsl_NTierSource63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_NTiersRelations66(self):
        return self.__myDsl_NTiersRelations66

    @myDsl_NTiersRelations66.setter
    def myDsl_NTiersRelations66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_NTiersRelations__myDsl_NTiersRelations66", None)
        self.__myDsl_NTiersRelations66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_NTierTarget65"):
                opp_val = getattr(old_value, "myDsl_NTierTarget65", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_NTierTarget65"):
                opp_val = getattr(value, "myDsl_NTierTarget65", None)
                if opp_val is None:
                    setattr(value, "myDsl_NTierTarget65", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_ReactSubModules:

    pass
class myDsl_NTierTarget:

    pass
class myDsl_NTiersConnections:

    def __init__(self, ntierconnection: str, name: str, myDsl_NTiersConnections: set["myDsl_NTierSource"] = None, myDsl_NTiersConnections61: set["myDsl_NTierTarget"] = None):
        self.ntierconnection = ntierconnection
        self.name = name
        self.myDsl_NTiersConnections = myDsl_NTiersConnections if myDsl_NTiersConnections is not None else set()
        self.myDsl_NTiersConnections61 = myDsl_NTiersConnections61 if myDsl_NTiersConnections61 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ntierconnection(self) -> str:
        return self.__ntierconnection

    @ntierconnection.setter
    def ntierconnection(self, ntierconnection: str):
        self.__ntierconnection = ntierconnection

    @property
    def myDsl_NTiersConnections61(self):
        return self.__myDsl_NTiersConnections61

    @myDsl_NTiersConnections61.setter
    def myDsl_NTiersConnections61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_NTiersConnections__myDsl_NTiersConnections61", None)
        self.__myDsl_NTiersConnections61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_NTierTarget"):
                    opp_val = getattr(item, "myDsl_NTierTarget", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_NTierTarget", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_NTierTarget"):
                    opp_val = getattr(item, "myDsl_NTierTarget", None)
                    
                    setattr(item, "myDsl_NTierTarget", self)
                    

    @property
    def myDsl_NTiersConnections(self):
        return self.__myDsl_NTiersConnections

    @myDsl_NTiersConnections.setter
    def myDsl_NTiersConnections(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_NTiersConnections__myDsl_NTiersConnections", None)
        self.__myDsl_NTiersConnections = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_NTierSource"):
                    opp_val = getattr(item, "myDsl_NTierSource", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_NTierSource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_NTierSource"):
                    opp_val = getattr(item, "myDsl_NTierSource", None)
                    
                    setattr(item, "myDsl_NTierSource", self)
                    

class myDsl_PersistenceDataComponent:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class myDsl_BackEnd:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class myDsl_FrontEnd:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class myDsl_ArchitectureComponents:

    pass
class myDsl_LayerTarget:

    def __init__(self, layerelations: str, myDsl_LayerTarget: "myDsl_LayerRelations" = None):
        self.layerelations = layerelations
        self.myDsl_LayerTarget = myDsl_LayerTarget
        
    @property
    def layerelations(self) -> str:
        return self.__layerelations

    @layerelations.setter
    def layerelations(self, layerelations: str):
        self.__layerelations = layerelations

    @property
    def myDsl_LayerTarget(self):
        return self.__myDsl_LayerTarget

    @myDsl_LayerTarget.setter
    def myDsl_LayerTarget(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_LayerTarget__myDsl_LayerTarget", None)
        self.__myDsl_LayerTarget = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_LayerRelations56"):
                opp_val = getattr(old_value, "myDsl_LayerRelations56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_LayerRelations56"):
                opp_val = getattr(value, "myDsl_LayerRelations56", None)
                if opp_val is None:
                    setattr(value, "myDsl_LayerRelations56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_NTierSource:

    pass
class myDsl_LayerRelations:

    def __init__(self, name: str, layerelations: str, myDsl_LayerRelations: set["myDsl_LayerSource"] = None, myDsl_LayerRelations56: set["myDsl_LayerTarget"] = None):
        self.name = name
        self.layerelations = layerelations
        self.myDsl_LayerRelations = myDsl_LayerRelations if myDsl_LayerRelations is not None else set()
        self.myDsl_LayerRelations56 = myDsl_LayerRelations56 if myDsl_LayerRelations56 is not None else set()
        
    @property
    def layerelations(self) -> str:
        return self.__layerelations

    @layerelations.setter
    def layerelations(self, layerelations: str):
        self.__layerelations = layerelations

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_LayerRelations(self):
        return self.__myDsl_LayerRelations

    @myDsl_LayerRelations.setter
    def myDsl_LayerRelations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_LayerRelations__myDsl_LayerRelations", None)
        self.__myDsl_LayerRelations = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_LayerSource"):
                    opp_val = getattr(item, "myDsl_LayerSource", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_LayerSource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_LayerSource"):
                    opp_val = getattr(item, "myDsl_LayerSource", None)
                    
                    setattr(item, "myDsl_LayerSource", self)
                    

    @property
    def myDsl_LayerRelations56(self):
        return self.__myDsl_LayerRelations56

    @myDsl_LayerRelations56.setter
    def myDsl_LayerRelations56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_LayerRelations__myDsl_LayerRelations56", None)
        self.__myDsl_LayerRelations56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_LayerTarget"):
                    opp_val = getattr(item, "myDsl_LayerTarget", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_LayerTarget", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_LayerTarget"):
                    opp_val = getattr(item, "myDsl_LayerTarget", None)
                    
                    setattr(item, "myDsl_LayerTarget", self)
                    

class myDsl_SingleFile:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class myDsl_MultipleFile:

    def __init__(self, name: str, myDsl_MultipleFile: "myDsl_Directories" = None):
        self.name = name
        self.myDsl_MultipleFile = myDsl_MultipleFile
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_MultipleFile(self):
        return self.__myDsl_MultipleFile

    @myDsl_MultipleFile.setter
    def myDsl_MultipleFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_MultipleFile__myDsl_MultipleFile", None)
        self.__myDsl_MultipleFile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Directories"):
                opp_val = getattr(old_value, "myDsl_Directories", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Directories"):
                opp_val = getattr(value, "myDsl_Directories", None)
                if opp_val is None:
                    setattr(value, "myDsl_Directories", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_Directories:

    pass
class myDsl_DirectoryContent:

    def __init__(self, name: str, myDsl_DirectoryContent: "myDsl_SegmentStructureContent" = None, myDsl_DirectoryContent51: set["myDsl_EObject"] = None):
        self.name = name
        self.myDsl_DirectoryContent = myDsl_DirectoryContent
        self.myDsl_DirectoryContent51 = myDsl_DirectoryContent51 if myDsl_DirectoryContent51 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_DirectoryContent51(self):
        return self.__myDsl_DirectoryContent51

    @myDsl_DirectoryContent51.setter
    def myDsl_DirectoryContent51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_DirectoryContent__myDsl_DirectoryContent51", None)
        self.__myDsl_DirectoryContent51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_EObject52"):
                    opp_val = getattr(item, "myDsl_EObject52", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_EObject52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_EObject52"):
                    opp_val = getattr(item, "myDsl_EObject52", None)
                    
                    setattr(item, "myDsl_EObject52", self)
                    

    @property
    def myDsl_DirectoryContent(self):
        return self.__myDsl_DirectoryContent

    @myDsl_DirectoryContent.setter
    def myDsl_DirectoryContent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_DirectoryContent__myDsl_DirectoryContent", None)
        self.__myDsl_DirectoryContent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_SegmentStructureContent49"):
                opp_val = getattr(old_value, "myDsl_SegmentStructureContent49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_SegmentStructureContent49"):
                opp_val = getattr(value, "myDsl_SegmentStructureContent49", None)
                if opp_val is None:
                    setattr(value, "myDsl_SegmentStructureContent49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_LayerSource:

    def __init__(self, layerelations: str, myDsl_LayerSource: "myDsl_LayerRelations" = None):
        self.layerelations = layerelations
        self.myDsl_LayerSource = myDsl_LayerSource
        
    @property
    def layerelations(self) -> str:
        return self.__layerelations

    @layerelations.setter
    def layerelations(self, layerelations: str):
        self.__layerelations = layerelations

    @property
    def myDsl_LayerSource(self):
        return self.__myDsl_LayerSource

    @myDsl_LayerSource.setter
    def myDsl_LayerSource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_LayerSource__myDsl_LayerSource", None)
        self.__myDsl_LayerSource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_LayerRelations"):
                opp_val = getattr(old_value, "myDsl_LayerRelations", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_LayerRelations"):
                opp_val = getattr(value, "myDsl_LayerRelations", None)
                if opp_val is None:
                    setattr(value, "myDsl_LayerRelations", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_DataPersistenceSegments:

    def __init__(self, name: str, myDsl_DataPersistenceSegments: "myDsl_DataPersistenceContent" = None):
        self.name = name
        self.myDsl_DataPersistenceSegments = myDsl_DataPersistenceSegments
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_DataPersistenceSegments(self):
        return self.__myDsl_DataPersistenceSegments

    @myDsl_DataPersistenceSegments.setter
    def myDsl_DataPersistenceSegments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_DataPersistenceSegments__myDsl_DataPersistenceSegments", None)
        self.__myDsl_DataPersistenceSegments = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_DataPersistenceContent46"):
                opp_val = getattr(old_value, "myDsl_DataPersistenceContent46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_DataPersistenceContent46"):
                opp_val = getattr(value, "myDsl_DataPersistenceContent46", None)
                if opp_val is None:
                    setattr(value, "myDsl_DataPersistenceContent46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_DataPersistenceContent:

    pass
class myDsl_DataPersistenceLayer:

    pass
class myDsl_BusinessLogicSegments:

    def __init__(self, name: str, myDsl_BusinessLogicSegments: "myDsl_BusinessLogicContent" = None):
        self.name = name
        self.myDsl_BusinessLogicSegments = myDsl_BusinessLogicSegments
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_BusinessLogicSegments(self):
        return self.__myDsl_BusinessLogicSegments

    @myDsl_BusinessLogicSegments.setter
    def myDsl_BusinessLogicSegments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_BusinessLogicSegments__myDsl_BusinessLogicSegments", None)
        self.__myDsl_BusinessLogicSegments = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_BusinessLogicContent"):
                opp_val = getattr(old_value, "myDsl_BusinessLogicContent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_BusinessLogicContent"):
                opp_val = getattr(value, "myDsl_BusinessLogicContent", None)
                if opp_val is None:
                    setattr(value, "myDsl_BusinessLogicContent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_BusinessLogicContent:

    pass
class myDsl_BusinessLogicLayer:

    pass
class myDsl_PresentationSegments:

    def __init__(self, name: str, myDsl_PresentationSegments: "myDsl_PresentationContent" = None):
        self.name = name
        self.myDsl_PresentationSegments = myDsl_PresentationSegments
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_PresentationSegments(self):
        return self.__myDsl_PresentationSegments

    @myDsl_PresentationSegments.setter
    def myDsl_PresentationSegments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_PresentationSegments__myDsl_PresentationSegments", None)
        self.__myDsl_PresentationSegments = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_PresentationContent"):
                opp_val = getattr(old_value, "myDsl_PresentationContent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_PresentationContent"):
                opp_val = getattr(value, "myDsl_PresentationContent", None)
                if opp_val is None:
                    setattr(value, "myDsl_PresentationContent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_PresentationContent:

    pass
class myDsl_SegmentStructureContent:

    def __init__(self, name: str, myDsl_SegmentStructureContent: "myDsl_SegmentStructure" = None, myDsl_SegmentStructureContent49: set["myDsl_DirectoryContent"] = None):
        self.name = name
        self.myDsl_SegmentStructureContent = myDsl_SegmentStructureContent
        self.myDsl_SegmentStructureContent49 = myDsl_SegmentStructureContent49 if myDsl_SegmentStructureContent49 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_SegmentStructureContent(self):
        return self.__myDsl_SegmentStructureContent

    @myDsl_SegmentStructureContent.setter
    def myDsl_SegmentStructureContent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_SegmentStructureContent__myDsl_SegmentStructureContent", None)
        self.__myDsl_SegmentStructureContent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_SegmentStructure"):
                opp_val = getattr(old_value, "myDsl_SegmentStructure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_SegmentStructure"):
                opp_val = getattr(value, "myDsl_SegmentStructure", None)
                if opp_val is None:
                    setattr(value, "myDsl_SegmentStructure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_SegmentStructureContent49(self):
        return self.__myDsl_SegmentStructureContent49

    @myDsl_SegmentStructureContent49.setter
    def myDsl_SegmentStructureContent49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_SegmentStructureContent__myDsl_SegmentStructureContent49", None)
        self.__myDsl_SegmentStructureContent49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_DirectoryContent"):
                    opp_val = getattr(item, "myDsl_DirectoryContent", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_DirectoryContent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_DirectoryContent"):
                    opp_val = getattr(item, "myDsl_DirectoryContent", None)
                    
                    setattr(item, "myDsl_DirectoryContent", self)
                    

class myDsl_SegmentStructure:

    pass
class myDsl_Layer:

    pass
class myDsl_NTiers:

    pass
class myDsl_Architecture:

    pass
class myDsl_PresentationLayer:

    pass
class myDsl_DomainRelations:

    def __init__(self, name: str, myDsl_DomainRelations30: set["myDsl_EObject"] = None, myDsl_DomainRelations: "myDsl_DomainConnection" = None):
        self.name = name
        self.myDsl_DomainRelations30 = myDsl_DomainRelations30 if myDsl_DomainRelations30 is not None else set()
        self.myDsl_DomainRelations = myDsl_DomainRelations
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_DomainRelations30(self):
        return self.__myDsl_DomainRelations30

    @myDsl_DomainRelations30.setter
    def myDsl_DomainRelations30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_DomainRelations__myDsl_DomainRelations30", None)
        self.__myDsl_DomainRelations30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_EObject31"):
                    opp_val = getattr(item, "myDsl_EObject31", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_EObject31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_EObject31"):
                    opp_val = getattr(item, "myDsl_EObject31", None)
                    
                    setattr(item, "myDsl_EObject31", self)
                    

    @property
    def myDsl_DomainRelations(self):
        return self.__myDsl_DomainRelations

    @myDsl_DomainRelations.setter
    def myDsl_DomainRelations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_DomainRelations__myDsl_DomainRelations", None)
        self.__myDsl_DomainRelations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_DomainConnection"):
                opp_val = getattr(old_value, "myDsl_DomainConnection", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_DomainConnection"):
                opp_val = getattr(value, "myDsl_DomainConnection", None)
                if opp_val is None:
                    setattr(value, "myDsl_DomainConnection", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_DomainConnection:

    pass
class myDsl_LandingFunctions:

    def __init__(self, name: str, myDsl_LandingFunctions: "myDsl_LandingActions" = None):
        self.name = name
        self.myDsl_LandingFunctions = myDsl_LandingFunctions
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_LandingFunctions(self):
        return self.__myDsl_LandingFunctions

    @myDsl_LandingFunctions.setter
    def myDsl_LandingFunctions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_LandingFunctions__myDsl_LandingFunctions", None)
        self.__myDsl_LandingFunctions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_LandingActions27"):
                opp_val = getattr(old_value, "myDsl_LandingActions27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_LandingActions27"):
                opp_val = getattr(value, "myDsl_LandingActions27", None)
                if opp_val is None:
                    setattr(value, "myDsl_LandingActions27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_PhotoActionsFunctions:

    def __init__(self, name: str, myDsl_PhotoActionsFunctions: "myDsl_PhotoActions" = None):
        self.name = name
        self.myDsl_PhotoActionsFunctions = myDsl_PhotoActionsFunctions
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_PhotoActionsFunctions(self):
        return self.__myDsl_PhotoActionsFunctions

    @myDsl_PhotoActionsFunctions.setter
    def myDsl_PhotoActionsFunctions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_PhotoActionsFunctions__myDsl_PhotoActionsFunctions", None)
        self.__myDsl_PhotoActionsFunctions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_PhotoActions25"):
                opp_val = getattr(old_value, "myDsl_PhotoActions25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_PhotoActions25"):
                opp_val = getattr(value, "myDsl_PhotoActions25", None)
                if opp_val is None:
                    setattr(value, "myDsl_PhotoActions25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_AlbumManagementFunctions:

    def __init__(self, name: str, myDsl_AlbumManagementFunctions: "myDsl_AlbumManagement" = None):
        self.name = name
        self.myDsl_AlbumManagementFunctions = myDsl_AlbumManagementFunctions
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_AlbumManagementFunctions(self):
        return self.__myDsl_AlbumManagementFunctions

    @myDsl_AlbumManagementFunctions.setter
    def myDsl_AlbumManagementFunctions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_AlbumManagementFunctions__myDsl_AlbumManagementFunctions", None)
        self.__myDsl_AlbumManagementFunctions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_AlbumManagement23"):
                opp_val = getattr(old_value, "myDsl_AlbumManagement23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_AlbumManagement23"):
                opp_val = getattr(value, "myDsl_AlbumManagement23", None)
                if opp_val is None:
                    setattr(value, "myDsl_AlbumManagement23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_AppAccessFunctions:

    def __init__(self, name: str, myDsl_AppAccessFunctions: "myDsl_AppAccess" = None):
        self.name = name
        self.myDsl_AppAccessFunctions = myDsl_AppAccessFunctions
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_AppAccessFunctions(self):
        return self.__myDsl_AppAccessFunctions

    @myDsl_AppAccessFunctions.setter
    def myDsl_AppAccessFunctions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_AppAccessFunctions__myDsl_AppAccessFunctions", None)
        self.__myDsl_AppAccessFunctions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_AppAccess21"):
                opp_val = getattr(old_value, "myDsl_AppAccess21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_AppAccess21"):
                opp_val = getattr(value, "myDsl_AppAccess21", None)
                if opp_val is None:
                    setattr(value, "myDsl_AppAccess21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_ProfileManagementFunctions:

    def __init__(self, name: str, myDsl_ProfileManagementFunctions: "myDsl_ProfileManagement" = None):
        self.name = name
        self.myDsl_ProfileManagementFunctions = myDsl_ProfileManagementFunctions
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_ProfileManagementFunctions(self):
        return self.__myDsl_ProfileManagementFunctions

    @myDsl_ProfileManagementFunctions.setter
    def myDsl_ProfileManagementFunctions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ProfileManagementFunctions__myDsl_ProfileManagementFunctions", None)
        self.__myDsl_ProfileManagementFunctions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ProfileManagement19"):
                opp_val = getattr(old_value, "myDsl_ProfileManagement19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ProfileManagement19"):
                opp_val = getattr(value, "myDsl_ProfileManagement19", None)
                if opp_val is None:
                    setattr(value, "myDsl_ProfileManagement19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_LandingActions:

    pass
class myDsl_ProfileManagement:

    pass
class myDsl_Functionalities:

    pass
class myDsl_Functionality:

    pass
class myDsl_UserDomain:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class myDsl_Album:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class myDsl_Photo:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class myDsl_PhotoActions:

    pass
class myDsl_AlbumManagement:

    pass
class myDsl_AppAccess:

    pass
class myDsl_Entity:

    pass
class myDsl_Domain:

    def __init__(self, name: str, myDsl_Domain: set["myDsl_EObject"] = None):
        self.name = name
        self.myDsl_Domain = myDsl_Domain if myDsl_Domain is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Domain(self):
        return self.__myDsl_Domain

    @myDsl_Domain.setter
    def myDsl_Domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Domain__myDsl_Domain", None)
        self.__myDsl_Domain = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_EObject2"):
                    opp_val = getattr(item, "myDsl_EObject2", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_EObject2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_EObject2"):
                    opp_val = getattr(item, "myDsl_EObject2", None)
                    
                    setattr(item, "myDsl_EObject2", self)
                    

class myDsl_EObject:

    pass
class myDsl_Model:

    pass
class myDsl_Entities:

    pass