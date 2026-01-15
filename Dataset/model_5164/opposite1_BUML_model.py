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
opposite1_Root = Class(name="opposite1::Root")
opposite1_AbstractSuperClass = Class(name="opposite1::AbstractSuperClass", is_abstract=True)
opposite1_ClassA = Class(name="opposite1::ClassA")
AbstractSuperClass = Class(name="AbstractSuperClass")
opposite1_ClassB = Class(name="opposite1::ClassB")

# opposite1_Root class attributes and methods

# opposite1_AbstractSuperClass class attributes and methods

# opposite1_ClassA class attributes and methods

# AbstractSuperClass class attributes and methods

# opposite1_ClassB class attributes and methods

# Relationships
classes0: BinaryAssociation = BinaryAssociation(
    name="classes0",
    ends={
        Property(name="opposite1_AbstractSuperClass", type=opposite1_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="opposite1_Root", type=opposite1_AbstractSuperClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
b1: BinaryAssociation = BinaryAssociation(
    name="b1",
    ends={
        Property(name="ClassB", type=opposite1_ClassA, multiplicity=Multiplicity(1, 1)),
        Property(name="a", type=opposite1_ClassB, multiplicity=Multiplicity(1, 1))
    }
)
a2: BinaryAssociation = BinaryAssociation(
    name="a2",
    ends={
        Property(name="ClassA", type=opposite1_ClassB, multiplicity=Multiplicity(1, 1)),
        Property(name="b", type=opposite1_ClassA, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_opposite1_ClassA_AbstractSuperClass = Generalization(general=AbstractSuperClass, specific=opposite1_ClassA)
gen_opposite1_ClassB_AbstractSuperClass = Generalization(general=AbstractSuperClass, specific=opposite1_ClassB)

# Domain Model
domain_model = DomainModel(
    name="opposite1",
    types={opposite1_Root, opposite1_AbstractSuperClass, opposite1_ClassA, AbstractSuperClass, opposite1_ClassB},
    associations={classes0, b1, a2},
    generalizations={gen_opposite1_ClassA_AbstractSuperClass, gen_opposite1_ClassB_AbstractSuperClass},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)