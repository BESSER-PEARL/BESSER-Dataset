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
TestEnum2: Enumeration = Enumeration(
    name="TestEnum2",
    literals={
            EnumerationLiteral(name="testLiteral"),
			EnumerationLiteral(name="testLiteral2")
    }
)

# Classes
My2_TestClass2 = Class(name="My2::TestClass2")

# My2_TestClass2 class attributes and methods
My2_TestClass2_testAtt: Property = Property(name="testAtt", type=StringType)
My2_TestClass2_testAtt2: Property = Property(name="testAtt2", type=StringType)
My2_TestClass2.attributes={My2_TestClass2_testAtt, My2_TestClass2_testAtt2}

# Domain Model
domain_model = DomainModel(
    name="My2",
    types={My2_TestClass2, TestEnum2},
    associations={},
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