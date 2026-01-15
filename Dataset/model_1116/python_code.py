from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Optimizer(Enum):
    RLE = "RLE"
    KTAIL = "KTAIL"
class FSMCombinator(Enum):
    AND = "AND"
    OR = "OR"
    NAND = "NAND"
    NOR = "NOR"
    NOT = "NOT"
class FSMComparator(Enum):
    EQ = "EQ"
    NEQ = "NEQ"
    GREATER = "GREATER"
    SMALLER = "SMALLER"
    GREQ = "GREQ"
    SMEQ = "SMEQ"
class FSMOp(Enum):
    ADD = "ADD"
    SET = "SET"


############################################
# Definition of Classes
############################################

class PartitionToActorSelectionScheduleMap:

    pass
class FSMCombination:

    pass
class analysis_scheduling_MarkovSchedulingState:

    def __init__(self, name: str, firings: str, analysis_scheduling_MarkovSchedulingState: "scheduling_analysis_Actor" = None, MarkovSchedulingTransition455: set["MarkovSchedulingTransition"] = None, MarkovSchedulingTransition457: set["MarkovSchedulingTransition"] = None):
        self.name = name
        self.firings = firings
        self.analysis_scheduling_MarkovSchedulingState = analysis_scheduling_MarkovSchedulingState
        self.MarkovSchedulingTransition455 = MarkovSchedulingTransition455 if MarkovSchedulingTransition455 is not None else set()
        self.MarkovSchedulingTransition457 = MarkovSchedulingTransition457 if MarkovSchedulingTransition457 is not None else set()
        
    @property
    def firings(self) -> str:
        return self.__firings

    @firings.setter
    def firings(self, firings: str):
        self.__firings = firings

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MarkovSchedulingTransition455(self):
        return self.__MarkovSchedulingTransition455

    @MarkovSchedulingTransition455.setter
    def MarkovSchedulingTransition455(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_scheduling_MarkovSchedulingState__MarkovSchedulingTransition455", None)
        self.__MarkovSchedulingTransition455 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scheduling"):
                    opp_val = getattr(item, "scheduling", None)
                    
                    if opp_val == self:
                        setattr(item, "scheduling", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scheduling"):
                    opp_val = getattr(item, "scheduling", None)
                    
                    setattr(item, "scheduling", self)
                    

    @property
    def MarkovSchedulingTransition457(self):
        return self.__MarkovSchedulingTransition457

    @MarkovSchedulingTransition457.setter
    def MarkovSchedulingTransition457(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_scheduling_MarkovSchedulingState__MarkovSchedulingTransition457", None)
        self.__MarkovSchedulingTransition457 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scheduling458"):
                    opp_val = getattr(item, "scheduling458", None)
                    
                    if opp_val == self:
                        setattr(item, "scheduling458", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scheduling458"):
                    opp_val = getattr(item, "scheduling458", None)
                    
                    setattr(item, "scheduling458", self)
                    

    @property
    def analysis_scheduling_MarkovSchedulingState(self):
        return self.__analysis_scheduling_MarkovSchedulingState

    @analysis_scheduling_MarkovSchedulingState.setter
    def analysis_scheduling_MarkovSchedulingState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_scheduling_MarkovSchedulingState__analysis_scheduling_MarkovSchedulingState", None)
        self.__analysis_scheduling_MarkovSchedulingState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scheduling_analysis_Actor453"):
                opp_val = getattr(old_value, "scheduling_analysis_Actor453", None)
                if opp_val == self:
                    setattr(old_value, "scheduling_analysis_Actor453", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scheduling_analysis_Actor453"):
                opp_val = getattr(value, "scheduling_analysis_Actor453", None)
                setattr(value, "scheduling_analysis_Actor453", self)

class MarkovSchedulingTransition:

    pass
class MarkovSchedulingState:

    pass
class scheduling_analysis_Actor:

    pass
class analysis_scheduling_MarkovPartitionScheduler:

    def __init__(self, partitionId: str, analysis_scheduling_MarkovPartitionScheduler: set["scheduling_analysis_Actor"] = None, analysis_scheduling_MarkovPartitionScheduler449: set["MarkovSchedulingState"] = None, analysis_scheduling_MarkovPartitionScheduler451: set["MarkovSchedulingTransition"] = None):
        self.partitionId = partitionId
        self.analysis_scheduling_MarkovPartitionScheduler = analysis_scheduling_MarkovPartitionScheduler if analysis_scheduling_MarkovPartitionScheduler is not None else set()
        self.analysis_scheduling_MarkovPartitionScheduler449 = analysis_scheduling_MarkovPartitionScheduler449 if analysis_scheduling_MarkovPartitionScheduler449 is not None else set()
        self.analysis_scheduling_MarkovPartitionScheduler451 = analysis_scheduling_MarkovPartitionScheduler451 if analysis_scheduling_MarkovPartitionScheduler451 is not None else set()
        
    @property
    def partitionId(self) -> str:
        return self.__partitionId

    @partitionId.setter
    def partitionId(self, partitionId: str):
        self.__partitionId = partitionId

    @property
    def analysis_scheduling_MarkovPartitionScheduler449(self):
        return self.__analysis_scheduling_MarkovPartitionScheduler449

    @analysis_scheduling_MarkovPartitionScheduler449.setter
    def analysis_scheduling_MarkovPartitionScheduler449(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_scheduling_MarkovPartitionScheduler__analysis_scheduling_MarkovPartitionScheduler449", None)
        self.__analysis_scheduling_MarkovPartitionScheduler449 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MarkovSchedulingState"):
                    opp_val = getattr(item, "MarkovSchedulingState", None)
                    
                    if opp_val == self:
                        setattr(item, "MarkovSchedulingState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MarkovSchedulingState"):
                    opp_val = getattr(item, "MarkovSchedulingState", None)
                    
                    setattr(item, "MarkovSchedulingState", self)
                    

    @property
    def analysis_scheduling_MarkovPartitionScheduler451(self):
        return self.__analysis_scheduling_MarkovPartitionScheduler451

    @analysis_scheduling_MarkovPartitionScheduler451.setter
    def analysis_scheduling_MarkovPartitionScheduler451(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_scheduling_MarkovPartitionScheduler__analysis_scheduling_MarkovPartitionScheduler451", None)
        self.__analysis_scheduling_MarkovPartitionScheduler451 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MarkovSchedulingTransition"):
                    opp_val = getattr(item, "MarkovSchedulingTransition", None)
                    
                    if opp_val == self:
                        setattr(item, "MarkovSchedulingTransition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MarkovSchedulingTransition"):
                    opp_val = getattr(item, "MarkovSchedulingTransition", None)
                    
                    setattr(item, "MarkovSchedulingTransition", self)
                    

    @property
    def analysis_scheduling_MarkovPartitionScheduler(self):
        return self.__analysis_scheduling_MarkovPartitionScheduler

    @analysis_scheduling_MarkovPartitionScheduler.setter
    def analysis_scheduling_MarkovPartitionScheduler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_scheduling_MarkovPartitionScheduler__analysis_scheduling_MarkovPartitionScheduler", None)
        self.__analysis_scheduling_MarkovPartitionScheduler = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scheduling_analysis_Actor"):
                    opp_val = getattr(item, "scheduling_analysis_Actor", None)
                    
                    if opp_val == self:
                        setattr(item, "scheduling_analysis_Actor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scheduling_analysis_Actor"):
                    opp_val = getattr(item, "scheduling_analysis_Actor", None)
                    
                    setattr(item, "scheduling_analysis_Actor", self)
                    

    def getAssociatedState(self, actor: str) -> str:
        # TODO: Implement getAssociatedState method
        pass

class scheduling_analysis_Network:

    pass
class MarkovPartitionScheduler:

    pass
class analysis_scheduling_MarkovSchedulingTransition:

    def __init__(self, firings: str, name: str, MarkovSchedulingState460: "MarkovSchedulingState" = None, MarkovSchedulingState463: "MarkovSchedulingState" = None):
        self.firings = firings
        self.name = name
        self.MarkovSchedulingState460 = MarkovSchedulingState460
        self.MarkovSchedulingState463 = MarkovSchedulingState463
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def firings(self) -> str:
        return self.__firings

    @firings.setter
    def firings(self, firings: str):
        self.__firings = firings

    @property
    def MarkovSchedulingState460(self):
        return self.__MarkovSchedulingState460

    @MarkovSchedulingState460.setter
    def MarkovSchedulingState460(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_scheduling_MarkovSchedulingTransition__MarkovSchedulingState460", None)
        self.__MarkovSchedulingState460 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scheduling461"):
                opp_val = getattr(old_value, "scheduling461", None)
                if opp_val == self:
                    setattr(old_value, "scheduling461", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scheduling461"):
                opp_val = getattr(value, "scheduling461", None)
                setattr(value, "scheduling461", self)

    @property
    def MarkovSchedulingState463(self):
        return self.__MarkovSchedulingState463

    @MarkovSchedulingState463.setter
    def MarkovSchedulingState463(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_scheduling_MarkovSchedulingTransition__MarkovSchedulingState463", None)
        self.__MarkovSchedulingState463 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scheduling464"):
                opp_val = getattr(old_value, "scheduling464", None)
                if opp_val == self:
                    setattr(old_value, "scheduling464", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scheduling464"):
                opp_val = getattr(value, "scheduling464", None)
                setattr(value, "scheduling464", self)

class analysis_scheduling_FSMCondition:

    def __init__(self, comp: str, valName: str, compval: str, analysis_scheduling_FSMCondition: "FSMCombination" = None):
        self.comp = comp
        self.valName = valName
        self.compval = compval
        self.analysis_scheduling_FSMCondition = analysis_scheduling_FSMCondition
        
    @property
    def valName(self) -> str:
        return self.__valName

    @valName.setter
    def valName(self, valName: str):
        self.__valName = valName

    @property
    def compval(self) -> str:
        return self.__compval

    @compval.setter
    def compval(self, compval: str):
        self.__compval = compval

    @property
    def comp(self) -> str:
        return self.__comp

    @comp.setter
    def comp(self, comp: str):
        self.__comp = comp

    @property
    def analysis_scheduling_FSMCondition(self):
        return self.__analysis_scheduling_FSMCondition

    @analysis_scheduling_FSMCondition.setter
    def analysis_scheduling_FSMCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_scheduling_FSMCondition__analysis_scheduling_FSMCondition", None)
        self.__analysis_scheduling_FSMCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMCombination"):
                opp_val = getattr(old_value, "FSMCombination", None)
                if opp_val == self:
                    setattr(old_value, "FSMCombination", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMCombination"):
                opp_val = getattr(value, "FSMCombination", None)
                setattr(value, "FSMCombination", self)

class analysis_scheduling_FSMCombination:

    def __init__(self, combinator: str, analysis_scheduling_FSMCombination: "FSMCondition" = None):
        self.combinator = combinator
        self.analysis_scheduling_FSMCombination = analysis_scheduling_FSMCombination
        
    @property
    def combinator(self) -> str:
        return self.__combinator

    @combinator.setter
    def combinator(self, combinator: str):
        self.__combinator = combinator

    @property
    def analysis_scheduling_FSMCombination(self):
        return self.__analysis_scheduling_FSMCombination

    @analysis_scheduling_FSMCombination.setter
    def analysis_scheduling_FSMCombination(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_scheduling_FSMCombination__analysis_scheduling_FSMCombination", None)
        self.__analysis_scheduling_FSMCombination = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMCondition440"):
                opp_val = getattr(old_value, "FSMCondition440", None)
                if opp_val == self:
                    setattr(old_value, "FSMCondition440", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMCondition440"):
                opp_val = getattr(value, "FSMCondition440", None)
                setattr(value, "FSMCondition440", self)

class analysis_scheduling_FSMOperation:

    def __init__(self, op: str, val: str, var: str):
        self.op = op
        self.val = val
        self.var = var
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def var(self) -> str:
        return self.__var

    @var.setter
    def var(self, var: str):
        self.__var = var

    @property
    def val(self) -> str:
        return self.__val

    @val.setter
    def val(self, val: str):
        self.__val = val

class analysis_scheduling_FSMVar:

    def __init__(self, name: str, initialVal: str, type: str):
        self.name = name
        self.initialVal = initialVal
        self.type = type
        
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
    def initialVal(self) -> str:
        return self.__initialVal

    @initialVal.setter
    def initialVal(self, initialVal: str):
        self.__initialVal = initialVal

class FSMOperation:

    pass
class analysis_scheduling_FSMVarUpdate:

    pass
class FSMTransition:

    pass
class analysis_scheduling_FSMTransitionWithState(FSMTransition):

    pass
class FSMVarUpdate:

    pass
class analysis_scheduling_FSMState:

    def __init__(self, enumName: str, analysis_scheduling_FSMState: set["FSMVarUpdate"] = None, analysis_scheduling_FSMState434: set["FSMTransition"] = None):
        self.enumName = enumName
        self.analysis_scheduling_FSMState = analysis_scheduling_FSMState if analysis_scheduling_FSMState is not None else set()
        self.analysis_scheduling_FSMState434 = analysis_scheduling_FSMState434 if analysis_scheduling_FSMState434 is not None else set()
        
    @property
    def enumName(self) -> str:
        return self.__enumName

    @enumName.setter
    def enumName(self, enumName: str):
        self.__enumName = enumName

    @property
    def analysis_scheduling_FSMState434(self):
        return self.__analysis_scheduling_FSMState434

    @analysis_scheduling_FSMState434.setter
    def analysis_scheduling_FSMState434(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_scheduling_FSMState__analysis_scheduling_FSMState434", None)
        self.__analysis_scheduling_FSMState434 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FSMTransition"):
                    opp_val = getattr(item, "FSMTransition", None)
                    
                    if opp_val == self:
                        setattr(item, "FSMTransition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FSMTransition"):
                    opp_val = getattr(item, "FSMTransition", None)
                    
                    setattr(item, "FSMTransition", self)
                    

    @property
    def analysis_scheduling_FSMState(self):
        return self.__analysis_scheduling_FSMState

    @analysis_scheduling_FSMState.setter
    def analysis_scheduling_FSMState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_scheduling_FSMState__analysis_scheduling_FSMState", None)
        self.__analysis_scheduling_FSMState = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FSMVarUpdate"):
                    opp_val = getattr(item, "FSMVarUpdate", None)
                    
                    if opp_val == self:
                        setattr(item, "FSMVarUpdate", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FSMVarUpdate"):
                    opp_val = getattr(item, "FSMVarUpdate", None)
                    
                    setattr(item, "FSMVarUpdate", self)
                    

class Sequence:

    pass
class FSMCondition:

    pass
class analysis_scheduling_FSMTransition:

    def __init__(self, targetStateEnumName: str, sourceStateEnumName: str, analysis_scheduling_FSMTransition: "FSMCondition" = None, analysis_scheduling_FSMTransition431: "Sequence" = None):
        self.targetStateEnumName = targetStateEnumName
        self.sourceStateEnumName = sourceStateEnumName
        self.analysis_scheduling_FSMTransition = analysis_scheduling_FSMTransition
        self.analysis_scheduling_FSMTransition431 = analysis_scheduling_FSMTransition431
        
    @property
    def sourceStateEnumName(self) -> str:
        return self.__sourceStateEnumName

    @sourceStateEnumName.setter
    def sourceStateEnumName(self, sourceStateEnumName: str):
        self.__sourceStateEnumName = sourceStateEnumName

    @property
    def targetStateEnumName(self) -> str:
        return self.__targetStateEnumName

    @targetStateEnumName.setter
    def targetStateEnumName(self, targetStateEnumName: str):
        self.__targetStateEnumName = targetStateEnumName

    @property
    def analysis_scheduling_FSMTransition(self):
        return self.__analysis_scheduling_FSMTransition

    @analysis_scheduling_FSMTransition.setter
    def analysis_scheduling_FSMTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_scheduling_FSMTransition__analysis_scheduling_FSMTransition", None)
        self.__analysis_scheduling_FSMTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMCondition"):
                opp_val = getattr(old_value, "FSMCondition", None)
                if opp_val == self:
                    setattr(old_value, "FSMCondition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMCondition"):
                opp_val = getattr(value, "FSMCondition", None)
                setattr(value, "FSMCondition", self)

    @property
    def analysis_scheduling_FSMTransition431(self):
        return self.__analysis_scheduling_FSMTransition431

    @analysis_scheduling_FSMTransition431.setter
    def analysis_scheduling_FSMTransition431(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_scheduling_FSMTransition__analysis_scheduling_FSMTransition431", None)
        self.__analysis_scheduling_FSMTransition431 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Sequence"):
                opp_val = getattr(old_value, "Sequence", None)
                if opp_val == self:
                    setattr(old_value, "Sequence", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Sequence"):
                opp_val = getattr(value, "Sequence", None)
                setattr(value, "Sequence", self)

class ActorFire:

    pass
class analysis_scheduling_PartitionedActorFire(ActorFire):

    pass
class analysis_scheduling_ActorSelectionSchedule(ABC):

    pass
class FSMVar:

    pass
class FSMState:

    pass
class analysis_profiling_ProfilingStatsActorData:

    def __init__(self, actorName: str, actionsWeight: float, schedulerWeight: float, actionsWeightPercent: float, schedulerWeightPercent: float):
        self.actorName = actorName
        self.actionsWeight = actionsWeight
        self.schedulerWeight = schedulerWeight
        self.actionsWeightPercent = actionsWeightPercent
        self.schedulerWeightPercent = schedulerWeightPercent
        
    @property
    def actionsWeight(self) -> float:
        return self.__actionsWeight

    @actionsWeight.setter
    def actionsWeight(self, actionsWeight: float):
        self.__actionsWeight = actionsWeight

    @property
    def schedulerWeight(self) -> float:
        return self.__schedulerWeight

    @schedulerWeight.setter
    def schedulerWeight(self, schedulerWeight: float):
        self.__schedulerWeight = schedulerWeight

    @property
    def actionsWeightPercent(self) -> float:
        return self.__actionsWeightPercent

    @actionsWeightPercent.setter
    def actionsWeightPercent(self, actionsWeightPercent: float):
        self.__actionsWeightPercent = actionsWeightPercent

    @property
    def schedulerWeightPercent(self) -> float:
        return self.__schedulerWeightPercent

    @schedulerWeightPercent.setter
    def schedulerWeightPercent(self, schedulerWeightPercent: float):
        self.__schedulerWeightPercent = schedulerWeightPercent

    @property
    def actorName(self) -> str:
        return self.__actorName

    @actorName.setter
    def actorName(self, actorName: str):
        self.__actorName = actorName

class ProfilingStatsActorData:

    pass
class profiling_analysis_Action:

    pass
class analysis_profiling_IntraActionCommunicationData:

    pass
class IntraActionCommunicationData:

    pass
class profiling_analysis_StatisticalData:

    pass
class profiling_analysis_Actor:

    pass
class analysis_profiling_IntraActorCommunicationData:

    pass
class profiling_analysis_Network:

    pass
class IntraActorCommunicationData:

    pass
class ActorToStatisticalDataMap:

    pass
class postprocessing_analysis_StatisticalData:

    pass
class analysis_postprocessing_SchedulerChecksPartition:

    pass
class SchedulerChecksPartition:

    pass
class ActionToDoubleMap:

    pass
class postprocessing_analysis_Actor:

    pass
class analysis_postprocessing_StatisticalActorPartition:

    def __init__(self, actors: str, occupancy: float, schedulingPolicy: str):
        self.actors = actors
        self.occupancy = occupancy
        self.schedulingPolicy = schedulingPolicy
        
    @property
    def actors(self) -> str:
        return self.__actors

    @actors.setter
    def actors(self, actors: str):
        self.__actors = actors

    @property
    def schedulingPolicy(self) -> str:
        return self.__schedulingPolicy

    @schedulingPolicy.setter
    def schedulingPolicy(self, schedulingPolicy: str):
        self.__schedulingPolicy = schedulingPolicy

    @property
    def occupancy(self) -> float:
        return self.__occupancy

    @occupancy.setter
    def occupancy(self, occupancy: float):
        self.__occupancy = occupancy

class StatisticalActorPartition:

    pass
class analysis_postprocessing_PostProcessingData(ABC):

    pass
class PostProcessingData:

    pass
class analysis_postprocessing_ActionStatisticsReport(PostProcessingData):

    pass
class analysis_postprocessing_SchedulerChecksReport(PostProcessingData):

    pass
class analysis_postprocessing_BufferBlockingReport(PostProcessingData):

    pass
class analysis_postprocessing_ActorStatisticsReport(PostProcessingData):

    def __init__(self, executionTime: float, averageOccupancy: float, occupancyDeviation: float, analysis_postprocessing_ActorStatisticsReport: "postprocessing_analysis_Network" = None, analysis_postprocessing_ActorStatisticsReport333: set["StatisticalActorPartition"] = None, analysis_postprocessing_ActorStatisticsReport335: set["StringToDoubleMap"] = None, analysis_postprocessing_ActorStatisticsReport338: set["StringToDoubleMap"] = None, analysis_postprocessing_ActorStatisticsReport341: set["StringToDoubleMap"] = None, analysis_postprocessing_ActorStatisticsReport344: set["StringToDoubleMap"] = None, PostProcessingData: "analysis_postprocessing_PostProcessingReport"):
        self.executionTime = executionTime
        self.averageOccupancy = averageOccupancy
        self.occupancyDeviation = occupancyDeviation
        self.analysis_postprocessing_ActorStatisticsReport = analysis_postprocessing_ActorStatisticsReport
        self.analysis_postprocessing_ActorStatisticsReport333 = analysis_postprocessing_ActorStatisticsReport333 if analysis_postprocessing_ActorStatisticsReport333 is not None else set()
        self.analysis_postprocessing_ActorStatisticsReport335 = analysis_postprocessing_ActorStatisticsReport335 if analysis_postprocessing_ActorStatisticsReport335 is not None else set()
        self.analysis_postprocessing_ActorStatisticsReport338 = analysis_postprocessing_ActorStatisticsReport338 if analysis_postprocessing_ActorStatisticsReport338 is not None else set()
        self.analysis_postprocessing_ActorStatisticsReport341 = analysis_postprocessing_ActorStatisticsReport341 if analysis_postprocessing_ActorStatisticsReport341 is not None else set()
        self.analysis_postprocessing_ActorStatisticsReport344 = analysis_postprocessing_ActorStatisticsReport344 if analysis_postprocessing_ActorStatisticsReport344 is not None else set()
        
    @property
    def executionTime(self) -> float:
        return self.__executionTime

    @executionTime.setter
    def executionTime(self, executionTime: float):
        self.__executionTime = executionTime

    @property
    def occupancyDeviation(self) -> float:
        return self.__occupancyDeviation

    @occupancyDeviation.setter
    def occupancyDeviation(self, occupancyDeviation: float):
        self.__occupancyDeviation = occupancyDeviation

    @property
    def averageOccupancy(self) -> float:
        return self.__averageOccupancy

    @averageOccupancy.setter
    def averageOccupancy(self, averageOccupancy: float):
        self.__averageOccupancy = averageOccupancy

    @property
    def analysis_postprocessing_ActorStatisticsReport335(self):
        return self.__analysis_postprocessing_ActorStatisticsReport335

    @analysis_postprocessing_ActorStatisticsReport335.setter
    def analysis_postprocessing_ActorStatisticsReport335(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_postprocessing_ActorStatisticsReport__analysis_postprocessing_ActorStatisticsReport335", None)
        self.__analysis_postprocessing_ActorStatisticsReport335 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StringToDoubleMap336"):
                    opp_val = getattr(item, "StringToDoubleMap336", None)
                    
                    if opp_val == self:
                        setattr(item, "StringToDoubleMap336", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StringToDoubleMap336"):
                    opp_val = getattr(item, "StringToDoubleMap336", None)
                    
                    setattr(item, "StringToDoubleMap336", self)
                    

    @property
    def analysis_postprocessing_ActorStatisticsReport341(self):
        return self.__analysis_postprocessing_ActorStatisticsReport341

    @analysis_postprocessing_ActorStatisticsReport341.setter
    def analysis_postprocessing_ActorStatisticsReport341(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_postprocessing_ActorStatisticsReport__analysis_postprocessing_ActorStatisticsReport341", None)
        self.__analysis_postprocessing_ActorStatisticsReport341 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StringToDoubleMap342"):
                    opp_val = getattr(item, "StringToDoubleMap342", None)
                    
                    if opp_val == self:
                        setattr(item, "StringToDoubleMap342", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StringToDoubleMap342"):
                    opp_val = getattr(item, "StringToDoubleMap342", None)
                    
                    setattr(item, "StringToDoubleMap342", self)
                    

    @property
    def analysis_postprocessing_ActorStatisticsReport(self):
        return self.__analysis_postprocessing_ActorStatisticsReport

    @analysis_postprocessing_ActorStatisticsReport.setter
    def analysis_postprocessing_ActorStatisticsReport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_postprocessing_ActorStatisticsReport__analysis_postprocessing_ActorStatisticsReport", None)
        self.__analysis_postprocessing_ActorStatisticsReport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "postprocessing_analysis_Network331"):
                opp_val = getattr(old_value, "postprocessing_analysis_Network331", None)
                if opp_val == self:
                    setattr(old_value, "postprocessing_analysis_Network331", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "postprocessing_analysis_Network331"):
                opp_val = getattr(value, "postprocessing_analysis_Network331", None)
                setattr(value, "postprocessing_analysis_Network331", self)

    @property
    def analysis_postprocessing_ActorStatisticsReport333(self):
        return self.__analysis_postprocessing_ActorStatisticsReport333

    @analysis_postprocessing_ActorStatisticsReport333.setter
    def analysis_postprocessing_ActorStatisticsReport333(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_postprocessing_ActorStatisticsReport__analysis_postprocessing_ActorStatisticsReport333", None)
        self.__analysis_postprocessing_ActorStatisticsReport333 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StatisticalActorPartition"):
                    opp_val = getattr(item, "StatisticalActorPartition", None)
                    
                    if opp_val == self:
                        setattr(item, "StatisticalActorPartition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StatisticalActorPartition"):
                    opp_val = getattr(item, "StatisticalActorPartition", None)
                    
                    setattr(item, "StatisticalActorPartition", self)
                    

    @property
    def analysis_postprocessing_ActorStatisticsReport338(self):
        return self.__analysis_postprocessing_ActorStatisticsReport338

    @analysis_postprocessing_ActorStatisticsReport338.setter
    def analysis_postprocessing_ActorStatisticsReport338(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_postprocessing_ActorStatisticsReport__analysis_postprocessing_ActorStatisticsReport338", None)
        self.__analysis_postprocessing_ActorStatisticsReport338 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StringToDoubleMap339"):
                    opp_val = getattr(item, "StringToDoubleMap339", None)
                    
                    if opp_val == self:
                        setattr(item, "StringToDoubleMap339", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StringToDoubleMap339"):
                    opp_val = getattr(item, "StringToDoubleMap339", None)
                    
                    setattr(item, "StringToDoubleMap339", self)
                    

    @property
    def analysis_postprocessing_ActorStatisticsReport344(self):
        return self.__analysis_postprocessing_ActorStatisticsReport344

    @analysis_postprocessing_ActorStatisticsReport344.setter
    def analysis_postprocessing_ActorStatisticsReport344(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_postprocessing_ActorStatisticsReport__analysis_postprocessing_ActorStatisticsReport344", None)
        self.__analysis_postprocessing_ActorStatisticsReport344 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StringToDoubleMap345"):
                    opp_val = getattr(item, "StringToDoubleMap345", None)
                    
                    if opp_val == self:
                        setattr(item, "StringToDoubleMap345", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StringToDoubleMap345"):
                    opp_val = getattr(item, "StringToDoubleMap345", None)
                    
                    setattr(item, "StringToDoubleMap345", self)
                    

class postprocessing_analysis_Network:

    pass
class pipelining_analysis_ActorClass:

    pass
class analysis_pipelining_ImpactAnalysisData:

    def __init__(self, cpReduction: float, analysis_pipelining_ImpactAnalysisData: "BottlenecksReport" = None, analysis_pipelining_ImpactAnalysisData323: set["pipelining_analysis_Action"] = None, analysis_pipelining_ImpactAnalysisData326: "pipelining_analysis_ActorClass" = None):
        self.cpReduction = cpReduction
        self.analysis_pipelining_ImpactAnalysisData = analysis_pipelining_ImpactAnalysisData
        self.analysis_pipelining_ImpactAnalysisData323 = analysis_pipelining_ImpactAnalysisData323 if analysis_pipelining_ImpactAnalysisData323 is not None else set()
        self.analysis_pipelining_ImpactAnalysisData326 = analysis_pipelining_ImpactAnalysisData326
        
    @property
    def cpReduction(self) -> float:
        return self.__cpReduction

    @cpReduction.setter
    def cpReduction(self, cpReduction: float):
        self.__cpReduction = cpReduction

    @property
    def analysis_pipelining_ImpactAnalysisData326(self):
        return self.__analysis_pipelining_ImpactAnalysisData326

    @analysis_pipelining_ImpactAnalysisData326.setter
    def analysis_pipelining_ImpactAnalysisData326(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_pipelining_ImpactAnalysisData__analysis_pipelining_ImpactAnalysisData326", None)
        self.__analysis_pipelining_ImpactAnalysisData326 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pipelining_analysis_ActorClass"):
                opp_val = getattr(old_value, "pipelining_analysis_ActorClass", None)
                if opp_val == self:
                    setattr(old_value, "pipelining_analysis_ActorClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pipelining_analysis_ActorClass"):
                opp_val = getattr(value, "pipelining_analysis_ActorClass", None)
                setattr(value, "pipelining_analysis_ActorClass", self)

    @property
    def analysis_pipelining_ImpactAnalysisData(self):
        return self.__analysis_pipelining_ImpactAnalysisData

    @analysis_pipelining_ImpactAnalysisData.setter
    def analysis_pipelining_ImpactAnalysisData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_pipelining_ImpactAnalysisData__analysis_pipelining_ImpactAnalysisData", None)
        self.__analysis_pipelining_ImpactAnalysisData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BottlenecksReport321"):
                opp_val = getattr(old_value, "BottlenecksReport321", None)
                if opp_val == self:
                    setattr(old_value, "BottlenecksReport321", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BottlenecksReport321"):
                opp_val = getattr(value, "BottlenecksReport321", None)
                setattr(value, "BottlenecksReport321", self)

    @property
    def analysis_pipelining_ImpactAnalysisData323(self):
        return self.__analysis_pipelining_ImpactAnalysisData323

    @analysis_pipelining_ImpactAnalysisData323.setter
    def analysis_pipelining_ImpactAnalysisData323(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_pipelining_ImpactAnalysisData__analysis_pipelining_ImpactAnalysisData323", None)
        self.__analysis_pipelining_ImpactAnalysisData323 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pipelining_analysis_Action324"):
                    opp_val = getattr(item, "pipelining_analysis_Action324", None)
                    
                    if opp_val == self:
                        setattr(item, "pipelining_analysis_Action324", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pipelining_analysis_Action324"):
                    opp_val = getattr(item, "pipelining_analysis_Action324", None)
                    
                    setattr(item, "pipelining_analysis_Action324", self)
                    

class ActionsVariablePipeliningReport:

    pass
class pipelining_analysis_StatisticalData:

    pass
class pipelining_analysis_Action:

    pass
class analysis_pipelining_ActionVariablePipeliningData:

    def __init__(self, pipelinable: bool, analysis_pipelining_ActionVariablePipeliningData: "pipelining_analysis_Action" = None, analysis_pipelining_ActionVariablePipeliningData306: "pipelining_analysis_StatisticalData" = None, analysis_pipelining_ActionVariablePipeliningData308: "pipelining_analysis_StatisticalData" = None):
        self.pipelinable = pipelinable
        self.analysis_pipelining_ActionVariablePipeliningData = analysis_pipelining_ActionVariablePipeliningData
        self.analysis_pipelining_ActionVariablePipeliningData306 = analysis_pipelining_ActionVariablePipeliningData306
        self.analysis_pipelining_ActionVariablePipeliningData308 = analysis_pipelining_ActionVariablePipeliningData308
        
    @property
    def pipelinable(self) -> bool:
        return self.__pipelinable

    @pipelinable.setter
    def pipelinable(self, pipelinable: bool):
        self.__pipelinable = pipelinable

    @property
    def analysis_pipelining_ActionVariablePipeliningData308(self):
        return self.__analysis_pipelining_ActionVariablePipeliningData308

    @analysis_pipelining_ActionVariablePipeliningData308.setter
    def analysis_pipelining_ActionVariablePipeliningData308(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_pipelining_ActionVariablePipeliningData__analysis_pipelining_ActionVariablePipeliningData308", None)
        self.__analysis_pipelining_ActionVariablePipeliningData308 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pipelining_analysis_StatisticalData309"):
                opp_val = getattr(old_value, "pipelining_analysis_StatisticalData309", None)
                if opp_val == self:
                    setattr(old_value, "pipelining_analysis_StatisticalData309", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pipelining_analysis_StatisticalData309"):
                opp_val = getattr(value, "pipelining_analysis_StatisticalData309", None)
                setattr(value, "pipelining_analysis_StatisticalData309", self)

    @property
    def analysis_pipelining_ActionVariablePipeliningData306(self):
        return self.__analysis_pipelining_ActionVariablePipeliningData306

    @analysis_pipelining_ActionVariablePipeliningData306.setter
    def analysis_pipelining_ActionVariablePipeliningData306(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_pipelining_ActionVariablePipeliningData__analysis_pipelining_ActionVariablePipeliningData306", None)
        self.__analysis_pipelining_ActionVariablePipeliningData306 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pipelining_analysis_StatisticalData"):
                opp_val = getattr(old_value, "pipelining_analysis_StatisticalData", None)
                if opp_val == self:
                    setattr(old_value, "pipelining_analysis_StatisticalData", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pipelining_analysis_StatisticalData"):
                opp_val = getattr(value, "pipelining_analysis_StatisticalData", None)
                setattr(value, "pipelining_analysis_StatisticalData", self)

    @property
    def analysis_pipelining_ActionVariablePipeliningData(self):
        return self.__analysis_pipelining_ActionVariablePipeliningData

    @analysis_pipelining_ActionVariablePipeliningData.setter
    def analysis_pipelining_ActionVariablePipeliningData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_pipelining_ActionVariablePipeliningData__analysis_pipelining_ActionVariablePipeliningData", None)
        self.__analysis_pipelining_ActionVariablePipeliningData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pipelining_analysis_Action"):
                opp_val = getattr(old_value, "pipelining_analysis_Action", None)
                if opp_val == self:
                    setattr(old_value, "pipelining_analysis_Action", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pipelining_analysis_Action"):
                opp_val = getattr(value, "pipelining_analysis_Action", None)
                setattr(value, "pipelining_analysis_Action", self)

class ActionVariablePipeliningData:

    pass
class pipelining_analysis_Network:

    pass
class BalancedPipelinePartition:

    pass
class analysis_partitioning_BalancedPipelinePartition:

    def __init__(self, workload: float, preWorkload: float, commonPredAvg: float, analysis_partitioning_BalancedPipelinePartition: set["partitioning_analysis_Actor"] = None):
        self.workload = workload
        self.preWorkload = preWorkload
        self.commonPredAvg = commonPredAvg
        self.analysis_partitioning_BalancedPipelinePartition = analysis_partitioning_BalancedPipelinePartition if analysis_partitioning_BalancedPipelinePartition is not None else set()
        
    @property
    def workload(self) -> float:
        return self.__workload

    @workload.setter
    def workload(self, workload: float):
        self.__workload = workload

    @property
    def preWorkload(self) -> float:
        return self.__preWorkload

    @preWorkload.setter
    def preWorkload(self, preWorkload: float):
        self.__preWorkload = preWorkload

    @property
    def commonPredAvg(self) -> float:
        return self.__commonPredAvg

    @commonPredAvg.setter
    def commonPredAvg(self, commonPredAvg: float):
        self.__commonPredAvg = commonPredAvg

    @property
    def analysis_partitioning_BalancedPipelinePartition(self):
        return self.__analysis_partitioning_BalancedPipelinePartition

    @analysis_partitioning_BalancedPipelinePartition.setter
    def analysis_partitioning_BalancedPipelinePartition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_partitioning_BalancedPipelinePartition__analysis_partitioning_BalancedPipelinePartition", None)
        self.__analysis_partitioning_BalancedPipelinePartition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "partitioning_analysis_Actor296"):
                    opp_val = getattr(item, "partitioning_analysis_Actor296", None)
                    
                    if opp_val == self:
                        setattr(item, "partitioning_analysis_Actor296", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "partitioning_analysis_Actor296"):
                    opp_val = getattr(item, "partitioning_analysis_Actor296", None)
                    
                    setattr(item, "partitioning_analysis_Actor296", self)
                    

class WorkloadBalancePartition:

    pass
class analysis_partitioning_WorkloadBalancePartition:

    def __init__(self, workload: float, analysis_partitioning_WorkloadBalancePartition: set["partitioning_analysis_Actor"] = None):
        self.workload = workload
        self.analysis_partitioning_WorkloadBalancePartition = analysis_partitioning_WorkloadBalancePartition if analysis_partitioning_WorkloadBalancePartition is not None else set()
        
    @property
    def workload(self) -> float:
        return self.__workload

    @workload.setter
    def workload(self, workload: float):
        self.__workload = workload

    @property
    def analysis_partitioning_WorkloadBalancePartition(self):
        return self.__analysis_partitioning_WorkloadBalancePartition

    @analysis_partitioning_WorkloadBalancePartition.setter
    def analysis_partitioning_WorkloadBalancePartition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_partitioning_WorkloadBalancePartition__analysis_partitioning_WorkloadBalancePartition", None)
        self.__analysis_partitioning_WorkloadBalancePartition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "partitioning_analysis_Actor290"):
                    opp_val = getattr(item, "partitioning_analysis_Actor290", None)
                    
                    if opp_val == self:
                        setattr(item, "partitioning_analysis_Actor290", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "partitioning_analysis_Actor290"):
                    opp_val = getattr(item, "partitioning_analysis_Actor290", None)
                    
                    setattr(item, "partitioning_analysis_Actor290", self)
                    

class buffers_analysis_Buffer:

    pass
class analysis_buffers_BoundedBufferData:

    def __init__(self, tokenSize: int, bitSize: int, analysis_buffers_BoundedBufferData: "buffers_analysis_Buffer" = None):
        self.tokenSize = tokenSize
        self.bitSize = bitSize
        self.analysis_buffers_BoundedBufferData = analysis_buffers_BoundedBufferData
        
    @property
    def bitSize(self) -> int:
        return self.__bitSize

    @bitSize.setter
    def bitSize(self, bitSize: int):
        self.__bitSize = bitSize

    @property
    def tokenSize(self) -> int:
        return self.__tokenSize

    @tokenSize.setter
    def tokenSize(self, tokenSize: int):
        self.__tokenSize = tokenSize

    @property
    def analysis_buffers_BoundedBufferData(self):
        return self.__analysis_buffers_BoundedBufferData

    @analysis_buffers_BoundedBufferData.setter
    def analysis_buffers_BoundedBufferData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_buffers_BoundedBufferData__analysis_buffers_BoundedBufferData", None)
        self.__analysis_buffers_BoundedBufferData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "buffers_analysis_Buffer"):
                opp_val = getattr(old_value, "buffers_analysis_Buffer", None)
                if opp_val == self:
                    setattr(old_value, "buffers_analysis_Buffer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "buffers_analysis_Buffer"):
                opp_val = getattr(value, "buffers_analysis_Buffer", None)
                setattr(value, "buffers_analysis_Buffer", self)

class partitioning_analysis_Actor:

    pass
class analysis_partitioning_ComCostPartition:

    def __init__(self, internalCost: str, externalCost: str, analysis_partitioning_ComCostPartition284: set["ActorToLongMap"] = None, analysis_partitioning_ComCostPartition287: set["ActorToLongMap"] = None, analysis_partitioning_ComCostPartition: set["partitioning_analysis_Actor"] = None):
        self.internalCost = internalCost
        self.externalCost = externalCost
        self.analysis_partitioning_ComCostPartition284 = analysis_partitioning_ComCostPartition284 if analysis_partitioning_ComCostPartition284 is not None else set()
        self.analysis_partitioning_ComCostPartition287 = analysis_partitioning_ComCostPartition287 if analysis_partitioning_ComCostPartition287 is not None else set()
        self.analysis_partitioning_ComCostPartition = analysis_partitioning_ComCostPartition if analysis_partitioning_ComCostPartition is not None else set()
        
    @property
    def externalCost(self) -> str:
        return self.__externalCost

    @externalCost.setter
    def externalCost(self, externalCost: str):
        self.__externalCost = externalCost

    @property
    def internalCost(self) -> str:
        return self.__internalCost

    @internalCost.setter
    def internalCost(self, internalCost: str):
        self.__internalCost = internalCost

    @property
    def analysis_partitioning_ComCostPartition287(self):
        return self.__analysis_partitioning_ComCostPartition287

    @analysis_partitioning_ComCostPartition287.setter
    def analysis_partitioning_ComCostPartition287(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_partitioning_ComCostPartition__analysis_partitioning_ComCostPartition287", None)
        self.__analysis_partitioning_ComCostPartition287 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActorToLongMap288"):
                    opp_val = getattr(item, "ActorToLongMap288", None)
                    
                    if opp_val == self:
                        setattr(item, "ActorToLongMap288", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActorToLongMap288"):
                    opp_val = getattr(item, "ActorToLongMap288", None)
                    
                    setattr(item, "ActorToLongMap288", self)
                    

    @property
    def analysis_partitioning_ComCostPartition(self):
        return self.__analysis_partitioning_ComCostPartition

    @analysis_partitioning_ComCostPartition.setter
    def analysis_partitioning_ComCostPartition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_partitioning_ComCostPartition__analysis_partitioning_ComCostPartition", None)
        self.__analysis_partitioning_ComCostPartition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "partitioning_analysis_Actor"):
                    opp_val = getattr(item, "partitioning_analysis_Actor", None)
                    
                    if opp_val == self:
                        setattr(item, "partitioning_analysis_Actor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "partitioning_analysis_Actor"):
                    opp_val = getattr(item, "partitioning_analysis_Actor", None)
                    
                    setattr(item, "partitioning_analysis_Actor", self)
                    

    @property
    def analysis_partitioning_ComCostPartition284(self):
        return self.__analysis_partitioning_ComCostPartition284

    @analysis_partitioning_ComCostPartition284.setter
    def analysis_partitioning_ComCostPartition284(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_partitioning_ComCostPartition__analysis_partitioning_ComCostPartition284", None)
        self.__analysis_partitioning_ComCostPartition284 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActorToLongMap285"):
                    opp_val = getattr(item, "ActorToLongMap285", None)
                    
                    if opp_val == self:
                        setattr(item, "ActorToLongMap285", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActorToLongMap285"):
                    opp_val = getattr(item, "ActorToLongMap285", None)
                    
                    setattr(item, "ActorToLongMap285", self)
                    

class ComCostPartition:

    pass
class partitioning_analysis_Network:

    pass
class analysis_buffers_OptimalBufferData:

    pass
class BoundedBuffersReport:

    pass
class OptimalBufferData:

    pass
class BoundedBufferData:

    pass
class buffers_analysis_Network:

    pass
class ScheduledImpactAnalysisData:

    pass
class BottlenecksWithSchedulingReport:

    pass
class analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap:

    def __init__(self, key: str, analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap: "BottlenecksWithSchedulingReport" = None):
        self.key = key
        self.analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap = analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap(self):
        return self.__analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap

    @analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap.setter
    def analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap__analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap", None)
        self.__analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BottlenecksWithSchedulingReport"):
                opp_val = getattr(old_value, "BottlenecksWithSchedulingReport", None)
                if opp_val == self:
                    setattr(old_value, "BottlenecksWithSchedulingReport", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BottlenecksWithSchedulingReport"):
                opp_val = getattr(value, "BottlenecksWithSchedulingReport", None)
                setattr(value, "BottlenecksWithSchedulingReport", self)

class DoubleToBottlenecksWithSchedulingReportMap:

    pass
class postprocessing_PostProcessingData:

    pass
class analysis_bottlenecks_ScheduledImpactAnalysisData:

    pass
class BufferToDoubleMap:

    pass
class BufferToIntegerMap:

    pass
class analysis_bottlenecks_ActionBottlenecksWithSchedulingData:

    def __init__(self, cpWeight: float, totalWeight: float, cpFirings: str, totalFirings: str, analysis_bottlenecks_ActionBottlenecksWithSchedulingData: "bottlenecks_analysis_Action" = None, analysis_bottlenecks_ActionBottlenecksWithSchedulingData234: set["BufferToIntegerMap"] = None, analysis_bottlenecks_ActionBottlenecksWithSchedulingData236: set["BufferToDoubleMap"] = None, analysis_bottlenecks_ActionBottlenecksWithSchedulingData238: set["BufferToIntegerMap"] = None):
        self.cpWeight = cpWeight
        self.totalWeight = totalWeight
        self.cpFirings = cpFirings
        self.totalFirings = totalFirings
        self.analysis_bottlenecks_ActionBottlenecksWithSchedulingData = analysis_bottlenecks_ActionBottlenecksWithSchedulingData
        self.analysis_bottlenecks_ActionBottlenecksWithSchedulingData234 = analysis_bottlenecks_ActionBottlenecksWithSchedulingData234 if analysis_bottlenecks_ActionBottlenecksWithSchedulingData234 is not None else set()
        self.analysis_bottlenecks_ActionBottlenecksWithSchedulingData236 = analysis_bottlenecks_ActionBottlenecksWithSchedulingData236 if analysis_bottlenecks_ActionBottlenecksWithSchedulingData236 is not None else set()
        self.analysis_bottlenecks_ActionBottlenecksWithSchedulingData238 = analysis_bottlenecks_ActionBottlenecksWithSchedulingData238 if analysis_bottlenecks_ActionBottlenecksWithSchedulingData238 is not None else set()
        
    @property
    def totalWeight(self) -> float:
        return self.__totalWeight

    @totalWeight.setter
    def totalWeight(self, totalWeight: float):
        self.__totalWeight = totalWeight

    @property
    def cpFirings(self) -> str:
        return self.__cpFirings

    @cpFirings.setter
    def cpFirings(self, cpFirings: str):
        self.__cpFirings = cpFirings

    @property
    def totalFirings(self) -> str:
        return self.__totalFirings

    @totalFirings.setter
    def totalFirings(self, totalFirings: str):
        self.__totalFirings = totalFirings

    @property
    def cpWeight(self) -> float:
        return self.__cpWeight

    @cpWeight.setter
    def cpWeight(self, cpWeight: float):
        self.__cpWeight = cpWeight

    @property
    def analysis_bottlenecks_ActionBottlenecksWithSchedulingData238(self):
        return self.__analysis_bottlenecks_ActionBottlenecksWithSchedulingData238

    @analysis_bottlenecks_ActionBottlenecksWithSchedulingData238.setter
    def analysis_bottlenecks_ActionBottlenecksWithSchedulingData238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_bottlenecks_ActionBottlenecksWithSchedulingData__analysis_bottlenecks_ActionBottlenecksWithSchedulingData238", None)
        self.__analysis_bottlenecks_ActionBottlenecksWithSchedulingData238 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BufferToIntegerMap239"):
                    opp_val = getattr(item, "BufferToIntegerMap239", None)
                    
                    if opp_val == self:
                        setattr(item, "BufferToIntegerMap239", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BufferToIntegerMap239"):
                    opp_val = getattr(item, "BufferToIntegerMap239", None)
                    
                    setattr(item, "BufferToIntegerMap239", self)
                    

    @property
    def analysis_bottlenecks_ActionBottlenecksWithSchedulingData(self):
        return self.__analysis_bottlenecks_ActionBottlenecksWithSchedulingData

    @analysis_bottlenecks_ActionBottlenecksWithSchedulingData.setter
    def analysis_bottlenecks_ActionBottlenecksWithSchedulingData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_bottlenecks_ActionBottlenecksWithSchedulingData__analysis_bottlenecks_ActionBottlenecksWithSchedulingData", None)
        self.__analysis_bottlenecks_ActionBottlenecksWithSchedulingData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bottlenecks_analysis_Action232"):
                opp_val = getattr(old_value, "bottlenecks_analysis_Action232", None)
                if opp_val == self:
                    setattr(old_value, "bottlenecks_analysis_Action232", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bottlenecks_analysis_Action232"):
                opp_val = getattr(value, "bottlenecks_analysis_Action232", None)
                setattr(value, "bottlenecks_analysis_Action232", self)

    @property
    def analysis_bottlenecks_ActionBottlenecksWithSchedulingData236(self):
        return self.__analysis_bottlenecks_ActionBottlenecksWithSchedulingData236

    @analysis_bottlenecks_ActionBottlenecksWithSchedulingData236.setter
    def analysis_bottlenecks_ActionBottlenecksWithSchedulingData236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_bottlenecks_ActionBottlenecksWithSchedulingData__analysis_bottlenecks_ActionBottlenecksWithSchedulingData236", None)
        self.__analysis_bottlenecks_ActionBottlenecksWithSchedulingData236 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BufferToDoubleMap"):
                    opp_val = getattr(item, "BufferToDoubleMap", None)
                    
                    if opp_val == self:
                        setattr(item, "BufferToDoubleMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BufferToDoubleMap"):
                    opp_val = getattr(item, "BufferToDoubleMap", None)
                    
                    setattr(item, "BufferToDoubleMap", self)
                    

    @property
    def analysis_bottlenecks_ActionBottlenecksWithSchedulingData234(self):
        return self.__analysis_bottlenecks_ActionBottlenecksWithSchedulingData234

    @analysis_bottlenecks_ActionBottlenecksWithSchedulingData234.setter
    def analysis_bottlenecks_ActionBottlenecksWithSchedulingData234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_bottlenecks_ActionBottlenecksWithSchedulingData__analysis_bottlenecks_ActionBottlenecksWithSchedulingData234", None)
        self.__analysis_bottlenecks_ActionBottlenecksWithSchedulingData234 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BufferToIntegerMap"):
                    opp_val = getattr(item, "BufferToIntegerMap", None)
                    
                    if opp_val == self:
                        setattr(item, "BufferToIntegerMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BufferToIntegerMap"):
                    opp_val = getattr(item, "BufferToIntegerMap", None)
                    
                    setattr(item, "BufferToIntegerMap", self)
                    

class StringToDoubleMap:

    pass
class ActionBottlenecksWithSchedulingData:

    pass
class analysis_bottlenecks_DoubleToBottlenecksReportMap:

    def __init__(self, key: str, analysis_bottlenecks_DoubleToBottlenecksReportMap: "BottlenecksReport" = None):
        self.key = key
        self.analysis_bottlenecks_DoubleToBottlenecksReportMap = analysis_bottlenecks_DoubleToBottlenecksReportMap
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def analysis_bottlenecks_DoubleToBottlenecksReportMap(self):
        return self.__analysis_bottlenecks_DoubleToBottlenecksReportMap

    @analysis_bottlenecks_DoubleToBottlenecksReportMap.setter
    def analysis_bottlenecks_DoubleToBottlenecksReportMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_bottlenecks_DoubleToBottlenecksReportMap__analysis_bottlenecks_DoubleToBottlenecksReportMap", None)
        self.__analysis_bottlenecks_DoubleToBottlenecksReportMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BottlenecksReport224"):
                opp_val = getattr(old_value, "BottlenecksReport224", None)
                if opp_val == self:
                    setattr(old_value, "BottlenecksReport224", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BottlenecksReport224"):
                opp_val = getattr(value, "BottlenecksReport224", None)
                setattr(value, "BottlenecksReport224", self)

class DoubleToBottlenecksReportMap:

    pass
class DoubleToDoubleMap:

    pass
class bottlenecks_analysis_ActorClass:

    pass
class analysis_bottlenecks_ImpactAnalysisData:

    pass
class BottlenecksReport:

    pass
class ImpactAnalysisData:

    pass
class bottlenecks_analysis_Action:

    pass
class analysis_bottlenecks_ActionBottlenecksData:

    def __init__(self, cpWeight: float, slackMin: float, slackMax: float, cpVariance: float, totalWeight: float, totalVariance: float, cpFirings: str, totalFirings: str, analysis_bottlenecks_ActionBottlenecksData: "bottlenecks_analysis_Action" = None):
        self.cpWeight = cpWeight
        self.slackMin = slackMin
        self.slackMax = slackMax
        self.cpVariance = cpVariance
        self.totalWeight = totalWeight
        self.totalVariance = totalVariance
        self.cpFirings = cpFirings
        self.totalFirings = totalFirings
        self.analysis_bottlenecks_ActionBottlenecksData = analysis_bottlenecks_ActionBottlenecksData
        
    @property
    def totalWeight(self) -> float:
        return self.__totalWeight

    @totalWeight.setter
    def totalWeight(self, totalWeight: float):
        self.__totalWeight = totalWeight

    @property
    def totalVariance(self) -> float:
        return self.__totalVariance

    @totalVariance.setter
    def totalVariance(self, totalVariance: float):
        self.__totalVariance = totalVariance

    @property
    def cpFirings(self) -> str:
        return self.__cpFirings

    @cpFirings.setter
    def cpFirings(self, cpFirings: str):
        self.__cpFirings = cpFirings

    @property
    def cpVariance(self) -> float:
        return self.__cpVariance

    @cpVariance.setter
    def cpVariance(self, cpVariance: float):
        self.__cpVariance = cpVariance

    @property
    def cpWeight(self) -> float:
        return self.__cpWeight

    @cpWeight.setter
    def cpWeight(self, cpWeight: float):
        self.__cpWeight = cpWeight

    @property
    def slackMin(self) -> float:
        return self.__slackMin

    @slackMin.setter
    def slackMin(self, slackMin: float):
        self.__slackMin = slackMin

    @property
    def slackMax(self) -> float:
        return self.__slackMax

    @slackMax.setter
    def slackMax(self, slackMax: float):
        self.__slackMax = slackMax

    @property
    def totalFirings(self) -> str:
        return self.__totalFirings

    @totalFirings.setter
    def totalFirings(self, totalFirings: str):
        self.__totalFirings = totalFirings

    @property
    def analysis_bottlenecks_ActionBottlenecksData(self):
        return self.__analysis_bottlenecks_ActionBottlenecksData

    @analysis_bottlenecks_ActionBottlenecksData.setter
    def analysis_bottlenecks_ActionBottlenecksData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_bottlenecks_ActionBottlenecksData__analysis_bottlenecks_ActionBottlenecksData", None)
        self.__analysis_bottlenecks_ActionBottlenecksData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bottlenecks_analysis_Action"):
                opp_val = getattr(old_value, "bottlenecks_analysis_Action", None)
                if opp_val == self:
                    setattr(old_value, "bottlenecks_analysis_Action", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bottlenecks_analysis_Action"):
                opp_val = getattr(value, "bottlenecks_analysis_Action", None)
                setattr(value, "bottlenecks_analysis_Action", self)

class ActionBottlenecksData:

    pass
class bottlenecks_analysis_Network:

    pass
class analysis_trace_MarkovModelActionData:

    def __init__(self, first: bool, successors: str, analysis_trace_MarkovModelActionData: "trace_analysis_Action" = None, analysis_trace_MarkovModelActionData203: set["ActionToLongMap"] = None):
        self.first = first
        self.successors = successors
        self.analysis_trace_MarkovModelActionData = analysis_trace_MarkovModelActionData
        self.analysis_trace_MarkovModelActionData203 = analysis_trace_MarkovModelActionData203 if analysis_trace_MarkovModelActionData203 is not None else set()
        
    @property
    def first(self) -> bool:
        return self.__first

    @first.setter
    def first(self, first: bool):
        self.__first = first

    @property
    def successors(self) -> str:
        return self.__successors

    @successors.setter
    def successors(self, successors: str):
        self.__successors = successors

    @property
    def analysis_trace_MarkovModelActionData203(self):
        return self.__analysis_trace_MarkovModelActionData203

    @analysis_trace_MarkovModelActionData203.setter
    def analysis_trace_MarkovModelActionData203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_trace_MarkovModelActionData__analysis_trace_MarkovModelActionData203", None)
        self.__analysis_trace_MarkovModelActionData203 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActionToLongMap204"):
                    opp_val = getattr(item, "ActionToLongMap204", None)
                    
                    if opp_val == self:
                        setattr(item, "ActionToLongMap204", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActionToLongMap204"):
                    opp_val = getattr(item, "ActionToLongMap204", None)
                    
                    setattr(item, "ActionToLongMap204", self)
                    

    @property
    def analysis_trace_MarkovModelActionData(self):
        return self.__analysis_trace_MarkovModelActionData

    @analysis_trace_MarkovModelActionData.setter
    def analysis_trace_MarkovModelActionData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_trace_MarkovModelActionData__analysis_trace_MarkovModelActionData", None)
        self.__analysis_trace_MarkovModelActionData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_analysis_Action201"):
                opp_val = getattr(old_value, "trace_analysis_Action201", None)
                if opp_val == self:
                    setattr(old_value, "trace_analysis_Action201", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_analysis_Action201"):
                opp_val = getattr(value, "trace_analysis_Action201", None)
                setattr(value, "trace_analysis_Action201", self)

class MarkovModelActionData:

    pass
class analysis_trace_ComparedAction:

    def __init__(self, found: bool, dSteps: str, dIncomings: str, dOutgoings: str, analysis_trace_ComparedAction: "trace_analysis_Action" = None):
        self.found = found
        self.dSteps = dSteps
        self.dIncomings = dIncomings
        self.dOutgoings = dOutgoings
        self.analysis_trace_ComparedAction = analysis_trace_ComparedAction
        
    @property
    def found(self) -> bool:
        return self.__found

    @found.setter
    def found(self, found: bool):
        self.__found = found

    @property
    def dOutgoings(self) -> str:
        return self.__dOutgoings

    @dOutgoings.setter
    def dOutgoings(self, dOutgoings: str):
        self.__dOutgoings = dOutgoings

    @property
    def dIncomings(self) -> str:
        return self.__dIncomings

    @dIncomings.setter
    def dIncomings(self, dIncomings: str):
        self.__dIncomings = dIncomings

    @property
    def dSteps(self) -> str:
        return self.__dSteps

    @dSteps.setter
    def dSteps(self, dSteps: str):
        self.__dSteps = dSteps

    @property
    def analysis_trace_ComparedAction(self):
        return self.__analysis_trace_ComparedAction

    @analysis_trace_ComparedAction.setter
    def analysis_trace_ComparedAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_trace_ComparedAction__analysis_trace_ComparedAction", None)
        self.__analysis_trace_ComparedAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_analysis_Action195"):
                opp_val = getattr(old_value, "trace_analysis_Action195", None)
                if opp_val == self:
                    setattr(old_value, "trace_analysis_Action195", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_analysis_Action195"):
                opp_val = getattr(value, "trace_analysis_Action195", None)
                setattr(value, "trace_analysis_Action195", self)

class ComparedAction:

    pass
class analysis_trace_ComparedTrace:

    def __init__(self, dSteps: str, dDependencies: str, equal: bool, analysis_trace_ComparedTrace: "CompressedTraceReport" = None, analysis_trace_ComparedTrace190: set["trace_analysis_Action"] = None, analysis_trace_ComparedTrace193: set["ComparedAction"] = None):
        self.dSteps = dSteps
        self.dDependencies = dDependencies
        self.equal = equal
        self.analysis_trace_ComparedTrace = analysis_trace_ComparedTrace
        self.analysis_trace_ComparedTrace190 = analysis_trace_ComparedTrace190 if analysis_trace_ComparedTrace190 is not None else set()
        self.analysis_trace_ComparedTrace193 = analysis_trace_ComparedTrace193 if analysis_trace_ComparedTrace193 is not None else set()
        
    @property
    def dSteps(self) -> str:
        return self.__dSteps

    @dSteps.setter
    def dSteps(self, dSteps: str):
        self.__dSteps = dSteps

    @property
    def dDependencies(self) -> str:
        return self.__dDependencies

    @dDependencies.setter
    def dDependencies(self, dDependencies: str):
        self.__dDependencies = dDependencies

    @property
    def equal(self) -> bool:
        return self.__equal

    @equal.setter
    def equal(self, equal: bool):
        self.__equal = equal

    @property
    def analysis_trace_ComparedTrace(self):
        return self.__analysis_trace_ComparedTrace

    @analysis_trace_ComparedTrace.setter
    def analysis_trace_ComparedTrace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_trace_ComparedTrace__analysis_trace_ComparedTrace", None)
        self.__analysis_trace_ComparedTrace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompressedTraceReport188"):
                opp_val = getattr(old_value, "CompressedTraceReport188", None)
                if opp_val == self:
                    setattr(old_value, "CompressedTraceReport188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompressedTraceReport188"):
                opp_val = getattr(value, "CompressedTraceReport188", None)
                setattr(value, "CompressedTraceReport188", self)

    @property
    def analysis_trace_ComparedTrace190(self):
        return self.__analysis_trace_ComparedTrace190

    @analysis_trace_ComparedTrace190.setter
    def analysis_trace_ComparedTrace190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_trace_ComparedTrace__analysis_trace_ComparedTrace190", None)
        self.__analysis_trace_ComparedTrace190 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trace_analysis_Action191"):
                    opp_val = getattr(item, "trace_analysis_Action191", None)
                    
                    if opp_val == self:
                        setattr(item, "trace_analysis_Action191", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trace_analysis_Action191"):
                    opp_val = getattr(item, "trace_analysis_Action191", None)
                    
                    setattr(item, "trace_analysis_Action191", self)
                    

    @property
    def analysis_trace_ComparedTrace193(self):
        return self.__analysis_trace_ComparedTrace193

    @analysis_trace_ComparedTrace193.setter
    def analysis_trace_ComparedTrace193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_trace_ComparedTrace__analysis_trace_ComparedTrace193", None)
        self.__analysis_trace_ComparedTrace193 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ComparedAction"):
                    opp_val = getattr(item, "ComparedAction", None)
                    
                    if opp_val == self:
                        setattr(item, "ComparedAction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ComparedAction"):
                    opp_val = getattr(item, "ComparedAction", None)
                    
                    setattr(item, "ComparedAction", self)
                    

class ComparedTrace:

    pass
class CompressedTraceReport:

    pass
class BufferToLongMap:

    pass
class PortToLongMap:

    pass
class VariableToLongMap:

    pass
class GuardToLongMap:

    pass
class analysis_trace_CompressedDependency(ABC):

    def __init__(self, count: str, CompressedStep157: "CompressedStep" = None, CompressedStep160: "CompressedStep" = None):
        self.count = count
        self.CompressedStep157 = CompressedStep157
        self.CompressedStep160 = CompressedStep160
        
    @property
    def count(self) -> str:
        return self.__count

    @count.setter
    def count(self, count: str):
        self.__count = count

    @property
    def CompressedStep157(self):
        return self.__CompressedStep157

    @CompressedStep157.setter
    def CompressedStep157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_trace_CompressedDependency__CompressedStep157", None)
        self.__CompressedStep157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace158"):
                opp_val = getattr(old_value, "trace158", None)
                if opp_val == self:
                    setattr(old_value, "trace158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace158"):
                opp_val = getattr(value, "trace158", None)
                setattr(value, "trace158", self)

    @property
    def CompressedStep160(self):
        return self.__CompressedStep160

    @CompressedStep160.setter
    def CompressedStep160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_trace_CompressedDependency__CompressedStep160", None)
        self.__CompressedStep160 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace161"):
                opp_val = getattr(old_value, "trace161", None)
                if opp_val == self:
                    setattr(old_value, "trace161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace161"):
                opp_val = getattr(value, "trace161", None)
                setattr(value, "trace161", self)

class trace_analysis_Action:

    pass
class analysis_trace_CompressedStep:

    def __init__(self, count: str, analysis_trace_CompressedStep: "trace_analysis_Action" = None, CompressedDependency143: set["CompressedDependency"] = None, CompressedDependency145: set["CompressedDependency"] = None, analysis_trace_CompressedStep148: set["CompressedStep"] = None, analysis_trace_CompressedStep151: set["CompressedStep"] = None, analysis_trace_CompressedStep154: set["CompressedStep"] = None):
        self.count = count
        self.analysis_trace_CompressedStep = analysis_trace_CompressedStep
        self.CompressedDependency143 = CompressedDependency143 if CompressedDependency143 is not None else set()
        self.CompressedDependency145 = CompressedDependency145 if CompressedDependency145 is not None else set()
        self.analysis_trace_CompressedStep148 = analysis_trace_CompressedStep148 if analysis_trace_CompressedStep148 is not None else set()
        self.analysis_trace_CompressedStep151 = analysis_trace_CompressedStep151 if analysis_trace_CompressedStep151 is not None else set()
        self.analysis_trace_CompressedStep154 = analysis_trace_CompressedStep154 if analysis_trace_CompressedStep154 is not None else set()
        
    @property
    def count(self) -> str:
        return self.__count

    @count.setter
    def count(self, count: str):
        self.__count = count

    @property
    def CompressedDependency145(self):
        return self.__CompressedDependency145

    @CompressedDependency145.setter
    def CompressedDependency145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_trace_CompressedStep__CompressedDependency145", None)
        self.__CompressedDependency145 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trace146"):
                    opp_val = getattr(item, "trace146", None)
                    
                    if opp_val == self:
                        setattr(item, "trace146", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trace146"):
                    opp_val = getattr(item, "trace146", None)
                    
                    setattr(item, "trace146", self)
                    

    @property
    def CompressedDependency143(self):
        return self.__CompressedDependency143

    @CompressedDependency143.setter
    def CompressedDependency143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_trace_CompressedStep__CompressedDependency143", None)
        self.__CompressedDependency143 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trace"):
                    opp_val = getattr(item, "trace", None)
                    
                    if opp_val == self:
                        setattr(item, "trace", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trace"):
                    opp_val = getattr(item, "trace", None)
                    
                    setattr(item, "trace", self)
                    

    @property
    def analysis_trace_CompressedStep(self):
        return self.__analysis_trace_CompressedStep

    @analysis_trace_CompressedStep.setter
    def analysis_trace_CompressedStep(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_trace_CompressedStep__analysis_trace_CompressedStep", None)
        self.__analysis_trace_CompressedStep = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_analysis_Action"):
                opp_val = getattr(old_value, "trace_analysis_Action", None)
                if opp_val == self:
                    setattr(old_value, "trace_analysis_Action", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_analysis_Action"):
                opp_val = getattr(value, "trace_analysis_Action", None)
                setattr(value, "trace_analysis_Action", self)

    @property
    def analysis_trace_CompressedStep148(self):
        return self.__analysis_trace_CompressedStep148

    @analysis_trace_CompressedStep148.setter
    def analysis_trace_CompressedStep148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_trace_CompressedStep__analysis_trace_CompressedStep148", None)
        self.__analysis_trace_CompressedStep148 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompressedStep149"):
                    opp_val = getattr(item, "CompressedStep149", None)
                    
                    if opp_val == self:
                        setattr(item, "CompressedStep149", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompressedStep149"):
                    opp_val = getattr(item, "CompressedStep149", None)
                    
                    setattr(item, "CompressedStep149", self)
                    

    @property
    def analysis_trace_CompressedStep154(self):
        return self.__analysis_trace_CompressedStep154

    @analysis_trace_CompressedStep154.setter
    def analysis_trace_CompressedStep154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_trace_CompressedStep__analysis_trace_CompressedStep154", None)
        self.__analysis_trace_CompressedStep154 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompressedStep155"):
                    opp_val = getattr(item, "CompressedStep155", None)
                    
                    if opp_val == self:
                        setattr(item, "CompressedStep155", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompressedStep155"):
                    opp_val = getattr(item, "CompressedStep155", None)
                    
                    setattr(item, "CompressedStep155", self)
                    

    @property
    def analysis_trace_CompressedStep151(self):
        return self.__analysis_trace_CompressedStep151

    @analysis_trace_CompressedStep151.setter
    def analysis_trace_CompressedStep151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_trace_CompressedStep__analysis_trace_CompressedStep151", None)
        self.__analysis_trace_CompressedStep151 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompressedStep152"):
                    opp_val = getattr(item, "CompressedStep152", None)
                    
                    if opp_val == self:
                        setattr(item, "CompressedStep152", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompressedStep152"):
                    opp_val = getattr(item, "CompressedStep152", None)
                    
                    setattr(item, "CompressedStep152", self)
                    

class CompressedDependency:

    pass
class analysis_trace_CompressedPortDependency(CompressedDependency):

    pass
class analysis_trace_CompressedTokensDependency(CompressedDependency):

    pass
class analysis_trace_CompressedFsmDependency(CompressedDependency):

    pass
class analysis_trace_CompressedVariableDependency(CompressedDependency):

    pass
class analysis_trace_CompressedGuardDependency(CompressedDependency):

    pass
class CompressedStep:

    pass
class trace_analysis_Network:

    pass
class StringToLongMap:

    pass
class ActorToLongMap:

    pass
class analysis_map_StringToStringMap:

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class ActorSelectionSchedule:

    pass
class analysis_caseoptimal_CaseOptimalActorSelectionSchedule(ActorSelectionSchedule):

    pass
class analysis_scheduling_Sequence(ActorSelectionSchedule):

    pass
class analysis_scheduling_FSM(ActorSelectionSchedule):

    def __init__(self, startState: str, terminalState: str, analysis_scheduling_FSM: set["FSMState"] = None, analysis_scheduling_FSM427: set["FSMVar"] = None, ActorSelectionSchedule: "analysis_map_PartitionToActorSelectionScheduleMap"):
        self.startState = startState
        self.terminalState = terminalState
        self.analysis_scheduling_FSM = analysis_scheduling_FSM if analysis_scheduling_FSM is not None else set()
        self.analysis_scheduling_FSM427 = analysis_scheduling_FSM427 if analysis_scheduling_FSM427 is not None else set()
        
    @property
    def startState(self) -> str:
        return self.__startState

    @startState.setter
    def startState(self, startState: str):
        self.__startState = startState

    @property
    def terminalState(self) -> str:
        return self.__terminalState

    @terminalState.setter
    def terminalState(self, terminalState: str):
        self.__terminalState = terminalState

    @property
    def analysis_scheduling_FSM427(self):
        return self.__analysis_scheduling_FSM427

    @analysis_scheduling_FSM427.setter
    def analysis_scheduling_FSM427(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_scheduling_FSM__analysis_scheduling_FSM427", None)
        self.__analysis_scheduling_FSM427 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FSMVar"):
                    opp_val = getattr(item, "FSMVar", None)
                    
                    if opp_val == self:
                        setattr(item, "FSMVar", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FSMVar"):
                    opp_val = getattr(item, "FSMVar", None)
                    
                    setattr(item, "FSMVar", self)
                    

    @property
    def analysis_scheduling_FSM(self):
        return self.__analysis_scheduling_FSM

    @analysis_scheduling_FSM.setter
    def analysis_scheduling_FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_scheduling_FSM__analysis_scheduling_FSM", None)
        self.__analysis_scheduling_FSM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FSMState"):
                    opp_val = getattr(item, "FSMState", None)
                    
                    if opp_val == self:
                        setattr(item, "FSMState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FSMState"):
                    opp_val = getattr(item, "FSMState", None)
                    
                    setattr(item, "FSMState", self)
                    

class analysis_scheduling_ActorFire(ActorSelectionSchedule):

    def __init__(self, Actor: str, Times: int, partition: str, dependencyPartitions: str, ActorSelectionSchedule: "analysis_map_PartitionToActorSelectionScheduleMap"):
        self.Actor = Actor
        self.Times = Times
        self.partition = partition
        self.dependencyPartitions = dependencyPartitions
        
    @property
    def partition(self) -> str:
        return self.__partition

    @partition.setter
    def partition(self, partition: str):
        self.__partition = partition

    @property
    def Times(self) -> int:
        return self.__Times

    @Times.setter
    def Times(self, Times: int):
        self.__Times = Times

    @property
    def dependencyPartitions(self) -> str:
        return self.__dependencyPartitions

    @dependencyPartitions.setter
    def dependencyPartitions(self, dependencyPartitions: str):
        self.__dependencyPartitions = dependencyPartitions

    @property
    def Actor(self) -> str:
        return self.__Actor

    @Actor.setter
    def Actor(self, Actor: str):
        self.__Actor = Actor

class analysis_map_PartitionToActorSelectionScheduleMap:

    def __init__(self, key: str, analysis_map_PartitionToActorSelectionScheduleMap: "ActorSelectionSchedule" = None):
        self.key = key
        self.analysis_map_PartitionToActorSelectionScheduleMap = analysis_map_PartitionToActorSelectionScheduleMap
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def analysis_map_PartitionToActorSelectionScheduleMap(self):
        return self.__analysis_map_PartitionToActorSelectionScheduleMap

    @analysis_map_PartitionToActorSelectionScheduleMap.setter
    def analysis_map_PartitionToActorSelectionScheduleMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_map_PartitionToActorSelectionScheduleMap__analysis_map_PartitionToActorSelectionScheduleMap", None)
        self.__analysis_map_PartitionToActorSelectionScheduleMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActorSelectionSchedule"):
                opp_val = getattr(old_value, "ActorSelectionSchedule", None)
                if opp_val == self:
                    setattr(old_value, "ActorSelectionSchedule", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActorSelectionSchedule"):
                opp_val = getattr(value, "ActorSelectionSchedule", None)
                setattr(value, "ActorSelectionSchedule", self)

class analysis_map_BufferToDoubleMap:

    def __init__(self, value: str, analysis_map_BufferToDoubleMap: "map_analysis_Buffer" = None):
        self.value = value
        self.analysis_map_BufferToDoubleMap = analysis_map_BufferToDoubleMap
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def analysis_map_BufferToDoubleMap(self):
        return self.__analysis_map_BufferToDoubleMap

    @analysis_map_BufferToDoubleMap.setter
    def analysis_map_BufferToDoubleMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_map_BufferToDoubleMap__analysis_map_BufferToDoubleMap", None)
        self.__analysis_map_BufferToDoubleMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "map_analysis_Buffer113"):
                opp_val = getattr(old_value, "map_analysis_Buffer113", None)
                if opp_val == self:
                    setattr(old_value, "map_analysis_Buffer113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "map_analysis_Buffer113"):
                opp_val = getattr(value, "map_analysis_Buffer113", None)
                setattr(value, "map_analysis_Buffer113", self)

class analysis_map_BufferToIntegerMap:

    def __init__(self, value: str, analysis_map_BufferToIntegerMap: "map_analysis_Buffer" = None):
        self.value = value
        self.analysis_map_BufferToIntegerMap = analysis_map_BufferToIntegerMap
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def analysis_map_BufferToIntegerMap(self):
        return self.__analysis_map_BufferToIntegerMap

    @analysis_map_BufferToIntegerMap.setter
    def analysis_map_BufferToIntegerMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_map_BufferToIntegerMap__analysis_map_BufferToIntegerMap", None)
        self.__analysis_map_BufferToIntegerMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "map_analysis_Buffer111"):
                opp_val = getattr(old_value, "map_analysis_Buffer111", None)
                if opp_val == self:
                    setattr(old_value, "map_analysis_Buffer111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "map_analysis_Buffer111"):
                opp_val = getattr(value, "map_analysis_Buffer111", None)
                setattr(value, "map_analysis_Buffer111", self)

class analysis_map_ActionToDoubleMap:

    def __init__(self, value: str, analysis_map_ActionToDoubleMap: "map_analysis_Action" = None):
        self.value = value
        self.analysis_map_ActionToDoubleMap = analysis_map_ActionToDoubleMap
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def analysis_map_ActionToDoubleMap(self):
        return self.__analysis_map_ActionToDoubleMap

    @analysis_map_ActionToDoubleMap.setter
    def analysis_map_ActionToDoubleMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_map_ActionToDoubleMap__analysis_map_ActionToDoubleMap", None)
        self.__analysis_map_ActionToDoubleMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "map_analysis_Action109"):
                opp_val = getattr(old_value, "map_analysis_Action109", None)
                if opp_val == self:
                    setattr(old_value, "map_analysis_Action109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "map_analysis_Action109"):
                opp_val = getattr(value, "map_analysis_Action109", None)
                setattr(value, "map_analysis_Action109", self)

class analysis_map_StringToDoubleMap:

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

class map_analysis_Port:

    pass
class analysis_map_PortToLongMap:

    def __init__(self, value: str, analysis_map_PortToLongMap: "map_analysis_Port" = None):
        self.value = value
        self.analysis_map_PortToLongMap = analysis_map_PortToLongMap
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def analysis_map_PortToLongMap(self):
        return self.__analysis_map_PortToLongMap

    @analysis_map_PortToLongMap.setter
    def analysis_map_PortToLongMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_map_PortToLongMap__analysis_map_PortToLongMap", None)
        self.__analysis_map_PortToLongMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "map_analysis_Port"):
                opp_val = getattr(old_value, "map_analysis_Port", None)
                if opp_val == self:
                    setattr(old_value, "map_analysis_Port", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "map_analysis_Port"):
                opp_val = getattr(value, "map_analysis_Port", None)
                setattr(value, "map_analysis_Port", self)

class map_analysis_Guard:

    pass
class analysis_map_GuardToLongMap:

    def __init__(self, value: str, analysis_map_GuardToLongMap: "map_analysis_Guard" = None):
        self.value = value
        self.analysis_map_GuardToLongMap = analysis_map_GuardToLongMap
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def analysis_map_GuardToLongMap(self):
        return self.__analysis_map_GuardToLongMap

    @analysis_map_GuardToLongMap.setter
    def analysis_map_GuardToLongMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_map_GuardToLongMap__analysis_map_GuardToLongMap", None)
        self.__analysis_map_GuardToLongMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "map_analysis_Guard"):
                opp_val = getattr(old_value, "map_analysis_Guard", None)
                if opp_val == self:
                    setattr(old_value, "map_analysis_Guard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "map_analysis_Guard"):
                opp_val = getattr(value, "map_analysis_Guard", None)
                setattr(value, "map_analysis_Guard", self)

class analysis_map_VariableToLongMap:

    def __init__(self, value: str, analysis_map_VariableToLongMap: "map_analysis_Variable" = None):
        self.value = value
        self.analysis_map_VariableToLongMap = analysis_map_VariableToLongMap
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def analysis_map_VariableToLongMap(self):
        return self.__analysis_map_VariableToLongMap

    @analysis_map_VariableToLongMap.setter
    def analysis_map_VariableToLongMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_map_VariableToLongMap__analysis_map_VariableToLongMap", None)
        self.__analysis_map_VariableToLongMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "map_analysis_Variable105"):
                opp_val = getattr(old_value, "map_analysis_Variable105", None)
                if opp_val == self:
                    setattr(old_value, "map_analysis_Variable105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "map_analysis_Variable105"):
                opp_val = getattr(value, "map_analysis_Variable105", None)
                setattr(value, "map_analysis_Variable105", self)

class analysis_map_DoubleToDoubleMap:

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class analysis_map_StringToLongMap:

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

class analysis_map_BufferToLongMap:

    def __init__(self, value: str, analysis_map_BufferToLongMap: "map_analysis_Buffer" = None):
        self.value = value
        self.analysis_map_BufferToLongMap = analysis_map_BufferToLongMap
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def analysis_map_BufferToLongMap(self):
        return self.__analysis_map_BufferToLongMap

    @analysis_map_BufferToLongMap.setter
    def analysis_map_BufferToLongMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_map_BufferToLongMap__analysis_map_BufferToLongMap", None)
        self.__analysis_map_BufferToLongMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "map_analysis_Buffer103"):
                opp_val = getattr(old_value, "map_analysis_Buffer103", None)
                if opp_val == self:
                    setattr(old_value, "map_analysis_Buffer103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "map_analysis_Buffer103"):
                opp_val = getattr(value, "map_analysis_Buffer103", None)
                setattr(value, "map_analysis_Buffer103", self)

class analysis_map_ActorToLongMap:

    def __init__(self, value: str, analysis_map_ActorToLongMap: "map_analysis_Actor" = None):
        self.value = value
        self.analysis_map_ActorToLongMap = analysis_map_ActorToLongMap
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def analysis_map_ActorToLongMap(self):
        return self.__analysis_map_ActorToLongMap

    @analysis_map_ActorToLongMap.setter
    def analysis_map_ActorToLongMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_map_ActorToLongMap__analysis_map_ActorToLongMap", None)
        self.__analysis_map_ActorToLongMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "map_analysis_Actor101"):
                opp_val = getattr(old_value, "map_analysis_Actor101", None)
                if opp_val == self:
                    setattr(old_value, "map_analysis_Actor101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "map_analysis_Actor101"):
                opp_val = getattr(value, "map_analysis_Actor101", None)
                setattr(value, "map_analysis_Actor101", self)

class analysis_map_ActionToLongMap:

    def __init__(self, value: str, analysis_map_ActionToLongMap: "map_analysis_Action" = None):
        self.value = value
        self.analysis_map_ActionToLongMap = analysis_map_ActionToLongMap
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def analysis_map_ActionToLongMap(self):
        return self.__analysis_map_ActionToLongMap

    @analysis_map_ActionToLongMap.setter
    def analysis_map_ActionToLongMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_map_ActionToLongMap__analysis_map_ActionToLongMap", None)
        self.__analysis_map_ActionToLongMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "map_analysis_Action99"):
                opp_val = getattr(old_value, "map_analysis_Action99", None)
                if opp_val == self:
                    setattr(old_value, "map_analysis_Action99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "map_analysis_Action99"):
                opp_val = getattr(value, "map_analysis_Action99", None)
                setattr(value, "map_analysis_Action99", self)

class analysis_map_EOperatorToStatisticalDataMap:

    def __init__(self, key: str, analysis_map_EOperatorToStatisticalDataMap: "map_analysis_StatisticalData" = None):
        self.key = key
        self.analysis_map_EOperatorToStatisticalDataMap = analysis_map_EOperatorToStatisticalDataMap
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def analysis_map_EOperatorToStatisticalDataMap(self):
        return self.__analysis_map_EOperatorToStatisticalDataMap

    @analysis_map_EOperatorToStatisticalDataMap.setter
    def analysis_map_EOperatorToStatisticalDataMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_map_EOperatorToStatisticalDataMap__analysis_map_EOperatorToStatisticalDataMap", None)
        self.__analysis_map_EOperatorToStatisticalDataMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "map_analysis_StatisticalData97"):
                opp_val = getattr(old_value, "map_analysis_StatisticalData97", None)
                if opp_val == self:
                    setattr(old_value, "map_analysis_StatisticalData97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "map_analysis_StatisticalData97"):
                opp_val = getattr(value, "map_analysis_StatisticalData97", None)
                setattr(value, "map_analysis_StatisticalData97", self)

class map_analysis_ActorClass:

    pass
class analysis_map_ActorClassToStatisticalDataMap:

    pass
class map_analysis_Variable:

    pass
class analysis_map_VariableToStatisticalDataMap:

    pass
class map_analysis_Procedure:

    pass
class analysis_map_ProcedureToStatisticalDataMap:

    pass
class map_analysis_Buffer:

    pass
class analysis_map_BufferToStatisticalDataMap:

    pass
class map_analysis_Action:

    pass
class analysis_map_ActionToStatisticalDataMap:

    pass
class map_analysis_StatisticalData:

    pass
class map_analysis_Actor:

    pass
class analysis_map_ActorToStatisticalDataMap:

    pass
class analysis_map_StringToIntegerMap:

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class StringToStringMap:

    pass
class analysis_profiler_TableRow:

    pass
class TableRow:

    pass
class AccessData:

    pass
class analysis_profiler_StringToAccessDataMap:

    def __init__(self, key: str, analysis_profiler_StringToAccessDataMap: "AccessData" = None):
        self.key = key
        self.analysis_profiler_StringToAccessDataMap = analysis_profiler_StringToAccessDataMap
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def analysis_profiler_StringToAccessDataMap(self):
        return self.__analysis_profiler_StringToAccessDataMap

    @analysis_profiler_StringToAccessDataMap.setter
    def analysis_profiler_StringToAccessDataMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_profiler_StringToAccessDataMap__analysis_profiler_StringToAccessDataMap", None)
        self.__analysis_profiler_StringToAccessDataMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AccessData"):
                opp_val = getattr(old_value, "AccessData", None)
                if opp_val == self:
                    setattr(old_value, "AccessData", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AccessData"):
                opp_val = getattr(value, "AccessData", None)
                setattr(value, "AccessData", self)

class analysis_profiler_AccessData:

    def __init__(self, accesses: float, min: float, max: float, average: float, total: float):
        self.accesses = accesses
        self.min = min
        self.max = max
        self.average = average
        self.total = total
        
    @property
    def min(self) -> float:
        return self.__min

    @min.setter
    def min(self, min: float):
        self.__min = min

    @property
    def average(self) -> float:
        return self.__average

    @average.setter
    def average(self, average: float):
        self.__average = average

    @property
    def total(self) -> float:
        return self.__total

    @total.setter
    def total(self, total: float):
        self.__total = total

    @property
    def accesses(self) -> float:
        return self.__accesses

    @accesses.setter
    def accesses(self, accesses: float):
        self.__accesses = accesses

    @property
    def max(self) -> float:
        return self.__max

    @max.setter
    def max(self, max: float):
        self.__max = max

class StringToAccessDataMap:

    pass
class analysis_profiler_MemoryAccessData(ABC):

    pass
class ProcedureToComplexDynamicDataMap:

    pass
class analysis_profiler_ActionMemoryProfilingData:

    def __init__(self, actor: str, action: str, analysis_profiler_ActionMemoryProfilingData: set["MemoryAccessData"] = None, analysis_profiler_ActionMemoryProfilingData67: set["MemoryAccessData"] = None):
        self.actor = actor
        self.action = action
        self.analysis_profiler_ActionMemoryProfilingData = analysis_profiler_ActionMemoryProfilingData if analysis_profiler_ActionMemoryProfilingData is not None else set()
        self.analysis_profiler_ActionMemoryProfilingData67 = analysis_profiler_ActionMemoryProfilingData67 if analysis_profiler_ActionMemoryProfilingData67 is not None else set()
        
    @property
    def actor(self) -> str:
        return self.__actor

    @actor.setter
    def actor(self, actor: str):
        self.__actor = actor

    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def analysis_profiler_ActionMemoryProfilingData(self):
        return self.__analysis_profiler_ActionMemoryProfilingData

    @analysis_profiler_ActionMemoryProfilingData.setter
    def analysis_profiler_ActionMemoryProfilingData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_profiler_ActionMemoryProfilingData__analysis_profiler_ActionMemoryProfilingData", None)
        self.__analysis_profiler_ActionMemoryProfilingData = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MemoryAccessData"):
                    opp_val = getattr(item, "MemoryAccessData", None)
                    
                    if opp_val == self:
                        setattr(item, "MemoryAccessData", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MemoryAccessData"):
                    opp_val = getattr(item, "MemoryAccessData", None)
                    
                    setattr(item, "MemoryAccessData", self)
                    

    @property
    def analysis_profiler_ActionMemoryProfilingData67(self):
        return self.__analysis_profiler_ActionMemoryProfilingData67

    @analysis_profiler_ActionMemoryProfilingData67.setter
    def analysis_profiler_ActionMemoryProfilingData67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_profiler_ActionMemoryProfilingData__analysis_profiler_ActionMemoryProfilingData67", None)
        self.__analysis_profiler_ActionMemoryProfilingData67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MemoryAccessData68"):
                    opp_val = getattr(item, "MemoryAccessData68", None)
                    
                    if opp_val == self:
                        setattr(item, "MemoryAccessData68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MemoryAccessData68"):
                    opp_val = getattr(item, "MemoryAccessData68", None)
                    
                    setattr(item, "MemoryAccessData68", self)
                    

    def getReadLocalVariableData(self, variable: str) -> str:
        # TODO: Implement getReadLocalVariableData method
        pass

    def getReadStateVariableData(self, variable: str) -> str:
        # TODO: Implement getReadStateVariableData method
        pass

    def getReadSharedVariableData(self, variable: str) -> str:
        # TODO: Implement getReadSharedVariableData method
        pass

    def getWriteStateVariableData(self, variable: str) -> str:
        # TODO: Implement getWriteStateVariableData method
        pass

    def getWriteLocalVariableData(self, variable: str) -> str:
        # TODO: Implement getWriteLocalVariableData method
        pass

    def getWriteSharedVariableData(self, variable: str) -> str:
        # TODO: Implement getWriteSharedVariableData method
        pass

    def getReadBufferData(self, targetPort: str, sourceActor: str, targetActor: str, sourcePort: str) -> str:
        # TODO: Implement getReadBufferData method
        pass

    def getWriteBufferData(self, targetActor: str, sourceActor: str, targetPort: str, sourcePort: str) -> str:
        # TODO: Implement getWriteBufferData method
        pass

class ActionMemoryProfilingData:

    pass
class profiler_analysis_Procedure:

    pass
class analysis_profiler_ProcedureToComplexDynamicDataMap:

    pass
class MemoryAccessData:

    pass
class analysis_profiler_BufferAccessData(MemoryAccessData):

    def __init__(self, sourceActor: str, sourcePort: str, targetActor: str, targetPort: str, MemoryAccessData: "analysis_profiler_ActionMemoryProfilingData", MemoryAccessData68: "analysis_profiler_ActionMemoryProfilingData"):
        self.sourceActor = sourceActor
        self.sourcePort = sourcePort
        self.targetActor = targetActor
        self.targetPort = targetPort
        
    @property
    def targetActor(self) -> str:
        return self.__targetActor

    @targetActor.setter
    def targetActor(self, targetActor: str):
        self.__targetActor = targetActor

    @property
    def targetPort(self) -> str:
        return self.__targetPort

    @targetPort.setter
    def targetPort(self, targetPort: str):
        self.__targetPort = targetPort

    @property
    def sourceActor(self) -> str:
        return self.__sourceActor

    @sourceActor.setter
    def sourceActor(self, sourceActor: str):
        self.__sourceActor = sourceActor

    @property
    def sourcePort(self) -> str:
        return self.__sourcePort

    @sourcePort.setter
    def sourcePort(self, sourcePort: str):
        self.__sourcePort = sourcePort

class analysis_profiler_LocalVariableAccessData(MemoryAccessData):

    def __init__(self, name: str, MemoryAccessData: "analysis_profiler_ActionMemoryProfilingData", MemoryAccessData68: "analysis_profiler_ActionMemoryProfilingData"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class analysis_profiler_StateVariableAccessData(MemoryAccessData):

    def __init__(self, name: str, MemoryAccessData: "analysis_profiler_ActionMemoryProfilingData", MemoryAccessData68: "analysis_profiler_ActionMemoryProfilingData"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class analysis_profiler_SharedVariableAccessData(MemoryAccessData):

    def __init__(self, name: str, MemoryAccessData: "analysis_profiler_ActionMemoryProfilingData", MemoryAccessData68: "analysis_profiler_ActionMemoryProfilingData"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class BufferToStatisticalDataMap:

    pass
class VariableToStatisticalDataMap:

    pass
class ProcedureToStatisticalDataMap:

    pass
class EOperatorToStatisticalDataMap:

    pass
class analysis_profiler_ComplexDynamicData:

    pass
class ActionToLongMap:

    pass
class ActionToStatisticalDataMap:

    pass
class profiler_analysis_StatisticalData:

    pass
class profiler_analysis_Action:

    pass
class ActionDynamicData:

    pass
class profiler_analysis_Actor:

    pass
class ComplexDynamicData:

    pass
class analysis_profiler_ActionDynamicData(ComplexDynamicData):

    pass
class analysis_profiler_ActorDynamicData(ComplexDynamicData):

    pass
class BufferDynamicData:

    pass
class ActorDynamicData:

    pass
class CodeData:

    pass
class analysis_profiler_ComplexCodeData(CodeData):

    def __init__(self, analysis_profiler_ComplexCodeData: set["CodeData"] = None, analysis_profiler_ComplexCodeData12: set["CodeData"] = None, CodeData: "analysis_profiler_ComplexCodeData", CodeData13: "analysis_profiler_ComplexCodeData"):
        self.analysis_profiler_ComplexCodeData = analysis_profiler_ComplexCodeData if analysis_profiler_ComplexCodeData is not None else set()
        self.analysis_profiler_ComplexCodeData12 = analysis_profiler_ComplexCodeData12 if analysis_profiler_ComplexCodeData12 is not None else set()
        
    @property
    def analysis_profiler_ComplexCodeData12(self):
        return self.__analysis_profiler_ComplexCodeData12

    @analysis_profiler_ComplexCodeData12.setter
    def analysis_profiler_ComplexCodeData12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_profiler_ComplexCodeData__analysis_profiler_ComplexCodeData12", None)
        self.__analysis_profiler_ComplexCodeData12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CodeData13"):
                    opp_val = getattr(item, "CodeData13", None)
                    
                    if opp_val == self:
                        setattr(item, "CodeData13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CodeData13"):
                    opp_val = getattr(item, "CodeData13", None)
                    
                    setattr(item, "CodeData13", self)
                    

    @property
    def analysis_profiler_ComplexCodeData(self):
        return self.__analysis_profiler_ComplexCodeData

    @analysis_profiler_ComplexCodeData.setter
    def analysis_profiler_ComplexCodeData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_profiler_ComplexCodeData__analysis_profiler_ComplexCodeData", None)
        self.__analysis_profiler_ComplexCodeData = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CodeData"):
                    opp_val = getattr(item, "CodeData", None)
                    
                    if opp_val == self:
                        setattr(item, "CodeData", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CodeData"):
                    opp_val = getattr(item, "CodeData", None)
                    
                    setattr(item, "CodeData", self)
                    

    def getActionData(self, action: str) -> str:
        # TODO: Implement getActionData method
        pass

    def getProcedureData(self, procedure: str) -> str:
        # TODO: Implement getProcedureData method
        pass

class StringToIntegerMap:

    pass
class profiler_analysis_Buffer:

    pass
class analysis_profiler_BufferDynamicData:

    def __init__(self, unconsumedTokens: int, analysis_profiler_BufferDynamicData: "profiler_analysis_Buffer" = None, analysis_profiler_BufferDynamicData26: "profiler_analysis_StatisticalData" = None, analysis_profiler_BufferDynamicData28: "profiler_analysis_StatisticalData" = None, analysis_profiler_BufferDynamicData31: "profiler_analysis_StatisticalData" = None, analysis_profiler_BufferDynamicData34: set["ActionToStatisticalDataMap"] = None, analysis_profiler_BufferDynamicData36: set["ActionToStatisticalDataMap"] = None, analysis_profiler_BufferDynamicData39: set["ActionToLongMap"] = None, analysis_profiler_BufferDynamicData41: set["ActionToLongMap"] = None, analysis_profiler_BufferDynamicData44: set["ActionToLongMap"] = None):
        self.unconsumedTokens = unconsumedTokens
        self.analysis_profiler_BufferDynamicData = analysis_profiler_BufferDynamicData
        self.analysis_profiler_BufferDynamicData26 = analysis_profiler_BufferDynamicData26
        self.analysis_profiler_BufferDynamicData28 = analysis_profiler_BufferDynamicData28
        self.analysis_profiler_BufferDynamicData31 = analysis_profiler_BufferDynamicData31
        self.analysis_profiler_BufferDynamicData34 = analysis_profiler_BufferDynamicData34 if analysis_profiler_BufferDynamicData34 is not None else set()
        self.analysis_profiler_BufferDynamicData36 = analysis_profiler_BufferDynamicData36 if analysis_profiler_BufferDynamicData36 is not None else set()
        self.analysis_profiler_BufferDynamicData39 = analysis_profiler_BufferDynamicData39 if analysis_profiler_BufferDynamicData39 is not None else set()
        self.analysis_profiler_BufferDynamicData41 = analysis_profiler_BufferDynamicData41 if analysis_profiler_BufferDynamicData41 is not None else set()
        self.analysis_profiler_BufferDynamicData44 = analysis_profiler_BufferDynamicData44 if analysis_profiler_BufferDynamicData44 is not None else set()
        
    @property
    def unconsumedTokens(self) -> int:
        return self.__unconsumedTokens

    @unconsumedTokens.setter
    def unconsumedTokens(self, unconsumedTokens: int):
        self.__unconsumedTokens = unconsumedTokens

    @property
    def analysis_profiler_BufferDynamicData36(self):
        return self.__analysis_profiler_BufferDynamicData36

    @analysis_profiler_BufferDynamicData36.setter
    def analysis_profiler_BufferDynamicData36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_profiler_BufferDynamicData__analysis_profiler_BufferDynamicData36", None)
        self.__analysis_profiler_BufferDynamicData36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActionToStatisticalDataMap37"):
                    opp_val = getattr(item, "ActionToStatisticalDataMap37", None)
                    
                    if opp_val == self:
                        setattr(item, "ActionToStatisticalDataMap37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActionToStatisticalDataMap37"):
                    opp_val = getattr(item, "ActionToStatisticalDataMap37", None)
                    
                    setattr(item, "ActionToStatisticalDataMap37", self)
                    

    @property
    def analysis_profiler_BufferDynamicData(self):
        return self.__analysis_profiler_BufferDynamicData

    @analysis_profiler_BufferDynamicData.setter
    def analysis_profiler_BufferDynamicData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_profiler_BufferDynamicData__analysis_profiler_BufferDynamicData", None)
        self.__analysis_profiler_BufferDynamicData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profiler_analysis_Buffer"):
                opp_val = getattr(old_value, "profiler_analysis_Buffer", None)
                if opp_val == self:
                    setattr(old_value, "profiler_analysis_Buffer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profiler_analysis_Buffer"):
                opp_val = getattr(value, "profiler_analysis_Buffer", None)
                setattr(value, "profiler_analysis_Buffer", self)

    @property
    def analysis_profiler_BufferDynamicData44(self):
        return self.__analysis_profiler_BufferDynamicData44

    @analysis_profiler_BufferDynamicData44.setter
    def analysis_profiler_BufferDynamicData44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_profiler_BufferDynamicData__analysis_profiler_BufferDynamicData44", None)
        self.__analysis_profiler_BufferDynamicData44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActionToLongMap45"):
                    opp_val = getattr(item, "ActionToLongMap45", None)
                    
                    if opp_val == self:
                        setattr(item, "ActionToLongMap45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActionToLongMap45"):
                    opp_val = getattr(item, "ActionToLongMap45", None)
                    
                    setattr(item, "ActionToLongMap45", self)
                    

    @property
    def analysis_profiler_BufferDynamicData39(self):
        return self.__analysis_profiler_BufferDynamicData39

    @analysis_profiler_BufferDynamicData39.setter
    def analysis_profiler_BufferDynamicData39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_profiler_BufferDynamicData__analysis_profiler_BufferDynamicData39", None)
        self.__analysis_profiler_BufferDynamicData39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActionToLongMap"):
                    opp_val = getattr(item, "ActionToLongMap", None)
                    
                    if opp_val == self:
                        setattr(item, "ActionToLongMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActionToLongMap"):
                    opp_val = getattr(item, "ActionToLongMap", None)
                    
                    setattr(item, "ActionToLongMap", self)
                    

    @property
    def analysis_profiler_BufferDynamicData28(self):
        return self.__analysis_profiler_BufferDynamicData28

    @analysis_profiler_BufferDynamicData28.setter
    def analysis_profiler_BufferDynamicData28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_profiler_BufferDynamicData__analysis_profiler_BufferDynamicData28", None)
        self.__analysis_profiler_BufferDynamicData28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profiler_analysis_StatisticalData29"):
                opp_val = getattr(old_value, "profiler_analysis_StatisticalData29", None)
                if opp_val == self:
                    setattr(old_value, "profiler_analysis_StatisticalData29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profiler_analysis_StatisticalData29"):
                opp_val = getattr(value, "profiler_analysis_StatisticalData29", None)
                setattr(value, "profiler_analysis_StatisticalData29", self)

    @property
    def analysis_profiler_BufferDynamicData26(self):
        return self.__analysis_profiler_BufferDynamicData26

    @analysis_profiler_BufferDynamicData26.setter
    def analysis_profiler_BufferDynamicData26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_profiler_BufferDynamicData__analysis_profiler_BufferDynamicData26", None)
        self.__analysis_profiler_BufferDynamicData26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profiler_analysis_StatisticalData"):
                opp_val = getattr(old_value, "profiler_analysis_StatisticalData", None)
                if opp_val == self:
                    setattr(old_value, "profiler_analysis_StatisticalData", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profiler_analysis_StatisticalData"):
                opp_val = getattr(value, "profiler_analysis_StatisticalData", None)
                setattr(value, "profiler_analysis_StatisticalData", self)

    @property
    def analysis_profiler_BufferDynamicData41(self):
        return self.__analysis_profiler_BufferDynamicData41

    @analysis_profiler_BufferDynamicData41.setter
    def analysis_profiler_BufferDynamicData41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_profiler_BufferDynamicData__analysis_profiler_BufferDynamicData41", None)
        self.__analysis_profiler_BufferDynamicData41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActionToLongMap42"):
                    opp_val = getattr(item, "ActionToLongMap42", None)
                    
                    if opp_val == self:
                        setattr(item, "ActionToLongMap42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActionToLongMap42"):
                    opp_val = getattr(item, "ActionToLongMap42", None)
                    
                    setattr(item, "ActionToLongMap42", self)
                    

    @property
    def analysis_profiler_BufferDynamicData31(self):
        return self.__analysis_profiler_BufferDynamicData31

    @analysis_profiler_BufferDynamicData31.setter
    def analysis_profiler_BufferDynamicData31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_profiler_BufferDynamicData__analysis_profiler_BufferDynamicData31", None)
        self.__analysis_profiler_BufferDynamicData31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profiler_analysis_StatisticalData32"):
                opp_val = getattr(old_value, "profiler_analysis_StatisticalData32", None)
                if opp_val == self:
                    setattr(old_value, "profiler_analysis_StatisticalData32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profiler_analysis_StatisticalData32"):
                opp_val = getattr(value, "profiler_analysis_StatisticalData32", None)
                setattr(value, "profiler_analysis_StatisticalData32", self)

    @property
    def analysis_profiler_BufferDynamicData34(self):
        return self.__analysis_profiler_BufferDynamicData34

    @analysis_profiler_BufferDynamicData34.setter
    def analysis_profiler_BufferDynamicData34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_profiler_BufferDynamicData__analysis_profiler_BufferDynamicData34", None)
        self.__analysis_profiler_BufferDynamicData34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActionToStatisticalDataMap"):
                    opp_val = getattr(item, "ActionToStatisticalDataMap", None)
                    
                    if opp_val == self:
                        setattr(item, "ActionToStatisticalDataMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActionToStatisticalDataMap"):
                    opp_val = getattr(item, "ActionToStatisticalDataMap", None)
                    
                    setattr(item, "ActionToStatisticalDataMap", self)
                    

class ComplexCodeData:

    pass
class profiler_analysis_Network:

    pass
class AnalysisReport:

    pass
class analysis_profiler_MemoryProfilingReport(AnalysisReport):

    def __init__(self, networkName: str, analysis_profiler_MemoryProfilingReport: set["ActionMemoryProfilingData"] = None):
        self.networkName = networkName
        self.analysis_profiler_MemoryProfilingReport = analysis_profiler_MemoryProfilingReport if analysis_profiler_MemoryProfilingReport is not None else set()
        
    @property
    def networkName(self) -> str:
        return self.__networkName

    @networkName.setter
    def networkName(self, networkName: str):
        self.__networkName = networkName

    @property
    def analysis_profiler_MemoryProfilingReport(self):
        return self.__analysis_profiler_MemoryProfilingReport

    @analysis_profiler_MemoryProfilingReport.setter
    def analysis_profiler_MemoryProfilingReport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_profiler_MemoryProfilingReport__analysis_profiler_MemoryProfilingReport", None)
        self.__analysis_profiler_MemoryProfilingReport = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActionMemoryProfilingData"):
                    opp_val = getattr(item, "ActionMemoryProfilingData", None)
                    
                    if opp_val == self:
                        setattr(item, "ActionMemoryProfilingData", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActionMemoryProfilingData"):
                    opp_val = getattr(item, "ActionMemoryProfilingData", None)
                    
                    setattr(item, "ActionMemoryProfilingData", self)
                    

    def getActionData(self, actor: str, action: str) -> str:
        # TODO: Implement getActionData method
        pass

class analysis_profiling_ProfilingStatsReport(AnalysisReport):

    def __init__(self, networkName: str, analysis_profiling_ProfilingStatsReport: set["ProfilingStatsActorData"] = None):
        self.networkName = networkName
        self.analysis_profiling_ProfilingStatsReport = analysis_profiling_ProfilingStatsReport if analysis_profiling_ProfilingStatsReport is not None else set()
        
    @property
    def networkName(self) -> str:
        return self.__networkName

    @networkName.setter
    def networkName(self, networkName: str):
        self.__networkName = networkName

    @property
    def analysis_profiling_ProfilingStatsReport(self):
        return self.__analysis_profiling_ProfilingStatsReport

    @analysis_profiling_ProfilingStatsReport.setter
    def analysis_profiling_ProfilingStatsReport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_profiling_ProfilingStatsReport__analysis_profiling_ProfilingStatsReport", None)
        self.__analysis_profiling_ProfilingStatsReport = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ProfilingStatsActorData"):
                    opp_val = getattr(item, "ProfilingStatsActorData", None)
                    
                    if opp_val == self:
                        setattr(item, "ProfilingStatsActorData", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ProfilingStatsActorData"):
                    opp_val = getattr(item, "ProfilingStatsActorData", None)
                    
                    setattr(item, "ProfilingStatsActorData", self)
                    

class analysis_bottlenecks_ImpactAnalysisReport(AnalysisReport):

    def __init__(self, classLevel: bool, analysis_bottlenecks_ImpactAnalysisReport: "bottlenecks_analysis_Network" = None, analysis_bottlenecks_ImpactAnalysisReport212: set["ImpactAnalysisData"] = None, analysis_bottlenecks_ImpactAnalysisReport214: "BottlenecksReport" = None):
        self.classLevel = classLevel
        self.analysis_bottlenecks_ImpactAnalysisReport = analysis_bottlenecks_ImpactAnalysisReport
        self.analysis_bottlenecks_ImpactAnalysisReport212 = analysis_bottlenecks_ImpactAnalysisReport212 if analysis_bottlenecks_ImpactAnalysisReport212 is not None else set()
        self.analysis_bottlenecks_ImpactAnalysisReport214 = analysis_bottlenecks_ImpactAnalysisReport214
        
    @property
    def classLevel(self) -> bool:
        return self.__classLevel

    @classLevel.setter
    def classLevel(self, classLevel: bool):
        self.__classLevel = classLevel

    @property
    def analysis_bottlenecks_ImpactAnalysisReport(self):
        return self.__analysis_bottlenecks_ImpactAnalysisReport

    @analysis_bottlenecks_ImpactAnalysisReport.setter
    def analysis_bottlenecks_ImpactAnalysisReport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_bottlenecks_ImpactAnalysisReport__analysis_bottlenecks_ImpactAnalysisReport", None)
        self.__analysis_bottlenecks_ImpactAnalysisReport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bottlenecks_analysis_Network210"):
                opp_val = getattr(old_value, "bottlenecks_analysis_Network210", None)
                if opp_val == self:
                    setattr(old_value, "bottlenecks_analysis_Network210", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bottlenecks_analysis_Network210"):
                opp_val = getattr(value, "bottlenecks_analysis_Network210", None)
                setattr(value, "bottlenecks_analysis_Network210", self)

    @property
    def analysis_bottlenecks_ImpactAnalysisReport212(self):
        return self.__analysis_bottlenecks_ImpactAnalysisReport212

    @analysis_bottlenecks_ImpactAnalysisReport212.setter
    def analysis_bottlenecks_ImpactAnalysisReport212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_bottlenecks_ImpactAnalysisReport__analysis_bottlenecks_ImpactAnalysisReport212", None)
        self.__analysis_bottlenecks_ImpactAnalysisReport212 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ImpactAnalysisData"):
                    opp_val = getattr(item, "ImpactAnalysisData", None)
                    
                    if opp_val == self:
                        setattr(item, "ImpactAnalysisData", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ImpactAnalysisData"):
                    opp_val = getattr(item, "ImpactAnalysisData", None)
                    
                    setattr(item, "ImpactAnalysisData", self)
                    

    @property
    def analysis_bottlenecks_ImpactAnalysisReport214(self):
        return self.__analysis_bottlenecks_ImpactAnalysisReport214

    @analysis_bottlenecks_ImpactAnalysisReport214.setter
    def analysis_bottlenecks_ImpactAnalysisReport214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_bottlenecks_ImpactAnalysisReport__analysis_bottlenecks_ImpactAnalysisReport214", None)
        self.__analysis_bottlenecks_ImpactAnalysisReport214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BottlenecksReport"):
                opp_val = getattr(old_value, "BottlenecksReport", None)
                if opp_val == self:
                    setattr(old_value, "BottlenecksReport", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BottlenecksReport"):
                opp_val = getattr(value, "BottlenecksReport", None)
                setattr(value, "BottlenecksReport", self)

class analysis_profiling_IntraActionCommunicationReport(AnalysisReport):

    pass
class analysis_bottlenecks_ScheduledImpactAnalysisReport(AnalysisReport):

    def __init__(self, classLevel: bool, analysis_bottlenecks_ScheduledImpactAnalysisReport: "bottlenecks_analysis_Network" = None, analysis_bottlenecks_ScheduledImpactAnalysisReport257: set["ScheduledImpactAnalysisData"] = None, analysis_bottlenecks_ScheduledImpactAnalysisReport259: "BottlenecksWithSchedulingReport" = None):
        self.classLevel = classLevel
        self.analysis_bottlenecks_ScheduledImpactAnalysisReport = analysis_bottlenecks_ScheduledImpactAnalysisReport
        self.analysis_bottlenecks_ScheduledImpactAnalysisReport257 = analysis_bottlenecks_ScheduledImpactAnalysisReport257 if analysis_bottlenecks_ScheduledImpactAnalysisReport257 is not None else set()
        self.analysis_bottlenecks_ScheduledImpactAnalysisReport259 = analysis_bottlenecks_ScheduledImpactAnalysisReport259
        
    @property
    def classLevel(self) -> bool:
        return self.__classLevel

    @classLevel.setter
    def classLevel(self, classLevel: bool):
        self.__classLevel = classLevel

    @property
    def analysis_bottlenecks_ScheduledImpactAnalysisReport259(self):
        return self.__analysis_bottlenecks_ScheduledImpactAnalysisReport259

    @analysis_bottlenecks_ScheduledImpactAnalysisReport259.setter
    def analysis_bottlenecks_ScheduledImpactAnalysisReport259(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_bottlenecks_ScheduledImpactAnalysisReport__analysis_bottlenecks_ScheduledImpactAnalysisReport259", None)
        self.__analysis_bottlenecks_ScheduledImpactAnalysisReport259 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BottlenecksWithSchedulingReport260"):
                opp_val = getattr(old_value, "BottlenecksWithSchedulingReport260", None)
                if opp_val == self:
                    setattr(old_value, "BottlenecksWithSchedulingReport260", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BottlenecksWithSchedulingReport260"):
                opp_val = getattr(value, "BottlenecksWithSchedulingReport260", None)
                setattr(value, "BottlenecksWithSchedulingReport260", self)

    @property
    def analysis_bottlenecks_ScheduledImpactAnalysisReport(self):
        return self.__analysis_bottlenecks_ScheduledImpactAnalysisReport

    @analysis_bottlenecks_ScheduledImpactAnalysisReport.setter
    def analysis_bottlenecks_ScheduledImpactAnalysisReport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_bottlenecks_ScheduledImpactAnalysisReport__analysis_bottlenecks_ScheduledImpactAnalysisReport", None)
        self.__analysis_bottlenecks_ScheduledImpactAnalysisReport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bottlenecks_analysis_Network255"):
                opp_val = getattr(old_value, "bottlenecks_analysis_Network255", None)
                if opp_val == self:
                    setattr(old_value, "bottlenecks_analysis_Network255", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bottlenecks_analysis_Network255"):
                opp_val = getattr(value, "bottlenecks_analysis_Network255", None)
                setattr(value, "bottlenecks_analysis_Network255", self)

    @property
    def analysis_bottlenecks_ScheduledImpactAnalysisReport257(self):
        return self.__analysis_bottlenecks_ScheduledImpactAnalysisReport257

    @analysis_bottlenecks_ScheduledImpactAnalysisReport257.setter
    def analysis_bottlenecks_ScheduledImpactAnalysisReport257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_bottlenecks_ScheduledImpactAnalysisReport__analysis_bottlenecks_ScheduledImpactAnalysisReport257", None)
        self.__analysis_bottlenecks_ScheduledImpactAnalysisReport257 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ScheduledImpactAnalysisData"):
                    opp_val = getattr(item, "ScheduledImpactAnalysisData", None)
                    
                    if opp_val == self:
                        setattr(item, "ScheduledImpactAnalysisData", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ScheduledImpactAnalysisData"):
                    opp_val = getattr(item, "ScheduledImpactAnalysisData", None)
                    
                    setattr(item, "ScheduledImpactAnalysisData", self)
                    

class analysis_pipelining_ImpactAnalysisReport(AnalysisReport):

    pass
class analysis_trace_TraceComparatorReport(AnalysisReport):

    pass
class analysis_buffers_BoundedBuffersReport(AnalysisReport):

    def __init__(self, pow2: bool, bitAccurate: bool, tokenSize: int, bitSize: int, analysis_buffers_BoundedBuffersReport: "buffers_analysis_Network" = None, analysis_buffers_BoundedBuffersReport263: set["BoundedBufferData"] = None):
        self.pow2 = pow2
        self.bitAccurate = bitAccurate
        self.tokenSize = tokenSize
        self.bitSize = bitSize
        self.analysis_buffers_BoundedBuffersReport = analysis_buffers_BoundedBuffersReport
        self.analysis_buffers_BoundedBuffersReport263 = analysis_buffers_BoundedBuffersReport263 if analysis_buffers_BoundedBuffersReport263 is not None else set()
        
    @property
    def pow2(self) -> bool:
        return self.__pow2

    @pow2.setter
    def pow2(self, pow2: bool):
        self.__pow2 = pow2

    @property
    def bitSize(self) -> int:
        return self.__bitSize

    @bitSize.setter
    def bitSize(self, bitSize: int):
        self.__bitSize = bitSize

    @property
    def tokenSize(self) -> int:
        return self.__tokenSize

    @tokenSize.setter
    def tokenSize(self, tokenSize: int):
        self.__tokenSize = tokenSize

    @property
    def bitAccurate(self) -> bool:
        return self.__bitAccurate

    @bitAccurate.setter
    def bitAccurate(self, bitAccurate: bool):
        self.__bitAccurate = bitAccurate

    @property
    def analysis_buffers_BoundedBuffersReport263(self):
        return self.__analysis_buffers_BoundedBuffersReport263

    @analysis_buffers_BoundedBuffersReport263.setter
    def analysis_buffers_BoundedBuffersReport263(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_buffers_BoundedBuffersReport__analysis_buffers_BoundedBuffersReport263", None)
        self.__analysis_buffers_BoundedBuffersReport263 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BoundedBufferData"):
                    opp_val = getattr(item, "BoundedBufferData", None)
                    
                    if opp_val == self:
                        setattr(item, "BoundedBufferData", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BoundedBufferData"):
                    opp_val = getattr(item, "BoundedBufferData", None)
                    
                    setattr(item, "BoundedBufferData", self)
                    

    @property
    def analysis_buffers_BoundedBuffersReport(self):
        return self.__analysis_buffers_BoundedBuffersReport

    @analysis_buffers_BoundedBuffersReport.setter
    def analysis_buffers_BoundedBuffersReport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_buffers_BoundedBuffersReport__analysis_buffers_BoundedBuffersReport", None)
        self.__analysis_buffers_BoundedBuffersReport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "buffers_analysis_Network"):
                opp_val = getattr(old_value, "buffers_analysis_Network", None)
                if opp_val == self:
                    setattr(old_value, "buffers_analysis_Network", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "buffers_analysis_Network"):
                opp_val = getattr(value, "buffers_analysis_Network", None)
                setattr(value, "buffers_analysis_Network", self)

class analysis_buffers_OptimalBuffersReport(AnalysisReport):

    def __init__(self, pow2: bool, bitAccurate: bool, analysis_buffers_OptimalBuffersReport: "buffers_analysis_Network" = None, analysis_buffers_OptimalBuffersReport268: set["OptimalBufferData"] = None, analysis_buffers_OptimalBuffersReport270: "BoundedBuffersReport" = None, analysis_buffers_OptimalBuffersReport272: "BottlenecksWithSchedulingReport" = None):
        self.pow2 = pow2
        self.bitAccurate = bitAccurate
        self.analysis_buffers_OptimalBuffersReport = analysis_buffers_OptimalBuffersReport
        self.analysis_buffers_OptimalBuffersReport268 = analysis_buffers_OptimalBuffersReport268 if analysis_buffers_OptimalBuffersReport268 is not None else set()
        self.analysis_buffers_OptimalBuffersReport270 = analysis_buffers_OptimalBuffersReport270
        self.analysis_buffers_OptimalBuffersReport272 = analysis_buffers_OptimalBuffersReport272
        
    @property
    def bitAccurate(self) -> bool:
        return self.__bitAccurate

    @bitAccurate.setter
    def bitAccurate(self, bitAccurate: bool):
        self.__bitAccurate = bitAccurate

    @property
    def pow2(self) -> bool:
        return self.__pow2

    @pow2.setter
    def pow2(self, pow2: bool):
        self.__pow2 = pow2

    @property
    def analysis_buffers_OptimalBuffersReport(self):
        return self.__analysis_buffers_OptimalBuffersReport

    @analysis_buffers_OptimalBuffersReport.setter
    def analysis_buffers_OptimalBuffersReport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_buffers_OptimalBuffersReport__analysis_buffers_OptimalBuffersReport", None)
        self.__analysis_buffers_OptimalBuffersReport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "buffers_analysis_Network266"):
                opp_val = getattr(old_value, "buffers_analysis_Network266", None)
                if opp_val == self:
                    setattr(old_value, "buffers_analysis_Network266", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "buffers_analysis_Network266"):
                opp_val = getattr(value, "buffers_analysis_Network266", None)
                setattr(value, "buffers_analysis_Network266", self)

    @property
    def analysis_buffers_OptimalBuffersReport268(self):
        return self.__analysis_buffers_OptimalBuffersReport268

    @analysis_buffers_OptimalBuffersReport268.setter
    def analysis_buffers_OptimalBuffersReport268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_buffers_OptimalBuffersReport__analysis_buffers_OptimalBuffersReport268", None)
        self.__analysis_buffers_OptimalBuffersReport268 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OptimalBufferData"):
                    opp_val = getattr(item, "OptimalBufferData", None)
                    
                    if opp_val == self:
                        setattr(item, "OptimalBufferData", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OptimalBufferData"):
                    opp_val = getattr(item, "OptimalBufferData", None)
                    
                    setattr(item, "OptimalBufferData", self)
                    

    @property
    def analysis_buffers_OptimalBuffersReport272(self):
        return self.__analysis_buffers_OptimalBuffersReport272

    @analysis_buffers_OptimalBuffersReport272.setter
    def analysis_buffers_OptimalBuffersReport272(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_buffers_OptimalBuffersReport__analysis_buffers_OptimalBuffersReport272", None)
        self.__analysis_buffers_OptimalBuffersReport272 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BottlenecksWithSchedulingReport273"):
                opp_val = getattr(old_value, "BottlenecksWithSchedulingReport273", None)
                if opp_val == self:
                    setattr(old_value, "BottlenecksWithSchedulingReport273", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BottlenecksWithSchedulingReport273"):
                opp_val = getattr(value, "BottlenecksWithSchedulingReport273", None)
                setattr(value, "BottlenecksWithSchedulingReport273", self)

    @property
    def analysis_buffers_OptimalBuffersReport270(self):
        return self.__analysis_buffers_OptimalBuffersReport270

    @analysis_buffers_OptimalBuffersReport270.setter
    def analysis_buffers_OptimalBuffersReport270(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_buffers_OptimalBuffersReport__analysis_buffers_OptimalBuffersReport270", None)
        self.__analysis_buffers_OptimalBuffersReport270 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BoundedBuffersReport"):
                opp_val = getattr(old_value, "BoundedBuffersReport", None)
                if opp_val == self:
                    setattr(old_value, "BoundedBuffersReport", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BoundedBuffersReport"):
                opp_val = getattr(value, "BoundedBuffersReport", None)
                setattr(value, "BoundedBuffersReport", self)

class analysis_caseoptimal_CaseOptimalScheduleReport(AnalysisReport):

    def __init__(self, traceFile: str, pipeline: str, partitionFilePath: str, analysis_caseoptimal_CaseOptimalScheduleReport: set["PartitionToActorSelectionScheduleMap"] = None):
        self.traceFile = traceFile
        self.pipeline = pipeline
        self.partitionFilePath = partitionFilePath
        self.analysis_caseoptimal_CaseOptimalScheduleReport = analysis_caseoptimal_CaseOptimalScheduleReport if analysis_caseoptimal_CaseOptimalScheduleReport is not None else set()
        
    @property
    def partitionFilePath(self) -> str:
        return self.__partitionFilePath

    @partitionFilePath.setter
    def partitionFilePath(self, partitionFilePath: str):
        self.__partitionFilePath = partitionFilePath

    @property
    def pipeline(self) -> str:
        return self.__pipeline

    @pipeline.setter
    def pipeline(self, pipeline: str):
        self.__pipeline = pipeline

    @property
    def traceFile(self) -> str:
        return self.__traceFile

    @traceFile.setter
    def traceFile(self, traceFile: str):
        self.__traceFile = traceFile

    @property
    def analysis_caseoptimal_CaseOptimalScheduleReport(self):
        return self.__analysis_caseoptimal_CaseOptimalScheduleReport

    @analysis_caseoptimal_CaseOptimalScheduleReport.setter
    def analysis_caseoptimal_CaseOptimalScheduleReport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_caseoptimal_CaseOptimalScheduleReport__analysis_caseoptimal_CaseOptimalScheduleReport", None)
        self.__analysis_caseoptimal_CaseOptimalScheduleReport = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PartitionToActorSelectionScheduleMap"):
                    opp_val = getattr(item, "PartitionToActorSelectionScheduleMap", None)
                    
                    if opp_val == self:
                        setattr(item, "PartitionToActorSelectionScheduleMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PartitionToActorSelectionScheduleMap"):
                    opp_val = getattr(item, "PartitionToActorSelectionScheduleMap", None)
                    
                    setattr(item, "PartitionToActorSelectionScheduleMap", self)
                    

class analysis_partitioning_WorkloadBalancePartitioningReport(AnalysisReport):

    pass
class analysis_pipelining_ActionsVariablePipeliningReport(AnalysisReport):

    pass
class analysis_profiler_BenchmarkReport(AnalysisReport):

    def __init__(self, column_names: str, analysis_profiler_BenchmarkReport: set["TableRow"] = None):
        self.column_names = column_names
        self.analysis_profiler_BenchmarkReport = analysis_profiler_BenchmarkReport if analysis_profiler_BenchmarkReport is not None else set()
        
    @property
    def column_names(self) -> str:
        return self.__column_names

    @column_names.setter
    def column_names(self, column_names: str):
        self.__column_names = column_names

    @property
    def analysis_profiler_BenchmarkReport(self):
        return self.__analysis_profiler_BenchmarkReport

    @analysis_profiler_BenchmarkReport.setter
    def analysis_profiler_BenchmarkReport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_profiler_BenchmarkReport__analysis_profiler_BenchmarkReport", None)
        self.__analysis_profiler_BenchmarkReport = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TableRow"):
                    opp_val = getattr(item, "TableRow", None)
                    
                    if opp_val == self:
                        setattr(item, "TableRow", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TableRow"):
                    opp_val = getattr(item, "TableRow", None)
                    
                    setattr(item, "TableRow", self)
                    

class analysis_trace_CompressedTraceReport(AnalysisReport):

    def __init__(self, traceFile: str, analysis_trace_CompressedTraceReport: "trace_analysis_Network" = None, analysis_trace_CompressedTraceReport138: set["CompressedStep"] = None, analysis_trace_CompressedTraceReport140: set["CompressedDependency"] = None):
        self.traceFile = traceFile
        self.analysis_trace_CompressedTraceReport = analysis_trace_CompressedTraceReport
        self.analysis_trace_CompressedTraceReport138 = analysis_trace_CompressedTraceReport138 if analysis_trace_CompressedTraceReport138 is not None else set()
        self.analysis_trace_CompressedTraceReport140 = analysis_trace_CompressedTraceReport140 if analysis_trace_CompressedTraceReport140 is not None else set()
        
    @property
    def traceFile(self) -> str:
        return self.__traceFile

    @traceFile.setter
    def traceFile(self, traceFile: str):
        self.__traceFile = traceFile

    @property
    def analysis_trace_CompressedTraceReport140(self):
        return self.__analysis_trace_CompressedTraceReport140

    @analysis_trace_CompressedTraceReport140.setter
    def analysis_trace_CompressedTraceReport140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_trace_CompressedTraceReport__analysis_trace_CompressedTraceReport140", None)
        self.__analysis_trace_CompressedTraceReport140 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompressedDependency"):
                    opp_val = getattr(item, "CompressedDependency", None)
                    
                    if opp_val == self:
                        setattr(item, "CompressedDependency", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompressedDependency"):
                    opp_val = getattr(item, "CompressedDependency", None)
                    
                    setattr(item, "CompressedDependency", self)
                    

    @property
    def analysis_trace_CompressedTraceReport(self):
        return self.__analysis_trace_CompressedTraceReport

    @analysis_trace_CompressedTraceReport.setter
    def analysis_trace_CompressedTraceReport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_trace_CompressedTraceReport__analysis_trace_CompressedTraceReport", None)
        self.__analysis_trace_CompressedTraceReport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_analysis_Network136"):
                opp_val = getattr(old_value, "trace_analysis_Network136", None)
                if opp_val == self:
                    setattr(old_value, "trace_analysis_Network136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_analysis_Network136"):
                opp_val = getattr(value, "trace_analysis_Network136", None)
                setattr(value, "trace_analysis_Network136", self)

    @property
    def analysis_trace_CompressedTraceReport138(self):
        return self.__analysis_trace_CompressedTraceReport138

    @analysis_trace_CompressedTraceReport138.setter
    def analysis_trace_CompressedTraceReport138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_trace_CompressedTraceReport__analysis_trace_CompressedTraceReport138", None)
        self.__analysis_trace_CompressedTraceReport138 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompressedStep"):
                    opp_val = getattr(item, "CompressedStep", None)
                    
                    if opp_val == self:
                        setattr(item, "CompressedStep", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompressedStep"):
                    opp_val = getattr(item, "CompressedStep", None)
                    
                    setattr(item, "CompressedStep", self)
                    

    def getSteps(self, action: str) -> str:
        # TODO: Implement getSteps method
        pass

    def getSteps(self, actor: str) -> str:
        # TODO: Implement getSteps method
        pass

class analysis_scheduling_MarkovSimpleSchedulerReport(AnalysisReport, postprocessing_PostProcessingData):

    pass
class analysis_partitioning_ComCostPartitioningReport(AnalysisReport):

    def __init__(self, bitAccurate: bool, analysis_partitioning_ComCostPartitioningReport: "partitioning_analysis_Network" = None, analysis_partitioning_ComCostPartitioningReport281: set["ComCostPartition"] = None):
        self.bitAccurate = bitAccurate
        self.analysis_partitioning_ComCostPartitioningReport = analysis_partitioning_ComCostPartitioningReport
        self.analysis_partitioning_ComCostPartitioningReport281 = analysis_partitioning_ComCostPartitioningReport281 if analysis_partitioning_ComCostPartitioningReport281 is not None else set()
        
    @property
    def bitAccurate(self) -> bool:
        return self.__bitAccurate

    @bitAccurate.setter
    def bitAccurate(self, bitAccurate: bool):
        self.__bitAccurate = bitAccurate

    @property
    def analysis_partitioning_ComCostPartitioningReport281(self):
        return self.__analysis_partitioning_ComCostPartitioningReport281

    @analysis_partitioning_ComCostPartitioningReport281.setter
    def analysis_partitioning_ComCostPartitioningReport281(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_partitioning_ComCostPartitioningReport__analysis_partitioning_ComCostPartitioningReport281", None)
        self.__analysis_partitioning_ComCostPartitioningReport281 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ComCostPartition"):
                    opp_val = getattr(item, "ComCostPartition", None)
                    
                    if opp_val == self:
                        setattr(item, "ComCostPartition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ComCostPartition"):
                    opp_val = getattr(item, "ComCostPartition", None)
                    
                    setattr(item, "ComCostPartition", self)
                    

    @property
    def analysis_partitioning_ComCostPartitioningReport(self):
        return self.__analysis_partitioning_ComCostPartitioningReport

    @analysis_partitioning_ComCostPartitioningReport.setter
    def analysis_partitioning_ComCostPartitioningReport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_partitioning_ComCostPartitioningReport__analysis_partitioning_ComCostPartitioningReport", None)
        self.__analysis_partitioning_ComCostPartitioningReport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "partitioning_analysis_Network"):
                opp_val = getattr(old_value, "partitioning_analysis_Network", None)
                if opp_val == self:
                    setattr(old_value, "partitioning_analysis_Network", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "partitioning_analysis_Network"):
                opp_val = getattr(value, "partitioning_analysis_Network", None)
                setattr(value, "partitioning_analysis_Network", self)

class analysis_bottlenecks_BottlenecksReport(AnalysisReport):

    def __init__(self, cpWeight: float, cpVariance: float, totalWeight: float, totalVariance: float, cpFirings: str, totalFirings: str, analysis_bottlenecks_BottlenecksReport: "bottlenecks_analysis_Network" = None, analysis_bottlenecks_BottlenecksReport207: set["ActionBottlenecksData"] = None):
        self.cpWeight = cpWeight
        self.cpVariance = cpVariance
        self.totalWeight = totalWeight
        self.totalVariance = totalVariance
        self.cpFirings = cpFirings
        self.totalFirings = totalFirings
        self.analysis_bottlenecks_BottlenecksReport = analysis_bottlenecks_BottlenecksReport
        self.analysis_bottlenecks_BottlenecksReport207 = analysis_bottlenecks_BottlenecksReport207 if analysis_bottlenecks_BottlenecksReport207 is not None else set()
        
    @property
    def totalWeight(self) -> float:
        return self.__totalWeight

    @totalWeight.setter
    def totalWeight(self, totalWeight: float):
        self.__totalWeight = totalWeight

    @property
    def cpVariance(self) -> float:
        return self.__cpVariance

    @cpVariance.setter
    def cpVariance(self, cpVariance: float):
        self.__cpVariance = cpVariance

    @property
    def totalVariance(self) -> float:
        return self.__totalVariance

    @totalVariance.setter
    def totalVariance(self, totalVariance: float):
        self.__totalVariance = totalVariance

    @property
    def cpFirings(self) -> str:
        return self.__cpFirings

    @cpFirings.setter
    def cpFirings(self, cpFirings: str):
        self.__cpFirings = cpFirings

    @property
    def cpWeight(self) -> float:
        return self.__cpWeight

    @cpWeight.setter
    def cpWeight(self, cpWeight: float):
        self.__cpWeight = cpWeight

    @property
    def totalFirings(self) -> str:
        return self.__totalFirings

    @totalFirings.setter
    def totalFirings(self, totalFirings: str):
        self.__totalFirings = totalFirings

    @property
    def analysis_bottlenecks_BottlenecksReport207(self):
        return self.__analysis_bottlenecks_BottlenecksReport207

    @analysis_bottlenecks_BottlenecksReport207.setter
    def analysis_bottlenecks_BottlenecksReport207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_bottlenecks_BottlenecksReport__analysis_bottlenecks_BottlenecksReport207", None)
        self.__analysis_bottlenecks_BottlenecksReport207 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActionBottlenecksData"):
                    opp_val = getattr(item, "ActionBottlenecksData", None)
                    
                    if opp_val == self:
                        setattr(item, "ActionBottlenecksData", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActionBottlenecksData"):
                    opp_val = getattr(item, "ActionBottlenecksData", None)
                    
                    setattr(item, "ActionBottlenecksData", self)
                    

    @property
    def analysis_bottlenecks_BottlenecksReport(self):
        return self.__analysis_bottlenecks_BottlenecksReport

    @analysis_bottlenecks_BottlenecksReport.setter
    def analysis_bottlenecks_BottlenecksReport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_bottlenecks_BottlenecksReport__analysis_bottlenecks_BottlenecksReport", None)
        self.__analysis_bottlenecks_BottlenecksReport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bottlenecks_analysis_Network"):
                opp_val = getattr(old_value, "bottlenecks_analysis_Network", None)
                if opp_val == self:
                    setattr(old_value, "bottlenecks_analysis_Network", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bottlenecks_analysis_Network"):
                opp_val = getattr(value, "bottlenecks_analysis_Network", None)
                setattr(value, "bottlenecks_analysis_Network", self)

class analysis_profiler_DynamicProfilingReport(AnalysisReport):

    pass
class analysis_postprocessing_PostProcessingReport(AnalysisReport):

    def __init__(self, time: float, deadlock: bool, analysis_postprocessing_PostProcessingReport: "postprocessing_analysis_Network" = None, analysis_postprocessing_PostProcessingReport329: set["PostProcessingData"] = None):
        self.time = time
        self.deadlock = deadlock
        self.analysis_postprocessing_PostProcessingReport = analysis_postprocessing_PostProcessingReport
        self.analysis_postprocessing_PostProcessingReport329 = analysis_postprocessing_PostProcessingReport329 if analysis_postprocessing_PostProcessingReport329 is not None else set()
        
    @property
    def deadlock(self) -> bool:
        return self.__deadlock

    @deadlock.setter
    def deadlock(self, deadlock: bool):
        self.__deadlock = deadlock

    @property
    def time(self) -> float:
        return self.__time

    @time.setter
    def time(self, time: float):
        self.__time = time

    @property
    def analysis_postprocessing_PostProcessingReport(self):
        return self.__analysis_postprocessing_PostProcessingReport

    @analysis_postprocessing_PostProcessingReport.setter
    def analysis_postprocessing_PostProcessingReport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_postprocessing_PostProcessingReport__analysis_postprocessing_PostProcessingReport", None)
        self.__analysis_postprocessing_PostProcessingReport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "postprocessing_analysis_Network"):
                opp_val = getattr(old_value, "postprocessing_analysis_Network", None)
                if opp_val == self:
                    setattr(old_value, "postprocessing_analysis_Network", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "postprocessing_analysis_Network"):
                opp_val = getattr(value, "postprocessing_analysis_Network", None)
                setattr(value, "postprocessing_analysis_Network", self)

    @property
    def analysis_postprocessing_PostProcessingReport329(self):
        return self.__analysis_postprocessing_PostProcessingReport329

    @analysis_postprocessing_PostProcessingReport329.setter
    def analysis_postprocessing_PostProcessingReport329(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_postprocessing_PostProcessingReport__analysis_postprocessing_PostProcessingReport329", None)
        self.__analysis_postprocessing_PostProcessingReport329 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PostProcessingData"):
                    opp_val = getattr(item, "PostProcessingData", None)
                    
                    if opp_val == self:
                        setattr(item, "PostProcessingData", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PostProcessingData"):
                    opp_val = getattr(item, "PostProcessingData", None)
                    
                    setattr(item, "PostProcessingData", self)
                    

class analysis_trace_MarkowModelTraceReport(AnalysisReport):

    def __init__(self, analysis_trace_MarkowModelTraceReport: "trace_analysis_Network" = None, analysis_trace_MarkowModelTraceReport199: set["MarkovModelActionData"] = None):
        self.analysis_trace_MarkowModelTraceReport = analysis_trace_MarkowModelTraceReport
        self.analysis_trace_MarkowModelTraceReport199 = analysis_trace_MarkowModelTraceReport199 if analysis_trace_MarkowModelTraceReport199 is not None else set()
        
    @property
    def analysis_trace_MarkowModelTraceReport(self):
        return self.__analysis_trace_MarkowModelTraceReport

    @analysis_trace_MarkowModelTraceReport.setter
    def analysis_trace_MarkowModelTraceReport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_trace_MarkowModelTraceReport__analysis_trace_MarkowModelTraceReport", None)
        self.__analysis_trace_MarkowModelTraceReport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_analysis_Network197"):
                opp_val = getattr(old_value, "trace_analysis_Network197", None)
                if opp_val == self:
                    setattr(old_value, "trace_analysis_Network197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_analysis_Network197"):
                opp_val = getattr(value, "trace_analysis_Network197", None)
                setattr(value, "trace_analysis_Network197", self)

    @property
    def analysis_trace_MarkowModelTraceReport199(self):
        return self.__analysis_trace_MarkowModelTraceReport199

    @analysis_trace_MarkowModelTraceReport199.setter
    def analysis_trace_MarkowModelTraceReport199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_trace_MarkowModelTraceReport__analysis_trace_MarkowModelTraceReport199", None)
        self.__analysis_trace_MarkowModelTraceReport199 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MarkovModelActionData"):
                    opp_val = getattr(item, "MarkovModelActionData", None)
                    
                    if opp_val == self:
                        setattr(item, "MarkovModelActionData", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MarkovModelActionData"):
                    opp_val = getattr(item, "MarkovModelActionData", None)
                    
                    setattr(item, "MarkovModelActionData", self)
                    

    def getData(self, actor: str) -> str:
        # TODO: Implement getData method
        pass

    def getData(self, action: str) -> str:
        # TODO: Implement getData method
        pass

class analysis_partitioning_BalancedPipelinePartitioningReport(AnalysisReport):

    pass
class analysis_bottlenecks_BottlenecksWithSchedulingReport(AnalysisReport, postprocessing_PostProcessingData):

    def __init__(self, cpWeight: float, totalWeight: float, cpFirings: str, totalFirings: str, executionTime: float, cpBlockingTime: float, analysis_bottlenecks_BottlenecksWithSchedulingReport: "bottlenecks_analysis_Network" = None, analysis_bottlenecks_BottlenecksWithSchedulingReport228: set["ActionBottlenecksWithSchedulingData"] = None, analysis_bottlenecks_BottlenecksWithSchedulingReport230: set["StringToDoubleMap"] = None):
        self.cpWeight = cpWeight
        self.totalWeight = totalWeight
        self.cpFirings = cpFirings
        self.totalFirings = totalFirings
        self.executionTime = executionTime
        self.cpBlockingTime = cpBlockingTime
        self.analysis_bottlenecks_BottlenecksWithSchedulingReport = analysis_bottlenecks_BottlenecksWithSchedulingReport
        self.analysis_bottlenecks_BottlenecksWithSchedulingReport228 = analysis_bottlenecks_BottlenecksWithSchedulingReport228 if analysis_bottlenecks_BottlenecksWithSchedulingReport228 is not None else set()
        self.analysis_bottlenecks_BottlenecksWithSchedulingReport230 = analysis_bottlenecks_BottlenecksWithSchedulingReport230 if analysis_bottlenecks_BottlenecksWithSchedulingReport230 is not None else set()
        
    @property
    def cpBlockingTime(self) -> float:
        return self.__cpBlockingTime

    @cpBlockingTime.setter
    def cpBlockingTime(self, cpBlockingTime: float):
        self.__cpBlockingTime = cpBlockingTime

    @property
    def totalFirings(self) -> str:
        return self.__totalFirings

    @totalFirings.setter
    def totalFirings(self, totalFirings: str):
        self.__totalFirings = totalFirings

    @property
    def executionTime(self) -> float:
        return self.__executionTime

    @executionTime.setter
    def executionTime(self, executionTime: float):
        self.__executionTime = executionTime

    @property
    def cpFirings(self) -> str:
        return self.__cpFirings

    @cpFirings.setter
    def cpFirings(self, cpFirings: str):
        self.__cpFirings = cpFirings

    @property
    def cpWeight(self) -> float:
        return self.__cpWeight

    @cpWeight.setter
    def cpWeight(self, cpWeight: float):
        self.__cpWeight = cpWeight

    @property
    def totalWeight(self) -> float:
        return self.__totalWeight

    @totalWeight.setter
    def totalWeight(self, totalWeight: float):
        self.__totalWeight = totalWeight

    @property
    def analysis_bottlenecks_BottlenecksWithSchedulingReport230(self):
        return self.__analysis_bottlenecks_BottlenecksWithSchedulingReport230

    @analysis_bottlenecks_BottlenecksWithSchedulingReport230.setter
    def analysis_bottlenecks_BottlenecksWithSchedulingReport230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_bottlenecks_BottlenecksWithSchedulingReport__analysis_bottlenecks_BottlenecksWithSchedulingReport230", None)
        self.__analysis_bottlenecks_BottlenecksWithSchedulingReport230 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StringToDoubleMap"):
                    opp_val = getattr(item, "StringToDoubleMap", None)
                    
                    if opp_val == self:
                        setattr(item, "StringToDoubleMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StringToDoubleMap"):
                    opp_val = getattr(item, "StringToDoubleMap", None)
                    
                    setattr(item, "StringToDoubleMap", self)
                    

    @property
    def analysis_bottlenecks_BottlenecksWithSchedulingReport228(self):
        return self.__analysis_bottlenecks_BottlenecksWithSchedulingReport228

    @analysis_bottlenecks_BottlenecksWithSchedulingReport228.setter
    def analysis_bottlenecks_BottlenecksWithSchedulingReport228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_bottlenecks_BottlenecksWithSchedulingReport__analysis_bottlenecks_BottlenecksWithSchedulingReport228", None)
        self.__analysis_bottlenecks_BottlenecksWithSchedulingReport228 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActionBottlenecksWithSchedulingData"):
                    opp_val = getattr(item, "ActionBottlenecksWithSchedulingData", None)
                    
                    if opp_val == self:
                        setattr(item, "ActionBottlenecksWithSchedulingData", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActionBottlenecksWithSchedulingData"):
                    opp_val = getattr(item, "ActionBottlenecksWithSchedulingData", None)
                    
                    setattr(item, "ActionBottlenecksWithSchedulingData", self)
                    

    @property
    def analysis_bottlenecks_BottlenecksWithSchedulingReport(self):
        return self.__analysis_bottlenecks_BottlenecksWithSchedulingReport

    @analysis_bottlenecks_BottlenecksWithSchedulingReport.setter
    def analysis_bottlenecks_BottlenecksWithSchedulingReport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_bottlenecks_BottlenecksWithSchedulingReport__analysis_bottlenecks_BottlenecksWithSchedulingReport", None)
        self.__analysis_bottlenecks_BottlenecksWithSchedulingReport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bottlenecks_analysis_Network226"):
                opp_val = getattr(old_value, "bottlenecks_analysis_Network226", None)
                if opp_val == self:
                    setattr(old_value, "bottlenecks_analysis_Network226", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bottlenecks_analysis_Network226"):
                opp_val = getattr(value, "bottlenecks_analysis_Network226", None)
                setattr(value, "bottlenecks_analysis_Network226", self)

class analysis_trace_TraceSizeReport(AnalysisReport):

    def __init__(self, firings: str, dependencies: str, analysis_trace_TraceSizeReport129: set["ActorToLongMap"] = None, analysis_trace_TraceSizeReport: set["ActionToLongMap"] = None, analysis_trace_TraceSizeReport118: set["ActionToLongMap"] = None, analysis_trace_TraceSizeReport121: set["ActionToLongMap"] = None, analysis_trace_TraceSizeReport124: set["ActorToLongMap"] = None, analysis_trace_TraceSizeReport126: set["ActorToLongMap"] = None, analysis_trace_TraceSizeReport132: set["StringToLongMap"] = None, analysis_trace_TraceSizeReport134: "trace_analysis_Network" = None):
        self.firings = firings
        self.dependencies = dependencies
        self.analysis_trace_TraceSizeReport129 = analysis_trace_TraceSizeReport129 if analysis_trace_TraceSizeReport129 is not None else set()
        self.analysis_trace_TraceSizeReport = analysis_trace_TraceSizeReport if analysis_trace_TraceSizeReport is not None else set()
        self.analysis_trace_TraceSizeReport118 = analysis_trace_TraceSizeReport118 if analysis_trace_TraceSizeReport118 is not None else set()
        self.analysis_trace_TraceSizeReport121 = analysis_trace_TraceSizeReport121 if analysis_trace_TraceSizeReport121 is not None else set()
        self.analysis_trace_TraceSizeReport124 = analysis_trace_TraceSizeReport124 if analysis_trace_TraceSizeReport124 is not None else set()
        self.analysis_trace_TraceSizeReport126 = analysis_trace_TraceSizeReport126 if analysis_trace_TraceSizeReport126 is not None else set()
        self.analysis_trace_TraceSizeReport132 = analysis_trace_TraceSizeReport132 if analysis_trace_TraceSizeReport132 is not None else set()
        self.analysis_trace_TraceSizeReport134 = analysis_trace_TraceSizeReport134
        
    @property
    def dependencies(self) -> str:
        return self.__dependencies

    @dependencies.setter
    def dependencies(self, dependencies: str):
        self.__dependencies = dependencies

    @property
    def firings(self) -> str:
        return self.__firings

    @firings.setter
    def firings(self, firings: str):
        self.__firings = firings

    @property
    def analysis_trace_TraceSizeReport118(self):
        return self.__analysis_trace_TraceSizeReport118

    @analysis_trace_TraceSizeReport118.setter
    def analysis_trace_TraceSizeReport118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_trace_TraceSizeReport__analysis_trace_TraceSizeReport118", None)
        self.__analysis_trace_TraceSizeReport118 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActionToLongMap119"):
                    opp_val = getattr(item, "ActionToLongMap119", None)
                    
                    if opp_val == self:
                        setattr(item, "ActionToLongMap119", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActionToLongMap119"):
                    opp_val = getattr(item, "ActionToLongMap119", None)
                    
                    setattr(item, "ActionToLongMap119", self)
                    

    @property
    def analysis_trace_TraceSizeReport134(self):
        return self.__analysis_trace_TraceSizeReport134

    @analysis_trace_TraceSizeReport134.setter
    def analysis_trace_TraceSizeReport134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_trace_TraceSizeReport__analysis_trace_TraceSizeReport134", None)
        self.__analysis_trace_TraceSizeReport134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_analysis_Network"):
                opp_val = getattr(old_value, "trace_analysis_Network", None)
                if opp_val == self:
                    setattr(old_value, "trace_analysis_Network", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_analysis_Network"):
                opp_val = getattr(value, "trace_analysis_Network", None)
                setattr(value, "trace_analysis_Network", self)

    @property
    def analysis_trace_TraceSizeReport132(self):
        return self.__analysis_trace_TraceSizeReport132

    @analysis_trace_TraceSizeReport132.setter
    def analysis_trace_TraceSizeReport132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_trace_TraceSizeReport__analysis_trace_TraceSizeReport132", None)
        self.__analysis_trace_TraceSizeReport132 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StringToLongMap"):
                    opp_val = getattr(item, "StringToLongMap", None)
                    
                    if opp_val == self:
                        setattr(item, "StringToLongMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StringToLongMap"):
                    opp_val = getattr(item, "StringToLongMap", None)
                    
                    setattr(item, "StringToLongMap", self)
                    

    @property
    def analysis_trace_TraceSizeReport121(self):
        return self.__analysis_trace_TraceSizeReport121

    @analysis_trace_TraceSizeReport121.setter
    def analysis_trace_TraceSizeReport121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_trace_TraceSizeReport__analysis_trace_TraceSizeReport121", None)
        self.__analysis_trace_TraceSizeReport121 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActionToLongMap122"):
                    opp_val = getattr(item, "ActionToLongMap122", None)
                    
                    if opp_val == self:
                        setattr(item, "ActionToLongMap122", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActionToLongMap122"):
                    opp_val = getattr(item, "ActionToLongMap122", None)
                    
                    setattr(item, "ActionToLongMap122", self)
                    

    @property
    def analysis_trace_TraceSizeReport124(self):
        return self.__analysis_trace_TraceSizeReport124

    @analysis_trace_TraceSizeReport124.setter
    def analysis_trace_TraceSizeReport124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_trace_TraceSizeReport__analysis_trace_TraceSizeReport124", None)
        self.__analysis_trace_TraceSizeReport124 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActorToLongMap"):
                    opp_val = getattr(item, "ActorToLongMap", None)
                    
                    if opp_val == self:
                        setattr(item, "ActorToLongMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActorToLongMap"):
                    opp_val = getattr(item, "ActorToLongMap", None)
                    
                    setattr(item, "ActorToLongMap", self)
                    

    @property
    def analysis_trace_TraceSizeReport126(self):
        return self.__analysis_trace_TraceSizeReport126

    @analysis_trace_TraceSizeReport126.setter
    def analysis_trace_TraceSizeReport126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_trace_TraceSizeReport__analysis_trace_TraceSizeReport126", None)
        self.__analysis_trace_TraceSizeReport126 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActorToLongMap127"):
                    opp_val = getattr(item, "ActorToLongMap127", None)
                    
                    if opp_val == self:
                        setattr(item, "ActorToLongMap127", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActorToLongMap127"):
                    opp_val = getattr(item, "ActorToLongMap127", None)
                    
                    setattr(item, "ActorToLongMap127", self)
                    

    @property
    def analysis_trace_TraceSizeReport129(self):
        return self.__analysis_trace_TraceSizeReport129

    @analysis_trace_TraceSizeReport129.setter
    def analysis_trace_TraceSizeReport129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_trace_TraceSizeReport__analysis_trace_TraceSizeReport129", None)
        self.__analysis_trace_TraceSizeReport129 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActorToLongMap130"):
                    opp_val = getattr(item, "ActorToLongMap130", None)
                    
                    if opp_val == self:
                        setattr(item, "ActorToLongMap130", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActorToLongMap130"):
                    opp_val = getattr(item, "ActorToLongMap130", None)
                    
                    setattr(item, "ActorToLongMap130", self)
                    

    @property
    def analysis_trace_TraceSizeReport(self):
        return self.__analysis_trace_TraceSizeReport

    @analysis_trace_TraceSizeReport.setter
    def analysis_trace_TraceSizeReport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_trace_TraceSizeReport__analysis_trace_TraceSizeReport", None)
        self.__analysis_trace_TraceSizeReport = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActionToLongMap116"):
                    opp_val = getattr(item, "ActionToLongMap116", None)
                    
                    if opp_val == self:
                        setattr(item, "ActionToLongMap116", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActionToLongMap116"):
                    opp_val = getattr(item, "ActionToLongMap116", None)
                    
                    setattr(item, "ActionToLongMap116", self)
                    

class analysis_profiler_CodeProfilingReport(AnalysisReport):

    def __init__(self, analysis_profiler_CodeProfilingReport: "profiler_analysis_Network" = None, analysis_profiler_CodeProfilingReport2: set["ComplexCodeData"] = None, analysis_profiler_CodeProfilingReport4: "ComplexCodeData" = None):
        self.analysis_profiler_CodeProfilingReport = analysis_profiler_CodeProfilingReport
        self.analysis_profiler_CodeProfilingReport2 = analysis_profiler_CodeProfilingReport2 if analysis_profiler_CodeProfilingReport2 is not None else set()
        self.analysis_profiler_CodeProfilingReport4 = analysis_profiler_CodeProfilingReport4
        
    @property
    def analysis_profiler_CodeProfilingReport4(self):
        return self.__analysis_profiler_CodeProfilingReport4

    @analysis_profiler_CodeProfilingReport4.setter
    def analysis_profiler_CodeProfilingReport4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_profiler_CodeProfilingReport__analysis_profiler_CodeProfilingReport4", None)
        self.__analysis_profiler_CodeProfilingReport4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ComplexCodeData5"):
                opp_val = getattr(old_value, "ComplexCodeData5", None)
                if opp_val == self:
                    setattr(old_value, "ComplexCodeData5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ComplexCodeData5"):
                opp_val = getattr(value, "ComplexCodeData5", None)
                setattr(value, "ComplexCodeData5", self)

    @property
    def analysis_profiler_CodeProfilingReport(self):
        return self.__analysis_profiler_CodeProfilingReport

    @analysis_profiler_CodeProfilingReport.setter
    def analysis_profiler_CodeProfilingReport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_profiler_CodeProfilingReport__analysis_profiler_CodeProfilingReport", None)
        self.__analysis_profiler_CodeProfilingReport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profiler_analysis_Network"):
                opp_val = getattr(old_value, "profiler_analysis_Network", None)
                if opp_val == self:
                    setattr(old_value, "profiler_analysis_Network", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profiler_analysis_Network"):
                opp_val = getattr(value, "profiler_analysis_Network", None)
                setattr(value, "profiler_analysis_Network", self)

    @property
    def analysis_profiler_CodeProfilingReport2(self):
        return self.__analysis_profiler_CodeProfilingReport2

    @analysis_profiler_CodeProfilingReport2.setter
    def analysis_profiler_CodeProfilingReport2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_profiler_CodeProfilingReport__analysis_profiler_CodeProfilingReport2", None)
        self.__analysis_profiler_CodeProfilingReport2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ComplexCodeData"):
                    opp_val = getattr(item, "ComplexCodeData", None)
                    
                    if opp_val == self:
                        setattr(item, "ComplexCodeData", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ComplexCodeData"):
                    opp_val = getattr(item, "ComplexCodeData", None)
                    
                    setattr(item, "ComplexCodeData", self)
                    

    def getActorClassData(self, actorClass: str) -> str:
        # TODO: Implement getActorClassData method
        pass

class analysis_AnalysisReport(ABC):

    def __init__(self, algorithm: str, date: date):
        self.algorithm = algorithm
        self.date = date
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def algorithm(self) -> str:
        return self.__algorithm

    @algorithm.setter
    def algorithm(self, algorithm: str):
        self.__algorithm = algorithm

class analysis_profiler_CodeData:

    def __init__(self, blockName: str, nol: str, analysis_profiler_CodeData: set["StringToIntegerMap"] = None, analysis_profiler_CodeData8: set["StringToIntegerMap"] = None):
        self.blockName = blockName
        self.nol = nol
        self.analysis_profiler_CodeData = analysis_profiler_CodeData if analysis_profiler_CodeData is not None else set()
        self.analysis_profiler_CodeData8 = analysis_profiler_CodeData8 if analysis_profiler_CodeData8 is not None else set()
        
    @property
    def blockName(self) -> str:
        return self.__blockName

    @blockName.setter
    def blockName(self, blockName: str):
        self.__blockName = blockName

    @property
    def nol(self) -> str:
        return self.__nol

    @nol.setter
    def nol(self, nol: str):
        self.__nol = nol

    @property
    def analysis_profiler_CodeData8(self):
        return self.__analysis_profiler_CodeData8

    @analysis_profiler_CodeData8.setter
    def analysis_profiler_CodeData8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_profiler_CodeData__analysis_profiler_CodeData8", None)
        self.__analysis_profiler_CodeData8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StringToIntegerMap9"):
                    opp_val = getattr(item, "StringToIntegerMap9", None)
                    
                    if opp_val == self:
                        setattr(item, "StringToIntegerMap9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StringToIntegerMap9"):
                    opp_val = getattr(item, "StringToIntegerMap9", None)
                    
                    setattr(item, "StringToIntegerMap9", self)
                    

    @property
    def analysis_profiler_CodeData(self):
        return self.__analysis_profiler_CodeData

    @analysis_profiler_CodeData.setter
    def analysis_profiler_CodeData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_profiler_CodeData__analysis_profiler_CodeData", None)
        self.__analysis_profiler_CodeData = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StringToIntegerMap"):
                    opp_val = getattr(item, "StringToIntegerMap", None)
                    
                    if opp_val == self:
                        setattr(item, "StringToIntegerMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StringToIntegerMap"):
                    opp_val = getattr(item, "StringToIntegerMap", None)
                    
                    setattr(item, "StringToIntegerMap", self)
                    
