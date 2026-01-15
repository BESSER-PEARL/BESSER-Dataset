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
entityDsl_AbstractType = Class(name="entityDsl::AbstractType")
entityDsl_Named = Class(name="entityDsl::Named")
entityDsl_BooleanType = Class(name="entityDsl::BooleanType")
AbstractType = Class(name="AbstractType")
entityDsl_IntType = Class(name="entityDsl::IntType")
entityDsl_StringType = Class(name="entityDsl::StringType")
entityDsl_Module = Class(name="entityDsl::Module")
Named = Class(name="Named")
entityDsl_Entity = Class(name="entityDsl::Entity")
entityDsl_Attribute = Class(name="entityDsl::Attribute")
entityDsl_EntityReference = Class(name="entityDsl::EntityReference")

# entityDsl_AbstractType class attributes and methods

# entityDsl_Named class attributes and methods
entityDsl_Named_name: Property = Property(name="name", type=StringType)
entityDsl_Named.attributes={entityDsl_Named_name}

# entityDsl_BooleanType class attributes and methods

# AbstractType class attributes and methods

# entityDsl_IntType class attributes and methods

# entityDsl_StringType class attributes and methods

# entityDsl_Module class attributes and methods

# Named class attributes and methods

# entityDsl_Entity class attributes and methods

# entityDsl_Attribute class attributes and methods

# entityDsl_EntityReference class attributes and methods

# Relationships
attributes1: BinaryAssociation = BinaryAssociation(
    name="attributes1",
    ends={
        Property(name="entityDsl_Attribute", type=entityDsl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entityDsl_Entity2", type=entityDsl_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type3: BinaryAssociation = BinaryAssociation(
    name="type3",
    ends={
        Property(name="entityDsl_AbstractType", type=entityDsl_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="entityDsl_Attribute4", type=entityDsl_AbstractType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entities0: BinaryAssociation = BinaryAssociation(
    name="entities0",
    ends={
        Property(name="entityDsl_Entity", type=entityDsl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="entityDsl_Module", type=entityDsl_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref5: BinaryAssociation = BinaryAssociation(
    name="ref5",
    ends={
        Property(name="entityDsl_Entity6", type=entityDsl_EntityReference, multiplicity=Multiplicity(1, 1)),
        Property(name="entityDsl_EntityReference", type=entityDsl_Entity, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_entityDsl_Attribute_Named = Generalization(general=Named, specific=entityDsl_Attribute)
gen_entityDsl_BooleanType_AbstractType = Generalization(general=AbstractType, specific=entityDsl_BooleanType)
gen_entityDsl_IntType_AbstractType = Generalization(general=AbstractType, specific=entityDsl_IntType)
gen_entityDsl_StringType_AbstractType = Generalization(general=AbstractType, specific=entityDsl_StringType)
gen_entityDsl_Module_Named = Generalization(general=Named, specific=entityDsl_Module)
gen_entityDsl_Entity_Named = Generalization(general=Named, specific=entityDsl_Entity)
gen_entityDsl_EntityReference_AbstractType = Generalization(general=AbstractType, specific=entityDsl_EntityReference)

# Domain Model
domain_model = DomainModel(
    name="entityDsl",
    types={entityDsl_AbstractType, entityDsl_Named, entityDsl_BooleanType, AbstractType, entityDsl_IntType, entityDsl_StringType, entityDsl_Module, Named, entityDsl_Entity, entityDsl_Attribute, entityDsl_EntityReference},
    associations={attributes1, type3, entities0, ref5},
    generalizations={gen_entityDsl_Attribute_Named, gen_entityDsl_BooleanType_AbstractType, gen_entityDsl_IntType_AbstractType, gen_entityDsl_StringType_AbstractType, gen_entityDsl_Module_Named, gen_entityDsl_Entity_Named, gen_entityDsl_EntityReference_AbstractType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)