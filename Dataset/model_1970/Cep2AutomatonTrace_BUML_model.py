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
trace_TraceModel = Class(name="trace::TraceModel")
trace_Trace = Class(name="trace::Trace")
trace_TimedZoneTrace = Class(name="trace::TimedZoneTrace")
trace_EventPattern = Class(name="trace::EventPattern")
trace_Automaton = Class(name="trace::Automaton")
trace_TimedZone = Class(name="trace::TimedZone")
trace_Transition = Class(name="trace::Transition")

# trace_TraceModel class attributes and methods

# trace_Trace class attributes and methods

# trace_TimedZoneTrace class attributes and methods

# trace_EventPattern class attributes and methods

# trace_Automaton class attributes and methods

# trace_TimedZone class attributes and methods

# trace_Transition class attributes and methods

# Relationships
traces0: BinaryAssociation = BinaryAssociation(
    name="traces0",
    ends={
        Property(name="trace_Trace", type=trace_TraceModel, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_TraceModel", type=trace_Trace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timedZoneTraces1: BinaryAssociation = BinaryAssociation(
    name="timedZoneTraces1",
    ends={
        Property(name="trace_TimedZoneTrace", type=trace_TraceModel, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_TraceModel2", type=trace_TimedZoneTrace, multiplicity=Multiplicity(0, 9999))
    }
)
eventPattern3: BinaryAssociation = BinaryAssociation(
    name="eventPattern3",
    ends={
        Property(name="trace_EventPattern", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace4", type=trace_EventPattern, multiplicity=Multiplicity(1, 1))
    }
)
automaton5: BinaryAssociation = BinaryAssociation(
    name="automaton5",
    ends={
        Property(name="trace_Automaton", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace6", type=trace_Automaton, multiplicity=Multiplicity(1, 1))
    }
)
timedZone7: BinaryAssociation = BinaryAssociation(
    name="timedZone7",
    ends={
        Property(name="trace_TimedZone", type=trace_TimedZoneTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_TimedZoneTrace8", type=trace_TimedZone, multiplicity=Multiplicity(1, 1))
    }
)
transition9: BinaryAssociation = BinaryAssociation(
    name="transition9",
    ends={
        Property(name="trace_Transition", type=trace_TimedZoneTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_TimedZoneTrace10", type=trace_Transition, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="trace",
    types={trace_TraceModel, trace_Trace, trace_TimedZoneTrace, trace_EventPattern, trace_Automaton, trace_TimedZone, trace_Transition},
    associations={traces0, timedZoneTraces1, eventPattern3, automaton5, timedZone7, transition9},
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