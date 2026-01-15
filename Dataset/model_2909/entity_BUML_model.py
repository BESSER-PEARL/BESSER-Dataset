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
entitymm_Attribute = Class(name="entitymm::Attribute")
entitymm_Entity = Class(name="entitymm::Entity")
entitymm_PrimitiveType = Class(name="entitymm::PrimitiveType")
Type = Class(name="Type")
entitymm_Model = Class(name="entitymm::Model")
entitymm_Type = Class(name="entitymm::Type", is_abstract=True)

# entitymm_Attribute class attributes and methods
entitymm_Attribute_name: Property = Property(name="name", type=StringType)
entitymm_Attribute.attributes={entitymm_Attribute_name}

# entitymm_Entity class attributes and methods
entitymm_Entity_isPersistent: Property = Property(name="isPersistent", type=BooleanType)
entitymm_Entity_size: Property = Property(name="size", type=IntegerType)
entitymm_Entity_desc: Property = Property(name="desc", type=StringType)
entitymm_Entity.attributes={entitymm_Entity_desc, entitymm_Entity_size, entitymm_Entity_isPersistent}

# entitymm_PrimitiveType class attributes and methods

# Type class attributes and methods

# entitymm_Model class attributes and methods
entitymm_Model_name: Property = Property(name="name", type=StringType)
entitymm_Model.attributes={entitymm_Model_name}

# entitymm_Type class attributes and methods
entitymm_Type_name: Property = Property(name="name", type=StringType)
entitymm_Type.attributes={entitymm_Type_name}

# Relationships
entity1: BinaryAssociation = BinaryAssociation(
    name="entity1",
    ends={
        Property(name="Entity", type=entitymm_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=entitymm_Entity, multiplicity=Multiplicity(1, 1))
    }
)
type2: BinaryAssociation = BinaryAssociation(
    name="type2",
    ends={
        Property(name="entitymm_PrimitiveType", type=entitymm_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="entitymm_Attribute", type=entitymm_PrimitiveType, multiplicity=Multiplicity(1, 1))
    }
)
attributes3: BinaryAssociation = BinaryAssociation(
    name="attributes3",
    ends={
        Property(name="Attribute", type=entitymm_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entity", type=entitymm_Attribute, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
types0: BinaryAssociation = BinaryAssociation(
    name="types0",
    ends={
        Property(name="entitymm_Type", type=entitymm_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="entitymm_Model", type=entitymm_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_entitymm_PrimitiveType_Type = Generalization(general=Type, specific=entitymm_PrimitiveType)
gen_entitymm_Entity_Type = Generalization(general=Type, specific=entitymm_Entity)

# Domain Model
domain_model = DomainModel(
    name="entitymm",
    types={entitymm_Attribute, entitymm_Entity, entitymm_PrimitiveType, Type, entitymm_Model, entitymm_Type},
    associations={entity1, type2, attributes3, types0},
    generalizations={gen_entitymm_PrimitiveType_Type, gen_entitymm_Entity_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)