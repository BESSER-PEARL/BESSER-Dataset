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
ClassA = Class(name="ClassA")
ClassB = Class(name="ClassB")
ClassC = Class(name="ClassC")

# ClassA class attributes and methods
ClassA_attA: Property = Property(name="attA", type=StringType)
ClassA.attributes={ClassA_attA}

# ClassB class attributes and methods
ClassB_attribute: Property = Property(name="attribute", type=IntegerType)
ClassB.attributes={ClassB_attribute}

# ClassC class attributes and methods
ClassC_attC1: Property = Property(name="attC1", type=IntegerType)
ClassC_attC2: Property = Property(name="attC2", type=BooleanType)
ClassC.attributes={ClassC_attC1, ClassC_attC2}

# Relationships
ClassA_ClassB: BinaryAssociation = BinaryAssociation(
    name="ClassA_ClassB",
    ends={
        Property(name="classB0", type=ClassB, multiplicity=Multiplicity(1, 9999)),
        Property(name="classA1", type=ClassA, multiplicity=Multiplicity(0, 1))
    }
)
ClassB_ClassC: BinaryAssociation = BinaryAssociation(
    name="ClassB_ClassC",
    ends={
        Property(name="classC2", type=ClassC, multiplicity=Multiplicity(0, 9999)),
        Property(name="classB3", type=ClassB, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_UWkIYO1zEei9dNtZPq67hQ",
    types={ClassA, ClassB, ClassC},
    associations={ClassA_ClassB, ClassB_ClassC},
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