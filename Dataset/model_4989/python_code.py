from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class TriggerType(Enum):
    Rising = "Rising"
    Falling = "Falling"
    Either = "Either"
    FunctionCall = "FunctionCall"
class TagVisibility(Enum):
    Local = "Local"
    Scoped = "Scoped"
    Global = "Global"
class EnableStates(Enum):
    Held = "Held"
    Reset = "Reset"
    Inherit = "Inherit"


############################################
# Definition of Classes
############################################

class OutPort:

    pass
class simulink_State(OutPort):

    pass
class SimulinkReference:

    pass
class simulink_SimulinkReference(ABC):

    def __init__(self, name: str, qualifier: str, simulink_SimulinkReference: "simulink_SimulinkElement" = None):
        self.name = name
        self.qualifier = qualifier
        self.simulink_SimulinkReference = simulink_SimulinkReference
        
    @property
    def qualifier(self) -> str:
        return self.__qualifier

    @qualifier.setter
    def qualifier(self, qualifier: str):
        self.__qualifier = qualifier

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simulink_SimulinkReference(self):
        return self.__simulink_SimulinkReference

    @simulink_SimulinkReference.setter
    def simulink_SimulinkReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_SimulinkReference__simulink_SimulinkReference", None)
        self.__simulink_SimulinkReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simulink_SimulinkElement38"):
                opp_val = getattr(old_value, "simulink_SimulinkElement38", None)
                if opp_val == self:
                    setattr(old_value, "simulink_SimulinkElement38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simulink_SimulinkElement38"):
                opp_val = getattr(value, "simulink_SimulinkElement38", None)
                setattr(value, "simulink_SimulinkElement38", self)

    def getFQN(self) -> str:
        # TODO: Implement getFQN method
        pass

class InPortBlock:

    pass
class simulink_EnableBlock(InPortBlock):

    pass
class simulink_TriggerBlock(InPortBlock):

    pass
class PortBlock:

    pass
class simulink_InPortBlock(PortBlock):

    pass
class simulink_OutPortBlock(PortBlock):

    pass
class Connection:

    pass
class simulink_MultiConnection(Connection):

    pass
class Block:

    pass
class simulink_ModelReference(Block):

    pass
class simulink_VirtualBlock(Block):

    pass
class VirtualBlock:

    pass
class simulink_From(VirtualBlock):

    pass
class simulink_GotoTagVisibility(VirtualBlock):

    pass
class simulink_Goto(VirtualBlock):

    def __init__(self, tagVisibility: str, gotoTag: str, gotoBlock: set["simulink_From"] = None, Goto: "simulink_From" = None, simulink_Goto: "simulink_GotoTagVisibility" = None):
        self.tagVisibility = tagVisibility
        self.gotoTag = gotoTag
        self.gotoBlock = gotoBlock if gotoBlock is not None else set()
        self.Goto = Goto
        self.simulink_Goto = simulink_Goto
        
    @property
    def gotoTag(self) -> str:
        return self.__gotoTag

    @gotoTag.setter
    def gotoTag(self, gotoTag: str):
        self.__gotoTag = gotoTag

    @property
    def tagVisibility(self) -> str:
        return self.__tagVisibility

    @tagVisibility.setter
    def tagVisibility(self, tagVisibility: str):
        self.__tagVisibility = tagVisibility

    @property
    def gotoBlock(self):
        return self.__gotoBlock

    @gotoBlock.setter
    def gotoBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Goto__gotoBlock", None)
        self.__gotoBlock = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "From"):
                    opp_val = getattr(item, "From", None)
                    
                    if opp_val == self:
                        setattr(item, "From", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "From"):
                    opp_val = getattr(item, "From", None)
                    
                    setattr(item, "From", self)
                    

    @property
    def Goto(self):
        return self.__Goto

    @Goto.setter
    def Goto(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Goto__Goto", None)
        self.__Goto = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fromBlocks"):
                opp_val = getattr(old_value, "fromBlocks", None)
                if opp_val == self:
                    setattr(old_value, "fromBlocks", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fromBlocks"):
                opp_val = getattr(value, "fromBlocks", None)
                setattr(value, "fromBlocks", self)

    @property
    def simulink_Goto(self):
        return self.__simulink_Goto

    @simulink_Goto.setter
    def simulink_Goto(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Goto__simulink_Goto", None)
        self.__simulink_Goto = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simulink_GotoTagVisibility"):
                opp_val = getattr(old_value, "simulink_GotoTagVisibility", None)
                if opp_val == self:
                    setattr(old_value, "simulink_GotoTagVisibility", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simulink_GotoTagVisibility"):
                opp_val = getattr(value, "simulink_GotoTagVisibility", None)
                setattr(value, "simulink_GotoTagVisibility", self)

class simulink_BusSpecification(Block):

    pass
class simulink_BusSignalMapping:

    def __init__(self, mappingPath: str, incomplete: bool, BusSignalMapping: "simulink_BusSelector" = None, mappings: "simulink_BusSelector" = None, simulink_BusSignalMapping: "simulink_OutPort" = None, simulink_BusSignalMapping52: "simulink_OutPort" = None):
        self.mappingPath = mappingPath
        self.incomplete = incomplete
        self.BusSignalMapping = BusSignalMapping
        self.mappings = mappings
        self.simulink_BusSignalMapping = simulink_BusSignalMapping
        self.simulink_BusSignalMapping52 = simulink_BusSignalMapping52
        
    @property
    def incomplete(self) -> bool:
        return self.__incomplete

    @incomplete.setter
    def incomplete(self, incomplete: bool):
        self.__incomplete = incomplete

    @property
    def mappingPath(self) -> str:
        return self.__mappingPath

    @mappingPath.setter
    def mappingPath(self, mappingPath: str):
        self.__mappingPath = mappingPath

    @property
    def BusSignalMapping(self):
        return self.__BusSignalMapping

    @BusSignalMapping.setter
    def BusSignalMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_BusSignalMapping__BusSignalMapping", None)
        self.__BusSignalMapping = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selector"):
                opp_val = getattr(old_value, "selector", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selector"):
                opp_val = getattr(value, "selector", None)
                if opp_val is None:
                    setattr(value, "selector", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simulink_BusSignalMapping52(self):
        return self.__simulink_BusSignalMapping52

    @simulink_BusSignalMapping52.setter
    def simulink_BusSignalMapping52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_BusSignalMapping__simulink_BusSignalMapping52", None)
        self.__simulink_BusSignalMapping52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simulink_OutPort53"):
                opp_val = getattr(old_value, "simulink_OutPort53", None)
                if opp_val == self:
                    setattr(old_value, "simulink_OutPort53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simulink_OutPort53"):
                opp_val = getattr(value, "simulink_OutPort53", None)
                setattr(value, "simulink_OutPort53", self)

    @property
    def mappings(self):
        return self.__mappings

    @mappings.setter
    def mappings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_BusSignalMapping__mappings", None)
        self.__mappings = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BusSelector"):
                opp_val = getattr(old_value, "BusSelector", None)
                if opp_val == self:
                    setattr(old_value, "BusSelector", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BusSelector"):
                opp_val = getattr(value, "BusSelector", None)
                setattr(value, "BusSelector", self)

    @property
    def simulink_BusSignalMapping(self):
        return self.__simulink_BusSignalMapping

    @simulink_BusSignalMapping.setter
    def simulink_BusSignalMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_BusSignalMapping__simulink_BusSignalMapping", None)
        self.__simulink_BusSignalMapping = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simulink_OutPort50"):
                opp_val = getattr(old_value, "simulink_OutPort50", None)
                if opp_val == self:
                    setattr(old_value, "simulink_OutPort50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simulink_OutPort50"):
                opp_val = getattr(value, "simulink_OutPort50", None)
                setattr(value, "simulink_OutPort50", self)

class BusSpecification:

    pass
class simulink_BusCreator(BusSpecification):

    pass
class simulink_BusSelector(BusSpecification):

    def __init__(self, outputAsBus: bool, selector: set["simulink_BusSignalMapping"] = None, simulink_BusSelector: "simulink_BusSpecification" = None, BusSelector: "simulink_BusSignalMapping" = None):
        self.outputAsBus = outputAsBus
        self.selector = selector if selector is not None else set()
        self.simulink_BusSelector = simulink_BusSelector
        self.BusSelector = BusSelector
        
    @property
    def outputAsBus(self) -> bool:
        return self.__outputAsBus

    @outputAsBus.setter
    def outputAsBus(self, outputAsBus: bool):
        self.__outputAsBus = outputAsBus

    @property
    def selector(self):
        return self.__selector

    @selector.setter
    def selector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_BusSelector__selector", None)
        self.__selector = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BusSignalMapping"):
                    opp_val = getattr(item, "BusSignalMapping", None)
                    
                    if opp_val == self:
                        setattr(item, "BusSignalMapping", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BusSignalMapping"):
                    opp_val = getattr(item, "BusSignalMapping", None)
                    
                    setattr(item, "BusSignalMapping", self)
                    

    @property
    def simulink_BusSelector(self):
        return self.__simulink_BusSelector

    @simulink_BusSelector.setter
    def simulink_BusSelector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_BusSelector__simulink_BusSelector", None)
        self.__simulink_BusSelector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simulink_BusSpecification"):
                opp_val = getattr(old_value, "simulink_BusSpecification", None)
                if opp_val == self:
                    setattr(old_value, "simulink_BusSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simulink_BusSpecification"):
                opp_val = getattr(value, "simulink_BusSpecification", None)
                setattr(value, "simulink_BusSpecification", self)

    @property
    def BusSelector(self):
        return self.__BusSelector

    @BusSelector.setter
    def BusSelector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_BusSelector__BusSelector", None)
        self.__BusSelector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mappings"):
                opp_val = getattr(old_value, "mappings", None)
                if opp_val == self:
                    setattr(old_value, "mappings", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mappings"):
                opp_val = getattr(value, "mappings", None)
                setattr(value, "mappings", self)

class InPort:

    pass
class simulink_SingleConnection(Connection):

    pass
class Port:

    pass
class simulink_PortBlock(VirtualBlock):

    pass
class simulink_LibraryLinkReference(SimulinkReference):

    def __init__(self, disabled: bool, simulink_LibraryLinkReference: "simulink_Block" = None):
        self.disabled = disabled
        self.simulink_LibraryLinkReference = simulink_LibraryLinkReference
        
    @property
    def disabled(self) -> bool:
        return self.__disabled

    @disabled.setter
    def disabled(self, disabled: bool):
        self.__disabled = disabled

    @property
    def simulink_LibraryLinkReference(self):
        return self.__simulink_LibraryLinkReference

    @simulink_LibraryLinkReference.setter
    def simulink_LibraryLinkReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_LibraryLinkReference__simulink_LibraryLinkReference", None)
        self.__simulink_LibraryLinkReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simulink_Block16"):
                opp_val = getattr(old_value, "simulink_Block16", None)
                if opp_val == self:
                    setattr(old_value, "simulink_Block16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simulink_Block16"):
                opp_val = getattr(value, "simulink_Block16", None)
                setattr(value, "simulink_Block16", self)

class simulink_SubSystem(Block):

    def __init__(self, tag: str, SubSystem: "simulink_Block" = None, parent41: set["simulink_Block"] = None):
        self.tag = tag
        self.SubSystem = SubSystem
        self.parent41 = parent41 if parent41 is not None else set()
        
    @property
    def tag(self) -> str:
        return self.__tag

    @tag.setter
    def tag(self, tag: str):
        self.__tag = tag

    @property
    def SubSystem(self):
        return self.__SubSystem

    @SubSystem.setter
    def SubSystem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_SubSystem__SubSystem", None)
        self.__SubSystem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subBlocks"):
                opp_val = getattr(old_value, "subBlocks", None)
                if opp_val == self:
                    setattr(old_value, "subBlocks", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subBlocks"):
                opp_val = getattr(value, "subBlocks", None)
                setattr(value, "subBlocks", self)

    @property
    def parent41(self):
        return self.__parent41

    @parent41.setter
    def parent41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_SubSystem__parent41", None)
        self.__parent41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Block42"):
                    opp_val = getattr(item, "Block42", None)
                    
                    if opp_val == self:
                        setattr(item, "Block42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Block42"):
                    opp_val = getattr(item, "Block42", None)
                    
                    setattr(item, "Block42", self)
                    

class simulink_OutPort(Port):

    pass
class simulink_InPort(Port):

    pass
class simulink_Enable(InPort):

    def __init__(self, statesWhenEnabling: str, simulink_Enable: "simulink_Block" = None):
        self.statesWhenEnabling = statesWhenEnabling
        self.simulink_Enable = simulink_Enable
        
    @property
    def statesWhenEnabling(self) -> str:
        return self.__statesWhenEnabling

    @statesWhenEnabling.setter
    def statesWhenEnabling(self, statesWhenEnabling: str):
        self.__statesWhenEnabling = statesWhenEnabling

    @property
    def simulink_Enable(self):
        return self.__simulink_Enable

    @simulink_Enable.setter
    def simulink_Enable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Enable__simulink_Enable", None)
        self.__simulink_Enable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simulink_Block6"):
                opp_val = getattr(old_value, "simulink_Block6", None)
                if opp_val == self:
                    setattr(old_value, "simulink_Block6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simulink_Block6"):
                opp_val = getattr(value, "simulink_Block6", None)
                setattr(value, "simulink_Block6", self)

class simulink_Trigger(InPort):

    def __init__(self, triggerType: str, statesWhenEnabling: str, simulink_Trigger: "simulink_Block" = None):
        self.triggerType = triggerType
        self.statesWhenEnabling = statesWhenEnabling
        self.simulink_Trigger = simulink_Trigger
        
    @property
    def triggerType(self) -> str:
        return self.__triggerType

    @triggerType.setter
    def triggerType(self, triggerType: str):
        self.__triggerType = triggerType

    @property
    def statesWhenEnabling(self) -> str:
        return self.__statesWhenEnabling

    @statesWhenEnabling.setter
    def statesWhenEnabling(self, statesWhenEnabling: str):
        self.__statesWhenEnabling = statesWhenEnabling

    @property
    def simulink_Trigger(self):
        return self.__simulink_Trigger

    @simulink_Trigger.setter
    def simulink_Trigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Trigger__simulink_Trigger", None)
        self.__simulink_Trigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simulink_Block4"):
                opp_val = getattr(old_value, "simulink_Block4", None)
                if opp_val == self:
                    setattr(old_value, "simulink_Block4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simulink_Block4"):
                opp_val = getattr(value, "simulink_Block4", None)
                setattr(value, "simulink_Block4", self)

class simulink_Parameter:

    def __init__(self, name: str, type: str, value: str, readOnly: bool, simulink_Parameter: "simulink_Block" = None, simulink_Parameter20: "simulink_Port" = None):
        self.name = name
        self.type = type
        self.value = value
        self.readOnly = readOnly
        self.simulink_Parameter = simulink_Parameter
        self.simulink_Parameter20 = simulink_Parameter20
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def readOnly(self) -> bool:
        return self.__readOnly

    @readOnly.setter
    def readOnly(self, readOnly: bool):
        self.__readOnly = readOnly

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simulink_Parameter(self):
        return self.__simulink_Parameter

    @simulink_Parameter.setter
    def simulink_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Parameter__simulink_Parameter", None)
        self.__simulink_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simulink_Block"):
                opp_val = getattr(old_value, "simulink_Block", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simulink_Block"):
                opp_val = getattr(value, "simulink_Block", None)
                if opp_val is None:
                    setattr(value, "simulink_Block", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simulink_Parameter20(self):
        return self.__simulink_Parameter20

    @simulink_Parameter20.setter
    def simulink_Parameter20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Parameter__simulink_Parameter20", None)
        self.__simulink_Parameter20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simulink_Port"):
                opp_val = getattr(old_value, "simulink_Port", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simulink_Port"):
                opp_val = getattr(value, "simulink_Port", None)
                if opp_val is None:
                    setattr(value, "simulink_Port", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SimulinkElement:

    pass
class simulink_Connection(SimulinkElement):

    def __init__(self, lineName: str, Connection: "simulink_OutPort" = None, connection: "simulink_OutPort" = None):
        self.lineName = lineName
        self.Connection = Connection
        self.connection = connection
        
    @property
    def lineName(self) -> str:
        return self.__lineName

    @lineName.setter
    def lineName(self, lineName: str):
        self.__lineName = lineName

    @property
    def Connection(self):
        return self.__Connection

    @Connection.setter
    def Connection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Connection__Connection", None)
        self.__Connection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "from"):
                opp_val = getattr(old_value, "from", None)
                if opp_val == self:
                    setattr(old_value, "from", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "from"):
                opp_val = getattr(value, "from", None)
                setattr(value, "from", self)

    @property
    def connection(self):
        return self.__connection

    @connection.setter
    def connection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Connection__connection", None)
        self.__connection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OutPort"):
                opp_val = getattr(old_value, "OutPort", None)
                if opp_val == self:
                    setattr(old_value, "OutPort", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OutPort"):
                opp_val = getattr(value, "OutPort", None)
                setattr(value, "OutPort", self)

class simulink_Port(SimulinkElement):

    pass
class simulink_SimulinkModel(SimulinkElement):

    def __init__(self, version: str, file: str, library: bool, simulink_SimulinkModel: set["simulink_Block"] = None, simulink_SimulinkModel44: "simulink_ModelReference" = None):
        self.version = version
        self.file = file
        self.library = library
        self.simulink_SimulinkModel = simulink_SimulinkModel if simulink_SimulinkModel is not None else set()
        self.simulink_SimulinkModel44 = simulink_SimulinkModel44
        
    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

    @property
    def library(self) -> bool:
        return self.__library

    @library.setter
    def library(self, library: bool):
        self.__library = library

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def simulink_SimulinkModel(self):
        return self.__simulink_SimulinkModel

    @simulink_SimulinkModel.setter
    def simulink_SimulinkModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_SimulinkModel__simulink_SimulinkModel", None)
        self.__simulink_SimulinkModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simulink_Block29"):
                    opp_val = getattr(item, "simulink_Block29", None)
                    
                    if opp_val == self:
                        setattr(item, "simulink_Block29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simulink_Block29"):
                    opp_val = getattr(item, "simulink_Block29", None)
                    
                    setattr(item, "simulink_Block29", self)
                    

    @property
    def simulink_SimulinkModel44(self):
        return self.__simulink_SimulinkModel44

    @simulink_SimulinkModel44.setter
    def simulink_SimulinkModel44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_SimulinkModel__simulink_SimulinkModel44", None)
        self.__simulink_SimulinkModel44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simulink_ModelReference"):
                opp_val = getattr(old_value, "simulink_ModelReference", None)
                if opp_val == self:
                    setattr(old_value, "simulink_ModelReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simulink_ModelReference"):
                opp_val = getattr(value, "simulink_ModelReference", None)
                setattr(value, "simulink_ModelReference", self)

class simulink_Block(SimulinkElement):

    pass
class simulink_IdentifierReference(SimulinkReference):

    pass
class simulink_SimulinkElement(ABC):

    def __init__(self, name: str, simulink_SimulinkElement: "simulink_IdentifierReference" = None, simulink_SimulinkElement38: "simulink_SimulinkReference" = None):
        self.name = name
        self.simulink_SimulinkElement = simulink_SimulinkElement
        self.simulink_SimulinkElement38 = simulink_SimulinkElement38
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simulink_SimulinkElement(self):
        return self.__simulink_SimulinkElement

    @simulink_SimulinkElement.setter
    def simulink_SimulinkElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_SimulinkElement__simulink_SimulinkElement", None)
        self.__simulink_SimulinkElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simulink_IdentifierReference"):
                opp_val = getattr(old_value, "simulink_IdentifierReference", None)
                if opp_val == self:
                    setattr(old_value, "simulink_IdentifierReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simulink_IdentifierReference"):
                opp_val = getattr(value, "simulink_IdentifierReference", None)
                setattr(value, "simulink_IdentifierReference", self)

    @property
    def simulink_SimulinkElement38(self):
        return self.__simulink_SimulinkElement38

    @simulink_SimulinkElement38.setter
    def simulink_SimulinkElement38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_SimulinkElement__simulink_SimulinkElement38", None)
        self.__simulink_SimulinkElement38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simulink_SimulinkReference"):
                opp_val = getattr(old_value, "simulink_SimulinkReference", None)
                if opp_val == self:
                    setattr(old_value, "simulink_SimulinkReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simulink_SimulinkReference"):
                opp_val = getattr(value, "simulink_SimulinkReference", None)
                setattr(value, "simulink_SimulinkReference", self)
