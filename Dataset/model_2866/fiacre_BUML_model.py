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
UnOp: Enumeration = Enumeration(
    name="UnOp",
    literals={
            EnumerationLiteral(name="UMINUS"),
			EnumerationLiteral(name="UDOLLAR"),
			EnumerationLiteral(name="UNOT"),
			EnumerationLiteral(name="UFULL"),
			EnumerationLiteral(name="UEMPTY"),
			EnumerationLiteral(name="DEQUEUE"),
			EnumerationLiteral(name="FIRST")
    }
)

BinOp: Enumeration = Enumeration(
    name="BinOp",
    literals={
            EnumerationLiteral(name="BOR"),
			EnumerationLiteral(name="BAND"),
			EnumerationLiteral(name="BEQ"),
			EnumerationLiteral(name="BNE"),
			EnumerationLiteral(name="BLT"),
			EnumerationLiteral(name="BGT"),
			EnumerationLiteral(name="BLE"),
			EnumerationLiteral(name="BGE"),
			EnumerationLiteral(name="BADD"),
			EnumerationLiteral(name="BMINUS"),
			EnumerationLiteral(name="BMUL"),
			EnumerationLiteral(name="BDIV"),
			EnumerationLiteral(name="BMOD"),
			EnumerationLiteral(name="ENQUEUE"),
			EnumerationLiteral(name="APPEND")
    }
)

# Classes
fiacre_Program = Class(name="fiacre::Program")
fiacre_Declaration = Class(name="fiacre::Declaration", is_abstract=True)
fiacre_NodeDecl = Class(name="fiacre::NodeDecl", is_abstract=True)
fiacre_ParamPortDecl = Class(name="fiacre::ParamPortDecl")
fiacre_LocalPortDecl = Class(name="fiacre::LocalPortDecl")
fiacre_Statement = Class(name="fiacre::Statement", is_abstract=True)
fiacre_TypeDecl = Class(name="fiacre::TypeDecl")
fiacre_Type = Class(name="fiacre::Type", is_abstract=True)
fiacre_ChannelDecl = Class(name="fiacre::ChannelDecl")
fiacre_Channel = Class(name="fiacre::Channel", is_abstract=True)
fiacre_ComponentDecl = Class(name="fiacre::ComponentDecl")
NodeDecl = Class(name="NodeDecl")
fiacre_Composition = Class(name="fiacre::Composition", is_abstract=True)
fiacre_Priority = Class(name="fiacre::Priority")
fiacre_ProcessDecl = Class(name="fiacre::ProcessDecl")
fiacre_State = Class(name="fiacre::State")
fiacre_Transition = Class(name="fiacre::Transition")
fiacre_PortDecl = Class(name="fiacre::PortDecl", is_abstract=True)
Declaration = Class(name="Declaration")
fiacre_ArgumentVariable = Class(name="fiacre::ArgumentVariable")
fiacre_LocalVariable = Class(name="fiacre::LocalVariable")
fiacre_Exp = Class(name="fiacre::Exp", is_abstract=True)
fiacre_Par = Class(name="fiacre::Par")
Composition = Class(name="Composition")
fiacre_InterfacedComp = Class(name="fiacre::InterfacedComp")
fiacre_Instance = Class(name="fiacre::Instance")
fiacre_Arg = Class(name="fiacre::Arg", is_abstract=True)
Arg = Class(name="Arg")
fiacre_NullStmt = Class(name="fiacre::NullStmt")
Statement = Class(name="Statement")
fiacre_Assignment = Class(name="fiacre::Assignment", is_abstract=True)
fiacre_Communication = Class(name="fiacre::Communication", is_abstract=True)
Variable = Class(name="Variable")
fiacre_IfStmt = Class(name="fiacre::IfStmt")
fiacre_Select = Class(name="fiacre::Select")
fiacre_To = Class(name="fiacre::To")
fiacre_Wait = Class(name="fiacre::Wait")
fiacre_MinBound = Class(name="fiacre::MinBound", is_abstract=True)
fiacre_MaxBound = Class(name="fiacre::MaxBound", is_abstract=True)
fiacre_DeterministicAssignment = Class(name="fiacre::DeterministicAssignment")
Assignment = Class(name="Assignment")
fiacre_SingleAssignment = Class(name="fiacre::SingleAssignment")
fiacre_NonDeterministicAssignment = Class(name="fiacre::NonDeterministicAssignment")
fiacre_Pattern = Class(name="fiacre::Pattern", is_abstract=True)
fiacre_WhileStmt = Class(name="fiacre::WhileStmt")
fiacre_NatLiteral = Class(name="fiacre::NatLiteral")
Literal = Class(name="Literal")
fiacre_BoolLiteral = Class(name="fiacre::BoolLiteral")
fiacre_VarRef = Class(name="fiacre::VarRef")
Pattern = Class(name="Pattern")
fiacre_UnExp = Class(name="fiacre::UnExp")
Exp = Class(name="Exp")
fiacre_BinExp = Class(name="fiacre::BinExp")
fiacre_Variable = Class(name="fiacre::Variable", is_abstract=True)
fiacre_ArrayElem = Class(name="fiacre::ArrayElem")
fiacre_RecordElem = Class(name="fiacre::RecordElem")
fiacre_InlineQueue = Class(name="fiacre::InlineQueue")
InlineCollection = Class(name="InlineCollection")
fiacre_BasicType = Class(name="fiacre::BasicType", is_abstract=True)
Type = Class(name="Type")
fiacre_BoolType = Class(name="fiacre::BoolType")
BasicType = Class(name="BasicType")
fiacre_NatType = Class(name="fiacre::NatType")
fiacre_IntType = Class(name="fiacre::IntType")
fiacre_Interval = Class(name="fiacre::Interval")
fiacre_Record = Class(name="fiacre::Record")
fiacre_Field = Class(name="fiacre::Field")
fiacre_Queue = Class(name="fiacre::Queue")
fiacre_TypeId = Class(name="fiacre::TypeId")
fiacre_Profile = Class(name="fiacre::Profile")
Channel = Class(name="Channel")
fiacre_InlineArray = Class(name="fiacre::InlineArray")
fiacre_InlineRecord = Class(name="fiacre::InlineRecord")
fiacre_ValuedField = Class(name="fiacre::ValuedField")
LabeledType = Class(name="LabeledType")
fiacre_Array = Class(name="fiacre::Array")
fiacre_Emission = Class(name="fiacre::Emission")
fiacre_Seq = Class(name="fiacre::Seq")
PortDecl = Class(name="PortDecl")
fiacre_Synchronization = Class(name="fiacre::Synchronization")
Communication = Class(name="Communication")
fiacre_Reception = Class(name="fiacre::Reception")
fiacre_Union = Class(name="fiacre::Union")
fiacre_Constr = Class(name="fiacre::Constr")
fiacre_ConstrPattern = Class(name="fiacre::ConstrPattern")
fiacre_ArrayPattern = Class(name="fiacre::ArrayPattern")
fiacre_FieldPattern = Class(name="fiacre::FieldPattern")
fiacre_ConstrExp = Class(name="fiacre::ConstrExp")
fiacre_CaseStmt = Class(name="fiacre::CaseStmt")
fiacre_Rule = Class(name="fiacre::Rule")
fiacre_RefArg = Class(name="fiacre::RefArg")
fiacre_ConstantDecl = Class(name="fiacre::ConstantDecl")
fiacre_AnyPattern = Class(name="fiacre::AnyPattern")
fiacre_Literal = Class(name="fiacre::Literal", is_abstract=True)
fiacre_InlineCollection = Class(name="fiacre::InlineCollection", is_abstract=True)
fiacre_LabeledType = Class(name="fiacre::LabeledType", is_abstract=True)
fiacre_FiniteBound = Class(name="fiacre::FiniteBound")
MinBound = Class(name="MinBound")
MaxBound = Class(name="MaxBound")
fiacre_InfiniteBound = Class(name="fiacre::InfiniteBound")
fiacre_CondExp = Class(name="fiacre::CondExp")
fiacre_ConstantRef = Class(name="fiacre::ConstantRef")
fiacre_Foreach = Class(name="fiacre::Foreach")

# fiacre_Program class attributes and methods

# fiacre_Declaration class attributes and methods
fiacre_Declaration_name: Property = Property(name="name", type=StringType)
fiacre_Declaration.attributes={fiacre_Declaration_name}

# fiacre_NodeDecl class attributes and methods

# fiacre_ParamPortDecl class attributes and methods

# fiacre_LocalPortDecl class attributes and methods

# fiacre_Statement class attributes and methods
fiacre_Statement_comment: Property = Property(name="comment", type=StringType)
fiacre_Statement.attributes={fiacre_Statement_comment}

# fiacre_TypeDecl class attributes and methods

# fiacre_Type class attributes and methods

# fiacre_ChannelDecl class attributes and methods

# fiacre_Channel class attributes and methods

# fiacre_ComponentDecl class attributes and methods

# NodeDecl class attributes and methods

# fiacre_Composition class attributes and methods

# fiacre_Priority class attributes and methods

# fiacre_ProcessDecl class attributes and methods

# fiacre_State class attributes and methods
fiacre_State_name: Property = Property(name="name", type=StringType)
fiacre_State.attributes={fiacre_State_name}

# fiacre_Transition class attributes and methods
fiacre_Transition_name: Property = Property(name="name", type=StringType)
fiacre_Transition.attributes={fiacre_Transition_name}

# fiacre_PortDecl class attributes and methods
fiacre_PortDecl_in: Property = Property(name="in", type=BooleanType)
fiacre_PortDecl_out: Property = Property(name="out", type=BooleanType)
fiacre_PortDecl_name: Property = Property(name="name", type=StringType)
fiacre_PortDecl.attributes={fiacre_PortDecl_name, fiacre_PortDecl_out, fiacre_PortDecl_in}

# Declaration class attributes and methods

# fiacre_ArgumentVariable class attributes and methods
fiacre_ArgumentVariable_ref: Property = Property(name="ref", type=BooleanType)
fiacre_ArgumentVariable_read: Property = Property(name="read", type=BooleanType)
fiacre_ArgumentVariable_write: Property = Property(name="write", type=BooleanType)
fiacre_ArgumentVariable.attributes={fiacre_ArgumentVariable_ref, fiacre_ArgumentVariable_write, fiacre_ArgumentVariable_read}

# fiacre_LocalVariable class attributes and methods
fiacre_LocalVariable_constant: Property = Property(name="constant", type=BooleanType)
fiacre_LocalVariable.attributes={fiacre_LocalVariable_constant}

# fiacre_Exp class attributes and methods

# fiacre_Par class attributes and methods

# Composition class attributes and methods

# fiacre_InterfacedComp class attributes and methods

# fiacre_Instance class attributes and methods
fiacre_Instance_name: Property = Property(name="name", type=StringType)
fiacre_Instance.attributes={fiacre_Instance_name}

# fiacre_Arg class attributes and methods

# Arg class attributes and methods

# fiacre_NullStmt class attributes and methods

# Statement class attributes and methods

# fiacre_Assignment class attributes and methods

# fiacre_Communication class attributes and methods

# Variable class attributes and methods

# fiacre_IfStmt class attributes and methods

# fiacre_Select class attributes and methods

# fiacre_To class attributes and methods

# fiacre_Wait class attributes and methods

# fiacre_MinBound class attributes and methods

# fiacre_MaxBound class attributes and methods

# fiacre_DeterministicAssignment class attributes and methods

# Assignment class attributes and methods

# fiacre_SingleAssignment class attributes and methods

# fiacre_NonDeterministicAssignment class attributes and methods

# fiacre_Pattern class attributes and methods

# fiacre_WhileStmt class attributes and methods

# fiacre_NatLiteral class attributes and methods
fiacre_NatLiteral_value: Property = Property(name="value", type=IntegerType)
fiacre_NatLiteral.attributes={fiacre_NatLiteral_value}

# Literal class attributes and methods

# fiacre_BoolLiteral class attributes and methods
fiacre_BoolLiteral_value: Property = Property(name="value", type=BooleanType)
fiacre_BoolLiteral.attributes={fiacre_BoolLiteral_value}

# fiacre_VarRef class attributes and methods

# Pattern class attributes and methods

# fiacre_UnExp class attributes and methods
fiacre_UnExp_unop: Property = Property(name="unop", type=StringType)
fiacre_UnExp.attributes={fiacre_UnExp_unop}

# Exp class attributes and methods

# fiacre_BinExp class attributes and methods
fiacre_BinExp_binOp: Property = Property(name="binOp", type=StringType)
fiacre_BinExp.attributes={fiacre_BinExp_binOp}

# fiacre_Variable class attributes and methods
fiacre_Variable_name: Property = Property(name="name", type=StringType)
fiacre_Variable.attributes={fiacre_Variable_name}

# fiacre_ArrayElem class attributes and methods

# fiacre_RecordElem class attributes and methods
fiacre_RecordElem_field: Property = Property(name="field", type=StringType)
fiacre_RecordElem.attributes={fiacre_RecordElem_field}

# fiacre_InlineQueue class attributes and methods

# InlineCollection class attributes and methods

# fiacre_BasicType class attributes and methods

# Type class attributes and methods

# fiacre_BoolType class attributes and methods

# BasicType class attributes and methods

# fiacre_NatType class attributes and methods

# fiacre_IntType class attributes and methods

# fiacre_Interval class attributes and methods

# fiacre_Record class attributes and methods

# fiacre_Field class attributes and methods

# fiacre_Queue class attributes and methods

# fiacre_TypeId class attributes and methods

# fiacre_Profile class attributes and methods

# Channel class attributes and methods

# fiacre_InlineArray class attributes and methods

# fiacre_InlineRecord class attributes and methods

# fiacre_ValuedField class attributes and methods
fiacre_ValuedField_field: Property = Property(name="field", type=StringType)
fiacre_ValuedField.attributes={fiacre_ValuedField_field}

# LabeledType class attributes and methods

# fiacre_Array class attributes and methods

# fiacre_Emission class attributes and methods

# fiacre_Seq class attributes and methods

# PortDecl class attributes and methods

# fiacre_Synchronization class attributes and methods

# Communication class attributes and methods

# fiacre_Reception class attributes and methods

# fiacre_Union class attributes and methods

# fiacre_Constr class attributes and methods

# fiacre_ConstrPattern class attributes and methods
fiacre_ConstrPattern_name: Property = Property(name="name", type=StringType)
fiacre_ConstrPattern.attributes={fiacre_ConstrPattern_name}

# fiacre_ArrayPattern class attributes and methods

# fiacre_FieldPattern class attributes and methods
fiacre_FieldPattern_field: Property = Property(name="field", type=StringType)
fiacre_FieldPattern.attributes={fiacre_FieldPattern_field}

# fiacre_ConstrExp class attributes and methods
fiacre_ConstrExp_name: Property = Property(name="name", type=StringType)
fiacre_ConstrExp.attributes={fiacre_ConstrExp_name}

# fiacre_CaseStmt class attributes and methods

# fiacre_Rule class attributes and methods

# fiacre_RefArg class attributes and methods

# fiacre_ConstantDecl class attributes and methods

# fiacre_AnyPattern class attributes and methods

# fiacre_Literal class attributes and methods

# fiacre_InlineCollection class attributes and methods

# fiacre_LabeledType class attributes and methods
fiacre_LabeledType_name: Property = Property(name="name", type=StringType)
fiacre_LabeledType.attributes={fiacre_LabeledType_name}

# fiacre_FiniteBound class attributes and methods
fiacre_FiniteBound_strict: Property = Property(name="strict", type=BooleanType)
fiacre_FiniteBound_val: Property = Property(name="val", type=IntegerType)
fiacre_FiniteBound.attributes={fiacre_FiniteBound_val, fiacre_FiniteBound_strict}

# MinBound class attributes and methods

# MaxBound class attributes and methods

# fiacre_InfiniteBound class attributes and methods

# fiacre_CondExp class attributes and methods

# fiacre_ConstantRef class attributes and methods

# fiacre_Foreach class attributes and methods

# Relationships
declaration0: BinaryAssociation = BinaryAssociation(
    name="declaration0",
    ends={
        Property(name="fiacre_Declaration", type=fiacre_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Program", type=fiacre_Declaration, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
root1: BinaryAssociation = BinaryAssociation(
    name="root1",
    ends={
        Property(name="fiacre_NodeDecl", type=fiacre_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Program2", type=fiacre_NodeDecl, multiplicity=Multiplicity(1, 1))
    }
)
port7: BinaryAssociation = BinaryAssociation(
    name="port7",
    ends={
        Property(name="fiacre_ParamPortDecl", type=fiacre_NodeDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_NodeDecl8", type=fiacre_ParamPortDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
localPort9: BinaryAssociation = BinaryAssociation(
    name="localPort9",
    ends={
        Property(name="fiacre_LocalPortDecl", type=fiacre_NodeDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_NodeDecl10", type=fiacre_LocalPortDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initAction11: BinaryAssociation = BinaryAssociation(
    name="initAction11",
    ends={
        Property(name="fiacre_Statement", type=fiacre_NodeDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_NodeDecl12", type=fiacre_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
is13: BinaryAssociation = BinaryAssociation(
    name="is13",
    ends={
        Property(name="fiacre_Type", type=fiacre_TypeDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_TypeDecl", type=fiacre_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
is14: BinaryAssociation = BinaryAssociation(
    name="is14",
    ends={
        Property(name="fiacre_Channel", type=fiacre_ChannelDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_ChannelDecl", type=fiacre_Channel, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body15: BinaryAssociation = BinaryAssociation(
    name="body15",
    ends={
        Property(name="fiacre_Composition", type=fiacre_ComponentDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_ComponentDecl", type=fiacre_Composition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
priority16: BinaryAssociation = BinaryAssociation(
    name="priority16",
    ends={
        Property(name="fiacre_Priority", type=fiacre_ComponentDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_ComponentDecl17", type=fiacre_Priority, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state18: BinaryAssociation = BinaryAssociation(
    name="state18",
    ends={
        Property(name="fiacre_State", type=fiacre_ProcessDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_ProcessDecl", type=fiacre_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition19: BinaryAssociation = BinaryAssociation(
    name="transition19",
    ends={
        Property(name="fiacre_Transition", type=fiacre_ProcessDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_ProcessDecl20", type=fiacre_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arg3: BinaryAssociation = BinaryAssociation(
    name="arg3",
    ends={
        Property(name="fiacre_ArgumentVariable", type=fiacre_NodeDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_NodeDecl4", type=fiacre_ArgumentVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
var5: BinaryAssociation = BinaryAssociation(
    name="var5",
    ends={
        Property(name="fiacre_LocalVariable", type=fiacre_NodeDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_NodeDecl6", type=fiacre_LocalVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializer23: BinaryAssociation = BinaryAssociation(
    name="initializer23",
    ends={
        Property(name="fiacre_Exp", type=fiacre_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_LocalVariable24", type=fiacre_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arg25: BinaryAssociation = BinaryAssociation(
    name="arg25",
    ends={
        Property(name="fiacre_InterfacedComp", type=fiacre_Par, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Par", type=fiacre_InterfacedComp, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
type26: BinaryAssociation = BinaryAssociation(
    name="type26",
    ends={
        Property(name="fiacre_NodeDecl27", type=fiacre_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Instance", type=fiacre_NodeDecl, multiplicity=Multiplicity(1, 1))
    }
)
arg28: BinaryAssociation = BinaryAssociation(
    name="arg28",
    ends={
        Property(name="fiacre_Arg", type=fiacre_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Instance29", type=fiacre_Arg, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
port30: BinaryAssociation = BinaryAssociation(
    name="port30",
    ends={
        Property(name="fiacre_PortDecl32", type=fiacre_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Instance31", type=fiacre_PortDecl, multiplicity=Multiplicity(0, 9999))
    }
)
composition33: BinaryAssociation = BinaryAssociation(
    name="composition33",
    ends={
        Property(name="fiacre_Composition35", type=fiacre_InterfacedComp, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_InterfacedComp34", type=fiacre_Composition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
syncPort36: BinaryAssociation = BinaryAssociation(
    name="syncPort36",
    ends={
        Property(name="fiacre_PortDecl38", type=fiacre_InterfacedComp, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_InterfacedComp37", type=fiacre_PortDecl, multiplicity=Multiplicity(0, 9999))
    }
)
from39: BinaryAssociation = BinaryAssociation(
    name="from39",
    ends={
        Property(name="fiacre_State41", type=fiacre_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Transition40", type=fiacre_State, multiplicity=Multiplicity(1, 1))
    }
)
action42: BinaryAssociation = BinaryAssociation(
    name="action42",
    ends={
        Property(name="fiacre_Statement44", type=fiacre_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Transition43", type=fiacre_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
channel21: BinaryAssociation = BinaryAssociation(
    name="channel21",
    ends={
        Property(name="fiacre_Channel22", type=fiacre_PortDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_PortDecl", type=fiacre_Channel, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition52: BinaryAssociation = BinaryAssociation(
    name="condition52",
    ends={
        Property(name="fiacre_Exp53", type=fiacre_IfStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_IfStmt", type=fiacre_Exp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
then54: BinaryAssociation = BinaryAssociation(
    name="then54",
    ends={
        Property(name="fiacre_Statement56", type=fiacre_IfStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_IfStmt55", type=fiacre_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
else57: BinaryAssociation = BinaryAssociation(
    name="else57",
    ends={
        Property(name="fiacre_Statement59", type=fiacre_IfStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_IfStmt58", type=fiacre_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement60: BinaryAssociation = BinaryAssociation(
    name="statement60",
    ends={
        Property(name="fiacre_Statement61", type=fiacre_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Select", type=fiacre_Statement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
dest62: BinaryAssociation = BinaryAssociation(
    name="dest62",
    ends={
        Property(name="fiacre_State63", type=fiacre_To, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_To", type=fiacre_State, multiplicity=Multiplicity(1, 1))
    }
)
mini64: BinaryAssociation = BinaryAssociation(
    name="mini64",
    ends={
        Property(name="fiacre_MinBound", type=fiacre_Wait, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Wait", type=fiacre_MinBound, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
maxi65: BinaryAssociation = BinaryAssociation(
    name="maxi65",
    ends={
        Property(name="fiacre_MaxBound", type=fiacre_Wait, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Wait66", type=fiacre_MaxBound, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
assignment67: BinaryAssociation = BinaryAssociation(
    name="assignment67",
    ends={
        Property(name="fiacre_SingleAssignment", type=fiacre_DeterministicAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_DeterministicAssignment", type=fiacre_SingleAssignment, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
lhs68: BinaryAssociation = BinaryAssociation(
    name="lhs68",
    ends={
        Property(name="fiacre_Pattern", type=fiacre_NonDeterministicAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_NonDeterministicAssignment", type=fiacre_Pattern, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
condition69: BinaryAssociation = BinaryAssociation(
    name="condition69",
    ends={
        Property(name="fiacre_Exp71", type=fiacre_NonDeterministicAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_NonDeterministicAssignment70", type=fiacre_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs72: BinaryAssociation = BinaryAssociation(
    name="lhs72",
    ends={
        Property(name="fiacre_Pattern74", type=fiacre_SingleAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_SingleAssignment73", type=fiacre_Pattern, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
port45: BinaryAssociation = BinaryAssociation(
    name="port45",
    ends={
        Property(name="fiacre_PortDecl46", type=fiacre_Communication, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Communication", type=fiacre_PortDecl, multiplicity=Multiplicity(1, 1))
    }
)
condition47: BinaryAssociation = BinaryAssociation(
    name="condition47",
    ends={
        Property(name="fiacre_Exp48", type=fiacre_WhileStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_WhileStmt", type=fiacre_Exp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body49: BinaryAssociation = BinaryAssociation(
    name="body49",
    ends={
        Property(name="fiacre_Statement51", type=fiacre_WhileStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_WhileStmt50", type=fiacre_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right80: BinaryAssociation = BinaryAssociation(
    name="right80",
    ends={
        Property(name="fiacre_Exp81", type=fiacre_BinExp, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_BinExp", type=fiacre_Exp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left82: BinaryAssociation = BinaryAssociation(
    name="left82",
    ends={
        Property(name="fiacre_Exp84", type=fiacre_BinExp, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_BinExp83", type=fiacre_Exp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs75: BinaryAssociation = BinaryAssociation(
    name="rhs75",
    ends={
        Property(name="fiacre_Exp77", type=fiacre_SingleAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_SingleAssignment76", type=fiacre_Exp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exp78: BinaryAssociation = BinaryAssociation(
    name="exp78",
    ends={
        Property(name="fiacre_Exp79", type=fiacre_UnExp, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_UnExp", type=fiacre_Exp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
decl85: BinaryAssociation = BinaryAssociation(
    name="decl85",
    ends={
        Property(name="fiacre_Variable", type=fiacre_VarRef, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_VarRef", type=fiacre_Variable, multiplicity=Multiplicity(1, 1))
    }
)
record91: BinaryAssociation = BinaryAssociation(
    name="record91",
    ends={
        Property(name="fiacre_Exp92", type=fiacre_RecordElem, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_RecordElem", type=fiacre_Exp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mini93: BinaryAssociation = BinaryAssociation(
    name="mini93",
    ends={
        Property(name="fiacre_Exp94", type=fiacre_Interval, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Interval", type=fiacre_Exp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
maxi95: BinaryAssociation = BinaryAssociation(
    name="maxi95",
    ends={
        Property(name="fiacre_Exp97", type=fiacre_Interval, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Interval96", type=fiacre_Exp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
field98: BinaryAssociation = BinaryAssociation(
    name="field98",
    ends={
        Property(name="fiacre_Field", type=fiacre_Record, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Record", type=fiacre_Field, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
array86: BinaryAssociation = BinaryAssociation(
    name="array86",
    ends={
        Property(name="fiacre_Exp87", type=fiacre_ArrayElem, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_ArrayElem", type=fiacre_Exp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
index88: BinaryAssociation = BinaryAssociation(
    name="index88",
    ends={
        Property(name="fiacre_Exp90", type=fiacre_ArrayElem, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_ArrayElem89", type=fiacre_Exp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type101: BinaryAssociation = BinaryAssociation(
    name="type101",
    ends={
        Property(name="fiacre_Type103", type=fiacre_Array, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Array102", type=fiacre_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type104: BinaryAssociation = BinaryAssociation(
    name="type104",
    ends={
        Property(name="fiacre_Type105", type=fiacre_Queue, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Queue", type=fiacre_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
size106: BinaryAssociation = BinaryAssociation(
    name="size106",
    ends={
        Property(name="fiacre_Exp108", type=fiacre_Queue, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Queue107", type=fiacre_Exp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
decl109: BinaryAssociation = BinaryAssociation(
    name="decl109",
    ends={
        Property(name="fiacre_TypeDecl110", type=fiacre_TypeId, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_TypeId", type=fiacre_TypeDecl, multiplicity=Multiplicity(1, 1))
    }
)
type111: BinaryAssociation = BinaryAssociation(
    name="type111",
    ends={
        Property(name="fiacre_Type112", type=fiacre_Profile, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Profile", type=fiacre_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value113: BinaryAssociation = BinaryAssociation(
    name="value113",
    ends={
        Property(name="fiacre_ValuedField", type=fiacre_InlineRecord, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_InlineRecord", type=fiacre_ValuedField, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
size99: BinaryAssociation = BinaryAssociation(
    name="size99",
    ends={
        Property(name="fiacre_Exp100", type=fiacre_Array, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Array", type=fiacre_Exp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
pattern117: BinaryAssociation = BinaryAssociation(
    name="pattern117",
    ends={
        Property(name="fiacre_Pattern118", type=fiacre_Reception, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Reception", type=fiacre_Pattern, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
where119: BinaryAssociation = BinaryAssociation(
    name="where119",
    ends={
        Property(name="fiacre_Exp121", type=fiacre_Reception, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Reception120", type=fiacre_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arg122: BinaryAssociation = BinaryAssociation(
    name="arg122",
    ends={
        Property(name="fiacre_Exp123", type=fiacre_Emission, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Emission", type=fiacre_Exp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement124: BinaryAssociation = BinaryAssociation(
    name="statement124",
    ends={
        Property(name="fiacre_Statement125", type=fiacre_Seq, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Seq", type=fiacre_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mini126: BinaryAssociation = BinaryAssociation(
    name="mini126",
    ends={
        Property(name="fiacre_MinBound128", type=fiacre_LocalPortDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_LocalPortDecl127", type=fiacre_MinBound, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
maxi129: BinaryAssociation = BinaryAssociation(
    name="maxi129",
    ends={
        Property(name="fiacre_MaxBound131", type=fiacre_LocalPortDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_LocalPortDecl130", type=fiacre_MaxBound, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type132: BinaryAssociation = BinaryAssociation(
    name="type132",
    ends={
        Property(name="fiacre_Type134", type=fiacre_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Variable133", type=fiacre_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value114: BinaryAssociation = BinaryAssociation(
    name="value114",
    ends={
        Property(name="fiacre_Exp116", type=fiacre_ValuedField, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_ValuedField115", type=fiacre_Exp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arg141: BinaryAssociation = BinaryAssociation(
    name="arg141",
    ends={
        Property(name="fiacre_Exp142", type=fiacre_ConstrExp, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_ConstrExp", type=fiacre_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constr143: BinaryAssociation = BinaryAssociation(
    name="constr143",
    ends={
        Property(name="fiacre_Constr", type=fiacre_Union, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Union", type=fiacre_Constr, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
arg144: BinaryAssociation = BinaryAssociation(
    name="arg144",
    ends={
        Property(name="fiacre_Pattern145", type=fiacre_ConstrPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_ConstrPattern", type=fiacre_Pattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
index146: BinaryAssociation = BinaryAssociation(
    name="index146",
    ends={
        Property(name="fiacre_Exp147", type=fiacre_ArrayPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_ArrayPattern", type=fiacre_Exp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
array148: BinaryAssociation = BinaryAssociation(
    name="array148",
    ends={
        Property(name="fiacre_Pattern150", type=fiacre_ArrayPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_ArrayPattern149", type=fiacre_Pattern, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inf135: BinaryAssociation = BinaryAssociation(
    name="inf135",
    ends={
        Property(name="fiacre_PortDecl137", type=fiacre_Priority, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Priority136", type=fiacre_PortDecl, multiplicity=Multiplicity(1, 9999))
    }
)
sup138: BinaryAssociation = BinaryAssociation(
    name="sup138",
    ends={
        Property(name="fiacre_PortDecl140", type=fiacre_Priority, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Priority139", type=fiacre_PortDecl, multiplicity=Multiplicity(1, 9999))
    }
)
rule153: BinaryAssociation = BinaryAssociation(
    name="rule153",
    ends={
        Property(name="fiacre_Rule", type=fiacre_CaseStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_CaseStmt", type=fiacre_Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp154: BinaryAssociation = BinaryAssociation(
    name="exp154",
    ends={
        Property(name="fiacre_Exp156", type=fiacre_CaseStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_CaseStmt155", type=fiacre_Exp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs157: BinaryAssociation = BinaryAssociation(
    name="lhs157",
    ends={
        Property(name="fiacre_Pattern159", type=fiacre_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Rule158", type=fiacre_Pattern, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
action160: BinaryAssociation = BinaryAssociation(
    name="action160",
    ends={
        Property(name="fiacre_Statement162", type=fiacre_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Rule161", type=fiacre_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ref163: BinaryAssociation = BinaryAssociation(
    name="ref163",
    ends={
        Property(name="fiacre_Variable164", type=fiacre_RefArg, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_RefArg", type=fiacre_Variable, multiplicity=Multiplicity(1, 1))
    }
)
type165: BinaryAssociation = BinaryAssociation(
    name="type165",
    ends={
        Property(name="fiacre_Type166", type=fiacre_ConstantDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_ConstantDecl", type=fiacre_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value167: BinaryAssociation = BinaryAssociation(
    name="value167",
    ends={
        Property(name="fiacre_Exp169", type=fiacre_ConstantDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_ConstantDecl168", type=fiacre_Exp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
record151: BinaryAssociation = BinaryAssociation(
    name="record151",
    ends={
        Property(name="fiacre_Pattern152", type=fiacre_FieldPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_FieldPattern", type=fiacre_Pattern, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elem172: BinaryAssociation = BinaryAssociation(
    name="elem172",
    ends={
        Property(name="fiacre_Exp173", type=fiacre_InlineCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_InlineCollection", type=fiacre_Exp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type174: BinaryAssociation = BinaryAssociation(
    name="type174",
    ends={
        Property(name="fiacre_Type175", type=fiacre_LabeledType, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_LabeledType", type=fiacre_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cond176: BinaryAssociation = BinaryAssociation(
    name="cond176",
    ends={
        Property(name="fiacre_Exp177", type=fiacre_CondExp, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_CondExp", type=fiacre_Exp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iff178: BinaryAssociation = BinaryAssociation(
    name="iff178",
    ends={
        Property(name="fiacre_Exp180", type=fiacre_CondExp, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_CondExp179", type=fiacre_Exp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
decl170: BinaryAssociation = BinaryAssociation(
    name="decl170",
    ends={
        Property(name="fiacre_ConstantDecl171", type=fiacre_ConstantRef, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_ConstantRef", type=fiacre_ConstantDecl, multiplicity=Multiplicity(1, 1))
    }
)
body184: BinaryAssociation = BinaryAssociation(
    name="body184",
    ends={
        Property(name="fiacre_Statement185", type=fiacre_Foreach, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Foreach", type=fiacre_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iter186: BinaryAssociation = BinaryAssociation(
    name="iter186",
    ends={
        Property(name="fiacre_LocalVariable188", type=fiacre_Foreach, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Foreach187", type=fiacre_LocalVariable, multiplicity=Multiplicity(1, 1))
    }
)
ift181: BinaryAssociation = BinaryAssociation(
    name="ift181",
    ends={
        Property(name="fiacre_Exp183", type=fiacre_CondExp, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_CondExp182", type=fiacre_Exp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_fiacre_TypeDecl_Declaration = Generalization(general=Declaration, specific=fiacre_TypeDecl)
gen_fiacre_ChannelDecl_Declaration = Generalization(general=Declaration, specific=fiacre_ChannelDecl)
gen_fiacre_ComponentDecl_NodeDecl = Generalization(general=NodeDecl, specific=fiacre_ComponentDecl)
gen_fiacre_ProcessDecl_NodeDecl = Generalization(general=NodeDecl, specific=fiacre_ProcessDecl)
gen_fiacre_NodeDecl_Declaration = Generalization(general=Declaration, specific=fiacre_NodeDecl)
gen_fiacre_LocalVariable_Variable = Generalization(general=Variable, specific=fiacre_LocalVariable)
gen_fiacre_Par_Composition = Generalization(general=Composition, specific=fiacre_Par)
gen_fiacre_Instance_Composition = Generalization(general=Composition, specific=fiacre_Instance)
gen_fiacre_Exp_Arg = Generalization(general=Arg, specific=fiacre_Exp)
gen_fiacre_NullStmt_Statement = Generalization(general=Statement, specific=fiacre_NullStmt)
gen_fiacre_Assignment_Statement = Generalization(general=Statement, specific=fiacre_Assignment)
gen_fiacre_Communication_Statement = Generalization(general=Statement, specific=fiacre_Communication)
gen_fiacre_ArgumentVariable_Variable = Generalization(general=Variable, specific=fiacre_ArgumentVariable)
gen_fiacre_IfStmt_Statement = Generalization(general=Statement, specific=fiacre_IfStmt)
gen_fiacre_Select_Statement = Generalization(general=Statement, specific=fiacre_Select)
gen_fiacre_To_Statement = Generalization(general=Statement, specific=fiacre_To)
gen_fiacre_Wait_Statement = Generalization(general=Statement, specific=fiacre_Wait)
gen_fiacre_DeterministicAssignment_Assignment = Generalization(general=Assignment, specific=fiacre_DeterministicAssignment)
gen_fiacre_NonDeterministicAssignment_Assignment = Generalization(general=Assignment, specific=fiacre_NonDeterministicAssignment)
gen_fiacre_WhileStmt_Statement = Generalization(general=Statement, specific=fiacre_WhileStmt)
gen_fiacre_NatLiteral_Literal = Generalization(general=Literal, specific=fiacre_NatLiteral)
gen_fiacre_BoolLiteral_Literal = Generalization(general=Literal, specific=fiacre_BoolLiteral)
gen_fiacre_UnExp_Exp = Generalization(general=Exp, specific=fiacre_UnExp)
gen_fiacre_BinExp_Exp = Generalization(general=Exp, specific=fiacre_BinExp)
gen_fiacre_VarRef_Pattern = Generalization(general=Pattern, specific=fiacre_VarRef)
gen_fiacre_VarRef_Exp = Generalization(general=Exp, specific=fiacre_VarRef)
gen_fiacre_ArrayElem_Exp = Generalization(general=Exp, specific=fiacre_ArrayElem)
gen_fiacre_RecordElem_Exp = Generalization(general=Exp, specific=fiacre_RecordElem)
gen_fiacre_InlineQueue_InlineCollection = Generalization(general=InlineCollection, specific=fiacre_InlineQueue)
gen_fiacre_BasicType_Type = Generalization(general=Type, specific=fiacre_BasicType)
gen_fiacre_BoolType_BasicType = Generalization(general=BasicType, specific=fiacre_BoolType)
gen_fiacre_NatType_BasicType = Generalization(general=BasicType, specific=fiacre_NatType)
gen_fiacre_IntType_BasicType = Generalization(general=BasicType, specific=fiacre_IntType)
gen_fiacre_Interval_Type = Generalization(general=Type, specific=fiacre_Interval)
gen_fiacre_Record_Type = Generalization(general=Type, specific=fiacre_Record)
gen_fiacre_Queue_Type = Generalization(general=Type, specific=fiacre_Queue)
gen_fiacre_TypeId_Type = Generalization(general=Type, specific=fiacre_TypeId)
gen_fiacre_Profile_Channel = Generalization(general=Channel, specific=fiacre_Profile)
gen_fiacre_InlineArray_InlineCollection = Generalization(general=InlineCollection, specific=fiacre_InlineArray)
gen_fiacre_InlineRecord_Exp = Generalization(general=Exp, specific=fiacre_InlineRecord)
gen_fiacre_Field_LabeledType = Generalization(general=LabeledType, specific=fiacre_Field)
gen_fiacre_Array_Type = Generalization(general=Type, specific=fiacre_Array)
gen_fiacre_Emission_Communication = Generalization(general=Communication, specific=fiacre_Emission)
gen_fiacre_Seq_Statement = Generalization(general=Statement, specific=fiacre_Seq)
gen_fiacre_LocalPortDecl_PortDecl = Generalization(general=PortDecl, specific=fiacre_LocalPortDecl)
gen_fiacre_ParamPortDecl_PortDecl = Generalization(general=PortDecl, specific=fiacre_ParamPortDecl)
gen_fiacre_Synchronization_Communication = Generalization(general=Communication, specific=fiacre_Synchronization)
gen_fiacre_Reception_Communication = Generalization(general=Communication, specific=fiacre_Reception)
gen_fiacre_Union_Type = Generalization(general=Type, specific=fiacre_Union)
gen_fiacre_ConstrPattern_Pattern = Generalization(general=Pattern, specific=fiacre_ConstrPattern)
gen_fiacre_ArrayPattern_Pattern = Generalization(general=Pattern, specific=fiacre_ArrayPattern)
gen_fiacre_FieldPattern_Pattern = Generalization(general=Pattern, specific=fiacre_FieldPattern)
gen_fiacre_ConstrExp_Exp = Generalization(general=Exp, specific=fiacre_ConstrExp)
gen_fiacre_Literal_Pattern = Generalization(general=Pattern, specific=fiacre_Literal)
gen_fiacre_CaseStmt_Statement = Generalization(general=Statement, specific=fiacre_CaseStmt)
gen_fiacre_RefArg_Arg = Generalization(general=Arg, specific=fiacre_RefArg)
gen_fiacre_ConstantDecl_Declaration = Generalization(general=Declaration, specific=fiacre_ConstantDecl)
gen_fiacre_AnyPattern_Pattern = Generalization(general=Pattern, specific=fiacre_AnyPattern)
gen_fiacre_Literal_Exp = Generalization(general=Exp, specific=fiacre_Literal)
gen_fiacre_InlineCollection_Exp = Generalization(general=Exp, specific=fiacre_InlineCollection)
gen_fiacre_Constr_LabeledType = Generalization(general=LabeledType, specific=fiacre_Constr)
gen_fiacre_FiniteBound_MinBound = Generalization(general=MinBound, specific=fiacre_FiniteBound)
gen_fiacre_FiniteBound_MaxBound = Generalization(general=MaxBound, specific=fiacre_FiniteBound)
gen_fiacre_InfiniteBound_MaxBound = Generalization(general=MaxBound, specific=fiacre_InfiniteBound)
gen_fiacre_CondExp_Exp = Generalization(general=Exp, specific=fiacre_CondExp)
gen_fiacre_ConstantRef_Exp = Generalization(general=Exp, specific=fiacre_ConstantRef)
gen_fiacre_ConstantRef_Pattern = Generalization(general=Pattern, specific=fiacre_ConstantRef)
gen_fiacre_Foreach_Statement = Generalization(general=Statement, specific=fiacre_Foreach)

# Domain Model
domain_model = DomainModel(
    name="fiacre",
    types={fiacre_Program, fiacre_Declaration, fiacre_NodeDecl, fiacre_ParamPortDecl, fiacre_LocalPortDecl, fiacre_Statement, fiacre_TypeDecl, fiacre_Type, fiacre_ChannelDecl, fiacre_Channel, fiacre_ComponentDecl, NodeDecl, fiacre_Composition, fiacre_Priority, fiacre_ProcessDecl, fiacre_State, fiacre_Transition, fiacre_PortDecl, Declaration, fiacre_ArgumentVariable, fiacre_LocalVariable, fiacre_Exp, fiacre_Par, Composition, fiacre_InterfacedComp, fiacre_Instance, fiacre_Arg, Arg, fiacre_NullStmt, Statement, fiacre_Assignment, fiacre_Communication, Variable, fiacre_IfStmt, fiacre_Select, fiacre_To, fiacre_Wait, fiacre_MinBound, fiacre_MaxBound, fiacre_DeterministicAssignment, Assignment, fiacre_SingleAssignment, fiacre_NonDeterministicAssignment, fiacre_Pattern, fiacre_WhileStmt, fiacre_NatLiteral, Literal, fiacre_BoolLiteral, fiacre_VarRef, Pattern, fiacre_UnExp, Exp, fiacre_BinExp, fiacre_Variable, fiacre_ArrayElem, fiacre_RecordElem, fiacre_InlineQueue, InlineCollection, fiacre_BasicType, Type, fiacre_BoolType, BasicType, fiacre_NatType, fiacre_IntType, fiacre_Interval, fiacre_Record, fiacre_Field, fiacre_Queue, fiacre_TypeId, fiacre_Profile, Channel, fiacre_InlineArray, fiacre_InlineRecord, fiacre_ValuedField, LabeledType, fiacre_Array, fiacre_Emission, fiacre_Seq, PortDecl, fiacre_Synchronization, Communication, fiacre_Reception, fiacre_Union, fiacre_Constr, fiacre_ConstrPattern, fiacre_ArrayPattern, fiacre_FieldPattern, fiacre_ConstrExp, fiacre_CaseStmt, fiacre_Rule, fiacre_RefArg, fiacre_ConstantDecl, fiacre_AnyPattern, fiacre_Literal, fiacre_InlineCollection, fiacre_LabeledType, fiacre_FiniteBound, MinBound, MaxBound, fiacre_InfiniteBound, fiacre_CondExp, fiacre_ConstantRef, fiacre_Foreach, UnOp, BinOp},
    associations={declaration0, root1, port7, localPort9, initAction11, is13, is14, body15, priority16, state18, transition19, arg3, var5, initializer23, arg25, type26, arg28, port30, composition33, syncPort36, from39, action42, channel21, condition52, then54, else57, statement60, dest62, mini64, maxi65, assignment67, lhs68, condition69, lhs72, port45, condition47, body49, right80, left82, rhs75, exp78, decl85, record91, mini93, maxi95, field98, array86, index88, type101, type104, size106, decl109, type111, value113, size99, pattern117, where119, arg122, statement124, mini126, maxi129, type132, value114, arg141, constr143, arg144, index146, array148, inf135, sup138, rule153, exp154, lhs157, action160, ref163, type165, value167, record151, elem172, type174, cond176, iff178, decl170, body184, iter186, ift181},
    generalizations={gen_fiacre_TypeDecl_Declaration, gen_fiacre_ChannelDecl_Declaration, gen_fiacre_ComponentDecl_NodeDecl, gen_fiacre_ProcessDecl_NodeDecl, gen_fiacre_NodeDecl_Declaration, gen_fiacre_LocalVariable_Variable, gen_fiacre_Par_Composition, gen_fiacre_Instance_Composition, gen_fiacre_Exp_Arg, gen_fiacre_NullStmt_Statement, gen_fiacre_Assignment_Statement, gen_fiacre_Communication_Statement, gen_fiacre_ArgumentVariable_Variable, gen_fiacre_IfStmt_Statement, gen_fiacre_Select_Statement, gen_fiacre_To_Statement, gen_fiacre_Wait_Statement, gen_fiacre_DeterministicAssignment_Assignment, gen_fiacre_NonDeterministicAssignment_Assignment, gen_fiacre_WhileStmt_Statement, gen_fiacre_NatLiteral_Literal, gen_fiacre_BoolLiteral_Literal, gen_fiacre_UnExp_Exp, gen_fiacre_BinExp_Exp, gen_fiacre_VarRef_Pattern, gen_fiacre_VarRef_Exp, gen_fiacre_ArrayElem_Exp, gen_fiacre_RecordElem_Exp, gen_fiacre_InlineQueue_InlineCollection, gen_fiacre_BasicType_Type, gen_fiacre_BoolType_BasicType, gen_fiacre_NatType_BasicType, gen_fiacre_IntType_BasicType, gen_fiacre_Interval_Type, gen_fiacre_Record_Type, gen_fiacre_Queue_Type, gen_fiacre_TypeId_Type, gen_fiacre_Profile_Channel, gen_fiacre_InlineArray_InlineCollection, gen_fiacre_InlineRecord_Exp, gen_fiacre_Field_LabeledType, gen_fiacre_Array_Type, gen_fiacre_Emission_Communication, gen_fiacre_Seq_Statement, gen_fiacre_LocalPortDecl_PortDecl, gen_fiacre_ParamPortDecl_PortDecl, gen_fiacre_Synchronization_Communication, gen_fiacre_Reception_Communication, gen_fiacre_Union_Type, gen_fiacre_ConstrPattern_Pattern, gen_fiacre_ArrayPattern_Pattern, gen_fiacre_FieldPattern_Pattern, gen_fiacre_ConstrExp_Exp, gen_fiacre_Literal_Pattern, gen_fiacre_CaseStmt_Statement, gen_fiacre_RefArg_Arg, gen_fiacre_ConstantDecl_Declaration, gen_fiacre_AnyPattern_Pattern, gen_fiacre_Literal_Exp, gen_fiacre_InlineCollection_Exp, gen_fiacre_Constr_LabeledType, gen_fiacre_FiniteBound_MinBound, gen_fiacre_FiniteBound_MaxBound, gen_fiacre_InfiniteBound_MaxBound, gen_fiacre_CondExp_Exp, gen_fiacre_ConstantRef_Exp, gen_fiacre_ConstantRef_Pattern, gen_fiacre_Foreach_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)