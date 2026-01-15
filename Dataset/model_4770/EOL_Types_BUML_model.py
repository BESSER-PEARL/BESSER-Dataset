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
eol_types_Type = Class(name="eol::types::Type")
eol_types_AnyType = Class(name="eol::types::AnyType")
Type = Class(name="Type")
eol_types_ModelType = Class(name="eol::types::ModelType")
AnyType = Class(name="AnyType")
eol_types_ModelElementType = Class(name="eol::types::ModelElementType")
eol_types_PseudoType = Class(name="eol::types::PseudoType", is_abstract=True)
eol_types_SelfType = Class(name="eol::types::SelfType")
PseudoType = Class(name="PseudoType")
eol_types_SelfContentType = Class(name="eol::types::SelfContentType")
eol_types_MapType = Class(name="eol::types::MapType")
UniqueCollectionType = Class(name="UniqueCollectionType")
eol_types_OrderedSetType = Class(name="eol::types::OrderedSetType")
OrderedCollectionType = Class(name="OrderedCollectionType")
eol_types_SequenceType = Class(name="eol::types::SequenceType")
eol_types_PrimitiveType = Class(name="eol::types::PrimitiveType", is_abstract=True)
eol_types_BooleanType = Class(name="eol::types::BooleanType")
PrimitiveType = Class(name="PrimitiveType")
eol_types_RealType = Class(name="eol::types::RealType")
eol_types_IntegerType = Class(name="eol::types::IntegerType")
RealType = Class(name="RealType")
eol_types_StringType = Class(name="eol::types::StringType")
eol_types_NativeType = Class(name="eol::types::NativeType")
eol_types_VoidType = Class(name="eol::types::VoidType")
eol_types_InvalidType = Class(name="eol::types::InvalidType")
eol_types_CollectionType = Class(name="eol::types::CollectionType")
eol_types_BagType = Class(name="eol::types::BagType")
CollectionType = Class(name="CollectionType")
eol_types_OrderedCollectionType = Class(name="eol::types::OrderedCollectionType", is_abstract=True)
eol_types_UniqueCollectionType = Class(name="eol::types::UniqueCollectionType", is_abstract=True)
eol_types_SetType = Class(name="eol::types::SetType")

# eol_types_Type class attributes and methods

# eol_types_AnyType class attributes and methods
eol_types_AnyType_declared: Property = Property(name="declared", type=BooleanType)
eol_types_AnyType.attributes={eol_types_AnyType_declared}

# Type class attributes and methods

# eol_types_ModelType class attributes and methods
eol_types_ModelType_modelName: Property = Property(name="modelName", type=StringType)
eol_types_ModelType.attributes={eol_types_ModelType_modelName}

# AnyType class attributes and methods

# eol_types_ModelElementType class attributes and methods
eol_types_ModelElementType_modelName: Property = Property(name="modelName", type=StringType)
eol_types_ModelElementType_elementName: Property = Property(name="elementName", type=StringType)
eol_types_ModelElementType.attributes={eol_types_ModelElementType_modelName, eol_types_ModelElementType_elementName}

# eol_types_PseudoType class attributes and methods

# eol_types_SelfType class attributes and methods

# PseudoType class attributes and methods

# eol_types_SelfContentType class attributes and methods

# eol_types_MapType class attributes and methods

# UniqueCollectionType class attributes and methods

# eol_types_OrderedSetType class attributes and methods

# OrderedCollectionType class attributes and methods

# eol_types_SequenceType class attributes and methods

# eol_types_PrimitiveType class attributes and methods

# eol_types_BooleanType class attributes and methods

# PrimitiveType class attributes and methods

# eol_types_RealType class attributes and methods

# eol_types_IntegerType class attributes and methods

# RealType class attributes and methods

# eol_types_StringType class attributes and methods

# eol_types_NativeType class attributes and methods
eol_types_NativeType_value: Property = Property(name="value", type=StringType)
eol_types_NativeType.attributes={eol_types_NativeType_value}

# eol_types_VoidType class attributes and methods

# eol_types_InvalidType class attributes and methods

# eol_types_CollectionType class attributes and methods

# eol_types_BagType class attributes and methods

# CollectionType class attributes and methods

# eol_types_OrderedCollectionType class attributes and methods

# eol_types_UniqueCollectionType class attributes and methods

# eol_types_SetType class attributes and methods

# Relationships
dynamicType0: BinaryAssociation = BinaryAssociation(
    name="dynamicType0",
    ends={
        Property(name="eol_types_Type", type=eol_types_AnyType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_types_AnyType", type=eol_types_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyType1: BinaryAssociation = BinaryAssociation(
    name="keyType1",
    ends={
        Property(name="eol_types_AnyType2", type=eol_types_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_types_MapType", type=eol_types_AnyType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
valueType3: BinaryAssociation = BinaryAssociation(
    name="valueType3",
    ends={
        Property(name="eol_types_AnyType5", type=eol_types_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_types_MapType4", type=eol_types_AnyType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contentType6: BinaryAssociation = BinaryAssociation(
    name="contentType6",
    ends={
        Property(name="eol_types_Type7", type=eol_types_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_types_CollectionType", type=eol_types_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_eol_types_AnyType_Type = Generalization(general=Type, specific=eol_types_AnyType)
gen_eol_types_ModelType_AnyType = Generalization(general=AnyType, specific=eol_types_ModelType)
gen_eol_types_ModelElementType_AnyType = Generalization(general=AnyType, specific=eol_types_ModelElementType)
gen_eol_types_PseudoType_AnyType = Generalization(general=AnyType, specific=eol_types_PseudoType)
gen_eol_types_SelfType_PseudoType = Generalization(general=PseudoType, specific=eol_types_SelfType)
gen_eol_types_SelfContentType_PseudoType = Generalization(general=PseudoType, specific=eol_types_SelfContentType)
gen_eol_types_MapType_AnyType = Generalization(general=AnyType, specific=eol_types_MapType)
gen_eol_types_SetType_UniqueCollectionType = Generalization(general=UniqueCollectionType, specific=eol_types_SetType)
gen_eol_types_OrderedSetType_UniqueCollectionType = Generalization(general=UniqueCollectionType, specific=eol_types_OrderedSetType)
gen_eol_types_OrderedSetType_OrderedCollectionType = Generalization(general=OrderedCollectionType, specific=eol_types_OrderedSetType)
gen_eol_types_SequenceType_OrderedCollectionType = Generalization(general=OrderedCollectionType, specific=eol_types_SequenceType)
gen_eol_types_PrimitiveType_AnyType = Generalization(general=AnyType, specific=eol_types_PrimitiveType)
gen_eol_types_BooleanType_PrimitiveType = Generalization(general=PrimitiveType, specific=eol_types_BooleanType)
gen_eol_types_RealType_PrimitiveType = Generalization(general=PrimitiveType, specific=eol_types_RealType)
gen_eol_types_IntegerType_RealType = Generalization(general=RealType, specific=eol_types_IntegerType)
gen_eol_types_StringType_PrimitiveType = Generalization(general=PrimitiveType, specific=eol_types_StringType)
gen_eol_types_NativeType_AnyType = Generalization(general=AnyType, specific=eol_types_NativeType)
gen_eol_types_VoidType_AnyType = Generalization(general=AnyType, specific=eol_types_VoidType)
gen_eol_types_InvalidType_AnyType = Generalization(general=AnyType, specific=eol_types_InvalidType)
gen_eol_types_CollectionType_AnyType = Generalization(general=AnyType, specific=eol_types_CollectionType)
gen_eol_types_BagType_CollectionType = Generalization(general=CollectionType, specific=eol_types_BagType)
gen_eol_types_OrderedCollectionType_CollectionType = Generalization(general=CollectionType, specific=eol_types_OrderedCollectionType)
gen_eol_types_UniqueCollectionType_CollectionType = Generalization(general=CollectionType, specific=eol_types_UniqueCollectionType)

# Domain Model
domain_model = DomainModel(
    name="eol_types",
    types={eol_types_Type, eol_types_AnyType, Type, eol_types_ModelType, AnyType, eol_types_ModelElementType, eol_types_PseudoType, eol_types_SelfType, PseudoType, eol_types_SelfContentType, eol_types_MapType, UniqueCollectionType, eol_types_OrderedSetType, OrderedCollectionType, eol_types_SequenceType, eol_types_PrimitiveType, eol_types_BooleanType, PrimitiveType, eol_types_RealType, eol_types_IntegerType, RealType, eol_types_StringType, eol_types_NativeType, eol_types_VoidType, eol_types_InvalidType, eol_types_CollectionType, eol_types_BagType, CollectionType, eol_types_OrderedCollectionType, eol_types_UniqueCollectionType, eol_types_SetType},
    associations={dynamicType0, keyType1, valueType3, contentType6},
    generalizations={gen_eol_types_AnyType_Type, gen_eol_types_ModelType_AnyType, gen_eol_types_ModelElementType_AnyType, gen_eol_types_PseudoType_AnyType, gen_eol_types_SelfType_PseudoType, gen_eol_types_SelfContentType_PseudoType, gen_eol_types_MapType_AnyType, gen_eol_types_SetType_UniqueCollectionType, gen_eol_types_OrderedSetType_UniqueCollectionType, gen_eol_types_OrderedSetType_OrderedCollectionType, gen_eol_types_SequenceType_OrderedCollectionType, gen_eol_types_PrimitiveType_AnyType, gen_eol_types_BooleanType_PrimitiveType, gen_eol_types_RealType_PrimitiveType, gen_eol_types_IntegerType_RealType, gen_eol_types_StringType_PrimitiveType, gen_eol_types_NativeType_AnyType, gen_eol_types_VoidType_AnyType, gen_eol_types_InvalidType_AnyType, gen_eol_types_CollectionType_AnyType, gen_eol_types_BagType_CollectionType, gen_eol_types_OrderedCollectionType_CollectionType, gen_eol_types_UniqueCollectionType_CollectionType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)