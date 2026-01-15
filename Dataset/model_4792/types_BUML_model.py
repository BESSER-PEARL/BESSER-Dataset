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
types_UnionForwardDcl = Class(name="types::UnionForwardDcl")
types_Switch = Class(name="types::Switch")
FileRegion = Class(name="FileRegion")
types_IdlType = Class(name="types::IdlType")
types_Case = Class(name="types::Case")
types_CaseLabel = Class(name="types::CaseLabel", is_abstract=True)
types_ElementSpec = Class(name="types::ElementSpec")
types_DefaultCaseLabel = Class(name="types::DefaultCaseLabel")
CaseLabel = Class(name="CaseLabel")
types_ExprCaseLabel = Class(name="types::ExprCaseLabel")
types_Expression = Class(name="types::Expression")
types_TypeDef = Class(name="types::TypeDef")
TypedElement = Class(name="TypedElement")
IdlTypeDcl = Class(name="IdlTypeDcl")
types_VoidType = Class(name="types::VoidType")
IdlType = Class(name="IdlType")
types_UnionType = Class(name="types::UnionType")
types_Short = Class(name="types::Short")
PrimitiveType = Class(name="PrimitiveType")
types_Long = Class(name="types::Long")
types_Octet = Class(name="types::Octet")
types_Float = Class(name="types::Float")
types_Double = Class(name="types::Double")
types_IdlChar = Class(name="types::IdlChar")
types_IdlWChar = Class(name="types::IdlWChar")
types_WChar = Class(name="types::WChar")
types_Boolean = Class(name="types::Boolean")
types_LongLong = Class(name="types::LongLong")
types_LongDouble = Class(name="types::LongDouble")
types_UShort = Class(name="types::UShort")
types_ULong = Class(name="types::ULong")
types_ULongLong = Class(name="types::ULongLong")
types_Any = Class(name="types::Any")
types_IdlObject = Class(name="types::IdlObject")
types_Declarator = Class(name="types::Declarator")
types_EnumType = Class(name="types::EnumType")
types_Enumeration = Class(name="types::Enumeration")
types_StructType = Class(name="types::StructType")
MemberContainer = Class(name="MemberContainer")
types_ForwardDcl = Class(name="types::ForwardDcl")
types_StructForwardDcl = Class(name="types::StructForwardDcl")
types_TemplateType = Class(name="types::TemplateType", is_abstract=True)
types_SequenceType = Class(name="types::SequenceType")
TemplateType = Class(name="TemplateType")
Typed = Class(name="Typed")
types_IdlString = Class(name="types::IdlString")
types_WString = Class(name="types::WString")
types_PrimitiveType = Class(name="types::PrimitiveType")
types_FixedPtType = Class(name="types::FixedPtType")
types_ValueBaseType = Class(name="types::ValueBaseType")
Declarator = Class(name="Declarator")

# types_UnionForwardDcl class attributes and methods

# types_Switch class attributes and methods

# FileRegion class attributes and methods

# types_IdlType class attributes and methods

# types_Case class attributes and methods

# types_CaseLabel class attributes and methods

# types_ElementSpec class attributes and methods

# types_DefaultCaseLabel class attributes and methods

# CaseLabel class attributes and methods

# types_ExprCaseLabel class attributes and methods

# types_Expression class attributes and methods

# types_TypeDef class attributes and methods

# TypedElement class attributes and methods

# IdlTypeDcl class attributes and methods

# types_VoidType class attributes and methods

# IdlType class attributes and methods

# types_UnionType class attributes and methods

# types_Short class attributes and methods

# PrimitiveType class attributes and methods

# types_Long class attributes and methods

# types_Octet class attributes and methods

# types_Float class attributes and methods

# types_Double class attributes and methods

# types_IdlChar class attributes and methods

# types_IdlWChar class attributes and methods

# types_WChar class attributes and methods

# types_Boolean class attributes and methods

# types_LongLong class attributes and methods

# types_LongDouble class attributes and methods

# types_UShort class attributes and methods

# types_ULong class attributes and methods

# types_ULongLong class attributes and methods

# types_Any class attributes and methods

# types_IdlObject class attributes and methods

# types_Declarator class attributes and methods

# types_EnumType class attributes and methods

# types_Enumeration class attributes and methods

# types_StructType class attributes and methods

# MemberContainer class attributes and methods

# types_ForwardDcl class attributes and methods

# types_StructForwardDcl class attributes and methods

# types_TemplateType class attributes and methods

# types_SequenceType class attributes and methods

# TemplateType class attributes and methods

# Typed class attributes and methods

# types_IdlString class attributes and methods

# types_WString class attributes and methods

# types_PrimitiveType class attributes and methods

# types_FixedPtType class attributes and methods

# types_ValueBaseType class attributes and methods

# Declarator class attributes and methods

# Relationships
forwardDcl0: BinaryAssociation = BinaryAssociation(
    name="forwardDcl0",
    ends={
        Property(name="UnionForwardDcl", type=types_UnionType, multiplicity=Multiplicity(1, 1)),
        Property(name="implementation", type=types_UnionForwardDcl, multiplicity=Multiplicity(0, 1))
    }
)
idlSwitch1: BinaryAssociation = BinaryAssociation(
    name="idlSwitch1",
    ends={
        Property(name="types_Switch", type=types_UnionType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_UnionType", type=types_Switch, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type2: BinaryAssociation = BinaryAssociation(
    name="type2",
    ends={
        Property(name="types_IdlType", type=types_Switch, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Switch3", type=types_IdlType, multiplicity=Multiplicity(0, 1))
    }
)
cases4: BinaryAssociation = BinaryAssociation(
    name="cases4",
    ends={
        Property(name="types_Case", type=types_Switch, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Switch5", type=types_Case, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
labels6: BinaryAssociation = BinaryAssociation(
    name="labels6",
    ends={
        Property(name="types_CaseLabel", type=types_Case, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Case7", type=types_CaseLabel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
spec8: BinaryAssociation = BinaryAssociation(
    name="spec8",
    ends={
        Property(name="types_ElementSpec", type=types_Case, multiplicity=Multiplicity(1, 1)),
        Property(name="types_Case9", type=types_ElementSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr10: BinaryAssociation = BinaryAssociation(
    name="expr10",
    ends={
        Property(name="types_Expression", type=types_ExprCaseLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="types_ExprCaseLabel", type=types_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
implementation22: BinaryAssociation = BinaryAssociation(
    name="implementation22",
    ends={
        Property(name="UnionType", type=types_UnionForwardDcl, multiplicity=Multiplicity(1, 1)),
        Property(name="forwardDcl", type=types_UnionType, multiplicity=Multiplicity(0, 1))
    }
)
type11: BinaryAssociation = BinaryAssociation(
    name="type11",
    ends={
        Property(name="types_IdlType13", type=types_ElementSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="types_ElementSpec12", type=types_IdlType, multiplicity=Multiplicity(0, 1))
    }
)
declarator14: BinaryAssociation = BinaryAssociation(
    name="declarator14",
    ends={
        Property(name="types_Declarator", type=types_ElementSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="types_ElementSpec15", type=types_Declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumerators16: BinaryAssociation = BinaryAssociation(
    name="enumerators16",
    ends={
        Property(name="types_Enumeration", type=types_EnumType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_EnumType", type=types_Enumeration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forwardDeclaration17: BinaryAssociation = BinaryAssociation(
    name="forwardDeclaration17",
    ends={
        Property(name="types_ForwardDcl", type=types_StructType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_StructType", type=types_ForwardDcl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
forwardDcl18: BinaryAssociation = BinaryAssociation(
    name="forwardDcl18",
    ends={
        Property(name="StructForwardDcl", type=types_StructType, multiplicity=Multiplicity(1, 1)),
        Property(name="implementation19", type=types_StructForwardDcl, multiplicity=Multiplicity(0, 1))
    }
)
size20: BinaryAssociation = BinaryAssociation(
    name="size20",
    ends={
        Property(name="types_Expression21", type=types_TemplateType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_TemplateType", type=types_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
implementation23: BinaryAssociation = BinaryAssociation(
    name="implementation23",
    ends={
        Property(name="StructType", type=types_StructForwardDcl, multiplicity=Multiplicity(1, 1)),
        Property(name="forwardDcl24", type=types_StructType, multiplicity=Multiplicity(0, 1))
    }
)
expr125: BinaryAssociation = BinaryAssociation(
    name="expr125",
    ends={
        Property(name="types_Expression26", type=types_FixedPtType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_FixedPtType", type=types_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr227: BinaryAssociation = BinaryAssociation(
    name="expr227",
    ends={
        Property(name="types_Expression29", type=types_FixedPtType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_FixedPtType28", type=types_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_types_Switch_FileRegion = Generalization(general=FileRegion, specific=types_Switch)
gen_types_Case_FileRegion = Generalization(general=FileRegion, specific=types_Case)
gen_types_CaseLabel_FileRegion = Generalization(general=FileRegion, specific=types_CaseLabel)
gen_types_DefaultCaseLabel_CaseLabel = Generalization(general=CaseLabel, specific=types_DefaultCaseLabel)
gen_types_ExprCaseLabel_CaseLabel = Generalization(general=CaseLabel, specific=types_ExprCaseLabel)
gen_types_ElementSpec_FileRegion = Generalization(general=FileRegion, specific=types_ElementSpec)
gen_types_TypeDef_TypedElement = Generalization(general=TypedElement, specific=types_TypeDef)
gen_types_TypeDef_IdlTypeDcl = Generalization(general=IdlTypeDcl, specific=types_TypeDef)
gen_types_VoidType_IdlType = Generalization(general=IdlType, specific=types_VoidType)
gen_types_UnionType_IdlTypeDcl = Generalization(general=IdlTypeDcl, specific=types_UnionType)
gen_types_Short_PrimitiveType = Generalization(general=PrimitiveType, specific=types_Short)
gen_types_Long_PrimitiveType = Generalization(general=PrimitiveType, specific=types_Long)
gen_types_Octet_PrimitiveType = Generalization(general=PrimitiveType, specific=types_Octet)
gen_types_Float_PrimitiveType = Generalization(general=PrimitiveType, specific=types_Float)
gen_types_Double_PrimitiveType = Generalization(general=PrimitiveType, specific=types_Double)
gen_types_IdlChar_PrimitiveType = Generalization(general=PrimitiveType, specific=types_IdlChar)
gen_types_IdlWChar_PrimitiveType = Generalization(general=PrimitiveType, specific=types_IdlWChar)
gen_types_WChar_PrimitiveType = Generalization(general=PrimitiveType, specific=types_WChar)
gen_types_Boolean_PrimitiveType = Generalization(general=PrimitiveType, specific=types_Boolean)
gen_types_LongLong_PrimitiveType = Generalization(general=PrimitiveType, specific=types_LongLong)
gen_types_LongDouble_PrimitiveType = Generalization(general=PrimitiveType, specific=types_LongDouble)
gen_types_UShort_PrimitiveType = Generalization(general=PrimitiveType, specific=types_UShort)
gen_types_ULong_PrimitiveType = Generalization(general=PrimitiveType, specific=types_ULong)
gen_types_ULongLong_PrimitiveType = Generalization(general=PrimitiveType, specific=types_ULongLong)
gen_types_Any_PrimitiveType = Generalization(general=PrimitiveType, specific=types_Any)
gen_types_IdlObject_PrimitiveType = Generalization(general=PrimitiveType, specific=types_IdlObject)
gen_types_UnionForwardDcl_IdlTypeDcl = Generalization(general=IdlTypeDcl, specific=types_UnionForwardDcl)
gen_types_StructForwardDcl_IdlTypeDcl = Generalization(general=IdlTypeDcl, specific=types_StructForwardDcl)
gen_types_EnumType_IdlTypeDcl = Generalization(general=IdlTypeDcl, specific=types_EnumType)
gen_types_StructType_IdlTypeDcl = Generalization(general=IdlTypeDcl, specific=types_StructType)
gen_types_StructType_MemberContainer = Generalization(general=MemberContainer, specific=types_StructType)
gen_types_TemplateType_IdlType = Generalization(general=IdlType, specific=types_TemplateType)
gen_types_SequenceType_TemplateType = Generalization(general=TemplateType, specific=types_SequenceType)
gen_types_SequenceType_Typed = Generalization(general=Typed, specific=types_SequenceType)
gen_types_IdlString_TemplateType = Generalization(general=TemplateType, specific=types_IdlString)
gen_types_WString_TemplateType = Generalization(general=TemplateType, specific=types_WString)
gen_types_PrimitiveType_IdlType = Generalization(general=IdlType, specific=types_PrimitiveType)
gen_types_FixedPtType_TemplateType = Generalization(general=TemplateType, specific=types_FixedPtType)
gen_types_ValueBaseType_PrimitiveType = Generalization(general=PrimitiveType, specific=types_ValueBaseType)
gen_types_Enumeration_Declarator = Generalization(general=Declarator, specific=types_Enumeration)
gen_types_Enumeration_IdlTypeDcl = Generalization(general=IdlTypeDcl, specific=types_Enumeration)

# Domain Model
domain_model = DomainModel(
    name="types",
    types={types_UnionForwardDcl, types_Switch, FileRegion, types_IdlType, types_Case, types_CaseLabel, types_ElementSpec, types_DefaultCaseLabel, CaseLabel, types_ExprCaseLabel, types_Expression, types_TypeDef, TypedElement, IdlTypeDcl, types_VoidType, IdlType, types_UnionType, types_Short, PrimitiveType, types_Long, types_Octet, types_Float, types_Double, types_IdlChar, types_IdlWChar, types_WChar, types_Boolean, types_LongLong, types_LongDouble, types_UShort, types_ULong, types_ULongLong, types_Any, types_IdlObject, types_Declarator, types_EnumType, types_Enumeration, types_StructType, MemberContainer, types_ForwardDcl, types_StructForwardDcl, types_TemplateType, types_SequenceType, TemplateType, Typed, types_IdlString, types_WString, types_PrimitiveType, types_FixedPtType, types_ValueBaseType, Declarator},
    associations={forwardDcl0, idlSwitch1, type2, cases4, labels6, spec8, expr10, implementation22, type11, declarator14, enumerators16, forwardDeclaration17, forwardDcl18, size20, implementation23, expr125, expr227},
    generalizations={gen_types_Switch_FileRegion, gen_types_Case_FileRegion, gen_types_CaseLabel_FileRegion, gen_types_DefaultCaseLabel_CaseLabel, gen_types_ExprCaseLabel_CaseLabel, gen_types_ElementSpec_FileRegion, gen_types_TypeDef_TypedElement, gen_types_TypeDef_IdlTypeDcl, gen_types_VoidType_IdlType, gen_types_UnionType_IdlTypeDcl, gen_types_Short_PrimitiveType, gen_types_Long_PrimitiveType, gen_types_Octet_PrimitiveType, gen_types_Float_PrimitiveType, gen_types_Double_PrimitiveType, gen_types_IdlChar_PrimitiveType, gen_types_IdlWChar_PrimitiveType, gen_types_WChar_PrimitiveType, gen_types_Boolean_PrimitiveType, gen_types_LongLong_PrimitiveType, gen_types_LongDouble_PrimitiveType, gen_types_UShort_PrimitiveType, gen_types_ULong_PrimitiveType, gen_types_ULongLong_PrimitiveType, gen_types_Any_PrimitiveType, gen_types_IdlObject_PrimitiveType, gen_types_UnionForwardDcl_IdlTypeDcl, gen_types_StructForwardDcl_IdlTypeDcl, gen_types_EnumType_IdlTypeDcl, gen_types_StructType_IdlTypeDcl, gen_types_StructType_MemberContainer, gen_types_TemplateType_IdlType, gen_types_SequenceType_TemplateType, gen_types_SequenceType_Typed, gen_types_IdlString_TemplateType, gen_types_WString_TemplateType, gen_types_PrimitiveType_IdlType, gen_types_FixedPtType_TemplateType, gen_types_ValueBaseType_PrimitiveType, gen_types_Enumeration_Declarator, gen_types_Enumeration_IdlTypeDcl},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)