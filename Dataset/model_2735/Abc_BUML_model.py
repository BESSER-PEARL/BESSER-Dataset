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
Abc_A = Class(name="Abc::A")
Abc_classB = Class(name="Abc::classB")
Abc_C = Class(name="Abc::C")

# Abc_A class attributes and methods

# Abc_classB class attributes and methods

# Abc_C class attributes and methods

# Relationships
AtoB0: BinaryAssociation = BinaryAssociation(
    name="AtoB0",
    ends={
        Property(name="Abc_classB", type=Abc_A, multiplicity=Multiplicity(1, 1)),
        Property(name="Abc_A", type=Abc_classB, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
AtoC1: BinaryAssociation = BinaryAssociation(
    name="AtoC1",
    ends={
        Property(name="Abc_C", type=Abc_A, multiplicity=Multiplicity(1, 1)),
        Property(name="Abc_A2", type=Abc_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
CtoB3: BinaryAssociation = BinaryAssociation(
    name="CtoB3",
    ends={
        Property(name="Abc_classB5", type=Abc_C, multiplicity=Multiplicity(1, 1)),
        Property(name="Abc_C4", type=Abc_classB, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="Abc",
    types={Abc_A, Abc_classB, Abc_C},
    associations={AtoB0, AtoC1, CtoB3},
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