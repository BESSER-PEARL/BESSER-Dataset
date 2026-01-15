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
GateType: Enumeration = Enumeration(
    name="GateType",
    literals={
            EnumerationLiteral(name="ORGate"),
			EnumerationLiteral(name="ANDGate")
    }
)

# Classes
fta_FTA = Class(name="fta::FTA")
fta_Diagram = Class(name="fta::Diagram", is_abstract=True)
fta_Hazard = Class(name="fta::Hazard")
Diagram = Class(name="Diagram")
fta_Condition = Class(name="fta::Condition")
fta_Event = Class(name="fta::Event")

# fta_FTA class attributes and methods

# fta_Diagram class attributes and methods
fta_Diagram_name: Property = Property(name="name", type=StringType)
fta_Diagram_detail: Property = Property(name="detail", type=StringType)
fta_Diagram_id: Property = Property(name="id", type=StringType)
fta_Diagram.attributes={fta_Diagram_name, fta_Diagram_id, fta_Diagram_detail}

# fta_Hazard class attributes and methods

# Diagram class attributes and methods

# fta_Condition class attributes and methods
fta_Condition_GateKind: Property = Property(name="GateKind", type=StringType)
fta_Condition.attributes={fta_Condition_GateKind}

# fta_Event class attributes and methods
fta_Event_BaseEvent: Property = Property(name="BaseEvent", type=BooleanType)
fta_Event.attributes={fta_Event_BaseEvent}

# Relationships
diagrams0: BinaryAssociation = BinaryAssociation(
    name="diagrams0",
    ends={
        Property(name="fta_Diagram", type=fta_FTA, multiplicity=Multiplicity(1, 1)),
        Property(name="fta_FTA", type=fta_Diagram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conditions1: BinaryAssociation = BinaryAssociation(
    name="conditions1",
    ends={
        Property(name="fta_Condition", type=fta_Hazard, multiplicity=Multiplicity(1, 1)),
        Property(name="fta_Hazard", type=fta_Condition, multiplicity=Multiplicity(0, 9999))
    }
)
condition2: BinaryAssociation = BinaryAssociation(
    name="condition2",
    ends={
        Property(name="fta_Condition3", type=fta_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="fta_Event", type=fta_Condition, multiplicity=Multiplicity(0, 1))
    }
)
events4: BinaryAssociation = BinaryAssociation(
    name="events4",
    ends={
        Property(name="fta_Event6", type=fta_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="fta_Condition5", type=fta_Event, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_fta_Hazard_Diagram = Generalization(general=Diagram, specific=fta_Hazard)
gen_fta_Event_Diagram = Generalization(general=Diagram, specific=fta_Event)
gen_fta_Condition_Diagram = Generalization(general=Diagram, specific=fta_Condition)

# Domain Model
domain_model = DomainModel(
    name="fta",
    types={fta_FTA, fta_Diagram, fta_Hazard, Diagram, fta_Condition, fta_Event, GateType},
    associations={diagrams0, conditions1, condition2, events4},
    generalizations={gen_fta_Hazard_Diagram, gen_fta_Event_Diagram, gen_fta_Condition_Diagram},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)