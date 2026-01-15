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
functioncall_ConceptB = Class(name="functioncall::ConceptB")
ConceptA = Class(name="ConceptA")
functioncall_ConceptC = Class(name="functioncall::ConceptC")
functioncall_ConceptA = Class(name="functioncall::ConceptA")

# functioncall_ConceptB class attributes and methods

# ConceptA class attributes and methods

# functioncall_ConceptC class attributes and methods

# functioncall_ConceptA class attributes and methods

# Relationships
concepta20: BinaryAssociation = BinaryAssociation(
    name="concepta20",
    ends={
        Property(name="functioncall_ConceptA", type=functioncall_ConceptC, multiplicity=Multiplicity(1, 1)),
        Property(name="functioncall_ConceptC", type=functioncall_ConceptA, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
concepta11: BinaryAssociation = BinaryAssociation(
    name="concepta11",
    ends={
        Property(name="functioncall_ConceptA3", type=functioncall_ConceptC, multiplicity=Multiplicity(1, 1)),
        Property(name="functioncall_ConceptC2", type=functioncall_ConceptA, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
conceptb4: BinaryAssociation = BinaryAssociation(
    name="conceptb4",
    ends={
        Property(name="functioncall_ConceptB", type=functioncall_ConceptC, multiplicity=Multiplicity(1, 1)),
        Property(name="functioncall_ConceptC5", type=functioncall_ConceptB, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_functioncall_ConceptB_ConceptA = Generalization(general=ConceptA, specific=functioncall_ConceptB)

# Domain Model
domain_model = DomainModel(
    name="functioncall",
    types={functioncall_ConceptB, ConceptA, functioncall_ConceptC, functioncall_ConceptA},
    associations={concepta20, concepta11, conceptb4},
    generalizations={gen_functioncall_ConceptB_ConceptA},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)