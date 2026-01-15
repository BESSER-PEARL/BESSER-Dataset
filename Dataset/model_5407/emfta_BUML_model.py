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
EventType: Enumeration = Enumeration(
    name="EventType",
    literals={
            EnumerationLiteral(name="Basic"),
			EnumerationLiteral(name="External"),
			EnumerationLiteral(name="Undevelopped"),
			EnumerationLiteral(name="Conditioning"),
			EnumerationLiteral(name="Intermediate")
    }
)

GateType: Enumeration = Enumeration(
    name="GateType",
    literals={
            EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="XOR"),
			EnumerationLiteral(name="PRIORITY_AND"),
			EnumerationLiteral(name="INHIBIT"),
			EnumerationLiteral(name="PRIORITY_OR"),
			EnumerationLiteral(name="INTERMEDIATE"),
			EnumerationLiteral(name="ORMORE"),
			EnumerationLiteral(name="ORLESS")
    }
)

# Classes
emfta_Event = Class(name="emfta::Event")
emfta_Gate = Class(name="emfta::Gate")
emfta_FTAModel = Class(name="emfta::FTAModel")

# emfta_Event class attributes and methods
emfta_Event_probability: Property = Property(name="probability", type=FloatType)
emfta_Event_type: Property = Property(name="type", type=StringType)
emfta_Event_name: Property = Property(name="name", type=StringType)
emfta_Event_description: Property = Property(name="description", type=StringType)
emfta_Event_relatedObject: Property = Property(name="relatedObject", type=StringType)
emfta_Event_referenceCount: Property = Property(name="referenceCount", type=IntegerType)
emfta_Event.attributes={emfta_Event_description, emfta_Event_name, emfta_Event_referenceCount, emfta_Event_type, emfta_Event_relatedObject, emfta_Event_probability}

# emfta_Gate class attributes and methods
emfta_Gate_type: Property = Property(name="type", type=StringType)
emfta_Gate_description: Property = Property(name="description", type=StringType)
emfta_Gate_nbOccurrences: Property = Property(name="nbOccurrences", type=IntegerType)
emfta_Gate.attributes={emfta_Gate_description, emfta_Gate_type, emfta_Gate_nbOccurrences}

# emfta_FTAModel class attributes and methods
emfta_FTAModel_name: Property = Property(name="name", type=StringType)
emfta_FTAModel_description: Property = Property(name="description", type=StringType)
emfta_FTAModel_comments: Property = Property(name="comments", type=StringType)
emfta_FTAModel.attributes={emfta_FTAModel_name, emfta_FTAModel_comments, emfta_FTAModel_description}

# Relationships
gate0: BinaryAssociation = BinaryAssociation(
    name="gate0",
    ends={
        Property(name="emfta_Gate", type=emfta_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="emfta_Event", type=emfta_Gate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
events1: BinaryAssociation = BinaryAssociation(
    name="events1",
    ends={
        Property(name="emfta_Event3", type=emfta_Gate, multiplicity=Multiplicity(1, 1)),
        Property(name="emfta_Gate2", type=emfta_Event, multiplicity=Multiplicity(0, 9999))
    }
)
root4: BinaryAssociation = BinaryAssociation(
    name="root4",
    ends={
        Property(name="emfta_Event5", type=emfta_FTAModel, multiplicity=Multiplicity(1, 1)),
        Property(name="emfta_FTAModel", type=emfta_Event, multiplicity=Multiplicity(0, 1))
    }
)
events6: BinaryAssociation = BinaryAssociation(
    name="events6",
    ends={
        Property(name="emfta_Event8", type=emfta_FTAModel, multiplicity=Multiplicity(1, 1)),
        Property(name="emfta_FTAModel7", type=emfta_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="emfta",
    types={emfta_Event, emfta_Gate, emfta_FTAModel, EventType, GateType},
    associations={gate0, events1, root4, events6},
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