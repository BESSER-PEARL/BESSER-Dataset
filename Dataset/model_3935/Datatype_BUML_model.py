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

# Enumerations
PrimitiveType: Enumeration = Enumeration(
    name="PrimitiveType",
    literals={
            EnumerationLiteral(name="string"),
			EnumerationLiteral(name="int"),
			EnumerationLiteral(name="float"),
			EnumerationLiteral(name="boolean"),
			EnumerationLiteral(name="datetime"),
			EnumerationLiteral(name="double"),
			EnumerationLiteral(name="long"),
			EnumerationLiteral(name="short"),
			EnumerationLiteral(name="base64Binary"),
			EnumerationLiteral(name="byte")
    }
)

ConstraintIntervalType: Enumeration = Enumeration(
    name="ConstraintIntervalType",
    literals={
            EnumerationLiteral(name="max"),
			EnumerationLiteral(name="strlen"),
			EnumerationLiteral(name="regex"),
			EnumerationLiteral(name="mimetype"),
			EnumerationLiteral(name="scaling"),
			EnumerationLiteral(name="default"),
			EnumerationLiteral(name="nullable"),
			EnumerationLiteral(name="min")
    }
)

BooleanPropertyAttributeType: Enumeration = Enumeration(
    name="BooleanPropertyAttributeType",
    literals={
            EnumerationLiteral(name="readable"),
			EnumerationLiteral(name="writable"),
			EnumerationLiteral(name="eventable")
    }
)

EnumLiteralPropertyAttributeType: Enumeration = Enumeration(
    name="EnumLiteralPropertyAttributeType",
    literals={
            EnumerationLiteral(name="measurementUnit")
    }
)

# Classes
datatype_Property = Class(name="datatype::Property")
datatype_Presence = Class(name="datatype::Presence")
datatype_ConstraintRule = Class(name="datatype::ConstraintRule")
datatype_Entity = Class(name="datatype::Entity")
Type = Class(name="Type")
datatype_Enum = Class(name="datatype::Enum")
datatype_EnumLiteral = Class(name="datatype::EnumLiteral")
Model = Class(name="Model")
datatype_PropertyType = Class(name="datatype::PropertyType")
datatype_PropertyAttribute = Class(name="datatype::PropertyAttribute", is_abstract=True)
datatype_PrimitivePropertyType = Class(name="datatype::PrimitivePropertyType")
PropertyType = Class(name="PropertyType")
datatype_ObjectPropertyType = Class(name="datatype::ObjectPropertyType")
datatype_Type = Class(name="datatype::Type")
datatype_Constraint = Class(name="datatype::Constraint")
datatype_BooleanPropertyAttribute = Class(name="datatype::BooleanPropertyAttribute")
PropertyAttribute = Class(name="PropertyAttribute")
datatype_EnumLiteralPropertyAttribute = Class(name="datatype::EnumLiteralPropertyAttribute")
datatype_ComplexPrimitivePropertyType = Class(name="datatype::ComplexPrimitivePropertyType")
datatype_DictionaryPropertyType = Class(name="datatype::DictionaryPropertyType")
ComplexPrimitivePropertyType = Class(name="ComplexPrimitivePropertyType")

# datatype_Property class attributes and methods
datatype_Property_multiplicity: Property = Property(name="multiplicity", type=BooleanType)
datatype_Property_name: Property = Property(name="name", type=StringType)
datatype_Property_description: Property = Property(name="description", type=StringType)
datatype_Property_extension: Property = Property(name="extension", type=BooleanType)
datatype_Property.attributes={datatype_Property_name, datatype_Property_multiplicity, datatype_Property_extension, datatype_Property_description}

# datatype_Presence class attributes and methods
datatype_Presence_mandatory: Property = Property(name="mandatory", type=BooleanType)
datatype_Presence.attributes={datatype_Presence_mandatory}

# datatype_ConstraintRule class attributes and methods

# datatype_Entity class attributes and methods

# Type class attributes and methods

# datatype_Enum class attributes and methods

# datatype_EnumLiteral class attributes and methods
datatype_EnumLiteral_name: Property = Property(name="name", type=StringType)
datatype_EnumLiteral_description: Property = Property(name="description", type=StringType)
datatype_EnumLiteral.attributes={datatype_EnumLiteral_description, datatype_EnumLiteral_name}

# Model class attributes and methods

# datatype_PropertyType class attributes and methods

# datatype_PropertyAttribute class attributes and methods

# datatype_PrimitivePropertyType class attributes and methods
datatype_PrimitivePropertyType_type: Property = Property(name="type", type=StringType)
datatype_PrimitivePropertyType.attributes={datatype_PrimitivePropertyType_type}

# PropertyType class attributes and methods

# datatype_ObjectPropertyType class attributes and methods

# datatype_Type class attributes and methods

# datatype_Constraint class attributes and methods
datatype_Constraint_type: Property = Property(name="type", type=StringType)
datatype_Constraint_constraintValues: Property = Property(name="constraintValues", type=StringType)
datatype_Constraint.attributes={datatype_Constraint_constraintValues, datatype_Constraint_type}

# datatype_BooleanPropertyAttribute class attributes and methods
datatype_BooleanPropertyAttribute_type: Property = Property(name="type", type=StringType)
datatype_BooleanPropertyAttribute_value: Property = Property(name="value", type=BooleanType)
datatype_BooleanPropertyAttribute.attributes={datatype_BooleanPropertyAttribute_type, datatype_BooleanPropertyAttribute_value}

# PropertyAttribute class attributes and methods

# datatype_EnumLiteralPropertyAttribute class attributes and methods
datatype_EnumLiteralPropertyAttribute_type: Property = Property(name="type", type=StringType)
datatype_EnumLiteralPropertyAttribute.attributes={datatype_EnumLiteralPropertyAttribute_type}

# datatype_ComplexPrimitivePropertyType class attributes and methods

# datatype_DictionaryPropertyType class attributes and methods

# ComplexPrimitivePropertyType class attributes and methods

# Relationships
superType1: BinaryAssociation = BinaryAssociation(
    name="superType1",
    ends={
        Property(name="datatype_Entity", type=datatype_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="datatype_Entity0", type=datatype_Entity, multiplicity=Multiplicity(0, 1))
    }
)
properties2: BinaryAssociation = BinaryAssociation(
    name="properties2",
    ends={
        Property(name="datatype_Property", type=datatype_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="datatype_Entity3", type=datatype_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
presence4: BinaryAssociation = BinaryAssociation(
    name="presence4",
    ends={
        Property(name="datatype_Presence", type=datatype_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="datatype_Property5", type=datatype_Presence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constraintRule6: BinaryAssociation = BinaryAssociation(
    name="constraintRule6",
    ends={
        Property(name="datatype_ConstraintRule", type=datatype_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="datatype_Property7", type=datatype_ConstraintRule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enums13: BinaryAssociation = BinaryAssociation(
    name="enums13",
    ends={
        Property(name="datatype_EnumLiteral", type=datatype_Enum, multiplicity=Multiplicity(1, 1)),
        Property(name="datatype_Enum", type=datatype_EnumLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type8: BinaryAssociation = BinaryAssociation(
    name="type8",
    ends={
        Property(name="datatype_PropertyType", type=datatype_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="datatype_Property9", type=datatype_PropertyType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propertyAttributes10: BinaryAssociation = BinaryAssociation(
    name="propertyAttributes10",
    ends={
        Property(name="datatype_PropertyAttribute", type=datatype_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="datatype_Property11", type=datatype_PropertyAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type12: BinaryAssociation = BinaryAssociation(
    name="type12",
    ends={
        Property(name="datatype_Type", type=datatype_ObjectPropertyType, multiplicity=Multiplicity(1, 1)),
        Property(name="datatype_ObjectPropertyType", type=datatype_Type, multiplicity=Multiplicity(0, 1))
    }
)
value14: BinaryAssociation = BinaryAssociation(
    name="value14",
    ends={
        Property(name="datatype_EnumLiteral15", type=datatype_EnumLiteralPropertyAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="datatype_EnumLiteralPropertyAttribute", type=datatype_EnumLiteral, multiplicity=Multiplicity(0, 1))
    }
)
Constraints16: BinaryAssociation = BinaryAssociation(
    name="Constraints16",
    ends={
        Property(name="datatype_Constraint", type=datatype_ConstraintRule, multiplicity=Multiplicity(1, 1)),
        Property(name="datatype_ConstraintRule17", type=datatype_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyType18: BinaryAssociation = BinaryAssociation(
    name="keyType18",
    ends={
        Property(name="datatype_PropertyType19", type=datatype_DictionaryPropertyType, multiplicity=Multiplicity(1, 1)),
        Property(name="datatype_DictionaryPropertyType", type=datatype_PropertyType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
valueType20: BinaryAssociation = BinaryAssociation(
    name="valueType20",
    ends={
        Property(name="datatype_PropertyType22", type=datatype_DictionaryPropertyType, multiplicity=Multiplicity(1, 1)),
        Property(name="datatype_DictionaryPropertyType21", type=datatype_PropertyType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_datatype_Entity_Type = Generalization(general=Type, specific=datatype_Entity)
gen_datatype_Enum_Type = Generalization(general=Type, specific=datatype_Enum)
gen_datatype_PrimitivePropertyType_PropertyType = Generalization(general=PropertyType, specific=datatype_PrimitivePropertyType)
gen_datatype_ObjectPropertyType_PropertyType = Generalization(general=PropertyType, specific=datatype_ObjectPropertyType)
gen_datatype_Type_Model = Generalization(general=Model, specific=datatype_Type)
gen_datatype_BooleanPropertyAttribute_PropertyAttribute = Generalization(general=PropertyAttribute, specific=datatype_BooleanPropertyAttribute)
gen_datatype_EnumLiteralPropertyAttribute_PropertyAttribute = Generalization(general=PropertyAttribute, specific=datatype_EnumLiteralPropertyAttribute)
gen_datatype_ComplexPrimitivePropertyType_PropertyType = Generalization(general=PropertyType, specific=datatype_ComplexPrimitivePropertyType)
gen_datatype_DictionaryPropertyType_ComplexPrimitivePropertyType = Generalization(general=ComplexPrimitivePropertyType, specific=datatype_DictionaryPropertyType)

# Domain Model
domain_model = DomainModel(
    name="datatype",
    types={datatype_Property, datatype_Presence, datatype_ConstraintRule, datatype_Entity, Type, datatype_Enum, datatype_EnumLiteral, Model, datatype_PropertyType, datatype_PropertyAttribute, datatype_PrimitivePropertyType, PropertyType, datatype_ObjectPropertyType, datatype_Type, datatype_Constraint, datatype_BooleanPropertyAttribute, PropertyAttribute, datatype_EnumLiteralPropertyAttribute, datatype_ComplexPrimitivePropertyType, datatype_DictionaryPropertyType, ComplexPrimitivePropertyType, PrimitiveType, ConstraintIntervalType, BooleanPropertyAttributeType, EnumLiteralPropertyAttributeType},
    associations={superType1, properties2, presence4, constraintRule6, enums13, type8, propertyAttributes10, type12, value14, Constraints16, keyType18, valueType20},
    generalizations={gen_datatype_Entity_Type, gen_datatype_Enum_Type, gen_datatype_PrimitivePropertyType_PropertyType, gen_datatype_ObjectPropertyType_PropertyType, gen_datatype_Type_Model, gen_datatype_BooleanPropertyAttribute_PropertyAttribute, gen_datatype_EnumLiteralPropertyAttribute_PropertyAttribute, gen_datatype_ComplexPrimitivePropertyType_PropertyType, gen_datatype_DictionaryPropertyType_ComplexPrimitivePropertyType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)