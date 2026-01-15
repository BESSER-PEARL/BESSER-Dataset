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
CollectionKind: Enumeration = Enumeration(
    name="CollectionKind",
    literals={
            EnumerationLiteral(name="Set"),
			EnumerationLiteral(name="OrderedSet"),
			EnumerationLiteral(name="Bag"),
			EnumerationLiteral(name="Sequence"),
			EnumerationLiteral(name="Collection")
    }
)

# Classes
EssentialOCL_CallExp = Class(name="EssentialOCL::CallExp", is_abstract=True)
OclExpression = Class(name="OclExpression")
EssentialOCL_CollectionItem = Class(name="EssentialOCL::CollectionItem")
CollectionLiteralPart = Class(name="CollectionLiteralPart")
EssentialOCL_CollectionLiteralExp = Class(name="EssentialOCL::CollectionLiteralExp")
LiteralExp = Class(name="LiteralExp")
EssentialOCL_AnyType = Class(name="EssentialOCL::AnyType")
Type = Class(name="Type")
EssentialOCL_BagType = Class(name="EssentialOCL::BagType")
CollectionType = Class(name="CollectionType")
EssentialOCL_BooleanLiteralExp = Class(name="EssentialOCL::BooleanLiteralExp")
PrimitiveLiteralExp = Class(name="PrimitiveLiteralExp")
EssentialOCL_CollectionType = Class(name="EssentialOCL::CollectionType")
DataType = Class(name="DataType")
EssentialOCL_EnumLiteralExp = Class(name="EssentialOCL::EnumLiteralExp")
EnumerationLiteral = Class(name="EnumerationLiteral")
EssentialOCL_ExpressionInOcl = Class(name="EssentialOCL::ExpressionInOcl")
Variable = Class(name="Variable")
EssentialOCL_CollectionLiteralPart = Class(name="EssentialOCL::CollectionLiteralPart", is_abstract=True)
TypedElement = Class(name="TypedElement")
CollectionLiteralExp = Class(name="CollectionLiteralExp")
EssentialOCL_CollectionRange = Class(name="EssentialOCL::CollectionRange")
EssentialOCL_FeatureCallExp = Class(name="EssentialOCL::FeatureCallExp", is_abstract=True)
CallExp = Class(name="CallExp")
EssentialOCL_IfExp = Class(name="EssentialOCL::IfExp")
EssentialOCL_IntegerLiteralExp = Class(name="EssentialOCL::IntegerLiteralExp")
NumericLiteralExp = Class(name="NumericLiteralExp")
EssentialOCL_InvalidLiteralExp = Class(name="EssentialOCL::InvalidLiteralExp")
EssentialOCL_IteratorExp = Class(name="EssentialOCL::IteratorExp")
EssentialOCL_LetExp = Class(name="EssentialOCL::LetExp")
EssentialOCL_LiteralExp = Class(name="EssentialOCL::LiteralExp", is_abstract=True)
EssentialOCL_LoopExp = Class(name="EssentialOCL::LoopExp", is_abstract=True)
EssentialOCL_InvalidType = Class(name="EssentialOCL::InvalidType")
EssentialOCL_IterateExp = Class(name="EssentialOCL::IterateExp")
LoopExp = Class(name="LoopExp")
EssentialOCL_NumericLiteralExp = Class(name="EssentialOCL::NumericLiteralExp", is_abstract=True)
EssentialOCL_OclExpression = Class(name="EssentialOCL::OclExpression", is_abstract=True)
EssentialOCL_OperationCallExp = Class(name="EssentialOCL::OperationCallExp")
Operation = Class(name="Operation")
EssentialOCL_OrderedSetType = Class(name="EssentialOCL::OrderedSetType")
EssentialOCL_PrimitiveLiteralExp = Class(name="EssentialOCL::PrimitiveLiteralExp", is_abstract=True)
EssentialOCL_PropertyCallExp = Class(name="EssentialOCL::PropertyCallExp")
NavigationCallExp = Class(name="NavigationCallExp")
Property_ = Class(name="Property")
EssentialOCL_RealLiteralExp = Class(name="EssentialOCL::RealLiteralExp")
EssentialOCL_SequenceType = Class(name="EssentialOCL::SequenceType")
EssentialOCL_SetType = Class(name="EssentialOCL::SetType")
EssentialOCL_NavigationCallExp = Class(name="EssentialOCL::NavigationCallExp")
FeatureCallExp = Class(name="FeatureCallExp")
EssentialOCL_NullLiteralExp = Class(name="EssentialOCL::NullLiteralExp")
TupleLiteralPart = Class(name="TupleLiteralPart")
EssentialOCL_TupleLiteralPart = Class(name="EssentialOCL::TupleLiteralPart")
TupleLiteralExp = Class(name="TupleLiteralExp")
EssentialOCL_TupleType = Class(name="EssentialOCL::TupleType")
Class_ = Class(name="Class")
EssentialOCL_TypeExp = Class(name="EssentialOCL::TypeExp")
EssentialOCL_UnlimitedNaturalExp = Class(name="EssentialOCL::UnlimitedNaturalExp")
EssentialOCL_StringLiteralExp = Class(name="EssentialOCL::StringLiteralExp")
EssentialOCL_TemplateParameterType = Class(name="EssentialOCL::TemplateParameterType")
EssentialOCL_TupleLiteralExp = Class(name="EssentialOCL::TupleLiteralExp")
Parameter_ = Class(name="Parameter")
EssentialOCL_VariableExp = Class(name="EssentialOCL::VariableExp")
EssentialOCL_VoidType = Class(name="EssentialOCL::VoidType")
EssentialOCL_Variable = Class(name="EssentialOCL::Variable")
LetExp = Class(name="LetExp")

# EssentialOCL_CallExp class attributes and methods

# OclExpression class attributes and methods

# EssentialOCL_CollectionItem class attributes and methods

# CollectionLiteralPart class attributes and methods

# EssentialOCL_CollectionLiteralExp class attributes and methods
EssentialOCL_CollectionLiteralExp_kind: Property = Property(name="kind", type=StringType)
EssentialOCL_CollectionLiteralExp.attributes={EssentialOCL_CollectionLiteralExp_kind}

# LiteralExp class attributes and methods

# EssentialOCL_AnyType class attributes and methods

# Type class attributes and methods

# EssentialOCL_BagType class attributes and methods

# CollectionType class attributes and methods

# EssentialOCL_BooleanLiteralExp class attributes and methods
EssentialOCL_BooleanLiteralExp_booleanSymbol: Property = Property(name="booleanSymbol", type=StringType)
EssentialOCL_BooleanLiteralExp.attributes={EssentialOCL_BooleanLiteralExp_booleanSymbol}

# PrimitiveLiteralExp class attributes and methods

# EssentialOCL_CollectionType class attributes and methods

# DataType class attributes and methods

# EssentialOCL_EnumLiteralExp class attributes and methods

# EnumerationLiteral class attributes and methods

# EssentialOCL_ExpressionInOcl class attributes and methods

# Variable class attributes and methods

# EssentialOCL_CollectionLiteralPart class attributes and methods

# TypedElement class attributes and methods

# CollectionLiteralExp class attributes and methods

# EssentialOCL_CollectionRange class attributes and methods

# EssentialOCL_FeatureCallExp class attributes and methods

# CallExp class attributes and methods

# EssentialOCL_IfExp class attributes and methods

# EssentialOCL_IntegerLiteralExp class attributes and methods
EssentialOCL_IntegerLiteralExp_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
EssentialOCL_IntegerLiteralExp.attributes={EssentialOCL_IntegerLiteralExp_integerSymbol}

# NumericLiteralExp class attributes and methods

# EssentialOCL_InvalidLiteralExp class attributes and methods

# EssentialOCL_IteratorExp class attributes and methods

# EssentialOCL_LetExp class attributes and methods

# EssentialOCL_LiteralExp class attributes and methods

# EssentialOCL_LoopExp class attributes and methods

# EssentialOCL_InvalidType class attributes and methods

# EssentialOCL_IterateExp class attributes and methods

# LoopExp class attributes and methods

# EssentialOCL_NumericLiteralExp class attributes and methods

# EssentialOCL_OclExpression class attributes and methods

# EssentialOCL_OperationCallExp class attributes and methods

# Operation class attributes and methods

# EssentialOCL_OrderedSetType class attributes and methods

# EssentialOCL_PrimitiveLiteralExp class attributes and methods

# EssentialOCL_PropertyCallExp class attributes and methods

# NavigationCallExp class attributes and methods

# Property class attributes and methods

# EssentialOCL_RealLiteralExp class attributes and methods
EssentialOCL_RealLiteralExp_realSymbol: Property = Property(name="realSymbol", type=StringType)
EssentialOCL_RealLiteralExp.attributes={EssentialOCL_RealLiteralExp_realSymbol}

# EssentialOCL_SequenceType class attributes and methods

# EssentialOCL_SetType class attributes and methods

# EssentialOCL_NavigationCallExp class attributes and methods

# FeatureCallExp class attributes and methods

# EssentialOCL_NullLiteralExp class attributes and methods

# TupleLiteralPart class attributes and methods

# EssentialOCL_TupleLiteralPart class attributes and methods

# TupleLiteralExp class attributes and methods

# EssentialOCL_TupleType class attributes and methods

# Class class attributes and methods

# EssentialOCL_TypeExp class attributes and methods

# EssentialOCL_UnlimitedNaturalExp class attributes and methods
EssentialOCL_UnlimitedNaturalExp_symbol: Property = Property(name="symbol", type=StringType)
EssentialOCL_UnlimitedNaturalExp.attributes={EssentialOCL_UnlimitedNaturalExp_symbol}

# EssentialOCL_StringLiteralExp class attributes and methods
EssentialOCL_StringLiteralExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
EssentialOCL_StringLiteralExp.attributes={EssentialOCL_StringLiteralExp_stringSymbol}

# EssentialOCL_TemplateParameterType class attributes and methods
EssentialOCL_TemplateParameterType_specification: Property = Property(name="specification", type=StringType)
EssentialOCL_TemplateParameterType.attributes={EssentialOCL_TemplateParameterType_specification}

# EssentialOCL_TupleLiteralExp class attributes and methods

# Parameter class attributes and methods

# EssentialOCL_VariableExp class attributes and methods

# EssentialOCL_VoidType class attributes and methods

# EssentialOCL_Variable class attributes and methods

# LetExp class attributes and methods

# Relationships
source0: BinaryAssociation = BinaryAssociation(
    name="source0",
    ends={
        Property(name="OclExpression", type=EssentialOCL_CallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_CallExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
item1: BinaryAssociation = BinaryAssociation(
    name="item1",
    ends={
        Property(name="OclExpression2", type=EssentialOCL_CollectionItem, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_CollectionItem", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
part3: BinaryAssociation = BinaryAssociation(
    name="part3",
    ends={
        Property(name="CollectionLiteralPart", type=EssentialOCL_CollectionLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_CollectionLiteralExp", type=CollectionLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
first5: BinaryAssociation = BinaryAssociation(
    name="first5",
    ends={
        Property(name="EssentialOCL_CollectionRange", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="OclExpression6", type=EssentialOCL_CollectionRange, multiplicity=Multiplicity(1, 1))
    }
)
last7: BinaryAssociation = BinaryAssociation(
    name="last7",
    ends={
        Property(name="OclExpression9", type=EssentialOCL_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_CollectionRange8", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementType10: BinaryAssociation = BinaryAssociation(
    name="elementType10",
    ends={
        Property(name="Type", type=EssentialOCL_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_CollectionType", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
referredEnumLiteral11: BinaryAssociation = BinaryAssociation(
    name="referredEnumLiteral11",
    ends={
        Property(name="EnumerationLiteral", type=EssentialOCL_EnumLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_EnumLiteralExp", type=EnumerationLiteral, multiplicity=Multiplicity(0, 1))
    }
)
bodyExpression12: BinaryAssociation = BinaryAssociation(
    name="bodyExpression12",
    ends={
        Property(name="OclExpression13", type=EssentialOCL_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_ExpressionInOcl", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
contextVariable14: BinaryAssociation = BinaryAssociation(
    name="contextVariable14",
    ends={
        Property(name="Variable", type=EssentialOCL_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_ExpressionInOcl15", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
collectionLiteralExp4: BinaryAssociation = BinaryAssociation(
    name="collectionLiteralExp4",
    ends={
        Property(name="CollectionLiteralExp", type=EssentialOCL_CollectionLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_CollectionLiteralPart", type=CollectionLiteralExp, multiplicity=Multiplicity(1, 1))
    }
)
resultVariable22: BinaryAssociation = BinaryAssociation(
    name="resultVariable22",
    ends={
        Property(name="Variable24", type=EssentialOCL_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_ExpressionInOcl23", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition25: BinaryAssociation = BinaryAssociation(
    name="condition25",
    ends={
        Property(name="OclExpression26", type=EssentialOCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_IfExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression27: BinaryAssociation = BinaryAssociation(
    name="elseExpression27",
    ends={
        Property(name="OclExpression29", type=EssentialOCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_IfExp28", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression30: BinaryAssociation = BinaryAssociation(
    name="thenExpression30",
    ends={
        Property(name="OclExpression32", type=EssentialOCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_IfExp31", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
generatedType16: BinaryAssociation = BinaryAssociation(
    name="generatedType16",
    ends={
        Property(name="Type18", type=EssentialOCL_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_ExpressionInOcl17", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameterVariable19: BinaryAssociation = BinaryAssociation(
    name="parameterVariable19",
    ends={
        Property(name="Variable21", type=EssentialOCL_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_ExpressionInOcl20", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
in35: BinaryAssociation = BinaryAssociation(
    name="in35",
    ends={
        Property(name="OclExpression36", type=EssentialOCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_LetExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable37: BinaryAssociation = BinaryAssociation(
    name="variable37",
    ends={
        Property(name="Variable39", type=EssentialOCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_LetExp38", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body40: BinaryAssociation = BinaryAssociation(
    name="body40",
    ends={
        Property(name="OclExpression41", type=EssentialOCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_LoopExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result33: BinaryAssociation = BinaryAssociation(
    name="result33",
    ends={
        Property(name="Variable34", type=EssentialOCL_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_IterateExp", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
argument45: BinaryAssociation = BinaryAssociation(
    name="argument45",
    ends={
        Property(name="OclExpression46", type=EssentialOCL_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_OperationCallExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredOperation47: BinaryAssociation = BinaryAssociation(
    name="referredOperation47",
    ends={
        Property(name="Operation", type=EssentialOCL_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_OperationCallExp48", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
referredProperty49: BinaryAssociation = BinaryAssociation(
    name="referredProperty49",
    ends={
        Property(name="Property", type=EssentialOCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_PropertyCallExp", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
iterator42: BinaryAssociation = BinaryAssociation(
    name="iterator42",
    ends={
        Property(name="Variable44", type=EssentialOCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_LoopExp43", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
part50: BinaryAssociation = BinaryAssociation(
    name="part50",
    ends={
        Property(name="TupleLiteralPart", type=EssentialOCL_TupleLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_TupleLiteralExp", type=TupleLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute51: BinaryAssociation = BinaryAssociation(
    name="attribute51",
    ends={
        Property(name="Property52", type=EssentialOCL_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_TupleLiteralPart", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
tupleLiteralExp53: BinaryAssociation = BinaryAssociation(
    name="tupleLiteralExp53",
    ends={
        Property(name="TupleLiteralExp", type=EssentialOCL_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_TupleLiteralPart54", type=TupleLiteralExp, multiplicity=Multiplicity(0, 1))
    }
)
value55: BinaryAssociation = BinaryAssociation(
    name="value55",
    ends={
        Property(name="OclExpression57", type=EssentialOCL_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_TupleLiteralPart56", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referredType58: BinaryAssociation = BinaryAssociation(
    name="referredType58",
    ends={
        Property(name="Type59", type=EssentialOCL_TypeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_TypeExp", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
representedParameter64: BinaryAssociation = BinaryAssociation(
    name="representedParameter64",
    ends={
        Property(name="Parameter", type=EssentialOCL_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_Variable65", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
referredVariable66: BinaryAssociation = BinaryAssociation(
    name="referredVariable66",
    ends={
        Property(name="Variable67", type=EssentialOCL_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_VariableExp", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
initExpression60: BinaryAssociation = BinaryAssociation(
    name="initExpression60",
    ends={
        Property(name="OclExpression61", type=EssentialOCL_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_Variable", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
letExp62: BinaryAssociation = BinaryAssociation(
    name="letExp62",
    ends={
        Property(name="LetExp", type=EssentialOCL_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_Variable63", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_EssentialOCL_CallExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_CallExp)
gen_EssentialOCL_CollectionItem_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=EssentialOCL_CollectionItem)
gen_EssentialOCL_CollectionLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=EssentialOCL_CollectionLiteralExp)
gen_EssentialOCL_AnyType_Type = Generalization(general=Type, specific=EssentialOCL_AnyType)
gen_EssentialOCL_BagType_CollectionType = Generalization(general=CollectionType, specific=EssentialOCL_BagType)
gen_EssentialOCL_BooleanLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=EssentialOCL_BooleanLiteralExp)
gen_EssentialOCL_CollectionType_DataType = Generalization(general=DataType, specific=EssentialOCL_CollectionType)
gen_EssentialOCL_EnumLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=EssentialOCL_EnumLiteralExp)
gen_EssentialOCL_ExpressionInOcl_TypedElement = Generalization(general=TypedElement, specific=EssentialOCL_ExpressionInOcl)
gen_EssentialOCL_CollectionLiteralPart_TypedElement = Generalization(general=TypedElement, specific=EssentialOCL_CollectionLiteralPart)
gen_EssentialOCL_CollectionRange_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=EssentialOCL_CollectionRange)
gen_EssentialOCL_FeatureCallExp_CallExp = Generalization(general=CallExp, specific=EssentialOCL_FeatureCallExp)
gen_EssentialOCL_IfExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_IfExp)
gen_EssentialOCL_IntegerLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=EssentialOCL_IntegerLiteralExp)
gen_EssentialOCL_InvalidLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=EssentialOCL_InvalidLiteralExp)
gen_EssentialOCL_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=EssentialOCL_IteratorExp)
gen_EssentialOCL_LetExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_LetExp)
gen_EssentialOCL_LiteralExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_LiteralExp)
gen_EssentialOCL_LoopExp_CallExp = Generalization(general=CallExp, specific=EssentialOCL_LoopExp)
gen_EssentialOCL_LoopExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_LoopExp)
gen_EssentialOCL_InvalidType_Type = Generalization(general=Type, specific=EssentialOCL_InvalidType)
gen_EssentialOCL_IterateExp_LoopExp = Generalization(general=LoopExp, specific=EssentialOCL_IterateExp)
gen_EssentialOCL_NumericLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=EssentialOCL_NumericLiteralExp)
gen_EssentialOCL_OclExpression_TypedElement = Generalization(general=TypedElement, specific=EssentialOCL_OclExpression)
gen_EssentialOCL_OperationCallExp_FeatureCallExp = Generalization(general=FeatureCallExp, specific=EssentialOCL_OperationCallExp)
gen_EssentialOCL_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=EssentialOCL_OrderedSetType)
gen_EssentialOCL_PrimitiveLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=EssentialOCL_PrimitiveLiteralExp)
gen_EssentialOCL_PropertyCallExp_NavigationCallExp = Generalization(general=NavigationCallExp, specific=EssentialOCL_PropertyCallExp)
gen_EssentialOCL_RealLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=EssentialOCL_RealLiteralExp)
gen_EssentialOCL_SequenceType_CollectionType = Generalization(general=CollectionType, specific=EssentialOCL_SequenceType)
gen_EssentialOCL_SetType_CollectionType = Generalization(general=CollectionType, specific=EssentialOCL_SetType)
gen_EssentialOCL_NavigationCallExp_FeatureCallExp = Generalization(general=FeatureCallExp, specific=EssentialOCL_NavigationCallExp)
gen_EssentialOCL_NullLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=EssentialOCL_NullLiteralExp)
gen_EssentialOCL_TupleLiteralPart_TypedElement = Generalization(general=TypedElement, specific=EssentialOCL_TupleLiteralPart)
gen_EssentialOCL_TupleType_Class = Generalization(general=Class_, specific=EssentialOCL_TupleType)
gen_EssentialOCL_TupleType_DataType = Generalization(general=DataType, specific=EssentialOCL_TupleType)
gen_EssentialOCL_TypeExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_TypeExp)
gen_EssentialOCL_UnlimitedNaturalExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=EssentialOCL_UnlimitedNaturalExp)
gen_EssentialOCL_StringLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=EssentialOCL_StringLiteralExp)
gen_EssentialOCL_TemplateParameterType_Type = Generalization(general=Type, specific=EssentialOCL_TemplateParameterType)
gen_EssentialOCL_TupleLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=EssentialOCL_TupleLiteralExp)
gen_EssentialOCL_VariableExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_VariableExp)
gen_EssentialOCL_VoidType_Type = Generalization(general=Type, specific=EssentialOCL_VoidType)
gen_EssentialOCL_Variable_TypedElement = Generalization(general=TypedElement, specific=EssentialOCL_Variable)

# Domain Model
domain_model = DomainModel(
    name="EssentialOCL",
    types={EssentialOCL_CallExp, OclExpression, EssentialOCL_CollectionItem, CollectionLiteralPart, EssentialOCL_CollectionLiteralExp, LiteralExp, EssentialOCL_AnyType, Type, EssentialOCL_BagType, CollectionType, EssentialOCL_BooleanLiteralExp, PrimitiveLiteralExp, EssentialOCL_CollectionType, DataType, EssentialOCL_EnumLiteralExp, EnumerationLiteral, EssentialOCL_ExpressionInOcl, Variable, EssentialOCL_CollectionLiteralPart, TypedElement, CollectionLiteralExp, EssentialOCL_CollectionRange, EssentialOCL_FeatureCallExp, CallExp, EssentialOCL_IfExp, EssentialOCL_IntegerLiteralExp, NumericLiteralExp, EssentialOCL_InvalidLiteralExp, EssentialOCL_IteratorExp, EssentialOCL_LetExp, EssentialOCL_LiteralExp, EssentialOCL_LoopExp, EssentialOCL_InvalidType, EssentialOCL_IterateExp, LoopExp, EssentialOCL_NumericLiteralExp, EssentialOCL_OclExpression, EssentialOCL_OperationCallExp, Operation, EssentialOCL_OrderedSetType, EssentialOCL_PrimitiveLiteralExp, EssentialOCL_PropertyCallExp, NavigationCallExp, Property_, EssentialOCL_RealLiteralExp, EssentialOCL_SequenceType, EssentialOCL_SetType, EssentialOCL_NavigationCallExp, FeatureCallExp, EssentialOCL_NullLiteralExp, TupleLiteralPart, EssentialOCL_TupleLiteralPart, TupleLiteralExp, EssentialOCL_TupleType, Class_, EssentialOCL_TypeExp, EssentialOCL_UnlimitedNaturalExp, EssentialOCL_StringLiteralExp, EssentialOCL_TemplateParameterType, EssentialOCL_TupleLiteralExp, Parameter_, EssentialOCL_VariableExp, EssentialOCL_VoidType, EssentialOCL_Variable, LetExp, CollectionKind},
    associations={source0, item1, part3, first5, last7, elementType10, referredEnumLiteral11, bodyExpression12, contextVariable14, collectionLiteralExp4, resultVariable22, condition25, elseExpression27, thenExpression30, generatedType16, parameterVariable19, in35, variable37, body40, result33, argument45, referredOperation47, referredProperty49, iterator42, part50, attribute51, tupleLiteralExp53, value55, referredType58, representedParameter64, referredVariable66, initExpression60, letExp62},
    generalizations={gen_EssentialOCL_CallExp_OclExpression, gen_EssentialOCL_CollectionItem_CollectionLiteralPart, gen_EssentialOCL_CollectionLiteralExp_LiteralExp, gen_EssentialOCL_AnyType_Type, gen_EssentialOCL_BagType_CollectionType, gen_EssentialOCL_BooleanLiteralExp_PrimitiveLiteralExp, gen_EssentialOCL_CollectionType_DataType, gen_EssentialOCL_EnumLiteralExp_LiteralExp, gen_EssentialOCL_ExpressionInOcl_TypedElement, gen_EssentialOCL_CollectionLiteralPart_TypedElement, gen_EssentialOCL_CollectionRange_CollectionLiteralPart, gen_EssentialOCL_FeatureCallExp_CallExp, gen_EssentialOCL_IfExp_OclExpression, gen_EssentialOCL_IntegerLiteralExp_NumericLiteralExp, gen_EssentialOCL_InvalidLiteralExp_LiteralExp, gen_EssentialOCL_IteratorExp_LoopExp, gen_EssentialOCL_LetExp_OclExpression, gen_EssentialOCL_LiteralExp_OclExpression, gen_EssentialOCL_LoopExp_CallExp, gen_EssentialOCL_LoopExp_OclExpression, gen_EssentialOCL_InvalidType_Type, gen_EssentialOCL_IterateExp_LoopExp, gen_EssentialOCL_NumericLiteralExp_PrimitiveLiteralExp, gen_EssentialOCL_OclExpression_TypedElement, gen_EssentialOCL_OperationCallExp_FeatureCallExp, gen_EssentialOCL_OrderedSetType_CollectionType, gen_EssentialOCL_PrimitiveLiteralExp_LiteralExp, gen_EssentialOCL_PropertyCallExp_NavigationCallExp, gen_EssentialOCL_RealLiteralExp_NumericLiteralExp, gen_EssentialOCL_SequenceType_CollectionType, gen_EssentialOCL_SetType_CollectionType, gen_EssentialOCL_NavigationCallExp_FeatureCallExp, gen_EssentialOCL_NullLiteralExp_LiteralExp, gen_EssentialOCL_TupleLiteralPart_TypedElement, gen_EssentialOCL_TupleType_Class, gen_EssentialOCL_TupleType_DataType, gen_EssentialOCL_TypeExp_OclExpression, gen_EssentialOCL_UnlimitedNaturalExp_NumericLiteralExp, gen_EssentialOCL_StringLiteralExp_PrimitiveLiteralExp, gen_EssentialOCL_TemplateParameterType_Type, gen_EssentialOCL_TupleLiteralExp_LiteralExp, gen_EssentialOCL_VariableExp_OclExpression, gen_EssentialOCL_VoidType_Type, gen_EssentialOCL_Variable_TypedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)