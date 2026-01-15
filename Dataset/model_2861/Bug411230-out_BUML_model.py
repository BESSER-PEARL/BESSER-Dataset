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
TestEnum: Enumeration = Enumeration(
    name="TestEnum",
    literals={
            EnumerationLiteral(name="testLiteral"),
			EnumerationLiteral(name="testLiteral2")
    }
)

# Classes
My_TestClass = Class(name="My::TestClass")
My_c1 = Class(name="My::c1")

# My_TestClass class attributes and methods
My_TestClass_testAtt: Property = Property(name="testAtt", type=StringType)
My_TestClass_testAtt2: Property = Property(name="testAtt2", type=StringType)
My_TestClass.attributes={My_TestClass_testAtt2, My_TestClass_testAtt}

# My_c1 class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="My",
    types={My_TestClass, My_c1, TestEnum},
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