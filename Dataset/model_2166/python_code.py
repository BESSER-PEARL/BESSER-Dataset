from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Direction(Enum):
    IN = "IN"
    OUT = "OUT"
class PortMemoryAnnotation(Enum):
    NONE = "NONE"
    READ_ONLY = "READ_ONLY"
    WRITE_ONLY = "WRITE_ONLY"
    UNUSED = "UNUSED"


############################################
# Definition of Classes
############################################

class Refinement:

    pass
class pimm_HRefinement(Refinement):

    pass
class pimm_visitor_PiMMVisitor(ABC):

    def __init__(self):
        
        pass
    def visit(self, pimm_subject):
        # TODO: Implement visit method
        pass

    def visitISetter(self, pimm_subject):
        # TODO: Implement visitISetter method
        pass

    def visitExpression(self, pimm_subject):
        # TODO: Implement visitExpression method
        pass

    def visitRoundBufferActor(self, pimm_subject):
        # TODO: Implement visitRoundBufferActor method
        pass

    def visitFunctionParameter(self, pimm_subject):
        # TODO: Implement visitFunctionParameter method
        pass

    def visitConfigInputPort(self, pimm_subject):
        # TODO: Implement visitConfigInputPort method
        pass

    def visitHRefinement(self, pimm_subject):
        # TODO: Implement visitHRefinement method
        pass

    def visitDataOutputPort(self, pimm_subject):
        # TODO: Implement visitDataOutputPort method
        pass

    def visitDataPort(self, pimm_subject):
        # TODO: Implement visitDataPort method
        pass

    def visitDataOutputInterface(self, pimm_subject):
        # TODO: Implement visitDataOutputInterface method
        pass

    def visitActor(self, pimm_subject):
        # TODO: Implement visitActor method
        pass

    def visitAbstractVertex(self, pimm_subject):
        # TODO: Implement visitAbstractVertex method
        pass

    def visitDependency(self, pimm_subject):
        # TODO: Implement visitDependency method
        pass

    def visitBroadcastActor(self, pimm_subject):
        # TODO: Implement visitBroadcastActor method
        pass

    def visitConfigOutputPort(self, pimm_subject):
        # TODO: Implement visitConfigOutputPort method
        pass

    def visitFifo(self, pimm_subject):
        # TODO: Implement visitFifo method
        pass

    def visitDataInputInterface(self, pimm_subject):
        # TODO: Implement visitDataInputInterface method
        pass

    def visitForkActor(self, pimm_subject):
        # TODO: Implement visitForkActor method
        pass

    def visitFunctionPrototype(self, pimm_subject):
        # TODO: Implement visitFunctionPrototype method
        pass

    def visitJoinActor(self, pimm_subject):
        # TODO: Implement visitJoinActor method
        pass

    def visitPort(self, pimm_subject):
        # TODO: Implement visitPort method
        pass

    def visitInterfaceActor(self, pimm_subject):
        # TODO: Implement visitInterfaceActor method
        pass

    def visitRefinement(self, pimm_subject):
        # TODO: Implement visitRefinement method
        pass

    def visitPiGraph(self, pimm_subject):
        # TODO: Implement visitPiGraph method
        pass

    def visitDelay(self, pimm_subject):
        # TODO: Implement visitDelay method
        pass

    def visitDataInputPort(self, pimm_subject):
        # TODO: Implement visitDataInputPort method
        pass

    def visitParameterizable(self, pimm_subject):
        # TODO: Implement visitParameterizable method
        pass

    def visitExecutableActor(self, pimm_subject):
        # TODO: Implement visitExecutableActor method
        pass

    def visitParameter(self, pimm_subject):
        # TODO: Implement visitParameter method
        pass

    def visitConfigOutputInterface(self, pimm_subject):
        # TODO: Implement visitConfigOutputInterface method
        pass

    def visitAbstractActor(self, pimm_subject):
        # TODO: Implement visitAbstractActor method
        pass

    def visitConfigInputInterface(self, pimm_subject):
        # TODO: Implement visitConfigInputInterface method
        pass

class pimm_visitor_PiMMVisitable(ABC):

    def __init__(self):
        
        pass
    def accept(self, pimm_subject):
        # TODO: Implement accept method
        pass

class pimm_ISetter(ABC):

    def __init__(self, ISetter: "pimm_Dependency" = None, setter: set["pimm_Dependency"] = None):
        self.ISetter = ISetter
        self.setter = setter if setter is not None else set()
        
        pass
    @property
    def setter(self):
        return self.__setter

    @setter.setter
    def setter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pimm_ISetter__setter", None)
        self.__setter = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Dependency32"):
                    opp_val = getattr(item, "Dependency32", None)
                    
                    if opp_val == self:
                        setattr(item, "Dependency32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Dependency32"):
                    opp_val = getattr(item, "Dependency32", None)
                    
                    setattr(item, "Dependency32", self)
                    

    @property
    def ISetter(self):
        return self.__ISetter

    @ISetter.setter
    def ISetter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pimm_ISetter__ISetter", None)
        self.__ISetter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoingDependencies"):
                opp_val = getattr(old_value, "outgoingDependencies", None)
                if opp_val == self:
                    setattr(old_value, "outgoingDependencies", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoingDependencies"):
                opp_val = getattr(value, "outgoingDependencies", None)
                setattr(value, "outgoingDependencies", self)

    def getValue(self) :
        # TODO: Implement getValue method
        pass

class Parameter:

    pass
class pimm_ConfigInputInterface(Parameter):

    pass
class InterfaceActor:

    pass
class pimm_DataOutputInterface(InterfaceActor):

    pass
class pimm_ConfigOutputInterface(InterfaceActor):

    pass
class pimm_DataInputInterface(InterfaceActor):

    pass
class ISetter:

    pass
class DataOutputPort:

    pass
class Port:

    pass
class pimm_DataPort(Port):

    def __init__(self, annotation: str, pimm_DataPort: "pimm_Expression" = None):
        self.annotation = annotation
        self.pimm_DataPort = pimm_DataPort
        
        pass
    @property
    def annotation(self):
        return self.__annotation

    @annotation.setter
    def annotation(self, annotation: str):
        self.__annotation = annotation


    @property
    def pimm_DataPort(self):
        return self.__pimm_DataPort

    @pimm_DataPort.setter
    def pimm_DataPort(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pimm_DataPort__pimm_DataPort", None)
        self.__pimm_DataPort = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pimm_Expression43"):
                opp_val = getattr(old_value, "pimm_Expression43", None)
                if opp_val == self:
                    setattr(old_value, "pimm_Expression43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pimm_Expression43"):
                opp_val = getattr(value, "pimm_Expression43", None)
                setattr(value, "pimm_Expression43", self)

class DataPort:

    pass
class ExecutableActor:

    pass
class pimm_JoinActor(ExecutableActor):

    pass
class pimm_RoundBufferActor(ExecutableActor):

    pass
class pimm_ForkActor(ExecutableActor):

    pass
class pimm_BroadcastActor(ExecutableActor):

    pass
class pimm_Actor(ExecutableActor):

    def __init__(self, configurationActor: bool, memoryScriptPath: str, pimm_Actor: "pimm_Refinement" = None):
        self.configurationActor = configurationActor
        self.memoryScriptPath = memoryScriptPath
        self.pimm_Actor = pimm_Actor
        
        pass
    @property
    def configurationActor(self):
        return self.__configurationActor

    @configurationActor.setter
    def configurationActor(self, configurationActor: bool):
        self.__configurationActor = configurationActor


    @property
    def memoryScriptPath(self):
        return self.__memoryScriptPath

    @memoryScriptPath.setter
    def memoryScriptPath(self, memoryScriptPath: str):
        self.__memoryScriptPath = memoryScriptPath


    @property
    def pimm_Actor(self):
        return self.__pimm_Actor

    @pimm_Actor.setter
    def pimm_Actor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pimm_Actor__pimm_Actor", None)
        self.__pimm_Actor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pimm_Refinement"):
                opp_val = getattr(old_value, "pimm_Refinement", None)
                if opp_val == self:
                    setattr(old_value, "pimm_Refinement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pimm_Refinement"):
                opp_val = getattr(value, "pimm_Refinement", None)
                setattr(value, "pimm_Refinement", self)

class Parameterizable:

    pass
class pimm_Delay(Parameterizable):

    pass
class pimm_AbstractVertex(Parameterizable):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class pimm_ConfigInputPort(Port):

    pass
class PiMMVisitable:

    pass
class pimm_Fifo(PiMMVisitable):

    def __init__(self, id: str, type: str, pimm_Fifo: "pimm_PiGraph" = None, Fifo: "pimm_DataInputPort" = None, Fifo17: "pimm_DataOutputPort" = None, outgoingFifo: "pimm_DataOutputPort" = None, incomingFifo: "pimm_DataInputPort" = None, pimm_Fifo22: "pimm_Delay" = None):
        self.id = id
        self.type = type
        self.pimm_Fifo = pimm_Fifo
        self.Fifo = Fifo
        self.Fifo17 = Fifo17
        self.outgoingFifo = outgoingFifo
        self.incomingFifo = incomingFifo
        self.pimm_Fifo22 = pimm_Fifo22
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def Fifo(self):
        return self.__Fifo

    @Fifo.setter
    def Fifo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pimm_Fifo__Fifo", None)
        self.__Fifo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "targetPort"):
                opp_val = getattr(old_value, "targetPort", None)
                if opp_val == self:
                    setattr(old_value, "targetPort", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "targetPort"):
                opp_val = getattr(value, "targetPort", None)
                setattr(value, "targetPort", self)

    @property
    def Fifo17(self):
        return self.__Fifo17

    @Fifo17.setter
    def Fifo17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pimm_Fifo__Fifo17", None)
        self.__Fifo17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourcePort"):
                opp_val = getattr(old_value, "sourcePort", None)
                if opp_val == self:
                    setattr(old_value, "sourcePort", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourcePort"):
                opp_val = getattr(value, "sourcePort", None)
                setattr(value, "sourcePort", self)

    @property
    def pimm_Fifo22(self):
        return self.__pimm_Fifo22

    @pimm_Fifo22.setter
    def pimm_Fifo22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pimm_Fifo__pimm_Fifo22", None)
        self.__pimm_Fifo22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pimm_Delay"):
                opp_val = getattr(old_value, "pimm_Delay", None)
                if opp_val == self:
                    setattr(old_value, "pimm_Delay", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pimm_Delay"):
                opp_val = getattr(value, "pimm_Delay", None)
                setattr(value, "pimm_Delay", self)

    @property
    def pimm_Fifo(self):
        return self.__pimm_Fifo

    @pimm_Fifo.setter
    def pimm_Fifo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pimm_Fifo__pimm_Fifo", None)
        self.__pimm_Fifo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pimm_PiGraph9"):
                opp_val = getattr(old_value, "pimm_PiGraph9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pimm_PiGraph9"):
                opp_val = getattr(value, "pimm_PiGraph9", None)
                if opp_val is None:
                    setattr(value, "pimm_PiGraph9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outgoingFifo(self):
        return self.__outgoingFifo

    @outgoingFifo.setter
    def outgoingFifo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pimm_Fifo__outgoingFifo", None)
        self.__outgoingFifo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataOutputPort"):
                opp_val = getattr(old_value, "DataOutputPort", None)
                if opp_val == self:
                    setattr(old_value, "DataOutputPort", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataOutputPort"):
                opp_val = getattr(value, "DataOutputPort", None)
                setattr(value, "DataOutputPort", self)

    @property
    def incomingFifo(self):
        return self.__incomingFifo

    @incomingFifo.setter
    def incomingFifo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pimm_Fifo__incomingFifo", None)
        self.__incomingFifo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataInputPort"):
                opp_val = getattr(old_value, "DataInputPort", None)
                if opp_val == self:
                    setattr(old_value, "DataInputPort", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataInputPort"):
                opp_val = getattr(value, "DataInputPort", None)
                setattr(value, "DataInputPort", self)

class pimm_Port(PiMMVisitable):

    def __init__(self, name: str, kind: str, pimm_Port: "pimm_InterfaceActor" = None):
        self.name = name
        self.kind = kind
        self.pimm_Port = pimm_Port
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def pimm_Port(self):
        return self.__pimm_Port

    @pimm_Port.setter
    def pimm_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pimm_Port__pimm_Port", None)
        self.__pimm_Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pimm_InterfaceActor"):
                opp_val = getattr(old_value, "pimm_InterfaceActor", None)
                if opp_val == self:
                    setattr(old_value, "pimm_InterfaceActor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pimm_InterfaceActor"):
                opp_val = getattr(value, "pimm_InterfaceActor", None)
                setattr(value, "pimm_InterfaceActor", self)

class pimm_Dependency(PiMMVisitable):

    pass
class pimm_Expression(PiMMVisitable):

    def __init__(self, string: str, pimm_Expression: "pimm_Parameter" = None, pimm_Expression43: "pimm_DataPort" = None, pimm_Expression35: "pimm_Delay" = None):
        self.string = string
        self.pimm_Expression = pimm_Expression
        self.pimm_Expression43 = pimm_Expression43
        self.pimm_Expression35 = pimm_Expression35
        
        pass
    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, string: str):
        self.__string = string


    @property
    def pimm_Expression43(self):
        return self.__pimm_Expression43

    @pimm_Expression43.setter
    def pimm_Expression43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pimm_Expression__pimm_Expression43", None)
        self.__pimm_Expression43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pimm_DataPort"):
                opp_val = getattr(old_value, "pimm_DataPort", None)
                if opp_val == self:
                    setattr(old_value, "pimm_DataPort", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pimm_DataPort"):
                opp_val = getattr(value, "pimm_DataPort", None)
                setattr(value, "pimm_DataPort", self)

    @property
    def pimm_Expression35(self):
        return self.__pimm_Expression35

    @pimm_Expression35.setter
    def pimm_Expression35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pimm_Expression__pimm_Expression35", None)
        self.__pimm_Expression35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pimm_Delay34"):
                opp_val = getattr(old_value, "pimm_Delay34", None)
                if opp_val == self:
                    setattr(old_value, "pimm_Delay34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pimm_Delay34"):
                opp_val = getattr(value, "pimm_Delay34", None)
                setattr(value, "pimm_Delay34", self)

    @property
    def pimm_Expression(self):
        return self.__pimm_Expression

    @pimm_Expression.setter
    def pimm_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pimm_Expression__pimm_Expression", None)
        self.__pimm_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pimm_Parameter28"):
                opp_val = getattr(old_value, "pimm_Parameter28", None)
                if opp_val == self:
                    setattr(old_value, "pimm_Parameter28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pimm_Parameter28"):
                opp_val = getattr(value, "pimm_Parameter28", None)
                setattr(value, "pimm_Parameter28", self)

    def evaluate(self) :
        # TODO: Implement evaluate method
        pass

class pimm_FunctionPrototype(PiMMVisitable):

    def __init__(self, name: str, pimm_FunctionPrototype: "pimm_HRefinement" = None, pimm_FunctionPrototype39: "pimm_HRefinement" = None, pimm_FunctionPrototype41: set["pimm_FunctionParameter"] = None):
        self.name = name
        self.pimm_FunctionPrototype = pimm_FunctionPrototype
        self.pimm_FunctionPrototype39 = pimm_FunctionPrototype39
        self.pimm_FunctionPrototype41 = pimm_FunctionPrototype41 if pimm_FunctionPrototype41 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def pimm_FunctionPrototype39(self):
        return self.__pimm_FunctionPrototype39

    @pimm_FunctionPrototype39.setter
    def pimm_FunctionPrototype39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pimm_FunctionPrototype__pimm_FunctionPrototype39", None)
        self.__pimm_FunctionPrototype39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pimm_HRefinement38"):
                opp_val = getattr(old_value, "pimm_HRefinement38", None)
                if opp_val == self:
                    setattr(old_value, "pimm_HRefinement38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pimm_HRefinement38"):
                opp_val = getattr(value, "pimm_HRefinement38", None)
                setattr(value, "pimm_HRefinement38", self)

    @property
    def pimm_FunctionPrototype41(self):
        return self.__pimm_FunctionPrototype41

    @pimm_FunctionPrototype41.setter
    def pimm_FunctionPrototype41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pimm_FunctionPrototype__pimm_FunctionPrototype41", None)
        self.__pimm_FunctionPrototype41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pimm_FunctionParameter"):
                    opp_val = getattr(item, "pimm_FunctionParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "pimm_FunctionParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pimm_FunctionParameter"):
                    opp_val = getattr(item, "pimm_FunctionParameter", None)
                    
                    setattr(item, "pimm_FunctionParameter", self)
                    

    @property
    def pimm_FunctionPrototype(self):
        return self.__pimm_FunctionPrototype

    @pimm_FunctionPrototype.setter
    def pimm_FunctionPrototype(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pimm_FunctionPrototype__pimm_FunctionPrototype", None)
        self.__pimm_FunctionPrototype = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pimm_HRefinement"):
                opp_val = getattr(old_value, "pimm_HRefinement", None)
                if opp_val == self:
                    setattr(old_value, "pimm_HRefinement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pimm_HRefinement"):
                opp_val = getattr(value, "pimm_HRefinement", None)
                setattr(value, "pimm_HRefinement", self)

class pimm_Refinement(PiMMVisitable):

    def __init__(self, fileName: str, filePath: str, pimm_Refinement: "pimm_Actor" = None):
        self.fileName = fileName
        self.filePath = filePath
        self.pimm_Refinement = pimm_Refinement
        
        pass
    @property
    def filePath(self):
        return self.__filePath

    @filePath.setter
    def filePath(self, filePath: str):
        self.__filePath = filePath


    @property
    def fileName(self):
        return self.__fileName

    @fileName.setter
    def fileName(self, fileName: str):
        self.__fileName = fileName


    @property
    def pimm_Refinement(self):
        return self.__pimm_Refinement

    @pimm_Refinement.setter
    def pimm_Refinement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pimm_Refinement__pimm_Refinement", None)
        self.__pimm_Refinement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pimm_Actor"):
                opp_val = getattr(old_value, "pimm_Actor", None)
                if opp_val == self:
                    setattr(old_value, "pimm_Actor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pimm_Actor"):
                opp_val = getattr(value, "pimm_Actor", None)
                setattr(value, "pimm_Actor", self)

    def getAbstractActor(self) :
        # TODO: Implement getAbstractActor method
        pass

class pimm_FunctionParameter(PiMMVisitable):

    def __init__(self, name: str, direction: str, type: str, isConfigurationParameter: bool, pimm_FunctionParameter: "pimm_FunctionPrototype" = None):
        self.name = name
        self.direction = direction
        self.type = type
        self.isConfigurationParameter = isConfigurationParameter
        self.pimm_FunctionParameter = pimm_FunctionParameter
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction


    @property
    def isConfigurationParameter(self):
        return self.__isConfigurationParameter

    @isConfigurationParameter.setter
    def isConfigurationParameter(self, isConfigurationParameter: bool):
        self.__isConfigurationParameter = isConfigurationParameter


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def pimm_FunctionParameter(self):
        return self.__pimm_FunctionParameter

    @pimm_FunctionParameter.setter
    def pimm_FunctionParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pimm_FunctionParameter__pimm_FunctionParameter", None)
        self.__pimm_FunctionParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pimm_FunctionPrototype41"):
                opp_val = getattr(old_value, "pimm_FunctionPrototype41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pimm_FunctionPrototype41"):
                opp_val = getattr(value, "pimm_FunctionPrototype41", None)
                if opp_val is None:
                    setattr(value, "pimm_FunctionPrototype41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pimm_Parameterizable(PiMMVisitable):

    def __init__(self, pimm_Parameterizable: set["pimm_ConfigInputPort"] = None):
        self.pimm_Parameterizable = pimm_Parameterizable if pimm_Parameterizable is not None else set()
        
        pass
    @property
    def pimm_Parameterizable(self):
        return self.__pimm_Parameterizable

    @pimm_Parameterizable.setter
    def pimm_Parameterizable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pimm_Parameterizable__pimm_Parameterizable", None)
        self.__pimm_Parameterizable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pimm_ConfigInputPort"):
                    opp_val = getattr(item, "pimm_ConfigInputPort", None)
                    
                    if opp_val == self:
                        setattr(item, "pimm_ConfigInputPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pimm_ConfigInputPort"):
                    opp_val = getattr(item, "pimm_ConfigInputPort", None)
                    
                    setattr(item, "pimm_ConfigInputPort", self)
                    

    def getInputParameters(self) :
        # TODO: Implement getInputParameters method
        pass

class AbstractActor:

    pass
class pimm_ExecutableActor(AbstractActor):

    pass
class pimm_InterfaceActor(AbstractActor):

    def __init__(self, kind: str, pimm_InterfaceActor: "pimm_Port" = None):
        self.kind = kind
        self.pimm_InterfaceActor = pimm_InterfaceActor
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def pimm_InterfaceActor(self):
        return self.__pimm_InterfaceActor

    @pimm_InterfaceActor.setter
    def pimm_InterfaceActor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pimm_InterfaceActor__pimm_InterfaceActor", None)
        self.__pimm_InterfaceActor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pimm_Port"):
                opp_val = getattr(old_value, "pimm_Port", None)
                if opp_val == self:
                    setattr(old_value, "pimm_Port", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pimm_Port"):
                opp_val = getattr(value, "pimm_Port", None)
                setattr(value, "pimm_Port", self)

class pimm_PiGraph(AbstractActor):

    def __init__(self, pimm_PiGraph9: set["pimm_Fifo"] = None, pimm_PiGraph11: set["pimm_Parameter"] = None, pimm_PiGraph13: set["pimm_Dependency"] = None, pimm_PiGraph: set["pimm_AbstractActor"] = None):
        self.pimm_PiGraph9 = pimm_PiGraph9 if pimm_PiGraph9 is not None else set()
        self.pimm_PiGraph11 = pimm_PiGraph11 if pimm_PiGraph11 is not None else set()
        self.pimm_PiGraph13 = pimm_PiGraph13 if pimm_PiGraph13 is not None else set()
        self.pimm_PiGraph = pimm_PiGraph if pimm_PiGraph is not None else set()
        
        pass
    @property
    def pimm_PiGraph(self):
        return self.__pimm_PiGraph

    @pimm_PiGraph.setter
    def pimm_PiGraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pimm_PiGraph__pimm_PiGraph", None)
        self.__pimm_PiGraph = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pimm_AbstractActor7"):
                    opp_val = getattr(item, "pimm_AbstractActor7", None)
                    
                    if opp_val == self:
                        setattr(item, "pimm_AbstractActor7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pimm_AbstractActor7"):
                    opp_val = getattr(item, "pimm_AbstractActor7", None)
                    
                    setattr(item, "pimm_AbstractActor7", self)
                    

    @property
    def pimm_PiGraph9(self):
        return self.__pimm_PiGraph9

    @pimm_PiGraph9.setter
    def pimm_PiGraph9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pimm_PiGraph__pimm_PiGraph9", None)
        self.__pimm_PiGraph9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pimm_Fifo"):
                    opp_val = getattr(item, "pimm_Fifo", None)
                    
                    if opp_val == self:
                        setattr(item, "pimm_Fifo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pimm_Fifo"):
                    opp_val = getattr(item, "pimm_Fifo", None)
                    
                    setattr(item, "pimm_Fifo", self)
                    

    @property
    def pimm_PiGraph11(self):
        return self.__pimm_PiGraph11

    @pimm_PiGraph11.setter
    def pimm_PiGraph11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pimm_PiGraph__pimm_PiGraph11", None)
        self.__pimm_PiGraph11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pimm_Parameter"):
                    opp_val = getattr(item, "pimm_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "pimm_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pimm_Parameter"):
                    opp_val = getattr(item, "pimm_Parameter", None)
                    
                    setattr(item, "pimm_Parameter", self)
                    

    @property
    def pimm_PiGraph13(self):
        return self.__pimm_PiGraph13

    @pimm_PiGraph13.setter
    def pimm_PiGraph13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pimm_PiGraph__pimm_PiGraph13", None)
        self.__pimm_PiGraph13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pimm_Dependency"):
                    opp_val = getattr(item, "pimm_Dependency", None)
                    
                    if opp_val == self:
                        setattr(item, "pimm_Dependency", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pimm_Dependency"):
                    opp_val = getattr(item, "pimm_Dependency", None)
                    
                    setattr(item, "pimm_Dependency", self)
                    

    def getAllParameters(self) :
        # TODO: Implement getAllParameters method
        pass

    def getVerticesNames(self) :
        # TODO: Implement getVerticesNames method
        pass

    def getActors(self) :
        # TODO: Implement getActors method
        pass

    def getParametersNames(self) :
        # TODO: Implement getParametersNames method
        pass

class pimm_ConfigOutputPort(DataOutputPort, ISetter):

    pass
class pimm_DataOutputPort(DataPort):

    pass
class pimm_DataInputPort(DataPort):

    pass
class AbstractVertex:

    pass
class pimm_Parameter(AbstractVertex, ISetter):

    def __init__(self, configurationInterface: bool, pimm_Parameter: "pimm_PiGraph" = None, pimm_Parameter25: "pimm_ConfigInputPort" = None, pimm_Parameter28: "pimm_Expression" = None):
        self.configurationInterface = configurationInterface
        self.pimm_Parameter = pimm_Parameter
        self.pimm_Parameter25 = pimm_Parameter25
        self.pimm_Parameter28 = pimm_Parameter28
        
        pass
    @property
    def configurationInterface(self):
        return self.__configurationInterface

    @configurationInterface.setter
    def configurationInterface(self, configurationInterface: bool):
        self.__configurationInterface = configurationInterface


    @property
    def pimm_Parameter28(self):
        return self.__pimm_Parameter28

    @pimm_Parameter28.setter
    def pimm_Parameter28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pimm_Parameter__pimm_Parameter28", None)
        self.__pimm_Parameter28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pimm_Expression"):
                opp_val = getattr(old_value, "pimm_Expression", None)
                if opp_val == self:
                    setattr(old_value, "pimm_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pimm_Expression"):
                opp_val = getattr(value, "pimm_Expression", None)
                setattr(value, "pimm_Expression", self)

    @property
    def pimm_Parameter25(self):
        return self.__pimm_Parameter25

    @pimm_Parameter25.setter
    def pimm_Parameter25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pimm_Parameter__pimm_Parameter25", None)
        self.__pimm_Parameter25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pimm_ConfigInputPort26"):
                opp_val = getattr(old_value, "pimm_ConfigInputPort26", None)
                if opp_val == self:
                    setattr(old_value, "pimm_ConfigInputPort26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pimm_ConfigInputPort26"):
                opp_val = getattr(value, "pimm_ConfigInputPort26", None)
                setattr(value, "pimm_ConfigInputPort26", self)

    @property
    def pimm_Parameter(self):
        return self.__pimm_Parameter

    @pimm_Parameter.setter
    def pimm_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pimm_Parameter__pimm_Parameter", None)
        self.__pimm_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pimm_PiGraph11"):
                opp_val = getattr(old_value, "pimm_PiGraph11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pimm_PiGraph11"):
                opp_val = getattr(value, "pimm_PiGraph11", None)
                if opp_val is None:
                    setattr(value, "pimm_PiGraph11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def isLocallyStatic(self) :
        # TODO: Implement isLocallyStatic method
        pass

    def isDependent(self) :
        # TODO: Implement isDependent method
        pass

class pimm_AbstractActor(AbstractVertex):

    def __init__(self, pimm_AbstractActor: set["pimm_DataInputPort"] = None, pimm_AbstractActor3: set["pimm_DataOutputPort"] = None, pimm_AbstractActor5: set["pimm_ConfigOutputPort"] = None, pimm_AbstractActor7: "pimm_PiGraph" = None):
        self.pimm_AbstractActor = pimm_AbstractActor if pimm_AbstractActor is not None else set()
        self.pimm_AbstractActor3 = pimm_AbstractActor3 if pimm_AbstractActor3 is not None else set()
        self.pimm_AbstractActor5 = pimm_AbstractActor5 if pimm_AbstractActor5 is not None else set()
        self.pimm_AbstractActor7 = pimm_AbstractActor7
        
        pass
    @property
    def pimm_AbstractActor5(self):
        return self.__pimm_AbstractActor5

    @pimm_AbstractActor5.setter
    def pimm_AbstractActor5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pimm_AbstractActor__pimm_AbstractActor5", None)
        self.__pimm_AbstractActor5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pimm_ConfigOutputPort"):
                    opp_val = getattr(item, "pimm_ConfigOutputPort", None)
                    
                    if opp_val == self:
                        setattr(item, "pimm_ConfigOutputPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pimm_ConfigOutputPort"):
                    opp_val = getattr(item, "pimm_ConfigOutputPort", None)
                    
                    setattr(item, "pimm_ConfigOutputPort", self)
                    

    @property
    def pimm_AbstractActor7(self):
        return self.__pimm_AbstractActor7

    @pimm_AbstractActor7.setter
    def pimm_AbstractActor7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pimm_AbstractActor__pimm_AbstractActor7", None)
        self.__pimm_AbstractActor7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pimm_PiGraph"):
                opp_val = getattr(old_value, "pimm_PiGraph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pimm_PiGraph"):
                opp_val = getattr(value, "pimm_PiGraph", None)
                if opp_val is None:
                    setattr(value, "pimm_PiGraph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pimm_AbstractActor3(self):
        return self.__pimm_AbstractActor3

    @pimm_AbstractActor3.setter
    def pimm_AbstractActor3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pimm_AbstractActor__pimm_AbstractActor3", None)
        self.__pimm_AbstractActor3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pimm_DataOutputPort"):
                    opp_val = getattr(item, "pimm_DataOutputPort", None)
                    
                    if opp_val == self:
                        setattr(item, "pimm_DataOutputPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pimm_DataOutputPort"):
                    opp_val = getattr(item, "pimm_DataOutputPort", None)
                    
                    setattr(item, "pimm_DataOutputPort", self)
                    

    @property
    def pimm_AbstractActor(self):
        return self.__pimm_AbstractActor

    @pimm_AbstractActor.setter
    def pimm_AbstractActor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pimm_AbstractActor__pimm_AbstractActor", None)
        self.__pimm_AbstractActor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pimm_DataInputPort"):
                    opp_val = getattr(item, "pimm_DataInputPort", None)
                    
                    if opp_val == self:
                        setattr(item, "pimm_DataInputPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pimm_DataInputPort"):
                    opp_val = getattr(item, "pimm_DataInputPort", None)
                    
                    setattr(item, "pimm_DataInputPort", self)
                    

    def getAllPorts(self) :
        # TODO: Implement getAllPorts method
        pass
