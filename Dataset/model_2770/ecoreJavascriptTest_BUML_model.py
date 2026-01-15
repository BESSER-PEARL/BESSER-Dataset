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
ecoreJavascriptTest_C2 = Class(name="ecoreJavascriptTest::C2")
ecoreJavascriptTest_C1 = Class(name="ecoreJavascriptTest::C1")
ecoreJavascriptTest_C3 = Class(name="ecoreJavascriptTest::C3")
C2 = Class(name="C2")

# ecoreJavascriptTest_C2 class attributes and methods
ecoreJavascriptTest_C2_name: Property = Property(name="name", type=StringType)
ecoreJavascriptTest_C2_value: Property = Property(name="value", type=IntegerType)
ecoreJavascriptTest_C2.attributes={ecoreJavascriptTest_C2_name, ecoreJavascriptTest_C2_value}

# ecoreJavascriptTest_C1 class attributes and methods
ecoreJavascriptTest_C1_name: Property = Property(name="name", type=StringType)
ecoreJavascriptTest_C1.attributes={ecoreJavascriptTest_C1_name}

# ecoreJavascriptTest_C3 class attributes and methods

# C2 class attributes and methods

# Relationships
c2s0: BinaryAssociation = BinaryAssociation(
    name="c2s0",
    ends={
        Property(name="C2", type=ecoreJavascriptTest_C1, multiplicity=Multiplicity(1, 1)),
        Property(name="c1", type=ecoreJavascriptTest_C2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
c1s2: BinaryAssociation = BinaryAssociation(
    name="c1s2",
    ends={
        Property(name="ecoreJavascriptTest_C1", type=ecoreJavascriptTest_C1, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreJavascriptTest_C11", type=ecoreJavascriptTest_C1, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
c13: BinaryAssociation = BinaryAssociation(
    name="c13",
    ends={
        Property(name="C1", type=ecoreJavascriptTest_C2, multiplicity=Multiplicity(1, 1)),
        Property(name="c2s", type=ecoreJavascriptTest_C1, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_ecoreJavascriptTest_C3_C2 = Generalization(general=C2, specific=ecoreJavascriptTest_C3)

# Domain Model
domain_model = DomainModel(
    name="ecoreJavascriptTest",
    types={ecoreJavascriptTest_C2, ecoreJavascriptTest_C1, ecoreJavascriptTest_C3, C2},
    associations={c2s0, c1s2, c13},
    generalizations={gen_ecoreJavascriptTest_C3_C2},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)