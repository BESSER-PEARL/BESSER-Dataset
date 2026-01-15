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
testpackage_User = Class(name="testpackage::User")
NamedElement = Class(name="NamedElement")
testpackage_Group = Class(name="testpackage::Group")
testpackage_NamedElement = Class(name="testpackage::NamedElement", is_abstract=True)

# testpackage_User class attributes and methods
testpackage_User_password: Property = Property(name="password", type=StringType)
testpackage_User.attributes={testpackage_User_password}

# NamedElement class attributes and methods

# testpackage_Group class attributes and methods
testpackage_Group_m_isMember: Method = Method(name="isMember", parameters={Parameter(name='user')}, type=BooleanType)
testpackage_Group.methods={testpackage_Group_m_isMember}

# testpackage_NamedElement class attributes and methods
testpackage_NamedElement_name: Property = Property(name="name", type=StringType)
testpackage_NamedElement.attributes={testpackage_NamedElement_name}

# Relationships
members0: BinaryAssociation = BinaryAssociation(
    name="members0",
    ends={
        Property(name="testpackage_User", type=testpackage_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="testpackage_Group", type=testpackage_User, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_testpackage_User_NamedElement = Generalization(general=NamedElement, specific=testpackage_User)
gen_testpackage_Group_NamedElement = Generalization(general=NamedElement, specific=testpackage_Group)

# Domain Model
domain_model = DomainModel(
    name="testpackage",
    types={testpackage_User, NamedElement, testpackage_Group, testpackage_NamedElement},
    associations={members0},
    generalizations={gen_testpackage_User_NamedElement, gen_testpackage_Group_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)