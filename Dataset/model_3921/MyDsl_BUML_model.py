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
myDsl_Model = Class(name="myDsl::Model")
myDsl_SimpleType = Class(name="myDsl::SimpleType")
Type = Class(name="Type")
myDsl_Entity = Class(name="myDsl::Entity")
myDsl_Property = Class(name="myDsl::Property")
myDsl_Import = Class(name="myDsl::Import")
myDsl_Type = Class(name="myDsl::Type")

# myDsl_Model class attributes and methods

# myDsl_SimpleType class attributes and methods

# Type class attributes and methods

# myDsl_Entity class attributes and methods

# myDsl_Property class attributes and methods
myDsl_Property_name: Property = Property(name="name", type=StringType)
myDsl_Property_many: Property = Property(name="many", type=BooleanType)
myDsl_Property.attributes={myDsl_Property_name, myDsl_Property_many}

# myDsl_Import class attributes and methods
myDsl_Import_importURI: Property = Property(name="importURI", type=StringType)
myDsl_Import.attributes={myDsl_Import_importURI}

# myDsl_Type class attributes and methods
myDsl_Type_name: Property = Property(name="name", type=StringType)
myDsl_Type.attributes={myDsl_Type_name}

# Relationships
extends4: BinaryAssociation = BinaryAssociation(
    name="extends4",
    ends={
        Property(name="myDsl_Entity", type=myDsl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Entity3", type=myDsl_Entity, multiplicity=Multiplicity(0, 1))
    }
)
properties5: BinaryAssociation = BinaryAssociation(
    name="properties5",
    ends={
        Property(name="myDsl_Property", type=myDsl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Entity6", type=myDsl_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="myDsl_Type9", type=myDsl_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Property8", type=myDsl_Type, multiplicity=Multiplicity(0, 1))
    }
)
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="myDsl_Import", type=myDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Model", type=myDsl_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="myDsl_Type", type=myDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Model2", type=myDsl_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_myDsl_SimpleType_Type = Generalization(general=Type, specific=myDsl_SimpleType)
gen_myDsl_Entity_Type = Generalization(general=Type, specific=myDsl_Entity)

# Domain Model
domain_model = DomainModel(
    name="myDsl",
    types={myDsl_Model, myDsl_SimpleType, Type, myDsl_Entity, myDsl_Property, myDsl_Import, myDsl_Type},
    associations={extends4, properties5, type7, imports0, elements1},
    generalizations={gen_myDsl_SimpleType_Type, gen_myDsl_Entity_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)