import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    analysis::scheduling::MarkovSchedulingTransition,
    PartitionToActorSelectionScheduleMap,
    analysis::partitioning::BalancedPipelinePartition,
    WorkloadBalancePartition,
    analysis::partitioning::WorkloadBalancePartition,
    ScheduledImpactAnalysisData,
    ComCostPartition,
    partitioning::analysis::Network,
    analysis::buffers::OptimalBufferData,
    BoundedBuffersReport,
    OptimalBufferData,
    buffers::analysis::Buffer,
    analysis::buffers::BoundedBufferData,
    BoundedBufferData,
    buffers::analysis::Network,
    BottlenecksWithSchedulingReport,
    analysis::bottlenecks::DoubleToBottlenecksWithSchedulingReportMap,
    DoubleToBottlenecksWithSchedulingReportMap,
    analysis::bottlenecks::ScheduledImpactAnalysisData,
    BufferToDoubleMap,
    BufferToIntegerMap,
    analysis::bottlenecks::ActionBottlenecksWithSchedulingData,
    StringToDoubleMap,
    ActionBottlenecksWithSchedulingData,
    postprocessing::PostProcessingData,
    analysis::bottlenecks::DoubleToBottlenecksReportMap,
    DoubleToBottlenecksReportMap,
    DoubleToDoubleMap,
    bottlenecks::analysis::ActorClass,
    analysis::bottlenecks::ImpactAnalysisData,
    BottlenecksReport,
    ImpactAnalysisData,
    analysis::bottlenecks::ActionBottlenecksData,
    ActionBottlenecksData,
    bottlenecks::analysis::Network,
    analysis::trace::MarkovModelActionData,
    MarkovModelActionData,
    analysis::scheduling::MarkovSchedulingState,
    MarkovSchedulingTransition,
    MarkovSchedulingState,
    scheduling::analysis::Actor,
    analysis::scheduling::MarkovPartitionScheduler,
    scheduling::analysis::Network,
    MarkovPartitionScheduler,
    FSMCombination,
    analysis::scheduling::FSMCondition,
    analysis::scheduling::FSMCombination,
    FSMVar,
    analysis::scheduling::FSMOperation,
    FSMOperation,
    analysis::scheduling::FSMVarUpdate,
    FSMTransition,
    analysis::scheduling::FSMTransitionWithState,
    FSMVarUpdate,
    analysis::scheduling::FSMState,
    Sequence,
    FSMCondition,
    analysis::scheduling::FSMTransition,
    analysis::scheduling::FSMVar,
    ActorFire,
    analysis::scheduling::PartitionedActorFire,
    analysis::scheduling::ActorSelectionSchedule,
    profiling::analysis::Actor,
    analysis::profiling::IntraActorCommunicationData,
    FSMState,
    analysis::profiling::ProfilingStatsActorData,
    ProfilingStatsActorData,
    profiling::analysis::Action,
    analysis::profiling::IntraActionCommunicationData,
    IntraActionCommunicationData,
    profiling::analysis::StatisticalData,
    profiling::analysis::Network,
    IntraActorCommunicationData,
    ActorToStatisticalDataMap,
    postprocessing::analysis::StatisticalData,
    analysis::postprocessing::SchedulerChecksPartition,
    SchedulerChecksPartition,
    pipelining::analysis::ActorClass,
    ActionToDoubleMap,
    postprocessing::analysis::Actor,
    analysis::postprocessing::StatisticalActorPartition,
    StatisticalActorPartition,
    analysis::postprocessing::PostProcessingData,
    PostProcessingData,
    analysis::postprocessing::BufferBlockingReport,
    analysis::postprocessing::SchedulerChecksReport,
    analysis::postprocessing::ActorStatisticsReport,
    analysis::postprocessing::ActionStatisticsReport,
    postprocessing::analysis::Network,
    analysis::pipelining::ImpactAnalysisData,
    ActionsVariablePipeliningReport,
    pipelining::analysis::StatisticalData,
    pipelining::analysis::Action,
    analysis::pipelining::ActionVariablePipeliningData,
    ActionVariablePipeliningData,
    pipelining::analysis::Network,
    BalancedPipelinePartition,
    partitioning::analysis::Actor,
    analysis::partitioning::ComCostPartition,
    ActionToStatisticalDataMap,
    profiler::analysis::StatisticalData,
    profiler::analysis::Buffer,
    analysis::profiler::BufferDynamicData,
    profiler::analysis::Action,
    profiler::analysis::Actor,
    ComplexDynamicData,
    analysis::profiler::ActionDynamicData,
    analysis::profiler::ActorDynamicData,
    BufferDynamicData,
    ActorDynamicData,
    CodeData,
    analysis::profiler::ComplexCodeData,
    StringToIntegerMap,
    analysis::profiler::CodeData,
    ComplexCodeData,
    profiler::analysis::Network,
    AnalysisReport,
    analysis::partitioning::ComCostPartitioningReport,
    analysis::buffers::BoundedBuffersReport,
    analysis::pipelining::ActionsVariablePipeliningReport,
    analysis::bottlenecks::BottlenecksReport,
    analysis::profiler::DynamicProfilingReport,
    analysis::bottlenecks::BottlenecksWithSchedulingReport,
    analysis::scheduling::MarkovSimpleSchedulerReport,
    analysis::buffers::OptimalBuffersReport,
    analysis::profiling::ProfilingStatsReport,
    analysis::trace::MarkowModelTraceReport,
    analysis::partitioning::WorkloadBalancePartitioningReport,
    analysis::postprocessing::PostProcessingReport,
    analysis::bottlenecks::ImpactAnalysisReport,
    analysis::pipelining::ImpactAnalysisReport,
    analysis::caseoptimal::CaseOptimalScheduleReport,
    analysis::bottlenecks::ScheduledImpactAnalysisReport,
    analysis::profiling::IntraActionCommunicationReport,
    analysis::partitioning::BalancedPipelinePartitioningReport,
    analysis::profiler::CodeProfilingReport,
    analysis::AnalysisReport,
    analysis::trace::ComparedAction,
    ComparedAction,
    bottlenecks::analysis::Action,
    analysis::trace::ComparedTrace,
    ComparedTrace,
    CompressedTraceReport,
    analysis::trace::TraceComparatorReport,
    BufferToLongMap,
    PortToLongMap,
    VariableToLongMap,
    GuardToLongMap,
    analysis::trace::CompressedDependency,
    trace::analysis::Action,
    analysis::trace::CompressedStep,
    CompressedDependency,
    analysis::trace::CompressedPortDependency,
    analysis::trace::CompressedGuardDependency,
    analysis::trace::CompressedTokensDependency,
    analysis::trace::CompressedVariableDependency,
    analysis::trace::CompressedFsmDependency,
    CompressedStep,
    analysis::trace::CompressedTraceReport,
    trace::analysis::Network,
    StringToLongMap,
    analysis::map::ActionToDoubleMap,
    ActorToLongMap,
    analysis::trace::TraceSizeReport,
    analysis::map::StringToStringMap,
    ActorSelectionSchedule,
    analysis::scheduling::FSM,
    analysis::scheduling::ActorFire,
    analysis::caseoptimal::CaseOptimalActorSelectionSchedule,
    analysis::scheduling::Sequence,
    analysis::map::PartitionToActorSelectionScheduleMap,
    analysis::map::BufferToDoubleMap,
    analysis::map::BufferToIntegerMap,
    map::analysis::Procedure,
    analysis::map::StringToDoubleMap,
    map::analysis::Port,
    analysis::map::PortToLongMap,
    map::analysis::Guard,
    analysis::map::GuardToLongMap,
    analysis::map::VariableToLongMap,
    analysis::map::DoubleToDoubleMap,
    analysis::map::StringToLongMap,
    analysis::map::BufferToLongMap,
    analysis::map::ActorToLongMap,
    analysis::map::ActionToLongMap,
    analysis::map::EOperatorToStatisticalDataMap,
    map::analysis::ActorClass,
    analysis::map::ActorClassToStatisticalDataMap,
    map::analysis::Variable,
    analysis::map::VariableToStatisticalDataMap,
    analysis::map::ProcedureToStatisticalDataMap,
    map::analysis::Buffer,
    analysis::map::BufferToStatisticalDataMap,
    map::analysis::Action,
    analysis::map::ActionToStatisticalDataMap,
    map::analysis::StatisticalData,
    map::analysis::Actor,
    analysis::map::ActorToStatisticalDataMap,
    analysis::map::StringToIntegerMap,
    StringToStringMap,
    analysis::profiler::TableRow,
    TableRow,
    analysis::profiler::BenchmarkReport,
    AccessData,
    analysis::profiler::StringToAccessDataMap,
    analysis::profiler::AccessData,
    profiler::analysis::Procedure,
    StringToAccessDataMap,
    analysis::profiler::MemoryAccessData,
    MemoryAccessData,
    analysis::profiler::SharedVariableAccessData,
    analysis::profiler::BufferAccessData,
    analysis::profiler::LocalVariableAccessData,
    analysis::profiler::StateVariableAccessData,
    analysis::profiler::ActionMemoryProfilingData,
    ActionMemoryProfilingData,
    analysis::profiler::MemoryProfilingReport,
    ActionDynamicData,
    analysis::profiler::ProcedureToComplexDynamicDataMap,
    BufferToStatisticalDataMap,
    ProcedureToComplexDynamicDataMap,
    VariableToStatisticalDataMap,
    ProcedureToStatisticalDataMap,
    EOperatorToStatisticalDataMap,
    analysis::profiler::ComplexDynamicData,
    ActionToLongMap,
    FSMOp,
    FSMComparator,
    Optimizer,
    FSMCombinator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_analysis::scheduling::markovschedulingtransition_is_not_abstract():
    assert not inspect.isabstract(analysis::scheduling::MarkovSchedulingTransition)


def test_analysis::scheduling::markovschedulingtransition_constructor_exists():
    assert callable(analysis::scheduling::MarkovSchedulingTransition.__init__)


def test_analysis::scheduling::markovschedulingtransition_constructor_args():
    sig = inspect.signature(analysis::scheduling::MarkovSchedulingTransition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "firings" in params, "Missing parameter 'firings'"

def test_analysis::scheduling::markovschedulingtransition_has_name():
    assert hasattr(analysis::scheduling::MarkovSchedulingTransition, "name")
    descriptor = None
    for klass in analysis::scheduling::MarkovSchedulingTransition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_analysis::scheduling::markovschedulingtransition_has_firings():
    assert hasattr(analysis::scheduling::MarkovSchedulingTransition, "firings")
    descriptor = None
    for klass in analysis::scheduling::MarkovSchedulingTransition.__mro__:
        if "firings" in klass.__dict__:
            descriptor = klass.__dict__["firings"]
            break
    assert isinstance(descriptor, property)



def test_partitiontoactorselectionschedulemap_is_not_abstract():
    assert not inspect.isabstract(PartitionToActorSelectionScheduleMap)


def test_partitiontoactorselectionschedulemap_constructor_exists():
    assert callable(PartitionToActorSelectionScheduleMap.__init__)


def test_partitiontoactorselectionschedulemap_constructor_args():
    sig = inspect.signature(PartitionToActorSelectionScheduleMap.__init__)
    params = list(sig.parameters.keys())



def test_analysis::partitioning::balancedpipelinepartition_is_not_abstract():
    assert not inspect.isabstract(analysis::partitioning::BalancedPipelinePartition)


def test_analysis::partitioning::balancedpipelinepartition_constructor_exists():
    assert callable(analysis::partitioning::BalancedPipelinePartition.__init__)


def test_analysis::partitioning::balancedpipelinepartition_constructor_args():
    sig = inspect.signature(analysis::partitioning::BalancedPipelinePartition.__init__)
    params = list(sig.parameters.keys())
    assert "commonPredAvg" in params, "Missing parameter 'commonPredAvg'"
    assert "workload" in params, "Missing parameter 'workload'"
    assert "preWorkload" in params, "Missing parameter 'preWorkload'"

def test_analysis::partitioning::balancedpipelinepartition_has_commonPredAvg():
    assert hasattr(analysis::partitioning::BalancedPipelinePartition, "commonPredAvg")
    descriptor = None
    for klass in analysis::partitioning::BalancedPipelinePartition.__mro__:
        if "commonPredAvg" in klass.__dict__:
            descriptor = klass.__dict__["commonPredAvg"]
            break
    assert isinstance(descriptor, property)

def test_analysis::partitioning::balancedpipelinepartition_has_workload():
    assert hasattr(analysis::partitioning::BalancedPipelinePartition, "workload")
    descriptor = None
    for klass in analysis::partitioning::BalancedPipelinePartition.__mro__:
        if "workload" in klass.__dict__:
            descriptor = klass.__dict__["workload"]
            break
    assert isinstance(descriptor, property)

def test_analysis::partitioning::balancedpipelinepartition_has_preWorkload():
    assert hasattr(analysis::partitioning::BalancedPipelinePartition, "preWorkload")
    descriptor = None
    for klass in analysis::partitioning::BalancedPipelinePartition.__mro__:
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



def test_analysis::partitioning::workloadbalancepartition_is_not_abstract():
    assert not inspect.isabstract(analysis::partitioning::WorkloadBalancePartition)


def test_analysis::partitioning::workloadbalancepartition_constructor_exists():
    assert callable(analysis::partitioning::WorkloadBalancePartition.__init__)


def test_analysis::partitioning::workloadbalancepartition_constructor_args():
    sig = inspect.signature(analysis::partitioning::WorkloadBalancePartition.__init__)
    params = list(sig.parameters.keys())
    assert "workload" in params, "Missing parameter 'workload'"

def test_analysis::partitioning::workloadbalancepartition_has_workload():
    assert hasattr(analysis::partitioning::WorkloadBalancePartition, "workload")
    descriptor = None
    for klass in analysis::partitioning::WorkloadBalancePartition.__mro__:
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



def test_partitioning::analysis::network_is_not_abstract():
    assert not inspect.isabstract(partitioning::analysis::Network)


def test_partitioning::analysis::network_constructor_exists():
    assert callable(partitioning::analysis::Network.__init__)


def test_partitioning::analysis::network_constructor_args():
    sig = inspect.signature(partitioning::analysis::Network.__init__)
    params = list(sig.parameters.keys())



def test_analysis::buffers::optimalbufferdata_is_not_abstract():
    assert not inspect.isabstract(analysis::buffers::OptimalBufferData)


def test_analysis::buffers::optimalbufferdata_constructor_exists():
    assert callable(analysis::buffers::OptimalBufferData.__init__)


def test_analysis::buffers::optimalbufferdata_constructor_args():
    sig = inspect.signature(analysis::buffers::OptimalBufferData.__init__)
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



def test_buffers::analysis::buffer_is_not_abstract():
    assert not inspect.isabstract(buffers::analysis::Buffer)


def test_buffers::analysis::buffer_constructor_exists():
    assert callable(buffers::analysis::Buffer.__init__)


def test_buffers::analysis::buffer_constructor_args():
    sig = inspect.signature(buffers::analysis::Buffer.__init__)
    params = list(sig.parameters.keys())



def test_analysis::buffers::boundedbufferdata_is_not_abstract():
    assert not inspect.isabstract(analysis::buffers::BoundedBufferData)


def test_analysis::buffers::boundedbufferdata_constructor_exists():
    assert callable(analysis::buffers::BoundedBufferData.__init__)


def test_analysis::buffers::boundedbufferdata_constructor_args():
    sig = inspect.signature(analysis::buffers::BoundedBufferData.__init__)
    params = list(sig.parameters.keys())
    assert "tokenSize" in params, "Missing parameter 'tokenSize'"
    assert "bitSize" in params, "Missing parameter 'bitSize'"

def test_analysis::buffers::boundedbufferdata_has_tokenSize():
    assert hasattr(analysis::buffers::BoundedBufferData, "tokenSize")
    descriptor = None
    for klass in analysis::buffers::BoundedBufferData.__mro__:
        if "tokenSize" in klass.__dict__:
            descriptor = klass.__dict__["tokenSize"]
            break
    assert isinstance(descriptor, property)

def test_analysis::buffers::boundedbufferdata_has_bitSize():
    assert hasattr(analysis::buffers::BoundedBufferData, "bitSize")
    descriptor = None
    for klass in analysis::buffers::BoundedBufferData.__mro__:
        if "bitSize" in klass.__dict__:
            descriptor = klass.__dict__["bitSize"]
            break
    assert isinstance(descriptor, property)



def test_boundedbufferdata_is_not_abstract():
    assert not inspect.isabstract(BoundedBufferData)


def test_boundedbufferdata_constructor_exists():
    assert callable(BoundedBufferData.__init__)


def test_boundedbufferdata_constructor_args():
    sig = inspect.signature(BoundedBufferData.__init__)
    params = list(sig.parameters.keys())



def test_buffers::analysis::network_is_not_abstract():
    assert not inspect.isabstract(buffers::analysis::Network)


def test_buffers::analysis::network_constructor_exists():
    assert callable(buffers::analysis::Network.__init__)


def test_buffers::analysis::network_constructor_args():
    sig = inspect.signature(buffers::analysis::Network.__init__)
    params = list(sig.parameters.keys())



def test_bottleneckswithschedulingreport_is_not_abstract():
    assert not inspect.isabstract(BottlenecksWithSchedulingReport)


def test_bottleneckswithschedulingreport_constructor_exists():
    assert callable(BottlenecksWithSchedulingReport.__init__)


def test_bottleneckswithschedulingreport_constructor_args():
    sig = inspect.signature(BottlenecksWithSchedulingReport.__init__)
    params = list(sig.parameters.keys())



def test_analysis::bottlenecks::doubletobottleneckswithschedulingreportmap_is_not_abstract():
    assert not inspect.isabstract(analysis::bottlenecks::DoubleToBottlenecksWithSchedulingReportMap)


def test_analysis::bottlenecks::doubletobottleneckswithschedulingreportmap_constructor_exists():
    assert callable(analysis::bottlenecks::DoubleToBottlenecksWithSchedulingReportMap.__init__)


def test_analysis::bottlenecks::doubletobottleneckswithschedulingreportmap_constructor_args():
    sig = inspect.signature(analysis::bottlenecks::DoubleToBottlenecksWithSchedulingReportMap.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_analysis::bottlenecks::doubletobottleneckswithschedulingreportmap_has_key():
    assert hasattr(analysis::bottlenecks::DoubleToBottlenecksWithSchedulingReportMap, "key")
    descriptor = None
    for klass in analysis::bottlenecks::DoubleToBottlenecksWithSchedulingReportMap.__mro__:
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



def test_analysis::bottlenecks::scheduledimpactanalysisdata_is_not_abstract():
    assert not inspect.isabstract(analysis::bottlenecks::ScheduledImpactAnalysisData)


def test_analysis::bottlenecks::scheduledimpactanalysisdata_constructor_exists():
    assert callable(analysis::bottlenecks::ScheduledImpactAnalysisData.__init__)


def test_analysis::bottlenecks::scheduledimpactanalysisdata_constructor_args():
    sig = inspect.signature(analysis::bottlenecks::ScheduledImpactAnalysisData.__init__)
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



def test_analysis::bottlenecks::actionbottleneckswithschedulingdata_is_not_abstract():
    assert not inspect.isabstract(analysis::bottlenecks::ActionBottlenecksWithSchedulingData)


def test_analysis::bottlenecks::actionbottleneckswithschedulingdata_constructor_exists():
    assert callable(analysis::bottlenecks::ActionBottlenecksWithSchedulingData.__init__)


def test_analysis::bottlenecks::actionbottleneckswithschedulingdata_constructor_args():
    sig = inspect.signature(analysis::bottlenecks::ActionBottlenecksWithSchedulingData.__init__)
    params = list(sig.parameters.keys())
    assert "totalFirings" in params, "Missing parameter 'totalFirings'"
    assert "cpWeight" in params, "Missing parameter 'cpWeight'"
    assert "cpFirings" in params, "Missing parameter 'cpFirings'"
    assert "totalWeight" in params, "Missing parameter 'totalWeight'"

def test_analysis::bottlenecks::actionbottleneckswithschedulingdata_has_totalFirings():
    assert hasattr(analysis::bottlenecks::ActionBottlenecksWithSchedulingData, "totalFirings")
    descriptor = None
    for klass in analysis::bottlenecks::ActionBottlenecksWithSchedulingData.__mro__:
        if "totalFirings" in klass.__dict__:
            descriptor = klass.__dict__["totalFirings"]
            break
    assert isinstance(descriptor, property)

def test_analysis::bottlenecks::actionbottleneckswithschedulingdata_has_cpWeight():
    assert hasattr(analysis::bottlenecks::ActionBottlenecksWithSchedulingData, "cpWeight")
    descriptor = None
    for klass in analysis::bottlenecks::ActionBottlenecksWithSchedulingData.__mro__:
        if "cpWeight" in klass.__dict__:
            descriptor = klass.__dict__["cpWeight"]
            break
    assert isinstance(descriptor, property)

def test_analysis::bottlenecks::actionbottleneckswithschedulingdata_has_cpFirings():
    assert hasattr(analysis::bottlenecks::ActionBottlenecksWithSchedulingData, "cpFirings")
    descriptor = None
    for klass in analysis::bottlenecks::ActionBottlenecksWithSchedulingData.__mro__:
        if "cpFirings" in klass.__dict__:
            descriptor = klass.__dict__["cpFirings"]
            break
    assert isinstance(descriptor, property)

def test_analysis::bottlenecks::actionbottleneckswithschedulingdata_has_totalWeight():
    assert hasattr(analysis::bottlenecks::ActionBottlenecksWithSchedulingData, "totalWeight")
    descriptor = None
    for klass in analysis::bottlenecks::ActionBottlenecksWithSchedulingData.__mro__:
        if "totalWeight" in klass.__dict__:
            descriptor = klass.__dict__["totalWeight"]
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



def test_postprocessing::postprocessingdata_is_not_abstract():
    assert not inspect.isabstract(postprocessing::PostProcessingData)


def test_postprocessing::postprocessingdata_constructor_exists():
    assert callable(postprocessing::PostProcessingData.__init__)


def test_postprocessing::postprocessingdata_constructor_args():
    sig = inspect.signature(postprocessing::PostProcessingData.__init__)
    params = list(sig.parameters.keys())



def test_analysis::bottlenecks::doubletobottlenecksreportmap_is_not_abstract():
    assert not inspect.isabstract(analysis::bottlenecks::DoubleToBottlenecksReportMap)


def test_analysis::bottlenecks::doubletobottlenecksreportmap_constructor_exists():
    assert callable(analysis::bottlenecks::DoubleToBottlenecksReportMap.__init__)


def test_analysis::bottlenecks::doubletobottlenecksreportmap_constructor_args():
    sig = inspect.signature(analysis::bottlenecks::DoubleToBottlenecksReportMap.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_analysis::bottlenecks::doubletobottlenecksreportmap_has_key():
    assert hasattr(analysis::bottlenecks::DoubleToBottlenecksReportMap, "key")
    descriptor = None
    for klass in analysis::bottlenecks::DoubleToBottlenecksReportMap.__mro__:
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



def test_bottlenecks::analysis::actorclass_is_not_abstract():
    assert not inspect.isabstract(bottlenecks::analysis::ActorClass)


def test_bottlenecks::analysis::actorclass_constructor_exists():
    assert callable(bottlenecks::analysis::ActorClass.__init__)


def test_bottlenecks::analysis::actorclass_constructor_args():
    sig = inspect.signature(bottlenecks::analysis::ActorClass.__init__)
    params = list(sig.parameters.keys())



def test_analysis::bottlenecks::impactanalysisdata_is_not_abstract():
    assert not inspect.isabstract(analysis::bottlenecks::ImpactAnalysisData)


def test_analysis::bottlenecks::impactanalysisdata_constructor_exists():
    assert callable(analysis::bottlenecks::ImpactAnalysisData.__init__)


def test_analysis::bottlenecks::impactanalysisdata_constructor_args():
    sig = inspect.signature(analysis::bottlenecks::ImpactAnalysisData.__init__)
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



def test_analysis::bottlenecks::actionbottlenecksdata_is_not_abstract():
    assert not inspect.isabstract(analysis::bottlenecks::ActionBottlenecksData)


def test_analysis::bottlenecks::actionbottlenecksdata_constructor_exists():
    assert callable(analysis::bottlenecks::ActionBottlenecksData.__init__)


def test_analysis::bottlenecks::actionbottlenecksdata_constructor_args():
    sig = inspect.signature(analysis::bottlenecks::ActionBottlenecksData.__init__)
    params = list(sig.parameters.keys())
    assert "totalWeight" in params, "Missing parameter 'totalWeight'"
    assert "slackMin" in params, "Missing parameter 'slackMin'"
    assert "slackMax" in params, "Missing parameter 'slackMax'"
    assert "totalVariance" in params, "Missing parameter 'totalVariance'"
    assert "totalFirings" in params, "Missing parameter 'totalFirings'"
    assert "cpVariance" in params, "Missing parameter 'cpVariance'"
    assert "cpFirings" in params, "Missing parameter 'cpFirings'"
    assert "cpWeight" in params, "Missing parameter 'cpWeight'"

def test_analysis::bottlenecks::actionbottlenecksdata_has_totalWeight():
    assert hasattr(analysis::bottlenecks::ActionBottlenecksData, "totalWeight")
    descriptor = None
    for klass in analysis::bottlenecks::ActionBottlenecksData.__mro__:
        if "totalWeight" in klass.__dict__:
            descriptor = klass.__dict__["totalWeight"]
            break
    assert isinstance(descriptor, property)

def test_analysis::bottlenecks::actionbottlenecksdata_has_slackMin():
    assert hasattr(analysis::bottlenecks::ActionBottlenecksData, "slackMin")
    descriptor = None
    for klass in analysis::bottlenecks::ActionBottlenecksData.__mro__:
        if "slackMin" in klass.__dict__:
            descriptor = klass.__dict__["slackMin"]
            break
    assert isinstance(descriptor, property)

def test_analysis::bottlenecks::actionbottlenecksdata_has_slackMax():
    assert hasattr(analysis::bottlenecks::ActionBottlenecksData, "slackMax")
    descriptor = None
    for klass in analysis::bottlenecks::ActionBottlenecksData.__mro__:
        if "slackMax" in klass.__dict__:
            descriptor = klass.__dict__["slackMax"]
            break
    assert isinstance(descriptor, property)

def test_analysis::bottlenecks::actionbottlenecksdata_has_totalVariance():
    assert hasattr(analysis::bottlenecks::ActionBottlenecksData, "totalVariance")
    descriptor = None
    for klass in analysis::bottlenecks::ActionBottlenecksData.__mro__:
        if "totalVariance" in klass.__dict__:
            descriptor = klass.__dict__["totalVariance"]
            break
    assert isinstance(descriptor, property)

def test_analysis::bottlenecks::actionbottlenecksdata_has_totalFirings():
    assert hasattr(analysis::bottlenecks::ActionBottlenecksData, "totalFirings")
    descriptor = None
    for klass in analysis::bottlenecks::ActionBottlenecksData.__mro__:
        if "totalFirings" in klass.__dict__:
            descriptor = klass.__dict__["totalFirings"]
            break
    assert isinstance(descriptor, property)

def test_analysis::bottlenecks::actionbottlenecksdata_has_cpVariance():
    assert hasattr(analysis::bottlenecks::ActionBottlenecksData, "cpVariance")
    descriptor = None
    for klass in analysis::bottlenecks::ActionBottlenecksData.__mro__:
        if "cpVariance" in klass.__dict__:
            descriptor = klass.__dict__["cpVariance"]
            break
    assert isinstance(descriptor, property)

def test_analysis::bottlenecks::actionbottlenecksdata_has_cpFirings():
    assert hasattr(analysis::bottlenecks::ActionBottlenecksData, "cpFirings")
    descriptor = None
    for klass in analysis::bottlenecks::ActionBottlenecksData.__mro__:
        if "cpFirings" in klass.__dict__:
            descriptor = klass.__dict__["cpFirings"]
            break
    assert isinstance(descriptor, property)

def test_analysis::bottlenecks::actionbottlenecksdata_has_cpWeight():
    assert hasattr(analysis::bottlenecks::ActionBottlenecksData, "cpWeight")
    descriptor = None
    for klass in analysis::bottlenecks::ActionBottlenecksData.__mro__:
        if "cpWeight" in klass.__dict__:
            descriptor = klass.__dict__["cpWeight"]
            break
    assert isinstance(descriptor, property)



def test_actionbottlenecksdata_is_not_abstract():
    assert not inspect.isabstract(ActionBottlenecksData)


def test_actionbottlenecksdata_constructor_exists():
    assert callable(ActionBottlenecksData.__init__)


def test_actionbottlenecksdata_constructor_args():
    sig = inspect.signature(ActionBottlenecksData.__init__)
    params = list(sig.parameters.keys())



def test_bottlenecks::analysis::network_is_not_abstract():
    assert not inspect.isabstract(bottlenecks::analysis::Network)


def test_bottlenecks::analysis::network_constructor_exists():
    assert callable(bottlenecks::analysis::Network.__init__)


def test_bottlenecks::analysis::network_constructor_args():
    sig = inspect.signature(bottlenecks::analysis::Network.__init__)
    params = list(sig.parameters.keys())



def test_analysis::trace::markovmodelactiondata_is_not_abstract():
    assert not inspect.isabstract(analysis::trace::MarkovModelActionData)


def test_analysis::trace::markovmodelactiondata_constructor_exists():
    assert callable(analysis::trace::MarkovModelActionData.__init__)


def test_analysis::trace::markovmodelactiondata_constructor_args():
    sig = inspect.signature(analysis::trace::MarkovModelActionData.__init__)
    params = list(sig.parameters.keys())
    assert "successors" in params, "Missing parameter 'successors'"
    assert "first" in params, "Missing parameter 'first'"

def test_analysis::trace::markovmodelactiondata_has_successors():
    assert hasattr(analysis::trace::MarkovModelActionData, "successors")
    descriptor = None
    for klass in analysis::trace::MarkovModelActionData.__mro__:
        if "successors" in klass.__dict__:
            descriptor = klass.__dict__["successors"]
            break
    assert isinstance(descriptor, property)

def test_analysis::trace::markovmodelactiondata_has_first():
    assert hasattr(analysis::trace::MarkovModelActionData, "first")
    descriptor = None
    for klass in analysis::trace::MarkovModelActionData.__mro__:
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



def test_analysis::scheduling::markovschedulingstate_is_not_abstract():
    assert not inspect.isabstract(analysis::scheduling::MarkovSchedulingState)


def test_analysis::scheduling::markovschedulingstate_constructor_exists():
    assert callable(analysis::scheduling::MarkovSchedulingState.__init__)


def test_analysis::scheduling::markovschedulingstate_constructor_args():
    sig = inspect.signature(analysis::scheduling::MarkovSchedulingState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "firings" in params, "Missing parameter 'firings'"

def test_analysis::scheduling::markovschedulingstate_has_name():
    assert hasattr(analysis::scheduling::MarkovSchedulingState, "name")
    descriptor = None
    for klass in analysis::scheduling::MarkovSchedulingState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_analysis::scheduling::markovschedulingstate_has_firings():
    assert hasattr(analysis::scheduling::MarkovSchedulingState, "firings")
    descriptor = None
    for klass in analysis::scheduling::MarkovSchedulingState.__mro__:
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



def test_scheduling::analysis::actor_is_not_abstract():
    assert not inspect.isabstract(scheduling::analysis::Actor)


def test_scheduling::analysis::actor_constructor_exists():
    assert callable(scheduling::analysis::Actor.__init__)


def test_scheduling::analysis::actor_constructor_args():
    sig = inspect.signature(scheduling::analysis::Actor.__init__)
    params = list(sig.parameters.keys())



def test_analysis::scheduling::markovpartitionscheduler_is_not_abstract():
    assert not inspect.isabstract(analysis::scheduling::MarkovPartitionScheduler)


def test_analysis::scheduling::markovpartitionscheduler_constructor_exists():
    assert callable(analysis::scheduling::MarkovPartitionScheduler.__init__)


def test_analysis::scheduling::markovpartitionscheduler_constructor_args():
    sig = inspect.signature(analysis::scheduling::MarkovPartitionScheduler.__init__)
    params = list(sig.parameters.keys())
    assert "partitionId" in params, "Missing parameter 'partitionId'"

def test_analysis::scheduling::markovpartitionscheduler_has_partitionId():
    assert hasattr(analysis::scheduling::MarkovPartitionScheduler, "partitionId")
    descriptor = None
    for klass in analysis::scheduling::MarkovPartitionScheduler.__mro__:
        if "partitionId" in klass.__dict__:
            descriptor = klass.__dict__["partitionId"]
            break
    assert isinstance(descriptor, property)



def test_scheduling::analysis::network_is_not_abstract():
    assert not inspect.isabstract(scheduling::analysis::Network)


def test_scheduling::analysis::network_constructor_exists():
    assert callable(scheduling::analysis::Network.__init__)


def test_scheduling::analysis::network_constructor_args():
    sig = inspect.signature(scheduling::analysis::Network.__init__)
    params = list(sig.parameters.keys())



def test_markovpartitionscheduler_is_not_abstract():
    assert not inspect.isabstract(MarkovPartitionScheduler)


def test_markovpartitionscheduler_constructor_exists():
    assert callable(MarkovPartitionScheduler.__init__)


def test_markovpartitionscheduler_constructor_args():
    sig = inspect.signature(MarkovPartitionScheduler.__init__)
    params = list(sig.parameters.keys())



def test_fsmcombination_is_not_abstract():
    assert not inspect.isabstract(FSMCombination)


def test_fsmcombination_constructor_exists():
    assert callable(FSMCombination.__init__)


def test_fsmcombination_constructor_args():
    sig = inspect.signature(FSMCombination.__init__)
    params = list(sig.parameters.keys())



def test_analysis::scheduling::fsmcondition_is_not_abstract():
    assert not inspect.isabstract(analysis::scheduling::FSMCondition)


def test_analysis::scheduling::fsmcondition_constructor_exists():
    assert callable(analysis::scheduling::FSMCondition.__init__)


def test_analysis::scheduling::fsmcondition_constructor_args():
    sig = inspect.signature(analysis::scheduling::FSMCondition.__init__)
    params = list(sig.parameters.keys())
    assert "compval" in params, "Missing parameter 'compval'"
    assert "valName" in params, "Missing parameter 'valName'"
    assert "comp" in params, "Missing parameter 'comp'"

def test_analysis::scheduling::fsmcondition_has_compval():
    assert hasattr(analysis::scheduling::FSMCondition, "compval")
    descriptor = None
    for klass in analysis::scheduling::FSMCondition.__mro__:
        if "compval" in klass.__dict__:
            descriptor = klass.__dict__["compval"]
            break
    assert isinstance(descriptor, property)

def test_analysis::scheduling::fsmcondition_has_valName():
    assert hasattr(analysis::scheduling::FSMCondition, "valName")
    descriptor = None
    for klass in analysis::scheduling::FSMCondition.__mro__:
        if "valName" in klass.__dict__:
            descriptor = klass.__dict__["valName"]
            break
    assert isinstance(descriptor, property)

def test_analysis::scheduling::fsmcondition_has_comp():
    assert hasattr(analysis::scheduling::FSMCondition, "comp")
    descriptor = None
    for klass in analysis::scheduling::FSMCondition.__mro__:
        if "comp" in klass.__dict__:
            descriptor = klass.__dict__["comp"]
            break
    assert isinstance(descriptor, property)



def test_analysis::scheduling::fsmcombination_is_not_abstract():
    assert not inspect.isabstract(analysis::scheduling::FSMCombination)


def test_analysis::scheduling::fsmcombination_constructor_exists():
    assert callable(analysis::scheduling::FSMCombination.__init__)


def test_analysis::scheduling::fsmcombination_constructor_args():
    sig = inspect.signature(analysis::scheduling::FSMCombination.__init__)
    params = list(sig.parameters.keys())
    assert "combinator" in params, "Missing parameter 'combinator'"

def test_analysis::scheduling::fsmcombination_has_combinator():
    assert hasattr(analysis::scheduling::FSMCombination, "combinator")
    descriptor = None
    for klass in analysis::scheduling::FSMCombination.__mro__:
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



def test_analysis::scheduling::fsmoperation_is_not_abstract():
    assert not inspect.isabstract(analysis::scheduling::FSMOperation)


def test_analysis::scheduling::fsmoperation_constructor_exists():
    assert callable(analysis::scheduling::FSMOperation.__init__)


def test_analysis::scheduling::fsmoperation_constructor_args():
    sig = inspect.signature(analysis::scheduling::FSMOperation.__init__)
    params = list(sig.parameters.keys())
    assert "var" in params, "Missing parameter 'var'"
    assert "val" in params, "Missing parameter 'val'"
    assert "op" in params, "Missing parameter 'op'"

def test_analysis::scheduling::fsmoperation_has_var():
    assert hasattr(analysis::scheduling::FSMOperation, "var")
    descriptor = None
    for klass in analysis::scheduling::FSMOperation.__mro__:
        if "var" in klass.__dict__:
            descriptor = klass.__dict__["var"]
            break
    assert isinstance(descriptor, property)

def test_analysis::scheduling::fsmoperation_has_val():
    assert hasattr(analysis::scheduling::FSMOperation, "val")
    descriptor = None
    for klass in analysis::scheduling::FSMOperation.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)

def test_analysis::scheduling::fsmoperation_has_op():
    assert hasattr(analysis::scheduling::FSMOperation, "op")
    descriptor = None
    for klass in analysis::scheduling::FSMOperation.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_fsmoperation_is_not_abstract():
    assert not inspect.isabstract(FSMOperation)


def test_fsmoperation_constructor_exists():
    assert callable(FSMOperation.__init__)


def test_fsmoperation_constructor_args():
    sig = inspect.signature(FSMOperation.__init__)
    params = list(sig.parameters.keys())



def test_analysis::scheduling::fsmvarupdate_is_not_abstract():
    assert not inspect.isabstract(analysis::scheduling::FSMVarUpdate)


def test_analysis::scheduling::fsmvarupdate_constructor_exists():
    assert callable(analysis::scheduling::FSMVarUpdate.__init__)


def test_analysis::scheduling::fsmvarupdate_constructor_args():
    sig = inspect.signature(analysis::scheduling::FSMVarUpdate.__init__)
    params = list(sig.parameters.keys())



def test_fsmtransition_is_not_abstract():
    assert not inspect.isabstract(FSMTransition)


def test_fsmtransition_constructor_exists():
    assert callable(FSMTransition.__init__)


def test_fsmtransition_constructor_args():
    sig = inspect.signature(FSMTransition.__init__)
    params = list(sig.parameters.keys())



def test_analysis::scheduling::fsmtransitionwithstate_is_not_abstract():
    assert not inspect.isabstract(analysis::scheduling::FSMTransitionWithState)


def test_analysis::scheduling::fsmtransitionwithstate_constructor_exists():
    assert callable(analysis::scheduling::FSMTransitionWithState.__init__)


def test_analysis::scheduling::fsmtransitionwithstate_constructor_args():
    sig = inspect.signature(analysis::scheduling::FSMTransitionWithState.__init__)
    params = list(sig.parameters.keys())



def test_fsmvarupdate_is_not_abstract():
    assert not inspect.isabstract(FSMVarUpdate)


def test_fsmvarupdate_constructor_exists():
    assert callable(FSMVarUpdate.__init__)


def test_fsmvarupdate_constructor_args():
    sig = inspect.signature(FSMVarUpdate.__init__)
    params = list(sig.parameters.keys())



def test_analysis::scheduling::fsmstate_is_not_abstract():
    assert not inspect.isabstract(analysis::scheduling::FSMState)


def test_analysis::scheduling::fsmstate_constructor_exists():
    assert callable(analysis::scheduling::FSMState.__init__)


def test_analysis::scheduling::fsmstate_constructor_args():
    sig = inspect.signature(analysis::scheduling::FSMState.__init__)
    params = list(sig.parameters.keys())
    assert "enumName" in params, "Missing parameter 'enumName'"

def test_analysis::scheduling::fsmstate_has_enumName():
    assert hasattr(analysis::scheduling::FSMState, "enumName")
    descriptor = None
    for klass in analysis::scheduling::FSMState.__mro__:
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



def test_analysis::scheduling::fsmtransition_is_not_abstract():
    assert not inspect.isabstract(analysis::scheduling::FSMTransition)


def test_analysis::scheduling::fsmtransition_constructor_exists():
    assert callable(analysis::scheduling::FSMTransition.__init__)


def test_analysis::scheduling::fsmtransition_constructor_args():
    sig = inspect.signature(analysis::scheduling::FSMTransition.__init__)
    params = list(sig.parameters.keys())
    assert "targetStateEnumName" in params, "Missing parameter 'targetStateEnumName'"
    assert "sourceStateEnumName" in params, "Missing parameter 'sourceStateEnumName'"

def test_analysis::scheduling::fsmtransition_has_targetStateEnumName():
    assert hasattr(analysis::scheduling::FSMTransition, "targetStateEnumName")
    descriptor = None
    for klass in analysis::scheduling::FSMTransition.__mro__:
        if "targetStateEnumName" in klass.__dict__:
            descriptor = klass.__dict__["targetStateEnumName"]
            break
    assert isinstance(descriptor, property)

def test_analysis::scheduling::fsmtransition_has_sourceStateEnumName():
    assert hasattr(analysis::scheduling::FSMTransition, "sourceStateEnumName")
    descriptor = None
    for klass in analysis::scheduling::FSMTransition.__mro__:
        if "sourceStateEnumName" in klass.__dict__:
            descriptor = klass.__dict__["sourceStateEnumName"]
            break
    assert isinstance(descriptor, property)



def test_analysis::scheduling::fsmvar_is_not_abstract():
    assert not inspect.isabstract(analysis::scheduling::FSMVar)


def test_analysis::scheduling::fsmvar_constructor_exists():
    assert callable(analysis::scheduling::FSMVar.__init__)


def test_analysis::scheduling::fsmvar_constructor_args():
    sig = inspect.signature(analysis::scheduling::FSMVar.__init__)
    params = list(sig.parameters.keys())
    assert "initialVal" in params, "Missing parameter 'initialVal'"
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_analysis::scheduling::fsmvar_has_initialVal():
    assert hasattr(analysis::scheduling::FSMVar, "initialVal")
    descriptor = None
    for klass in analysis::scheduling::FSMVar.__mro__:
        if "initialVal" in klass.__dict__:
            descriptor = klass.__dict__["initialVal"]
            break
    assert isinstance(descriptor, property)

def test_analysis::scheduling::fsmvar_has_type():
    assert hasattr(analysis::scheduling::FSMVar, "type")
    descriptor = None
    for klass in analysis::scheduling::FSMVar.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_analysis::scheduling::fsmvar_has_name():
    assert hasattr(analysis::scheduling::FSMVar, "name")
    descriptor = None
    for klass in analysis::scheduling::FSMVar.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_actorfire_is_not_abstract():
    assert not inspect.isabstract(ActorFire)


def test_actorfire_constructor_exists():
    assert callable(ActorFire.__init__)


def test_actorfire_constructor_args():
    sig = inspect.signature(ActorFire.__init__)
    params = list(sig.parameters.keys())



def test_analysis::scheduling::partitionedactorfire_is_not_abstract():
    assert not inspect.isabstract(analysis::scheduling::PartitionedActorFire)


def test_analysis::scheduling::partitionedactorfire_constructor_exists():
    assert callable(analysis::scheduling::PartitionedActorFire.__init__)


def test_analysis::scheduling::partitionedactorfire_constructor_args():
    sig = inspect.signature(analysis::scheduling::PartitionedActorFire.__init__)
    params = list(sig.parameters.keys())



def test_analysis::scheduling::actorselectionschedule_is_not_abstract():
    assert not inspect.isabstract(analysis::scheduling::ActorSelectionSchedule)


def test_analysis::scheduling::actorselectionschedule_constructor_exists():
    assert callable(analysis::scheduling::ActorSelectionSchedule.__init__)


def test_analysis::scheduling::actorselectionschedule_constructor_args():
    sig = inspect.signature(analysis::scheduling::ActorSelectionSchedule.__init__)
    params = list(sig.parameters.keys())



def test_profiling::analysis::actor_is_not_abstract():
    assert not inspect.isabstract(profiling::analysis::Actor)


def test_profiling::analysis::actor_constructor_exists():
    assert callable(profiling::analysis::Actor.__init__)


def test_profiling::analysis::actor_constructor_args():
    sig = inspect.signature(profiling::analysis::Actor.__init__)
    params = list(sig.parameters.keys())



def test_analysis::profiling::intraactorcommunicationdata_is_not_abstract():
    assert not inspect.isabstract(analysis::profiling::IntraActorCommunicationData)


def test_analysis::profiling::intraactorcommunicationdata_constructor_exists():
    assert callable(analysis::profiling::IntraActorCommunicationData.__init__)


def test_analysis::profiling::intraactorcommunicationdata_constructor_args():
    sig = inspect.signature(analysis::profiling::IntraActorCommunicationData.__init__)
    params = list(sig.parameters.keys())



def test_fsmstate_is_not_abstract():
    assert not inspect.isabstract(FSMState)


def test_fsmstate_constructor_exists():
    assert callable(FSMState.__init__)


def test_fsmstate_constructor_args():
    sig = inspect.signature(FSMState.__init__)
    params = list(sig.parameters.keys())



def test_analysis::profiling::profilingstatsactordata_is_not_abstract():
    assert not inspect.isabstract(analysis::profiling::ProfilingStatsActorData)


def test_analysis::profiling::profilingstatsactordata_constructor_exists():
    assert callable(analysis::profiling::ProfilingStatsActorData.__init__)


def test_analysis::profiling::profilingstatsactordata_constructor_args():
    sig = inspect.signature(analysis::profiling::ProfilingStatsActorData.__init__)
    params = list(sig.parameters.keys())
    assert "actorName" in params, "Missing parameter 'actorName'"
    assert "actionsWeightPercent" in params, "Missing parameter 'actionsWeightPercent'"
    assert "schedulerWeightPercent" in params, "Missing parameter 'schedulerWeightPercent'"
    assert "schedulerWeight" in params, "Missing parameter 'schedulerWeight'"
    assert "actionsWeight" in params, "Missing parameter 'actionsWeight'"

def test_analysis::profiling::profilingstatsactordata_has_actorName():
    assert hasattr(analysis::profiling::ProfilingStatsActorData, "actorName")
    descriptor = None
    for klass in analysis::profiling::ProfilingStatsActorData.__mro__:
        if "actorName" in klass.__dict__:
            descriptor = klass.__dict__["actorName"]
            break
    assert isinstance(descriptor, property)

def test_analysis::profiling::profilingstatsactordata_has_actionsWeightPercent():
    assert hasattr(analysis::profiling::ProfilingStatsActorData, "actionsWeightPercent")
    descriptor = None
    for klass in analysis::profiling::ProfilingStatsActorData.__mro__:
        if "actionsWeightPercent" in klass.__dict__:
            descriptor = klass.__dict__["actionsWeightPercent"]
            break
    assert isinstance(descriptor, property)

def test_analysis::profiling::profilingstatsactordata_has_schedulerWeightPercent():
    assert hasattr(analysis::profiling::ProfilingStatsActorData, "schedulerWeightPercent")
    descriptor = None
    for klass in analysis::profiling::ProfilingStatsActorData.__mro__:
        if "schedulerWeightPercent" in klass.__dict__:
            descriptor = klass.__dict__["schedulerWeightPercent"]
            break
    assert isinstance(descriptor, property)

def test_analysis::profiling::profilingstatsactordata_has_schedulerWeight():
    assert hasattr(analysis::profiling::ProfilingStatsActorData, "schedulerWeight")
    descriptor = None
    for klass in analysis::profiling::ProfilingStatsActorData.__mro__:
        if "schedulerWeight" in klass.__dict__:
            descriptor = klass.__dict__["schedulerWeight"]
            break
    assert isinstance(descriptor, property)

def test_analysis::profiling::profilingstatsactordata_has_actionsWeight():
    assert hasattr(analysis::profiling::ProfilingStatsActorData, "actionsWeight")
    descriptor = None
    for klass in analysis::profiling::ProfilingStatsActorData.__mro__:
        if "actionsWeight" in klass.__dict__:
            descriptor = klass.__dict__["actionsWeight"]
            break
    assert isinstance(descriptor, property)



def test_profilingstatsactordata_is_not_abstract():
    assert not inspect.isabstract(ProfilingStatsActorData)


def test_profilingstatsactordata_constructor_exists():
    assert callable(ProfilingStatsActorData.__init__)


def test_profilingstatsactordata_constructor_args():
    sig = inspect.signature(ProfilingStatsActorData.__init__)
    params = list(sig.parameters.keys())



def test_profiling::analysis::action_is_not_abstract():
    assert not inspect.isabstract(profiling::analysis::Action)


def test_profiling::analysis::action_constructor_exists():
    assert callable(profiling::analysis::Action.__init__)


def test_profiling::analysis::action_constructor_args():
    sig = inspect.signature(profiling::analysis::Action.__init__)
    params = list(sig.parameters.keys())



def test_analysis::profiling::intraactioncommunicationdata_is_not_abstract():
    assert not inspect.isabstract(analysis::profiling::IntraActionCommunicationData)


def test_analysis::profiling::intraactioncommunicationdata_constructor_exists():
    assert callable(analysis::profiling::IntraActionCommunicationData.__init__)


def test_analysis::profiling::intraactioncommunicationdata_constructor_args():
    sig = inspect.signature(analysis::profiling::IntraActionCommunicationData.__init__)
    params = list(sig.parameters.keys())



def test_intraactioncommunicationdata_is_not_abstract():
    assert not inspect.isabstract(IntraActionCommunicationData)


def test_intraactioncommunicationdata_constructor_exists():
    assert callable(IntraActionCommunicationData.__init__)


def test_intraactioncommunicationdata_constructor_args():
    sig = inspect.signature(IntraActionCommunicationData.__init__)
    params = list(sig.parameters.keys())



def test_profiling::analysis::statisticaldata_is_not_abstract():
    assert not inspect.isabstract(profiling::analysis::StatisticalData)


def test_profiling::analysis::statisticaldata_constructor_exists():
    assert callable(profiling::analysis::StatisticalData.__init__)


def test_profiling::analysis::statisticaldata_constructor_args():
    sig = inspect.signature(profiling::analysis::StatisticalData.__init__)
    params = list(sig.parameters.keys())



def test_profiling::analysis::network_is_not_abstract():
    assert not inspect.isabstract(profiling::analysis::Network)


def test_profiling::analysis::network_constructor_exists():
    assert callable(profiling::analysis::Network.__init__)


def test_profiling::analysis::network_constructor_args():
    sig = inspect.signature(profiling::analysis::Network.__init__)
    params = list(sig.parameters.keys())



def test_intraactorcommunicationdata_is_not_abstract():
    assert not inspect.isabstract(IntraActorCommunicationData)


def test_intraactorcommunicationdata_constructor_exists():
    assert callable(IntraActorCommunicationData.__init__)


def test_intraactorcommunicationdata_constructor_args():
    sig = inspect.signature(IntraActorCommunicationData.__init__)
    params = list(sig.parameters.keys())



def test_actortostatisticaldatamap_is_not_abstract():
    assert not inspect.isabstract(ActorToStatisticalDataMap)


def test_actortostatisticaldatamap_constructor_exists():
    assert callable(ActorToStatisticalDataMap.__init__)


def test_actortostatisticaldatamap_constructor_args():
    sig = inspect.signature(ActorToStatisticalDataMap.__init__)
    params = list(sig.parameters.keys())



def test_postprocessing::analysis::statisticaldata_is_not_abstract():
    assert not inspect.isabstract(postprocessing::analysis::StatisticalData)


def test_postprocessing::analysis::statisticaldata_constructor_exists():
    assert callable(postprocessing::analysis::StatisticalData.__init__)


def test_postprocessing::analysis::statisticaldata_constructor_args():
    sig = inspect.signature(postprocessing::analysis::StatisticalData.__init__)
    params = list(sig.parameters.keys())



def test_analysis::postprocessing::schedulercheckspartition_is_not_abstract():
    assert not inspect.isabstract(analysis::postprocessing::SchedulerChecksPartition)


def test_analysis::postprocessing::schedulercheckspartition_constructor_exists():
    assert callable(analysis::postprocessing::SchedulerChecksPartition.__init__)


def test_analysis::postprocessing::schedulercheckspartition_constructor_args():
    sig = inspect.signature(analysis::postprocessing::SchedulerChecksPartition.__init__)
    params = list(sig.parameters.keys())



def test_schedulercheckspartition_is_not_abstract():
    assert not inspect.isabstract(SchedulerChecksPartition)


def test_schedulercheckspartition_constructor_exists():
    assert callable(SchedulerChecksPartition.__init__)


def test_schedulercheckspartition_constructor_args():
    sig = inspect.signature(SchedulerChecksPartition.__init__)
    params = list(sig.parameters.keys())



def test_pipelining::analysis::actorclass_is_not_abstract():
    assert not inspect.isabstract(pipelining::analysis::ActorClass)


def test_pipelining::analysis::actorclass_constructor_exists():
    assert callable(pipelining::analysis::ActorClass.__init__)


def test_pipelining::analysis::actorclass_constructor_args():
    sig = inspect.signature(pipelining::analysis::ActorClass.__init__)
    params = list(sig.parameters.keys())



def test_actiontodoublemap_is_not_abstract():
    assert not inspect.isabstract(ActionToDoubleMap)


def test_actiontodoublemap_constructor_exists():
    assert callable(ActionToDoubleMap.__init__)


def test_actiontodoublemap_constructor_args():
    sig = inspect.signature(ActionToDoubleMap.__init__)
    params = list(sig.parameters.keys())



def test_postprocessing::analysis::actor_is_not_abstract():
    assert not inspect.isabstract(postprocessing::analysis::Actor)


def test_postprocessing::analysis::actor_constructor_exists():
    assert callable(postprocessing::analysis::Actor.__init__)


def test_postprocessing::analysis::actor_constructor_args():
    sig = inspect.signature(postprocessing::analysis::Actor.__init__)
    params = list(sig.parameters.keys())



def test_analysis::postprocessing::statisticalactorpartition_is_not_abstract():
    assert not inspect.isabstract(analysis::postprocessing::StatisticalActorPartition)


def test_analysis::postprocessing::statisticalactorpartition_constructor_exists():
    assert callable(analysis::postprocessing::StatisticalActorPartition.__init__)


def test_analysis::postprocessing::statisticalactorpartition_constructor_args():
    sig = inspect.signature(analysis::postprocessing::StatisticalActorPartition.__init__)
    params = list(sig.parameters.keys())
    assert "actors" in params, "Missing parameter 'actors'"
    assert "schedulingPolicy" in params, "Missing parameter 'schedulingPolicy'"
    assert "occupancy" in params, "Missing parameter 'occupancy'"

def test_analysis::postprocessing::statisticalactorpartition_has_actors():
    assert hasattr(analysis::postprocessing::StatisticalActorPartition, "actors")
    descriptor = None
    for klass in analysis::postprocessing::StatisticalActorPartition.__mro__:
        if "actors" in klass.__dict__:
            descriptor = klass.__dict__["actors"]
            break
    assert isinstance(descriptor, property)

def test_analysis::postprocessing::statisticalactorpartition_has_schedulingPolicy():
    assert hasattr(analysis::postprocessing::StatisticalActorPartition, "schedulingPolicy")
    descriptor = None
    for klass in analysis::postprocessing::StatisticalActorPartition.__mro__:
        if "schedulingPolicy" in klass.__dict__:
            descriptor = klass.__dict__["schedulingPolicy"]
            break
    assert isinstance(descriptor, property)

def test_analysis::postprocessing::statisticalactorpartition_has_occupancy():
    assert hasattr(analysis::postprocessing::StatisticalActorPartition, "occupancy")
    descriptor = None
    for klass in analysis::postprocessing::StatisticalActorPartition.__mro__:
        if "occupancy" in klass.__dict__:
            descriptor = klass.__dict__["occupancy"]
            break
    assert isinstance(descriptor, property)



def test_statisticalactorpartition_is_not_abstract():
    assert not inspect.isabstract(StatisticalActorPartition)


def test_statisticalactorpartition_constructor_exists():
    assert callable(StatisticalActorPartition.__init__)


def test_statisticalactorpartition_constructor_args():
    sig = inspect.signature(StatisticalActorPartition.__init__)
    params = list(sig.parameters.keys())



def test_analysis::postprocessing::postprocessingdata_is_not_abstract():
    assert not inspect.isabstract(analysis::postprocessing::PostProcessingData)


def test_analysis::postprocessing::postprocessingdata_constructor_exists():
    assert callable(analysis::postprocessing::PostProcessingData.__init__)


def test_analysis::postprocessing::postprocessingdata_constructor_args():
    sig = inspect.signature(analysis::postprocessing::PostProcessingData.__init__)
    params = list(sig.parameters.keys())



def test_postprocessingdata_is_not_abstract():
    assert not inspect.isabstract(PostProcessingData)


def test_postprocessingdata_constructor_exists():
    assert callable(PostProcessingData.__init__)


def test_postprocessingdata_constructor_args():
    sig = inspect.signature(PostProcessingData.__init__)
    params = list(sig.parameters.keys())



def test_analysis::postprocessing::bufferblockingreport_is_not_abstract():
    assert not inspect.isabstract(analysis::postprocessing::BufferBlockingReport)


def test_analysis::postprocessing::bufferblockingreport_constructor_exists():
    assert callable(analysis::postprocessing::BufferBlockingReport.__init__)


def test_analysis::postprocessing::bufferblockingreport_constructor_args():
    sig = inspect.signature(analysis::postprocessing::BufferBlockingReport.__init__)
    params = list(sig.parameters.keys())



def test_analysis::postprocessing::schedulerchecksreport_is_not_abstract():
    assert not inspect.isabstract(analysis::postprocessing::SchedulerChecksReport)


def test_analysis::postprocessing::schedulerchecksreport_constructor_exists():
    assert callable(analysis::postprocessing::SchedulerChecksReport.__init__)


def test_analysis::postprocessing::schedulerchecksreport_constructor_args():
    sig = inspect.signature(analysis::postprocessing::SchedulerChecksReport.__init__)
    params = list(sig.parameters.keys())



def test_analysis::postprocessing::actorstatisticsreport_is_not_abstract():
    assert not inspect.isabstract(analysis::postprocessing::ActorStatisticsReport)


def test_analysis::postprocessing::actorstatisticsreport_constructor_exists():
    assert callable(analysis::postprocessing::ActorStatisticsReport.__init__)


def test_analysis::postprocessing::actorstatisticsreport_constructor_args():
    sig = inspect.signature(analysis::postprocessing::ActorStatisticsReport.__init__)
    params = list(sig.parameters.keys())
    assert "averageOccupancy" in params, "Missing parameter 'averageOccupancy'"
    assert "occupancyDeviation" in params, "Missing parameter 'occupancyDeviation'"
    assert "executionTime" in params, "Missing parameter 'executionTime'"

def test_analysis::postprocessing::actorstatisticsreport_has_averageOccupancy():
    assert hasattr(analysis::postprocessing::ActorStatisticsReport, "averageOccupancy")
    descriptor = None
    for klass in analysis::postprocessing::ActorStatisticsReport.__mro__:
        if "averageOccupancy" in klass.__dict__:
            descriptor = klass.__dict__["averageOccupancy"]
            break
    assert isinstance(descriptor, property)

def test_analysis::postprocessing::actorstatisticsreport_has_occupancyDeviation():
    assert hasattr(analysis::postprocessing::ActorStatisticsReport, "occupancyDeviation")
    descriptor = None
    for klass in analysis::postprocessing::ActorStatisticsReport.__mro__:
        if "occupancyDeviation" in klass.__dict__:
            descriptor = klass.__dict__["occupancyDeviation"]
            break
    assert isinstance(descriptor, property)

def test_analysis::postprocessing::actorstatisticsreport_has_executionTime():
    assert hasattr(analysis::postprocessing::ActorStatisticsReport, "executionTime")
    descriptor = None
    for klass in analysis::postprocessing::ActorStatisticsReport.__mro__:
        if "executionTime" in klass.__dict__:
            descriptor = klass.__dict__["executionTime"]
            break
    assert isinstance(descriptor, property)



def test_analysis::postprocessing::actionstatisticsreport_is_not_abstract():
    assert not inspect.isabstract(analysis::postprocessing::ActionStatisticsReport)


def test_analysis::postprocessing::actionstatisticsreport_constructor_exists():
    assert callable(analysis::postprocessing::ActionStatisticsReport.__init__)


def test_analysis::postprocessing::actionstatisticsreport_constructor_args():
    sig = inspect.signature(analysis::postprocessing::ActionStatisticsReport.__init__)
    params = list(sig.parameters.keys())



def test_postprocessing::analysis::network_is_not_abstract():
    assert not inspect.isabstract(postprocessing::analysis::Network)


def test_postprocessing::analysis::network_constructor_exists():
    assert callable(postprocessing::analysis::Network.__init__)


def test_postprocessing::analysis::network_constructor_args():
    sig = inspect.signature(postprocessing::analysis::Network.__init__)
    params = list(sig.parameters.keys())



def test_analysis::pipelining::impactanalysisdata_is_not_abstract():
    assert not inspect.isabstract(analysis::pipelining::ImpactAnalysisData)


def test_analysis::pipelining::impactanalysisdata_constructor_exists():
    assert callable(analysis::pipelining::ImpactAnalysisData.__init__)


def test_analysis::pipelining::impactanalysisdata_constructor_args():
    sig = inspect.signature(analysis::pipelining::ImpactAnalysisData.__init__)
    params = list(sig.parameters.keys())
    assert "cpReduction" in params, "Missing parameter 'cpReduction'"

def test_analysis::pipelining::impactanalysisdata_has_cpReduction():
    assert hasattr(analysis::pipelining::ImpactAnalysisData, "cpReduction")
    descriptor = None
    for klass in analysis::pipelining::ImpactAnalysisData.__mro__:
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



def test_pipelining::analysis::statisticaldata_is_not_abstract():
    assert not inspect.isabstract(pipelining::analysis::StatisticalData)


def test_pipelining::analysis::statisticaldata_constructor_exists():
    assert callable(pipelining::analysis::StatisticalData.__init__)


def test_pipelining::analysis::statisticaldata_constructor_args():
    sig = inspect.signature(pipelining::analysis::StatisticalData.__init__)
    params = list(sig.parameters.keys())



def test_pipelining::analysis::action_is_not_abstract():
    assert not inspect.isabstract(pipelining::analysis::Action)


def test_pipelining::analysis::action_constructor_exists():
    assert callable(pipelining::analysis::Action.__init__)


def test_pipelining::analysis::action_constructor_args():
    sig = inspect.signature(pipelining::analysis::Action.__init__)
    params = list(sig.parameters.keys())



def test_analysis::pipelining::actionvariablepipeliningdata_is_not_abstract():
    assert not inspect.isabstract(analysis::pipelining::ActionVariablePipeliningData)


def test_analysis::pipelining::actionvariablepipeliningdata_constructor_exists():
    assert callable(analysis::pipelining::ActionVariablePipeliningData.__init__)


def test_analysis::pipelining::actionvariablepipeliningdata_constructor_args():
    sig = inspect.signature(analysis::pipelining::ActionVariablePipeliningData.__init__)
    params = list(sig.parameters.keys())
    assert "pipelinable" in params, "Missing parameter 'pipelinable'"

def test_analysis::pipelining::actionvariablepipeliningdata_has_pipelinable():
    assert hasattr(analysis::pipelining::ActionVariablePipeliningData, "pipelinable")
    descriptor = None
    for klass in analysis::pipelining::ActionVariablePipeliningData.__mro__:
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



def test_pipelining::analysis::network_is_not_abstract():
    assert not inspect.isabstract(pipelining::analysis::Network)


def test_pipelining::analysis::network_constructor_exists():
    assert callable(pipelining::analysis::Network.__init__)


def test_pipelining::analysis::network_constructor_args():
    sig = inspect.signature(pipelining::analysis::Network.__init__)
    params = list(sig.parameters.keys())



def test_balancedpipelinepartition_is_not_abstract():
    assert not inspect.isabstract(BalancedPipelinePartition)


def test_balancedpipelinepartition_constructor_exists():
    assert callable(BalancedPipelinePartition.__init__)


def test_balancedpipelinepartition_constructor_args():
    sig = inspect.signature(BalancedPipelinePartition.__init__)
    params = list(sig.parameters.keys())



def test_partitioning::analysis::actor_is_not_abstract():
    assert not inspect.isabstract(partitioning::analysis::Actor)


def test_partitioning::analysis::actor_constructor_exists():
    assert callable(partitioning::analysis::Actor.__init__)


def test_partitioning::analysis::actor_constructor_args():
    sig = inspect.signature(partitioning::analysis::Actor.__init__)
    params = list(sig.parameters.keys())



def test_analysis::partitioning::comcostpartition_is_not_abstract():
    assert not inspect.isabstract(analysis::partitioning::ComCostPartition)


def test_analysis::partitioning::comcostpartition_constructor_exists():
    assert callable(analysis::partitioning::ComCostPartition.__init__)


def test_analysis::partitioning::comcostpartition_constructor_args():
    sig = inspect.signature(analysis::partitioning::ComCostPartition.__init__)
    params = list(sig.parameters.keys())
    assert "internalCost" in params, "Missing parameter 'internalCost'"
    assert "externalCost" in params, "Missing parameter 'externalCost'"

def test_analysis::partitioning::comcostpartition_has_internalCost():
    assert hasattr(analysis::partitioning::ComCostPartition, "internalCost")
    descriptor = None
    for klass in analysis::partitioning::ComCostPartition.__mro__:
        if "internalCost" in klass.__dict__:
            descriptor = klass.__dict__["internalCost"]
            break
    assert isinstance(descriptor, property)

def test_analysis::partitioning::comcostpartition_has_externalCost():
    assert hasattr(analysis::partitioning::ComCostPartition, "externalCost")
    descriptor = None
    for klass in analysis::partitioning::ComCostPartition.__mro__:
        if "externalCost" in klass.__dict__:
            descriptor = klass.__dict__["externalCost"]
            break
    assert isinstance(descriptor, property)



def test_actiontostatisticaldatamap_is_not_abstract():
    assert not inspect.isabstract(ActionToStatisticalDataMap)


def test_actiontostatisticaldatamap_constructor_exists():
    assert callable(ActionToStatisticalDataMap.__init__)


def test_actiontostatisticaldatamap_constructor_args():
    sig = inspect.signature(ActionToStatisticalDataMap.__init__)
    params = list(sig.parameters.keys())



def test_profiler::analysis::statisticaldata_is_not_abstract():
    assert not inspect.isabstract(profiler::analysis::StatisticalData)


def test_profiler::analysis::statisticaldata_constructor_exists():
    assert callable(profiler::analysis::StatisticalData.__init__)


def test_profiler::analysis::statisticaldata_constructor_args():
    sig = inspect.signature(profiler::analysis::StatisticalData.__init__)
    params = list(sig.parameters.keys())



def test_profiler::analysis::buffer_is_not_abstract():
    assert not inspect.isabstract(profiler::analysis::Buffer)


def test_profiler::analysis::buffer_constructor_exists():
    assert callable(profiler::analysis::Buffer.__init__)


def test_profiler::analysis::buffer_constructor_args():
    sig = inspect.signature(profiler::analysis::Buffer.__init__)
    params = list(sig.parameters.keys())



def test_analysis::profiler::bufferdynamicdata_is_not_abstract():
    assert not inspect.isabstract(analysis::profiler::BufferDynamicData)


def test_analysis::profiler::bufferdynamicdata_constructor_exists():
    assert callable(analysis::profiler::BufferDynamicData.__init__)


def test_analysis::profiler::bufferdynamicdata_constructor_args():
    sig = inspect.signature(analysis::profiler::BufferDynamicData.__init__)
    params = list(sig.parameters.keys())
    assert "unconsumedTokens" in params, "Missing parameter 'unconsumedTokens'"

def test_analysis::profiler::bufferdynamicdata_has_unconsumedTokens():
    assert hasattr(analysis::profiler::BufferDynamicData, "unconsumedTokens")
    descriptor = None
    for klass in analysis::profiler::BufferDynamicData.__mro__:
        if "unconsumedTokens" in klass.__dict__:
            descriptor = klass.__dict__["unconsumedTokens"]
            break
    assert isinstance(descriptor, property)



def test_profiler::analysis::action_is_not_abstract():
    assert not inspect.isabstract(profiler::analysis::Action)


def test_profiler::analysis::action_constructor_exists():
    assert callable(profiler::analysis::Action.__init__)


def test_profiler::analysis::action_constructor_args():
    sig = inspect.signature(profiler::analysis::Action.__init__)
    params = list(sig.parameters.keys())



def test_profiler::analysis::actor_is_not_abstract():
    assert not inspect.isabstract(profiler::analysis::Actor)


def test_profiler::analysis::actor_constructor_exists():
    assert callable(profiler::analysis::Actor.__init__)


def test_profiler::analysis::actor_constructor_args():
    sig = inspect.signature(profiler::analysis::Actor.__init__)
    params = list(sig.parameters.keys())



def test_complexdynamicdata_is_not_abstract():
    assert not inspect.isabstract(ComplexDynamicData)


def test_complexdynamicdata_constructor_exists():
    assert callable(ComplexDynamicData.__init__)


def test_complexdynamicdata_constructor_args():
    sig = inspect.signature(ComplexDynamicData.__init__)
    params = list(sig.parameters.keys())



def test_analysis::profiler::actiondynamicdata_is_not_abstract():
    assert not inspect.isabstract(analysis::profiler::ActionDynamicData)


def test_analysis::profiler::actiondynamicdata_constructor_exists():
    assert callable(analysis::profiler::ActionDynamicData.__init__)


def test_analysis::profiler::actiondynamicdata_constructor_args():
    sig = inspect.signature(analysis::profiler::ActionDynamicData.__init__)
    params = list(sig.parameters.keys())



def test_analysis::profiler::actordynamicdata_is_not_abstract():
    assert not inspect.isabstract(analysis::profiler::ActorDynamicData)


def test_analysis::profiler::actordynamicdata_constructor_exists():
    assert callable(analysis::profiler::ActorDynamicData.__init__)


def test_analysis::profiler::actordynamicdata_constructor_args():
    sig = inspect.signature(analysis::profiler::ActorDynamicData.__init__)
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



def test_analysis::profiler::complexcodedata_is_not_abstract():
    assert not inspect.isabstract(analysis::profiler::ComplexCodeData)


def test_analysis::profiler::complexcodedata_constructor_exists():
    assert callable(analysis::profiler::ComplexCodeData.__init__)


def test_analysis::profiler::complexcodedata_constructor_args():
    sig = inspect.signature(analysis::profiler::ComplexCodeData.__init__)
    params = list(sig.parameters.keys())



def test_stringtointegermap_is_not_abstract():
    assert not inspect.isabstract(StringToIntegerMap)


def test_stringtointegermap_constructor_exists():
    assert callable(StringToIntegerMap.__init__)


def test_stringtointegermap_constructor_args():
    sig = inspect.signature(StringToIntegerMap.__init__)
    params = list(sig.parameters.keys())



def test_analysis::profiler::codedata_is_not_abstract():
    assert not inspect.isabstract(analysis::profiler::CodeData)


def test_analysis::profiler::codedata_constructor_exists():
    assert callable(analysis::profiler::CodeData.__init__)


def test_analysis::profiler::codedata_constructor_args():
    sig = inspect.signature(analysis::profiler::CodeData.__init__)
    params = list(sig.parameters.keys())
    assert "nol" in params, "Missing parameter 'nol'"
    assert "blockName" in params, "Missing parameter 'blockName'"

def test_analysis::profiler::codedata_has_nol():
    assert hasattr(analysis::profiler::CodeData, "nol")
    descriptor = None
    for klass in analysis::profiler::CodeData.__mro__:
        if "nol" in klass.__dict__:
            descriptor = klass.__dict__["nol"]
            break
    assert isinstance(descriptor, property)

def test_analysis::profiler::codedata_has_blockName():
    assert hasattr(analysis::profiler::CodeData, "blockName")
    descriptor = None
    for klass in analysis::profiler::CodeData.__mro__:
        if "blockName" in klass.__dict__:
            descriptor = klass.__dict__["blockName"]
            break
    assert isinstance(descriptor, property)



def test_complexcodedata_is_not_abstract():
    assert not inspect.isabstract(ComplexCodeData)


def test_complexcodedata_constructor_exists():
    assert callable(ComplexCodeData.__init__)


def test_complexcodedata_constructor_args():
    sig = inspect.signature(ComplexCodeData.__init__)
    params = list(sig.parameters.keys())



def test_profiler::analysis::network_is_not_abstract():
    assert not inspect.isabstract(profiler::analysis::Network)


def test_profiler::analysis::network_constructor_exists():
    assert callable(profiler::analysis::Network.__init__)


def test_profiler::analysis::network_constructor_args():
    sig = inspect.signature(profiler::analysis::Network.__init__)
    params = list(sig.parameters.keys())



def test_analysisreport_is_not_abstract():
    assert not inspect.isabstract(AnalysisReport)


def test_analysisreport_constructor_exists():
    assert callable(AnalysisReport.__init__)


def test_analysisreport_constructor_args():
    sig = inspect.signature(AnalysisReport.__init__)
    params = list(sig.parameters.keys())



def test_analysis::partitioning::comcostpartitioningreport_is_not_abstract():
    assert not inspect.isabstract(analysis::partitioning::ComCostPartitioningReport)


def test_analysis::partitioning::comcostpartitioningreport_constructor_exists():
    assert callable(analysis::partitioning::ComCostPartitioningReport.__init__)


def test_analysis::partitioning::comcostpartitioningreport_constructor_args():
    sig = inspect.signature(analysis::partitioning::ComCostPartitioningReport.__init__)
    params = list(sig.parameters.keys())
    assert "bitAccurate" in params, "Missing parameter 'bitAccurate'"

def test_analysis::partitioning::comcostpartitioningreport_has_bitAccurate():
    assert hasattr(analysis::partitioning::ComCostPartitioningReport, "bitAccurate")
    descriptor = None
    for klass in analysis::partitioning::ComCostPartitioningReport.__mro__:
        if "bitAccurate" in klass.__dict__:
            descriptor = klass.__dict__["bitAccurate"]
            break
    assert isinstance(descriptor, property)



def test_analysis::buffers::boundedbuffersreport_is_not_abstract():
    assert not inspect.isabstract(analysis::buffers::BoundedBuffersReport)


def test_analysis::buffers::boundedbuffersreport_constructor_exists():
    assert callable(analysis::buffers::BoundedBuffersReport.__init__)


def test_analysis::buffers::boundedbuffersreport_constructor_args():
    sig = inspect.signature(analysis::buffers::BoundedBuffersReport.__init__)
    params = list(sig.parameters.keys())
    assert "bitSize" in params, "Missing parameter 'bitSize'"
    assert "pow2" in params, "Missing parameter 'pow2'"
    assert "bitAccurate" in params, "Missing parameter 'bitAccurate'"
    assert "tokenSize" in params, "Missing parameter 'tokenSize'"

def test_analysis::buffers::boundedbuffersreport_has_bitSize():
    assert hasattr(analysis::buffers::BoundedBuffersReport, "bitSize")
    descriptor = None
    for klass in analysis::buffers::BoundedBuffersReport.__mro__:
        if "bitSize" in klass.__dict__:
            descriptor = klass.__dict__["bitSize"]
            break
    assert isinstance(descriptor, property)

def test_analysis::buffers::boundedbuffersreport_has_pow2():
    assert hasattr(analysis::buffers::BoundedBuffersReport, "pow2")
    descriptor = None
    for klass in analysis::buffers::BoundedBuffersReport.__mro__:
        if "pow2" in klass.__dict__:
            descriptor = klass.__dict__["pow2"]
            break
    assert isinstance(descriptor, property)

def test_analysis::buffers::boundedbuffersreport_has_bitAccurate():
    assert hasattr(analysis::buffers::BoundedBuffersReport, "bitAccurate")
    descriptor = None
    for klass in analysis::buffers::BoundedBuffersReport.__mro__:
        if "bitAccurate" in klass.__dict__:
            descriptor = klass.__dict__["bitAccurate"]
            break
    assert isinstance(descriptor, property)

def test_analysis::buffers::boundedbuffersreport_has_tokenSize():
    assert hasattr(analysis::buffers::BoundedBuffersReport, "tokenSize")
    descriptor = None
    for klass in analysis::buffers::BoundedBuffersReport.__mro__:
        if "tokenSize" in klass.__dict__:
            descriptor = klass.__dict__["tokenSize"]
            break
    assert isinstance(descriptor, property)



def test_analysis::pipelining::actionsvariablepipeliningreport_is_not_abstract():
    assert not inspect.isabstract(analysis::pipelining::ActionsVariablePipeliningReport)


def test_analysis::pipelining::actionsvariablepipeliningreport_constructor_exists():
    assert callable(analysis::pipelining::ActionsVariablePipeliningReport.__init__)


def test_analysis::pipelining::actionsvariablepipeliningreport_constructor_args():
    sig = inspect.signature(analysis::pipelining::ActionsVariablePipeliningReport.__init__)
    params = list(sig.parameters.keys())



def test_analysis::bottlenecks::bottlenecksreport_is_not_abstract():
    assert not inspect.isabstract(analysis::bottlenecks::BottlenecksReport)


def test_analysis::bottlenecks::bottlenecksreport_constructor_exists():
    assert callable(analysis::bottlenecks::BottlenecksReport.__init__)


def test_analysis::bottlenecks::bottlenecksreport_constructor_args():
    sig = inspect.signature(analysis::bottlenecks::BottlenecksReport.__init__)
    params = list(sig.parameters.keys())
    assert "totalFirings" in params, "Missing parameter 'totalFirings'"
    assert "cpVariance" in params, "Missing parameter 'cpVariance'"
    assert "totalWeight" in params, "Missing parameter 'totalWeight'"
    assert "cpWeight" in params, "Missing parameter 'cpWeight'"
    assert "totalVariance" in params, "Missing parameter 'totalVariance'"
    assert "cpFirings" in params, "Missing parameter 'cpFirings'"

def test_analysis::bottlenecks::bottlenecksreport_has_totalFirings():
    assert hasattr(analysis::bottlenecks::BottlenecksReport, "totalFirings")
    descriptor = None
    for klass in analysis::bottlenecks::BottlenecksReport.__mro__:
        if "totalFirings" in klass.__dict__:
            descriptor = klass.__dict__["totalFirings"]
            break
    assert isinstance(descriptor, property)

def test_analysis::bottlenecks::bottlenecksreport_has_cpVariance():
    assert hasattr(analysis::bottlenecks::BottlenecksReport, "cpVariance")
    descriptor = None
    for klass in analysis::bottlenecks::BottlenecksReport.__mro__:
        if "cpVariance" in klass.__dict__:
            descriptor = klass.__dict__["cpVariance"]
            break
    assert isinstance(descriptor, property)

def test_analysis::bottlenecks::bottlenecksreport_has_totalWeight():
    assert hasattr(analysis::bottlenecks::BottlenecksReport, "totalWeight")
    descriptor = None
    for klass in analysis::bottlenecks::BottlenecksReport.__mro__:
        if "totalWeight" in klass.__dict__:
            descriptor = klass.__dict__["totalWeight"]
            break
    assert isinstance(descriptor, property)

def test_analysis::bottlenecks::bottlenecksreport_has_cpWeight():
    assert hasattr(analysis::bottlenecks::BottlenecksReport, "cpWeight")
    descriptor = None
    for klass in analysis::bottlenecks::BottlenecksReport.__mro__:
        if "cpWeight" in klass.__dict__:
            descriptor = klass.__dict__["cpWeight"]
            break
    assert isinstance(descriptor, property)

def test_analysis::bottlenecks::bottlenecksreport_has_totalVariance():
    assert hasattr(analysis::bottlenecks::BottlenecksReport, "totalVariance")
    descriptor = None
    for klass in analysis::bottlenecks::BottlenecksReport.__mro__:
        if "totalVariance" in klass.__dict__:
            descriptor = klass.__dict__["totalVariance"]
            break
    assert isinstance(descriptor, property)

def test_analysis::bottlenecks::bottlenecksreport_has_cpFirings():
    assert hasattr(analysis::bottlenecks::BottlenecksReport, "cpFirings")
    descriptor = None
    for klass in analysis::bottlenecks::BottlenecksReport.__mro__:
        if "cpFirings" in klass.__dict__:
            descriptor = klass.__dict__["cpFirings"]
            break
    assert isinstance(descriptor, property)



def test_analysis::profiler::dynamicprofilingreport_is_not_abstract():
    assert not inspect.isabstract(analysis::profiler::DynamicProfilingReport)


def test_analysis::profiler::dynamicprofilingreport_constructor_exists():
    assert callable(analysis::profiler::DynamicProfilingReport.__init__)


def test_analysis::profiler::dynamicprofilingreport_constructor_args():
    sig = inspect.signature(analysis::profiler::DynamicProfilingReport.__init__)
    params = list(sig.parameters.keys())



def test_analysis::bottlenecks::bottleneckswithschedulingreport_is_not_abstract():
    assert not inspect.isabstract(analysis::bottlenecks::BottlenecksWithSchedulingReport)


def test_analysis::bottlenecks::bottleneckswithschedulingreport_constructor_exists():
    assert callable(analysis::bottlenecks::BottlenecksWithSchedulingReport.__init__)


def test_analysis::bottlenecks::bottleneckswithschedulingreport_constructor_args():
    sig = inspect.signature(analysis::bottlenecks::BottlenecksWithSchedulingReport.__init__)
    params = list(sig.parameters.keys())
    assert "executionTime" in params, "Missing parameter 'executionTime'"
    assert "cpWeight" in params, "Missing parameter 'cpWeight'"
    assert "totalFirings" in params, "Missing parameter 'totalFirings'"
    assert "cpBlockingTime" in params, "Missing parameter 'cpBlockingTime'"
    assert "cpFirings" in params, "Missing parameter 'cpFirings'"
    assert "totalWeight" in params, "Missing parameter 'totalWeight'"

def test_analysis::bottlenecks::bottleneckswithschedulingreport_has_executionTime():
    assert hasattr(analysis::bottlenecks::BottlenecksWithSchedulingReport, "executionTime")
    descriptor = None
    for klass in analysis::bottlenecks::BottlenecksWithSchedulingReport.__mro__:
        if "executionTime" in klass.__dict__:
            descriptor = klass.__dict__["executionTime"]
            break
    assert isinstance(descriptor, property)

def test_analysis::bottlenecks::bottleneckswithschedulingreport_has_cpWeight():
    assert hasattr(analysis::bottlenecks::BottlenecksWithSchedulingReport, "cpWeight")
    descriptor = None
    for klass in analysis::bottlenecks::BottlenecksWithSchedulingReport.__mro__:
        if "cpWeight" in klass.__dict__:
            descriptor = klass.__dict__["cpWeight"]
            break
    assert isinstance(descriptor, property)

def test_analysis::bottlenecks::bottleneckswithschedulingreport_has_totalFirings():
    assert hasattr(analysis::bottlenecks::BottlenecksWithSchedulingReport, "totalFirings")
    descriptor = None
    for klass in analysis::bottlenecks::BottlenecksWithSchedulingReport.__mro__:
        if "totalFirings" in klass.__dict__:
            descriptor = klass.__dict__["totalFirings"]
            break
    assert isinstance(descriptor, property)

def test_analysis::bottlenecks::bottleneckswithschedulingreport_has_cpBlockingTime():
    assert hasattr(analysis::bottlenecks::BottlenecksWithSchedulingReport, "cpBlockingTime")
    descriptor = None
    for klass in analysis::bottlenecks::BottlenecksWithSchedulingReport.__mro__:
        if "cpBlockingTime" in klass.__dict__:
            descriptor = klass.__dict__["cpBlockingTime"]
            break
    assert isinstance(descriptor, property)

def test_analysis::bottlenecks::bottleneckswithschedulingreport_has_cpFirings():
    assert hasattr(analysis::bottlenecks::BottlenecksWithSchedulingReport, "cpFirings")
    descriptor = None
    for klass in analysis::bottlenecks::BottlenecksWithSchedulingReport.__mro__:
        if "cpFirings" in klass.__dict__:
            descriptor = klass.__dict__["cpFirings"]
            break
    assert isinstance(descriptor, property)

def test_analysis::bottlenecks::bottleneckswithschedulingreport_has_totalWeight():
    assert hasattr(analysis::bottlenecks::BottlenecksWithSchedulingReport, "totalWeight")
    descriptor = None
    for klass in analysis::bottlenecks::BottlenecksWithSchedulingReport.__mro__:
        if "totalWeight" in klass.__dict__:
            descriptor = klass.__dict__["totalWeight"]
            break
    assert isinstance(descriptor, property)



def test_analysis::scheduling::markovsimpleschedulerreport_is_not_abstract():
    assert not inspect.isabstract(analysis::scheduling::MarkovSimpleSchedulerReport)


def test_analysis::scheduling::markovsimpleschedulerreport_constructor_exists():
    assert callable(analysis::scheduling::MarkovSimpleSchedulerReport.__init__)


def test_analysis::scheduling::markovsimpleschedulerreport_constructor_args():
    sig = inspect.signature(analysis::scheduling::MarkovSimpleSchedulerReport.__init__)
    params = list(sig.parameters.keys())



def test_analysis::buffers::optimalbuffersreport_is_not_abstract():
    assert not inspect.isabstract(analysis::buffers::OptimalBuffersReport)


def test_analysis::buffers::optimalbuffersreport_constructor_exists():
    assert callable(analysis::buffers::OptimalBuffersReport.__init__)


def test_analysis::buffers::optimalbuffersreport_constructor_args():
    sig = inspect.signature(analysis::buffers::OptimalBuffersReport.__init__)
    params = list(sig.parameters.keys())
    assert "bitAccurate" in params, "Missing parameter 'bitAccurate'"
    assert "pow2" in params, "Missing parameter 'pow2'"

def test_analysis::buffers::optimalbuffersreport_has_bitAccurate():
    assert hasattr(analysis::buffers::OptimalBuffersReport, "bitAccurate")
    descriptor = None
    for klass in analysis::buffers::OptimalBuffersReport.__mro__:
        if "bitAccurate" in klass.__dict__:
            descriptor = klass.__dict__["bitAccurate"]
            break
    assert isinstance(descriptor, property)

def test_analysis::buffers::optimalbuffersreport_has_pow2():
    assert hasattr(analysis::buffers::OptimalBuffersReport, "pow2")
    descriptor = None
    for klass in analysis::buffers::OptimalBuffersReport.__mro__:
        if "pow2" in klass.__dict__:
            descriptor = klass.__dict__["pow2"]
            break
    assert isinstance(descriptor, property)



def test_analysis::profiling::profilingstatsreport_is_not_abstract():
    assert not inspect.isabstract(analysis::profiling::ProfilingStatsReport)


def test_analysis::profiling::profilingstatsreport_constructor_exists():
    assert callable(analysis::profiling::ProfilingStatsReport.__init__)


def test_analysis::profiling::profilingstatsreport_constructor_args():
    sig = inspect.signature(analysis::profiling::ProfilingStatsReport.__init__)
    params = list(sig.parameters.keys())
    assert "networkName" in params, "Missing parameter 'networkName'"

def test_analysis::profiling::profilingstatsreport_has_networkName():
    assert hasattr(analysis::profiling::ProfilingStatsReport, "networkName")
    descriptor = None
    for klass in analysis::profiling::ProfilingStatsReport.__mro__:
        if "networkName" in klass.__dict__:
            descriptor = klass.__dict__["networkName"]
            break
    assert isinstance(descriptor, property)



def test_analysis::trace::markowmodeltracereport_is_not_abstract():
    assert not inspect.isabstract(analysis::trace::MarkowModelTraceReport)


def test_analysis::trace::markowmodeltracereport_constructor_exists():
    assert callable(analysis::trace::MarkowModelTraceReport.__init__)


def test_analysis::trace::markowmodeltracereport_constructor_args():
    sig = inspect.signature(analysis::trace::MarkowModelTraceReport.__init__)
    params = list(sig.parameters.keys())



def test_analysis::partitioning::workloadbalancepartitioningreport_is_not_abstract():
    assert not inspect.isabstract(analysis::partitioning::WorkloadBalancePartitioningReport)


def test_analysis::partitioning::workloadbalancepartitioningreport_constructor_exists():
    assert callable(analysis::partitioning::WorkloadBalancePartitioningReport.__init__)


def test_analysis::partitioning::workloadbalancepartitioningreport_constructor_args():
    sig = inspect.signature(analysis::partitioning::WorkloadBalancePartitioningReport.__init__)
    params = list(sig.parameters.keys())



def test_analysis::postprocessing::postprocessingreport_is_not_abstract():
    assert not inspect.isabstract(analysis::postprocessing::PostProcessingReport)


def test_analysis::postprocessing::postprocessingreport_constructor_exists():
    assert callable(analysis::postprocessing::PostProcessingReport.__init__)


def test_analysis::postprocessing::postprocessingreport_constructor_args():
    sig = inspect.signature(analysis::postprocessing::PostProcessingReport.__init__)
    params = list(sig.parameters.keys())
    assert "deadlock" in params, "Missing parameter 'deadlock'"
    assert "time" in params, "Missing parameter 'time'"

def test_analysis::postprocessing::postprocessingreport_has_deadlock():
    assert hasattr(analysis::postprocessing::PostProcessingReport, "deadlock")
    descriptor = None
    for klass in analysis::postprocessing::PostProcessingReport.__mro__:
        if "deadlock" in klass.__dict__:
            descriptor = klass.__dict__["deadlock"]
            break
    assert isinstance(descriptor, property)

def test_analysis::postprocessing::postprocessingreport_has_time():
    assert hasattr(analysis::postprocessing::PostProcessingReport, "time")
    descriptor = None
    for klass in analysis::postprocessing::PostProcessingReport.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_analysis::bottlenecks::impactanalysisreport_is_not_abstract():
    assert not inspect.isabstract(analysis::bottlenecks::ImpactAnalysisReport)


def test_analysis::bottlenecks::impactanalysisreport_constructor_exists():
    assert callable(analysis::bottlenecks::ImpactAnalysisReport.__init__)


def test_analysis::bottlenecks::impactanalysisreport_constructor_args():
    sig = inspect.signature(analysis::bottlenecks::ImpactAnalysisReport.__init__)
    params = list(sig.parameters.keys())
    assert "classLevel" in params, "Missing parameter 'classLevel'"

def test_analysis::bottlenecks::impactanalysisreport_has_classLevel():
    assert hasattr(analysis::bottlenecks::ImpactAnalysisReport, "classLevel")
    descriptor = None
    for klass in analysis::bottlenecks::ImpactAnalysisReport.__mro__:
        if "classLevel" in klass.__dict__:
            descriptor = klass.__dict__["classLevel"]
            break
    assert isinstance(descriptor, property)



def test_analysis::pipelining::impactanalysisreport_is_not_abstract():
    assert not inspect.isabstract(analysis::pipelining::ImpactAnalysisReport)


def test_analysis::pipelining::impactanalysisreport_constructor_exists():
    assert callable(analysis::pipelining::ImpactAnalysisReport.__init__)


def test_analysis::pipelining::impactanalysisreport_constructor_args():
    sig = inspect.signature(analysis::pipelining::ImpactAnalysisReport.__init__)
    params = list(sig.parameters.keys())



def test_analysis::caseoptimal::caseoptimalschedulereport_is_not_abstract():
    assert not inspect.isabstract(analysis::caseoptimal::CaseOptimalScheduleReport)


def test_analysis::caseoptimal::caseoptimalschedulereport_constructor_exists():
    assert callable(analysis::caseoptimal::CaseOptimalScheduleReport.__init__)


def test_analysis::caseoptimal::caseoptimalschedulereport_constructor_args():
    sig = inspect.signature(analysis::caseoptimal::CaseOptimalScheduleReport.__init__)
    params = list(sig.parameters.keys())
    assert "traceFile" in params, "Missing parameter 'traceFile'"
    assert "partitionFilePath" in params, "Missing parameter 'partitionFilePath'"
    assert "pipeline" in params, "Missing parameter 'pipeline'"

def test_analysis::caseoptimal::caseoptimalschedulereport_has_traceFile():
    assert hasattr(analysis::caseoptimal::CaseOptimalScheduleReport, "traceFile")
    descriptor = None
    for klass in analysis::caseoptimal::CaseOptimalScheduleReport.__mro__:
        if "traceFile" in klass.__dict__:
            descriptor = klass.__dict__["traceFile"]
            break
    assert isinstance(descriptor, property)

def test_analysis::caseoptimal::caseoptimalschedulereport_has_partitionFilePath():
    assert hasattr(analysis::caseoptimal::CaseOptimalScheduleReport, "partitionFilePath")
    descriptor = None
    for klass in analysis::caseoptimal::CaseOptimalScheduleReport.__mro__:
        if "partitionFilePath" in klass.__dict__:
            descriptor = klass.__dict__["partitionFilePath"]
            break
    assert isinstance(descriptor, property)

def test_analysis::caseoptimal::caseoptimalschedulereport_has_pipeline():
    assert hasattr(analysis::caseoptimal::CaseOptimalScheduleReport, "pipeline")
    descriptor = None
    for klass in analysis::caseoptimal::CaseOptimalScheduleReport.__mro__:
        if "pipeline" in klass.__dict__:
            descriptor = klass.__dict__["pipeline"]
            break
    assert isinstance(descriptor, property)



def test_analysis::bottlenecks::scheduledimpactanalysisreport_is_not_abstract():
    assert not inspect.isabstract(analysis::bottlenecks::ScheduledImpactAnalysisReport)


def test_analysis::bottlenecks::scheduledimpactanalysisreport_constructor_exists():
    assert callable(analysis::bottlenecks::ScheduledImpactAnalysisReport.__init__)


def test_analysis::bottlenecks::scheduledimpactanalysisreport_constructor_args():
    sig = inspect.signature(analysis::bottlenecks::ScheduledImpactAnalysisReport.__init__)
    params = list(sig.parameters.keys())
    assert "classLevel" in params, "Missing parameter 'classLevel'"

def test_analysis::bottlenecks::scheduledimpactanalysisreport_has_classLevel():
    assert hasattr(analysis::bottlenecks::ScheduledImpactAnalysisReport, "classLevel")
    descriptor = None
    for klass in analysis::bottlenecks::ScheduledImpactAnalysisReport.__mro__:
        if "classLevel" in klass.__dict__:
            descriptor = klass.__dict__["classLevel"]
            break
    assert isinstance(descriptor, property)



def test_analysis::profiling::intraactioncommunicationreport_is_not_abstract():
    assert not inspect.isabstract(analysis::profiling::IntraActionCommunicationReport)


def test_analysis::profiling::intraactioncommunicationreport_constructor_exists():
    assert callable(analysis::profiling::IntraActionCommunicationReport.__init__)


def test_analysis::profiling::intraactioncommunicationreport_constructor_args():
    sig = inspect.signature(analysis::profiling::IntraActionCommunicationReport.__init__)
    params = list(sig.parameters.keys())



def test_analysis::partitioning::balancedpipelinepartitioningreport_is_not_abstract():
    assert not inspect.isabstract(analysis::partitioning::BalancedPipelinePartitioningReport)


def test_analysis::partitioning::balancedpipelinepartitioningreport_constructor_exists():
    assert callable(analysis::partitioning::BalancedPipelinePartitioningReport.__init__)


def test_analysis::partitioning::balancedpipelinepartitioningreport_constructor_args():
    sig = inspect.signature(analysis::partitioning::BalancedPipelinePartitioningReport.__init__)
    params = list(sig.parameters.keys())



def test_analysis::profiler::codeprofilingreport_is_not_abstract():
    assert not inspect.isabstract(analysis::profiler::CodeProfilingReport)


def test_analysis::profiler::codeprofilingreport_constructor_exists():
    assert callable(analysis::profiler::CodeProfilingReport.__init__)


def test_analysis::profiler::codeprofilingreport_constructor_args():
    sig = inspect.signature(analysis::profiler::CodeProfilingReport.__init__)
    params = list(sig.parameters.keys())



def test_analysis::analysisreport_is_not_abstract():
    assert not inspect.isabstract(analysis::AnalysisReport)


def test_analysis::analysisreport_constructor_exists():
    assert callable(analysis::AnalysisReport.__init__)


def test_analysis::analysisreport_constructor_args():
    sig = inspect.signature(analysis::AnalysisReport.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"
    assert "algorithm" in params, "Missing parameter 'algorithm'"

def test_analysis::analysisreport_has_date():
    assert hasattr(analysis::AnalysisReport, "date")
    descriptor = None
    for klass in analysis::AnalysisReport.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_analysis::analysisreport_has_algorithm():
    assert hasattr(analysis::AnalysisReport, "algorithm")
    descriptor = None
    for klass in analysis::AnalysisReport.__mro__:
        if "algorithm" in klass.__dict__:
            descriptor = klass.__dict__["algorithm"]
            break
    assert isinstance(descriptor, property)



def test_analysis::trace::comparedaction_is_not_abstract():
    assert not inspect.isabstract(analysis::trace::ComparedAction)


def test_analysis::trace::comparedaction_constructor_exists():
    assert callable(analysis::trace::ComparedAction.__init__)


def test_analysis::trace::comparedaction_constructor_args():
    sig = inspect.signature(analysis::trace::ComparedAction.__init__)
    params = list(sig.parameters.keys())
    assert "found" in params, "Missing parameter 'found'"
    assert "dSteps" in params, "Missing parameter 'dSteps'"
    assert "dIncomings" in params, "Missing parameter 'dIncomings'"
    assert "dOutgoings" in params, "Missing parameter 'dOutgoings'"

def test_analysis::trace::comparedaction_has_found():
    assert hasattr(analysis::trace::ComparedAction, "found")
    descriptor = None
    for klass in analysis::trace::ComparedAction.__mro__:
        if "found" in klass.__dict__:
            descriptor = klass.__dict__["found"]
            break
    assert isinstance(descriptor, property)

def test_analysis::trace::comparedaction_has_dSteps():
    assert hasattr(analysis::trace::ComparedAction, "dSteps")
    descriptor = None
    for klass in analysis::trace::ComparedAction.__mro__:
        if "dSteps" in klass.__dict__:
            descriptor = klass.__dict__["dSteps"]
            break
    assert isinstance(descriptor, property)

def test_analysis::trace::comparedaction_has_dIncomings():
    assert hasattr(analysis::trace::ComparedAction, "dIncomings")
    descriptor = None
    for klass in analysis::trace::ComparedAction.__mro__:
        if "dIncomings" in klass.__dict__:
            descriptor = klass.__dict__["dIncomings"]
            break
    assert isinstance(descriptor, property)

def test_analysis::trace::comparedaction_has_dOutgoings():
    assert hasattr(analysis::trace::ComparedAction, "dOutgoings")
    descriptor = None
    for klass in analysis::trace::ComparedAction.__mro__:
        if "dOutgoings" in klass.__dict__:
            descriptor = klass.__dict__["dOutgoings"]
            break
    assert isinstance(descriptor, property)



def test_comparedaction_is_not_abstract():
    assert not inspect.isabstract(ComparedAction)


def test_comparedaction_constructor_exists():
    assert callable(ComparedAction.__init__)


def test_comparedaction_constructor_args():
    sig = inspect.signature(ComparedAction.__init__)
    params = list(sig.parameters.keys())



def test_bottlenecks::analysis::action_is_not_abstract():
    assert not inspect.isabstract(bottlenecks::analysis::Action)


def test_bottlenecks::analysis::action_constructor_exists():
    assert callable(bottlenecks::analysis::Action.__init__)


def test_bottlenecks::analysis::action_constructor_args():
    sig = inspect.signature(bottlenecks::analysis::Action.__init__)
    params = list(sig.parameters.keys())



def test_analysis::trace::comparedtrace_is_not_abstract():
    assert not inspect.isabstract(analysis::trace::ComparedTrace)


def test_analysis::trace::comparedtrace_constructor_exists():
    assert callable(analysis::trace::ComparedTrace.__init__)


def test_analysis::trace::comparedtrace_constructor_args():
    sig = inspect.signature(analysis::trace::ComparedTrace.__init__)
    params = list(sig.parameters.keys())
    assert "equal" in params, "Missing parameter 'equal'"
    assert "dSteps" in params, "Missing parameter 'dSteps'"
    assert "dDependencies" in params, "Missing parameter 'dDependencies'"

def test_analysis::trace::comparedtrace_has_equal():
    assert hasattr(analysis::trace::ComparedTrace, "equal")
    descriptor = None
    for klass in analysis::trace::ComparedTrace.__mro__:
        if "equal" in klass.__dict__:
            descriptor = klass.__dict__["equal"]
            break
    assert isinstance(descriptor, property)

def test_analysis::trace::comparedtrace_has_dSteps():
    assert hasattr(analysis::trace::ComparedTrace, "dSteps")
    descriptor = None
    for klass in analysis::trace::ComparedTrace.__mro__:
        if "dSteps" in klass.__dict__:
            descriptor = klass.__dict__["dSteps"]
            break
    assert isinstance(descriptor, property)

def test_analysis::trace::comparedtrace_has_dDependencies():
    assert hasattr(analysis::trace::ComparedTrace, "dDependencies")
    descriptor = None
    for klass in analysis::trace::ComparedTrace.__mro__:
        if "dDependencies" in klass.__dict__:
            descriptor = klass.__dict__["dDependencies"]
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



def test_analysis::trace::tracecomparatorreport_is_not_abstract():
    assert not inspect.isabstract(analysis::trace::TraceComparatorReport)


def test_analysis::trace::tracecomparatorreport_constructor_exists():
    assert callable(analysis::trace::TraceComparatorReport.__init__)


def test_analysis::trace::tracecomparatorreport_constructor_args():
    sig = inspect.signature(analysis::trace::TraceComparatorReport.__init__)
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



def test_analysis::trace::compresseddependency_is_not_abstract():
    assert not inspect.isabstract(analysis::trace::CompressedDependency)


def test_analysis::trace::compresseddependency_constructor_exists():
    assert callable(analysis::trace::CompressedDependency.__init__)


def test_analysis::trace::compresseddependency_constructor_args():
    sig = inspect.signature(analysis::trace::CompressedDependency.__init__)
    params = list(sig.parameters.keys())
    assert "count" in params, "Missing parameter 'count'"

def test_analysis::trace::compresseddependency_has_count():
    assert hasattr(analysis::trace::CompressedDependency, "count")
    descriptor = None
    for klass in analysis::trace::CompressedDependency.__mro__:
        if "count" in klass.__dict__:
            descriptor = klass.__dict__["count"]
            break
    assert isinstance(descriptor, property)



def test_trace::analysis::action_is_not_abstract():
    assert not inspect.isabstract(trace::analysis::Action)


def test_trace::analysis::action_constructor_exists():
    assert callable(trace::analysis::Action.__init__)


def test_trace::analysis::action_constructor_args():
    sig = inspect.signature(trace::analysis::Action.__init__)
    params = list(sig.parameters.keys())



def test_analysis::trace::compressedstep_is_not_abstract():
    assert not inspect.isabstract(analysis::trace::CompressedStep)


def test_analysis::trace::compressedstep_constructor_exists():
    assert callable(analysis::trace::CompressedStep.__init__)


def test_analysis::trace::compressedstep_constructor_args():
    sig = inspect.signature(analysis::trace::CompressedStep.__init__)
    params = list(sig.parameters.keys())
    assert "count" in params, "Missing parameter 'count'"

def test_analysis::trace::compressedstep_has_count():
    assert hasattr(analysis::trace::CompressedStep, "count")
    descriptor = None
    for klass in analysis::trace::CompressedStep.__mro__:
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



def test_analysis::trace::compressedportdependency_is_not_abstract():
    assert not inspect.isabstract(analysis::trace::CompressedPortDependency)


def test_analysis::trace::compressedportdependency_constructor_exists():
    assert callable(analysis::trace::CompressedPortDependency.__init__)


def test_analysis::trace::compressedportdependency_constructor_args():
    sig = inspect.signature(analysis::trace::CompressedPortDependency.__init__)
    params = list(sig.parameters.keys())



def test_analysis::trace::compressedguarddependency_is_not_abstract():
    assert not inspect.isabstract(analysis::trace::CompressedGuardDependency)


def test_analysis::trace::compressedguarddependency_constructor_exists():
    assert callable(analysis::trace::CompressedGuardDependency.__init__)


def test_analysis::trace::compressedguarddependency_constructor_args():
    sig = inspect.signature(analysis::trace::CompressedGuardDependency.__init__)
    params = list(sig.parameters.keys())



def test_analysis::trace::compressedtokensdependency_is_not_abstract():
    assert not inspect.isabstract(analysis::trace::CompressedTokensDependency)


def test_analysis::trace::compressedtokensdependency_constructor_exists():
    assert callable(analysis::trace::CompressedTokensDependency.__init__)


def test_analysis::trace::compressedtokensdependency_constructor_args():
    sig = inspect.signature(analysis::trace::CompressedTokensDependency.__init__)
    params = list(sig.parameters.keys())



def test_analysis::trace::compressedvariabledependency_is_not_abstract():
    assert not inspect.isabstract(analysis::trace::CompressedVariableDependency)


def test_analysis::trace::compressedvariabledependency_constructor_exists():
    assert callable(analysis::trace::CompressedVariableDependency.__init__)


def test_analysis::trace::compressedvariabledependency_constructor_args():
    sig = inspect.signature(analysis::trace::CompressedVariableDependency.__init__)
    params = list(sig.parameters.keys())



def test_analysis::trace::compressedfsmdependency_is_not_abstract():
    assert not inspect.isabstract(analysis::trace::CompressedFsmDependency)


def test_analysis::trace::compressedfsmdependency_constructor_exists():
    assert callable(analysis::trace::CompressedFsmDependency.__init__)


def test_analysis::trace::compressedfsmdependency_constructor_args():
    sig = inspect.signature(analysis::trace::CompressedFsmDependency.__init__)
    params = list(sig.parameters.keys())



def test_compressedstep_is_not_abstract():
    assert not inspect.isabstract(CompressedStep)


def test_compressedstep_constructor_exists():
    assert callable(CompressedStep.__init__)


def test_compressedstep_constructor_args():
    sig = inspect.signature(CompressedStep.__init__)
    params = list(sig.parameters.keys())



def test_analysis::trace::compressedtracereport_is_not_abstract():
    assert not inspect.isabstract(analysis::trace::CompressedTraceReport)


def test_analysis::trace::compressedtracereport_constructor_exists():
    assert callable(analysis::trace::CompressedTraceReport.__init__)


def test_analysis::trace::compressedtracereport_constructor_args():
    sig = inspect.signature(analysis::trace::CompressedTraceReport.__init__)
    params = list(sig.parameters.keys())
    assert "traceFile" in params, "Missing parameter 'traceFile'"

def test_analysis::trace::compressedtracereport_has_traceFile():
    assert hasattr(analysis::trace::CompressedTraceReport, "traceFile")
    descriptor = None
    for klass in analysis::trace::CompressedTraceReport.__mro__:
        if "traceFile" in klass.__dict__:
            descriptor = klass.__dict__["traceFile"]
            break
    assert isinstance(descriptor, property)



def test_trace::analysis::network_is_not_abstract():
    assert not inspect.isabstract(trace::analysis::Network)


def test_trace::analysis::network_constructor_exists():
    assert callable(trace::analysis::Network.__init__)


def test_trace::analysis::network_constructor_args():
    sig = inspect.signature(trace::analysis::Network.__init__)
    params = list(sig.parameters.keys())



def test_stringtolongmap_is_not_abstract():
    assert not inspect.isabstract(StringToLongMap)


def test_stringtolongmap_constructor_exists():
    assert callable(StringToLongMap.__init__)


def test_stringtolongmap_constructor_args():
    sig = inspect.signature(StringToLongMap.__init__)
    params = list(sig.parameters.keys())



def test_analysis::map::actiontodoublemap_is_not_abstract():
    assert not inspect.isabstract(analysis::map::ActionToDoubleMap)


def test_analysis::map::actiontodoublemap_constructor_exists():
    assert callable(analysis::map::ActionToDoubleMap.__init__)


def test_analysis::map::actiontodoublemap_constructor_args():
    sig = inspect.signature(analysis::map::ActionToDoubleMap.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_analysis::map::actiontodoublemap_has_value():
    assert hasattr(analysis::map::ActionToDoubleMap, "value")
    descriptor = None
    for klass in analysis::map::ActionToDoubleMap.__mro__:
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



def test_analysis::trace::tracesizereport_is_not_abstract():
    assert not inspect.isabstract(analysis::trace::TraceSizeReport)


def test_analysis::trace::tracesizereport_constructor_exists():
    assert callable(analysis::trace::TraceSizeReport.__init__)


def test_analysis::trace::tracesizereport_constructor_args():
    sig = inspect.signature(analysis::trace::TraceSizeReport.__init__)
    params = list(sig.parameters.keys())
    assert "dependencies" in params, "Missing parameter 'dependencies'"
    assert "firings" in params, "Missing parameter 'firings'"

def test_analysis::trace::tracesizereport_has_dependencies():
    assert hasattr(analysis::trace::TraceSizeReport, "dependencies")
    descriptor = None
    for klass in analysis::trace::TraceSizeReport.__mro__:
        if "dependencies" in klass.__dict__:
            descriptor = klass.__dict__["dependencies"]
            break
    assert isinstance(descriptor, property)

def test_analysis::trace::tracesizereport_has_firings():
    assert hasattr(analysis::trace::TraceSizeReport, "firings")
    descriptor = None
    for klass in analysis::trace::TraceSizeReport.__mro__:
        if "firings" in klass.__dict__:
            descriptor = klass.__dict__["firings"]
            break
    assert isinstance(descriptor, property)



def test_analysis::map::stringtostringmap_is_not_abstract():
    assert not inspect.isabstract(analysis::map::StringToStringMap)


def test_analysis::map::stringtostringmap_constructor_exists():
    assert callable(analysis::map::StringToStringMap.__init__)


def test_analysis::map::stringtostringmap_constructor_args():
    sig = inspect.signature(analysis::map::StringToStringMap.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_analysis::map::stringtostringmap_has_value():
    assert hasattr(analysis::map::StringToStringMap, "value")
    descriptor = None
    for klass in analysis::map::StringToStringMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_analysis::map::stringtostringmap_has_key():
    assert hasattr(analysis::map::StringToStringMap, "key")
    descriptor = None
    for klass in analysis::map::StringToStringMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_actorselectionschedule_is_not_abstract():
    assert not inspect.isabstract(ActorSelectionSchedule)


def test_actorselectionschedule_constructor_exists():
    assert callable(ActorSelectionSchedule.__init__)


def test_actorselectionschedule_constructor_args():
    sig = inspect.signature(ActorSelectionSchedule.__init__)
    params = list(sig.parameters.keys())



def test_analysis::scheduling::fsm_is_not_abstract():
    assert not inspect.isabstract(analysis::scheduling::FSM)


def test_analysis::scheduling::fsm_constructor_exists():
    assert callable(analysis::scheduling::FSM.__init__)


def test_analysis::scheduling::fsm_constructor_args():
    sig = inspect.signature(analysis::scheduling::FSM.__init__)
    params = list(sig.parameters.keys())
    assert "terminalState" in params, "Missing parameter 'terminalState'"
    assert "startState" in params, "Missing parameter 'startState'"

def test_analysis::scheduling::fsm_has_terminalState():
    assert hasattr(analysis::scheduling::FSM, "terminalState")
    descriptor = None
    for klass in analysis::scheduling::FSM.__mro__:
        if "terminalState" in klass.__dict__:
            descriptor = klass.__dict__["terminalState"]
            break
    assert isinstance(descriptor, property)

def test_analysis::scheduling::fsm_has_startState():
    assert hasattr(analysis::scheduling::FSM, "startState")
    descriptor = None
    for klass in analysis::scheduling::FSM.__mro__:
        if "startState" in klass.__dict__:
            descriptor = klass.__dict__["startState"]
            break
    assert isinstance(descriptor, property)



def test_analysis::scheduling::actorfire_is_not_abstract():
    assert not inspect.isabstract(analysis::scheduling::ActorFire)


def test_analysis::scheduling::actorfire_constructor_exists():
    assert callable(analysis::scheduling::ActorFire.__init__)


def test_analysis::scheduling::actorfire_constructor_args():
    sig = inspect.signature(analysis::scheduling::ActorFire.__init__)
    params = list(sig.parameters.keys())
    assert "Actor" in params, "Missing parameter 'Actor'"
    assert "partition" in params, "Missing parameter 'partition'"
    assert "dependencyPartitions" in params, "Missing parameter 'dependencyPartitions'"
    assert "Times" in params, "Missing parameter 'Times'"

def test_analysis::scheduling::actorfire_has_Actor():
    assert hasattr(analysis::scheduling::ActorFire, "Actor")
    descriptor = None
    for klass in analysis::scheduling::ActorFire.__mro__:
        if "Actor" in klass.__dict__:
            descriptor = klass.__dict__["Actor"]
            break
    assert isinstance(descriptor, property)

def test_analysis::scheduling::actorfire_has_partition():
    assert hasattr(analysis::scheduling::ActorFire, "partition")
    descriptor = None
    for klass in analysis::scheduling::ActorFire.__mro__:
        if "partition" in klass.__dict__:
            descriptor = klass.__dict__["partition"]
            break
    assert isinstance(descriptor, property)

def test_analysis::scheduling::actorfire_has_dependencyPartitions():
    assert hasattr(analysis::scheduling::ActorFire, "dependencyPartitions")
    descriptor = None
    for klass in analysis::scheduling::ActorFire.__mro__:
        if "dependencyPartitions" in klass.__dict__:
            descriptor = klass.__dict__["dependencyPartitions"]
            break
    assert isinstance(descriptor, property)

def test_analysis::scheduling::actorfire_has_Times():
    assert hasattr(analysis::scheduling::ActorFire, "Times")
    descriptor = None
    for klass in analysis::scheduling::ActorFire.__mro__:
        if "Times" in klass.__dict__:
            descriptor = klass.__dict__["Times"]
            break
    assert isinstance(descriptor, property)



def test_analysis::caseoptimal::caseoptimalactorselectionschedule_is_not_abstract():
    assert not inspect.isabstract(analysis::caseoptimal::CaseOptimalActorSelectionSchedule)


def test_analysis::caseoptimal::caseoptimalactorselectionschedule_constructor_exists():
    assert callable(analysis::caseoptimal::CaseOptimalActorSelectionSchedule.__init__)


def test_analysis::caseoptimal::caseoptimalactorselectionschedule_constructor_args():
    sig = inspect.signature(analysis::caseoptimal::CaseOptimalActorSelectionSchedule.__init__)
    params = list(sig.parameters.keys())



def test_analysis::scheduling::sequence_is_not_abstract():
    assert not inspect.isabstract(analysis::scheduling::Sequence)


def test_analysis::scheduling::sequence_constructor_exists():
    assert callable(analysis::scheduling::Sequence.__init__)


def test_analysis::scheduling::sequence_constructor_args():
    sig = inspect.signature(analysis::scheduling::Sequence.__init__)
    params = list(sig.parameters.keys())



def test_analysis::map::partitiontoactorselectionschedulemap_is_not_abstract():
    assert not inspect.isabstract(analysis::map::PartitionToActorSelectionScheduleMap)


def test_analysis::map::partitiontoactorselectionschedulemap_constructor_exists():
    assert callable(analysis::map::PartitionToActorSelectionScheduleMap.__init__)


def test_analysis::map::partitiontoactorselectionschedulemap_constructor_args():
    sig = inspect.signature(analysis::map::PartitionToActorSelectionScheduleMap.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_analysis::map::partitiontoactorselectionschedulemap_has_key():
    assert hasattr(analysis::map::PartitionToActorSelectionScheduleMap, "key")
    descriptor = None
    for klass in analysis::map::PartitionToActorSelectionScheduleMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_analysis::map::buffertodoublemap_is_not_abstract():
    assert not inspect.isabstract(analysis::map::BufferToDoubleMap)


def test_analysis::map::buffertodoublemap_constructor_exists():
    assert callable(analysis::map::BufferToDoubleMap.__init__)


def test_analysis::map::buffertodoublemap_constructor_args():
    sig = inspect.signature(analysis::map::BufferToDoubleMap.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_analysis::map::buffertodoublemap_has_value():
    assert hasattr(analysis::map::BufferToDoubleMap, "value")
    descriptor = None
    for klass in analysis::map::BufferToDoubleMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_analysis::map::buffertointegermap_is_not_abstract():
    assert not inspect.isabstract(analysis::map::BufferToIntegerMap)


def test_analysis::map::buffertointegermap_constructor_exists():
    assert callable(analysis::map::BufferToIntegerMap.__init__)


def test_analysis::map::buffertointegermap_constructor_args():
    sig = inspect.signature(analysis::map::BufferToIntegerMap.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_analysis::map::buffertointegermap_has_value():
    assert hasattr(analysis::map::BufferToIntegerMap, "value")
    descriptor = None
    for klass in analysis::map::BufferToIntegerMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_map::analysis::procedure_is_not_abstract():
    assert not inspect.isabstract(map::analysis::Procedure)


def test_map::analysis::procedure_constructor_exists():
    assert callable(map::analysis::Procedure.__init__)


def test_map::analysis::procedure_constructor_args():
    sig = inspect.signature(map::analysis::Procedure.__init__)
    params = list(sig.parameters.keys())



def test_analysis::map::stringtodoublemap_is_not_abstract():
    assert not inspect.isabstract(analysis::map::StringToDoubleMap)


def test_analysis::map::stringtodoublemap_constructor_exists():
    assert callable(analysis::map::StringToDoubleMap.__init__)


def test_analysis::map::stringtodoublemap_constructor_args():
    sig = inspect.signature(analysis::map::StringToDoubleMap.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_analysis::map::stringtodoublemap_has_key():
    assert hasattr(analysis::map::StringToDoubleMap, "key")
    descriptor = None
    for klass in analysis::map::StringToDoubleMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_analysis::map::stringtodoublemap_has_value():
    assert hasattr(analysis::map::StringToDoubleMap, "value")
    descriptor = None
    for klass in analysis::map::StringToDoubleMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_map::analysis::port_is_not_abstract():
    assert not inspect.isabstract(map::analysis::Port)


def test_map::analysis::port_constructor_exists():
    assert callable(map::analysis::Port.__init__)


def test_map::analysis::port_constructor_args():
    sig = inspect.signature(map::analysis::Port.__init__)
    params = list(sig.parameters.keys())



def test_analysis::map::porttolongmap_is_not_abstract():
    assert not inspect.isabstract(analysis::map::PortToLongMap)


def test_analysis::map::porttolongmap_constructor_exists():
    assert callable(analysis::map::PortToLongMap.__init__)


def test_analysis::map::porttolongmap_constructor_args():
    sig = inspect.signature(analysis::map::PortToLongMap.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_analysis::map::porttolongmap_has_value():
    assert hasattr(analysis::map::PortToLongMap, "value")
    descriptor = None
    for klass in analysis::map::PortToLongMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_map::analysis::guard_is_not_abstract():
    assert not inspect.isabstract(map::analysis::Guard)


def test_map::analysis::guard_constructor_exists():
    assert callable(map::analysis::Guard.__init__)


def test_map::analysis::guard_constructor_args():
    sig = inspect.signature(map::analysis::Guard.__init__)
    params = list(sig.parameters.keys())



def test_analysis::map::guardtolongmap_is_not_abstract():
    assert not inspect.isabstract(analysis::map::GuardToLongMap)


def test_analysis::map::guardtolongmap_constructor_exists():
    assert callable(analysis::map::GuardToLongMap.__init__)


def test_analysis::map::guardtolongmap_constructor_args():
    sig = inspect.signature(analysis::map::GuardToLongMap.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_analysis::map::guardtolongmap_has_value():
    assert hasattr(analysis::map::GuardToLongMap, "value")
    descriptor = None
    for klass in analysis::map::GuardToLongMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_analysis::map::variabletolongmap_is_not_abstract():
    assert not inspect.isabstract(analysis::map::VariableToLongMap)


def test_analysis::map::variabletolongmap_constructor_exists():
    assert callable(analysis::map::VariableToLongMap.__init__)


def test_analysis::map::variabletolongmap_constructor_args():
    sig = inspect.signature(analysis::map::VariableToLongMap.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_analysis::map::variabletolongmap_has_value():
    assert hasattr(analysis::map::VariableToLongMap, "value")
    descriptor = None
    for klass in analysis::map::VariableToLongMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_analysis::map::doubletodoublemap_is_not_abstract():
    assert not inspect.isabstract(analysis::map::DoubleToDoubleMap)


def test_analysis::map::doubletodoublemap_constructor_exists():
    assert callable(analysis::map::DoubleToDoubleMap.__init__)


def test_analysis::map::doubletodoublemap_constructor_args():
    sig = inspect.signature(analysis::map::DoubleToDoubleMap.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_analysis::map::doubletodoublemap_has_key():
    assert hasattr(analysis::map::DoubleToDoubleMap, "key")
    descriptor = None
    for klass in analysis::map::DoubleToDoubleMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_analysis::map::doubletodoublemap_has_value():
    assert hasattr(analysis::map::DoubleToDoubleMap, "value")
    descriptor = None
    for klass in analysis::map::DoubleToDoubleMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_analysis::map::stringtolongmap_is_not_abstract():
    assert not inspect.isabstract(analysis::map::StringToLongMap)


def test_analysis::map::stringtolongmap_constructor_exists():
    assert callable(analysis::map::StringToLongMap.__init__)


def test_analysis::map::stringtolongmap_constructor_args():
    sig = inspect.signature(analysis::map::StringToLongMap.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_analysis::map::stringtolongmap_has_key():
    assert hasattr(analysis::map::StringToLongMap, "key")
    descriptor = None
    for klass in analysis::map::StringToLongMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_analysis::map::stringtolongmap_has_value():
    assert hasattr(analysis::map::StringToLongMap, "value")
    descriptor = None
    for klass in analysis::map::StringToLongMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_analysis::map::buffertolongmap_is_not_abstract():
    assert not inspect.isabstract(analysis::map::BufferToLongMap)


def test_analysis::map::buffertolongmap_constructor_exists():
    assert callable(analysis::map::BufferToLongMap.__init__)


def test_analysis::map::buffertolongmap_constructor_args():
    sig = inspect.signature(analysis::map::BufferToLongMap.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_analysis::map::buffertolongmap_has_value():
    assert hasattr(analysis::map::BufferToLongMap, "value")
    descriptor = None
    for klass in analysis::map::BufferToLongMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_analysis::map::actortolongmap_is_not_abstract():
    assert not inspect.isabstract(analysis::map::ActorToLongMap)


def test_analysis::map::actortolongmap_constructor_exists():
    assert callable(analysis::map::ActorToLongMap.__init__)


def test_analysis::map::actortolongmap_constructor_args():
    sig = inspect.signature(analysis::map::ActorToLongMap.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_analysis::map::actortolongmap_has_value():
    assert hasattr(analysis::map::ActorToLongMap, "value")
    descriptor = None
    for klass in analysis::map::ActorToLongMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_analysis::map::actiontolongmap_is_not_abstract():
    assert not inspect.isabstract(analysis::map::ActionToLongMap)


def test_analysis::map::actiontolongmap_constructor_exists():
    assert callable(analysis::map::ActionToLongMap.__init__)


def test_analysis::map::actiontolongmap_constructor_args():
    sig = inspect.signature(analysis::map::ActionToLongMap.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_analysis::map::actiontolongmap_has_value():
    assert hasattr(analysis::map::ActionToLongMap, "value")
    descriptor = None
    for klass in analysis::map::ActionToLongMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_analysis::map::eoperatortostatisticaldatamap_is_not_abstract():
    assert not inspect.isabstract(analysis::map::EOperatorToStatisticalDataMap)


def test_analysis::map::eoperatortostatisticaldatamap_constructor_exists():
    assert callable(analysis::map::EOperatorToStatisticalDataMap.__init__)


def test_analysis::map::eoperatortostatisticaldatamap_constructor_args():
    sig = inspect.signature(analysis::map::EOperatorToStatisticalDataMap.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_analysis::map::eoperatortostatisticaldatamap_has_key():
    assert hasattr(analysis::map::EOperatorToStatisticalDataMap, "key")
    descriptor = None
    for klass in analysis::map::EOperatorToStatisticalDataMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_map::analysis::actorclass_is_not_abstract():
    assert not inspect.isabstract(map::analysis::ActorClass)


def test_map::analysis::actorclass_constructor_exists():
    assert callable(map::analysis::ActorClass.__init__)


def test_map::analysis::actorclass_constructor_args():
    sig = inspect.signature(map::analysis::ActorClass.__init__)
    params = list(sig.parameters.keys())



def test_analysis::map::actorclasstostatisticaldatamap_is_not_abstract():
    assert not inspect.isabstract(analysis::map::ActorClassToStatisticalDataMap)


def test_analysis::map::actorclasstostatisticaldatamap_constructor_exists():
    assert callable(analysis::map::ActorClassToStatisticalDataMap.__init__)


def test_analysis::map::actorclasstostatisticaldatamap_constructor_args():
    sig = inspect.signature(analysis::map::ActorClassToStatisticalDataMap.__init__)
    params = list(sig.parameters.keys())



def test_map::analysis::variable_is_not_abstract():
    assert not inspect.isabstract(map::analysis::Variable)


def test_map::analysis::variable_constructor_exists():
    assert callable(map::analysis::Variable.__init__)


def test_map::analysis::variable_constructor_args():
    sig = inspect.signature(map::analysis::Variable.__init__)
    params = list(sig.parameters.keys())



def test_analysis::map::variabletostatisticaldatamap_is_not_abstract():
    assert not inspect.isabstract(analysis::map::VariableToStatisticalDataMap)


def test_analysis::map::variabletostatisticaldatamap_constructor_exists():
    assert callable(analysis::map::VariableToStatisticalDataMap.__init__)


def test_analysis::map::variabletostatisticaldatamap_constructor_args():
    sig = inspect.signature(analysis::map::VariableToStatisticalDataMap.__init__)
    params = list(sig.parameters.keys())



def test_analysis::map::proceduretostatisticaldatamap_is_not_abstract():
    assert not inspect.isabstract(analysis::map::ProcedureToStatisticalDataMap)


def test_analysis::map::proceduretostatisticaldatamap_constructor_exists():
    assert callable(analysis::map::ProcedureToStatisticalDataMap.__init__)


def test_analysis::map::proceduretostatisticaldatamap_constructor_args():
    sig = inspect.signature(analysis::map::ProcedureToStatisticalDataMap.__init__)
    params = list(sig.parameters.keys())



def test_map::analysis::buffer_is_not_abstract():
    assert not inspect.isabstract(map::analysis::Buffer)


def test_map::analysis::buffer_constructor_exists():
    assert callable(map::analysis::Buffer.__init__)


def test_map::analysis::buffer_constructor_args():
    sig = inspect.signature(map::analysis::Buffer.__init__)
    params = list(sig.parameters.keys())



def test_analysis::map::buffertostatisticaldatamap_is_not_abstract():
    assert not inspect.isabstract(analysis::map::BufferToStatisticalDataMap)


def test_analysis::map::buffertostatisticaldatamap_constructor_exists():
    assert callable(analysis::map::BufferToStatisticalDataMap.__init__)


def test_analysis::map::buffertostatisticaldatamap_constructor_args():
    sig = inspect.signature(analysis::map::BufferToStatisticalDataMap.__init__)
    params = list(sig.parameters.keys())



def test_map::analysis::action_is_not_abstract():
    assert not inspect.isabstract(map::analysis::Action)


def test_map::analysis::action_constructor_exists():
    assert callable(map::analysis::Action.__init__)


def test_map::analysis::action_constructor_args():
    sig = inspect.signature(map::analysis::Action.__init__)
    params = list(sig.parameters.keys())



def test_analysis::map::actiontostatisticaldatamap_is_not_abstract():
    assert not inspect.isabstract(analysis::map::ActionToStatisticalDataMap)


def test_analysis::map::actiontostatisticaldatamap_constructor_exists():
    assert callable(analysis::map::ActionToStatisticalDataMap.__init__)


def test_analysis::map::actiontostatisticaldatamap_constructor_args():
    sig = inspect.signature(analysis::map::ActionToStatisticalDataMap.__init__)
    params = list(sig.parameters.keys())



def test_map::analysis::statisticaldata_is_not_abstract():
    assert not inspect.isabstract(map::analysis::StatisticalData)


def test_map::analysis::statisticaldata_constructor_exists():
    assert callable(map::analysis::StatisticalData.__init__)


def test_map::analysis::statisticaldata_constructor_args():
    sig = inspect.signature(map::analysis::StatisticalData.__init__)
    params = list(sig.parameters.keys())



def test_map::analysis::actor_is_not_abstract():
    assert not inspect.isabstract(map::analysis::Actor)


def test_map::analysis::actor_constructor_exists():
    assert callable(map::analysis::Actor.__init__)


def test_map::analysis::actor_constructor_args():
    sig = inspect.signature(map::analysis::Actor.__init__)
    params = list(sig.parameters.keys())



def test_analysis::map::actortostatisticaldatamap_is_not_abstract():
    assert not inspect.isabstract(analysis::map::ActorToStatisticalDataMap)


def test_analysis::map::actortostatisticaldatamap_constructor_exists():
    assert callable(analysis::map::ActorToStatisticalDataMap.__init__)


def test_analysis::map::actortostatisticaldatamap_constructor_args():
    sig = inspect.signature(analysis::map::ActorToStatisticalDataMap.__init__)
    params = list(sig.parameters.keys())



def test_analysis::map::stringtointegermap_is_not_abstract():
    assert not inspect.isabstract(analysis::map::StringToIntegerMap)


def test_analysis::map::stringtointegermap_constructor_exists():
    assert callable(analysis::map::StringToIntegerMap.__init__)


def test_analysis::map::stringtointegermap_constructor_args():
    sig = inspect.signature(analysis::map::StringToIntegerMap.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_analysis::map::stringtointegermap_has_value():
    assert hasattr(analysis::map::StringToIntegerMap, "value")
    descriptor = None
    for klass in analysis::map::StringToIntegerMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_analysis::map::stringtointegermap_has_key():
    assert hasattr(analysis::map::StringToIntegerMap, "key")
    descriptor = None
    for klass in analysis::map::StringToIntegerMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_stringtostringmap_is_not_abstract():
    assert not inspect.isabstract(StringToStringMap)


def test_stringtostringmap_constructor_exists():
    assert callable(StringToStringMap.__init__)


def test_stringtostringmap_constructor_args():
    sig = inspect.signature(StringToStringMap.__init__)
    params = list(sig.parameters.keys())



def test_analysis::profiler::tablerow_is_not_abstract():
    assert not inspect.isabstract(analysis::profiler::TableRow)


def test_analysis::profiler::tablerow_constructor_exists():
    assert callable(analysis::profiler::TableRow.__init__)


def test_analysis::profiler::tablerow_constructor_args():
    sig = inspect.signature(analysis::profiler::TableRow.__init__)
    params = list(sig.parameters.keys())



def test_tablerow_is_not_abstract():
    assert not inspect.isabstract(TableRow)


def test_tablerow_constructor_exists():
    assert callable(TableRow.__init__)


def test_tablerow_constructor_args():
    sig = inspect.signature(TableRow.__init__)
    params = list(sig.parameters.keys())



def test_analysis::profiler::benchmarkreport_is_not_abstract():
    assert not inspect.isabstract(analysis::profiler::BenchmarkReport)


def test_analysis::profiler::benchmarkreport_constructor_exists():
    assert callable(analysis::profiler::BenchmarkReport.__init__)


def test_analysis::profiler::benchmarkreport_constructor_args():
    sig = inspect.signature(analysis::profiler::BenchmarkReport.__init__)
    params = list(sig.parameters.keys())
    assert "column_names" in params, "Missing parameter 'column_names'"

def test_analysis::profiler::benchmarkreport_has_column_names():
    assert hasattr(analysis::profiler::BenchmarkReport, "column_names")
    descriptor = None
    for klass in analysis::profiler::BenchmarkReport.__mro__:
        if "column_names" in klass.__dict__:
            descriptor = klass.__dict__["column_names"]
            break
    assert isinstance(descriptor, property)



def test_accessdata_is_not_abstract():
    assert not inspect.isabstract(AccessData)


def test_accessdata_constructor_exists():
    assert callable(AccessData.__init__)


def test_accessdata_constructor_args():
    sig = inspect.signature(AccessData.__init__)
    params = list(sig.parameters.keys())



def test_analysis::profiler::stringtoaccessdatamap_is_not_abstract():
    assert not inspect.isabstract(analysis::profiler::StringToAccessDataMap)


def test_analysis::profiler::stringtoaccessdatamap_constructor_exists():
    assert callable(analysis::profiler::StringToAccessDataMap.__init__)


def test_analysis::profiler::stringtoaccessdatamap_constructor_args():
    sig = inspect.signature(analysis::profiler::StringToAccessDataMap.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_analysis::profiler::stringtoaccessdatamap_has_key():
    assert hasattr(analysis::profiler::StringToAccessDataMap, "key")
    descriptor = None
    for klass in analysis::profiler::StringToAccessDataMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_analysis::profiler::accessdata_is_not_abstract():
    assert not inspect.isabstract(analysis::profiler::AccessData)


def test_analysis::profiler::accessdata_constructor_exists():
    assert callable(analysis::profiler::AccessData.__init__)


def test_analysis::profiler::accessdata_constructor_args():
    sig = inspect.signature(analysis::profiler::AccessData.__init__)
    params = list(sig.parameters.keys())
    assert "accesses" in params, "Missing parameter 'accesses'"
    assert "total" in params, "Missing parameter 'total'"
    assert "min" in params, "Missing parameter 'min'"
    assert "average" in params, "Missing parameter 'average'"
    assert "max" in params, "Missing parameter 'max'"

def test_analysis::profiler::accessdata_has_accesses():
    assert hasattr(analysis::profiler::AccessData, "accesses")
    descriptor = None
    for klass in analysis::profiler::AccessData.__mro__:
        if "accesses" in klass.__dict__:
            descriptor = klass.__dict__["accesses"]
            break
    assert isinstance(descriptor, property)

def test_analysis::profiler::accessdata_has_total():
    assert hasattr(analysis::profiler::AccessData, "total")
    descriptor = None
    for klass in analysis::profiler::AccessData.__mro__:
        if "total" in klass.__dict__:
            descriptor = klass.__dict__["total"]
            break
    assert isinstance(descriptor, property)

def test_analysis::profiler::accessdata_has_min():
    assert hasattr(analysis::profiler::AccessData, "min")
    descriptor = None
    for klass in analysis::profiler::AccessData.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_analysis::profiler::accessdata_has_average():
    assert hasattr(analysis::profiler::AccessData, "average")
    descriptor = None
    for klass in analysis::profiler::AccessData.__mro__:
        if "average" in klass.__dict__:
            descriptor = klass.__dict__["average"]
            break
    assert isinstance(descriptor, property)

def test_analysis::profiler::accessdata_has_max():
    assert hasattr(analysis::profiler::AccessData, "max")
    descriptor = None
    for klass in analysis::profiler::AccessData.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)



def test_profiler::analysis::procedure_is_not_abstract():
    assert not inspect.isabstract(profiler::analysis::Procedure)


def test_profiler::analysis::procedure_constructor_exists():
    assert callable(profiler::analysis::Procedure.__init__)


def test_profiler::analysis::procedure_constructor_args():
    sig = inspect.signature(profiler::analysis::Procedure.__init__)
    params = list(sig.parameters.keys())



def test_stringtoaccessdatamap_is_not_abstract():
    assert not inspect.isabstract(StringToAccessDataMap)


def test_stringtoaccessdatamap_constructor_exists():
    assert callable(StringToAccessDataMap.__init__)


def test_stringtoaccessdatamap_constructor_args():
    sig = inspect.signature(StringToAccessDataMap.__init__)
    params = list(sig.parameters.keys())



def test_analysis::profiler::memoryaccessdata_is_not_abstract():
    assert not inspect.isabstract(analysis::profiler::MemoryAccessData)


def test_analysis::profiler::memoryaccessdata_constructor_exists():
    assert callable(analysis::profiler::MemoryAccessData.__init__)


def test_analysis::profiler::memoryaccessdata_constructor_args():
    sig = inspect.signature(analysis::profiler::MemoryAccessData.__init__)
    params = list(sig.parameters.keys())



def test_memoryaccessdata_is_not_abstract():
    assert not inspect.isabstract(MemoryAccessData)


def test_memoryaccessdata_constructor_exists():
    assert callable(MemoryAccessData.__init__)


def test_memoryaccessdata_constructor_args():
    sig = inspect.signature(MemoryAccessData.__init__)
    params = list(sig.parameters.keys())



def test_analysis::profiler::sharedvariableaccessdata_is_not_abstract():
    assert not inspect.isabstract(analysis::profiler::SharedVariableAccessData)


def test_analysis::profiler::sharedvariableaccessdata_constructor_exists():
    assert callable(analysis::profiler::SharedVariableAccessData.__init__)


def test_analysis::profiler::sharedvariableaccessdata_constructor_args():
    sig = inspect.signature(analysis::profiler::SharedVariableAccessData.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_analysis::profiler::sharedvariableaccessdata_has_name():
    assert hasattr(analysis::profiler::SharedVariableAccessData, "name")
    descriptor = None
    for klass in analysis::profiler::SharedVariableAccessData.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_analysis::profiler::bufferaccessdata_is_not_abstract():
    assert not inspect.isabstract(analysis::profiler::BufferAccessData)


def test_analysis::profiler::bufferaccessdata_constructor_exists():
    assert callable(analysis::profiler::BufferAccessData.__init__)


def test_analysis::profiler::bufferaccessdata_constructor_args():
    sig = inspect.signature(analysis::profiler::BufferAccessData.__init__)
    params = list(sig.parameters.keys())
    assert "sourceActor" in params, "Missing parameter 'sourceActor'"
    assert "targetActor" in params, "Missing parameter 'targetActor'"
    assert "targetPort" in params, "Missing parameter 'targetPort'"
    assert "sourcePort" in params, "Missing parameter 'sourcePort'"

def test_analysis::profiler::bufferaccessdata_has_sourceActor():
    assert hasattr(analysis::profiler::BufferAccessData, "sourceActor")
    descriptor = None
    for klass in analysis::profiler::BufferAccessData.__mro__:
        if "sourceActor" in klass.__dict__:
            descriptor = klass.__dict__["sourceActor"]
            break
    assert isinstance(descriptor, property)

def test_analysis::profiler::bufferaccessdata_has_targetActor():
    assert hasattr(analysis::profiler::BufferAccessData, "targetActor")
    descriptor = None
    for klass in analysis::profiler::BufferAccessData.__mro__:
        if "targetActor" in klass.__dict__:
            descriptor = klass.__dict__["targetActor"]
            break
    assert isinstance(descriptor, property)

def test_analysis::profiler::bufferaccessdata_has_targetPort():
    assert hasattr(analysis::profiler::BufferAccessData, "targetPort")
    descriptor = None
    for klass in analysis::profiler::BufferAccessData.__mro__:
        if "targetPort" in klass.__dict__:
            descriptor = klass.__dict__["targetPort"]
            break
    assert isinstance(descriptor, property)

def test_analysis::profiler::bufferaccessdata_has_sourcePort():
    assert hasattr(analysis::profiler::BufferAccessData, "sourcePort")
    descriptor = None
    for klass in analysis::profiler::BufferAccessData.__mro__:
        if "sourcePort" in klass.__dict__:
            descriptor = klass.__dict__["sourcePort"]
            break
    assert isinstance(descriptor, property)



def test_analysis::profiler::localvariableaccessdata_is_not_abstract():
    assert not inspect.isabstract(analysis::profiler::LocalVariableAccessData)


def test_analysis::profiler::localvariableaccessdata_constructor_exists():
    assert callable(analysis::profiler::LocalVariableAccessData.__init__)


def test_analysis::profiler::localvariableaccessdata_constructor_args():
    sig = inspect.signature(analysis::profiler::LocalVariableAccessData.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_analysis::profiler::localvariableaccessdata_has_name():
    assert hasattr(analysis::profiler::LocalVariableAccessData, "name")
    descriptor = None
    for klass in analysis::profiler::LocalVariableAccessData.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_analysis::profiler::statevariableaccessdata_is_not_abstract():
    assert not inspect.isabstract(analysis::profiler::StateVariableAccessData)


def test_analysis::profiler::statevariableaccessdata_constructor_exists():
    assert callable(analysis::profiler::StateVariableAccessData.__init__)


def test_analysis::profiler::statevariableaccessdata_constructor_args():
    sig = inspect.signature(analysis::profiler::StateVariableAccessData.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_analysis::profiler::statevariableaccessdata_has_name():
    assert hasattr(analysis::profiler::StateVariableAccessData, "name")
    descriptor = None
    for klass in analysis::profiler::StateVariableAccessData.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_analysis::profiler::actionmemoryprofilingdata_is_not_abstract():
    assert not inspect.isabstract(analysis::profiler::ActionMemoryProfilingData)


def test_analysis::profiler::actionmemoryprofilingdata_constructor_exists():
    assert callable(analysis::profiler::ActionMemoryProfilingData.__init__)


def test_analysis::profiler::actionmemoryprofilingdata_constructor_args():
    sig = inspect.signature(analysis::profiler::ActionMemoryProfilingData.__init__)
    params = list(sig.parameters.keys())
    assert "actor" in params, "Missing parameter 'actor'"
    assert "action" in params, "Missing parameter 'action'"

def test_analysis::profiler::actionmemoryprofilingdata_has_actor():
    assert hasattr(analysis::profiler::ActionMemoryProfilingData, "actor")
    descriptor = None
    for klass in analysis::profiler::ActionMemoryProfilingData.__mro__:
        if "actor" in klass.__dict__:
            descriptor = klass.__dict__["actor"]
            break
    assert isinstance(descriptor, property)

def test_analysis::profiler::actionmemoryprofilingdata_has_action():
    assert hasattr(analysis::profiler::ActionMemoryProfilingData, "action")
    descriptor = None
    for klass in analysis::profiler::ActionMemoryProfilingData.__mro__:
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



def test_analysis::profiler::memoryprofilingreport_is_not_abstract():
    assert not inspect.isabstract(analysis::profiler::MemoryProfilingReport)


def test_analysis::profiler::memoryprofilingreport_constructor_exists():
    assert callable(analysis::profiler::MemoryProfilingReport.__init__)


def test_analysis::profiler::memoryprofilingreport_constructor_args():
    sig = inspect.signature(analysis::profiler::MemoryProfilingReport.__init__)
    params = list(sig.parameters.keys())
    assert "networkName" in params, "Missing parameter 'networkName'"

def test_analysis::profiler::memoryprofilingreport_has_networkName():
    assert hasattr(analysis::profiler::MemoryProfilingReport, "networkName")
    descriptor = None
    for klass in analysis::profiler::MemoryProfilingReport.__mro__:
        if "networkName" in klass.__dict__:
            descriptor = klass.__dict__["networkName"]
            break
    assert isinstance(descriptor, property)



def test_actiondynamicdata_is_not_abstract():
    assert not inspect.isabstract(ActionDynamicData)


def test_actiondynamicdata_constructor_exists():
    assert callable(ActionDynamicData.__init__)


def test_actiondynamicdata_constructor_args():
    sig = inspect.signature(ActionDynamicData.__init__)
    params = list(sig.parameters.keys())



def test_analysis::profiler::proceduretocomplexdynamicdatamap_is_not_abstract():
    assert not inspect.isabstract(analysis::profiler::ProcedureToComplexDynamicDataMap)


def test_analysis::profiler::proceduretocomplexdynamicdatamap_constructor_exists():
    assert callable(analysis::profiler::ProcedureToComplexDynamicDataMap.__init__)


def test_analysis::profiler::proceduretocomplexdynamicdatamap_constructor_args():
    sig = inspect.signature(analysis::profiler::ProcedureToComplexDynamicDataMap.__init__)
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



def test_analysis::profiler::complexdynamicdata_is_not_abstract():
    assert not inspect.isabstract(analysis::profiler::ComplexDynamicData)


def test_analysis::profiler::complexdynamicdata_constructor_exists():
    assert callable(analysis::profiler::ComplexDynamicData.__init__)


def test_analysis::profiler::complexdynamicdata_constructor_args():
    sig = inspect.signature(analysis::profiler::ComplexDynamicData.__init__)
    params = list(sig.parameters.keys())



def test_actiontolongmap_is_not_abstract():
    assert not inspect.isabstract(ActionToLongMap)


def test_actiontolongmap_constructor_exists():
    assert callable(ActionToLongMap.__init__)


def test_actiontolongmap_constructor_args():
    sig = inspect.signature(ActionToLongMap.__init__)
    params = list(sig.parameters.keys())

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

def test_fsmcomparator_exists():
    # Check that the Enumeration exists
    assert FSMComparator is not None

def test_fsmcomparator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FSMComparator]
    expected_literals = [
        "NEQ",
        "GREQ",
        "SMALLER",
        "EQ",
        "SMEQ",
        "GREATER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FSMComparator"

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

def test_fsmcombinator_exists():
    # Check that the Enumeration exists
    assert FSMCombinator is not None

def test_fsmcombinator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FSMCombinator]
    expected_literals = [
        "NAND",
        "NOT",
        "AND",
        "OR",
        "NOR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FSMCombinator"


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
analysis::scheduling::MarkovSchedulingTransition_strategy = st.builds(
    analysis::scheduling::MarkovSchedulingTransition,
    name=
        safe_text,
    firings=
        safe_text
)
PartitionToActorSelectionScheduleMap_strategy = st.builds(
    PartitionToActorSelectionScheduleMap,
)
analysis::partitioning::BalancedPipelinePartition_strategy = st.builds(
    analysis::partitioning::BalancedPipelinePartition,
    commonPredAvg=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    workload=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    preWorkload=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
WorkloadBalancePartition_strategy = st.builds(
    WorkloadBalancePartition,
)
analysis::partitioning::WorkloadBalancePartition_strategy = st.builds(
    analysis::partitioning::WorkloadBalancePartition,
    workload=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ScheduledImpactAnalysisData_strategy = st.builds(
    ScheduledImpactAnalysisData,
)
ComCostPartition_strategy = st.builds(
    ComCostPartition,
)
partitioning::analysis::Network_strategy = st.builds(
    partitioning::analysis::Network,
)
analysis::buffers::OptimalBufferData_strategy = st.builds(
    analysis::buffers::OptimalBufferData,
)
BoundedBuffersReport_strategy = st.builds(
    BoundedBuffersReport,
)
OptimalBufferData_strategy = st.builds(
    OptimalBufferData,
)
buffers::analysis::Buffer_strategy = st.builds(
    buffers::analysis::Buffer,
)
analysis::buffers::BoundedBufferData_strategy = st.builds(
    analysis::buffers::BoundedBufferData,
    tokenSize=
        st.integers(),
    bitSize=
        st.integers()
)
BoundedBufferData_strategy = st.builds(
    BoundedBufferData,
)
buffers::analysis::Network_strategy = st.builds(
    buffers::analysis::Network,
)
BottlenecksWithSchedulingReport_strategy = st.builds(
    BottlenecksWithSchedulingReport,
)
analysis::bottlenecks::DoubleToBottlenecksWithSchedulingReportMap_strategy = st.builds(
    analysis::bottlenecks::DoubleToBottlenecksWithSchedulingReportMap,
    key=
        safe_text
)
DoubleToBottlenecksWithSchedulingReportMap_strategy = st.builds(
    DoubleToBottlenecksWithSchedulingReportMap,
)
analysis::bottlenecks::ScheduledImpactAnalysisData_strategy = st.builds(
    analysis::bottlenecks::ScheduledImpactAnalysisData,
)
BufferToDoubleMap_strategy = st.builds(
    BufferToDoubleMap,
)
BufferToIntegerMap_strategy = st.builds(
    BufferToIntegerMap,
)
analysis::bottlenecks::ActionBottlenecksWithSchedulingData_strategy = st.builds(
    analysis::bottlenecks::ActionBottlenecksWithSchedulingData,
    totalFirings=
        safe_text,
    cpWeight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    cpFirings=
        safe_text,
    totalWeight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
StringToDoubleMap_strategy = st.builds(
    StringToDoubleMap,
)
ActionBottlenecksWithSchedulingData_strategy = st.builds(
    ActionBottlenecksWithSchedulingData,
)
postprocessing::PostProcessingData_strategy = st.builds(
    postprocessing::PostProcessingData,
)
analysis::bottlenecks::DoubleToBottlenecksReportMap_strategy = st.builds(
    analysis::bottlenecks::DoubleToBottlenecksReportMap,
    key=
        safe_text
)
DoubleToBottlenecksReportMap_strategy = st.builds(
    DoubleToBottlenecksReportMap,
)
DoubleToDoubleMap_strategy = st.builds(
    DoubleToDoubleMap,
)
bottlenecks::analysis::ActorClass_strategy = st.builds(
    bottlenecks::analysis::ActorClass,
)
analysis::bottlenecks::ImpactAnalysisData_strategy = st.builds(
    analysis::bottlenecks::ImpactAnalysisData,
)
BottlenecksReport_strategy = st.builds(
    BottlenecksReport,
)
ImpactAnalysisData_strategy = st.builds(
    ImpactAnalysisData,
)
analysis::bottlenecks::ActionBottlenecksData_strategy = st.builds(
    analysis::bottlenecks::ActionBottlenecksData,
    totalWeight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    slackMin=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    slackMax=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    totalVariance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    totalFirings=
        safe_text,
    cpVariance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    cpFirings=
        safe_text,
    cpWeight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ActionBottlenecksData_strategy = st.builds(
    ActionBottlenecksData,
)
bottlenecks::analysis::Network_strategy = st.builds(
    bottlenecks::analysis::Network,
)
analysis::trace::MarkovModelActionData_strategy = st.builds(
    analysis::trace::MarkovModelActionData,
    successors=
        safe_text,
    first=
        st.booleans()
)
MarkovModelActionData_strategy = st.builds(
    MarkovModelActionData,
)
analysis::scheduling::MarkovSchedulingState_strategy = st.builds(
    analysis::scheduling::MarkovSchedulingState,
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
scheduling::analysis::Actor_strategy = st.builds(
    scheduling::analysis::Actor,
)
analysis::scheduling::MarkovPartitionScheduler_strategy = st.builds(
    analysis::scheduling::MarkovPartitionScheduler,
    partitionId=
        safe_text
)
scheduling::analysis::Network_strategy = st.builds(
    scheduling::analysis::Network,
)
MarkovPartitionScheduler_strategy = st.builds(
    MarkovPartitionScheduler,
)
FSMCombination_strategy = st.builds(
    FSMCombination,
)
analysis::scheduling::FSMCondition_strategy = st.builds(
    analysis::scheduling::FSMCondition,
    compval=
        safe_text,
    valName=
        safe_text,
    comp=
        safe_text
)
analysis::scheduling::FSMCombination_strategy = st.builds(
    analysis::scheduling::FSMCombination,
    combinator=
        safe_text
)
FSMVar_strategy = st.builds(
    FSMVar,
)
analysis::scheduling::FSMOperation_strategy = st.builds(
    analysis::scheduling::FSMOperation,
    var=
        safe_text,
    val=
        safe_text,
    op=
        safe_text
)
FSMOperation_strategy = st.builds(
    FSMOperation,
)
analysis::scheduling::FSMVarUpdate_strategy = st.builds(
    analysis::scheduling::FSMVarUpdate,
)
FSMTransition_strategy = st.builds(
    FSMTransition,
)
analysis::scheduling::FSMTransitionWithState_strategy = st.builds(
    analysis::scheduling::FSMTransitionWithState,
)
FSMVarUpdate_strategy = st.builds(
    FSMVarUpdate,
)
analysis::scheduling::FSMState_strategy = st.builds(
    analysis::scheduling::FSMState,
    enumName=
        safe_text
)
Sequence_strategy = st.builds(
    Sequence,
)
FSMCondition_strategy = st.builds(
    FSMCondition,
)
analysis::scheduling::FSMTransition_strategy = st.builds(
    analysis::scheduling::FSMTransition,
    targetStateEnumName=
        safe_text,
    sourceStateEnumName=
        safe_text
)
analysis::scheduling::FSMVar_strategy = st.builds(
    analysis::scheduling::FSMVar,
    initialVal=
        safe_text,
    type=
        safe_text,
    name=
        safe_text
)
ActorFire_strategy = st.builds(
    ActorFire,
)
analysis::scheduling::PartitionedActorFire_strategy = st.builds(
    analysis::scheduling::PartitionedActorFire,
)
analysis::scheduling::ActorSelectionSchedule_strategy = st.builds(
    analysis::scheduling::ActorSelectionSchedule,
)
profiling::analysis::Actor_strategy = st.builds(
    profiling::analysis::Actor,
)
analysis::profiling::IntraActorCommunicationData_strategy = st.builds(
    analysis::profiling::IntraActorCommunicationData,
)
FSMState_strategy = st.builds(
    FSMState,
)
analysis::profiling::ProfilingStatsActorData_strategy = st.builds(
    analysis::profiling::ProfilingStatsActorData,
    actorName=
        safe_text,
    actionsWeightPercent=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    schedulerWeightPercent=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    schedulerWeight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    actionsWeight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ProfilingStatsActorData_strategy = st.builds(
    ProfilingStatsActorData,
)
profiling::analysis::Action_strategy = st.builds(
    profiling::analysis::Action,
)
analysis::profiling::IntraActionCommunicationData_strategy = st.builds(
    analysis::profiling::IntraActionCommunicationData,
)
IntraActionCommunicationData_strategy = st.builds(
    IntraActionCommunicationData,
)
profiling::analysis::StatisticalData_strategy = st.builds(
    profiling::analysis::StatisticalData,
)
profiling::analysis::Network_strategy = st.builds(
    profiling::analysis::Network,
)
IntraActorCommunicationData_strategy = st.builds(
    IntraActorCommunicationData,
)
ActorToStatisticalDataMap_strategy = st.builds(
    ActorToStatisticalDataMap,
)
postprocessing::analysis::StatisticalData_strategy = st.builds(
    postprocessing::analysis::StatisticalData,
)
analysis::postprocessing::SchedulerChecksPartition_strategy = st.builds(
    analysis::postprocessing::SchedulerChecksPartition,
)
SchedulerChecksPartition_strategy = st.builds(
    SchedulerChecksPartition,
)
pipelining::analysis::ActorClass_strategy = st.builds(
    pipelining::analysis::ActorClass,
)
ActionToDoubleMap_strategy = st.builds(
    ActionToDoubleMap,
)
postprocessing::analysis::Actor_strategy = st.builds(
    postprocessing::analysis::Actor,
)
analysis::postprocessing::StatisticalActorPartition_strategy = st.builds(
    analysis::postprocessing::StatisticalActorPartition,
    actors=
        safe_text,
    schedulingPolicy=
        safe_text,
    occupancy=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
StatisticalActorPartition_strategy = st.builds(
    StatisticalActorPartition,
)
analysis::postprocessing::PostProcessingData_strategy = st.builds(
    analysis::postprocessing::PostProcessingData,
)
PostProcessingData_strategy = st.builds(
    PostProcessingData,
)
analysis::postprocessing::BufferBlockingReport_strategy = st.builds(
    analysis::postprocessing::BufferBlockingReport,
)
analysis::postprocessing::SchedulerChecksReport_strategy = st.builds(
    analysis::postprocessing::SchedulerChecksReport,
)
analysis::postprocessing::ActorStatisticsReport_strategy = st.builds(
    analysis::postprocessing::ActorStatisticsReport,
    averageOccupancy=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    occupancyDeviation=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    executionTime=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
analysis::postprocessing::ActionStatisticsReport_strategy = st.builds(
    analysis::postprocessing::ActionStatisticsReport,
)
postprocessing::analysis::Network_strategy = st.builds(
    postprocessing::analysis::Network,
)
analysis::pipelining::ImpactAnalysisData_strategy = st.builds(
    analysis::pipelining::ImpactAnalysisData,
    cpReduction=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ActionsVariablePipeliningReport_strategy = st.builds(
    ActionsVariablePipeliningReport,
)
pipelining::analysis::StatisticalData_strategy = st.builds(
    pipelining::analysis::StatisticalData,
)
pipelining::analysis::Action_strategy = st.builds(
    pipelining::analysis::Action,
)
analysis::pipelining::ActionVariablePipeliningData_strategy = st.builds(
    analysis::pipelining::ActionVariablePipeliningData,
    pipelinable=
        st.booleans()
)
ActionVariablePipeliningData_strategy = st.builds(
    ActionVariablePipeliningData,
)
pipelining::analysis::Network_strategy = st.builds(
    pipelining::analysis::Network,
)
BalancedPipelinePartition_strategy = st.builds(
    BalancedPipelinePartition,
)
partitioning::analysis::Actor_strategy = st.builds(
    partitioning::analysis::Actor,
)
analysis::partitioning::ComCostPartition_strategy = st.builds(
    analysis::partitioning::ComCostPartition,
    internalCost=
        safe_text,
    externalCost=
        safe_text
)
ActionToStatisticalDataMap_strategy = st.builds(
    ActionToStatisticalDataMap,
)
profiler::analysis::StatisticalData_strategy = st.builds(
    profiler::analysis::StatisticalData,
)
profiler::analysis::Buffer_strategy = st.builds(
    profiler::analysis::Buffer,
)
analysis::profiler::BufferDynamicData_strategy = st.builds(
    analysis::profiler::BufferDynamicData,
    unconsumedTokens=
        st.integers()
)
profiler::analysis::Action_strategy = st.builds(
    profiler::analysis::Action,
)
profiler::analysis::Actor_strategy = st.builds(
    profiler::analysis::Actor,
)
ComplexDynamicData_strategy = st.builds(
    ComplexDynamicData,
)
analysis::profiler::ActionDynamicData_strategy = st.builds(
    analysis::profiler::ActionDynamicData,
)
analysis::profiler::ActorDynamicData_strategy = st.builds(
    analysis::profiler::ActorDynamicData,
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
analysis::profiler::ComplexCodeData_strategy = st.builds(
    analysis::profiler::ComplexCodeData,
)
StringToIntegerMap_strategy = st.builds(
    StringToIntegerMap,
)
analysis::profiler::CodeData_strategy = st.builds(
    analysis::profiler::CodeData,
    nol=
        safe_text,
    blockName=
        safe_text
)
ComplexCodeData_strategy = st.builds(
    ComplexCodeData,
)
profiler::analysis::Network_strategy = st.builds(
    profiler::analysis::Network,
)
AnalysisReport_strategy = st.builds(
    AnalysisReport,
)
analysis::partitioning::ComCostPartitioningReport_strategy = st.builds(
    analysis::partitioning::ComCostPartitioningReport,
    bitAccurate=
        st.booleans()
)
analysis::buffers::BoundedBuffersReport_strategy = st.builds(
    analysis::buffers::BoundedBuffersReport,
    bitSize=
        st.integers(),
    pow2=
        st.booleans(),
    bitAccurate=
        st.booleans(),
    tokenSize=
        st.integers()
)
analysis::pipelining::ActionsVariablePipeliningReport_strategy = st.builds(
    analysis::pipelining::ActionsVariablePipeliningReport,
)
analysis::bottlenecks::BottlenecksReport_strategy = st.builds(
    analysis::bottlenecks::BottlenecksReport,
    totalFirings=
        safe_text,
    cpVariance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    totalWeight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    cpWeight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    totalVariance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    cpFirings=
        safe_text
)
analysis::profiler::DynamicProfilingReport_strategy = st.builds(
    analysis::profiler::DynamicProfilingReport,
)
analysis::bottlenecks::BottlenecksWithSchedulingReport_strategy = st.builds(
    analysis::bottlenecks::BottlenecksWithSchedulingReport,
    executionTime=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    cpWeight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    totalFirings=
        safe_text,
    cpBlockingTime=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    cpFirings=
        safe_text,
    totalWeight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
analysis::scheduling::MarkovSimpleSchedulerReport_strategy = st.builds(
    analysis::scheduling::MarkovSimpleSchedulerReport,
)
analysis::buffers::OptimalBuffersReport_strategy = st.builds(
    analysis::buffers::OptimalBuffersReport,
    bitAccurate=
        st.booleans(),
    pow2=
        st.booleans()
)
analysis::profiling::ProfilingStatsReport_strategy = st.builds(
    analysis::profiling::ProfilingStatsReport,
    networkName=
        safe_text
)
analysis::trace::MarkowModelTraceReport_strategy = st.builds(
    analysis::trace::MarkowModelTraceReport,
)
analysis::partitioning::WorkloadBalancePartitioningReport_strategy = st.builds(
    analysis::partitioning::WorkloadBalancePartitioningReport,
)
analysis::postprocessing::PostProcessingReport_strategy = st.builds(
    analysis::postprocessing::PostProcessingReport,
    deadlock=
        st.booleans(),
    time=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
analysis::bottlenecks::ImpactAnalysisReport_strategy = st.builds(
    analysis::bottlenecks::ImpactAnalysisReport,
    classLevel=
        st.booleans()
)
analysis::pipelining::ImpactAnalysisReport_strategy = st.builds(
    analysis::pipelining::ImpactAnalysisReport,
)
analysis::caseoptimal::CaseOptimalScheduleReport_strategy = st.builds(
    analysis::caseoptimal::CaseOptimalScheduleReport,
    traceFile=
        safe_text,
    partitionFilePath=
        safe_text,
    pipeline=
        safe_text
)
analysis::bottlenecks::ScheduledImpactAnalysisReport_strategy = st.builds(
    analysis::bottlenecks::ScheduledImpactAnalysisReport,
    classLevel=
        st.booleans()
)
analysis::profiling::IntraActionCommunicationReport_strategy = st.builds(
    analysis::profiling::IntraActionCommunicationReport,
)
analysis::partitioning::BalancedPipelinePartitioningReport_strategy = st.builds(
    analysis::partitioning::BalancedPipelinePartitioningReport,
)
analysis::profiler::CodeProfilingReport_strategy = st.builds(
    analysis::profiler::CodeProfilingReport,
)
analysis::AnalysisReport_strategy = st.builds(
    analysis::AnalysisReport,
    date=
        st.dates(),
    algorithm=
        safe_text
)
analysis::trace::ComparedAction_strategy = st.builds(
    analysis::trace::ComparedAction,
    found=
        st.booleans(),
    dSteps=
        safe_text,
    dIncomings=
        safe_text,
    dOutgoings=
        safe_text
)
ComparedAction_strategy = st.builds(
    ComparedAction,
)
bottlenecks::analysis::Action_strategy = st.builds(
    bottlenecks::analysis::Action,
)
analysis::trace::ComparedTrace_strategy = st.builds(
    analysis::trace::ComparedTrace,
    equal=
        st.booleans(),
    dSteps=
        safe_text,
    dDependencies=
        safe_text
)
ComparedTrace_strategy = st.builds(
    ComparedTrace,
)
CompressedTraceReport_strategy = st.builds(
    CompressedTraceReport,
)
analysis::trace::TraceComparatorReport_strategy = st.builds(
    analysis::trace::TraceComparatorReport,
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
analysis::trace::CompressedDependency_strategy = st.builds(
    analysis::trace::CompressedDependency,
    count=
        safe_text
)
trace::analysis::Action_strategy = st.builds(
    trace::analysis::Action,
)
analysis::trace::CompressedStep_strategy = st.builds(
    analysis::trace::CompressedStep,
    count=
        safe_text
)
CompressedDependency_strategy = st.builds(
    CompressedDependency,
)
analysis::trace::CompressedPortDependency_strategy = st.builds(
    analysis::trace::CompressedPortDependency,
)
analysis::trace::CompressedGuardDependency_strategy = st.builds(
    analysis::trace::CompressedGuardDependency,
)
analysis::trace::CompressedTokensDependency_strategy = st.builds(
    analysis::trace::CompressedTokensDependency,
)
analysis::trace::CompressedVariableDependency_strategy = st.builds(
    analysis::trace::CompressedVariableDependency,
)
analysis::trace::CompressedFsmDependency_strategy = st.builds(
    analysis::trace::CompressedFsmDependency,
)
CompressedStep_strategy = st.builds(
    CompressedStep,
)
analysis::trace::CompressedTraceReport_strategy = st.builds(
    analysis::trace::CompressedTraceReport,
    traceFile=
        safe_text
)
trace::analysis::Network_strategy = st.builds(
    trace::analysis::Network,
)
StringToLongMap_strategy = st.builds(
    StringToLongMap,
)
analysis::map::ActionToDoubleMap_strategy = st.builds(
    analysis::map::ActionToDoubleMap,
    value=
        safe_text
)
ActorToLongMap_strategy = st.builds(
    ActorToLongMap,
)
analysis::trace::TraceSizeReport_strategy = st.builds(
    analysis::trace::TraceSizeReport,
    dependencies=
        safe_text,
    firings=
        safe_text
)
analysis::map::StringToStringMap_strategy = st.builds(
    analysis::map::StringToStringMap,
    value=
        safe_text,
    key=
        safe_text
)
ActorSelectionSchedule_strategy = st.builds(
    ActorSelectionSchedule,
)
analysis::scheduling::FSM_strategy = st.builds(
    analysis::scheduling::FSM,
    terminalState=
        safe_text,
    startState=
        safe_text
)
analysis::scheduling::ActorFire_strategy = st.builds(
    analysis::scheduling::ActorFire,
    Actor=
        safe_text,
    partition=
        safe_text,
    dependencyPartitions=
        safe_text,
    Times=
        st.integers()
)
analysis::caseoptimal::CaseOptimalActorSelectionSchedule_strategy = st.builds(
    analysis::caseoptimal::CaseOptimalActorSelectionSchedule,
)
analysis::scheduling::Sequence_strategy = st.builds(
    analysis::scheduling::Sequence,
)
analysis::map::PartitionToActorSelectionScheduleMap_strategy = st.builds(
    analysis::map::PartitionToActorSelectionScheduleMap,
    key=
        safe_text
)
analysis::map::BufferToDoubleMap_strategy = st.builds(
    analysis::map::BufferToDoubleMap,
    value=
        safe_text
)
analysis::map::BufferToIntegerMap_strategy = st.builds(
    analysis::map::BufferToIntegerMap,
    value=
        safe_text
)
map::analysis::Procedure_strategy = st.builds(
    map::analysis::Procedure,
)
analysis::map::StringToDoubleMap_strategy = st.builds(
    analysis::map::StringToDoubleMap,
    key=
        safe_text,
    value=
        safe_text
)
map::analysis::Port_strategy = st.builds(
    map::analysis::Port,
)
analysis::map::PortToLongMap_strategy = st.builds(
    analysis::map::PortToLongMap,
    value=
        safe_text
)
map::analysis::Guard_strategy = st.builds(
    map::analysis::Guard,
)
analysis::map::GuardToLongMap_strategy = st.builds(
    analysis::map::GuardToLongMap,
    value=
        safe_text
)
analysis::map::VariableToLongMap_strategy = st.builds(
    analysis::map::VariableToLongMap,
    value=
        safe_text
)
analysis::map::DoubleToDoubleMap_strategy = st.builds(
    analysis::map::DoubleToDoubleMap,
    key=
        safe_text,
    value=
        safe_text
)
analysis::map::StringToLongMap_strategy = st.builds(
    analysis::map::StringToLongMap,
    key=
        safe_text,
    value=
        safe_text
)
analysis::map::BufferToLongMap_strategy = st.builds(
    analysis::map::BufferToLongMap,
    value=
        safe_text
)
analysis::map::ActorToLongMap_strategy = st.builds(
    analysis::map::ActorToLongMap,
    value=
        safe_text
)
analysis::map::ActionToLongMap_strategy = st.builds(
    analysis::map::ActionToLongMap,
    value=
        safe_text
)
analysis::map::EOperatorToStatisticalDataMap_strategy = st.builds(
    analysis::map::EOperatorToStatisticalDataMap,
    key=
        safe_text
)
map::analysis::ActorClass_strategy = st.builds(
    map::analysis::ActorClass,
)
analysis::map::ActorClassToStatisticalDataMap_strategy = st.builds(
    analysis::map::ActorClassToStatisticalDataMap,
)
map::analysis::Variable_strategy = st.builds(
    map::analysis::Variable,
)
analysis::map::VariableToStatisticalDataMap_strategy = st.builds(
    analysis::map::VariableToStatisticalDataMap,
)
analysis::map::ProcedureToStatisticalDataMap_strategy = st.builds(
    analysis::map::ProcedureToStatisticalDataMap,
)
map::analysis::Buffer_strategy = st.builds(
    map::analysis::Buffer,
)
analysis::map::BufferToStatisticalDataMap_strategy = st.builds(
    analysis::map::BufferToStatisticalDataMap,
)
map::analysis::Action_strategy = st.builds(
    map::analysis::Action,
)
analysis::map::ActionToStatisticalDataMap_strategy = st.builds(
    analysis::map::ActionToStatisticalDataMap,
)
map::analysis::StatisticalData_strategy = st.builds(
    map::analysis::StatisticalData,
)
map::analysis::Actor_strategy = st.builds(
    map::analysis::Actor,
)
analysis::map::ActorToStatisticalDataMap_strategy = st.builds(
    analysis::map::ActorToStatisticalDataMap,
)
analysis::map::StringToIntegerMap_strategy = st.builds(
    analysis::map::StringToIntegerMap,
    value=
        safe_text,
    key=
        safe_text
)
StringToStringMap_strategy = st.builds(
    StringToStringMap,
)
analysis::profiler::TableRow_strategy = st.builds(
    analysis::profiler::TableRow,
)
TableRow_strategy = st.builds(
    TableRow,
)
analysis::profiler::BenchmarkReport_strategy = st.builds(
    analysis::profiler::BenchmarkReport,
    column_names=
        safe_text
)
AccessData_strategy = st.builds(
    AccessData,
)
analysis::profiler::StringToAccessDataMap_strategy = st.builds(
    analysis::profiler::StringToAccessDataMap,
    key=
        safe_text
)
analysis::profiler::AccessData_strategy = st.builds(
    analysis::profiler::AccessData,
    accesses=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    total=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    min=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    average=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    max=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
profiler::analysis::Procedure_strategy = st.builds(
    profiler::analysis::Procedure,
)
StringToAccessDataMap_strategy = st.builds(
    StringToAccessDataMap,
)
analysis::profiler::MemoryAccessData_strategy = st.builds(
    analysis::profiler::MemoryAccessData,
)
MemoryAccessData_strategy = st.builds(
    MemoryAccessData,
)
analysis::profiler::SharedVariableAccessData_strategy = st.builds(
    analysis::profiler::SharedVariableAccessData,
    name=
        safe_text
)
analysis::profiler::BufferAccessData_strategy = st.builds(
    analysis::profiler::BufferAccessData,
    sourceActor=
        safe_text,
    targetActor=
        safe_text,
    targetPort=
        safe_text,
    sourcePort=
        safe_text
)
analysis::profiler::LocalVariableAccessData_strategy = st.builds(
    analysis::profiler::LocalVariableAccessData,
    name=
        safe_text
)
analysis::profiler::StateVariableAccessData_strategy = st.builds(
    analysis::profiler::StateVariableAccessData,
    name=
        safe_text
)
analysis::profiler::ActionMemoryProfilingData_strategy = st.builds(
    analysis::profiler::ActionMemoryProfilingData,
    actor=
        safe_text,
    action=
        safe_text
)
ActionMemoryProfilingData_strategy = st.builds(
    ActionMemoryProfilingData,
)
analysis::profiler::MemoryProfilingReport_strategy = st.builds(
    analysis::profiler::MemoryProfilingReport,
    networkName=
        safe_text
)
ActionDynamicData_strategy = st.builds(
    ActionDynamicData,
)
analysis::profiler::ProcedureToComplexDynamicDataMap_strategy = st.builds(
    analysis::profiler::ProcedureToComplexDynamicDataMap,
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
analysis::profiler::ComplexDynamicData_strategy = st.builds(
    analysis::profiler::ComplexDynamicData,
)
ActionToLongMap_strategy = st.builds(
    ActionToLongMap,
)

@given(instance=analysis::scheduling::MarkovSchedulingTransition_strategy)
@settings(max_examples=50)
def test_analysis::scheduling::markovschedulingtransition_instantiation(instance):
    assert isinstance(instance, analysis::scheduling::MarkovSchedulingTransition)

@given(instance=analysis::scheduling::MarkovSchedulingTransition_strategy)
def test_analysis::scheduling::markovschedulingtransition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=analysis::scheduling::MarkovSchedulingTransition_strategy)
def test_analysis::scheduling::markovschedulingtransition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=analysis::scheduling::MarkovSchedulingTransition_strategy)
def test_analysis::scheduling::markovschedulingtransition_firings_type(instance):
    assert isinstance(instance.firings, str)


@given(instance=analysis::scheduling::MarkovSchedulingTransition_strategy)
def test_analysis::scheduling::markovschedulingtransition_firings_setter(instance):
    original = instance.firings
    instance.firings = original
    assert instance.firings == original

@given(instance=PartitionToActorSelectionScheduleMap_strategy)
@settings(max_examples=50)
def test_partitiontoactorselectionschedulemap_instantiation(instance):
    assert isinstance(instance, PartitionToActorSelectionScheduleMap)

@given(instance=analysis::partitioning::BalancedPipelinePartition_strategy)
@settings(max_examples=50)
def test_analysis::partitioning::balancedpipelinepartition_instantiation(instance):
    assert isinstance(instance, analysis::partitioning::BalancedPipelinePartition)

@given(instance=analysis::partitioning::BalancedPipelinePartition_strategy)
def test_analysis::partitioning::balancedpipelinepartition_commonPredAvg_type(instance):
    assert isinstance(instance.commonPredAvg, float)


@given(instance=analysis::partitioning::BalancedPipelinePartition_strategy)
def test_analysis::partitioning::balancedpipelinepartition_commonPredAvg_setter(instance):
    original = instance.commonPredAvg
    instance.commonPredAvg = original
    assert instance.commonPredAvg == original

@given(instance=analysis::partitioning::BalancedPipelinePartition_strategy)
def test_analysis::partitioning::balancedpipelinepartition_workload_type(instance):
    assert isinstance(instance.workload, float)


@given(instance=analysis::partitioning::BalancedPipelinePartition_strategy)
def test_analysis::partitioning::balancedpipelinepartition_workload_setter(instance):
    original = instance.workload
    instance.workload = original
    assert instance.workload == original

@given(instance=analysis::partitioning::BalancedPipelinePartition_strategy)
def test_analysis::partitioning::balancedpipelinepartition_preWorkload_type(instance):
    assert isinstance(instance.preWorkload, float)


@given(instance=analysis::partitioning::BalancedPipelinePartition_strategy)
def test_analysis::partitioning::balancedpipelinepartition_preWorkload_setter(instance):
    original = instance.preWorkload
    instance.preWorkload = original
    assert instance.preWorkload == original

@given(instance=WorkloadBalancePartition_strategy)
@settings(max_examples=50)
def test_workloadbalancepartition_instantiation(instance):
    assert isinstance(instance, WorkloadBalancePartition)

@given(instance=analysis::partitioning::WorkloadBalancePartition_strategy)
@settings(max_examples=50)
def test_analysis::partitioning::workloadbalancepartition_instantiation(instance):
    assert isinstance(instance, analysis::partitioning::WorkloadBalancePartition)

@given(instance=analysis::partitioning::WorkloadBalancePartition_strategy)
def test_analysis::partitioning::workloadbalancepartition_workload_type(instance):
    assert isinstance(instance.workload, float)


@given(instance=analysis::partitioning::WorkloadBalancePartition_strategy)
def test_analysis::partitioning::workloadbalancepartition_workload_setter(instance):
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

@given(instance=partitioning::analysis::Network_strategy)
@settings(max_examples=50)
def test_partitioning::analysis::network_instantiation(instance):
    assert isinstance(instance, partitioning::analysis::Network)

@given(instance=analysis::buffers::OptimalBufferData_strategy)
@settings(max_examples=50)
def test_analysis::buffers::optimalbufferdata_instantiation(instance):
    assert isinstance(instance, analysis::buffers::OptimalBufferData)

@given(instance=BoundedBuffersReport_strategy)
@settings(max_examples=50)
def test_boundedbuffersreport_instantiation(instance):
    assert isinstance(instance, BoundedBuffersReport)

@given(instance=OptimalBufferData_strategy)
@settings(max_examples=50)
def test_optimalbufferdata_instantiation(instance):
    assert isinstance(instance, OptimalBufferData)

@given(instance=buffers::analysis::Buffer_strategy)
@settings(max_examples=50)
def test_buffers::analysis::buffer_instantiation(instance):
    assert isinstance(instance, buffers::analysis::Buffer)

@given(instance=analysis::buffers::BoundedBufferData_strategy)
@settings(max_examples=50)
def test_analysis::buffers::boundedbufferdata_instantiation(instance):
    assert isinstance(instance, analysis::buffers::BoundedBufferData)

@given(instance=analysis::buffers::BoundedBufferData_strategy)
def test_analysis::buffers::boundedbufferdata_tokenSize_type(instance):
    assert isinstance(instance.tokenSize, int)


@given(instance=analysis::buffers::BoundedBufferData_strategy)
def test_analysis::buffers::boundedbufferdata_tokenSize_setter(instance):
    original = instance.tokenSize
    instance.tokenSize = original
    assert instance.tokenSize == original

@given(instance=analysis::buffers::BoundedBufferData_strategy)
def test_analysis::buffers::boundedbufferdata_bitSize_type(instance):
    assert isinstance(instance.bitSize, int)


@given(instance=analysis::buffers::BoundedBufferData_strategy)
def test_analysis::buffers::boundedbufferdata_bitSize_setter(instance):
    original = instance.bitSize
    instance.bitSize = original
    assert instance.bitSize == original

@given(instance=BoundedBufferData_strategy)
@settings(max_examples=50)
def test_boundedbufferdata_instantiation(instance):
    assert isinstance(instance, BoundedBufferData)

@given(instance=buffers::analysis::Network_strategy)
@settings(max_examples=50)
def test_buffers::analysis::network_instantiation(instance):
    assert isinstance(instance, buffers::analysis::Network)

@given(instance=BottlenecksWithSchedulingReport_strategy)
@settings(max_examples=50)
def test_bottleneckswithschedulingreport_instantiation(instance):
    assert isinstance(instance, BottlenecksWithSchedulingReport)

@given(instance=analysis::bottlenecks::DoubleToBottlenecksWithSchedulingReportMap_strategy)
@settings(max_examples=50)
def test_analysis::bottlenecks::doubletobottleneckswithschedulingreportmap_instantiation(instance):
    assert isinstance(instance, analysis::bottlenecks::DoubleToBottlenecksWithSchedulingReportMap)

@given(instance=analysis::bottlenecks::DoubleToBottlenecksWithSchedulingReportMap_strategy)
def test_analysis::bottlenecks::doubletobottleneckswithschedulingreportmap_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=analysis::bottlenecks::DoubleToBottlenecksWithSchedulingReportMap_strategy)
def test_analysis::bottlenecks::doubletobottleneckswithschedulingreportmap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=DoubleToBottlenecksWithSchedulingReportMap_strategy)
@settings(max_examples=50)
def test_doubletobottleneckswithschedulingreportmap_instantiation(instance):
    assert isinstance(instance, DoubleToBottlenecksWithSchedulingReportMap)

@given(instance=analysis::bottlenecks::ScheduledImpactAnalysisData_strategy)
@settings(max_examples=50)
def test_analysis::bottlenecks::scheduledimpactanalysisdata_instantiation(instance):
    assert isinstance(instance, analysis::bottlenecks::ScheduledImpactAnalysisData)

@given(instance=BufferToDoubleMap_strategy)
@settings(max_examples=50)
def test_buffertodoublemap_instantiation(instance):
    assert isinstance(instance, BufferToDoubleMap)

@given(instance=BufferToIntegerMap_strategy)
@settings(max_examples=50)
def test_buffertointegermap_instantiation(instance):
    assert isinstance(instance, BufferToIntegerMap)

@given(instance=analysis::bottlenecks::ActionBottlenecksWithSchedulingData_strategy)
@settings(max_examples=50)
def test_analysis::bottlenecks::actionbottleneckswithschedulingdata_instantiation(instance):
    assert isinstance(instance, analysis::bottlenecks::ActionBottlenecksWithSchedulingData)

@given(instance=analysis::bottlenecks::ActionBottlenecksWithSchedulingData_strategy)
def test_analysis::bottlenecks::actionbottleneckswithschedulingdata_totalFirings_type(instance):
    assert isinstance(instance.totalFirings, str)


@given(instance=analysis::bottlenecks::ActionBottlenecksWithSchedulingData_strategy)
def test_analysis::bottlenecks::actionbottleneckswithschedulingdata_totalFirings_setter(instance):
    original = instance.totalFirings
    instance.totalFirings = original
    assert instance.totalFirings == original

@given(instance=analysis::bottlenecks::ActionBottlenecksWithSchedulingData_strategy)
def test_analysis::bottlenecks::actionbottleneckswithschedulingdata_cpWeight_type(instance):
    assert isinstance(instance.cpWeight, float)


@given(instance=analysis::bottlenecks::ActionBottlenecksWithSchedulingData_strategy)
def test_analysis::bottlenecks::actionbottleneckswithschedulingdata_cpWeight_setter(instance):
    original = instance.cpWeight
    instance.cpWeight = original
    assert instance.cpWeight == original

@given(instance=analysis::bottlenecks::ActionBottlenecksWithSchedulingData_strategy)
def test_analysis::bottlenecks::actionbottleneckswithschedulingdata_cpFirings_type(instance):
    assert isinstance(instance.cpFirings, str)


@given(instance=analysis::bottlenecks::ActionBottlenecksWithSchedulingData_strategy)
def test_analysis::bottlenecks::actionbottleneckswithschedulingdata_cpFirings_setter(instance):
    original = instance.cpFirings
    instance.cpFirings = original
    assert instance.cpFirings == original

@given(instance=analysis::bottlenecks::ActionBottlenecksWithSchedulingData_strategy)
def test_analysis::bottlenecks::actionbottleneckswithschedulingdata_totalWeight_type(instance):
    assert isinstance(instance.totalWeight, float)


@given(instance=analysis::bottlenecks::ActionBottlenecksWithSchedulingData_strategy)
def test_analysis::bottlenecks::actionbottleneckswithschedulingdata_totalWeight_setter(instance):
    original = instance.totalWeight
    instance.totalWeight = original
    assert instance.totalWeight == original

@given(instance=StringToDoubleMap_strategy)
@settings(max_examples=50)
def test_stringtodoublemap_instantiation(instance):
    assert isinstance(instance, StringToDoubleMap)

@given(instance=ActionBottlenecksWithSchedulingData_strategy)
@settings(max_examples=50)
def test_actionbottleneckswithschedulingdata_instantiation(instance):
    assert isinstance(instance, ActionBottlenecksWithSchedulingData)

@given(instance=postprocessing::PostProcessingData_strategy)
@settings(max_examples=50)
def test_postprocessing::postprocessingdata_instantiation(instance):
    assert isinstance(instance, postprocessing::PostProcessingData)

@given(instance=analysis::bottlenecks::DoubleToBottlenecksReportMap_strategy)
@settings(max_examples=50)
def test_analysis::bottlenecks::doubletobottlenecksreportmap_instantiation(instance):
    assert isinstance(instance, analysis::bottlenecks::DoubleToBottlenecksReportMap)

@given(instance=analysis::bottlenecks::DoubleToBottlenecksReportMap_strategy)
def test_analysis::bottlenecks::doubletobottlenecksreportmap_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=analysis::bottlenecks::DoubleToBottlenecksReportMap_strategy)
def test_analysis::bottlenecks::doubletobottlenecksreportmap_key_setter(instance):
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

@given(instance=bottlenecks::analysis::ActorClass_strategy)
@settings(max_examples=50)
def test_bottlenecks::analysis::actorclass_instantiation(instance):
    assert isinstance(instance, bottlenecks::analysis::ActorClass)

@given(instance=analysis::bottlenecks::ImpactAnalysisData_strategy)
@settings(max_examples=50)
def test_analysis::bottlenecks::impactanalysisdata_instantiation(instance):
    assert isinstance(instance, analysis::bottlenecks::ImpactAnalysisData)

@given(instance=BottlenecksReport_strategy)
@settings(max_examples=50)
def test_bottlenecksreport_instantiation(instance):
    assert isinstance(instance, BottlenecksReport)

@given(instance=ImpactAnalysisData_strategy)
@settings(max_examples=50)
def test_impactanalysisdata_instantiation(instance):
    assert isinstance(instance, ImpactAnalysisData)

@given(instance=analysis::bottlenecks::ActionBottlenecksData_strategy)
@settings(max_examples=50)
def test_analysis::bottlenecks::actionbottlenecksdata_instantiation(instance):
    assert isinstance(instance, analysis::bottlenecks::ActionBottlenecksData)

@given(instance=analysis::bottlenecks::ActionBottlenecksData_strategy)
def test_analysis::bottlenecks::actionbottlenecksdata_totalWeight_type(instance):
    assert isinstance(instance.totalWeight, float)


@given(instance=analysis::bottlenecks::ActionBottlenecksData_strategy)
def test_analysis::bottlenecks::actionbottlenecksdata_totalWeight_setter(instance):
    original = instance.totalWeight
    instance.totalWeight = original
    assert instance.totalWeight == original

@given(instance=analysis::bottlenecks::ActionBottlenecksData_strategy)
def test_analysis::bottlenecks::actionbottlenecksdata_slackMin_type(instance):
    assert isinstance(instance.slackMin, float)


@given(instance=analysis::bottlenecks::ActionBottlenecksData_strategy)
def test_analysis::bottlenecks::actionbottlenecksdata_slackMin_setter(instance):
    original = instance.slackMin
    instance.slackMin = original
    assert instance.slackMin == original

@given(instance=analysis::bottlenecks::ActionBottlenecksData_strategy)
def test_analysis::bottlenecks::actionbottlenecksdata_slackMax_type(instance):
    assert isinstance(instance.slackMax, float)


@given(instance=analysis::bottlenecks::ActionBottlenecksData_strategy)
def test_analysis::bottlenecks::actionbottlenecksdata_slackMax_setter(instance):
    original = instance.slackMax
    instance.slackMax = original
    assert instance.slackMax == original

@given(instance=analysis::bottlenecks::ActionBottlenecksData_strategy)
def test_analysis::bottlenecks::actionbottlenecksdata_totalVariance_type(instance):
    assert isinstance(instance.totalVariance, float)


@given(instance=analysis::bottlenecks::ActionBottlenecksData_strategy)
def test_analysis::bottlenecks::actionbottlenecksdata_totalVariance_setter(instance):
    original = instance.totalVariance
    instance.totalVariance = original
    assert instance.totalVariance == original

@given(instance=analysis::bottlenecks::ActionBottlenecksData_strategy)
def test_analysis::bottlenecks::actionbottlenecksdata_totalFirings_type(instance):
    assert isinstance(instance.totalFirings, str)


@given(instance=analysis::bottlenecks::ActionBottlenecksData_strategy)
def test_analysis::bottlenecks::actionbottlenecksdata_totalFirings_setter(instance):
    original = instance.totalFirings
    instance.totalFirings = original
    assert instance.totalFirings == original

@given(instance=analysis::bottlenecks::ActionBottlenecksData_strategy)
def test_analysis::bottlenecks::actionbottlenecksdata_cpVariance_type(instance):
    assert isinstance(instance.cpVariance, float)


@given(instance=analysis::bottlenecks::ActionBottlenecksData_strategy)
def test_analysis::bottlenecks::actionbottlenecksdata_cpVariance_setter(instance):
    original = instance.cpVariance
    instance.cpVariance = original
    assert instance.cpVariance == original

@given(instance=analysis::bottlenecks::ActionBottlenecksData_strategy)
def test_analysis::bottlenecks::actionbottlenecksdata_cpFirings_type(instance):
    assert isinstance(instance.cpFirings, str)


@given(instance=analysis::bottlenecks::ActionBottlenecksData_strategy)
def test_analysis::bottlenecks::actionbottlenecksdata_cpFirings_setter(instance):
    original = instance.cpFirings
    instance.cpFirings = original
    assert instance.cpFirings == original

@given(instance=analysis::bottlenecks::ActionBottlenecksData_strategy)
def test_analysis::bottlenecks::actionbottlenecksdata_cpWeight_type(instance):
    assert isinstance(instance.cpWeight, float)


@given(instance=analysis::bottlenecks::ActionBottlenecksData_strategy)
def test_analysis::bottlenecks::actionbottlenecksdata_cpWeight_setter(instance):
    original = instance.cpWeight
    instance.cpWeight = original
    assert instance.cpWeight == original

@given(instance=ActionBottlenecksData_strategy)
@settings(max_examples=50)
def test_actionbottlenecksdata_instantiation(instance):
    assert isinstance(instance, ActionBottlenecksData)

@given(instance=bottlenecks::analysis::Network_strategy)
@settings(max_examples=50)
def test_bottlenecks::analysis::network_instantiation(instance):
    assert isinstance(instance, bottlenecks::analysis::Network)

@given(instance=analysis::trace::MarkovModelActionData_strategy)
@settings(max_examples=50)
def test_analysis::trace::markovmodelactiondata_instantiation(instance):
    assert isinstance(instance, analysis::trace::MarkovModelActionData)

@given(instance=analysis::trace::MarkovModelActionData_strategy)
def test_analysis::trace::markovmodelactiondata_successors_type(instance):
    assert isinstance(instance.successors, str)


@given(instance=analysis::trace::MarkovModelActionData_strategy)
def test_analysis::trace::markovmodelactiondata_successors_setter(instance):
    original = instance.successors
    instance.successors = original
    assert instance.successors == original

@given(instance=analysis::trace::MarkovModelActionData_strategy)
def test_analysis::trace::markovmodelactiondata_first_type(instance):
    assert isinstance(instance.first, bool)


@given(instance=analysis::trace::MarkovModelActionData_strategy)
def test_analysis::trace::markovmodelactiondata_first_setter(instance):
    original = instance.first
    instance.first = original
    assert instance.first == original

@given(instance=MarkovModelActionData_strategy)
@settings(max_examples=50)
def test_markovmodelactiondata_instantiation(instance):
    assert isinstance(instance, MarkovModelActionData)

@given(instance=analysis::scheduling::MarkovSchedulingState_strategy)
@settings(max_examples=50)
def test_analysis::scheduling::markovschedulingstate_instantiation(instance):
    assert isinstance(instance, analysis::scheduling::MarkovSchedulingState)

@given(instance=analysis::scheduling::MarkovSchedulingState_strategy)
def test_analysis::scheduling::markovschedulingstate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=analysis::scheduling::MarkovSchedulingState_strategy)
def test_analysis::scheduling::markovschedulingstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=analysis::scheduling::MarkovSchedulingState_strategy)
def test_analysis::scheduling::markovschedulingstate_firings_type(instance):
    assert isinstance(instance.firings, str)


@given(instance=analysis::scheduling::MarkovSchedulingState_strategy)
def test_analysis::scheduling::markovschedulingstate_firings_setter(instance):
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

@given(instance=scheduling::analysis::Actor_strategy)
@settings(max_examples=50)
def test_scheduling::analysis::actor_instantiation(instance):
    assert isinstance(instance, scheduling::analysis::Actor)

@given(instance=analysis::scheduling::MarkovPartitionScheduler_strategy)
@settings(max_examples=50)
def test_analysis::scheduling::markovpartitionscheduler_instantiation(instance):
    assert isinstance(instance, analysis::scheduling::MarkovPartitionScheduler)

@given(instance=analysis::scheduling::MarkovPartitionScheduler_strategy)
def test_analysis::scheduling::markovpartitionscheduler_partitionId_type(instance):
    assert isinstance(instance.partitionId, str)


@given(instance=analysis::scheduling::MarkovPartitionScheduler_strategy)
def test_analysis::scheduling::markovpartitionscheduler_partitionId_setter(instance):
    original = instance.partitionId
    instance.partitionId = original
    assert instance.partitionId == original

@given(instance=scheduling::analysis::Network_strategy)
@settings(max_examples=50)
def test_scheduling::analysis::network_instantiation(instance):
    assert isinstance(instance, scheduling::analysis::Network)

@given(instance=MarkovPartitionScheduler_strategy)
@settings(max_examples=50)
def test_markovpartitionscheduler_instantiation(instance):
    assert isinstance(instance, MarkovPartitionScheduler)

@given(instance=FSMCombination_strategy)
@settings(max_examples=50)
def test_fsmcombination_instantiation(instance):
    assert isinstance(instance, FSMCombination)

@given(instance=analysis::scheduling::FSMCondition_strategy)
@settings(max_examples=50)
def test_analysis::scheduling::fsmcondition_instantiation(instance):
    assert isinstance(instance, analysis::scheduling::FSMCondition)

@given(instance=analysis::scheduling::FSMCondition_strategy)
def test_analysis::scheduling::fsmcondition_compval_type(instance):
    assert isinstance(instance.compval, str)


@given(instance=analysis::scheduling::FSMCondition_strategy)
def test_analysis::scheduling::fsmcondition_compval_setter(instance):
    original = instance.compval
    instance.compval = original
    assert instance.compval == original

@given(instance=analysis::scheduling::FSMCondition_strategy)
def test_analysis::scheduling::fsmcondition_valName_type(instance):
    assert isinstance(instance.valName, str)


@given(instance=analysis::scheduling::FSMCondition_strategy)
def test_analysis::scheduling::fsmcondition_valName_setter(instance):
    original = instance.valName
    instance.valName = original
    assert instance.valName == original

@given(instance=analysis::scheduling::FSMCondition_strategy)
def test_analysis::scheduling::fsmcondition_comp_type(instance):
    assert isinstance(instance.comp, str)


@given(instance=analysis::scheduling::FSMCondition_strategy)
def test_analysis::scheduling::fsmcondition_comp_setter(instance):
    original = instance.comp
    instance.comp = original
    assert instance.comp == original

@given(instance=analysis::scheduling::FSMCombination_strategy)
@settings(max_examples=50)
def test_analysis::scheduling::fsmcombination_instantiation(instance):
    assert isinstance(instance, analysis::scheduling::FSMCombination)

@given(instance=analysis::scheduling::FSMCombination_strategy)
def test_analysis::scheduling::fsmcombination_combinator_type(instance):
    assert isinstance(instance.combinator, str)


@given(instance=analysis::scheduling::FSMCombination_strategy)
def test_analysis::scheduling::fsmcombination_combinator_setter(instance):
    original = instance.combinator
    instance.combinator = original
    assert instance.combinator == original

@given(instance=FSMVar_strategy)
@settings(max_examples=50)
def test_fsmvar_instantiation(instance):
    assert isinstance(instance, FSMVar)

@given(instance=analysis::scheduling::FSMOperation_strategy)
@settings(max_examples=50)
def test_analysis::scheduling::fsmoperation_instantiation(instance):
    assert isinstance(instance, analysis::scheduling::FSMOperation)

@given(instance=analysis::scheduling::FSMOperation_strategy)
def test_analysis::scheduling::fsmoperation_var_type(instance):
    assert isinstance(instance.var, str)


@given(instance=analysis::scheduling::FSMOperation_strategy)
def test_analysis::scheduling::fsmoperation_var_setter(instance):
    original = instance.var
    instance.var = original
    assert instance.var == original

@given(instance=analysis::scheduling::FSMOperation_strategy)
def test_analysis::scheduling::fsmoperation_val_type(instance):
    assert isinstance(instance.val, str)


@given(instance=analysis::scheduling::FSMOperation_strategy)
def test_analysis::scheduling::fsmoperation_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=analysis::scheduling::FSMOperation_strategy)
def test_analysis::scheduling::fsmoperation_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=analysis::scheduling::FSMOperation_strategy)
def test_analysis::scheduling::fsmoperation_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=FSMOperation_strategy)
@settings(max_examples=50)
def test_fsmoperation_instantiation(instance):
    assert isinstance(instance, FSMOperation)

@given(instance=analysis::scheduling::FSMVarUpdate_strategy)
@settings(max_examples=50)
def test_analysis::scheduling::fsmvarupdate_instantiation(instance):
    assert isinstance(instance, analysis::scheduling::FSMVarUpdate)

@given(instance=FSMTransition_strategy)
@settings(max_examples=50)
def test_fsmtransition_instantiation(instance):
    assert isinstance(instance, FSMTransition)

@given(instance=analysis::scheduling::FSMTransitionWithState_strategy)
@settings(max_examples=50)
def test_analysis::scheduling::fsmtransitionwithstate_instantiation(instance):
    assert isinstance(instance, analysis::scheduling::FSMTransitionWithState)

@given(instance=FSMVarUpdate_strategy)
@settings(max_examples=50)
def test_fsmvarupdate_instantiation(instance):
    assert isinstance(instance, FSMVarUpdate)

@given(instance=analysis::scheduling::FSMState_strategy)
@settings(max_examples=50)
def test_analysis::scheduling::fsmstate_instantiation(instance):
    assert isinstance(instance, analysis::scheduling::FSMState)

@given(instance=analysis::scheduling::FSMState_strategy)
def test_analysis::scheduling::fsmstate_enumName_type(instance):
    assert isinstance(instance.enumName, str)


@given(instance=analysis::scheduling::FSMState_strategy)
def test_analysis::scheduling::fsmstate_enumName_setter(instance):
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

@given(instance=analysis::scheduling::FSMTransition_strategy)
@settings(max_examples=50)
def test_analysis::scheduling::fsmtransition_instantiation(instance):
    assert isinstance(instance, analysis::scheduling::FSMTransition)

@given(instance=analysis::scheduling::FSMTransition_strategy)
def test_analysis::scheduling::fsmtransition_targetStateEnumName_type(instance):
    assert isinstance(instance.targetStateEnumName, str)


@given(instance=analysis::scheduling::FSMTransition_strategy)
def test_analysis::scheduling::fsmtransition_targetStateEnumName_setter(instance):
    original = instance.targetStateEnumName
    instance.targetStateEnumName = original
    assert instance.targetStateEnumName == original

@given(instance=analysis::scheduling::FSMTransition_strategy)
def test_analysis::scheduling::fsmtransition_sourceStateEnumName_type(instance):
    assert isinstance(instance.sourceStateEnumName, str)


@given(instance=analysis::scheduling::FSMTransition_strategy)
def test_analysis::scheduling::fsmtransition_sourceStateEnumName_setter(instance):
    original = instance.sourceStateEnumName
    instance.sourceStateEnumName = original
    assert instance.sourceStateEnumName == original

@given(instance=analysis::scheduling::FSMVar_strategy)
@settings(max_examples=50)
def test_analysis::scheduling::fsmvar_instantiation(instance):
    assert isinstance(instance, analysis::scheduling::FSMVar)

@given(instance=analysis::scheduling::FSMVar_strategy)
def test_analysis::scheduling::fsmvar_initialVal_type(instance):
    assert isinstance(instance.initialVal, str)


@given(instance=analysis::scheduling::FSMVar_strategy)
def test_analysis::scheduling::fsmvar_initialVal_setter(instance):
    original = instance.initialVal
    instance.initialVal = original
    assert instance.initialVal == original

@given(instance=analysis::scheduling::FSMVar_strategy)
def test_analysis::scheduling::fsmvar_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=analysis::scheduling::FSMVar_strategy)
def test_analysis::scheduling::fsmvar_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=analysis::scheduling::FSMVar_strategy)
def test_analysis::scheduling::fsmvar_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=analysis::scheduling::FSMVar_strategy)
def test_analysis::scheduling::fsmvar_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ActorFire_strategy)
@settings(max_examples=50)
def test_actorfire_instantiation(instance):
    assert isinstance(instance, ActorFire)

@given(instance=analysis::scheduling::PartitionedActorFire_strategy)
@settings(max_examples=50)
def test_analysis::scheduling::partitionedactorfire_instantiation(instance):
    assert isinstance(instance, analysis::scheduling::PartitionedActorFire)

@given(instance=analysis::scheduling::ActorSelectionSchedule_strategy)
@settings(max_examples=50)
def test_analysis::scheduling::actorselectionschedule_instantiation(instance):
    assert isinstance(instance, analysis::scheduling::ActorSelectionSchedule)

@given(instance=profiling::analysis::Actor_strategy)
@settings(max_examples=50)
def test_profiling::analysis::actor_instantiation(instance):
    assert isinstance(instance, profiling::analysis::Actor)

@given(instance=analysis::profiling::IntraActorCommunicationData_strategy)
@settings(max_examples=50)
def test_analysis::profiling::intraactorcommunicationdata_instantiation(instance):
    assert isinstance(instance, analysis::profiling::IntraActorCommunicationData)

@given(instance=FSMState_strategy)
@settings(max_examples=50)
def test_fsmstate_instantiation(instance):
    assert isinstance(instance, FSMState)

@given(instance=analysis::profiling::ProfilingStatsActorData_strategy)
@settings(max_examples=50)
def test_analysis::profiling::profilingstatsactordata_instantiation(instance):
    assert isinstance(instance, analysis::profiling::ProfilingStatsActorData)

@given(instance=analysis::profiling::ProfilingStatsActorData_strategy)
def test_analysis::profiling::profilingstatsactordata_actorName_type(instance):
    assert isinstance(instance.actorName, str)


@given(instance=analysis::profiling::ProfilingStatsActorData_strategy)
def test_analysis::profiling::profilingstatsactordata_actorName_setter(instance):
    original = instance.actorName
    instance.actorName = original
    assert instance.actorName == original

@given(instance=analysis::profiling::ProfilingStatsActorData_strategy)
def test_analysis::profiling::profilingstatsactordata_actionsWeightPercent_type(instance):
    assert isinstance(instance.actionsWeightPercent, float)


@given(instance=analysis::profiling::ProfilingStatsActorData_strategy)
def test_analysis::profiling::profilingstatsactordata_actionsWeightPercent_setter(instance):
    original = instance.actionsWeightPercent
    instance.actionsWeightPercent = original
    assert instance.actionsWeightPercent == original

@given(instance=analysis::profiling::ProfilingStatsActorData_strategy)
def test_analysis::profiling::profilingstatsactordata_schedulerWeightPercent_type(instance):
    assert isinstance(instance.schedulerWeightPercent, float)


@given(instance=analysis::profiling::ProfilingStatsActorData_strategy)
def test_analysis::profiling::profilingstatsactordata_schedulerWeightPercent_setter(instance):
    original = instance.schedulerWeightPercent
    instance.schedulerWeightPercent = original
    assert instance.schedulerWeightPercent == original

@given(instance=analysis::profiling::ProfilingStatsActorData_strategy)
def test_analysis::profiling::profilingstatsactordata_schedulerWeight_type(instance):
    assert isinstance(instance.schedulerWeight, float)


@given(instance=analysis::profiling::ProfilingStatsActorData_strategy)
def test_analysis::profiling::profilingstatsactordata_schedulerWeight_setter(instance):
    original = instance.schedulerWeight
    instance.schedulerWeight = original
    assert instance.schedulerWeight == original

@given(instance=analysis::profiling::ProfilingStatsActorData_strategy)
def test_analysis::profiling::profilingstatsactordata_actionsWeight_type(instance):
    assert isinstance(instance.actionsWeight, float)


@given(instance=analysis::profiling::ProfilingStatsActorData_strategy)
def test_analysis::profiling::profilingstatsactordata_actionsWeight_setter(instance):
    original = instance.actionsWeight
    instance.actionsWeight = original
    assert instance.actionsWeight == original

@given(instance=ProfilingStatsActorData_strategy)
@settings(max_examples=50)
def test_profilingstatsactordata_instantiation(instance):
    assert isinstance(instance, ProfilingStatsActorData)

@given(instance=profiling::analysis::Action_strategy)
@settings(max_examples=50)
def test_profiling::analysis::action_instantiation(instance):
    assert isinstance(instance, profiling::analysis::Action)

@given(instance=analysis::profiling::IntraActionCommunicationData_strategy)
@settings(max_examples=50)
def test_analysis::profiling::intraactioncommunicationdata_instantiation(instance):
    assert isinstance(instance, analysis::profiling::IntraActionCommunicationData)

@given(instance=IntraActionCommunicationData_strategy)
@settings(max_examples=50)
def test_intraactioncommunicationdata_instantiation(instance):
    assert isinstance(instance, IntraActionCommunicationData)

@given(instance=profiling::analysis::StatisticalData_strategy)
@settings(max_examples=50)
def test_profiling::analysis::statisticaldata_instantiation(instance):
    assert isinstance(instance, profiling::analysis::StatisticalData)

@given(instance=profiling::analysis::Network_strategy)
@settings(max_examples=50)
def test_profiling::analysis::network_instantiation(instance):
    assert isinstance(instance, profiling::analysis::Network)

@given(instance=IntraActorCommunicationData_strategy)
@settings(max_examples=50)
def test_intraactorcommunicationdata_instantiation(instance):
    assert isinstance(instance, IntraActorCommunicationData)

@given(instance=ActorToStatisticalDataMap_strategy)
@settings(max_examples=50)
def test_actortostatisticaldatamap_instantiation(instance):
    assert isinstance(instance, ActorToStatisticalDataMap)

@given(instance=postprocessing::analysis::StatisticalData_strategy)
@settings(max_examples=50)
def test_postprocessing::analysis::statisticaldata_instantiation(instance):
    assert isinstance(instance, postprocessing::analysis::StatisticalData)

@given(instance=analysis::postprocessing::SchedulerChecksPartition_strategy)
@settings(max_examples=50)
def test_analysis::postprocessing::schedulercheckspartition_instantiation(instance):
    assert isinstance(instance, analysis::postprocessing::SchedulerChecksPartition)

@given(instance=SchedulerChecksPartition_strategy)
@settings(max_examples=50)
def test_schedulercheckspartition_instantiation(instance):
    assert isinstance(instance, SchedulerChecksPartition)

@given(instance=pipelining::analysis::ActorClass_strategy)
@settings(max_examples=50)
def test_pipelining::analysis::actorclass_instantiation(instance):
    assert isinstance(instance, pipelining::analysis::ActorClass)

@given(instance=ActionToDoubleMap_strategy)
@settings(max_examples=50)
def test_actiontodoublemap_instantiation(instance):
    assert isinstance(instance, ActionToDoubleMap)

@given(instance=postprocessing::analysis::Actor_strategy)
@settings(max_examples=50)
def test_postprocessing::analysis::actor_instantiation(instance):
    assert isinstance(instance, postprocessing::analysis::Actor)

@given(instance=analysis::postprocessing::StatisticalActorPartition_strategy)
@settings(max_examples=50)
def test_analysis::postprocessing::statisticalactorpartition_instantiation(instance):
    assert isinstance(instance, analysis::postprocessing::StatisticalActorPartition)

@given(instance=analysis::postprocessing::StatisticalActorPartition_strategy)
def test_analysis::postprocessing::statisticalactorpartition_actors_type(instance):
    assert isinstance(instance.actors, str)


@given(instance=analysis::postprocessing::StatisticalActorPartition_strategy)
def test_analysis::postprocessing::statisticalactorpartition_actors_setter(instance):
    original = instance.actors
    instance.actors = original
    assert instance.actors == original

@given(instance=analysis::postprocessing::StatisticalActorPartition_strategy)
def test_analysis::postprocessing::statisticalactorpartition_schedulingPolicy_type(instance):
    assert isinstance(instance.schedulingPolicy, str)


@given(instance=analysis::postprocessing::StatisticalActorPartition_strategy)
def test_analysis::postprocessing::statisticalactorpartition_schedulingPolicy_setter(instance):
    original = instance.schedulingPolicy
    instance.schedulingPolicy = original
    assert instance.schedulingPolicy == original

@given(instance=analysis::postprocessing::StatisticalActorPartition_strategy)
def test_analysis::postprocessing::statisticalactorpartition_occupancy_type(instance):
    assert isinstance(instance.occupancy, float)


@given(instance=analysis::postprocessing::StatisticalActorPartition_strategy)
def test_analysis::postprocessing::statisticalactorpartition_occupancy_setter(instance):
    original = instance.occupancy
    instance.occupancy = original
    assert instance.occupancy == original

@given(instance=StatisticalActorPartition_strategy)
@settings(max_examples=50)
def test_statisticalactorpartition_instantiation(instance):
    assert isinstance(instance, StatisticalActorPartition)

@given(instance=analysis::postprocessing::PostProcessingData_strategy)
@settings(max_examples=50)
def test_analysis::postprocessing::postprocessingdata_instantiation(instance):
    assert isinstance(instance, analysis::postprocessing::PostProcessingData)

@given(instance=PostProcessingData_strategy)
@settings(max_examples=50)
def test_postprocessingdata_instantiation(instance):
    assert isinstance(instance, PostProcessingData)

@given(instance=analysis::postprocessing::BufferBlockingReport_strategy)
@settings(max_examples=50)
def test_analysis::postprocessing::bufferblockingreport_instantiation(instance):
    assert isinstance(instance, analysis::postprocessing::BufferBlockingReport)

@given(instance=analysis::postprocessing::SchedulerChecksReport_strategy)
@settings(max_examples=50)
def test_analysis::postprocessing::schedulerchecksreport_instantiation(instance):
    assert isinstance(instance, analysis::postprocessing::SchedulerChecksReport)

@given(instance=analysis::postprocessing::ActorStatisticsReport_strategy)
@settings(max_examples=50)
def test_analysis::postprocessing::actorstatisticsreport_instantiation(instance):
    assert isinstance(instance, analysis::postprocessing::ActorStatisticsReport)

@given(instance=analysis::postprocessing::ActorStatisticsReport_strategy)
def test_analysis::postprocessing::actorstatisticsreport_averageOccupancy_type(instance):
    assert isinstance(instance.averageOccupancy, float)


@given(instance=analysis::postprocessing::ActorStatisticsReport_strategy)
def test_analysis::postprocessing::actorstatisticsreport_averageOccupancy_setter(instance):
    original = instance.averageOccupancy
    instance.averageOccupancy = original
    assert instance.averageOccupancy == original

@given(instance=analysis::postprocessing::ActorStatisticsReport_strategy)
def test_analysis::postprocessing::actorstatisticsreport_occupancyDeviation_type(instance):
    assert isinstance(instance.occupancyDeviation, float)


@given(instance=analysis::postprocessing::ActorStatisticsReport_strategy)
def test_analysis::postprocessing::actorstatisticsreport_occupancyDeviation_setter(instance):
    original = instance.occupancyDeviation
    instance.occupancyDeviation = original
    assert instance.occupancyDeviation == original

@given(instance=analysis::postprocessing::ActorStatisticsReport_strategy)
def test_analysis::postprocessing::actorstatisticsreport_executionTime_type(instance):
    assert isinstance(instance.executionTime, float)


@given(instance=analysis::postprocessing::ActorStatisticsReport_strategy)
def test_analysis::postprocessing::actorstatisticsreport_executionTime_setter(instance):
    original = instance.executionTime
    instance.executionTime = original
    assert instance.executionTime == original

@given(instance=analysis::postprocessing::ActionStatisticsReport_strategy)
@settings(max_examples=50)
def test_analysis::postprocessing::actionstatisticsreport_instantiation(instance):
    assert isinstance(instance, analysis::postprocessing::ActionStatisticsReport)

@given(instance=postprocessing::analysis::Network_strategy)
@settings(max_examples=50)
def test_postprocessing::analysis::network_instantiation(instance):
    assert isinstance(instance, postprocessing::analysis::Network)

@given(instance=analysis::pipelining::ImpactAnalysisData_strategy)
@settings(max_examples=50)
def test_analysis::pipelining::impactanalysisdata_instantiation(instance):
    assert isinstance(instance, analysis::pipelining::ImpactAnalysisData)

@given(instance=analysis::pipelining::ImpactAnalysisData_strategy)
def test_analysis::pipelining::impactanalysisdata_cpReduction_type(instance):
    assert isinstance(instance.cpReduction, float)


@given(instance=analysis::pipelining::ImpactAnalysisData_strategy)
def test_analysis::pipelining::impactanalysisdata_cpReduction_setter(instance):
    original = instance.cpReduction
    instance.cpReduction = original
    assert instance.cpReduction == original

@given(instance=ActionsVariablePipeliningReport_strategy)
@settings(max_examples=50)
def test_actionsvariablepipeliningreport_instantiation(instance):
    assert isinstance(instance, ActionsVariablePipeliningReport)

@given(instance=pipelining::analysis::StatisticalData_strategy)
@settings(max_examples=50)
def test_pipelining::analysis::statisticaldata_instantiation(instance):
    assert isinstance(instance, pipelining::analysis::StatisticalData)

@given(instance=pipelining::analysis::Action_strategy)
@settings(max_examples=50)
def test_pipelining::analysis::action_instantiation(instance):
    assert isinstance(instance, pipelining::analysis::Action)

@given(instance=analysis::pipelining::ActionVariablePipeliningData_strategy)
@settings(max_examples=50)
def test_analysis::pipelining::actionvariablepipeliningdata_instantiation(instance):
    assert isinstance(instance, analysis::pipelining::ActionVariablePipeliningData)

@given(instance=analysis::pipelining::ActionVariablePipeliningData_strategy)
def test_analysis::pipelining::actionvariablepipeliningdata_pipelinable_type(instance):
    assert isinstance(instance.pipelinable, bool)


@given(instance=analysis::pipelining::ActionVariablePipeliningData_strategy)
def test_analysis::pipelining::actionvariablepipeliningdata_pipelinable_setter(instance):
    original = instance.pipelinable
    instance.pipelinable = original
    assert instance.pipelinable == original

@given(instance=ActionVariablePipeliningData_strategy)
@settings(max_examples=50)
def test_actionvariablepipeliningdata_instantiation(instance):
    assert isinstance(instance, ActionVariablePipeliningData)

@given(instance=pipelining::analysis::Network_strategy)
@settings(max_examples=50)
def test_pipelining::analysis::network_instantiation(instance):
    assert isinstance(instance, pipelining::analysis::Network)

@given(instance=BalancedPipelinePartition_strategy)
@settings(max_examples=50)
def test_balancedpipelinepartition_instantiation(instance):
    assert isinstance(instance, BalancedPipelinePartition)

@given(instance=partitioning::analysis::Actor_strategy)
@settings(max_examples=50)
def test_partitioning::analysis::actor_instantiation(instance):
    assert isinstance(instance, partitioning::analysis::Actor)

@given(instance=analysis::partitioning::ComCostPartition_strategy)
@settings(max_examples=50)
def test_analysis::partitioning::comcostpartition_instantiation(instance):
    assert isinstance(instance, analysis::partitioning::ComCostPartition)

@given(instance=analysis::partitioning::ComCostPartition_strategy)
def test_analysis::partitioning::comcostpartition_internalCost_type(instance):
    assert isinstance(instance.internalCost, str)


@given(instance=analysis::partitioning::ComCostPartition_strategy)
def test_analysis::partitioning::comcostpartition_internalCost_setter(instance):
    original = instance.internalCost
    instance.internalCost = original
    assert instance.internalCost == original

@given(instance=analysis::partitioning::ComCostPartition_strategy)
def test_analysis::partitioning::comcostpartition_externalCost_type(instance):
    assert isinstance(instance.externalCost, str)


@given(instance=analysis::partitioning::ComCostPartition_strategy)
def test_analysis::partitioning::comcostpartition_externalCost_setter(instance):
    original = instance.externalCost
    instance.externalCost = original
    assert instance.externalCost == original

@given(instance=ActionToStatisticalDataMap_strategy)
@settings(max_examples=50)
def test_actiontostatisticaldatamap_instantiation(instance):
    assert isinstance(instance, ActionToStatisticalDataMap)

@given(instance=profiler::analysis::StatisticalData_strategy)
@settings(max_examples=50)
def test_profiler::analysis::statisticaldata_instantiation(instance):
    assert isinstance(instance, profiler::analysis::StatisticalData)

@given(instance=profiler::analysis::Buffer_strategy)
@settings(max_examples=50)
def test_profiler::analysis::buffer_instantiation(instance):
    assert isinstance(instance, profiler::analysis::Buffer)

@given(instance=analysis::profiler::BufferDynamicData_strategy)
@settings(max_examples=50)
def test_analysis::profiler::bufferdynamicdata_instantiation(instance):
    assert isinstance(instance, analysis::profiler::BufferDynamicData)

@given(instance=analysis::profiler::BufferDynamicData_strategy)
def test_analysis::profiler::bufferdynamicdata_unconsumedTokens_type(instance):
    assert isinstance(instance.unconsumedTokens, int)


@given(instance=analysis::profiler::BufferDynamicData_strategy)
def test_analysis::profiler::bufferdynamicdata_unconsumedTokens_setter(instance):
    original = instance.unconsumedTokens
    instance.unconsumedTokens = original
    assert instance.unconsumedTokens == original

@given(instance=profiler::analysis::Action_strategy)
@settings(max_examples=50)
def test_profiler::analysis::action_instantiation(instance):
    assert isinstance(instance, profiler::analysis::Action)

@given(instance=profiler::analysis::Actor_strategy)
@settings(max_examples=50)
def test_profiler::analysis::actor_instantiation(instance):
    assert isinstance(instance, profiler::analysis::Actor)

@given(instance=ComplexDynamicData_strategy)
@settings(max_examples=50)
def test_complexdynamicdata_instantiation(instance):
    assert isinstance(instance, ComplexDynamicData)

@given(instance=analysis::profiler::ActionDynamicData_strategy)
@settings(max_examples=50)
def test_analysis::profiler::actiondynamicdata_instantiation(instance):
    assert isinstance(instance, analysis::profiler::ActionDynamicData)

@given(instance=analysis::profiler::ActorDynamicData_strategy)
@settings(max_examples=50)
def test_analysis::profiler::actordynamicdata_instantiation(instance):
    assert isinstance(instance, analysis::profiler::ActorDynamicData)

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

@given(instance=analysis::profiler::ComplexCodeData_strategy)
@settings(max_examples=50)
def test_analysis::profiler::complexcodedata_instantiation(instance):
    assert isinstance(instance, analysis::profiler::ComplexCodeData)

@given(instance=StringToIntegerMap_strategy)
@settings(max_examples=50)
def test_stringtointegermap_instantiation(instance):
    assert isinstance(instance, StringToIntegerMap)

@given(instance=analysis::profiler::CodeData_strategy)
@settings(max_examples=50)
def test_analysis::profiler::codedata_instantiation(instance):
    assert isinstance(instance, analysis::profiler::CodeData)

@given(instance=analysis::profiler::CodeData_strategy)
def test_analysis::profiler::codedata_nol_type(instance):
    assert isinstance(instance.nol, str)


@given(instance=analysis::profiler::CodeData_strategy)
def test_analysis::profiler::codedata_nol_setter(instance):
    original = instance.nol
    instance.nol = original
    assert instance.nol == original

@given(instance=analysis::profiler::CodeData_strategy)
def test_analysis::profiler::codedata_blockName_type(instance):
    assert isinstance(instance.blockName, str)


@given(instance=analysis::profiler::CodeData_strategy)
def test_analysis::profiler::codedata_blockName_setter(instance):
    original = instance.blockName
    instance.blockName = original
    assert instance.blockName == original

@given(instance=ComplexCodeData_strategy)
@settings(max_examples=50)
def test_complexcodedata_instantiation(instance):
    assert isinstance(instance, ComplexCodeData)

@given(instance=profiler::analysis::Network_strategy)
@settings(max_examples=50)
def test_profiler::analysis::network_instantiation(instance):
    assert isinstance(instance, profiler::analysis::Network)

@given(instance=AnalysisReport_strategy)
@settings(max_examples=50)
def test_analysisreport_instantiation(instance):
    assert isinstance(instance, AnalysisReport)

@given(instance=analysis::partitioning::ComCostPartitioningReport_strategy)
@settings(max_examples=50)
def test_analysis::partitioning::comcostpartitioningreport_instantiation(instance):
    assert isinstance(instance, analysis::partitioning::ComCostPartitioningReport)

@given(instance=analysis::partitioning::ComCostPartitioningReport_strategy)
def test_analysis::partitioning::comcostpartitioningreport_bitAccurate_type(instance):
    assert isinstance(instance.bitAccurate, bool)


@given(instance=analysis::partitioning::ComCostPartitioningReport_strategy)
def test_analysis::partitioning::comcostpartitioningreport_bitAccurate_setter(instance):
    original = instance.bitAccurate
    instance.bitAccurate = original
    assert instance.bitAccurate == original

@given(instance=analysis::buffers::BoundedBuffersReport_strategy)
@settings(max_examples=50)
def test_analysis::buffers::boundedbuffersreport_instantiation(instance):
    assert isinstance(instance, analysis::buffers::BoundedBuffersReport)

@given(instance=analysis::buffers::BoundedBuffersReport_strategy)
def test_analysis::buffers::boundedbuffersreport_bitSize_type(instance):
    assert isinstance(instance.bitSize, int)


@given(instance=analysis::buffers::BoundedBuffersReport_strategy)
def test_analysis::buffers::boundedbuffersreport_bitSize_setter(instance):
    original = instance.bitSize
    instance.bitSize = original
    assert instance.bitSize == original

@given(instance=analysis::buffers::BoundedBuffersReport_strategy)
def test_analysis::buffers::boundedbuffersreport_pow2_type(instance):
    assert isinstance(instance.pow2, bool)


@given(instance=analysis::buffers::BoundedBuffersReport_strategy)
def test_analysis::buffers::boundedbuffersreport_pow2_setter(instance):
    original = instance.pow2
    instance.pow2 = original
    assert instance.pow2 == original

@given(instance=analysis::buffers::BoundedBuffersReport_strategy)
def test_analysis::buffers::boundedbuffersreport_bitAccurate_type(instance):
    assert isinstance(instance.bitAccurate, bool)


@given(instance=analysis::buffers::BoundedBuffersReport_strategy)
def test_analysis::buffers::boundedbuffersreport_bitAccurate_setter(instance):
    original = instance.bitAccurate
    instance.bitAccurate = original
    assert instance.bitAccurate == original

@given(instance=analysis::buffers::BoundedBuffersReport_strategy)
def test_analysis::buffers::boundedbuffersreport_tokenSize_type(instance):
    assert isinstance(instance.tokenSize, int)


@given(instance=analysis::buffers::BoundedBuffersReport_strategy)
def test_analysis::buffers::boundedbuffersreport_tokenSize_setter(instance):
    original = instance.tokenSize
    instance.tokenSize = original
    assert instance.tokenSize == original

@given(instance=analysis::pipelining::ActionsVariablePipeliningReport_strategy)
@settings(max_examples=50)
def test_analysis::pipelining::actionsvariablepipeliningreport_instantiation(instance):
    assert isinstance(instance, analysis::pipelining::ActionsVariablePipeliningReport)

@given(instance=analysis::bottlenecks::BottlenecksReport_strategy)
@settings(max_examples=50)
def test_analysis::bottlenecks::bottlenecksreport_instantiation(instance):
    assert isinstance(instance, analysis::bottlenecks::BottlenecksReport)

@given(instance=analysis::bottlenecks::BottlenecksReport_strategy)
def test_analysis::bottlenecks::bottlenecksreport_totalFirings_type(instance):
    assert isinstance(instance.totalFirings, str)


@given(instance=analysis::bottlenecks::BottlenecksReport_strategy)
def test_analysis::bottlenecks::bottlenecksreport_totalFirings_setter(instance):
    original = instance.totalFirings
    instance.totalFirings = original
    assert instance.totalFirings == original

@given(instance=analysis::bottlenecks::BottlenecksReport_strategy)
def test_analysis::bottlenecks::bottlenecksreport_cpVariance_type(instance):
    assert isinstance(instance.cpVariance, float)


@given(instance=analysis::bottlenecks::BottlenecksReport_strategy)
def test_analysis::bottlenecks::bottlenecksreport_cpVariance_setter(instance):
    original = instance.cpVariance
    instance.cpVariance = original
    assert instance.cpVariance == original

@given(instance=analysis::bottlenecks::BottlenecksReport_strategy)
def test_analysis::bottlenecks::bottlenecksreport_totalWeight_type(instance):
    assert isinstance(instance.totalWeight, float)


@given(instance=analysis::bottlenecks::BottlenecksReport_strategy)
def test_analysis::bottlenecks::bottlenecksreport_totalWeight_setter(instance):
    original = instance.totalWeight
    instance.totalWeight = original
    assert instance.totalWeight == original

@given(instance=analysis::bottlenecks::BottlenecksReport_strategy)
def test_analysis::bottlenecks::bottlenecksreport_cpWeight_type(instance):
    assert isinstance(instance.cpWeight, float)


@given(instance=analysis::bottlenecks::BottlenecksReport_strategy)
def test_analysis::bottlenecks::bottlenecksreport_cpWeight_setter(instance):
    original = instance.cpWeight
    instance.cpWeight = original
    assert instance.cpWeight == original

@given(instance=analysis::bottlenecks::BottlenecksReport_strategy)
def test_analysis::bottlenecks::bottlenecksreport_totalVariance_type(instance):
    assert isinstance(instance.totalVariance, float)


@given(instance=analysis::bottlenecks::BottlenecksReport_strategy)
def test_analysis::bottlenecks::bottlenecksreport_totalVariance_setter(instance):
    original = instance.totalVariance
    instance.totalVariance = original
    assert instance.totalVariance == original

@given(instance=analysis::bottlenecks::BottlenecksReport_strategy)
def test_analysis::bottlenecks::bottlenecksreport_cpFirings_type(instance):
    assert isinstance(instance.cpFirings, str)


@given(instance=analysis::bottlenecks::BottlenecksReport_strategy)
def test_analysis::bottlenecks::bottlenecksreport_cpFirings_setter(instance):
    original = instance.cpFirings
    instance.cpFirings = original
    assert instance.cpFirings == original

@given(instance=analysis::profiler::DynamicProfilingReport_strategy)
@settings(max_examples=50)
def test_analysis::profiler::dynamicprofilingreport_instantiation(instance):
    assert isinstance(instance, analysis::profiler::DynamicProfilingReport)

@given(instance=analysis::bottlenecks::BottlenecksWithSchedulingReport_strategy)
@settings(max_examples=50)
def test_analysis::bottlenecks::bottleneckswithschedulingreport_instantiation(instance):
    assert isinstance(instance, analysis::bottlenecks::BottlenecksWithSchedulingReport)

@given(instance=analysis::bottlenecks::BottlenecksWithSchedulingReport_strategy)
def test_analysis::bottlenecks::bottleneckswithschedulingreport_executionTime_type(instance):
    assert isinstance(instance.executionTime, float)


@given(instance=analysis::bottlenecks::BottlenecksWithSchedulingReport_strategy)
def test_analysis::bottlenecks::bottleneckswithschedulingreport_executionTime_setter(instance):
    original = instance.executionTime
    instance.executionTime = original
    assert instance.executionTime == original

@given(instance=analysis::bottlenecks::BottlenecksWithSchedulingReport_strategy)
def test_analysis::bottlenecks::bottleneckswithschedulingreport_cpWeight_type(instance):
    assert isinstance(instance.cpWeight, float)


@given(instance=analysis::bottlenecks::BottlenecksWithSchedulingReport_strategy)
def test_analysis::bottlenecks::bottleneckswithschedulingreport_cpWeight_setter(instance):
    original = instance.cpWeight
    instance.cpWeight = original
    assert instance.cpWeight == original

@given(instance=analysis::bottlenecks::BottlenecksWithSchedulingReport_strategy)
def test_analysis::bottlenecks::bottleneckswithschedulingreport_totalFirings_type(instance):
    assert isinstance(instance.totalFirings, str)


@given(instance=analysis::bottlenecks::BottlenecksWithSchedulingReport_strategy)
def test_analysis::bottlenecks::bottleneckswithschedulingreport_totalFirings_setter(instance):
    original = instance.totalFirings
    instance.totalFirings = original
    assert instance.totalFirings == original

@given(instance=analysis::bottlenecks::BottlenecksWithSchedulingReport_strategy)
def test_analysis::bottlenecks::bottleneckswithschedulingreport_cpBlockingTime_type(instance):
    assert isinstance(instance.cpBlockingTime, float)


@given(instance=analysis::bottlenecks::BottlenecksWithSchedulingReport_strategy)
def test_analysis::bottlenecks::bottleneckswithschedulingreport_cpBlockingTime_setter(instance):
    original = instance.cpBlockingTime
    instance.cpBlockingTime = original
    assert instance.cpBlockingTime == original

@given(instance=analysis::bottlenecks::BottlenecksWithSchedulingReport_strategy)
def test_analysis::bottlenecks::bottleneckswithschedulingreport_cpFirings_type(instance):
    assert isinstance(instance.cpFirings, str)


@given(instance=analysis::bottlenecks::BottlenecksWithSchedulingReport_strategy)
def test_analysis::bottlenecks::bottleneckswithschedulingreport_cpFirings_setter(instance):
    original = instance.cpFirings
    instance.cpFirings = original
    assert instance.cpFirings == original

@given(instance=analysis::bottlenecks::BottlenecksWithSchedulingReport_strategy)
def test_analysis::bottlenecks::bottleneckswithschedulingreport_totalWeight_type(instance):
    assert isinstance(instance.totalWeight, float)


@given(instance=analysis::bottlenecks::BottlenecksWithSchedulingReport_strategy)
def test_analysis::bottlenecks::bottleneckswithschedulingreport_totalWeight_setter(instance):
    original = instance.totalWeight
    instance.totalWeight = original
    assert instance.totalWeight == original

@given(instance=analysis::scheduling::MarkovSimpleSchedulerReport_strategy)
@settings(max_examples=50)
def test_analysis::scheduling::markovsimpleschedulerreport_instantiation(instance):
    assert isinstance(instance, analysis::scheduling::MarkovSimpleSchedulerReport)

@given(instance=analysis::buffers::OptimalBuffersReport_strategy)
@settings(max_examples=50)
def test_analysis::buffers::optimalbuffersreport_instantiation(instance):
    assert isinstance(instance, analysis::buffers::OptimalBuffersReport)

@given(instance=analysis::buffers::OptimalBuffersReport_strategy)
def test_analysis::buffers::optimalbuffersreport_bitAccurate_type(instance):
    assert isinstance(instance.bitAccurate, bool)


@given(instance=analysis::buffers::OptimalBuffersReport_strategy)
def test_analysis::buffers::optimalbuffersreport_bitAccurate_setter(instance):
    original = instance.bitAccurate
    instance.bitAccurate = original
    assert instance.bitAccurate == original

@given(instance=analysis::buffers::OptimalBuffersReport_strategy)
def test_analysis::buffers::optimalbuffersreport_pow2_type(instance):
    assert isinstance(instance.pow2, bool)


@given(instance=analysis::buffers::OptimalBuffersReport_strategy)
def test_analysis::buffers::optimalbuffersreport_pow2_setter(instance):
    original = instance.pow2
    instance.pow2 = original
    assert instance.pow2 == original

@given(instance=analysis::profiling::ProfilingStatsReport_strategy)
@settings(max_examples=50)
def test_analysis::profiling::profilingstatsreport_instantiation(instance):
    assert isinstance(instance, analysis::profiling::ProfilingStatsReport)

@given(instance=analysis::profiling::ProfilingStatsReport_strategy)
def test_analysis::profiling::profilingstatsreport_networkName_type(instance):
    assert isinstance(instance.networkName, str)


@given(instance=analysis::profiling::ProfilingStatsReport_strategy)
def test_analysis::profiling::profilingstatsreport_networkName_setter(instance):
    original = instance.networkName
    instance.networkName = original
    assert instance.networkName == original

@given(instance=analysis::trace::MarkowModelTraceReport_strategy)
@settings(max_examples=50)
def test_analysis::trace::markowmodeltracereport_instantiation(instance):
    assert isinstance(instance, analysis::trace::MarkowModelTraceReport)

@given(instance=analysis::partitioning::WorkloadBalancePartitioningReport_strategy)
@settings(max_examples=50)
def test_analysis::partitioning::workloadbalancepartitioningreport_instantiation(instance):
    assert isinstance(instance, analysis::partitioning::WorkloadBalancePartitioningReport)

@given(instance=analysis::postprocessing::PostProcessingReport_strategy)
@settings(max_examples=50)
def test_analysis::postprocessing::postprocessingreport_instantiation(instance):
    assert isinstance(instance, analysis::postprocessing::PostProcessingReport)

@given(instance=analysis::postprocessing::PostProcessingReport_strategy)
def test_analysis::postprocessing::postprocessingreport_deadlock_type(instance):
    assert isinstance(instance.deadlock, bool)


@given(instance=analysis::postprocessing::PostProcessingReport_strategy)
def test_analysis::postprocessing::postprocessingreport_deadlock_setter(instance):
    original = instance.deadlock
    instance.deadlock = original
    assert instance.deadlock == original

@given(instance=analysis::postprocessing::PostProcessingReport_strategy)
def test_analysis::postprocessing::postprocessingreport_time_type(instance):
    assert isinstance(instance.time, float)


@given(instance=analysis::postprocessing::PostProcessingReport_strategy)
def test_analysis::postprocessing::postprocessingreport_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=analysis::bottlenecks::ImpactAnalysisReport_strategy)
@settings(max_examples=50)
def test_analysis::bottlenecks::impactanalysisreport_instantiation(instance):
    assert isinstance(instance, analysis::bottlenecks::ImpactAnalysisReport)

@given(instance=analysis::bottlenecks::ImpactAnalysisReport_strategy)
def test_analysis::bottlenecks::impactanalysisreport_classLevel_type(instance):
    assert isinstance(instance.classLevel, bool)


@given(instance=analysis::bottlenecks::ImpactAnalysisReport_strategy)
def test_analysis::bottlenecks::impactanalysisreport_classLevel_setter(instance):
    original = instance.classLevel
    instance.classLevel = original
    assert instance.classLevel == original

@given(instance=analysis::pipelining::ImpactAnalysisReport_strategy)
@settings(max_examples=50)
def test_analysis::pipelining::impactanalysisreport_instantiation(instance):
    assert isinstance(instance, analysis::pipelining::ImpactAnalysisReport)

@given(instance=analysis::caseoptimal::CaseOptimalScheduleReport_strategy)
@settings(max_examples=50)
def test_analysis::caseoptimal::caseoptimalschedulereport_instantiation(instance):
    assert isinstance(instance, analysis::caseoptimal::CaseOptimalScheduleReport)

@given(instance=analysis::caseoptimal::CaseOptimalScheduleReport_strategy)
def test_analysis::caseoptimal::caseoptimalschedulereport_traceFile_type(instance):
    assert isinstance(instance.traceFile, str)


@given(instance=analysis::caseoptimal::CaseOptimalScheduleReport_strategy)
def test_analysis::caseoptimal::caseoptimalschedulereport_traceFile_setter(instance):
    original = instance.traceFile
    instance.traceFile = original
    assert instance.traceFile == original

@given(instance=analysis::caseoptimal::CaseOptimalScheduleReport_strategy)
def test_analysis::caseoptimal::caseoptimalschedulereport_partitionFilePath_type(instance):
    assert isinstance(instance.partitionFilePath, str)


@given(instance=analysis::caseoptimal::CaseOptimalScheduleReport_strategy)
def test_analysis::caseoptimal::caseoptimalschedulereport_partitionFilePath_setter(instance):
    original = instance.partitionFilePath
    instance.partitionFilePath = original
    assert instance.partitionFilePath == original

@given(instance=analysis::caseoptimal::CaseOptimalScheduleReport_strategy)
def test_analysis::caseoptimal::caseoptimalschedulereport_pipeline_type(instance):
    assert isinstance(instance.pipeline, str)


@given(instance=analysis::caseoptimal::CaseOptimalScheduleReport_strategy)
def test_analysis::caseoptimal::caseoptimalschedulereport_pipeline_setter(instance):
    original = instance.pipeline
    instance.pipeline = original
    assert instance.pipeline == original

@given(instance=analysis::bottlenecks::ScheduledImpactAnalysisReport_strategy)
@settings(max_examples=50)
def test_analysis::bottlenecks::scheduledimpactanalysisreport_instantiation(instance):
    assert isinstance(instance, analysis::bottlenecks::ScheduledImpactAnalysisReport)

@given(instance=analysis::bottlenecks::ScheduledImpactAnalysisReport_strategy)
def test_analysis::bottlenecks::scheduledimpactanalysisreport_classLevel_type(instance):
    assert isinstance(instance.classLevel, bool)


@given(instance=analysis::bottlenecks::ScheduledImpactAnalysisReport_strategy)
def test_analysis::bottlenecks::scheduledimpactanalysisreport_classLevel_setter(instance):
    original = instance.classLevel
    instance.classLevel = original
    assert instance.classLevel == original

@given(instance=analysis::profiling::IntraActionCommunicationReport_strategy)
@settings(max_examples=50)
def test_analysis::profiling::intraactioncommunicationreport_instantiation(instance):
    assert isinstance(instance, analysis::profiling::IntraActionCommunicationReport)

@given(instance=analysis::partitioning::BalancedPipelinePartitioningReport_strategy)
@settings(max_examples=50)
def test_analysis::partitioning::balancedpipelinepartitioningreport_instantiation(instance):
    assert isinstance(instance, analysis::partitioning::BalancedPipelinePartitioningReport)

@given(instance=analysis::profiler::CodeProfilingReport_strategy)
@settings(max_examples=50)
def test_analysis::profiler::codeprofilingreport_instantiation(instance):
    assert isinstance(instance, analysis::profiler::CodeProfilingReport)

@given(instance=analysis::AnalysisReport_strategy)
@settings(max_examples=50)
def test_analysis::analysisreport_instantiation(instance):
    assert isinstance(instance, analysis::AnalysisReport)

@given(instance=analysis::AnalysisReport_strategy)
def test_analysis::analysisreport_date_type(instance):
    assert isinstance(instance.date, date)


@given(instance=analysis::AnalysisReport_strategy)
def test_analysis::analysisreport_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=analysis::AnalysisReport_strategy)
def test_analysis::analysisreport_algorithm_type(instance):
    assert isinstance(instance.algorithm, str)


@given(instance=analysis::AnalysisReport_strategy)
def test_analysis::analysisreport_algorithm_setter(instance):
    original = instance.algorithm
    instance.algorithm = original
    assert instance.algorithm == original

@given(instance=analysis::trace::ComparedAction_strategy)
@settings(max_examples=50)
def test_analysis::trace::comparedaction_instantiation(instance):
    assert isinstance(instance, analysis::trace::ComparedAction)

@given(instance=analysis::trace::ComparedAction_strategy)
def test_analysis::trace::comparedaction_found_type(instance):
    assert isinstance(instance.found, bool)


@given(instance=analysis::trace::ComparedAction_strategy)
def test_analysis::trace::comparedaction_found_setter(instance):
    original = instance.found
    instance.found = original
    assert instance.found == original

@given(instance=analysis::trace::ComparedAction_strategy)
def test_analysis::trace::comparedaction_dSteps_type(instance):
    assert isinstance(instance.dSteps, str)


@given(instance=analysis::trace::ComparedAction_strategy)
def test_analysis::trace::comparedaction_dSteps_setter(instance):
    original = instance.dSteps
    instance.dSteps = original
    assert instance.dSteps == original

@given(instance=analysis::trace::ComparedAction_strategy)
def test_analysis::trace::comparedaction_dIncomings_type(instance):
    assert isinstance(instance.dIncomings, str)


@given(instance=analysis::trace::ComparedAction_strategy)
def test_analysis::trace::comparedaction_dIncomings_setter(instance):
    original = instance.dIncomings
    instance.dIncomings = original
    assert instance.dIncomings == original

@given(instance=analysis::trace::ComparedAction_strategy)
def test_analysis::trace::comparedaction_dOutgoings_type(instance):
    assert isinstance(instance.dOutgoings, str)


@given(instance=analysis::trace::ComparedAction_strategy)
def test_analysis::trace::comparedaction_dOutgoings_setter(instance):
    original = instance.dOutgoings
    instance.dOutgoings = original
    assert instance.dOutgoings == original

@given(instance=ComparedAction_strategy)
@settings(max_examples=50)
def test_comparedaction_instantiation(instance):
    assert isinstance(instance, ComparedAction)

@given(instance=bottlenecks::analysis::Action_strategy)
@settings(max_examples=50)
def test_bottlenecks::analysis::action_instantiation(instance):
    assert isinstance(instance, bottlenecks::analysis::Action)

@given(instance=analysis::trace::ComparedTrace_strategy)
@settings(max_examples=50)
def test_analysis::trace::comparedtrace_instantiation(instance):
    assert isinstance(instance, analysis::trace::ComparedTrace)

@given(instance=analysis::trace::ComparedTrace_strategy)
def test_analysis::trace::comparedtrace_equal_type(instance):
    assert isinstance(instance.equal, bool)


@given(instance=analysis::trace::ComparedTrace_strategy)
def test_analysis::trace::comparedtrace_equal_setter(instance):
    original = instance.equal
    instance.equal = original
    assert instance.equal == original

@given(instance=analysis::trace::ComparedTrace_strategy)
def test_analysis::trace::comparedtrace_dSteps_type(instance):
    assert isinstance(instance.dSteps, str)


@given(instance=analysis::trace::ComparedTrace_strategy)
def test_analysis::trace::comparedtrace_dSteps_setter(instance):
    original = instance.dSteps
    instance.dSteps = original
    assert instance.dSteps == original

@given(instance=analysis::trace::ComparedTrace_strategy)
def test_analysis::trace::comparedtrace_dDependencies_type(instance):
    assert isinstance(instance.dDependencies, str)


@given(instance=analysis::trace::ComparedTrace_strategy)
def test_analysis::trace::comparedtrace_dDependencies_setter(instance):
    original = instance.dDependencies
    instance.dDependencies = original
    assert instance.dDependencies == original

@given(instance=ComparedTrace_strategy)
@settings(max_examples=50)
def test_comparedtrace_instantiation(instance):
    assert isinstance(instance, ComparedTrace)

@given(instance=CompressedTraceReport_strategy)
@settings(max_examples=50)
def test_compressedtracereport_instantiation(instance):
    assert isinstance(instance, CompressedTraceReport)

@given(instance=analysis::trace::TraceComparatorReport_strategy)
@settings(max_examples=50)
def test_analysis::trace::tracecomparatorreport_instantiation(instance):
    assert isinstance(instance, analysis::trace::TraceComparatorReport)

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

@given(instance=analysis::trace::CompressedDependency_strategy)
@settings(max_examples=50)
def test_analysis::trace::compresseddependency_instantiation(instance):
    assert isinstance(instance, analysis::trace::CompressedDependency)

@given(instance=analysis::trace::CompressedDependency_strategy)
def test_analysis::trace::compresseddependency_count_type(instance):
    assert isinstance(instance.count, str)


@given(instance=analysis::trace::CompressedDependency_strategy)
def test_analysis::trace::compresseddependency_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original

@given(instance=trace::analysis::Action_strategy)
@settings(max_examples=50)
def test_trace::analysis::action_instantiation(instance):
    assert isinstance(instance, trace::analysis::Action)

@given(instance=analysis::trace::CompressedStep_strategy)
@settings(max_examples=50)
def test_analysis::trace::compressedstep_instantiation(instance):
    assert isinstance(instance, analysis::trace::CompressedStep)

@given(instance=analysis::trace::CompressedStep_strategy)
def test_analysis::trace::compressedstep_count_type(instance):
    assert isinstance(instance.count, str)


@given(instance=analysis::trace::CompressedStep_strategy)
def test_analysis::trace::compressedstep_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original

@given(instance=CompressedDependency_strategy)
@settings(max_examples=50)
def test_compresseddependency_instantiation(instance):
    assert isinstance(instance, CompressedDependency)

@given(instance=analysis::trace::CompressedPortDependency_strategy)
@settings(max_examples=50)
def test_analysis::trace::compressedportdependency_instantiation(instance):
    assert isinstance(instance, analysis::trace::CompressedPortDependency)

@given(instance=analysis::trace::CompressedGuardDependency_strategy)
@settings(max_examples=50)
def test_analysis::trace::compressedguarddependency_instantiation(instance):
    assert isinstance(instance, analysis::trace::CompressedGuardDependency)

@given(instance=analysis::trace::CompressedTokensDependency_strategy)
@settings(max_examples=50)
def test_analysis::trace::compressedtokensdependency_instantiation(instance):
    assert isinstance(instance, analysis::trace::CompressedTokensDependency)

@given(instance=analysis::trace::CompressedVariableDependency_strategy)
@settings(max_examples=50)
def test_analysis::trace::compressedvariabledependency_instantiation(instance):
    assert isinstance(instance, analysis::trace::CompressedVariableDependency)

@given(instance=analysis::trace::CompressedFsmDependency_strategy)
@settings(max_examples=50)
def test_analysis::trace::compressedfsmdependency_instantiation(instance):
    assert isinstance(instance, analysis::trace::CompressedFsmDependency)

@given(instance=CompressedStep_strategy)
@settings(max_examples=50)
def test_compressedstep_instantiation(instance):
    assert isinstance(instance, CompressedStep)

@given(instance=analysis::trace::CompressedTraceReport_strategy)
@settings(max_examples=50)
def test_analysis::trace::compressedtracereport_instantiation(instance):
    assert isinstance(instance, analysis::trace::CompressedTraceReport)

@given(instance=analysis::trace::CompressedTraceReport_strategy)
def test_analysis::trace::compressedtracereport_traceFile_type(instance):
    assert isinstance(instance.traceFile, str)


@given(instance=analysis::trace::CompressedTraceReport_strategy)
def test_analysis::trace::compressedtracereport_traceFile_setter(instance):
    original = instance.traceFile
    instance.traceFile = original
    assert instance.traceFile == original

@given(instance=trace::analysis::Network_strategy)
@settings(max_examples=50)
def test_trace::analysis::network_instantiation(instance):
    assert isinstance(instance, trace::analysis::Network)

@given(instance=StringToLongMap_strategy)
@settings(max_examples=50)
def test_stringtolongmap_instantiation(instance):
    assert isinstance(instance, StringToLongMap)

@given(instance=analysis::map::ActionToDoubleMap_strategy)
@settings(max_examples=50)
def test_analysis::map::actiontodoublemap_instantiation(instance):
    assert isinstance(instance, analysis::map::ActionToDoubleMap)

@given(instance=analysis::map::ActionToDoubleMap_strategy)
def test_analysis::map::actiontodoublemap_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=analysis::map::ActionToDoubleMap_strategy)
def test_analysis::map::actiontodoublemap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ActorToLongMap_strategy)
@settings(max_examples=50)
def test_actortolongmap_instantiation(instance):
    assert isinstance(instance, ActorToLongMap)

@given(instance=analysis::trace::TraceSizeReport_strategy)
@settings(max_examples=50)
def test_analysis::trace::tracesizereport_instantiation(instance):
    assert isinstance(instance, analysis::trace::TraceSizeReport)

@given(instance=analysis::trace::TraceSizeReport_strategy)
def test_analysis::trace::tracesizereport_dependencies_type(instance):
    assert isinstance(instance.dependencies, str)


@given(instance=analysis::trace::TraceSizeReport_strategy)
def test_analysis::trace::tracesizereport_dependencies_setter(instance):
    original = instance.dependencies
    instance.dependencies = original
    assert instance.dependencies == original

@given(instance=analysis::trace::TraceSizeReport_strategy)
def test_analysis::trace::tracesizereport_firings_type(instance):
    assert isinstance(instance.firings, str)


@given(instance=analysis::trace::TraceSizeReport_strategy)
def test_analysis::trace::tracesizereport_firings_setter(instance):
    original = instance.firings
    instance.firings = original
    assert instance.firings == original

@given(instance=analysis::map::StringToStringMap_strategy)
@settings(max_examples=50)
def test_analysis::map::stringtostringmap_instantiation(instance):
    assert isinstance(instance, analysis::map::StringToStringMap)

@given(instance=analysis::map::StringToStringMap_strategy)
def test_analysis::map::stringtostringmap_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=analysis::map::StringToStringMap_strategy)
def test_analysis::map::stringtostringmap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=analysis::map::StringToStringMap_strategy)
def test_analysis::map::stringtostringmap_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=analysis::map::StringToStringMap_strategy)
def test_analysis::map::stringtostringmap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=ActorSelectionSchedule_strategy)
@settings(max_examples=50)
def test_actorselectionschedule_instantiation(instance):
    assert isinstance(instance, ActorSelectionSchedule)

@given(instance=analysis::scheduling::FSM_strategy)
@settings(max_examples=50)
def test_analysis::scheduling::fsm_instantiation(instance):
    assert isinstance(instance, analysis::scheduling::FSM)

@given(instance=analysis::scheduling::FSM_strategy)
def test_analysis::scheduling::fsm_terminalState_type(instance):
    assert isinstance(instance.terminalState, str)


@given(instance=analysis::scheduling::FSM_strategy)
def test_analysis::scheduling::fsm_terminalState_setter(instance):
    original = instance.terminalState
    instance.terminalState = original
    assert instance.terminalState == original

@given(instance=analysis::scheduling::FSM_strategy)
def test_analysis::scheduling::fsm_startState_type(instance):
    assert isinstance(instance.startState, str)


@given(instance=analysis::scheduling::FSM_strategy)
def test_analysis::scheduling::fsm_startState_setter(instance):
    original = instance.startState
    instance.startState = original
    assert instance.startState == original

@given(instance=analysis::scheduling::ActorFire_strategy)
@settings(max_examples=50)
def test_analysis::scheduling::actorfire_instantiation(instance):
    assert isinstance(instance, analysis::scheduling::ActorFire)

@given(instance=analysis::scheduling::ActorFire_strategy)
def test_analysis::scheduling::actorfire_Actor_type(instance):
    assert isinstance(instance.Actor, str)


@given(instance=analysis::scheduling::ActorFire_strategy)
def test_analysis::scheduling::actorfire_Actor_setter(instance):
    original = instance.Actor
    instance.Actor = original
    assert instance.Actor == original

@given(instance=analysis::scheduling::ActorFire_strategy)
def test_analysis::scheduling::actorfire_partition_type(instance):
    assert isinstance(instance.partition, str)


@given(instance=analysis::scheduling::ActorFire_strategy)
def test_analysis::scheduling::actorfire_partition_setter(instance):
    original = instance.partition
    instance.partition = original
    assert instance.partition == original

@given(instance=analysis::scheduling::ActorFire_strategy)
def test_analysis::scheduling::actorfire_dependencyPartitions_type(instance):
    assert isinstance(instance.dependencyPartitions, str)


@given(instance=analysis::scheduling::ActorFire_strategy)
def test_analysis::scheduling::actorfire_dependencyPartitions_setter(instance):
    original = instance.dependencyPartitions
    instance.dependencyPartitions = original
    assert instance.dependencyPartitions == original

@given(instance=analysis::scheduling::ActorFire_strategy)
def test_analysis::scheduling::actorfire_Times_type(instance):
    assert isinstance(instance.Times, int)


@given(instance=analysis::scheduling::ActorFire_strategy)
def test_analysis::scheduling::actorfire_Times_setter(instance):
    original = instance.Times
    instance.Times = original
    assert instance.Times == original

@given(instance=analysis::caseoptimal::CaseOptimalActorSelectionSchedule_strategy)
@settings(max_examples=50)
def test_analysis::caseoptimal::caseoptimalactorselectionschedule_instantiation(instance):
    assert isinstance(instance, analysis::caseoptimal::CaseOptimalActorSelectionSchedule)

@given(instance=analysis::scheduling::Sequence_strategy)
@settings(max_examples=50)
def test_analysis::scheduling::sequence_instantiation(instance):
    assert isinstance(instance, analysis::scheduling::Sequence)

@given(instance=analysis::map::PartitionToActorSelectionScheduleMap_strategy)
@settings(max_examples=50)
def test_analysis::map::partitiontoactorselectionschedulemap_instantiation(instance):
    assert isinstance(instance, analysis::map::PartitionToActorSelectionScheduleMap)

@given(instance=analysis::map::PartitionToActorSelectionScheduleMap_strategy)
def test_analysis::map::partitiontoactorselectionschedulemap_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=analysis::map::PartitionToActorSelectionScheduleMap_strategy)
def test_analysis::map::partitiontoactorselectionschedulemap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=analysis::map::BufferToDoubleMap_strategy)
@settings(max_examples=50)
def test_analysis::map::buffertodoublemap_instantiation(instance):
    assert isinstance(instance, analysis::map::BufferToDoubleMap)

@given(instance=analysis::map::BufferToDoubleMap_strategy)
def test_analysis::map::buffertodoublemap_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=analysis::map::BufferToDoubleMap_strategy)
def test_analysis::map::buffertodoublemap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=analysis::map::BufferToIntegerMap_strategy)
@settings(max_examples=50)
def test_analysis::map::buffertointegermap_instantiation(instance):
    assert isinstance(instance, analysis::map::BufferToIntegerMap)

@given(instance=analysis::map::BufferToIntegerMap_strategy)
def test_analysis::map::buffertointegermap_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=analysis::map::BufferToIntegerMap_strategy)
def test_analysis::map::buffertointegermap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=map::analysis::Procedure_strategy)
@settings(max_examples=50)
def test_map::analysis::procedure_instantiation(instance):
    assert isinstance(instance, map::analysis::Procedure)

@given(instance=analysis::map::StringToDoubleMap_strategy)
@settings(max_examples=50)
def test_analysis::map::stringtodoublemap_instantiation(instance):
    assert isinstance(instance, analysis::map::StringToDoubleMap)

@given(instance=analysis::map::StringToDoubleMap_strategy)
def test_analysis::map::stringtodoublemap_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=analysis::map::StringToDoubleMap_strategy)
def test_analysis::map::stringtodoublemap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=analysis::map::StringToDoubleMap_strategy)
def test_analysis::map::stringtodoublemap_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=analysis::map::StringToDoubleMap_strategy)
def test_analysis::map::stringtodoublemap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=map::analysis::Port_strategy)
@settings(max_examples=50)
def test_map::analysis::port_instantiation(instance):
    assert isinstance(instance, map::analysis::Port)

@given(instance=analysis::map::PortToLongMap_strategy)
@settings(max_examples=50)
def test_analysis::map::porttolongmap_instantiation(instance):
    assert isinstance(instance, analysis::map::PortToLongMap)

@given(instance=analysis::map::PortToLongMap_strategy)
def test_analysis::map::porttolongmap_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=analysis::map::PortToLongMap_strategy)
def test_analysis::map::porttolongmap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=map::analysis::Guard_strategy)
@settings(max_examples=50)
def test_map::analysis::guard_instantiation(instance):
    assert isinstance(instance, map::analysis::Guard)

@given(instance=analysis::map::GuardToLongMap_strategy)
@settings(max_examples=50)
def test_analysis::map::guardtolongmap_instantiation(instance):
    assert isinstance(instance, analysis::map::GuardToLongMap)

@given(instance=analysis::map::GuardToLongMap_strategy)
def test_analysis::map::guardtolongmap_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=analysis::map::GuardToLongMap_strategy)
def test_analysis::map::guardtolongmap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=analysis::map::VariableToLongMap_strategy)
@settings(max_examples=50)
def test_analysis::map::variabletolongmap_instantiation(instance):
    assert isinstance(instance, analysis::map::VariableToLongMap)

@given(instance=analysis::map::VariableToLongMap_strategy)
def test_analysis::map::variabletolongmap_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=analysis::map::VariableToLongMap_strategy)
def test_analysis::map::variabletolongmap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=analysis::map::DoubleToDoubleMap_strategy)
@settings(max_examples=50)
def test_analysis::map::doubletodoublemap_instantiation(instance):
    assert isinstance(instance, analysis::map::DoubleToDoubleMap)

@given(instance=analysis::map::DoubleToDoubleMap_strategy)
def test_analysis::map::doubletodoublemap_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=analysis::map::DoubleToDoubleMap_strategy)
def test_analysis::map::doubletodoublemap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=analysis::map::DoubleToDoubleMap_strategy)
def test_analysis::map::doubletodoublemap_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=analysis::map::DoubleToDoubleMap_strategy)
def test_analysis::map::doubletodoublemap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=analysis::map::StringToLongMap_strategy)
@settings(max_examples=50)
def test_analysis::map::stringtolongmap_instantiation(instance):
    assert isinstance(instance, analysis::map::StringToLongMap)

@given(instance=analysis::map::StringToLongMap_strategy)
def test_analysis::map::stringtolongmap_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=analysis::map::StringToLongMap_strategy)
def test_analysis::map::stringtolongmap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=analysis::map::StringToLongMap_strategy)
def test_analysis::map::stringtolongmap_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=analysis::map::StringToLongMap_strategy)
def test_analysis::map::stringtolongmap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=analysis::map::BufferToLongMap_strategy)
@settings(max_examples=50)
def test_analysis::map::buffertolongmap_instantiation(instance):
    assert isinstance(instance, analysis::map::BufferToLongMap)

@given(instance=analysis::map::BufferToLongMap_strategy)
def test_analysis::map::buffertolongmap_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=analysis::map::BufferToLongMap_strategy)
def test_analysis::map::buffertolongmap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=analysis::map::ActorToLongMap_strategy)
@settings(max_examples=50)
def test_analysis::map::actortolongmap_instantiation(instance):
    assert isinstance(instance, analysis::map::ActorToLongMap)

@given(instance=analysis::map::ActorToLongMap_strategy)
def test_analysis::map::actortolongmap_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=analysis::map::ActorToLongMap_strategy)
def test_analysis::map::actortolongmap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=analysis::map::ActionToLongMap_strategy)
@settings(max_examples=50)
def test_analysis::map::actiontolongmap_instantiation(instance):
    assert isinstance(instance, analysis::map::ActionToLongMap)

@given(instance=analysis::map::ActionToLongMap_strategy)
def test_analysis::map::actiontolongmap_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=analysis::map::ActionToLongMap_strategy)
def test_analysis::map::actiontolongmap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=analysis::map::EOperatorToStatisticalDataMap_strategy)
@settings(max_examples=50)
def test_analysis::map::eoperatortostatisticaldatamap_instantiation(instance):
    assert isinstance(instance, analysis::map::EOperatorToStatisticalDataMap)

@given(instance=analysis::map::EOperatorToStatisticalDataMap_strategy)
def test_analysis::map::eoperatortostatisticaldatamap_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=analysis::map::EOperatorToStatisticalDataMap_strategy)
def test_analysis::map::eoperatortostatisticaldatamap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=map::analysis::ActorClass_strategy)
@settings(max_examples=50)
def test_map::analysis::actorclass_instantiation(instance):
    assert isinstance(instance, map::analysis::ActorClass)

@given(instance=analysis::map::ActorClassToStatisticalDataMap_strategy)
@settings(max_examples=50)
def test_analysis::map::actorclasstostatisticaldatamap_instantiation(instance):
    assert isinstance(instance, analysis::map::ActorClassToStatisticalDataMap)

@given(instance=map::analysis::Variable_strategy)
@settings(max_examples=50)
def test_map::analysis::variable_instantiation(instance):
    assert isinstance(instance, map::analysis::Variable)

@given(instance=analysis::map::VariableToStatisticalDataMap_strategy)
@settings(max_examples=50)
def test_analysis::map::variabletostatisticaldatamap_instantiation(instance):
    assert isinstance(instance, analysis::map::VariableToStatisticalDataMap)

@given(instance=analysis::map::ProcedureToStatisticalDataMap_strategy)
@settings(max_examples=50)
def test_analysis::map::proceduretostatisticaldatamap_instantiation(instance):
    assert isinstance(instance, analysis::map::ProcedureToStatisticalDataMap)

@given(instance=map::analysis::Buffer_strategy)
@settings(max_examples=50)
def test_map::analysis::buffer_instantiation(instance):
    assert isinstance(instance, map::analysis::Buffer)

@given(instance=analysis::map::BufferToStatisticalDataMap_strategy)
@settings(max_examples=50)
def test_analysis::map::buffertostatisticaldatamap_instantiation(instance):
    assert isinstance(instance, analysis::map::BufferToStatisticalDataMap)

@given(instance=map::analysis::Action_strategy)
@settings(max_examples=50)
def test_map::analysis::action_instantiation(instance):
    assert isinstance(instance, map::analysis::Action)

@given(instance=analysis::map::ActionToStatisticalDataMap_strategy)
@settings(max_examples=50)
def test_analysis::map::actiontostatisticaldatamap_instantiation(instance):
    assert isinstance(instance, analysis::map::ActionToStatisticalDataMap)

@given(instance=map::analysis::StatisticalData_strategy)
@settings(max_examples=50)
def test_map::analysis::statisticaldata_instantiation(instance):
    assert isinstance(instance, map::analysis::StatisticalData)

@given(instance=map::analysis::Actor_strategy)
@settings(max_examples=50)
def test_map::analysis::actor_instantiation(instance):
    assert isinstance(instance, map::analysis::Actor)

@given(instance=analysis::map::ActorToStatisticalDataMap_strategy)
@settings(max_examples=50)
def test_analysis::map::actortostatisticaldatamap_instantiation(instance):
    assert isinstance(instance, analysis::map::ActorToStatisticalDataMap)

@given(instance=analysis::map::StringToIntegerMap_strategy)
@settings(max_examples=50)
def test_analysis::map::stringtointegermap_instantiation(instance):
    assert isinstance(instance, analysis::map::StringToIntegerMap)

@given(instance=analysis::map::StringToIntegerMap_strategy)
def test_analysis::map::stringtointegermap_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=analysis::map::StringToIntegerMap_strategy)
def test_analysis::map::stringtointegermap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=analysis::map::StringToIntegerMap_strategy)
def test_analysis::map::stringtointegermap_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=analysis::map::StringToIntegerMap_strategy)
def test_analysis::map::stringtointegermap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=StringToStringMap_strategy)
@settings(max_examples=50)
def test_stringtostringmap_instantiation(instance):
    assert isinstance(instance, StringToStringMap)

@given(instance=analysis::profiler::TableRow_strategy)
@settings(max_examples=50)
def test_analysis::profiler::tablerow_instantiation(instance):
    assert isinstance(instance, analysis::profiler::TableRow)

@given(instance=TableRow_strategy)
@settings(max_examples=50)
def test_tablerow_instantiation(instance):
    assert isinstance(instance, TableRow)

@given(instance=analysis::profiler::BenchmarkReport_strategy)
@settings(max_examples=50)
def test_analysis::profiler::benchmarkreport_instantiation(instance):
    assert isinstance(instance, analysis::profiler::BenchmarkReport)

@given(instance=analysis::profiler::BenchmarkReport_strategy)
def test_analysis::profiler::benchmarkreport_column_names_type(instance):
    assert isinstance(instance.column_names, str)


@given(instance=analysis::profiler::BenchmarkReport_strategy)
def test_analysis::profiler::benchmarkreport_column_names_setter(instance):
    original = instance.column_names
    instance.column_names = original
    assert instance.column_names == original

@given(instance=AccessData_strategy)
@settings(max_examples=50)
def test_accessdata_instantiation(instance):
    assert isinstance(instance, AccessData)

@given(instance=analysis::profiler::StringToAccessDataMap_strategy)
@settings(max_examples=50)
def test_analysis::profiler::stringtoaccessdatamap_instantiation(instance):
    assert isinstance(instance, analysis::profiler::StringToAccessDataMap)

@given(instance=analysis::profiler::StringToAccessDataMap_strategy)
def test_analysis::profiler::stringtoaccessdatamap_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=analysis::profiler::StringToAccessDataMap_strategy)
def test_analysis::profiler::stringtoaccessdatamap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=analysis::profiler::AccessData_strategy)
@settings(max_examples=50)
def test_analysis::profiler::accessdata_instantiation(instance):
    assert isinstance(instance, analysis::profiler::AccessData)

@given(instance=analysis::profiler::AccessData_strategy)
def test_analysis::profiler::accessdata_accesses_type(instance):
    assert isinstance(instance.accesses, float)


@given(instance=analysis::profiler::AccessData_strategy)
def test_analysis::profiler::accessdata_accesses_setter(instance):
    original = instance.accesses
    instance.accesses = original
    assert instance.accesses == original

@given(instance=analysis::profiler::AccessData_strategy)
def test_analysis::profiler::accessdata_total_type(instance):
    assert isinstance(instance.total, float)


@given(instance=analysis::profiler::AccessData_strategy)
def test_analysis::profiler::accessdata_total_setter(instance):
    original = instance.total
    instance.total = original
    assert instance.total == original

@given(instance=analysis::profiler::AccessData_strategy)
def test_analysis::profiler::accessdata_min_type(instance):
    assert isinstance(instance.min, float)


@given(instance=analysis::profiler::AccessData_strategy)
def test_analysis::profiler::accessdata_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=analysis::profiler::AccessData_strategy)
def test_analysis::profiler::accessdata_average_type(instance):
    assert isinstance(instance.average, float)


@given(instance=analysis::profiler::AccessData_strategy)
def test_analysis::profiler::accessdata_average_setter(instance):
    original = instance.average
    instance.average = original
    assert instance.average == original

@given(instance=analysis::profiler::AccessData_strategy)
def test_analysis::profiler::accessdata_max_type(instance):
    assert isinstance(instance.max, float)


@given(instance=analysis::profiler::AccessData_strategy)
def test_analysis::profiler::accessdata_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=profiler::analysis::Procedure_strategy)
@settings(max_examples=50)
def test_profiler::analysis::procedure_instantiation(instance):
    assert isinstance(instance, profiler::analysis::Procedure)

@given(instance=StringToAccessDataMap_strategy)
@settings(max_examples=50)
def test_stringtoaccessdatamap_instantiation(instance):
    assert isinstance(instance, StringToAccessDataMap)

@given(instance=analysis::profiler::MemoryAccessData_strategy)
@settings(max_examples=50)
def test_analysis::profiler::memoryaccessdata_instantiation(instance):
    assert isinstance(instance, analysis::profiler::MemoryAccessData)

@given(instance=MemoryAccessData_strategy)
@settings(max_examples=50)
def test_memoryaccessdata_instantiation(instance):
    assert isinstance(instance, MemoryAccessData)

@given(instance=analysis::profiler::SharedVariableAccessData_strategy)
@settings(max_examples=50)
def test_analysis::profiler::sharedvariableaccessdata_instantiation(instance):
    assert isinstance(instance, analysis::profiler::SharedVariableAccessData)

@given(instance=analysis::profiler::SharedVariableAccessData_strategy)
def test_analysis::profiler::sharedvariableaccessdata_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=analysis::profiler::SharedVariableAccessData_strategy)
def test_analysis::profiler::sharedvariableaccessdata_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=analysis::profiler::BufferAccessData_strategy)
@settings(max_examples=50)
def test_analysis::profiler::bufferaccessdata_instantiation(instance):
    assert isinstance(instance, analysis::profiler::BufferAccessData)

@given(instance=analysis::profiler::BufferAccessData_strategy)
def test_analysis::profiler::bufferaccessdata_sourceActor_type(instance):
    assert isinstance(instance.sourceActor, str)


@given(instance=analysis::profiler::BufferAccessData_strategy)
def test_analysis::profiler::bufferaccessdata_sourceActor_setter(instance):
    original = instance.sourceActor
    instance.sourceActor = original
    assert instance.sourceActor == original

@given(instance=analysis::profiler::BufferAccessData_strategy)
def test_analysis::profiler::bufferaccessdata_targetActor_type(instance):
    assert isinstance(instance.targetActor, str)


@given(instance=analysis::profiler::BufferAccessData_strategy)
def test_analysis::profiler::bufferaccessdata_targetActor_setter(instance):
    original = instance.targetActor
    instance.targetActor = original
    assert instance.targetActor == original

@given(instance=analysis::profiler::BufferAccessData_strategy)
def test_analysis::profiler::bufferaccessdata_targetPort_type(instance):
    assert isinstance(instance.targetPort, str)


@given(instance=analysis::profiler::BufferAccessData_strategy)
def test_analysis::profiler::bufferaccessdata_targetPort_setter(instance):
    original = instance.targetPort
    instance.targetPort = original
    assert instance.targetPort == original

@given(instance=analysis::profiler::BufferAccessData_strategy)
def test_analysis::profiler::bufferaccessdata_sourcePort_type(instance):
    assert isinstance(instance.sourcePort, str)


@given(instance=analysis::profiler::BufferAccessData_strategy)
def test_analysis::profiler::bufferaccessdata_sourcePort_setter(instance):
    original = instance.sourcePort
    instance.sourcePort = original
    assert instance.sourcePort == original

@given(instance=analysis::profiler::LocalVariableAccessData_strategy)
@settings(max_examples=50)
def test_analysis::profiler::localvariableaccessdata_instantiation(instance):
    assert isinstance(instance, analysis::profiler::LocalVariableAccessData)

@given(instance=analysis::profiler::LocalVariableAccessData_strategy)
def test_analysis::profiler::localvariableaccessdata_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=analysis::profiler::LocalVariableAccessData_strategy)
def test_analysis::profiler::localvariableaccessdata_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=analysis::profiler::StateVariableAccessData_strategy)
@settings(max_examples=50)
def test_analysis::profiler::statevariableaccessdata_instantiation(instance):
    assert isinstance(instance, analysis::profiler::StateVariableAccessData)

@given(instance=analysis::profiler::StateVariableAccessData_strategy)
def test_analysis::profiler::statevariableaccessdata_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=analysis::profiler::StateVariableAccessData_strategy)
def test_analysis::profiler::statevariableaccessdata_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=analysis::profiler::ActionMemoryProfilingData_strategy)
@settings(max_examples=50)
def test_analysis::profiler::actionmemoryprofilingdata_instantiation(instance):
    assert isinstance(instance, analysis::profiler::ActionMemoryProfilingData)

@given(instance=analysis::profiler::ActionMemoryProfilingData_strategy)
def test_analysis::profiler::actionmemoryprofilingdata_actor_type(instance):
    assert isinstance(instance.actor, str)


@given(instance=analysis::profiler::ActionMemoryProfilingData_strategy)
def test_analysis::profiler::actionmemoryprofilingdata_actor_setter(instance):
    original = instance.actor
    instance.actor = original
    assert instance.actor == original

@given(instance=analysis::profiler::ActionMemoryProfilingData_strategy)
def test_analysis::profiler::actionmemoryprofilingdata_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=analysis::profiler::ActionMemoryProfilingData_strategy)
def test_analysis::profiler::actionmemoryprofilingdata_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=ActionMemoryProfilingData_strategy)
@settings(max_examples=50)
def test_actionmemoryprofilingdata_instantiation(instance):
    assert isinstance(instance, ActionMemoryProfilingData)

@given(instance=analysis::profiler::MemoryProfilingReport_strategy)
@settings(max_examples=50)
def test_analysis::profiler::memoryprofilingreport_instantiation(instance):
    assert isinstance(instance, analysis::profiler::MemoryProfilingReport)

@given(instance=analysis::profiler::MemoryProfilingReport_strategy)
def test_analysis::profiler::memoryprofilingreport_networkName_type(instance):
    assert isinstance(instance.networkName, str)


@given(instance=analysis::profiler::MemoryProfilingReport_strategy)
def test_analysis::profiler::memoryprofilingreport_networkName_setter(instance):
    original = instance.networkName
    instance.networkName = original
    assert instance.networkName == original

@given(instance=ActionDynamicData_strategy)
@settings(max_examples=50)
def test_actiondynamicdata_instantiation(instance):
    assert isinstance(instance, ActionDynamicData)

@given(instance=analysis::profiler::ProcedureToComplexDynamicDataMap_strategy)
@settings(max_examples=50)
def test_analysis::profiler::proceduretocomplexdynamicdatamap_instantiation(instance):
    assert isinstance(instance, analysis::profiler::ProcedureToComplexDynamicDataMap)

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

@given(instance=analysis::profiler::ComplexDynamicData_strategy)
@settings(max_examples=50)
def test_analysis::profiler::complexdynamicdata_instantiation(instance):
    assert isinstance(instance, analysis::profiler::ComplexDynamicData)

@given(instance=ActionToLongMap_strategy)
@settings(max_examples=50)
def test_actiontolongmap_instantiation(instance):
    assert isinstance(instance, ActionToLongMap)
