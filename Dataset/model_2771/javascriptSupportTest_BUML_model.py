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
javascriptSupportTest_C1 = Class(name="javascriptSupportTest::C1")
javascriptSupportTest_C2 = Class(name="javascriptSupportTest::C2")
javascriptSupportTest_C3 = Class(name="javascriptSupportTest::C3")
C2 = Class(name="C2")

# javascriptSupportTest_C1 class attributes and methods
javascriptSupportTest_C1_string1: Property = Property(name="string1", type=StringType)
javascriptSupportTest_C1_int1: Property = Property(name="int1", type=IntegerType)
javascriptSupportTest_C1_name: Property = Property(name="name", type=StringType)
javascriptSupportTest_C1_m_getPrefixedName: Method = Method(name="getPrefixedName", parameters={Parameter(name='prefix')})
javascriptSupportTest_C1_m_createC2: Method = Method(name="createC2", parameters={Parameter(name='name')})
javascriptSupportTest_C1.attributes={javascriptSupportTest_C1_string1, javascriptSupportTest_C1_int1, javascriptSupportTest_C1_name}
javascriptSupportTest_C1.methods={javascriptSupportTest_C1_m_getPrefixedName, javascriptSupportTest_C1_m_createC2}

# javascriptSupportTest_C2 class attributes and methods
javascriptSupportTest_C2_name: Property = Property(name="name", type=StringType)
javascriptSupportTest_C2_string1: Property = Property(name="string1", type=StringType)
javascriptSupportTest_C2_int1: Property = Property(name="int1", type=IntegerType)
javascriptSupportTest_C2_m_getSuffixedName: Method = Method(name="getSuffixedName", parameters={Parameter(name='suffix')})
javascriptSupportTest_C2.attributes={javascriptSupportTest_C2_int1, javascriptSupportTest_C2_name, javascriptSupportTest_C2_string1}
javascriptSupportTest_C2.methods={javascriptSupportTest_C2_m_getSuffixedName}

# javascriptSupportTest_C3 class attributes and methods
javascriptSupportTest_C3_title: Property = Property(name="title", type=StringType)
javascriptSupportTest_C3.attributes={javascriptSupportTest_C3_title}

# C2 class attributes and methods

# Relationships
c2s0: BinaryAssociation = BinaryAssociation(
    name="c2s0",
    ends={
        Property(name="C2", type=javascriptSupportTest_C1, multiplicity=Multiplicity(1, 1)),
        Property(name="c1", type=javascriptSupportTest_C2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
c11: BinaryAssociation = BinaryAssociation(
    name="c11",
    ends={
        Property(name="C1", type=javascriptSupportTest_C2, multiplicity=Multiplicity(1, 1)),
        Property(name="c2s", type=javascriptSupportTest_C1, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_javascriptSupportTest_C3_C2 = Generalization(general=C2, specific=javascriptSupportTest_C3)

# Domain Model
domain_model = DomainModel(
    name="javascriptSupportTest",
    types={javascriptSupportTest_C1, javascriptSupportTest_C2, javascriptSupportTest_C3, C2},
    associations={c2s0, c11},
    generalizations={gen_javascriptSupportTest_C3_C2},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)