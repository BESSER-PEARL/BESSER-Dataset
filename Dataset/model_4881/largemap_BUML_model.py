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
largemapvalue_TestElement = Class(name="largemapvalue::TestElement")
largemapvalue_StringToStringMap = Class(name="largemapvalue::StringToStringMap")

# largemapvalue_TestElement class attributes and methods
largemapvalue_TestElement_testProp: Property = Property(name="testProp", type=StringType)
largemapvalue_TestElement.attributes={largemapvalue_TestElement_testProp}

# largemapvalue_StringToStringMap class attributes and methods
largemapvalue_StringToStringMap_key: Property = Property(name="key", type=StringType)
largemapvalue_StringToStringMap_value: Property = Property(name="value", type=StringType)
largemapvalue_StringToStringMap.attributes={largemapvalue_StringToStringMap_value, largemapvalue_StringToStringMap_key}

# Relationships
testMap0: BinaryAssociation = BinaryAssociation(
    name="testMap0",
    ends={
        Property(name="largemapvalue_StringToStringMap", type=largemapvalue_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="largemapvalue_TestElement", type=largemapvalue_StringToStringMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="largemapvalue",
    types={largemapvalue_TestElement, largemapvalue_StringToStringMap},
    associations={testMap0},
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