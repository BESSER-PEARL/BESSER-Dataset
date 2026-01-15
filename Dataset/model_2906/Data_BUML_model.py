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
Data_Model = Class(name="Data::Model")
Data_Type = Class(name="Data::Type", is_abstract=True)
Data_Attribute = Class(name="Data::Attribute")
Data_Entity = Class(name="Data::Entity")
Type = Class(name="Type")
Data_PrimitiveType = Class(name="Data::PrimitiveType")

# Data_Model class attributes and methods

# Data_Type class attributes and methods
Data_Type_name: Property = Property(name="name", type=StringType)
Data_Type.attributes={Data_Type_name}

# Data_Attribute class attributes and methods
Data_Attribute_name: Property = Property(name="name", type=StringType)
Data_Attribute.attributes={Data_Attribute_name}

# Data_Entity class attributes and methods

# Type class attributes and methods

# Data_PrimitiveType class attributes and methods

# Relationships
types0: BinaryAssociation = BinaryAssociation(
    name="types0",
    ends={
        Property(name="Data_Type", type=Data_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="Data_Model", type=Data_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type1: BinaryAssociation = BinaryAssociation(
    name="type1",
    ends={
        Property(name="Data_Type2", type=Data_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="Data_Attribute", type=Data_Type, multiplicity=Multiplicity(1, 1))
    }
)
attributes3: BinaryAssociation = BinaryAssociation(
    name="attributes3",
    ends={
        Property(name="Data_Attribute4", type=Data_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="Data_Entity", type=Data_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_Data_Entity_Type = Generalization(general=Type, specific=Data_Entity)
gen_Data_PrimitiveType_Type = Generalization(general=Type, specific=Data_PrimitiveType)

# Domain Model
domain_model = DomainModel(
    name="Data",
    types={Data_Model, Data_Type, Data_Attribute, Data_Entity, Type, Data_PrimitiveType},
    associations={types0, type1, attributes3},
    generalizations={gen_Data_Entity_Type, gen_Data_PrimitiveType_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)