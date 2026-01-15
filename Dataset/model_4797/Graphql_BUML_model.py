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
Graphql_ScalarType = Class(name="Graphql::ScalarType", is_abstract=True)
Type = Class(name="Type")
Graphql_SystemType = Class(name="Graphql::SystemType")
Graphql_Int = Class(name="Graphql::Int")
ScalarType = Class(name="ScalarType")
Graphql_Float = Class(name="Graphql::Float")
Graphql_String = Class(name="Graphql::String")
Graphql_Boolean = Class(name="Graphql::Boolean")
Graphql_ID = Class(name="Graphql::ID")
Graphql_Enum = Class(name="Graphql::Enum")
Graphql_EnumValue = Class(name="Graphql::EnumValue")
Graphql_Type = Class(name="Graphql::Type", is_abstract=True)
Graphql_Attribute = Class(name="Graphql::Attribute")
Graphql_Schema = Class(name="Graphql::Schema")

# Graphql_ScalarType class attributes and methods

# Type class attributes and methods

# Graphql_SystemType class attributes and methods

# Graphql_Int class attributes and methods

# ScalarType class attributes and methods

# Graphql_Float class attributes and methods

# Graphql_String class attributes and methods

# Graphql_Boolean class attributes and methods

# Graphql_ID class attributes and methods

# Graphql_Enum class attributes and methods

# Graphql_EnumValue class attributes and methods
Graphql_EnumValue_value: Property = Property(name="value", type=StringType)
Graphql_EnumValue_number: Property = Property(name="number", type=StringType)
Graphql_EnumValue.attributes={Graphql_EnumValue_value, Graphql_EnumValue_number}

# Graphql_Type class attributes and methods
Graphql_Type_name: Property = Property(name="name", type=StringType)
Graphql_Type.attributes={Graphql_Type_name}

# Graphql_Attribute class attributes and methods
Graphql_Attribute_name: Property = Property(name="name", type=StringType)
Graphql_Attribute_isArray: Property = Property(name="isArray", type=StringType)
Graphql_Attribute_isNullable: Property = Property(name="isNullable", type=StringType)
Graphql_Attribute_typeName: Property = Property(name="typeName", type=StringType)
Graphql_Attribute.attributes={Graphql_Attribute_isArray, Graphql_Attribute_typeName, Graphql_Attribute_name, Graphql_Attribute_isNullable}

# Graphql_Schema class attributes and methods
Graphql_Schema_name: Property = Property(name="name", type=StringType)
Graphql_Schema.attributes={Graphql_Schema_name}

# Relationships
type1: BinaryAssociation = BinaryAssociation(
    name="type1",
    ends={
        Property(name="Graphql_Type2", type=Graphql_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="Graphql_Schema", type=Graphql_Type, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
enumvalue3: BinaryAssociation = BinaryAssociation(
    name="enumvalue3",
    ends={
        Property(name="Graphql_EnumValue", type=Graphql_Enum, multiplicity=Multiplicity(1, 1)),
        Property(name="Graphql_Enum", type=Graphql_EnumValue, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
attribute0: BinaryAssociation = BinaryAssociation(
    name="attribute0",
    ends={
        Property(name="Graphql_Attribute", type=Graphql_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="Graphql_Type", type=Graphql_Attribute, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_Graphql_ScalarType_Type = Generalization(general=Type, specific=Graphql_ScalarType)
gen_Graphql_SystemType_Type = Generalization(general=Type, specific=Graphql_SystemType)
gen_Graphql_Int_ScalarType = Generalization(general=ScalarType, specific=Graphql_Int)
gen_Graphql_Float_ScalarType = Generalization(general=ScalarType, specific=Graphql_Float)
gen_Graphql_String_ScalarType = Generalization(general=ScalarType, specific=Graphql_String)
gen_Graphql_Boolean_ScalarType = Generalization(general=ScalarType, specific=Graphql_Boolean)
gen_Graphql_ID_ScalarType = Generalization(general=ScalarType, specific=Graphql_ID)
gen_Graphql_Enum_Type = Generalization(general=Type, specific=Graphql_Enum)

# Domain Model
domain_model = DomainModel(
    name="Graphql",
    types={Graphql_ScalarType, Type, Graphql_SystemType, Graphql_Int, ScalarType, Graphql_Float, Graphql_String, Graphql_Boolean, Graphql_ID, Graphql_Enum, Graphql_EnumValue, Graphql_Type, Graphql_Attribute, Graphql_Schema},
    associations={type1, enumvalue3, attribute0},
    generalizations={gen_Graphql_ScalarType_Type, gen_Graphql_SystemType_Type, gen_Graphql_Int_ScalarType, gen_Graphql_Float_ScalarType, gen_Graphql_String_ScalarType, gen_Graphql_Boolean_ScalarType, gen_Graphql_ID_ScalarType, gen_Graphql_Enum_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)