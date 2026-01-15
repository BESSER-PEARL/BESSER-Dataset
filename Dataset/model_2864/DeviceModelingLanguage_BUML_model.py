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
deviceModelingLanguage_Decl = Class(name="deviceModelingLanguage::Decl")
deviceModelingLanguage_TypeDecl = Class(name="deviceModelingLanguage::TypeDecl")
Decl = Class(name="Decl")
deviceModelingLanguage_Model = Class(name="deviceModelingLanguage::Model")
deviceModelingLanguage_AttrDecl = Class(name="deviceModelingLanguage::AttrDecl")
MemberDecl = Class(name="MemberDecl")
Accessor = Class(name="Accessor")
deviceModelingLanguage_Modifier = Class(name="deviceModelingLanguage::Modifier")
deviceModelingLanguage_Type = Class(name="deviceModelingLanguage::Type")
deviceModelingLanguage_Literal = Class(name="deviceModelingLanguage::Literal")
deviceModelingLanguage_FeatureDecl = Class(name="deviceModelingLanguage::FeatureDecl")
deviceModelingLanguage_MemberDecl = Class(name="deviceModelingLanguage::MemberDecl")
deviceModelingLanguage_Device = Class(name="deviceModelingLanguage::Device")
deviceModelingLanguage_Assignment = Class(name="deviceModelingLanguage::Assignment")
deviceModelingLanguage_Exp = Class(name="deviceModelingLanguage::Exp")
deviceModelingLanguage_BaseFeatureType = Class(name="deviceModelingLanguage::BaseFeatureType")
FeatureType = Class(name="FeatureType")
deviceModelingLanguage_InvariantDecl = Class(name="deviceModelingLanguage::InvariantDecl")
deviceModelingLanguage_SubMemberDecl = Class(name="deviceModelingLanguage::SubMemberDecl")
deviceModelingLanguage_MModifier = Class(name="deviceModelingLanguage::MModifier")
deviceModelingLanguage_FeatureType = Class(name="deviceModelingLanguage::FeatureType")
deviceModelingLanguage_Report = Class(name="deviceModelingLanguage::Report")
FeatureDecl = Class(name="FeatureDecl")
deviceModelingLanguage_MultiplicityInvariant = Class(name="deviceModelingLanguage::MultiplicityInvariant")
InvariantDecl = Class(name="InvariantDecl")
deviceModelingLanguage_ConstraintNat = Class(name="deviceModelingLanguage::ConstraintNat")
deviceModelingLanguage_SubMemberMatch = Class(name="deviceModelingLanguage::SubMemberMatch")
deviceModelingLanguage_GeneralInvariant = Class(name="deviceModelingLanguage::GeneralInvariant")
deviceModelingLanguage_Primary = Class(name="deviceModelingLanguage::Primary")
deviceModelingLanguage_BaseType = Class(name="deviceModelingLanguage::BaseType")
Type = Class(name="Type")
deviceModelingLanguage_BasicLiteral = Class(name="deviceModelingLanguage::BasicLiteral")
Literal = Class(name="Literal")
deviceModelingLanguage_TupleLiteral = Class(name="deviceModelingLanguage::TupleLiteral")
deviceModelingLanguage_ConstraintExp = Class(name="deviceModelingLanguage::ConstraintExp")
deviceModelingLanguage_Param = Class(name="deviceModelingLanguage::Param")
deviceModelingLanguage_ReportMemberDecl = Class(name="deviceModelingLanguage::ReportMemberDecl")
deviceModelingLanguage_Accessor = Class(name="deviceModelingLanguage::Accessor")
deviceModelingLanguage_SimpleBasicLiteral = Class(name="deviceModelingLanguage::SimpleBasicLiteral")
SimpleLiteral = Class(name="SimpleLiteral")
deviceModelingLanguage_SimpleTupleLiteral = Class(name="deviceModelingLanguage::SimpleTupleLiteral")
deviceModelingLanguage_SimpleOptionLiteral = Class(name="deviceModelingLanguage::SimpleOptionLiteral")
deviceModelingLanguage_SimpleSeqLiteral = Class(name="deviceModelingLanguage::SimpleSeqLiteral")
deviceModelingLanguage_SeqLiteral = Class(name="deviceModelingLanguage::SeqLiteral")
deviceModelingLanguage_SimpleLiteral = Class(name="deviceModelingLanguage::SimpleLiteral")
deviceModelingLanguage_SetLiteral = Class(name="deviceModelingLanguage::SetLiteral")
deviceModelingLanguage_OptionLiteral = Class(name="deviceModelingLanguage::OptionLiteral")
deviceModelingLanguage_Val = Class(name="deviceModelingLanguage::Val")
deviceModelingLanguage_Var = Class(name="deviceModelingLanguage::Var")
deviceModelingLanguage_Override = Class(name="deviceModelingLanguage::Override")
deviceModelingLanguage_OptionFeatureType = Class(name="deviceModelingLanguage::OptionFeatureType")
deviceModelingLanguage_SimpleSetLiteral = Class(name="deviceModelingLanguage::SimpleSetLiteral")
deviceModelingLanguage_Feature = Class(name="deviceModelingLanguage::Feature")
deviceModelingLanguage_Data = Class(name="deviceModelingLanguage::Data")
MModifier = Class(name="MModifier")
deviceModelingLanguage_App = Class(name="deviceModelingLanguage::App")
deviceModelingLanguage_Const = Class(name="deviceModelingLanguage::Const")
Modifier = Class(name="Modifier")
deviceModelingLanguage_SeqFeatureType = Class(name="deviceModelingLanguage::SeqFeatureType")
deviceModelingLanguage_SetFeatureType = Class(name="deviceModelingLanguage::SetFeatureType")
deviceModelingLanguage_SomeFeatureType = Class(name="deviceModelingLanguage::SomeFeatureType")
deviceModelingLanguage_EitherFeatureType = Class(name="deviceModelingLanguage::EitherFeatureType")
deviceModelingLanguage_UnaryExp = Class(name="deviceModelingLanguage::UnaryExp")
deviceModelingLanguage_PrimaryExp = Class(name="deviceModelingLanguage::PrimaryExp")
deviceModelingLanguage_AccessExp = Class(name="deviceModelingLanguage::AccessExp")
deviceModelingLanguage_NumNatConstraint = Class(name="deviceModelingLanguage::NumNatConstraint")
ConstraintNat = Class(name="ConstraintNat")
deviceModelingLanguage_AnyNatConstraint = Class(name="deviceModelingLanguage::AnyNatConstraint")
deviceModelingLanguage_BinaryExp = Class(name="deviceModelingLanguage::BinaryExp")
Exp = Class(name="Exp")
deviceModelingLanguage_TupleType = Class(name="deviceModelingLanguage::TupleType")
BaseType = Class(name="BaseType")
deviceModelingLanguage_OptionType = Class(name="deviceModelingLanguage::OptionType")
deviceModelingLanguage_SomeType = Class(name="deviceModelingLanguage::SomeType")
deviceModelingLanguage_NameExp = Class(name="deviceModelingLanguage::NameExp")
Primary = Class(name="Primary")
deviceModelingLanguage_LiteralExp = Class(name="deviceModelingLanguage::LiteralExp")
deviceModelingLanguage_SeqType = Class(name="deviceModelingLanguage::SeqType")
deviceModelingLanguage_SetType = Class(name="deviceModelingLanguage::SetType")
deviceModelingLanguage_SimpleSomeLiteral = Class(name="deviceModelingLanguage::SimpleSomeLiteral")
deviceModelingLanguage_NoneType = Class(name="deviceModelingLanguage::NoneType")
deviceModelingLanguage_NoneLiteral = Class(name="deviceModelingLanguage::NoneLiteral")
OptionLiteral = Class(name="OptionLiteral")
deviceModelingLanguage_SomeLiteral = Class(name="deviceModelingLanguage::SomeLiteral")
deviceModelingLanguage_SimpleNoneLiteral = Class(name="deviceModelingLanguage::SimpleNoneLiteral")
SimpleOptionLiteral = Class(name="SimpleOptionLiteral")

# deviceModelingLanguage_Decl class attributes and methods
deviceModelingLanguage_Decl_name: Property = Property(name="name", type=StringType)
deviceModelingLanguage_Decl.attributes={deviceModelingLanguage_Decl_name}

# deviceModelingLanguage_TypeDecl class attributes and methods

# Decl class attributes and methods

# deviceModelingLanguage_Model class attributes and methods
deviceModelingLanguage_Model_schema: Property = Property(name="schema", type=BooleanType)
deviceModelingLanguage_Model_class: Property = Property(name="class", type=BooleanType)
deviceModelingLanguage_Model_product: Property = Property(name="product", type=BooleanType)
deviceModelingLanguage_Model.attributes={deviceModelingLanguage_Model_schema, deviceModelingLanguage_Model_class, deviceModelingLanguage_Model_product}

# deviceModelingLanguage_AttrDecl class attributes and methods
deviceModelingLanguage_AttrDecl_attributeName: Property = Property(name="attributeName", type=StringType)
deviceModelingLanguage_AttrDecl.attributes={deviceModelingLanguage_AttrDecl_attributeName}

# MemberDecl class attributes and methods

# Accessor class attributes and methods

# deviceModelingLanguage_Modifier class attributes and methods

# deviceModelingLanguage_Type class attributes and methods

# deviceModelingLanguage_Literal class attributes and methods

# deviceModelingLanguage_FeatureDecl class attributes and methods

# deviceModelingLanguage_MemberDecl class attributes and methods

# deviceModelingLanguage_Device class attributes and methods

# deviceModelingLanguage_Assignment class attributes and methods
deviceModelingLanguage_Assignment_name: Property = Property(name="name", type=StringType)
deviceModelingLanguage_Assignment.attributes={deviceModelingLanguage_Assignment_name}

# deviceModelingLanguage_Exp class attributes and methods

# deviceModelingLanguage_BaseFeatureType class attributes and methods

# FeatureType class attributes and methods

# deviceModelingLanguage_InvariantDecl class attributes and methods
deviceModelingLanguage_InvariantDecl_invName: Property = Property(name="invName", type=StringType)
deviceModelingLanguage_InvariantDecl.attributes={deviceModelingLanguage_InvariantDecl_invName}

# deviceModelingLanguage_SubMemberDecl class attributes and methods
deviceModelingLanguage_SubMemberDecl_name: Property = Property(name="name", type=StringType)
deviceModelingLanguage_SubMemberDecl.attributes={deviceModelingLanguage_SubMemberDecl_name}

# deviceModelingLanguage_MModifier class attributes and methods

# deviceModelingLanguage_FeatureType class attributes and methods

# deviceModelingLanguage_Report class attributes and methods
deviceModelingLanguage_Report_name: Property = Property(name="name", type=StringType)
deviceModelingLanguage_Report.attributes={deviceModelingLanguage_Report_name}

# FeatureDecl class attributes and methods

# deviceModelingLanguage_MultiplicityInvariant class attributes and methods

# InvariantDecl class attributes and methods

# deviceModelingLanguage_ConstraintNat class attributes and methods

# deviceModelingLanguage_SubMemberMatch class attributes and methods
deviceModelingLanguage_SubMemberMatch_qNames: Property = Property(name="qNames", type=StringType)
deviceModelingLanguage_SubMemberMatch_name: Property = Property(name="name", type=StringType)
deviceModelingLanguage_SubMemberMatch_any: Property = Property(name="any", type=StringType)
deviceModelingLanguage_SubMemberMatch.attributes={deviceModelingLanguage_SubMemberMatch_qNames, deviceModelingLanguage_SubMemberMatch_any, deviceModelingLanguage_SubMemberMatch_name}

# deviceModelingLanguage_GeneralInvariant class attributes and methods

# deviceModelingLanguage_Primary class attributes and methods

# deviceModelingLanguage_BaseType class attributes and methods

# Type class attributes and methods

# deviceModelingLanguage_BasicLiteral class attributes and methods
deviceModelingLanguage_BasicLiteral_lit: Property = Property(name="lit", type=StringType)
deviceModelingLanguage_BasicLiteral.attributes={deviceModelingLanguage_BasicLiteral_lit}

# Literal class attributes and methods

# deviceModelingLanguage_TupleLiteral class attributes and methods

# deviceModelingLanguage_ConstraintExp class attributes and methods

# deviceModelingLanguage_Param class attributes and methods
deviceModelingLanguage_Param_name: Property = Property(name="name", type=StringType)
deviceModelingLanguage_Param.attributes={deviceModelingLanguage_Param_name}

# deviceModelingLanguage_ReportMemberDecl class attributes and methods
deviceModelingLanguage_ReportMemberDecl_name: Property = Property(name="name", type=StringType)
deviceModelingLanguage_ReportMemberDecl.attributes={deviceModelingLanguage_ReportMemberDecl_name}

# deviceModelingLanguage_Accessor class attributes and methods

# deviceModelingLanguage_SimpleBasicLiteral class attributes and methods
deviceModelingLanguage_SimpleBasicLiteral_lit: Property = Property(name="lit", type=StringType)
deviceModelingLanguage_SimpleBasicLiteral.attributes={deviceModelingLanguage_SimpleBasicLiteral_lit}

# SimpleLiteral class attributes and methods

# deviceModelingLanguage_SimpleTupleLiteral class attributes and methods

# deviceModelingLanguage_SimpleOptionLiteral class attributes and methods

# deviceModelingLanguage_SimpleSeqLiteral class attributes and methods

# deviceModelingLanguage_SeqLiteral class attributes and methods

# deviceModelingLanguage_SimpleLiteral class attributes and methods

# deviceModelingLanguage_SetLiteral class attributes and methods

# deviceModelingLanguage_OptionLiteral class attributes and methods

# deviceModelingLanguage_Val class attributes and methods

# deviceModelingLanguage_Var class attributes and methods

# deviceModelingLanguage_Override class attributes and methods

# deviceModelingLanguage_OptionFeatureType class attributes and methods
deviceModelingLanguage_OptionFeatureType_none: Property = Property(name="none", type=BooleanType)
deviceModelingLanguage_OptionFeatureType.attributes={deviceModelingLanguage_OptionFeatureType_none}

# deviceModelingLanguage_SimpleSetLiteral class attributes and methods

# deviceModelingLanguage_Feature class attributes and methods
deviceModelingLanguage_Feature_schema: Property = Property(name="schema", type=BooleanType)
deviceModelingLanguage_Feature_class: Property = Property(name="class", type=BooleanType)
deviceModelingLanguage_Feature_product: Property = Property(name="product", type=BooleanType)
deviceModelingLanguage_Feature.attributes={deviceModelingLanguage_Feature_schema, deviceModelingLanguage_Feature_class, deviceModelingLanguage_Feature_product}

# deviceModelingLanguage_Data class attributes and methods

# MModifier class attributes and methods

# deviceModelingLanguage_App class attributes and methods

# deviceModelingLanguage_Const class attributes and methods
deviceModelingLanguage_Const_schema: Property = Property(name="schema", type=BooleanType)
deviceModelingLanguage_Const_class: Property = Property(name="class", type=BooleanType)
deviceModelingLanguage_Const_product: Property = Property(name="product", type=BooleanType)
deviceModelingLanguage_Const_instance: Property = Property(name="instance", type=BooleanType)
deviceModelingLanguage_Const.attributes={deviceModelingLanguage_Const_schema, deviceModelingLanguage_Const_product, deviceModelingLanguage_Const_class, deviceModelingLanguage_Const_instance}

# Modifier class attributes and methods

# deviceModelingLanguage_SeqFeatureType class attributes and methods

# deviceModelingLanguage_SetFeatureType class attributes and methods

# deviceModelingLanguage_SomeFeatureType class attributes and methods

# deviceModelingLanguage_EitherFeatureType class attributes and methods
deviceModelingLanguage_EitherFeatureType_choice: Property = Property(name="choice", type=StringType)
deviceModelingLanguage_EitherFeatureType.attributes={deviceModelingLanguage_EitherFeatureType_choice}

# deviceModelingLanguage_UnaryExp class attributes and methods
deviceModelingLanguage_UnaryExp_op: Property = Property(name="op", type=StringType)
deviceModelingLanguage_UnaryExp.attributes={deviceModelingLanguage_UnaryExp_op}

# deviceModelingLanguage_PrimaryExp class attributes and methods

# deviceModelingLanguage_AccessExp class attributes and methods

# deviceModelingLanguage_NumNatConstraint class attributes and methods
deviceModelingLanguage_NumNatConstraint_num: Property = Property(name="num", type=StringType)
deviceModelingLanguage_NumNatConstraint.attributes={deviceModelingLanguage_NumNatConstraint_num}

# ConstraintNat class attributes and methods

# deviceModelingLanguage_AnyNatConstraint class attributes and methods

# deviceModelingLanguage_BinaryExp class attributes and methods
deviceModelingLanguage_BinaryExp_op: Property = Property(name="op", type=StringType)
deviceModelingLanguage_BinaryExp.attributes={deviceModelingLanguage_BinaryExp_op}

# Exp class attributes and methods

# deviceModelingLanguage_TupleType class attributes and methods

# BaseType class attributes and methods

# deviceModelingLanguage_OptionType class attributes and methods

# deviceModelingLanguage_SomeType class attributes and methods

# deviceModelingLanguage_NameExp class attributes and methods
deviceModelingLanguage_NameExp_id: Property = Property(name="id", type=StringType)
deviceModelingLanguage_NameExp.attributes={deviceModelingLanguage_NameExp_id}

# Primary class attributes and methods

# deviceModelingLanguage_LiteralExp class attributes and methods

# deviceModelingLanguage_SeqType class attributes and methods

# deviceModelingLanguage_SetType class attributes and methods

# deviceModelingLanguage_SimpleSomeLiteral class attributes and methods

# deviceModelingLanguage_NoneType class attributes and methods

# deviceModelingLanguage_NoneLiteral class attributes and methods

# OptionLiteral class attributes and methods

# deviceModelingLanguage_SomeLiteral class attributes and methods

# deviceModelingLanguage_SimpleNoneLiteral class attributes and methods

# SimpleOptionLiteral class attributes and methods

# Relationships
decls0: BinaryAssociation = BinaryAssociation(
    name="decls0",
    ends={
        Property(name="deviceModelingLanguage_Decl", type=deviceModelingLanguage_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_Model", type=deviceModelingLanguage_Decl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifier13: BinaryAssociation = BinaryAssociation(
    name="modifier13",
    ends={
        Property(name="deviceModelingLanguage_Modifier", type=deviceModelingLanguage_AttrDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_AttrDecl", type=deviceModelingLanguage_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type14: BinaryAssociation = BinaryAssociation(
    name="type14",
    ends={
        Property(name="deviceModelingLanguage_Type", type=deviceModelingLanguage_AttrDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_AttrDecl15", type=deviceModelingLanguage_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
literal16: BinaryAssociation = BinaryAssociation(
    name="literal16",
    ends={
        Property(name="deviceModelingLanguage_Literal", type=deviceModelingLanguage_AttrDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_AttrDecl17", type=deviceModelingLanguage_Literal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
supers2: BinaryAssociation = BinaryAssociation(
    name="supers2",
    ends={
        Property(name="deviceModelingLanguage_TypeDecl", type=deviceModelingLanguage_TypeDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_TypeDecl1", type=deviceModelingLanguage_TypeDecl, multiplicity=Multiplicity(0, 9999))
    }
)
supers4: BinaryAssociation = BinaryAssociation(
    name="supers4",
    ends={
        Property(name="deviceModelingLanguage_FeatureDecl", type=deviceModelingLanguage_FeatureDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_FeatureDecl3", type=deviceModelingLanguage_FeatureDecl, multiplicity=Multiplicity(0, 9999))
    }
)
members5: BinaryAssociation = BinaryAssociation(
    name="members5",
    ends={
        Property(name="deviceModelingLanguage_MemberDecl", type=deviceModelingLanguage_FeatureDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_FeatureDecl6", type=deviceModelingLanguage_MemberDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
devices7: BinaryAssociation = BinaryAssociation(
    name="devices7",
    ends={
        Property(name="deviceModelingLanguage_Device", type=deviceModelingLanguage_FeatureDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_FeatureDecl8", type=deviceModelingLanguage_Device, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assigns9: BinaryAssociation = BinaryAssociation(
    name="assigns9",
    ends={
        Property(name="deviceModelingLanguage_Assignment", type=deviceModelingLanguage_FeatureDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_FeatureDecl10", type=deviceModelingLanguage_Assignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp11: BinaryAssociation = BinaryAssociation(
    name="exp11",
    ends={
        Property(name="deviceModelingLanguage_Exp", type=deviceModelingLanguage_FeatureDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_FeatureDecl12", type=deviceModelingLanguage_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args24: BinaryAssociation = BinaryAssociation(
    name="args24",
    ends={
        Property(name="deviceModelingLanguage_Exp25", type=deviceModelingLanguage_Report, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_Report", type=deviceModelingLanguage_Exp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
components26: BinaryAssociation = BinaryAssociation(
    name="components26",
    ends={
        Property(name="deviceModelingLanguage_FeatureDecl27", type=deviceModelingLanguage_BaseFeatureType, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_BaseFeatureType", type=deviceModelingLanguage_FeatureDecl, multiplicity=Multiplicity(0, 9999))
    }
)
members28: BinaryAssociation = BinaryAssociation(
    name="members28",
    ends={
        Property(name="deviceModelingLanguage_MemberDecl30", type=deviceModelingLanguage_BaseFeatureType, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_BaseFeatureType29", type=deviceModelingLanguage_MemberDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifier18: BinaryAssociation = BinaryAssociation(
    name="modifier18",
    ends={
        Property(name="deviceModelingLanguage_MModifier", type=deviceModelingLanguage_SubMemberDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_SubMemberDecl", type=deviceModelingLanguage_MModifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type19: BinaryAssociation = BinaryAssociation(
    name="type19",
    ends={
        Property(name="deviceModelingLanguage_FeatureType", type=deviceModelingLanguage_SubMemberDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_SubMemberDecl20", type=deviceModelingLanguage_FeatureType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp21: BinaryAssociation = BinaryAssociation(
    name="exp21",
    ends={
        Property(name="deviceModelingLanguage_Exp23", type=deviceModelingLanguage_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_Assignment22", type=deviceModelingLanguage_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp40: BinaryAssociation = BinaryAssociation(
    name="exp40",
    ends={
        Property(name="deviceModelingLanguage_Exp41", type=deviceModelingLanguage_GeneralInvariant, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_GeneralInvariant", type=deviceModelingLanguage_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
components42: BinaryAssociation = BinaryAssociation(
    name="components42",
    ends={
        Property(name="deviceModelingLanguage_FeatureDecl44", type=deviceModelingLanguage_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_Device43", type=deviceModelingLanguage_FeatureDecl, multiplicity=Multiplicity(0, 9999))
    }
)
lo31: BinaryAssociation = BinaryAssociation(
    name="lo31",
    ends={
        Property(name="deviceModelingLanguage_ConstraintNat", type=deviceModelingLanguage_MultiplicityInvariant, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_MultiplicityInvariant", type=deviceModelingLanguage_ConstraintNat, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
hi32: BinaryAssociation = BinaryAssociation(
    name="hi32",
    ends={
        Property(name="deviceModelingLanguage_ConstraintNat34", type=deviceModelingLanguage_MultiplicityInvariant, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_MultiplicityInvariant33", type=deviceModelingLanguage_ConstraintNat, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
match35: BinaryAssociation = BinaryAssociation(
    name="match35",
    ends={
        Property(name="deviceModelingLanguage_SubMemberMatch", type=deviceModelingLanguage_MultiplicityInvariant, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_MultiplicityInvariant36", type=deviceModelingLanguage_SubMemberMatch, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type37: BinaryAssociation = BinaryAssociation(
    name="type37",
    ends={
        Property(name="deviceModelingLanguage_FeatureDecl39", type=deviceModelingLanguage_MultiplicityInvariant, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_MultiplicityInvariant38", type=deviceModelingLanguage_FeatureDecl, multiplicity=Multiplicity(0, 1))
    }
)
type53: BinaryAssociation = BinaryAssociation(
    name="type53",
    ends={
        Property(name="deviceModelingLanguage_TypeDecl54", type=deviceModelingLanguage_BaseType, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_BaseType", type=deviceModelingLanguage_TypeDecl, multiplicity=Multiplicity(0, 1))
    }
)
typeCons55: BinaryAssociation = BinaryAssociation(
    name="typeCons55",
    ends={
        Property(name="deviceModelingLanguage_TypeDecl56", type=deviceModelingLanguage_BasicLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_BasicLiteral", type=deviceModelingLanguage_TypeDecl, multiplicity=Multiplicity(0, 1))
    }
)
constraint45: BinaryAssociation = BinaryAssociation(
    name="constraint45",
    ends={
        Property(name="deviceModelingLanguage_ConstraintExp", type=deviceModelingLanguage_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_Device46", type=deviceModelingLanguage_ConstraintExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cond47: BinaryAssociation = BinaryAssociation(
    name="cond47",
    ends={
        Property(name="deviceModelingLanguage_Exp49", type=deviceModelingLanguage_ConstraintExp, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_ConstraintExp48", type=deviceModelingLanguage_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type50: BinaryAssociation = BinaryAssociation(
    name="type50",
    ends={
        Property(name="deviceModelingLanguage_BaseFeatureType51", type=deviceModelingLanguage_Param, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_Param", type=deviceModelingLanguage_BaseFeatureType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bindingName52: BinaryAssociation = BinaryAssociation(
    name="bindingName52",
    ends={
        Property(name="deviceModelingLanguage_Accessor", type=deviceModelingLanguage_ReportMemberDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_ReportMemberDecl", type=deviceModelingLanguage_Accessor, multiplicity=Multiplicity(0, 9999))
    }
)
elems68: BinaryAssociation = BinaryAssociation(
    name="elems68",
    ends={
        Property(name="deviceModelingLanguage_SimpleLiteral69", type=deviceModelingLanguage_SimpleTupleLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_SimpleTupleLiteral", type=deviceModelingLanguage_SimpleLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elems57: BinaryAssociation = BinaryAssociation(
    name="elems57",
    ends={
        Property(name="deviceModelingLanguage_Literal58", type=deviceModelingLanguage_TupleLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_TupleLiteral", type=deviceModelingLanguage_Literal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elementType59: BinaryAssociation = BinaryAssociation(
    name="elementType59",
    ends={
        Property(name="deviceModelingLanguage_Type60", type=deviceModelingLanguage_SeqLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_SeqLiteral", type=deviceModelingLanguage_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elems61: BinaryAssociation = BinaryAssociation(
    name="elems61",
    ends={
        Property(name="deviceModelingLanguage_SimpleLiteral", type=deviceModelingLanguage_SeqLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_SeqLiteral62", type=deviceModelingLanguage_SimpleLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elementType63: BinaryAssociation = BinaryAssociation(
    name="elementType63",
    ends={
        Property(name="deviceModelingLanguage_Type64", type=deviceModelingLanguage_SetLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_SetLiteral", type=deviceModelingLanguage_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elems65: BinaryAssociation = BinaryAssociation(
    name="elems65",
    ends={
        Property(name="deviceModelingLanguage_SimpleLiteral67", type=deviceModelingLanguage_SetLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_SetLiteral66", type=deviceModelingLanguage_SimpleLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elems70: BinaryAssociation = BinaryAssociation(
    name="elems70",
    ends={
        Property(name="deviceModelingLanguage_SimpleLiteral71", type=deviceModelingLanguage_SimpleSeqLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_SimpleSeqLiteral", type=deviceModelingLanguage_SimpleLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elems72: BinaryAssociation = BinaryAssociation(
    name="elems72",
    ends={
        Property(name="deviceModelingLanguage_SimpleLiteral73", type=deviceModelingLanguage_SimpleSetLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_SimpleSetLiteral", type=deviceModelingLanguage_SimpleLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members83: BinaryAssociation = BinaryAssociation(
    name="members83",
    ends={
        Property(name="deviceModelingLanguage_MemberDecl85", type=deviceModelingLanguage_EitherFeatureType, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_EitherFeatureType84", type=deviceModelingLanguage_MemberDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
base86: BinaryAssociation = BinaryAssociation(
    name="base86",
    ends={
        Property(name="deviceModelingLanguage_BaseFeatureType87", type=deviceModelingLanguage_SeqFeatureType, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_SeqFeatureType", type=deviceModelingLanguage_BaseFeatureType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements88: BinaryAssociation = BinaryAssociation(
    name="elements88",
    ends={
        Property(name="deviceModelingLanguage_BaseFeatureType90", type=deviceModelingLanguage_SeqFeatureType, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_SeqFeatureType89", type=deviceModelingLanguage_BaseFeatureType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
base91: BinaryAssociation = BinaryAssociation(
    name="base91",
    ends={
        Property(name="deviceModelingLanguage_BaseFeatureType92", type=deviceModelingLanguage_SetFeatureType, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_SetFeatureType", type=deviceModelingLanguage_BaseFeatureType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base74: BinaryAssociation = BinaryAssociation(
    name="base74",
    ends={
        Property(name="deviceModelingLanguage_BaseFeatureType75", type=deviceModelingLanguage_OptionFeatureType, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_OptionFeatureType", type=deviceModelingLanguage_BaseFeatureType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base76: BinaryAssociation = BinaryAssociation(
    name="base76",
    ends={
        Property(name="deviceModelingLanguage_BaseFeatureType77", type=deviceModelingLanguage_SomeFeatureType, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_SomeFeatureType", type=deviceModelingLanguage_BaseFeatureType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
members78: BinaryAssociation = BinaryAssociation(
    name="members78",
    ends={
        Property(name="deviceModelingLanguage_MemberDecl80", type=deviceModelingLanguage_SomeFeatureType, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_SomeFeatureType79", type=deviceModelingLanguage_MemberDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bases81: BinaryAssociation = BinaryAssociation(
    name="bases81",
    ends={
        Property(name="deviceModelingLanguage_BaseFeatureType82", type=deviceModelingLanguage_EitherFeatureType, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_EitherFeatureType", type=deviceModelingLanguage_BaseFeatureType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arg101: BinaryAssociation = BinaryAssociation(
    name="arg101",
    ends={
        Property(name="deviceModelingLanguage_Exp102", type=deviceModelingLanguage_UnaryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_UnaryExp", type=deviceModelingLanguage_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
primary103: BinaryAssociation = BinaryAssociation(
    name="primary103",
    ends={
        Property(name="deviceModelingLanguage_Primary", type=deviceModelingLanguage_PrimaryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_PrimaryExp", type=deviceModelingLanguage_Primary, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base104: BinaryAssociation = BinaryAssociation(
    name="base104",
    ends={
        Property(name="deviceModelingLanguage_PrimaryExp105", type=deviceModelingLanguage_AccessExp, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_AccessExp", type=deviceModelingLanguage_PrimaryExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements93: BinaryAssociation = BinaryAssociation(
    name="elements93",
    ends={
        Property(name="deviceModelingLanguage_BaseFeatureType95", type=deviceModelingLanguage_SetFeatureType, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_SetFeatureType94", type=deviceModelingLanguage_BaseFeatureType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left96: BinaryAssociation = BinaryAssociation(
    name="left96",
    ends={
        Property(name="deviceModelingLanguage_Exp97", type=deviceModelingLanguage_BinaryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_BinaryExp", type=deviceModelingLanguage_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right98: BinaryAssociation = BinaryAssociation(
    name="right98",
    ends={
        Property(name="deviceModelingLanguage_Exp100", type=deviceModelingLanguage_BinaryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_BinaryExp99", type=deviceModelingLanguage_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base113: BinaryAssociation = BinaryAssociation(
    name="base113",
    ends={
        Property(name="deviceModelingLanguage_Type114", type=deviceModelingLanguage_SetType, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_SetType", type=deviceModelingLanguage_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elemTypes115: BinaryAssociation = BinaryAssociation(
    name="elemTypes115",
    ends={
        Property(name="deviceModelingLanguage_Type116", type=deviceModelingLanguage_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_TupleType", type=deviceModelingLanguage_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
base117: BinaryAssociation = BinaryAssociation(
    name="base117",
    ends={
        Property(name="deviceModelingLanguage_Type118", type=deviceModelingLanguage_OptionType, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_OptionType", type=deviceModelingLanguage_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base119: BinaryAssociation = BinaryAssociation(
    name="base119",
    ends={
        Property(name="deviceModelingLanguage_Type120", type=deviceModelingLanguage_SomeType, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_SomeType", type=deviceModelingLanguage_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accessor106: BinaryAssociation = BinaryAssociation(
    name="accessor106",
    ends={
        Property(name="deviceModelingLanguage_Accessor108", type=deviceModelingLanguage_AccessExp, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_AccessExp107", type=deviceModelingLanguage_Accessor, multiplicity=Multiplicity(0, 1))
    }
)
lit109: BinaryAssociation = BinaryAssociation(
    name="lit109",
    ends={
        Property(name="deviceModelingLanguage_BasicLiteral110", type=deviceModelingLanguage_LiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_LiteralExp", type=deviceModelingLanguage_BasicLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base111: BinaryAssociation = BinaryAssociation(
    name="base111",
    ends={
        Property(name="deviceModelingLanguage_Type112", type=deviceModelingLanguage_SeqType, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_SeqType", type=deviceModelingLanguage_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lit127: BinaryAssociation = BinaryAssociation(
    name="lit127",
    ends={
        Property(name="deviceModelingLanguage_SimpleLiteral128", type=deviceModelingLanguage_SimpleSomeLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_SimpleSomeLiteral", type=deviceModelingLanguage_SimpleLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base121: BinaryAssociation = BinaryAssociation(
    name="base121",
    ends={
        Property(name="deviceModelingLanguage_Type122", type=deviceModelingLanguage_NoneType, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_NoneType", type=deviceModelingLanguage_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type123: BinaryAssociation = BinaryAssociation(
    name="type123",
    ends={
        Property(name="deviceModelingLanguage_Type124", type=deviceModelingLanguage_NoneLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_NoneLiteral", type=deviceModelingLanguage_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lit125: BinaryAssociation = BinaryAssociation(
    name="lit125",
    ends={
        Property(name="deviceModelingLanguage_Literal126", type=deviceModelingLanguage_SomeLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="deviceModelingLanguage_SomeLiteral", type=deviceModelingLanguage_Literal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_deviceModelingLanguage_TypeDecl_Decl = Generalization(general=Decl, specific=deviceModelingLanguage_TypeDecl)
gen_deviceModelingLanguage_AttrDecl_MemberDecl = Generalization(general=MemberDecl, specific=deviceModelingLanguage_AttrDecl)
gen_deviceModelingLanguage_AttrDecl_Accessor = Generalization(general=Accessor, specific=deviceModelingLanguage_AttrDecl)
gen_deviceModelingLanguage_FeatureDecl_Decl = Generalization(general=Decl, specific=deviceModelingLanguage_FeatureDecl)
gen_deviceModelingLanguage_BaseFeatureType_FeatureType = Generalization(general=FeatureType, specific=deviceModelingLanguage_BaseFeatureType)
gen_deviceModelingLanguage_InvariantDecl_MemberDecl = Generalization(general=MemberDecl, specific=deviceModelingLanguage_InvariantDecl)
gen_deviceModelingLanguage_SubMemberDecl_MemberDecl = Generalization(general=MemberDecl, specific=deviceModelingLanguage_SubMemberDecl)
gen_deviceModelingLanguage_SubMemberDecl_Accessor = Generalization(general=Accessor, specific=deviceModelingLanguage_SubMemberDecl)
gen_deviceModelingLanguage_Device_FeatureDecl = Generalization(general=FeatureDecl, specific=deviceModelingLanguage_Device)
gen_deviceModelingLanguage_MultiplicityInvariant_InvariantDecl = Generalization(general=InvariantDecl, specific=deviceModelingLanguage_MultiplicityInvariant)
gen_deviceModelingLanguage_GeneralInvariant_InvariantDecl = Generalization(general=InvariantDecl, specific=deviceModelingLanguage_GeneralInvariant)
gen_deviceModelingLanguage_BaseType_Type = Generalization(general=Type, specific=deviceModelingLanguage_BaseType)
gen_deviceModelingLanguage_BasicLiteral_Literal = Generalization(general=Literal, specific=deviceModelingLanguage_BasicLiteral)
gen_deviceModelingLanguage_TupleLiteral_Literal = Generalization(general=Literal, specific=deviceModelingLanguage_TupleLiteral)
gen_deviceModelingLanguage_SimpleBasicLiteral_SimpleLiteral = Generalization(general=SimpleLiteral, specific=deviceModelingLanguage_SimpleBasicLiteral)
gen_deviceModelingLanguage_SimpleTupleLiteral_SimpleLiteral = Generalization(general=SimpleLiteral, specific=deviceModelingLanguage_SimpleTupleLiteral)
gen_deviceModelingLanguage_SimpleOptionLiteral_SimpleLiteral = Generalization(general=SimpleLiteral, specific=deviceModelingLanguage_SimpleOptionLiteral)
gen_deviceModelingLanguage_SimpleSeqLiteral_SimpleLiteral = Generalization(general=SimpleLiteral, specific=deviceModelingLanguage_SimpleSeqLiteral)
gen_deviceModelingLanguage_SeqLiteral_Literal = Generalization(general=Literal, specific=deviceModelingLanguage_SeqLiteral)
gen_deviceModelingLanguage_SetLiteral_Literal = Generalization(general=Literal, specific=deviceModelingLanguage_SetLiteral)
gen_deviceModelingLanguage_OptionLiteral_Literal = Generalization(general=Literal, specific=deviceModelingLanguage_OptionLiteral)
gen_deviceModelingLanguage_Val_Modifier = Generalization(general=Modifier, specific=deviceModelingLanguage_Val)
gen_deviceModelingLanguage_Val_MModifier = Generalization(general=MModifier, specific=deviceModelingLanguage_Val)
gen_deviceModelingLanguage_Var_Modifier = Generalization(general=Modifier, specific=deviceModelingLanguage_Var)
gen_deviceModelingLanguage_Var_MModifier = Generalization(general=MModifier, specific=deviceModelingLanguage_Var)
gen_deviceModelingLanguage_Override_Modifier = Generalization(general=Modifier, specific=deviceModelingLanguage_Override)
gen_deviceModelingLanguage_Override_MModifier = Generalization(general=MModifier, specific=deviceModelingLanguage_Override)
gen_deviceModelingLanguage_OptionFeatureType_FeatureType = Generalization(general=FeatureType, specific=deviceModelingLanguage_OptionFeatureType)
gen_deviceModelingLanguage_SimpleSetLiteral_SimpleLiteral = Generalization(general=SimpleLiteral, specific=deviceModelingLanguage_SimpleSetLiteral)
gen_deviceModelingLanguage_Feature_FeatureDecl = Generalization(general=FeatureDecl, specific=deviceModelingLanguage_Feature)
gen_deviceModelingLanguage_Data_FeatureDecl = Generalization(general=FeatureDecl, specific=deviceModelingLanguage_Data)
gen_deviceModelingLanguage_Data_MModifier = Generalization(general=MModifier, specific=deviceModelingLanguage_Data)
gen_deviceModelingLanguage_App_FeatureDecl = Generalization(general=FeatureDecl, specific=deviceModelingLanguage_App)
gen_deviceModelingLanguage_Const_Modifier = Generalization(general=Modifier, specific=deviceModelingLanguage_Const)
gen_deviceModelingLanguage_Const_MModifier = Generalization(general=MModifier, specific=deviceModelingLanguage_Const)
gen_deviceModelingLanguage_SeqFeatureType_FeatureType = Generalization(general=FeatureType, specific=deviceModelingLanguage_SeqFeatureType)
gen_deviceModelingLanguage_SetFeatureType_FeatureType = Generalization(general=FeatureType, specific=deviceModelingLanguage_SetFeatureType)
gen_deviceModelingLanguage_SomeFeatureType_FeatureType = Generalization(general=FeatureType, specific=deviceModelingLanguage_SomeFeatureType)
gen_deviceModelingLanguage_EitherFeatureType_FeatureType = Generalization(general=FeatureType, specific=deviceModelingLanguage_EitherFeatureType)
gen_deviceModelingLanguage_UnaryExp_Exp = Generalization(general=Exp, specific=deviceModelingLanguage_UnaryExp)
gen_deviceModelingLanguage_PrimaryExp_Exp = Generalization(general=Exp, specific=deviceModelingLanguage_PrimaryExp)
gen_deviceModelingLanguage_AccessExp_Exp = Generalization(general=Exp, specific=deviceModelingLanguage_AccessExp)
gen_deviceModelingLanguage_NumNatConstraint_ConstraintNat = Generalization(general=ConstraintNat, specific=deviceModelingLanguage_NumNatConstraint)
gen_deviceModelingLanguage_AnyNatConstraint_ConstraintNat = Generalization(general=ConstraintNat, specific=deviceModelingLanguage_AnyNatConstraint)
gen_deviceModelingLanguage_BinaryExp_Exp = Generalization(general=Exp, specific=deviceModelingLanguage_BinaryExp)
gen_deviceModelingLanguage_TupleType_BaseType = Generalization(general=BaseType, specific=deviceModelingLanguage_TupleType)
gen_deviceModelingLanguage_OptionType_BaseType = Generalization(general=BaseType, specific=deviceModelingLanguage_OptionType)
gen_deviceModelingLanguage_SomeType_BaseType = Generalization(general=BaseType, specific=deviceModelingLanguage_SomeType)
gen_deviceModelingLanguage_NameExp_Primary = Generalization(general=Primary, specific=deviceModelingLanguage_NameExp)
gen_deviceModelingLanguage_LiteralExp_Primary = Generalization(general=Primary, specific=deviceModelingLanguage_LiteralExp)
gen_deviceModelingLanguage_SeqType_Type = Generalization(general=Type, specific=deviceModelingLanguage_SeqType)
gen_deviceModelingLanguage_SetType_Type = Generalization(general=Type, specific=deviceModelingLanguage_SetType)
gen_deviceModelingLanguage_SimpleSomeLiteral_SimpleOptionLiteral = Generalization(general=SimpleOptionLiteral, specific=deviceModelingLanguage_SimpleSomeLiteral)
gen_deviceModelingLanguage_NoneType_BaseType = Generalization(general=BaseType, specific=deviceModelingLanguage_NoneType)
gen_deviceModelingLanguage_NoneLiteral_OptionLiteral = Generalization(general=OptionLiteral, specific=deviceModelingLanguage_NoneLiteral)
gen_deviceModelingLanguage_SomeLiteral_OptionLiteral = Generalization(general=OptionLiteral, specific=deviceModelingLanguage_SomeLiteral)
gen_deviceModelingLanguage_SimpleNoneLiteral_SimpleOptionLiteral = Generalization(general=SimpleOptionLiteral, specific=deviceModelingLanguage_SimpleNoneLiteral)

# Domain Model
domain_model = DomainModel(
    name="deviceModelingLanguage",
    types={deviceModelingLanguage_Decl, deviceModelingLanguage_TypeDecl, Decl, deviceModelingLanguage_Model, deviceModelingLanguage_AttrDecl, MemberDecl, Accessor, deviceModelingLanguage_Modifier, deviceModelingLanguage_Type, deviceModelingLanguage_Literal, deviceModelingLanguage_FeatureDecl, deviceModelingLanguage_MemberDecl, deviceModelingLanguage_Device, deviceModelingLanguage_Assignment, deviceModelingLanguage_Exp, deviceModelingLanguage_BaseFeatureType, FeatureType, deviceModelingLanguage_InvariantDecl, deviceModelingLanguage_SubMemberDecl, deviceModelingLanguage_MModifier, deviceModelingLanguage_FeatureType, deviceModelingLanguage_Report, FeatureDecl, deviceModelingLanguage_MultiplicityInvariant, InvariantDecl, deviceModelingLanguage_ConstraintNat, deviceModelingLanguage_SubMemberMatch, deviceModelingLanguage_GeneralInvariant, deviceModelingLanguage_Primary, deviceModelingLanguage_BaseType, Type, deviceModelingLanguage_BasicLiteral, Literal, deviceModelingLanguage_TupleLiteral, deviceModelingLanguage_ConstraintExp, deviceModelingLanguage_Param, deviceModelingLanguage_ReportMemberDecl, deviceModelingLanguage_Accessor, deviceModelingLanguage_SimpleBasicLiteral, SimpleLiteral, deviceModelingLanguage_SimpleTupleLiteral, deviceModelingLanguage_SimpleOptionLiteral, deviceModelingLanguage_SimpleSeqLiteral, deviceModelingLanguage_SeqLiteral, deviceModelingLanguage_SimpleLiteral, deviceModelingLanguage_SetLiteral, deviceModelingLanguage_OptionLiteral, deviceModelingLanguage_Val, deviceModelingLanguage_Var, deviceModelingLanguage_Override, deviceModelingLanguage_OptionFeatureType, deviceModelingLanguage_SimpleSetLiteral, deviceModelingLanguage_Feature, deviceModelingLanguage_Data, MModifier, deviceModelingLanguage_App, deviceModelingLanguage_Const, Modifier, deviceModelingLanguage_SeqFeatureType, deviceModelingLanguage_SetFeatureType, deviceModelingLanguage_SomeFeatureType, deviceModelingLanguage_EitherFeatureType, deviceModelingLanguage_UnaryExp, deviceModelingLanguage_PrimaryExp, deviceModelingLanguage_AccessExp, deviceModelingLanguage_NumNatConstraint, ConstraintNat, deviceModelingLanguage_AnyNatConstraint, deviceModelingLanguage_BinaryExp, Exp, deviceModelingLanguage_TupleType, BaseType, deviceModelingLanguage_OptionType, deviceModelingLanguage_SomeType, deviceModelingLanguage_NameExp, Primary, deviceModelingLanguage_LiteralExp, deviceModelingLanguage_SeqType, deviceModelingLanguage_SetType, deviceModelingLanguage_SimpleSomeLiteral, deviceModelingLanguage_NoneType, deviceModelingLanguage_NoneLiteral, OptionLiteral, deviceModelingLanguage_SomeLiteral, deviceModelingLanguage_SimpleNoneLiteral, SimpleOptionLiteral},
    associations={decls0, modifier13, type14, literal16, supers2, supers4, members5, devices7, assigns9, exp11, args24, components26, members28, modifier18, type19, exp21, exp40, components42, lo31, hi32, match35, type37, type53, typeCons55, constraint45, cond47, type50, bindingName52, elems68, elems57, elementType59, elems61, elementType63, elems65, elems70, elems72, members83, base86, elements88, base91, base74, base76, members78, bases81, arg101, primary103, base104, elements93, left96, right98, base113, elemTypes115, base117, base119, accessor106, lit109, base111, lit127, base121, type123, lit125},
    generalizations={gen_deviceModelingLanguage_TypeDecl_Decl, gen_deviceModelingLanguage_AttrDecl_MemberDecl, gen_deviceModelingLanguage_AttrDecl_Accessor, gen_deviceModelingLanguage_FeatureDecl_Decl, gen_deviceModelingLanguage_BaseFeatureType_FeatureType, gen_deviceModelingLanguage_InvariantDecl_MemberDecl, gen_deviceModelingLanguage_SubMemberDecl_MemberDecl, gen_deviceModelingLanguage_SubMemberDecl_Accessor, gen_deviceModelingLanguage_Device_FeatureDecl, gen_deviceModelingLanguage_MultiplicityInvariant_InvariantDecl, gen_deviceModelingLanguage_GeneralInvariant_InvariantDecl, gen_deviceModelingLanguage_BaseType_Type, gen_deviceModelingLanguage_BasicLiteral_Literal, gen_deviceModelingLanguage_TupleLiteral_Literal, gen_deviceModelingLanguage_SimpleBasicLiteral_SimpleLiteral, gen_deviceModelingLanguage_SimpleTupleLiteral_SimpleLiteral, gen_deviceModelingLanguage_SimpleOptionLiteral_SimpleLiteral, gen_deviceModelingLanguage_SimpleSeqLiteral_SimpleLiteral, gen_deviceModelingLanguage_SeqLiteral_Literal, gen_deviceModelingLanguage_SetLiteral_Literal, gen_deviceModelingLanguage_OptionLiteral_Literal, gen_deviceModelingLanguage_Val_Modifier, gen_deviceModelingLanguage_Val_MModifier, gen_deviceModelingLanguage_Var_Modifier, gen_deviceModelingLanguage_Var_MModifier, gen_deviceModelingLanguage_Override_Modifier, gen_deviceModelingLanguage_Override_MModifier, gen_deviceModelingLanguage_OptionFeatureType_FeatureType, gen_deviceModelingLanguage_SimpleSetLiteral_SimpleLiteral, gen_deviceModelingLanguage_Feature_FeatureDecl, gen_deviceModelingLanguage_Data_FeatureDecl, gen_deviceModelingLanguage_Data_MModifier, gen_deviceModelingLanguage_App_FeatureDecl, gen_deviceModelingLanguage_Const_Modifier, gen_deviceModelingLanguage_Const_MModifier, gen_deviceModelingLanguage_SeqFeatureType_FeatureType, gen_deviceModelingLanguage_SetFeatureType_FeatureType, gen_deviceModelingLanguage_SomeFeatureType_FeatureType, gen_deviceModelingLanguage_EitherFeatureType_FeatureType, gen_deviceModelingLanguage_UnaryExp_Exp, gen_deviceModelingLanguage_PrimaryExp_Exp, gen_deviceModelingLanguage_AccessExp_Exp, gen_deviceModelingLanguage_NumNatConstraint_ConstraintNat, gen_deviceModelingLanguage_AnyNatConstraint_ConstraintNat, gen_deviceModelingLanguage_BinaryExp_Exp, gen_deviceModelingLanguage_TupleType_BaseType, gen_deviceModelingLanguage_OptionType_BaseType, gen_deviceModelingLanguage_SomeType_BaseType, gen_deviceModelingLanguage_NameExp_Primary, gen_deviceModelingLanguage_LiteralExp_Primary, gen_deviceModelingLanguage_SeqType_Type, gen_deviceModelingLanguage_SetType_Type, gen_deviceModelingLanguage_SimpleSomeLiteral_SimpleOptionLiteral, gen_deviceModelingLanguage_NoneType_BaseType, gen_deviceModelingLanguage_NoneLiteral_OptionLiteral, gen_deviceModelingLanguage_SomeLiteral_OptionLiteral, gen_deviceModelingLanguage_SimpleNoneLiteral_SimpleOptionLiteral},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)