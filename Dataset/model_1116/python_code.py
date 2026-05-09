from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

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
class Optimizer(Enum):
    RLE = "RLE"
    KTAIL = "KTAIL"
class FSMOp(Enum):
    ADD = "ADD"
    SET = "SET"


############################################
# Definition of Classes
############################################

class PartitionToActorSelectionScheduleMap:

    pass
class analysis_scheduling_MarkovSchedulingState:

    def __init__(self, firings: str, name: str, target455: set["MarkovSchedulingTransition"] = None, analysis_scheduling_MarkovSchedulingState: "scheduling_analysis_Actor" = None, source452: set["MarkovSchedulingTransition"] = None):
        self.firings = firings
        self.name = name
        self.target455 = target455 if target455 is not None else set()
        self.analysis_scheduling_MarkovSchedulingState = analysis_scheduling_MarkovSchedulingState
        self.source452 = source452 if source452 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def firings(self):
        return self.__firings

    @firings.setter
    def firings(self, firings: str):
        self.__firings = firings


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
            if hasattr(old_value, "scheduling_analysis_Actor450"):
                opp_val = getattr(old_value, "scheduling_analysis_Actor450", None)
                if opp_val == self:
                    setattr(old_value, "scheduling_analysis_Actor450", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scheduling_analysis_Actor450"):
                opp_val = getattr(value, "scheduling_analysis_Actor450", None)
                setattr(value, "scheduling_analysis_Actor450", self)

    @property
    def target455(self):
        return self.__target455

    @target455.setter
    def target455(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_scheduling_MarkovSchedulingState__target455", None)
        self.__target455 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MarkovSchedulingTransition456"):
                    opp_val = getattr(item, "MarkovSchedulingTransition456", None)
                    
                    if opp_val == self:
                        setattr(item, "MarkovSchedulingTransition456", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MarkovSchedulingTransition456"):
                    opp_val = getattr(item, "MarkovSchedulingTransition456", None)
                    
                    setattr(item, "MarkovSchedulingTransition456", self)
                    

    @property
    def source452(self):
        return self.__source452

    @source452.setter
    def source452(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_scheduling_MarkovSchedulingState__source452", None)
        self.__source452 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MarkovSchedulingTransition453"):
                    opp_val = getattr(item, "MarkovSchedulingTransition453", None)
                    
                    if opp_val == self:
                        setattr(item, "MarkovSchedulingTransition453", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MarkovSchedulingTransition453"):
                    opp_val = getattr(item, "MarkovSchedulingTransition453", None)
                    
                    setattr(item, "MarkovSchedulingTransition453", self)
                    

class MarkovSchedulingTransition:

    pass
class MarkovSchedulingState:

    pass
class scheduling_analysis_Actor:

    pass
class analysis_scheduling_MarkovPartitionScheduler:

    def __init__(self, partitionId: str, analysis_scheduling_MarkovPartitionScheduler: set["scheduling_analysis_Actor"] = None, analysis_scheduling_MarkovPartitionScheduler446: set["MarkovSchedulingState"] = None, analysis_scheduling_MarkovPartitionScheduler448: set["MarkovSchedulingTransition"] = None):
        self.partitionId = partitionId
        self.analysis_scheduling_MarkovPartitionScheduler = analysis_scheduling_MarkovPartitionScheduler if analysis_scheduling_MarkovPartitionScheduler is not None else set()
        self.analysis_scheduling_MarkovPartitionScheduler446 = analysis_scheduling_MarkovPartitionScheduler446 if analysis_scheduling_MarkovPartitionScheduler446 is not None else set()
        self.analysis_scheduling_MarkovPartitionScheduler448 = analysis_scheduling_MarkovPartitionScheduler448 if analysis_scheduling_MarkovPartitionScheduler448 is not None else set()
        
        pass
    @property
    def partitionId(self):
        return self.__partitionId

    @partitionId.setter
    def partitionId(self, partitionId: str):
        self.__partitionId = partitionId


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
                    

    @property
    def analysis_scheduling_MarkovPartitionScheduler446(self):
        return self.__analysis_scheduling_MarkovPartitionScheduler446

    @analysis_scheduling_MarkovPartitionScheduler446.setter
    def analysis_scheduling_MarkovPartitionScheduler446(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_scheduling_MarkovPartitionScheduler__analysis_scheduling_MarkovPartitionScheduler446", None)
        self.__analysis_scheduling_MarkovPartitionScheduler446 = value if value is not None else set()
        
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
    def analysis_scheduling_MarkovPartitionScheduler448(self):
        return self.__analysis_scheduling_MarkovPartitionScheduler448

    @analysis_scheduling_MarkovPartitionScheduler448.setter
    def analysis_scheduling_MarkovPartitionScheduler448(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_scheduling_MarkovPartitionScheduler__analysis_scheduling_MarkovPartitionScheduler448", None)
        self.__analysis_scheduling_MarkovPartitionScheduler448 = value if value is not None else set()
        
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
                    

    def getAssociatedState(self, analysis_actor) :
        # TODO: Implement getAssociatedState method
        pass

class scheduling_analysis_Network:

    pass
class MarkovPartitionScheduler:

    pass
class FSMCombination:

    pass
class analysis_scheduling_FSMCondition:

    def __init__(self, comp: str, compval: str, valName: str, analysis_scheduling_FSMCondition: "FSMCombination" = None):
        self.comp = comp
        self.compval = compval
        self.valName = valName
        self.analysis_scheduling_FSMCondition = analysis_scheduling_FSMCondition
        
        pass
    @property
    def valName(self):
        return self.__valName

    @valName.setter
    def valName(self, valName: str):
        self.__valName = valName


    @property
    def compval(self):
        return self.__compval

    @compval.setter
    def compval(self, compval: str):
        self.__compval = compval


    @property
    def comp(self):
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
        
        pass
    @property
    def combinator(self):
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
            if hasattr(old_value, "FSMCondition437"):
                opp_val = getattr(old_value, "FSMCondition437", None)
                if opp_val == self:
                    setattr(old_value, "FSMCondition437", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMCondition437"):
                opp_val = getattr(value, "FSMCondition437", None)
                setattr(value, "FSMCondition437", self)

class FSMVar:

    pass
class analysis_scheduling_FSMOperation:

    def __init__(self, op: str, val: str, var: str):
        self.op = op
        self.val = val
        self.var = var
        
        pass
    @property
    def var(self):
        return self.__var

    @var.setter
    def var(self, var: str):
        self.__var = var


    @property
    def val(self):
        return self.__val

    @val.setter
    def val(self, val: str):
        self.__val = val


    @property
    def op(self):
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op


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

    def __init__(self, enumName: str, analysis_scheduling_FSMState: set["FSMVarUpdate"] = None, analysis_scheduling_FSMState431: set["FSMTransition"] = None):
        self.enumName = enumName
        self.analysis_scheduling_FSMState = analysis_scheduling_FSMState if analysis_scheduling_FSMState is not None else set()
        self.analysis_scheduling_FSMState431 = analysis_scheduling_FSMState431 if analysis_scheduling_FSMState431 is not None else set()
        
        pass
    @property
    def enumName(self):
        return self.__enumName

    @enumName.setter
    def enumName(self, enumName: str):
        self.__enumName = enumName


    @property
    def analysis_scheduling_FSMState431(self):
        return self.__analysis_scheduling_FSMState431

    @analysis_scheduling_FSMState431.setter
    def analysis_scheduling_FSMState431(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_scheduling_FSMState__analysis_scheduling_FSMState431", None)
        self.__analysis_scheduling_FSMState431 = value if value is not None else set()
        
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

    def __init__(self, targetStateEnumName: str, sourceStateEnumName: str, analysis_scheduling_FSMTransition: "FSMCondition" = None, analysis_scheduling_FSMTransition428: "Sequence" = None):
        self.targetStateEnumName = targetStateEnumName
        self.sourceStateEnumName = sourceStateEnumName
        self.analysis_scheduling_FSMTransition = analysis_scheduling_FSMTransition
        self.analysis_scheduling_FSMTransition428 = analysis_scheduling_FSMTransition428
        
        pass
    @property
    def targetStateEnumName(self):
        return self.__targetStateEnumName

    @targetStateEnumName.setter
    def targetStateEnumName(self, targetStateEnumName: str):
        self.__targetStateEnumName = targetStateEnumName


    @property
    def sourceStateEnumName(self):
        return self.__sourceStateEnumName

    @sourceStateEnumName.setter
    def sourceStateEnumName(self, sourceStateEnumName: str):
        self.__sourceStateEnumName = sourceStateEnumName


    @property
    def analysis_scheduling_FSMTransition428(self):
        return self.__analysis_scheduling_FSMTransition428

    @analysis_scheduling_FSMTransition428.setter
    def analysis_scheduling_FSMTransition428(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_scheduling_FSMTransition__analysis_scheduling_FSMTransition428", None)
        self.__analysis_scheduling_FSMTransition428 = value
        
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

class analysis_scheduling_FSMVar:

    def __init__(self, name: str, initialVal: str, type: str):
        self.name = name
        self.initialVal = initialVal
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def initialVal(self):
        return self.__initialVal

    @initialVal.setter
    def initialVal(self, initialVal: str):
        self.__initialVal = initialVal


class ActorFire:

    pass
class analysis_scheduling_PartitionedActorFire(ActorFire):

    pass
class analysis_scheduling_ActorSelectionSchedule(ABC):

    pass
class profiling_analysis_Actor:

    pass
class analysis_profiling_IntraActorCommunicationData:

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
        
        pass
    @property
    def schedulerWeight(self):
        return self.__schedulerWeight

    @schedulerWeight.setter
    def schedulerWeight(self, schedulerWeight: float):
        self.__schedulerWeight = schedulerWeight


    @property
    def actorName(self):
        return self.__actorName

    @actorName.setter
    def actorName(self, actorName: str):
        self.__actorName = actorName


    @property
    def actionsWeightPercent(self):
        return self.__actionsWeightPercent

    @actionsWeightPercent.setter
    def actionsWeightPercent(self, actionsWeightPercent: float):
        self.__actionsWeightPercent = actionsWeightPercent


    @property
    def actionsWeight(self):
        return self.__actionsWeight

    @actionsWeight.setter
    def actionsWeight(self, actionsWeight: float):
        self.__actionsWeight = actionsWeight


    @property
    def schedulerWeightPercent(self):
        return self.__schedulerWeightPercent

    @schedulerWeightPercent.setter
    def schedulerWeightPercent(self, schedulerWeightPercent: float):
        self.__schedulerWeightPercent = schedulerWeightPercent


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
class pipelining_analysis_ActorClass:

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
        
        pass
    @property
    def schedulingPolicy(self):
        return self.__schedulingPolicy

    @schedulingPolicy.setter
    def schedulingPolicy(self, schedulingPolicy: str):
        self.__schedulingPolicy = schedulingPolicy


    @property
    def actors(self):
        return self.__actors

    @actors.setter
    def actors(self, actors: str):
        self.__actors = actors


    @property
    def occupancy(self):
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
class analysis_postprocessing_BufferBlockingReport(PostProcessingData):

    pass
class analysis_postprocessing_ActionStatisticsReport(PostProcessingData):

    pass
class analysis_postprocessing_SchedulerChecksReport(PostProcessingData):

    pass
class analysis_postprocessing_ActorStatisticsReport(PostProcessingData):

    def __init__(self, executionTime: float, averageOccupancy: float, occupancyDeviation: float, analysis_postprocessing_ActorStatisticsReport: "postprocessing_analysis_Network" = None, analysis_postprocessing_ActorStatisticsReport330: set["StatisticalActorPartition"] = None, analysis_postprocessing_ActorStatisticsReport332: set["StringToDoubleMap"] = None, analysis_postprocessing_ActorStatisticsReport335: set["StringToDoubleMap"] = None, analysis_postprocessing_ActorStatisticsReport338: set["StringToDoubleMap"] = None, analysis_postprocessing_ActorStatisticsReport341: set["StringToDoubleMap"] = None, PostProcessingData: "analysis_postprocessing_PostProcessingReport" = None):
        self.executionTime = executionTime
        self.averageOccupancy = averageOccupancy
        self.occupancyDeviation = occupancyDeviation
        self.analysis_postprocessing_ActorStatisticsReport = analysis_postprocessing_ActorStatisticsReport
        self.analysis_postprocessing_ActorStatisticsReport330 = analysis_postprocessing_ActorStatisticsReport330 if analysis_postprocessing_ActorStatisticsReport330 is not None else set()
        self.analysis_postprocessing_ActorStatisticsReport332 = analysis_postprocessing_ActorStatisticsReport332 if analysis_postprocessing_ActorStatisticsReport332 is not None else set()
        self.analysis_postprocessing_ActorStatisticsReport335 = analysis_postprocessing_ActorStatisticsReport335 if analysis_postprocessing_ActorStatisticsReport335 is not None else set()
        self.analysis_postprocessing_ActorStatisticsReport338 = analysis_postprocessing_ActorStatisticsReport338 if analysis_postprocessing_ActorStatisticsReport338 is not None else set()
        self.analysis_postprocessing_ActorStatisticsReport341 = analysis_postprocessing_ActorStatisticsReport341 if analysis_postprocessing_ActorStatisticsReport341 is not None else set()
        
        pass
    @property
    def averageOccupancy(self):
        return self.__averageOccupancy

    @averageOccupancy.setter
    def averageOccupancy(self, averageOccupancy: float):
        self.__averageOccupancy = averageOccupancy


    @property
    def occupancyDeviation(self):
        return self.__occupancyDeviation

    @occupancyDeviation.setter
    def occupancyDeviation(self, occupancyDeviation: float):
        self.__occupancyDeviation = occupancyDeviation


    @property
    def executionTime(self):
        return self.__executionTime

    @executionTime.setter
    def executionTime(self, executionTime: float):
        self.__executionTime = executionTime


    @property
    def analysis_postprocessing_ActorStatisticsReport330(self):
        return self.__analysis_postprocessing_ActorStatisticsReport330

    @analysis_postprocessing_ActorStatisticsReport330.setter
    def analysis_postprocessing_ActorStatisticsReport330(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_postprocessing_ActorStatisticsReport__analysis_postprocessing_ActorStatisticsReport330", None)
        self.__analysis_postprocessing_ActorStatisticsReport330 = value if value is not None else set()
        
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
            if hasattr(old_value, "postprocessing_analysis_Network328"):
                opp_val = getattr(old_value, "postprocessing_analysis_Network328", None)
                if opp_val == self:
                    setattr(old_value, "postprocessing_analysis_Network328", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "postprocessing_analysis_Network328"):
                opp_val = getattr(value, "postprocessing_analysis_Network328", None)
                setattr(value, "postprocessing_analysis_Network328", self)

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
    def analysis_postprocessing_ActorStatisticsReport332(self):
        return self.__analysis_postprocessing_ActorStatisticsReport332

    @analysis_postprocessing_ActorStatisticsReport332.setter
    def analysis_postprocessing_ActorStatisticsReport332(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_postprocessing_ActorStatisticsReport__analysis_postprocessing_ActorStatisticsReport332", None)
        self.__analysis_postprocessing_ActorStatisticsReport332 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StringToDoubleMap333"):
                    opp_val = getattr(item, "StringToDoubleMap333", None)
                    
                    if opp_val == self:
                        setattr(item, "StringToDoubleMap333", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StringToDoubleMap333"):
                    opp_val = getattr(item, "StringToDoubleMap333", None)
                    
                    setattr(item, "StringToDoubleMap333", self)
                    

class postprocessing_analysis_Network:

    pass
class analysis_pipelining_ImpactAnalysisData:

    def __init__(self, cpReduction: float, analysis_pipelining_ImpactAnalysisData: "BottlenecksReport" = None, analysis_pipelining_ImpactAnalysisData320: set["pipelining_analysis_Action"] = None, analysis_pipelining_ImpactAnalysisData323: "pipelining_analysis_ActorClass" = None):
        self.cpReduction = cpReduction
        self.analysis_pipelining_ImpactAnalysisData = analysis_pipelining_ImpactAnalysisData
        self.analysis_pipelining_ImpactAnalysisData320 = analysis_pipelining_ImpactAnalysisData320 if analysis_pipelining_ImpactAnalysisData320 is not None else set()
        self.analysis_pipelining_ImpactAnalysisData323 = analysis_pipelining_ImpactAnalysisData323
        
        pass
    @property
    def cpReduction(self):
        return self.__cpReduction

    @cpReduction.setter
    def cpReduction(self, cpReduction: float):
        self.__cpReduction = cpReduction


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
            if hasattr(old_value, "BottlenecksReport318"):
                opp_val = getattr(old_value, "BottlenecksReport318", None)
                if opp_val == self:
                    setattr(old_value, "BottlenecksReport318", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BottlenecksReport318"):
                opp_val = getattr(value, "BottlenecksReport318", None)
                setattr(value, "BottlenecksReport318", self)

    @property
    def analysis_pipelining_ImpactAnalysisData323(self):
        return self.__analysis_pipelining_ImpactAnalysisData323

    @analysis_pipelining_ImpactAnalysisData323.setter
    def analysis_pipelining_ImpactAnalysisData323(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_pipelining_ImpactAnalysisData__analysis_pipelining_ImpactAnalysisData323", None)
        self.__analysis_pipelining_ImpactAnalysisData323 = value
        
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
    def analysis_pipelining_ImpactAnalysisData320(self):
        return self.__analysis_pipelining_ImpactAnalysisData320

    @analysis_pipelining_ImpactAnalysisData320.setter
    def analysis_pipelining_ImpactAnalysisData320(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_pipelining_ImpactAnalysisData__analysis_pipelining_ImpactAnalysisData320", None)
        self.__analysis_pipelining_ImpactAnalysisData320 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pipelining_analysis_Action321"):
                    opp_val = getattr(item, "pipelining_analysis_Action321", None)
                    
                    if opp_val == self:
                        setattr(item, "pipelining_analysis_Action321", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pipelining_analysis_Action321"):
                    opp_val = getattr(item, "pipelining_analysis_Action321", None)
                    
                    setattr(item, "pipelining_analysis_Action321", self)
                    

class ActionsVariablePipeliningReport:

    pass
class pipelining_analysis_StatisticalData:

    pass
class pipelining_analysis_Action:

    pass
class analysis_pipelining_ActionVariablePipeliningData:

    def __init__(self, pipelinable: bool, analysis_pipelining_ActionVariablePipeliningData: "pipelining_analysis_Action" = None, analysis_pipelining_ActionVariablePipeliningData303: "pipelining_analysis_StatisticalData" = None, analysis_pipelining_ActionVariablePipeliningData305: "pipelining_analysis_StatisticalData" = None):
        self.pipelinable = pipelinable
        self.analysis_pipelining_ActionVariablePipeliningData = analysis_pipelining_ActionVariablePipeliningData
        self.analysis_pipelining_ActionVariablePipeliningData303 = analysis_pipelining_ActionVariablePipeliningData303
        self.analysis_pipelining_ActionVariablePipeliningData305 = analysis_pipelining_ActionVariablePipeliningData305
        
        pass
    @property
    def pipelinable(self):
        return self.__pipelinable

    @pipelinable.setter
    def pipelinable(self, pipelinable: bool):
        self.__pipelinable = pipelinable


    @property
    def analysis_pipelining_ActionVariablePipeliningData305(self):
        return self.__analysis_pipelining_ActionVariablePipeliningData305

    @analysis_pipelining_ActionVariablePipeliningData305.setter
    def analysis_pipelining_ActionVariablePipeliningData305(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_pipelining_ActionVariablePipeliningData__analysis_pipelining_ActionVariablePipeliningData305", None)
        self.__analysis_pipelining_ActionVariablePipeliningData305 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pipelining_analysis_StatisticalData306"):
                opp_val = getattr(old_value, "pipelining_analysis_StatisticalData306", None)
                if opp_val == self:
                    setattr(old_value, "pipelining_analysis_StatisticalData306", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pipelining_analysis_StatisticalData306"):
                opp_val = getattr(value, "pipelining_analysis_StatisticalData306", None)
                setattr(value, "pipelining_analysis_StatisticalData306", self)

    @property
    def analysis_pipelining_ActionVariablePipeliningData303(self):
        return self.__analysis_pipelining_ActionVariablePipeliningData303

    @analysis_pipelining_ActionVariablePipeliningData303.setter
    def analysis_pipelining_ActionVariablePipeliningData303(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_pipelining_ActionVariablePipeliningData__analysis_pipelining_ActionVariablePipeliningData303", None)
        self.__analysis_pipelining_ActionVariablePipeliningData303 = value
        
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
class partitioning_analysis_Actor:

    pass
class analysis_partitioning_ComCostPartition:

    def __init__(self, internalCost: str, externalCost: str, analysis_partitioning_ComCostPartition281: set["ActorToLongMap"] = None, analysis_partitioning_ComCostPartition284: set["ActorToLongMap"] = None, analysis_partitioning_ComCostPartition: set["partitioning_analysis_Actor"] = None):
        self.internalCost = internalCost
        self.externalCost = externalCost
        self.analysis_partitioning_ComCostPartition281 = analysis_partitioning_ComCostPartition281 if analysis_partitioning_ComCostPartition281 is not None else set()
        self.analysis_partitioning_ComCostPartition284 = analysis_partitioning_ComCostPartition284 if analysis_partitioning_ComCostPartition284 is not None else set()
        self.analysis_partitioning_ComCostPartition = analysis_partitioning_ComCostPartition if analysis_partitioning_ComCostPartition is not None else set()
        
        pass
    @property
    def externalCost(self):
        return self.__externalCost

    @externalCost.setter
    def externalCost(self, externalCost: str):
        self.__externalCost = externalCost


    @property
    def internalCost(self):
        return self.__internalCost

    @internalCost.setter
    def internalCost(self, internalCost: str):
        self.__internalCost = internalCost


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
                    

    @property
    def analysis_partitioning_ComCostPartition281(self):
        return self.__analysis_partitioning_ComCostPartition281

    @analysis_partitioning_ComCostPartition281.setter
    def analysis_partitioning_ComCostPartition281(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_partitioning_ComCostPartition__analysis_partitioning_ComCostPartition281", None)
        self.__analysis_partitioning_ComCostPartition281 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActorToLongMap282"):
                    opp_val = getattr(item, "ActorToLongMap282", None)
                    
                    if opp_val == self:
                        setattr(item, "ActorToLongMap282", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActorToLongMap282"):
                    opp_val = getattr(item, "ActorToLongMap282", None)
                    
                    setattr(item, "ActorToLongMap282", self)
                    

class analysis_partitioning_BalancedPipelinePartition:

    def __init__(self, workload: float, preWorkload: float, commonPredAvg: float, analysis_partitioning_BalancedPipelinePartition: set["partitioning_analysis_Actor"] = None):
        self.workload = workload
        self.preWorkload = preWorkload
        self.commonPredAvg = commonPredAvg
        self.analysis_partitioning_BalancedPipelinePartition = analysis_partitioning_BalancedPipelinePartition if analysis_partitioning_BalancedPipelinePartition is not None else set()
        
        pass
    @property
    def preWorkload(self):
        return self.__preWorkload

    @preWorkload.setter
    def preWorkload(self, preWorkload: float):
        self.__preWorkload = preWorkload


    @property
    def commonPredAvg(self):
        return self.__commonPredAvg

    @commonPredAvg.setter
    def commonPredAvg(self, commonPredAvg: float):
        self.__commonPredAvg = commonPredAvg


    @property
    def workload(self):
        return self.__workload

    @workload.setter
    def workload(self, workload: float):
        self.__workload = workload


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
                if hasattr(item, "partitioning_analysis_Actor293"):
                    opp_val = getattr(item, "partitioning_analysis_Actor293", None)
                    
                    if opp_val == self:
                        setattr(item, "partitioning_analysis_Actor293", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "partitioning_analysis_Actor293"):
                    opp_val = getattr(item, "partitioning_analysis_Actor293", None)
                    
                    setattr(item, "partitioning_analysis_Actor293", self)
                    

class WorkloadBalancePartition:

    pass
class analysis_partitioning_WorkloadBalancePartition:

    def __init__(self, workload: float, analysis_partitioning_WorkloadBalancePartition: set["partitioning_analysis_Actor"] = None):
        self.workload = workload
        self.analysis_partitioning_WorkloadBalancePartition = analysis_partitioning_WorkloadBalancePartition if analysis_partitioning_WorkloadBalancePartition is not None else set()
        
        pass
    @property
    def workload(self):
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
                if hasattr(item, "partitioning_analysis_Actor287"):
                    opp_val = getattr(item, "partitioning_analysis_Actor287", None)
                    
                    if opp_val == self:
                        setattr(item, "partitioning_analysis_Actor287", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "partitioning_analysis_Actor287"):
                    opp_val = getattr(item, "partitioning_analysis_Actor287", None)
                    
                    setattr(item, "partitioning_analysis_Actor287", self)
                    

class ScheduledImpactAnalysisData:

    pass
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
class buffers_analysis_Buffer:

    pass
class analysis_buffers_BoundedBufferData:

    def __init__(self, tokenSize: int, bitSize: int, analysis_buffers_BoundedBufferData: "buffers_analysis_Buffer" = None):
        self.tokenSize = tokenSize
        self.bitSize = bitSize
        self.analysis_buffers_BoundedBufferData = analysis_buffers_BoundedBufferData
        
        pass
    @property
    def bitSize(self):
        return self.__bitSize

    @bitSize.setter
    def bitSize(self, bitSize: int):
        self.__bitSize = bitSize


    @property
    def tokenSize(self):
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

class BoundedBufferData:

    pass
class buffers_analysis_Network:

    pass
class BottlenecksWithSchedulingReport:

    pass
class analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap:

    def __init__(self, key: str, analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap: "BottlenecksWithSchedulingReport" = None):
        self.key = key
        self.analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap = analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap
        
        pass
    @property
    def key(self):
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
class analysis_bottlenecks_ScheduledImpactAnalysisData:

    pass
class BufferToDoubleMap:

    pass
class BufferToIntegerMap:

    pass
class analysis_bottlenecks_ActionBottlenecksWithSchedulingData:

    def __init__(self, cpWeight: float, totalWeight: float, cpFirings: str, totalFirings: str, analysis_bottlenecks_ActionBottlenecksWithSchedulingData: "bottlenecks_analysis_Action" = None, analysis_bottlenecks_ActionBottlenecksWithSchedulingData231: set["BufferToIntegerMap"] = None, analysis_bottlenecks_ActionBottlenecksWithSchedulingData233: set["BufferToDoubleMap"] = None, analysis_bottlenecks_ActionBottlenecksWithSchedulingData235: set["BufferToIntegerMap"] = None):
        self.cpWeight = cpWeight
        self.totalWeight = totalWeight
        self.cpFirings = cpFirings
        self.totalFirings = totalFirings
        self.analysis_bottlenecks_ActionBottlenecksWithSchedulingData = analysis_bottlenecks_ActionBottlenecksWithSchedulingData
        self.analysis_bottlenecks_ActionBottlenecksWithSchedulingData231 = analysis_bottlenecks_ActionBottlenecksWithSchedulingData231 if analysis_bottlenecks_ActionBottlenecksWithSchedulingData231 is not None else set()
        self.analysis_bottlenecks_ActionBottlenecksWithSchedulingData233 = analysis_bottlenecks_ActionBottlenecksWithSchedulingData233 if analysis_bottlenecks_ActionBottlenecksWithSchedulingData233 is not None else set()
        self.analysis_bottlenecks_ActionBottlenecksWithSchedulingData235 = analysis_bottlenecks_ActionBottlenecksWithSchedulingData235 if analysis_bottlenecks_ActionBottlenecksWithSchedulingData235 is not None else set()
        
        pass
    @property
    def cpWeight(self):
        return self.__cpWeight

    @cpWeight.setter
    def cpWeight(self, cpWeight: float):
        self.__cpWeight = cpWeight


    @property
    def totalFirings(self):
        return self.__totalFirings

    @totalFirings.setter
    def totalFirings(self, totalFirings: str):
        self.__totalFirings = totalFirings


    @property
    def cpFirings(self):
        return self.__cpFirings

    @cpFirings.setter
    def cpFirings(self, cpFirings: str):
        self.__cpFirings = cpFirings


    @property
    def totalWeight(self):
        return self.__totalWeight

    @totalWeight.setter
    def totalWeight(self, totalWeight: float):
        self.__totalWeight = totalWeight


    @property
    def analysis_bottlenecks_ActionBottlenecksWithSchedulingData235(self):
        return self.__analysis_bottlenecks_ActionBottlenecksWithSchedulingData235

    @analysis_bottlenecks_ActionBottlenecksWithSchedulingData235.setter
    def analysis_bottlenecks_ActionBottlenecksWithSchedulingData235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_bottlenecks_ActionBottlenecksWithSchedulingData__analysis_bottlenecks_ActionBottlenecksWithSchedulingData235", None)
        self.__analysis_bottlenecks_ActionBottlenecksWithSchedulingData235 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BufferToIntegerMap236"):
                    opp_val = getattr(item, "BufferToIntegerMap236", None)
                    
                    if opp_val == self:
                        setattr(item, "BufferToIntegerMap236", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BufferToIntegerMap236"):
                    opp_val = getattr(item, "BufferToIntegerMap236", None)
                    
                    setattr(item, "BufferToIntegerMap236", self)
                    

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
            if hasattr(old_value, "bottlenecks_analysis_Action229"):
                opp_val = getattr(old_value, "bottlenecks_analysis_Action229", None)
                if opp_val == self:
                    setattr(old_value, "bottlenecks_analysis_Action229", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bottlenecks_analysis_Action229"):
                opp_val = getattr(value, "bottlenecks_analysis_Action229", None)
                setattr(value, "bottlenecks_analysis_Action229", self)

    @property
    def analysis_bottlenecks_ActionBottlenecksWithSchedulingData231(self):
        return self.__analysis_bottlenecks_ActionBottlenecksWithSchedulingData231

    @analysis_bottlenecks_ActionBottlenecksWithSchedulingData231.setter
    def analysis_bottlenecks_ActionBottlenecksWithSchedulingData231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_bottlenecks_ActionBottlenecksWithSchedulingData__analysis_bottlenecks_ActionBottlenecksWithSchedulingData231", None)
        self.__analysis_bottlenecks_ActionBottlenecksWithSchedulingData231 = value if value is not None else set()
        
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
                    

    @property
    def analysis_bottlenecks_ActionBottlenecksWithSchedulingData233(self):
        return self.__analysis_bottlenecks_ActionBottlenecksWithSchedulingData233

    @analysis_bottlenecks_ActionBottlenecksWithSchedulingData233.setter
    def analysis_bottlenecks_ActionBottlenecksWithSchedulingData233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_bottlenecks_ActionBottlenecksWithSchedulingData__analysis_bottlenecks_ActionBottlenecksWithSchedulingData233", None)
        self.__analysis_bottlenecks_ActionBottlenecksWithSchedulingData233 = value if value is not None else set()
        
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
                    

class StringToDoubleMap:

    pass
class ActionBottlenecksWithSchedulingData:

    pass
class postprocessing_PostProcessingData:

    pass
class analysis_bottlenecks_DoubleToBottlenecksReportMap:

    def __init__(self, key: str, analysis_bottlenecks_DoubleToBottlenecksReportMap: "BottlenecksReport" = None):
        self.key = key
        self.analysis_bottlenecks_DoubleToBottlenecksReportMap = analysis_bottlenecks_DoubleToBottlenecksReportMap
        
        pass
    @property
    def key(self):
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
            if hasattr(old_value, "BottlenecksReport221"):
                opp_val = getattr(old_value, "BottlenecksReport221", None)
                if opp_val == self:
                    setattr(old_value, "BottlenecksReport221", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BottlenecksReport221"):
                opp_val = getattr(value, "BottlenecksReport221", None)
                setattr(value, "BottlenecksReport221", self)

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
class analysis_bottlenecks_ActionBottlenecksData:

    def __init__(self, slackMin: float, slackMax: float, cpWeight: float, cpVariance: float, totalWeight: float, totalVariance: float, cpFirings: str, totalFirings: str, analysis_bottlenecks_ActionBottlenecksData: "bottlenecks_analysis_Action" = None):
        self.slackMin = slackMin
        self.slackMax = slackMax
        self.cpWeight = cpWeight
        self.cpVariance = cpVariance
        self.totalWeight = totalWeight
        self.totalVariance = totalVariance
        self.cpFirings = cpFirings
        self.totalFirings = totalFirings
        self.analysis_bottlenecks_ActionBottlenecksData = analysis_bottlenecks_ActionBottlenecksData
        
        pass
    @property
    def cpWeight(self):
        return self.__cpWeight

    @cpWeight.setter
    def cpWeight(self, cpWeight: float):
        self.__cpWeight = cpWeight


    @property
    def slackMax(self):
        return self.__slackMax

    @slackMax.setter
    def slackMax(self, slackMax: float):
        self.__slackMax = slackMax


    @property
    def cpVariance(self):
        return self.__cpVariance

    @cpVariance.setter
    def cpVariance(self, cpVariance: float):
        self.__cpVariance = cpVariance


    @property
    def totalVariance(self):
        return self.__totalVariance

    @totalVariance.setter
    def totalVariance(self, totalVariance: float):
        self.__totalVariance = totalVariance


    @property
    def slackMin(self):
        return self.__slackMin

    @slackMin.setter
    def slackMin(self, slackMin: float):
        self.__slackMin = slackMin


    @property
    def totalFirings(self):
        return self.__totalFirings

    @totalFirings.setter
    def totalFirings(self, totalFirings: str):
        self.__totalFirings = totalFirings


    @property
    def totalWeight(self):
        return self.__totalWeight

    @totalWeight.setter
    def totalWeight(self, totalWeight: float):
        self.__totalWeight = totalWeight


    @property
    def cpFirings(self):
        return self.__cpFirings

    @cpFirings.setter
    def cpFirings(self, cpFirings: str):
        self.__cpFirings = cpFirings


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

    def __init__(self, first: bool, successors: str, analysis_trace_MarkovModelActionData: "trace_analysis_Action" = None, analysis_trace_MarkovModelActionData200: set["ActionToLongMap"] = None):
        self.first = first
        self.successors = successors
        self.analysis_trace_MarkovModelActionData = analysis_trace_MarkovModelActionData
        self.analysis_trace_MarkovModelActionData200 = analysis_trace_MarkovModelActionData200 if analysis_trace_MarkovModelActionData200 is not None else set()
        
        pass
    @property
    def first(self):
        return self.__first

    @first.setter
    def first(self, first: bool):
        self.__first = first


    @property
    def successors(self):
        return self.__successors

    @successors.setter
    def successors(self, successors: str):
        self.__successors = successors


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
            if hasattr(old_value, "trace_analysis_Action198"):
                opp_val = getattr(old_value, "trace_analysis_Action198", None)
                if opp_val == self:
                    setattr(old_value, "trace_analysis_Action198", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_analysis_Action198"):
                opp_val = getattr(value, "trace_analysis_Action198", None)
                setattr(value, "trace_analysis_Action198", self)

    @property
    def analysis_trace_MarkovModelActionData200(self):
        return self.__analysis_trace_MarkovModelActionData200

    @analysis_trace_MarkovModelActionData200.setter
    def analysis_trace_MarkovModelActionData200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_trace_MarkovModelActionData__analysis_trace_MarkovModelActionData200", None)
        self.__analysis_trace_MarkovModelActionData200 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActionToLongMap201"):
                    opp_val = getattr(item, "ActionToLongMap201", None)
                    
                    if opp_val == self:
                        setattr(item, "ActionToLongMap201", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActionToLongMap201"):
                    opp_val = getattr(item, "ActionToLongMap201", None)
                    
                    setattr(item, "ActionToLongMap201", self)
                    

class analysis_scheduling_MarkovSchedulingTransition:

    def __init__(self, firings: str, name: str, incomings461: "MarkovSchedulingState" = None, outgoings458: "MarkovSchedulingState" = None):
        self.firings = firings
        self.name = name
        self.incomings461 = incomings461
        self.outgoings458 = outgoings458
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def firings(self):
        return self.__firings

    @firings.setter
    def firings(self, firings: str):
        self.__firings = firings


    @property
    def outgoings458(self):
        return self.__outgoings458

    @outgoings458.setter
    def outgoings458(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_scheduling_MarkovSchedulingTransition__outgoings458", None)
        self.__outgoings458 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MarkovSchedulingState459"):
                opp_val = getattr(old_value, "MarkovSchedulingState459", None)
                if opp_val == self:
                    setattr(old_value, "MarkovSchedulingState459", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MarkovSchedulingState459"):
                opp_val = getattr(value, "MarkovSchedulingState459", None)
                setattr(value, "MarkovSchedulingState459", self)

    @property
    def incomings461(self):
        return self.__incomings461

    @incomings461.setter
    def incomings461(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_scheduling_MarkovSchedulingTransition__incomings461", None)
        self.__incomings461 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MarkovSchedulingState462"):
                opp_val = getattr(old_value, "MarkovSchedulingState462", None)
                if opp_val == self:
                    setattr(old_value, "MarkovSchedulingState462", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MarkovSchedulingState462"):
                opp_val = getattr(value, "MarkovSchedulingState462", None)
                setattr(value, "MarkovSchedulingState462", self)

class MarkovModelActionData:

    pass
class analysis_trace_ComparedAction:

    def __init__(self, found: bool, dSteps: str, dIncomings: str, dOutgoings: str, analysis_trace_ComparedAction: "trace_analysis_Action" = None):
        self.found = found
        self.dSteps = dSteps
        self.dIncomings = dIncomings
        self.dOutgoings = dOutgoings
        self.analysis_trace_ComparedAction = analysis_trace_ComparedAction
        
        pass
    @property
    def dSteps(self):
        return self.__dSteps

    @dSteps.setter
    def dSteps(self, dSteps: str):
        self.__dSteps = dSteps


    @property
    def dOutgoings(self):
        return self.__dOutgoings

    @dOutgoings.setter
    def dOutgoings(self, dOutgoings: str):
        self.__dOutgoings = dOutgoings


    @property
    def found(self):
        return self.__found

    @found.setter
    def found(self, found: bool):
        self.__found = found


    @property
    def dIncomings(self):
        return self.__dIncomings

    @dIncomings.setter
    def dIncomings(self, dIncomings: str):
        self.__dIncomings = dIncomings


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
            if hasattr(old_value, "trace_analysis_Action192"):
                opp_val = getattr(old_value, "trace_analysis_Action192", None)
                if opp_val == self:
                    setattr(old_value, "trace_analysis_Action192", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_analysis_Action192"):
                opp_val = getattr(value, "trace_analysis_Action192", None)
                setattr(value, "trace_analysis_Action192", self)

class ComparedAction:

    pass
class bottlenecks_analysis_Action:

    pass
class analysis_trace_ComparedTrace:

    def __init__(self, dDependencies: str, dSteps: str, equal: bool, analysis_trace_ComparedTrace: "CompressedTraceReport" = None, analysis_trace_ComparedTrace187: set["trace_analysis_Action"] = None, analysis_trace_ComparedTrace190: set["ComparedAction"] = None):
        self.dDependencies = dDependencies
        self.dSteps = dSteps
        self.equal = equal
        self.analysis_trace_ComparedTrace = analysis_trace_ComparedTrace
        self.analysis_trace_ComparedTrace187 = analysis_trace_ComparedTrace187 if analysis_trace_ComparedTrace187 is not None else set()
        self.analysis_trace_ComparedTrace190 = analysis_trace_ComparedTrace190 if analysis_trace_ComparedTrace190 is not None else set()
        
        pass
    @property
    def dSteps(self):
        return self.__dSteps

    @dSteps.setter
    def dSteps(self, dSteps: str):
        self.__dSteps = dSteps


    @property
    def equal(self):
        return self.__equal

    @equal.setter
    def equal(self, equal: bool):
        self.__equal = equal


    @property
    def dDependencies(self):
        return self.__dDependencies

    @dDependencies.setter
    def dDependencies(self, dDependencies: str):
        self.__dDependencies = dDependencies


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
            if hasattr(old_value, "CompressedTraceReport185"):
                opp_val = getattr(old_value, "CompressedTraceReport185", None)
                if opp_val == self:
                    setattr(old_value, "CompressedTraceReport185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompressedTraceReport185"):
                opp_val = getattr(value, "CompressedTraceReport185", None)
                setattr(value, "CompressedTraceReport185", self)

    @property
    def analysis_trace_ComparedTrace187(self):
        return self.__analysis_trace_ComparedTrace187

    @analysis_trace_ComparedTrace187.setter
    def analysis_trace_ComparedTrace187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_trace_ComparedTrace__analysis_trace_ComparedTrace187", None)
        self.__analysis_trace_ComparedTrace187 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trace_analysis_Action188"):
                    opp_val = getattr(item, "trace_analysis_Action188", None)
                    
                    if opp_val == self:
                        setattr(item, "trace_analysis_Action188", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trace_analysis_Action188"):
                    opp_val = getattr(item, "trace_analysis_Action188", None)
                    
                    setattr(item, "trace_analysis_Action188", self)
                    

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

    def __init__(self, count: str, outgoings: "CompressedStep" = None, incomings: "CompressedStep" = None):
        self.count = count
        self.outgoings = outgoings
        self.incomings = incomings
        
        pass
    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count: str):
        self.__count = count


    @property
    def incomings(self):
        return self.__incomings

    @incomings.setter
    def incomings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_trace_CompressedDependency__incomings", None)
        self.__incomings = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompressedStep158"):
                opp_val = getattr(old_value, "CompressedStep158", None)
                if opp_val == self:
                    setattr(old_value, "CompressedStep158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompressedStep158"):
                opp_val = getattr(value, "CompressedStep158", None)
                setattr(value, "CompressedStep158", self)

    @property
    def outgoings(self):
        return self.__outgoings

    @outgoings.setter
    def outgoings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_trace_CompressedDependency__outgoings", None)
        self.__outgoings = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompressedStep156"):
                opp_val = getattr(old_value, "CompressedStep156", None)
                if opp_val == self:
                    setattr(old_value, "CompressedStep156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompressedStep156"):
                opp_val = getattr(value, "CompressedStep156", None)
                setattr(value, "CompressedStep156", self)

class trace_analysis_Action:

    pass
class analysis_trace_CompressedStep:

    def __init__(self, count: str, analysis_trace_CompressedStep: "trace_analysis_Action" = None, target: set["CompressedDependency"] = None, source: set["CompressedDependency"] = None, analysis_trace_CompressedStep147: set["CompressedStep"] = None, analysis_trace_CompressedStep150: set["CompressedStep"] = None, analysis_trace_CompressedStep153: set["CompressedStep"] = None):
        self.count = count
        self.analysis_trace_CompressedStep = analysis_trace_CompressedStep
        self.target = target if target is not None else set()
        self.source = source if source is not None else set()
        self.analysis_trace_CompressedStep147 = analysis_trace_CompressedStep147 if analysis_trace_CompressedStep147 is not None else set()
        self.analysis_trace_CompressedStep150 = analysis_trace_CompressedStep150 if analysis_trace_CompressedStep150 is not None else set()
        self.analysis_trace_CompressedStep153 = analysis_trace_CompressedStep153 if analysis_trace_CompressedStep153 is not None else set()
        
        pass
    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count: str):
        self.__count = count


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
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_trace_CompressedStep__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompressedDependency145"):
                    opp_val = getattr(item, "CompressedDependency145", None)
                    
                    if opp_val == self:
                        setattr(item, "CompressedDependency145", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompressedDependency145"):
                    opp_val = getattr(item, "CompressedDependency145", None)
                    
                    setattr(item, "CompressedDependency145", self)
                    

    @property
    def analysis_trace_CompressedStep153(self):
        return self.__analysis_trace_CompressedStep153

    @analysis_trace_CompressedStep153.setter
    def analysis_trace_CompressedStep153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_trace_CompressedStep__analysis_trace_CompressedStep153", None)
        self.__analysis_trace_CompressedStep153 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompressedStep154"):
                    opp_val = getattr(item, "CompressedStep154", None)
                    
                    if opp_val == self:
                        setattr(item, "CompressedStep154", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompressedStep154"):
                    opp_val = getattr(item, "CompressedStep154", None)
                    
                    setattr(item, "CompressedStep154", self)
                    

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_trace_CompressedStep__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompressedDependency143"):
                    opp_val = getattr(item, "CompressedDependency143", None)
                    
                    if opp_val == self:
                        setattr(item, "CompressedDependency143", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompressedDependency143"):
                    opp_val = getattr(item, "CompressedDependency143", None)
                    
                    setattr(item, "CompressedDependency143", self)
                    

    @property
    def analysis_trace_CompressedStep147(self):
        return self.__analysis_trace_CompressedStep147

    @analysis_trace_CompressedStep147.setter
    def analysis_trace_CompressedStep147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_trace_CompressedStep__analysis_trace_CompressedStep147", None)
        self.__analysis_trace_CompressedStep147 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompressedStep148"):
                    opp_val = getattr(item, "CompressedStep148", None)
                    
                    if opp_val == self:
                        setattr(item, "CompressedStep148", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompressedStep148"):
                    opp_val = getattr(item, "CompressedStep148", None)
                    
                    setattr(item, "CompressedStep148", self)
                    

    @property
    def analysis_trace_CompressedStep150(self):
        return self.__analysis_trace_CompressedStep150

    @analysis_trace_CompressedStep150.setter
    def analysis_trace_CompressedStep150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_trace_CompressedStep__analysis_trace_CompressedStep150", None)
        self.__analysis_trace_CompressedStep150 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompressedStep151"):
                    opp_val = getattr(item, "CompressedStep151", None)
                    
                    if opp_val == self:
                        setattr(item, "CompressedStep151", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompressedStep151"):
                    opp_val = getattr(item, "CompressedStep151", None)
                    
                    setattr(item, "CompressedStep151", self)
                    

class CompressedDependency:

    pass
class analysis_trace_CompressedPortDependency(CompressedDependency):

    pass
class analysis_trace_CompressedFsmDependency(CompressedDependency):

    pass
class analysis_trace_CompressedGuardDependency(CompressedDependency):

    pass
class analysis_trace_CompressedVariableDependency(CompressedDependency):

    pass
class analysis_trace_CompressedTokensDependency(CompressedDependency):

    pass
class CompressedStep:

    pass
class trace_analysis_Network:

    pass
class StringToLongMap:

    pass
class analysis_map_ActionToDoubleMap:

    def __init__(self, value: str, analysis_map_ActionToDoubleMap: "map_analysis_Action" = None):
        self.value = value
        self.analysis_map_ActionToDoubleMap = analysis_map_ActionToDoubleMap
        
        pass
    @property
    def value(self):
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

class ActorToLongMap:

    pass
class analysis_map_StringToStringMap:

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class ActorSelectionSchedule:

    pass
class analysis_scheduling_ActorFire(ActorSelectionSchedule):

    def __init__(self, Actor: str, Times: int, partition: str, dependencyPartitions: str, ActorSelectionSchedule: "analysis_map_PartitionToActorSelectionScheduleMap" = None):
        self.Actor = Actor
        self.Times = Times
        self.partition = partition
        self.dependencyPartitions = dependencyPartitions
        
        pass
    @property
    def dependencyPartitions(self):
        return self.__dependencyPartitions

    @dependencyPartitions.setter
    def dependencyPartitions(self, dependencyPartitions: str):
        self.__dependencyPartitions = dependencyPartitions


    @property
    def Actor(self):
        return self.__Actor

    @Actor.setter
    def Actor(self, Actor: str):
        self.__Actor = Actor


    @property
    def partition(self):
        return self.__partition

    @partition.setter
    def partition(self, partition: str):
        self.__partition = partition


    @property
    def Times(self):
        return self.__Times

    @Times.setter
    def Times(self, Times: int):
        self.__Times = Times


class analysis_scheduling_FSM(ActorSelectionSchedule):

    def __init__(self, startState: str, terminalState: str, analysis_scheduling_FSM: set["FSMState"] = None, analysis_scheduling_FSM424: set["FSMVar"] = None, ActorSelectionSchedule: "analysis_map_PartitionToActorSelectionScheduleMap" = None):
        self.startState = startState
        self.terminalState = terminalState
        self.analysis_scheduling_FSM = analysis_scheduling_FSM if analysis_scheduling_FSM is not None else set()
        self.analysis_scheduling_FSM424 = analysis_scheduling_FSM424 if analysis_scheduling_FSM424 is not None else set()
        
        pass
    @property
    def terminalState(self):
        return self.__terminalState

    @terminalState.setter
    def terminalState(self, terminalState: str):
        self.__terminalState = terminalState


    @property
    def startState(self):
        return self.__startState

    @startState.setter
    def startState(self, startState: str):
        self.__startState = startState


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
                    

    @property
    def analysis_scheduling_FSM424(self):
        return self.__analysis_scheduling_FSM424

    @analysis_scheduling_FSM424.setter
    def analysis_scheduling_FSM424(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_scheduling_FSM__analysis_scheduling_FSM424", None)
        self.__analysis_scheduling_FSM424 = value if value is not None else set()
        
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
                    

class analysis_caseoptimal_CaseOptimalActorSelectionSchedule(ActorSelectionSchedule):

    pass
class analysis_scheduling_Sequence(ActorSelectionSchedule):

    pass
class analysis_map_PartitionToActorSelectionScheduleMap:

    def __init__(self, key: str, analysis_map_PartitionToActorSelectionScheduleMap: "ActorSelectionSchedule" = None):
        self.key = key
        self.analysis_map_PartitionToActorSelectionScheduleMap = analysis_map_PartitionToActorSelectionScheduleMap
        
        pass
    @property
    def key(self):
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
        
        pass
    @property
    def value(self):
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
        
        pass
    @property
    def value(self):
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

class map_analysis_Procedure:

    pass
class analysis_map_StringToDoubleMap:

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class map_analysis_Port:

    pass
class analysis_map_PortToLongMap:

    def __init__(self, value: str, analysis_map_PortToLongMap: "map_analysis_Port" = None):
        self.value = value
        self.analysis_map_PortToLongMap = analysis_map_PortToLongMap
        
        pass
    @property
    def value(self):
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
        
        pass
    @property
    def value(self):
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
        
        pass
    @property
    def value(self):
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
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


class analysis_map_StringToLongMap:

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class analysis_map_BufferToLongMap:

    def __init__(self, value: str, analysis_map_BufferToLongMap: "map_analysis_Buffer" = None):
        self.value = value
        self.analysis_map_BufferToLongMap = analysis_map_BufferToLongMap
        
        pass
    @property
    def value(self):
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
        
        pass
    @property
    def value(self):
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
        
        pass
    @property
    def value(self):
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
        
        pass
    @property
    def key(self):
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
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


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
        
        pass
    @property
    def key(self):
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
        
        pass
    @property
    def min(self):
        return self.__min

    @min.setter
    def min(self, min: float):
        self.__min = min


    @property
    def average(self):
        return self.__average

    @average.setter
    def average(self, average: float):
        self.__average = average


    @property
    def accesses(self):
        return self.__accesses

    @accesses.setter
    def accesses(self, accesses: float):
        self.__accesses = accesses


    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, total: float):
        self.__total = total


    @property
    def max(self):
        return self.__max

    @max.setter
    def max(self, max: float):
        self.__max = max


class profiler_analysis_Procedure:

    pass
class StringToAccessDataMap:

    pass
class analysis_profiler_MemoryAccessData(ABC):

    pass
class MemoryAccessData:

    pass
class analysis_profiler_StateVariableAccessData(MemoryAccessData):

    def __init__(self, name: str, MemoryAccessData68: "analysis_profiler_ActionMemoryProfilingData" = None, MemoryAccessData: "analysis_profiler_ActionMemoryProfilingData" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class analysis_profiler_SharedVariableAccessData(MemoryAccessData):

    def __init__(self, name: str, MemoryAccessData68: "analysis_profiler_ActionMemoryProfilingData" = None, MemoryAccessData: "analysis_profiler_ActionMemoryProfilingData" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class analysis_profiler_BufferAccessData(MemoryAccessData):

    def __init__(self, sourceActor: str, sourcePort: str, targetActor: str, targetPort: str, MemoryAccessData68: "analysis_profiler_ActionMemoryProfilingData" = None, MemoryAccessData: "analysis_profiler_ActionMemoryProfilingData" = None):
        self.sourceActor = sourceActor
        self.sourcePort = sourcePort
        self.targetActor = targetActor
        self.targetPort = targetPort
        
        pass
    @property
    def sourcePort(self):
        return self.__sourcePort

    @sourcePort.setter
    def sourcePort(self, sourcePort: str):
        self.__sourcePort = sourcePort


    @property
    def targetActor(self):
        return self.__targetActor

    @targetActor.setter
    def targetActor(self, targetActor: str):
        self.__targetActor = targetActor


    @property
    def targetPort(self):
        return self.__targetPort

    @targetPort.setter
    def targetPort(self, targetPort: str):
        self.__targetPort = targetPort


    @property
    def sourceActor(self):
        return self.__sourceActor

    @sourceActor.setter
    def sourceActor(self, sourceActor: str):
        self.__sourceActor = sourceActor


class analysis_profiler_LocalVariableAccessData(MemoryAccessData):

    def __init__(self, name: str, MemoryAccessData68: "analysis_profiler_ActionMemoryProfilingData" = None, MemoryAccessData: "analysis_profiler_ActionMemoryProfilingData" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class analysis_profiler_ActionMemoryProfilingData:

    def __init__(self, actor: str, action: str, analysis_profiler_ActionMemoryProfilingData: set["MemoryAccessData"] = None, analysis_profiler_ActionMemoryProfilingData67: set["MemoryAccessData"] = None):
        self.actor = actor
        self.action = action
        self.analysis_profiler_ActionMemoryProfilingData = analysis_profiler_ActionMemoryProfilingData if analysis_profiler_ActionMemoryProfilingData is not None else set()
        self.analysis_profiler_ActionMemoryProfilingData67 = analysis_profiler_ActionMemoryProfilingData67 if analysis_profiler_ActionMemoryProfilingData67 is not None else set()
        
        pass
    @property
    def actor(self):
        return self.__actor

    @actor.setter
    def actor(self, actor: str):
        self.__actor = actor


    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action


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
                    

    def getWriteSharedVariableData(self, analysis_variable) :
        # TODO: Implement getWriteSharedVariableData method
        pass

    def getReadBufferData(self, analysis_targetActor, analysis_sourceActor, analysis_sourcePort, analysis_targetPort) :
        # TODO: Implement getReadBufferData method
        pass

    def getWriteStateVariableData(self, analysis_variable) :
        # TODO: Implement getWriteStateVariableData method
        pass

    def getReadStateVariableData(self, analysis_variable) :
        # TODO: Implement getReadStateVariableData method
        pass

    def getReadLocalVariableData(self, analysis_variable) :
        # TODO: Implement getReadLocalVariableData method
        pass

    def getReadSharedVariableData(self, analysis_variable) :
        # TODO: Implement getReadSharedVariableData method
        pass

    def getWriteLocalVariableData(self, analysis_variable) :
        # TODO: Implement getWriteLocalVariableData method
        pass

    def getWriteBufferData(self, analysis_targetActor, analysis_sourcePort, analysis_targetPort, analysis_sourceActor) :
        # TODO: Implement getWriteBufferData method
        pass

class ActionMemoryProfilingData:

    pass
class ActionDynamicData:

    pass
class analysis_profiler_ProcedureToComplexDynamicDataMap:

    pass
class BufferToStatisticalDataMap:

    pass
class ProcedureToComplexDynamicDataMap:

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
class profiler_analysis_Buffer:

    pass
class analysis_profiler_BufferDynamicData:

    def __init__(self, unconsumedTokens: int, analysis_profiler_BufferDynamicData41: set["ActionToLongMap"] = None, analysis_profiler_BufferDynamicData44: set["ActionToLongMap"] = None, analysis_profiler_BufferDynamicData: "profiler_analysis_Buffer" = None, analysis_profiler_BufferDynamicData26: "profiler_analysis_StatisticalData" = None, analysis_profiler_BufferDynamicData28: "profiler_analysis_StatisticalData" = None, analysis_profiler_BufferDynamicData31: "profiler_analysis_StatisticalData" = None, analysis_profiler_BufferDynamicData34: set["ActionToStatisticalDataMap"] = None, analysis_profiler_BufferDynamicData36: set["ActionToStatisticalDataMap"] = None, analysis_profiler_BufferDynamicData39: set["ActionToLongMap"] = None):
        self.unconsumedTokens = unconsumedTokens
        self.analysis_profiler_BufferDynamicData41 = analysis_profiler_BufferDynamicData41 if analysis_profiler_BufferDynamicData41 is not None else set()
        self.analysis_profiler_BufferDynamicData44 = analysis_profiler_BufferDynamicData44 if analysis_profiler_BufferDynamicData44 is not None else set()
        self.analysis_profiler_BufferDynamicData = analysis_profiler_BufferDynamicData
        self.analysis_profiler_BufferDynamicData26 = analysis_profiler_BufferDynamicData26
        self.analysis_profiler_BufferDynamicData28 = analysis_profiler_BufferDynamicData28
        self.analysis_profiler_BufferDynamicData31 = analysis_profiler_BufferDynamicData31
        self.analysis_profiler_BufferDynamicData34 = analysis_profiler_BufferDynamicData34 if analysis_profiler_BufferDynamicData34 is not None else set()
        self.analysis_profiler_BufferDynamicData36 = analysis_profiler_BufferDynamicData36 if analysis_profiler_BufferDynamicData36 is not None else set()
        self.analysis_profiler_BufferDynamicData39 = analysis_profiler_BufferDynamicData39 if analysis_profiler_BufferDynamicData39 is not None else set()
        
        pass
    @property
    def unconsumedTokens(self):
        return self.__unconsumedTokens

    @unconsumedTokens.setter
    def unconsumedTokens(self, unconsumedTokens: int):
        self.__unconsumedTokens = unconsumedTokens


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

class profiler_analysis_Action:

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

    def __init__(self, analysis_profiler_ComplexCodeData: set["CodeData"] = None, analysis_profiler_ComplexCodeData12: set["CodeData"] = None, CodeData: "analysis_profiler_ComplexCodeData" = None, CodeData13: "analysis_profiler_ComplexCodeData" = None):
        self.analysis_profiler_ComplexCodeData = analysis_profiler_ComplexCodeData if analysis_profiler_ComplexCodeData is not None else set()
        self.analysis_profiler_ComplexCodeData12 = analysis_profiler_ComplexCodeData12 if analysis_profiler_ComplexCodeData12 is not None else set()
        
        pass
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
                    

    def getActionData(self, analysis_action) :
        # TODO: Implement getActionData method
        pass

    def getProcedureData(self, analysis_procedure) :
        # TODO: Implement getProcedureData method
        pass

class StringToIntegerMap:

    pass
class analysis_profiler_CodeData:

    def __init__(self, blockName: str, nol: str, analysis_profiler_CodeData: set["StringToIntegerMap"] = None, analysis_profiler_CodeData8: set["StringToIntegerMap"] = None):
        self.blockName = blockName
        self.nol = nol
        self.analysis_profiler_CodeData = analysis_profiler_CodeData if analysis_profiler_CodeData is not None else set()
        self.analysis_profiler_CodeData8 = analysis_profiler_CodeData8 if analysis_profiler_CodeData8 is not None else set()
        
        pass
    @property
    def blockName(self):
        return self.__blockName

    @blockName.setter
    def blockName(self, blockName: str):
        self.__blockName = blockName


    @property
    def nol(self):
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
                    

class ComplexCodeData:

    pass
class profiler_analysis_Network:

    pass
class AnalysisReport:

    pass
class analysis_scheduling_MarkovSimpleSchedulerReport(AnalysisReport, postprocessing_PostProcessingData):

    pass
class analysis_profiler_MemoryProfilingReport(AnalysisReport):

    def __init__(self, networkName: str, analysis_profiler_MemoryProfilingReport: set["ActionMemoryProfilingData"] = None):
        self.networkName = networkName
        self.analysis_profiler_MemoryProfilingReport = analysis_profiler_MemoryProfilingReport if analysis_profiler_MemoryProfilingReport is not None else set()
        
        pass
    @property
    def networkName(self):
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
                    

    def getActionData(self, analysis_actor, analysis_action) :
        # TODO: Implement getActionData method
        pass

class analysis_buffers_BoundedBuffersReport(AnalysisReport):

    def __init__(self, pow2: bool, bitAccurate: bool, tokenSize: int, bitSize: int, analysis_buffers_BoundedBuffersReport: "buffers_analysis_Network" = None, analysis_buffers_BoundedBuffersReport260: set["BoundedBufferData"] = None):
        self.pow2 = pow2
        self.bitAccurate = bitAccurate
        self.tokenSize = tokenSize
        self.bitSize = bitSize
        self.analysis_buffers_BoundedBuffersReport = analysis_buffers_BoundedBuffersReport
        self.analysis_buffers_BoundedBuffersReport260 = analysis_buffers_BoundedBuffersReport260 if analysis_buffers_BoundedBuffersReport260 is not None else set()
        
        pass
    @property
    def tokenSize(self):
        return self.__tokenSize

    @tokenSize.setter
    def tokenSize(self, tokenSize: int):
        self.__tokenSize = tokenSize


    @property
    def pow2(self):
        return self.__pow2

    @pow2.setter
    def pow2(self, pow2: bool):
        self.__pow2 = pow2


    @property
    def bitSize(self):
        return self.__bitSize

    @bitSize.setter
    def bitSize(self, bitSize: int):
        self.__bitSize = bitSize


    @property
    def bitAccurate(self):
        return self.__bitAccurate

    @bitAccurate.setter
    def bitAccurate(self, bitAccurate: bool):
        self.__bitAccurate = bitAccurate


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

    @property
    def analysis_buffers_BoundedBuffersReport260(self):
        return self.__analysis_buffers_BoundedBuffersReport260

    @analysis_buffers_BoundedBuffersReport260.setter
    def analysis_buffers_BoundedBuffersReport260(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_buffers_BoundedBuffersReport__analysis_buffers_BoundedBuffersReport260", None)
        self.__analysis_buffers_BoundedBuffersReport260 = value if value is not None else set()
        
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
                    

class analysis_trace_TraceSizeReport(AnalysisReport):

    def __init__(self, firings: str, dependencies: str, analysis_trace_TraceSizeReport: set["ActionToLongMap"] = None, analysis_trace_TraceSizeReport118: set["ActionToLongMap"] = None, analysis_trace_TraceSizeReport121: set["ActionToLongMap"] = None, analysis_trace_TraceSizeReport124: set["ActorToLongMap"] = None, analysis_trace_TraceSizeReport129: set["ActorToLongMap"] = None, analysis_trace_TraceSizeReport132: set["StringToLongMap"] = None, analysis_trace_TraceSizeReport134: "trace_analysis_Network" = None, analysis_trace_TraceSizeReport126: set["ActorToLongMap"] = None):
        self.firings = firings
        self.dependencies = dependencies
        self.analysis_trace_TraceSizeReport = analysis_trace_TraceSizeReport if analysis_trace_TraceSizeReport is not None else set()
        self.analysis_trace_TraceSizeReport118 = analysis_trace_TraceSizeReport118 if analysis_trace_TraceSizeReport118 is not None else set()
        self.analysis_trace_TraceSizeReport121 = analysis_trace_TraceSizeReport121 if analysis_trace_TraceSizeReport121 is not None else set()
        self.analysis_trace_TraceSizeReport124 = analysis_trace_TraceSizeReport124 if analysis_trace_TraceSizeReport124 is not None else set()
        self.analysis_trace_TraceSizeReport129 = analysis_trace_TraceSizeReport129 if analysis_trace_TraceSizeReport129 is not None else set()
        self.analysis_trace_TraceSizeReport132 = analysis_trace_TraceSizeReport132 if analysis_trace_TraceSizeReport132 is not None else set()
        self.analysis_trace_TraceSizeReport134 = analysis_trace_TraceSizeReport134
        self.analysis_trace_TraceSizeReport126 = analysis_trace_TraceSizeReport126 if analysis_trace_TraceSizeReport126 is not None else set()
        
        pass
    @property
    def firings(self):
        return self.__firings

    @firings.setter
    def firings(self, firings: str):
        self.__firings = firings


    @property
    def dependencies(self):
        return self.__dependencies

    @dependencies.setter
    def dependencies(self, dependencies: str):
        self.__dependencies = dependencies


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
                    

class analysis_bottlenecks_ScheduledImpactAnalysisReport(AnalysisReport):

    def __init__(self, classLevel: bool, analysis_bottlenecks_ScheduledImpactAnalysisReport: "bottlenecks_analysis_Network" = None, analysis_bottlenecks_ScheduledImpactAnalysisReport256: "BottlenecksWithSchedulingReport" = None, analysis_bottlenecks_ScheduledImpactAnalysisReport254: set["ScheduledImpactAnalysisData"] = None):
        self.classLevel = classLevel
        self.analysis_bottlenecks_ScheduledImpactAnalysisReport = analysis_bottlenecks_ScheduledImpactAnalysisReport
        self.analysis_bottlenecks_ScheduledImpactAnalysisReport256 = analysis_bottlenecks_ScheduledImpactAnalysisReport256
        self.analysis_bottlenecks_ScheduledImpactAnalysisReport254 = analysis_bottlenecks_ScheduledImpactAnalysisReport254 if analysis_bottlenecks_ScheduledImpactAnalysisReport254 is not None else set()
        
        pass
    @property
    def classLevel(self):
        return self.__classLevel

    @classLevel.setter
    def classLevel(self, classLevel: bool):
        self.__classLevel = classLevel


    @property
    def analysis_bottlenecks_ScheduledImpactAnalysisReport254(self):
        return self.__analysis_bottlenecks_ScheduledImpactAnalysisReport254

    @analysis_bottlenecks_ScheduledImpactAnalysisReport254.setter
    def analysis_bottlenecks_ScheduledImpactAnalysisReport254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_bottlenecks_ScheduledImpactAnalysisReport__analysis_bottlenecks_ScheduledImpactAnalysisReport254", None)
        self.__analysis_bottlenecks_ScheduledImpactAnalysisReport254 = value if value is not None else set()
        
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
            if hasattr(old_value, "bottlenecks_analysis_Network252"):
                opp_val = getattr(old_value, "bottlenecks_analysis_Network252", None)
                if opp_val == self:
                    setattr(old_value, "bottlenecks_analysis_Network252", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bottlenecks_analysis_Network252"):
                opp_val = getattr(value, "bottlenecks_analysis_Network252", None)
                setattr(value, "bottlenecks_analysis_Network252", self)

    @property
    def analysis_bottlenecks_ScheduledImpactAnalysisReport256(self):
        return self.__analysis_bottlenecks_ScheduledImpactAnalysisReport256

    @analysis_bottlenecks_ScheduledImpactAnalysisReport256.setter
    def analysis_bottlenecks_ScheduledImpactAnalysisReport256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_bottlenecks_ScheduledImpactAnalysisReport__analysis_bottlenecks_ScheduledImpactAnalysisReport256", None)
        self.__analysis_bottlenecks_ScheduledImpactAnalysisReport256 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BottlenecksWithSchedulingReport257"):
                opp_val = getattr(old_value, "BottlenecksWithSchedulingReport257", None)
                if opp_val == self:
                    setattr(old_value, "BottlenecksWithSchedulingReport257", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BottlenecksWithSchedulingReport257"):
                opp_val = getattr(value, "BottlenecksWithSchedulingReport257", None)
                setattr(value, "BottlenecksWithSchedulingReport257", self)

class analysis_pipelining_ImpactAnalysisReport(AnalysisReport):

    pass
class analysis_partitioning_BalancedPipelinePartitioningReport(AnalysisReport):

    pass
class analysis_pipelining_ActionsVariablePipeliningReport(AnalysisReport):

    pass
class analysis_profiler_BenchmarkReport(AnalysisReport):

    def __init__(self, column_names: str, analysis_profiler_BenchmarkReport: set["TableRow"] = None):
        self.column_names = column_names
        self.analysis_profiler_BenchmarkReport = analysis_profiler_BenchmarkReport if analysis_profiler_BenchmarkReport is not None else set()
        
        pass
    @property
    def column_names(self):
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
                    

class analysis_bottlenecks_BottlenecksReport(AnalysisReport):

    def __init__(self, cpWeight: float, cpVariance: float, totalWeight: float, totalVariance: float, cpFirings: str, totalFirings: str, analysis_bottlenecks_BottlenecksReport: "bottlenecks_analysis_Network" = None, analysis_bottlenecks_BottlenecksReport204: set["ActionBottlenecksData"] = None):
        self.cpWeight = cpWeight
        self.cpVariance = cpVariance
        self.totalWeight = totalWeight
        self.totalVariance = totalVariance
        self.cpFirings = cpFirings
        self.totalFirings = totalFirings
        self.analysis_bottlenecks_BottlenecksReport = analysis_bottlenecks_BottlenecksReport
        self.analysis_bottlenecks_BottlenecksReport204 = analysis_bottlenecks_BottlenecksReport204 if analysis_bottlenecks_BottlenecksReport204 is not None else set()
        
        pass
    @property
    def cpFirings(self):
        return self.__cpFirings

    @cpFirings.setter
    def cpFirings(self, cpFirings: str):
        self.__cpFirings = cpFirings


    @property
    def totalVariance(self):
        return self.__totalVariance

    @totalVariance.setter
    def totalVariance(self, totalVariance: float):
        self.__totalVariance = totalVariance


    @property
    def totalWeight(self):
        return self.__totalWeight

    @totalWeight.setter
    def totalWeight(self, totalWeight: float):
        self.__totalWeight = totalWeight


    @property
    def cpWeight(self):
        return self.__cpWeight

    @cpWeight.setter
    def cpWeight(self, cpWeight: float):
        self.__cpWeight = cpWeight


    @property
    def cpVariance(self):
        return self.__cpVariance

    @cpVariance.setter
    def cpVariance(self, cpVariance: float):
        self.__cpVariance = cpVariance


    @property
    def totalFirings(self):
        return self.__totalFirings

    @totalFirings.setter
    def totalFirings(self, totalFirings: str):
        self.__totalFirings = totalFirings


    @property
    def analysis_bottlenecks_BottlenecksReport204(self):
        return self.__analysis_bottlenecks_BottlenecksReport204

    @analysis_bottlenecks_BottlenecksReport204.setter
    def analysis_bottlenecks_BottlenecksReport204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_bottlenecks_BottlenecksReport__analysis_bottlenecks_BottlenecksReport204", None)
        self.__analysis_bottlenecks_BottlenecksReport204 = value if value is not None else set()
        
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

class analysis_profiling_ProfilingStatsReport(AnalysisReport):

    def __init__(self, networkName: str, analysis_profiling_ProfilingStatsReport: set["ProfilingStatsActorData"] = None):
        self.networkName = networkName
        self.analysis_profiling_ProfilingStatsReport = analysis_profiling_ProfilingStatsReport if analysis_profiling_ProfilingStatsReport is not None else set()
        
        pass
    @property
    def networkName(self):
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

    def __init__(self, classLevel: bool, analysis_bottlenecks_ImpactAnalysisReport: "bottlenecks_analysis_Network" = None, analysis_bottlenecks_ImpactAnalysisReport209: set["ImpactAnalysisData"] = None, analysis_bottlenecks_ImpactAnalysisReport211: "BottlenecksReport" = None):
        self.classLevel = classLevel
        self.analysis_bottlenecks_ImpactAnalysisReport = analysis_bottlenecks_ImpactAnalysisReport
        self.analysis_bottlenecks_ImpactAnalysisReport209 = analysis_bottlenecks_ImpactAnalysisReport209 if analysis_bottlenecks_ImpactAnalysisReport209 is not None else set()
        self.analysis_bottlenecks_ImpactAnalysisReport211 = analysis_bottlenecks_ImpactAnalysisReport211
        
        pass
    @property
    def classLevel(self):
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
            if hasattr(old_value, "bottlenecks_analysis_Network207"):
                opp_val = getattr(old_value, "bottlenecks_analysis_Network207", None)
                if opp_val == self:
                    setattr(old_value, "bottlenecks_analysis_Network207", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bottlenecks_analysis_Network207"):
                opp_val = getattr(value, "bottlenecks_analysis_Network207", None)
                setattr(value, "bottlenecks_analysis_Network207", self)

    @property
    def analysis_bottlenecks_ImpactAnalysisReport211(self):
        return self.__analysis_bottlenecks_ImpactAnalysisReport211

    @analysis_bottlenecks_ImpactAnalysisReport211.setter
    def analysis_bottlenecks_ImpactAnalysisReport211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_bottlenecks_ImpactAnalysisReport__analysis_bottlenecks_ImpactAnalysisReport211", None)
        self.__analysis_bottlenecks_ImpactAnalysisReport211 = value
        
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

    @property
    def analysis_bottlenecks_ImpactAnalysisReport209(self):
        return self.__analysis_bottlenecks_ImpactAnalysisReport209

    @analysis_bottlenecks_ImpactAnalysisReport209.setter
    def analysis_bottlenecks_ImpactAnalysisReport209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_bottlenecks_ImpactAnalysisReport__analysis_bottlenecks_ImpactAnalysisReport209", None)
        self.__analysis_bottlenecks_ImpactAnalysisReport209 = value if value is not None else set()
        
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
                    

class analysis_profiler_DynamicProfilingReport(AnalysisReport):

    pass
class analysis_buffers_OptimalBuffersReport(AnalysisReport):

    def __init__(self, pow2: bool, bitAccurate: bool, analysis_buffers_OptimalBuffersReport: "buffers_analysis_Network" = None, analysis_buffers_OptimalBuffersReport265: set["OptimalBufferData"] = None, analysis_buffers_OptimalBuffersReport267: "BoundedBuffersReport" = None, analysis_buffers_OptimalBuffersReport269: "BottlenecksWithSchedulingReport" = None):
        self.pow2 = pow2
        self.bitAccurate = bitAccurate
        self.analysis_buffers_OptimalBuffersReport = analysis_buffers_OptimalBuffersReport
        self.analysis_buffers_OptimalBuffersReport265 = analysis_buffers_OptimalBuffersReport265 if analysis_buffers_OptimalBuffersReport265 is not None else set()
        self.analysis_buffers_OptimalBuffersReport267 = analysis_buffers_OptimalBuffersReport267
        self.analysis_buffers_OptimalBuffersReport269 = analysis_buffers_OptimalBuffersReport269
        
        pass
    @property
    def bitAccurate(self):
        return self.__bitAccurate

    @bitAccurate.setter
    def bitAccurate(self, bitAccurate: bool):
        self.__bitAccurate = bitAccurate


    @property
    def pow2(self):
        return self.__pow2

    @pow2.setter
    def pow2(self, pow2: bool):
        self.__pow2 = pow2


    @property
    def analysis_buffers_OptimalBuffersReport265(self):
        return self.__analysis_buffers_OptimalBuffersReport265

    @analysis_buffers_OptimalBuffersReport265.setter
    def analysis_buffers_OptimalBuffersReport265(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_buffers_OptimalBuffersReport__analysis_buffers_OptimalBuffersReport265", None)
        self.__analysis_buffers_OptimalBuffersReport265 = value if value is not None else set()
        
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
    def analysis_buffers_OptimalBuffersReport267(self):
        return self.__analysis_buffers_OptimalBuffersReport267

    @analysis_buffers_OptimalBuffersReport267.setter
    def analysis_buffers_OptimalBuffersReport267(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_buffers_OptimalBuffersReport__analysis_buffers_OptimalBuffersReport267", None)
        self.__analysis_buffers_OptimalBuffersReport267 = value
        
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

    @property
    def analysis_buffers_OptimalBuffersReport269(self):
        return self.__analysis_buffers_OptimalBuffersReport269

    @analysis_buffers_OptimalBuffersReport269.setter
    def analysis_buffers_OptimalBuffersReport269(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_buffers_OptimalBuffersReport__analysis_buffers_OptimalBuffersReport269", None)
        self.__analysis_buffers_OptimalBuffersReport269 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BottlenecksWithSchedulingReport270"):
                opp_val = getattr(old_value, "BottlenecksWithSchedulingReport270", None)
                if opp_val == self:
                    setattr(old_value, "BottlenecksWithSchedulingReport270", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BottlenecksWithSchedulingReport270"):
                opp_val = getattr(value, "BottlenecksWithSchedulingReport270", None)
                setattr(value, "BottlenecksWithSchedulingReport270", self)

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
            if hasattr(old_value, "buffers_analysis_Network263"):
                opp_val = getattr(old_value, "buffers_analysis_Network263", None)
                if opp_val == self:
                    setattr(old_value, "buffers_analysis_Network263", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "buffers_analysis_Network263"):
                opp_val = getattr(value, "buffers_analysis_Network263", None)
                setattr(value, "buffers_analysis_Network263", self)

class analysis_profiling_IntraActionCommunicationReport(AnalysisReport):

    pass
class analysis_bottlenecks_BottlenecksWithSchedulingReport(AnalysisReport, postprocessing_PostProcessingData):

    def __init__(self, totalFirings: str, cpWeight: float, totalWeight: float, cpFirings: str, executionTime: float, cpBlockingTime: float, analysis_bottlenecks_BottlenecksWithSchedulingReport: "bottlenecks_analysis_Network" = None, analysis_bottlenecks_BottlenecksWithSchedulingReport225: set["ActionBottlenecksWithSchedulingData"] = None, analysis_bottlenecks_BottlenecksWithSchedulingReport227: set["StringToDoubleMap"] = None):
        self.totalFirings = totalFirings
        self.cpWeight = cpWeight
        self.totalWeight = totalWeight
        self.cpFirings = cpFirings
        self.executionTime = executionTime
        self.cpBlockingTime = cpBlockingTime
        self.analysis_bottlenecks_BottlenecksWithSchedulingReport = analysis_bottlenecks_BottlenecksWithSchedulingReport
        self.analysis_bottlenecks_BottlenecksWithSchedulingReport225 = analysis_bottlenecks_BottlenecksWithSchedulingReport225 if analysis_bottlenecks_BottlenecksWithSchedulingReport225 is not None else set()
        self.analysis_bottlenecks_BottlenecksWithSchedulingReport227 = analysis_bottlenecks_BottlenecksWithSchedulingReport227 if analysis_bottlenecks_BottlenecksWithSchedulingReport227 is not None else set()
        
        pass
    @property
    def totalFirings(self):
        return self.__totalFirings

    @totalFirings.setter
    def totalFirings(self, totalFirings: str):
        self.__totalFirings = totalFirings


    @property
    def executionTime(self):
        return self.__executionTime

    @executionTime.setter
    def executionTime(self, executionTime: float):
        self.__executionTime = executionTime


    @property
    def cpBlockingTime(self):
        return self.__cpBlockingTime

    @cpBlockingTime.setter
    def cpBlockingTime(self, cpBlockingTime: float):
        self.__cpBlockingTime = cpBlockingTime


    @property
    def cpFirings(self):
        return self.__cpFirings

    @cpFirings.setter
    def cpFirings(self, cpFirings: str):
        self.__cpFirings = cpFirings


    @property
    def cpWeight(self):
        return self.__cpWeight

    @cpWeight.setter
    def cpWeight(self, cpWeight: float):
        self.__cpWeight = cpWeight


    @property
    def totalWeight(self):
        return self.__totalWeight

    @totalWeight.setter
    def totalWeight(self, totalWeight: float):
        self.__totalWeight = totalWeight


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
            if hasattr(old_value, "bottlenecks_analysis_Network223"):
                opp_val = getattr(old_value, "bottlenecks_analysis_Network223", None)
                if opp_val == self:
                    setattr(old_value, "bottlenecks_analysis_Network223", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bottlenecks_analysis_Network223"):
                opp_val = getattr(value, "bottlenecks_analysis_Network223", None)
                setattr(value, "bottlenecks_analysis_Network223", self)

    @property
    def analysis_bottlenecks_BottlenecksWithSchedulingReport225(self):
        return self.__analysis_bottlenecks_BottlenecksWithSchedulingReport225

    @analysis_bottlenecks_BottlenecksWithSchedulingReport225.setter
    def analysis_bottlenecks_BottlenecksWithSchedulingReport225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_bottlenecks_BottlenecksWithSchedulingReport__analysis_bottlenecks_BottlenecksWithSchedulingReport225", None)
        self.__analysis_bottlenecks_BottlenecksWithSchedulingReport225 = value if value is not None else set()
        
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
    def analysis_bottlenecks_BottlenecksWithSchedulingReport227(self):
        return self.__analysis_bottlenecks_BottlenecksWithSchedulingReport227

    @analysis_bottlenecks_BottlenecksWithSchedulingReport227.setter
    def analysis_bottlenecks_BottlenecksWithSchedulingReport227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_bottlenecks_BottlenecksWithSchedulingReport__analysis_bottlenecks_BottlenecksWithSchedulingReport227", None)
        self.__analysis_bottlenecks_BottlenecksWithSchedulingReport227 = value if value is not None else set()
        
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
                    

class analysis_caseoptimal_CaseOptimalScheduleReport(AnalysisReport):

    def __init__(self, traceFile: str, pipeline: str, partitionFilePath: str, analysis_caseoptimal_CaseOptimalScheduleReport: set["PartitionToActorSelectionScheduleMap"] = None):
        self.traceFile = traceFile
        self.pipeline = pipeline
        self.partitionFilePath = partitionFilePath
        self.analysis_caseoptimal_CaseOptimalScheduleReport = analysis_caseoptimal_CaseOptimalScheduleReport if analysis_caseoptimal_CaseOptimalScheduleReport is not None else set()
        
        pass
    @property
    def partitionFilePath(self):
        return self.__partitionFilePath

    @partitionFilePath.setter
    def partitionFilePath(self, partitionFilePath: str):
        self.__partitionFilePath = partitionFilePath


    @property
    def traceFile(self):
        return self.__traceFile

    @traceFile.setter
    def traceFile(self, traceFile: str):
        self.__traceFile = traceFile


    @property
    def pipeline(self):
        return self.__pipeline

    @pipeline.setter
    def pipeline(self, pipeline: str):
        self.__pipeline = pipeline


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
                    

class analysis_trace_TraceComparatorReport(AnalysisReport):

    pass
class analysis_trace_MarkowModelTraceReport(AnalysisReport):

    def __init__(self, analysis_trace_MarkowModelTraceReport: "trace_analysis_Network" = None, analysis_trace_MarkowModelTraceReport196: set["MarkovModelActionData"] = None):
        self.analysis_trace_MarkowModelTraceReport = analysis_trace_MarkowModelTraceReport
        self.analysis_trace_MarkowModelTraceReport196 = analysis_trace_MarkowModelTraceReport196 if analysis_trace_MarkowModelTraceReport196 is not None else set()
        
        pass
    @property
    def analysis_trace_MarkowModelTraceReport196(self):
        return self.__analysis_trace_MarkowModelTraceReport196

    @analysis_trace_MarkowModelTraceReport196.setter
    def analysis_trace_MarkowModelTraceReport196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_trace_MarkowModelTraceReport__analysis_trace_MarkowModelTraceReport196", None)
        self.__analysis_trace_MarkowModelTraceReport196 = value if value is not None else set()
        
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
            if hasattr(old_value, "trace_analysis_Network194"):
                opp_val = getattr(old_value, "trace_analysis_Network194", None)
                if opp_val == self:
                    setattr(old_value, "trace_analysis_Network194", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_analysis_Network194"):
                opp_val = getattr(value, "trace_analysis_Network194", None)
                setattr(value, "trace_analysis_Network194", self)

    def getData(self, analysis_action) :
        # TODO: Implement getData method
        pass

class analysis_partitioning_WorkloadBalancePartitioningReport(AnalysisReport):

    pass
class analysis_postprocessing_PostProcessingReport(AnalysisReport):

    def __init__(self, time: float, deadlock: bool, analysis_postprocessing_PostProcessingReport: "postprocessing_analysis_Network" = None, analysis_postprocessing_PostProcessingReport326: set["PostProcessingData"] = None):
        self.time = time
        self.deadlock = deadlock
        self.analysis_postprocessing_PostProcessingReport = analysis_postprocessing_PostProcessingReport
        self.analysis_postprocessing_PostProcessingReport326 = analysis_postprocessing_PostProcessingReport326 if analysis_postprocessing_PostProcessingReport326 is not None else set()
        
        pass
    @property
    def deadlock(self):
        return self.__deadlock

    @deadlock.setter
    def deadlock(self, deadlock: bool):
        self.__deadlock = deadlock


    @property
    def time(self):
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
    def analysis_postprocessing_PostProcessingReport326(self):
        return self.__analysis_postprocessing_PostProcessingReport326

    @analysis_postprocessing_PostProcessingReport326.setter
    def analysis_postprocessing_PostProcessingReport326(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_postprocessing_PostProcessingReport__analysis_postprocessing_PostProcessingReport326", None)
        self.__analysis_postprocessing_PostProcessingReport326 = value if value is not None else set()
        
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
                    

class analysis_partitioning_ComCostPartitioningReport(AnalysisReport):

    def __init__(self, bitAccurate: bool, analysis_partitioning_ComCostPartitioningReport: "partitioning_analysis_Network" = None, analysis_partitioning_ComCostPartitioningReport278: set["ComCostPartition"] = None):
        self.bitAccurate = bitAccurate
        self.analysis_partitioning_ComCostPartitioningReport = analysis_partitioning_ComCostPartitioningReport
        self.analysis_partitioning_ComCostPartitioningReport278 = analysis_partitioning_ComCostPartitioningReport278 if analysis_partitioning_ComCostPartitioningReport278 is not None else set()
        
        pass
    @property
    def bitAccurate(self):
        return self.__bitAccurate

    @bitAccurate.setter
    def bitAccurate(self, bitAccurate: bool):
        self.__bitAccurate = bitAccurate


    @property
    def analysis_partitioning_ComCostPartitioningReport278(self):
        return self.__analysis_partitioning_ComCostPartitioningReport278

    @analysis_partitioning_ComCostPartitioningReport278.setter
    def analysis_partitioning_ComCostPartitioningReport278(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_analysis_partitioning_ComCostPartitioningReport__analysis_partitioning_ComCostPartitioningReport278", None)
        self.__analysis_partitioning_ComCostPartitioningReport278 = value if value is not None else set()
        
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

class analysis_trace_CompressedTraceReport(AnalysisReport):

    def __init__(self, traceFile: str, analysis_trace_CompressedTraceReport: "trace_analysis_Network" = None, analysis_trace_CompressedTraceReport138: set["CompressedStep"] = None, analysis_trace_CompressedTraceReport140: set["CompressedDependency"] = None):
        self.traceFile = traceFile
        self.analysis_trace_CompressedTraceReport = analysis_trace_CompressedTraceReport
        self.analysis_trace_CompressedTraceReport138 = analysis_trace_CompressedTraceReport138 if analysis_trace_CompressedTraceReport138 is not None else set()
        self.analysis_trace_CompressedTraceReport140 = analysis_trace_CompressedTraceReport140 if analysis_trace_CompressedTraceReport140 is not None else set()
        
        pass
    @property
    def traceFile(self):
        return self.__traceFile

    @traceFile.setter
    def traceFile(self, traceFile: str):
        self.__traceFile = traceFile


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
                    

    def getSteps(self, analysis_actor) :
        # TODO: Implement getSteps method
        pass

class analysis_profiler_CodeProfilingReport(AnalysisReport):

    def __init__(self, analysis_profiler_CodeProfilingReport: "profiler_analysis_Network" = None, analysis_profiler_CodeProfilingReport2: set["ComplexCodeData"] = None, analysis_profiler_CodeProfilingReport4: "ComplexCodeData" = None):
        self.analysis_profiler_CodeProfilingReport = analysis_profiler_CodeProfilingReport
        self.analysis_profiler_CodeProfilingReport2 = analysis_profiler_CodeProfilingReport2 if analysis_profiler_CodeProfilingReport2 is not None else set()
        self.analysis_profiler_CodeProfilingReport4 = analysis_profiler_CodeProfilingReport4
        
        pass
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

    def getActorClassData(self, analysis_actorClass) :
        # TODO: Implement getActorClassData method
        pass

class analysis_AnalysisReport(ABC):

    def __init__(self, algorithm: str, date: date):
        self.algorithm = algorithm
        self.date = date
        
        pass
    @property
    def algorithm(self):
        return self.__algorithm

    @algorithm.setter
    def algorithm(self, algorithm: str):
        self.__algorithm = algorithm


    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

