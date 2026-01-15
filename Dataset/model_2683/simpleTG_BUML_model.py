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
simpleTG_Container = Class(name="simpleTG::Container")
simpleTG_A = Class(name="simpleTG::A")
simpleTG_B = Class(name="simpleTG::B")
simpleTG_C = Class(name="simpleTG::C")

# simpleTG_Container class attributes and methods

# simpleTG_A class attributes and methods

# simpleTG_B class attributes and methods

# simpleTG_C class attributes and methods

# Relationships
as0: BinaryAssociation = BinaryAssociation(
    name="as0",
    ends={
        Property(name="simpleTG_A", type=simpleTG_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleTG_Container", type=simpleTG_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bs1: BinaryAssociation = BinaryAssociation(
    name="bs1",
    ends={
        Property(name="simpleTG_B", type=simpleTG_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleTG_Container2", type=simpleTG_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cs3: BinaryAssociation = BinaryAssociation(
    name="cs3",
    ends={
        Property(name="simpleTG_C", type=simpleTG_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleTG_Container4", type=simpleTG_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
b5: BinaryAssociation = BinaryAssociation(
    name="b5",
    ends={
        Property(name="simpleTG_B7", type=simpleTG_A, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleTG_A6", type=simpleTG_B, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="simpleTG",
    types={simpleTG_Container, simpleTG_A, simpleTG_B, simpleTG_C},
    associations={as0, bs1, cs3, b5},
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