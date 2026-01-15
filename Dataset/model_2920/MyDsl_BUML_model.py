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
myDsl_Domainmodel = Class(name="myDsl::Domainmodel")
myDsl_Type = Class(name="myDsl::Type")
myDsl_DataType = Class(name="myDsl::DataType")
Type = Class(name="Type")
myDsl_Entity = Class(name="myDsl::Entity")
myDsl_Feature = Class(name="myDsl::Feature")

# myDsl_Domainmodel class attributes and methods

# myDsl_Type class attributes and methods
myDsl_Type_name: Property = Property(name="name", type=StringType)
myDsl_Type.attributes={myDsl_Type_name}

# myDsl_DataType class attributes and methods

# Type class attributes and methods

# myDsl_Entity class attributes and methods

# myDsl_Feature class attributes and methods
myDsl_Feature_many: Property = Property(name="many", type=BooleanType)
myDsl_Feature_name: Property = Property(name="name", type=StringType)
myDsl_Feature.attributes={myDsl_Feature_many, myDsl_Feature_name}

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="myDsl_Type", type=myDsl_Domainmodel, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Domainmodel", type=myDsl_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superType2: BinaryAssociation = BinaryAssociation(
    name="superType2",
    ends={
        Property(name="myDsl_Entity", type=myDsl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Entity1", type=myDsl_Entity, multiplicity=Multiplicity(0, 1))
    }
)
features3: BinaryAssociation = BinaryAssociation(
    name="features3",
    ends={
        Property(name="myDsl_Feature", type=myDsl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Entity4", type=myDsl_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type5: BinaryAssociation = BinaryAssociation(
    name="type5",
    ends={
        Property(name="myDsl_Type7", type=myDsl_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Feature6", type=myDsl_Type, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_myDsl_DataType_Type = Generalization(general=Type, specific=myDsl_DataType)
gen_myDsl_Entity_Type = Generalization(general=Type, specific=myDsl_Entity)

# Domain Model
domain_model = DomainModel(
    name="myDsl",
    types={myDsl_Domainmodel, myDsl_Type, myDsl_DataType, Type, myDsl_Entity, myDsl_Feature},
    associations={elements0, superType2, features3, type5},
    generalizations={gen_myDsl_DataType_Type, gen_myDsl_Entity_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)