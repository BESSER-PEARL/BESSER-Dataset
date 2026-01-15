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

# Classes
jbatch_Analyzer = Class(name="jbatch::Analyzer")
jbatch_ItemProcessor = Class(name="jbatch::ItemProcessor")
jbatch_Properties = Class(name="jbatch::Properties")
jbatch_Batchlet = Class(name="jbatch::Batchlet")
jbatch_CheckpointAlgorithm = Class(name="jbatch::CheckpointAlgorithm")
jbatch_Chunk = Class(name="jbatch::Chunk")
jbatch_ItemReader = Class(name="jbatch::ItemReader")
jbatch_ItemWriter = Class(name="jbatch::ItemWriter")
jbatch_ExceptionClassFilter = Class(name="jbatch::ExceptionClassFilter")
jbatch_Collector = Class(name="jbatch::Collector")
jbatch_Decision = Class(name="jbatch::Decision")
jbatch_DocumentRoot = Class(name="jbatch::DocumentRoot")
jbatch_End = Class(name="jbatch::End")
jbatch_Fail = Class(name="jbatch::Fail")
jbatch_Next = Class(name="jbatch::Next")
jbatch_Stop = Class(name="jbatch::Stop")
jbatch_EStringToStringMapEntry = Class(name="jbatch::EStringToStringMapEntry")
jbatch_Flow = Class(name="jbatch::Flow")
jbatch_Job = Class(name="jbatch::Job")
jbatch_IncludeType = Class(name="jbatch::IncludeType")
jbatch_ExcludeType = Class(name="jbatch::ExcludeType")
jbatch_Step = Class(name="jbatch::Step")
jbatch_Split = Class(name="jbatch::Split")
jbatch_Listeners = Class(name="jbatch::Listeners")
jbatch_Listener = Class(name="jbatch::Listener")
jbatch_PartitionPlan = Class(name="jbatch::PartitionPlan")
jbatch_Partition = Class(name="jbatch::Partition")
jbatch_PartitionMapper = Class(name="jbatch::PartitionMapper")
jbatch_PartitionReducer = Class(name="jbatch::PartitionReducer")
jbatch_Property = Class(name="jbatch::Property")

# jbatch_Analyzer class attributes and methods
jbatch_Analyzer_ref: Property = Property(name="ref", type=StringType)
jbatch_Analyzer.attributes={jbatch_Analyzer_ref}

# jbatch_ItemProcessor class attributes and methods
jbatch_ItemProcessor_ref: Property = Property(name="ref", type=StringType)
jbatch_ItemProcessor.attributes={jbatch_ItemProcessor_ref}

# jbatch_Properties class attributes and methods
jbatch_Properties_partition: Property = Property(name="partition", type=StringType)
jbatch_Properties.attributes={jbatch_Properties_partition}

# jbatch_Batchlet class attributes and methods
jbatch_Batchlet_ref: Property = Property(name="ref", type=StringType)
jbatch_Batchlet.attributes={jbatch_Batchlet_ref}

# jbatch_CheckpointAlgorithm class attributes and methods
jbatch_CheckpointAlgorithm_ref: Property = Property(name="ref", type=StringType)
jbatch_CheckpointAlgorithm.attributes={jbatch_CheckpointAlgorithm_ref}

# jbatch_Chunk class attributes and methods
jbatch_Chunk_timeLimit: Property = Property(name="timeLimit", type=StringType)
jbatch_Chunk_checkpointPolicy: Property = Property(name="checkpointPolicy", type=StringType)
jbatch_Chunk_itemCount: Property = Property(name="itemCount", type=StringType)
jbatch_Chunk_retryLimit: Property = Property(name="retryLimit", type=StringType)
jbatch_Chunk_skipLimit: Property = Property(name="skipLimit", type=StringType)
jbatch_Chunk.attributes={jbatch_Chunk_skipLimit, jbatch_Chunk_retryLimit, jbatch_Chunk_timeLimit, jbatch_Chunk_itemCount, jbatch_Chunk_checkpointPolicy}

# jbatch_ItemReader class attributes and methods
jbatch_ItemReader_ref: Property = Property(name="ref", type=StringType)
jbatch_ItemReader.attributes={jbatch_ItemReader_ref}

# jbatch_ItemWriter class attributes and methods
jbatch_ItemWriter_ref: Property = Property(name="ref", type=StringType)
jbatch_ItemWriter.attributes={jbatch_ItemWriter_ref}

# jbatch_ExceptionClassFilter class attributes and methods

# jbatch_Collector class attributes and methods
jbatch_Collector_ref: Property = Property(name="ref", type=StringType)
jbatch_Collector.attributes={jbatch_Collector_ref}

# jbatch_Decision class attributes and methods
jbatch_Decision_transitionElements: Property = Property(name="transitionElements", type=StringType)
jbatch_Decision_ref: Property = Property(name="ref", type=StringType)
jbatch_Decision_id: Property = Property(name="id", type=StringType)
jbatch_Decision.attributes={jbatch_Decision_transitionElements, jbatch_Decision_ref, jbatch_Decision_id}

# jbatch_DocumentRoot class attributes and methods
jbatch_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
jbatch_DocumentRoot.attributes={jbatch_DocumentRoot_mixed}

# jbatch_End class attributes and methods
jbatch_End_exitStatus: Property = Property(name="exitStatus", type=StringType)
jbatch_End_on: Property = Property(name="on", type=StringType)
jbatch_End.attributes={jbatch_End_on, jbatch_End_exitStatus}

# jbatch_Fail class attributes and methods
jbatch_Fail_exitStatus: Property = Property(name="exitStatus", type=StringType)
jbatch_Fail_on: Property = Property(name="on", type=StringType)
jbatch_Fail.attributes={jbatch_Fail_exitStatus, jbatch_Fail_on}

# jbatch_Next class attributes and methods
jbatch_Next_on: Property = Property(name="on", type=StringType)
jbatch_Next_to: Property = Property(name="to", type=StringType)
jbatch_Next.attributes={jbatch_Next_to, jbatch_Next_on}

# jbatch_Stop class attributes and methods
jbatch_Stop_on: Property = Property(name="on", type=StringType)
jbatch_Stop_restart: Property = Property(name="restart", type=StringType)
jbatch_Stop_exitStatus: Property = Property(name="exitStatus", type=StringType)
jbatch_Stop.attributes={jbatch_Stop_restart, jbatch_Stop_on, jbatch_Stop_exitStatus}

# jbatch_EStringToStringMapEntry class attributes and methods

# jbatch_Flow class attributes and methods
jbatch_Flow_group: Property = Property(name="group", type=StringType)
jbatch_Flow_transitionElements: Property = Property(name="transitionElements", type=StringType)
jbatch_Flow_id: Property = Property(name="id", type=StringType)
jbatch_Flow_next1: Property = Property(name="next1", type=StringType)
jbatch_Flow.attributes={jbatch_Flow_transitionElements, jbatch_Flow_next1, jbatch_Flow_id, jbatch_Flow_group}

# jbatch_Job class attributes and methods
jbatch_Job_group: Property = Property(name="group", type=StringType)
jbatch_Job_id: Property = Property(name="id", type=StringType)
jbatch_Job_restartable: Property = Property(name="restartable", type=StringType)
jbatch_Job_version: Property = Property(name="version", type=StringType)
jbatch_Job.attributes={jbatch_Job_version, jbatch_Job_restartable, jbatch_Job_group, jbatch_Job_id}

# jbatch_IncludeType class attributes and methods
jbatch_IncludeType_class: Property = Property(name="class", type=StringType)
jbatch_IncludeType.attributes={jbatch_IncludeType_class}

# jbatch_ExcludeType class attributes and methods
jbatch_ExcludeType_class: Property = Property(name="class", type=StringType)
jbatch_ExcludeType.attributes={jbatch_ExcludeType_class}

# jbatch_Step class attributes and methods
jbatch_Step_transitionElements: Property = Property(name="transitionElements", type=StringType)
jbatch_Step_allowStartIfComplete: Property = Property(name="allowStartIfComplete", type=StringType)
jbatch_Step_id: Property = Property(name="id", type=StringType)
jbatch_Step_next1: Property = Property(name="next1", type=StringType)
jbatch_Step_startLimit: Property = Property(name="startLimit", type=StringType)
jbatch_Step.attributes={jbatch_Step_id, jbatch_Step_startLimit, jbatch_Step_allowStartIfComplete, jbatch_Step_transitionElements, jbatch_Step_next1}

# jbatch_Split class attributes and methods
jbatch_Split_next: Property = Property(name="next", type=StringType)
jbatch_Split_id: Property = Property(name="id", type=StringType)
jbatch_Split.attributes={jbatch_Split_id, jbatch_Split_next}

# jbatch_Listeners class attributes and methods

# jbatch_Listener class attributes and methods
jbatch_Listener_ref: Property = Property(name="ref", type=StringType)
jbatch_Listener.attributes={jbatch_Listener_ref}

# jbatch_PartitionPlan class attributes and methods
jbatch_PartitionPlan_partitions: Property = Property(name="partitions", type=StringType)
jbatch_PartitionPlan_threads: Property = Property(name="threads", type=StringType)
jbatch_PartitionPlan.attributes={jbatch_PartitionPlan_partitions, jbatch_PartitionPlan_threads}

# jbatch_Partition class attributes and methods

# jbatch_PartitionMapper class attributes and methods
jbatch_PartitionMapper_ref: Property = Property(name="ref", type=StringType)
jbatch_PartitionMapper.attributes={jbatch_PartitionMapper_ref}

# jbatch_PartitionReducer class attributes and methods
jbatch_PartitionReducer_ref: Property = Property(name="ref", type=StringType)
jbatch_PartitionReducer.attributes={jbatch_PartitionReducer_ref}

# jbatch_Property class attributes and methods
jbatch_Property_value: Property = Property(name="value", type=StringType)
jbatch_Property_name: Property = Property(name="name", type=StringType)
jbatch_Property.attributes={jbatch_Property_name, jbatch_Property_value}

# Relationships
properties0: BinaryAssociation = BinaryAssociation(
    name="properties0",
    ends={
        Property(name="jbatch_Properties", type=jbatch_Analyzer, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Analyzer", type=jbatch_Properties, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
processor6: BinaryAssociation = BinaryAssociation(
    name="processor6",
    ends={
        Property(name="jbatch_ItemProcessor", type=jbatch_Chunk, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Chunk7", type=jbatch_ItemProcessor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties1: BinaryAssociation = BinaryAssociation(
    name="properties1",
    ends={
        Property(name="jbatch_Properties2", type=jbatch_Batchlet, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Batchlet", type=jbatch_Properties, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties3: BinaryAssociation = BinaryAssociation(
    name="properties3",
    ends={
        Property(name="jbatch_Properties4", type=jbatch_CheckpointAlgorithm, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_CheckpointAlgorithm", type=jbatch_Properties, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reader5: BinaryAssociation = BinaryAssociation(
    name="reader5",
    ends={
        Property(name="jbatch_ItemReader", type=jbatch_Chunk, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Chunk", type=jbatch_ItemReader, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
writer8: BinaryAssociation = BinaryAssociation(
    name="writer8",
    ends={
        Property(name="jbatch_ItemWriter", type=jbatch_Chunk, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Chunk9", type=jbatch_ItemWriter, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
checkpointAlgorithm10: BinaryAssociation = BinaryAssociation(
    name="checkpointAlgorithm10",
    ends={
        Property(name="jbatch_CheckpointAlgorithm12", type=jbatch_Chunk, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Chunk11", type=jbatch_CheckpointAlgorithm, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
skippableExceptionClasses13: BinaryAssociation = BinaryAssociation(
    name="skippableExceptionClasses13",
    ends={
        Property(name="jbatch_ExceptionClassFilter", type=jbatch_Chunk, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Chunk14", type=jbatch_ExceptionClassFilter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
retryableExceptionClasses15: BinaryAssociation = BinaryAssociation(
    name="retryableExceptionClasses15",
    ends={
        Property(name="jbatch_ExceptionClassFilter17", type=jbatch_Chunk, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Chunk16", type=jbatch_ExceptionClassFilter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
noRollbackExceptionClasses18: BinaryAssociation = BinaryAssociation(
    name="noRollbackExceptionClasses18",
    ends={
        Property(name="jbatch_ExceptionClassFilter20", type=jbatch_Chunk, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Chunk19", type=jbatch_ExceptionClassFilter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties21: BinaryAssociation = BinaryAssociation(
    name="properties21",
    ends={
        Property(name="jbatch_Properties22", type=jbatch_Collector, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Collector", type=jbatch_Properties, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties23: BinaryAssociation = BinaryAssociation(
    name="properties23",
    ends={
        Property(name="jbatch_Properties24", type=jbatch_Decision, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Decision", type=jbatch_Properties, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
end25: BinaryAssociation = BinaryAssociation(
    name="end25",
    ends={
        Property(name="jbatch_End", type=jbatch_Decision, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Decision26", type=jbatch_End, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fail27: BinaryAssociation = BinaryAssociation(
    name="fail27",
    ends={
        Property(name="jbatch_Fail", type=jbatch_Decision, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Decision28", type=jbatch_Fail, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
next29: BinaryAssociation = BinaryAssociation(
    name="next29",
    ends={
        Property(name="jbatch_Next", type=jbatch_Decision, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Decision30", type=jbatch_Next, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stop31: BinaryAssociation = BinaryAssociation(
    name="stop31",
    ends={
        Property(name="jbatch_Stop", type=jbatch_Decision, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Decision32", type=jbatch_Stop, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xMLNSPrefixMap33: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap33",
    ends={
        Property(name="jbatch_EStringToStringMapEntry", type=jbatch_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_DocumentRoot", type=jbatch_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation34: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation34",
    ends={
        Property(name="jbatch_EStringToStringMapEntry36", type=jbatch_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_DocumentRoot35", type=jbatch_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
job37: BinaryAssociation = BinaryAssociation(
    name="job37",
    ends={
        Property(name="jbatch_Job", type=jbatch_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_DocumentRoot38", type=jbatch_Job, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
include39: BinaryAssociation = BinaryAssociation(
    name="include39",
    ends={
        Property(name="jbatch_IncludeType", type=jbatch_ExceptionClassFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_ExceptionClassFilter40", type=jbatch_IncludeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exclude41: BinaryAssociation = BinaryAssociation(
    name="exclude41",
    ends={
        Property(name="jbatch_ExcludeType", type=jbatch_ExceptionClassFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_ExceptionClassFilter42", type=jbatch_ExcludeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
step50: BinaryAssociation = BinaryAssociation(
    name="step50",
    ends={
        Property(name="jbatch_Step", type=jbatch_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Flow51", type=jbatch_Step, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
decision43: BinaryAssociation = BinaryAssociation(
    name="decision43",
    ends={
        Property(name="jbatch_Decision44", type=jbatch_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Flow", type=jbatch_Decision, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
flow46: BinaryAssociation = BinaryAssociation(
    name="flow46",
    ends={
        Property(name="jbatch_Flow47", type=jbatch_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Flow45", type=jbatch_Flow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
split48: BinaryAssociation = BinaryAssociation(
    name="split48",
    ends={
        Property(name="jbatch_Split", type=jbatch_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Flow49", type=jbatch_Split, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
end52: BinaryAssociation = BinaryAssociation(
    name="end52",
    ends={
        Property(name="jbatch_End54", type=jbatch_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Flow53", type=jbatch_End, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fail55: BinaryAssociation = BinaryAssociation(
    name="fail55",
    ends={
        Property(name="jbatch_Fail57", type=jbatch_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Flow56", type=jbatch_Fail, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
next58: BinaryAssociation = BinaryAssociation(
    name="next58",
    ends={
        Property(name="jbatch_Next60", type=jbatch_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Flow59", type=jbatch_Next, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties64: BinaryAssociation = BinaryAssociation(
    name="properties64",
    ends={
        Property(name="jbatch_Properties66", type=jbatch_ItemProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_ItemProcessor65", type=jbatch_Properties, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stop61: BinaryAssociation = BinaryAssociation(
    name="stop61",
    ends={
        Property(name="jbatch_Stop63", type=jbatch_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Flow62", type=jbatch_Stop, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties70: BinaryAssociation = BinaryAssociation(
    name="properties70",
    ends={
        Property(name="jbatch_ItemWriter71", type=jbatch_Properties, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="jbatch_Properties72", type=jbatch_ItemWriter, multiplicity=Multiplicity(1, 1))
    }
)
properties67: BinaryAssociation = BinaryAssociation(
    name="properties67",
    ends={
        Property(name="jbatch_Properties69", type=jbatch_ItemReader, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_ItemReader68", type=jbatch_Properties, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
listeners76: BinaryAssociation = BinaryAssociation(
    name="listeners76",
    ends={
        Property(name="jbatch_Listeners", type=jbatch_Job, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Job77", type=jbatch_Listeners, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties73: BinaryAssociation = BinaryAssociation(
    name="properties73",
    ends={
        Property(name="jbatch_Properties75", type=jbatch_Job, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Job74", type=jbatch_Properties, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
flow81: BinaryAssociation = BinaryAssociation(
    name="flow81",
    ends={
        Property(name="jbatch_Flow83", type=jbatch_Job, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Job82", type=jbatch_Flow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
decision78: BinaryAssociation = BinaryAssociation(
    name="decision78",
    ends={
        Property(name="jbatch_Decision80", type=jbatch_Job, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Job79", type=jbatch_Decision, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
split84: BinaryAssociation = BinaryAssociation(
    name="split84",
    ends={
        Property(name="jbatch_Split86", type=jbatch_Job, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Job85", type=jbatch_Split, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
step87: BinaryAssociation = BinaryAssociation(
    name="step87",
    ends={
        Property(name="jbatch_Step89", type=jbatch_Job, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Job88", type=jbatch_Step, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listener92: BinaryAssociation = BinaryAssociation(
    name="listener92",
    ends={
        Property(name="jbatch_Listener94", type=jbatch_Listeners, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Listeners93", type=jbatch_Listener, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties90: BinaryAssociation = BinaryAssociation(
    name="properties90",
    ends={
        Property(name="jbatch_Properties91", type=jbatch_Listener, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Listener", type=jbatch_Properties, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
plan96: BinaryAssociation = BinaryAssociation(
    name="plan96",
    ends={
        Property(name="jbatch_PartitionPlan", type=jbatch_Partition, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Partition97", type=jbatch_PartitionPlan, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
collector98: BinaryAssociation = BinaryAssociation(
    name="collector98",
    ends={
        Property(name="jbatch_Collector100", type=jbatch_Partition, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Partition99", type=jbatch_Collector, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
analyzer101: BinaryAssociation = BinaryAssociation(
    name="analyzer101",
    ends={
        Property(name="jbatch_Analyzer103", type=jbatch_Partition, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Partition102", type=jbatch_Analyzer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mapper95: BinaryAssociation = BinaryAssociation(
    name="mapper95",
    ends={
        Property(name="jbatch_PartitionMapper", type=jbatch_Partition, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Partition", type=jbatch_PartitionMapper, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties109: BinaryAssociation = BinaryAssociation(
    name="properties109",
    ends={
        Property(name="jbatch_Properties111", type=jbatch_PartitionPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_PartitionPlan110", type=jbatch_Properties, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reducer104: BinaryAssociation = BinaryAssociation(
    name="reducer104",
    ends={
        Property(name="jbatch_PartitionReducer", type=jbatch_Partition, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Partition105", type=jbatch_PartitionReducer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties106: BinaryAssociation = BinaryAssociation(
    name="properties106",
    ends={
        Property(name="jbatch_Properties108", type=jbatch_PartitionMapper, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_PartitionMapper107", type=jbatch_Properties, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
property115: BinaryAssociation = BinaryAssociation(
    name="property115",
    ends={
        Property(name="jbatch_Property", type=jbatch_Properties, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Properties116", type=jbatch_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties112: BinaryAssociation = BinaryAssociation(
    name="properties112",
    ends={
        Property(name="jbatch_Properties114", type=jbatch_PartitionReducer, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_PartitionReducer113", type=jbatch_Properties, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
flow117: BinaryAssociation = BinaryAssociation(
    name="flow117",
    ends={
        Property(name="jbatch_Flow119", type=jbatch_Split, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Split118", type=jbatch_Flow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listeners123: BinaryAssociation = BinaryAssociation(
    name="listeners123",
    ends={
        Property(name="jbatch_Listeners125", type=jbatch_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Step124", type=jbatch_Listeners, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
batchlet126: BinaryAssociation = BinaryAssociation(
    name="batchlet126",
    ends={
        Property(name="jbatch_Batchlet128", type=jbatch_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Step127", type=jbatch_Batchlet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties120: BinaryAssociation = BinaryAssociation(
    name="properties120",
    ends={
        Property(name="jbatch_Properties122", type=jbatch_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Step121", type=jbatch_Properties, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
partition132: BinaryAssociation = BinaryAssociation(
    name="partition132",
    ends={
        Property(name="jbatch_Partition134", type=jbatch_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Step133", type=jbatch_Partition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
chunk129: BinaryAssociation = BinaryAssociation(
    name="chunk129",
    ends={
        Property(name="jbatch_Chunk131", type=jbatch_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Step130", type=jbatch_Chunk, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
next141: BinaryAssociation = BinaryAssociation(
    name="next141",
    ends={
        Property(name="jbatch_Step142", type=jbatch_Next, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="jbatch_Next143", type=jbatch_Step, multiplicity=Multiplicity(1, 1))
    }
)
stop144: BinaryAssociation = BinaryAssociation(
    name="stop144",
    ends={
        Property(name="jbatch_Stop146", type=jbatch_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Step145", type=jbatch_Stop, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
end135: BinaryAssociation = BinaryAssociation(
    name="end135",
    ends={
        Property(name="jbatch_End137", type=jbatch_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Step136", type=jbatch_End, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fail138: BinaryAssociation = BinaryAssociation(
    name="fail138",
    ends={
        Property(name="jbatch_Fail140", type=jbatch_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="jbatch_Step139", type=jbatch_Fail, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="jbatch",
    types={jbatch_Analyzer, jbatch_ItemProcessor, jbatch_Properties, jbatch_Batchlet, jbatch_CheckpointAlgorithm, jbatch_Chunk, jbatch_ItemReader, jbatch_ItemWriter, jbatch_ExceptionClassFilter, jbatch_Collector, jbatch_Decision, jbatch_DocumentRoot, jbatch_End, jbatch_Fail, jbatch_Next, jbatch_Stop, jbatch_EStringToStringMapEntry, jbatch_Flow, jbatch_Job, jbatch_IncludeType, jbatch_ExcludeType, jbatch_Step, jbatch_Split, jbatch_Listeners, jbatch_Listener, jbatch_PartitionPlan, jbatch_Partition, jbatch_PartitionMapper, jbatch_PartitionReducer, jbatch_Property},
    associations={properties0, processor6, properties1, properties3, reader5, writer8, checkpointAlgorithm10, skippableExceptionClasses13, retryableExceptionClasses15, noRollbackExceptionClasses18, properties21, properties23, end25, fail27, next29, stop31, xMLNSPrefixMap33, xSISchemaLocation34, job37, include39, exclude41, step50, decision43, flow46, split48, end52, fail55, next58, properties64, stop61, properties70, properties67, listeners76, properties73, flow81, decision78, split84, step87, listener92, properties90, plan96, collector98, analyzer101, mapper95, properties109, reducer104, properties106, property115, properties112, flow117, listeners123, batchlet126, properties120, partition132, chunk129, next141, stop144, end135, fail138},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)