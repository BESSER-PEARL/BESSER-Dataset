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
ocl_uml_AnyType = Class(name="ocl::uml::AnyType")
uml_ocl_Operation = Class(name="uml::ocl::Operation")
ocl_uml_VoidType = Class(name="ocl::uml::VoidType")
ocl_uml_InvalidType = Class(name="ocl::uml::InvalidType")
ocl_uml_ElementType = Class(name="ocl::uml::ElementType")
Classifier = Class(name="Classifier")
ocl_uml_MessageType = Class(name="ocl::uml::MessageType")
uml_ocl_Property = Class(name="uml::ocl::Property")
ocl_uml_PrimitiveType = Class(name="ocl::uml::PrimitiveType")
ocl_uml_CollectionType = Class(name="ocl::uml::CollectionType")
ocl_uml_TupleType = Class(name="ocl::uml::TupleType")
ocl_uml_BagType = Class(name="ocl::uml::BagType")
ocl_uml_SetType = Class(name="ocl::uml::SetType")
ocl_uml_OrderedSetType = Class(name="ocl::uml::OrderedSetType")
ocl_uml_SequenceType = Class(name="ocl::uml::SequenceType")
ocl_uml_ExpressionInOCL = Class(name="ocl::uml::ExpressionInOCL")
ocl_uml_AssociationClassCallExp = Class(name="ocl::uml::AssociationClassCallExp")
types_ElementType = Class(name="types::ElementType")
ocl_uml_TypeType = Class(name="ocl::uml::TypeType")
ocl_uml_FeatureCallExp = Class(name="ocl::uml::FeatureCallExp", is_abstract=True)
ocl_uml_CallExp = Class(name="ocl::uml::CallExp", is_abstract=True)
ocl_uml_OCLExpression = Class(name="ocl::uml::OCLExpression", is_abstract=True)
ocl_uml_BooleanLiteralExp = Class(name="ocl::uml::BooleanLiteralExp")
ocl_uml_PrimitiveLiteralExp = Class(name="ocl::uml::PrimitiveLiteralExp", is_abstract=True)
ocl_uml_LiteralExp = Class(name="ocl::uml::LiteralExp", is_abstract=True)
ocl_uml_CollectionItem = Class(name="ocl::uml::CollectionItem")
ocl_uml_CollectionLiteralPart = Class(name="ocl::uml::CollectionLiteralPart", is_abstract=True)
ocl_uml_CollectionLiteralExp = Class(name="ocl::uml::CollectionLiteralExp")
ocl_uml_CollectionRange = Class(name="ocl::uml::CollectionRange")
ocl_uml_EnumLiteralExp = Class(name="ocl::uml::EnumLiteralExp")
ocl_uml_IfExp = Class(name="ocl::uml::IfExp")
ocl_uml_IntegerLiteralExp = Class(name="ocl::uml::IntegerLiteralExp")
ocl_uml_UnspecifiedValueExp = Class(name="ocl::uml::UnspecifiedValueExp")
ocl_uml_UnlimitedNaturalLiteralExp = Class(name="ocl::uml::UnlimitedNaturalLiteralExp")
ocl_uml_NavigationCallExp = Class(name="ocl::uml::NavigationCallExp", is_abstract=True)
ocl_uml_InvalidLiteralExp = Class(name="ocl::uml::InvalidLiteralExp")
ocl_uml_IterateExp = Class(name="ocl::uml::IterateExp")
ocl_uml_LoopExp = Class(name="ocl::uml::LoopExp", is_abstract=True)
ocl_uml_IteratorExp = Class(name="ocl::uml::IteratorExp")
ocl_uml_LetExp = Class(name="ocl::uml::LetExp")
ocl_uml_MessageExp = Class(name="ocl::uml::MessageExp")
ocl_uml_NullLiteralExp = Class(name="ocl::uml::NullLiteralExp")
ocl_uml_OperationCallExp = Class(name="ocl::uml::OperationCallExp")
ocl_uml_PropertyCallExp = Class(name="ocl::uml::PropertyCallExp")
ocl_uml_RealLiteralExp = Class(name="ocl::uml::RealLiteralExp")
ocl_uml_StateExp = Class(name="ocl::uml::StateExp")
ocl_uml_StringLiteralExp = Class(name="ocl::uml::StringLiteralExp")
ocl_uml_TupleLiteralExp = Class(name="ocl::uml::TupleLiteralExp")
ocl_uml_TupleLiteralPart = Class(name="ocl::uml::TupleLiteralPart")
ocl_uml_TypeExp = Class(name="ocl::uml::TypeExp")
ocl_uml_NumericLiteralExp = Class(name="ocl::uml::NumericLiteralExp", is_abstract=True)
ocl_uml_Variable = Class(name="ocl::uml::Variable")
ocl_uml_VariableExp = Class(name="ocl::uml::VariableExp")
ocl_uml_TemplateParameterType = Class(name="ocl::uml::TemplateParameterType")

# ocl_uml_AnyType class attributes and methods

# uml_ocl_Operation class attributes and methods

# ocl_uml_VoidType class attributes and methods

# ocl_uml_InvalidType class attributes and methods

# ocl_uml_ElementType class attributes and methods

# Classifier class attributes and methods

# ocl_uml_MessageType class attributes and methods

# uml_ocl_Property class attributes and methods

# ocl_uml_PrimitiveType class attributes and methods

# ocl_uml_CollectionType class attributes and methods

# ocl_uml_TupleType class attributes and methods

# ocl_uml_BagType class attributes and methods

# ocl_uml_SetType class attributes and methods

# ocl_uml_OrderedSetType class attributes and methods

# ocl_uml_SequenceType class attributes and methods

# ocl_uml_ExpressionInOCL class attributes and methods

# ocl_uml_AssociationClassCallExp class attributes and methods

# types_ElementType class attributes and methods

# ocl_uml_TypeType class attributes and methods

# ocl_uml_FeatureCallExp class attributes and methods

# ocl_uml_CallExp class attributes and methods

# ocl_uml_OCLExpression class attributes and methods

# ocl_uml_BooleanLiteralExp class attributes and methods

# ocl_uml_PrimitiveLiteralExp class attributes and methods

# ocl_uml_LiteralExp class attributes and methods

# ocl_uml_CollectionItem class attributes and methods

# ocl_uml_CollectionLiteralPart class attributes and methods

# ocl_uml_CollectionLiteralExp class attributes and methods

# ocl_uml_CollectionRange class attributes and methods

# ocl_uml_EnumLiteralExp class attributes and methods

# ocl_uml_IfExp class attributes and methods

# ocl_uml_IntegerLiteralExp class attributes and methods

# ocl_uml_UnspecifiedValueExp class attributes and methods

# ocl_uml_UnlimitedNaturalLiteralExp class attributes and methods

# ocl_uml_NavigationCallExp class attributes and methods

# ocl_uml_InvalidLiteralExp class attributes and methods

# ocl_uml_IterateExp class attributes and methods

# ocl_uml_LoopExp class attributes and methods

# ocl_uml_IteratorExp class attributes and methods

# ocl_uml_LetExp class attributes and methods

# ocl_uml_MessageExp class attributes and methods

# ocl_uml_NullLiteralExp class attributes and methods

# ocl_uml_OperationCallExp class attributes and methods

# ocl_uml_PropertyCallExp class attributes and methods

# ocl_uml_RealLiteralExp class attributes and methods

# ocl_uml_StateExp class attributes and methods

# ocl_uml_StringLiteralExp class attributes and methods

# ocl_uml_TupleLiteralExp class attributes and methods

# ocl_uml_TupleLiteralPart class attributes and methods

# ocl_uml_TypeExp class attributes and methods

# ocl_uml_NumericLiteralExp class attributes and methods

# ocl_uml_Variable class attributes and methods

# ocl_uml_VariableExp class attributes and methods

# ocl_uml_TemplateParameterType class attributes and methods

# Relationships
ownedOperation0: BinaryAssociation = BinaryAssociation(
    name="ownedOperation0",
    ends={
        Property(name="uml_ocl_Operation", type=ocl_uml_AnyType, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_uml_AnyType", type=uml_ocl_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation1: BinaryAssociation = BinaryAssociation(
    name="ownedOperation1",
    ends={
        Property(name="uml_ocl_Operation2", type=ocl_uml_VoidType, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_uml_VoidType", type=uml_ocl_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation3: BinaryAssociation = BinaryAssociation(
    name="ownedOperation3",
    ends={
        Property(name="uml_ocl_Operation4", type=ocl_uml_InvalidType, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_uml_InvalidType", type=uml_ocl_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation5: BinaryAssociation = BinaryAssociation(
    name="ownedOperation5",
    ends={
        Property(name="uml_ocl_Operation6", type=ocl_uml_TypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_uml_TypeType", type=uml_ocl_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation7: BinaryAssociation = BinaryAssociation(
    name="ownedOperation7",
    ends={
        Property(name="uml_ocl_Operation8", type=ocl_uml_MessageType, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_uml_MessageType", type=uml_ocl_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute9: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute9",
    ends={
        Property(name="uml_ocl_Property", type=ocl_uml_MessageType, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_uml_MessageType10", type=uml_ocl_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation11: BinaryAssociation = BinaryAssociation(
    name="ownedOperation11",
    ends={
        Property(name="uml_ocl_Operation12", type=ocl_uml_TemplateParameterType, multiplicity=Multiplicity(1, 1)),
        Property(name="ocl_uml_TemplateParameterType", type=uml_ocl_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_ocl_uml_ElementType_Classifier = Generalization(general=Classifier, specific=ocl_uml_ElementType)
gen_ocl_uml_ElementType_types_ElementType = Generalization(general=types_ElementType, specific=ocl_uml_ElementType)

# Domain Model
domain_model = DomainModel(
    name="ocl",
    types={ocl_uml_AnyType, uml_ocl_Operation, ocl_uml_VoidType, ocl_uml_InvalidType, ocl_uml_ElementType, Classifier, ocl_uml_MessageType, uml_ocl_Property, ocl_uml_PrimitiveType, ocl_uml_CollectionType, ocl_uml_TupleType, ocl_uml_BagType, ocl_uml_SetType, ocl_uml_OrderedSetType, ocl_uml_SequenceType, ocl_uml_ExpressionInOCL, ocl_uml_AssociationClassCallExp, types_ElementType, ocl_uml_TypeType, ocl_uml_FeatureCallExp, ocl_uml_CallExp, ocl_uml_OCLExpression, ocl_uml_BooleanLiteralExp, ocl_uml_PrimitiveLiteralExp, ocl_uml_LiteralExp, ocl_uml_CollectionItem, ocl_uml_CollectionLiteralPart, ocl_uml_CollectionLiteralExp, ocl_uml_CollectionRange, ocl_uml_EnumLiteralExp, ocl_uml_IfExp, ocl_uml_IntegerLiteralExp, ocl_uml_UnspecifiedValueExp, ocl_uml_UnlimitedNaturalLiteralExp, ocl_uml_NavigationCallExp, ocl_uml_InvalidLiteralExp, ocl_uml_IterateExp, ocl_uml_LoopExp, ocl_uml_IteratorExp, ocl_uml_LetExp, ocl_uml_MessageExp, ocl_uml_NullLiteralExp, ocl_uml_OperationCallExp, ocl_uml_PropertyCallExp, ocl_uml_RealLiteralExp, ocl_uml_StateExp, ocl_uml_StringLiteralExp, ocl_uml_TupleLiteralExp, ocl_uml_TupleLiteralPart, ocl_uml_TypeExp, ocl_uml_NumericLiteralExp, ocl_uml_Variable, ocl_uml_VariableExp, ocl_uml_TemplateParameterType},
    associations={ownedOperation0, ownedOperation1, ownedOperation3, ownedOperation5, ownedOperation7, ownedAttribute9, ownedOperation11},
    generalizations={gen_ocl_uml_ElementType_Classifier, gen_ocl_uml_ElementType_types_ElementType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)