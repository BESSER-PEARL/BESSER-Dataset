from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class TextTypeMember0(Enum):
    inflow = "inflow"
    outflow = "outflow"
    biflow = "biflow"
    inhibitor = "inhibitor"
    reset = "reset"
class Tool(Enum):
    Yasper = "Yasper"
class TextType2(Enum):
    channel = "channel"
    store = "store"
class TextType1(Enum):
    AND = "AND"
    XOR = "XOR"
class Version(Enum):
    _1 = "_1"


############################################
# Definition of Classes
############################################

class YasperEPNML114_TransitionSpecific:

    def __init__(self, tokenCaseSensitive: str, tool: str, version: str, YasperEPNML114_TransitionSpecific: "YasperEPNML114_Roles" = None, YasperEPNML114_TransitionSpecific161: "YasperEPNML114_Cost" = None, YasperEPNML114_TransitionSpecific164: "YasperEPNML114_ProcessingTime" = None):
        self.tokenCaseSensitive = tokenCaseSensitive
        self.tool = tool
        self.version = version
        self.YasperEPNML114_TransitionSpecific = YasperEPNML114_TransitionSpecific
        self.YasperEPNML114_TransitionSpecific161 = YasperEPNML114_TransitionSpecific161
        self.YasperEPNML114_TransitionSpecific164 = YasperEPNML114_TransitionSpecific164
        
        pass
    @property
    def tool(self):
        return self.__tool

    @tool.setter
    def tool(self, tool: str):
        self.__tool = tool


    @property
    def tokenCaseSensitive(self):
        return self.__tokenCaseSensitive

    @tokenCaseSensitive.setter
    def tokenCaseSensitive(self, tokenCaseSensitive: str):
        self.__tokenCaseSensitive = tokenCaseSensitive


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def YasperEPNML114_TransitionSpecific161(self):
        return self.__YasperEPNML114_TransitionSpecific161

    @YasperEPNML114_TransitionSpecific161.setter
    def YasperEPNML114_TransitionSpecific161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_TransitionSpecific__YasperEPNML114_TransitionSpecific161", None)
        self.__YasperEPNML114_TransitionSpecific161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Cost162"):
                opp_val = getattr(old_value, "YasperEPNML114_Cost162", None)
                if opp_val == self:
                    setattr(old_value, "YasperEPNML114_Cost162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Cost162"):
                opp_val = getattr(value, "YasperEPNML114_Cost162", None)
                setattr(value, "YasperEPNML114_Cost162", self)

    @property
    def YasperEPNML114_TransitionSpecific164(self):
        return self.__YasperEPNML114_TransitionSpecific164

    @YasperEPNML114_TransitionSpecific164.setter
    def YasperEPNML114_TransitionSpecific164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_TransitionSpecific__YasperEPNML114_TransitionSpecific164", None)
        self.__YasperEPNML114_TransitionSpecific164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_ProcessingTime165"):
                opp_val = getattr(old_value, "YasperEPNML114_ProcessingTime165", None)
                if opp_val == self:
                    setattr(old_value, "YasperEPNML114_ProcessingTime165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_ProcessingTime165"):
                opp_val = getattr(value, "YasperEPNML114_ProcessingTime165", None)
                setattr(value, "YasperEPNML114_ProcessingTime165", self)

    @property
    def YasperEPNML114_TransitionSpecific(self):
        return self.__YasperEPNML114_TransitionSpecific

    @YasperEPNML114_TransitionSpecific.setter
    def YasperEPNML114_TransitionSpecific(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_TransitionSpecific__YasperEPNML114_TransitionSpecific", None)
        self.__YasperEPNML114_TransitionSpecific = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Roles159"):
                opp_val = getattr(old_value, "YasperEPNML114_Roles159", None)
                if opp_val == self:
                    setattr(old_value, "YasperEPNML114_Roles159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Roles159"):
                opp_val = getattr(value, "YasperEPNML114_Roles159", None)
                setattr(value, "YasperEPNML114_Roles159", self)

class YasperEPNML114_Transformation:

    def __init__(self, text: str, YasperEPNML114_Transformation: "YasperEPNML114_AnnotationGraphics" = None, YasperEPNML114_Transformation148: "YasperEPNML114_Transition" = None):
        self.text = text
        self.YasperEPNML114_Transformation = YasperEPNML114_Transformation
        self.YasperEPNML114_Transformation148 = YasperEPNML114_Transformation148
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def YasperEPNML114_Transformation148(self):
        return self.__YasperEPNML114_Transformation148

    @YasperEPNML114_Transformation148.setter
    def YasperEPNML114_Transformation148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Transformation__YasperEPNML114_Transformation148", None)
        self.__YasperEPNML114_Transformation148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Transition147"):
                opp_val = getattr(old_value, "YasperEPNML114_Transition147", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Transition147"):
                opp_val = getattr(value, "YasperEPNML114_Transition147", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_Transition147", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_Transformation(self):
        return self.__YasperEPNML114_Transformation

    @YasperEPNML114_Transformation.setter
    def YasperEPNML114_Transformation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Transformation__YasperEPNML114_Transformation", None)
        self.__YasperEPNML114_Transformation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_AnnotationGraphics139"):
                opp_val = getattr(old_value, "YasperEPNML114_AnnotationGraphics139", None)
                if opp_val == self:
                    setattr(old_value, "YasperEPNML114_AnnotationGraphics139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_AnnotationGraphics139"):
                opp_val = getattr(value, "YasperEPNML114_AnnotationGraphics139", None)
                setattr(value, "YasperEPNML114_AnnotationGraphics139", self)

class YasperEPNML114_Roles:

    pass
class YasperEPNML114_Role:

    def __init__(self, text: str, YasperEPNML114_Role: "YasperEPNML114_Roles" = None):
        self.text = text
        self.YasperEPNML114_Role = YasperEPNML114_Role
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def YasperEPNML114_Role(self):
        return self.__YasperEPNML114_Role

    @YasperEPNML114_Role.setter
    def YasperEPNML114_Role(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Role__YasperEPNML114_Role", None)
        self.__YasperEPNML114_Role = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Roles"):
                opp_val = getattr(old_value, "YasperEPNML114_Roles", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Roles"):
                opp_val = getattr(value, "YasperEPNML114_Roles", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_Roles", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class YasperEPNML114_ReferencePlaceSpecific:

    def __init__(self, tool: str, version: str, YasperEPNML114_ReferencePlaceSpecific: "YasperEPNML114_NodeGraphics" = None):
        self.tool = tool
        self.version = version
        self.YasperEPNML114_ReferencePlaceSpecific = YasperEPNML114_ReferencePlaceSpecific
        
        pass
    @property
    def tool(self):
        return self.__tool

    @tool.setter
    def tool(self, tool: str):
        self.__tool = tool


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def YasperEPNML114_ReferencePlaceSpecific(self):
        return self.__YasperEPNML114_ReferencePlaceSpecific

    @YasperEPNML114_ReferencePlaceSpecific.setter
    def YasperEPNML114_ReferencePlaceSpecific(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_ReferencePlaceSpecific__YasperEPNML114_ReferencePlaceSpecific", None)
        self.__YasperEPNML114_ReferencePlaceSpecific = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_NodeGraphics136"):
                opp_val = getattr(old_value, "YasperEPNML114_NodeGraphics136", None)
                if opp_val == self:
                    setattr(old_value, "YasperEPNML114_NodeGraphics136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_NodeGraphics136"):
                opp_val = getattr(value, "YasperEPNML114_NodeGraphics136", None)
                setattr(value, "YasperEPNML114_NodeGraphics136", self)

class YasperEPNML114_ProcessingTime:

    pass
class Place:

    pass
class YasperEPNML114_PlaceType:

    def __init__(self, text: str, YasperEPNML114_PlaceType: "YasperEPNML114_Place" = None):
        self.text = text
        self.YasperEPNML114_PlaceType = YasperEPNML114_PlaceType
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def YasperEPNML114_PlaceType(self):
        return self.__YasperEPNML114_PlaceType

    @YasperEPNML114_PlaceType.setter
    def YasperEPNML114_PlaceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_PlaceType__YasperEPNML114_PlaceType", None)
        self.__YasperEPNML114_PlaceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Place"):
                opp_val = getattr(old_value, "YasperEPNML114_Place", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Place"):
                opp_val = getattr(value, "YasperEPNML114_Place", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_Place", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class YasperEPNML114_Place:

    def __init__(self, group: str, id: str, YasperEPNML114_Place95: set["YasperEPNML114_NodeGraphics"] = None, YasperEPNML114_Place: set["YasperEPNML114_PlaceType"] = None, YasperEPNML114_Place101: set["YasperEPNML114_PnmlAnnotation"] = None, YasperEPNML114_Place104: set["YasperEPNML114_PnmlAnnotation"] = None, YasperEPNML114_Place98: set["YasperEPNML114_InitialMarking"] = None, YasperEPNML114_Place107: set["YasperEPNML114_ToolspecificType"] = None):
        self.group = group
        self.id = id
        self.YasperEPNML114_Place95 = YasperEPNML114_Place95 if YasperEPNML114_Place95 is not None else set()
        self.YasperEPNML114_Place = YasperEPNML114_Place if YasperEPNML114_Place is not None else set()
        self.YasperEPNML114_Place101 = YasperEPNML114_Place101 if YasperEPNML114_Place101 is not None else set()
        self.YasperEPNML114_Place104 = YasperEPNML114_Place104 if YasperEPNML114_Place104 is not None else set()
        self.YasperEPNML114_Place98 = YasperEPNML114_Place98 if YasperEPNML114_Place98 is not None else set()
        self.YasperEPNML114_Place107 = YasperEPNML114_Place107 if YasperEPNML114_Place107 is not None else set()
        
        pass
    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def YasperEPNML114_Place104(self):
        return self.__YasperEPNML114_Place104

    @YasperEPNML114_Place104.setter
    def YasperEPNML114_Place104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Place__YasperEPNML114_Place104", None)
        self.__YasperEPNML114_Place104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_PnmlAnnotation105"):
                    opp_val = getattr(item, "YasperEPNML114_PnmlAnnotation105", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_PnmlAnnotation105", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_PnmlAnnotation105"):
                    opp_val = getattr(item, "YasperEPNML114_PnmlAnnotation105", None)
                    
                    setattr(item, "YasperEPNML114_PnmlAnnotation105", self)
                    

    @property
    def YasperEPNML114_Place107(self):
        return self.__YasperEPNML114_Place107

    @YasperEPNML114_Place107.setter
    def YasperEPNML114_Place107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Place__YasperEPNML114_Place107", None)
        self.__YasperEPNML114_Place107 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_ToolspecificType108"):
                    opp_val = getattr(item, "YasperEPNML114_ToolspecificType108", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_ToolspecificType108", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_ToolspecificType108"):
                    opp_val = getattr(item, "YasperEPNML114_ToolspecificType108", None)
                    
                    setattr(item, "YasperEPNML114_ToolspecificType108", self)
                    

    @property
    def YasperEPNML114_Place95(self):
        return self.__YasperEPNML114_Place95

    @YasperEPNML114_Place95.setter
    def YasperEPNML114_Place95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Place__YasperEPNML114_Place95", None)
        self.__YasperEPNML114_Place95 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_NodeGraphics96"):
                    opp_val = getattr(item, "YasperEPNML114_NodeGraphics96", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_NodeGraphics96", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_NodeGraphics96"):
                    opp_val = getattr(item, "YasperEPNML114_NodeGraphics96", None)
                    
                    setattr(item, "YasperEPNML114_NodeGraphics96", self)
                    

    @property
    def YasperEPNML114_Place101(self):
        return self.__YasperEPNML114_Place101

    @YasperEPNML114_Place101.setter
    def YasperEPNML114_Place101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Place__YasperEPNML114_Place101", None)
        self.__YasperEPNML114_Place101 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_PnmlAnnotation102"):
                    opp_val = getattr(item, "YasperEPNML114_PnmlAnnotation102", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_PnmlAnnotation102", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_PnmlAnnotation102"):
                    opp_val = getattr(item, "YasperEPNML114_PnmlAnnotation102", None)
                    
                    setattr(item, "YasperEPNML114_PnmlAnnotation102", self)
                    

    @property
    def YasperEPNML114_Place(self):
        return self.__YasperEPNML114_Place

    @YasperEPNML114_Place.setter
    def YasperEPNML114_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Place__YasperEPNML114_Place", None)
        self.__YasperEPNML114_Place = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_PlaceType"):
                    opp_val = getattr(item, "YasperEPNML114_PlaceType", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_PlaceType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_PlaceType"):
                    opp_val = getattr(item, "YasperEPNML114_PlaceType", None)
                    
                    setattr(item, "YasperEPNML114_PlaceType", self)
                    

    @property
    def YasperEPNML114_Place98(self):
        return self.__YasperEPNML114_Place98

    @YasperEPNML114_Place98.setter
    def YasperEPNML114_Place98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Place__YasperEPNML114_Place98", None)
        self.__YasperEPNML114_Place98 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_InitialMarking99"):
                    opp_val = getattr(item, "YasperEPNML114_InitialMarking99", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_InitialMarking99", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_InitialMarking99"):
                    opp_val = getattr(item, "YasperEPNML114_InitialMarking99", None)
                    
                    setattr(item, "YasperEPNML114_InitialMarking99", self)
                    

class YasperEPNML114_TransitionType:

    def __init__(self, text: str, YasperEPNML114_TransitionType: "YasperEPNML114_Page" = None, YasperEPNML114_TransitionType142: "YasperEPNML114_Transition" = None):
        self.text = text
        self.YasperEPNML114_TransitionType = YasperEPNML114_TransitionType
        self.YasperEPNML114_TransitionType142 = YasperEPNML114_TransitionType142
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def YasperEPNML114_TransitionType142(self):
        return self.__YasperEPNML114_TransitionType142

    @YasperEPNML114_TransitionType142.setter
    def YasperEPNML114_TransitionType142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_TransitionType__YasperEPNML114_TransitionType142", None)
        self.__YasperEPNML114_TransitionType142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Transition141"):
                opp_val = getattr(old_value, "YasperEPNML114_Transition141", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Transition141"):
                opp_val = getattr(value, "YasperEPNML114_Transition141", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_Transition141", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_TransitionType(self):
        return self.__YasperEPNML114_TransitionType

    @YasperEPNML114_TransitionType.setter
    def YasperEPNML114_TransitionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_TransitionType__YasperEPNML114_TransitionType", None)
        self.__YasperEPNML114_TransitionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Page71"):
                opp_val = getattr(old_value, "YasperEPNML114_Page71", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Page71"):
                opp_val = getattr(value, "YasperEPNML114_Page71", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_Page71", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class YasperEPNML114_ReferencePlace:

    def __init__(self, group: str, id: str, ref: str, YasperEPNML114_ReferencePlace: "YasperEPNML114_Page" = None, YasperEPNML114_ReferencePlace130: set["YasperEPNML114_PnmlAnnotation"] = None, YasperEPNML114_ReferencePlace124: set["YasperEPNML114_NodeGraphics"] = None, YasperEPNML114_ReferencePlace127: set["YasperEPNML114_PnmlAnnotation"] = None, YasperEPNML114_ReferencePlace133: set["YasperEPNML114_ToolspecificType"] = None):
        self.group = group
        self.id = id
        self.ref = ref
        self.YasperEPNML114_ReferencePlace = YasperEPNML114_ReferencePlace
        self.YasperEPNML114_ReferencePlace130 = YasperEPNML114_ReferencePlace130 if YasperEPNML114_ReferencePlace130 is not None else set()
        self.YasperEPNML114_ReferencePlace124 = YasperEPNML114_ReferencePlace124 if YasperEPNML114_ReferencePlace124 is not None else set()
        self.YasperEPNML114_ReferencePlace127 = YasperEPNML114_ReferencePlace127 if YasperEPNML114_ReferencePlace127 is not None else set()
        self.YasperEPNML114_ReferencePlace133 = YasperEPNML114_ReferencePlace133 if YasperEPNML114_ReferencePlace133 is not None else set()
        
        pass
    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def ref(self):
        return self.__ref

    @ref.setter
    def ref(self, ref: str):
        self.__ref = ref


    @property
    def YasperEPNML114_ReferencePlace127(self):
        return self.__YasperEPNML114_ReferencePlace127

    @YasperEPNML114_ReferencePlace127.setter
    def YasperEPNML114_ReferencePlace127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_ReferencePlace__YasperEPNML114_ReferencePlace127", None)
        self.__YasperEPNML114_ReferencePlace127 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_PnmlAnnotation128"):
                    opp_val = getattr(item, "YasperEPNML114_PnmlAnnotation128", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_PnmlAnnotation128", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_PnmlAnnotation128"):
                    opp_val = getattr(item, "YasperEPNML114_PnmlAnnotation128", None)
                    
                    setattr(item, "YasperEPNML114_PnmlAnnotation128", self)
                    

    @property
    def YasperEPNML114_ReferencePlace(self):
        return self.__YasperEPNML114_ReferencePlace

    @YasperEPNML114_ReferencePlace.setter
    def YasperEPNML114_ReferencePlace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_ReferencePlace__YasperEPNML114_ReferencePlace", None)
        self.__YasperEPNML114_ReferencePlace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Page66"):
                opp_val = getattr(old_value, "YasperEPNML114_Page66", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Page66"):
                opp_val = getattr(value, "YasperEPNML114_Page66", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_Page66", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_ReferencePlace133(self):
        return self.__YasperEPNML114_ReferencePlace133

    @YasperEPNML114_ReferencePlace133.setter
    def YasperEPNML114_ReferencePlace133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_ReferencePlace__YasperEPNML114_ReferencePlace133", None)
        self.__YasperEPNML114_ReferencePlace133 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_ToolspecificType134"):
                    opp_val = getattr(item, "YasperEPNML114_ToolspecificType134", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_ToolspecificType134", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_ToolspecificType134"):
                    opp_val = getattr(item, "YasperEPNML114_ToolspecificType134", None)
                    
                    setattr(item, "YasperEPNML114_ToolspecificType134", self)
                    

    @property
    def YasperEPNML114_ReferencePlace130(self):
        return self.__YasperEPNML114_ReferencePlace130

    @YasperEPNML114_ReferencePlace130.setter
    def YasperEPNML114_ReferencePlace130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_ReferencePlace__YasperEPNML114_ReferencePlace130", None)
        self.__YasperEPNML114_ReferencePlace130 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_PnmlAnnotation131"):
                    opp_val = getattr(item, "YasperEPNML114_PnmlAnnotation131", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_PnmlAnnotation131", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_PnmlAnnotation131"):
                    opp_val = getattr(item, "YasperEPNML114_PnmlAnnotation131", None)
                    
                    setattr(item, "YasperEPNML114_PnmlAnnotation131", self)
                    

    @property
    def YasperEPNML114_ReferencePlace124(self):
        return self.__YasperEPNML114_ReferencePlace124

    @YasperEPNML114_ReferencePlace124.setter
    def YasperEPNML114_ReferencePlace124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_ReferencePlace__YasperEPNML114_ReferencePlace124", None)
        self.__YasperEPNML114_ReferencePlace124 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_NodeGraphics125"):
                    opp_val = getattr(item, "YasperEPNML114_NodeGraphics125", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_NodeGraphics125", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_NodeGraphics125"):
                    opp_val = getattr(item, "YasperEPNML114_NodeGraphics125", None)
                    
                    setattr(item, "YasperEPNML114_NodeGraphics125", self)
                    

class YasperEPNML114_NodeGraphics:

    def __init__(self, group: str, YasperEPNML114_NodeGraphics: set["YasperEPNML114_TwoDimVector"] = None, YasperEPNML114_NodeGraphics63: set["YasperEPNML114_TwoDimVector"] = None, YasperEPNML114_NodeGraphics96: "YasperEPNML114_Place" = None, YasperEPNML114_NodeGraphics125: "YasperEPNML114_ReferencePlace" = None, YasperEPNML114_NodeGraphics136: "YasperEPNML114_ReferencePlaceSpecific" = None, YasperEPNML114_NodeGraphics145: "YasperEPNML114_Transition" = None):
        self.group = group
        self.YasperEPNML114_NodeGraphics = YasperEPNML114_NodeGraphics if YasperEPNML114_NodeGraphics is not None else set()
        self.YasperEPNML114_NodeGraphics63 = YasperEPNML114_NodeGraphics63 if YasperEPNML114_NodeGraphics63 is not None else set()
        self.YasperEPNML114_NodeGraphics96 = YasperEPNML114_NodeGraphics96
        self.YasperEPNML114_NodeGraphics125 = YasperEPNML114_NodeGraphics125
        self.YasperEPNML114_NodeGraphics136 = YasperEPNML114_NodeGraphics136
        self.YasperEPNML114_NodeGraphics145 = YasperEPNML114_NodeGraphics145
        
        pass
    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group


    @property
    def YasperEPNML114_NodeGraphics136(self):
        return self.__YasperEPNML114_NodeGraphics136

    @YasperEPNML114_NodeGraphics136.setter
    def YasperEPNML114_NodeGraphics136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_NodeGraphics__YasperEPNML114_NodeGraphics136", None)
        self.__YasperEPNML114_NodeGraphics136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_ReferencePlaceSpecific"):
                opp_val = getattr(old_value, "YasperEPNML114_ReferencePlaceSpecific", None)
                if opp_val == self:
                    setattr(old_value, "YasperEPNML114_ReferencePlaceSpecific", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_ReferencePlaceSpecific"):
                opp_val = getattr(value, "YasperEPNML114_ReferencePlaceSpecific", None)
                setattr(value, "YasperEPNML114_ReferencePlaceSpecific", self)

    @property
    def YasperEPNML114_NodeGraphics145(self):
        return self.__YasperEPNML114_NodeGraphics145

    @YasperEPNML114_NodeGraphics145.setter
    def YasperEPNML114_NodeGraphics145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_NodeGraphics__YasperEPNML114_NodeGraphics145", None)
        self.__YasperEPNML114_NodeGraphics145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Transition144"):
                opp_val = getattr(old_value, "YasperEPNML114_Transition144", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Transition144"):
                opp_val = getattr(value, "YasperEPNML114_Transition144", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_Transition144", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_NodeGraphics96(self):
        return self.__YasperEPNML114_NodeGraphics96

    @YasperEPNML114_NodeGraphics96.setter
    def YasperEPNML114_NodeGraphics96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_NodeGraphics__YasperEPNML114_NodeGraphics96", None)
        self.__YasperEPNML114_NodeGraphics96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Place95"):
                opp_val = getattr(old_value, "YasperEPNML114_Place95", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Place95"):
                opp_val = getattr(value, "YasperEPNML114_Place95", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_Place95", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_NodeGraphics63(self):
        return self.__YasperEPNML114_NodeGraphics63

    @YasperEPNML114_NodeGraphics63.setter
    def YasperEPNML114_NodeGraphics63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_NodeGraphics__YasperEPNML114_NodeGraphics63", None)
        self.__YasperEPNML114_NodeGraphics63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_TwoDimVector64"):
                    opp_val = getattr(item, "YasperEPNML114_TwoDimVector64", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_TwoDimVector64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_TwoDimVector64"):
                    opp_val = getattr(item, "YasperEPNML114_TwoDimVector64", None)
                    
                    setattr(item, "YasperEPNML114_TwoDimVector64", self)
                    

    @property
    def YasperEPNML114_NodeGraphics(self):
        return self.__YasperEPNML114_NodeGraphics

    @YasperEPNML114_NodeGraphics.setter
    def YasperEPNML114_NodeGraphics(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_NodeGraphics__YasperEPNML114_NodeGraphics", None)
        self.__YasperEPNML114_NodeGraphics = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_TwoDimVector61"):
                    opp_val = getattr(item, "YasperEPNML114_TwoDimVector61", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_TwoDimVector61", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_TwoDimVector61"):
                    opp_val = getattr(item, "YasperEPNML114_TwoDimVector61", None)
                    
                    setattr(item, "YasperEPNML114_TwoDimVector61", self)
                    

    @property
    def YasperEPNML114_NodeGraphics125(self):
        return self.__YasperEPNML114_NodeGraphics125

    @YasperEPNML114_NodeGraphics125.setter
    def YasperEPNML114_NodeGraphics125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_NodeGraphics__YasperEPNML114_NodeGraphics125", None)
        self.__YasperEPNML114_NodeGraphics125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_ReferencePlace124"):
                opp_val = getattr(old_value, "YasperEPNML114_ReferencePlace124", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_ReferencePlace124"):
                opp_val = getattr(value, "YasperEPNML114_ReferencePlace124", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_ReferencePlace124", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class YasperEPNML114_Page:

    def __init__(self, group: str, id: str, YasperEPNML114_Page66: set["YasperEPNML114_ReferencePlace"] = None, YasperEPNML114_Page71: set["YasperEPNML114_TransitionType"] = None, YasperEPNML114_Page: "YasperEPNML114_Net" = None, YasperEPNML114_Page73: set["YasperEPNML114_PlaceType1"] = None, YasperEPNML114_Page68: set["YasperEPNML114_NetGraphics"] = None, YasperEPNML114_Page79: set["YasperEPNML114_Arc"] = None, YasperEPNML114_Page83: "YasperEPNML114_Page" = None, YasperEPNML114_Page81: set["YasperEPNML114_Page"] = None, YasperEPNML114_Page76: set["YasperEPNML114_Transition"] = None, YasperEPNML114_Page85: set["YasperEPNML114_PnmlAnnotation"] = None, YasperEPNML114_Page88: set["YasperEPNML114_PnmlAnnotation"] = None, YasperEPNML114_Page91: set["YasperEPNML114_ToolspecificType"] = None):
        self.group = group
        self.id = id
        self.YasperEPNML114_Page66 = YasperEPNML114_Page66 if YasperEPNML114_Page66 is not None else set()
        self.YasperEPNML114_Page71 = YasperEPNML114_Page71 if YasperEPNML114_Page71 is not None else set()
        self.YasperEPNML114_Page = YasperEPNML114_Page
        self.YasperEPNML114_Page73 = YasperEPNML114_Page73 if YasperEPNML114_Page73 is not None else set()
        self.YasperEPNML114_Page68 = YasperEPNML114_Page68 if YasperEPNML114_Page68 is not None else set()
        self.YasperEPNML114_Page79 = YasperEPNML114_Page79 if YasperEPNML114_Page79 is not None else set()
        self.YasperEPNML114_Page83 = YasperEPNML114_Page83
        self.YasperEPNML114_Page81 = YasperEPNML114_Page81 if YasperEPNML114_Page81 is not None else set()
        self.YasperEPNML114_Page76 = YasperEPNML114_Page76 if YasperEPNML114_Page76 is not None else set()
        self.YasperEPNML114_Page85 = YasperEPNML114_Page85 if YasperEPNML114_Page85 is not None else set()
        self.YasperEPNML114_Page88 = YasperEPNML114_Page88 if YasperEPNML114_Page88 is not None else set()
        self.YasperEPNML114_Page91 = YasperEPNML114_Page91 if YasperEPNML114_Page91 is not None else set()
        
        pass
    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def YasperEPNML114_Page76(self):
        return self.__YasperEPNML114_Page76

    @YasperEPNML114_Page76.setter
    def YasperEPNML114_Page76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Page__YasperEPNML114_Page76", None)
        self.__YasperEPNML114_Page76 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_Transition77"):
                    opp_val = getattr(item, "YasperEPNML114_Transition77", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_Transition77", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_Transition77"):
                    opp_val = getattr(item, "YasperEPNML114_Transition77", None)
                    
                    setattr(item, "YasperEPNML114_Transition77", self)
                    

    @property
    def YasperEPNML114_Page68(self):
        return self.__YasperEPNML114_Page68

    @YasperEPNML114_Page68.setter
    def YasperEPNML114_Page68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Page__YasperEPNML114_Page68", None)
        self.__YasperEPNML114_Page68 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_NetGraphics69"):
                    opp_val = getattr(item, "YasperEPNML114_NetGraphics69", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_NetGraphics69", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_NetGraphics69"):
                    opp_val = getattr(item, "YasperEPNML114_NetGraphics69", None)
                    
                    setattr(item, "YasperEPNML114_NetGraphics69", self)
                    

    @property
    def YasperEPNML114_Page66(self):
        return self.__YasperEPNML114_Page66

    @YasperEPNML114_Page66.setter
    def YasperEPNML114_Page66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Page__YasperEPNML114_Page66", None)
        self.__YasperEPNML114_Page66 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_ReferencePlace"):
                    opp_val = getattr(item, "YasperEPNML114_ReferencePlace", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_ReferencePlace", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_ReferencePlace"):
                    opp_val = getattr(item, "YasperEPNML114_ReferencePlace", None)
                    
                    setattr(item, "YasperEPNML114_ReferencePlace", self)
                    

    @property
    def YasperEPNML114_Page83(self):
        return self.__YasperEPNML114_Page83

    @YasperEPNML114_Page83.setter
    def YasperEPNML114_Page83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Page__YasperEPNML114_Page83", None)
        self.__YasperEPNML114_Page83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Page81"):
                opp_val = getattr(old_value, "YasperEPNML114_Page81", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Page81"):
                opp_val = getattr(value, "YasperEPNML114_Page81", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_Page81", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_Page73(self):
        return self.__YasperEPNML114_Page73

    @YasperEPNML114_Page73.setter
    def YasperEPNML114_Page73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Page__YasperEPNML114_Page73", None)
        self.__YasperEPNML114_Page73 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_PlaceType174"):
                    opp_val = getattr(item, "YasperEPNML114_PlaceType174", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_PlaceType174", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_PlaceType174"):
                    opp_val = getattr(item, "YasperEPNML114_PlaceType174", None)
                    
                    setattr(item, "YasperEPNML114_PlaceType174", self)
                    

    @property
    def YasperEPNML114_Page79(self):
        return self.__YasperEPNML114_Page79

    @YasperEPNML114_Page79.setter
    def YasperEPNML114_Page79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Page__YasperEPNML114_Page79", None)
        self.__YasperEPNML114_Page79 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_Arc80"):
                    opp_val = getattr(item, "YasperEPNML114_Arc80", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_Arc80", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_Arc80"):
                    opp_val = getattr(item, "YasperEPNML114_Arc80", None)
                    
                    setattr(item, "YasperEPNML114_Arc80", self)
                    

    @property
    def YasperEPNML114_Page81(self):
        return self.__YasperEPNML114_Page81

    @YasperEPNML114_Page81.setter
    def YasperEPNML114_Page81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Page__YasperEPNML114_Page81", None)
        self.__YasperEPNML114_Page81 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_Page83"):
                    opp_val = getattr(item, "YasperEPNML114_Page83", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_Page83", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_Page83"):
                    opp_val = getattr(item, "YasperEPNML114_Page83", None)
                    
                    setattr(item, "YasperEPNML114_Page83", self)
                    

    @property
    def YasperEPNML114_Page71(self):
        return self.__YasperEPNML114_Page71

    @YasperEPNML114_Page71.setter
    def YasperEPNML114_Page71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Page__YasperEPNML114_Page71", None)
        self.__YasperEPNML114_Page71 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_TransitionType"):
                    opp_val = getattr(item, "YasperEPNML114_TransitionType", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_TransitionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_TransitionType"):
                    opp_val = getattr(item, "YasperEPNML114_TransitionType", None)
                    
                    setattr(item, "YasperEPNML114_TransitionType", self)
                    

    @property
    def YasperEPNML114_Page(self):
        return self.__YasperEPNML114_Page

    @YasperEPNML114_Page.setter
    def YasperEPNML114_Page(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Page__YasperEPNML114_Page", None)
        self.__YasperEPNML114_Page = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Net44"):
                opp_val = getattr(old_value, "YasperEPNML114_Net44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Net44"):
                opp_val = getattr(value, "YasperEPNML114_Net44", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_Net44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_Page85(self):
        return self.__YasperEPNML114_Page85

    @YasperEPNML114_Page85.setter
    def YasperEPNML114_Page85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Page__YasperEPNML114_Page85", None)
        self.__YasperEPNML114_Page85 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_PnmlAnnotation86"):
                    opp_val = getattr(item, "YasperEPNML114_PnmlAnnotation86", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_PnmlAnnotation86", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_PnmlAnnotation86"):
                    opp_val = getattr(item, "YasperEPNML114_PnmlAnnotation86", None)
                    
                    setattr(item, "YasperEPNML114_PnmlAnnotation86", self)
                    

    @property
    def YasperEPNML114_Page88(self):
        return self.__YasperEPNML114_Page88

    @YasperEPNML114_Page88.setter
    def YasperEPNML114_Page88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Page__YasperEPNML114_Page88", None)
        self.__YasperEPNML114_Page88 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_PnmlAnnotation89"):
                    opp_val = getattr(item, "YasperEPNML114_PnmlAnnotation89", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_PnmlAnnotation89", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_PnmlAnnotation89"):
                    opp_val = getattr(item, "YasperEPNML114_PnmlAnnotation89", None)
                    
                    setattr(item, "YasperEPNML114_PnmlAnnotation89", self)
                    

    @property
    def YasperEPNML114_Page91(self):
        return self.__YasperEPNML114_Page91

    @YasperEPNML114_Page91.setter
    def YasperEPNML114_Page91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Page__YasperEPNML114_Page91", None)
        self.__YasperEPNML114_Page91 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_ToolspecificType92"):
                    opp_val = getattr(item, "YasperEPNML114_ToolspecificType92", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_ToolspecificType92", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_ToolspecificType92"):
                    opp_val = getattr(item, "YasperEPNML114_ToolspecificType92", None)
                    
                    setattr(item, "YasperEPNML114_ToolspecificType92", self)
                    

class YasperEPNML114_Transition:

    def __init__(self, group: str, id: str, YasperEPNML114_Transition: "YasperEPNML114_Net" = None, YasperEPNML114_Transition77: "YasperEPNML114_Page" = None, YasperEPNML114_Transition141: set["YasperEPNML114_TransitionType"] = None, YasperEPNML114_Transition144: set["YasperEPNML114_NodeGraphics"] = None, YasperEPNML114_Transition147: set["YasperEPNML114_Transformation"] = None, YasperEPNML114_Transition150: set["YasperEPNML114_PnmlAnnotation"] = None, YasperEPNML114_Transition153: set["YasperEPNML114_PnmlAnnotation"] = None, YasperEPNML114_Transition156: set["YasperEPNML114_ToolspecificType"] = None):
        self.group = group
        self.id = id
        self.YasperEPNML114_Transition = YasperEPNML114_Transition
        self.YasperEPNML114_Transition77 = YasperEPNML114_Transition77
        self.YasperEPNML114_Transition141 = YasperEPNML114_Transition141 if YasperEPNML114_Transition141 is not None else set()
        self.YasperEPNML114_Transition144 = YasperEPNML114_Transition144 if YasperEPNML114_Transition144 is not None else set()
        self.YasperEPNML114_Transition147 = YasperEPNML114_Transition147 if YasperEPNML114_Transition147 is not None else set()
        self.YasperEPNML114_Transition150 = YasperEPNML114_Transition150 if YasperEPNML114_Transition150 is not None else set()
        self.YasperEPNML114_Transition153 = YasperEPNML114_Transition153 if YasperEPNML114_Transition153 is not None else set()
        self.YasperEPNML114_Transition156 = YasperEPNML114_Transition156 if YasperEPNML114_Transition156 is not None else set()
        
        pass
    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def YasperEPNML114_Transition141(self):
        return self.__YasperEPNML114_Transition141

    @YasperEPNML114_Transition141.setter
    def YasperEPNML114_Transition141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Transition__YasperEPNML114_Transition141", None)
        self.__YasperEPNML114_Transition141 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_TransitionType142"):
                    opp_val = getattr(item, "YasperEPNML114_TransitionType142", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_TransitionType142", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_TransitionType142"):
                    opp_val = getattr(item, "YasperEPNML114_TransitionType142", None)
                    
                    setattr(item, "YasperEPNML114_TransitionType142", self)
                    

    @property
    def YasperEPNML114_Transition156(self):
        return self.__YasperEPNML114_Transition156

    @YasperEPNML114_Transition156.setter
    def YasperEPNML114_Transition156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Transition__YasperEPNML114_Transition156", None)
        self.__YasperEPNML114_Transition156 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_ToolspecificType157"):
                    opp_val = getattr(item, "YasperEPNML114_ToolspecificType157", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_ToolspecificType157", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_ToolspecificType157"):
                    opp_val = getattr(item, "YasperEPNML114_ToolspecificType157", None)
                    
                    setattr(item, "YasperEPNML114_ToolspecificType157", self)
                    

    @property
    def YasperEPNML114_Transition77(self):
        return self.__YasperEPNML114_Transition77

    @YasperEPNML114_Transition77.setter
    def YasperEPNML114_Transition77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Transition__YasperEPNML114_Transition77", None)
        self.__YasperEPNML114_Transition77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Page76"):
                opp_val = getattr(old_value, "YasperEPNML114_Page76", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Page76"):
                opp_val = getattr(value, "YasperEPNML114_Page76", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_Page76", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_Transition(self):
        return self.__YasperEPNML114_Transition

    @YasperEPNML114_Transition.setter
    def YasperEPNML114_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Transition__YasperEPNML114_Transition", None)
        self.__YasperEPNML114_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Net39"):
                opp_val = getattr(old_value, "YasperEPNML114_Net39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Net39"):
                opp_val = getattr(value, "YasperEPNML114_Net39", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_Net39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_Transition153(self):
        return self.__YasperEPNML114_Transition153

    @YasperEPNML114_Transition153.setter
    def YasperEPNML114_Transition153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Transition__YasperEPNML114_Transition153", None)
        self.__YasperEPNML114_Transition153 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_PnmlAnnotation154"):
                    opp_val = getattr(item, "YasperEPNML114_PnmlAnnotation154", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_PnmlAnnotation154", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_PnmlAnnotation154"):
                    opp_val = getattr(item, "YasperEPNML114_PnmlAnnotation154", None)
                    
                    setattr(item, "YasperEPNML114_PnmlAnnotation154", self)
                    

    @property
    def YasperEPNML114_Transition150(self):
        return self.__YasperEPNML114_Transition150

    @YasperEPNML114_Transition150.setter
    def YasperEPNML114_Transition150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Transition__YasperEPNML114_Transition150", None)
        self.__YasperEPNML114_Transition150 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_PnmlAnnotation151"):
                    opp_val = getattr(item, "YasperEPNML114_PnmlAnnotation151", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_PnmlAnnotation151", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_PnmlAnnotation151"):
                    opp_val = getattr(item, "YasperEPNML114_PnmlAnnotation151", None)
                    
                    setattr(item, "YasperEPNML114_PnmlAnnotation151", self)
                    

    @property
    def YasperEPNML114_Transition147(self):
        return self.__YasperEPNML114_Transition147

    @YasperEPNML114_Transition147.setter
    def YasperEPNML114_Transition147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Transition__YasperEPNML114_Transition147", None)
        self.__YasperEPNML114_Transition147 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_Transformation148"):
                    opp_val = getattr(item, "YasperEPNML114_Transformation148", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_Transformation148", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_Transformation148"):
                    opp_val = getattr(item, "YasperEPNML114_Transformation148", None)
                    
                    setattr(item, "YasperEPNML114_Transformation148", self)
                    

    @property
    def YasperEPNML114_Transition144(self):
        return self.__YasperEPNML114_Transition144

    @YasperEPNML114_Transition144.setter
    def YasperEPNML114_Transition144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Transition__YasperEPNML114_Transition144", None)
        self.__YasperEPNML114_Transition144 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_NodeGraphics145"):
                    opp_val = getattr(item, "YasperEPNML114_NodeGraphics145", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_NodeGraphics145", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_NodeGraphics145"):
                    opp_val = getattr(item, "YasperEPNML114_NodeGraphics145", None)
                    
                    setattr(item, "YasperEPNML114_NodeGraphics145", self)
                    

class YasperEPNML114_Net:

    def __init__(self, group: str, id: str, type: str, YasperEPNML114_Net: set["YasperEPNML114_NetGraphics"] = None, YasperEPNML114_Net37: set["YasperEPNML114_PlaceType1"] = None, YasperEPNML114_Net39: set["YasperEPNML114_Transition"] = None, YasperEPNML114_Net41: set["YasperEPNML114_Arc"] = None, YasperEPNML114_Net46: set["YasperEPNML114_PnmlAnnotation"] = None, YasperEPNML114_Net49: set["YasperEPNML114_PnmlAnnotation"] = None, YasperEPNML114_Net44: set["YasperEPNML114_Page"] = None, YasperEPNML114_Net52: set["YasperEPNML114_ToolspecificType"] = None, YasperEPNML114_Net111: "YasperEPNML114_Pnml" = None):
        self.group = group
        self.id = id
        self.type = type
        self.YasperEPNML114_Net = YasperEPNML114_Net if YasperEPNML114_Net is not None else set()
        self.YasperEPNML114_Net37 = YasperEPNML114_Net37 if YasperEPNML114_Net37 is not None else set()
        self.YasperEPNML114_Net39 = YasperEPNML114_Net39 if YasperEPNML114_Net39 is not None else set()
        self.YasperEPNML114_Net41 = YasperEPNML114_Net41 if YasperEPNML114_Net41 is not None else set()
        self.YasperEPNML114_Net46 = YasperEPNML114_Net46 if YasperEPNML114_Net46 is not None else set()
        self.YasperEPNML114_Net49 = YasperEPNML114_Net49 if YasperEPNML114_Net49 is not None else set()
        self.YasperEPNML114_Net44 = YasperEPNML114_Net44 if YasperEPNML114_Net44 is not None else set()
        self.YasperEPNML114_Net52 = YasperEPNML114_Net52 if YasperEPNML114_Net52 is not None else set()
        self.YasperEPNML114_Net111 = YasperEPNML114_Net111
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def YasperEPNML114_Net(self):
        return self.__YasperEPNML114_Net

    @YasperEPNML114_Net.setter
    def YasperEPNML114_Net(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Net__YasperEPNML114_Net", None)
        self.__YasperEPNML114_Net = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_NetGraphics"):
                    opp_val = getattr(item, "YasperEPNML114_NetGraphics", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_NetGraphics", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_NetGraphics"):
                    opp_val = getattr(item, "YasperEPNML114_NetGraphics", None)
                    
                    setattr(item, "YasperEPNML114_NetGraphics", self)
                    

    @property
    def YasperEPNML114_Net39(self):
        return self.__YasperEPNML114_Net39

    @YasperEPNML114_Net39.setter
    def YasperEPNML114_Net39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Net__YasperEPNML114_Net39", None)
        self.__YasperEPNML114_Net39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_Transition"):
                    opp_val = getattr(item, "YasperEPNML114_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_Transition"):
                    opp_val = getattr(item, "YasperEPNML114_Transition", None)
                    
                    setattr(item, "YasperEPNML114_Transition", self)
                    

    @property
    def YasperEPNML114_Net44(self):
        return self.__YasperEPNML114_Net44

    @YasperEPNML114_Net44.setter
    def YasperEPNML114_Net44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Net__YasperEPNML114_Net44", None)
        self.__YasperEPNML114_Net44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_Page"):
                    opp_val = getattr(item, "YasperEPNML114_Page", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_Page", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_Page"):
                    opp_val = getattr(item, "YasperEPNML114_Page", None)
                    
                    setattr(item, "YasperEPNML114_Page", self)
                    

    @property
    def YasperEPNML114_Net49(self):
        return self.__YasperEPNML114_Net49

    @YasperEPNML114_Net49.setter
    def YasperEPNML114_Net49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Net__YasperEPNML114_Net49", None)
        self.__YasperEPNML114_Net49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_PnmlAnnotation50"):
                    opp_val = getattr(item, "YasperEPNML114_PnmlAnnotation50", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_PnmlAnnotation50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_PnmlAnnotation50"):
                    opp_val = getattr(item, "YasperEPNML114_PnmlAnnotation50", None)
                    
                    setattr(item, "YasperEPNML114_PnmlAnnotation50", self)
                    

    @property
    def YasperEPNML114_Net46(self):
        return self.__YasperEPNML114_Net46

    @YasperEPNML114_Net46.setter
    def YasperEPNML114_Net46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Net__YasperEPNML114_Net46", None)
        self.__YasperEPNML114_Net46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_PnmlAnnotation47"):
                    opp_val = getattr(item, "YasperEPNML114_PnmlAnnotation47", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_PnmlAnnotation47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_PnmlAnnotation47"):
                    opp_val = getattr(item, "YasperEPNML114_PnmlAnnotation47", None)
                    
                    setattr(item, "YasperEPNML114_PnmlAnnotation47", self)
                    

    @property
    def YasperEPNML114_Net111(self):
        return self.__YasperEPNML114_Net111

    @YasperEPNML114_Net111.setter
    def YasperEPNML114_Net111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Net__YasperEPNML114_Net111", None)
        self.__YasperEPNML114_Net111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Pnml110"):
                opp_val = getattr(old_value, "YasperEPNML114_Pnml110", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Pnml110"):
                opp_val = getattr(value, "YasperEPNML114_Pnml110", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_Pnml110", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_Net37(self):
        return self.__YasperEPNML114_Net37

    @YasperEPNML114_Net37.setter
    def YasperEPNML114_Net37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Net__YasperEPNML114_Net37", None)
        self.__YasperEPNML114_Net37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_PlaceType1"):
                    opp_val = getattr(item, "YasperEPNML114_PlaceType1", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_PlaceType1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_PlaceType1"):
                    opp_val = getattr(item, "YasperEPNML114_PlaceType1", None)
                    
                    setattr(item, "YasperEPNML114_PlaceType1", self)
                    

    @property
    def YasperEPNML114_Net41(self):
        return self.__YasperEPNML114_Net41

    @YasperEPNML114_Net41.setter
    def YasperEPNML114_Net41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Net__YasperEPNML114_Net41", None)
        self.__YasperEPNML114_Net41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_Arc42"):
                    opp_val = getattr(item, "YasperEPNML114_Arc42", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_Arc42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_Arc42"):
                    opp_val = getattr(item, "YasperEPNML114_Arc42", None)
                    
                    setattr(item, "YasperEPNML114_Arc42", self)
                    

    @property
    def YasperEPNML114_Net52(self):
        return self.__YasperEPNML114_Net52

    @YasperEPNML114_Net52.setter
    def YasperEPNML114_Net52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Net__YasperEPNML114_Net52", None)
        self.__YasperEPNML114_Net52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_ToolspecificType53"):
                    opp_val = getattr(item, "YasperEPNML114_ToolspecificType53", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_ToolspecificType53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_ToolspecificType53"):
                    opp_val = getattr(item, "YasperEPNML114_ToolspecificType53", None)
                    
                    setattr(item, "YasperEPNML114_ToolspecificType53", self)
                    

class YasperEPNML114_PlaceType1(Place):

    pass
class YasperEPNML114_NetGraphics:

    def __init__(self, group: str, YasperEPNML114_NetGraphics58: set["YasperEPNML114_TwoDimVector"] = None, YasperEPNML114_NetGraphics: "YasperEPNML114_Net" = None, YasperEPNML114_NetGraphics55: set["YasperEPNML114_TwoDimVector"] = None, YasperEPNML114_NetGraphics69: "YasperEPNML114_Page" = None):
        self.group = group
        self.YasperEPNML114_NetGraphics58 = YasperEPNML114_NetGraphics58 if YasperEPNML114_NetGraphics58 is not None else set()
        self.YasperEPNML114_NetGraphics = YasperEPNML114_NetGraphics
        self.YasperEPNML114_NetGraphics55 = YasperEPNML114_NetGraphics55 if YasperEPNML114_NetGraphics55 is not None else set()
        self.YasperEPNML114_NetGraphics69 = YasperEPNML114_NetGraphics69
        
        pass
    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group


    @property
    def YasperEPNML114_NetGraphics(self):
        return self.__YasperEPNML114_NetGraphics

    @YasperEPNML114_NetGraphics.setter
    def YasperEPNML114_NetGraphics(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_NetGraphics__YasperEPNML114_NetGraphics", None)
        self.__YasperEPNML114_NetGraphics = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Net"):
                opp_val = getattr(old_value, "YasperEPNML114_Net", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Net"):
                opp_val = getattr(value, "YasperEPNML114_Net", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_Net", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_NetGraphics58(self):
        return self.__YasperEPNML114_NetGraphics58

    @YasperEPNML114_NetGraphics58.setter
    def YasperEPNML114_NetGraphics58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_NetGraphics__YasperEPNML114_NetGraphics58", None)
        self.__YasperEPNML114_NetGraphics58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_TwoDimVector59"):
                    opp_val = getattr(item, "YasperEPNML114_TwoDimVector59", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_TwoDimVector59", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_TwoDimVector59"):
                    opp_val = getattr(item, "YasperEPNML114_TwoDimVector59", None)
                    
                    setattr(item, "YasperEPNML114_TwoDimVector59", self)
                    

    @property
    def YasperEPNML114_NetGraphics69(self):
        return self.__YasperEPNML114_NetGraphics69

    @YasperEPNML114_NetGraphics69.setter
    def YasperEPNML114_NetGraphics69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_NetGraphics__YasperEPNML114_NetGraphics69", None)
        self.__YasperEPNML114_NetGraphics69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Page68"):
                opp_val = getattr(old_value, "YasperEPNML114_Page68", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Page68"):
                opp_val = getattr(value, "YasperEPNML114_Page68", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_Page68", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_NetGraphics55(self):
        return self.__YasperEPNML114_NetGraphics55

    @YasperEPNML114_NetGraphics55.setter
    def YasperEPNML114_NetGraphics55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_NetGraphics__YasperEPNML114_NetGraphics55", None)
        self.__YasperEPNML114_NetGraphics55 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_TwoDimVector56"):
                    opp_val = getattr(item, "YasperEPNML114_TwoDimVector56", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_TwoDimVector56", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_TwoDimVector56"):
                    opp_val = getattr(item, "YasperEPNML114_TwoDimVector56", None)
                    
                    setattr(item, "YasperEPNML114_TwoDimVector56", self)
                    

class YasperEPNML114_InitialMarking:

    def __init__(self, text: str, YasperEPNML114_InitialMarking: "YasperEPNML114_AnnotationGraphics" = None, YasperEPNML114_InitialMarking99: "YasperEPNML114_Place" = None):
        self.text = text
        self.YasperEPNML114_InitialMarking = YasperEPNML114_InitialMarking
        self.YasperEPNML114_InitialMarking99 = YasperEPNML114_InitialMarking99
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def YasperEPNML114_InitialMarking(self):
        return self.__YasperEPNML114_InitialMarking

    @YasperEPNML114_InitialMarking.setter
    def YasperEPNML114_InitialMarking(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_InitialMarking__YasperEPNML114_InitialMarking", None)
        self.__YasperEPNML114_InitialMarking = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_AnnotationGraphics31"):
                opp_val = getattr(old_value, "YasperEPNML114_AnnotationGraphics31", None)
                if opp_val == self:
                    setattr(old_value, "YasperEPNML114_AnnotationGraphics31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_AnnotationGraphics31"):
                opp_val = getattr(value, "YasperEPNML114_AnnotationGraphics31", None)
                setattr(value, "YasperEPNML114_AnnotationGraphics31", self)

    @property
    def YasperEPNML114_InitialMarking99(self):
        return self.__YasperEPNML114_InitialMarking99

    @YasperEPNML114_InitialMarking99.setter
    def YasperEPNML114_InitialMarking99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_InitialMarking__YasperEPNML114_InitialMarking99", None)
        self.__YasperEPNML114_InitialMarking99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Place98"):
                opp_val = getattr(old_value, "YasperEPNML114_Place98", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Place98"):
                opp_val = getattr(value, "YasperEPNML114_Place98", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_Place98", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class YasperEPNML114_DocumentRoot:

    def __init__(self, mixed: str, YasperEPNML114_DocumentRoot: set["YasperEPNML114_EStringToStringMapEntry"] = None, YasperEPNML114_DocumentRoot23: set["YasperEPNML114_EStringToStringMapEntry"] = None, YasperEPNML114_DocumentRoot26: set["YasperEPNML114_Pnml"] = None):
        self.mixed = mixed
        self.YasperEPNML114_DocumentRoot = YasperEPNML114_DocumentRoot if YasperEPNML114_DocumentRoot is not None else set()
        self.YasperEPNML114_DocumentRoot23 = YasperEPNML114_DocumentRoot23 if YasperEPNML114_DocumentRoot23 is not None else set()
        self.YasperEPNML114_DocumentRoot26 = YasperEPNML114_DocumentRoot26 if YasperEPNML114_DocumentRoot26 is not None else set()
        
        pass
    @property
    def mixed(self):
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed


    @property
    def YasperEPNML114_DocumentRoot23(self):
        return self.__YasperEPNML114_DocumentRoot23

    @YasperEPNML114_DocumentRoot23.setter
    def YasperEPNML114_DocumentRoot23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_DocumentRoot__YasperEPNML114_DocumentRoot23", None)
        self.__YasperEPNML114_DocumentRoot23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_EStringToStringMapEntry24"):
                    opp_val = getattr(item, "YasperEPNML114_EStringToStringMapEntry24", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_EStringToStringMapEntry24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_EStringToStringMapEntry24"):
                    opp_val = getattr(item, "YasperEPNML114_EStringToStringMapEntry24", None)
                    
                    setattr(item, "YasperEPNML114_EStringToStringMapEntry24", self)
                    

    @property
    def YasperEPNML114_DocumentRoot(self):
        return self.__YasperEPNML114_DocumentRoot

    @YasperEPNML114_DocumentRoot.setter
    def YasperEPNML114_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_DocumentRoot__YasperEPNML114_DocumentRoot", None)
        self.__YasperEPNML114_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_EStringToStringMapEntry"):
                    opp_val = getattr(item, "YasperEPNML114_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_EStringToStringMapEntry"):
                    opp_val = getattr(item, "YasperEPNML114_EStringToStringMapEntry", None)
                    
                    setattr(item, "YasperEPNML114_EStringToStringMapEntry", self)
                    

    @property
    def YasperEPNML114_DocumentRoot26(self):
        return self.__YasperEPNML114_DocumentRoot26

    @YasperEPNML114_DocumentRoot26.setter
    def YasperEPNML114_DocumentRoot26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_DocumentRoot__YasperEPNML114_DocumentRoot26", None)
        self.__YasperEPNML114_DocumentRoot26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_Pnml"):
                    opp_val = getattr(item, "YasperEPNML114_Pnml", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_Pnml", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_Pnml"):
                    opp_val = getattr(item, "YasperEPNML114_Pnml", None)
                    
                    setattr(item, "YasperEPNML114_Pnml", self)
                    

class YasperEPNML114_Cost:

    pass
class YasperEPNML114_Pnml:

    def __init__(self, group: str, YasperEPNML114_Pnml: "YasperEPNML114_DocumentRoot" = None, YasperEPNML114_Pnml110: set["YasperEPNML114_Net"] = None, YasperEPNML114_Pnml113: set["YasperEPNML114_ToolspecificType"] = None):
        self.group = group
        self.YasperEPNML114_Pnml = YasperEPNML114_Pnml
        self.YasperEPNML114_Pnml110 = YasperEPNML114_Pnml110 if YasperEPNML114_Pnml110 is not None else set()
        self.YasperEPNML114_Pnml113 = YasperEPNML114_Pnml113 if YasperEPNML114_Pnml113 is not None else set()
        
        pass
    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group


    @property
    def YasperEPNML114_Pnml(self):
        return self.__YasperEPNML114_Pnml

    @YasperEPNML114_Pnml.setter
    def YasperEPNML114_Pnml(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Pnml__YasperEPNML114_Pnml", None)
        self.__YasperEPNML114_Pnml = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_DocumentRoot26"):
                opp_val = getattr(old_value, "YasperEPNML114_DocumentRoot26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_DocumentRoot26"):
                opp_val = getattr(value, "YasperEPNML114_DocumentRoot26", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_DocumentRoot26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_Pnml113(self):
        return self.__YasperEPNML114_Pnml113

    @YasperEPNML114_Pnml113.setter
    def YasperEPNML114_Pnml113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Pnml__YasperEPNML114_Pnml113", None)
        self.__YasperEPNML114_Pnml113 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_ToolspecificType114"):
                    opp_val = getattr(item, "YasperEPNML114_ToolspecificType114", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_ToolspecificType114", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_ToolspecificType114"):
                    opp_val = getattr(item, "YasperEPNML114_ToolspecificType114", None)
                    
                    setattr(item, "YasperEPNML114_ToolspecificType114", self)
                    

    @property
    def YasperEPNML114_Pnml110(self):
        return self.__YasperEPNML114_Pnml110

    @YasperEPNML114_Pnml110.setter
    def YasperEPNML114_Pnml110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Pnml__YasperEPNML114_Pnml110", None)
        self.__YasperEPNML114_Pnml110 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_Net111"):
                    opp_val = getattr(item, "YasperEPNML114_Net111", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_Net111", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_Net111"):
                    opp_val = getattr(item, "YasperEPNML114_Net111", None)
                    
                    setattr(item, "YasperEPNML114_Net111", self)
                    

class YasperEPNML114_EStringToStringMapEntry:

    pass
class YasperEPNML114_ConnectionWeight:

    def __init__(self, connection: str, YasperEPNML114_ConnectionWeight: "YasperEPNML114_Stat" = None, YasperEPNML114_ConnectionWeight15: "YasperEPNML114_ConnectionWeights" = None):
        self.connection = connection
        self.YasperEPNML114_ConnectionWeight = YasperEPNML114_ConnectionWeight
        self.YasperEPNML114_ConnectionWeight15 = YasperEPNML114_ConnectionWeight15
        
        pass
    @property
    def connection(self):
        return self.__connection

    @connection.setter
    def connection(self, connection: str):
        self.__connection = connection


    @property
    def YasperEPNML114_ConnectionWeight(self):
        return self.__YasperEPNML114_ConnectionWeight

    @YasperEPNML114_ConnectionWeight.setter
    def YasperEPNML114_ConnectionWeight(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_ConnectionWeight__YasperEPNML114_ConnectionWeight", None)
        self.__YasperEPNML114_ConnectionWeight = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Stat"):
                opp_val = getattr(old_value, "YasperEPNML114_Stat", None)
                if opp_val == self:
                    setattr(old_value, "YasperEPNML114_Stat", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Stat"):
                opp_val = getattr(value, "YasperEPNML114_Stat", None)
                setattr(value, "YasperEPNML114_Stat", self)

    @property
    def YasperEPNML114_ConnectionWeight15(self):
        return self.__YasperEPNML114_ConnectionWeight15

    @YasperEPNML114_ConnectionWeight15.setter
    def YasperEPNML114_ConnectionWeight15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_ConnectionWeight__YasperEPNML114_ConnectionWeight15", None)
        self.__YasperEPNML114_ConnectionWeight15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_ConnectionWeights"):
                opp_val = getattr(old_value, "YasperEPNML114_ConnectionWeights", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_ConnectionWeights"):
                opp_val = getattr(value, "YasperEPNML114_ConnectionWeights", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_ConnectionWeights", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class YasperEPNML114_ConnectionWeights:

    pass
class YasperEPNML114_Stat:

    def __init__(self, text: str, YasperEPNML114_Stat: "YasperEPNML114_ConnectionWeight" = None, YasperEPNML114_Stat17: "YasperEPNML114_Cost" = None, YasperEPNML114_Stat20: "YasperEPNML114_Cost" = None, YasperEPNML114_Stat119: "YasperEPNML114_ProcessingTime" = None, YasperEPNML114_Stat122: "YasperEPNML114_ProcessingTime" = None):
        self.text = text
        self.YasperEPNML114_Stat = YasperEPNML114_Stat
        self.YasperEPNML114_Stat17 = YasperEPNML114_Stat17
        self.YasperEPNML114_Stat20 = YasperEPNML114_Stat20
        self.YasperEPNML114_Stat119 = YasperEPNML114_Stat119
        self.YasperEPNML114_Stat122 = YasperEPNML114_Stat122
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def YasperEPNML114_Stat20(self):
        return self.__YasperEPNML114_Stat20

    @YasperEPNML114_Stat20.setter
    def YasperEPNML114_Stat20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Stat__YasperEPNML114_Stat20", None)
        self.__YasperEPNML114_Stat20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Cost19"):
                opp_val = getattr(old_value, "YasperEPNML114_Cost19", None)
                if opp_val == self:
                    setattr(old_value, "YasperEPNML114_Cost19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Cost19"):
                opp_val = getattr(value, "YasperEPNML114_Cost19", None)
                setattr(value, "YasperEPNML114_Cost19", self)

    @property
    def YasperEPNML114_Stat122(self):
        return self.__YasperEPNML114_Stat122

    @YasperEPNML114_Stat122.setter
    def YasperEPNML114_Stat122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Stat__YasperEPNML114_Stat122", None)
        self.__YasperEPNML114_Stat122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_ProcessingTime121"):
                opp_val = getattr(old_value, "YasperEPNML114_ProcessingTime121", None)
                if opp_val == self:
                    setattr(old_value, "YasperEPNML114_ProcessingTime121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_ProcessingTime121"):
                opp_val = getattr(value, "YasperEPNML114_ProcessingTime121", None)
                setattr(value, "YasperEPNML114_ProcessingTime121", self)

    @property
    def YasperEPNML114_Stat(self):
        return self.__YasperEPNML114_Stat

    @YasperEPNML114_Stat.setter
    def YasperEPNML114_Stat(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Stat__YasperEPNML114_Stat", None)
        self.__YasperEPNML114_Stat = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_ConnectionWeight"):
                opp_val = getattr(old_value, "YasperEPNML114_ConnectionWeight", None)
                if opp_val == self:
                    setattr(old_value, "YasperEPNML114_ConnectionWeight", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_ConnectionWeight"):
                opp_val = getattr(value, "YasperEPNML114_ConnectionWeight", None)
                setattr(value, "YasperEPNML114_ConnectionWeight", self)

    @property
    def YasperEPNML114_Stat119(self):
        return self.__YasperEPNML114_Stat119

    @YasperEPNML114_Stat119.setter
    def YasperEPNML114_Stat119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Stat__YasperEPNML114_Stat119", None)
        self.__YasperEPNML114_Stat119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_ProcessingTime"):
                opp_val = getattr(old_value, "YasperEPNML114_ProcessingTime", None)
                if opp_val == self:
                    setattr(old_value, "YasperEPNML114_ProcessingTime", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_ProcessingTime"):
                opp_val = getattr(value, "YasperEPNML114_ProcessingTime", None)
                setattr(value, "YasperEPNML114_ProcessingTime", self)

    @property
    def YasperEPNML114_Stat17(self):
        return self.__YasperEPNML114_Stat17

    @YasperEPNML114_Stat17.setter
    def YasperEPNML114_Stat17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Stat__YasperEPNML114_Stat17", None)
        self.__YasperEPNML114_Stat17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Cost"):
                opp_val = getattr(old_value, "YasperEPNML114_Cost", None)
                if opp_val == self:
                    setattr(old_value, "YasperEPNML114_Cost", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Cost"):
                opp_val = getattr(value, "YasperEPNML114_Cost", None)
                setattr(value, "YasperEPNML114_Cost", self)

class YasperEPNML114_PnmlAnnotation:

    def __init__(self, text: str, YasperEPNML114_PnmlAnnotation10: "YasperEPNML114_Arc" = None, YasperEPNML114_PnmlAnnotation: "YasperEPNML114_Arc" = None, YasperEPNML114_PnmlAnnotation47: "YasperEPNML114_Net" = None, YasperEPNML114_PnmlAnnotation50: "YasperEPNML114_Net" = None, YasperEPNML114_PnmlAnnotation86: "YasperEPNML114_Page" = None, YasperEPNML114_PnmlAnnotation89: "YasperEPNML114_Page" = None, YasperEPNML114_PnmlAnnotation102: "YasperEPNML114_Place" = None, YasperEPNML114_PnmlAnnotation105: "YasperEPNML114_Place" = None, YasperEPNML114_PnmlAnnotation116: "YasperEPNML114_AnnotationGraphics" = None, YasperEPNML114_PnmlAnnotation131: "YasperEPNML114_ReferencePlace" = None, YasperEPNML114_PnmlAnnotation128: "YasperEPNML114_ReferencePlace" = None, YasperEPNML114_PnmlAnnotation151: "YasperEPNML114_Transition" = None, YasperEPNML114_PnmlAnnotation154: "YasperEPNML114_Transition" = None):
        self.text = text
        self.YasperEPNML114_PnmlAnnotation10 = YasperEPNML114_PnmlAnnotation10
        self.YasperEPNML114_PnmlAnnotation = YasperEPNML114_PnmlAnnotation
        self.YasperEPNML114_PnmlAnnotation47 = YasperEPNML114_PnmlAnnotation47
        self.YasperEPNML114_PnmlAnnotation50 = YasperEPNML114_PnmlAnnotation50
        self.YasperEPNML114_PnmlAnnotation86 = YasperEPNML114_PnmlAnnotation86
        self.YasperEPNML114_PnmlAnnotation89 = YasperEPNML114_PnmlAnnotation89
        self.YasperEPNML114_PnmlAnnotation102 = YasperEPNML114_PnmlAnnotation102
        self.YasperEPNML114_PnmlAnnotation105 = YasperEPNML114_PnmlAnnotation105
        self.YasperEPNML114_PnmlAnnotation116 = YasperEPNML114_PnmlAnnotation116
        self.YasperEPNML114_PnmlAnnotation131 = YasperEPNML114_PnmlAnnotation131
        self.YasperEPNML114_PnmlAnnotation128 = YasperEPNML114_PnmlAnnotation128
        self.YasperEPNML114_PnmlAnnotation151 = YasperEPNML114_PnmlAnnotation151
        self.YasperEPNML114_PnmlAnnotation154 = YasperEPNML114_PnmlAnnotation154
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def YasperEPNML114_PnmlAnnotation(self):
        return self.__YasperEPNML114_PnmlAnnotation

    @YasperEPNML114_PnmlAnnotation.setter
    def YasperEPNML114_PnmlAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_PnmlAnnotation__YasperEPNML114_PnmlAnnotation", None)
        self.__YasperEPNML114_PnmlAnnotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Arc7"):
                opp_val = getattr(old_value, "YasperEPNML114_Arc7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Arc7"):
                opp_val = getattr(value, "YasperEPNML114_Arc7", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_Arc7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_PnmlAnnotation10(self):
        return self.__YasperEPNML114_PnmlAnnotation10

    @YasperEPNML114_PnmlAnnotation10.setter
    def YasperEPNML114_PnmlAnnotation10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_PnmlAnnotation__YasperEPNML114_PnmlAnnotation10", None)
        self.__YasperEPNML114_PnmlAnnotation10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Arc9"):
                opp_val = getattr(old_value, "YasperEPNML114_Arc9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Arc9"):
                opp_val = getattr(value, "YasperEPNML114_Arc9", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_Arc9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_PnmlAnnotation47(self):
        return self.__YasperEPNML114_PnmlAnnotation47

    @YasperEPNML114_PnmlAnnotation47.setter
    def YasperEPNML114_PnmlAnnotation47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_PnmlAnnotation__YasperEPNML114_PnmlAnnotation47", None)
        self.__YasperEPNML114_PnmlAnnotation47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Net46"):
                opp_val = getattr(old_value, "YasperEPNML114_Net46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Net46"):
                opp_val = getattr(value, "YasperEPNML114_Net46", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_Net46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_PnmlAnnotation151(self):
        return self.__YasperEPNML114_PnmlAnnotation151

    @YasperEPNML114_PnmlAnnotation151.setter
    def YasperEPNML114_PnmlAnnotation151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_PnmlAnnotation__YasperEPNML114_PnmlAnnotation151", None)
        self.__YasperEPNML114_PnmlAnnotation151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Transition150"):
                opp_val = getattr(old_value, "YasperEPNML114_Transition150", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Transition150"):
                opp_val = getattr(value, "YasperEPNML114_Transition150", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_Transition150", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_PnmlAnnotation116(self):
        return self.__YasperEPNML114_PnmlAnnotation116

    @YasperEPNML114_PnmlAnnotation116.setter
    def YasperEPNML114_PnmlAnnotation116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_PnmlAnnotation__YasperEPNML114_PnmlAnnotation116", None)
        self.__YasperEPNML114_PnmlAnnotation116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_AnnotationGraphics117"):
                opp_val = getattr(old_value, "YasperEPNML114_AnnotationGraphics117", None)
                if opp_val == self:
                    setattr(old_value, "YasperEPNML114_AnnotationGraphics117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_AnnotationGraphics117"):
                opp_val = getattr(value, "YasperEPNML114_AnnotationGraphics117", None)
                setattr(value, "YasperEPNML114_AnnotationGraphics117", self)

    @property
    def YasperEPNML114_PnmlAnnotation89(self):
        return self.__YasperEPNML114_PnmlAnnotation89

    @YasperEPNML114_PnmlAnnotation89.setter
    def YasperEPNML114_PnmlAnnotation89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_PnmlAnnotation__YasperEPNML114_PnmlAnnotation89", None)
        self.__YasperEPNML114_PnmlAnnotation89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Page88"):
                opp_val = getattr(old_value, "YasperEPNML114_Page88", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Page88"):
                opp_val = getattr(value, "YasperEPNML114_Page88", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_Page88", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_PnmlAnnotation154(self):
        return self.__YasperEPNML114_PnmlAnnotation154

    @YasperEPNML114_PnmlAnnotation154.setter
    def YasperEPNML114_PnmlAnnotation154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_PnmlAnnotation__YasperEPNML114_PnmlAnnotation154", None)
        self.__YasperEPNML114_PnmlAnnotation154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Transition153"):
                opp_val = getattr(old_value, "YasperEPNML114_Transition153", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Transition153"):
                opp_val = getattr(value, "YasperEPNML114_Transition153", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_Transition153", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_PnmlAnnotation131(self):
        return self.__YasperEPNML114_PnmlAnnotation131

    @YasperEPNML114_PnmlAnnotation131.setter
    def YasperEPNML114_PnmlAnnotation131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_PnmlAnnotation__YasperEPNML114_PnmlAnnotation131", None)
        self.__YasperEPNML114_PnmlAnnotation131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_ReferencePlace130"):
                opp_val = getattr(old_value, "YasperEPNML114_ReferencePlace130", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_ReferencePlace130"):
                opp_val = getattr(value, "YasperEPNML114_ReferencePlace130", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_ReferencePlace130", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_PnmlAnnotation50(self):
        return self.__YasperEPNML114_PnmlAnnotation50

    @YasperEPNML114_PnmlAnnotation50.setter
    def YasperEPNML114_PnmlAnnotation50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_PnmlAnnotation__YasperEPNML114_PnmlAnnotation50", None)
        self.__YasperEPNML114_PnmlAnnotation50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Net49"):
                opp_val = getattr(old_value, "YasperEPNML114_Net49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Net49"):
                opp_val = getattr(value, "YasperEPNML114_Net49", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_Net49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_PnmlAnnotation105(self):
        return self.__YasperEPNML114_PnmlAnnotation105

    @YasperEPNML114_PnmlAnnotation105.setter
    def YasperEPNML114_PnmlAnnotation105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_PnmlAnnotation__YasperEPNML114_PnmlAnnotation105", None)
        self.__YasperEPNML114_PnmlAnnotation105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Place104"):
                opp_val = getattr(old_value, "YasperEPNML114_Place104", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Place104"):
                opp_val = getattr(value, "YasperEPNML114_Place104", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_Place104", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_PnmlAnnotation86(self):
        return self.__YasperEPNML114_PnmlAnnotation86

    @YasperEPNML114_PnmlAnnotation86.setter
    def YasperEPNML114_PnmlAnnotation86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_PnmlAnnotation__YasperEPNML114_PnmlAnnotation86", None)
        self.__YasperEPNML114_PnmlAnnotation86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Page85"):
                opp_val = getattr(old_value, "YasperEPNML114_Page85", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Page85"):
                opp_val = getattr(value, "YasperEPNML114_Page85", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_Page85", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_PnmlAnnotation102(self):
        return self.__YasperEPNML114_PnmlAnnotation102

    @YasperEPNML114_PnmlAnnotation102.setter
    def YasperEPNML114_PnmlAnnotation102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_PnmlAnnotation__YasperEPNML114_PnmlAnnotation102", None)
        self.__YasperEPNML114_PnmlAnnotation102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Place101"):
                opp_val = getattr(old_value, "YasperEPNML114_Place101", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Place101"):
                opp_val = getattr(value, "YasperEPNML114_Place101", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_Place101", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_PnmlAnnotation128(self):
        return self.__YasperEPNML114_PnmlAnnotation128

    @YasperEPNML114_PnmlAnnotation128.setter
    def YasperEPNML114_PnmlAnnotation128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_PnmlAnnotation__YasperEPNML114_PnmlAnnotation128", None)
        self.__YasperEPNML114_PnmlAnnotation128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_ReferencePlace127"):
                opp_val = getattr(old_value, "YasperEPNML114_ReferencePlace127", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_ReferencePlace127"):
                opp_val = getattr(value, "YasperEPNML114_ReferencePlace127", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_ReferencePlace127", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class YasperEPNML114_Inscription:

    def __init__(self, text: str, YasperEPNML114_Inscription: "YasperEPNML114_Arc" = None, YasperEPNML114_Inscription33: "YasperEPNML114_AnnotationGraphics" = None):
        self.text = text
        self.YasperEPNML114_Inscription = YasperEPNML114_Inscription
        self.YasperEPNML114_Inscription33 = YasperEPNML114_Inscription33
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def YasperEPNML114_Inscription(self):
        return self.__YasperEPNML114_Inscription

    @YasperEPNML114_Inscription.setter
    def YasperEPNML114_Inscription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Inscription__YasperEPNML114_Inscription", None)
        self.__YasperEPNML114_Inscription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Arc5"):
                opp_val = getattr(old_value, "YasperEPNML114_Arc5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Arc5"):
                opp_val = getattr(value, "YasperEPNML114_Arc5", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_Arc5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_Inscription33(self):
        return self.__YasperEPNML114_Inscription33

    @YasperEPNML114_Inscription33.setter
    def YasperEPNML114_Inscription33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Inscription__YasperEPNML114_Inscription33", None)
        self.__YasperEPNML114_Inscription33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_AnnotationGraphics34"):
                opp_val = getattr(old_value, "YasperEPNML114_AnnotationGraphics34", None)
                if opp_val == self:
                    setattr(old_value, "YasperEPNML114_AnnotationGraphics34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_AnnotationGraphics34"):
                opp_val = getattr(value, "YasperEPNML114_AnnotationGraphics34", None)
                setattr(value, "YasperEPNML114_AnnotationGraphics34", self)

class YasperEPNML114_EdgeGraphics:

    pass
class YasperEPNML114_ToolspecificType:

    def __init__(self, mixed: str, group: str, any: str, tool: str, version: str, YasperEPNML114_ToolspecificType: "YasperEPNML114_Arc" = None, YasperEPNML114_ToolspecificType53: "YasperEPNML114_Net" = None, YasperEPNML114_ToolspecificType92: "YasperEPNML114_Page" = None, YasperEPNML114_ToolspecificType108: "YasperEPNML114_Place" = None, YasperEPNML114_ToolspecificType114: "YasperEPNML114_Pnml" = None, YasperEPNML114_ToolspecificType134: "YasperEPNML114_ReferencePlace" = None, YasperEPNML114_ToolspecificType157: "YasperEPNML114_Transition" = None):
        self.mixed = mixed
        self.group = group
        self.any = any
        self.tool = tool
        self.version = version
        self.YasperEPNML114_ToolspecificType = YasperEPNML114_ToolspecificType
        self.YasperEPNML114_ToolspecificType53 = YasperEPNML114_ToolspecificType53
        self.YasperEPNML114_ToolspecificType92 = YasperEPNML114_ToolspecificType92
        self.YasperEPNML114_ToolspecificType108 = YasperEPNML114_ToolspecificType108
        self.YasperEPNML114_ToolspecificType114 = YasperEPNML114_ToolspecificType114
        self.YasperEPNML114_ToolspecificType134 = YasperEPNML114_ToolspecificType134
        self.YasperEPNML114_ToolspecificType157 = YasperEPNML114_ToolspecificType157
        
        pass
    @property
    def any(self):
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any


    @property
    def tool(self):
        return self.__tool

    @tool.setter
    def tool(self, tool: str):
        self.__tool = tool


    @property
    def mixed(self):
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group


    @property
    def YasperEPNML114_ToolspecificType157(self):
        return self.__YasperEPNML114_ToolspecificType157

    @YasperEPNML114_ToolspecificType157.setter
    def YasperEPNML114_ToolspecificType157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_ToolspecificType__YasperEPNML114_ToolspecificType157", None)
        self.__YasperEPNML114_ToolspecificType157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Transition156"):
                opp_val = getattr(old_value, "YasperEPNML114_Transition156", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Transition156"):
                opp_val = getattr(value, "YasperEPNML114_Transition156", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_Transition156", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_ToolspecificType108(self):
        return self.__YasperEPNML114_ToolspecificType108

    @YasperEPNML114_ToolspecificType108.setter
    def YasperEPNML114_ToolspecificType108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_ToolspecificType__YasperEPNML114_ToolspecificType108", None)
        self.__YasperEPNML114_ToolspecificType108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Place107"):
                opp_val = getattr(old_value, "YasperEPNML114_Place107", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Place107"):
                opp_val = getattr(value, "YasperEPNML114_Place107", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_Place107", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_ToolspecificType53(self):
        return self.__YasperEPNML114_ToolspecificType53

    @YasperEPNML114_ToolspecificType53.setter
    def YasperEPNML114_ToolspecificType53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_ToolspecificType__YasperEPNML114_ToolspecificType53", None)
        self.__YasperEPNML114_ToolspecificType53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Net52"):
                opp_val = getattr(old_value, "YasperEPNML114_Net52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Net52"):
                opp_val = getattr(value, "YasperEPNML114_Net52", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_Net52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_ToolspecificType(self):
        return self.__YasperEPNML114_ToolspecificType

    @YasperEPNML114_ToolspecificType.setter
    def YasperEPNML114_ToolspecificType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_ToolspecificType__YasperEPNML114_ToolspecificType", None)
        self.__YasperEPNML114_ToolspecificType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Arc12"):
                opp_val = getattr(old_value, "YasperEPNML114_Arc12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Arc12"):
                opp_val = getattr(value, "YasperEPNML114_Arc12", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_Arc12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_ToolspecificType134(self):
        return self.__YasperEPNML114_ToolspecificType134

    @YasperEPNML114_ToolspecificType134.setter
    def YasperEPNML114_ToolspecificType134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_ToolspecificType__YasperEPNML114_ToolspecificType134", None)
        self.__YasperEPNML114_ToolspecificType134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_ReferencePlace133"):
                opp_val = getattr(old_value, "YasperEPNML114_ReferencePlace133", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_ReferencePlace133"):
                opp_val = getattr(value, "YasperEPNML114_ReferencePlace133", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_ReferencePlace133", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_ToolspecificType114(self):
        return self.__YasperEPNML114_ToolspecificType114

    @YasperEPNML114_ToolspecificType114.setter
    def YasperEPNML114_ToolspecificType114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_ToolspecificType__YasperEPNML114_ToolspecificType114", None)
        self.__YasperEPNML114_ToolspecificType114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Pnml113"):
                opp_val = getattr(old_value, "YasperEPNML114_Pnml113", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Pnml113"):
                opp_val = getattr(value, "YasperEPNML114_Pnml113", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_Pnml113", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_ToolspecificType92(self):
        return self.__YasperEPNML114_ToolspecificType92

    @YasperEPNML114_ToolspecificType92.setter
    def YasperEPNML114_ToolspecificType92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_ToolspecificType__YasperEPNML114_ToolspecificType92", None)
        self.__YasperEPNML114_ToolspecificType92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Page91"):
                opp_val = getattr(old_value, "YasperEPNML114_Page91", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Page91"):
                opp_val = getattr(value, "YasperEPNML114_Page91", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_Page91", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class YasperEPNML114_TwoDimVector:

    def __init__(self, x: str, y: str, YasperEPNML114_TwoDimVector59: "YasperEPNML114_NetGraphics" = None, YasperEPNML114_TwoDimVector61: "YasperEPNML114_NodeGraphics" = None, YasperEPNML114_TwoDimVector64: "YasperEPNML114_NodeGraphics" = None, YasperEPNML114_TwoDimVector: "YasperEPNML114_AnnotationGraphics" = None, YasperEPNML114_TwoDimVector29: "YasperEPNML114_EdgeGraphics" = None, YasperEPNML114_TwoDimVector56: "YasperEPNML114_NetGraphics" = None):
        self.x = x
        self.y = y
        self.YasperEPNML114_TwoDimVector59 = YasperEPNML114_TwoDimVector59
        self.YasperEPNML114_TwoDimVector61 = YasperEPNML114_TwoDimVector61
        self.YasperEPNML114_TwoDimVector64 = YasperEPNML114_TwoDimVector64
        self.YasperEPNML114_TwoDimVector = YasperEPNML114_TwoDimVector
        self.YasperEPNML114_TwoDimVector29 = YasperEPNML114_TwoDimVector29
        self.YasperEPNML114_TwoDimVector56 = YasperEPNML114_TwoDimVector56
        
        pass
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y


    @property
    def YasperEPNML114_TwoDimVector64(self):
        return self.__YasperEPNML114_TwoDimVector64

    @YasperEPNML114_TwoDimVector64.setter
    def YasperEPNML114_TwoDimVector64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_TwoDimVector__YasperEPNML114_TwoDimVector64", None)
        self.__YasperEPNML114_TwoDimVector64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_NodeGraphics63"):
                opp_val = getattr(old_value, "YasperEPNML114_NodeGraphics63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_NodeGraphics63"):
                opp_val = getattr(value, "YasperEPNML114_NodeGraphics63", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_NodeGraphics63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_TwoDimVector29(self):
        return self.__YasperEPNML114_TwoDimVector29

    @YasperEPNML114_TwoDimVector29.setter
    def YasperEPNML114_TwoDimVector29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_TwoDimVector__YasperEPNML114_TwoDimVector29", None)
        self.__YasperEPNML114_TwoDimVector29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_EdgeGraphics28"):
                opp_val = getattr(old_value, "YasperEPNML114_EdgeGraphics28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_EdgeGraphics28"):
                opp_val = getattr(value, "YasperEPNML114_EdgeGraphics28", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_EdgeGraphics28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_TwoDimVector(self):
        return self.__YasperEPNML114_TwoDimVector

    @YasperEPNML114_TwoDimVector.setter
    def YasperEPNML114_TwoDimVector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_TwoDimVector__YasperEPNML114_TwoDimVector", None)
        self.__YasperEPNML114_TwoDimVector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_AnnotationGraphics"):
                opp_val = getattr(old_value, "YasperEPNML114_AnnotationGraphics", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_AnnotationGraphics"):
                opp_val = getattr(value, "YasperEPNML114_AnnotationGraphics", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_AnnotationGraphics", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_TwoDimVector59(self):
        return self.__YasperEPNML114_TwoDimVector59

    @YasperEPNML114_TwoDimVector59.setter
    def YasperEPNML114_TwoDimVector59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_TwoDimVector__YasperEPNML114_TwoDimVector59", None)
        self.__YasperEPNML114_TwoDimVector59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_NetGraphics58"):
                opp_val = getattr(old_value, "YasperEPNML114_NetGraphics58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_NetGraphics58"):
                opp_val = getattr(value, "YasperEPNML114_NetGraphics58", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_NetGraphics58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_TwoDimVector56(self):
        return self.__YasperEPNML114_TwoDimVector56

    @YasperEPNML114_TwoDimVector56.setter
    def YasperEPNML114_TwoDimVector56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_TwoDimVector__YasperEPNML114_TwoDimVector56", None)
        self.__YasperEPNML114_TwoDimVector56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_NetGraphics55"):
                opp_val = getattr(old_value, "YasperEPNML114_NetGraphics55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_NetGraphics55"):
                opp_val = getattr(value, "YasperEPNML114_NetGraphics55", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_NetGraphics55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_TwoDimVector61(self):
        return self.__YasperEPNML114_TwoDimVector61

    @YasperEPNML114_TwoDimVector61.setter
    def YasperEPNML114_TwoDimVector61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_TwoDimVector__YasperEPNML114_TwoDimVector61", None)
        self.__YasperEPNML114_TwoDimVector61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_NodeGraphics"):
                opp_val = getattr(old_value, "YasperEPNML114_NodeGraphics", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_NodeGraphics"):
                opp_val = getattr(value, "YasperEPNML114_NodeGraphics", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_NodeGraphics", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class YasperEPNML114_AnnotationGraphics:

    pass
class YasperEPNML114_ArcType:

    def __init__(self, text: str, YasperEPNML114_ArcType: "YasperEPNML114_Arc" = None):
        self.text = text
        self.YasperEPNML114_ArcType = YasperEPNML114_ArcType
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def YasperEPNML114_ArcType(self):
        return self.__YasperEPNML114_ArcType

    @YasperEPNML114_ArcType.setter
    def YasperEPNML114_ArcType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_ArcType__YasperEPNML114_ArcType", None)
        self.__YasperEPNML114_ArcType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Arc"):
                opp_val = getattr(old_value, "YasperEPNML114_Arc", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Arc"):
                opp_val = getattr(value, "YasperEPNML114_Arc", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_Arc", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class YasperEPNML114_Arc:

    def __init__(self, group: str, id: str, source: str, target: str, YasperEPNML114_Arc: set["YasperEPNML114_ArcType"] = None, YasperEPNML114_Arc9: set["YasperEPNML114_PnmlAnnotation"] = None, YasperEPNML114_Arc12: set["YasperEPNML114_ToolspecificType"] = None, YasperEPNML114_Arc3: set["YasperEPNML114_EdgeGraphics"] = None, YasperEPNML114_Arc5: set["YasperEPNML114_Inscription"] = None, YasperEPNML114_Arc7: set["YasperEPNML114_PnmlAnnotation"] = None, YasperEPNML114_Arc42: "YasperEPNML114_Net" = None, YasperEPNML114_Arc80: "YasperEPNML114_Page" = None):
        self.group = group
        self.id = id
        self.source = source
        self.target = target
        self.YasperEPNML114_Arc = YasperEPNML114_Arc if YasperEPNML114_Arc is not None else set()
        self.YasperEPNML114_Arc9 = YasperEPNML114_Arc9 if YasperEPNML114_Arc9 is not None else set()
        self.YasperEPNML114_Arc12 = YasperEPNML114_Arc12 if YasperEPNML114_Arc12 is not None else set()
        self.YasperEPNML114_Arc3 = YasperEPNML114_Arc3 if YasperEPNML114_Arc3 is not None else set()
        self.YasperEPNML114_Arc5 = YasperEPNML114_Arc5 if YasperEPNML114_Arc5 is not None else set()
        self.YasperEPNML114_Arc7 = YasperEPNML114_Arc7 if YasperEPNML114_Arc7 is not None else set()
        self.YasperEPNML114_Arc42 = YasperEPNML114_Arc42
        self.YasperEPNML114_Arc80 = YasperEPNML114_Arc80
        
        pass
    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target


    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group


    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def YasperEPNML114_Arc12(self):
        return self.__YasperEPNML114_Arc12

    @YasperEPNML114_Arc12.setter
    def YasperEPNML114_Arc12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Arc__YasperEPNML114_Arc12", None)
        self.__YasperEPNML114_Arc12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_ToolspecificType"):
                    opp_val = getattr(item, "YasperEPNML114_ToolspecificType", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_ToolspecificType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_ToolspecificType"):
                    opp_val = getattr(item, "YasperEPNML114_ToolspecificType", None)
                    
                    setattr(item, "YasperEPNML114_ToolspecificType", self)
                    

    @property
    def YasperEPNML114_Arc7(self):
        return self.__YasperEPNML114_Arc7

    @YasperEPNML114_Arc7.setter
    def YasperEPNML114_Arc7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Arc__YasperEPNML114_Arc7", None)
        self.__YasperEPNML114_Arc7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_PnmlAnnotation"):
                    opp_val = getattr(item, "YasperEPNML114_PnmlAnnotation", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_PnmlAnnotation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_PnmlAnnotation"):
                    opp_val = getattr(item, "YasperEPNML114_PnmlAnnotation", None)
                    
                    setattr(item, "YasperEPNML114_PnmlAnnotation", self)
                    

    @property
    def YasperEPNML114_Arc80(self):
        return self.__YasperEPNML114_Arc80

    @YasperEPNML114_Arc80.setter
    def YasperEPNML114_Arc80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Arc__YasperEPNML114_Arc80", None)
        self.__YasperEPNML114_Arc80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Page79"):
                opp_val = getattr(old_value, "YasperEPNML114_Page79", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Page79"):
                opp_val = getattr(value, "YasperEPNML114_Page79", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_Page79", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_Arc5(self):
        return self.__YasperEPNML114_Arc5

    @YasperEPNML114_Arc5.setter
    def YasperEPNML114_Arc5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Arc__YasperEPNML114_Arc5", None)
        self.__YasperEPNML114_Arc5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_Inscription"):
                    opp_val = getattr(item, "YasperEPNML114_Inscription", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_Inscription", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_Inscription"):
                    opp_val = getattr(item, "YasperEPNML114_Inscription", None)
                    
                    setattr(item, "YasperEPNML114_Inscription", self)
                    

    @property
    def YasperEPNML114_Arc3(self):
        return self.__YasperEPNML114_Arc3

    @YasperEPNML114_Arc3.setter
    def YasperEPNML114_Arc3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Arc__YasperEPNML114_Arc3", None)
        self.__YasperEPNML114_Arc3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_EdgeGraphics"):
                    opp_val = getattr(item, "YasperEPNML114_EdgeGraphics", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_EdgeGraphics", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_EdgeGraphics"):
                    opp_val = getattr(item, "YasperEPNML114_EdgeGraphics", None)
                    
                    setattr(item, "YasperEPNML114_EdgeGraphics", self)
                    

    @property
    def YasperEPNML114_Arc42(self):
        return self.__YasperEPNML114_Arc42

    @YasperEPNML114_Arc42.setter
    def YasperEPNML114_Arc42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Arc__YasperEPNML114_Arc42", None)
        self.__YasperEPNML114_Arc42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "YasperEPNML114_Net41"):
                opp_val = getattr(old_value, "YasperEPNML114_Net41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "YasperEPNML114_Net41"):
                opp_val = getattr(value, "YasperEPNML114_Net41", None)
                if opp_val is None:
                    setattr(value, "YasperEPNML114_Net41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def YasperEPNML114_Arc9(self):
        return self.__YasperEPNML114_Arc9

    @YasperEPNML114_Arc9.setter
    def YasperEPNML114_Arc9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Arc__YasperEPNML114_Arc9", None)
        self.__YasperEPNML114_Arc9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_PnmlAnnotation10"):
                    opp_val = getattr(item, "YasperEPNML114_PnmlAnnotation10", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_PnmlAnnotation10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_PnmlAnnotation10"):
                    opp_val = getattr(item, "YasperEPNML114_PnmlAnnotation10", None)
                    
                    setattr(item, "YasperEPNML114_PnmlAnnotation10", self)
                    

    @property
    def YasperEPNML114_Arc(self):
        return self.__YasperEPNML114_Arc

    @YasperEPNML114_Arc.setter
    def YasperEPNML114_Arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_YasperEPNML114_Arc__YasperEPNML114_Arc", None)
        self.__YasperEPNML114_Arc = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "YasperEPNML114_ArcType"):
                    opp_val = getattr(item, "YasperEPNML114_ArcType", None)
                    
                    if opp_val == self:
                        setattr(item, "YasperEPNML114_ArcType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "YasperEPNML114_ArcType"):
                    opp_val = getattr(item, "YasperEPNML114_ArcType", None)
                    
                    setattr(item, "YasperEPNML114_ArcType", self)
                    
