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
SchedulingEventKind: Enumeration = Enumeration(
    name="SchedulingEventKind",
    literals={
            EnumerationLiteral(name="ACTIVATED"),
			EnumerationLiteral(name="RUNNING"),
			EnumerationLiteral(name="SUSPENDED"),
			EnumerationLiteral(name="BLOCKED"),
			EnumerationLiteral(name="TERMINATED"),
			EnumerationLiteral(name="DEADLINE")
    }
)

ResourceEventKind: Enumeration = Enumeration(
    name="ResourceEventKind",
    literals={
            EnumerationLiteral(name="ACQUIRED"),
			EnumerationLiteral(name="RELEASED"),
			EnumerationLiteral(name="REQUESTED")
    }
)

SliceKind: Enumeration = Enumeration(
    name="SliceKind",
    literals={
            EnumerationLiteral(name="OTHER"),
			EnumerationLiteral(name="TASK"),
			EnumerationLiteral(name="JOB"),
			EnumerationLiteral(name="FUNCTION"),
			EnumerationLiteral(name="FUNCTION_INSTANCE"),
			EnumerationLiteral(name="PACKET"),
			EnumerationLiteral(name="FRAME"),
			EnumerationLiteral(name="LINK"),
			EnumerationLiteral(name="RESOURCE"),
			EnumerationLiteral(name="STATE"),
			EnumerationLiteral(name="AUTOMATON"),
			EnumerationLiteral(name="TEMPORAL_CHAIN"),
			EnumerationLiteral(name="OS")
    }
)

MessageEventKind: Enumeration = Enumeration(
    name="MessageEventKind",
    literals={
            EnumerationLiteral(name="INSTANTIATED"),
			EnumerationLiteral(name="TRANSMITTED"),
			EnumerationLiteral(name="RECEIVED"),
			EnumerationLiteral(name="ERROR")
    }
)

# Classes
trace_ResourceEvent = Class(name="trace::ResourceEvent")
Event = Class(name="Event")
trace_SchedulingEvent = Class(name="trace::SchedulingEvent")
trace_Trace = Class(name="trace::Trace")
EModelElement = Class(name="EModelElement")
trace_Event = Class(name="trace::Event")
trace_Slice = Class(name="trace::Slice")
trace_Properties = Class(name="trace::Properties")
trace_MessageEvent = Class(name="trace::MessageEvent")
trace_DurationValueChangeEvent = Class(name="trace::DurationValueChangeEvent")
trace_DataSizeValueChangeEvent = Class(name="trace::DataSizeValueChangeEvent")
trace_NumberValueChangeEvent = Class(name="trace::NumberValueChangeEvent")
trace_ValueChangeEvent = Class(name="trace::ValueChangeEvent")
trace_EStructuralFeature = Class(name="trace::EStructuralFeature")
trace_EObject = Class(name="trace::EObject")
trace_ObjectValueChangeEvent = Class(name="trace::ObjectValueChangeEvent")
ValueChangeEvent = Class(name="ValueChangeEvent")

# trace_ResourceEvent class attributes and methods
trace_ResourceEvent_kind: Property = Property(name="kind", type=StringType)
trace_ResourceEvent.attributes={trace_ResourceEvent_kind}

# Event class attributes and methods

# trace_SchedulingEvent class attributes and methods
trace_SchedulingEvent_kind: Property = Property(name="kind", type=StringType)
trace_SchedulingEvent.attributes={trace_SchedulingEvent_kind}

# trace_Trace class attributes and methods
trace_Trace_hostId: Property = Property(name="hostId", type=StringType)
trace_Trace_precision: Property = Property(name="precision", type=StringType)
trace_Trace_range: Property = Property(name="range", type=StringType)
trace_Trace.attributes={trace_Trace_hostId, trace_Trace_range, trace_Trace_precision}

# EModelElement class attributes and methods

# trace_Event class attributes and methods
trace_Event_timestamp: Property = Property(name="timestamp", type=StringType)
trace_Event.attributes={trace_Event_timestamp}

# trace_Slice class attributes and methods
trace_Slice_name: Property = Property(name="name", type=StringType)
trace_Slice_kind: Property = Property(name="kind", type=StringType)
trace_Slice_kindLabel: Property = Property(name="kindLabel", type=StringType)
trace_Slice_m_getHierarchicalName: Method = Method(name="getHierarchicalName", parameters={Parameter(name='separator')}, type=StringType)
trace_Slice_m_getAggregatedEvents: Method = Method(name="getAggregatedEvents", parameters={}, type=Event)
trace_Slice_m_getLatestTimestamp: Method = Method(name="getLatestTimestamp", parameters={}, type=StringType)
trace_Slice.attributes={trace_Slice_kind, trace_Slice_name, trace_Slice_kindLabel}
trace_Slice.methods={trace_Slice_m_getAggregatedEvents, trace_Slice_m_getLatestTimestamp, trace_Slice_m_getHierarchicalName}

# trace_Properties class attributes and methods
trace_Properties_range: Property = Property(name="range", type=StringType)
trace_Properties_blockingTime: Property = Property(name="blockingTime", type=StringType)
trace_Properties_executionTime: Property = Property(name="executionTime", type=StringType)
trace_Properties_remainingTime: Property = Property(name="remainingTime", type=StringType)
trace_Properties_responseTime: Property = Property(name="responseTime", type=StringType)
trace_Properties_absoluteDeadline: Property = Property(name="absoluteDeadline", type=StringType)
trace_Properties_index: Property = Property(name="index", type=StringType)
trace_Properties.attributes={trace_Properties_remainingTime, trace_Properties_executionTime, trace_Properties_index, trace_Properties_responseTime, trace_Properties_range, trace_Properties_absoluteDeadline, trace_Properties_blockingTime}

# trace_MessageEvent class attributes and methods
trace_MessageEvent_kind: Property = Property(name="kind", type=StringType)
trace_MessageEvent.attributes={trace_MessageEvent_kind}

# trace_DurationValueChangeEvent class attributes and methods
trace_DurationValueChangeEvent_value: Property = Property(name="value", type=StringType)
trace_DurationValueChangeEvent.attributes={trace_DurationValueChangeEvent_value}

# trace_DataSizeValueChangeEvent class attributes and methods
trace_DataSizeValueChangeEvent_value: Property = Property(name="value", type=StringType)
trace_DataSizeValueChangeEvent.attributes={trace_DataSizeValueChangeEvent_value}

# trace_NumberValueChangeEvent class attributes and methods
trace_NumberValueChangeEvent_value: Property = Property(name="value", type=StringType)
trace_NumberValueChangeEvent.attributes={trace_NumberValueChangeEvent_value}

# trace_ValueChangeEvent class attributes and methods

# trace_EStructuralFeature class attributes and methods

# trace_EObject class attributes and methods

# trace_ObjectValueChangeEvent class attributes and methods

# ValueChangeEvent class attributes and methods

# Relationships
trace2: BinaryAssociation = BinaryAssociation(
    name="trace2",
    ends={
        Property(name="Trace", type=trace_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="events", type=trace_Trace, multiplicity=Multiplicity(1, 1))
    }
)
about3: BinaryAssociation = BinaryAssociation(
    name="about3",
    ends={
        Property(name="trace_Slice4", type=trace_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Event", type=trace_Slice, multiplicity=Multiplicity(0, 9999))
    }
)
events0: BinaryAssociation = BinaryAssociation(
    name="events0",
    ends={
        Property(name="Event", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace", type=trace_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
slices1: BinaryAssociation = BinaryAssociation(
    name="slices1",
    ends={
        Property(name="trace_Slice", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace", type=trace_Slice, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubSlices9: BinaryAssociation = BinaryAssociation(
    name="ownedSubSlices9",
    ends={
        Property(name="Slice", type=trace_Slice, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=trace_Slice, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent11: BinaryAssociation = BinaryAssociation(
    name="parent11",
    ends={
        Property(name="Slice12", type=trace_Slice, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedSubSlices", type=trace_Slice, multiplicity=Multiplicity(0, 1))
    }
)
properties13: BinaryAssociation = BinaryAssociation(
    name="properties13",
    ends={
        Property(name="trace_Properties", type=trace_Slice, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Slice14", type=trace_Properties, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subSlices16: BinaryAssociation = BinaryAssociation(
    name="subSlices16",
    ends={
        Property(name="trace_Slice17", type=trace_Slice, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Slice15", type=trace_Slice, multiplicity=Multiplicity(0, 9999))
    }
)
events5: BinaryAssociation = BinaryAssociation(
    name="events5",
    ends={
        Property(name="trace_Event7", type=trace_Slice, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Slice6", type=trace_Event, multiplicity=Multiplicity(0, 9999))
    }
)
property18: BinaryAssociation = BinaryAssociation(
    name="property18",
    ends={
        Property(name="trace_EStructuralFeature", type=trace_ValueChangeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_ValueChangeEvent", type=trace_EStructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
object19: BinaryAssociation = BinaryAssociation(
    name="object19",
    ends={
        Property(name="trace_EObject", type=trace_ValueChangeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_ValueChangeEvent20", type=trace_EObject, multiplicity=Multiplicity(0, 1))
    }
)
value21: BinaryAssociation = BinaryAssociation(
    name="value21",
    ends={
        Property(name="trace_EObject22", type=trace_ObjectValueChangeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_ObjectValueChangeEvent", type=trace_EObject, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_trace_Event_EModelElement = Generalization(general=EModelElement, specific=trace_Event)
gen_trace_ResourceEvent_Event = Generalization(general=Event, specific=trace_ResourceEvent)
gen_trace_SchedulingEvent_Event = Generalization(general=Event, specific=trace_SchedulingEvent)
gen_trace_Trace_EModelElement = Generalization(general=EModelElement, specific=trace_Trace)
gen_trace_MessageEvent_Event = Generalization(general=Event, specific=trace_MessageEvent)
gen_trace_Slice_EModelElement = Generalization(general=EModelElement, specific=trace_Slice)
gen_trace_DurationValueChangeEvent_ValueChangeEvent = Generalization(general=ValueChangeEvent, specific=trace_DurationValueChangeEvent)
gen_trace_DataSizeValueChangeEvent_ValueChangeEvent = Generalization(general=ValueChangeEvent, specific=trace_DataSizeValueChangeEvent)
gen_trace_NumberValueChangeEvent_ValueChangeEvent = Generalization(general=ValueChangeEvent, specific=trace_NumberValueChangeEvent)
gen_trace_Properties_EModelElement = Generalization(general=EModelElement, specific=trace_Properties)
gen_trace_ValueChangeEvent_Event = Generalization(general=Event, specific=trace_ValueChangeEvent)
gen_trace_ObjectValueChangeEvent_ValueChangeEvent = Generalization(general=ValueChangeEvent, specific=trace_ObjectValueChangeEvent)

# Domain Model
domain_model = DomainModel(
    name="trace",
    types={trace_ResourceEvent, Event, trace_SchedulingEvent, trace_Trace, EModelElement, trace_Event, trace_Slice, trace_Properties, trace_MessageEvent, trace_DurationValueChangeEvent, trace_DataSizeValueChangeEvent, trace_NumberValueChangeEvent, trace_ValueChangeEvent, trace_EStructuralFeature, trace_EObject, trace_ObjectValueChangeEvent, ValueChangeEvent, SchedulingEventKind, ResourceEventKind, SliceKind, MessageEventKind},
    associations={trace2, about3, events0, slices1, ownedSubSlices9, parent11, properties13, subSlices16, events5, property18, object19, value21},
    generalizations={gen_trace_Event_EModelElement, gen_trace_ResourceEvent_Event, gen_trace_SchedulingEvent_Event, gen_trace_Trace_EModelElement, gen_trace_MessageEvent_Event, gen_trace_Slice_EModelElement, gen_trace_DurationValueChangeEvent_ValueChangeEvent, gen_trace_DataSizeValueChangeEvent_ValueChangeEvent, gen_trace_NumberValueChangeEvent_ValueChangeEvent, gen_trace_Properties_EModelElement, gen_trace_ValueChangeEvent_Event, gen_trace_ObjectValueChangeEvent_ValueChangeEvent},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)