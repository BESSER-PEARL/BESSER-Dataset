####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Enumerations
FSMOp: Enumeration = Enumeration(
    name="FSMOp",
    literals={
            EnumerationLiteral(name="ADD"),
			EnumerationLiteral(name="SET")
    }
)

FSMComparator: Enumeration = Enumeration(
    name="FSMComparator",
    literals={
            EnumerationLiteral(name="EQ"),
			EnumerationLiteral(name="NEQ"),
			EnumerationLiteral(name="GREATER"),
			EnumerationLiteral(name="SMALLER"),
			EnumerationLiteral(name="GREQ"),
			EnumerationLiteral(name="SMEQ")
    }
)

FSMCombinator: Enumeration = Enumeration(
    name="FSMCombinator",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="NAND"),
			EnumerationLiteral(name="NOR"),
			EnumerationLiteral(name="NOT")
    }
)

Optimizer: Enumeration = Enumeration(
    name="Optimizer",
    literals={
            EnumerationLiteral(name="RLE"),
			EnumerationLiteral(name="KTAIL")
    }
)

# Classes
analysis_AnalysisReport = Class(name="analysis_AnalysisReport", is_abstract=True)
analysis_profiler_CodeProfilingReport = Class(name="analysis_profiler_CodeProfilingReport")
AnalysisReport = Class(name="AnalysisReport")
profiler_analysis_Network = Class(name="profiler_analysis_Network")
ComplexCodeData = Class(name="ComplexCodeData")
analysis_profiler_CodeData = Class(name="analysis_profiler_CodeData")
StringToIntegerMap = Class(name="StringToIntegerMap")
analysis_profiler_ComplexCodeData = Class(name="analysis_profiler_ComplexCodeData")
CodeData = Class(name="CodeData")
analysis_profiler_DynamicProfilingReport = Class(name="analysis_profiler_DynamicProfilingReport")
ActorDynamicData = Class(name="ActorDynamicData")
BufferDynamicData = Class(name="BufferDynamicData")
analysis_profiler_ActorDynamicData = Class(name="analysis_profiler_ActorDynamicData")
ComplexDynamicData = Class(name="ComplexDynamicData")
profiler_analysis_Actor = Class(name="profiler_analysis_Actor")
analysis_profiler_ActionDynamicData = Class(name="analysis_profiler_ActionDynamicData")
profiler_analysis_Action = Class(name="profiler_analysis_Action")
analysis_profiler_BufferDynamicData = Class(name="analysis_profiler_BufferDynamicData")
profiler_analysis_Buffer = Class(name="profiler_analysis_Buffer")
profiler_analysis_StatisticalData = Class(name="profiler_analysis_StatisticalData")
ActionToStatisticalDataMap = Class(name="ActionToStatisticalDataMap")
ActionToLongMap = Class(name="ActionToLongMap")
analysis_profiler_ComplexDynamicData = Class(name="analysis_profiler_ComplexDynamicData")
EOperatorToStatisticalDataMap = Class(name="EOperatorToStatisticalDataMap")
ProcedureToStatisticalDataMap = Class(name="ProcedureToStatisticalDataMap")
VariableToStatisticalDataMap = Class(name="VariableToStatisticalDataMap")
ProcedureToComplexDynamicDataMap = Class(name="ProcedureToComplexDynamicDataMap")
BufferToStatisticalDataMap = Class(name="BufferToStatisticalDataMap")
analysis_profiler_ProcedureToComplexDynamicDataMap = Class(name="analysis_profiler_ProcedureToComplexDynamicDataMap")
ActionDynamicData = Class(name="ActionDynamicData")
analysis_profiler_MemoryProfilingReport = Class(name="analysis_profiler_MemoryProfilingReport")
ActionMemoryProfilingData = Class(name="ActionMemoryProfilingData")
analysis_profiler_ActionMemoryProfilingData = Class(name="analysis_profiler_ActionMemoryProfilingData")
MemoryAccessData = Class(name="MemoryAccessData")
analysis_profiler_MemoryAccessData = Class(name="analysis_profiler_MemoryAccessData", is_abstract=True)
StringToAccessDataMap = Class(name="StringToAccessDataMap")
analysis_profiler_BufferAccessData = Class(name="analysis_profiler_BufferAccessData")
profiler_analysis_Procedure = Class(name="profiler_analysis_Procedure")
analysis_profiler_SharedVariableAccessData = Class(name="analysis_profiler_SharedVariableAccessData")
analysis_profiler_AccessData = Class(name="analysis_profiler_AccessData")
analysis_profiler_StringToAccessDataMap = Class(name="analysis_profiler_StringToAccessDataMap")
AccessData = Class(name="AccessData")
analysis_profiler_BenchmarkReport = Class(name="analysis_profiler_BenchmarkReport")
TableRow = Class(name="TableRow")
analysis_profiler_TableRow = Class(name="analysis_profiler_TableRow")
StringToStringMap = Class(name="StringToStringMap")
analysis_map_StringToIntegerMap = Class(name="analysis_map_StringToIntegerMap")
analysis_map_ActorToStatisticalDataMap = Class(name="analysis_map_ActorToStatisticalDataMap")
map_analysis_Actor = Class(name="map_analysis_Actor")
map_analysis_StatisticalData = Class(name="map_analysis_StatisticalData")
analysis_map_ActionToStatisticalDataMap = Class(name="analysis_map_ActionToStatisticalDataMap")
map_analysis_Action = Class(name="map_analysis_Action")
analysis_map_BufferToStatisticalDataMap = Class(name="analysis_map_BufferToStatisticalDataMap")
map_analysis_Buffer = Class(name="map_analysis_Buffer")
analysis_map_ProcedureToStatisticalDataMap = Class(name="analysis_map_ProcedureToStatisticalDataMap")
analysis_profiler_StateVariableAccessData = Class(name="analysis_profiler_StateVariableAccessData")
analysis_profiler_LocalVariableAccessData = Class(name="analysis_profiler_LocalVariableAccessData")
analysis_map_VariableToStatisticalDataMap = Class(name="analysis_map_VariableToStatisticalDataMap")
map_analysis_Variable = Class(name="map_analysis_Variable")
analysis_map_ActorClassToStatisticalDataMap = Class(name="analysis_map_ActorClassToStatisticalDataMap")
map_analysis_ActorClass = Class(name="map_analysis_ActorClass")
analysis_map_EOperatorToStatisticalDataMap = Class(name="analysis_map_EOperatorToStatisticalDataMap")
analysis_map_ActionToLongMap = Class(name="analysis_map_ActionToLongMap")
analysis_map_ActorToLongMap = Class(name="analysis_map_ActorToLongMap")
analysis_map_BufferToLongMap = Class(name="analysis_map_BufferToLongMap")
analysis_map_StringToLongMap = Class(name="analysis_map_StringToLongMap")
analysis_map_DoubleToDoubleMap = Class(name="analysis_map_DoubleToDoubleMap")
analysis_map_VariableToLongMap = Class(name="analysis_map_VariableToLongMap")
analysis_map_GuardToLongMap = Class(name="analysis_map_GuardToLongMap")
map_analysis_Guard = Class(name="map_analysis_Guard")
analysis_map_PortToLongMap = Class(name="analysis_map_PortToLongMap")
map_analysis_Port = Class(name="map_analysis_Port")
analysis_map_StringToDoubleMap = Class(name="analysis_map_StringToDoubleMap")
map_analysis_Procedure = Class(name="map_analysis_Procedure")
analysis_map_BufferToIntegerMap = Class(name="analysis_map_BufferToIntegerMap")
analysis_map_BufferToDoubleMap = Class(name="analysis_map_BufferToDoubleMap")
analysis_map_PartitionToActorSelectionScheduleMap = Class(name="analysis_map_PartitionToActorSelectionScheduleMap")
ActorSelectionSchedule = Class(name="ActorSelectionSchedule")
analysis_map_StringToStringMap = Class(name="analysis_map_StringToStringMap")
analysis_trace_TraceSizeReport = Class(name="analysis_trace_TraceSizeReport")
ActorToLongMap = Class(name="ActorToLongMap")
analysis_map_ActionToDoubleMap = Class(name="analysis_map_ActionToDoubleMap")
StringToLongMap = Class(name="StringToLongMap")
trace_analysis_Network = Class(name="trace_analysis_Network")
analysis_trace_CompressedTraceReport = Class(name="analysis_trace_CompressedTraceReport")
CompressedStep = Class(name="CompressedStep")
CompressedDependency = Class(name="CompressedDependency")
analysis_trace_CompressedStep = Class(name="analysis_trace_CompressedStep")
trace_analysis_Action = Class(name="trace_analysis_Action")
analysis_trace_CompressedDependency = Class(name="analysis_trace_CompressedDependency", is_abstract=True)
analysis_trace_CompressedFsmDependency = Class(name="analysis_trace_CompressedFsmDependency")
analysis_trace_CompressedGuardDependency = Class(name="analysis_trace_CompressedGuardDependency")
GuardToLongMap = Class(name="GuardToLongMap")
analysis_trace_CompressedVariableDependency = Class(name="analysis_trace_CompressedVariableDependency")
VariableToLongMap = Class(name="VariableToLongMap")
analysis_trace_CompressedPortDependency = Class(name="analysis_trace_CompressedPortDependency")
PortToLongMap = Class(name="PortToLongMap")
analysis_trace_CompressedTokensDependency = Class(name="analysis_trace_CompressedTokensDependency")
BufferToLongMap = Class(name="BufferToLongMap")
analysis_trace_TraceComparatorReport = Class(name="analysis_trace_TraceComparatorReport")
CompressedTraceReport = Class(name="CompressedTraceReport")
ComparedTrace = Class(name="ComparedTrace")
analysis_trace_ComparedTrace = Class(name="analysis_trace_ComparedTrace")
bottlenecks_analysis_Action = Class(name="bottlenecks_analysis_Action")
ComparedAction = Class(name="ComparedAction")
analysis_trace_ComparedAction = Class(name="analysis_trace_ComparedAction")
analysis_trace_MarkowModelTraceReport = Class(name="analysis_trace_MarkowModelTraceReport")
MarkovModelActionData = Class(name="MarkovModelActionData")
analysis_trace_MarkovModelActionData = Class(name="analysis_trace_MarkovModelActionData")
analysis_bottlenecks_BottlenecksReport = Class(name="analysis_bottlenecks_BottlenecksReport")
bottlenecks_analysis_Network = Class(name="bottlenecks_analysis_Network")
ActionBottlenecksData = Class(name="ActionBottlenecksData")
analysis_bottlenecks_ActionBottlenecksData = Class(name="analysis_bottlenecks_ActionBottlenecksData")
analysis_bottlenecks_ImpactAnalysisReport = Class(name="analysis_bottlenecks_ImpactAnalysisReport")
ImpactAnalysisData = Class(name="ImpactAnalysisData")
BottlenecksReport = Class(name="BottlenecksReport")
analysis_bottlenecks_ImpactAnalysisData = Class(name="analysis_bottlenecks_ImpactAnalysisData")
bottlenecks_analysis_ActorClass = Class(name="bottlenecks_analysis_ActorClass")
DoubleToDoubleMap = Class(name="DoubleToDoubleMap")
DoubleToBottlenecksReportMap = Class(name="DoubleToBottlenecksReportMap")
analysis_bottlenecks_DoubleToBottlenecksReportMap = Class(name="analysis_bottlenecks_DoubleToBottlenecksReportMap")
analysis_bottlenecks_BottlenecksWithSchedulingReport = Class(name="analysis_bottlenecks_BottlenecksWithSchedulingReport")
postprocessing_PostProcessingData = Class(name="postprocessing_PostProcessingData")
ActionBottlenecksWithSchedulingData = Class(name="ActionBottlenecksWithSchedulingData")
StringToDoubleMap = Class(name="StringToDoubleMap")
analysis_bottlenecks_ActionBottlenecksWithSchedulingData = Class(name="analysis_bottlenecks_ActionBottlenecksWithSchedulingData")
BufferToIntegerMap = Class(name="BufferToIntegerMap")
BufferToDoubleMap = Class(name="BufferToDoubleMap")
analysis_bottlenecks_ScheduledImpactAnalysisData = Class(name="analysis_bottlenecks_ScheduledImpactAnalysisData")
DoubleToBottlenecksWithSchedulingReportMap = Class(name="DoubleToBottlenecksWithSchedulingReportMap")
analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap = Class(name="analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap")
BottlenecksWithSchedulingReport = Class(name="BottlenecksWithSchedulingReport")
analysis_bottlenecks_ScheduledImpactAnalysisReport = Class(name="analysis_bottlenecks_ScheduledImpactAnalysisReport")
analysis_buffers_BoundedBuffersReport = Class(name="analysis_buffers_BoundedBuffersReport")
buffers_analysis_Network = Class(name="buffers_analysis_Network")
BoundedBufferData = Class(name="BoundedBufferData")
analysis_buffers_BoundedBufferData = Class(name="analysis_buffers_BoundedBufferData")
buffers_analysis_Buffer = Class(name="buffers_analysis_Buffer")
analysis_buffers_OptimalBuffersReport = Class(name="analysis_buffers_OptimalBuffersReport")
OptimalBufferData = Class(name="OptimalBufferData")
BoundedBuffersReport = Class(name="BoundedBuffersReport")
analysis_buffers_OptimalBufferData = Class(name="analysis_buffers_OptimalBufferData")
analysis_partitioning_ComCostPartitioningReport = Class(name="analysis_partitioning_ComCostPartitioningReport")
partitioning_analysis_Network = Class(name="partitioning_analysis_Network")
ComCostPartition = Class(name="ComCostPartition")
ScheduledImpactAnalysisData = Class(name="ScheduledImpactAnalysisData")
analysis_partitioning_WorkloadBalancePartition = Class(name="analysis_partitioning_WorkloadBalancePartition")
analysis_partitioning_WorkloadBalancePartitioningReport = Class(name="analysis_partitioning_WorkloadBalancePartitioningReport")
WorkloadBalancePartition = Class(name="WorkloadBalancePartition")
analysis_partitioning_BalancedPipelinePartition = Class(name="analysis_partitioning_BalancedPipelinePartition")
analysis_partitioning_BalancedPipelinePartitioningReport = Class(name="analysis_partitioning_BalancedPipelinePartitioningReport")
analysis_partitioning_ComCostPartition = Class(name="analysis_partitioning_ComCostPartition")
partitioning_analysis_Actor = Class(name="partitioning_analysis_Actor")
BalancedPipelinePartition = Class(name="BalancedPipelinePartition")
analysis_pipelining_ActionsVariablePipeliningReport = Class(name="analysis_pipelining_ActionsVariablePipeliningReport")
pipelining_analysis_Network = Class(name="pipelining_analysis_Network")
ActionVariablePipeliningData = Class(name="ActionVariablePipeliningData")
analysis_pipelining_ActionVariablePipeliningData = Class(name="analysis_pipelining_ActionVariablePipeliningData")
pipelining_analysis_Action = Class(name="pipelining_analysis_Action")
pipelining_analysis_StatisticalData = Class(name="pipelining_analysis_StatisticalData")
analysis_pipelining_ImpactAnalysisReport = Class(name="analysis_pipelining_ImpactAnalysisReport")
ActionsVariablePipeliningReport = Class(name="ActionsVariablePipeliningReport")
analysis_pipelining_ImpactAnalysisData = Class(name="analysis_pipelining_ImpactAnalysisData")
analysis_postprocessing_PostProcessingReport = Class(name="analysis_postprocessing_PostProcessingReport")
postprocessing_analysis_Network = Class(name="postprocessing_analysis_Network")
PostProcessingData = Class(name="PostProcessingData")
analysis_postprocessing_PostProcessingData = Class(name="analysis_postprocessing_PostProcessingData", is_abstract=True)
analysis_postprocessing_ActorStatisticsReport = Class(name="analysis_postprocessing_ActorStatisticsReport")
StatisticalActorPartition = Class(name="StatisticalActorPartition")
analysis_postprocessing_StatisticalActorPartition = Class(name="analysis_postprocessing_StatisticalActorPartition")
analysis_postprocessing_ActionStatisticsReport = Class(name="analysis_postprocessing_ActionStatisticsReport")
postprocessing_analysis_Actor = Class(name="postprocessing_analysis_Actor")
ActionToDoubleMap = Class(name="ActionToDoubleMap")
pipelining_analysis_ActorClass = Class(name="pipelining_analysis_ActorClass")
analysis_postprocessing_SchedulerChecksReport = Class(name="analysis_postprocessing_SchedulerChecksReport")
SchedulerChecksPartition = Class(name="SchedulerChecksPartition")
analysis_postprocessing_SchedulerChecksPartition = Class(name="analysis_postprocessing_SchedulerChecksPartition")
postprocessing_analysis_StatisticalData = Class(name="postprocessing_analysis_StatisticalData")
ActorToStatisticalDataMap = Class(name="ActorToStatisticalDataMap")
analysis_postprocessing_BufferBlockingReport = Class(name="analysis_postprocessing_BufferBlockingReport")
analysis_profiling_IntraActionCommunicationReport = Class(name="analysis_profiling_IntraActionCommunicationReport")
IntraActorCommunicationData = Class(name="IntraActorCommunicationData")
profiling_analysis_Network = Class(name="profiling_analysis_Network")
profiling_analysis_StatisticalData = Class(name="profiling_analysis_StatisticalData")
IntraActionCommunicationData = Class(name="IntraActionCommunicationData")
analysis_profiling_IntraActionCommunicationData = Class(name="analysis_profiling_IntraActionCommunicationData")
profiling_analysis_Action = Class(name="profiling_analysis_Action")
analysis_profiling_ProfilingStatsReport = Class(name="analysis_profiling_ProfilingStatsReport")
ProfilingStatsActorData = Class(name="ProfilingStatsActorData")
analysis_profiling_ProfilingStatsActorData = Class(name="analysis_profiling_ProfilingStatsActorData")
analysis_scheduling_ActorFire = Class(name="analysis_scheduling_ActorFire")
analysis_scheduling_FSM = Class(name="analysis_scheduling_FSM")
FSMState = Class(name="FSMState")
analysis_profiling_IntraActorCommunicationData = Class(name="analysis_profiling_IntraActorCommunicationData")
profiling_analysis_Actor = Class(name="profiling_analysis_Actor")
analysis_scheduling_ActorSelectionSchedule = Class(name="analysis_scheduling_ActorSelectionSchedule", is_abstract=True)
analysis_scheduling_Sequence = Class(name="analysis_scheduling_Sequence")
ActorFire = Class(name="ActorFire")
analysis_scheduling_FSMVar = Class(name="analysis_scheduling_FSMVar")
analysis_scheduling_FSMTransition = Class(name="analysis_scheduling_FSMTransition")
FSMCondition = Class(name="FSMCondition")
Sequence = Class(name="Sequence")
analysis_scheduling_FSMState = Class(name="analysis_scheduling_FSMState")
FSMVarUpdate = Class(name="FSMVarUpdate")
FSMTransition = Class(name="FSMTransition")
analysis_scheduling_FSMVarUpdate = Class(name="analysis_scheduling_FSMVarUpdate")
FSMOperation = Class(name="FSMOperation")
analysis_scheduling_FSMOperation = Class(name="analysis_scheduling_FSMOperation")
FSMVar = Class(name="FSMVar")
analysis_scheduling_FSMCombination = Class(name="analysis_scheduling_FSMCombination")
analysis_scheduling_FSMCondition = Class(name="analysis_scheduling_FSMCondition")
FSMCombination = Class(name="FSMCombination")
analysis_scheduling_FSMTransitionWithState = Class(name="analysis_scheduling_FSMTransitionWithState")
analysis_scheduling_PartitionedActorFire = Class(name="analysis_scheduling_PartitionedActorFire")
analysis_scheduling_MarkovSimpleSchedulerReport = Class(name="analysis_scheduling_MarkovSimpleSchedulerReport")
MarkovPartitionScheduler = Class(name="MarkovPartitionScheduler")
scheduling_analysis_Network = Class(name="scheduling_analysis_Network")
analysis_scheduling_MarkovPartitionScheduler = Class(name="analysis_scheduling_MarkovPartitionScheduler")
scheduling_analysis_Actor = Class(name="scheduling_analysis_Actor")
MarkovSchedulingState = Class(name="MarkovSchedulingState")
MarkovSchedulingTransition = Class(name="MarkovSchedulingTransition")
analysis_scheduling_MarkovSchedulingState = Class(name="analysis_scheduling_MarkovSchedulingState")
analysis_caseoptimal_CaseOptimalScheduleReport = Class(name="analysis_caseoptimal_CaseOptimalScheduleReport")
PartitionToActorSelectionScheduleMap = Class(name="PartitionToActorSelectionScheduleMap")
analysis_caseoptimal_CaseOptimalActorSelectionSchedule = Class(name="analysis_caseoptimal_CaseOptimalActorSelectionSchedule")
analysis_scheduling_MarkovSchedulingTransition = Class(name="analysis_scheduling_MarkovSchedulingTransition")

# analysis_AnalysisReport class attributes and methods
analysis_AnalysisReport_algorithm: Property = Property(name="algorithm", type=StringType)
analysis_AnalysisReport_date: Property = Property(name="date", type=DateType)
analysis_AnalysisReport.attributes={analysis_AnalysisReport_date, analysis_AnalysisReport_algorithm}

# analysis_profiler_CodeProfilingReport class attributes and methods
analysis_profiler_CodeProfilingReport_m_getActorClassData: Method = Method(name="getActorClassData", parameters={Parameter(name='analysis_actorClass', type=StringType)}, type=StringType)
analysis_profiler_CodeProfilingReport.methods={analysis_profiler_CodeProfilingReport_m_getActorClassData}

# AnalysisReport class attributes and methods

# profiler_analysis_Network class attributes and methods

# ComplexCodeData class attributes and methods

# analysis_profiler_CodeData class attributes and methods
analysis_profiler_CodeData_blockName: Property = Property(name="blockName", type=StringType)
analysis_profiler_CodeData_nol: Property = Property(name="nol", type=StringType)
analysis_profiler_CodeData.attributes={analysis_profiler_CodeData_blockName, analysis_profiler_CodeData_nol}

# StringToIntegerMap class attributes and methods

# analysis_profiler_ComplexCodeData class attributes and methods
analysis_profiler_ComplexCodeData_m_getActionData: Method = Method(name="getActionData", parameters={Parameter(name='analysis_action', type=StringType)}, type=StringType)
analysis_profiler_ComplexCodeData_m_getProcedureData: Method = Method(name="getProcedureData", parameters={Parameter(name='analysis_procedure', type=StringType)}, type=StringType)
analysis_profiler_ComplexCodeData.methods={analysis_profiler_ComplexCodeData_m_getProcedureData, analysis_profiler_ComplexCodeData_m_getActionData}

# CodeData class attributes and methods

# analysis_profiler_DynamicProfilingReport class attributes and methods

# ActorDynamicData class attributes and methods

# BufferDynamicData class attributes and methods

# analysis_profiler_ActorDynamicData class attributes and methods

# ComplexDynamicData class attributes and methods

# profiler_analysis_Actor class attributes and methods

# analysis_profiler_ActionDynamicData class attributes and methods

# profiler_analysis_Action class attributes and methods

# analysis_profiler_BufferDynamicData class attributes and methods
analysis_profiler_BufferDynamicData_unconsumedTokens: Property = Property(name="unconsumedTokens", type=IntegerType)
analysis_profiler_BufferDynamicData.attributes={analysis_profiler_BufferDynamicData_unconsumedTokens}

# profiler_analysis_Buffer class attributes and methods

# profiler_analysis_StatisticalData class attributes and methods

# ActionToStatisticalDataMap class attributes and methods

# ActionToLongMap class attributes and methods

# analysis_profiler_ComplexDynamicData class attributes and methods

# EOperatorToStatisticalDataMap class attributes and methods

# ProcedureToStatisticalDataMap class attributes and methods

# VariableToStatisticalDataMap class attributes and methods

# ProcedureToComplexDynamicDataMap class attributes and methods

# BufferToStatisticalDataMap class attributes and methods

# analysis_profiler_ProcedureToComplexDynamicDataMap class attributes and methods

# ActionDynamicData class attributes and methods

# analysis_profiler_MemoryProfilingReport class attributes and methods
analysis_profiler_MemoryProfilingReport_networkName: Property = Property(name="networkName", type=StringType)
analysis_profiler_MemoryProfilingReport_m_getActionData: Method = Method(name="getActionData", parameters={Parameter(name='analysis_action', type=StringType), Parameter(name='analysis_actor', type=StringType)}, type=StringType)
analysis_profiler_MemoryProfilingReport.attributes={analysis_profiler_MemoryProfilingReport_networkName}
analysis_profiler_MemoryProfilingReport.methods={analysis_profiler_MemoryProfilingReport_m_getActionData}

# ActionMemoryProfilingData class attributes and methods

# analysis_profiler_ActionMemoryProfilingData class attributes and methods
analysis_profiler_ActionMemoryProfilingData_actor: Property = Property(name="actor", type=StringType)
analysis_profiler_ActionMemoryProfilingData_action: Property = Property(name="action", type=StringType)
analysis_profiler_ActionMemoryProfilingData_m_getReadBufferData: Method = Method(name="getReadBufferData", parameters={Parameter(name='analysis_sourceActor', type=StringType), Parameter(name='analysis_targetPort', type=StringType), Parameter(name='analysis_sourcePort', type=StringType), Parameter(name='analysis_targetActor', type=StringType)}, type=StringType)
analysis_profiler_ActionMemoryProfilingData_m_getWriteBufferData: Method = Method(name="getWriteBufferData", parameters={Parameter(name='analysis_targetActor', type=StringType), Parameter(name='analysis_sourceActor', type=StringType), Parameter(name='analysis_sourcePort', type=StringType), Parameter(name='analysis_targetPort', type=StringType)}, type=StringType)
analysis_profiler_ActionMemoryProfilingData_m_getReadStateVariableData: Method = Method(name="getReadStateVariableData", parameters={Parameter(name='analysis_variable', type=StringType)}, type=StringType)
analysis_profiler_ActionMemoryProfilingData_m_getWriteStateVariableData: Method = Method(name="getWriteStateVariableData", parameters={Parameter(name='analysis_variable', type=StringType)}, type=StringType)
analysis_profiler_ActionMemoryProfilingData_m_getReadLocalVariableData: Method = Method(name="getReadLocalVariableData", parameters={Parameter(name='analysis_variable', type=StringType)}, type=StringType)
analysis_profiler_ActionMemoryProfilingData_m_getWriteLocalVariableData: Method = Method(name="getWriteLocalVariableData", parameters={Parameter(name='analysis_variable', type=StringType)}, type=StringType)
analysis_profiler_ActionMemoryProfilingData_m_getReadSharedVariableData: Method = Method(name="getReadSharedVariableData", parameters={Parameter(name='analysis_variable', type=StringType)}, type=StringType)
analysis_profiler_ActionMemoryProfilingData_m_getWriteSharedVariableData: Method = Method(name="getWriteSharedVariableData", parameters={Parameter(name='analysis_variable', type=StringType)}, type=StringType)
analysis_profiler_ActionMemoryProfilingData.attributes={analysis_profiler_ActionMemoryProfilingData_actor, analysis_profiler_ActionMemoryProfilingData_action}
analysis_profiler_ActionMemoryProfilingData.methods={analysis_profiler_ActionMemoryProfilingData_m_getWriteBufferData, analysis_profiler_ActionMemoryProfilingData_m_getReadStateVariableData, analysis_profiler_ActionMemoryProfilingData_m_getWriteStateVariableData, analysis_profiler_ActionMemoryProfilingData_m_getReadBufferData, analysis_profiler_ActionMemoryProfilingData_m_getWriteSharedVariableData, analysis_profiler_ActionMemoryProfilingData_m_getReadSharedVariableData, analysis_profiler_ActionMemoryProfilingData_m_getReadLocalVariableData, analysis_profiler_ActionMemoryProfilingData_m_getWriteLocalVariableData}

# MemoryAccessData class attributes and methods

# analysis_profiler_MemoryAccessData class attributes and methods

# StringToAccessDataMap class attributes and methods

# analysis_profiler_BufferAccessData class attributes and methods
analysis_profiler_BufferAccessData_sourceActor: Property = Property(name="sourceActor", type=StringType)
analysis_profiler_BufferAccessData_sourcePort: Property = Property(name="sourcePort", type=StringType)
analysis_profiler_BufferAccessData_targetActor: Property = Property(name="targetActor", type=StringType)
analysis_profiler_BufferAccessData_targetPort: Property = Property(name="targetPort", type=StringType)
analysis_profiler_BufferAccessData.attributes={analysis_profiler_BufferAccessData_targetPort, analysis_profiler_BufferAccessData_targetActor, analysis_profiler_BufferAccessData_sourcePort, analysis_profiler_BufferAccessData_sourceActor}

# profiler_analysis_Procedure class attributes and methods

# analysis_profiler_SharedVariableAccessData class attributes and methods
analysis_profiler_SharedVariableAccessData_name: Property = Property(name="name", type=StringType)
analysis_profiler_SharedVariableAccessData.attributes={analysis_profiler_SharedVariableAccessData_name}

# analysis_profiler_AccessData class attributes and methods
analysis_profiler_AccessData_accesses: Property = Property(name="accesses", type=FloatType)
analysis_profiler_AccessData_min: Property = Property(name="min", type=FloatType)
analysis_profiler_AccessData_max: Property = Property(name="max", type=FloatType)
analysis_profiler_AccessData_average: Property = Property(name="average", type=FloatType)
analysis_profiler_AccessData_total: Property = Property(name="total", type=FloatType)
analysis_profiler_AccessData.attributes={analysis_profiler_AccessData_accesses, analysis_profiler_AccessData_total, analysis_profiler_AccessData_max, analysis_profiler_AccessData_average, analysis_profiler_AccessData_min}

# analysis_profiler_StringToAccessDataMap class attributes and methods
analysis_profiler_StringToAccessDataMap_key: Property = Property(name="key", type=StringType)
analysis_profiler_StringToAccessDataMap.attributes={analysis_profiler_StringToAccessDataMap_key}

# AccessData class attributes and methods

# analysis_profiler_BenchmarkReport class attributes and methods
analysis_profiler_BenchmarkReport_column_names: Property = Property(name="column_names", type=StringType)
analysis_profiler_BenchmarkReport.attributes={analysis_profiler_BenchmarkReport_column_names}

# TableRow class attributes and methods

# analysis_profiler_TableRow class attributes and methods

# StringToStringMap class attributes and methods

# analysis_map_StringToIntegerMap class attributes and methods
analysis_map_StringToIntegerMap_key: Property = Property(name="key", type=StringType)
analysis_map_StringToIntegerMap_value: Property = Property(name="value", type=StringType)
analysis_map_StringToIntegerMap.attributes={analysis_map_StringToIntegerMap_key, analysis_map_StringToIntegerMap_value}

# analysis_map_ActorToStatisticalDataMap class attributes and methods

# map_analysis_Actor class attributes and methods

# map_analysis_StatisticalData class attributes and methods

# analysis_map_ActionToStatisticalDataMap class attributes and methods

# map_analysis_Action class attributes and methods

# analysis_map_BufferToStatisticalDataMap class attributes and methods

# map_analysis_Buffer class attributes and methods

# analysis_map_ProcedureToStatisticalDataMap class attributes and methods

# analysis_profiler_StateVariableAccessData class attributes and methods
analysis_profiler_StateVariableAccessData_name: Property = Property(name="name", type=StringType)
analysis_profiler_StateVariableAccessData.attributes={analysis_profiler_StateVariableAccessData_name}

# analysis_profiler_LocalVariableAccessData class attributes and methods
analysis_profiler_LocalVariableAccessData_name: Property = Property(name="name", type=StringType)
analysis_profiler_LocalVariableAccessData.attributes={analysis_profiler_LocalVariableAccessData_name}

# analysis_map_VariableToStatisticalDataMap class attributes and methods

# map_analysis_Variable class attributes and methods

# analysis_map_ActorClassToStatisticalDataMap class attributes and methods

# map_analysis_ActorClass class attributes and methods

# analysis_map_EOperatorToStatisticalDataMap class attributes and methods
analysis_map_EOperatorToStatisticalDataMap_key: Property = Property(name="key", type=StringType)
analysis_map_EOperatorToStatisticalDataMap.attributes={analysis_map_EOperatorToStatisticalDataMap_key}

# analysis_map_ActionToLongMap class attributes and methods
analysis_map_ActionToLongMap_value: Property = Property(name="value", type=StringType)
analysis_map_ActionToLongMap.attributes={analysis_map_ActionToLongMap_value}

# analysis_map_ActorToLongMap class attributes and methods
analysis_map_ActorToLongMap_value: Property = Property(name="value", type=StringType)
analysis_map_ActorToLongMap.attributes={analysis_map_ActorToLongMap_value}

# analysis_map_BufferToLongMap class attributes and methods
analysis_map_BufferToLongMap_value: Property = Property(name="value", type=StringType)
analysis_map_BufferToLongMap.attributes={analysis_map_BufferToLongMap_value}

# analysis_map_StringToLongMap class attributes and methods
analysis_map_StringToLongMap_key: Property = Property(name="key", type=StringType)
analysis_map_StringToLongMap_value: Property = Property(name="value", type=StringType)
analysis_map_StringToLongMap.attributes={analysis_map_StringToLongMap_value, analysis_map_StringToLongMap_key}

# analysis_map_DoubleToDoubleMap class attributes and methods
analysis_map_DoubleToDoubleMap_key: Property = Property(name="key", type=StringType)
analysis_map_DoubleToDoubleMap_value: Property = Property(name="value", type=StringType)
analysis_map_DoubleToDoubleMap.attributes={analysis_map_DoubleToDoubleMap_value, analysis_map_DoubleToDoubleMap_key}

# analysis_map_VariableToLongMap class attributes and methods
analysis_map_VariableToLongMap_value: Property = Property(name="value", type=StringType)
analysis_map_VariableToLongMap.attributes={analysis_map_VariableToLongMap_value}

# analysis_map_GuardToLongMap class attributes and methods
analysis_map_GuardToLongMap_value: Property = Property(name="value", type=StringType)
analysis_map_GuardToLongMap.attributes={analysis_map_GuardToLongMap_value}

# map_analysis_Guard class attributes and methods

# analysis_map_PortToLongMap class attributes and methods
analysis_map_PortToLongMap_value: Property = Property(name="value", type=StringType)
analysis_map_PortToLongMap.attributes={analysis_map_PortToLongMap_value}

# map_analysis_Port class attributes and methods

# analysis_map_StringToDoubleMap class attributes and methods
analysis_map_StringToDoubleMap_key: Property = Property(name="key", type=StringType)
analysis_map_StringToDoubleMap_value: Property = Property(name="value", type=StringType)
analysis_map_StringToDoubleMap.attributes={analysis_map_StringToDoubleMap_key, analysis_map_StringToDoubleMap_value}

# map_analysis_Procedure class attributes and methods

# analysis_map_BufferToIntegerMap class attributes and methods
analysis_map_BufferToIntegerMap_value: Property = Property(name="value", type=StringType)
analysis_map_BufferToIntegerMap.attributes={analysis_map_BufferToIntegerMap_value}

# analysis_map_BufferToDoubleMap class attributes and methods
analysis_map_BufferToDoubleMap_value: Property = Property(name="value", type=StringType)
analysis_map_BufferToDoubleMap.attributes={analysis_map_BufferToDoubleMap_value}

# analysis_map_PartitionToActorSelectionScheduleMap class attributes and methods
analysis_map_PartitionToActorSelectionScheduleMap_key: Property = Property(name="key", type=StringType)
analysis_map_PartitionToActorSelectionScheduleMap.attributes={analysis_map_PartitionToActorSelectionScheduleMap_key}

# ActorSelectionSchedule class attributes and methods

# analysis_map_StringToStringMap class attributes and methods
analysis_map_StringToStringMap_key: Property = Property(name="key", type=StringType)
analysis_map_StringToStringMap_value: Property = Property(name="value", type=StringType)
analysis_map_StringToStringMap.attributes={analysis_map_StringToStringMap_value, analysis_map_StringToStringMap_key}

# analysis_trace_TraceSizeReport class attributes and methods
analysis_trace_TraceSizeReport_firings: Property = Property(name="firings", type=StringType)
analysis_trace_TraceSizeReport_dependencies: Property = Property(name="dependencies", type=StringType)
analysis_trace_TraceSizeReport.attributes={analysis_trace_TraceSizeReport_dependencies, analysis_trace_TraceSizeReport_firings}

# ActorToLongMap class attributes and methods

# analysis_map_ActionToDoubleMap class attributes and methods
analysis_map_ActionToDoubleMap_value: Property = Property(name="value", type=StringType)
analysis_map_ActionToDoubleMap.attributes={analysis_map_ActionToDoubleMap_value}

# StringToLongMap class attributes and methods

# trace_analysis_Network class attributes and methods

# analysis_trace_CompressedTraceReport class attributes and methods
analysis_trace_CompressedTraceReport_traceFile: Property = Property(name="traceFile", type=StringType)
analysis_trace_CompressedTraceReport_m_getSteps: Method = Method(name="getSteps", parameters={Parameter(name='analysis_action', type=StringType)}, type=StringType)
analysis_trace_CompressedTraceReport_m_getSteps: Method = Method(name="getSteps", parameters={Parameter(name='analysis_actor', type=StringType)}, type=StringType)
analysis_trace_CompressedTraceReport.attributes={analysis_trace_CompressedTraceReport_traceFile}
analysis_trace_CompressedTraceReport.methods={analysis_trace_CompressedTraceReport_m_getSteps, analysis_trace_CompressedTraceReport_m_getSteps}

# CompressedStep class attributes and methods

# CompressedDependency class attributes and methods

# analysis_trace_CompressedStep class attributes and methods
analysis_trace_CompressedStep_count: Property = Property(name="count", type=StringType)
analysis_trace_CompressedStep.attributes={analysis_trace_CompressedStep_count}

# trace_analysis_Action class attributes and methods

# analysis_trace_CompressedDependency class attributes and methods
analysis_trace_CompressedDependency_count: Property = Property(name="count", type=StringType)
analysis_trace_CompressedDependency.attributes={analysis_trace_CompressedDependency_count}

# analysis_trace_CompressedFsmDependency class attributes and methods

# analysis_trace_CompressedGuardDependency class attributes and methods

# GuardToLongMap class attributes and methods

# analysis_trace_CompressedVariableDependency class attributes and methods

# VariableToLongMap class attributes and methods

# analysis_trace_CompressedPortDependency class attributes and methods

# PortToLongMap class attributes and methods

# analysis_trace_CompressedTokensDependency class attributes and methods

# BufferToLongMap class attributes and methods

# analysis_trace_TraceComparatorReport class attributes and methods

# CompressedTraceReport class attributes and methods

# ComparedTrace class attributes and methods

# analysis_trace_ComparedTrace class attributes and methods
analysis_trace_ComparedTrace_dDependencies: Property = Property(name="dDependencies", type=StringType)
analysis_trace_ComparedTrace_dSteps: Property = Property(name="dSteps", type=StringType)
analysis_trace_ComparedTrace_equal: Property = Property(name="equal", type=BooleanType)
analysis_trace_ComparedTrace.attributes={analysis_trace_ComparedTrace_dSteps, analysis_trace_ComparedTrace_equal, analysis_trace_ComparedTrace_dDependencies}

# bottlenecks_analysis_Action class attributes and methods

# ComparedAction class attributes and methods

# analysis_trace_ComparedAction class attributes and methods
analysis_trace_ComparedAction_found: Property = Property(name="found", type=BooleanType)
analysis_trace_ComparedAction_dSteps: Property = Property(name="dSteps", type=StringType)
analysis_trace_ComparedAction_dIncomings: Property = Property(name="dIncomings", type=StringType)
analysis_trace_ComparedAction_dOutgoings: Property = Property(name="dOutgoings", type=StringType)
analysis_trace_ComparedAction.attributes={analysis_trace_ComparedAction_dOutgoings, analysis_trace_ComparedAction_found, analysis_trace_ComparedAction_dIncomings, analysis_trace_ComparedAction_dSteps}

# analysis_trace_MarkowModelTraceReport class attributes and methods
analysis_trace_MarkowModelTraceReport_m_getData: Method = Method(name="getData", parameters={Parameter(name='analysis_actor', type=StringType)}, type=StringType)
analysis_trace_MarkowModelTraceReport_m_getData: Method = Method(name="getData", parameters={Parameter(name='analysis_action', type=StringType)}, type=StringType)
analysis_trace_MarkowModelTraceReport.methods={analysis_trace_MarkowModelTraceReport_m_getData, analysis_trace_MarkowModelTraceReport_m_getData}

# MarkovModelActionData class attributes and methods

# analysis_trace_MarkovModelActionData class attributes and methods
analysis_trace_MarkovModelActionData_first: Property = Property(name="first", type=BooleanType)
analysis_trace_MarkovModelActionData_successors: Property = Property(name="successors", type=StringType)
analysis_trace_MarkovModelActionData.attributes={analysis_trace_MarkovModelActionData_first, analysis_trace_MarkovModelActionData_successors}

# analysis_bottlenecks_BottlenecksReport class attributes and methods
analysis_bottlenecks_BottlenecksReport_cpWeight: Property = Property(name="cpWeight", type=FloatType)
analysis_bottlenecks_BottlenecksReport_cpVariance: Property = Property(name="cpVariance", type=FloatType)
analysis_bottlenecks_BottlenecksReport_totalWeight: Property = Property(name="totalWeight", type=FloatType)
analysis_bottlenecks_BottlenecksReport_totalVariance: Property = Property(name="totalVariance", type=FloatType)
analysis_bottlenecks_BottlenecksReport_cpFirings: Property = Property(name="cpFirings", type=StringType)
analysis_bottlenecks_BottlenecksReport_totalFirings: Property = Property(name="totalFirings", type=StringType)
analysis_bottlenecks_BottlenecksReport.attributes={analysis_bottlenecks_BottlenecksReport_totalVariance, analysis_bottlenecks_BottlenecksReport_cpVariance, analysis_bottlenecks_BottlenecksReport_totalFirings, analysis_bottlenecks_BottlenecksReport_cpWeight, analysis_bottlenecks_BottlenecksReport_cpFirings, analysis_bottlenecks_BottlenecksReport_totalWeight}

# bottlenecks_analysis_Network class attributes and methods

# ActionBottlenecksData class attributes and methods

# analysis_bottlenecks_ActionBottlenecksData class attributes and methods
analysis_bottlenecks_ActionBottlenecksData_slackMin: Property = Property(name="slackMin", type=FloatType)
analysis_bottlenecks_ActionBottlenecksData_slackMax: Property = Property(name="slackMax", type=FloatType)
analysis_bottlenecks_ActionBottlenecksData_cpWeight: Property = Property(name="cpWeight", type=FloatType)
analysis_bottlenecks_ActionBottlenecksData_cpVariance: Property = Property(name="cpVariance", type=FloatType)
analysis_bottlenecks_ActionBottlenecksData_totalWeight: Property = Property(name="totalWeight", type=FloatType)
analysis_bottlenecks_ActionBottlenecksData_totalVariance: Property = Property(name="totalVariance", type=FloatType)
analysis_bottlenecks_ActionBottlenecksData_cpFirings: Property = Property(name="cpFirings", type=StringType)
analysis_bottlenecks_ActionBottlenecksData_totalFirings: Property = Property(name="totalFirings", type=StringType)
analysis_bottlenecks_ActionBottlenecksData.attributes={analysis_bottlenecks_ActionBottlenecksData_slackMin, analysis_bottlenecks_ActionBottlenecksData_totalVariance, analysis_bottlenecks_ActionBottlenecksData_cpFirings, analysis_bottlenecks_ActionBottlenecksData_slackMax, analysis_bottlenecks_ActionBottlenecksData_totalWeight, analysis_bottlenecks_ActionBottlenecksData_totalFirings, analysis_bottlenecks_ActionBottlenecksData_cpVariance, analysis_bottlenecks_ActionBottlenecksData_cpWeight}

# analysis_bottlenecks_ImpactAnalysisReport class attributes and methods
analysis_bottlenecks_ImpactAnalysisReport_classLevel: Property = Property(name="classLevel", type=BooleanType)
analysis_bottlenecks_ImpactAnalysisReport.attributes={analysis_bottlenecks_ImpactAnalysisReport_classLevel}

# ImpactAnalysisData class attributes and methods

# BottlenecksReport class attributes and methods

# analysis_bottlenecks_ImpactAnalysisData class attributes and methods

# bottlenecks_analysis_ActorClass class attributes and methods

# DoubleToDoubleMap class attributes and methods

# DoubleToBottlenecksReportMap class attributes and methods

# analysis_bottlenecks_DoubleToBottlenecksReportMap class attributes and methods
analysis_bottlenecks_DoubleToBottlenecksReportMap_key: Property = Property(name="key", type=StringType)
analysis_bottlenecks_DoubleToBottlenecksReportMap.attributes={analysis_bottlenecks_DoubleToBottlenecksReportMap_key}

# analysis_bottlenecks_BottlenecksWithSchedulingReport class attributes and methods
analysis_bottlenecks_BottlenecksWithSchedulingReport_totalFirings: Property = Property(name="totalFirings", type=StringType)
analysis_bottlenecks_BottlenecksWithSchedulingReport_cpWeight: Property = Property(name="cpWeight", type=FloatType)
analysis_bottlenecks_BottlenecksWithSchedulingReport_totalWeight: Property = Property(name="totalWeight", type=FloatType)
analysis_bottlenecks_BottlenecksWithSchedulingReport_cpFirings: Property = Property(name="cpFirings", type=StringType)
analysis_bottlenecks_BottlenecksWithSchedulingReport_executionTime: Property = Property(name="executionTime", type=FloatType)
analysis_bottlenecks_BottlenecksWithSchedulingReport_cpBlockingTime: Property = Property(name="cpBlockingTime", type=FloatType)
analysis_bottlenecks_BottlenecksWithSchedulingReport.attributes={analysis_bottlenecks_BottlenecksWithSchedulingReport_cpBlockingTime, analysis_bottlenecks_BottlenecksWithSchedulingReport_totalFirings, analysis_bottlenecks_BottlenecksWithSchedulingReport_cpWeight, analysis_bottlenecks_BottlenecksWithSchedulingReport_cpFirings, analysis_bottlenecks_BottlenecksWithSchedulingReport_totalWeight, analysis_bottlenecks_BottlenecksWithSchedulingReport_executionTime}

# postprocessing_PostProcessingData class attributes and methods

# ActionBottlenecksWithSchedulingData class attributes and methods

# StringToDoubleMap class attributes and methods

# analysis_bottlenecks_ActionBottlenecksWithSchedulingData class attributes and methods
analysis_bottlenecks_ActionBottlenecksWithSchedulingData_cpWeight: Property = Property(name="cpWeight", type=FloatType)
analysis_bottlenecks_ActionBottlenecksWithSchedulingData_totalWeight: Property = Property(name="totalWeight", type=FloatType)
analysis_bottlenecks_ActionBottlenecksWithSchedulingData_cpFirings: Property = Property(name="cpFirings", type=StringType)
analysis_bottlenecks_ActionBottlenecksWithSchedulingData_totalFirings: Property = Property(name="totalFirings", type=StringType)
analysis_bottlenecks_ActionBottlenecksWithSchedulingData.attributes={analysis_bottlenecks_ActionBottlenecksWithSchedulingData_totalFirings, analysis_bottlenecks_ActionBottlenecksWithSchedulingData_cpWeight, analysis_bottlenecks_ActionBottlenecksWithSchedulingData_cpFirings, analysis_bottlenecks_ActionBottlenecksWithSchedulingData_totalWeight}

# BufferToIntegerMap class attributes and methods

# BufferToDoubleMap class attributes and methods

# analysis_bottlenecks_ScheduledImpactAnalysisData class attributes and methods

# DoubleToBottlenecksWithSchedulingReportMap class attributes and methods

# analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap class attributes and methods
analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap_key: Property = Property(name="key", type=StringType)
analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap.attributes={analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap_key}

# BottlenecksWithSchedulingReport class attributes and methods

# analysis_bottlenecks_ScheduledImpactAnalysisReport class attributes and methods
analysis_bottlenecks_ScheduledImpactAnalysisReport_classLevel: Property = Property(name="classLevel", type=BooleanType)
analysis_bottlenecks_ScheduledImpactAnalysisReport.attributes={analysis_bottlenecks_ScheduledImpactAnalysisReport_classLevel}

# analysis_buffers_BoundedBuffersReport class attributes and methods
analysis_buffers_BoundedBuffersReport_pow2: Property = Property(name="pow2", type=BooleanType)
analysis_buffers_BoundedBuffersReport_bitAccurate: Property = Property(name="bitAccurate", type=BooleanType)
analysis_buffers_BoundedBuffersReport_tokenSize: Property = Property(name="tokenSize", type=IntegerType)
analysis_buffers_BoundedBuffersReport_bitSize: Property = Property(name="bitSize", type=IntegerType)
analysis_buffers_BoundedBuffersReport.attributes={analysis_buffers_BoundedBuffersReport_bitSize, analysis_buffers_BoundedBuffersReport_pow2, analysis_buffers_BoundedBuffersReport_bitAccurate, analysis_buffers_BoundedBuffersReport_tokenSize}

# buffers_analysis_Network class attributes and methods

# BoundedBufferData class attributes and methods

# analysis_buffers_BoundedBufferData class attributes and methods
analysis_buffers_BoundedBufferData_tokenSize: Property = Property(name="tokenSize", type=IntegerType)
analysis_buffers_BoundedBufferData_bitSize: Property = Property(name="bitSize", type=IntegerType)
analysis_buffers_BoundedBufferData.attributes={analysis_buffers_BoundedBufferData_tokenSize, analysis_buffers_BoundedBufferData_bitSize}

# buffers_analysis_Buffer class attributes and methods

# analysis_buffers_OptimalBuffersReport class attributes and methods
analysis_buffers_OptimalBuffersReport_pow2: Property = Property(name="pow2", type=BooleanType)
analysis_buffers_OptimalBuffersReport_bitAccurate: Property = Property(name="bitAccurate", type=BooleanType)
analysis_buffers_OptimalBuffersReport.attributes={analysis_buffers_OptimalBuffersReport_bitAccurate, analysis_buffers_OptimalBuffersReport_pow2}

# OptimalBufferData class attributes and methods

# BoundedBuffersReport class attributes and methods

# analysis_buffers_OptimalBufferData class attributes and methods

# analysis_partitioning_ComCostPartitioningReport class attributes and methods
analysis_partitioning_ComCostPartitioningReport_bitAccurate: Property = Property(name="bitAccurate", type=BooleanType)
analysis_partitioning_ComCostPartitioningReport.attributes={analysis_partitioning_ComCostPartitioningReport_bitAccurate}

# partitioning_analysis_Network class attributes and methods

# ComCostPartition class attributes and methods

# ScheduledImpactAnalysisData class attributes and methods

# analysis_partitioning_WorkloadBalancePartition class attributes and methods
analysis_partitioning_WorkloadBalancePartition_workload: Property = Property(name="workload", type=FloatType)
analysis_partitioning_WorkloadBalancePartition.attributes={analysis_partitioning_WorkloadBalancePartition_workload}

# analysis_partitioning_WorkloadBalancePartitioningReport class attributes and methods

# WorkloadBalancePartition class attributes and methods

# analysis_partitioning_BalancedPipelinePartition class attributes and methods
analysis_partitioning_BalancedPipelinePartition_workload: Property = Property(name="workload", type=FloatType)
analysis_partitioning_BalancedPipelinePartition_preWorkload: Property = Property(name="preWorkload", type=FloatType)
analysis_partitioning_BalancedPipelinePartition_commonPredAvg: Property = Property(name="commonPredAvg", type=FloatType)
analysis_partitioning_BalancedPipelinePartition.attributes={analysis_partitioning_BalancedPipelinePartition_workload, analysis_partitioning_BalancedPipelinePartition_commonPredAvg, analysis_partitioning_BalancedPipelinePartition_preWorkload}

# analysis_partitioning_BalancedPipelinePartitioningReport class attributes and methods

# analysis_partitioning_ComCostPartition class attributes and methods
analysis_partitioning_ComCostPartition_internalCost: Property = Property(name="internalCost", type=StringType)
analysis_partitioning_ComCostPartition_externalCost: Property = Property(name="externalCost", type=StringType)
analysis_partitioning_ComCostPartition.attributes={analysis_partitioning_ComCostPartition_internalCost, analysis_partitioning_ComCostPartition_externalCost}

# partitioning_analysis_Actor class attributes and methods

# BalancedPipelinePartition class attributes and methods

# analysis_pipelining_ActionsVariablePipeliningReport class attributes and methods

# pipelining_analysis_Network class attributes and methods

# ActionVariablePipeliningData class attributes and methods

# analysis_pipelining_ActionVariablePipeliningData class attributes and methods
analysis_pipelining_ActionVariablePipeliningData_pipelinable: Property = Property(name="pipelinable", type=BooleanType)
analysis_pipelining_ActionVariablePipeliningData.attributes={analysis_pipelining_ActionVariablePipeliningData_pipelinable}

# pipelining_analysis_Action class attributes and methods

# pipelining_analysis_StatisticalData class attributes and methods

# analysis_pipelining_ImpactAnalysisReport class attributes and methods

# ActionsVariablePipeliningReport class attributes and methods

# analysis_pipelining_ImpactAnalysisData class attributes and methods
analysis_pipelining_ImpactAnalysisData_cpReduction: Property = Property(name="cpReduction", type=FloatType)
analysis_pipelining_ImpactAnalysisData.attributes={analysis_pipelining_ImpactAnalysisData_cpReduction}

# analysis_postprocessing_PostProcessingReport class attributes and methods
analysis_postprocessing_PostProcessingReport_time: Property = Property(name="time", type=FloatType)
analysis_postprocessing_PostProcessingReport_deadlock: Property = Property(name="deadlock", type=BooleanType)
analysis_postprocessing_PostProcessingReport.attributes={analysis_postprocessing_PostProcessingReport_deadlock, analysis_postprocessing_PostProcessingReport_time}

# postprocessing_analysis_Network class attributes and methods

# PostProcessingData class attributes and methods

# analysis_postprocessing_PostProcessingData class attributes and methods

# analysis_postprocessing_ActorStatisticsReport class attributes and methods
analysis_postprocessing_ActorStatisticsReport_executionTime: Property = Property(name="executionTime", type=FloatType)
analysis_postprocessing_ActorStatisticsReport_averageOccupancy: Property = Property(name="averageOccupancy", type=FloatType)
analysis_postprocessing_ActorStatisticsReport_occupancyDeviation: Property = Property(name="occupancyDeviation", type=FloatType)
analysis_postprocessing_ActorStatisticsReport.attributes={analysis_postprocessing_ActorStatisticsReport_executionTime, analysis_postprocessing_ActorStatisticsReport_averageOccupancy, analysis_postprocessing_ActorStatisticsReport_occupancyDeviation}

# StatisticalActorPartition class attributes and methods

# analysis_postprocessing_StatisticalActorPartition class attributes and methods
analysis_postprocessing_StatisticalActorPartition_actors: Property = Property(name="actors", type=StringType)
analysis_postprocessing_StatisticalActorPartition_occupancy: Property = Property(name="occupancy", type=FloatType)
analysis_postprocessing_StatisticalActorPartition_schedulingPolicy: Property = Property(name="schedulingPolicy", type=StringType)
analysis_postprocessing_StatisticalActorPartition.attributes={analysis_postprocessing_StatisticalActorPartition_actors, analysis_postprocessing_StatisticalActorPartition_schedulingPolicy, analysis_postprocessing_StatisticalActorPartition_occupancy}

# analysis_postprocessing_ActionStatisticsReport class attributes and methods

# postprocessing_analysis_Actor class attributes and methods

# ActionToDoubleMap class attributes and methods

# pipelining_analysis_ActorClass class attributes and methods

# analysis_postprocessing_SchedulerChecksReport class attributes and methods

# SchedulerChecksPartition class attributes and methods

# analysis_postprocessing_SchedulerChecksPartition class attributes and methods

# postprocessing_analysis_StatisticalData class attributes and methods

# ActorToStatisticalDataMap class attributes and methods

# analysis_postprocessing_BufferBlockingReport class attributes and methods

# analysis_profiling_IntraActionCommunicationReport class attributes and methods

# IntraActorCommunicationData class attributes and methods

# profiling_analysis_Network class attributes and methods

# profiling_analysis_StatisticalData class attributes and methods

# IntraActionCommunicationData class attributes and methods

# analysis_profiling_IntraActionCommunicationData class attributes and methods

# profiling_analysis_Action class attributes and methods

# analysis_profiling_ProfilingStatsReport class attributes and methods
analysis_profiling_ProfilingStatsReport_networkName: Property = Property(name="networkName", type=StringType)
analysis_profiling_ProfilingStatsReport.attributes={analysis_profiling_ProfilingStatsReport_networkName}

# ProfilingStatsActorData class attributes and methods

# analysis_profiling_ProfilingStatsActorData class attributes and methods
analysis_profiling_ProfilingStatsActorData_actorName: Property = Property(name="actorName", type=StringType)
analysis_profiling_ProfilingStatsActorData_actionsWeight: Property = Property(name="actionsWeight", type=FloatType)
analysis_profiling_ProfilingStatsActorData_schedulerWeight: Property = Property(name="schedulerWeight", type=FloatType)
analysis_profiling_ProfilingStatsActorData_actionsWeightPercent: Property = Property(name="actionsWeightPercent", type=FloatType)
analysis_profiling_ProfilingStatsActorData_schedulerWeightPercent: Property = Property(name="schedulerWeightPercent", type=FloatType)
analysis_profiling_ProfilingStatsActorData.attributes={analysis_profiling_ProfilingStatsActorData_actorName, analysis_profiling_ProfilingStatsActorData_actionsWeight, analysis_profiling_ProfilingStatsActorData_schedulerWeightPercent, analysis_profiling_ProfilingStatsActorData_schedulerWeight, analysis_profiling_ProfilingStatsActorData_actionsWeightPercent}

# analysis_scheduling_ActorFire class attributes and methods
analysis_scheduling_ActorFire_Actor: Property = Property(name="Actor", type=StringType)
analysis_scheduling_ActorFire_Times: Property = Property(name="Times", type=IntegerType)
analysis_scheduling_ActorFire_partition: Property = Property(name="partition", type=StringType)
analysis_scheduling_ActorFire_dependencyPartitions: Property = Property(name="dependencyPartitions", type=StringType)
analysis_scheduling_ActorFire.attributes={analysis_scheduling_ActorFire_Actor, analysis_scheduling_ActorFire_dependencyPartitions, analysis_scheduling_ActorFire_Times, analysis_scheduling_ActorFire_partition}

# analysis_scheduling_FSM class attributes and methods
analysis_scheduling_FSM_startState: Property = Property(name="startState", type=StringType)
analysis_scheduling_FSM_terminalState: Property = Property(name="terminalState", type=StringType)
analysis_scheduling_FSM.attributes={analysis_scheduling_FSM_startState, analysis_scheduling_FSM_terminalState}

# FSMState class attributes and methods

# analysis_profiling_IntraActorCommunicationData class attributes and methods

# profiling_analysis_Actor class attributes and methods

# analysis_scheduling_ActorSelectionSchedule class attributes and methods

# analysis_scheduling_Sequence class attributes and methods

# ActorFire class attributes and methods

# analysis_scheduling_FSMVar class attributes and methods
analysis_scheduling_FSMVar_name: Property = Property(name="name", type=StringType)
analysis_scheduling_FSMVar_initialVal: Property = Property(name="initialVal", type=StringType)
analysis_scheduling_FSMVar_type: Property = Property(name="type", type=StringType)
analysis_scheduling_FSMVar.attributes={analysis_scheduling_FSMVar_name, analysis_scheduling_FSMVar_type, analysis_scheduling_FSMVar_initialVal}

# analysis_scheduling_FSMTransition class attributes and methods
analysis_scheduling_FSMTransition_targetStateEnumName: Property = Property(name="targetStateEnumName", type=StringType)
analysis_scheduling_FSMTransition_sourceStateEnumName: Property = Property(name="sourceStateEnumName", type=StringType)
analysis_scheduling_FSMTransition.attributes={analysis_scheduling_FSMTransition_sourceStateEnumName, analysis_scheduling_FSMTransition_targetStateEnumName}

# FSMCondition class attributes and methods

# Sequence class attributes and methods

# analysis_scheduling_FSMState class attributes and methods
analysis_scheduling_FSMState_enumName: Property = Property(name="enumName", type=StringType)
analysis_scheduling_FSMState.attributes={analysis_scheduling_FSMState_enumName}

# FSMVarUpdate class attributes and methods

# FSMTransition class attributes and methods

# analysis_scheduling_FSMVarUpdate class attributes and methods

# FSMOperation class attributes and methods

# analysis_scheduling_FSMOperation class attributes and methods
analysis_scheduling_FSMOperation_op: Property = Property(name="op", type=StringType)
analysis_scheduling_FSMOperation_val: Property = Property(name="val", type=StringType)
analysis_scheduling_FSMOperation_var: Property = Property(name="var", type=StringType)
analysis_scheduling_FSMOperation.attributes={analysis_scheduling_FSMOperation_val, analysis_scheduling_FSMOperation_op, analysis_scheduling_FSMOperation_var}

# FSMVar class attributes and methods

# analysis_scheduling_FSMCombination class attributes and methods
analysis_scheduling_FSMCombination_combinator: Property = Property(name="combinator", type=StringType)
analysis_scheduling_FSMCombination.attributes={analysis_scheduling_FSMCombination_combinator}

# analysis_scheduling_FSMCondition class attributes and methods
analysis_scheduling_FSMCondition_comp: Property = Property(name="comp", type=StringType)
analysis_scheduling_FSMCondition_compval: Property = Property(name="compval", type=StringType)
analysis_scheduling_FSMCondition_valName: Property = Property(name="valName", type=StringType)
analysis_scheduling_FSMCondition.attributes={analysis_scheduling_FSMCondition_comp, analysis_scheduling_FSMCondition_valName, analysis_scheduling_FSMCondition_compval}

# FSMCombination class attributes and methods

# analysis_scheduling_FSMTransitionWithState class attributes and methods

# analysis_scheduling_PartitionedActorFire class attributes and methods

# analysis_scheduling_MarkovSimpleSchedulerReport class attributes and methods

# MarkovPartitionScheduler class attributes and methods

# scheduling_analysis_Network class attributes and methods

# analysis_scheduling_MarkovPartitionScheduler class attributes and methods
analysis_scheduling_MarkovPartitionScheduler_partitionId: Property = Property(name="partitionId", type=StringType)
analysis_scheduling_MarkovPartitionScheduler_m_getAssociatedState: Method = Method(name="getAssociatedState", parameters={Parameter(name='analysis_actor', type=StringType)}, type=StringType)
analysis_scheduling_MarkovPartitionScheduler.attributes={analysis_scheduling_MarkovPartitionScheduler_partitionId}
analysis_scheduling_MarkovPartitionScheduler.methods={analysis_scheduling_MarkovPartitionScheduler_m_getAssociatedState}

# scheduling_analysis_Actor class attributes and methods

# MarkovSchedulingState class attributes and methods

# MarkovSchedulingTransition class attributes and methods

# analysis_scheduling_MarkovSchedulingState class attributes and methods
analysis_scheduling_MarkovSchedulingState_firings: Property = Property(name="firings", type=StringType)
analysis_scheduling_MarkovSchedulingState_name: Property = Property(name="name", type=StringType)
analysis_scheduling_MarkovSchedulingState.attributes={analysis_scheduling_MarkovSchedulingState_name, analysis_scheduling_MarkovSchedulingState_firings}

# analysis_caseoptimal_CaseOptimalScheduleReport class attributes and methods
analysis_caseoptimal_CaseOptimalScheduleReport_traceFile: Property = Property(name="traceFile", type=StringType)
analysis_caseoptimal_CaseOptimalScheduleReport_pipeline: Property = Property(name="pipeline", type=StringType)
analysis_caseoptimal_CaseOptimalScheduleReport_partitionFilePath: Property = Property(name="partitionFilePath", type=StringType)
analysis_caseoptimal_CaseOptimalScheduleReport.attributes={analysis_caseoptimal_CaseOptimalScheduleReport_traceFile, analysis_caseoptimal_CaseOptimalScheduleReport_pipeline, analysis_caseoptimal_CaseOptimalScheduleReport_partitionFilePath}

# PartitionToActorSelectionScheduleMap class attributes and methods

# analysis_caseoptimal_CaseOptimalActorSelectionSchedule class attributes and methods

# analysis_scheduling_MarkovSchedulingTransition class attributes and methods
analysis_scheduling_MarkovSchedulingTransition_firings: Property = Property(name="firings", type=StringType)
analysis_scheduling_MarkovSchedulingTransition_name: Property = Property(name="name", type=StringType)
analysis_scheduling_MarkovSchedulingTransition.attributes={analysis_scheduling_MarkovSchedulingTransition_name, analysis_scheduling_MarkovSchedulingTransition_firings}

# Relationships
network0: BinaryAssociation = BinaryAssociation(
    name="network0",
    ends={
        Property(name="profiler_analysis_Network", type=analysis_profiler_CodeProfilingReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_CodeProfilingReport", type=profiler_analysis_Network, multiplicity=Multiplicity(0, 1))
    }
)
actorClassesData1: BinaryAssociation = BinaryAssociation(
    name="actorClassesData1",
    ends={
        Property(name="ComplexCodeData", type=analysis_profiler_CodeProfilingReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_CodeProfilingReport2", type=ComplexCodeData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operatorsCount6: BinaryAssociation = BinaryAssociation(
    name="operatorsCount6",
    ends={
        Property(name="StringToIntegerMap", type=analysis_profiler_CodeData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_CodeData", type=StringToIntegerMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operandsCount7: BinaryAssociation = BinaryAssociation(
    name="operandsCount7",
    ends={
        Property(name="StringToIntegerMap9", type=analysis_profiler_CodeData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_CodeData8", type=StringToIntegerMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actionsData10: BinaryAssociation = BinaryAssociation(
    name="actionsData10",
    ends={
        Property(name="CodeData", type=analysis_profiler_ComplexCodeData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_ComplexCodeData", type=CodeData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
proceduresData11: BinaryAssociation = BinaryAssociation(
    name="proceduresData11",
    ends={
        Property(name="CodeData13", type=analysis_profiler_ComplexCodeData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_ComplexCodeData12", type=CodeData, multiplicity=Multiplicity(0, 9999))
    }
)
network14: BinaryAssociation = BinaryAssociation(
    name="network14",
    ends={
        Property(name="profiler_analysis_Network15", type=analysis_profiler_DynamicProfilingReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_DynamicProfilingReport", type=profiler_analysis_Network, multiplicity=Multiplicity(0, 1))
    }
)
actorsData16: BinaryAssociation = BinaryAssociation(
    name="actorsData16",
    ends={
        Property(name="ActorDynamicData", type=analysis_profiler_DynamicProfilingReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_DynamicProfilingReport17", type=ActorDynamicData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
buffersData18: BinaryAssociation = BinaryAssociation(
    name="buffersData18",
    ends={
        Property(name="BufferDynamicData", type=analysis_profiler_DynamicProfilingReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_DynamicProfilingReport19", type=BufferDynamicData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
networkData3: BinaryAssociation = BinaryAssociation(
    name="networkData3",
    ends={
        Property(name="ComplexCodeData5", type=analysis_profiler_CodeProfilingReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_CodeProfilingReport4", type=ComplexCodeData, multiplicity=Multiplicity(1, 1))
    }
)
action23: BinaryAssociation = BinaryAssociation(
    name="action23",
    ends={
        Property(name="profiler_analysis_Action", type=analysis_profiler_ActionDynamicData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_ActionDynamicData", type=profiler_analysis_Action, multiplicity=Multiplicity(0, 1))
    }
)
buffer24: BinaryAssociation = BinaryAssociation(
    name="buffer24",
    ends={
        Property(name="profiler_analysis_Buffer", type=analysis_profiler_BufferDynamicData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_BufferDynamicData", type=profiler_analysis_Buffer, multiplicity=Multiplicity(0, 1))
    }
)
reads25: BinaryAssociation = BinaryAssociation(
    name="reads25",
    ends={
        Property(name="profiler_analysis_StatisticalData", type=analysis_profiler_BufferDynamicData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_BufferDynamicData26", type=profiler_analysis_StatisticalData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
writes27: BinaryAssociation = BinaryAssociation(
    name="writes27",
    ends={
        Property(name="profiler_analysis_StatisticalData29", type=analysis_profiler_BufferDynamicData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_BufferDynamicData28", type=profiler_analysis_StatisticalData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
occupancy30: BinaryAssociation = BinaryAssociation(
    name="occupancy30",
    ends={
        Property(name="profiler_analysis_StatisticalData32", type=analysis_profiler_BufferDynamicData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_BufferDynamicData31", type=profiler_analysis_StatisticalData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actionReads33: BinaryAssociation = BinaryAssociation(
    name="actionReads33",
    ends={
        Property(name="ActionToStatisticalDataMap", type=analysis_profiler_BufferDynamicData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_BufferDynamicData34", type=ActionToStatisticalDataMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actionWrites35: BinaryAssociation = BinaryAssociation(
    name="actionWrites35",
    ends={
        Property(name="ActionToStatisticalDataMap37", type=analysis_profiler_BufferDynamicData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_BufferDynamicData36", type=ActionToStatisticalDataMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actionPeeks38: BinaryAssociation = BinaryAssociation(
    name="actionPeeks38",
    ends={
        Property(name="ActionToLongMap", type=analysis_profiler_BufferDynamicData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_BufferDynamicData39", type=ActionToLongMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actionReadMisses40: BinaryAssociation = BinaryAssociation(
    name="actionReadMisses40",
    ends={
        Property(name="ActionToLongMap42", type=analysis_profiler_BufferDynamicData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_BufferDynamicData41", type=ActionToLongMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actionWriteMisses43: BinaryAssociation = BinaryAssociation(
    name="actionWriteMisses43",
    ends={
        Property(name="ActionToLongMap45", type=analysis_profiler_BufferDynamicData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_BufferDynamicData44", type=ActionToLongMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operandsCalls46: BinaryAssociation = BinaryAssociation(
    name="operandsCalls46",
    ends={
        Property(name="EOperatorToStatisticalDataMap", type=analysis_profiler_ComplexDynamicData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_ComplexDynamicData", type=EOperatorToStatisticalDataMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
proceduresCalls47: BinaryAssociation = BinaryAssociation(
    name="proceduresCalls47",
    ends={
        Property(name="ProcedureToStatisticalDataMap", type=analysis_profiler_ComplexDynamicData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_ComplexDynamicData48", type=ProcedureToStatisticalDataMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variablesStores49: BinaryAssociation = BinaryAssociation(
    name="variablesStores49",
    ends={
        Property(name="VariableToStatisticalDataMap", type=analysis_profiler_ComplexDynamicData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_ComplexDynamicData50", type=VariableToStatisticalDataMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variablesLoads51: BinaryAssociation = BinaryAssociation(
    name="variablesLoads51",
    ends={
        Property(name="VariableToStatisticalDataMap53", type=analysis_profiler_ComplexDynamicData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_ComplexDynamicData52", type=VariableToStatisticalDataMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
proceduresData54: BinaryAssociation = BinaryAssociation(
    name="proceduresData54",
    ends={
        Property(name="ProcedureToComplexDynamicDataMap", type=analysis_profiler_ComplexDynamicData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_ComplexDynamicData55", type=ProcedureToComplexDynamicDataMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
readTokens56: BinaryAssociation = BinaryAssociation(
    name="readTokens56",
    ends={
        Property(name="BufferToStatisticalDataMap", type=analysis_profiler_ComplexDynamicData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_ComplexDynamicData57", type=BufferToStatisticalDataMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
writeTokens58: BinaryAssociation = BinaryAssociation(
    name="writeTokens58",
    ends={
        Property(name="BufferToStatisticalDataMap60", type=analysis_profiler_ComplexDynamicData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_ComplexDynamicData59", type=BufferToStatisticalDataMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actor20: BinaryAssociation = BinaryAssociation(
    name="actor20",
    ends={
        Property(name="profiler_analysis_Actor", type=analysis_profiler_ActorDynamicData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_ActorDynamicData", type=profiler_analysis_Actor, multiplicity=Multiplicity(0, 1))
    }
)
actionsData21: BinaryAssociation = BinaryAssociation(
    name="actionsData21",
    ends={
        Property(name="ActionDynamicData", type=analysis_profiler_ActorDynamicData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_ActorDynamicData22", type=ActionDynamicData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actionsData64: BinaryAssociation = BinaryAssociation(
    name="actionsData64",
    ends={
        Property(name="ActionMemoryProfilingData", type=analysis_profiler_MemoryProfilingReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_MemoryProfilingReport", type=ActionMemoryProfilingData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reads65: BinaryAssociation = BinaryAssociation(
    name="reads65",
    ends={
        Property(name="MemoryAccessData", type=analysis_profiler_ActionMemoryProfilingData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_ActionMemoryProfilingData", type=MemoryAccessData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
writes66: BinaryAssociation = BinaryAssociation(
    name="writes66",
    ends={
        Property(name="MemoryAccessData68", type=analysis_profiler_ActionMemoryProfilingData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_ActionMemoryProfilingData67", type=MemoryAccessData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
accessesData69: BinaryAssociation = BinaryAssociation(
    name="accessesData69",
    ends={
        Property(name="StringToAccessDataMap", type=analysis_profiler_MemoryAccessData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_MemoryAccessData", type=StringToAccessDataMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key61: BinaryAssociation = BinaryAssociation(
    name="key61",
    ends={
        Property(name="profiler_analysis_Procedure", type=analysis_profiler_ProcedureToComplexDynamicDataMap, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_ProcedureToComplexDynamicDataMap", type=profiler_analysis_Procedure, multiplicity=Multiplicity(0, 1))
    }
)
value62: BinaryAssociation = BinaryAssociation(
    name="value62",
    ends={
        Property(name="ComplexDynamicData", type=analysis_profiler_ProcedureToComplexDynamicDataMap, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_ProcedureToComplexDynamicDataMap63", type=ComplexDynamicData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value70: BinaryAssociation = BinaryAssociation(
    name="value70",
    ends={
        Property(name="AccessData", type=analysis_profiler_StringToAccessDataMap, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_StringToAccessDataMap", type=AccessData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rows71: BinaryAssociation = BinaryAssociation(
    name="rows71",
    ends={
        Property(name="TableRow", type=analysis_profiler_BenchmarkReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_BenchmarkReport", type=TableRow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cells72: BinaryAssociation = BinaryAssociation(
    name="cells72",
    ends={
        Property(name="StringToStringMap", type=analysis_profiler_TableRow, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiler_TableRow", type=StringToStringMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key73: BinaryAssociation = BinaryAssociation(
    name="key73",
    ends={
        Property(name="map_analysis_Actor", type=analysis_map_ActorToStatisticalDataMap, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_map_ActorToStatisticalDataMap", type=map_analysis_Actor, multiplicity=Multiplicity(0, 1))
    }
)
value74: BinaryAssociation = BinaryAssociation(
    name="value74",
    ends={
        Property(name="map_analysis_StatisticalData", type=analysis_map_ActorToStatisticalDataMap, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_map_ActorToStatisticalDataMap75", type=map_analysis_StatisticalData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
key76: BinaryAssociation = BinaryAssociation(
    name="key76",
    ends={
        Property(name="map_analysis_Action", type=analysis_map_ActionToStatisticalDataMap, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_map_ActionToStatisticalDataMap", type=map_analysis_Action, multiplicity=Multiplicity(0, 1))
    }
)
value77: BinaryAssociation = BinaryAssociation(
    name="value77",
    ends={
        Property(name="map_analysis_StatisticalData79", type=analysis_map_ActionToStatisticalDataMap, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_map_ActionToStatisticalDataMap78", type=map_analysis_StatisticalData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
key80: BinaryAssociation = BinaryAssociation(
    name="key80",
    ends={
        Property(name="map_analysis_Buffer", type=analysis_map_BufferToStatisticalDataMap, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_map_BufferToStatisticalDataMap", type=map_analysis_Buffer, multiplicity=Multiplicity(0, 1))
    }
)
value81: BinaryAssociation = BinaryAssociation(
    name="value81",
    ends={
        Property(name="map_analysis_StatisticalData83", type=analysis_map_BufferToStatisticalDataMap, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_map_BufferToStatisticalDataMap82", type=map_analysis_StatisticalData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
key88: BinaryAssociation = BinaryAssociation(
    name="key88",
    ends={
        Property(name="map_analysis_Variable", type=analysis_map_VariableToStatisticalDataMap, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_map_VariableToStatisticalDataMap", type=map_analysis_Variable, multiplicity=Multiplicity(0, 1))
    }
)
value89: BinaryAssociation = BinaryAssociation(
    name="value89",
    ends={
        Property(name="map_analysis_StatisticalData91", type=analysis_map_VariableToStatisticalDataMap, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_map_VariableToStatisticalDataMap90", type=map_analysis_StatisticalData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
key92: BinaryAssociation = BinaryAssociation(
    name="key92",
    ends={
        Property(name="map_analysis_ActorClass", type=analysis_map_ActorClassToStatisticalDataMap, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_map_ActorClassToStatisticalDataMap", type=map_analysis_ActorClass, multiplicity=Multiplicity(0, 1))
    }
)
value93: BinaryAssociation = BinaryAssociation(
    name="value93",
    ends={
        Property(name="map_analysis_StatisticalData95", type=analysis_map_ActorClassToStatisticalDataMap, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_map_ActorClassToStatisticalDataMap94", type=map_analysis_StatisticalData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value96: BinaryAssociation = BinaryAssociation(
    name="value96",
    ends={
        Property(name="map_analysis_StatisticalData97", type=analysis_map_EOperatorToStatisticalDataMap, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_map_EOperatorToStatisticalDataMap", type=map_analysis_StatisticalData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
key98: BinaryAssociation = BinaryAssociation(
    name="key98",
    ends={
        Property(name="map_analysis_Action99", type=analysis_map_ActionToLongMap, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_map_ActionToLongMap", type=map_analysis_Action, multiplicity=Multiplicity(0, 1))
    }
)
key100: BinaryAssociation = BinaryAssociation(
    name="key100",
    ends={
        Property(name="map_analysis_Actor101", type=analysis_map_ActorToLongMap, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_map_ActorToLongMap", type=map_analysis_Actor, multiplicity=Multiplicity(0, 1))
    }
)
key102: BinaryAssociation = BinaryAssociation(
    name="key102",
    ends={
        Property(name="map_analysis_Buffer103", type=analysis_map_BufferToLongMap, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_map_BufferToLongMap", type=map_analysis_Buffer, multiplicity=Multiplicity(0, 1))
    }
)
key104: BinaryAssociation = BinaryAssociation(
    name="key104",
    ends={
        Property(name="map_analysis_Variable105", type=analysis_map_VariableToLongMap, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_map_VariableToLongMap", type=map_analysis_Variable, multiplicity=Multiplicity(0, 1))
    }
)
key106: BinaryAssociation = BinaryAssociation(
    name="key106",
    ends={
        Property(name="map_analysis_Guard", type=analysis_map_GuardToLongMap, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_map_GuardToLongMap", type=map_analysis_Guard, multiplicity=Multiplicity(0, 1))
    }
)
key107: BinaryAssociation = BinaryAssociation(
    name="key107",
    ends={
        Property(name="map_analysis_Port", type=analysis_map_PortToLongMap, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_map_PortToLongMap", type=map_analysis_Port, multiplicity=Multiplicity(0, 1))
    }
)
key84: BinaryAssociation = BinaryAssociation(
    name="key84",
    ends={
        Property(name="map_analysis_Procedure", type=analysis_map_ProcedureToStatisticalDataMap, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_map_ProcedureToStatisticalDataMap", type=map_analysis_Procedure, multiplicity=Multiplicity(0, 1))
    }
)
value85: BinaryAssociation = BinaryAssociation(
    name="value85",
    ends={
        Property(name="map_analysis_StatisticalData87", type=analysis_map_ProcedureToStatisticalDataMap, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_map_ProcedureToStatisticalDataMap86", type=map_analysis_StatisticalData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
key108: BinaryAssociation = BinaryAssociation(
    name="key108",
    ends={
        Property(name="map_analysis_Action109", type=analysis_map_ActionToDoubleMap, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_map_ActionToDoubleMap", type=map_analysis_Action, multiplicity=Multiplicity(0, 1))
    }
)
key110: BinaryAssociation = BinaryAssociation(
    name="key110",
    ends={
        Property(name="map_analysis_Buffer111", type=analysis_map_BufferToIntegerMap, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_map_BufferToIntegerMap", type=map_analysis_Buffer, multiplicity=Multiplicity(0, 1))
    }
)
key112: BinaryAssociation = BinaryAssociation(
    name="key112",
    ends={
        Property(name="map_analysis_Buffer113", type=analysis_map_BufferToDoubleMap, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_map_BufferToDoubleMap", type=map_analysis_Buffer, multiplicity=Multiplicity(0, 1))
    }
)
value114: BinaryAssociation = BinaryAssociation(
    name="value114",
    ends={
        Property(name="ActorSelectionSchedule", type=analysis_map_PartitionToActorSelectionScheduleMap, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_map_PartitionToActorSelectionScheduleMap", type=ActorSelectionSchedule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actionsFirings115: BinaryAssociation = BinaryAssociation(
    name="actionsFirings115",
    ends={
        Property(name="ActionToLongMap116", type=analysis_trace_TraceSizeReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_trace_TraceSizeReport", type=ActionToLongMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actionsIncomings117: BinaryAssociation = BinaryAssociation(
    name="actionsIncomings117",
    ends={
        Property(name="ActionToLongMap119", type=analysis_trace_TraceSizeReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_trace_TraceSizeReport118", type=ActionToLongMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actionsOutgoings120: BinaryAssociation = BinaryAssociation(
    name="actionsOutgoings120",
    ends={
        Property(name="ActionToLongMap122", type=analysis_trace_TraceSizeReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_trace_TraceSizeReport121", type=ActionToLongMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actorsFirings123: BinaryAssociation = BinaryAssociation(
    name="actorsFirings123",
    ends={
        Property(name="ActorToLongMap", type=analysis_trace_TraceSizeReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_trace_TraceSizeReport124", type=ActorToLongMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actorsOutgoings128: BinaryAssociation = BinaryAssociation(
    name="actorsOutgoings128",
    ends={
        Property(name="ActorToLongMap130", type=analysis_trace_TraceSizeReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_trace_TraceSizeReport129", type=ActorToLongMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependenciesKinds131: BinaryAssociation = BinaryAssociation(
    name="dependenciesKinds131",
    ends={
        Property(name="StringToLongMap", type=analysis_trace_TraceSizeReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_trace_TraceSizeReport132", type=StringToLongMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
network133: BinaryAssociation = BinaryAssociation(
    name="network133",
    ends={
        Property(name="trace_analysis_Network", type=analysis_trace_TraceSizeReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_trace_TraceSizeReport134", type=trace_analysis_Network, multiplicity=Multiplicity(0, 1))
    }
)
network135: BinaryAssociation = BinaryAssociation(
    name="network135",
    ends={
        Property(name="trace_analysis_Network136", type=analysis_trace_CompressedTraceReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_trace_CompressedTraceReport", type=trace_analysis_Network, multiplicity=Multiplicity(0, 1))
    }
)
steps137: BinaryAssociation = BinaryAssociation(
    name="steps137",
    ends={
        Property(name="CompressedStep", type=analysis_trace_CompressedTraceReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_trace_CompressedTraceReport138", type=CompressedStep, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependencies139: BinaryAssociation = BinaryAssociation(
    name="dependencies139",
    ends={
        Property(name="CompressedDependency", type=analysis_trace_CompressedTraceReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_trace_CompressedTraceReport140", type=CompressedDependency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action141: BinaryAssociation = BinaryAssociation(
    name="action141",
    ends={
        Property(name="trace_analysis_Action", type=analysis_trace_CompressedStep, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_trace_CompressedStep", type=trace_analysis_Action, multiplicity=Multiplicity(0, 1))
    }
)
incomings142: BinaryAssociation = BinaryAssociation(
    name="incomings142",
    ends={
        Property(name="CompressedDependency143", type=analysis_trace_CompressedStep, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=CompressedDependency, multiplicity=Multiplicity(0, 9999))
    }
)
outgoings144: BinaryAssociation = BinaryAssociation(
    name="outgoings144",
    ends={
        Property(name="CompressedDependency145", type=analysis_trace_CompressedStep, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=CompressedDependency, multiplicity=Multiplicity(0, 9999))
    }
)
predecessors146: BinaryAssociation = BinaryAssociation(
    name="predecessors146",
    ends={
        Property(name="CompressedStep148", type=analysis_trace_CompressedStep, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_trace_CompressedStep147", type=CompressedStep, multiplicity=Multiplicity(0, 9999))
    }
)
successors149: BinaryAssociation = BinaryAssociation(
    name="successors149",
    ends={
        Property(name="CompressedStep151", type=analysis_trace_CompressedStep, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_trace_CompressedStep150", type=CompressedStep, multiplicity=Multiplicity(0, 9999))
    }
)
neighbors152: BinaryAssociation = BinaryAssociation(
    name="neighbors152",
    ends={
        Property(name="CompressedStep154", type=analysis_trace_CompressedStep, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_trace_CompressedStep153", type=CompressedStep, multiplicity=Multiplicity(0, 9999))
    }
)
actorsIncoming125: BinaryAssociation = BinaryAssociation(
    name="actorsIncoming125",
    ends={
        Property(name="ActorToLongMap127", type=analysis_trace_TraceSizeReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_trace_TraceSizeReport126", type=ActorToLongMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target157: BinaryAssociation = BinaryAssociation(
    name="target157",
    ends={
        Property(name="CompressedStep158", type=analysis_trace_CompressedDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="incomings", type=CompressedStep, multiplicity=Multiplicity(0, 1))
    }
)
enableMap159: BinaryAssociation = BinaryAssociation(
    name="enableMap159",
    ends={
        Property(name="GuardToLongMap", type=analysis_trace_CompressedGuardDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_trace_CompressedGuardDependency", type=GuardToLongMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
disableMap160: BinaryAssociation = BinaryAssociation(
    name="disableMap160",
    ends={
        Property(name="GuardToLongMap162", type=analysis_trace_CompressedGuardDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_trace_CompressedGuardDependency161", type=GuardToLongMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
readReadMap163: BinaryAssociation = BinaryAssociation(
    name="readReadMap163",
    ends={
        Property(name="VariableToLongMap", type=analysis_trace_CompressedVariableDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_trace_CompressedVariableDependency", type=VariableToLongMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
readWriteMap164: BinaryAssociation = BinaryAssociation(
    name="readWriteMap164",
    ends={
        Property(name="VariableToLongMap166", type=analysis_trace_CompressedVariableDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_trace_CompressedVariableDependency165", type=VariableToLongMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
writeReadMap167: BinaryAssociation = BinaryAssociation(
    name="writeReadMap167",
    ends={
        Property(name="VariableToLongMap169", type=analysis_trace_CompressedVariableDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_trace_CompressedVariableDependency168", type=VariableToLongMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
writeWriteMap170: BinaryAssociation = BinaryAssociation(
    name="writeWriteMap170",
    ends={
        Property(name="VariableToLongMap172", type=analysis_trace_CompressedVariableDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_trace_CompressedVariableDependency171", type=VariableToLongMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
readMap173: BinaryAssociation = BinaryAssociation(
    name="readMap173",
    ends={
        Property(name="PortToLongMap", type=analysis_trace_CompressedPortDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_trace_CompressedPortDependency", type=PortToLongMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
writeMap174: BinaryAssociation = BinaryAssociation(
    name="writeMap174",
    ends={
        Property(name="PortToLongMap176", type=analysis_trace_CompressedPortDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_trace_CompressedPortDependency175", type=PortToLongMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
countMap177: BinaryAssociation = BinaryAssociation(
    name="countMap177",
    ends={
        Property(name="BufferToLongMap", type=analysis_trace_CompressedTokensDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_trace_CompressedTokensDependency", type=BufferToLongMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tokensMap178: BinaryAssociation = BinaryAssociation(
    name="tokensMap178",
    ends={
        Property(name="BufferToStatisticalDataMap180", type=analysis_trace_CompressedTokensDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_trace_CompressedTokensDependency179", type=BufferToStatisticalDataMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reference181: BinaryAssociation = BinaryAssociation(
    name="reference181",
    ends={
        Property(name="CompressedTraceReport", type=analysis_trace_TraceComparatorReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_trace_TraceComparatorReport", type=CompressedTraceReport, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
traces182: BinaryAssociation = BinaryAssociation(
    name="traces182",
    ends={
        Property(name="ComparedTrace", type=analysis_trace_TraceComparatorReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_trace_TraceComparatorReport183", type=ComparedTrace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compressedTrace184: BinaryAssociation = BinaryAssociation(
    name="compressedTrace184",
    ends={
        Property(name="CompressedTraceReport185", type=analysis_trace_ComparedTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_trace_ComparedTrace", type=CompressedTraceReport, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source155: BinaryAssociation = BinaryAssociation(
    name="source155",
    ends={
        Property(name="CompressedStep156", type=analysis_trace_CompressedDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoings", type=CompressedStep, multiplicity=Multiplicity(0, 1))
    }
)
containedReferenceActions186: BinaryAssociation = BinaryAssociation(
    name="containedReferenceActions186",
    ends={
        Property(name="trace_analysis_Action188", type=analysis_trace_ComparedTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_trace_ComparedTrace187", type=trace_analysis_Action, multiplicity=Multiplicity(0, 9999))
    }
)
actions189: BinaryAssociation = BinaryAssociation(
    name="actions189",
    ends={
        Property(name="ComparedAction", type=analysis_trace_ComparedTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_trace_ComparedTrace190", type=ComparedAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action191: BinaryAssociation = BinaryAssociation(
    name="action191",
    ends={
        Property(name="trace_analysis_Action192", type=analysis_trace_ComparedAction, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_trace_ComparedAction", type=trace_analysis_Action, multiplicity=Multiplicity(0, 1))
    }
)
network193: BinaryAssociation = BinaryAssociation(
    name="network193",
    ends={
        Property(name="trace_analysis_Network194", type=analysis_trace_MarkowModelTraceReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_trace_MarkowModelTraceReport", type=trace_analysis_Network, multiplicity=Multiplicity(0, 1))
    }
)
actionsData195: BinaryAssociation = BinaryAssociation(
    name="actionsData195",
    ends={
        Property(name="MarkovModelActionData", type=analysis_trace_MarkowModelTraceReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_trace_MarkowModelTraceReport196", type=MarkovModelActionData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action197: BinaryAssociation = BinaryAssociation(
    name="action197",
    ends={
        Property(name="trace_analysis_Action198", type=analysis_trace_MarkovModelActionData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_trace_MarkovModelActionData", type=trace_analysis_Action, multiplicity=Multiplicity(0, 1))
    }
)
successorsMap199: BinaryAssociation = BinaryAssociation(
    name="successorsMap199",
    ends={
        Property(name="ActionToLongMap201", type=analysis_trace_MarkovModelActionData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_trace_MarkovModelActionData200", type=ActionToLongMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
network202: BinaryAssociation = BinaryAssociation(
    name="network202",
    ends={
        Property(name="bottlenecks_analysis_Network", type=analysis_bottlenecks_BottlenecksReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_bottlenecks_BottlenecksReport", type=bottlenecks_analysis_Network, multiplicity=Multiplicity(0, 1))
    }
)
actionsData203: BinaryAssociation = BinaryAssociation(
    name="actionsData203",
    ends={
        Property(name="ActionBottlenecksData", type=analysis_bottlenecks_BottlenecksReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_bottlenecks_BottlenecksReport204", type=ActionBottlenecksData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action205: BinaryAssociation = BinaryAssociation(
    name="action205",
    ends={
        Property(name="bottlenecks_analysis_Action", type=analysis_bottlenecks_ActionBottlenecksData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_bottlenecks_ActionBottlenecksData", type=bottlenecks_analysis_Action, multiplicity=Multiplicity(0, 1))
    }
)
network206: BinaryAssociation = BinaryAssociation(
    name="network206",
    ends={
        Property(name="bottlenecks_analysis_Network207", type=analysis_bottlenecks_ImpactAnalysisReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_bottlenecks_ImpactAnalysisReport", type=bottlenecks_analysis_Network, multiplicity=Multiplicity(0, 1))
    }
)
impactData208: BinaryAssociation = BinaryAssociation(
    name="impactData208",
    ends={
        Property(name="ImpactAnalysisData", type=analysis_bottlenecks_ImpactAnalysisReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_bottlenecks_ImpactAnalysisReport209", type=ImpactAnalysisData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialBottlenecks210: BinaryAssociation = BinaryAssociation(
    name="initialBottlenecks210",
    ends={
        Property(name="BottlenecksReport", type=analysis_bottlenecks_ImpactAnalysisReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_bottlenecks_ImpactAnalysisReport211", type=BottlenecksReport, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actions212: BinaryAssociation = BinaryAssociation(
    name="actions212",
    ends={
        Property(name="bottlenecks_analysis_Action213", type=analysis_bottlenecks_ImpactAnalysisData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_bottlenecks_ImpactAnalysisData", type=bottlenecks_analysis_Action, multiplicity=Multiplicity(1, 9999))
    }
)
actorClass214: BinaryAssociation = BinaryAssociation(
    name="actorClass214",
    ends={
        Property(name="bottlenecks_analysis_ActorClass", type=analysis_bottlenecks_ImpactAnalysisData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_bottlenecks_ImpactAnalysisData215", type=bottlenecks_analysis_ActorClass, multiplicity=Multiplicity(0, 1))
    }
)
cpReductionMap216: BinaryAssociation = BinaryAssociation(
    name="cpReductionMap216",
    ends={
        Property(name="DoubleToDoubleMap", type=analysis_bottlenecks_ImpactAnalysisData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_bottlenecks_ImpactAnalysisData217", type=DoubleToDoubleMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reportsMap218: BinaryAssociation = BinaryAssociation(
    name="reportsMap218",
    ends={
        Property(name="DoubleToBottlenecksReportMap", type=analysis_bottlenecks_ImpactAnalysisData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_bottlenecks_ImpactAnalysisData219", type=DoubleToBottlenecksReportMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value220: BinaryAssociation = BinaryAssociation(
    name="value220",
    ends={
        Property(name="BottlenecksReport221", type=analysis_bottlenecks_DoubleToBottlenecksReportMap, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_bottlenecks_DoubleToBottlenecksReportMap", type=BottlenecksReport, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
network222: BinaryAssociation = BinaryAssociation(
    name="network222",
    ends={
        Property(name="bottlenecks_analysis_Network223", type=analysis_bottlenecks_BottlenecksWithSchedulingReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_bottlenecks_BottlenecksWithSchedulingReport", type=bottlenecks_analysis_Network, multiplicity=Multiplicity(0, 1))
    }
)
actionsData224: BinaryAssociation = BinaryAssociation(
    name="actionsData224",
    ends={
        Property(name="ActionBottlenecksWithSchedulingData", type=analysis_bottlenecks_BottlenecksWithSchedulingReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_bottlenecks_BottlenecksWithSchedulingReport225", type=ActionBottlenecksWithSchedulingData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cpPartitionsBlockingTime226: BinaryAssociation = BinaryAssociation(
    name="cpPartitionsBlockingTime226",
    ends={
        Property(name="StringToDoubleMap", type=analysis_bottlenecks_BottlenecksWithSchedulingReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_bottlenecks_BottlenecksWithSchedulingReport227", type=StringToDoubleMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action228: BinaryAssociation = BinaryAssociation(
    name="action228",
    ends={
        Property(name="bottlenecks_analysis_Action229", type=analysis_bottlenecks_ActionBottlenecksWithSchedulingData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_bottlenecks_ActionBottlenecksWithSchedulingData", type=bottlenecks_analysis_Action, multiplicity=Multiplicity(0, 1))
    }
)
maxBlockedOutputTokens230: BinaryAssociation = BinaryAssociation(
    name="maxBlockedOutputTokens230",
    ends={
        Property(name="BufferToIntegerMap", type=analysis_bottlenecks_ActionBottlenecksWithSchedulingData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_bottlenecks_ActionBottlenecksWithSchedulingData231", type=BufferToIntegerMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
maxBlockedMultiplication232: BinaryAssociation = BinaryAssociation(
    name="maxBlockedMultiplication232",
    ends={
        Property(name="BufferToDoubleMap", type=analysis_bottlenecks_ActionBottlenecksWithSchedulingData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_bottlenecks_ActionBottlenecksWithSchedulingData233", type=BufferToDoubleMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blockingInstances234: BinaryAssociation = BinaryAssociation(
    name="blockingInstances234",
    ends={
        Property(name="BufferToIntegerMap236", type=analysis_bottlenecks_ActionBottlenecksWithSchedulingData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_bottlenecks_ActionBottlenecksWithSchedulingData235", type=BufferToIntegerMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actions237: BinaryAssociation = BinaryAssociation(
    name="actions237",
    ends={
        Property(name="bottlenecks_analysis_Action238", type=analysis_bottlenecks_ScheduledImpactAnalysisData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_bottlenecks_ScheduledImpactAnalysisData", type=bottlenecks_analysis_Action, multiplicity=Multiplicity(1, 9999))
    }
)
actorClass239: BinaryAssociation = BinaryAssociation(
    name="actorClass239",
    ends={
        Property(name="bottlenecks_analysis_ActorClass241", type=analysis_bottlenecks_ScheduledImpactAnalysisData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_bottlenecks_ScheduledImpactAnalysisData240", type=bottlenecks_analysis_ActorClass, multiplicity=Multiplicity(0, 1))
    }
)
cpReductionMap242: BinaryAssociation = BinaryAssociation(
    name="cpReductionMap242",
    ends={
        Property(name="DoubleToDoubleMap244", type=analysis_bottlenecks_ScheduledImpactAnalysisData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_bottlenecks_ScheduledImpactAnalysisData243", type=DoubleToDoubleMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timeReductionMap245: BinaryAssociation = BinaryAssociation(
    name="timeReductionMap245",
    ends={
        Property(name="DoubleToDoubleMap247", type=analysis_bottlenecks_ScheduledImpactAnalysisData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_bottlenecks_ScheduledImpactAnalysisData246", type=DoubleToDoubleMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reportsMap248: BinaryAssociation = BinaryAssociation(
    name="reportsMap248",
    ends={
        Property(name="DoubleToBottlenecksWithSchedulingReportMap", type=analysis_bottlenecks_ScheduledImpactAnalysisData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_bottlenecks_ScheduledImpactAnalysisData249", type=DoubleToBottlenecksWithSchedulingReportMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value250: BinaryAssociation = BinaryAssociation(
    name="value250",
    ends={
        Property(name="BottlenecksWithSchedulingReport", type=analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap", type=BottlenecksWithSchedulingReport, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
network251: BinaryAssociation = BinaryAssociation(
    name="network251",
    ends={
        Property(name="bottlenecks_analysis_Network252", type=analysis_bottlenecks_ScheduledImpactAnalysisReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_bottlenecks_ScheduledImpactAnalysisReport", type=bottlenecks_analysis_Network, multiplicity=Multiplicity(0, 1))
    }
)
initialBottlenecksWithScheduling255: BinaryAssociation = BinaryAssociation(
    name="initialBottlenecksWithScheduling255",
    ends={
        Property(name="BottlenecksWithSchedulingReport257", type=analysis_bottlenecks_ScheduledImpactAnalysisReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_bottlenecks_ScheduledImpactAnalysisReport256", type=BottlenecksWithSchedulingReport, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
network258: BinaryAssociation = BinaryAssociation(
    name="network258",
    ends={
        Property(name="buffers_analysis_Network", type=analysis_buffers_BoundedBuffersReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_buffers_BoundedBuffersReport", type=buffers_analysis_Network, multiplicity=Multiplicity(0, 1))
    }
)
buffersData259: BinaryAssociation = BinaryAssociation(
    name="buffersData259",
    ends={
        Property(name="BoundedBufferData", type=analysis_buffers_BoundedBuffersReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_buffers_BoundedBuffersReport260", type=BoundedBufferData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
buffer261: BinaryAssociation = BinaryAssociation(
    name="buffer261",
    ends={
        Property(name="buffers_analysis_Buffer", type=analysis_buffers_BoundedBufferData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_buffers_BoundedBufferData", type=buffers_analysis_Buffer, multiplicity=Multiplicity(0, 1))
    }
)
network262: BinaryAssociation = BinaryAssociation(
    name="network262",
    ends={
        Property(name="buffers_analysis_Network263", type=analysis_buffers_OptimalBuffersReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_buffers_OptimalBuffersReport", type=buffers_analysis_Network, multiplicity=Multiplicity(0, 1))
    }
)
buffersData264: BinaryAssociation = BinaryAssociation(
    name="buffersData264",
    ends={
        Property(name="OptimalBufferData", type=analysis_buffers_OptimalBuffersReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_buffers_OptimalBuffersReport265", type=OptimalBufferData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialBufferConfiguration266: BinaryAssociation = BinaryAssociation(
    name="initialBufferConfiguration266",
    ends={
        Property(name="BoundedBuffersReport", type=analysis_buffers_OptimalBuffersReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_buffers_OptimalBuffersReport267", type=BoundedBuffersReport, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialBottlenecks268: BinaryAssociation = BinaryAssociation(
    name="initialBottlenecks268",
    ends={
        Property(name="BottlenecksWithSchedulingReport270", type=analysis_buffers_OptimalBuffersReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_buffers_OptimalBuffersReport269", type=BottlenecksWithSchedulingReport, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bufferData271: BinaryAssociation = BinaryAssociation(
    name="bufferData271",
    ends={
        Property(name="BoundedBuffersReport272", type=analysis_buffers_OptimalBufferData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_buffers_OptimalBufferData", type=BoundedBuffersReport, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bottlenecksData273: BinaryAssociation = BinaryAssociation(
    name="bottlenecksData273",
    ends={
        Property(name="BottlenecksWithSchedulingReport275", type=analysis_buffers_OptimalBufferData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_buffers_OptimalBufferData274", type=BottlenecksWithSchedulingReport, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
network276: BinaryAssociation = BinaryAssociation(
    name="network276",
    ends={
        Property(name="partitioning_analysis_Network", type=analysis_partitioning_ComCostPartitioningReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_partitioning_ComCostPartitioningReport", type=partitioning_analysis_Network, multiplicity=Multiplicity(0, 1))
    }
)
partitions277: BinaryAssociation = BinaryAssociation(
    name="partitions277",
    ends={
        Property(name="ComCostPartition", type=analysis_partitioning_ComCostPartitioningReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_partitioning_ComCostPartitioningReport278", type=ComCostPartition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scheduledImpactData253: BinaryAssociation = BinaryAssociation(
    name="scheduledImpactData253",
    ends={
        Property(name="ScheduledImpactAnalysisData", type=analysis_bottlenecks_ScheduledImpactAnalysisReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_bottlenecks_ScheduledImpactAnalysisReport254", type=ScheduledImpactAnalysisData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
internalCostMap280: BinaryAssociation = BinaryAssociation(
    name="internalCostMap280",
    ends={
        Property(name="ActorToLongMap282", type=analysis_partitioning_ComCostPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_partitioning_ComCostPartition281", type=ActorToLongMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
externalCostMap283: BinaryAssociation = BinaryAssociation(
    name="externalCostMap283",
    ends={
        Property(name="ActorToLongMap285", type=analysis_partitioning_ComCostPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_partitioning_ComCostPartition284", type=ActorToLongMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actors286: BinaryAssociation = BinaryAssociation(
    name="actors286",
    ends={
        Property(name="partitioning_analysis_Actor287", type=analysis_partitioning_WorkloadBalancePartition, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_partitioning_WorkloadBalancePartition", type=partitioning_analysis_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
network288: BinaryAssociation = BinaryAssociation(
    name="network288",
    ends={
        Property(name="partitioning_analysis_Network289", type=analysis_partitioning_WorkloadBalancePartitioningReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_partitioning_WorkloadBalancePartitioningReport", type=partitioning_analysis_Network, multiplicity=Multiplicity(0, 1))
    }
)
partitions290: BinaryAssociation = BinaryAssociation(
    name="partitions290",
    ends={
        Property(name="WorkloadBalancePartition", type=analysis_partitioning_WorkloadBalancePartitioningReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_partitioning_WorkloadBalancePartitioningReport291", type=WorkloadBalancePartition, multiplicity=Multiplicity(0, 9999))
    }
)
actors292: BinaryAssociation = BinaryAssociation(
    name="actors292",
    ends={
        Property(name="partitioning_analysis_Actor293", type=analysis_partitioning_BalancedPipelinePartition, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_partitioning_BalancedPipelinePartition", type=partitioning_analysis_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
actors279: BinaryAssociation = BinaryAssociation(
    name="actors279",
    ends={
        Property(name="partitioning_analysis_Actor", type=analysis_partitioning_ComCostPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_partitioning_ComCostPartition", type=partitioning_analysis_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
partitions294: BinaryAssociation = BinaryAssociation(
    name="partitions294",
    ends={
        Property(name="BalancedPipelinePartition", type=analysis_partitioning_BalancedPipelinePartitioningReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_partitioning_BalancedPipelinePartitioningReport", type=BalancedPipelinePartition, multiplicity=Multiplicity(0, 9999))
    }
)
network295: BinaryAssociation = BinaryAssociation(
    name="network295",
    ends={
        Property(name="partitioning_analysis_Network297", type=analysis_partitioning_BalancedPipelinePartitioningReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_partitioning_BalancedPipelinePartitioningReport296", type=partitioning_analysis_Network, multiplicity=Multiplicity(0, 1))
    }
)
network298: BinaryAssociation = BinaryAssociation(
    name="network298",
    ends={
        Property(name="pipelining_analysis_Network", type=analysis_pipelining_ActionsVariablePipeliningReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_pipelining_ActionsVariablePipeliningReport", type=pipelining_analysis_Network, multiplicity=Multiplicity(0, 1))
    }
)
actionsData299: BinaryAssociation = BinaryAssociation(
    name="actionsData299",
    ends={
        Property(name="ActionVariablePipeliningData", type=analysis_pipelining_ActionsVariablePipeliningReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_pipelining_ActionsVariablePipeliningReport300", type=ActionVariablePipeliningData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action301: BinaryAssociation = BinaryAssociation(
    name="action301",
    ends={
        Property(name="pipelining_analysis_Action", type=analysis_pipelining_ActionVariablePipeliningData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_pipelining_ActionVariablePipeliningData", type=pipelining_analysis_Action, multiplicity=Multiplicity(0, 1))
    }
)
consecutiveFirings302: BinaryAssociation = BinaryAssociation(
    name="consecutiveFirings302",
    ends={
        Property(name="pipelining_analysis_StatisticalData", type=analysis_pipelining_ActionVariablePipeliningData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_pipelining_ActionVariablePipeliningData303", type=pipelining_analysis_StatisticalData, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
pipelinableFirings304: BinaryAssociation = BinaryAssociation(
    name="pipelinableFirings304",
    ends={
        Property(name="pipelining_analysis_StatisticalData306", type=analysis_pipelining_ActionVariablePipeliningData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_pipelining_ActionVariablePipeliningData305", type=pipelining_analysis_StatisticalData, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
network307: BinaryAssociation = BinaryAssociation(
    name="network307",
    ends={
        Property(name="pipelining_analysis_Network308", type=analysis_pipelining_ImpactAnalysisReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_pipelining_ImpactAnalysisReport", type=pipelining_analysis_Network, multiplicity=Multiplicity(0, 1))
    }
)
initialBottlenecks309: BinaryAssociation = BinaryAssociation(
    name="initialBottlenecks309",
    ends={
        Property(name="BottlenecksReport311", type=analysis_pipelining_ImpactAnalysisReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_pipelining_ImpactAnalysisReport310", type=BottlenecksReport, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
piplenablesActions312: BinaryAssociation = BinaryAssociation(
    name="piplenablesActions312",
    ends={
        Property(name="ActionsVariablePipeliningReport", type=analysis_pipelining_ImpactAnalysisReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_pipelining_ImpactAnalysisReport313", type=ActionsVariablePipeliningReport, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
impactData314: BinaryAssociation = BinaryAssociation(
    name="impactData314",
    ends={
        Property(name="ImpactAnalysisData316", type=analysis_pipelining_ImpactAnalysisReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_pipelining_ImpactAnalysisReport315", type=ImpactAnalysisData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
estimatedBottlenecks317: BinaryAssociation = BinaryAssociation(
    name="estimatedBottlenecks317",
    ends={
        Property(name="BottlenecksReport318", type=analysis_pipelining_ImpactAnalysisData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_pipelining_ImpactAnalysisData", type=BottlenecksReport, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actions319: BinaryAssociation = BinaryAssociation(
    name="actions319",
    ends={
        Property(name="pipelining_analysis_Action321", type=analysis_pipelining_ImpactAnalysisData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_pipelining_ImpactAnalysisData320", type=pipelining_analysis_Action, multiplicity=Multiplicity(1, 9999))
    }
)
network324: BinaryAssociation = BinaryAssociation(
    name="network324",
    ends={
        Property(name="postprocessing_analysis_Network", type=analysis_postprocessing_PostProcessingReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_postprocessing_PostProcessingReport", type=postprocessing_analysis_Network, multiplicity=Multiplicity(0, 1))
    }
)
reports325: BinaryAssociation = BinaryAssociation(
    name="reports325",
    ends={
        Property(name="PostProcessingData", type=analysis_postprocessing_PostProcessingReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_postprocessing_PostProcessingReport326", type=PostProcessingData, multiplicity=Multiplicity(0, 9999))
    }
)
network327: BinaryAssociation = BinaryAssociation(
    name="network327",
    ends={
        Property(name="postprocessing_analysis_Network328", type=analysis_postprocessing_ActorStatisticsReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_postprocessing_ActorStatisticsReport", type=postprocessing_analysis_Network, multiplicity=Multiplicity(0, 1))
    }
)
partitions329: BinaryAssociation = BinaryAssociation(
    name="partitions329",
    ends={
        Property(name="StatisticalActorPartition", type=analysis_postprocessing_ActorStatisticsReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_postprocessing_ActorStatisticsReport330", type=StatisticalActorPartition, multiplicity=Multiplicity(0, 9999))
    }
)
idleTimes331: BinaryAssociation = BinaryAssociation(
    name="idleTimes331",
    ends={
        Property(name="StringToDoubleMap333", type=analysis_postprocessing_ActorStatisticsReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_postprocessing_ActorStatisticsReport332", type=StringToDoubleMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blockedReadingTimes334: BinaryAssociation = BinaryAssociation(
    name="blockedReadingTimes334",
    ends={
        Property(name="StringToDoubleMap336", type=analysis_postprocessing_ActorStatisticsReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_postprocessing_ActorStatisticsReport335", type=StringToDoubleMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blockedWritingTimes337: BinaryAssociation = BinaryAssociation(
    name="blockedWritingTimes337",
    ends={
        Property(name="StringToDoubleMap339", type=analysis_postprocessing_ActorStatisticsReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_postprocessing_ActorStatisticsReport338", type=StringToDoubleMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processingTimes340: BinaryAssociation = BinaryAssociation(
    name="processingTimes340",
    ends={
        Property(name="StringToDoubleMap342", type=analysis_postprocessing_ActorStatisticsReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_postprocessing_ActorStatisticsReport341", type=StringToDoubleMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actors343: BinaryAssociation = BinaryAssociation(
    name="actors343",
    ends={
        Property(name="postprocessing_analysis_Actor", type=analysis_postprocessing_ActionStatisticsReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_postprocessing_ActionStatisticsReport", type=postprocessing_analysis_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
idleTimes344: BinaryAssociation = BinaryAssociation(
    name="idleTimes344",
    ends={
        Property(name="ActionToDoubleMap", type=analysis_postprocessing_ActionStatisticsReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_postprocessing_ActionStatisticsReport345", type=ActionToDoubleMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
idleMinTimes346: BinaryAssociation = BinaryAssociation(
    name="idleMinTimes346",
    ends={
        Property(name="ActionToDoubleMap348", type=analysis_postprocessing_ActionStatisticsReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_postprocessing_ActionStatisticsReport347", type=ActionToDoubleMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
idleMaxTimes349: BinaryAssociation = BinaryAssociation(
    name="idleMaxTimes349",
    ends={
        Property(name="ActionToDoubleMap351", type=analysis_postprocessing_ActionStatisticsReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_postprocessing_ActionStatisticsReport350", type=ActionToDoubleMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blockedReadingTimes352: BinaryAssociation = BinaryAssociation(
    name="blockedReadingTimes352",
    ends={
        Property(name="ActionToDoubleMap354", type=analysis_postprocessing_ActionStatisticsReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_postprocessing_ActionStatisticsReport353", type=ActionToDoubleMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blockedReadingMinTimes355: BinaryAssociation = BinaryAssociation(
    name="blockedReadingMinTimes355",
    ends={
        Property(name="ActionToDoubleMap357", type=analysis_postprocessing_ActionStatisticsReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_postprocessing_ActionStatisticsReport356", type=ActionToDoubleMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actorClass322: BinaryAssociation = BinaryAssociation(
    name="actorClass322",
    ends={
        Property(name="pipelining_analysis_ActorClass", type=analysis_pipelining_ImpactAnalysisData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_pipelining_ImpactAnalysisData323", type=pipelining_analysis_ActorClass, multiplicity=Multiplicity(0, 1))
    }
)
blockedWritingTimes361: BinaryAssociation = BinaryAssociation(
    name="blockedWritingTimes361",
    ends={
        Property(name="ActionToDoubleMap363", type=analysis_postprocessing_ActionStatisticsReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_postprocessing_ActionStatisticsReport362", type=ActionToDoubleMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blockedWritingMinTimes364: BinaryAssociation = BinaryAssociation(
    name="blockedWritingMinTimes364",
    ends={
        Property(name="ActionToDoubleMap366", type=analysis_postprocessing_ActionStatisticsReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_postprocessing_ActionStatisticsReport365", type=ActionToDoubleMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blockedWritingMaxTimes367: BinaryAssociation = BinaryAssociation(
    name="blockedWritingMaxTimes367",
    ends={
        Property(name="ActionToDoubleMap369", type=analysis_postprocessing_ActionStatisticsReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_postprocessing_ActionStatisticsReport368", type=ActionToDoubleMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processingTimes370: BinaryAssociation = BinaryAssociation(
    name="processingTimes370",
    ends={
        Property(name="ActionToDoubleMap372", type=analysis_postprocessing_ActionStatisticsReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_postprocessing_ActionStatisticsReport371", type=ActionToDoubleMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
executionCounts373: BinaryAssociation = BinaryAssociation(
    name="executionCounts373",
    ends={
        Property(name="ActionToLongMap375", type=analysis_postprocessing_ActionStatisticsReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_postprocessing_ActionStatisticsReport374", type=ActionToLongMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
partitions376: BinaryAssociation = BinaryAssociation(
    name="partitions376",
    ends={
        Property(name="SchedulerChecksPartition", type=analysis_postprocessing_SchedulerChecksReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_postprocessing_SchedulerChecksReport", type=SchedulerChecksPartition, multiplicity=Multiplicity(0, 9999))
    }
)
aggregatedCheckedData377: BinaryAssociation = BinaryAssociation(
    name="aggregatedCheckedData377",
    ends={
        Property(name="postprocessing_analysis_StatisticalData", type=analysis_postprocessing_SchedulerChecksPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_postprocessing_SchedulerChecksPartition", type=postprocessing_analysis_StatisticalData, multiplicity=Multiplicity(0, 1))
    }
)
aggregatedFailedData378: BinaryAssociation = BinaryAssociation(
    name="aggregatedFailedData378",
    ends={
        Property(name="postprocessing_analysis_StatisticalData380", type=analysis_postprocessing_SchedulerChecksPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_postprocessing_SchedulerChecksPartition379", type=postprocessing_analysis_StatisticalData, multiplicity=Multiplicity(0, 1))
    }
)
checkedConditionsMap381: BinaryAssociation = BinaryAssociation(
    name="checkedConditionsMap381",
    ends={
        Property(name="ActorToStatisticalDataMap", type=analysis_postprocessing_SchedulerChecksPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_postprocessing_SchedulerChecksPartition382", type=ActorToStatisticalDataMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failedConditionsMap383: BinaryAssociation = BinaryAssociation(
    name="failedConditionsMap383",
    ends={
        Property(name="ActorToStatisticalDataMap385", type=analysis_postprocessing_SchedulerChecksPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_postprocessing_SchedulerChecksPartition384", type=ActorToStatisticalDataMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
network386: BinaryAssociation = BinaryAssociation(
    name="network386",
    ends={
        Property(name="postprocessing_analysis_Network387", type=analysis_postprocessing_BufferBlockingReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_postprocessing_BufferBlockingReport", type=postprocessing_analysis_Network, multiplicity=Multiplicity(0, 1))
    }
)
maxBlockedOutputTokens388: BinaryAssociation = BinaryAssociation(
    name="maxBlockedOutputTokens388",
    ends={
        Property(name="BufferToIntegerMap390", type=analysis_postprocessing_BufferBlockingReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_postprocessing_BufferBlockingReport389", type=BufferToIntegerMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
maxBlockedMultiplication391: BinaryAssociation = BinaryAssociation(
    name="maxBlockedMultiplication391",
    ends={
        Property(name="BufferToDoubleMap393", type=analysis_postprocessing_BufferBlockingReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_postprocessing_BufferBlockingReport392", type=BufferToDoubleMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blockingInstances394: BinaryAssociation = BinaryAssociation(
    name="blockingInstances394",
    ends={
        Property(name="BufferToIntegerMap396", type=analysis_postprocessing_BufferBlockingReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_postprocessing_BufferBlockingReport395", type=BufferToIntegerMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actorsData397: BinaryAssociation = BinaryAssociation(
    name="actorsData397",
    ends={
        Property(name="IntraActorCommunicationData", type=analysis_profiling_IntraActionCommunicationReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiling_IntraActionCommunicationReport", type=IntraActorCommunicationData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blockedReadingMaxTimes358: BinaryAssociation = BinaryAssociation(
    name="blockedReadingMaxTimes358",
    ends={
        Property(name="ActionToDoubleMap360", type=analysis_postprocessing_ActionStatisticsReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_postprocessing_ActionStatisticsReport359", type=ActionToDoubleMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
consumedTokens401: BinaryAssociation = BinaryAssociation(
    name="consumedTokens401",
    ends={
        Property(name="profiling_analysis_StatisticalData", type=analysis_profiling_IntraActorCommunicationData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiling_IntraActorCommunicationData402", type=profiling_analysis_StatisticalData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
producedTokens403: BinaryAssociation = BinaryAssociation(
    name="producedTokens403",
    ends={
        Property(name="profiling_analysis_StatisticalData405", type=analysis_profiling_IntraActorCommunicationData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiling_IntraActorCommunicationData404", type=profiling_analysis_StatisticalData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tokensProducersMap406: BinaryAssociation = BinaryAssociation(
    name="tokensProducersMap406",
    ends={
        Property(name="ActorToStatisticalDataMap408", type=analysis_profiling_IntraActorCommunicationData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiling_IntraActorCommunicationData407", type=ActorToStatisticalDataMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actionsData409: BinaryAssociation = BinaryAssociation(
    name="actionsData409",
    ends={
        Property(name="IntraActionCommunicationData", type=analysis_profiling_IntraActorCommunicationData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiling_IntraActorCommunicationData410", type=IntraActionCommunicationData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action411: BinaryAssociation = BinaryAssociation(
    name="action411",
    ends={
        Property(name="profiling_analysis_Action", type=analysis_profiling_IntraActionCommunicationData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiling_IntraActionCommunicationData", type=profiling_analysis_Action, multiplicity=Multiplicity(0, 1))
    }
)
consumedTokens412: BinaryAssociation = BinaryAssociation(
    name="consumedTokens412",
    ends={
        Property(name="profiling_analysis_StatisticalData414", type=analysis_profiling_IntraActionCommunicationData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiling_IntraActionCommunicationData413", type=profiling_analysis_StatisticalData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
producedTokens415: BinaryAssociation = BinaryAssociation(
    name="producedTokens415",
    ends={
        Property(name="profiling_analysis_StatisticalData417", type=analysis_profiling_IntraActionCommunicationData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiling_IntraActionCommunicationData416", type=profiling_analysis_StatisticalData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tokensProducersMap418: BinaryAssociation = BinaryAssociation(
    name="tokensProducersMap418",
    ends={
        Property(name="ActionToStatisticalDataMap420", type=analysis_profiling_IntraActionCommunicationData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiling_IntraActionCommunicationData419", type=ActionToStatisticalDataMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actorsStatsData421: BinaryAssociation = BinaryAssociation(
    name="actorsStatsData421",
    ends={
        Property(name="ProfilingStatsActorData", type=analysis_profiling_ProfilingStatsReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiling_ProfilingStatsReport", type=ProfilingStatsActorData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
network398: BinaryAssociation = BinaryAssociation(
    name="network398",
    ends={
        Property(name="profiling_analysis_Network", type=analysis_profiling_IntraActionCommunicationReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiling_IntraActionCommunicationReport399", type=profiling_analysis_Network, multiplicity=Multiplicity(0, 1))
    }
)
actor400: BinaryAssociation = BinaryAssociation(
    name="actor400",
    ends={
        Property(name="profiling_analysis_Actor", type=analysis_profiling_IntraActorCommunicationData, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_profiling_IntraActorCommunicationData", type=profiling_analysis_Actor, multiplicity=Multiplicity(0, 1))
    }
)
actions425: BinaryAssociation = BinaryAssociation(
    name="actions425",
    ends={
        Property(name="ActorFire", type=analysis_scheduling_Sequence, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_scheduling_Sequence", type=ActorFire, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cond426: BinaryAssociation = BinaryAssociation(
    name="cond426",
    ends={
        Property(name="FSMCondition", type=analysis_scheduling_FSMTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_scheduling_FSMTransition", type=FSMCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transitionSchedule427: BinaryAssociation = BinaryAssociation(
    name="transitionSchedule427",
    ends={
        Property(name="Sequence", type=analysis_scheduling_FSMTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_scheduling_FSMTransition428", type=Sequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
varUpdates429: BinaryAssociation = BinaryAssociation(
    name="varUpdates429",
    ends={
        Property(name="FSMVarUpdate", type=analysis_scheduling_FSMState, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_scheduling_FSMState", type=FSMVarUpdate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions430: BinaryAssociation = BinaryAssociation(
    name="transitions430",
    ends={
        Property(name="FSMTransition", type=analysis_scheduling_FSMState, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_scheduling_FSMState431", type=FSMTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operation432: BinaryAssociation = BinaryAssociation(
    name="operation432",
    ends={
        Property(name="FSMOperation", type=analysis_scheduling_FSMVarUpdate, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_scheduling_FSMVarUpdate", type=FSMOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition433: BinaryAssociation = BinaryAssociation(
    name="condition433",
    ends={
        Property(name="FSMCondition435", type=analysis_scheduling_FSMVarUpdate, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_scheduling_FSMVarUpdate434", type=FSMCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
states422: BinaryAssociation = BinaryAssociation(
    name="states422",
    ends={
        Property(name="FSMState", type=analysis_scheduling_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_scheduling_FSM", type=FSMState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vars423: BinaryAssociation = BinaryAssociation(
    name="vars423",
    ends={
        Property(name="FSMVar", type=analysis_scheduling_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_scheduling_FSM424", type=FSMVar, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cond436: BinaryAssociation = BinaryAssociation(
    name="cond436",
    ends={
        Property(name="FSMCondition437", type=analysis_scheduling_FSMCombination, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_scheduling_FSMCombination", type=FSMCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
combinedCond438: BinaryAssociation = BinaryAssociation(
    name="combinedCond438",
    ends={
        Property(name="FSMCombination", type=analysis_scheduling_FSMCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_scheduling_FSMCondition", type=FSMCombination, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
varStates439: BinaryAssociation = BinaryAssociation(
    name="varStates439",
    ends={
        Property(name="StringToIntegerMap440", type=analysis_scheduling_FSMTransitionWithState, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_scheduling_FSMTransitionWithState", type=StringToIntegerMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
partitions441: BinaryAssociation = BinaryAssociation(
    name="partitions441",
    ends={
        Property(name="MarkovPartitionScheduler", type=analysis_scheduling_MarkovSimpleSchedulerReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_scheduling_MarkovSimpleSchedulerReport", type=MarkovPartitionScheduler, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
network442: BinaryAssociation = BinaryAssociation(
    name="network442",
    ends={
        Property(name="scheduling_analysis_Network", type=analysis_scheduling_MarkovSimpleSchedulerReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_scheduling_MarkovSimpleSchedulerReport443", type=scheduling_analysis_Network, multiplicity=Multiplicity(0, 1))
    }
)
actors444: BinaryAssociation = BinaryAssociation(
    name="actors444",
    ends={
        Property(name="scheduling_analysis_Actor", type=analysis_scheduling_MarkovPartitionScheduler, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_scheduling_MarkovPartitionScheduler", type=scheduling_analysis_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
states445: BinaryAssociation = BinaryAssociation(
    name="states445",
    ends={
        Property(name="MarkovSchedulingState", type=analysis_scheduling_MarkovPartitionScheduler, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_scheduling_MarkovPartitionScheduler446", type=MarkovSchedulingState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions447: BinaryAssociation = BinaryAssociation(
    name="transitions447",
    ends={
        Property(name="MarkovSchedulingTransition", type=analysis_scheduling_MarkovPartitionScheduler, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_scheduling_MarkovPartitionScheduler448", type=MarkovSchedulingTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actor449: BinaryAssociation = BinaryAssociation(
    name="actor449",
    ends={
        Property(name="scheduling_analysis_Actor450", type=analysis_scheduling_MarkovSchedulingState, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_scheduling_MarkovSchedulingState", type=scheduling_analysis_Actor, multiplicity=Multiplicity(1, 1))
    }
)
outgoings451: BinaryAssociation = BinaryAssociation(
    name="outgoings451",
    ends={
        Property(name="MarkovSchedulingTransition453", type=analysis_scheduling_MarkovSchedulingState, multiplicity=Multiplicity(1, 1)),
        Property(name="source452", type=MarkovSchedulingTransition, multiplicity=Multiplicity(0, 9999))
    }
)
incomings454: BinaryAssociation = BinaryAssociation(
    name="incomings454",
    ends={
        Property(name="MarkovSchedulingTransition456", type=analysis_scheduling_MarkovSchedulingState, multiplicity=Multiplicity(1, 1)),
        Property(name="target455", type=MarkovSchedulingTransition, multiplicity=Multiplicity(0, 9999))
    }
)
target460: BinaryAssociation = BinaryAssociation(
    name="target460",
    ends={
        Property(name="MarkovSchedulingState462", type=analysis_scheduling_MarkovSchedulingTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomings461", type=MarkovSchedulingState, multiplicity=Multiplicity(1, 1))
    }
)
partitionSchedules463: BinaryAssociation = BinaryAssociation(
    name="partitionSchedules463",
    ends={
        Property(name="PartitionToActorSelectionScheduleMap", type=analysis_caseoptimal_CaseOptimalScheduleReport, multiplicity=Multiplicity(1, 1)),
        Property(name="analysis_caseoptimal_CaseOptimalScheduleReport", type=PartitionToActorSelectionScheduleMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source457: BinaryAssociation = BinaryAssociation(
    name="source457",
    ends={
        Property(name="MarkovSchedulingState459", type=analysis_scheduling_MarkovSchedulingTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoings458", type=MarkovSchedulingState, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_analysis_profiler_CodeProfilingReport_AnalysisReport = Generalization(general=AnalysisReport, specific=analysis_profiler_CodeProfilingReport)
gen_analysis_profiler_ComplexCodeData_CodeData = Generalization(general=CodeData, specific=analysis_profiler_ComplexCodeData)
gen_analysis_profiler_DynamicProfilingReport_AnalysisReport = Generalization(general=AnalysisReport, specific=analysis_profiler_DynamicProfilingReport)
gen_analysis_profiler_ActorDynamicData_ComplexDynamicData = Generalization(general=ComplexDynamicData, specific=analysis_profiler_ActorDynamicData)
gen_analysis_profiler_ActionDynamicData_ComplexDynamicData = Generalization(general=ComplexDynamicData, specific=analysis_profiler_ActionDynamicData)
gen_analysis_profiler_MemoryProfilingReport_AnalysisReport = Generalization(general=AnalysisReport, specific=analysis_profiler_MemoryProfilingReport)
gen_analysis_profiler_BufferAccessData_MemoryAccessData = Generalization(general=MemoryAccessData, specific=analysis_profiler_BufferAccessData)
gen_analysis_profiler_LocalVariableAccessData_MemoryAccessData = Generalization(general=MemoryAccessData, specific=analysis_profiler_LocalVariableAccessData)
gen_analysis_profiler_SharedVariableAccessData_MemoryAccessData = Generalization(general=MemoryAccessData, specific=analysis_profiler_SharedVariableAccessData)
gen_analysis_profiler_BenchmarkReport_AnalysisReport = Generalization(general=AnalysisReport, specific=analysis_profiler_BenchmarkReport)
gen_analysis_profiler_StateVariableAccessData_MemoryAccessData = Generalization(general=MemoryAccessData, specific=analysis_profiler_StateVariableAccessData)
gen_analysis_trace_TraceSizeReport_AnalysisReport = Generalization(general=AnalysisReport, specific=analysis_trace_TraceSizeReport)
gen_analysis_trace_CompressedTraceReport_AnalysisReport = Generalization(general=AnalysisReport, specific=analysis_trace_CompressedTraceReport)
gen_analysis_trace_CompressedFsmDependency_CompressedDependency = Generalization(general=CompressedDependency, specific=analysis_trace_CompressedFsmDependency)
gen_analysis_trace_CompressedGuardDependency_CompressedDependency = Generalization(general=CompressedDependency, specific=analysis_trace_CompressedGuardDependency)
gen_analysis_trace_CompressedVariableDependency_CompressedDependency = Generalization(general=CompressedDependency, specific=analysis_trace_CompressedVariableDependency)
gen_analysis_trace_CompressedPortDependency_CompressedDependency = Generalization(general=CompressedDependency, specific=analysis_trace_CompressedPortDependency)
gen_analysis_trace_CompressedTokensDependency_CompressedDependency = Generalization(general=CompressedDependency, specific=analysis_trace_CompressedTokensDependency)
gen_analysis_trace_TraceComparatorReport_AnalysisReport = Generalization(general=AnalysisReport, specific=analysis_trace_TraceComparatorReport)
gen_analysis_trace_MarkowModelTraceReport_AnalysisReport = Generalization(general=AnalysisReport, specific=analysis_trace_MarkowModelTraceReport)
gen_analysis_bottlenecks_BottlenecksReport_AnalysisReport = Generalization(general=AnalysisReport, specific=analysis_bottlenecks_BottlenecksReport)
gen_analysis_bottlenecks_ImpactAnalysisReport_AnalysisReport = Generalization(general=AnalysisReport, specific=analysis_bottlenecks_ImpactAnalysisReport)
gen_analysis_bottlenecks_BottlenecksWithSchedulingReport_AnalysisReport = Generalization(general=AnalysisReport, specific=analysis_bottlenecks_BottlenecksWithSchedulingReport)
gen_analysis_bottlenecks_BottlenecksWithSchedulingReport_postprocessing_PostProcessingData = Generalization(general=postprocessing_PostProcessingData, specific=analysis_bottlenecks_BottlenecksWithSchedulingReport)
gen_analysis_bottlenecks_ScheduledImpactAnalysisReport_AnalysisReport = Generalization(general=AnalysisReport, specific=analysis_bottlenecks_ScheduledImpactAnalysisReport)
gen_analysis_buffers_BoundedBuffersReport_AnalysisReport = Generalization(general=AnalysisReport, specific=analysis_buffers_BoundedBuffersReport)
gen_analysis_buffers_OptimalBuffersReport_AnalysisReport = Generalization(general=AnalysisReport, specific=analysis_buffers_OptimalBuffersReport)
gen_analysis_partitioning_ComCostPartitioningReport_AnalysisReport = Generalization(general=AnalysisReport, specific=analysis_partitioning_ComCostPartitioningReport)
gen_analysis_partitioning_WorkloadBalancePartitioningReport_AnalysisReport = Generalization(general=AnalysisReport, specific=analysis_partitioning_WorkloadBalancePartitioningReport)
gen_analysis_partitioning_BalancedPipelinePartitioningReport_AnalysisReport = Generalization(general=AnalysisReport, specific=analysis_partitioning_BalancedPipelinePartitioningReport)
gen_analysis_pipelining_ActionsVariablePipeliningReport_AnalysisReport = Generalization(general=AnalysisReport, specific=analysis_pipelining_ActionsVariablePipeliningReport)
gen_analysis_pipelining_ImpactAnalysisReport_AnalysisReport = Generalization(general=AnalysisReport, specific=analysis_pipelining_ImpactAnalysisReport)
gen_analysis_postprocessing_PostProcessingReport_AnalysisReport = Generalization(general=AnalysisReport, specific=analysis_postprocessing_PostProcessingReport)
gen_analysis_postprocessing_ActorStatisticsReport_PostProcessingData = Generalization(general=PostProcessingData, specific=analysis_postprocessing_ActorStatisticsReport)
gen_analysis_postprocessing_ActionStatisticsReport_PostProcessingData = Generalization(general=PostProcessingData, specific=analysis_postprocessing_ActionStatisticsReport)
gen_analysis_postprocessing_SchedulerChecksReport_PostProcessingData = Generalization(general=PostProcessingData, specific=analysis_postprocessing_SchedulerChecksReport)
gen_analysis_postprocessing_BufferBlockingReport_PostProcessingData = Generalization(general=PostProcessingData, specific=analysis_postprocessing_BufferBlockingReport)
gen_analysis_profiling_IntraActionCommunicationReport_AnalysisReport = Generalization(general=AnalysisReport, specific=analysis_profiling_IntraActionCommunicationReport)
gen_analysis_profiling_ProfilingStatsReport_AnalysisReport = Generalization(general=AnalysisReport, specific=analysis_profiling_ProfilingStatsReport)
gen_analysis_scheduling_ActorFire_ActorSelectionSchedule = Generalization(general=ActorSelectionSchedule, specific=analysis_scheduling_ActorFire)
gen_analysis_scheduling_FSM_ActorSelectionSchedule = Generalization(general=ActorSelectionSchedule, specific=analysis_scheduling_FSM)
gen_analysis_scheduling_Sequence_ActorSelectionSchedule = Generalization(general=ActorSelectionSchedule, specific=analysis_scheduling_Sequence)
gen_analysis_scheduling_FSMTransitionWithState_FSMTransition = Generalization(general=FSMTransition, specific=analysis_scheduling_FSMTransitionWithState)
gen_analysis_scheduling_PartitionedActorFire_ActorFire = Generalization(general=ActorFire, specific=analysis_scheduling_PartitionedActorFire)
gen_analysis_scheduling_MarkovSimpleSchedulerReport_AnalysisReport = Generalization(general=AnalysisReport, specific=analysis_scheduling_MarkovSimpleSchedulerReport)
gen_analysis_scheduling_MarkovSimpleSchedulerReport_postprocessing_PostProcessingData = Generalization(general=postprocessing_PostProcessingData, specific=analysis_scheduling_MarkovSimpleSchedulerReport)
gen_analysis_caseoptimal_CaseOptimalScheduleReport_AnalysisReport = Generalization(general=AnalysisReport, specific=analysis_caseoptimal_CaseOptimalScheduleReport)
gen_analysis_caseoptimal_CaseOptimalActorSelectionSchedule_ActorSelectionSchedule = Generalization(general=ActorSelectionSchedule, specific=analysis_caseoptimal_CaseOptimalActorSelectionSchedule)

# Domain Model
domain_model = DomainModel(
    name="analysis",
    types={analysis_AnalysisReport, analysis_profiler_CodeProfilingReport, AnalysisReport, profiler_analysis_Network, ComplexCodeData, analysis_profiler_CodeData, StringToIntegerMap, analysis_profiler_ComplexCodeData, CodeData, analysis_profiler_DynamicProfilingReport, ActorDynamicData, BufferDynamicData, analysis_profiler_ActorDynamicData, ComplexDynamicData, profiler_analysis_Actor, analysis_profiler_ActionDynamicData, profiler_analysis_Action, analysis_profiler_BufferDynamicData, profiler_analysis_Buffer, profiler_analysis_StatisticalData, ActionToStatisticalDataMap, ActionToLongMap, analysis_profiler_ComplexDynamicData, EOperatorToStatisticalDataMap, ProcedureToStatisticalDataMap, VariableToStatisticalDataMap, ProcedureToComplexDynamicDataMap, BufferToStatisticalDataMap, analysis_profiler_ProcedureToComplexDynamicDataMap, ActionDynamicData, analysis_profiler_MemoryProfilingReport, ActionMemoryProfilingData, analysis_profiler_ActionMemoryProfilingData, MemoryAccessData, analysis_profiler_MemoryAccessData, StringToAccessDataMap, analysis_profiler_BufferAccessData, profiler_analysis_Procedure, analysis_profiler_SharedVariableAccessData, analysis_profiler_AccessData, analysis_profiler_StringToAccessDataMap, AccessData, analysis_profiler_BenchmarkReport, TableRow, analysis_profiler_TableRow, StringToStringMap, analysis_map_StringToIntegerMap, analysis_map_ActorToStatisticalDataMap, map_analysis_Actor, map_analysis_StatisticalData, analysis_map_ActionToStatisticalDataMap, map_analysis_Action, analysis_map_BufferToStatisticalDataMap, map_analysis_Buffer, analysis_map_ProcedureToStatisticalDataMap, analysis_profiler_StateVariableAccessData, analysis_profiler_LocalVariableAccessData, analysis_map_VariableToStatisticalDataMap, map_analysis_Variable, analysis_map_ActorClassToStatisticalDataMap, map_analysis_ActorClass, analysis_map_EOperatorToStatisticalDataMap, analysis_map_ActionToLongMap, analysis_map_ActorToLongMap, analysis_map_BufferToLongMap, analysis_map_StringToLongMap, analysis_map_DoubleToDoubleMap, analysis_map_VariableToLongMap, analysis_map_GuardToLongMap, map_analysis_Guard, analysis_map_PortToLongMap, map_analysis_Port, analysis_map_StringToDoubleMap, map_analysis_Procedure, analysis_map_BufferToIntegerMap, analysis_map_BufferToDoubleMap, analysis_map_PartitionToActorSelectionScheduleMap, ActorSelectionSchedule, analysis_map_StringToStringMap, analysis_trace_TraceSizeReport, ActorToLongMap, analysis_map_ActionToDoubleMap, StringToLongMap, trace_analysis_Network, analysis_trace_CompressedTraceReport, CompressedStep, CompressedDependency, analysis_trace_CompressedStep, trace_analysis_Action, analysis_trace_CompressedDependency, analysis_trace_CompressedFsmDependency, analysis_trace_CompressedGuardDependency, GuardToLongMap, analysis_trace_CompressedVariableDependency, VariableToLongMap, analysis_trace_CompressedPortDependency, PortToLongMap, analysis_trace_CompressedTokensDependency, BufferToLongMap, analysis_trace_TraceComparatorReport, CompressedTraceReport, ComparedTrace, analysis_trace_ComparedTrace, bottlenecks_analysis_Action, ComparedAction, analysis_trace_ComparedAction, analysis_trace_MarkowModelTraceReport, MarkovModelActionData, analysis_trace_MarkovModelActionData, analysis_bottlenecks_BottlenecksReport, bottlenecks_analysis_Network, ActionBottlenecksData, analysis_bottlenecks_ActionBottlenecksData, analysis_bottlenecks_ImpactAnalysisReport, ImpactAnalysisData, BottlenecksReport, analysis_bottlenecks_ImpactAnalysisData, bottlenecks_analysis_ActorClass, DoubleToDoubleMap, DoubleToBottlenecksReportMap, analysis_bottlenecks_DoubleToBottlenecksReportMap, analysis_bottlenecks_BottlenecksWithSchedulingReport, postprocessing_PostProcessingData, ActionBottlenecksWithSchedulingData, StringToDoubleMap, analysis_bottlenecks_ActionBottlenecksWithSchedulingData, BufferToIntegerMap, BufferToDoubleMap, analysis_bottlenecks_ScheduledImpactAnalysisData, DoubleToBottlenecksWithSchedulingReportMap, analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap, BottlenecksWithSchedulingReport, analysis_bottlenecks_ScheduledImpactAnalysisReport, analysis_buffers_BoundedBuffersReport, buffers_analysis_Network, BoundedBufferData, analysis_buffers_BoundedBufferData, buffers_analysis_Buffer, analysis_buffers_OptimalBuffersReport, OptimalBufferData, BoundedBuffersReport, analysis_buffers_OptimalBufferData, analysis_partitioning_ComCostPartitioningReport, partitioning_analysis_Network, ComCostPartition, ScheduledImpactAnalysisData, analysis_partitioning_WorkloadBalancePartition, analysis_partitioning_WorkloadBalancePartitioningReport, WorkloadBalancePartition, analysis_partitioning_BalancedPipelinePartition, analysis_partitioning_BalancedPipelinePartitioningReport, analysis_partitioning_ComCostPartition, partitioning_analysis_Actor, BalancedPipelinePartition, analysis_pipelining_ActionsVariablePipeliningReport, pipelining_analysis_Network, ActionVariablePipeliningData, analysis_pipelining_ActionVariablePipeliningData, pipelining_analysis_Action, pipelining_analysis_StatisticalData, analysis_pipelining_ImpactAnalysisReport, ActionsVariablePipeliningReport, analysis_pipelining_ImpactAnalysisData, analysis_postprocessing_PostProcessingReport, postprocessing_analysis_Network, PostProcessingData, analysis_postprocessing_PostProcessingData, analysis_postprocessing_ActorStatisticsReport, StatisticalActorPartition, analysis_postprocessing_StatisticalActorPartition, analysis_postprocessing_ActionStatisticsReport, postprocessing_analysis_Actor, ActionToDoubleMap, pipelining_analysis_ActorClass, analysis_postprocessing_SchedulerChecksReport, SchedulerChecksPartition, analysis_postprocessing_SchedulerChecksPartition, postprocessing_analysis_StatisticalData, ActorToStatisticalDataMap, analysis_postprocessing_BufferBlockingReport, analysis_profiling_IntraActionCommunicationReport, IntraActorCommunicationData, profiling_analysis_Network, profiling_analysis_StatisticalData, IntraActionCommunicationData, analysis_profiling_IntraActionCommunicationData, profiling_analysis_Action, analysis_profiling_ProfilingStatsReport, ProfilingStatsActorData, analysis_profiling_ProfilingStatsActorData, analysis_scheduling_ActorFire, analysis_scheduling_FSM, FSMState, analysis_profiling_IntraActorCommunicationData, profiling_analysis_Actor, analysis_scheduling_ActorSelectionSchedule, analysis_scheduling_Sequence, ActorFire, analysis_scheduling_FSMVar, analysis_scheduling_FSMTransition, FSMCondition, Sequence, analysis_scheduling_FSMState, FSMVarUpdate, FSMTransition, analysis_scheduling_FSMVarUpdate, FSMOperation, analysis_scheduling_FSMOperation, FSMVar, analysis_scheduling_FSMCombination, analysis_scheduling_FSMCondition, FSMCombination, analysis_scheduling_FSMTransitionWithState, analysis_scheduling_PartitionedActorFire, analysis_scheduling_MarkovSimpleSchedulerReport, MarkovPartitionScheduler, scheduling_analysis_Network, analysis_scheduling_MarkovPartitionScheduler, scheduling_analysis_Actor, MarkovSchedulingState, MarkovSchedulingTransition, analysis_scheduling_MarkovSchedulingState, analysis_caseoptimal_CaseOptimalScheduleReport, PartitionToActorSelectionScheduleMap, analysis_caseoptimal_CaseOptimalActorSelectionSchedule, analysis_scheduling_MarkovSchedulingTransition, FSMOp, FSMComparator, FSMCombinator, Optimizer},
    associations={network0, actorClassesData1, operatorsCount6, operandsCount7, actionsData10, proceduresData11, network14, actorsData16, buffersData18, networkData3, action23, buffer24, reads25, writes27, occupancy30, actionReads33, actionWrites35, actionPeeks38, actionReadMisses40, actionWriteMisses43, operandsCalls46, proceduresCalls47, variablesStores49, variablesLoads51, proceduresData54, readTokens56, writeTokens58, actor20, actionsData21, actionsData64, reads65, writes66, accessesData69, key61, value62, value70, rows71, cells72, key73, value74, key76, value77, key80, value81, key88, value89, key92, value93, value96, key98, key100, key102, key104, key106, key107, key84, value85, key108, key110, key112, value114, actionsFirings115, actionsIncomings117, actionsOutgoings120, actorsFirings123, actorsOutgoings128, dependenciesKinds131, network133, network135, steps137, dependencies139, action141, incomings142, outgoings144, predecessors146, successors149, neighbors152, actorsIncoming125, target157, enableMap159, disableMap160, readReadMap163, readWriteMap164, writeReadMap167, writeWriteMap170, readMap173, writeMap174, countMap177, tokensMap178, reference181, traces182, compressedTrace184, source155, containedReferenceActions186, actions189, action191, network193, actionsData195, action197, successorsMap199, network202, actionsData203, action205, network206, impactData208, initialBottlenecks210, actions212, actorClass214, cpReductionMap216, reportsMap218, value220, network222, actionsData224, cpPartitionsBlockingTime226, action228, maxBlockedOutputTokens230, maxBlockedMultiplication232, blockingInstances234, actions237, actorClass239, cpReductionMap242, timeReductionMap245, reportsMap248, value250, network251, initialBottlenecksWithScheduling255, network258, buffersData259, buffer261, network262, buffersData264, initialBufferConfiguration266, initialBottlenecks268, bufferData271, bottlenecksData273, network276, partitions277, scheduledImpactData253, internalCostMap280, externalCostMap283, actors286, network288, partitions290, actors292, actors279, partitions294, network295, network298, actionsData299, action301, consecutiveFirings302, pipelinableFirings304, network307, initialBottlenecks309, piplenablesActions312, impactData314, estimatedBottlenecks317, actions319, network324, reports325, network327, partitions329, idleTimes331, blockedReadingTimes334, blockedWritingTimes337, processingTimes340, actors343, idleTimes344, idleMinTimes346, idleMaxTimes349, blockedReadingTimes352, blockedReadingMinTimes355, actorClass322, blockedWritingTimes361, blockedWritingMinTimes364, blockedWritingMaxTimes367, processingTimes370, executionCounts373, partitions376, aggregatedCheckedData377, aggregatedFailedData378, checkedConditionsMap381, failedConditionsMap383, network386, maxBlockedOutputTokens388, maxBlockedMultiplication391, blockingInstances394, actorsData397, blockedReadingMaxTimes358, consumedTokens401, producedTokens403, tokensProducersMap406, actionsData409, action411, consumedTokens412, producedTokens415, tokensProducersMap418, actorsStatsData421, network398, actor400, actions425, cond426, transitionSchedule427, varUpdates429, transitions430, operation432, condition433, states422, vars423, cond436, combinedCond438, varStates439, partitions441, network442, actors444, states445, transitions447, actor449, outgoings451, incomings454, target460, partitionSchedules463, source457},
    generalizations={gen_analysis_profiler_CodeProfilingReport_AnalysisReport, gen_analysis_profiler_ComplexCodeData_CodeData, gen_analysis_profiler_DynamicProfilingReport_AnalysisReport, gen_analysis_profiler_ActorDynamicData_ComplexDynamicData, gen_analysis_profiler_ActionDynamicData_ComplexDynamicData, gen_analysis_profiler_MemoryProfilingReport_AnalysisReport, gen_analysis_profiler_BufferAccessData_MemoryAccessData, gen_analysis_profiler_LocalVariableAccessData_MemoryAccessData, gen_analysis_profiler_SharedVariableAccessData_MemoryAccessData, gen_analysis_profiler_BenchmarkReport_AnalysisReport, gen_analysis_profiler_StateVariableAccessData_MemoryAccessData, gen_analysis_trace_TraceSizeReport_AnalysisReport, gen_analysis_trace_CompressedTraceReport_AnalysisReport, gen_analysis_trace_CompressedFsmDependency_CompressedDependency, gen_analysis_trace_CompressedGuardDependency_CompressedDependency, gen_analysis_trace_CompressedVariableDependency_CompressedDependency, gen_analysis_trace_CompressedPortDependency_CompressedDependency, gen_analysis_trace_CompressedTokensDependency_CompressedDependency, gen_analysis_trace_TraceComparatorReport_AnalysisReport, gen_analysis_trace_MarkowModelTraceReport_AnalysisReport, gen_analysis_bottlenecks_BottlenecksReport_AnalysisReport, gen_analysis_bottlenecks_ImpactAnalysisReport_AnalysisReport, gen_analysis_bottlenecks_BottlenecksWithSchedulingReport_AnalysisReport, gen_analysis_bottlenecks_BottlenecksWithSchedulingReport_postprocessing_PostProcessingData, gen_analysis_bottlenecks_ScheduledImpactAnalysisReport_AnalysisReport, gen_analysis_buffers_BoundedBuffersReport_AnalysisReport, gen_analysis_buffers_OptimalBuffersReport_AnalysisReport, gen_analysis_partitioning_ComCostPartitioningReport_AnalysisReport, gen_analysis_partitioning_WorkloadBalancePartitioningReport_AnalysisReport, gen_analysis_partitioning_BalancedPipelinePartitioningReport_AnalysisReport, gen_analysis_pipelining_ActionsVariablePipeliningReport_AnalysisReport, gen_analysis_pipelining_ImpactAnalysisReport_AnalysisReport, gen_analysis_postprocessing_PostProcessingReport_AnalysisReport, gen_analysis_postprocessing_ActorStatisticsReport_PostProcessingData, gen_analysis_postprocessing_ActionStatisticsReport_PostProcessingData, gen_analysis_postprocessing_SchedulerChecksReport_PostProcessingData, gen_analysis_postprocessing_BufferBlockingReport_PostProcessingData, gen_analysis_profiling_IntraActionCommunicationReport_AnalysisReport, gen_analysis_profiling_ProfilingStatsReport_AnalysisReport, gen_analysis_scheduling_ActorFire_ActorSelectionSchedule, gen_analysis_scheduling_FSM_ActorSelectionSchedule, gen_analysis_scheduling_Sequence_ActorSelectionSchedule, gen_analysis_scheduling_FSMTransitionWithState_FSMTransition, gen_analysis_scheduling_PartitionedActorFire_ActorFire, gen_analysis_scheduling_MarkovSimpleSchedulerReport_AnalysisReport, gen_analysis_scheduling_MarkovSimpleSchedulerReport_postprocessing_PostProcessingData, gen_analysis_caseoptimal_CaseOptimalScheduleReport_AnalysisReport, gen_analysis_caseoptimal_CaseOptimalActorSelectionSchedule_ActorSelectionSchedule},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)