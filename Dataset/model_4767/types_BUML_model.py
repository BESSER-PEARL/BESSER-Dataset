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
types_Type = Class(name="types::Type", is_abstract=True)
types_PrimitiveType = Class(name="types::PrimitiveType", is_abstract=True)
types_BooleanType = Class(name="types::BooleanType")
PrimitiveType = Class(name="PrimitiveType")
types_Metaclass = Class(name="types::Metaclass")
types_IntegerType = Class(name="types::IntegerType")
types_StringType = Class(name="types::StringType")
types_FloatType = Class(name="types::FloatType")
types_TupleType = Class(name="types::TupleType")
types_TupleAttribute = Class(name="types::TupleAttribute")
types_MapType = Class(name="types::MapType")
types_RefType = Class(name="types::RefType")
types_Unknown = Class(name="types::Unknown")
RefType = Class(name="RefType")
types_EmptyCollectionType = Class(name="types::EmptyCollectionType")
types_TypeError = Class(name="types::TypeError")
types_EObject = Class(name="types::EObject")
types_UnresolvedTypeError = Class(name="types::UnresolvedTypeError")
TypeError = Class(name="TypeError")
Metaclass = Class(name="Metaclass")
types_UnknownFeature = Class(name="types::UnknownFeature")
EStructuralFeature = Class(name="EStructuralFeature")
types_EClass = Class(name="types::EClass")
types_EmptyCollection = Class(name="types::EmptyCollection")
types_EnumType = Class(name="types::EnumType")
types_OclUndefinedType = Class(name="types::OclUndefinedType")
Type = Class(name="Type")
types_ReflectiveType = Class(name="types::ReflectiveType", is_abstract=True)
types_UnionType = Class(name="types::UnionType")
types_ThisModuleType = Class(name="types::ThisModuleType")
types_ReflectiveClass = Class(name="types::ReflectiveClass")
ReflectiveType = Class(name="ReflectiveType")
types_CollectionType = Class(name="types::CollectionType", is_abstract=True)
types_SequenceType = Class(name="types::SequenceType")
CollectionType = Class(name="CollectionType")
types_BagType = Class(name="types::BagType")
types_SetType = Class(name="types::SetType")
types_OrderedSetType = Class(name="types::OrderedSetType")
types_MetaModel = Class(name="types::MetaModel")

# types_Type class attributes and methods
types_Type_multivalued: Property = Property(name="multivalued", type=BooleanType)
types_Type_metamodelRef: Property = Property(name="metamodelRef", type=StringType)
types_Type_mayBeUndefined: Property = Property(name="mayBeUndefined", type=BooleanType)
types_Type.attributes={types_Type_mayBeUndefined, types_Type_multivalued, types_Type_metamodelRef}

# types_PrimitiveType class attributes and methods

# types_BooleanType class attributes and methods

# PrimitiveType class attributes and methods

# types_Metaclass class attributes and methods
types_Metaclass_name: Property = Property(name="name", type=StringType)
types_Metaclass_explicitOcurrence: Property = Property(name="explicitOcurrence", type=BooleanType)
types_Metaclass.attributes={types_Metaclass_explicitOcurrence, types_Metaclass_name}

# types_IntegerType class attributes and methods

# types_StringType class attributes and methods

# types_FloatType class attributes and methods

# types_TupleType class attributes and methods

# types_TupleAttribute class attributes and methods
types_TupleAttribute_name: Property = Property(name="name", type=StringType)
types_TupleAttribute.attributes={types_TupleAttribute_name}

# types_MapType class attributes and methods

# types_RefType class attributes and methods

# types_Unknown class attributes and methods

# RefType class attributes and methods

# types_EmptyCollectionType class attributes and methods

# types_TypeError class attributes and methods

# types_EObject class attributes and methods

# types_UnresolvedTypeError class attributes and methods

# TypeError class attributes and methods

# Metaclass class attributes and methods

# types_UnknownFeature class attributes and methods

# EStructuralFeature class attributes and methods

# types_EClass class attributes and methods

# types_EmptyCollection class attributes and methods

# types_EnumType class attributes and methods
types_EnumType_name: Property = Property(name="name", type=StringType)
types_EnumType.attributes={types_EnumType_name}

# types_OclUndefinedType class attributes and methods

# Type class attributes and methods

# types_ReflectiveType class attributes and methods

# types_UnionType class attributes and methods

# types_ThisModuleType class attributes and methods

# types_ReflectiveClass class attributes and methods

# ReflectiveType class attributes and methods

# types_CollectionType class attributes and methods

# types_SequenceType class attributes and methods

# CollectionType class attributes and methods

# types_BagType class attributes and methods

# types_SetType class attributes and methods

# types_OrderedSetType class attributes and methods

# types_MetaModel class attributes and methods
types_MetaModel_name: Property = Property(name="name", type=StringType)
types_MetaModel.attributes={types_MetaModel_name}

# Relationships
kindOfTypes2: BinaryAssociation = BinaryAssociation(
    name="kindOfTypes2",
    ends={
        Property(name="types_Metaclass", type=types_BooleanType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_BooleanType", type=types_Metaclass, multiplicity=Multiplicity(0, 9999))
    }
)
attributes3: BinaryAssociation = BinaryAssociation(
    name="attributes3",
    ends={
        Property(name="types_TupleAttribute", type=types_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_TupleType", type=types_TupleAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyType4: BinaryAssociation = BinaryAssociation(
    name="keyType4",
    ends={
        Property(name="types_Type5", type=types_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_MapType", type=types_Type, multiplicity=Multiplicity(1, 1))
    }
)
valueType6: BinaryAssociation = BinaryAssociation(
    name="valueType6",
    ends={
        Property(name="types_Type8", type=types_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_MapType7", type=types_Type, multiplicity=Multiplicity(1, 1))
    }
)
type9: BinaryAssociation = BinaryAssociation(
    name="type9",
    ends={
        Property(name="types_Type11", type=types_TupleAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="types_TupleAttribute10", type=types_Type, multiplicity=Multiplicity(1, 1))
    }
)
problem12: BinaryAssociation = BinaryAssociation(
    name="problem12",
    ends={
        Property(name="types_EObject", type=types_TypeError, multiplicity=Multiplicity(1, 1)),
        Property(name="types_TypeError", type=types_EObject, multiplicity=Multiplicity(0, 1))
    }
)
theContainingClass13: BinaryAssociation = BinaryAssociation(
    name="theContainingClass13",
    ends={
        Property(name="types_EClass", type=types_UnknownFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="types_UnknownFeature", type=types_EClass, multiplicity=Multiplicity(1, 1))
    }
)
noCastedType1: BinaryAssociation = BinaryAssociation(
    name="noCastedType1",
    ends={
        Property(name="types_Type", type=types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Type0", type=types_Type, multiplicity=Multiplicity(1, 1))
    }
)
klass16: BinaryAssociation = BinaryAssociation(
    name="klass16",
    ends={
        Property(name="types_EClass18", type=types_Metaclass, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Metaclass17", type=types_EClass, multiplicity=Multiplicity(1, 1))
    }
)
model19: BinaryAssociation = BinaryAssociation(
    name="model19",
    ends={
        Property(name="types_MetaModel", type=types_Metaclass, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Metaclass20", type=types_MetaModel, multiplicity=Multiplicity(1, 1))
    }
)
possibleTypes21: BinaryAssociation = BinaryAssociation(
    name="possibleTypes21",
    ends={
        Property(name="types_Type22", type=types_UnionType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_UnionType", type=types_Type, multiplicity=Multiplicity(0, 9999))
    }
)
containedType23: BinaryAssociation = BinaryAssociation(
    name="containedType23",
    ends={
        Property(name="types_Type24", type=types_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_CollectionType", type=types_Type, multiplicity=Multiplicity(1, 1))
    }
)
eenum14: BinaryAssociation = BinaryAssociation(
    name="eenum14",
    ends={
        Property(name="types_EObject15", type=types_EnumType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_EnumType", type=types_EObject, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_types_PrimitiveType_Type = Generalization(general=Type, specific=types_PrimitiveType)
gen_types_BooleanType_PrimitiveType = Generalization(general=PrimitiveType, specific=types_BooleanType)
gen_types_IntegerType_PrimitiveType = Generalization(general=PrimitiveType, specific=types_IntegerType)
gen_types_StringType_PrimitiveType = Generalization(general=PrimitiveType, specific=types_StringType)
gen_types_FloatType_PrimitiveType = Generalization(general=PrimitiveType, specific=types_FloatType)
gen_types_TupleType_Type = Generalization(general=Type, specific=types_TupleType)
gen_types_MapType_Type = Generalization(general=Type, specific=types_MapType)
gen_types_RefType_Type = Generalization(general=Type, specific=types_RefType)
gen_types_Unknown_RefType = Generalization(general=RefType, specific=types_Unknown)
gen_types_EmptyCollectionType_Type = Generalization(general=Type, specific=types_EmptyCollectionType)
gen_types_TypeError_Type = Generalization(general=Type, specific=types_TypeError)
gen_types_UnresolvedTypeError_TypeError = Generalization(general=TypeError, specific=types_UnresolvedTypeError)
gen_types_UnresolvedTypeError_Metaclass = Generalization(general=Metaclass, specific=types_UnresolvedTypeError)
gen_types_UnknownFeature_EStructuralFeature = Generalization(general=EStructuralFeature, specific=types_UnknownFeature)
gen_types_EmptyCollection_Type = Generalization(general=Type, specific=types_EmptyCollection)
gen_types_EnumType_Type = Generalization(general=Type, specific=types_EnumType)
gen_types_OclUndefinedType_Type = Generalization(general=Type, specific=types_OclUndefinedType)
gen_types_Metaclass_RefType = Generalization(general=RefType, specific=types_Metaclass)
gen_types_ReflectiveType_Type = Generalization(general=Type, specific=types_ReflectiveType)
gen_types_UnionType_Type = Generalization(general=Type, specific=types_UnionType)
gen_types_ThisModuleType_Type = Generalization(general=Type, specific=types_ThisModuleType)
gen_types_ReflectiveClass_ReflectiveType = Generalization(general=ReflectiveType, specific=types_ReflectiveClass)
gen_types_CollectionType_Type = Generalization(general=Type, specific=types_CollectionType)
gen_types_SequenceType_CollectionType = Generalization(general=CollectionType, specific=types_SequenceType)
gen_types_BagType_CollectionType = Generalization(general=CollectionType, specific=types_BagType)
gen_types_SetType_CollectionType = Generalization(general=CollectionType, specific=types_SetType)
gen_types_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=types_OrderedSetType)

# Domain Model
domain_model = DomainModel(
    name="types",
    types={types_Type, types_PrimitiveType, types_BooleanType, PrimitiveType, types_Metaclass, types_IntegerType, types_StringType, types_FloatType, types_TupleType, types_TupleAttribute, types_MapType, types_RefType, types_Unknown, RefType, types_EmptyCollectionType, types_TypeError, types_EObject, types_UnresolvedTypeError, TypeError, Metaclass, types_UnknownFeature, EStructuralFeature, types_EClass, types_EmptyCollection, types_EnumType, types_OclUndefinedType, Type, types_ReflectiveType, types_UnionType, types_ThisModuleType, types_ReflectiveClass, ReflectiveType, types_CollectionType, types_SequenceType, CollectionType, types_BagType, types_SetType, types_OrderedSetType, types_MetaModel},
    associations={kindOfTypes2, attributes3, keyType4, valueType6, type9, problem12, theContainingClass13, noCastedType1, klass16, model19, possibleTypes21, containedType23, eenum14},
    generalizations={gen_types_PrimitiveType_Type, gen_types_BooleanType_PrimitiveType, gen_types_IntegerType_PrimitiveType, gen_types_StringType_PrimitiveType, gen_types_FloatType_PrimitiveType, gen_types_TupleType_Type, gen_types_MapType_Type, gen_types_RefType_Type, gen_types_Unknown_RefType, gen_types_EmptyCollectionType_Type, gen_types_TypeError_Type, gen_types_UnresolvedTypeError_TypeError, gen_types_UnresolvedTypeError_Metaclass, gen_types_UnknownFeature_EStructuralFeature, gen_types_EmptyCollection_Type, gen_types_EnumType_Type, gen_types_OclUndefinedType_Type, gen_types_Metaclass_RefType, gen_types_ReflectiveType_Type, gen_types_UnionType_Type, gen_types_ThisModuleType_Type, gen_types_ReflectiveClass_ReflectiveType, gen_types_CollectionType_Type, gen_types_SequenceType_CollectionType, gen_types_BagType_CollectionType, gen_types_SetType_CollectionType, gen_types_OrderedSetType_CollectionType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)