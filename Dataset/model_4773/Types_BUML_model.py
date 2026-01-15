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
TypeStorageModifier: Enumeration = Enumeration(
    name="TypeStorageModifier",
    literals={
            EnumerationLiteral(name="STORABLE"),
			EnumerationLiteral(name="EMBEDDABLE")
    }
)

EntityRelationshipKind: Enumeration = Enumeration(
    name="EntityRelationshipKind",
    literals={
            EnumerationLiteral(name="UNIQUE"),
			EnumerationLiteral(name="MANY")
    }
)

PropertyStorageModifier: Enumeration = Enumeration(
    name="PropertyStorageModifier",
    literals={
            EnumerationLiteral(name="VARIABLE"),
			EnumerationLiteral(name="VALUE"),
			EnumerationLiteral(name="TRANSIENT")
    }
)

# Classes
types_CollectionType = Class(name="types::CollectionType")
DeclarationTypeReference = Class(name="DeclarationTypeReference")
types_TypeReference = Class(name="types::TypeReference")
types_MapType = Class(name="types::MapType")
types_Model = Class(name="types::Model")
types_Import = Class(name="types::Import")
types_ComplexType = Class(name="types::ComplexType")
types_Type = Class(name="types::Type")
types_NamedType = Class(name="types::NamedType")
Type = Class(name="Type")
types_PropertyReference = Class(name="types::PropertyReference")
types_Literal = Class(name="types::Literal")
types_DeclarationTypeReference = Class(name="types::DeclarationTypeReference")
types_PrimitiveType = Class(name="types::PrimitiveType")
NamedType = Class(name="NamedType")
types_EnumerationType = Class(name="types::EnumerationType")
ComplexType = Class(name="ComplexType")
types_EnumerationLiteral = Class(name="types::EnumerationLiteral")
types_EntityType = Class(name="types::EntityType")
types_Property = Class(name="types::Property")
types_EntityRelationship = Class(name="types::EntityRelationship")
types_MappedByReference = Class(name="types::MappedByReference")
types_StringLiteral = Class(name="types::StringLiteral")
Literal = Class(name="Literal")
types_CharLiteral = Class(name="types::CharLiteral")
types_NumberLiteral = Class(name="types::NumberLiteral")
types_BooleanLiteral = Class(name="types::BooleanLiteral")

# types_CollectionType class attributes and methods
types_CollectionType_size: Property = Property(name="size", type=IntegerType)
types_CollectionType.attributes={types_CollectionType_size}

# DeclarationTypeReference class attributes and methods

# types_TypeReference class attributes and methods

# types_MapType class attributes and methods
types_MapType_size: Property = Property(name="size", type=IntegerType)
types_MapType.attributes={types_MapType_size}

# types_Model class attributes and methods
types_Model_name: Property = Property(name="name", type=StringType)
types_Model.attributes={types_Model_name}

# types_Import class attributes and methods
types_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
types_Import.attributes={types_Import_importedNamespace}

# types_ComplexType class attributes and methods

# types_Type class attributes and methods

# types_NamedType class attributes and methods
types_NamedType_name: Property = Property(name="name", type=StringType)
types_NamedType.attributes={types_NamedType_name}

# Type class attributes and methods

# types_PropertyReference class attributes and methods

# types_Literal class attributes and methods

# types_DeclarationTypeReference class attributes and methods

# types_PrimitiveType class attributes and methods

# NamedType class attributes and methods

# types_EnumerationType class attributes and methods

# ComplexType class attributes and methods

# types_EnumerationLiteral class attributes and methods
types_EnumerationLiteral_name: Property = Property(name="name", type=StringType)
types_EnumerationLiteral.attributes={types_EnumerationLiteral_name}

# types_EntityType class attributes and methods
types_EntityType_storageModifier: Property = Property(name="storageModifier", type=StringType)
types_EntityType.attributes={types_EntityType_storageModifier}

# types_Property class attributes and methods
types_Property_storageModifier: Property = Property(name="storageModifier", type=StringType)
types_Property_name: Property = Property(name="name", type=StringType)
types_Property.attributes={types_Property_storageModifier, types_Property_name}

# types_EntityRelationship class attributes and methods
types_EntityRelationship_kind: Property = Property(name="kind", type=StringType)
types_EntityRelationship.attributes={types_EntityRelationship_kind}

# types_MappedByReference class attributes and methods

# types_StringLiteral class attributes and methods
types_StringLiteral_value: Property = Property(name="value", type=StringType)
types_StringLiteral.attributes={types_StringLiteral_value}

# Literal class attributes and methods

# types_CharLiteral class attributes and methods
types_CharLiteral_value: Property = Property(name="value", type=StringType)
types_CharLiteral.attributes={types_CharLiteral_value}

# types_NumberLiteral class attributes and methods
types_NumberLiteral_value: Property = Property(name="value", type=StringType)
types_NumberLiteral.attributes={types_NumberLiteral_value}

# types_BooleanLiteral class attributes and methods
types_BooleanLiteral_value: Property = Property(name="value", type=BooleanType)
types_BooleanLiteral.attributes={types_BooleanLiteral_value}

# Relationships
reference3: BinaryAssociation = BinaryAssociation(
    name="reference3",
    ends={
        Property(name="types_TypeReference", type=types_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_CollectionType", type=types_TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="types_Import", type=types_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Model", type=types_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types1: BinaryAssociation = BinaryAssociation(
    name="types1",
    ends={
        Property(name="types_ComplexType", type=types_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Model2", type=types_ComplexType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relationship18: BinaryAssociation = BinaryAssociation(
    name="relationship18",
    ends={
        Property(name="types_Property19", type=types_EntityRelationship, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="types_EntityRelationship", type=types_Property, multiplicity=Multiplicity(1, 1))
    }
)
orderBy20: BinaryAssociation = BinaryAssociation(
    name="orderBy20",
    ends={
        Property(name="types_PropertyReference", type=types_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Property21", type=types_PropertyReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mapKey22: BinaryAssociation = BinaryAssociation(
    name="mapKey22",
    ends={
        Property(name="types_PropertyReference24", type=types_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Property23", type=types_PropertyReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
literal25: BinaryAssociation = BinaryAssociation(
    name="literal25",
    ends={
        Property(name="types_Literal", type=types_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Property26", type=types_Literal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reference4: BinaryAssociation = BinaryAssociation(
    name="reference4",
    ends={
        Property(name="types_TypeReference5", type=types_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_MapType", type=types_TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mapType6: BinaryAssociation = BinaryAssociation(
    name="mapType6",
    ends={
        Property(name="types_TypeReference8", type=types_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_MapType7", type=types_TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reference9: BinaryAssociation = BinaryAssociation(
    name="reference9",
    ends={
        Property(name="types_NamedType", type=types_TypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="types_TypeReference10", type=types_NamedType, multiplicity=Multiplicity(0, 1))
    }
)
parent12: BinaryAssociation = BinaryAssociation(
    name="parent12",
    ends={
        Property(name="types_ComplexType13", type=types_ComplexType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_ComplexType11", type=types_ComplexType, multiplicity=Multiplicity(0, 1))
    }
)
literals14: BinaryAssociation = BinaryAssociation(
    name="literals14",
    ends={
        Property(name="types_EnumerationLiteral", type=types_EnumerationType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_EnumerationType", type=types_EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties15: BinaryAssociation = BinaryAssociation(
    name="properties15",
    ends={
        Property(name="types_Property", type=types_EntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_EntityType", type=types_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type16: BinaryAssociation = BinaryAssociation(
    name="type16",
    ends={
        Property(name="types_DeclarationTypeReference", type=types_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Property17", type=types_DeclarationTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mappedBy27: BinaryAssociation = BinaryAssociation(
    name="mappedBy27",
    ends={
        Property(name="types_MappedByReference", type=types_EntityRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="types_EntityRelationship28", type=types_MappedByReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base29: BinaryAssociation = BinaryAssociation(
    name="base29",
    ends={
        Property(name="types_Property31", type=types_MappedByReference, multiplicity=Multiplicity(1, 1)),
        Property(name="types_MappedByReference30", type=types_Property, multiplicity=Multiplicity(0, 1))
    }
)
path33: BinaryAssociation = BinaryAssociation(
    name="path33",
    ends={
        Property(name="types_MappedByReference34", type=types_MappedByReference, multiplicity=Multiplicity(1, 1)),
        Property(name="types_MappedByReference32", type=types_MappedByReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reference35: BinaryAssociation = BinaryAssociation(
    name="reference35",
    ends={
        Property(name="types_Property37", type=types_PropertyReference, multiplicity=Multiplicity(1, 1)),
        Property(name="types_PropertyReference36", type=types_Property, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_types_NamedType_Type = Generalization(general=Type, specific=types_NamedType)
gen_types_CollectionType_Type = Generalization(general=Type, specific=types_CollectionType)
gen_types_CollectionType_DeclarationTypeReference = Generalization(general=DeclarationTypeReference, specific=types_CollectionType)
gen_types_MapType_Type = Generalization(general=Type, specific=types_MapType)
gen_types_MapType_DeclarationTypeReference = Generalization(general=DeclarationTypeReference, specific=types_MapType)
gen_types_TypeReference_DeclarationTypeReference = Generalization(general=DeclarationTypeReference, specific=types_TypeReference)
gen_types_PrimitiveType_NamedType = Generalization(general=NamedType, specific=types_PrimitiveType)
gen_types_ComplexType_NamedType = Generalization(general=NamedType, specific=types_ComplexType)
gen_types_EnumerationType_ComplexType = Generalization(general=ComplexType, specific=types_EnumerationType)
gen_types_EntityType_ComplexType = Generalization(general=ComplexType, specific=types_EntityType)
gen_types_StringLiteral_Literal = Generalization(general=Literal, specific=types_StringLiteral)
gen_types_CharLiteral_Literal = Generalization(general=Literal, specific=types_CharLiteral)
gen_types_NumberLiteral_Literal = Generalization(general=Literal, specific=types_NumberLiteral)
gen_types_BooleanLiteral_Literal = Generalization(general=Literal, specific=types_BooleanLiteral)
gen_types_PropertyReference_Literal = Generalization(general=Literal, specific=types_PropertyReference)

# Domain Model
domain_model = DomainModel(
    name="types",
    types={types_CollectionType, DeclarationTypeReference, types_TypeReference, types_MapType, types_Model, types_Import, types_ComplexType, types_Type, types_NamedType, Type, types_PropertyReference, types_Literal, types_DeclarationTypeReference, types_PrimitiveType, NamedType, types_EnumerationType, ComplexType, types_EnumerationLiteral, types_EntityType, types_Property, types_EntityRelationship, types_MappedByReference, types_StringLiteral, Literal, types_CharLiteral, types_NumberLiteral, types_BooleanLiteral, TypeStorageModifier, EntityRelationshipKind, PropertyStorageModifier},
    associations={reference3, imports0, types1, relationship18, orderBy20, mapKey22, literal25, reference4, mapType6, reference9, parent12, literals14, properties15, type16, mappedBy27, base29, path33, reference35},
    generalizations={gen_types_NamedType_Type, gen_types_CollectionType_Type, gen_types_CollectionType_DeclarationTypeReference, gen_types_MapType_Type, gen_types_MapType_DeclarationTypeReference, gen_types_TypeReference_DeclarationTypeReference, gen_types_PrimitiveType_NamedType, gen_types_ComplexType_NamedType, gen_types_EnumerationType_ComplexType, gen_types_EntityType_ComplexType, gen_types_StringLiteral_Literal, gen_types_CharLiteral_Literal, gen_types_NumberLiteral_Literal, gen_types_BooleanLiteral_Literal, gen_types_PropertyReference_Literal},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)