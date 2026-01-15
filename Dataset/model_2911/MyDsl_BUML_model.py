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
myDsl_DomainModel = Class(name="myDsl::DomainModel")
myDsl_Type = Class(name="myDsl::Type")
myDsl_DataType = Class(name="myDsl::DataType")
Type = Class(name="Type")
myDsl_Features = Class(name="myDsl::Features")
myDsl_Entity = Class(name="myDsl::Entity")

# myDsl_DomainModel class attributes and methods

# myDsl_Type class attributes and methods
myDsl_Type_name: Property = Property(name="name", type=StringType)
myDsl_Type.attributes={myDsl_Type_name}

# myDsl_DataType class attributes and methods

# Type class attributes and methods

# myDsl_Features class attributes and methods
myDsl_Features_name: Property = Property(name="name", type=StringType)
myDsl_Features.attributes={myDsl_Features_name}

# myDsl_Entity class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="myDsl_Type", type=myDsl_DomainModel, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_DomainModel", type=myDsl_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type1: BinaryAssociation = BinaryAssociation(
    name="type1",
    ends={
        Property(name="myDsl_Type2", type=myDsl_Features, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Features", type=myDsl_Type, multiplicity=Multiplicity(0, 1))
    }
)
supertype4: BinaryAssociation = BinaryAssociation(
    name="supertype4",
    ends={
        Property(name="myDsl_Entity", type=myDsl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Entity3", type=myDsl_Entity, multiplicity=Multiplicity(0, 1))
    }
)
features5: BinaryAssociation = BinaryAssociation(
    name="features5",
    ends={
        Property(name="myDsl_Features7", type=myDsl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Entity6", type=myDsl_Features, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_myDsl_DataType_Type = Generalization(general=Type, specific=myDsl_DataType)
gen_myDsl_Entity_Type = Generalization(general=Type, specific=myDsl_Entity)

# Domain Model
domain_model = DomainModel(
    name="myDsl",
    types={myDsl_DomainModel, myDsl_Type, myDsl_DataType, Type, myDsl_Features, myDsl_Entity},
    associations={elements0, type1, supertype4, features5},
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