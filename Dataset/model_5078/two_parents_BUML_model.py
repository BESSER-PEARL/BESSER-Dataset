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
test_Input = Class(name="test::Input")
test_Output = Class(name="test::Output")

# test_Input class attributes and methods
test_Input_test: Property = Property(name="test", type=StringType)
test_Input_key: Property = Property(name="key", type=StringType)
test_Input.attributes={test_Input_key, test_Input_test}

# test_Output class attributes and methods
test_Output_key: Property = Property(name="key", type=StringType)
test_Output_m_test: Method = Method(name="test", parameters={}, type=StringType)
test_Output.attributes={test_Output_key}
test_Output.methods={test_Output_m_test}

# Domain Model
domain_model = DomainModel(
    name="test",
    types={test_Input, test_Output},
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