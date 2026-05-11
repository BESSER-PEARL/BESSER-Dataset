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
entitiesDsl_Attribute = Class(name="entitiesDsl_Attribute")
Feature = Class(name="Feature")
entitiesDsl_Model = Class(name="entitiesDsl_Model")
entitiesDsl_Type = Class(name="entitiesDsl_Type")
entitiesDsl_DataType = Class(name="entitiesDsl_DataType")
Type = Class(name="Type")
entitiesDsl_Entity = Class(name="entitiesDsl_Entity")
entitiesDsl_Feature = Class(name="entitiesDsl_Feature")

# entitiesDsl_Attribute class attributes and methods
entitiesDsl_Attribute_attrrName: Property = Property(name="attrrName", type=StringType)
entitiesDsl_Attribute.attributes={entitiesDsl_Attribute_attrrName}

# Feature class attributes and methods

# entitiesDsl_Model class attributes and methods

# entitiesDsl_Type class attributes and methods
entitiesDsl_Type_name: Property = Property(name="name", type=StringType)
entitiesDsl_Type.attributes={entitiesDsl_Type_name}

# entitiesDsl_DataType class attributes and methods

# Type class attributes and methods

# entitiesDsl_Entity class attributes and methods

# entitiesDsl_Feature class attributes and methods

# Relationships
features1: BinaryAssociation = BinaryAssociation(
    name="features1",
    ends={
        Property(name="entitiesDsl_Entity", type=entitiesDsl_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="entitiesDsl_Feature", type=entitiesDsl_Entity, multiplicity=Multiplicity(1, 1))
    }
)
type2: BinaryAssociation = BinaryAssociation(
    name="type2",
    ends={
        Property(name="entitiesDsl_Type3", type=entitiesDsl_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="entitiesDsl_Attribute", type=entitiesDsl_Type, multiplicity=Multiplicity(0, 1))
    }
)
types0: BinaryAssociation = BinaryAssociation(
    name="types0",
    ends={
        Property(name="entitiesDsl_Type", type=entitiesDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="entitiesDsl_Model", type=entitiesDsl_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_entitiesDsl_Attribute_Feature = Generalization(general=Feature, specific=entitiesDsl_Attribute)
gen_entitiesDsl_DataType_Type = Generalization(general=Type, specific=entitiesDsl_DataType)
gen_entitiesDsl_Entity_Type = Generalization(general=Type, specific=entitiesDsl_Entity)

# Domain Model
domain_model = DomainModel(
    name="entitiesDsl",
    types={entitiesDsl_Attribute, Feature, entitiesDsl_Model, entitiesDsl_Type, entitiesDsl_DataType, Type, entitiesDsl_Entity, entitiesDsl_Feature},
    associations={features1, type2, types0},
    generalizations={gen_entitiesDsl_Attribute_Feature, gen_entitiesDsl_DataType_Type, gen_entitiesDsl_Entity_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)