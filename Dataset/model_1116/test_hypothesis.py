import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    analysis_pipelining_ImpactAnalysisData,
    ActionsVariablePipeliningReport,
    pipelining_analysis_StatisticalData,
    pipelining_analysis_Action,
    analysis_pipelining_ActionVariablePipeliningData,
    ActionVariablePipeliningData,
    pipelining_analysis_Network,
    BalancedPipelinePartition,
    partitioning_analysis_Actor,
    analysis_partitioning_ComCostPartition,
    analysis_partitioning_BalancedPipelinePartition,
    WorkloadBalancePartition,
    analysis_partitioning_WorkloadBalancePartition,
    ScheduledImpactAnalysisData,
    ComCostPartition,
    partitioning_analysis_Network,
    analysis_buffers_OptimalBufferData,
    BoundedBuffersReport,
    OptimalBufferData,
    buffers_analysis_Buffer,
    analysis_buffers_BoundedBufferData,
    BoundedBufferData,
    buffers_analysis_Network,
    BottlenecksWithSchedulingReport,
    analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap,
    DoubleToBottlenecksWithSchedulingReportMap,
    analysis_bottlenecks_ScheduledImpactAnalysisData,
    BufferToDoubleMap,
    BufferToIntegerMap,
    analysis_bottlenecks_ActionBottlenecksWithSchedulingData,
    StringToDoubleMap,
    ActionBottlenecksWithSchedulingData,
    postprocessing_PostProcessingData,
    analysis_bottlenecks_DoubleToBottlenecksReportMap,
    DoubleToBottlenecksReportMap,
    DoubleToDoubleMap,
    bottlenecks_analysis_ActorClass,
    analysis_bottlenecks_ImpactAnalysisData,
    BottlenecksReport,
    ImpactAnalysisData,
    analysis_bottlenecks_ActionBottlenecksData,
    ActionBottlenecksData,
    bottlenecks_analysis_Network,
    analysis_trace_MarkovModelActionData,
    MarkovModelActionData,
    analysis_trace_ComparedAction,
    ComparedAction,
    bottlenecks_analysis_Action,
    analysis_trace_ComparedTrace,
    ComparedTrace,
    CompressedTraceReport,
    BufferToLongMap,
    PortToLongMap,
    VariableToLongMap,
    GuardToLongMap,
    analysis_trace_CompressedDependency,
    trace_analysis_Action,
    analysis_trace_CompressedStep,
    CompressedDependency,
    analysis_trace_CompressedVariableDependency,
    analysis_trace_CompressedFsmDependency,
    analysis_trace_CompressedTokensDependency,
    analysis_trace_CompressedPortDependency,
    analysis_trace_CompressedGuardDependency,
    CompressedStep,
    trace_analysis_Network,
    StringToLongMap,
    analysis_map_ActionToDoubleMap,
    ActorToLongMap,
    analysis_map_StringToStringMap,
    ActorSelectionSchedule,
    analysis_map_PartitionToActorSelectionScheduleMap,
    analysis_map_BufferToDoubleMap,
    analysis_map_BufferToIntegerMap,
    map_analysis_Procedure,
    analysis_map_StringToDoubleMap,
    map_analysis_Port,
    analysis_map_PortToLongMap,
    map_analysis_Guard,
    analysis_map_GuardToLongMap,
    analysis_map_VariableToLongMap,
    analysis_map_DoubleToDoubleMap,
    analysis_map_StringToLongMap,
    analysis_map_BufferToLongMap,
    analysis_map_ActorToLongMap,
    analysis_map_ActionToLongMap,
    analysis_map_EOperatorToStatisticalDataMap,
    map_analysis_ActorClass,
    analysis_map_ActorClassToStatisticalDataMap,
    map_analysis_Variable,
    analysis_map_VariableToStatisticalDataMap,
    analysis_map_ProcedureToStatisticalDataMap,
    map_analysis_Buffer,
    analysis_map_BufferToStatisticalDataMap,
    map_analysis_Action,
    analysis_map_ActionToStatisticalDataMap,
    map_analysis_StatisticalData,
    map_analysis_Actor,
    analysis_map_ActorToStatisticalDataMap,
    analysis_map_StringToIntegerMap,
    StringToStringMap,
    analysis_profiler_TableRow,
    TableRow,
    AccessData,
    analysis_profiler_StringToAccessDataMap,
    analysis_profiler_AccessData,
    profiler_analysis_Procedure,
    StringToAccessDataMap,
    analysis_profiler_MemoryAccessData,
    MemoryAccessData,
    analysis_profiler_StateVariableAccessData,
    analysis_profiler_LocalVariableAccessData,
    analysis_profiler_SharedVariableAccessData,
    analysis_profiler_BufferAccessData,
    analysis_profiler_ActionMemoryProfilingData,
    ActionMemoryProfilingData,
    ActionDynamicData,
    analysis_profiler_ProcedureToComplexDynamicDataMap,
    BufferToStatisticalDataMap,
    ProcedureToComplexDynamicDataMap,
    VariableToStatisticalDataMap,
    ProcedureToStatisticalDataMap,
    EOperatorToStatisticalDataMap,
    analysis_profiler_ComplexDynamicData,
    ActionToLongMap,
    ActionToStatisticalDataMap,
    profiler_analysis_StatisticalData,
    profiler_analysis_Buffer,
    analysis_profiler_BufferDynamicData,
    profiler_analysis_Action,
    profiler_analysis_Actor,
    ComplexDynamicData,
    analysis_profiler_ActionDynamicData,
    analysis_profiler_ActorDynamicData,
    BufferDynamicData,
    ActorDynamicData,
    CodeData,
    analysis_profiler_ComplexCodeData,
    StringToIntegerMap,
    analysis_profiler_CodeData,
    ComplexCodeData,
    profiler_analysis_Network,
    AnalysisReport,
    analysis_profiler_MemoryProfilingReport,
    analysis_partitioning_ComCostPartitioningReport,
    analysis_trace_TraceSizeReport,
    analysis_bottlenecks_ScheduledImpactAnalysisReport,
    analysis_pipelining_ImpactAnalysisReport,
    analysis_buffers_OptimalBuffersReport,
    analysis_profiler_BenchmarkReport,
    analysis_profiler_DynamicProfilingReport,
    analysis_trace_TraceComparatorReport,
    analysis_bottlenecks_BottlenecksWithSchedulingReport,
    analysis_trace_CompressedTraceReport,
    analysis_pipelining_ActionsVariablePipeliningReport,
    analysis_buffers_BoundedBuffersReport,
    analysis_partitioning_WorkloadBalancePartitioningReport,
    analysis_bottlenecks_BottlenecksReport,
    analysis_trace_MarkowModelTraceReport,
    analysis_bottlenecks_ImpactAnalysisReport,
    analysis_partitioning_BalancedPipelinePartitioningReport,
    analysis_profiler_CodeProfilingReport,
    analysis_AnalysisReport,
    analysis_scheduling_MarkovSchedulingTransition,
    analysis_caseoptimal_CaseOptimalActorSelectionSchedule,
    PartitionToActorSelectionScheduleMap,
    analysis_caseoptimal_CaseOptimalScheduleReport,
    analysis_scheduling_MarkovSchedulingState,
    MarkovSchedulingTransition,
    MarkovSchedulingState,
    scheduling_analysis_Actor,
    analysis_scheduling_MarkovPartitionScheduler,
    scheduling_analysis_Network,
    MarkovPartitionScheduler,
    analysis_scheduling_MarkovSimpleSchedulerReport,
    FSMCombination,
    analysis_scheduling_FSMCondition,
    analysis_scheduling_FSMCombination,
    FSMVar,
    analysis_scheduling_FSMOperation,
    FSMOperation,
    analysis_scheduling_FSMVarUpdate,
    FSMTransition,
    analysis_scheduling_FSMTransitionWithState,
    FSMVarUpdate,
    analysis_scheduling_FSMState,
    Sequence,
    FSMCondition,
    analysis_scheduling_FSMTransition,
    analysis_scheduling_FSMVar,
    ActorFire,
    analysis_scheduling_PartitionedActorFire,
    analysis_scheduling_Sequence,
    analysis_scheduling_ActorSelectionSchedule,
    profiling_analysis_Actor,
    analysis_profiling_IntraActorCommunicationData,
    FSMState,
    analysis_scheduling_FSM,
    analysis_scheduling_ActorFire,
    analysis_profiling_ProfilingStatsActorData,
    ProfilingStatsActorData,
    analysis_profiling_ProfilingStatsReport,
    profiling_analysis_Action,
    analysis_profiling_IntraActionCommunicationData,
    IntraActionCommunicationData,
    profiling_analysis_StatisticalData,
    profiling_analysis_Network,
    IntraActorCommunicationData,
    analysis_profiling_IntraActionCommunicationReport,
    ActorToStatisticalDataMap,
    postprocessing_analysis_StatisticalData,
    analysis_postprocessing_SchedulerChecksPartition,
    SchedulerChecksPartition,
    pipelining_analysis_ActorClass,
    ActionToDoubleMap,
    postprocessing_analysis_Actor,
    analysis_postprocessing_StatisticalActorPartition,
    StatisticalActorPartition,
    analysis_postprocessing_PostProcessingData,
    PostProcessingData,
    analysis_postprocessing_ActorStatisticsReport,
    analysis_postprocessing_BufferBlockingReport,
    analysis_postprocessing_ActionStatisticsReport,
    analysis_postprocessing_SchedulerChecksReport,
    postprocessing_analysis_Network,
    analysis_postprocessing_PostProcessingReport,
    FSMOp,
    FSMCombinator,
    Optimizer,
    FSMComparator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_analysis_pipelining_impactanalysisdata_is_not_abstract():
    assert not inspect.isabstract(analysis_pipelining_ImpactAnalysisData)


def test_analysis_pipelining_impactanalysisdata_constructor_exists():
    assert callable(analysis_pipelining_ImpactAnalysisData.__init__)


def test_analysis_pipelining_impactanalysisdata_constructor_args():
    sig = inspect.signature(analysis_pipelining_ImpactAnalysisData.__init__)
    params = list(sig.parameters.keys())
    assert "cpReduction" in params, "Missing parameter 'cpReduction'"

def test_analysis_pipelining_impactanalysisdata_has_cpReduction():
    assert hasattr(analysis_pipelining_ImpactAnalysisData, "cpReduction")
    descriptor = None
    for klass in analysis_pipelining_ImpactAnalysisData.__mro__:
        if "cpReduction" in klass.__dict__:
            descriptor = klass.__dict__["cpReduction"]
            break
    assert isinstance(descriptor, property)



def test_actionsvariablepipeliningreport_is_not_abstract():
    assert not inspect.isabstract(ActionsVariablePipeliningReport)


def test_actionsvariablepipeliningreport_constructor_exists():
    assert callable(ActionsVariablePipeliningReport.__init__)


def test_actionsvariablepipeliningreport_constructor_args():
    sig = inspect.signature(ActionsVariablePipeliningReport.__init__)
    params = list(sig.parameters.keys())



def test_pipelining_analysis_statisticaldata_is_not_abstract():
    assert not inspect.isabstract(pipelining_analysis_StatisticalData)


def test_pipelining_analysis_statisticaldata_constructor_exists():
    assert callable(pipelining_analysis_StatisticalData.__init__)


def test_pipelining_analysis_statisticaldata_constructor_args():
    sig = inspect.signature(pipelining_analysis_StatisticalData.__init__)
    params = list(sig.parameters.keys())



def test_pipelining_analysis_action_is_not_abstract():
    assert not inspect.isabstract(pipelining_analysis_Action)


def test_pipelining_analysis_action_constructor_exists():
    assert callable(pipelining_analysis_Action.__init__)


def test_pipelining_analysis_action_constructor_args():
    sig = inspect.signature(pipelining_analysis_Action.__init__)
    params = list(sig.parameters.keys())



def test_analysis_pipelining_actionvariablepipeliningdata_is_not_abstract():
    assert not inspect.isabstract(analysis_pipelining_ActionVariablePipeliningData)


def test_analysis_pipelining_actionvariablepipeliningdata_constructor_exists():
    assert callable(analysis_pipelining_ActionVariablePipeliningData.__init__)


def test_analysis_pipelining_actionvariablepipeliningdata_constructor_args():
    sig = inspect.signature(analysis_pipelining_ActionVariablePipeliningData.__init__)
    params = list(sig.parameters.keys())
    assert "pipelinable" in params, "Missing parameter 'pipelinable'"

def test_analysis_pipelining_actionvariablepipeliningdata_has_pipelinable():
    assert hasattr(analysis_pipelining_ActionVariablePipeliningData, "pipelinable")
    descriptor = None
    for klass in analysis_pipelining_ActionVariablePipeliningData.__mro__:
        if "pipelinable" in klass.__dict__:
            descriptor = klass.__dict__["pipelinable"]
            break
    assert isinstance(descriptor, property)



def test_actionvariablepipeliningdata_is_not_abstract():
    assert not inspect.isabstract(ActionVariablePipeliningData)


def test_actionvariablepipeliningdata_constructor_exists():
    assert callable(ActionVariablePipeliningData.__init__)


def test_actionvariablepipeliningdata_constructor_args():
    sig = inspect.signature(ActionVariablePipeliningData.__init__)
    params = list(sig.parameters.keys())



def test_pipelining_analysis_network_is_not_abstract():
    assert not inspect.isabstract(pipelining_analysis_Network)


def test_pipelining_analysis_network_constructor_exists():
    assert callable(pipelining_analysis_Network.__init__)


def test_pipelining_analysis_network_constructor_args():
    sig = inspect.signature(pipelining_analysis_Network.__init__)
    params = list(sig.parameters.keys())



def test_balancedpipelinepartition_is_not_abstract():
    assert not inspect.isabstract(BalancedPipelinePartition)


def test_balancedpipelinepartition_constructor_exists():
    assert callable(BalancedPipelinePartition.__init__)


def test_balancedpipelinepartition_constructor_args():
    sig = inspect.signature(BalancedPipelinePartition.__init__)
    params = list(sig.parameters.keys())



def test_partitioning_analysis_actor_is_not_abstract():
    assert not inspect.isabstract(partitioning_analysis_Actor)


def test_partitioning_analysis_actor_constructor_exists():
    assert callable(partitioning_analysis_Actor.__init__)


def test_partitioning_analysis_actor_constructor_args():
    sig = inspect.signature(partitioning_analysis_Actor.__init__)
    params = list(sig.parameters.keys())



def test_analysis_partitioning_comcostpartition_is_not_abstract():
    assert not inspect.isabstract(analysis_partitioning_ComCostPartition)


def test_analysis_partitioning_comcostpartition_constructor_exists():
    assert callable(analysis_partitioning_ComCostPartition.__init__)


def test_analysis_partitioning_comcostpartition_constructor_args():
    sig = inspect.signature(analysis_partitioning_ComCostPartition.__init__)
    params = list(sig.parameters.keys())
    assert "internalCost" in params, "Missing parameter 'internalCost'"
    assert "externalCost" in params, "Missing parameter 'externalCost'"

def test_analysis_partitioning_comcostpartition_has_internalCost():
    assert hasattr(analysis_partitioning_ComCostPartition, "internalCost")
    descriptor = None
    for klass in analysis_partitioning_ComCostPartition.__mro__:
        if "internalCost" in klass.__dict__:
            descriptor = klass.__dict__["internalCost"]
            break
    assert isinstance(descriptor, property)

def test_analysis_partitioning_comcostpartition_has_externalCost():
    assert hasattr(analysis_partitioning_ComCostPartition, "externalCost")
    descriptor = None
    for klass in analysis_partitioning_ComCostPartition.__mro__:
        if "externalCost" in klass.__dict__:
            descriptor = klass.__dict__["externalCost"]
            break
    assert isinstance(descriptor, property)



def test_analysis_partitioning_balancedpipelinepartition_is_not_abstract():
    assert not inspect.isabstract(analysis_partitioning_BalancedPipelinePartition)


def test_analysis_partitioning_balancedpipelinepartition_constructor_exists():
    assert callable(analysis_partitioning_BalancedPipelinePartition.__init__)


def test_analysis_partitioning_balancedpipelinepartition_constructor_args():
    sig = inspect.signature(analysis_partitioning_BalancedPipelinePartition.__init__)
    params = list(sig.parameters.keys())
    assert "workload" in params, "Missing parameter 'workload'"
    assert "commonPredAvg" in params, "Missing parameter 'commonPredAvg'"
    assert "preWorkload" in params, "Missing parameter 'preWorkload'"

def test_analysis_partitioning_balancedpipelinepartition_has_workload():
    assert hasattr(analysis_partitioning_BalancedPipelinePartition, "workload")
    descriptor = None
    for klass in analysis_partitioning_BalancedPipelinePartition.__mro__:
        if "workload" in klass.__dict__:
            descriptor = klass.__dict__["workload"]
            break
    assert isinstance(descriptor, property)

def test_analysis_partitioning_balancedpipelinepartition_has_commonPredAvg():
    assert hasattr(analysis_partitioning_BalancedPipelinePartition, "commonPredAvg")
    descriptor = None
    for klass in analysis_partitioning_BalancedPipelinePartition.__mro__:
        if "commonPredAvg" in klass.__dict__:
            descriptor = klass.__dict__["commonPredAvg"]
            break
    assert isinstance(descriptor, property)

def test_analysis_partitioning_balancedpipelinepartition_has_preWorkload():
    assert hasattr(analysis_partitioning_BalancedPipelinePartition, "preWorkload")
    descriptor = None
    for klass in analysis_partitioning_BalancedPipelinePartition.__mro__:
        if "preWorkload" in klass.__dict__:
            descriptor = klass.__dict__["preWorkload"]
            break
    assert isinstance(descriptor, property)



def test_workloadbalancepartition_is_not_abstract():
    assert not inspect.isabstract(WorkloadBalancePartition)


def test_workloadbalancepartition_constructor_exists():
    assert callable(WorkloadBalancePartition.__init__)


def test_workloadbalancepartition_constructor_args():
    sig = inspect.signature(WorkloadBalancePartition.__init__)
    params = list(sig.parameters.keys())



def test_analysis_partitioning_workloadbalancepartition_is_not_abstract():
    assert not inspect.isabstract(analysis_partitioning_WorkloadBalancePartition)


def test_analysis_partitioning_workloadbalancepartition_constructor_exists():
    assert callable(analysis_partitioning_WorkloadBalancePartition.__init__)


def test_analysis_partitioning_workloadbalancepartition_constructor_args():
    sig = inspect.signature(analysis_partitioning_WorkloadBalancePartition.__init__)
    params = list(sig.parameters.keys())
    assert "workload" in params, "Missing parameter 'workload'"

def test_analysis_partitioning_workloadbalancepartition_has_workload():
    assert hasattr(analysis_partitioning_WorkloadBalancePartition, "workload")
    descriptor = None
    for klass in analysis_partitioning_WorkloadBalancePartition.__mro__:
        if "workload" in klass.__dict__:
            descriptor = klass.__dict__["workload"]
            break
    assert isinstance(descriptor, property)



def test_scheduledimpactanalysisdata_is_not_abstract():
    assert not inspect.isabstract(ScheduledImpactAnalysisData)


def test_scheduledimpactanalysisdata_constructor_exists():
    assert callable(ScheduledImpactAnalysisData.__init__)


def test_scheduledimpactanalysisdata_constructor_args():
    sig = inspect.signature(ScheduledImpactAnalysisData.__init__)
    params = list(sig.parameters.keys())



def test_comcostpartition_is_not_abstract():
    assert not inspect.isabstract(ComCostPartition)


def test_comcostpartition_constructor_exists():
    assert callable(ComCostPartition.__init__)


def test_comcostpartition_constructor_args():
    sig = inspect.signature(ComCostPartition.__init__)
    params = list(sig.parameters.keys())



def test_partitioning_analysis_network_is_not_abstract():
    assert not inspect.isabstract(partitioning_analysis_Network)


def test_partitioning_analysis_network_constructor_exists():
    assert callable(partitioning_analysis_Network.__init__)


def test_partitioning_analysis_network_constructor_args():
    sig = inspect.signature(partitioning_analysis_Network.__init__)
    params = list(sig.parameters.keys())



def test_analysis_buffers_optimalbufferdata_is_not_abstract():
    assert not inspect.isabstract(analysis_buffers_OptimalBufferData)


def test_analysis_buffers_optimalbufferdata_constructor_exists():
    assert callable(analysis_buffers_OptimalBufferData.__init__)


def test_analysis_buffers_optimalbufferdata_constructor_args():
    sig = inspect.signature(analysis_buffers_OptimalBufferData.__init__)
    params = list(sig.parameters.keys())



def test_boundedbuffersreport_is_not_abstract():
    assert not inspect.isabstract(BoundedBuffersReport)


def test_boundedbuffersreport_constructor_exists():
    assert callable(BoundedBuffersReport.__init__)


def test_boundedbuffersreport_constructor_args():
    sig = inspect.signature(BoundedBuffersReport.__init__)
    params = list(sig.parameters.keys())



def test_optimalbufferdata_is_not_abstract():
    assert not inspect.isabstract(OptimalBufferData)


def test_optimalbufferdata_constructor_exists():
    assert callable(OptimalBufferData.__init__)


def test_optimalbufferdata_constructor_args():
    sig = inspect.signature(OptimalBufferData.__init__)
    params = list(sig.parameters.keys())



def test_buffers_analysis_buffer_is_not_abstract():
    assert not inspect.isabstract(buffers_analysis_Buffer)


def test_buffers_analysis_buffer_constructor_exists():
    assert callable(buffers_analysis_Buffer.__init__)


def test_buffers_analysis_buffer_constructor_args():
    sig = inspect.signature(buffers_analysis_Buffer.__init__)
    params = list(sig.parameters.keys())



def test_analysis_buffers_boundedbufferdata_is_not_abstract():
    assert not inspect.isabstract(analysis_buffers_BoundedBufferData)


def test_analysis_buffers_boundedbufferdata_constructor_exists():
    assert callable(analysis_buffers_BoundedBufferData.__init__)


def test_analysis_buffers_boundedbufferdata_constructor_args():
    sig = inspect.signature(analysis_buffers_BoundedBufferData.__init__)
    params = list(sig.parameters.keys())
    assert "bitSize" in params, "Missing parameter 'bitSize'"
    assert "tokenSize" in params, "Missing parameter 'tokenSize'"

def test_analysis_buffers_boundedbufferdata_has_bitSize():
    assert hasattr(analysis_buffers_BoundedBufferData, "bitSize")
    descriptor = None
    for klass in analysis_buffers_BoundedBufferData.__mro__:
        if "bitSize" in klass.__dict__:
            descriptor = klass.__dict__["bitSize"]
            break
    assert isinstance(descriptor, property)

def test_analysis_buffers_boundedbufferdata_has_tokenSize():
    assert hasattr(analysis_buffers_BoundedBufferData, "tokenSize")
    descriptor = None
    for klass in analysis_buffers_BoundedBufferData.__mro__:
        if "tokenSize" in klass.__dict__:
            descriptor = klass.__dict__["tokenSize"]
            break
    assert isinstance(descriptor, property)



def test_boundedbufferdata_is_not_abstract():
    assert not inspect.isabstract(BoundedBufferData)


def test_boundedbufferdata_constructor_exists():
    assert callable(BoundedBufferData.__init__)


def test_boundedbufferdata_constructor_args():
    sig = inspect.signature(BoundedBufferData.__init__)
    params = list(sig.parameters.keys())



def test_buffers_analysis_network_is_not_abstract():
    assert not inspect.isabstract(buffers_analysis_Network)


def test_buffers_analysis_network_constructor_exists():
    assert callable(buffers_analysis_Network.__init__)


def test_buffers_analysis_network_constructor_args():
    sig = inspect.signature(buffers_analysis_Network.__init__)
    params = list(sig.parameters.keys())



def test_bottleneckswithschedulingreport_is_not_abstract():
    assert not inspect.isabstract(BottlenecksWithSchedulingReport)


def test_bottleneckswithschedulingreport_constructor_exists():
    assert callable(BottlenecksWithSchedulingReport.__init__)


def test_bottleneckswithschedulingreport_constructor_args():
    sig = inspect.signature(BottlenecksWithSchedulingReport.__init__)
    params = list(sig.parameters.keys())



def test_analysis_bottlenecks_doubletobottleneckswithschedulingreportmap_is_not_abstract():
    assert not inspect.isabstract(analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap)


def test_analysis_bottlenecks_doubletobottleneckswithschedulingreportmap_constructor_exists():
    assert callable(analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap.__init__)


def test_analysis_bottlenecks_doubletobottleneckswithschedulingreportmap_constructor_args():
    sig = inspect.signature(analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_analysis_bottlenecks_doubletobottleneckswithschedulingreportmap_has_key():
    assert hasattr(analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap, "key")
    descriptor = None
    for klass in analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_doubletobottleneckswithschedulingreportmap_is_not_abstract():
    assert not inspect.isabstract(DoubleToBottlenecksWithSchedulingReportMap)


def test_doubletobottleneckswithschedulingreportmap_constructor_exists():
    assert callable(DoubleToBottlenecksWithSchedulingReportMap.__init__)


def test_doubletobottleneckswithschedulingreportmap_constructor_args():
    sig = inspect.signature(DoubleToBottlenecksWithSchedulingReportMap.__init__)
    params = list(sig.parameters.keys())



def test_analysis_bottlenecks_scheduledimpactanalysisdata_is_not_abstract():
    assert not inspect.isabstract(analysis_bottlenecks_ScheduledImpactAnalysisData)


def test_analysis_bottlenecks_scheduledimpactanalysisdata_constructor_exists():
    assert callable(analysis_bottlenecks_ScheduledImpactAnalysisData.__init__)


def test_analysis_bottlenecks_scheduledimpactanalysisdata_constructor_args():
    sig = inspect.signature(analysis_bottlenecks_ScheduledImpactAnalysisData.__init__)
    params = list(sig.parameters.keys())



def test_buffertodoublemap_is_not_abstract():
    assert not inspect.isabstract(BufferToDoubleMap)


def test_buffertodoublemap_constructor_exists():
    assert callable(BufferToDoubleMap.__init__)


def test_buffertodoublemap_constructor_args():
    sig = inspect.signature(BufferToDoubleMap.__init__)
    params = list(sig.parameters.keys())



def test_buffertointegermap_is_not_abstract():
    assert not inspect.isabstract(BufferToIntegerMap)


def test_buffertointegermap_constructor_exists():
    assert callable(BufferToIntegerMap.__init__)


def test_buffertointegermap_constructor_args():
    sig = inspect.signature(BufferToIntegerMap.__init__)
    params = list(sig.parameters.keys())



def test_analysis_bottlenecks_actionbottleneckswithschedulingdata_is_not_abstract():
    assert not inspect.isabstract(analysis_bottlenecks_ActionBottlenecksWithSchedulingData)


def test_analysis_bottlenecks_actionbottleneckswithschedulingdata_constructor_exists():
    assert callable(analysis_bottlenecks_ActionBottlenecksWithSchedulingData.__init__)


def test_analysis_bottlenecks_actionbottleneckswithschedulingdata_constructor_args():
    sig = inspect.signature(analysis_bottlenecks_ActionBottlenecksWithSchedulingData.__init__)
    params = list(sig.parameters.keys())
    assert "totalWeight" in params, "Missing parameter 'totalWeight'"
    assert "cpFirings" in params, "Missing parameter 'cpFirings'"
    assert "cpWeight" in params, "Missing parameter 'cpWeight'"
    assert "totalFirings" in params, "Missing parameter 'totalFirings'"

def test_analysis_bottlenecks_actionbottleneckswithschedulingdata_has_totalWeight():
    assert hasattr(analysis_bottlenecks_ActionBottlenecksWithSchedulingData, "totalWeight")
    descriptor = None
    for klass in analysis_bottlenecks_ActionBottlenecksWithSchedulingData.__mro__:
        if "totalWeight" in klass.__dict__:
            descriptor = klass.__dict__["totalWeight"]
            break
    assert isinstance(descriptor, property)

def test_analysis_bottlenecks_actionbottleneckswithschedulingdata_has_cpFirings():
    assert hasattr(analysis_bottlenecks_ActionBottlenecksWithSchedulingData, "cpFirings")
    descriptor = None
    for klass in analysis_bottlenecks_ActionBottlenecksWithSchedulingData.__mro__:
        if "cpFirings" in klass.__dict__:
            descriptor = klass.__dict__["cpFirings"]
            break
    assert isinstance(descriptor, property)

def test_analysis_bottlenecks_actionbottleneckswithschedulingdata_has_cpWeight():
    assert hasattr(analysis_bottlenecks_ActionBottlenecksWithSchedulingData, "cpWeight")
    descriptor = None
    for klass in analysis_bottlenecks_ActionBottlenecksWithSchedulingData.__mro__:
        if "cpWeight" in klass.__dict__:
            descriptor = klass.__dict__["cpWeight"]
            break
    assert isinstance(descriptor, property)

def test_analysis_bottlenecks_actionbottleneckswithschedulingdata_has_totalFirings():
    assert hasattr(analysis_bottlenecks_ActionBottlenecksWithSchedulingData, "totalFirings")
    descriptor = None
    for klass in analysis_bottlenecks_ActionBottlenecksWithSchedulingData.__mro__:
        if "totalFirings" in klass.__dict__:
            descriptor = klass.__dict__["totalFirings"]
            break
    assert isinstance(descriptor, property)



def test_stringtodoublemap_is_not_abstract():
    assert not inspect.isabstract(StringToDoubleMap)


def test_stringtodoublemap_constructor_exists():
    assert callable(StringToDoubleMap.__init__)


def test_stringtodoublemap_constructor_args():
    sig = inspect.signature(StringToDoubleMap.__init__)
    params = list(sig.parameters.keys())



def test_actionbottleneckswithschedulingdata_is_not_abstract():
    assert not inspect.isabstract(ActionBottlenecksWithSchedulingData)


def test_actionbottleneckswithschedulingdata_constructor_exists():
    assert callable(ActionBottlenecksWithSchedulingData.__init__)


def test_actionbottleneckswithschedulingdata_constructor_args():
    sig = inspect.signature(ActionBottlenecksWithSchedulingData.__init__)
    params = list(sig.parameters.keys())



def test_postprocessing_postprocessingdata_is_not_abstract():
    assert not inspect.isabstract(postprocessing_PostProcessingData)


def test_postprocessing_postprocessingdata_constructor_exists():
    assert callable(postprocessing_PostProcessingData.__init__)


def test_postprocessing_postprocessingdata_constructor_args():
    sig = inspect.signature(postprocessing_PostProcessingData.__init__)
    params = list(sig.parameters.keys())



def test_analysis_bottlenecks_doubletobottlenecksreportmap_is_not_abstract():
    assert not inspect.isabstract(analysis_bottlenecks_DoubleToBottlenecksReportMap)


def test_analysis_bottlenecks_doubletobottlenecksreportmap_constructor_exists():
    assert callable(analysis_bottlenecks_DoubleToBottlenecksReportMap.__init__)


def test_analysis_bottlenecks_doubletobottlenecksreportmap_constructor_args():
    sig = inspect.signature(analysis_bottlenecks_DoubleToBottlenecksReportMap.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_analysis_bottlenecks_doubletobottlenecksreportmap_has_key():
    assert hasattr(analysis_bottlenecks_DoubleToBottlenecksReportMap, "key")
    descriptor = None
    for klass in analysis_bottlenecks_DoubleToBottlenecksReportMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_doubletobottlenecksreportmap_is_not_abstract():
    assert not inspect.isabstract(DoubleToBottlenecksReportMap)


def test_doubletobottlenecksreportmap_constructor_exists():
    assert callable(DoubleToBottlenecksReportMap.__init__)


def test_doubletobottlenecksreportmap_constructor_args():
    sig = inspect.signature(DoubleToBottlenecksReportMap.__init__)
    params = list(sig.parameters.keys())



def test_doubletodoublemap_is_not_abstract():
    assert not inspect.isabstract(DoubleToDoubleMap)


def test_doubletodoublemap_constructor_exists():
    assert callable(DoubleToDoubleMap.__init__)


def test_doubletodoublemap_constructor_args():
    sig = inspect.signature(DoubleToDoubleMap.__init__)
    params = list(sig.parameters.keys())



def test_bottlenecks_analysis_actorclass_is_not_abstract():
    assert not inspect.isabstract(bottlenecks_analysis_ActorClass)


def test_bottlenecks_analysis_actorclass_constructor_exists():
    assert callable(bottlenecks_analysis_ActorClass.__init__)


def test_bottlenecks_analysis_actorclass_constructor_args():
    sig = inspect.signature(bottlenecks_analysis_ActorClass.__init__)
    params = list(sig.parameters.keys())



def test_analysis_bottlenecks_impactanalysisdata_is_not_abstract():
    assert not inspect.isabstract(analysis_bottlenecks_ImpactAnalysisData)


def test_analysis_bottlenecks_impactanalysisdata_constructor_exists():
    assert callable(analysis_bottlenecks_ImpactAnalysisData.__init__)


def test_analysis_bottlenecks_impactanalysisdata_constructor_args():
    sig = inspect.signature(analysis_bottlenecks_ImpactAnalysisData.__init__)
    params = list(sig.parameters.keys())



def test_bottlenecksreport_is_not_abstract():
    assert not inspect.isabstract(BottlenecksReport)


def test_bottlenecksreport_constructor_exists():
    assert callable(BottlenecksReport.__init__)


def test_bottlenecksreport_constructor_args():
    sig = inspect.signature(BottlenecksReport.__init__)
    params = list(sig.parameters.keys())



def test_impactanalysisdata_is_not_abstract():
    assert not inspect.isabstract(ImpactAnalysisData)


def test_impactanalysisdata_constructor_exists():
    assert callable(ImpactAnalysisData.__init__)


def test_impactanalysisdata_constructor_args():
    sig = inspect.signature(ImpactAnalysisData.__init__)
    params = list(sig.parameters.keys())



def test_analysis_bottlenecks_actionbottlenecksdata_is_not_abstract():
    assert not inspect.isabstract(analysis_bottlenecks_ActionBottlenecksData)


def test_analysis_bottlenecks_actionbottlenecksdata_constructor_exists():
    assert callable(analysis_bottlenecks_ActionBottlenecksData.__init__)


def test_analysis_bottlenecks_actionbottlenecksdata_constructor_args():
    sig = inspect.signature(analysis_bottlenecks_ActionBottlenecksData.__init__)
    params = list(sig.parameters.keys())
    assert "totalVariance" in params, "Missing parameter 'totalVariance'"
    assert "totalFirings" in params, "Missing parameter 'totalFirings'"
    assert "totalWeight" in params, "Missing parameter 'totalWeight'"
    assert "slackMin" in params, "Missing parameter 'slackMin'"
    assert "cpVariance" in params, "Missing parameter 'cpVariance'"
    assert "cpWeight" in params, "Missing parameter 'cpWeight'"
    assert "cpFirings" in params, "Missing parameter 'cpFirings'"
    assert "slackMax" in params, "Missing parameter 'slackMax'"

def test_analysis_bottlenecks_actionbottlenecksdata_has_totalVariance():
    assert hasattr(analysis_bottlenecks_ActionBottlenecksData, "totalVariance")
    descriptor = None
    for klass in analysis_bottlenecks_ActionBottlenecksData.__mro__:
        if "totalVariance" in klass.__dict__:
            descriptor = klass.__dict__["totalVariance"]
            break
    assert isinstance(descriptor, property)

def test_analysis_bottlenecks_actionbottlenecksdata_has_totalFirings():
    assert hasattr(analysis_bottlenecks_ActionBottlenecksData, "totalFirings")
    descriptor = None
    for klass in analysis_bottlenecks_ActionBottlenecksData.__mro__:
        if "totalFirings" in klass.__dict__:
            descriptor = klass.__dict__["totalFirings"]
            break
    assert isinstance(descriptor, property)

def test_analysis_bottlenecks_actionbottlenecksdata_has_totalWeight():
    assert hasattr(analysis_bottlenecks_ActionBottlenecksData, "totalWeight")
    descriptor = None
    for klass in analysis_bottlenecks_ActionBottlenecksData.__mro__:
        if "totalWeight" in klass.__dict__:
            descriptor = klass.__dict__["totalWeight"]
            break
    assert isinstance(descriptor, property)

def test_analysis_bottlenecks_actionbottlenecksdata_has_slackMin():
    assert hasattr(analysis_bottlenecks_ActionBottlenecksData, "slackMin")
    descriptor = None
    for klass in analysis_bottlenecks_ActionBottlenecksData.__mro__:
        if "slackMin" in klass.__dict__:
            descriptor = klass.__dict__["slackMin"]
            break
    assert isinstance(descriptor, property)

def test_analysis_bottlenecks_actionbottlenecksdata_has_cpVariance():
    assert hasattr(analysis_bottlenecks_ActionBottlenecksData, "cpVariance")
    descriptor = None
    for klass in analysis_bottlenecks_ActionBottlenecksData.__mro__:
        if "cpVariance" in klass.__dict__:
            descriptor = klass.__dict__["cpVariance"]
            break
    assert isinstance(descriptor, property)

def test_analysis_bottlenecks_actionbottlenecksdata_has_cpWeight():
    assert hasattr(analysis_bottlenecks_ActionBottlenecksData, "cpWeight")
    descriptor = None
    for klass in analysis_bottlenecks_ActionBottlenecksData.__mro__:
        if "cpWeight" in klass.__dict__:
            descriptor = klass.__dict__["cpWeight"]
            break
    assert isinstance(descriptor, property)

def test_analysis_bottlenecks_actionbottlenecksdata_has_cpFirings():
    assert hasattr(analysis_bottlenecks_ActionBottlenecksData, "cpFirings")
    descriptor = None
    for klass in analysis_bottlenecks_ActionBottlenecksData.__mro__:
        if "cpFirings" in klass.__dict__:
            descriptor = klass.__dict__["cpFirings"]
            break
    assert isinstance(descriptor, property)

def test_analysis_bottlenecks_actionbottlenecksdata_has_slackMax():
    assert hasattr(analysis_bottlenecks_ActionBottlenecksData, "slackMax")
    descriptor = None
    for klass in analysis_bottlenecks_ActionBottlenecksData.__mro__:
        if "slackMax" in klass.__dict__:
            descriptor = klass.__dict__["slackMax"]
            break
    assert isinstance(descriptor, property)



def test_actionbottlenecksdata_is_not_abstract():
    assert not inspect.isabstract(ActionBottlenecksData)


def test_actionbottlenecksdata_constructor_exists():
    assert callable(ActionBottlenecksData.__init__)


def test_actionbottlenecksdata_constructor_args():
    sig = inspect.signature(ActionBottlenecksData.__init__)
    params = list(sig.parameters.keys())



def test_bottlenecks_analysis_network_is_not_abstract():
    assert not inspect.isabstract(bottlenecks_analysis_Network)


def test_bottlenecks_analysis_network_constructor_exists():
    assert callable(bottlenecks_analysis_Network.__init__)


def test_bottlenecks_analysis_network_constructor_args():
    sig = inspect.signature(bottlenecks_analysis_Network.__init__)
    params = list(sig.parameters.keys())



def test_analysis_trace_markovmodelactiondata_is_not_abstract():
    assert not inspect.isabstract(analysis_trace_MarkovModelActionData)


def test_analysis_trace_markovmodelactiondata_constructor_exists():
    assert callable(analysis_trace_MarkovModelActionData.__init__)


def test_analysis_trace_markovmodelactiondata_constructor_args():
    sig = inspect.signature(analysis_trace_MarkovModelActionData.__init__)
    params = list(sig.parameters.keys())
    assert "successors" in params, "Missing parameter 'successors'"
    assert "first" in params, "Missing parameter 'first'"

def test_analysis_trace_markovmodelactiondata_has_successors():
    assert hasattr(analysis_trace_MarkovModelActionData, "successors")
    descriptor = None
    for klass in analysis_trace_MarkovModelActionData.__mro__:
        if "successors" in klass.__dict__:
            descriptor = klass.__dict__["successors"]
            break
    assert isinstance(descriptor, property)

def test_analysis_trace_markovmodelactiondata_has_first():
    assert hasattr(analysis_trace_MarkovModelActionData, "first")
    descriptor = None
    for klass in analysis_trace_MarkovModelActionData.__mro__:
        if "first" in klass.__dict__:
            descriptor = klass.__dict__["first"]
            break
    assert isinstance(descriptor, property)



def test_markovmodelactiondata_is_not_abstract():
    assert not inspect.isabstract(MarkovModelActionData)


def test_markovmodelactiondata_constructor_exists():
    assert callable(MarkovModelActionData.__init__)


def test_markovmodelactiondata_constructor_args():
    sig = inspect.signature(MarkovModelActionData.__init__)
    params = list(sig.parameters.keys())



def test_analysis_trace_comparedaction_is_not_abstract():
    assert not inspect.isabstract(analysis_trace_ComparedAction)


def test_analysis_trace_comparedaction_constructor_exists():
    assert callable(analysis_trace_ComparedAction.__init__)


def test_analysis_trace_comparedaction_constructor_args():
    sig = inspect.signature(analysis_trace_ComparedAction.__init__)
    params = list(sig.parameters.keys())
    assert "found" in params, "Missing parameter 'found'"
    assert "dIncomings" in params, "Missing parameter 'dIncomings'"
    assert "dOutgoings" in params, "Missing parameter 'dOutgoings'"
    assert "dSteps" in params, "Missing parameter 'dSteps'"

def test_analysis_trace_comparedaction_has_found():
    assert hasattr(analysis_trace_ComparedAction, "found")
    descriptor = None
    for klass in analysis_trace_ComparedAction.__mro__:
        if "found" in klass.__dict__:
            descriptor = klass.__dict__["found"]
            break
    assert isinstance(descriptor, property)

def test_analysis_trace_comparedaction_has_dIncomings():
    assert hasattr(analysis_trace_ComparedAction, "dIncomings")
    descriptor = None
    for klass in analysis_trace_ComparedAction.__mro__:
        if "dIncomings" in klass.__dict__:
            descriptor = klass.__dict__["dIncomings"]
            break
    assert isinstance(descriptor, property)

def test_analysis_trace_comparedaction_has_dOutgoings():
    assert hasattr(analysis_trace_ComparedAction, "dOutgoings")
    descriptor = None
    for klass in analysis_trace_ComparedAction.__mro__:
        if "dOutgoings" in klass.__dict__:
            descriptor = klass.__dict__["dOutgoings"]
            break
    assert isinstance(descriptor, property)

def test_analysis_trace_comparedaction_has_dSteps():
    assert hasattr(analysis_trace_ComparedAction, "dSteps")
    descriptor = None
    for klass in analysis_trace_ComparedAction.__mro__:
        if "dSteps" in klass.__dict__:
            descriptor = klass.__dict__["dSteps"]
            break
    assert isinstance(descriptor, property)



def test_comparedaction_is_not_abstract():
    assert not inspect.isabstract(ComparedAction)


def test_comparedaction_constructor_exists():
    assert callable(ComparedAction.__init__)


def test_comparedaction_constructor_args():
    sig = inspect.signature(ComparedAction.__init__)
    params = list(sig.parameters.keys())



def test_bottlenecks_analysis_action_is_not_abstract():
    assert not inspect.isabstract(bottlenecks_analysis_Action)


def test_bottlenecks_analysis_action_constructor_exists():
    assert callable(bottlenecks_analysis_Action.__init__)


def test_bottlenecks_analysis_action_constructor_args():
    sig = inspect.signature(bottlenecks_analysis_Action.__init__)
    params = list(sig.parameters.keys())



def test_analysis_trace_comparedtrace_is_not_abstract():
    assert not inspect.isabstract(analysis_trace_ComparedTrace)


def test_analysis_trace_comparedtrace_constructor_exists():
    assert callable(analysis_trace_ComparedTrace.__init__)


def test_analysis_trace_comparedtrace_constructor_args():
    sig = inspect.signature(analysis_trace_ComparedTrace.__init__)
    params = list(sig.parameters.keys())
    assert "dDependencies" in params, "Missing parameter 'dDependencies'"
    assert "dSteps" in params, "Missing parameter 'dSteps'"
    assert "equal" in params, "Missing parameter 'equal'"

def test_analysis_trace_comparedtrace_has_dDependencies():
    assert hasattr(analysis_trace_ComparedTrace, "dDependencies")
    descriptor = None
    for klass in analysis_trace_ComparedTrace.__mro__:
        if "dDependencies" in klass.__dict__:
            descriptor = klass.__dict__["dDependencies"]
            break
    assert isinstance(descriptor, property)

def test_analysis_trace_comparedtrace_has_dSteps():
    assert hasattr(analysis_trace_ComparedTrace, "dSteps")
    descriptor = None
    for klass in analysis_trace_ComparedTrace.__mro__:
        if "dSteps" in klass.__dict__:
            descriptor = klass.__dict__["dSteps"]
            break
    assert isinstance(descriptor, property)

def test_analysis_trace_comparedtrace_has_equal():
    assert hasattr(analysis_trace_ComparedTrace, "equal")
    descriptor = None
    for klass in analysis_trace_ComparedTrace.__mro__:
        if "equal" in klass.__dict__:
            descriptor = klass.__dict__["equal"]
            break
    assert isinstance(descriptor, property)



def test_comparedtrace_is_not_abstract():
    assert not inspect.isabstract(ComparedTrace)


def test_comparedtrace_constructor_exists():
    assert callable(ComparedTrace.__init__)


def test_comparedtrace_constructor_args():
    sig = inspect.signature(ComparedTrace.__init__)
    params = list(sig.parameters.keys())



def test_compressedtracereport_is_not_abstract():
    assert not inspect.isabstract(CompressedTraceReport)


def test_compressedtracereport_constructor_exists():
    assert callable(CompressedTraceReport.__init__)


def test_compressedtracereport_constructor_args():
    sig = inspect.signature(CompressedTraceReport.__init__)
    params = list(sig.parameters.keys())



def test_buffertolongmap_is_not_abstract():
    assert not inspect.isabstract(BufferToLongMap)


def test_buffertolongmap_constructor_exists():
    assert callable(BufferToLongMap.__init__)


def test_buffertolongmap_constructor_args():
    sig = inspect.signature(BufferToLongMap.__init__)
    params = list(sig.parameters.keys())



def test_porttolongmap_is_not_abstract():
    assert not inspect.isabstract(PortToLongMap)


def test_porttolongmap_constructor_exists():
    assert callable(PortToLongMap.__init__)


def test_porttolongmap_constructor_args():
    sig = inspect.signature(PortToLongMap.__init__)
    params = list(sig.parameters.keys())



def test_variabletolongmap_is_not_abstract():
    assert not inspect.isabstract(VariableToLongMap)


def test_variabletolongmap_constructor_exists():
    assert callable(VariableToLongMap.__init__)


def test_variabletolongmap_constructor_args():
    sig = inspect.signature(VariableToLongMap.__init__)
    params = list(sig.parameters.keys())



def test_guardtolongmap_is_not_abstract():
    assert not inspect.isabstract(GuardToLongMap)


def test_guardtolongmap_constructor_exists():
    assert callable(GuardToLongMap.__init__)


def test_guardtolongmap_constructor_args():
    sig = inspect.signature(GuardToLongMap.__init__)
    params = list(sig.parameters.keys())



def test_analysis_trace_compresseddependency_is_not_abstract():
    assert not inspect.isabstract(analysis_trace_CompressedDependency)


def test_analysis_trace_compresseddependency_constructor_exists():
    assert callable(analysis_trace_CompressedDependency.__init__)


def test_analysis_trace_compresseddependency_constructor_args():
    sig = inspect.signature(analysis_trace_CompressedDependency.__init__)
    params = list(sig.parameters.keys())
    assert "count" in params, "Missing parameter 'count'"

def test_analysis_trace_compresseddependency_has_count():
    assert hasattr(analysis_trace_CompressedDependency, "count")
    descriptor = None
    for klass in analysis_trace_CompressedDependency.__mro__:
        if "count" in klass.__dict__:
            descriptor = klass.__dict__["count"]
            break
    assert isinstance(descriptor, property)



def test_trace_analysis_action_is_not_abstract():
    assert not inspect.isabstract(trace_analysis_Action)


def test_trace_analysis_action_constructor_exists():
    assert callable(trace_analysis_Action.__init__)


def test_trace_analysis_action_constructor_args():
    sig = inspect.signature(trace_analysis_Action.__init__)
    params = list(sig.parameters.keys())



def test_analysis_trace_compressedstep_is_not_abstract():
    assert not inspect.isabstract(analysis_trace_CompressedStep)


def test_analysis_trace_compressedstep_constructor_exists():
    assert callable(analysis_trace_CompressedStep.__init__)


def test_analysis_trace_compressedstep_constructor_args():
    sig = inspect.signature(analysis_trace_CompressedStep.__init__)
    params = list(sig.parameters.keys())
    assert "count" in params, "Missing parameter 'count'"

def test_analysis_trace_compressedstep_has_count():
    assert hasattr(analysis_trace_CompressedStep, "count")
    descriptor = None
    for klass in analysis_trace_CompressedStep.__mro__:
        if "count" in klass.__dict__:
            descriptor = klass.__dict__["count"]
            break
    assert isinstance(descriptor, property)



def test_compresseddependency_is_not_abstract():
    assert not inspect.isabstract(CompressedDependency)


def test_compresseddependency_constructor_exists():
    assert callable(CompressedDependency.__init__)


def test_compresseddependency_constructor_args():
    sig = inspect.signature(CompressedDependency.__init__)
    params = list(sig.parameters.keys())



def test_analysis_trace_compressedvariabledependency_is_not_abstract():
    assert not inspect.isabstract(analysis_trace_CompressedVariableDependency)


def test_analysis_trace_compressedvariabledependency_constructor_exists():
    assert callable(analysis_trace_CompressedVariableDependency.__init__)


def test_analysis_trace_compressedvariabledependency_constructor_args():
    sig = inspect.signature(analysis_trace_CompressedVariableDependency.__init__)
    params = list(sig.parameters.keys())



def test_analysis_trace_compressedfsmdependency_is_not_abstract():
    assert not inspect.isabstract(analysis_trace_CompressedFsmDependency)


def test_analysis_trace_compressedfsmdependency_constructor_exists():
    assert callable(analysis_trace_CompressedFsmDependency.__init__)


def test_analysis_trace_compressedfsmdependency_constructor_args():
    sig = inspect.signature(analysis_trace_CompressedFsmDependency.__init__)
    params = list(sig.parameters.keys())



def test_analysis_trace_compressedtokensdependency_is_not_abstract():
    assert not inspect.isabstract(analysis_trace_CompressedTokensDependency)


def test_analysis_trace_compressedtokensdependency_constructor_exists():
    assert callable(analysis_trace_CompressedTokensDependency.__init__)


def test_analysis_trace_compressedtokensdependency_constructor_args():
    sig = inspect.signature(analysis_trace_CompressedTokensDependency.__init__)
    params = list(sig.parameters.keys())



def test_analysis_trace_compressedportdependency_is_not_abstract():
    assert not inspect.isabstract(analysis_trace_CompressedPortDependency)


def test_analysis_trace_compressedportdependency_constructor_exists():
    assert callable(analysis_trace_CompressedPortDependency.__init__)


def test_analysis_trace_compressedportdependency_constructor_args():
    sig = inspect.signature(analysis_trace_CompressedPortDependency.__init__)
    params = list(sig.parameters.keys())



def test_analysis_trace_compressedguarddependency_is_not_abstract():
    assert not inspect.isabstract(analysis_trace_CompressedGuardDependency)


def test_analysis_trace_compressedguarddependency_constructor_exists():
    assert callable(analysis_trace_CompressedGuardDependency.__init__)


def test_analysis_trace_compressedguarddependency_constructor_args():
    sig = inspect.signature(analysis_trace_CompressedGuardDependency.__init__)
    params = list(sig.parameters.keys())



def test_compressedstep_is_not_abstract():
    assert not inspect.isabstract(CompressedStep)


def test_compressedstep_constructor_exists():
    assert callable(CompressedStep.__init__)


def test_compressedstep_constructor_args():
    sig = inspect.signature(CompressedStep.__init__)
    params = list(sig.parameters.keys())



def test_trace_analysis_network_is_not_abstract():
    assert not inspect.isabstract(trace_analysis_Network)


def test_trace_analysis_network_constructor_exists():
    assert callable(trace_analysis_Network.__init__)


def test_trace_analysis_network_constructor_args():
    sig = inspect.signature(trace_analysis_Network.__init__)
    params = list(sig.parameters.keys())



def test_stringtolongmap_is_not_abstract():
    assert not inspect.isabstract(StringToLongMap)


def test_stringtolongmap_constructor_exists():
    assert callable(StringToLongMap.__init__)


def test_stringtolongmap_constructor_args():
    sig = inspect.signature(StringToLongMap.__init__)
    params = list(sig.parameters.keys())



def test_analysis_map_actiontodoublemap_is_not_abstract():
    assert not inspect.isabstract(analysis_map_ActionToDoubleMap)


def test_analysis_map_actiontodoublemap_constructor_exists():
    assert callable(analysis_map_ActionToDoubleMap.__init__)


def test_analysis_map_actiontodoublemap_constructor_args():
    sig = inspect.signature(analysis_map_ActionToDoubleMap.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_analysis_map_actiontodoublemap_has_value():
    assert hasattr(analysis_map_ActionToDoubleMap, "value")
    descriptor = None
    for klass in analysis_map_ActionToDoubleMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_actortolongmap_is_not_abstract():
    assert not inspect.isabstract(ActorToLongMap)


def test_actortolongmap_constructor_exists():
    assert callable(ActorToLongMap.__init__)


def test_actortolongmap_constructor_args():
    sig = inspect.signature(ActorToLongMap.__init__)
    params = list(sig.parameters.keys())



def test_analysis_map_stringtostringmap_is_not_abstract():
    assert not inspect.isabstract(analysis_map_StringToStringMap)


def test_analysis_map_stringtostringmap_constructor_exists():
    assert callable(analysis_map_StringToStringMap.__init__)


def test_analysis_map_stringtostringmap_constructor_args():
    sig = inspect.signature(analysis_map_StringToStringMap.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_analysis_map_stringtostringmap_has_key():
    assert hasattr(analysis_map_StringToStringMap, "key")
    descriptor = None
    for klass in analysis_map_StringToStringMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_analysis_map_stringtostringmap_has_value():
    assert hasattr(analysis_map_StringToStringMap, "value")
    descriptor = None
    for klass in analysis_map_StringToStringMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_actorselectionschedule_is_not_abstract():
    assert not inspect.isabstract(ActorSelectionSchedule)


def test_actorselectionschedule_constructor_exists():
    assert callable(ActorSelectionSchedule.__init__)


def test_actorselectionschedule_constructor_args():
    sig = inspect.signature(ActorSelectionSchedule.__init__)
    params = list(sig.parameters.keys())



def test_analysis_map_partitiontoactorselectionschedulemap_is_not_abstract():
    assert not inspect.isabstract(analysis_map_PartitionToActorSelectionScheduleMap)


def test_analysis_map_partitiontoactorselectionschedulemap_constructor_exists():
    assert callable(analysis_map_PartitionToActorSelectionScheduleMap.__init__)


def test_analysis_map_partitiontoactorselectionschedulemap_constructor_args():
    sig = inspect.signature(analysis_map_PartitionToActorSelectionScheduleMap.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_analysis_map_partitiontoactorselectionschedulemap_has_key():
    assert hasattr(analysis_map_PartitionToActorSelectionScheduleMap, "key")
    descriptor = None
    for klass in analysis_map_PartitionToActorSelectionScheduleMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_analysis_map_buffertodoublemap_is_not_abstract():
    assert not inspect.isabstract(analysis_map_BufferToDoubleMap)


def test_analysis_map_buffertodoublemap_constructor_exists():
    assert callable(analysis_map_BufferToDoubleMap.__init__)


def test_analysis_map_buffertodoublemap_constructor_args():
    sig = inspect.signature(analysis_map_BufferToDoubleMap.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_analysis_map_buffertodoublemap_has_value():
    assert hasattr(analysis_map_BufferToDoubleMap, "value")
    descriptor = None
    for klass in analysis_map_BufferToDoubleMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_analysis_map_buffertointegermap_is_not_abstract():
    assert not inspect.isabstract(analysis_map_BufferToIntegerMap)


def test_analysis_map_buffertointegermap_constructor_exists():
    assert callable(analysis_map_BufferToIntegerMap.__init__)


def test_analysis_map_buffertointegermap_constructor_args():
    sig = inspect.signature(analysis_map_BufferToIntegerMap.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_analysis_map_buffertointegermap_has_value():
    assert hasattr(analysis_map_BufferToIntegerMap, "value")
    descriptor = None
    for klass in analysis_map_BufferToIntegerMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_map_analysis_procedure_is_not_abstract():
    assert not inspect.isabstract(map_analysis_Procedure)


def test_map_analysis_procedure_constructor_exists():
    assert callable(map_analysis_Procedure.__init__)


def test_map_analysis_procedure_constructor_args():
    sig = inspect.signature(map_analysis_Procedure.__init__)
    params = list(sig.parameters.keys())



def test_analysis_map_stringtodoublemap_is_not_abstract():
    assert not inspect.isabstract(analysis_map_StringToDoubleMap)


def test_analysis_map_stringtodoublemap_constructor_exists():
    assert callable(analysis_map_StringToDoubleMap.__init__)


def test_analysis_map_stringtodoublemap_constructor_args():
    sig = inspect.signature(analysis_map_StringToDoubleMap.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_analysis_map_stringtodoublemap_has_key():
    assert hasattr(analysis_map_StringToDoubleMap, "key")
    descriptor = None
    for klass in analysis_map_StringToDoubleMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_analysis_map_stringtodoublemap_has_value():
    assert hasattr(analysis_map_StringToDoubleMap, "value")
    descriptor = None
    for klass in analysis_map_StringToDoubleMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_map_analysis_port_is_not_abstract():
    assert not inspect.isabstract(map_analysis_Port)


def test_map_analysis_port_constructor_exists():
    assert callable(map_analysis_Port.__init__)


def test_map_analysis_port_constructor_args():
    sig = inspect.signature(map_analysis_Port.__init__)
    params = list(sig.parameters.keys())



def test_analysis_map_porttolongmap_is_not_abstract():
    assert not inspect.isabstract(analysis_map_PortToLongMap)


def test_analysis_map_porttolongmap_constructor_exists():
    assert callable(analysis_map_PortToLongMap.__init__)


def test_analysis_map_porttolongmap_constructor_args():
    sig = inspect.signature(analysis_map_PortToLongMap.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_analysis_map_porttolongmap_has_value():
    assert hasattr(analysis_map_PortToLongMap, "value")
    descriptor = None
    for klass in analysis_map_PortToLongMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_map_analysis_guard_is_not_abstract():
    assert not inspect.isabstract(map_analysis_Guard)


def test_map_analysis_guard_constructor_exists():
    assert callable(map_analysis_Guard.__init__)


def test_map_analysis_guard_constructor_args():
    sig = inspect.signature(map_analysis_Guard.__init__)
    params = list(sig.parameters.keys())



def test_analysis_map_guardtolongmap_is_not_abstract():
    assert not inspect.isabstract(analysis_map_GuardToLongMap)


def test_analysis_map_guardtolongmap_constructor_exists():
    assert callable(analysis_map_GuardToLongMap.__init__)


def test_analysis_map_guardtolongmap_constructor_args():
    sig = inspect.signature(analysis_map_GuardToLongMap.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_analysis_map_guardtolongmap_has_value():
    assert hasattr(analysis_map_GuardToLongMap, "value")
    descriptor = None
    for klass in analysis_map_GuardToLongMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_analysis_map_variabletolongmap_is_not_abstract():
    assert not inspect.isabstract(analysis_map_VariableToLongMap)


def test_analysis_map_variabletolongmap_constructor_exists():
    assert callable(analysis_map_VariableToLongMap.__init__)


def test_analysis_map_variabletolongmap_constructor_args():
    sig = inspect.signature(analysis_map_VariableToLongMap.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_analysis_map_variabletolongmap_has_value():
    assert hasattr(analysis_map_VariableToLongMap, "value")
    descriptor = None
    for klass in analysis_map_VariableToLongMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_analysis_map_doubletodoublemap_is_not_abstract():
    assert not inspect.isabstract(analysis_map_DoubleToDoubleMap)


def test_analysis_map_doubletodoublemap_constructor_exists():
    assert callable(analysis_map_DoubleToDoubleMap.__init__)


def test_analysis_map_doubletodoublemap_constructor_args():
    sig = inspect.signature(analysis_map_DoubleToDoubleMap.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_analysis_map_doubletodoublemap_has_key():
    assert hasattr(analysis_map_DoubleToDoubleMap, "key")
    descriptor = None
    for klass in analysis_map_DoubleToDoubleMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_analysis_map_doubletodoublemap_has_value():
    assert hasattr(analysis_map_DoubleToDoubleMap, "value")
    descriptor = None
    for klass in analysis_map_DoubleToDoubleMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_analysis_map_stringtolongmap_is_not_abstract():
    assert not inspect.isabstract(analysis_map_StringToLongMap)


def test_analysis_map_stringtolongmap_constructor_exists():
    assert callable(analysis_map_StringToLongMap.__init__)


def test_analysis_map_stringtolongmap_constructor_args():
    sig = inspect.signature(analysis_map_StringToLongMap.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_analysis_map_stringtolongmap_has_key():
    assert hasattr(analysis_map_StringToLongMap, "key")
    descriptor = None
    for klass in analysis_map_StringToLongMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_analysis_map_stringtolongmap_has_value():
    assert hasattr(analysis_map_StringToLongMap, "value")
    descriptor = None
    for klass in analysis_map_StringToLongMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_analysis_map_buffertolongmap_is_not_abstract():
    assert not inspect.isabstract(analysis_map_BufferToLongMap)


def test_analysis_map_buffertolongmap_constructor_exists():
    assert callable(analysis_map_BufferToLongMap.__init__)


def test_analysis_map_buffertolongmap_constructor_args():
    sig = inspect.signature(analysis_map_BufferToLongMap.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_analysis_map_buffertolongmap_has_value():
    assert hasattr(analysis_map_BufferToLongMap, "value")
    descriptor = None
    for klass in analysis_map_BufferToLongMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_analysis_map_actortolongmap_is_not_abstract():
    assert not inspect.isabstract(analysis_map_ActorToLongMap)


def test_analysis_map_actortolongmap_constructor_exists():
    assert callable(analysis_map_ActorToLongMap.__init__)


def test_analysis_map_actortolongmap_constructor_args():
    sig = inspect.signature(analysis_map_ActorToLongMap.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_analysis_map_actortolongmap_has_value():
    assert hasattr(analysis_map_ActorToLongMap, "value")
    descriptor = None
    for klass in analysis_map_ActorToLongMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_analysis_map_actiontolongmap_is_not_abstract():
    assert not inspect.isabstract(analysis_map_ActionToLongMap)


def test_analysis_map_actiontolongmap_constructor_exists():
    assert callable(analysis_map_ActionToLongMap.__init__)


def test_analysis_map_actiontolongmap_constructor_args():
    sig = inspect.signature(analysis_map_ActionToLongMap.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_analysis_map_actiontolongmap_has_value():
    assert hasattr(analysis_map_ActionToLongMap, "value")
    descriptor = None
    for klass in analysis_map_ActionToLongMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_analysis_map_eoperatortostatisticaldatamap_is_not_abstract():
    assert not inspect.isabstract(analysis_map_EOperatorToStatisticalDataMap)


def test_analysis_map_eoperatortostatisticaldatamap_constructor_exists():
    assert callable(analysis_map_EOperatorToStatisticalDataMap.__init__)


def test_analysis_map_eoperatortostatisticaldatamap_constructor_args():
    sig = inspect.signature(analysis_map_EOperatorToStatisticalDataMap.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_analysis_map_eoperatortostatisticaldatamap_has_key():
    assert hasattr(analysis_map_EOperatorToStatisticalDataMap, "key")
    descriptor = None
    for klass in analysis_map_EOperatorToStatisticalDataMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_map_analysis_actorclass_is_not_abstract():
    assert not inspect.isabstract(map_analysis_ActorClass)


def test_map_analysis_actorclass_constructor_exists():
    assert callable(map_analysis_ActorClass.__init__)


def test_map_analysis_actorclass_constructor_args():
    sig = inspect.signature(map_analysis_ActorClass.__init__)
    params = list(sig.parameters.keys())



def test_analysis_map_actorclasstostatisticaldatamap_is_not_abstract():
    assert not inspect.isabstract(analysis_map_ActorClassToStatisticalDataMap)


def test_analysis_map_actorclasstostatisticaldatamap_constructor_exists():
    assert callable(analysis_map_ActorClassToStatisticalDataMap.__init__)


def test_analysis_map_actorclasstostatisticaldatamap_constructor_args():
    sig = inspect.signature(analysis_map_ActorClassToStatisticalDataMap.__init__)
    params = list(sig.parameters.keys())



def test_map_analysis_variable_is_not_abstract():
    assert not inspect.isabstract(map_analysis_Variable)


def test_map_analysis_variable_constructor_exists():
    assert callable(map_analysis_Variable.__init__)


def test_map_analysis_variable_constructor_args():
    sig = inspect.signature(map_analysis_Variable.__init__)
    params = list(sig.parameters.keys())



def test_analysis_map_variabletostatisticaldatamap_is_not_abstract():
    assert not inspect.isabstract(analysis_map_VariableToStatisticalDataMap)


def test_analysis_map_variabletostatisticaldatamap_constructor_exists():
    assert callable(analysis_map_VariableToStatisticalDataMap.__init__)


def test_analysis_map_variabletostatisticaldatamap_constructor_args():
    sig = inspect.signature(analysis_map_VariableToStatisticalDataMap.__init__)
    params = list(sig.parameters.keys())



def test_analysis_map_proceduretostatisticaldatamap_is_not_abstract():
    assert not inspect.isabstract(analysis_map_ProcedureToStatisticalDataMap)


def test_analysis_map_proceduretostatisticaldatamap_constructor_exists():
    assert callable(analysis_map_ProcedureToStatisticalDataMap.__init__)


def test_analysis_map_proceduretostatisticaldatamap_constructor_args():
    sig = inspect.signature(analysis_map_ProcedureToStatisticalDataMap.__init__)
    params = list(sig.parameters.keys())



def test_map_analysis_buffer_is_not_abstract():
    assert not inspect.isabstract(map_analysis_Buffer)


def test_map_analysis_buffer_constructor_exists():
    assert callable(map_analysis_Buffer.__init__)


def test_map_analysis_buffer_constructor_args():
    sig = inspect.signature(map_analysis_Buffer.__init__)
    params = list(sig.parameters.keys())



def test_analysis_map_buffertostatisticaldatamap_is_not_abstract():
    assert not inspect.isabstract(analysis_map_BufferToStatisticalDataMap)


def test_analysis_map_buffertostatisticaldatamap_constructor_exists():
    assert callable(analysis_map_BufferToStatisticalDataMap.__init__)


def test_analysis_map_buffertostatisticaldatamap_constructor_args():
    sig = inspect.signature(analysis_map_BufferToStatisticalDataMap.__init__)
    params = list(sig.parameters.keys())



def test_map_analysis_action_is_not_abstract():
    assert not inspect.isabstract(map_analysis_Action)


def test_map_analysis_action_constructor_exists():
    assert callable(map_analysis_Action.__init__)


def test_map_analysis_action_constructor_args():
    sig = inspect.signature(map_analysis_Action.__init__)
    params = list(sig.parameters.keys())



def test_analysis_map_actiontostatisticaldatamap_is_not_abstract():
    assert not inspect.isabstract(analysis_map_ActionToStatisticalDataMap)


def test_analysis_map_actiontostatisticaldatamap_constructor_exists():
    assert callable(analysis_map_ActionToStatisticalDataMap.__init__)


def test_analysis_map_actiontostatisticaldatamap_constructor_args():
    sig = inspect.signature(analysis_map_ActionToStatisticalDataMap.__init__)
    params = list(sig.parameters.keys())



def test_map_analysis_statisticaldata_is_not_abstract():
    assert not inspect.isabstract(map_analysis_StatisticalData)


def test_map_analysis_statisticaldata_constructor_exists():
    assert callable(map_analysis_StatisticalData.__init__)


def test_map_analysis_statisticaldata_constructor_args():
    sig = inspect.signature(map_analysis_StatisticalData.__init__)
    params = list(sig.parameters.keys())



def test_map_analysis_actor_is_not_abstract():
    assert not inspect.isabstract(map_analysis_Actor)


def test_map_analysis_actor_constructor_exists():
    assert callable(map_analysis_Actor.__init__)


def test_map_analysis_actor_constructor_args():
    sig = inspect.signature(map_analysis_Actor.__init__)
    params = list(sig.parameters.keys())



def test_analysis_map_actortostatisticaldatamap_is_not_abstract():
    assert not inspect.isabstract(analysis_map_ActorToStatisticalDataMap)


def test_analysis_map_actortostatisticaldatamap_constructor_exists():
    assert callable(analysis_map_ActorToStatisticalDataMap.__init__)


def test_analysis_map_actortostatisticaldatamap_constructor_args():
    sig = inspect.signature(analysis_map_ActorToStatisticalDataMap.__init__)
    params = list(sig.parameters.keys())



def test_analysis_map_stringtointegermap_is_not_abstract():
    assert not inspect.isabstract(analysis_map_StringToIntegerMap)


def test_analysis_map_stringtointegermap_constructor_exists():
    assert callable(analysis_map_StringToIntegerMap.__init__)


def test_analysis_map_stringtointegermap_constructor_args():
    sig = inspect.signature(analysis_map_StringToIntegerMap.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_analysis_map_stringtointegermap_has_key():
    assert hasattr(analysis_map_StringToIntegerMap, "key")
    descriptor = None
    for klass in analysis_map_StringToIntegerMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_analysis_map_stringtointegermap_has_value():
    assert hasattr(analysis_map_StringToIntegerMap, "value")
    descriptor = None
    for klass in analysis_map_StringToIntegerMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_stringtostringmap_is_not_abstract():
    assert not inspect.isabstract(StringToStringMap)


def test_stringtostringmap_constructor_exists():
    assert callable(StringToStringMap.__init__)


def test_stringtostringmap_constructor_args():
    sig = inspect.signature(StringToStringMap.__init__)
    params = list(sig.parameters.keys())



def test_analysis_profiler_tablerow_is_not_abstract():
    assert not inspect.isabstract(analysis_profiler_TableRow)


def test_analysis_profiler_tablerow_constructor_exists():
    assert callable(analysis_profiler_TableRow.__init__)


def test_analysis_profiler_tablerow_constructor_args():
    sig = inspect.signature(analysis_profiler_TableRow.__init__)
    params = list(sig.parameters.keys())



def test_tablerow_is_not_abstract():
    assert not inspect.isabstract(TableRow)


def test_tablerow_constructor_exists():
    assert callable(TableRow.__init__)


def test_tablerow_constructor_args():
    sig = inspect.signature(TableRow.__init__)
    params = list(sig.parameters.keys())



def test_accessdata_is_not_abstract():
    assert not inspect.isabstract(AccessData)


def test_accessdata_constructor_exists():
    assert callable(AccessData.__init__)


def test_accessdata_constructor_args():
    sig = inspect.signature(AccessData.__init__)
    params = list(sig.parameters.keys())



def test_analysis_profiler_stringtoaccessdatamap_is_not_abstract():
    assert not inspect.isabstract(analysis_profiler_StringToAccessDataMap)


def test_analysis_profiler_stringtoaccessdatamap_constructor_exists():
    assert callable(analysis_profiler_StringToAccessDataMap.__init__)


def test_analysis_profiler_stringtoaccessdatamap_constructor_args():
    sig = inspect.signature(analysis_profiler_StringToAccessDataMap.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_analysis_profiler_stringtoaccessdatamap_has_key():
    assert hasattr(analysis_profiler_StringToAccessDataMap, "key")
    descriptor = None
    for klass in analysis_profiler_StringToAccessDataMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_analysis_profiler_accessdata_is_not_abstract():
    assert not inspect.isabstract(analysis_profiler_AccessData)


def test_analysis_profiler_accessdata_constructor_exists():
    assert callable(analysis_profiler_AccessData.__init__)


def test_analysis_profiler_accessdata_constructor_args():
    sig = inspect.signature(analysis_profiler_AccessData.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "average" in params, "Missing parameter 'average'"
    assert "total" in params, "Missing parameter 'total'"
    assert "min" in params, "Missing parameter 'min'"
    assert "accesses" in params, "Missing parameter 'accesses'"

def test_analysis_profiler_accessdata_has_max():
    assert hasattr(analysis_profiler_AccessData, "max")
    descriptor = None
    for klass in analysis_profiler_AccessData.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_analysis_profiler_accessdata_has_average():
    assert hasattr(analysis_profiler_AccessData, "average")
    descriptor = None
    for klass in analysis_profiler_AccessData.__mro__:
        if "average" in klass.__dict__:
            descriptor = klass.__dict__["average"]
            break
    assert isinstance(descriptor, property)

def test_analysis_profiler_accessdata_has_total():
    assert hasattr(analysis_profiler_AccessData, "total")
    descriptor = None
    for klass in analysis_profiler_AccessData.__mro__:
        if "total" in klass.__dict__:
            descriptor = klass.__dict__["total"]
            break
    assert isinstance(descriptor, property)

def test_analysis_profiler_accessdata_has_min():
    assert hasattr(analysis_profiler_AccessData, "min")
    descriptor = None
    for klass in analysis_profiler_AccessData.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_analysis_profiler_accessdata_has_accesses():
    assert hasattr(analysis_profiler_AccessData, "accesses")
    descriptor = None
    for klass in analysis_profiler_AccessData.__mro__:
        if "accesses" in klass.__dict__:
            descriptor = klass.__dict__["accesses"]
            break
    assert isinstance(descriptor, property)



def test_profiler_analysis_procedure_is_not_abstract():
    assert not inspect.isabstract(profiler_analysis_Procedure)


def test_profiler_analysis_procedure_constructor_exists():
    assert callable(profiler_analysis_Procedure.__init__)


def test_profiler_analysis_procedure_constructor_args():
    sig = inspect.signature(profiler_analysis_Procedure.__init__)
    params = list(sig.parameters.keys())



def test_stringtoaccessdatamap_is_not_abstract():
    assert not inspect.isabstract(StringToAccessDataMap)


def test_stringtoaccessdatamap_constructor_exists():
    assert callable(StringToAccessDataMap.__init__)


def test_stringtoaccessdatamap_constructor_args():
    sig = inspect.signature(StringToAccessDataMap.__init__)
    params = list(sig.parameters.keys())



def test_analysis_profiler_memoryaccessdata_is_not_abstract():
    assert not inspect.isabstract(analysis_profiler_MemoryAccessData)


def test_analysis_profiler_memoryaccessdata_constructor_exists():
    assert callable(analysis_profiler_MemoryAccessData.__init__)


def test_analysis_profiler_memoryaccessdata_constructor_args():
    sig = inspect.signature(analysis_profiler_MemoryAccessData.__init__)
    params = list(sig.parameters.keys())



def test_memoryaccessdata_is_not_abstract():
    assert not inspect.isabstract(MemoryAccessData)


def test_memoryaccessdata_constructor_exists():
    assert callable(MemoryAccessData.__init__)


def test_memoryaccessdata_constructor_args():
    sig = inspect.signature(MemoryAccessData.__init__)
    params = list(sig.parameters.keys())



def test_analysis_profiler_statevariableaccessdata_is_not_abstract():
    assert not inspect.isabstract(analysis_profiler_StateVariableAccessData)


def test_analysis_profiler_statevariableaccessdata_constructor_exists():
    assert callable(analysis_profiler_StateVariableAccessData.__init__)


def test_analysis_profiler_statevariableaccessdata_constructor_args():
    sig = inspect.signature(analysis_profiler_StateVariableAccessData.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_analysis_profiler_statevariableaccessdata_has_name():
    assert hasattr(analysis_profiler_StateVariableAccessData, "name")
    descriptor = None
    for klass in analysis_profiler_StateVariableAccessData.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_analysis_profiler_localvariableaccessdata_is_not_abstract():
    assert not inspect.isabstract(analysis_profiler_LocalVariableAccessData)


def test_analysis_profiler_localvariableaccessdata_constructor_exists():
    assert callable(analysis_profiler_LocalVariableAccessData.__init__)


def test_analysis_profiler_localvariableaccessdata_constructor_args():
    sig = inspect.signature(analysis_profiler_LocalVariableAccessData.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_analysis_profiler_localvariableaccessdata_has_name():
    assert hasattr(analysis_profiler_LocalVariableAccessData, "name")
    descriptor = None
    for klass in analysis_profiler_LocalVariableAccessData.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_analysis_profiler_sharedvariableaccessdata_is_not_abstract():
    assert not inspect.isabstract(analysis_profiler_SharedVariableAccessData)


def test_analysis_profiler_sharedvariableaccessdata_constructor_exists():
    assert callable(analysis_profiler_SharedVariableAccessData.__init__)


def test_analysis_profiler_sharedvariableaccessdata_constructor_args():
    sig = inspect.signature(analysis_profiler_SharedVariableAccessData.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_analysis_profiler_sharedvariableaccessdata_has_name():
    assert hasattr(analysis_profiler_SharedVariableAccessData, "name")
    descriptor = None
    for klass in analysis_profiler_SharedVariableAccessData.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_analysis_profiler_bufferaccessdata_is_not_abstract():
    assert not inspect.isabstract(analysis_profiler_BufferAccessData)


def test_analysis_profiler_bufferaccessdata_constructor_exists():
    assert callable(analysis_profiler_BufferAccessData.__init__)


def test_analysis_profiler_bufferaccessdata_constructor_args():
    sig = inspect.signature(analysis_profiler_BufferAccessData.__init__)
    params = list(sig.parameters.keys())
    assert "targetActor" in params, "Missing parameter 'targetActor'"
    assert "targetPort" in params, "Missing parameter 'targetPort'"
    assert "sourceActor" in params, "Missing parameter 'sourceActor'"
    assert "sourcePort" in params, "Missing parameter 'sourcePort'"

def test_analysis_profiler_bufferaccessdata_has_targetActor():
    assert hasattr(analysis_profiler_BufferAccessData, "targetActor")
    descriptor = None
    for klass in analysis_profiler_BufferAccessData.__mro__:
        if "targetActor" in klass.__dict__:
            descriptor = klass.__dict__["targetActor"]
            break
    assert isinstance(descriptor, property)

def test_analysis_profiler_bufferaccessdata_has_targetPort():
    assert hasattr(analysis_profiler_BufferAccessData, "targetPort")
    descriptor = None
    for klass in analysis_profiler_BufferAccessData.__mro__:
        if "targetPort" in klass.__dict__:
            descriptor = klass.__dict__["targetPort"]
            break
    assert isinstance(descriptor, property)

def test_analysis_profiler_bufferaccessdata_has_sourceActor():
    assert hasattr(analysis_profiler_BufferAccessData, "sourceActor")
    descriptor = None
    for klass in analysis_profiler_BufferAccessData.__mro__:
        if "sourceActor" in klass.__dict__:
            descriptor = klass.__dict__["sourceActor"]
            break
    assert isinstance(descriptor, property)

def test_analysis_profiler_bufferaccessdata_has_sourcePort():
    assert hasattr(analysis_profiler_BufferAccessData, "sourcePort")
    descriptor = None
    for klass in analysis_profiler_BufferAccessData.__mro__:
        if "sourcePort" in klass.__dict__:
            descriptor = klass.__dict__["sourcePort"]
            break
    assert isinstance(descriptor, property)



def test_analysis_profiler_actionmemoryprofilingdata_is_not_abstract():
    assert not inspect.isabstract(analysis_profiler_ActionMemoryProfilingData)


def test_analysis_profiler_actionmemoryprofilingdata_constructor_exists():
    assert callable(analysis_profiler_ActionMemoryProfilingData.__init__)


def test_analysis_profiler_actionmemoryprofilingdata_constructor_args():
    sig = inspect.signature(analysis_profiler_ActionMemoryProfilingData.__init__)
    params = list(sig.parameters.keys())
    assert "actor" in params, "Missing parameter 'actor'"
    assert "action" in params, "Missing parameter 'action'"

def test_analysis_profiler_actionmemoryprofilingdata_has_actor():
    assert hasattr(analysis_profiler_ActionMemoryProfilingData, "actor")
    descriptor = None
    for klass in analysis_profiler_ActionMemoryProfilingData.__mro__:
        if "actor" in klass.__dict__:
            descriptor = klass.__dict__["actor"]
            break
    assert isinstance(descriptor, property)

def test_analysis_profiler_actionmemoryprofilingdata_has_action():
    assert hasattr(analysis_profiler_ActionMemoryProfilingData, "action")
    descriptor = None
    for klass in analysis_profiler_ActionMemoryProfilingData.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)



def test_actionmemoryprofilingdata_is_not_abstract():
    assert not inspect.isabstract(ActionMemoryProfilingData)


def test_actionmemoryprofilingdata_constructor_exists():
    assert callable(ActionMemoryProfilingData.__init__)


def test_actionmemoryprofilingdata_constructor_args():
    sig = inspect.signature(ActionMemoryProfilingData.__init__)
    params = list(sig.parameters.keys())



def test_actiondynamicdata_is_not_abstract():
    assert not inspect.isabstract(ActionDynamicData)


def test_actiondynamicdata_constructor_exists():
    assert callable(ActionDynamicData.__init__)


def test_actiondynamicdata_constructor_args():
    sig = inspect.signature(ActionDynamicData.__init__)
    params = list(sig.parameters.keys())



def test_analysis_profiler_proceduretocomplexdynamicdatamap_is_not_abstract():
    assert not inspect.isabstract(analysis_profiler_ProcedureToComplexDynamicDataMap)


def test_analysis_profiler_proceduretocomplexdynamicdatamap_constructor_exists():
    assert callable(analysis_profiler_ProcedureToComplexDynamicDataMap.__init__)


def test_analysis_profiler_proceduretocomplexdynamicdatamap_constructor_args():
    sig = inspect.signature(analysis_profiler_ProcedureToComplexDynamicDataMap.__init__)
    params = list(sig.parameters.keys())



def test_buffertostatisticaldatamap_is_not_abstract():
    assert not inspect.isabstract(BufferToStatisticalDataMap)


def test_buffertostatisticaldatamap_constructor_exists():
    assert callable(BufferToStatisticalDataMap.__init__)


def test_buffertostatisticaldatamap_constructor_args():
    sig = inspect.signature(BufferToStatisticalDataMap.__init__)
    params = list(sig.parameters.keys())



def test_proceduretocomplexdynamicdatamap_is_not_abstract():
    assert not inspect.isabstract(ProcedureToComplexDynamicDataMap)


def test_proceduretocomplexdynamicdatamap_constructor_exists():
    assert callable(ProcedureToComplexDynamicDataMap.__init__)


def test_proceduretocomplexdynamicdatamap_constructor_args():
    sig = inspect.signature(ProcedureToComplexDynamicDataMap.__init__)
    params = list(sig.parameters.keys())



def test_variabletostatisticaldatamap_is_not_abstract():
    assert not inspect.isabstract(VariableToStatisticalDataMap)


def test_variabletostatisticaldatamap_constructor_exists():
    assert callable(VariableToStatisticalDataMap.__init__)


def test_variabletostatisticaldatamap_constructor_args():
    sig = inspect.signature(VariableToStatisticalDataMap.__init__)
    params = list(sig.parameters.keys())



def test_proceduretostatisticaldatamap_is_not_abstract():
    assert not inspect.isabstract(ProcedureToStatisticalDataMap)


def test_proceduretostatisticaldatamap_constructor_exists():
    assert callable(ProcedureToStatisticalDataMap.__init__)


def test_proceduretostatisticaldatamap_constructor_args():
    sig = inspect.signature(ProcedureToStatisticalDataMap.__init__)
    params = list(sig.parameters.keys())



def test_eoperatortostatisticaldatamap_is_not_abstract():
    assert not inspect.isabstract(EOperatorToStatisticalDataMap)


def test_eoperatortostatisticaldatamap_constructor_exists():
    assert callable(EOperatorToStatisticalDataMap.__init__)


def test_eoperatortostatisticaldatamap_constructor_args():
    sig = inspect.signature(EOperatorToStatisticalDataMap.__init__)
    params = list(sig.parameters.keys())



def test_analysis_profiler_complexdynamicdata_is_not_abstract():
    assert not inspect.isabstract(analysis_profiler_ComplexDynamicData)


def test_analysis_profiler_complexdynamicdata_constructor_exists():
    assert callable(analysis_profiler_ComplexDynamicData.__init__)


def test_analysis_profiler_complexdynamicdata_constructor_args():
    sig = inspect.signature(analysis_profiler_ComplexDynamicData.__init__)
    params = list(sig.parameters.keys())



def test_actiontolongmap_is_not_abstract():
    assert not inspect.isabstract(ActionToLongMap)


def test_actiontolongmap_constructor_exists():
    assert callable(ActionToLongMap.__init__)


def test_actiontolongmap_constructor_args():
    sig = inspect.signature(ActionToLongMap.__init__)
    params = list(sig.parameters.keys())



def test_actiontostatisticaldatamap_is_not_abstract():
    assert not inspect.isabstract(ActionToStatisticalDataMap)


def test_actiontostatisticaldatamap_constructor_exists():
    assert callable(ActionToStatisticalDataMap.__init__)


def test_actiontostatisticaldatamap_constructor_args():
    sig = inspect.signature(ActionToStatisticalDataMap.__init__)
    params = list(sig.parameters.keys())



def test_profiler_analysis_statisticaldata_is_not_abstract():
    assert not inspect.isabstract(profiler_analysis_StatisticalData)


def test_profiler_analysis_statisticaldata_constructor_exists():
    assert callable(profiler_analysis_StatisticalData.__init__)


def test_profiler_analysis_statisticaldata_constructor_args():
    sig = inspect.signature(profiler_analysis_StatisticalData.__init__)
    params = list(sig.parameters.keys())



def test_profiler_analysis_buffer_is_not_abstract():
    assert not inspect.isabstract(profiler_analysis_Buffer)


def test_profiler_analysis_buffer_constructor_exists():
    assert callable(profiler_analysis_Buffer.__init__)


def test_profiler_analysis_buffer_constructor_args():
    sig = inspect.signature(profiler_analysis_Buffer.__init__)
    params = list(sig.parameters.keys())



def test_analysis_profiler_bufferdynamicdata_is_not_abstract():
    assert not inspect.isabstract(analysis_profiler_BufferDynamicData)


def test_analysis_profiler_bufferdynamicdata_constructor_exists():
    assert callable(analysis_profiler_BufferDynamicData.__init__)


def test_analysis_profiler_bufferdynamicdata_constructor_args():
    sig = inspect.signature(analysis_profiler_BufferDynamicData.__init__)
    params = list(sig.parameters.keys())
    assert "unconsumedTokens" in params, "Missing parameter 'unconsumedTokens'"

def test_analysis_profiler_bufferdynamicdata_has_unconsumedTokens():
    assert hasattr(analysis_profiler_BufferDynamicData, "unconsumedTokens")
    descriptor = None
    for klass in analysis_profiler_BufferDynamicData.__mro__:
        if "unconsumedTokens" in klass.__dict__:
            descriptor = klass.__dict__["unconsumedTokens"]
            break
    assert isinstance(descriptor, property)



def test_profiler_analysis_action_is_not_abstract():
    assert not inspect.isabstract(profiler_analysis_Action)


def test_profiler_analysis_action_constructor_exists():
    assert callable(profiler_analysis_Action.__init__)


def test_profiler_analysis_action_constructor_args():
    sig = inspect.signature(profiler_analysis_Action.__init__)
    params = list(sig.parameters.keys())



def test_profiler_analysis_actor_is_not_abstract():
    assert not inspect.isabstract(profiler_analysis_Actor)


def test_profiler_analysis_actor_constructor_exists():
    assert callable(profiler_analysis_Actor.__init__)


def test_profiler_analysis_actor_constructor_args():
    sig = inspect.signature(profiler_analysis_Actor.__init__)
    params = list(sig.parameters.keys())



def test_complexdynamicdata_is_not_abstract():
    assert not inspect.isabstract(ComplexDynamicData)


def test_complexdynamicdata_constructor_exists():
    assert callable(ComplexDynamicData.__init__)


def test_complexdynamicdata_constructor_args():
    sig = inspect.signature(ComplexDynamicData.__init__)
    params = list(sig.parameters.keys())



def test_analysis_profiler_actiondynamicdata_is_not_abstract():
    assert not inspect.isabstract(analysis_profiler_ActionDynamicData)


def test_analysis_profiler_actiondynamicdata_constructor_exists():
    assert callable(analysis_profiler_ActionDynamicData.__init__)


def test_analysis_profiler_actiondynamicdata_constructor_args():
    sig = inspect.signature(analysis_profiler_ActionDynamicData.__init__)
    params = list(sig.parameters.keys())



def test_analysis_profiler_actordynamicdata_is_not_abstract():
    assert not inspect.isabstract(analysis_profiler_ActorDynamicData)


def test_analysis_profiler_actordynamicdata_constructor_exists():
    assert callable(analysis_profiler_ActorDynamicData.__init__)


def test_analysis_profiler_actordynamicdata_constructor_args():
    sig = inspect.signature(analysis_profiler_ActorDynamicData.__init__)
    params = list(sig.parameters.keys())



def test_bufferdynamicdata_is_not_abstract():
    assert not inspect.isabstract(BufferDynamicData)


def test_bufferdynamicdata_constructor_exists():
    assert callable(BufferDynamicData.__init__)


def test_bufferdynamicdata_constructor_args():
    sig = inspect.signature(BufferDynamicData.__init__)
    params = list(sig.parameters.keys())



def test_actordynamicdata_is_not_abstract():
    assert not inspect.isabstract(ActorDynamicData)


def test_actordynamicdata_constructor_exists():
    assert callable(ActorDynamicData.__init__)


def test_actordynamicdata_constructor_args():
    sig = inspect.signature(ActorDynamicData.__init__)
    params = list(sig.parameters.keys())



def test_codedata_is_not_abstract():
    assert not inspect.isabstract(CodeData)


def test_codedata_constructor_exists():
    assert callable(CodeData.__init__)


def test_codedata_constructor_args():
    sig = inspect.signature(CodeData.__init__)
    params = list(sig.parameters.keys())



def test_analysis_profiler_complexcodedata_is_not_abstract():
    assert not inspect.isabstract(analysis_profiler_ComplexCodeData)


def test_analysis_profiler_complexcodedata_constructor_exists():
    assert callable(analysis_profiler_ComplexCodeData.__init__)


def test_analysis_profiler_complexcodedata_constructor_args():
    sig = inspect.signature(analysis_profiler_ComplexCodeData.__init__)
    params = list(sig.parameters.keys())



def test_stringtointegermap_is_not_abstract():
    assert not inspect.isabstract(StringToIntegerMap)


def test_stringtointegermap_constructor_exists():
    assert callable(StringToIntegerMap.__init__)


def test_stringtointegermap_constructor_args():
    sig = inspect.signature(StringToIntegerMap.__init__)
    params = list(sig.parameters.keys())



def test_analysis_profiler_codedata_is_not_abstract():
    assert not inspect.isabstract(analysis_profiler_CodeData)


def test_analysis_profiler_codedata_constructor_exists():
    assert callable(analysis_profiler_CodeData.__init__)


def test_analysis_profiler_codedata_constructor_args():
    sig = inspect.signature(analysis_profiler_CodeData.__init__)
    params = list(sig.parameters.keys())
    assert "blockName" in params, "Missing parameter 'blockName'"
    assert "nol" in params, "Missing parameter 'nol'"

def test_analysis_profiler_codedata_has_blockName():
    assert hasattr(analysis_profiler_CodeData, "blockName")
    descriptor = None
    for klass in analysis_profiler_CodeData.__mro__:
        if "blockName" in klass.__dict__:
            descriptor = klass.__dict__["blockName"]
            break
    assert isinstance(descriptor, property)

def test_analysis_profiler_codedata_has_nol():
    assert hasattr(analysis_profiler_CodeData, "nol")
    descriptor = None
    for klass in analysis_profiler_CodeData.__mro__:
        if "nol" in klass.__dict__:
            descriptor = klass.__dict__["nol"]
            break
    assert isinstance(descriptor, property)



def test_complexcodedata_is_not_abstract():
    assert not inspect.isabstract(ComplexCodeData)


def test_complexcodedata_constructor_exists():
    assert callable(ComplexCodeData.__init__)


def test_complexcodedata_constructor_args():
    sig = inspect.signature(ComplexCodeData.__init__)
    params = list(sig.parameters.keys())



def test_profiler_analysis_network_is_not_abstract():
    assert not inspect.isabstract(profiler_analysis_Network)


def test_profiler_analysis_network_constructor_exists():
    assert callable(profiler_analysis_Network.__init__)


def test_profiler_analysis_network_constructor_args():
    sig = inspect.signature(profiler_analysis_Network.__init__)
    params = list(sig.parameters.keys())



def test_analysisreport_is_not_abstract():
    assert not inspect.isabstract(AnalysisReport)


def test_analysisreport_constructor_exists():
    assert callable(AnalysisReport.__init__)


def test_analysisreport_constructor_args():
    sig = inspect.signature(AnalysisReport.__init__)
    params = list(sig.parameters.keys())



def test_analysis_profiler_memoryprofilingreport_is_not_abstract():
    assert not inspect.isabstract(analysis_profiler_MemoryProfilingReport)


def test_analysis_profiler_memoryprofilingreport_constructor_exists():
    assert callable(analysis_profiler_MemoryProfilingReport.__init__)


def test_analysis_profiler_memoryprofilingreport_constructor_args():
    sig = inspect.signature(analysis_profiler_MemoryProfilingReport.__init__)
    params = list(sig.parameters.keys())
    assert "networkName" in params, "Missing parameter 'networkName'"

def test_analysis_profiler_memoryprofilingreport_has_networkName():
    assert hasattr(analysis_profiler_MemoryProfilingReport, "networkName")
    descriptor = None
    for klass in analysis_profiler_MemoryProfilingReport.__mro__:
        if "networkName" in klass.__dict__:
            descriptor = klass.__dict__["networkName"]
            break
    assert isinstance(descriptor, property)



def test_analysis_partitioning_comcostpartitioningreport_is_not_abstract():
    assert not inspect.isabstract(analysis_partitioning_ComCostPartitioningReport)


def test_analysis_partitioning_comcostpartitioningreport_constructor_exists():
    assert callable(analysis_partitioning_ComCostPartitioningReport.__init__)


def test_analysis_partitioning_comcostpartitioningreport_constructor_args():
    sig = inspect.signature(analysis_partitioning_ComCostPartitioningReport.__init__)
    params = list(sig.parameters.keys())
    assert "bitAccurate" in params, "Missing parameter 'bitAccurate'"

def test_analysis_partitioning_comcostpartitioningreport_has_bitAccurate():
    assert hasattr(analysis_partitioning_ComCostPartitioningReport, "bitAccurate")
    descriptor = None
    for klass in analysis_partitioning_ComCostPartitioningReport.__mro__:
        if "bitAccurate" in klass.__dict__:
            descriptor = klass.__dict__["bitAccurate"]
            break
    assert isinstance(descriptor, property)



def test_analysis_trace_tracesizereport_is_not_abstract():
    assert not inspect.isabstract(analysis_trace_TraceSizeReport)


def test_analysis_trace_tracesizereport_constructor_exists():
    assert callable(analysis_trace_TraceSizeReport.__init__)


def test_analysis_trace_tracesizereport_constructor_args():
    sig = inspect.signature(analysis_trace_TraceSizeReport.__init__)
    params = list(sig.parameters.keys())
    assert "firings" in params, "Missing parameter 'firings'"
    assert "dependencies" in params, "Missing parameter 'dependencies'"

def test_analysis_trace_tracesizereport_has_firings():
    assert hasattr(analysis_trace_TraceSizeReport, "firings")
    descriptor = None
    for klass in analysis_trace_TraceSizeReport.__mro__:
        if "firings" in klass.__dict__:
            descriptor = klass.__dict__["firings"]
            break
    assert isinstance(descriptor, property)

def test_analysis_trace_tracesizereport_has_dependencies():
    assert hasattr(analysis_trace_TraceSizeReport, "dependencies")
    descriptor = None
    for klass in analysis_trace_TraceSizeReport.__mro__:
        if "dependencies" in klass.__dict__:
            descriptor = klass.__dict__["dependencies"]
            break
    assert isinstance(descriptor, property)



def test_analysis_bottlenecks_scheduledimpactanalysisreport_is_not_abstract():
    assert not inspect.isabstract(analysis_bottlenecks_ScheduledImpactAnalysisReport)


def test_analysis_bottlenecks_scheduledimpactanalysisreport_constructor_exists():
    assert callable(analysis_bottlenecks_ScheduledImpactAnalysisReport.__init__)


def test_analysis_bottlenecks_scheduledimpactanalysisreport_constructor_args():
    sig = inspect.signature(analysis_bottlenecks_ScheduledImpactAnalysisReport.__init__)
    params = list(sig.parameters.keys())
    assert "classLevel" in params, "Missing parameter 'classLevel'"

def test_analysis_bottlenecks_scheduledimpactanalysisreport_has_classLevel():
    assert hasattr(analysis_bottlenecks_ScheduledImpactAnalysisReport, "classLevel")
    descriptor = None
    for klass in analysis_bottlenecks_ScheduledImpactAnalysisReport.__mro__:
        if "classLevel" in klass.__dict__:
            descriptor = klass.__dict__["classLevel"]
            break
    assert isinstance(descriptor, property)



def test_analysis_pipelining_impactanalysisreport_is_not_abstract():
    assert not inspect.isabstract(analysis_pipelining_ImpactAnalysisReport)


def test_analysis_pipelining_impactanalysisreport_constructor_exists():
    assert callable(analysis_pipelining_ImpactAnalysisReport.__init__)


def test_analysis_pipelining_impactanalysisreport_constructor_args():
    sig = inspect.signature(analysis_pipelining_ImpactAnalysisReport.__init__)
    params = list(sig.parameters.keys())



def test_analysis_buffers_optimalbuffersreport_is_not_abstract():
    assert not inspect.isabstract(analysis_buffers_OptimalBuffersReport)


def test_analysis_buffers_optimalbuffersreport_constructor_exists():
    assert callable(analysis_buffers_OptimalBuffersReport.__init__)


def test_analysis_buffers_optimalbuffersreport_constructor_args():
    sig = inspect.signature(analysis_buffers_OptimalBuffersReport.__init__)
    params = list(sig.parameters.keys())
    assert "bitAccurate" in params, "Missing parameter 'bitAccurate'"
    assert "pow2" in params, "Missing parameter 'pow2'"

def test_analysis_buffers_optimalbuffersreport_has_bitAccurate():
    assert hasattr(analysis_buffers_OptimalBuffersReport, "bitAccurate")
    descriptor = None
    for klass in analysis_buffers_OptimalBuffersReport.__mro__:
        if "bitAccurate" in klass.__dict__:
            descriptor = klass.__dict__["bitAccurate"]
            break
    assert isinstance(descriptor, property)

def test_analysis_buffers_optimalbuffersreport_has_pow2():
    assert hasattr(analysis_buffers_OptimalBuffersReport, "pow2")
    descriptor = None
    for klass in analysis_buffers_OptimalBuffersReport.__mro__:
        if "pow2" in klass.__dict__:
            descriptor = klass.__dict__["pow2"]
            break
    assert isinstance(descriptor, property)



def test_analysis_profiler_benchmarkreport_is_not_abstract():
    assert not inspect.isabstract(analysis_profiler_BenchmarkReport)


def test_analysis_profiler_benchmarkreport_constructor_exists():
    assert callable(analysis_profiler_BenchmarkReport.__init__)


def test_analysis_profiler_benchmarkreport_constructor_args():
    sig = inspect.signature(analysis_profiler_BenchmarkReport.__init__)
    params = list(sig.parameters.keys())
    assert "column_names" in params, "Missing parameter 'column_names'"

def test_analysis_profiler_benchmarkreport_has_column_names():
    assert hasattr(analysis_profiler_BenchmarkReport, "column_names")
    descriptor = None
    for klass in analysis_profiler_BenchmarkReport.__mro__:
        if "column_names" in klass.__dict__:
            descriptor = klass.__dict__["column_names"]
            break
    assert isinstance(descriptor, property)



def test_analysis_profiler_dynamicprofilingreport_is_not_abstract():
    assert not inspect.isabstract(analysis_profiler_DynamicProfilingReport)


def test_analysis_profiler_dynamicprofilingreport_constructor_exists():
    assert callable(analysis_profiler_DynamicProfilingReport.__init__)


def test_analysis_profiler_dynamicprofilingreport_constructor_args():
    sig = inspect.signature(analysis_profiler_DynamicProfilingReport.__init__)
    params = list(sig.parameters.keys())



def test_analysis_trace_tracecomparatorreport_is_not_abstract():
    assert not inspect.isabstract(analysis_trace_TraceComparatorReport)


def test_analysis_trace_tracecomparatorreport_constructor_exists():
    assert callable(analysis_trace_TraceComparatorReport.__init__)


def test_analysis_trace_tracecomparatorreport_constructor_args():
    sig = inspect.signature(analysis_trace_TraceComparatorReport.__init__)
    params = list(sig.parameters.keys())



def test_analysis_bottlenecks_bottleneckswithschedulingreport_is_not_abstract():
    assert not inspect.isabstract(analysis_bottlenecks_BottlenecksWithSchedulingReport)


def test_analysis_bottlenecks_bottleneckswithschedulingreport_constructor_exists():
    assert callable(analysis_bottlenecks_BottlenecksWithSchedulingReport.__init__)


def test_analysis_bottlenecks_bottleneckswithschedulingreport_constructor_args():
    sig = inspect.signature(analysis_bottlenecks_BottlenecksWithSchedulingReport.__init__)
    params = list(sig.parameters.keys())
    assert "totalFirings" in params, "Missing parameter 'totalFirings'"
    assert "cpFirings" in params, "Missing parameter 'cpFirings'"
    assert "cpWeight" in params, "Missing parameter 'cpWeight'"
    assert "cpBlockingTime" in params, "Missing parameter 'cpBlockingTime'"
    assert "executionTime" in params, "Missing parameter 'executionTime'"
    assert "totalWeight" in params, "Missing parameter 'totalWeight'"

def test_analysis_bottlenecks_bottleneckswithschedulingreport_has_totalFirings():
    assert hasattr(analysis_bottlenecks_BottlenecksWithSchedulingReport, "totalFirings")
    descriptor = None
    for klass in analysis_bottlenecks_BottlenecksWithSchedulingReport.__mro__:
        if "totalFirings" in klass.__dict__:
            descriptor = klass.__dict__["totalFirings"]
            break
    assert isinstance(descriptor, property)

def test_analysis_bottlenecks_bottleneckswithschedulingreport_has_cpFirings():
    assert hasattr(analysis_bottlenecks_BottlenecksWithSchedulingReport, "cpFirings")
    descriptor = None
    for klass in analysis_bottlenecks_BottlenecksWithSchedulingReport.__mro__:
        if "cpFirings" in klass.__dict__:
            descriptor = klass.__dict__["cpFirings"]
            break
    assert isinstance(descriptor, property)

def test_analysis_bottlenecks_bottleneckswithschedulingreport_has_cpWeight():
    assert hasattr(analysis_bottlenecks_BottlenecksWithSchedulingReport, "cpWeight")
    descriptor = None
    for klass in analysis_bottlenecks_BottlenecksWithSchedulingReport.__mro__:
        if "cpWeight" in klass.__dict__:
            descriptor = klass.__dict__["cpWeight"]
            break
    assert isinstance(descriptor, property)

def test_analysis_bottlenecks_bottleneckswithschedulingreport_has_cpBlockingTime():
    assert hasattr(analysis_bottlenecks_BottlenecksWithSchedulingReport, "cpBlockingTime")
    descriptor = None
    for klass in analysis_bottlenecks_BottlenecksWithSchedulingReport.__mro__:
        if "cpBlockingTime" in klass.__dict__:
            descriptor = klass.__dict__["cpBlockingTime"]
            break
    assert isinstance(descriptor, property)

def test_analysis_bottlenecks_bottleneckswithschedulingreport_has_executionTime():
    assert hasattr(analysis_bottlenecks_BottlenecksWithSchedulingReport, "executionTime")
    descriptor = None
    for klass in analysis_bottlenecks_BottlenecksWithSchedulingReport.__mro__:
        if "executionTime" in klass.__dict__:
            descriptor = klass.__dict__["executionTime"]
            break
    assert isinstance(descriptor, property)

def test_analysis_bottlenecks_bottleneckswithschedulingreport_has_totalWeight():
    assert hasattr(analysis_bottlenecks_BottlenecksWithSchedulingReport, "totalWeight")
    descriptor = None
    for klass in analysis_bottlenecks_BottlenecksWithSchedulingReport.__mro__:
        if "totalWeight" in klass.__dict__:
            descriptor = klass.__dict__["totalWeight"]
            break
    assert isinstance(descriptor, property)



def test_analysis_trace_compressedtracereport_is_not_abstract():
    assert not inspect.isabstract(analysis_trace_CompressedTraceReport)


def test_analysis_trace_compressedtracereport_constructor_exists():
    assert callable(analysis_trace_CompressedTraceReport.__init__)


def test_analysis_trace_compressedtracereport_constructor_args():
    sig = inspect.signature(analysis_trace_CompressedTraceReport.__init__)
    params = list(sig.parameters.keys())
    assert "traceFile" in params, "Missing parameter 'traceFile'"

def test_analysis_trace_compressedtracereport_has_traceFile():
    assert hasattr(analysis_trace_CompressedTraceReport, "traceFile")
    descriptor = None
    for klass in analysis_trace_CompressedTraceReport.__mro__:
        if "traceFile" in klass.__dict__:
            descriptor = klass.__dict__["traceFile"]
            break
    assert isinstance(descriptor, property)



def test_analysis_pipelining_actionsvariablepipeliningreport_is_not_abstract():
    assert not inspect.isabstract(analysis_pipelining_ActionsVariablePipeliningReport)


def test_analysis_pipelining_actionsvariablepipeliningreport_constructor_exists():
    assert callable(analysis_pipelining_ActionsVariablePipeliningReport.__init__)


def test_analysis_pipelining_actionsvariablepipeliningreport_constructor_args():
    sig = inspect.signature(analysis_pipelining_ActionsVariablePipeliningReport.__init__)
    params = list(sig.parameters.keys())



def test_analysis_buffers_boundedbuffersreport_is_not_abstract():
    assert not inspect.isabstract(analysis_buffers_BoundedBuffersReport)


def test_analysis_buffers_boundedbuffersreport_constructor_exists():
    assert callable(analysis_buffers_BoundedBuffersReport.__init__)


def test_analysis_buffers_boundedbuffersreport_constructor_args():
    sig = inspect.signature(analysis_buffers_BoundedBuffersReport.__init__)
    params = list(sig.parameters.keys())
    assert "bitSize" in params, "Missing parameter 'bitSize'"
    assert "tokenSize" in params, "Missing parameter 'tokenSize'"
    assert "bitAccurate" in params, "Missing parameter 'bitAccurate'"
    assert "pow2" in params, "Missing parameter 'pow2'"

def test_analysis_buffers_boundedbuffersreport_has_bitSize():
    assert hasattr(analysis_buffers_BoundedBuffersReport, "bitSize")
    descriptor = None
    for klass in analysis_buffers_BoundedBuffersReport.__mro__:
        if "bitSize" in klass.__dict__:
            descriptor = klass.__dict__["bitSize"]
            break
    assert isinstance(descriptor, property)

def test_analysis_buffers_boundedbuffersreport_has_tokenSize():
    assert hasattr(analysis_buffers_BoundedBuffersReport, "tokenSize")
    descriptor = None
    for klass in analysis_buffers_BoundedBuffersReport.__mro__:
        if "tokenSize" in klass.__dict__:
            descriptor = klass.__dict__["tokenSize"]
            break
    assert isinstance(descriptor, property)

def test_analysis_buffers_boundedbuffersreport_has_bitAccurate():
    assert hasattr(analysis_buffers_BoundedBuffersReport, "bitAccurate")
    descriptor = None
    for klass in analysis_buffers_BoundedBuffersReport.__mro__:
        if "bitAccurate" in klass.__dict__:
            descriptor = klass.__dict__["bitAccurate"]
            break
    assert isinstance(descriptor, property)

def test_analysis_buffers_boundedbuffersreport_has_pow2():
    assert hasattr(analysis_buffers_BoundedBuffersReport, "pow2")
    descriptor = None
    for klass in analysis_buffers_BoundedBuffersReport.__mro__:
        if "pow2" in klass.__dict__:
            descriptor = klass.__dict__["pow2"]
            break
    assert isinstance(descriptor, property)



def test_analysis_partitioning_workloadbalancepartitioningreport_is_not_abstract():
    assert not inspect.isabstract(analysis_partitioning_WorkloadBalancePartitioningReport)


def test_analysis_partitioning_workloadbalancepartitioningreport_constructor_exists():
    assert callable(analysis_partitioning_WorkloadBalancePartitioningReport.__init__)


def test_analysis_partitioning_workloadbalancepartitioningreport_constructor_args():
    sig = inspect.signature(analysis_partitioning_WorkloadBalancePartitioningReport.__init__)
    params = list(sig.parameters.keys())



def test_analysis_bottlenecks_bottlenecksreport_is_not_abstract():
    assert not inspect.isabstract(analysis_bottlenecks_BottlenecksReport)


def test_analysis_bottlenecks_bottlenecksreport_constructor_exists():
    assert callable(analysis_bottlenecks_BottlenecksReport.__init__)


def test_analysis_bottlenecks_bottlenecksreport_constructor_args():
    sig = inspect.signature(analysis_bottlenecks_BottlenecksReport.__init__)
    params = list(sig.parameters.keys())
    assert "cpWeight" in params, "Missing parameter 'cpWeight'"
    assert "cpFirings" in params, "Missing parameter 'cpFirings'"
    assert "totalVariance" in params, "Missing parameter 'totalVariance'"
    assert "totalFirings" in params, "Missing parameter 'totalFirings'"
    assert "totalWeight" in params, "Missing parameter 'totalWeight'"
    assert "cpVariance" in params, "Missing parameter 'cpVariance'"

def test_analysis_bottlenecks_bottlenecksreport_has_cpWeight():
    assert hasattr(analysis_bottlenecks_BottlenecksReport, "cpWeight")
    descriptor = None
    for klass in analysis_bottlenecks_BottlenecksReport.__mro__:
        if "cpWeight" in klass.__dict__:
            descriptor = klass.__dict__["cpWeight"]
            break
    assert isinstance(descriptor, property)

def test_analysis_bottlenecks_bottlenecksreport_has_cpFirings():
    assert hasattr(analysis_bottlenecks_BottlenecksReport, "cpFirings")
    descriptor = None
    for klass in analysis_bottlenecks_BottlenecksReport.__mro__:
        if "cpFirings" in klass.__dict__:
            descriptor = klass.__dict__["cpFirings"]
            break
    assert isinstance(descriptor, property)

def test_analysis_bottlenecks_bottlenecksreport_has_totalVariance():
    assert hasattr(analysis_bottlenecks_BottlenecksReport, "totalVariance")
    descriptor = None
    for klass in analysis_bottlenecks_BottlenecksReport.__mro__:
        if "totalVariance" in klass.__dict__:
            descriptor = klass.__dict__["totalVariance"]
            break
    assert isinstance(descriptor, property)

def test_analysis_bottlenecks_bottlenecksreport_has_totalFirings():
    assert hasattr(analysis_bottlenecks_BottlenecksReport, "totalFirings")
    descriptor = None
    for klass in analysis_bottlenecks_BottlenecksReport.__mro__:
        if "totalFirings" in klass.__dict__:
            descriptor = klass.__dict__["totalFirings"]
            break
    assert isinstance(descriptor, property)

def test_analysis_bottlenecks_bottlenecksreport_has_totalWeight():
    assert hasattr(analysis_bottlenecks_BottlenecksReport, "totalWeight")
    descriptor = None
    for klass in analysis_bottlenecks_BottlenecksReport.__mro__:
        if "totalWeight" in klass.__dict__:
            descriptor = klass.__dict__["totalWeight"]
            break
    assert isinstance(descriptor, property)

def test_analysis_bottlenecks_bottlenecksreport_has_cpVariance():
    assert hasattr(analysis_bottlenecks_BottlenecksReport, "cpVariance")
    descriptor = None
    for klass in analysis_bottlenecks_BottlenecksReport.__mro__:
        if "cpVariance" in klass.__dict__:
            descriptor = klass.__dict__["cpVariance"]
            break
    assert isinstance(descriptor, property)



def test_analysis_trace_markowmodeltracereport_is_not_abstract():
    assert not inspect.isabstract(analysis_trace_MarkowModelTraceReport)


def test_analysis_trace_markowmodeltracereport_constructor_exists():
    assert callable(analysis_trace_MarkowModelTraceReport.__init__)


def test_analysis_trace_markowmodeltracereport_constructor_args():
    sig = inspect.signature(analysis_trace_MarkowModelTraceReport.__init__)
    params = list(sig.parameters.keys())



def test_analysis_bottlenecks_impactanalysisreport_is_not_abstract():
    assert not inspect.isabstract(analysis_bottlenecks_ImpactAnalysisReport)


def test_analysis_bottlenecks_impactanalysisreport_constructor_exists():
    assert callable(analysis_bottlenecks_ImpactAnalysisReport.__init__)


def test_analysis_bottlenecks_impactanalysisreport_constructor_args():
    sig = inspect.signature(analysis_bottlenecks_ImpactAnalysisReport.__init__)
    params = list(sig.parameters.keys())
    assert "classLevel" in params, "Missing parameter 'classLevel'"

def test_analysis_bottlenecks_impactanalysisreport_has_classLevel():
    assert hasattr(analysis_bottlenecks_ImpactAnalysisReport, "classLevel")
    descriptor = None
    for klass in analysis_bottlenecks_ImpactAnalysisReport.__mro__:
        if "classLevel" in klass.__dict__:
            descriptor = klass.__dict__["classLevel"]
            break
    assert isinstance(descriptor, property)



def test_analysis_partitioning_balancedpipelinepartitioningreport_is_not_abstract():
    assert not inspect.isabstract(analysis_partitioning_BalancedPipelinePartitioningReport)


def test_analysis_partitioning_balancedpipelinepartitioningreport_constructor_exists():
    assert callable(analysis_partitioning_BalancedPipelinePartitioningReport.__init__)


def test_analysis_partitioning_balancedpipelinepartitioningreport_constructor_args():
    sig = inspect.signature(analysis_partitioning_BalancedPipelinePartitioningReport.__init__)
    params = list(sig.parameters.keys())



def test_analysis_profiler_codeprofilingreport_is_not_abstract():
    assert not inspect.isabstract(analysis_profiler_CodeProfilingReport)


def test_analysis_profiler_codeprofilingreport_constructor_exists():
    assert callable(analysis_profiler_CodeProfilingReport.__init__)


def test_analysis_profiler_codeprofilingreport_constructor_args():
    sig = inspect.signature(analysis_profiler_CodeProfilingReport.__init__)
    params = list(sig.parameters.keys())



def test_analysis_analysisreport_is_not_abstract():
    assert not inspect.isabstract(analysis_AnalysisReport)


def test_analysis_analysisreport_constructor_exists():
    assert callable(analysis_AnalysisReport.__init__)


def test_analysis_analysisreport_constructor_args():
    sig = inspect.signature(analysis_AnalysisReport.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"
    assert "algorithm" in params, "Missing parameter 'algorithm'"

def test_analysis_analysisreport_has_date():
    assert hasattr(analysis_AnalysisReport, "date")
    descriptor = None
    for klass in analysis_AnalysisReport.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_analysis_analysisreport_has_algorithm():
    assert hasattr(analysis_AnalysisReport, "algorithm")
    descriptor = None
    for klass in analysis_AnalysisReport.__mro__:
        if "algorithm" in klass.__dict__:
            descriptor = klass.__dict__["algorithm"]
            break
    assert isinstance(descriptor, property)



def test_analysis_scheduling_markovschedulingtransition_is_not_abstract():
    assert not inspect.isabstract(analysis_scheduling_MarkovSchedulingTransition)


def test_analysis_scheduling_markovschedulingtransition_constructor_exists():
    assert callable(analysis_scheduling_MarkovSchedulingTransition.__init__)


def test_analysis_scheduling_markovschedulingtransition_constructor_args():
    sig = inspect.signature(analysis_scheduling_MarkovSchedulingTransition.__init__)
    params = list(sig.parameters.keys())
    assert "firings" in params, "Missing parameter 'firings'"
    assert "name" in params, "Missing parameter 'name'"

def test_analysis_scheduling_markovschedulingtransition_has_firings():
    assert hasattr(analysis_scheduling_MarkovSchedulingTransition, "firings")
    descriptor = None
    for klass in analysis_scheduling_MarkovSchedulingTransition.__mro__:
        if "firings" in klass.__dict__:
            descriptor = klass.__dict__["firings"]
            break
    assert isinstance(descriptor, property)

def test_analysis_scheduling_markovschedulingtransition_has_name():
    assert hasattr(analysis_scheduling_MarkovSchedulingTransition, "name")
    descriptor = None
    for klass in analysis_scheduling_MarkovSchedulingTransition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_analysis_caseoptimal_caseoptimalactorselectionschedule_is_not_abstract():
    assert not inspect.isabstract(analysis_caseoptimal_CaseOptimalActorSelectionSchedule)


def test_analysis_caseoptimal_caseoptimalactorselectionschedule_constructor_exists():
    assert callable(analysis_caseoptimal_CaseOptimalActorSelectionSchedule.__init__)


def test_analysis_caseoptimal_caseoptimalactorselectionschedule_constructor_args():
    sig = inspect.signature(analysis_caseoptimal_CaseOptimalActorSelectionSchedule.__init__)
    params = list(sig.parameters.keys())



def test_partitiontoactorselectionschedulemap_is_not_abstract():
    assert not inspect.isabstract(PartitionToActorSelectionScheduleMap)


def test_partitiontoactorselectionschedulemap_constructor_exists():
    assert callable(PartitionToActorSelectionScheduleMap.__init__)


def test_partitiontoactorselectionschedulemap_constructor_args():
    sig = inspect.signature(PartitionToActorSelectionScheduleMap.__init__)
    params = list(sig.parameters.keys())



def test_analysis_caseoptimal_caseoptimalschedulereport_is_not_abstract():
    assert not inspect.isabstract(analysis_caseoptimal_CaseOptimalScheduleReport)


def test_analysis_caseoptimal_caseoptimalschedulereport_constructor_exists():
    assert callable(analysis_caseoptimal_CaseOptimalScheduleReport.__init__)


def test_analysis_caseoptimal_caseoptimalschedulereport_constructor_args():
    sig = inspect.signature(analysis_caseoptimal_CaseOptimalScheduleReport.__init__)
    params = list(sig.parameters.keys())
    assert "partitionFilePath" in params, "Missing parameter 'partitionFilePath'"
    assert "traceFile" in params, "Missing parameter 'traceFile'"
    assert "pipeline" in params, "Missing parameter 'pipeline'"

def test_analysis_caseoptimal_caseoptimalschedulereport_has_partitionFilePath():
    assert hasattr(analysis_caseoptimal_CaseOptimalScheduleReport, "partitionFilePath")
    descriptor = None
    for klass in analysis_caseoptimal_CaseOptimalScheduleReport.__mro__:
        if "partitionFilePath" in klass.__dict__:
            descriptor = klass.__dict__["partitionFilePath"]
            break
    assert isinstance(descriptor, property)

def test_analysis_caseoptimal_caseoptimalschedulereport_has_traceFile():
    assert hasattr(analysis_caseoptimal_CaseOptimalScheduleReport, "traceFile")
    descriptor = None
    for klass in analysis_caseoptimal_CaseOptimalScheduleReport.__mro__:
        if "traceFile" in klass.__dict__:
            descriptor = klass.__dict__["traceFile"]
            break
    assert isinstance(descriptor, property)

def test_analysis_caseoptimal_caseoptimalschedulereport_has_pipeline():
    assert hasattr(analysis_caseoptimal_CaseOptimalScheduleReport, "pipeline")
    descriptor = None
    for klass in analysis_caseoptimal_CaseOptimalScheduleReport.__mro__:
        if "pipeline" in klass.__dict__:
            descriptor = klass.__dict__["pipeline"]
            break
    assert isinstance(descriptor, property)



def test_analysis_scheduling_markovschedulingstate_is_not_abstract():
    assert not inspect.isabstract(analysis_scheduling_MarkovSchedulingState)


def test_analysis_scheduling_markovschedulingstate_constructor_exists():
    assert callable(analysis_scheduling_MarkovSchedulingState.__init__)


def test_analysis_scheduling_markovschedulingstate_constructor_args():
    sig = inspect.signature(analysis_scheduling_MarkovSchedulingState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "firings" in params, "Missing parameter 'firings'"

def test_analysis_scheduling_markovschedulingstate_has_name():
    assert hasattr(analysis_scheduling_MarkovSchedulingState, "name")
    descriptor = None
    for klass in analysis_scheduling_MarkovSchedulingState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_analysis_scheduling_markovschedulingstate_has_firings():
    assert hasattr(analysis_scheduling_MarkovSchedulingState, "firings")
    descriptor = None
    for klass in analysis_scheduling_MarkovSchedulingState.__mro__:
        if "firings" in klass.__dict__:
            descriptor = klass.__dict__["firings"]
            break
    assert isinstance(descriptor, property)



def test_markovschedulingtransition_is_not_abstract():
    assert not inspect.isabstract(MarkovSchedulingTransition)


def test_markovschedulingtransition_constructor_exists():
    assert callable(MarkovSchedulingTransition.__init__)


def test_markovschedulingtransition_constructor_args():
    sig = inspect.signature(MarkovSchedulingTransition.__init__)
    params = list(sig.parameters.keys())



def test_markovschedulingstate_is_not_abstract():
    assert not inspect.isabstract(MarkovSchedulingState)


def test_markovschedulingstate_constructor_exists():
    assert callable(MarkovSchedulingState.__init__)


def test_markovschedulingstate_constructor_args():
    sig = inspect.signature(MarkovSchedulingState.__init__)
    params = list(sig.parameters.keys())



def test_scheduling_analysis_actor_is_not_abstract():
    assert not inspect.isabstract(scheduling_analysis_Actor)


def test_scheduling_analysis_actor_constructor_exists():
    assert callable(scheduling_analysis_Actor.__init__)


def test_scheduling_analysis_actor_constructor_args():
    sig = inspect.signature(scheduling_analysis_Actor.__init__)
    params = list(sig.parameters.keys())



def test_analysis_scheduling_markovpartitionscheduler_is_not_abstract():
    assert not inspect.isabstract(analysis_scheduling_MarkovPartitionScheduler)


def test_analysis_scheduling_markovpartitionscheduler_constructor_exists():
    assert callable(analysis_scheduling_MarkovPartitionScheduler.__init__)


def test_analysis_scheduling_markovpartitionscheduler_constructor_args():
    sig = inspect.signature(analysis_scheduling_MarkovPartitionScheduler.__init__)
    params = list(sig.parameters.keys())
    assert "partitionId" in params, "Missing parameter 'partitionId'"

def test_analysis_scheduling_markovpartitionscheduler_has_partitionId():
    assert hasattr(analysis_scheduling_MarkovPartitionScheduler, "partitionId")
    descriptor = None
    for klass in analysis_scheduling_MarkovPartitionScheduler.__mro__:
        if "partitionId" in klass.__dict__:
            descriptor = klass.__dict__["partitionId"]
            break
    assert isinstance(descriptor, property)



def test_scheduling_analysis_network_is_not_abstract():
    assert not inspect.isabstract(scheduling_analysis_Network)


def test_scheduling_analysis_network_constructor_exists():
    assert callable(scheduling_analysis_Network.__init__)


def test_scheduling_analysis_network_constructor_args():
    sig = inspect.signature(scheduling_analysis_Network.__init__)
    params = list(sig.parameters.keys())



def test_markovpartitionscheduler_is_not_abstract():
    assert not inspect.isabstract(MarkovPartitionScheduler)


def test_markovpartitionscheduler_constructor_exists():
    assert callable(MarkovPartitionScheduler.__init__)


def test_markovpartitionscheduler_constructor_args():
    sig = inspect.signature(MarkovPartitionScheduler.__init__)
    params = list(sig.parameters.keys())



def test_analysis_scheduling_markovsimpleschedulerreport_is_not_abstract():
    assert not inspect.isabstract(analysis_scheduling_MarkovSimpleSchedulerReport)


def test_analysis_scheduling_markovsimpleschedulerreport_constructor_exists():
    assert callable(analysis_scheduling_MarkovSimpleSchedulerReport.__init__)


def test_analysis_scheduling_markovsimpleschedulerreport_constructor_args():
    sig = inspect.signature(analysis_scheduling_MarkovSimpleSchedulerReport.__init__)
    params = list(sig.parameters.keys())



def test_fsmcombination_is_not_abstract():
    assert not inspect.isabstract(FSMCombination)


def test_fsmcombination_constructor_exists():
    assert callable(FSMCombination.__init__)


def test_fsmcombination_constructor_args():
    sig = inspect.signature(FSMCombination.__init__)
    params = list(sig.parameters.keys())



def test_analysis_scheduling_fsmcondition_is_not_abstract():
    assert not inspect.isabstract(analysis_scheduling_FSMCondition)


def test_analysis_scheduling_fsmcondition_constructor_exists():
    assert callable(analysis_scheduling_FSMCondition.__init__)


def test_analysis_scheduling_fsmcondition_constructor_args():
    sig = inspect.signature(analysis_scheduling_FSMCondition.__init__)
    params = list(sig.parameters.keys())
    assert "valName" in params, "Missing parameter 'valName'"
    assert "compval" in params, "Missing parameter 'compval'"
    assert "comp" in params, "Missing parameter 'comp'"

def test_analysis_scheduling_fsmcondition_has_valName():
    assert hasattr(analysis_scheduling_FSMCondition, "valName")
    descriptor = None
    for klass in analysis_scheduling_FSMCondition.__mro__:
        if "valName" in klass.__dict__:
            descriptor = klass.__dict__["valName"]
            break
    assert isinstance(descriptor, property)

def test_analysis_scheduling_fsmcondition_has_compval():
    assert hasattr(analysis_scheduling_FSMCondition, "compval")
    descriptor = None
    for klass in analysis_scheduling_FSMCondition.__mro__:
        if "compval" in klass.__dict__:
            descriptor = klass.__dict__["compval"]
            break
    assert isinstance(descriptor, property)

def test_analysis_scheduling_fsmcondition_has_comp():
    assert hasattr(analysis_scheduling_FSMCondition, "comp")
    descriptor = None
    for klass in analysis_scheduling_FSMCondition.__mro__:
        if "comp" in klass.__dict__:
            descriptor = klass.__dict__["comp"]
            break
    assert isinstance(descriptor, property)



def test_analysis_scheduling_fsmcombination_is_not_abstract():
    assert not inspect.isabstract(analysis_scheduling_FSMCombination)


def test_analysis_scheduling_fsmcombination_constructor_exists():
    assert callable(analysis_scheduling_FSMCombination.__init__)


def test_analysis_scheduling_fsmcombination_constructor_args():
    sig = inspect.signature(analysis_scheduling_FSMCombination.__init__)
    params = list(sig.parameters.keys())
    assert "combinator" in params, "Missing parameter 'combinator'"

def test_analysis_scheduling_fsmcombination_has_combinator():
    assert hasattr(analysis_scheduling_FSMCombination, "combinator")
    descriptor = None
    for klass in analysis_scheduling_FSMCombination.__mro__:
        if "combinator" in klass.__dict__:
            descriptor = klass.__dict__["combinator"]
            break
    assert isinstance(descriptor, property)



def test_fsmvar_is_not_abstract():
    assert not inspect.isabstract(FSMVar)


def test_fsmvar_constructor_exists():
    assert callable(FSMVar.__init__)


def test_fsmvar_constructor_args():
    sig = inspect.signature(FSMVar.__init__)
    params = list(sig.parameters.keys())



def test_analysis_scheduling_fsmoperation_is_not_abstract():
    assert not inspect.isabstract(analysis_scheduling_FSMOperation)


def test_analysis_scheduling_fsmoperation_constructor_exists():
    assert callable(analysis_scheduling_FSMOperation.__init__)


def test_analysis_scheduling_fsmoperation_constructor_args():
    sig = inspect.signature(analysis_scheduling_FSMOperation.__init__)
    params = list(sig.parameters.keys())
    assert "var" in params, "Missing parameter 'var'"
    assert "op" in params, "Missing parameter 'op'"
    assert "val" in params, "Missing parameter 'val'"

def test_analysis_scheduling_fsmoperation_has_var():
    assert hasattr(analysis_scheduling_FSMOperation, "var")
    descriptor = None
    for klass in analysis_scheduling_FSMOperation.__mro__:
        if "var" in klass.__dict__:
            descriptor = klass.__dict__["var"]
            break
    assert isinstance(descriptor, property)

def test_analysis_scheduling_fsmoperation_has_op():
    assert hasattr(analysis_scheduling_FSMOperation, "op")
    descriptor = None
    for klass in analysis_scheduling_FSMOperation.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)

def test_analysis_scheduling_fsmoperation_has_val():
    assert hasattr(analysis_scheduling_FSMOperation, "val")
    descriptor = None
    for klass in analysis_scheduling_FSMOperation.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_fsmoperation_is_not_abstract():
    assert not inspect.isabstract(FSMOperation)


def test_fsmoperation_constructor_exists():
    assert callable(FSMOperation.__init__)


def test_fsmoperation_constructor_args():
    sig = inspect.signature(FSMOperation.__init__)
    params = list(sig.parameters.keys())



def test_analysis_scheduling_fsmvarupdate_is_not_abstract():
    assert not inspect.isabstract(analysis_scheduling_FSMVarUpdate)


def test_analysis_scheduling_fsmvarupdate_constructor_exists():
    assert callable(analysis_scheduling_FSMVarUpdate.__init__)


def test_analysis_scheduling_fsmvarupdate_constructor_args():
    sig = inspect.signature(analysis_scheduling_FSMVarUpdate.__init__)
    params = list(sig.parameters.keys())



def test_fsmtransition_is_not_abstract():
    assert not inspect.isabstract(FSMTransition)


def test_fsmtransition_constructor_exists():
    assert callable(FSMTransition.__init__)


def test_fsmtransition_constructor_args():
    sig = inspect.signature(FSMTransition.__init__)
    params = list(sig.parameters.keys())



def test_analysis_scheduling_fsmtransitionwithstate_is_not_abstract():
    assert not inspect.isabstract(analysis_scheduling_FSMTransitionWithState)


def test_analysis_scheduling_fsmtransitionwithstate_constructor_exists():
    assert callable(analysis_scheduling_FSMTransitionWithState.__init__)


def test_analysis_scheduling_fsmtransitionwithstate_constructor_args():
    sig = inspect.signature(analysis_scheduling_FSMTransitionWithState.__init__)
    params = list(sig.parameters.keys())



def test_fsmvarupdate_is_not_abstract():
    assert not inspect.isabstract(FSMVarUpdate)


def test_fsmvarupdate_constructor_exists():
    assert callable(FSMVarUpdate.__init__)


def test_fsmvarupdate_constructor_args():
    sig = inspect.signature(FSMVarUpdate.__init__)
    params = list(sig.parameters.keys())



def test_analysis_scheduling_fsmstate_is_not_abstract():
    assert not inspect.isabstract(analysis_scheduling_FSMState)


def test_analysis_scheduling_fsmstate_constructor_exists():
    assert callable(analysis_scheduling_FSMState.__init__)


def test_analysis_scheduling_fsmstate_constructor_args():
    sig = inspect.signature(analysis_scheduling_FSMState.__init__)
    params = list(sig.parameters.keys())
    assert "enumName" in params, "Missing parameter 'enumName'"

def test_analysis_scheduling_fsmstate_has_enumName():
    assert hasattr(analysis_scheduling_FSMState, "enumName")
    descriptor = None
    for klass in analysis_scheduling_FSMState.__mro__:
        if "enumName" in klass.__dict__:
            descriptor = klass.__dict__["enumName"]
            break
    assert isinstance(descriptor, property)



def test_sequence_is_not_abstract():
    assert not inspect.isabstract(Sequence)


def test_sequence_constructor_exists():
    assert callable(Sequence.__init__)


def test_sequence_constructor_args():
    sig = inspect.signature(Sequence.__init__)
    params = list(sig.parameters.keys())



def test_fsmcondition_is_not_abstract():
    assert not inspect.isabstract(FSMCondition)


def test_fsmcondition_constructor_exists():
    assert callable(FSMCondition.__init__)


def test_fsmcondition_constructor_args():
    sig = inspect.signature(FSMCondition.__init__)
    params = list(sig.parameters.keys())



def test_analysis_scheduling_fsmtransition_is_not_abstract():
    assert not inspect.isabstract(analysis_scheduling_FSMTransition)


def test_analysis_scheduling_fsmtransition_constructor_exists():
    assert callable(analysis_scheduling_FSMTransition.__init__)


def test_analysis_scheduling_fsmtransition_constructor_args():
    sig = inspect.signature(analysis_scheduling_FSMTransition.__init__)
    params = list(sig.parameters.keys())
    assert "sourceStateEnumName" in params, "Missing parameter 'sourceStateEnumName'"
    assert "targetStateEnumName" in params, "Missing parameter 'targetStateEnumName'"

def test_analysis_scheduling_fsmtransition_has_sourceStateEnumName():
    assert hasattr(analysis_scheduling_FSMTransition, "sourceStateEnumName")
    descriptor = None
    for klass in analysis_scheduling_FSMTransition.__mro__:
        if "sourceStateEnumName" in klass.__dict__:
            descriptor = klass.__dict__["sourceStateEnumName"]
            break
    assert isinstance(descriptor, property)

def test_analysis_scheduling_fsmtransition_has_targetStateEnumName():
    assert hasattr(analysis_scheduling_FSMTransition, "targetStateEnumName")
    descriptor = None
    for klass in analysis_scheduling_FSMTransition.__mro__:
        if "targetStateEnumName" in klass.__dict__:
            descriptor = klass.__dict__["targetStateEnumName"]
            break
    assert isinstance(descriptor, property)



def test_analysis_scheduling_fsmvar_is_not_abstract():
    assert not inspect.isabstract(analysis_scheduling_FSMVar)


def test_analysis_scheduling_fsmvar_constructor_exists():
    assert callable(analysis_scheduling_FSMVar.__init__)


def test_analysis_scheduling_fsmvar_constructor_args():
    sig = inspect.signature(analysis_scheduling_FSMVar.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "initialVal" in params, "Missing parameter 'initialVal'"

def test_analysis_scheduling_fsmvar_has_type():
    assert hasattr(analysis_scheduling_FSMVar, "type")
    descriptor = None
    for klass in analysis_scheduling_FSMVar.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_analysis_scheduling_fsmvar_has_name():
    assert hasattr(analysis_scheduling_FSMVar, "name")
    descriptor = None
    for klass in analysis_scheduling_FSMVar.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_analysis_scheduling_fsmvar_has_initialVal():
    assert hasattr(analysis_scheduling_FSMVar, "initialVal")
    descriptor = None
    for klass in analysis_scheduling_FSMVar.__mro__:
        if "initialVal" in klass.__dict__:
            descriptor = klass.__dict__["initialVal"]
            break
    assert isinstance(descriptor, property)



def test_actorfire_is_not_abstract():
    assert not inspect.isabstract(ActorFire)


def test_actorfire_constructor_exists():
    assert callable(ActorFire.__init__)


def test_actorfire_constructor_args():
    sig = inspect.signature(ActorFire.__init__)
    params = list(sig.parameters.keys())



def test_analysis_scheduling_partitionedactorfire_is_not_abstract():
    assert not inspect.isabstract(analysis_scheduling_PartitionedActorFire)


def test_analysis_scheduling_partitionedactorfire_constructor_exists():
    assert callable(analysis_scheduling_PartitionedActorFire.__init__)


def test_analysis_scheduling_partitionedactorfire_constructor_args():
    sig = inspect.signature(analysis_scheduling_PartitionedActorFire.__init__)
    params = list(sig.parameters.keys())



def test_analysis_scheduling_sequence_is_not_abstract():
    assert not inspect.isabstract(analysis_scheduling_Sequence)


def test_analysis_scheduling_sequence_constructor_exists():
    assert callable(analysis_scheduling_Sequence.__init__)


def test_analysis_scheduling_sequence_constructor_args():
    sig = inspect.signature(analysis_scheduling_Sequence.__init__)
    params = list(sig.parameters.keys())



def test_analysis_scheduling_actorselectionschedule_is_not_abstract():
    assert not inspect.isabstract(analysis_scheduling_ActorSelectionSchedule)


def test_analysis_scheduling_actorselectionschedule_constructor_exists():
    assert callable(analysis_scheduling_ActorSelectionSchedule.__init__)


def test_analysis_scheduling_actorselectionschedule_constructor_args():
    sig = inspect.signature(analysis_scheduling_ActorSelectionSchedule.__init__)
    params = list(sig.parameters.keys())



def test_profiling_analysis_actor_is_not_abstract():
    assert not inspect.isabstract(profiling_analysis_Actor)


def test_profiling_analysis_actor_constructor_exists():
    assert callable(profiling_analysis_Actor.__init__)


def test_profiling_analysis_actor_constructor_args():
    sig = inspect.signature(profiling_analysis_Actor.__init__)
    params = list(sig.parameters.keys())



def test_analysis_profiling_intraactorcommunicationdata_is_not_abstract():
    assert not inspect.isabstract(analysis_profiling_IntraActorCommunicationData)


def test_analysis_profiling_intraactorcommunicationdata_constructor_exists():
    assert callable(analysis_profiling_IntraActorCommunicationData.__init__)


def test_analysis_profiling_intraactorcommunicationdata_constructor_args():
    sig = inspect.signature(analysis_profiling_IntraActorCommunicationData.__init__)
    params = list(sig.parameters.keys())



def test_fsmstate_is_not_abstract():
    assert not inspect.isabstract(FSMState)


def test_fsmstate_constructor_exists():
    assert callable(FSMState.__init__)


def test_fsmstate_constructor_args():
    sig = inspect.signature(FSMState.__init__)
    params = list(sig.parameters.keys())



def test_analysis_scheduling_fsm_is_not_abstract():
    assert not inspect.isabstract(analysis_scheduling_FSM)


def test_analysis_scheduling_fsm_constructor_exists():
    assert callable(analysis_scheduling_FSM.__init__)


def test_analysis_scheduling_fsm_constructor_args():
    sig = inspect.signature(analysis_scheduling_FSM.__init__)
    params = list(sig.parameters.keys())
    assert "startState" in params, "Missing parameter 'startState'"
    assert "terminalState" in params, "Missing parameter 'terminalState'"

def test_analysis_scheduling_fsm_has_startState():
    assert hasattr(analysis_scheduling_FSM, "startState")
    descriptor = None
    for klass in analysis_scheduling_FSM.__mro__:
        if "startState" in klass.__dict__:
            descriptor = klass.__dict__["startState"]
            break
    assert isinstance(descriptor, property)

def test_analysis_scheduling_fsm_has_terminalState():
    assert hasattr(analysis_scheduling_FSM, "terminalState")
    descriptor = None
    for klass in analysis_scheduling_FSM.__mro__:
        if "terminalState" in klass.__dict__:
            descriptor = klass.__dict__["terminalState"]
            break
    assert isinstance(descriptor, property)



def test_analysis_scheduling_actorfire_is_not_abstract():
    assert not inspect.isabstract(analysis_scheduling_ActorFire)


def test_analysis_scheduling_actorfire_constructor_exists():
    assert callable(analysis_scheduling_ActorFire.__init__)


def test_analysis_scheduling_actorfire_constructor_args():
    sig = inspect.signature(analysis_scheduling_ActorFire.__init__)
    params = list(sig.parameters.keys())
    assert "partition" in params, "Missing parameter 'partition'"
    assert "Actor" in params, "Missing parameter 'Actor'"
    assert "dependencyPartitions" in params, "Missing parameter 'dependencyPartitions'"
    assert "Times" in params, "Missing parameter 'Times'"

def test_analysis_scheduling_actorfire_has_partition():
    assert hasattr(analysis_scheduling_ActorFire, "partition")
    descriptor = None
    for klass in analysis_scheduling_ActorFire.__mro__:
        if "partition" in klass.__dict__:
            descriptor = klass.__dict__["partition"]
            break
    assert isinstance(descriptor, property)

def test_analysis_scheduling_actorfire_has_Actor():
    assert hasattr(analysis_scheduling_ActorFire, "Actor")
    descriptor = None
    for klass in analysis_scheduling_ActorFire.__mro__:
        if "Actor" in klass.__dict__:
            descriptor = klass.__dict__["Actor"]
            break
    assert isinstance(descriptor, property)

def test_analysis_scheduling_actorfire_has_dependencyPartitions():
    assert hasattr(analysis_scheduling_ActorFire, "dependencyPartitions")
    descriptor = None
    for klass in analysis_scheduling_ActorFire.__mro__:
        if "dependencyPartitions" in klass.__dict__:
            descriptor = klass.__dict__["dependencyPartitions"]
            break
    assert isinstance(descriptor, property)

def test_analysis_scheduling_actorfire_has_Times():
    assert hasattr(analysis_scheduling_ActorFire, "Times")
    descriptor = None
    for klass in analysis_scheduling_ActorFire.__mro__:
        if "Times" in klass.__dict__:
            descriptor = klass.__dict__["Times"]
            break
    assert isinstance(descriptor, property)



def test_analysis_profiling_profilingstatsactordata_is_not_abstract():
    assert not inspect.isabstract(analysis_profiling_ProfilingStatsActorData)


def test_analysis_profiling_profilingstatsactordata_constructor_exists():
    assert callable(analysis_profiling_ProfilingStatsActorData.__init__)


def test_analysis_profiling_profilingstatsactordata_constructor_args():
    sig = inspect.signature(analysis_profiling_ProfilingStatsActorData.__init__)
    params = list(sig.parameters.keys())
    assert "actorName" in params, "Missing parameter 'actorName'"
    assert "schedulerWeight" in params, "Missing parameter 'schedulerWeight'"
    assert "actionsWeight" in params, "Missing parameter 'actionsWeight'"
    assert "actionsWeightPercent" in params, "Missing parameter 'actionsWeightPercent'"
    assert "schedulerWeightPercent" in params, "Missing parameter 'schedulerWeightPercent'"

def test_analysis_profiling_profilingstatsactordata_has_actorName():
    assert hasattr(analysis_profiling_ProfilingStatsActorData, "actorName")
    descriptor = None
    for klass in analysis_profiling_ProfilingStatsActorData.__mro__:
        if "actorName" in klass.__dict__:
            descriptor = klass.__dict__["actorName"]
            break
    assert isinstance(descriptor, property)

def test_analysis_profiling_profilingstatsactordata_has_schedulerWeight():
    assert hasattr(analysis_profiling_ProfilingStatsActorData, "schedulerWeight")
    descriptor = None
    for klass in analysis_profiling_ProfilingStatsActorData.__mro__:
        if "schedulerWeight" in klass.__dict__:
            descriptor = klass.__dict__["schedulerWeight"]
            break
    assert isinstance(descriptor, property)

def test_analysis_profiling_profilingstatsactordata_has_actionsWeight():
    assert hasattr(analysis_profiling_ProfilingStatsActorData, "actionsWeight")
    descriptor = None
    for klass in analysis_profiling_ProfilingStatsActorData.__mro__:
        if "actionsWeight" in klass.__dict__:
            descriptor = klass.__dict__["actionsWeight"]
            break
    assert isinstance(descriptor, property)

def test_analysis_profiling_profilingstatsactordata_has_actionsWeightPercent():
    assert hasattr(analysis_profiling_ProfilingStatsActorData, "actionsWeightPercent")
    descriptor = None
    for klass in analysis_profiling_ProfilingStatsActorData.__mro__:
        if "actionsWeightPercent" in klass.__dict__:
            descriptor = klass.__dict__["actionsWeightPercent"]
            break
    assert isinstance(descriptor, property)

def test_analysis_profiling_profilingstatsactordata_has_schedulerWeightPercent():
    assert hasattr(analysis_profiling_ProfilingStatsActorData, "schedulerWeightPercent")
    descriptor = None
    for klass in analysis_profiling_ProfilingStatsActorData.__mro__:
        if "schedulerWeightPercent" in klass.__dict__:
            descriptor = klass.__dict__["schedulerWeightPercent"]
            break
    assert isinstance(descriptor, property)



def test_profilingstatsactordata_is_not_abstract():
    assert not inspect.isabstract(ProfilingStatsActorData)


def test_profilingstatsactordata_constructor_exists():
    assert callable(ProfilingStatsActorData.__init__)


def test_profilingstatsactordata_constructor_args():
    sig = inspect.signature(ProfilingStatsActorData.__init__)
    params = list(sig.parameters.keys())



def test_analysis_profiling_profilingstatsreport_is_not_abstract():
    assert not inspect.isabstract(analysis_profiling_ProfilingStatsReport)


def test_analysis_profiling_profilingstatsreport_constructor_exists():
    assert callable(analysis_profiling_ProfilingStatsReport.__init__)


def test_analysis_profiling_profilingstatsreport_constructor_args():
    sig = inspect.signature(analysis_profiling_ProfilingStatsReport.__init__)
    params = list(sig.parameters.keys())
    assert "networkName" in params, "Missing parameter 'networkName'"

def test_analysis_profiling_profilingstatsreport_has_networkName():
    assert hasattr(analysis_profiling_ProfilingStatsReport, "networkName")
    descriptor = None
    for klass in analysis_profiling_ProfilingStatsReport.__mro__:
        if "networkName" in klass.__dict__:
            descriptor = klass.__dict__["networkName"]
            break
    assert isinstance(descriptor, property)



def test_profiling_analysis_action_is_not_abstract():
    assert not inspect.isabstract(profiling_analysis_Action)


def test_profiling_analysis_action_constructor_exists():
    assert callable(profiling_analysis_Action.__init__)


def test_profiling_analysis_action_constructor_args():
    sig = inspect.signature(profiling_analysis_Action.__init__)
    params = list(sig.parameters.keys())



def test_analysis_profiling_intraactioncommunicationdata_is_not_abstract():
    assert not inspect.isabstract(analysis_profiling_IntraActionCommunicationData)


def test_analysis_profiling_intraactioncommunicationdata_constructor_exists():
    assert callable(analysis_profiling_IntraActionCommunicationData.__init__)


def test_analysis_profiling_intraactioncommunicationdata_constructor_args():
    sig = inspect.signature(analysis_profiling_IntraActionCommunicationData.__init__)
    params = list(sig.parameters.keys())



def test_intraactioncommunicationdata_is_not_abstract():
    assert not inspect.isabstract(IntraActionCommunicationData)


def test_intraactioncommunicationdata_constructor_exists():
    assert callable(IntraActionCommunicationData.__init__)


def test_intraactioncommunicationdata_constructor_args():
    sig = inspect.signature(IntraActionCommunicationData.__init__)
    params = list(sig.parameters.keys())



def test_profiling_analysis_statisticaldata_is_not_abstract():
    assert not inspect.isabstract(profiling_analysis_StatisticalData)


def test_profiling_analysis_statisticaldata_constructor_exists():
    assert callable(profiling_analysis_StatisticalData.__init__)


def test_profiling_analysis_statisticaldata_constructor_args():
    sig = inspect.signature(profiling_analysis_StatisticalData.__init__)
    params = list(sig.parameters.keys())



def test_profiling_analysis_network_is_not_abstract():
    assert not inspect.isabstract(profiling_analysis_Network)


def test_profiling_analysis_network_constructor_exists():
    assert callable(profiling_analysis_Network.__init__)


def test_profiling_analysis_network_constructor_args():
    sig = inspect.signature(profiling_analysis_Network.__init__)
    params = list(sig.parameters.keys())



def test_intraactorcommunicationdata_is_not_abstract():
    assert not inspect.isabstract(IntraActorCommunicationData)


def test_intraactorcommunicationdata_constructor_exists():
    assert callable(IntraActorCommunicationData.__init__)


def test_intraactorcommunicationdata_constructor_args():
    sig = inspect.signature(IntraActorCommunicationData.__init__)
    params = list(sig.parameters.keys())



def test_analysis_profiling_intraactioncommunicationreport_is_not_abstract():
    assert not inspect.isabstract(analysis_profiling_IntraActionCommunicationReport)


def test_analysis_profiling_intraactioncommunicationreport_constructor_exists():
    assert callable(analysis_profiling_IntraActionCommunicationReport.__init__)


def test_analysis_profiling_intraactioncommunicationreport_constructor_args():
    sig = inspect.signature(analysis_profiling_IntraActionCommunicationReport.__init__)
    params = list(sig.parameters.keys())



def test_actortostatisticaldatamap_is_not_abstract():
    assert not inspect.isabstract(ActorToStatisticalDataMap)


def test_actortostatisticaldatamap_constructor_exists():
    assert callable(ActorToStatisticalDataMap.__init__)


def test_actortostatisticaldatamap_constructor_args():
    sig = inspect.signature(ActorToStatisticalDataMap.__init__)
    params = list(sig.parameters.keys())



def test_postprocessing_analysis_statisticaldata_is_not_abstract():
    assert not inspect.isabstract(postprocessing_analysis_StatisticalData)


def test_postprocessing_analysis_statisticaldata_constructor_exists():
    assert callable(postprocessing_analysis_StatisticalData.__init__)


def test_postprocessing_analysis_statisticaldata_constructor_args():
    sig = inspect.signature(postprocessing_analysis_StatisticalData.__init__)
    params = list(sig.parameters.keys())



def test_analysis_postprocessing_schedulercheckspartition_is_not_abstract():
    assert not inspect.isabstract(analysis_postprocessing_SchedulerChecksPartition)


def test_analysis_postprocessing_schedulercheckspartition_constructor_exists():
    assert callable(analysis_postprocessing_SchedulerChecksPartition.__init__)


def test_analysis_postprocessing_schedulercheckspartition_constructor_args():
    sig = inspect.signature(analysis_postprocessing_SchedulerChecksPartition.__init__)
    params = list(sig.parameters.keys())



def test_schedulercheckspartition_is_not_abstract():
    assert not inspect.isabstract(SchedulerChecksPartition)


def test_schedulercheckspartition_constructor_exists():
    assert callable(SchedulerChecksPartition.__init__)


def test_schedulercheckspartition_constructor_args():
    sig = inspect.signature(SchedulerChecksPartition.__init__)
    params = list(sig.parameters.keys())



def test_pipelining_analysis_actorclass_is_not_abstract():
    assert not inspect.isabstract(pipelining_analysis_ActorClass)


def test_pipelining_analysis_actorclass_constructor_exists():
    assert callable(pipelining_analysis_ActorClass.__init__)


def test_pipelining_analysis_actorclass_constructor_args():
    sig = inspect.signature(pipelining_analysis_ActorClass.__init__)
    params = list(sig.parameters.keys())



def test_actiontodoublemap_is_not_abstract():
    assert not inspect.isabstract(ActionToDoubleMap)


def test_actiontodoublemap_constructor_exists():
    assert callable(ActionToDoubleMap.__init__)


def test_actiontodoublemap_constructor_args():
    sig = inspect.signature(ActionToDoubleMap.__init__)
    params = list(sig.parameters.keys())



def test_postprocessing_analysis_actor_is_not_abstract():
    assert not inspect.isabstract(postprocessing_analysis_Actor)


def test_postprocessing_analysis_actor_constructor_exists():
    assert callable(postprocessing_analysis_Actor.__init__)


def test_postprocessing_analysis_actor_constructor_args():
    sig = inspect.signature(postprocessing_analysis_Actor.__init__)
    params = list(sig.parameters.keys())



def test_analysis_postprocessing_statisticalactorpartition_is_not_abstract():
    assert not inspect.isabstract(analysis_postprocessing_StatisticalActorPartition)


def test_analysis_postprocessing_statisticalactorpartition_constructor_exists():
    assert callable(analysis_postprocessing_StatisticalActorPartition.__init__)


def test_analysis_postprocessing_statisticalactorpartition_constructor_args():
    sig = inspect.signature(analysis_postprocessing_StatisticalActorPartition.__init__)
    params = list(sig.parameters.keys())
    assert "occupancy" in params, "Missing parameter 'occupancy'"
    assert "schedulingPolicy" in params, "Missing parameter 'schedulingPolicy'"
    assert "actors" in params, "Missing parameter 'actors'"

def test_analysis_postprocessing_statisticalactorpartition_has_occupancy():
    assert hasattr(analysis_postprocessing_StatisticalActorPartition, "occupancy")
    descriptor = None
    for klass in analysis_postprocessing_StatisticalActorPartition.__mro__:
        if "occupancy" in klass.__dict__:
            descriptor = klass.__dict__["occupancy"]
            break
    assert isinstance(descriptor, property)

def test_analysis_postprocessing_statisticalactorpartition_has_schedulingPolicy():
    assert hasattr(analysis_postprocessing_StatisticalActorPartition, "schedulingPolicy")
    descriptor = None
    for klass in analysis_postprocessing_StatisticalActorPartition.__mro__:
        if "schedulingPolicy" in klass.__dict__:
            descriptor = klass.__dict__["schedulingPolicy"]
            break
    assert isinstance(descriptor, property)

def test_analysis_postprocessing_statisticalactorpartition_has_actors():
    assert hasattr(analysis_postprocessing_StatisticalActorPartition, "actors")
    descriptor = None
    for klass in analysis_postprocessing_StatisticalActorPartition.__mro__:
        if "actors" in klass.__dict__:
            descriptor = klass.__dict__["actors"]
            break
    assert isinstance(descriptor, property)



def test_statisticalactorpartition_is_not_abstract():
    assert not inspect.isabstract(StatisticalActorPartition)


def test_statisticalactorpartition_constructor_exists():
    assert callable(StatisticalActorPartition.__init__)


def test_statisticalactorpartition_constructor_args():
    sig = inspect.signature(StatisticalActorPartition.__init__)
    params = list(sig.parameters.keys())



def test_analysis_postprocessing_postprocessingdata_is_not_abstract():
    assert not inspect.isabstract(analysis_postprocessing_PostProcessingData)


def test_analysis_postprocessing_postprocessingdata_constructor_exists():
    assert callable(analysis_postprocessing_PostProcessingData.__init__)


def test_analysis_postprocessing_postprocessingdata_constructor_args():
    sig = inspect.signature(analysis_postprocessing_PostProcessingData.__init__)
    params = list(sig.parameters.keys())



def test_postprocessingdata_is_not_abstract():
    assert not inspect.isabstract(PostProcessingData)


def test_postprocessingdata_constructor_exists():
    assert callable(PostProcessingData.__init__)


def test_postprocessingdata_constructor_args():
    sig = inspect.signature(PostProcessingData.__init__)
    params = list(sig.parameters.keys())



def test_analysis_postprocessing_actorstatisticsreport_is_not_abstract():
    assert not inspect.isabstract(analysis_postprocessing_ActorStatisticsReport)


def test_analysis_postprocessing_actorstatisticsreport_constructor_exists():
    assert callable(analysis_postprocessing_ActorStatisticsReport.__init__)


def test_analysis_postprocessing_actorstatisticsreport_constructor_args():
    sig = inspect.signature(analysis_postprocessing_ActorStatisticsReport.__init__)
    params = list(sig.parameters.keys())
    assert "averageOccupancy" in params, "Missing parameter 'averageOccupancy'"
    assert "executionTime" in params, "Missing parameter 'executionTime'"
    assert "occupancyDeviation" in params, "Missing parameter 'occupancyDeviation'"

def test_analysis_postprocessing_actorstatisticsreport_has_averageOccupancy():
    assert hasattr(analysis_postprocessing_ActorStatisticsReport, "averageOccupancy")
    descriptor = None
    for klass in analysis_postprocessing_ActorStatisticsReport.__mro__:
        if "averageOccupancy" in klass.__dict__:
            descriptor = klass.__dict__["averageOccupancy"]
            break
    assert isinstance(descriptor, property)

def test_analysis_postprocessing_actorstatisticsreport_has_executionTime():
    assert hasattr(analysis_postprocessing_ActorStatisticsReport, "executionTime")
    descriptor = None
    for klass in analysis_postprocessing_ActorStatisticsReport.__mro__:
        if "executionTime" in klass.__dict__:
            descriptor = klass.__dict__["executionTime"]
            break
    assert isinstance(descriptor, property)

def test_analysis_postprocessing_actorstatisticsreport_has_occupancyDeviation():
    assert hasattr(analysis_postprocessing_ActorStatisticsReport, "occupancyDeviation")
    descriptor = None
    for klass in analysis_postprocessing_ActorStatisticsReport.__mro__:
        if "occupancyDeviation" in klass.__dict__:
            descriptor = klass.__dict__["occupancyDeviation"]
            break
    assert isinstance(descriptor, property)



def test_analysis_postprocessing_bufferblockingreport_is_not_abstract():
    assert not inspect.isabstract(analysis_postprocessing_BufferBlockingReport)


def test_analysis_postprocessing_bufferblockingreport_constructor_exists():
    assert callable(analysis_postprocessing_BufferBlockingReport.__init__)


def test_analysis_postprocessing_bufferblockingreport_constructor_args():
    sig = inspect.signature(analysis_postprocessing_BufferBlockingReport.__init__)
    params = list(sig.parameters.keys())



def test_analysis_postprocessing_actionstatisticsreport_is_not_abstract():
    assert not inspect.isabstract(analysis_postprocessing_ActionStatisticsReport)


def test_analysis_postprocessing_actionstatisticsreport_constructor_exists():
    assert callable(analysis_postprocessing_ActionStatisticsReport.__init__)


def test_analysis_postprocessing_actionstatisticsreport_constructor_args():
    sig = inspect.signature(analysis_postprocessing_ActionStatisticsReport.__init__)
    params = list(sig.parameters.keys())



def test_analysis_postprocessing_schedulerchecksreport_is_not_abstract():
    assert not inspect.isabstract(analysis_postprocessing_SchedulerChecksReport)


def test_analysis_postprocessing_schedulerchecksreport_constructor_exists():
    assert callable(analysis_postprocessing_SchedulerChecksReport.__init__)


def test_analysis_postprocessing_schedulerchecksreport_constructor_args():
    sig = inspect.signature(analysis_postprocessing_SchedulerChecksReport.__init__)
    params = list(sig.parameters.keys())



def test_postprocessing_analysis_network_is_not_abstract():
    assert not inspect.isabstract(postprocessing_analysis_Network)


def test_postprocessing_analysis_network_constructor_exists():
    assert callable(postprocessing_analysis_Network.__init__)


def test_postprocessing_analysis_network_constructor_args():
    sig = inspect.signature(postprocessing_analysis_Network.__init__)
    params = list(sig.parameters.keys())



def test_analysis_postprocessing_postprocessingreport_is_not_abstract():
    assert not inspect.isabstract(analysis_postprocessing_PostProcessingReport)


def test_analysis_postprocessing_postprocessingreport_constructor_exists():
    assert callable(analysis_postprocessing_PostProcessingReport.__init__)


def test_analysis_postprocessing_postprocessingreport_constructor_args():
    sig = inspect.signature(analysis_postprocessing_PostProcessingReport.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"
    assert "deadlock" in params, "Missing parameter 'deadlock'"

def test_analysis_postprocessing_postprocessingreport_has_time():
    assert hasattr(analysis_postprocessing_PostProcessingReport, "time")
    descriptor = None
    for klass in analysis_postprocessing_PostProcessingReport.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_analysis_postprocessing_postprocessingreport_has_deadlock():
    assert hasattr(analysis_postprocessing_PostProcessingReport, "deadlock")
    descriptor = None
    for klass in analysis_postprocessing_PostProcessingReport.__mro__:
        if "deadlock" in klass.__dict__:
            descriptor = klass.__dict__["deadlock"]
            break
    assert isinstance(descriptor, property)

def test_fsmop_exists():
    # Check that the Enumeration exists
    assert FSMOp is not None

def test_fsmop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FSMOp]
    expected_literals = [
        "ADD",
        "SET",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FSMOp"

def test_fsmcombinator_exists():
    # Check that the Enumeration exists
    assert FSMCombinator is not None

def test_fsmcombinator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FSMCombinator]
    expected_literals = [
        "NOR",
        "OR",
        "NOT",
        "AND",
        "NAND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FSMCombinator"

def test_optimizer_exists():
    # Check that the Enumeration exists
    assert Optimizer is not None

def test_optimizer_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Optimizer]
    expected_literals = [
        "RLE",
        "KTAIL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Optimizer"

def test_fsmcomparator_exists():
    # Check that the Enumeration exists
    assert FSMComparator is not None

def test_fsmcomparator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FSMComparator]
    expected_literals = [
        "SMALLER",
        "EQ",
        "GREQ",
        "SMEQ",
        "GREATER",
        "NEQ",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FSMComparator"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
analysis_pipelining_ImpactAnalysisData_strategy = st.builds(
    analysis_pipelining_ImpactAnalysisData,
    cpReduction=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ActionsVariablePipeliningReport_strategy = st.builds(
    ActionsVariablePipeliningReport,
)
pipelining_analysis_StatisticalData_strategy = st.builds(
    pipelining_analysis_StatisticalData,
)
pipelining_analysis_Action_strategy = st.builds(
    pipelining_analysis_Action,
)
analysis_pipelining_ActionVariablePipeliningData_strategy = st.builds(
    analysis_pipelining_ActionVariablePipeliningData,
    pipelinable=
        st.booleans()
)
ActionVariablePipeliningData_strategy = st.builds(
    ActionVariablePipeliningData,
)
pipelining_analysis_Network_strategy = st.builds(
    pipelining_analysis_Network,
)
BalancedPipelinePartition_strategy = st.builds(
    BalancedPipelinePartition,
)
partitioning_analysis_Actor_strategy = st.builds(
    partitioning_analysis_Actor,
)
analysis_partitioning_ComCostPartition_strategy = st.builds(
    analysis_partitioning_ComCostPartition,
    internalCost=
        safe_text,
    externalCost=
        safe_text
)
analysis_partitioning_BalancedPipelinePartition_strategy = st.builds(
    analysis_partitioning_BalancedPipelinePartition,
    workload=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    commonPredAvg=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    preWorkload=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
WorkloadBalancePartition_strategy = st.builds(
    WorkloadBalancePartition,
)
analysis_partitioning_WorkloadBalancePartition_strategy = st.builds(
    analysis_partitioning_WorkloadBalancePartition,
    workload=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ScheduledImpactAnalysisData_strategy = st.builds(
    ScheduledImpactAnalysisData,
)
ComCostPartition_strategy = st.builds(
    ComCostPartition,
)
partitioning_analysis_Network_strategy = st.builds(
    partitioning_analysis_Network,
)
analysis_buffers_OptimalBufferData_strategy = st.builds(
    analysis_buffers_OptimalBufferData,
)
BoundedBuffersReport_strategy = st.builds(
    BoundedBuffersReport,
)
OptimalBufferData_strategy = st.builds(
    OptimalBufferData,
)
buffers_analysis_Buffer_strategy = st.builds(
    buffers_analysis_Buffer,
)
analysis_buffers_BoundedBufferData_strategy = st.builds(
    analysis_buffers_BoundedBufferData,
    bitSize=
        st.integers(),
    tokenSize=
        st.integers()
)
BoundedBufferData_strategy = st.builds(
    BoundedBufferData,
)
buffers_analysis_Network_strategy = st.builds(
    buffers_analysis_Network,
)
BottlenecksWithSchedulingReport_strategy = st.builds(
    BottlenecksWithSchedulingReport,
)
analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap_strategy = st.builds(
    analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap,
    key=
        safe_text
)
DoubleToBottlenecksWithSchedulingReportMap_strategy = st.builds(
    DoubleToBottlenecksWithSchedulingReportMap,
)
analysis_bottlenecks_ScheduledImpactAnalysisData_strategy = st.builds(
    analysis_bottlenecks_ScheduledImpactAnalysisData,
)
BufferToDoubleMap_strategy = st.builds(
    BufferToDoubleMap,
)
BufferToIntegerMap_strategy = st.builds(
    BufferToIntegerMap,
)
analysis_bottlenecks_ActionBottlenecksWithSchedulingData_strategy = st.builds(
    analysis_bottlenecks_ActionBottlenecksWithSchedulingData,
    totalWeight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    cpFirings=
        safe_text,
    cpWeight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    totalFirings=
        safe_text
)
StringToDoubleMap_strategy = st.builds(
    StringToDoubleMap,
)
ActionBottlenecksWithSchedulingData_strategy = st.builds(
    ActionBottlenecksWithSchedulingData,
)
postprocessing_PostProcessingData_strategy = st.builds(
    postprocessing_PostProcessingData,
)
analysis_bottlenecks_DoubleToBottlenecksReportMap_strategy = st.builds(
    analysis_bottlenecks_DoubleToBottlenecksReportMap,
    key=
        safe_text
)
DoubleToBottlenecksReportMap_strategy = st.builds(
    DoubleToBottlenecksReportMap,
)
DoubleToDoubleMap_strategy = st.builds(
    DoubleToDoubleMap,
)
bottlenecks_analysis_ActorClass_strategy = st.builds(
    bottlenecks_analysis_ActorClass,
)
analysis_bottlenecks_ImpactAnalysisData_strategy = st.builds(
    analysis_bottlenecks_ImpactAnalysisData,
)
BottlenecksReport_strategy = st.builds(
    BottlenecksReport,
)
ImpactAnalysisData_strategy = st.builds(
    ImpactAnalysisData,
)
analysis_bottlenecks_ActionBottlenecksData_strategy = st.builds(
    analysis_bottlenecks_ActionBottlenecksData,
    totalVariance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    totalFirings=
        safe_text,
    totalWeight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    slackMin=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    cpVariance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    cpWeight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    cpFirings=
        safe_text,
    slackMax=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ActionBottlenecksData_strategy = st.builds(
    ActionBottlenecksData,
)
bottlenecks_analysis_Network_strategy = st.builds(
    bottlenecks_analysis_Network,
)
analysis_trace_MarkovModelActionData_strategy = st.builds(
    analysis_trace_MarkovModelActionData,
    successors=
        safe_text,
    first=
        st.booleans()
)
MarkovModelActionData_strategy = st.builds(
    MarkovModelActionData,
)
analysis_trace_ComparedAction_strategy = st.builds(
    analysis_trace_ComparedAction,
    found=
        st.booleans(),
    dIncomings=
        safe_text,
    dOutgoings=
        safe_text,
    dSteps=
        safe_text
)
ComparedAction_strategy = st.builds(
    ComparedAction,
)
bottlenecks_analysis_Action_strategy = st.builds(
    bottlenecks_analysis_Action,
)
analysis_trace_ComparedTrace_strategy = st.builds(
    analysis_trace_ComparedTrace,
    dDependencies=
        safe_text,
    dSteps=
        safe_text,
    equal=
        st.booleans()
)
ComparedTrace_strategy = st.builds(
    ComparedTrace,
)
CompressedTraceReport_strategy = st.builds(
    CompressedTraceReport,
)
BufferToLongMap_strategy = st.builds(
    BufferToLongMap,
)
PortToLongMap_strategy = st.builds(
    PortToLongMap,
)
VariableToLongMap_strategy = st.builds(
    VariableToLongMap,
)
GuardToLongMap_strategy = st.builds(
    GuardToLongMap,
)
analysis_trace_CompressedDependency_strategy = st.builds(
    analysis_trace_CompressedDependency,
    count=
        safe_text
)
trace_analysis_Action_strategy = st.builds(
    trace_analysis_Action,
)
analysis_trace_CompressedStep_strategy = st.builds(
    analysis_trace_CompressedStep,
    count=
        safe_text
)
CompressedDependency_strategy = st.builds(
    CompressedDependency,
)
analysis_trace_CompressedVariableDependency_strategy = st.builds(
    analysis_trace_CompressedVariableDependency,
)
analysis_trace_CompressedFsmDependency_strategy = st.builds(
    analysis_trace_CompressedFsmDependency,
)
analysis_trace_CompressedTokensDependency_strategy = st.builds(
    analysis_trace_CompressedTokensDependency,
)
analysis_trace_CompressedPortDependency_strategy = st.builds(
    analysis_trace_CompressedPortDependency,
)
analysis_trace_CompressedGuardDependency_strategy = st.builds(
    analysis_trace_CompressedGuardDependency,
)
CompressedStep_strategy = st.builds(
    CompressedStep,
)
trace_analysis_Network_strategy = st.builds(
    trace_analysis_Network,
)
StringToLongMap_strategy = st.builds(
    StringToLongMap,
)
analysis_map_ActionToDoubleMap_strategy = st.builds(
    analysis_map_ActionToDoubleMap,
    value=
        safe_text
)
ActorToLongMap_strategy = st.builds(
    ActorToLongMap,
)
analysis_map_StringToStringMap_strategy = st.builds(
    analysis_map_StringToStringMap,
    key=
        safe_text,
    value=
        safe_text
)
ActorSelectionSchedule_strategy = st.builds(
    ActorSelectionSchedule,
)
analysis_map_PartitionToActorSelectionScheduleMap_strategy = st.builds(
    analysis_map_PartitionToActorSelectionScheduleMap,
    key=
        safe_text
)
analysis_map_BufferToDoubleMap_strategy = st.builds(
    analysis_map_BufferToDoubleMap,
    value=
        safe_text
)
analysis_map_BufferToIntegerMap_strategy = st.builds(
    analysis_map_BufferToIntegerMap,
    value=
        safe_text
)
map_analysis_Procedure_strategy = st.builds(
    map_analysis_Procedure,
)
analysis_map_StringToDoubleMap_strategy = st.builds(
    analysis_map_StringToDoubleMap,
    key=
        safe_text,
    value=
        safe_text
)
map_analysis_Port_strategy = st.builds(
    map_analysis_Port,
)
analysis_map_PortToLongMap_strategy = st.builds(
    analysis_map_PortToLongMap,
    value=
        safe_text
)
map_analysis_Guard_strategy = st.builds(
    map_analysis_Guard,
)
analysis_map_GuardToLongMap_strategy = st.builds(
    analysis_map_GuardToLongMap,
    value=
        safe_text
)
analysis_map_VariableToLongMap_strategy = st.builds(
    analysis_map_VariableToLongMap,
    value=
        safe_text
)
analysis_map_DoubleToDoubleMap_strategy = st.builds(
    analysis_map_DoubleToDoubleMap,
    key=
        safe_text,
    value=
        safe_text
)
analysis_map_StringToLongMap_strategy = st.builds(
    analysis_map_StringToLongMap,
    key=
        safe_text,
    value=
        safe_text
)
analysis_map_BufferToLongMap_strategy = st.builds(
    analysis_map_BufferToLongMap,
    value=
        safe_text
)
analysis_map_ActorToLongMap_strategy = st.builds(
    analysis_map_ActorToLongMap,
    value=
        safe_text
)
analysis_map_ActionToLongMap_strategy = st.builds(
    analysis_map_ActionToLongMap,
    value=
        safe_text
)
analysis_map_EOperatorToStatisticalDataMap_strategy = st.builds(
    analysis_map_EOperatorToStatisticalDataMap,
    key=
        safe_text
)
map_analysis_ActorClass_strategy = st.builds(
    map_analysis_ActorClass,
)
analysis_map_ActorClassToStatisticalDataMap_strategy = st.builds(
    analysis_map_ActorClassToStatisticalDataMap,
)
map_analysis_Variable_strategy = st.builds(
    map_analysis_Variable,
)
analysis_map_VariableToStatisticalDataMap_strategy = st.builds(
    analysis_map_VariableToStatisticalDataMap,
)
analysis_map_ProcedureToStatisticalDataMap_strategy = st.builds(
    analysis_map_ProcedureToStatisticalDataMap,
)
map_analysis_Buffer_strategy = st.builds(
    map_analysis_Buffer,
)
analysis_map_BufferToStatisticalDataMap_strategy = st.builds(
    analysis_map_BufferToStatisticalDataMap,
)
map_analysis_Action_strategy = st.builds(
    map_analysis_Action,
)
analysis_map_ActionToStatisticalDataMap_strategy = st.builds(
    analysis_map_ActionToStatisticalDataMap,
)
map_analysis_StatisticalData_strategy = st.builds(
    map_analysis_StatisticalData,
)
map_analysis_Actor_strategy = st.builds(
    map_analysis_Actor,
)
analysis_map_ActorToStatisticalDataMap_strategy = st.builds(
    analysis_map_ActorToStatisticalDataMap,
)
analysis_map_StringToIntegerMap_strategy = st.builds(
    analysis_map_StringToIntegerMap,
    key=
        safe_text,
    value=
        safe_text
)
StringToStringMap_strategy = st.builds(
    StringToStringMap,
)
analysis_profiler_TableRow_strategy = st.builds(
    analysis_profiler_TableRow,
)
TableRow_strategy = st.builds(
    TableRow,
)
AccessData_strategy = st.builds(
    AccessData,
)
analysis_profiler_StringToAccessDataMap_strategy = st.builds(
    analysis_profiler_StringToAccessDataMap,
    key=
        safe_text
)
analysis_profiler_AccessData_strategy = st.builds(
    analysis_profiler_AccessData,
    max=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    average=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    total=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    min=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    accesses=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
profiler_analysis_Procedure_strategy = st.builds(
    profiler_analysis_Procedure,
)
StringToAccessDataMap_strategy = st.builds(
    StringToAccessDataMap,
)
analysis_profiler_MemoryAccessData_strategy = st.builds(
    analysis_profiler_MemoryAccessData,
)
MemoryAccessData_strategy = st.builds(
    MemoryAccessData,
)
analysis_profiler_StateVariableAccessData_strategy = st.builds(
    analysis_profiler_StateVariableAccessData,
    name=
        safe_text
)
analysis_profiler_LocalVariableAccessData_strategy = st.builds(
    analysis_profiler_LocalVariableAccessData,
    name=
        safe_text
)
analysis_profiler_SharedVariableAccessData_strategy = st.builds(
    analysis_profiler_SharedVariableAccessData,
    name=
        safe_text
)
analysis_profiler_BufferAccessData_strategy = st.builds(
    analysis_profiler_BufferAccessData,
    targetActor=
        safe_text,
    targetPort=
        safe_text,
    sourceActor=
        safe_text,
    sourcePort=
        safe_text
)
analysis_profiler_ActionMemoryProfilingData_strategy = st.builds(
    analysis_profiler_ActionMemoryProfilingData,
    actor=
        safe_text,
    action=
        safe_text
)
ActionMemoryProfilingData_strategy = st.builds(
    ActionMemoryProfilingData,
)
ActionDynamicData_strategy = st.builds(
    ActionDynamicData,
)
analysis_profiler_ProcedureToComplexDynamicDataMap_strategy = st.builds(
    analysis_profiler_ProcedureToComplexDynamicDataMap,
)
BufferToStatisticalDataMap_strategy = st.builds(
    BufferToStatisticalDataMap,
)
ProcedureToComplexDynamicDataMap_strategy = st.builds(
    ProcedureToComplexDynamicDataMap,
)
VariableToStatisticalDataMap_strategy = st.builds(
    VariableToStatisticalDataMap,
)
ProcedureToStatisticalDataMap_strategy = st.builds(
    ProcedureToStatisticalDataMap,
)
EOperatorToStatisticalDataMap_strategy = st.builds(
    EOperatorToStatisticalDataMap,
)
analysis_profiler_ComplexDynamicData_strategy = st.builds(
    analysis_profiler_ComplexDynamicData,
)
ActionToLongMap_strategy = st.builds(
    ActionToLongMap,
)
ActionToStatisticalDataMap_strategy = st.builds(
    ActionToStatisticalDataMap,
)
profiler_analysis_StatisticalData_strategy = st.builds(
    profiler_analysis_StatisticalData,
)
profiler_analysis_Buffer_strategy = st.builds(
    profiler_analysis_Buffer,
)
analysis_profiler_BufferDynamicData_strategy = st.builds(
    analysis_profiler_BufferDynamicData,
    unconsumedTokens=
        st.integers()
)
profiler_analysis_Action_strategy = st.builds(
    profiler_analysis_Action,
)
profiler_analysis_Actor_strategy = st.builds(
    profiler_analysis_Actor,
)
ComplexDynamicData_strategy = st.builds(
    ComplexDynamicData,
)
analysis_profiler_ActionDynamicData_strategy = st.builds(
    analysis_profiler_ActionDynamicData,
)
analysis_profiler_ActorDynamicData_strategy = st.builds(
    analysis_profiler_ActorDynamicData,
)
BufferDynamicData_strategy = st.builds(
    BufferDynamicData,
)
ActorDynamicData_strategy = st.builds(
    ActorDynamicData,
)
CodeData_strategy = st.builds(
    CodeData,
)
analysis_profiler_ComplexCodeData_strategy = st.builds(
    analysis_profiler_ComplexCodeData,
)
StringToIntegerMap_strategy = st.builds(
    StringToIntegerMap,
)
analysis_profiler_CodeData_strategy = st.builds(
    analysis_profiler_CodeData,
    blockName=
        safe_text,
    nol=
        safe_text
)
ComplexCodeData_strategy = st.builds(
    ComplexCodeData,
)
profiler_analysis_Network_strategy = st.builds(
    profiler_analysis_Network,
)
AnalysisReport_strategy = st.builds(
    AnalysisReport,
)
analysis_profiler_MemoryProfilingReport_strategy = st.builds(
    analysis_profiler_MemoryProfilingReport,
    networkName=
        safe_text
)
analysis_partitioning_ComCostPartitioningReport_strategy = st.builds(
    analysis_partitioning_ComCostPartitioningReport,
    bitAccurate=
        st.booleans()
)
analysis_trace_TraceSizeReport_strategy = st.builds(
    analysis_trace_TraceSizeReport,
    firings=
        safe_text,
    dependencies=
        safe_text
)
analysis_bottlenecks_ScheduledImpactAnalysisReport_strategy = st.builds(
    analysis_bottlenecks_ScheduledImpactAnalysisReport,
    classLevel=
        st.booleans()
)
analysis_pipelining_ImpactAnalysisReport_strategy = st.builds(
    analysis_pipelining_ImpactAnalysisReport,
)
analysis_buffers_OptimalBuffersReport_strategy = st.builds(
    analysis_buffers_OptimalBuffersReport,
    bitAccurate=
        st.booleans(),
    pow2=
        st.booleans()
)
analysis_profiler_BenchmarkReport_strategy = st.builds(
    analysis_profiler_BenchmarkReport,
    column_names=
        safe_text
)
analysis_profiler_DynamicProfilingReport_strategy = st.builds(
    analysis_profiler_DynamicProfilingReport,
)
analysis_trace_TraceComparatorReport_strategy = st.builds(
    analysis_trace_TraceComparatorReport,
)
analysis_bottlenecks_BottlenecksWithSchedulingReport_strategy = st.builds(
    analysis_bottlenecks_BottlenecksWithSchedulingReport,
    totalFirings=
        safe_text,
    cpFirings=
        safe_text,
    cpWeight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    cpBlockingTime=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    executionTime=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    totalWeight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
analysis_trace_CompressedTraceReport_strategy = st.builds(
    analysis_trace_CompressedTraceReport,
    traceFile=
        safe_text
)
analysis_pipelining_ActionsVariablePipeliningReport_strategy = st.builds(
    analysis_pipelining_ActionsVariablePipeliningReport,
)
analysis_buffers_BoundedBuffersReport_strategy = st.builds(
    analysis_buffers_BoundedBuffersReport,
    bitSize=
        st.integers(),
    tokenSize=
        st.integers(),
    bitAccurate=
        st.booleans(),
    pow2=
        st.booleans()
)
analysis_partitioning_WorkloadBalancePartitioningReport_strategy = st.builds(
    analysis_partitioning_WorkloadBalancePartitioningReport,
)
analysis_bottlenecks_BottlenecksReport_strategy = st.builds(
    analysis_bottlenecks_BottlenecksReport,
    cpWeight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    cpFirings=
        safe_text,
    totalVariance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    totalFirings=
        safe_text,
    totalWeight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    cpVariance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
analysis_trace_MarkowModelTraceReport_strategy = st.builds(
    analysis_trace_MarkowModelTraceReport,
)
analysis_bottlenecks_ImpactAnalysisReport_strategy = st.builds(
    analysis_bottlenecks_ImpactAnalysisReport,
    classLevel=
        st.booleans()
)
analysis_partitioning_BalancedPipelinePartitioningReport_strategy = st.builds(
    analysis_partitioning_BalancedPipelinePartitioningReport,
)
analysis_profiler_CodeProfilingReport_strategy = st.builds(
    analysis_profiler_CodeProfilingReport,
)
analysis_AnalysisReport_strategy = st.builds(
    analysis_AnalysisReport,
    date=
        st.dates(),
    algorithm=
        safe_text
)
analysis_scheduling_MarkovSchedulingTransition_strategy = st.builds(
    analysis_scheduling_MarkovSchedulingTransition,
    firings=
        safe_text,
    name=
        safe_text
)
analysis_caseoptimal_CaseOptimalActorSelectionSchedule_strategy = st.builds(
    analysis_caseoptimal_CaseOptimalActorSelectionSchedule,
)
PartitionToActorSelectionScheduleMap_strategy = st.builds(
    PartitionToActorSelectionScheduleMap,
)
analysis_caseoptimal_CaseOptimalScheduleReport_strategy = st.builds(
    analysis_caseoptimal_CaseOptimalScheduleReport,
    partitionFilePath=
        safe_text,
    traceFile=
        safe_text,
    pipeline=
        safe_text
)
analysis_scheduling_MarkovSchedulingState_strategy = st.builds(
    analysis_scheduling_MarkovSchedulingState,
    name=
        safe_text,
    firings=
        safe_text
)
MarkovSchedulingTransition_strategy = st.builds(
    MarkovSchedulingTransition,
)
MarkovSchedulingState_strategy = st.builds(
    MarkovSchedulingState,
)
scheduling_analysis_Actor_strategy = st.builds(
    scheduling_analysis_Actor,
)
analysis_scheduling_MarkovPartitionScheduler_strategy = st.builds(
    analysis_scheduling_MarkovPartitionScheduler,
    partitionId=
        safe_text
)
scheduling_analysis_Network_strategy = st.builds(
    scheduling_analysis_Network,
)
MarkovPartitionScheduler_strategy = st.builds(
    MarkovPartitionScheduler,
)
analysis_scheduling_MarkovSimpleSchedulerReport_strategy = st.builds(
    analysis_scheduling_MarkovSimpleSchedulerReport,
)
FSMCombination_strategy = st.builds(
    FSMCombination,
)
analysis_scheduling_FSMCondition_strategy = st.builds(
    analysis_scheduling_FSMCondition,
    valName=
        safe_text,
    compval=
        safe_text,
    comp=
        safe_text
)
analysis_scheduling_FSMCombination_strategy = st.builds(
    analysis_scheduling_FSMCombination,
    combinator=
        safe_text
)
FSMVar_strategy = st.builds(
    FSMVar,
)
analysis_scheduling_FSMOperation_strategy = st.builds(
    analysis_scheduling_FSMOperation,
    var=
        safe_text,
    op=
        safe_text,
    val=
        safe_text
)
FSMOperation_strategy = st.builds(
    FSMOperation,
)
analysis_scheduling_FSMVarUpdate_strategy = st.builds(
    analysis_scheduling_FSMVarUpdate,
)
FSMTransition_strategy = st.builds(
    FSMTransition,
)
analysis_scheduling_FSMTransitionWithState_strategy = st.builds(
    analysis_scheduling_FSMTransitionWithState,
)
FSMVarUpdate_strategy = st.builds(
    FSMVarUpdate,
)
analysis_scheduling_FSMState_strategy = st.builds(
    analysis_scheduling_FSMState,
    enumName=
        safe_text
)
Sequence_strategy = st.builds(
    Sequence,
)
FSMCondition_strategy = st.builds(
    FSMCondition,
)
analysis_scheduling_FSMTransition_strategy = st.builds(
    analysis_scheduling_FSMTransition,
    sourceStateEnumName=
        safe_text,
    targetStateEnumName=
        safe_text
)
analysis_scheduling_FSMVar_strategy = st.builds(
    analysis_scheduling_FSMVar,
    type=
        safe_text,
    name=
        safe_text,
    initialVal=
        safe_text
)
ActorFire_strategy = st.builds(
    ActorFire,
)
analysis_scheduling_PartitionedActorFire_strategy = st.builds(
    analysis_scheduling_PartitionedActorFire,
)
analysis_scheduling_Sequence_strategy = st.builds(
    analysis_scheduling_Sequence,
)
analysis_scheduling_ActorSelectionSchedule_strategy = st.builds(
    analysis_scheduling_ActorSelectionSchedule,
)
profiling_analysis_Actor_strategy = st.builds(
    profiling_analysis_Actor,
)
analysis_profiling_IntraActorCommunicationData_strategy = st.builds(
    analysis_profiling_IntraActorCommunicationData,
)
FSMState_strategy = st.builds(
    FSMState,
)
analysis_scheduling_FSM_strategy = st.builds(
    analysis_scheduling_FSM,
    startState=
        safe_text,
    terminalState=
        safe_text
)
analysis_scheduling_ActorFire_strategy = st.builds(
    analysis_scheduling_ActorFire,
    partition=
        safe_text,
    Actor=
        safe_text,
    dependencyPartitions=
        safe_text,
    Times=
        st.integers()
)
analysis_profiling_ProfilingStatsActorData_strategy = st.builds(
    analysis_profiling_ProfilingStatsActorData,
    actorName=
        safe_text,
    schedulerWeight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    actionsWeight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    actionsWeightPercent=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    schedulerWeightPercent=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ProfilingStatsActorData_strategy = st.builds(
    ProfilingStatsActorData,
)
analysis_profiling_ProfilingStatsReport_strategy = st.builds(
    analysis_profiling_ProfilingStatsReport,
    networkName=
        safe_text
)
profiling_analysis_Action_strategy = st.builds(
    profiling_analysis_Action,
)
analysis_profiling_IntraActionCommunicationData_strategy = st.builds(
    analysis_profiling_IntraActionCommunicationData,
)
IntraActionCommunicationData_strategy = st.builds(
    IntraActionCommunicationData,
)
profiling_analysis_StatisticalData_strategy = st.builds(
    profiling_analysis_StatisticalData,
)
profiling_analysis_Network_strategy = st.builds(
    profiling_analysis_Network,
)
IntraActorCommunicationData_strategy = st.builds(
    IntraActorCommunicationData,
)
analysis_profiling_IntraActionCommunicationReport_strategy = st.builds(
    analysis_profiling_IntraActionCommunicationReport,
)
ActorToStatisticalDataMap_strategy = st.builds(
    ActorToStatisticalDataMap,
)
postprocessing_analysis_StatisticalData_strategy = st.builds(
    postprocessing_analysis_StatisticalData,
)
analysis_postprocessing_SchedulerChecksPartition_strategy = st.builds(
    analysis_postprocessing_SchedulerChecksPartition,
)
SchedulerChecksPartition_strategy = st.builds(
    SchedulerChecksPartition,
)
pipelining_analysis_ActorClass_strategy = st.builds(
    pipelining_analysis_ActorClass,
)
ActionToDoubleMap_strategy = st.builds(
    ActionToDoubleMap,
)
postprocessing_analysis_Actor_strategy = st.builds(
    postprocessing_analysis_Actor,
)
analysis_postprocessing_StatisticalActorPartition_strategy = st.builds(
    analysis_postprocessing_StatisticalActorPartition,
    occupancy=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    schedulingPolicy=
        safe_text,
    actors=
        safe_text
)
StatisticalActorPartition_strategy = st.builds(
    StatisticalActorPartition,
)
analysis_postprocessing_PostProcessingData_strategy = st.builds(
    analysis_postprocessing_PostProcessingData,
)
PostProcessingData_strategy = st.builds(
    PostProcessingData,
)
analysis_postprocessing_ActorStatisticsReport_strategy = st.builds(
    analysis_postprocessing_ActorStatisticsReport,
    averageOccupancy=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    executionTime=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    occupancyDeviation=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
analysis_postprocessing_BufferBlockingReport_strategy = st.builds(
    analysis_postprocessing_BufferBlockingReport,
)
analysis_postprocessing_ActionStatisticsReport_strategy = st.builds(
    analysis_postprocessing_ActionStatisticsReport,
)
analysis_postprocessing_SchedulerChecksReport_strategy = st.builds(
    analysis_postprocessing_SchedulerChecksReport,
)
postprocessing_analysis_Network_strategy = st.builds(
    postprocessing_analysis_Network,
)
analysis_postprocessing_PostProcessingReport_strategy = st.builds(
    analysis_postprocessing_PostProcessingReport,
    time=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    deadlock=
        st.booleans()
)

@given(instance=analysis_pipelining_ImpactAnalysisData_strategy)
@settings(max_examples=50)
def test_analysis_pipelining_impactanalysisdata_instantiation(instance):
    assert isinstance(instance, analysis_pipelining_ImpactAnalysisData)



@given(instance=analysis_pipelining_ImpactAnalysisData_strategy)
def test_analysis_pipelining_impactanalysisdata_cpReduction_setter(instance):
    original = instance.cpReduction
    instance.cpReduction = original
    assert instance.cpReduction == original

@given(instance=ActionsVariablePipeliningReport_strategy)
@settings(max_examples=50)
def test_actionsvariablepipeliningreport_instantiation(instance):
    assert isinstance(instance, ActionsVariablePipeliningReport)

@given(instance=pipelining_analysis_StatisticalData_strategy)
@settings(max_examples=50)
def test_pipelining_analysis_statisticaldata_instantiation(instance):
    assert isinstance(instance, pipelining_analysis_StatisticalData)

@given(instance=pipelining_analysis_Action_strategy)
@settings(max_examples=50)
def test_pipelining_analysis_action_instantiation(instance):
    assert isinstance(instance, pipelining_analysis_Action)

@given(instance=analysis_pipelining_ActionVariablePipeliningData_strategy)
@settings(max_examples=50)
def test_analysis_pipelining_actionvariablepipeliningdata_instantiation(instance):
    assert isinstance(instance, analysis_pipelining_ActionVariablePipeliningData)



@given(instance=analysis_pipelining_ActionVariablePipeliningData_strategy)
def test_analysis_pipelining_actionvariablepipeliningdata_pipelinable_setter(instance):
    original = instance.pipelinable
    instance.pipelinable = original
    assert instance.pipelinable == original

@given(instance=ActionVariablePipeliningData_strategy)
@settings(max_examples=50)
def test_actionvariablepipeliningdata_instantiation(instance):
    assert isinstance(instance, ActionVariablePipeliningData)

@given(instance=pipelining_analysis_Network_strategy)
@settings(max_examples=50)
def test_pipelining_analysis_network_instantiation(instance):
    assert isinstance(instance, pipelining_analysis_Network)

@given(instance=BalancedPipelinePartition_strategy)
@settings(max_examples=50)
def test_balancedpipelinepartition_instantiation(instance):
    assert isinstance(instance, BalancedPipelinePartition)

@given(instance=partitioning_analysis_Actor_strategy)
@settings(max_examples=50)
def test_partitioning_analysis_actor_instantiation(instance):
    assert isinstance(instance, partitioning_analysis_Actor)

@given(instance=analysis_partitioning_ComCostPartition_strategy)
@settings(max_examples=50)
def test_analysis_partitioning_comcostpartition_instantiation(instance):
    assert isinstance(instance, analysis_partitioning_ComCostPartition)



@given(instance=analysis_partitioning_ComCostPartition_strategy)
def test_analysis_partitioning_comcostpartition_internalCost_setter(instance):
    original = instance.internalCost
    instance.internalCost = original
    assert instance.internalCost == original



@given(instance=analysis_partitioning_ComCostPartition_strategy)
def test_analysis_partitioning_comcostpartition_externalCost_setter(instance):
    original = instance.externalCost
    instance.externalCost = original
    assert instance.externalCost == original

@given(instance=analysis_partitioning_BalancedPipelinePartition_strategy)
@settings(max_examples=50)
def test_analysis_partitioning_balancedpipelinepartition_instantiation(instance):
    assert isinstance(instance, analysis_partitioning_BalancedPipelinePartition)



@given(instance=analysis_partitioning_BalancedPipelinePartition_strategy)
def test_analysis_partitioning_balancedpipelinepartition_workload_setter(instance):
    original = instance.workload
    instance.workload = original
    assert instance.workload == original



@given(instance=analysis_partitioning_BalancedPipelinePartition_strategy)
def test_analysis_partitioning_balancedpipelinepartition_commonPredAvg_setter(instance):
    original = instance.commonPredAvg
    instance.commonPredAvg = original
    assert instance.commonPredAvg == original



@given(instance=analysis_partitioning_BalancedPipelinePartition_strategy)
def test_analysis_partitioning_balancedpipelinepartition_preWorkload_setter(instance):
    original = instance.preWorkload
    instance.preWorkload = original
    assert instance.preWorkload == original

@given(instance=WorkloadBalancePartition_strategy)
@settings(max_examples=50)
def test_workloadbalancepartition_instantiation(instance):
    assert isinstance(instance, WorkloadBalancePartition)

@given(instance=analysis_partitioning_WorkloadBalancePartition_strategy)
@settings(max_examples=50)
def test_analysis_partitioning_workloadbalancepartition_instantiation(instance):
    assert isinstance(instance, analysis_partitioning_WorkloadBalancePartition)



@given(instance=analysis_partitioning_WorkloadBalancePartition_strategy)
def test_analysis_partitioning_workloadbalancepartition_workload_setter(instance):
    original = instance.workload
    instance.workload = original
    assert instance.workload == original

@given(instance=ScheduledImpactAnalysisData_strategy)
@settings(max_examples=50)
def test_scheduledimpactanalysisdata_instantiation(instance):
    assert isinstance(instance, ScheduledImpactAnalysisData)

@given(instance=ComCostPartition_strategy)
@settings(max_examples=50)
def test_comcostpartition_instantiation(instance):
    assert isinstance(instance, ComCostPartition)

@given(instance=partitioning_analysis_Network_strategy)
@settings(max_examples=50)
def test_partitioning_analysis_network_instantiation(instance):
    assert isinstance(instance, partitioning_analysis_Network)

@given(instance=analysis_buffers_OptimalBufferData_strategy)
@settings(max_examples=50)
def test_analysis_buffers_optimalbufferdata_instantiation(instance):
    assert isinstance(instance, analysis_buffers_OptimalBufferData)

@given(instance=BoundedBuffersReport_strategy)
@settings(max_examples=50)
def test_boundedbuffersreport_instantiation(instance):
    assert isinstance(instance, BoundedBuffersReport)

@given(instance=OptimalBufferData_strategy)
@settings(max_examples=50)
def test_optimalbufferdata_instantiation(instance):
    assert isinstance(instance, OptimalBufferData)

@given(instance=buffers_analysis_Buffer_strategy)
@settings(max_examples=50)
def test_buffers_analysis_buffer_instantiation(instance):
    assert isinstance(instance, buffers_analysis_Buffer)

@given(instance=analysis_buffers_BoundedBufferData_strategy)
@settings(max_examples=50)
def test_analysis_buffers_boundedbufferdata_instantiation(instance):
    assert isinstance(instance, analysis_buffers_BoundedBufferData)



@given(instance=analysis_buffers_BoundedBufferData_strategy)
def test_analysis_buffers_boundedbufferdata_bitSize_setter(instance):
    original = instance.bitSize
    instance.bitSize = original
    assert instance.bitSize == original



@given(instance=analysis_buffers_BoundedBufferData_strategy)
def test_analysis_buffers_boundedbufferdata_tokenSize_setter(instance):
    original = instance.tokenSize
    instance.tokenSize = original
    assert instance.tokenSize == original

@given(instance=BoundedBufferData_strategy)
@settings(max_examples=50)
def test_boundedbufferdata_instantiation(instance):
    assert isinstance(instance, BoundedBufferData)

@given(instance=buffers_analysis_Network_strategy)
@settings(max_examples=50)
def test_buffers_analysis_network_instantiation(instance):
    assert isinstance(instance, buffers_analysis_Network)

@given(instance=BottlenecksWithSchedulingReport_strategy)
@settings(max_examples=50)
def test_bottleneckswithschedulingreport_instantiation(instance):
    assert isinstance(instance, BottlenecksWithSchedulingReport)

@given(instance=analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap_strategy)
@settings(max_examples=50)
def test_analysis_bottlenecks_doubletobottleneckswithschedulingreportmap_instantiation(instance):
    assert isinstance(instance, analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap)



@given(instance=analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap_strategy)
def test_analysis_bottlenecks_doubletobottleneckswithschedulingreportmap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=DoubleToBottlenecksWithSchedulingReportMap_strategy)
@settings(max_examples=50)
def test_doubletobottleneckswithschedulingreportmap_instantiation(instance):
    assert isinstance(instance, DoubleToBottlenecksWithSchedulingReportMap)

@given(instance=analysis_bottlenecks_ScheduledImpactAnalysisData_strategy)
@settings(max_examples=50)
def test_analysis_bottlenecks_scheduledimpactanalysisdata_instantiation(instance):
    assert isinstance(instance, analysis_bottlenecks_ScheduledImpactAnalysisData)

@given(instance=BufferToDoubleMap_strategy)
@settings(max_examples=50)
def test_buffertodoublemap_instantiation(instance):
    assert isinstance(instance, BufferToDoubleMap)

@given(instance=BufferToIntegerMap_strategy)
@settings(max_examples=50)
def test_buffertointegermap_instantiation(instance):
    assert isinstance(instance, BufferToIntegerMap)

@given(instance=analysis_bottlenecks_ActionBottlenecksWithSchedulingData_strategy)
@settings(max_examples=50)
def test_analysis_bottlenecks_actionbottleneckswithschedulingdata_instantiation(instance):
    assert isinstance(instance, analysis_bottlenecks_ActionBottlenecksWithSchedulingData)



@given(instance=analysis_bottlenecks_ActionBottlenecksWithSchedulingData_strategy)
def test_analysis_bottlenecks_actionbottleneckswithschedulingdata_totalWeight_setter(instance):
    original = instance.totalWeight
    instance.totalWeight = original
    assert instance.totalWeight == original



@given(instance=analysis_bottlenecks_ActionBottlenecksWithSchedulingData_strategy)
def test_analysis_bottlenecks_actionbottleneckswithschedulingdata_cpFirings_setter(instance):
    original = instance.cpFirings
    instance.cpFirings = original
    assert instance.cpFirings == original



@given(instance=analysis_bottlenecks_ActionBottlenecksWithSchedulingData_strategy)
def test_analysis_bottlenecks_actionbottleneckswithschedulingdata_cpWeight_setter(instance):
    original = instance.cpWeight
    instance.cpWeight = original
    assert instance.cpWeight == original



@given(instance=analysis_bottlenecks_ActionBottlenecksWithSchedulingData_strategy)
def test_analysis_bottlenecks_actionbottleneckswithschedulingdata_totalFirings_setter(instance):
    original = instance.totalFirings
    instance.totalFirings = original
    assert instance.totalFirings == original

@given(instance=StringToDoubleMap_strategy)
@settings(max_examples=50)
def test_stringtodoublemap_instantiation(instance):
    assert isinstance(instance, StringToDoubleMap)

@given(instance=ActionBottlenecksWithSchedulingData_strategy)
@settings(max_examples=50)
def test_actionbottleneckswithschedulingdata_instantiation(instance):
    assert isinstance(instance, ActionBottlenecksWithSchedulingData)

@given(instance=postprocessing_PostProcessingData_strategy)
@settings(max_examples=50)
def test_postprocessing_postprocessingdata_instantiation(instance):
    assert isinstance(instance, postprocessing_PostProcessingData)

@given(instance=analysis_bottlenecks_DoubleToBottlenecksReportMap_strategy)
@settings(max_examples=50)
def test_analysis_bottlenecks_doubletobottlenecksreportmap_instantiation(instance):
    assert isinstance(instance, analysis_bottlenecks_DoubleToBottlenecksReportMap)



@given(instance=analysis_bottlenecks_DoubleToBottlenecksReportMap_strategy)
def test_analysis_bottlenecks_doubletobottlenecksreportmap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=DoubleToBottlenecksReportMap_strategy)
@settings(max_examples=50)
def test_doubletobottlenecksreportmap_instantiation(instance):
    assert isinstance(instance, DoubleToBottlenecksReportMap)

@given(instance=DoubleToDoubleMap_strategy)
@settings(max_examples=50)
def test_doubletodoublemap_instantiation(instance):
    assert isinstance(instance, DoubleToDoubleMap)

@given(instance=bottlenecks_analysis_ActorClass_strategy)
@settings(max_examples=50)
def test_bottlenecks_analysis_actorclass_instantiation(instance):
    assert isinstance(instance, bottlenecks_analysis_ActorClass)

@given(instance=analysis_bottlenecks_ImpactAnalysisData_strategy)
@settings(max_examples=50)
def test_analysis_bottlenecks_impactanalysisdata_instantiation(instance):
    assert isinstance(instance, analysis_bottlenecks_ImpactAnalysisData)

@given(instance=BottlenecksReport_strategy)
@settings(max_examples=50)
def test_bottlenecksreport_instantiation(instance):
    assert isinstance(instance, BottlenecksReport)

@given(instance=ImpactAnalysisData_strategy)
@settings(max_examples=50)
def test_impactanalysisdata_instantiation(instance):
    assert isinstance(instance, ImpactAnalysisData)

@given(instance=analysis_bottlenecks_ActionBottlenecksData_strategy)
@settings(max_examples=50)
def test_analysis_bottlenecks_actionbottlenecksdata_instantiation(instance):
    assert isinstance(instance, analysis_bottlenecks_ActionBottlenecksData)



@given(instance=analysis_bottlenecks_ActionBottlenecksData_strategy)
def test_analysis_bottlenecks_actionbottlenecksdata_totalVariance_setter(instance):
    original = instance.totalVariance
    instance.totalVariance = original
    assert instance.totalVariance == original



@given(instance=analysis_bottlenecks_ActionBottlenecksData_strategy)
def test_analysis_bottlenecks_actionbottlenecksdata_totalFirings_setter(instance):
    original = instance.totalFirings
    instance.totalFirings = original
    assert instance.totalFirings == original



@given(instance=analysis_bottlenecks_ActionBottlenecksData_strategy)
def test_analysis_bottlenecks_actionbottlenecksdata_totalWeight_setter(instance):
    original = instance.totalWeight
    instance.totalWeight = original
    assert instance.totalWeight == original



@given(instance=analysis_bottlenecks_ActionBottlenecksData_strategy)
def test_analysis_bottlenecks_actionbottlenecksdata_slackMin_setter(instance):
    original = instance.slackMin
    instance.slackMin = original
    assert instance.slackMin == original



@given(instance=analysis_bottlenecks_ActionBottlenecksData_strategy)
def test_analysis_bottlenecks_actionbottlenecksdata_cpVariance_setter(instance):
    original = instance.cpVariance
    instance.cpVariance = original
    assert instance.cpVariance == original



@given(instance=analysis_bottlenecks_ActionBottlenecksData_strategy)
def test_analysis_bottlenecks_actionbottlenecksdata_cpWeight_setter(instance):
    original = instance.cpWeight
    instance.cpWeight = original
    assert instance.cpWeight == original



@given(instance=analysis_bottlenecks_ActionBottlenecksData_strategy)
def test_analysis_bottlenecks_actionbottlenecksdata_cpFirings_setter(instance):
    original = instance.cpFirings
    instance.cpFirings = original
    assert instance.cpFirings == original



@given(instance=analysis_bottlenecks_ActionBottlenecksData_strategy)
def test_analysis_bottlenecks_actionbottlenecksdata_slackMax_setter(instance):
    original = instance.slackMax
    instance.slackMax = original
    assert instance.slackMax == original

@given(instance=ActionBottlenecksData_strategy)
@settings(max_examples=50)
def test_actionbottlenecksdata_instantiation(instance):
    assert isinstance(instance, ActionBottlenecksData)

@given(instance=bottlenecks_analysis_Network_strategy)
@settings(max_examples=50)
def test_bottlenecks_analysis_network_instantiation(instance):
    assert isinstance(instance, bottlenecks_analysis_Network)

@given(instance=analysis_trace_MarkovModelActionData_strategy)
@settings(max_examples=50)
def test_analysis_trace_markovmodelactiondata_instantiation(instance):
    assert isinstance(instance, analysis_trace_MarkovModelActionData)



@given(instance=analysis_trace_MarkovModelActionData_strategy)
def test_analysis_trace_markovmodelactiondata_successors_setter(instance):
    original = instance.successors
    instance.successors = original
    assert instance.successors == original



@given(instance=analysis_trace_MarkovModelActionData_strategy)
def test_analysis_trace_markovmodelactiondata_first_setter(instance):
    original = instance.first
    instance.first = original
    assert instance.first == original

@given(instance=MarkovModelActionData_strategy)
@settings(max_examples=50)
def test_markovmodelactiondata_instantiation(instance):
    assert isinstance(instance, MarkovModelActionData)

@given(instance=analysis_trace_ComparedAction_strategy)
@settings(max_examples=50)
def test_analysis_trace_comparedaction_instantiation(instance):
    assert isinstance(instance, analysis_trace_ComparedAction)



@given(instance=analysis_trace_ComparedAction_strategy)
def test_analysis_trace_comparedaction_found_setter(instance):
    original = instance.found
    instance.found = original
    assert instance.found == original



@given(instance=analysis_trace_ComparedAction_strategy)
def test_analysis_trace_comparedaction_dIncomings_setter(instance):
    original = instance.dIncomings
    instance.dIncomings = original
    assert instance.dIncomings == original



@given(instance=analysis_trace_ComparedAction_strategy)
def test_analysis_trace_comparedaction_dOutgoings_setter(instance):
    original = instance.dOutgoings
    instance.dOutgoings = original
    assert instance.dOutgoings == original



@given(instance=analysis_trace_ComparedAction_strategy)
def test_analysis_trace_comparedaction_dSteps_setter(instance):
    original = instance.dSteps
    instance.dSteps = original
    assert instance.dSteps == original

@given(instance=ComparedAction_strategy)
@settings(max_examples=50)
def test_comparedaction_instantiation(instance):
    assert isinstance(instance, ComparedAction)

@given(instance=bottlenecks_analysis_Action_strategy)
@settings(max_examples=50)
def test_bottlenecks_analysis_action_instantiation(instance):
    assert isinstance(instance, bottlenecks_analysis_Action)

@given(instance=analysis_trace_ComparedTrace_strategy)
@settings(max_examples=50)
def test_analysis_trace_comparedtrace_instantiation(instance):
    assert isinstance(instance, analysis_trace_ComparedTrace)



@given(instance=analysis_trace_ComparedTrace_strategy)
def test_analysis_trace_comparedtrace_dDependencies_setter(instance):
    original = instance.dDependencies
    instance.dDependencies = original
    assert instance.dDependencies == original



@given(instance=analysis_trace_ComparedTrace_strategy)
def test_analysis_trace_comparedtrace_dSteps_setter(instance):
    original = instance.dSteps
    instance.dSteps = original
    assert instance.dSteps == original



@given(instance=analysis_trace_ComparedTrace_strategy)
def test_analysis_trace_comparedtrace_equal_setter(instance):
    original = instance.equal
    instance.equal = original
    assert instance.equal == original

@given(instance=ComparedTrace_strategy)
@settings(max_examples=50)
def test_comparedtrace_instantiation(instance):
    assert isinstance(instance, ComparedTrace)

@given(instance=CompressedTraceReport_strategy)
@settings(max_examples=50)
def test_compressedtracereport_instantiation(instance):
    assert isinstance(instance, CompressedTraceReport)

@given(instance=BufferToLongMap_strategy)
@settings(max_examples=50)
def test_buffertolongmap_instantiation(instance):
    assert isinstance(instance, BufferToLongMap)

@given(instance=PortToLongMap_strategy)
@settings(max_examples=50)
def test_porttolongmap_instantiation(instance):
    assert isinstance(instance, PortToLongMap)

@given(instance=VariableToLongMap_strategy)
@settings(max_examples=50)
def test_variabletolongmap_instantiation(instance):
    assert isinstance(instance, VariableToLongMap)

@given(instance=GuardToLongMap_strategy)
@settings(max_examples=50)
def test_guardtolongmap_instantiation(instance):
    assert isinstance(instance, GuardToLongMap)

@given(instance=analysis_trace_CompressedDependency_strategy)
@settings(max_examples=50)
def test_analysis_trace_compresseddependency_instantiation(instance):
    assert isinstance(instance, analysis_trace_CompressedDependency)



@given(instance=analysis_trace_CompressedDependency_strategy)
def test_analysis_trace_compresseddependency_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original

@given(instance=trace_analysis_Action_strategy)
@settings(max_examples=50)
def test_trace_analysis_action_instantiation(instance):
    assert isinstance(instance, trace_analysis_Action)

@given(instance=analysis_trace_CompressedStep_strategy)
@settings(max_examples=50)
def test_analysis_trace_compressedstep_instantiation(instance):
    assert isinstance(instance, analysis_trace_CompressedStep)



@given(instance=analysis_trace_CompressedStep_strategy)
def test_analysis_trace_compressedstep_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original

@given(instance=CompressedDependency_strategy)
@settings(max_examples=50)
def test_compresseddependency_instantiation(instance):
    assert isinstance(instance, CompressedDependency)

@given(instance=analysis_trace_CompressedVariableDependency_strategy)
@settings(max_examples=50)
def test_analysis_trace_compressedvariabledependency_instantiation(instance):
    assert isinstance(instance, analysis_trace_CompressedVariableDependency)

@given(instance=analysis_trace_CompressedFsmDependency_strategy)
@settings(max_examples=50)
def test_analysis_trace_compressedfsmdependency_instantiation(instance):
    assert isinstance(instance, analysis_trace_CompressedFsmDependency)

@given(instance=analysis_trace_CompressedTokensDependency_strategy)
@settings(max_examples=50)
def test_analysis_trace_compressedtokensdependency_instantiation(instance):
    assert isinstance(instance, analysis_trace_CompressedTokensDependency)

@given(instance=analysis_trace_CompressedPortDependency_strategy)
@settings(max_examples=50)
def test_analysis_trace_compressedportdependency_instantiation(instance):
    assert isinstance(instance, analysis_trace_CompressedPortDependency)

@given(instance=analysis_trace_CompressedGuardDependency_strategy)
@settings(max_examples=50)
def test_analysis_trace_compressedguarddependency_instantiation(instance):
    assert isinstance(instance, analysis_trace_CompressedGuardDependency)

@given(instance=CompressedStep_strategy)
@settings(max_examples=50)
def test_compressedstep_instantiation(instance):
    assert isinstance(instance, CompressedStep)

@given(instance=trace_analysis_Network_strategy)
@settings(max_examples=50)
def test_trace_analysis_network_instantiation(instance):
    assert isinstance(instance, trace_analysis_Network)

@given(instance=StringToLongMap_strategy)
@settings(max_examples=50)
def test_stringtolongmap_instantiation(instance):
    assert isinstance(instance, StringToLongMap)

@given(instance=analysis_map_ActionToDoubleMap_strategy)
@settings(max_examples=50)
def test_analysis_map_actiontodoublemap_instantiation(instance):
    assert isinstance(instance, analysis_map_ActionToDoubleMap)



@given(instance=analysis_map_ActionToDoubleMap_strategy)
def test_analysis_map_actiontodoublemap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ActorToLongMap_strategy)
@settings(max_examples=50)
def test_actortolongmap_instantiation(instance):
    assert isinstance(instance, ActorToLongMap)

@given(instance=analysis_map_StringToStringMap_strategy)
@settings(max_examples=50)
def test_analysis_map_stringtostringmap_instantiation(instance):
    assert isinstance(instance, analysis_map_StringToStringMap)



@given(instance=analysis_map_StringToStringMap_strategy)
def test_analysis_map_stringtostringmap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=analysis_map_StringToStringMap_strategy)
def test_analysis_map_stringtostringmap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ActorSelectionSchedule_strategy)
@settings(max_examples=50)
def test_actorselectionschedule_instantiation(instance):
    assert isinstance(instance, ActorSelectionSchedule)

@given(instance=analysis_map_PartitionToActorSelectionScheduleMap_strategy)
@settings(max_examples=50)
def test_analysis_map_partitiontoactorselectionschedulemap_instantiation(instance):
    assert isinstance(instance, analysis_map_PartitionToActorSelectionScheduleMap)



@given(instance=analysis_map_PartitionToActorSelectionScheduleMap_strategy)
def test_analysis_map_partitiontoactorselectionschedulemap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=analysis_map_BufferToDoubleMap_strategy)
@settings(max_examples=50)
def test_analysis_map_buffertodoublemap_instantiation(instance):
    assert isinstance(instance, analysis_map_BufferToDoubleMap)



@given(instance=analysis_map_BufferToDoubleMap_strategy)
def test_analysis_map_buffertodoublemap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=analysis_map_BufferToIntegerMap_strategy)
@settings(max_examples=50)
def test_analysis_map_buffertointegermap_instantiation(instance):
    assert isinstance(instance, analysis_map_BufferToIntegerMap)



@given(instance=analysis_map_BufferToIntegerMap_strategy)
def test_analysis_map_buffertointegermap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=map_analysis_Procedure_strategy)
@settings(max_examples=50)
def test_map_analysis_procedure_instantiation(instance):
    assert isinstance(instance, map_analysis_Procedure)

@given(instance=analysis_map_StringToDoubleMap_strategy)
@settings(max_examples=50)
def test_analysis_map_stringtodoublemap_instantiation(instance):
    assert isinstance(instance, analysis_map_StringToDoubleMap)



@given(instance=analysis_map_StringToDoubleMap_strategy)
def test_analysis_map_stringtodoublemap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=analysis_map_StringToDoubleMap_strategy)
def test_analysis_map_stringtodoublemap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=map_analysis_Port_strategy)
@settings(max_examples=50)
def test_map_analysis_port_instantiation(instance):
    assert isinstance(instance, map_analysis_Port)

@given(instance=analysis_map_PortToLongMap_strategy)
@settings(max_examples=50)
def test_analysis_map_porttolongmap_instantiation(instance):
    assert isinstance(instance, analysis_map_PortToLongMap)



@given(instance=analysis_map_PortToLongMap_strategy)
def test_analysis_map_porttolongmap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=map_analysis_Guard_strategy)
@settings(max_examples=50)
def test_map_analysis_guard_instantiation(instance):
    assert isinstance(instance, map_analysis_Guard)

@given(instance=analysis_map_GuardToLongMap_strategy)
@settings(max_examples=50)
def test_analysis_map_guardtolongmap_instantiation(instance):
    assert isinstance(instance, analysis_map_GuardToLongMap)



@given(instance=analysis_map_GuardToLongMap_strategy)
def test_analysis_map_guardtolongmap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=analysis_map_VariableToLongMap_strategy)
@settings(max_examples=50)
def test_analysis_map_variabletolongmap_instantiation(instance):
    assert isinstance(instance, analysis_map_VariableToLongMap)



@given(instance=analysis_map_VariableToLongMap_strategy)
def test_analysis_map_variabletolongmap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=analysis_map_DoubleToDoubleMap_strategy)
@settings(max_examples=50)
def test_analysis_map_doubletodoublemap_instantiation(instance):
    assert isinstance(instance, analysis_map_DoubleToDoubleMap)



@given(instance=analysis_map_DoubleToDoubleMap_strategy)
def test_analysis_map_doubletodoublemap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=analysis_map_DoubleToDoubleMap_strategy)
def test_analysis_map_doubletodoublemap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=analysis_map_StringToLongMap_strategy)
@settings(max_examples=50)
def test_analysis_map_stringtolongmap_instantiation(instance):
    assert isinstance(instance, analysis_map_StringToLongMap)



@given(instance=analysis_map_StringToLongMap_strategy)
def test_analysis_map_stringtolongmap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=analysis_map_StringToLongMap_strategy)
def test_analysis_map_stringtolongmap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=analysis_map_BufferToLongMap_strategy)
@settings(max_examples=50)
def test_analysis_map_buffertolongmap_instantiation(instance):
    assert isinstance(instance, analysis_map_BufferToLongMap)



@given(instance=analysis_map_BufferToLongMap_strategy)
def test_analysis_map_buffertolongmap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=analysis_map_ActorToLongMap_strategy)
@settings(max_examples=50)
def test_analysis_map_actortolongmap_instantiation(instance):
    assert isinstance(instance, analysis_map_ActorToLongMap)



@given(instance=analysis_map_ActorToLongMap_strategy)
def test_analysis_map_actortolongmap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=analysis_map_ActionToLongMap_strategy)
@settings(max_examples=50)
def test_analysis_map_actiontolongmap_instantiation(instance):
    assert isinstance(instance, analysis_map_ActionToLongMap)



@given(instance=analysis_map_ActionToLongMap_strategy)
def test_analysis_map_actiontolongmap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=analysis_map_EOperatorToStatisticalDataMap_strategy)
@settings(max_examples=50)
def test_analysis_map_eoperatortostatisticaldatamap_instantiation(instance):
    assert isinstance(instance, analysis_map_EOperatorToStatisticalDataMap)



@given(instance=analysis_map_EOperatorToStatisticalDataMap_strategy)
def test_analysis_map_eoperatortostatisticaldatamap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=map_analysis_ActorClass_strategy)
@settings(max_examples=50)
def test_map_analysis_actorclass_instantiation(instance):
    assert isinstance(instance, map_analysis_ActorClass)

@given(instance=analysis_map_ActorClassToStatisticalDataMap_strategy)
@settings(max_examples=50)
def test_analysis_map_actorclasstostatisticaldatamap_instantiation(instance):
    assert isinstance(instance, analysis_map_ActorClassToStatisticalDataMap)

@given(instance=map_analysis_Variable_strategy)
@settings(max_examples=50)
def test_map_analysis_variable_instantiation(instance):
    assert isinstance(instance, map_analysis_Variable)

@given(instance=analysis_map_VariableToStatisticalDataMap_strategy)
@settings(max_examples=50)
def test_analysis_map_variabletostatisticaldatamap_instantiation(instance):
    assert isinstance(instance, analysis_map_VariableToStatisticalDataMap)

@given(instance=analysis_map_ProcedureToStatisticalDataMap_strategy)
@settings(max_examples=50)
def test_analysis_map_proceduretostatisticaldatamap_instantiation(instance):
    assert isinstance(instance, analysis_map_ProcedureToStatisticalDataMap)

@given(instance=map_analysis_Buffer_strategy)
@settings(max_examples=50)
def test_map_analysis_buffer_instantiation(instance):
    assert isinstance(instance, map_analysis_Buffer)

@given(instance=analysis_map_BufferToStatisticalDataMap_strategy)
@settings(max_examples=50)
def test_analysis_map_buffertostatisticaldatamap_instantiation(instance):
    assert isinstance(instance, analysis_map_BufferToStatisticalDataMap)

@given(instance=map_analysis_Action_strategy)
@settings(max_examples=50)
def test_map_analysis_action_instantiation(instance):
    assert isinstance(instance, map_analysis_Action)

@given(instance=analysis_map_ActionToStatisticalDataMap_strategy)
@settings(max_examples=50)
def test_analysis_map_actiontostatisticaldatamap_instantiation(instance):
    assert isinstance(instance, analysis_map_ActionToStatisticalDataMap)

@given(instance=map_analysis_StatisticalData_strategy)
@settings(max_examples=50)
def test_map_analysis_statisticaldata_instantiation(instance):
    assert isinstance(instance, map_analysis_StatisticalData)

@given(instance=map_analysis_Actor_strategy)
@settings(max_examples=50)
def test_map_analysis_actor_instantiation(instance):
    assert isinstance(instance, map_analysis_Actor)

@given(instance=analysis_map_ActorToStatisticalDataMap_strategy)
@settings(max_examples=50)
def test_analysis_map_actortostatisticaldatamap_instantiation(instance):
    assert isinstance(instance, analysis_map_ActorToStatisticalDataMap)

@given(instance=analysis_map_StringToIntegerMap_strategy)
@settings(max_examples=50)
def test_analysis_map_stringtointegermap_instantiation(instance):
    assert isinstance(instance, analysis_map_StringToIntegerMap)



@given(instance=analysis_map_StringToIntegerMap_strategy)
def test_analysis_map_stringtointegermap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=analysis_map_StringToIntegerMap_strategy)
def test_analysis_map_stringtointegermap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=StringToStringMap_strategy)
@settings(max_examples=50)
def test_stringtostringmap_instantiation(instance):
    assert isinstance(instance, StringToStringMap)

@given(instance=analysis_profiler_TableRow_strategy)
@settings(max_examples=50)
def test_analysis_profiler_tablerow_instantiation(instance):
    assert isinstance(instance, analysis_profiler_TableRow)

@given(instance=TableRow_strategy)
@settings(max_examples=50)
def test_tablerow_instantiation(instance):
    assert isinstance(instance, TableRow)

@given(instance=AccessData_strategy)
@settings(max_examples=50)
def test_accessdata_instantiation(instance):
    assert isinstance(instance, AccessData)

@given(instance=analysis_profiler_StringToAccessDataMap_strategy)
@settings(max_examples=50)
def test_analysis_profiler_stringtoaccessdatamap_instantiation(instance):
    assert isinstance(instance, analysis_profiler_StringToAccessDataMap)



@given(instance=analysis_profiler_StringToAccessDataMap_strategy)
def test_analysis_profiler_stringtoaccessdatamap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=analysis_profiler_AccessData_strategy)
@settings(max_examples=50)
def test_analysis_profiler_accessdata_instantiation(instance):
    assert isinstance(instance, analysis_profiler_AccessData)



@given(instance=analysis_profiler_AccessData_strategy)
def test_analysis_profiler_accessdata_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original



@given(instance=analysis_profiler_AccessData_strategy)
def test_analysis_profiler_accessdata_average_setter(instance):
    original = instance.average
    instance.average = original
    assert instance.average == original



@given(instance=analysis_profiler_AccessData_strategy)
def test_analysis_profiler_accessdata_total_setter(instance):
    original = instance.total
    instance.total = original
    assert instance.total == original



@given(instance=analysis_profiler_AccessData_strategy)
def test_analysis_profiler_accessdata_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original



@given(instance=analysis_profiler_AccessData_strategy)
def test_analysis_profiler_accessdata_accesses_setter(instance):
    original = instance.accesses
    instance.accesses = original
    assert instance.accesses == original

@given(instance=profiler_analysis_Procedure_strategy)
@settings(max_examples=50)
def test_profiler_analysis_procedure_instantiation(instance):
    assert isinstance(instance, profiler_analysis_Procedure)

@given(instance=StringToAccessDataMap_strategy)
@settings(max_examples=50)
def test_stringtoaccessdatamap_instantiation(instance):
    assert isinstance(instance, StringToAccessDataMap)

@given(instance=analysis_profiler_MemoryAccessData_strategy)
@settings(max_examples=50)
def test_analysis_profiler_memoryaccessdata_instantiation(instance):
    assert isinstance(instance, analysis_profiler_MemoryAccessData)

@given(instance=MemoryAccessData_strategy)
@settings(max_examples=50)
def test_memoryaccessdata_instantiation(instance):
    assert isinstance(instance, MemoryAccessData)

@given(instance=analysis_profiler_StateVariableAccessData_strategy)
@settings(max_examples=50)
def test_analysis_profiler_statevariableaccessdata_instantiation(instance):
    assert isinstance(instance, analysis_profiler_StateVariableAccessData)



@given(instance=analysis_profiler_StateVariableAccessData_strategy)
def test_analysis_profiler_statevariableaccessdata_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=analysis_profiler_LocalVariableAccessData_strategy)
@settings(max_examples=50)
def test_analysis_profiler_localvariableaccessdata_instantiation(instance):
    assert isinstance(instance, analysis_profiler_LocalVariableAccessData)



@given(instance=analysis_profiler_LocalVariableAccessData_strategy)
def test_analysis_profiler_localvariableaccessdata_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=analysis_profiler_SharedVariableAccessData_strategy)
@settings(max_examples=50)
def test_analysis_profiler_sharedvariableaccessdata_instantiation(instance):
    assert isinstance(instance, analysis_profiler_SharedVariableAccessData)



@given(instance=analysis_profiler_SharedVariableAccessData_strategy)
def test_analysis_profiler_sharedvariableaccessdata_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=analysis_profiler_BufferAccessData_strategy)
@settings(max_examples=50)
def test_analysis_profiler_bufferaccessdata_instantiation(instance):
    assert isinstance(instance, analysis_profiler_BufferAccessData)



@given(instance=analysis_profiler_BufferAccessData_strategy)
def test_analysis_profiler_bufferaccessdata_targetActor_setter(instance):
    original = instance.targetActor
    instance.targetActor = original
    assert instance.targetActor == original



@given(instance=analysis_profiler_BufferAccessData_strategy)
def test_analysis_profiler_bufferaccessdata_targetPort_setter(instance):
    original = instance.targetPort
    instance.targetPort = original
    assert instance.targetPort == original



@given(instance=analysis_profiler_BufferAccessData_strategy)
def test_analysis_profiler_bufferaccessdata_sourceActor_setter(instance):
    original = instance.sourceActor
    instance.sourceActor = original
    assert instance.sourceActor == original



@given(instance=analysis_profiler_BufferAccessData_strategy)
def test_analysis_profiler_bufferaccessdata_sourcePort_setter(instance):
    original = instance.sourcePort
    instance.sourcePort = original
    assert instance.sourcePort == original

@given(instance=analysis_profiler_ActionMemoryProfilingData_strategy)
@settings(max_examples=50)
def test_analysis_profiler_actionmemoryprofilingdata_instantiation(instance):
    assert isinstance(instance, analysis_profiler_ActionMemoryProfilingData)



@given(instance=analysis_profiler_ActionMemoryProfilingData_strategy)
def test_analysis_profiler_actionmemoryprofilingdata_actor_setter(instance):
    original = instance.actor
    instance.actor = original
    assert instance.actor == original



@given(instance=analysis_profiler_ActionMemoryProfilingData_strategy)
def test_analysis_profiler_actionmemoryprofilingdata_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=ActionMemoryProfilingData_strategy)
@settings(max_examples=50)
def test_actionmemoryprofilingdata_instantiation(instance):
    assert isinstance(instance, ActionMemoryProfilingData)

@given(instance=ActionDynamicData_strategy)
@settings(max_examples=50)
def test_actiondynamicdata_instantiation(instance):
    assert isinstance(instance, ActionDynamicData)

@given(instance=analysis_profiler_ProcedureToComplexDynamicDataMap_strategy)
@settings(max_examples=50)
def test_analysis_profiler_proceduretocomplexdynamicdatamap_instantiation(instance):
    assert isinstance(instance, analysis_profiler_ProcedureToComplexDynamicDataMap)

@given(instance=BufferToStatisticalDataMap_strategy)
@settings(max_examples=50)
def test_buffertostatisticaldatamap_instantiation(instance):
    assert isinstance(instance, BufferToStatisticalDataMap)

@given(instance=ProcedureToComplexDynamicDataMap_strategy)
@settings(max_examples=50)
def test_proceduretocomplexdynamicdatamap_instantiation(instance):
    assert isinstance(instance, ProcedureToComplexDynamicDataMap)

@given(instance=VariableToStatisticalDataMap_strategy)
@settings(max_examples=50)
def test_variabletostatisticaldatamap_instantiation(instance):
    assert isinstance(instance, VariableToStatisticalDataMap)

@given(instance=ProcedureToStatisticalDataMap_strategy)
@settings(max_examples=50)
def test_proceduretostatisticaldatamap_instantiation(instance):
    assert isinstance(instance, ProcedureToStatisticalDataMap)

@given(instance=EOperatorToStatisticalDataMap_strategy)
@settings(max_examples=50)
def test_eoperatortostatisticaldatamap_instantiation(instance):
    assert isinstance(instance, EOperatorToStatisticalDataMap)

@given(instance=analysis_profiler_ComplexDynamicData_strategy)
@settings(max_examples=50)
def test_analysis_profiler_complexdynamicdata_instantiation(instance):
    assert isinstance(instance, analysis_profiler_ComplexDynamicData)

@given(instance=ActionToLongMap_strategy)
@settings(max_examples=50)
def test_actiontolongmap_instantiation(instance):
    assert isinstance(instance, ActionToLongMap)

@given(instance=ActionToStatisticalDataMap_strategy)
@settings(max_examples=50)
def test_actiontostatisticaldatamap_instantiation(instance):
    assert isinstance(instance, ActionToStatisticalDataMap)

@given(instance=profiler_analysis_StatisticalData_strategy)
@settings(max_examples=50)
def test_profiler_analysis_statisticaldata_instantiation(instance):
    assert isinstance(instance, profiler_analysis_StatisticalData)

@given(instance=profiler_analysis_Buffer_strategy)
@settings(max_examples=50)
def test_profiler_analysis_buffer_instantiation(instance):
    assert isinstance(instance, profiler_analysis_Buffer)

@given(instance=analysis_profiler_BufferDynamicData_strategy)
@settings(max_examples=50)
def test_analysis_profiler_bufferdynamicdata_instantiation(instance):
    assert isinstance(instance, analysis_profiler_BufferDynamicData)



@given(instance=analysis_profiler_BufferDynamicData_strategy)
def test_analysis_profiler_bufferdynamicdata_unconsumedTokens_setter(instance):
    original = instance.unconsumedTokens
    instance.unconsumedTokens = original
    assert instance.unconsumedTokens == original

@given(instance=profiler_analysis_Action_strategy)
@settings(max_examples=50)
def test_profiler_analysis_action_instantiation(instance):
    assert isinstance(instance, profiler_analysis_Action)

@given(instance=profiler_analysis_Actor_strategy)
@settings(max_examples=50)
def test_profiler_analysis_actor_instantiation(instance):
    assert isinstance(instance, profiler_analysis_Actor)

@given(instance=ComplexDynamicData_strategy)
@settings(max_examples=50)
def test_complexdynamicdata_instantiation(instance):
    assert isinstance(instance, ComplexDynamicData)

@given(instance=analysis_profiler_ActionDynamicData_strategy)
@settings(max_examples=50)
def test_analysis_profiler_actiondynamicdata_instantiation(instance):
    assert isinstance(instance, analysis_profiler_ActionDynamicData)

@given(instance=analysis_profiler_ActorDynamicData_strategy)
@settings(max_examples=50)
def test_analysis_profiler_actordynamicdata_instantiation(instance):
    assert isinstance(instance, analysis_profiler_ActorDynamicData)

@given(instance=BufferDynamicData_strategy)
@settings(max_examples=50)
def test_bufferdynamicdata_instantiation(instance):
    assert isinstance(instance, BufferDynamicData)

@given(instance=ActorDynamicData_strategy)
@settings(max_examples=50)
def test_actordynamicdata_instantiation(instance):
    assert isinstance(instance, ActorDynamicData)

@given(instance=CodeData_strategy)
@settings(max_examples=50)
def test_codedata_instantiation(instance):
    assert isinstance(instance, CodeData)

@given(instance=analysis_profiler_ComplexCodeData_strategy)
@settings(max_examples=50)
def test_analysis_profiler_complexcodedata_instantiation(instance):
    assert isinstance(instance, analysis_profiler_ComplexCodeData)

@given(instance=StringToIntegerMap_strategy)
@settings(max_examples=50)
def test_stringtointegermap_instantiation(instance):
    assert isinstance(instance, StringToIntegerMap)

@given(instance=analysis_profiler_CodeData_strategy)
@settings(max_examples=50)
def test_analysis_profiler_codedata_instantiation(instance):
    assert isinstance(instance, analysis_profiler_CodeData)



@given(instance=analysis_profiler_CodeData_strategy)
def test_analysis_profiler_codedata_blockName_setter(instance):
    original = instance.blockName
    instance.blockName = original
    assert instance.blockName == original



@given(instance=analysis_profiler_CodeData_strategy)
def test_analysis_profiler_codedata_nol_setter(instance):
    original = instance.nol
    instance.nol = original
    assert instance.nol == original

@given(instance=ComplexCodeData_strategy)
@settings(max_examples=50)
def test_complexcodedata_instantiation(instance):
    assert isinstance(instance, ComplexCodeData)

@given(instance=profiler_analysis_Network_strategy)
@settings(max_examples=50)
def test_profiler_analysis_network_instantiation(instance):
    assert isinstance(instance, profiler_analysis_Network)

@given(instance=AnalysisReport_strategy)
@settings(max_examples=50)
def test_analysisreport_instantiation(instance):
    assert isinstance(instance, AnalysisReport)

@given(instance=analysis_profiler_MemoryProfilingReport_strategy)
@settings(max_examples=50)
def test_analysis_profiler_memoryprofilingreport_instantiation(instance):
    assert isinstance(instance, analysis_profiler_MemoryProfilingReport)



@given(instance=analysis_profiler_MemoryProfilingReport_strategy)
def test_analysis_profiler_memoryprofilingreport_networkName_setter(instance):
    original = instance.networkName
    instance.networkName = original
    assert instance.networkName == original

@given(instance=analysis_partitioning_ComCostPartitioningReport_strategy)
@settings(max_examples=50)
def test_analysis_partitioning_comcostpartitioningreport_instantiation(instance):
    assert isinstance(instance, analysis_partitioning_ComCostPartitioningReport)



@given(instance=analysis_partitioning_ComCostPartitioningReport_strategy)
def test_analysis_partitioning_comcostpartitioningreport_bitAccurate_setter(instance):
    original = instance.bitAccurate
    instance.bitAccurate = original
    assert instance.bitAccurate == original

@given(instance=analysis_trace_TraceSizeReport_strategy)
@settings(max_examples=50)
def test_analysis_trace_tracesizereport_instantiation(instance):
    assert isinstance(instance, analysis_trace_TraceSizeReport)



@given(instance=analysis_trace_TraceSizeReport_strategy)
def test_analysis_trace_tracesizereport_firings_setter(instance):
    original = instance.firings
    instance.firings = original
    assert instance.firings == original



@given(instance=analysis_trace_TraceSizeReport_strategy)
def test_analysis_trace_tracesizereport_dependencies_setter(instance):
    original = instance.dependencies
    instance.dependencies = original
    assert instance.dependencies == original

@given(instance=analysis_bottlenecks_ScheduledImpactAnalysisReport_strategy)
@settings(max_examples=50)
def test_analysis_bottlenecks_scheduledimpactanalysisreport_instantiation(instance):
    assert isinstance(instance, analysis_bottlenecks_ScheduledImpactAnalysisReport)



@given(instance=analysis_bottlenecks_ScheduledImpactAnalysisReport_strategy)
def test_analysis_bottlenecks_scheduledimpactanalysisreport_classLevel_setter(instance):
    original = instance.classLevel
    instance.classLevel = original
    assert instance.classLevel == original

@given(instance=analysis_pipelining_ImpactAnalysisReport_strategy)
@settings(max_examples=50)
def test_analysis_pipelining_impactanalysisreport_instantiation(instance):
    assert isinstance(instance, analysis_pipelining_ImpactAnalysisReport)

@given(instance=analysis_buffers_OptimalBuffersReport_strategy)
@settings(max_examples=50)
def test_analysis_buffers_optimalbuffersreport_instantiation(instance):
    assert isinstance(instance, analysis_buffers_OptimalBuffersReport)



@given(instance=analysis_buffers_OptimalBuffersReport_strategy)
def test_analysis_buffers_optimalbuffersreport_bitAccurate_setter(instance):
    original = instance.bitAccurate
    instance.bitAccurate = original
    assert instance.bitAccurate == original



@given(instance=analysis_buffers_OptimalBuffersReport_strategy)
def test_analysis_buffers_optimalbuffersreport_pow2_setter(instance):
    original = instance.pow2
    instance.pow2 = original
    assert instance.pow2 == original

@given(instance=analysis_profiler_BenchmarkReport_strategy)
@settings(max_examples=50)
def test_analysis_profiler_benchmarkreport_instantiation(instance):
    assert isinstance(instance, analysis_profiler_BenchmarkReport)



@given(instance=analysis_profiler_BenchmarkReport_strategy)
def test_analysis_profiler_benchmarkreport_column_names_setter(instance):
    original = instance.column_names
    instance.column_names = original
    assert instance.column_names == original

@given(instance=analysis_profiler_DynamicProfilingReport_strategy)
@settings(max_examples=50)
def test_analysis_profiler_dynamicprofilingreport_instantiation(instance):
    assert isinstance(instance, analysis_profiler_DynamicProfilingReport)

@given(instance=analysis_trace_TraceComparatorReport_strategy)
@settings(max_examples=50)
def test_analysis_trace_tracecomparatorreport_instantiation(instance):
    assert isinstance(instance, analysis_trace_TraceComparatorReport)

@given(instance=analysis_bottlenecks_BottlenecksWithSchedulingReport_strategy)
@settings(max_examples=50)
def test_analysis_bottlenecks_bottleneckswithschedulingreport_instantiation(instance):
    assert isinstance(instance, analysis_bottlenecks_BottlenecksWithSchedulingReport)



@given(instance=analysis_bottlenecks_BottlenecksWithSchedulingReport_strategy)
def test_analysis_bottlenecks_bottleneckswithschedulingreport_totalFirings_setter(instance):
    original = instance.totalFirings
    instance.totalFirings = original
    assert instance.totalFirings == original



@given(instance=analysis_bottlenecks_BottlenecksWithSchedulingReport_strategy)
def test_analysis_bottlenecks_bottleneckswithschedulingreport_cpFirings_setter(instance):
    original = instance.cpFirings
    instance.cpFirings = original
    assert instance.cpFirings == original



@given(instance=analysis_bottlenecks_BottlenecksWithSchedulingReport_strategy)
def test_analysis_bottlenecks_bottleneckswithschedulingreport_cpWeight_setter(instance):
    original = instance.cpWeight
    instance.cpWeight = original
    assert instance.cpWeight == original



@given(instance=analysis_bottlenecks_BottlenecksWithSchedulingReport_strategy)
def test_analysis_bottlenecks_bottleneckswithschedulingreport_cpBlockingTime_setter(instance):
    original = instance.cpBlockingTime
    instance.cpBlockingTime = original
    assert instance.cpBlockingTime == original



@given(instance=analysis_bottlenecks_BottlenecksWithSchedulingReport_strategy)
def test_analysis_bottlenecks_bottleneckswithschedulingreport_executionTime_setter(instance):
    original = instance.executionTime
    instance.executionTime = original
    assert instance.executionTime == original



@given(instance=analysis_bottlenecks_BottlenecksWithSchedulingReport_strategy)
def test_analysis_bottlenecks_bottleneckswithschedulingreport_totalWeight_setter(instance):
    original = instance.totalWeight
    instance.totalWeight = original
    assert instance.totalWeight == original

@given(instance=analysis_trace_CompressedTraceReport_strategy)
@settings(max_examples=50)
def test_analysis_trace_compressedtracereport_instantiation(instance):
    assert isinstance(instance, analysis_trace_CompressedTraceReport)



@given(instance=analysis_trace_CompressedTraceReport_strategy)
def test_analysis_trace_compressedtracereport_traceFile_setter(instance):
    original = instance.traceFile
    instance.traceFile = original
    assert instance.traceFile == original

@given(instance=analysis_pipelining_ActionsVariablePipeliningReport_strategy)
@settings(max_examples=50)
def test_analysis_pipelining_actionsvariablepipeliningreport_instantiation(instance):
    assert isinstance(instance, analysis_pipelining_ActionsVariablePipeliningReport)

@given(instance=analysis_buffers_BoundedBuffersReport_strategy)
@settings(max_examples=50)
def test_analysis_buffers_boundedbuffersreport_instantiation(instance):
    assert isinstance(instance, analysis_buffers_BoundedBuffersReport)



@given(instance=analysis_buffers_BoundedBuffersReport_strategy)
def test_analysis_buffers_boundedbuffersreport_bitSize_setter(instance):
    original = instance.bitSize
    instance.bitSize = original
    assert instance.bitSize == original



@given(instance=analysis_buffers_BoundedBuffersReport_strategy)
def test_analysis_buffers_boundedbuffersreport_tokenSize_setter(instance):
    original = instance.tokenSize
    instance.tokenSize = original
    assert instance.tokenSize == original



@given(instance=analysis_buffers_BoundedBuffersReport_strategy)
def test_analysis_buffers_boundedbuffersreport_bitAccurate_setter(instance):
    original = instance.bitAccurate
    instance.bitAccurate = original
    assert instance.bitAccurate == original



@given(instance=analysis_buffers_BoundedBuffersReport_strategy)
def test_analysis_buffers_boundedbuffersreport_pow2_setter(instance):
    original = instance.pow2
    instance.pow2 = original
    assert instance.pow2 == original

@given(instance=analysis_partitioning_WorkloadBalancePartitioningReport_strategy)
@settings(max_examples=50)
def test_analysis_partitioning_workloadbalancepartitioningreport_instantiation(instance):
    assert isinstance(instance, analysis_partitioning_WorkloadBalancePartitioningReport)

@given(instance=analysis_bottlenecks_BottlenecksReport_strategy)
@settings(max_examples=50)
def test_analysis_bottlenecks_bottlenecksreport_instantiation(instance):
    assert isinstance(instance, analysis_bottlenecks_BottlenecksReport)



@given(instance=analysis_bottlenecks_BottlenecksReport_strategy)
def test_analysis_bottlenecks_bottlenecksreport_cpWeight_setter(instance):
    original = instance.cpWeight
    instance.cpWeight = original
    assert instance.cpWeight == original



@given(instance=analysis_bottlenecks_BottlenecksReport_strategy)
def test_analysis_bottlenecks_bottlenecksreport_cpFirings_setter(instance):
    original = instance.cpFirings
    instance.cpFirings = original
    assert instance.cpFirings == original



@given(instance=analysis_bottlenecks_BottlenecksReport_strategy)
def test_analysis_bottlenecks_bottlenecksreport_totalVariance_setter(instance):
    original = instance.totalVariance
    instance.totalVariance = original
    assert instance.totalVariance == original



@given(instance=analysis_bottlenecks_BottlenecksReport_strategy)
def test_analysis_bottlenecks_bottlenecksreport_totalFirings_setter(instance):
    original = instance.totalFirings
    instance.totalFirings = original
    assert instance.totalFirings == original



@given(instance=analysis_bottlenecks_BottlenecksReport_strategy)
def test_analysis_bottlenecks_bottlenecksreport_totalWeight_setter(instance):
    original = instance.totalWeight
    instance.totalWeight = original
    assert instance.totalWeight == original



@given(instance=analysis_bottlenecks_BottlenecksReport_strategy)
def test_analysis_bottlenecks_bottlenecksreport_cpVariance_setter(instance):
    original = instance.cpVariance
    instance.cpVariance = original
    assert instance.cpVariance == original

@given(instance=analysis_trace_MarkowModelTraceReport_strategy)
@settings(max_examples=50)
def test_analysis_trace_markowmodeltracereport_instantiation(instance):
    assert isinstance(instance, analysis_trace_MarkowModelTraceReport)

@given(instance=analysis_bottlenecks_ImpactAnalysisReport_strategy)
@settings(max_examples=50)
def test_analysis_bottlenecks_impactanalysisreport_instantiation(instance):
    assert isinstance(instance, analysis_bottlenecks_ImpactAnalysisReport)



@given(instance=analysis_bottlenecks_ImpactAnalysisReport_strategy)
def test_analysis_bottlenecks_impactanalysisreport_classLevel_setter(instance):
    original = instance.classLevel
    instance.classLevel = original
    assert instance.classLevel == original

@given(instance=analysis_partitioning_BalancedPipelinePartitioningReport_strategy)
@settings(max_examples=50)
def test_analysis_partitioning_balancedpipelinepartitioningreport_instantiation(instance):
    assert isinstance(instance, analysis_partitioning_BalancedPipelinePartitioningReport)

@given(instance=analysis_profiler_CodeProfilingReport_strategy)
@settings(max_examples=50)
def test_analysis_profiler_codeprofilingreport_instantiation(instance):
    assert isinstance(instance, analysis_profiler_CodeProfilingReport)

@given(instance=analysis_AnalysisReport_strategy)
@settings(max_examples=50)
def test_analysis_analysisreport_instantiation(instance):
    assert isinstance(instance, analysis_AnalysisReport)



@given(instance=analysis_AnalysisReport_strategy)
def test_analysis_analysisreport_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=analysis_AnalysisReport_strategy)
def test_analysis_analysisreport_algorithm_setter(instance):
    original = instance.algorithm
    instance.algorithm = original
    assert instance.algorithm == original

@given(instance=analysis_scheduling_MarkovSchedulingTransition_strategy)
@settings(max_examples=50)
def test_analysis_scheduling_markovschedulingtransition_instantiation(instance):
    assert isinstance(instance, analysis_scheduling_MarkovSchedulingTransition)



@given(instance=analysis_scheduling_MarkovSchedulingTransition_strategy)
def test_analysis_scheduling_markovschedulingtransition_firings_setter(instance):
    original = instance.firings
    instance.firings = original
    assert instance.firings == original



@given(instance=analysis_scheduling_MarkovSchedulingTransition_strategy)
def test_analysis_scheduling_markovschedulingtransition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=analysis_caseoptimal_CaseOptimalActorSelectionSchedule_strategy)
@settings(max_examples=50)
def test_analysis_caseoptimal_caseoptimalactorselectionschedule_instantiation(instance):
    assert isinstance(instance, analysis_caseoptimal_CaseOptimalActorSelectionSchedule)

@given(instance=PartitionToActorSelectionScheduleMap_strategy)
@settings(max_examples=50)
def test_partitiontoactorselectionschedulemap_instantiation(instance):
    assert isinstance(instance, PartitionToActorSelectionScheduleMap)

@given(instance=analysis_caseoptimal_CaseOptimalScheduleReport_strategy)
@settings(max_examples=50)
def test_analysis_caseoptimal_caseoptimalschedulereport_instantiation(instance):
    assert isinstance(instance, analysis_caseoptimal_CaseOptimalScheduleReport)



@given(instance=analysis_caseoptimal_CaseOptimalScheduleReport_strategy)
def test_analysis_caseoptimal_caseoptimalschedulereport_partitionFilePath_setter(instance):
    original = instance.partitionFilePath
    instance.partitionFilePath = original
    assert instance.partitionFilePath == original



@given(instance=analysis_caseoptimal_CaseOptimalScheduleReport_strategy)
def test_analysis_caseoptimal_caseoptimalschedulereport_traceFile_setter(instance):
    original = instance.traceFile
    instance.traceFile = original
    assert instance.traceFile == original



@given(instance=analysis_caseoptimal_CaseOptimalScheduleReport_strategy)
def test_analysis_caseoptimal_caseoptimalschedulereport_pipeline_setter(instance):
    original = instance.pipeline
    instance.pipeline = original
    assert instance.pipeline == original

@given(instance=analysis_scheduling_MarkovSchedulingState_strategy)
@settings(max_examples=50)
def test_analysis_scheduling_markovschedulingstate_instantiation(instance):
    assert isinstance(instance, analysis_scheduling_MarkovSchedulingState)



@given(instance=analysis_scheduling_MarkovSchedulingState_strategy)
def test_analysis_scheduling_markovschedulingstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=analysis_scheduling_MarkovSchedulingState_strategy)
def test_analysis_scheduling_markovschedulingstate_firings_setter(instance):
    original = instance.firings
    instance.firings = original
    assert instance.firings == original

@given(instance=MarkovSchedulingTransition_strategy)
@settings(max_examples=50)
def test_markovschedulingtransition_instantiation(instance):
    assert isinstance(instance, MarkovSchedulingTransition)

@given(instance=MarkovSchedulingState_strategy)
@settings(max_examples=50)
def test_markovschedulingstate_instantiation(instance):
    assert isinstance(instance, MarkovSchedulingState)

@given(instance=scheduling_analysis_Actor_strategy)
@settings(max_examples=50)
def test_scheduling_analysis_actor_instantiation(instance):
    assert isinstance(instance, scheduling_analysis_Actor)

@given(instance=analysis_scheduling_MarkovPartitionScheduler_strategy)
@settings(max_examples=50)
def test_analysis_scheduling_markovpartitionscheduler_instantiation(instance):
    assert isinstance(instance, analysis_scheduling_MarkovPartitionScheduler)



@given(instance=analysis_scheduling_MarkovPartitionScheduler_strategy)
def test_analysis_scheduling_markovpartitionscheduler_partitionId_setter(instance):
    original = instance.partitionId
    instance.partitionId = original
    assert instance.partitionId == original

@given(instance=scheduling_analysis_Network_strategy)
@settings(max_examples=50)
def test_scheduling_analysis_network_instantiation(instance):
    assert isinstance(instance, scheduling_analysis_Network)

@given(instance=MarkovPartitionScheduler_strategy)
@settings(max_examples=50)
def test_markovpartitionscheduler_instantiation(instance):
    assert isinstance(instance, MarkovPartitionScheduler)

@given(instance=analysis_scheduling_MarkovSimpleSchedulerReport_strategy)
@settings(max_examples=50)
def test_analysis_scheduling_markovsimpleschedulerreport_instantiation(instance):
    assert isinstance(instance, analysis_scheduling_MarkovSimpleSchedulerReport)

@given(instance=FSMCombination_strategy)
@settings(max_examples=50)
def test_fsmcombination_instantiation(instance):
    assert isinstance(instance, FSMCombination)

@given(instance=analysis_scheduling_FSMCondition_strategy)
@settings(max_examples=50)
def test_analysis_scheduling_fsmcondition_instantiation(instance):
    assert isinstance(instance, analysis_scheduling_FSMCondition)



@given(instance=analysis_scheduling_FSMCondition_strategy)
def test_analysis_scheduling_fsmcondition_valName_setter(instance):
    original = instance.valName
    instance.valName = original
    assert instance.valName == original



@given(instance=analysis_scheduling_FSMCondition_strategy)
def test_analysis_scheduling_fsmcondition_compval_setter(instance):
    original = instance.compval
    instance.compval = original
    assert instance.compval == original



@given(instance=analysis_scheduling_FSMCondition_strategy)
def test_analysis_scheduling_fsmcondition_comp_setter(instance):
    original = instance.comp
    instance.comp = original
    assert instance.comp == original

@given(instance=analysis_scheduling_FSMCombination_strategy)
@settings(max_examples=50)
def test_analysis_scheduling_fsmcombination_instantiation(instance):
    assert isinstance(instance, analysis_scheduling_FSMCombination)



@given(instance=analysis_scheduling_FSMCombination_strategy)
def test_analysis_scheduling_fsmcombination_combinator_setter(instance):
    original = instance.combinator
    instance.combinator = original
    assert instance.combinator == original

@given(instance=FSMVar_strategy)
@settings(max_examples=50)
def test_fsmvar_instantiation(instance):
    assert isinstance(instance, FSMVar)

@given(instance=analysis_scheduling_FSMOperation_strategy)
@settings(max_examples=50)
def test_analysis_scheduling_fsmoperation_instantiation(instance):
    assert isinstance(instance, analysis_scheduling_FSMOperation)



@given(instance=analysis_scheduling_FSMOperation_strategy)
def test_analysis_scheduling_fsmoperation_var_setter(instance):
    original = instance.var
    instance.var = original
    assert instance.var == original



@given(instance=analysis_scheduling_FSMOperation_strategy)
def test_analysis_scheduling_fsmoperation_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original



@given(instance=analysis_scheduling_FSMOperation_strategy)
def test_analysis_scheduling_fsmoperation_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=FSMOperation_strategy)
@settings(max_examples=50)
def test_fsmoperation_instantiation(instance):
    assert isinstance(instance, FSMOperation)

@given(instance=analysis_scheduling_FSMVarUpdate_strategy)
@settings(max_examples=50)
def test_analysis_scheduling_fsmvarupdate_instantiation(instance):
    assert isinstance(instance, analysis_scheduling_FSMVarUpdate)

@given(instance=FSMTransition_strategy)
@settings(max_examples=50)
def test_fsmtransition_instantiation(instance):
    assert isinstance(instance, FSMTransition)

@given(instance=analysis_scheduling_FSMTransitionWithState_strategy)
@settings(max_examples=50)
def test_analysis_scheduling_fsmtransitionwithstate_instantiation(instance):
    assert isinstance(instance, analysis_scheduling_FSMTransitionWithState)

@given(instance=FSMVarUpdate_strategy)
@settings(max_examples=50)
def test_fsmvarupdate_instantiation(instance):
    assert isinstance(instance, FSMVarUpdate)

@given(instance=analysis_scheduling_FSMState_strategy)
@settings(max_examples=50)
def test_analysis_scheduling_fsmstate_instantiation(instance):
    assert isinstance(instance, analysis_scheduling_FSMState)



@given(instance=analysis_scheduling_FSMState_strategy)
def test_analysis_scheduling_fsmstate_enumName_setter(instance):
    original = instance.enumName
    instance.enumName = original
    assert instance.enumName == original

@given(instance=Sequence_strategy)
@settings(max_examples=50)
def test_sequence_instantiation(instance):
    assert isinstance(instance, Sequence)

@given(instance=FSMCondition_strategy)
@settings(max_examples=50)
def test_fsmcondition_instantiation(instance):
    assert isinstance(instance, FSMCondition)

@given(instance=analysis_scheduling_FSMTransition_strategy)
@settings(max_examples=50)
def test_analysis_scheduling_fsmtransition_instantiation(instance):
    assert isinstance(instance, analysis_scheduling_FSMTransition)



@given(instance=analysis_scheduling_FSMTransition_strategy)
def test_analysis_scheduling_fsmtransition_sourceStateEnumName_setter(instance):
    original = instance.sourceStateEnumName
    instance.sourceStateEnumName = original
    assert instance.sourceStateEnumName == original



@given(instance=analysis_scheduling_FSMTransition_strategy)
def test_analysis_scheduling_fsmtransition_targetStateEnumName_setter(instance):
    original = instance.targetStateEnumName
    instance.targetStateEnumName = original
    assert instance.targetStateEnumName == original

@given(instance=analysis_scheduling_FSMVar_strategy)
@settings(max_examples=50)
def test_analysis_scheduling_fsmvar_instantiation(instance):
    assert isinstance(instance, analysis_scheduling_FSMVar)



@given(instance=analysis_scheduling_FSMVar_strategy)
def test_analysis_scheduling_fsmvar_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=analysis_scheduling_FSMVar_strategy)
def test_analysis_scheduling_fsmvar_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=analysis_scheduling_FSMVar_strategy)
def test_analysis_scheduling_fsmvar_initialVal_setter(instance):
    original = instance.initialVal
    instance.initialVal = original
    assert instance.initialVal == original

@given(instance=ActorFire_strategy)
@settings(max_examples=50)
def test_actorfire_instantiation(instance):
    assert isinstance(instance, ActorFire)

@given(instance=analysis_scheduling_PartitionedActorFire_strategy)
@settings(max_examples=50)
def test_analysis_scheduling_partitionedactorfire_instantiation(instance):
    assert isinstance(instance, analysis_scheduling_PartitionedActorFire)

@given(instance=analysis_scheduling_Sequence_strategy)
@settings(max_examples=50)
def test_analysis_scheduling_sequence_instantiation(instance):
    assert isinstance(instance, analysis_scheduling_Sequence)

@given(instance=analysis_scheduling_ActorSelectionSchedule_strategy)
@settings(max_examples=50)
def test_analysis_scheduling_actorselectionschedule_instantiation(instance):
    assert isinstance(instance, analysis_scheduling_ActorSelectionSchedule)

@given(instance=profiling_analysis_Actor_strategy)
@settings(max_examples=50)
def test_profiling_analysis_actor_instantiation(instance):
    assert isinstance(instance, profiling_analysis_Actor)

@given(instance=analysis_profiling_IntraActorCommunicationData_strategy)
@settings(max_examples=50)
def test_analysis_profiling_intraactorcommunicationdata_instantiation(instance):
    assert isinstance(instance, analysis_profiling_IntraActorCommunicationData)

@given(instance=FSMState_strategy)
@settings(max_examples=50)
def test_fsmstate_instantiation(instance):
    assert isinstance(instance, FSMState)

@given(instance=analysis_scheduling_FSM_strategy)
@settings(max_examples=50)
def test_analysis_scheduling_fsm_instantiation(instance):
    assert isinstance(instance, analysis_scheduling_FSM)



@given(instance=analysis_scheduling_FSM_strategy)
def test_analysis_scheduling_fsm_startState_setter(instance):
    original = instance.startState
    instance.startState = original
    assert instance.startState == original



@given(instance=analysis_scheduling_FSM_strategy)
def test_analysis_scheduling_fsm_terminalState_setter(instance):
    original = instance.terminalState
    instance.terminalState = original
    assert instance.terminalState == original

@given(instance=analysis_scheduling_ActorFire_strategy)
@settings(max_examples=50)
def test_analysis_scheduling_actorfire_instantiation(instance):
    assert isinstance(instance, analysis_scheduling_ActorFire)



@given(instance=analysis_scheduling_ActorFire_strategy)
def test_analysis_scheduling_actorfire_partition_setter(instance):
    original = instance.partition
    instance.partition = original
    assert instance.partition == original



@given(instance=analysis_scheduling_ActorFire_strategy)
def test_analysis_scheduling_actorfire_Actor_setter(instance):
    original = instance.Actor
    instance.Actor = original
    assert instance.Actor == original



@given(instance=analysis_scheduling_ActorFire_strategy)
def test_analysis_scheduling_actorfire_dependencyPartitions_setter(instance):
    original = instance.dependencyPartitions
    instance.dependencyPartitions = original
    assert instance.dependencyPartitions == original



@given(instance=analysis_scheduling_ActorFire_strategy)
def test_analysis_scheduling_actorfire_Times_setter(instance):
    original = instance.Times
    instance.Times = original
    assert instance.Times == original

@given(instance=analysis_profiling_ProfilingStatsActorData_strategy)
@settings(max_examples=50)
def test_analysis_profiling_profilingstatsactordata_instantiation(instance):
    assert isinstance(instance, analysis_profiling_ProfilingStatsActorData)



@given(instance=analysis_profiling_ProfilingStatsActorData_strategy)
def test_analysis_profiling_profilingstatsactordata_actorName_setter(instance):
    original = instance.actorName
    instance.actorName = original
    assert instance.actorName == original



@given(instance=analysis_profiling_ProfilingStatsActorData_strategy)
def test_analysis_profiling_profilingstatsactordata_schedulerWeight_setter(instance):
    original = instance.schedulerWeight
    instance.schedulerWeight = original
    assert instance.schedulerWeight == original



@given(instance=analysis_profiling_ProfilingStatsActorData_strategy)
def test_analysis_profiling_profilingstatsactordata_actionsWeight_setter(instance):
    original = instance.actionsWeight
    instance.actionsWeight = original
    assert instance.actionsWeight == original



@given(instance=analysis_profiling_ProfilingStatsActorData_strategy)
def test_analysis_profiling_profilingstatsactordata_actionsWeightPercent_setter(instance):
    original = instance.actionsWeightPercent
    instance.actionsWeightPercent = original
    assert instance.actionsWeightPercent == original



@given(instance=analysis_profiling_ProfilingStatsActorData_strategy)
def test_analysis_profiling_profilingstatsactordata_schedulerWeightPercent_setter(instance):
    original = instance.schedulerWeightPercent
    instance.schedulerWeightPercent = original
    assert instance.schedulerWeightPercent == original

@given(instance=ProfilingStatsActorData_strategy)
@settings(max_examples=50)
def test_profilingstatsactordata_instantiation(instance):
    assert isinstance(instance, ProfilingStatsActorData)

@given(instance=analysis_profiling_ProfilingStatsReport_strategy)
@settings(max_examples=50)
def test_analysis_profiling_profilingstatsreport_instantiation(instance):
    assert isinstance(instance, analysis_profiling_ProfilingStatsReport)



@given(instance=analysis_profiling_ProfilingStatsReport_strategy)
def test_analysis_profiling_profilingstatsreport_networkName_setter(instance):
    original = instance.networkName
    instance.networkName = original
    assert instance.networkName == original

@given(instance=profiling_analysis_Action_strategy)
@settings(max_examples=50)
def test_profiling_analysis_action_instantiation(instance):
    assert isinstance(instance, profiling_analysis_Action)

@given(instance=analysis_profiling_IntraActionCommunicationData_strategy)
@settings(max_examples=50)
def test_analysis_profiling_intraactioncommunicationdata_instantiation(instance):
    assert isinstance(instance, analysis_profiling_IntraActionCommunicationData)

@given(instance=IntraActionCommunicationData_strategy)
@settings(max_examples=50)
def test_intraactioncommunicationdata_instantiation(instance):
    assert isinstance(instance, IntraActionCommunicationData)

@given(instance=profiling_analysis_StatisticalData_strategy)
@settings(max_examples=50)
def test_profiling_analysis_statisticaldata_instantiation(instance):
    assert isinstance(instance, profiling_analysis_StatisticalData)

@given(instance=profiling_analysis_Network_strategy)
@settings(max_examples=50)
def test_profiling_analysis_network_instantiation(instance):
    assert isinstance(instance, profiling_analysis_Network)

@given(instance=IntraActorCommunicationData_strategy)
@settings(max_examples=50)
def test_intraactorcommunicationdata_instantiation(instance):
    assert isinstance(instance, IntraActorCommunicationData)

@given(instance=analysis_profiling_IntraActionCommunicationReport_strategy)
@settings(max_examples=50)
def test_analysis_profiling_intraactioncommunicationreport_instantiation(instance):
    assert isinstance(instance, analysis_profiling_IntraActionCommunicationReport)

@given(instance=ActorToStatisticalDataMap_strategy)
@settings(max_examples=50)
def test_actortostatisticaldatamap_instantiation(instance):
    assert isinstance(instance, ActorToStatisticalDataMap)

@given(instance=postprocessing_analysis_StatisticalData_strategy)
@settings(max_examples=50)
def test_postprocessing_analysis_statisticaldata_instantiation(instance):
    assert isinstance(instance, postprocessing_analysis_StatisticalData)

@given(instance=analysis_postprocessing_SchedulerChecksPartition_strategy)
@settings(max_examples=50)
def test_analysis_postprocessing_schedulercheckspartition_instantiation(instance):
    assert isinstance(instance, analysis_postprocessing_SchedulerChecksPartition)

@given(instance=SchedulerChecksPartition_strategy)
@settings(max_examples=50)
def test_schedulercheckspartition_instantiation(instance):
    assert isinstance(instance, SchedulerChecksPartition)

@given(instance=pipelining_analysis_ActorClass_strategy)
@settings(max_examples=50)
def test_pipelining_analysis_actorclass_instantiation(instance):
    assert isinstance(instance, pipelining_analysis_ActorClass)

@given(instance=ActionToDoubleMap_strategy)
@settings(max_examples=50)
def test_actiontodoublemap_instantiation(instance):
    assert isinstance(instance, ActionToDoubleMap)

@given(instance=postprocessing_analysis_Actor_strategy)
@settings(max_examples=50)
def test_postprocessing_analysis_actor_instantiation(instance):
    assert isinstance(instance, postprocessing_analysis_Actor)

@given(instance=analysis_postprocessing_StatisticalActorPartition_strategy)
@settings(max_examples=50)
def test_analysis_postprocessing_statisticalactorpartition_instantiation(instance):
    assert isinstance(instance, analysis_postprocessing_StatisticalActorPartition)



@given(instance=analysis_postprocessing_StatisticalActorPartition_strategy)
def test_analysis_postprocessing_statisticalactorpartition_occupancy_setter(instance):
    original = instance.occupancy
    instance.occupancy = original
    assert instance.occupancy == original



@given(instance=analysis_postprocessing_StatisticalActorPartition_strategy)
def test_analysis_postprocessing_statisticalactorpartition_schedulingPolicy_setter(instance):
    original = instance.schedulingPolicy
    instance.schedulingPolicy = original
    assert instance.schedulingPolicy == original



@given(instance=analysis_postprocessing_StatisticalActorPartition_strategy)
def test_analysis_postprocessing_statisticalactorpartition_actors_setter(instance):
    original = instance.actors
    instance.actors = original
    assert instance.actors == original

@given(instance=StatisticalActorPartition_strategy)
@settings(max_examples=50)
def test_statisticalactorpartition_instantiation(instance):
    assert isinstance(instance, StatisticalActorPartition)

@given(instance=analysis_postprocessing_PostProcessingData_strategy)
@settings(max_examples=50)
def test_analysis_postprocessing_postprocessingdata_instantiation(instance):
    assert isinstance(instance, analysis_postprocessing_PostProcessingData)

@given(instance=PostProcessingData_strategy)
@settings(max_examples=50)
def test_postprocessingdata_instantiation(instance):
    assert isinstance(instance, PostProcessingData)

@given(instance=analysis_postprocessing_ActorStatisticsReport_strategy)
@settings(max_examples=50)
def test_analysis_postprocessing_actorstatisticsreport_instantiation(instance):
    assert isinstance(instance, analysis_postprocessing_ActorStatisticsReport)



@given(instance=analysis_postprocessing_ActorStatisticsReport_strategy)
def test_analysis_postprocessing_actorstatisticsreport_averageOccupancy_setter(instance):
    original = instance.averageOccupancy
    instance.averageOccupancy = original
    assert instance.averageOccupancy == original



@given(instance=analysis_postprocessing_ActorStatisticsReport_strategy)
def test_analysis_postprocessing_actorstatisticsreport_executionTime_setter(instance):
    original = instance.executionTime
    instance.executionTime = original
    assert instance.executionTime == original



@given(instance=analysis_postprocessing_ActorStatisticsReport_strategy)
def test_analysis_postprocessing_actorstatisticsreport_occupancyDeviation_setter(instance):
    original = instance.occupancyDeviation
    instance.occupancyDeviation = original
    assert instance.occupancyDeviation == original

@given(instance=analysis_postprocessing_BufferBlockingReport_strategy)
@settings(max_examples=50)
def test_analysis_postprocessing_bufferblockingreport_instantiation(instance):
    assert isinstance(instance, analysis_postprocessing_BufferBlockingReport)

@given(instance=analysis_postprocessing_ActionStatisticsReport_strategy)
@settings(max_examples=50)
def test_analysis_postprocessing_actionstatisticsreport_instantiation(instance):
    assert isinstance(instance, analysis_postprocessing_ActionStatisticsReport)

@given(instance=analysis_postprocessing_SchedulerChecksReport_strategy)
@settings(max_examples=50)
def test_analysis_postprocessing_schedulerchecksreport_instantiation(instance):
    assert isinstance(instance, analysis_postprocessing_SchedulerChecksReport)

@given(instance=postprocessing_analysis_Network_strategy)
@settings(max_examples=50)
def test_postprocessing_analysis_network_instantiation(instance):
    assert isinstance(instance, postprocessing_analysis_Network)

@given(instance=analysis_postprocessing_PostProcessingReport_strategy)
@settings(max_examples=50)
def test_analysis_postprocessing_postprocessingreport_instantiation(instance):
    assert isinstance(instance, analysis_postprocessing_PostProcessingReport)



@given(instance=analysis_postprocessing_PostProcessingReport_strategy)
def test_analysis_postprocessing_postprocessingreport_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=analysis_postprocessing_PostProcessingReport_strategy)
def test_analysis_postprocessing_postprocessingreport_deadlock_setter(instance):
    original = instance.deadlock
    instance.deadlock = original
    assert instance.deadlock == original
