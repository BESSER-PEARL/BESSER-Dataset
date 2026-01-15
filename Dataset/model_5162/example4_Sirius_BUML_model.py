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
example4_Sirius_A = Class(name="example4::Sirius::A")
example4_Sirius_B = Class(name="example4::Sirius::B")
example4_Sirius_Container = Class(name="example4::Sirius::Container")
example4_Sirius_Element = Class(name="example4::Sirius::Element")

# example4_Sirius_A class attributes and methods

# example4_Sirius_B class attributes and methods

# example4_Sirius_Container class attributes and methods

# example4_Sirius_Element class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="example4_Sirius_Container", type=example4_Sirius_Element, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="example4_Sirius_Element", type=example4_Sirius_Container, multiplicity=Multiplicity(1, 1))
    }
)
a1: BinaryAssociation = BinaryAssociation(
    name="a1",
    ends={
        Property(name="example4_Sirius_A", type=example4_Sirius_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="example4_Sirius_Element2", type=example4_Sirius_A, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
b3: BinaryAssociation = BinaryAssociation(
    name="b3",
    ends={
        Property(name="example4_Sirius_B", type=example4_Sirius_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="example4_Sirius_Element4", type=example4_Sirius_B, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="example4_Sirius",
    types={example4_Sirius_A, example4_Sirius_B, example4_Sirius_Container, example4_Sirius_Element},
    associations={elements0, a1, b3},
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