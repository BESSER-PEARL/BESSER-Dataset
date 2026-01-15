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
events_Automaton = Class(name="events::Automaton")
events_AtomicEventPattern = Class(name="events::AtomicEventPattern")
EventPattern = Class(name="EventPattern")
events_EventModel = Class(name="events::EventModel")
events_EventPattern = Class(name="events::EventPattern", is_abstract=True)
events_ComplexEventPattern = Class(name="events::ComplexEventPattern")
events_ComplexEventOperator = Class(name="events::ComplexEventOperator", is_abstract=True)
events_Timewindow = Class(name="events::Timewindow")
events_EventPatternReference = Class(name="events::EventPatternReference")
events_AbstractMultiplicity = Class(name="events::AbstractMultiplicity", is_abstract=True)
events_Event = Class(name="events::Event")
events_EventSource = Class(name="events::EventSource", is_abstract=True)
events_OR = Class(name="events::OR")
ComplexEventOperator = Class(name="ComplexEventOperator")
events_NEG = Class(name="events::NEG")
events_FOLLOWS = Class(name="events::FOLLOWS")
events_AND = Class(name="events::AND")
events_Multiplicity = Class(name="events::Multiplicity")
AbstractMultiplicity = Class(name="AbstractMultiplicity")
events_Infinite = Class(name="events::Infinite")
events_AtLeastOne = Class(name="events::AtLeastOne")

# events_Automaton class attributes and methods

# events_AtomicEventPattern class attributes and methods
events_AtomicEventPattern_type: Property = Property(name="type", type=StringType)
events_AtomicEventPattern.attributes={events_AtomicEventPattern_type}

# EventPattern class attributes and methods

# events_EventModel class attributes and methods

# events_EventPattern class attributes and methods
events_EventPattern_id: Property = Property(name="id", type=StringType)
events_EventPattern.attributes={events_EventPattern_id}

# events_ComplexEventPattern class attributes and methods

# events_ComplexEventOperator class attributes and methods

# events_Timewindow class attributes and methods
events_Timewindow_time: Property = Property(name="time", type=StringType)
events_Timewindow.attributes={events_Timewindow_time}

# events_EventPatternReference class attributes and methods
events_EventPatternReference_parameterSymbolicNames: Property = Property(name="parameterSymbolicNames", type=StringType)
events_EventPatternReference.attributes={events_EventPatternReference_parameterSymbolicNames}

# events_AbstractMultiplicity class attributes and methods

# events_Event class attributes and methods
events_Event_type: Property = Property(name="type", type=StringType)
events_Event_timestamp: Property = Property(name="timestamp", type=StringType)
events_Event_isProcessed: Property = Property(name="isProcessed", type=BooleanType)
events_Event.attributes={events_Event_timestamp, events_Event_type, events_Event_isProcessed}

# events_EventSource class attributes and methods
events_EventSource_m_getId: Method = Method(name="getId", parameters={}, type=StringType)
events_EventSource.methods={events_EventSource_m_getId}

# events_OR class attributes and methods

# ComplexEventOperator class attributes and methods

# events_NEG class attributes and methods

# events_FOLLOWS class attributes and methods

# events_AND class attributes and methods

# events_Multiplicity class attributes and methods
events_Multiplicity_value: Property = Property(name="value", type=IntegerType)
events_Multiplicity.attributes={events_Multiplicity_value}

# AbstractMultiplicity class attributes and methods

# events_Infinite class attributes and methods

# events_AtLeastOne class attributes and methods

# Relationships
automaton2: BinaryAssociation = BinaryAssociation(
    name="automaton2",
    ends={
        Property(name="events_Automaton", type=events_EventPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="events_EventPattern", type=events_Automaton, multiplicity=Multiplicity(0, 1))
    }
)
eventPatterns0: BinaryAssociation = BinaryAssociation(
    name="eventPatterns0",
    ends={
        Property(name="EventPattern", type=events_EventModel, multiplicity=Multiplicity(1, 1)),
        Property(name="eventModel", type=events_EventPattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventModel1: BinaryAssociation = BinaryAssociation(
    name="eventModel1",
    ends={
        Property(name="EventModel", type=events_EventPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="eventPatterns", type=events_EventModel, multiplicity=Multiplicity(0, 1))
    }
)
operator3: BinaryAssociation = BinaryAssociation(
    name="operator3",
    ends={
        Property(name="events_ComplexEventOperator", type=events_ComplexEventPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="events_ComplexEventPattern", type=events_ComplexEventOperator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
timewindow4: BinaryAssociation = BinaryAssociation(
    name="timewindow4",
    ends={
        Property(name="events_Timewindow", type=events_ComplexEventPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="events_ComplexEventPattern5", type=events_Timewindow, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containedEventPatterns6: BinaryAssociation = BinaryAssociation(
    name="containedEventPatterns6",
    ends={
        Property(name="events_EventPatternReference", type=events_ComplexEventPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="events_ComplexEventPattern7", type=events_EventPatternReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventPattern8: BinaryAssociation = BinaryAssociation(
    name="eventPattern8",
    ends={
        Property(name="events_EventPattern10", type=events_EventPatternReference, multiplicity=Multiplicity(1, 1)),
        Property(name="events_EventPatternReference9", type=events_EventPattern, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
multiplicity11: BinaryAssociation = BinaryAssociation(
    name="multiplicity11",
    ends={
        Property(name="events_AbstractMultiplicity", type=events_EventPatternReference, multiplicity=Multiplicity(1, 1)),
        Property(name="events_EventPatternReference12", type=events_AbstractMultiplicity, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source13: BinaryAssociation = BinaryAssociation(
    name="source13",
    ends={
        Property(name="events_EventSource", type=events_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="events_Event", type=events_EventSource, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_events_AtomicEventPattern_EventPattern = Generalization(general=EventPattern, specific=events_AtomicEventPattern)
gen_events_ComplexEventPattern_EventPattern = Generalization(general=EventPattern, specific=events_ComplexEventPattern)
gen_events_OR_ComplexEventOperator = Generalization(general=ComplexEventOperator, specific=events_OR)
gen_events_NEG_ComplexEventOperator = Generalization(general=ComplexEventOperator, specific=events_NEG)
gen_events_FOLLOWS_ComplexEventOperator = Generalization(general=ComplexEventOperator, specific=events_FOLLOWS)
gen_events_AND_ComplexEventOperator = Generalization(general=ComplexEventOperator, specific=events_AND)
gen_events_Multiplicity_AbstractMultiplicity = Generalization(general=AbstractMultiplicity, specific=events_Multiplicity)
gen_events_Infinite_AbstractMultiplicity = Generalization(general=AbstractMultiplicity, specific=events_Infinite)
gen_events_AtLeastOne_AbstractMultiplicity = Generalization(general=AbstractMultiplicity, specific=events_AtLeastOne)

# Domain Model
domain_model = DomainModel(
    name="events",
    types={events_Automaton, events_AtomicEventPattern, EventPattern, events_EventModel, events_EventPattern, events_ComplexEventPattern, events_ComplexEventOperator, events_Timewindow, events_EventPatternReference, events_AbstractMultiplicity, events_Event, events_EventSource, events_OR, ComplexEventOperator, events_NEG, events_FOLLOWS, events_AND, events_Multiplicity, AbstractMultiplicity, events_Infinite, events_AtLeastOne},
    associations={automaton2, eventPatterns0, eventModel1, operator3, timewindow4, containedEventPatterns6, eventPattern8, multiplicity11, source13},
    generalizations={gen_events_AtomicEventPattern_EventPattern, gen_events_ComplexEventPattern_EventPattern, gen_events_OR_ComplexEventOperator, gen_events_NEG_ComplexEventOperator, gen_events_FOLLOWS_ComplexEventOperator, gen_events_AND_ComplexEventOperator, gen_events_Multiplicity_AbstractMultiplicity, gen_events_Infinite_AbstractMultiplicity, gen_events_AtLeastOne_AbstractMultiplicity},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)