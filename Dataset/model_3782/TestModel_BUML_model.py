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
test_Root = Class(name="test::Root")
test_TestPolicy = Class(name="test::TestPolicy")
test_TestElement = Class(name="test::TestElement")
test_TestClassDelegate = Class(name="test::TestClassDelegate")
test_NamedElement = Class(name="test::NamedElement")
test_TestElementWrapper = Class(name="test::TestElementWrapper")
NamedElement = Class(name="NamedElement")

# test_Root class attributes and methods
test_Root_ttt: Property = Property(name="ttt", type=StringType)
test_Root.attributes={test_Root_ttt}

# test_TestPolicy class attributes and methods

# test_TestElement class attributes and methods
test_TestElement_m_getRoot: Method = Method(name="getRoot", parameters={}, type=StringType)
test_TestElement.methods={test_TestElement_m_getRoot}

# test_TestClassDelegate class attributes and methods

# test_NamedElement class attributes and methods
test_NamedElement_Name: Property = Property(name="Name", type=StringType)
test_NamedElement.attributes={test_NamedElement_Name}

# test_TestElementWrapper class attributes and methods

# NamedElement class attributes and methods

# Relationships
policies1: BinaryAssociation = BinaryAssociation(
    name="policies1",
    ends={
        Property(name="test_TestPolicy", type=test_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="test_TestElement2", type=test_TestPolicy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
testClassDelegate3: BinaryAssociation = BinaryAssociation(
    name="testClassDelegate3",
    ends={
        Property(name="test_TestClassDelegate", type=test_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="test_TestElement4", type=test_TestClassDelegate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
element5: BinaryAssociation = BinaryAssociation(
    name="element5",
    ends={
        Property(name="test_TestElement6", type=test_TestElementWrapper, multiplicity=Multiplicity(1, 1)),
        Property(name="test_TestElementWrapper", type=test_TestElement, multiplicity=Multiplicity(0, 1))
    }
)
children0: BinaryAssociation = BinaryAssociation(
    name="children0",
    ends={
        Property(name="test_TestElement", type=test_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="test_Root", type=test_TestElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_test_TestPolicy_NamedElement = Generalization(general=NamedElement, specific=test_TestPolicy)
gen_test_TestElementWrapper_NamedElement = Generalization(general=NamedElement, specific=test_TestElementWrapper)
gen_test_TestClassDelegate_NamedElement = Generalization(general=NamedElement, specific=test_TestClassDelegate)
gen_test_TestElement_NamedElement = Generalization(general=NamedElement, specific=test_TestElement)

# Domain Model
domain_model = DomainModel(
    name="test",
    types={test_Root, test_TestPolicy, test_TestElement, test_TestClassDelegate, test_NamedElement, test_TestElementWrapper, NamedElement},
    associations={policies1, testClassDelegate3, element5, children0},
    generalizations={gen_test_TestPolicy_NamedElement, gen_test_TestElementWrapper_NamedElement, gen_test_TestClassDelegate_NamedElement, gen_test_TestElement_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)