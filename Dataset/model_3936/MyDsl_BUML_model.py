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
myDsl_Association = Class(name="myDsl::Association")
myDsl_Attribute = Class(name="myDsl::Attribute")
myDsl_Role = Class(name="myDsl::Role")
myDsl_Entity = Class(name="myDsl::Entity")

# myDsl_Domainmodel class attributes and methods

# myDsl_Type class attributes and methods
myDsl_Type_name: Property = Property(name="name", type=StringType)
myDsl_Type.attributes={myDsl_Type_name}

# myDsl_DataType class attributes and methods

# Type class attributes and methods

# myDsl_Association class attributes and methods

# myDsl_Attribute class attributes and methods
myDsl_Attribute_many: Property = Property(name="many", type=BooleanType)
myDsl_Attribute_name: Property = Property(name="name", type=StringType)
myDsl_Attribute.attributes={myDsl_Attribute_name, myDsl_Attribute_many}

# myDsl_Role class attributes and methods
myDsl_Role_many: Property = Property(name="many", type=BooleanType)
myDsl_Role_name: Property = Property(name="name", type=StringType)
myDsl_Role.attributes={myDsl_Role_name, myDsl_Role_many}

# myDsl_Entity class attributes and methods

# Relationships
attribute6: BinaryAssociation = BinaryAssociation(
    name="attribute6",
    ends={
        Property(name="myDsl_Attribute8", type=myDsl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Entity7", type=myDsl_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
role9: BinaryAssociation = BinaryAssociation(
    name="role9",
    ends={
        Property(name="myDsl_Role11", type=myDsl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Entity10", type=myDsl_Role, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type12: BinaryAssociation = BinaryAssociation(
    name="type12",
    ends={
        Property(name="myDsl_Type14", type=myDsl_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Attribute13", type=myDsl_Type, multiplicity=Multiplicity(0, 1))
    }
)
type15: BinaryAssociation = BinaryAssociation(
    name="type15",
    ends={
        Property(name="myDsl_Type17", type=myDsl_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Role16", type=myDsl_Type, multiplicity=Multiplicity(0, 1))
    }
)
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="myDsl_Type", type=myDsl_Domainmodel, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Domainmodel", type=myDsl_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute1: BinaryAssociation = BinaryAssociation(
    name="attribute1",
    ends={
        Property(name="myDsl_Attribute", type=myDsl_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Association", type=myDsl_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
role2: BinaryAssociation = BinaryAssociation(
    name="role2",
    ends={
        Property(name="myDsl_Role", type=myDsl_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Association3", type=myDsl_Role, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superType5: BinaryAssociation = BinaryAssociation(
    name="superType5",
    ends={
        Property(name="myDsl_Entity", type=myDsl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Entity4", type=myDsl_Entity, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_myDsl_DataType_Type = Generalization(general=Type, specific=myDsl_DataType)
gen_myDsl_Association_Type = Generalization(general=Type, specific=myDsl_Association)
gen_myDsl_Entity_Type = Generalization(general=Type, specific=myDsl_Entity)

# Domain Model
domain_model = DomainModel(
    name="myDsl",
    types={myDsl_Domainmodel, myDsl_Type, myDsl_DataType, Type, myDsl_Association, myDsl_Attribute, myDsl_Role, myDsl_Entity},
    associations={attribute6, role9, type12, type15, elements0, attribute1, role2, superType5},
    generalizations={gen_myDsl_DataType_Type, gen_myDsl_Association_Type, gen_myDsl_Entity_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)