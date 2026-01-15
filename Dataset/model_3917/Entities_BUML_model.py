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
entities_Model = Class(name="entities::Model")
entities_Import = Class(name="entities::Import")
entities_Type = Class(name="entities::Type")
entities_SimpleType = Class(name="entities::SimpleType")
Type = Class(name="Type")
entities_Entity = Class(name="entities::Entity")
entities_Property = Class(name="entities::Property")
entities_SimpleProperty = Class(name="entities::SimpleProperty")
Property_ = Class(name="Property")
entities_Reference = Class(name="entities::Reference")

# entities_Model class attributes and methods

# entities_Import class attributes and methods
entities_Import_importURI: Property = Property(name="importURI", type=StringType)
entities_Import.attributes={entities_Import_importURI}

# entities_Type class attributes and methods
entities_Type_name: Property = Property(name="name", type=StringType)
entities_Type.attributes={entities_Type_name}

# entities_SimpleType class attributes and methods

# Type class attributes and methods

# entities_Entity class attributes and methods

# entities_Property class attributes and methods
entities_Property_name: Property = Property(name="name", type=StringType)
entities_Property_many: Property = Property(name="many", type=BooleanType)
entities_Property.attributes={entities_Property_name, entities_Property_many}

# entities_SimpleProperty class attributes and methods

# Property class attributes and methods

# entities_Reference class attributes and methods

# Relationships
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="entities_Import", type=entities_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="entities_Model", type=entities_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extends4: BinaryAssociation = BinaryAssociation(
    name="extends4",
    ends={
        Property(name="entities_Entity", type=entities_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entities_Entity3", type=entities_Entity, multiplicity=Multiplicity(0, 1))
    }
)
properties5: BinaryAssociation = BinaryAssociation(
    name="properties5",
    ends={
        Property(name="entities_Property", type=entities_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entities_Entity6", type=entities_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="entities_SimpleType", type=entities_SimpleProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="entities_SimpleProperty", type=entities_SimpleType, multiplicity=Multiplicity(0, 1))
    }
)
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="entities_Type", type=entities_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="entities_Model2", type=entities_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type8: BinaryAssociation = BinaryAssociation(
    name="type8",
    ends={
        Property(name="entities_Entity9", type=entities_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="entities_Reference", type=entities_Entity, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_entities_SimpleType_Type = Generalization(general=Type, specific=entities_SimpleType)
gen_entities_Entity_Type = Generalization(general=Type, specific=entities_Entity)
gen_entities_SimpleProperty_Property = Generalization(general=Property_, specific=entities_SimpleProperty)
gen_entities_Reference_Property = Generalization(general=Property_, specific=entities_Reference)

# Domain Model
domain_model = DomainModel(
    name="entities",
    types={entities_Model, entities_Import, entities_Type, entities_SimpleType, Type, entities_Entity, entities_Property, entities_SimpleProperty, Property_, entities_Reference},
    associations={imports0, extends4, properties5, type7, elements1, type8},
    generalizations={gen_entities_SimpleType_Type, gen_entities_Entity_Type, gen_entities_SimpleProperty_Property, gen_entities_Reference_Property},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)