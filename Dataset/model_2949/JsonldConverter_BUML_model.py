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
jsonldConverter_Model = Class(name="jsonldConverter::Model")
jsonldConverter_Property = Class(name="jsonldConverter::Property")
jsonldConverter_Type = Class(name="jsonldConverter::Type")
jsonldConverter_DataType = Class(name="jsonldConverter::DataType")
Type = Class(name="Type")
jsonldConverter_Entity = Class(name="jsonldConverter::Entity")
jsonldConverter_Enum = Class(name="jsonldConverter::Enum")
jsonldConverter_EnumItem = Class(name="jsonldConverter::EnumItem")

# jsonldConverter_Model class attributes and methods

# jsonldConverter_Property class attributes and methods
jsonldConverter_Property_name: Property = Property(name="name", type=StringType)
jsonldConverter_Property_many: Property = Property(name="many", type=BooleanType)
jsonldConverter_Property_one: Property = Property(name="one", type=BooleanType)
jsonldConverter_Property.attributes={jsonldConverter_Property_one, jsonldConverter_Property_name, jsonldConverter_Property_many}

# jsonldConverter_Type class attributes and methods
jsonldConverter_Type_name: Property = Property(name="name", type=StringType)
jsonldConverter_Type.attributes={jsonldConverter_Type_name}

# jsonldConverter_DataType class attributes and methods

# Type class attributes and methods

# jsonldConverter_Entity class attributes and methods

# jsonldConverter_Enum class attributes and methods

# jsonldConverter_EnumItem class attributes and methods
jsonldConverter_EnumItem_name: Property = Property(name="name", type=StringType)
jsonldConverter_EnumItem_type: Property = Property(name="type", type=StringType)
jsonldConverter_EnumItem.attributes={jsonldConverter_EnumItem_type, jsonldConverter_EnumItem_name}

# Relationships
superType2: BinaryAssociation = BinaryAssociation(
    name="superType2",
    ends={
        Property(name="jsonldConverter_Entity", type=jsonldConverter_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="jsonldConverter_Entity1", type=jsonldConverter_Entity, multiplicity=Multiplicity(0, 1))
    }
)
features3: BinaryAssociation = BinaryAssociation(
    name="features3",
    ends={
        Property(name="jsonldConverter_Property", type=jsonldConverter_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="jsonldConverter_Entity4", type=jsonldConverter_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type5: BinaryAssociation = BinaryAssociation(
    name="type5",
    ends={
        Property(name="jsonldConverter_Type7", type=jsonldConverter_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="jsonldConverter_Property6", type=jsonldConverter_Type, multiplicity=Multiplicity(0, 1))
    }
)
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="jsonldConverter_Type", type=jsonldConverter_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="jsonldConverter_Model", type=jsonldConverter_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features8: BinaryAssociation = BinaryAssociation(
    name="features8",
    ends={
        Property(name="jsonldConverter_EnumItem", type=jsonldConverter_Enum, multiplicity=Multiplicity(1, 1)),
        Property(name="jsonldConverter_Enum", type=jsonldConverter_EnumItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_jsonldConverter_DataType_Type = Generalization(general=Type, specific=jsonldConverter_DataType)
gen_jsonldConverter_Entity_Type = Generalization(general=Type, specific=jsonldConverter_Entity)
gen_jsonldConverter_Enum_Type = Generalization(general=Type, specific=jsonldConverter_Enum)

# Domain Model
domain_model = DomainModel(
    name="jsonldConverter",
    types={jsonldConverter_Model, jsonldConverter_Property, jsonldConverter_Type, jsonldConverter_DataType, Type, jsonldConverter_Entity, jsonldConverter_Enum, jsonldConverter_EnumItem},
    associations={superType2, features3, type5, elements0, features8},
    generalizations={gen_jsonldConverter_DataType_Type, gen_jsonldConverter_Entity_Type, gen_jsonldConverter_Enum_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)