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
atl_types_TupleAttribute = Class(name="atl::types::TupleAttribute")
atl_types_MapType = Class(name="atl::types::MapType")
atl_types_RefType = Class(name="atl::types::RefType")
atl_types_Unknown = Class(name="atl::types::Unknown")
RefType = Class(name="RefType")
atl_types_EmptyCollection = Class(name="atl::types::EmptyCollection")
atl_types_EnumType = Class(name="atl::types::EnumType")
atl_types_EObject = Class(name="atl::types::EObject")
atl_types_Metaclass = Class(name="atl::types::Metaclass")
atl_types_EClass = Class(name="atl::types::EClass")
atl_types_ReflectiveType = Class(name="atl::types::ReflectiveType", is_abstract=True)
atl_types_UnionType = Class(name="atl::types::UnionType")
atl_types_Type = Class(name="atl::types::Type", is_abstract=True)
atl_types_PrimitiveType = Class(name="atl::types::PrimitiveType", is_abstract=True)
Type = Class(name="Type")
atl_types_BooleanType = Class(name="atl::types::BooleanType")
PrimitiveType = Class(name="PrimitiveType")
atl_types_IntegerType = Class(name="atl::types::IntegerType")
atl_types_StringType = Class(name="atl::types::StringType")
atl_types_FloatType = Class(name="atl::types::FloatType")
atl_types_TupleType = Class(name="atl::types::TupleType")
atl_types_annotations_ExpressionAnnotation = Class(name="atl::types::annotations::ExpressionAnnotation")
atl_types_ThisModuleType = Class(name="atl::types::ThisModuleType")
atl_types_ReflectiveClass = Class(name="atl::types::ReflectiveClass")
ReflectiveType = Class(name="ReflectiveType")
atl_types_annotations_AtlAnnotation = Class(name="atl::types::annotations::AtlAnnotation", is_abstract=True)
atl_types_annotations_HelperAnnotation = Class(name="atl::types::annotations::HelperAnnotation")
AtlAnnotation = Class(name="AtlAnnotation")
annotations_atl_types_EObject = Class(name="annotations::atl::types::EObject")
annotations_atl_types_Type = Class(name="annotations::atl::types::Type")
atl_types_annotations_BindingAnnotation = Class(name="atl::types::annotations::BindingAnnotation")

# atl_types_TupleAttribute class attributes and methods
atl_types_TupleAttribute_name: Property = Property(name="name", type=StringType)
atl_types_TupleAttribute.attributes={atl_types_TupleAttribute_name}

# atl_types_MapType class attributes and methods

# atl_types_RefType class attributes and methods

# atl_types_Unknown class attributes and methods

# RefType class attributes and methods

# atl_types_EmptyCollection class attributes and methods

# atl_types_EnumType class attributes and methods
atl_types_EnumType_name: Property = Property(name="name", type=StringType)
atl_types_EnumType.attributes={atl_types_EnumType_name}

# atl_types_EObject class attributes and methods

# atl_types_Metaclass class attributes and methods
atl_types_Metaclass_name: Property = Property(name="name", type=StringType)
atl_types_Metaclass.attributes={atl_types_Metaclass_name}

# atl_types_EClass class attributes and methods

# atl_types_ReflectiveType class attributes and methods

# atl_types_UnionType class attributes and methods

# atl_types_Type class attributes and methods
atl_types_Type_multivalued: Property = Property(name="multivalued", type=BooleanType)
atl_types_Type.attributes={atl_types_Type_multivalued}

# atl_types_PrimitiveType class attributes and methods

# Type class attributes and methods

# atl_types_BooleanType class attributes and methods

# PrimitiveType class attributes and methods

# atl_types_IntegerType class attributes and methods

# atl_types_StringType class attributes and methods

# atl_types_FloatType class attributes and methods

# atl_types_TupleType class attributes and methods

# atl_types_annotations_ExpressionAnnotation class attributes and methods

# atl_types_ThisModuleType class attributes and methods

# atl_types_ReflectiveClass class attributes and methods

# ReflectiveType class attributes and methods

# atl_types_annotations_AtlAnnotation class attributes and methods

# atl_types_annotations_HelperAnnotation class attributes and methods
atl_types_annotations_HelperAnnotation_name: Property = Property(name="name", type=StringType)
atl_types_annotations_HelperAnnotation.attributes={atl_types_annotations_HelperAnnotation_name}

# AtlAnnotation class attributes and methods

# annotations_atl_types_EObject class attributes and methods

# annotations_atl_types_Type class attributes and methods

# atl_types_annotations_BindingAnnotation class attributes and methods
atl_types_annotations_BindingAnnotation_name: Property = Property(name="name", type=StringType)
atl_types_annotations_BindingAnnotation.attributes={atl_types_annotations_BindingAnnotation_name}

# Relationships
attributes0: BinaryAssociation = BinaryAssociation(
    name="attributes0",
    ends={
        Property(name="atl_types_TupleAttribute", type=atl_types_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_types_TupleType", type=atl_types_TupleAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyType1: BinaryAssociation = BinaryAssociation(
    name="keyType1",
    ends={
        Property(name="atl_types_Type", type=atl_types_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_types_MapType", type=atl_types_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
valueType2: BinaryAssociation = BinaryAssociation(
    name="valueType2",
    ends={
        Property(name="atl_types_Type4", type=atl_types_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_types_MapType3", type=atl_types_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type5: BinaryAssociation = BinaryAssociation(
    name="type5",
    ends={
        Property(name="atl_types_Type7", type=atl_types_TupleAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_types_TupleAttribute6", type=atl_types_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
eenum8: BinaryAssociation = BinaryAssociation(
    name="eenum8",
    ends={
        Property(name="atl_types_EObject", type=atl_types_EnumType, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_types_EnumType", type=atl_types_EObject, multiplicity=Multiplicity(1, 1))
    }
)
klass9: BinaryAssociation = BinaryAssociation(
    name="klass9",
    ends={
        Property(name="atl_types_EClass", type=atl_types_Metaclass, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_types_Metaclass", type=atl_types_EClass, multiplicity=Multiplicity(1, 1))
    }
)
rule15: BinaryAssociation = BinaryAssociation(
    name="rule15",
    ends={
        Property(name="annotations_atl_types_EObject16", type=atl_types_annotations_BindingAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_types_annotations_BindingAnnotation", type=annotations_atl_types_EObject, multiplicity=Multiplicity(0, 1))
    }
)
binding17: BinaryAssociation = BinaryAssociation(
    name="binding17",
    ends={
        Property(name="annotations_atl_types_EObject19", type=atl_types_annotations_BindingAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_types_annotations_BindingAnnotation18", type=annotations_atl_types_EObject, multiplicity=Multiplicity(0, 1))
    }
)
sourceType20: BinaryAssociation = BinaryAssociation(
    name="sourceType20",
    ends={
        Property(name="annotations_atl_types_Type22", type=atl_types_annotations_BindingAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_types_annotations_BindingAnnotation21", type=annotations_atl_types_Type, multiplicity=Multiplicity(1, 1))
    }
)
targetType23: BinaryAssociation = BinaryAssociation(
    name="targetType23",
    ends={
        Property(name="annotations_atl_types_Type25", type=atl_types_annotations_BindingAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_types_annotations_BindingAnnotation24", type=annotations_atl_types_Type, multiplicity=Multiplicity(1, 1))
    }
)
expr26: BinaryAssociation = BinaryAssociation(
    name="expr26",
    ends={
        Property(name="annotations_atl_types_EObject27", type=atl_types_annotations_ExpressionAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_types_annotations_ExpressionAnnotation", type=annotations_atl_types_EObject, multiplicity=Multiplicity(0, 1))
    }
)
type28: BinaryAssociation = BinaryAssociation(
    name="type28",
    ends={
        Property(name="annotations_atl_types_Type30", type=atl_types_annotations_ExpressionAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_types_annotations_ExpressionAnnotation29", type=annotations_atl_types_Type, multiplicity=Multiplicity(1, 1))
    }
)
possibleTypes10: BinaryAssociation = BinaryAssociation(
    name="possibleTypes10",
    ends={
        Property(name="atl_types_Type11", type=atl_types_UnionType, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_types_UnionType", type=atl_types_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
helper12: BinaryAssociation = BinaryAssociation(
    name="helper12",
    ends={
        Property(name="annotations_atl_types_EObject", type=atl_types_annotations_HelperAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_types_annotations_HelperAnnotation", type=annotations_atl_types_EObject, multiplicity=Multiplicity(0, 1))
    }
)
type13: BinaryAssociation = BinaryAssociation(
    name="type13",
    ends={
        Property(name="annotations_atl_types_Type", type=atl_types_annotations_HelperAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_types_annotations_HelperAnnotation14", type=annotations_atl_types_Type, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_atl_types_MapType_Type = Generalization(general=Type, specific=atl_types_MapType)
gen_atl_types_RefType_Type = Generalization(general=Type, specific=atl_types_RefType)
gen_atl_types_Unknown_RefType = Generalization(general=RefType, specific=atl_types_Unknown)
gen_atl_types_EmptyCollection_Type = Generalization(general=Type, specific=atl_types_EmptyCollection)
gen_atl_types_EnumType_Type = Generalization(general=Type, specific=atl_types_EnumType)
gen_atl_types_Metaclass_RefType = Generalization(general=RefType, specific=atl_types_Metaclass)
gen_atl_types_ReflectiveType_Type = Generalization(general=Type, specific=atl_types_ReflectiveType)
gen_atl_types_UnionType_Type = Generalization(general=Type, specific=atl_types_UnionType)
gen_atl_types_PrimitiveType_Type = Generalization(general=Type, specific=atl_types_PrimitiveType)
gen_atl_types_BooleanType_PrimitiveType = Generalization(general=PrimitiveType, specific=atl_types_BooleanType)
gen_atl_types_IntegerType_PrimitiveType = Generalization(general=PrimitiveType, specific=atl_types_IntegerType)
gen_atl_types_StringType_PrimitiveType = Generalization(general=PrimitiveType, specific=atl_types_StringType)
gen_atl_types_FloatType_PrimitiveType = Generalization(general=PrimitiveType, specific=atl_types_FloatType)
gen_atl_types_TupleType_Type = Generalization(general=Type, specific=atl_types_TupleType)
gen_atl_types_annotations_BindingAnnotation_AtlAnnotation = Generalization(general=AtlAnnotation, specific=atl_types_annotations_BindingAnnotation)
gen_atl_types_annotations_ExpressionAnnotation_AtlAnnotation = Generalization(general=AtlAnnotation, specific=atl_types_annotations_ExpressionAnnotation)
gen_atl_types_ThisModuleType_Type = Generalization(general=Type, specific=atl_types_ThisModuleType)
gen_atl_types_ReflectiveClass_ReflectiveType = Generalization(general=ReflectiveType, specific=atl_types_ReflectiveClass)
gen_atl_types_annotations_HelperAnnotation_AtlAnnotation = Generalization(general=AtlAnnotation, specific=atl_types_annotations_HelperAnnotation)

# Domain Model
domain_model = DomainModel(
    name="atl_types",
    types={atl_types_TupleAttribute, atl_types_MapType, atl_types_RefType, atl_types_Unknown, RefType, atl_types_EmptyCollection, atl_types_EnumType, atl_types_EObject, atl_types_Metaclass, atl_types_EClass, atl_types_ReflectiveType, atl_types_UnionType, atl_types_Type, atl_types_PrimitiveType, Type, atl_types_BooleanType, PrimitiveType, atl_types_IntegerType, atl_types_StringType, atl_types_FloatType, atl_types_TupleType, atl_types_annotations_ExpressionAnnotation, atl_types_ThisModuleType, atl_types_ReflectiveClass, ReflectiveType, atl_types_annotations_AtlAnnotation, atl_types_annotations_HelperAnnotation, AtlAnnotation, annotations_atl_types_EObject, annotations_atl_types_Type, atl_types_annotations_BindingAnnotation},
    associations={attributes0, keyType1, valueType2, type5, eenum8, klass9, rule15, binding17, sourceType20, targetType23, expr26, type28, possibleTypes10, helper12, type13},
    generalizations={gen_atl_types_MapType_Type, gen_atl_types_RefType_Type, gen_atl_types_Unknown_RefType, gen_atl_types_EmptyCollection_Type, gen_atl_types_EnumType_Type, gen_atl_types_Metaclass_RefType, gen_atl_types_ReflectiveType_Type, gen_atl_types_UnionType_Type, gen_atl_types_PrimitiveType_Type, gen_atl_types_BooleanType_PrimitiveType, gen_atl_types_IntegerType_PrimitiveType, gen_atl_types_StringType_PrimitiveType, gen_atl_types_FloatType_PrimitiveType, gen_atl_types_TupleType_Type, gen_atl_types_annotations_BindingAnnotation_AtlAnnotation, gen_atl_types_annotations_ExpressionAnnotation_AtlAnnotation, gen_atl_types_ThisModuleType_Type, gen_atl_types_ReflectiveClass_ReflectiveType, gen_atl_types_annotations_HelperAnnotation_AtlAnnotation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)