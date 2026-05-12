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
MyClass = Class(name="MyClass")
sfbsdf = Class(name="sfbsdf")
MyClass2 = Class(name="MyClass2")
MyClass3 = Class(name="MyClass3")
MyClass4 = Class(name="MyClass4")
MyClass5 = Class(name="MyClass5")
MyClass6 = Class(name="MyClass6")
MyClass32 = Class(name="MyClass32")
MyClass33 = Class(name="MyClass33")
MyClass34 = Class(name="MyClass34")
MyClass35 = Class(name="MyClass35")
MyClass36 = Class(name="MyClass36")
MyClass37 = Class(name="MyClass37")

# MyClass class attributes and methods
MyClass_TenCoSo: Property = Property(name="TenCoSo", type=StringType)
MyClass_attribute: Property = Property(name="attribute", type=StringType)
MyClass_attribute2: Property = Property(name="attribute2", type=StringType)
MyClass_attribute3: Property = Property(name="attribute3", type=StringType)
MyClass.attributes={MyClass_attribute2, MyClass_attribute3, MyClass_attribute, MyClass_TenCoSo}

# sfbsdf class attributes and methods

# MyClass2 class attributes and methods

# MyClass3 class attributes and methods

# MyClass4 class attributes and methods

# MyClass5 class attributes and methods

# MyClass6 class attributes and methods

# MyClass32 class attributes and methods

# MyClass33 class attributes and methods

# MyClass34 class attributes and methods

# MyClass35 class attributes and methods

# MyClass36 class attributes and methods

# MyClass37 class attributes and methods

# Relationships
MyClass_sfbsdf: BinaryAssociation = BinaryAssociation(
    name="MyClass_sfbsdf",
    ends={
        Property(name="MyClass_sfbsdf_00", type=sfbsdf, multiplicity=Multiplicity(0, 1)),
        Property(name="MyClass_sfbsdf_11", type=MyClass, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_UR1H4MCwEeeEXb8Dudo6PQ",
    types={MyClass, sfbsdf, MyClass2, MyClass3, MyClass4, MyClass5, MyClass6, MyClass32, MyClass33, MyClass34, MyClass35, MyClass36, MyClass37},
    associations={MyClass_sfbsdf},
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