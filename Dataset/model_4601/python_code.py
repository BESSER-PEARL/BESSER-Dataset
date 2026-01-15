from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Port:

    pass
class adfg_InputPort(Port):

    pass
class Connection:

    pass
class adfg_LossyChannel(Connection):

    pass
class adfg_Channel(Connection):

    def __init__(self, initial: int):
        self.initial = initial
        
    @property
    def initial(self) -> int:
        return self.__initial

    @initial.setter
    def initial(self, initial: int):
        self.__initial = initial

class Actor:

    pass
class adfg_AperiodicActor(Actor):

    def __init__(self, capacity: str, replenishmentPeriod: str):
        self.capacity = capacity
        self.replenishmentPeriod = replenishmentPeriod
        
    @property
    def replenishmentPeriod(self) -> str:
        return self.__replenishmentPeriod

    @replenishmentPeriod.setter
    def replenishmentPeriod(self, replenishmentPeriod: str):
        self.__replenishmentPeriod = replenishmentPeriod

    @property
    def capacity(self) -> str:
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: str):
        self.__capacity = capacity

class adfg_Connection:

    def __init__(self, size: int, id: int, Connection: "adfg_Graph" = None, Connection35: "adfg_OutputPort" = None, connection: "adfg_OutputPort" = None, connection27: "adfg_InputPort" = None, connections: "adfg_Graph" = None, Connection33: "adfg_InputPort" = None):
        self.size = size
        self.id = id
        self.Connection = Connection
        self.Connection35 = Connection35
        self.connection = connection
        self.connection27 = connection27
        self.connections = connections
        self.Connection33 = Connection33
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def connection27(self):
        return self.__connection27

    @connection27.setter
    def connection27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adfg_Connection__connection27", None)
        self.__connection27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InputPort"):
                opp_val = getattr(old_value, "InputPort", None)
                if opp_val == self:
                    setattr(old_value, "InputPort", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InputPort"):
                opp_val = getattr(value, "InputPort", None)
                setattr(value, "InputPort", self)

    @property
    def connections(self):
        return self.__connections

    @connections.setter
    def connections(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adfg_Connection__connections", None)
        self.__connections = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph29"):
                opp_val = getattr(old_value, "Graph29", None)
                if opp_val == self:
                    setattr(old_value, "Graph29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph29"):
                opp_val = getattr(value, "Graph29", None)
                setattr(value, "Graph29", self)

    @property
    def Connection(self):
        return self.__Connection

    @Connection.setter
    def Connection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adfg_Connection__Connection", None)
        self.__Connection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner9"):
                opp_val = getattr(old_value, "owner9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner9"):
                opp_val = getattr(value, "owner9", None)
                if opp_val is None:
                    setattr(value, "owner9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def connection(self):
        return self.__connection

    @connection.setter
    def connection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adfg_Connection__connection", None)
        self.__connection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OutputPort"):
                opp_val = getattr(old_value, "OutputPort", None)
                if opp_val == self:
                    setattr(old_value, "OutputPort", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OutputPort"):
                opp_val = getattr(value, "OutputPort", None)
                setattr(value, "OutputPort", self)

    @property
    def Connection35(self):
        return self.__Connection35

    @Connection35.setter
    def Connection35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adfg_Connection__Connection35", None)
        self.__Connection35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if opp_val == self:
                    setattr(old_value, "source", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                setattr(value, "source", self)

    @property
    def Connection33(self):
        return self.__Connection33

    @Connection33.setter
    def Connection33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adfg_Connection__Connection33", None)
        self.__Connection33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if opp_val == self:
                    setattr(old_value, "target", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                setattr(value, "target", self)

class adfg_AffineRelation:

    def __init__(self, n: int, phi: int, d: int, affineRelationSource: "adfg_PeriodicActor" = None, affineRelationTarget: "adfg_PeriodicActor" = None, affineRelations: "adfg_Graph" = None, AffineRelation: "adfg_Graph" = None, AffineRelation38: "adfg_PeriodicActor" = None, AffineRelation41: "adfg_PeriodicActor" = None):
        self.n = n
        self.phi = phi
        self.d = d
        self.affineRelationSource = affineRelationSource
        self.affineRelationTarget = affineRelationTarget
        self.affineRelations = affineRelations
        self.AffineRelation = AffineRelation
        self.AffineRelation38 = AffineRelation38
        self.AffineRelation41 = AffineRelation41
        
    @property
    def d(self) -> int:
        return self.__d

    @d.setter
    def d(self, d: int):
        self.__d = d

    @property
    def phi(self) -> int:
        return self.__phi

    @phi.setter
    def phi(self, phi: int):
        self.__phi = phi

    @property
    def n(self) -> int:
        return self.__n

    @n.setter
    def n(self, n: int):
        self.__n = n

    @property
    def AffineRelation(self):
        return self.__AffineRelation

    @AffineRelation.setter
    def AffineRelation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adfg_AffineRelation__AffineRelation", None)
        self.__AffineRelation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner7"):
                opp_val = getattr(old_value, "owner7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner7"):
                opp_val = getattr(value, "owner7", None)
                if opp_val is None:
                    setattr(value, "owner7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def affineRelations(self):
        return self.__affineRelations

    @affineRelations.setter
    def affineRelations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adfg_AffineRelation__affineRelations", None)
        self.__affineRelations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph24"):
                opp_val = getattr(old_value, "Graph24", None)
                if opp_val == self:
                    setattr(old_value, "Graph24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph24"):
                opp_val = getattr(value, "Graph24", None)
                setattr(value, "Graph24", self)

    @property
    def affineRelationTarget(self):
        return self.__affineRelationTarget

    @affineRelationTarget.setter
    def affineRelationTarget(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adfg_AffineRelation__affineRelationTarget", None)
        self.__affineRelationTarget = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PeriodicActor22"):
                opp_val = getattr(old_value, "PeriodicActor22", None)
                if opp_val == self:
                    setattr(old_value, "PeriodicActor22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PeriodicActor22"):
                opp_val = getattr(value, "PeriodicActor22", None)
                setattr(value, "PeriodicActor22", self)

    @property
    def AffineRelation41(self):
        return self.__AffineRelation41

    @AffineRelation41.setter
    def AffineRelation41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adfg_AffineRelation__AffineRelation41", None)
        self.__AffineRelation41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target40"):
                opp_val = getattr(old_value, "target40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target40"):
                opp_val = getattr(value, "target40", None)
                if opp_val is None:
                    setattr(value, "target40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def AffineRelation38(self):
        return self.__AffineRelation38

    @AffineRelation38.setter
    def AffineRelation38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adfg_AffineRelation__AffineRelation38", None)
        self.__AffineRelation38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source37"):
                opp_val = getattr(old_value, "source37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source37"):
                opp_val = getattr(value, "source37", None)
                if opp_val is None:
                    setattr(value, "source37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def affineRelationSource(self):
        return self.__affineRelationSource

    @affineRelationSource.setter
    def affineRelationSource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adfg_AffineRelation__affineRelationSource", None)
        self.__affineRelationSource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PeriodicActor"):
                opp_val = getattr(old_value, "PeriodicActor", None)
                if opp_val == self:
                    setattr(old_value, "PeriodicActor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PeriodicActor"):
                opp_val = getattr(value, "PeriodicActor", None)
                setattr(value, "PeriodicActor", self)

class adfg_OutputPort(Port):

    pass
class adfg_PeriodicActor(Actor):

    def __init__(self, period: str, periodUpperBound: str, phase: str, periodLowerBound: str, deadline: str, wcet: str, PeriodicActor: "adfg_AffineRelation" = None, PeriodicActor22: "adfg_AffineRelation" = None, source37: set["adfg_AffineRelation"] = None, target40: set["adfg_AffineRelation"] = None):
        self.period = period
        self.periodUpperBound = periodUpperBound
        self.phase = phase
        self.periodLowerBound = periodLowerBound
        self.deadline = deadline
        self.wcet = wcet
        self.PeriodicActor = PeriodicActor
        self.PeriodicActor22 = PeriodicActor22
        self.source37 = source37 if source37 is not None else set()
        self.target40 = target40 if target40 is not None else set()
        
    @property
    def periodUpperBound(self) -> str:
        return self.__periodUpperBound

    @periodUpperBound.setter
    def periodUpperBound(self, periodUpperBound: str):
        self.__periodUpperBound = periodUpperBound

    @property
    def periodLowerBound(self) -> str:
        return self.__periodLowerBound

    @periodLowerBound.setter
    def periodLowerBound(self, periodLowerBound: str):
        self.__periodLowerBound = periodLowerBound

    @property
    def wcet(self) -> str:
        return self.__wcet

    @wcet.setter
    def wcet(self, wcet: str):
        self.__wcet = wcet

    @property
    def deadline(self) -> str:
        return self.__deadline

    @deadline.setter
    def deadline(self, deadline: str):
        self.__deadline = deadline

    @property
    def phase(self) -> str:
        return self.__phase

    @phase.setter
    def phase(self, phase: str):
        self.__phase = phase

    @property
    def period(self) -> str:
        return self.__period

    @period.setter
    def period(self, period: str):
        self.__period = period

    @property
    def PeriodicActor22(self):
        return self.__PeriodicActor22

    @PeriodicActor22.setter
    def PeriodicActor22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adfg_PeriodicActor__PeriodicActor22", None)
        self.__PeriodicActor22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "affineRelationTarget"):
                opp_val = getattr(old_value, "affineRelationTarget", None)
                if opp_val == self:
                    setattr(old_value, "affineRelationTarget", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "affineRelationTarget"):
                opp_val = getattr(value, "affineRelationTarget", None)
                setattr(value, "affineRelationTarget", self)

    @property
    def source37(self):
        return self.__source37

    @source37.setter
    def source37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adfg_PeriodicActor__source37", None)
        self.__source37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AffineRelation38"):
                    opp_val = getattr(item, "AffineRelation38", None)
                    
                    if opp_val == self:
                        setattr(item, "AffineRelation38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AffineRelation38"):
                    opp_val = getattr(item, "AffineRelation38", None)
                    
                    setattr(item, "AffineRelation38", self)
                    

    @property
    def PeriodicActor(self):
        return self.__PeriodicActor

    @PeriodicActor.setter
    def PeriodicActor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adfg_PeriodicActor__PeriodicActor", None)
        self.__PeriodicActor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "affineRelationSource"):
                opp_val = getattr(old_value, "affineRelationSource", None)
                if opp_val == self:
                    setattr(old_value, "affineRelationSource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "affineRelationSource"):
                opp_val = getattr(value, "affineRelationSource", None)
                setattr(value, "affineRelationSource", self)

    @property
    def target40(self):
        return self.__target40

    @target40.setter
    def target40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adfg_PeriodicActor__target40", None)
        self.__target40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AffineRelation41"):
                    opp_val = getattr(item, "AffineRelation41", None)
                    
                    if opp_val == self:
                        setattr(item, "AffineRelation41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AffineRelation41"):
                    opp_val = getattr(item, "AffineRelation41", None)
                    
                    setattr(item, "AffineRelation41", self)
                    

class adfg_Port(ABC):

    def __init__(self, sequence: str, name: str, type: str, Port: "adfg_Actor" = None, ports: "adfg_Actor" = None):
        self.sequence = sequence
        self.name = name
        self.type = type
        self.Port = Port
        self.ports = ports
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sequence(self) -> str:
        return self.__sequence

    @sequence.setter
    def sequence(self, sequence: str):
        self.__sequence = sequence

    @property
    def Port(self):
        return self.__Port

    @Port.setter
    def Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adfg_Port__Port", None)
        self.__Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner19"):
                opp_val = getattr(old_value, "owner19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner19"):
                opp_val = getattr(value, "owner19", None)
                if opp_val is None:
                    setattr(value, "owner19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ports(self):
        return self.__ports

    @ports.setter
    def ports(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adfg_Port__ports", None)
        self.__ports = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Actor31"):
                opp_val = getattr(old_value, "Actor31", None)
                if opp_val == self:
                    setattr(old_value, "Actor31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Actor31"):
                opp_val = getattr(value, "Actor31", None)
                setattr(value, "Actor31", self)

class adfg_Actor(ABC):

    def __init__(self, nbPorts: int, name: str, sourceCode: str, priority: int, procNumber: int, nodes: "adfg_Graph" = None, owner19: set["adfg_Port"] = None, Actor: "adfg_Graph" = None, Actor31: "adfg_Port" = None):
        self.nbPorts = nbPorts
        self.name = name
        self.sourceCode = sourceCode
        self.priority = priority
        self.procNumber = procNumber
        self.nodes = nodes
        self.owner19 = owner19 if owner19 is not None else set()
        self.Actor = Actor
        self.Actor31 = Actor31
        
    @property
    def nbPorts(self) -> int:
        return self.__nbPorts

    @nbPorts.setter
    def nbPorts(self, nbPorts: int):
        self.__nbPorts = nbPorts

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def procNumber(self) -> int:
        return self.__procNumber

    @procNumber.setter
    def procNumber(self, procNumber: int):
        self.__procNumber = procNumber

    @property
    def sourceCode(self) -> str:
        return self.__sourceCode

    @sourceCode.setter
    def sourceCode(self, sourceCode: str):
        self.__sourceCode = sourceCode

    @property
    def priority(self) -> int:
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority

    @property
    def Actor(self):
        return self.__Actor

    @Actor.setter
    def Actor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adfg_Actor__Actor", None)
        self.__Actor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner5"):
                opp_val = getattr(old_value, "owner5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner5"):
                opp_val = getattr(value, "owner5", None)
                if opp_val is None:
                    setattr(value, "owner5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Actor31(self):
        return self.__Actor31

    @Actor31.setter
    def Actor31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adfg_Actor__Actor31", None)
        self.__Actor31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ports"):
                opp_val = getattr(old_value, "ports", None)
                if opp_val == self:
                    setattr(old_value, "ports", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ports"):
                opp_val = getattr(value, "ports", None)
                setattr(value, "ports", self)

    @property
    def nodes(self):
        return self.__nodes

    @nodes.setter
    def nodes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adfg_Actor__nodes", None)
        self.__nodes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph17"):
                opp_val = getattr(old_value, "Graph17", None)
                if opp_val == self:
                    setattr(old_value, "Graph17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph17"):
                opp_val = getattr(value, "Graph17", None)
                setattr(value, "Graph17", self)

    @property
    def owner19(self):
        return self.__owner19

    @owner19.setter
    def owner19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adfg_Actor__owner19", None)
        self.__owner19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Port"):
                    opp_val = getattr(item, "Port", None)
                    
                    if opp_val == self:
                        setattr(item, "Port", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Port"):
                    opp_val = getattr(item, "Port", None)
                    
                    setattr(item, "Port", self)
                    

class adfg_GraphConnection:

    pass
class adfg_Graph:

    def __init__(self, name: str, nbActors: int, nbBuffers: int, id: int, sourceCode: str, processorUtilization: float, bufferingRequirements: int, Graph: "adfg_Application" = None, graphs: "adfg_Application" = None, Graph17: "adfg_Actor" = None, Graph24: "adfg_AffineRelation" = None, owner5: set["adfg_Actor"] = None, owner7: set["adfg_AffineRelation"] = None, owner9: set["adfg_Connection"] = None, adfg_Graph: "adfg_GraphConnection" = None, adfg_Graph13: "adfg_GraphConnection" = None, Graph29: "adfg_Connection" = None):
        self.name = name
        self.nbActors = nbActors
        self.nbBuffers = nbBuffers
        self.id = id
        self.sourceCode = sourceCode
        self.processorUtilization = processorUtilization
        self.bufferingRequirements = bufferingRequirements
        self.Graph = Graph
        self.graphs = graphs
        self.Graph17 = Graph17
        self.Graph24 = Graph24
        self.owner5 = owner5 if owner5 is not None else set()
        self.owner7 = owner7 if owner7 is not None else set()
        self.owner9 = owner9 if owner9 is not None else set()
        self.adfg_Graph = adfg_Graph
        self.adfg_Graph13 = adfg_Graph13
        self.Graph29 = Graph29
        
    @property
    def bufferingRequirements(self) -> int:
        return self.__bufferingRequirements

    @bufferingRequirements.setter
    def bufferingRequirements(self, bufferingRequirements: int):
        self.__bufferingRequirements = bufferingRequirements

    @property
    def nbActors(self) -> int:
        return self.__nbActors

    @nbActors.setter
    def nbActors(self, nbActors: int):
        self.__nbActors = nbActors

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def processorUtilization(self) -> float:
        return self.__processorUtilization

    @processorUtilization.setter
    def processorUtilization(self, processorUtilization: float):
        self.__processorUtilization = processorUtilization

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sourceCode(self) -> str:
        return self.__sourceCode

    @sourceCode.setter
    def sourceCode(self, sourceCode: str):
        self.__sourceCode = sourceCode

    @property
    def nbBuffers(self) -> int:
        return self.__nbBuffers

    @nbBuffers.setter
    def nbBuffers(self, nbBuffers: int):
        self.__nbBuffers = nbBuffers

    @property
    def Graph24(self):
        return self.__Graph24

    @Graph24.setter
    def Graph24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adfg_Graph__Graph24", None)
        self.__Graph24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "affineRelations"):
                opp_val = getattr(old_value, "affineRelations", None)
                if opp_val == self:
                    setattr(old_value, "affineRelations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "affineRelations"):
                opp_val = getattr(value, "affineRelations", None)
                setattr(value, "affineRelations", self)

    @property
    def Graph(self):
        return self.__Graph

    @Graph.setter
    def Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adfg_Graph__Graph", None)
        self.__Graph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner"):
                opp_val = getattr(old_value, "owner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner"):
                opp_val = getattr(value, "owner", None)
                if opp_val is None:
                    setattr(value, "owner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graphs(self):
        return self.__graphs

    @graphs.setter
    def graphs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adfg_Graph__graphs", None)
        self.__graphs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Application"):
                opp_val = getattr(old_value, "Application", None)
                if opp_val == self:
                    setattr(old_value, "Application", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Application"):
                opp_val = getattr(value, "Application", None)
                setattr(value, "Application", self)

    @property
    def Graph17(self):
        return self.__Graph17

    @Graph17.setter
    def Graph17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adfg_Graph__Graph17", None)
        self.__Graph17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nodes"):
                opp_val = getattr(old_value, "nodes", None)
                if opp_val == self:
                    setattr(old_value, "nodes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nodes"):
                opp_val = getattr(value, "nodes", None)
                setattr(value, "nodes", self)

    @property
    def Graph29(self):
        return self.__Graph29

    @Graph29.setter
    def Graph29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adfg_Graph__Graph29", None)
        self.__Graph29 = value
        
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
    def owner9(self):
        return self.__owner9

    @owner9.setter
    def owner9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adfg_Graph__owner9", None)
        self.__owner9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Connection"):
                    opp_val = getattr(item, "Connection", None)
                    
                    if opp_val == self:
                        setattr(item, "Connection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Connection"):
                    opp_val = getattr(item, "Connection", None)
                    
                    setattr(item, "Connection", self)
                    

    @property
    def adfg_Graph13(self):
        return self.__adfg_Graph13

    @adfg_Graph13.setter
    def adfg_Graph13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adfg_Graph__adfg_Graph13", None)
        self.__adfg_Graph13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adfg_GraphConnection12"):
                opp_val = getattr(old_value, "adfg_GraphConnection12", None)
                if opp_val == self:
                    setattr(old_value, "adfg_GraphConnection12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adfg_GraphConnection12"):
                opp_val = getattr(value, "adfg_GraphConnection12", None)
                setattr(value, "adfg_GraphConnection12", self)

    @property
    def owner7(self):
        return self.__owner7

    @owner7.setter
    def owner7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adfg_Graph__owner7", None)
        self.__owner7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AffineRelation"):
                    opp_val = getattr(item, "AffineRelation", None)
                    
                    if opp_val == self:
                        setattr(item, "AffineRelation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AffineRelation"):
                    opp_val = getattr(item, "AffineRelation", None)
                    
                    setattr(item, "AffineRelation", self)
                    

    @property
    def adfg_Graph(self):
        return self.__adfg_Graph

    @adfg_Graph.setter
    def adfg_Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adfg_Graph__adfg_Graph", None)
        self.__adfg_Graph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adfg_GraphConnection"):
                opp_val = getattr(old_value, "adfg_GraphConnection", None)
                if opp_val == self:
                    setattr(old_value, "adfg_GraphConnection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adfg_GraphConnection"):
                opp_val = getattr(value, "adfg_GraphConnection", None)
                setattr(value, "adfg_GraphConnection", self)

    @property
    def owner5(self):
        return self.__owner5

    @owner5.setter
    def owner5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adfg_Graph__owner5", None)
        self.__owner5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Actor"):
                    opp_val = getattr(item, "Actor", None)
                    
                    if opp_val == self:
                        setattr(item, "Actor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Actor"):
                    opp_val = getattr(item, "Actor", None)
                    
                    setattr(item, "Actor", self)
                    

class adfg_Application:

    def __init__(self, nbGraphs: int, name: str, nbProcessors: int, dynamicChecking: bool, schedulingAlgorithm: str, sourceCode: str, owner: set["adfg_Graph"] = None, owner2: set["adfg_GraphConnection"] = None, Application: "adfg_Graph" = None, Application15: "adfg_GraphConnection" = None):
        self.nbGraphs = nbGraphs
        self.name = name
        self.nbProcessors = nbProcessors
        self.dynamicChecking = dynamicChecking
        self.schedulingAlgorithm = schedulingAlgorithm
        self.sourceCode = sourceCode
        self.owner = owner if owner is not None else set()
        self.owner2 = owner2 if owner2 is not None else set()
        self.Application = Application
        self.Application15 = Application15
        
    @property
    def dynamicChecking(self) -> bool:
        return self.__dynamicChecking

    @dynamicChecking.setter
    def dynamicChecking(self, dynamicChecking: bool):
        self.__dynamicChecking = dynamicChecking

    @property
    def sourceCode(self) -> str:
        return self.__sourceCode

    @sourceCode.setter
    def sourceCode(self, sourceCode: str):
        self.__sourceCode = sourceCode

    @property
    def nbProcessors(self) -> int:
        return self.__nbProcessors

    @nbProcessors.setter
    def nbProcessors(self, nbProcessors: int):
        self.__nbProcessors = nbProcessors

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def nbGraphs(self) -> int:
        return self.__nbGraphs

    @nbGraphs.setter
    def nbGraphs(self, nbGraphs: int):
        self.__nbGraphs = nbGraphs

    @property
    def schedulingAlgorithm(self) -> str:
        return self.__schedulingAlgorithm

    @schedulingAlgorithm.setter
    def schedulingAlgorithm(self, schedulingAlgorithm: str):
        self.__schedulingAlgorithm = schedulingAlgorithm

    @property
    def Application(self):
        return self.__Application

    @Application.setter
    def Application(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adfg_Application__Application", None)
        self.__Application = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphs"):
                opp_val = getattr(old_value, "graphs", None)
                if opp_val == self:
                    setattr(old_value, "graphs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphs"):
                opp_val = getattr(value, "graphs", None)
                setattr(value, "graphs", self)

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adfg_Application__owner", None)
        self.__owner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Graph"):
                    opp_val = getattr(item, "Graph", None)
                    
                    if opp_val == self:
                        setattr(item, "Graph", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Graph"):
                    opp_val = getattr(item, "Graph", None)
                    
                    setattr(item, "Graph", self)
                    

    @property
    def owner2(self):
        return self.__owner2

    @owner2.setter
    def owner2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adfg_Application__owner2", None)
        self.__owner2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GraphConnection"):
                    opp_val = getattr(item, "GraphConnection", None)
                    
                    if opp_val == self:
                        setattr(item, "GraphConnection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GraphConnection"):
                    opp_val = getattr(item, "GraphConnection", None)
                    
                    setattr(item, "GraphConnection", self)
                    

    @property
    def Application15(self):
        return self.__Application15

    @Application15.setter
    def Application15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adfg_Application__Application15", None)
        self.__Application15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphConnections"):
                opp_val = getattr(old_value, "GraphConnections", None)
                if opp_val == self:
                    setattr(old_value, "GraphConnections", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphConnections"):
                opp_val = getattr(value, "GraphConnections", None)
                setattr(value, "GraphConnections", self)
