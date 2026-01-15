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
autocast_ConceptA = Class(name="autocast::ConceptA")
autocast_ConceptB = Class(name="autocast::ConceptB")
ConceptA = Class(name="ConceptA")
autocast_ConceptC = Class(name="autocast::ConceptC")

# autocast_ConceptA class attributes and methods

# autocast_ConceptB class attributes and methods
autocast_ConceptB_name: Property = Property(name="name", type=StringType)
autocast_ConceptB.attributes={autocast_ConceptB_name}

# ConceptA class attributes and methods

# autocast_ConceptC class attributes and methods

# Relationships
ax0: BinaryAssociation = BinaryAssociation(
    name="ax0",
    ends={
        Property(name="autocast_ConceptA", type=autocast_ConceptC, multiplicity=Multiplicity(1, 1)),
        Property(name="autocast_ConceptC", type=autocast_ConceptA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_autocast_ConceptB_ConceptA = Generalization(general=ConceptA, specific=autocast_ConceptB)

# Domain Model
domain_model = DomainModel(
    name="autocast",
    types={autocast_ConceptA, autocast_ConceptB, ConceptA, autocast_ConceptC},
    associations={ax0},
    generalizations={gen_autocast_ConceptB_ConceptA},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)