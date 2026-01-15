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
entityDsl_SimpleType = Class(name="entityDsl::SimpleType")
Type = Class(name="Type")
entityDsl_Entity = Class(name="entityDsl::Entity")
entityDsl_Property = Class(name="entityDsl::Property")
entityDsl_Model = Class(name="entityDsl::Model")
entityDsl_Type = Class(name="entityDsl::Type")

# entityDsl_SimpleType class attributes and methods

# Type class attributes and methods

# entityDsl_Entity class attributes and methods

# entityDsl_Property class attributes and methods
entityDsl_Property_name: Property = Property(name="name", type=StringType)
entityDsl_Property_many: Property = Property(name="many", type=BooleanType)
entityDsl_Property.attributes={entityDsl_Property_name, entityDsl_Property_many}

# entityDsl_Model class attributes and methods

# entityDsl_Type class attributes and methods
entityDsl_Type_name: Property = Property(name="name", type=StringType)
entityDsl_Type.attributes={entityDsl_Type_name}

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="entityDsl_Model", type=entityDsl_Type, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="entityDsl_Type", type=entityDsl_Model, multiplicity=Multiplicity(1, 1))
    }
)
extends2: BinaryAssociation = BinaryAssociation(
    name="extends2",
    ends={
        Property(name="entityDsl_Entity", type=entityDsl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entityDsl_Entity1", type=entityDsl_Entity, multiplicity=Multiplicity(0, 1))
    }
)
properties3: BinaryAssociation = BinaryAssociation(
    name="properties3",
    ends={
        Property(name="entityDsl_Property", type=entityDsl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entityDsl_Entity4", type=entityDsl_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type5: BinaryAssociation = BinaryAssociation(
    name="type5",
    ends={
        Property(name="entityDsl_Type7", type=entityDsl_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="entityDsl_Property6", type=entityDsl_Type, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_entityDsl_SimpleType_Type = Generalization(general=Type, specific=entityDsl_SimpleType)
gen_entityDsl_Entity_Type = Generalization(general=Type, specific=entityDsl_Entity)

# Domain Model
domain_model = DomainModel(
    name="entityDsl",
    types={entityDsl_SimpleType, Type, entityDsl_Entity, entityDsl_Property, entityDsl_Model, entityDsl_Type},
    associations={elements0, extends2, properties3, type5},
    generalizations={gen_entityDsl_SimpleType_Type, gen_entityDsl_Entity_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)