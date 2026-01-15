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
LazyRuleInheritanceTest_ClassA = Class(name="LazyRuleInheritanceTest::ClassA")
LazyRuleInheritanceTest_subpackage_ClassB = Class(name="LazyRuleInheritanceTest::subpackage::ClassB", is_abstract=True)

# LazyRuleInheritanceTest_ClassA class attributes and methods

# LazyRuleInheritanceTest_subpackage_ClassB class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="LazyRuleInheritanceTest",
    types={LazyRuleInheritanceTest_ClassA, LazyRuleInheritanceTest_subpackage_ClassB},
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