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
EssentialOCL_AnyType = Class(name="EssentialOCL::AnyType")
EssentialOCL_BagType = Class(name="EssentialOCL::BagType")
CollectionType = Class(name="CollectionType")
EssentialOCL_BooleanLiteralExp = Class(name="EssentialOCL::BooleanLiteralExp")
PrimitiveLiteralExp = Class(name="PrimitiveLiteralExp")
EssentialOCL_CallExp = Class(name="EssentialOCL::CallExp", is_abstract=True)
OclExpression = Class(name="OclExpression")
EssentialOCL_CollectionItem = Class(name="EssentialOCL::CollectionItem")
CollectionLiteralPart = Class(name="CollectionLiteralPart")
EssentialOCL_CollectionRange = Class(name="EssentialOCL::CollectionRange")
EssentialOCL_CollectionType = Class(name="EssentialOCL::CollectionType")
EssentialOCL_EnumLiteralExp = Class(name="EssentialOCL::EnumLiteralExp")
EssentialOCL_ExpressionInOcl = Class(name="EssentialOCL::ExpressionInOcl")
EssentialOCL_CollectionLiteralExp = Class(name="EssentialOCL::CollectionLiteralExp")
LiteralExp = Class(name="LiteralExp")
EssentialOCL_CollectionLiteralPart = Class(name="EssentialOCL::CollectionLiteralPart", is_abstract=True)
CollectionLiteralExp = Class(name="CollectionLiteralExp")
EssentialOCL_FeatureCallExp = Class(name="EssentialOCL::FeatureCallExp", is_abstract=True)
CallExp = Class(name="CallExp")
EssentialOCL_IfExp = Class(name="EssentialOCL::IfExp")
Variable = Class(name="Variable")
EssentialOCL_LiteralExp = Class(name="EssentialOCL::LiteralExp", is_abstract=True)
EssentialOCL_LoopExp = Class(name="EssentialOCL::LoopExp", is_abstract=True)
EssentialOCL_NavigationCallExp = Class(name="EssentialOCL::NavigationCallExp")
FeatureCallExp = Class(name="FeatureCallExp")
EssentialOCL_IntegerLiteralExp = Class(name="EssentialOCL::IntegerLiteralExp")
NumericLiteralExp = Class(name="NumericLiteralExp")
EssentialOCL_InvalidLiteralExp = Class(name="EssentialOCL::InvalidLiteralExp")
EssentialOCL_InvalidType = Class(name="EssentialOCL::InvalidType")
EssentialOCL_IterateExp = Class(name="EssentialOCL::IterateExp")
LoopExp = Class(name="LoopExp")
EssentialOCL_IteratorExp = Class(name="EssentialOCL::IteratorExp")
EssentialOCL_LetExp = Class(name="EssentialOCL::LetExp")
EssentialOCL_RealLiteralExp = Class(name="EssentialOCL::RealLiteralExp")
EssentialOCL_SequenceType = Class(name="EssentialOCL::SequenceType")
EssentialOCL_SetType = Class(name="EssentialOCL::SetType")
EssentialOCL_StringLiteralExp = Class(name="EssentialOCL::StringLiteralExp")
EssentialOCL_TemplateParameterType = Class(name="EssentialOCL::TemplateParameterType")
EssentialOCL_TupleLiteralExp = Class(name="EssentialOCL::TupleLiteralExp")
TupleLiteralPart = Class(name="TupleLiteralPart")
EssentialOCL_NullLiteralExp = Class(name="EssentialOCL::NullLiteralExp")
EssentialOCL_NumericLiteralExp = Class(name="EssentialOCL::NumericLiteralExp", is_abstract=True)
EssentialOCL_OclExpression = Class(name="EssentialOCL::OclExpression", is_abstract=True)
EssentialOCL_OperationCallExp = Class(name="EssentialOCL::OperationCallExp")
EssentialOCL_OrderedSetType = Class(name="EssentialOCL::OrderedSetType")
EssentialOCL_PrimitiveLiteralExp = Class(name="EssentialOCL::PrimitiveLiteralExp", is_abstract=True)
EssentialOCL_PropertyCallExp = Class(name="EssentialOCL::PropertyCallExp")
NavigationCallExp = Class(name="NavigationCallExp")
EssentialOCL_Variable = Class(name="EssentialOCL::Variable")
LetExp = Class(name="LetExp")
EssentialOCL_VariableExp = Class(name="EssentialOCL::VariableExp")
EssentialOCL_VoidType = Class(name="EssentialOCL::VoidType")
EssentialOCL_TupleLiteralPart = Class(name="EssentialOCL::TupleLiteralPart")
TupleLiteralExp = Class(name="TupleLiteralExp")
EssentialOCL_TupleType = Class(name="EssentialOCL::TupleType")
EssentialOCL_TypeExp = Class(name="EssentialOCL::TypeExp")
EssentialOCL_UnlimitedNaturalExp = Class(name="EssentialOCL::UnlimitedNaturalExp")

# EssentialOCL_AnyType class attributes and methods

# EssentialOCL_BagType class attributes and methods

# CollectionType class attributes and methods

# EssentialOCL_BooleanLiteralExp class attributes and methods
EssentialOCL_BooleanLiteralExp_booleanSymbol: Property = Property(name="booleanSymbol", type=StringType)
EssentialOCL_BooleanLiteralExp.attributes={EssentialOCL_BooleanLiteralExp_booleanSymbol}

# PrimitiveLiteralExp class attributes and methods

# EssentialOCL_CallExp class attributes and methods

# OclExpression class attributes and methods

# EssentialOCL_CollectionItem class attributes and methods

# CollectionLiteralPart class attributes and methods

# EssentialOCL_CollectionRange class attributes and methods

# EssentialOCL_CollectionType class attributes and methods

# EssentialOCL_EnumLiteralExp class attributes and methods

# EssentialOCL_ExpressionInOcl class attributes and methods

# EssentialOCL_CollectionLiteralExp class attributes and methods
EssentialOCL_CollectionLiteralExp_kind: Property = Property(name="kind", type=StringType)
EssentialOCL_CollectionLiteralExp.attributes={EssentialOCL_CollectionLiteralExp_kind}

# LiteralExp class attributes and methods

# EssentialOCL_CollectionLiteralPart class attributes and methods

# CollectionLiteralExp class attributes and methods

# EssentialOCL_FeatureCallExp class attributes and methods

# CallExp class attributes and methods

# EssentialOCL_IfExp class attributes and methods

# Variable class attributes and methods

# EssentialOCL_LiteralExp class attributes and methods

# EssentialOCL_LoopExp class attributes and methods

# EssentialOCL_NavigationCallExp class attributes and methods

# FeatureCallExp class attributes and methods

# EssentialOCL_IntegerLiteralExp class attributes and methods
EssentialOCL_IntegerLiteralExp_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
EssentialOCL_IntegerLiteralExp.attributes={EssentialOCL_IntegerLiteralExp_integerSymbol}

# NumericLiteralExp class attributes and methods

# EssentialOCL_InvalidLiteralExp class attributes and methods

# EssentialOCL_InvalidType class attributes and methods

# EssentialOCL_IterateExp class attributes and methods

# LoopExp class attributes and methods

# EssentialOCL_IteratorExp class attributes and methods

# EssentialOCL_LetExp class attributes and methods

# EssentialOCL_RealLiteralExp class attributes and methods
EssentialOCL_RealLiteralExp_realSymbol: Property = Property(name="realSymbol", type=StringType)
EssentialOCL_RealLiteralExp.attributes={EssentialOCL_RealLiteralExp_realSymbol}

# EssentialOCL_SequenceType class attributes and methods

# EssentialOCL_SetType class attributes and methods

# EssentialOCL_StringLiteralExp class attributes and methods
EssentialOCL_StringLiteralExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
EssentialOCL_StringLiteralExp.attributes={EssentialOCL_StringLiteralExp_stringSymbol}

# EssentialOCL_TemplateParameterType class attributes and methods
EssentialOCL_TemplateParameterType_specification: Property = Property(name="specification", type=StringType)
EssentialOCL_TemplateParameterType.attributes={EssentialOCL_TemplateParameterType_specification}

# EssentialOCL_TupleLiteralExp class attributes and methods

# TupleLiteralPart class attributes and methods

# EssentialOCL_NullLiteralExp class attributes and methods

# EssentialOCL_NumericLiteralExp class attributes and methods

# EssentialOCL_OclExpression class attributes and methods

# EssentialOCL_OperationCallExp class attributes and methods

# EssentialOCL_OrderedSetType class attributes and methods

# EssentialOCL_PrimitiveLiteralExp class attributes and methods

# EssentialOCL_PropertyCallExp class attributes and methods

# NavigationCallExp class attributes and methods

# EssentialOCL_Variable class attributes and methods

# LetExp class attributes and methods

# EssentialOCL_VariableExp class attributes and methods

# EssentialOCL_VoidType class attributes and methods

# EssentialOCL_TupleLiteralPart class attributes and methods

# TupleLiteralExp class attributes and methods

# EssentialOCL_TupleType class attributes and methods

# EssentialOCL_TypeExp class attributes and methods

# EssentialOCL_UnlimitedNaturalExp class attributes and methods
EssentialOCL_UnlimitedNaturalExp_symbol: Property = Property(name="symbol", type=StringType)
EssentialOCL_UnlimitedNaturalExp.attributes={EssentialOCL_UnlimitedNaturalExp_symbol}

# Relationships
source0: BinaryAssociation = BinaryAssociation(
    name="source0",
    ends={
        Property(name="OclExpression", type=EssentialOCL_CallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_CallExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
first5: BinaryAssociation = BinaryAssociation(
    name="first5",
    ends={
        Property(name="OclExpression6", type=EssentialOCL_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_CollectionRange", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
last7: BinaryAssociation = BinaryAssociation(
    name="last7",
    ends={
        Property(name="OclExpression9", type=EssentialOCL_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_CollectionRange8", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
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
collectionLiteralExp4: BinaryAssociation = BinaryAssociation(
    name="collectionLiteralExp4",
    ends={
        Property(name="CollectionLiteralExp", type=EssentialOCL_CollectionLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_CollectionLiteralPart", type=CollectionLiteralExp, multiplicity=Multiplicity(1, 1))
    }
)
resultVariable17: BinaryAssociation = BinaryAssociation(
    name="resultVariable17",
    ends={
        Property(name="Variable19", type=EssentialOCL_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_ExpressionInOcl18", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition20: BinaryAssociation = BinaryAssociation(
    name="condition20",
    ends={
        Property(name="OclExpression21", type=EssentialOCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_IfExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression22: BinaryAssociation = BinaryAssociation(
    name="elseExpression22",
    ends={
        Property(name="OclExpression24", type=EssentialOCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_IfExp23", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression25: BinaryAssociation = BinaryAssociation(
    name="thenExpression25",
    ends={
        Property(name="OclExpression27", type=EssentialOCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_IfExp26", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bodyExpression10: BinaryAssociation = BinaryAssociation(
    name="bodyExpression10",
    ends={
        Property(name="OclExpression11", type=EssentialOCL_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_ExpressionInOcl", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
contextVariable12: BinaryAssociation = BinaryAssociation(
    name="contextVariable12",
    ends={
        Property(name="Variable", type=EssentialOCL_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_ExpressionInOcl13", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterVariable14: BinaryAssociation = BinaryAssociation(
    name="parameterVariable14",
    ends={
        Property(name="Variable16", type=EssentialOCL_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_ExpressionInOcl15", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
in30: BinaryAssociation = BinaryAssociation(
    name="in30",
    ends={
        Property(name="OclExpression31", type=EssentialOCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_LetExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable32: BinaryAssociation = BinaryAssociation(
    name="variable32",
    ends={
        Property(name="Variable34", type=EssentialOCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_LetExp33", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body35: BinaryAssociation = BinaryAssociation(
    name="body35",
    ends={
        Property(name="OclExpression36", type=EssentialOCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_LoopExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterator37: BinaryAssociation = BinaryAssociation(
    name="iterator37",
    ends={
        Property(name="Variable39", type=EssentialOCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_LoopExp38", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
result28: BinaryAssociation = BinaryAssociation(
    name="result28",
    ends={
        Property(name="Variable29", type=EssentialOCL_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_IterateExp", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
argument40: BinaryAssociation = BinaryAssociation(
    name="argument40",
    ends={
        Property(name="OclExpression41", type=EssentialOCL_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_OperationCallExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initExpression47: BinaryAssociation = BinaryAssociation(
    name="initExpression47",
    ends={
        Property(name="OclExpression48", type=EssentialOCL_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_Variable", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
letExp49: BinaryAssociation = BinaryAssociation(
    name="letExp49",
    ends={
        Property(name="LetExp", type=EssentialOCL_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_Variable50", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
referredVariable51: BinaryAssociation = BinaryAssociation(
    name="referredVariable51",
    ends={
        Property(name="Variable52", type=EssentialOCL_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_VariableExp", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
part42: BinaryAssociation = BinaryAssociation(
    name="part42",
    ends={
        Property(name="TupleLiteralPart", type=EssentialOCL_TupleLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_TupleLiteralExp", type=TupleLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tupleLiteralExp43: BinaryAssociation = BinaryAssociation(
    name="tupleLiteralExp43",
    ends={
        Property(name="TupleLiteralExp", type=EssentialOCL_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_TupleLiteralPart", type=TupleLiteralExp, multiplicity=Multiplicity(0, 1))
    }
)
value44: BinaryAssociation = BinaryAssociation(
    name="value44",
    ends={
        Property(name="OclExpression46", type=EssentialOCL_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="EssentialOCL_TupleLiteralPart45", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_EssentialOCL_BagType_CollectionType = Generalization(general=CollectionType, specific=EssentialOCL_BagType)
gen_EssentialOCL_BooleanLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=EssentialOCL_BooleanLiteralExp)
gen_EssentialOCL_CallExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_CallExp)
gen_EssentialOCL_CollectionItem_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=EssentialOCL_CollectionItem)
gen_EssentialOCL_CollectionRange_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=EssentialOCL_CollectionRange)
gen_EssentialOCL_EnumLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=EssentialOCL_EnumLiteralExp)
gen_EssentialOCL_CollectionLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=EssentialOCL_CollectionLiteralExp)
gen_EssentialOCL_FeatureCallExp_CallExp = Generalization(general=CallExp, specific=EssentialOCL_FeatureCallExp)
gen_EssentialOCL_IfExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_IfExp)
gen_EssentialOCL_LiteralExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_LiteralExp)
gen_EssentialOCL_LoopExp_CallExp = Generalization(general=CallExp, specific=EssentialOCL_LoopExp)
gen_EssentialOCL_LoopExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_LoopExp)
gen_EssentialOCL_NavigationCallExp_FeatureCallExp = Generalization(general=FeatureCallExp, specific=EssentialOCL_NavigationCallExp)
gen_EssentialOCL_IntegerLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=EssentialOCL_IntegerLiteralExp)
gen_EssentialOCL_InvalidLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=EssentialOCL_InvalidLiteralExp)
gen_EssentialOCL_IterateExp_LoopExp = Generalization(general=LoopExp, specific=EssentialOCL_IterateExp)
gen_EssentialOCL_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=EssentialOCL_IteratorExp)
gen_EssentialOCL_LetExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_LetExp)
gen_EssentialOCL_RealLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=EssentialOCL_RealLiteralExp)
gen_EssentialOCL_SequenceType_CollectionType = Generalization(general=CollectionType, specific=EssentialOCL_SequenceType)
gen_EssentialOCL_SetType_CollectionType = Generalization(general=CollectionType, specific=EssentialOCL_SetType)
gen_EssentialOCL_StringLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=EssentialOCL_StringLiteralExp)
gen_EssentialOCL_TupleLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=EssentialOCL_TupleLiteralExp)
gen_EssentialOCL_NullLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=EssentialOCL_NullLiteralExp)
gen_EssentialOCL_NumericLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=EssentialOCL_NumericLiteralExp)
gen_EssentialOCL_OperationCallExp_FeatureCallExp = Generalization(general=FeatureCallExp, specific=EssentialOCL_OperationCallExp)
gen_EssentialOCL_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=EssentialOCL_OrderedSetType)
gen_EssentialOCL_PrimitiveLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=EssentialOCL_PrimitiveLiteralExp)
gen_EssentialOCL_PropertyCallExp_NavigationCallExp = Generalization(general=NavigationCallExp, specific=EssentialOCL_PropertyCallExp)
gen_EssentialOCL_VariableExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_VariableExp)
gen_EssentialOCL_TypeExp_OclExpression = Generalization(general=OclExpression, specific=EssentialOCL_TypeExp)
gen_EssentialOCL_UnlimitedNaturalExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=EssentialOCL_UnlimitedNaturalExp)

# Domain Model
domain_model = DomainModel(
    name="EssentialOCL",
    types={EssentialOCL_AnyType, EssentialOCL_BagType, CollectionType, EssentialOCL_BooleanLiteralExp, PrimitiveLiteralExp, EssentialOCL_CallExp, OclExpression, EssentialOCL_CollectionItem, CollectionLiteralPart, EssentialOCL_CollectionRange, EssentialOCL_CollectionType, EssentialOCL_EnumLiteralExp, EssentialOCL_ExpressionInOcl, EssentialOCL_CollectionLiteralExp, LiteralExp, EssentialOCL_CollectionLiteralPart, CollectionLiteralExp, EssentialOCL_FeatureCallExp, CallExp, EssentialOCL_IfExp, Variable, EssentialOCL_LiteralExp, EssentialOCL_LoopExp, EssentialOCL_NavigationCallExp, FeatureCallExp, EssentialOCL_IntegerLiteralExp, NumericLiteralExp, EssentialOCL_InvalidLiteralExp, EssentialOCL_InvalidType, EssentialOCL_IterateExp, LoopExp, EssentialOCL_IteratorExp, EssentialOCL_LetExp, EssentialOCL_RealLiteralExp, EssentialOCL_SequenceType, EssentialOCL_SetType, EssentialOCL_StringLiteralExp, EssentialOCL_TemplateParameterType, EssentialOCL_TupleLiteralExp, TupleLiteralPart, EssentialOCL_NullLiteralExp, EssentialOCL_NumericLiteralExp, EssentialOCL_OclExpression, EssentialOCL_OperationCallExp, EssentialOCL_OrderedSetType, EssentialOCL_PrimitiveLiteralExp, EssentialOCL_PropertyCallExp, NavigationCallExp, EssentialOCL_Variable, LetExp, EssentialOCL_VariableExp, EssentialOCL_VoidType, EssentialOCL_TupleLiteralPart, TupleLiteralExp, EssentialOCL_TupleType, EssentialOCL_TypeExp, EssentialOCL_UnlimitedNaturalExp, CollectionKind},
    associations={source0, first5, last7, item1, part3, collectionLiteralExp4, resultVariable17, condition20, elseExpression22, thenExpression25, bodyExpression10, contextVariable12, parameterVariable14, in30, variable32, body35, iterator37, result28, argument40, initExpression47, letExp49, referredVariable51, part42, tupleLiteralExp43, value44},
    generalizations={gen_EssentialOCL_BagType_CollectionType, gen_EssentialOCL_BooleanLiteralExp_PrimitiveLiteralExp, gen_EssentialOCL_CallExp_OclExpression, gen_EssentialOCL_CollectionItem_CollectionLiteralPart, gen_EssentialOCL_CollectionRange_CollectionLiteralPart, gen_EssentialOCL_EnumLiteralExp_LiteralExp, gen_EssentialOCL_CollectionLiteralExp_LiteralExp, gen_EssentialOCL_FeatureCallExp_CallExp, gen_EssentialOCL_IfExp_OclExpression, gen_EssentialOCL_LiteralExp_OclExpression, gen_EssentialOCL_LoopExp_CallExp, gen_EssentialOCL_LoopExp_OclExpression, gen_EssentialOCL_NavigationCallExp_FeatureCallExp, gen_EssentialOCL_IntegerLiteralExp_NumericLiteralExp, gen_EssentialOCL_InvalidLiteralExp_LiteralExp, gen_EssentialOCL_IterateExp_LoopExp, gen_EssentialOCL_IteratorExp_LoopExp, gen_EssentialOCL_LetExp_OclExpression, gen_EssentialOCL_RealLiteralExp_NumericLiteralExp, gen_EssentialOCL_SequenceType_CollectionType, gen_EssentialOCL_SetType_CollectionType, gen_EssentialOCL_StringLiteralExp_PrimitiveLiteralExp, gen_EssentialOCL_TupleLiteralExp_LiteralExp, gen_EssentialOCL_NullLiteralExp_LiteralExp, gen_EssentialOCL_NumericLiteralExp_PrimitiveLiteralExp, gen_EssentialOCL_OperationCallExp_FeatureCallExp, gen_EssentialOCL_OrderedSetType_CollectionType, gen_EssentialOCL_PrimitiveLiteralExp_LiteralExp, gen_EssentialOCL_PropertyCallExp_NavigationCallExp, gen_EssentialOCL_VariableExp_OclExpression, gen_EssentialOCL_TypeExp_OclExpression, gen_EssentialOCL_UnlimitedNaturalExp_NumericLiteralExp},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)