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
main_MainType = Class(name="main::MainType")
main_sub1_Sub1Type = Class(name="main::sub1::Sub1Type")
main_sub2_Sub2Type = Class(name="main::sub2::Sub2Type")

# main_MainType class attributes and methods
main_MainType_name: Property = Property(name="name", type=StringType)
main_MainType.attributes={main_MainType_name}

# main_sub1_Sub1Type class attributes and methods
main_sub1_Sub1Type_name: Property = Property(name="name", type=StringType)
main_sub1_Sub1Type.attributes={main_sub1_Sub1Type_name}

# main_sub2_Sub2Type class attributes and methods
main_sub2_Sub2Type_name: Property = Property(name="name", type=StringType)
main_sub2_Sub2Type.attributes={main_sub2_Sub2Type_name}

# Domain Model
domain_model = DomainModel(
    name="main",
    types={main_MainType, main_sub1_Sub1Type, main_sub2_Sub2Type},
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