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
debugSeq_DebugSeqModel = Class(name="debugSeq::DebugSeqModel")
debugSeq_DebugVars = Class(name="debugSeq::DebugVars")
debugSeq_CodeBlock = Class(name="debugSeq::CodeBlock")
debugSeq_Block = Class(name="debugSeq::Block")
CodeBlock = Class(name="CodeBlock")
debugSeq_Control = Class(name="debugSeq::Control")
Parameter_ = Class(name="Parameter")
debugSeq_Parameter = Class(name="debugSeq::Parameter")
debugSeq_Assignment = Class(name="debugSeq::Assignment")
Expression = Class(name="Expression")
debugSeq_Ternary = Class(name="debugSeq::Ternary")
debugSeq_Sequences = Class(name="debugSeq::Sequences")
debugSeq_Statement = Class(name="debugSeq::Statement")
debugSeq_VariableDeclaration = Class(name="debugSeq::VariableDeclaration")
Statement = Class(name="Statement")
debugSeq_Expression = Class(name="debugSeq::Expression")
debugSeq_Sequence = Class(name="debugSeq::Sequence")
debugSeq_BitXor = Class(name="debugSeq::BitXor")
debugSeq_BitAnd = Class(name="debugSeq::BitAnd")
debugSeq_Equality = Class(name="debugSeq::Equality")
debugSeq_Or = Class(name="debugSeq::Or")
debugSeq_And = Class(name="debugSeq::And")
debugSeq_BitOr = Class(name="debugSeq::BitOr")
debugSeq_Shift = Class(name="debugSeq::Shift")
debugSeq_Plus = Class(name="debugSeq::Plus")
debugSeq_Comparison = Class(name="debugSeq::Comparison")
debugSeq_SequenceCall = Class(name="debugSeq::SequenceCall")
debugSeq_Query = Class(name="debugSeq::Query")
debugSeq_Div = Class(name="debugSeq::Div")
debugSeq_Rem = Class(name="debugSeq::Rem")
debugSeq_Minus = Class(name="debugSeq::Minus")
debugSeq_Not = Class(name="debugSeq::Not")
debugSeq_BitNot = Class(name="debugSeq::BitNot")
debugSeq_Mul = Class(name="debugSeq::Mul")
debugSeq_Read8 = Class(name="debugSeq::Read8")
debugSeq_Read16 = Class(name="debugSeq::Read16")
debugSeq_Read32 = Class(name="debugSeq::Read32")
debugSeq_Read64 = Class(name="debugSeq::Read64")
debugSeq_QueryValue = Class(name="debugSeq::QueryValue")
debugSeq_Message = Class(name="debugSeq::Message")
debugSeq_LoadDebugInfo = Class(name="debugSeq::LoadDebugInfo")
debugSeq_Write64 = Class(name="debugSeq::Write64")
debugSeq_WriteAP = Class(name="debugSeq::WriteAP")
debugSeq_ReadAP = Class(name="debugSeq::ReadAP")
debugSeq_ReadDP = Class(name="debugSeq::ReadDP")
debugSeq_Write8 = Class(name="debugSeq::Write8")
debugSeq_Write16 = Class(name="debugSeq::Write16")
debugSeq_Write32 = Class(name="debugSeq::Write32")
debugSeq_DapSwjClock = Class(name="debugSeq::DapSwjClock")
debugSeq_WriteDP = Class(name="debugSeq::WriteDP")
debugSeq_DapDelay = Class(name="debugSeq::DapDelay")
debugSeq_DapWriteABORT = Class(name="debugSeq::DapWriteABORT")
debugSeq_DapSwjPins = Class(name="debugSeq::DapSwjPins")
debugSeq_IntConstant = Class(name="debugSeq::IntConstant")
debugSeq_StringConstant = Class(name="debugSeq::StringConstant")
debugSeq_VariableRef = Class(name="debugSeq::VariableRef")
debugSeq_DapSwjSequence = Class(name="debugSeq::DapSwjSequence")
debugSeq_DapJtagSequence = Class(name="debugSeq::DapJtagSequence")

# debugSeq_DebugSeqModel class attributes and methods

# debugSeq_DebugVars class attributes and methods
debugSeq_DebugVars_configfile: Property = Property(name="configfile", type=StringType)
debugSeq_DebugVars_version: Property = Property(name="version", type=StringType)
debugSeq_DebugVars_pname: Property = Property(name="pname", type=StringType)
debugSeq_DebugVars.attributes={debugSeq_DebugVars_version, debugSeq_DebugVars_pname, debugSeq_DebugVars_configfile}

# debugSeq_CodeBlock class attributes and methods
debugSeq_CodeBlock_info: Property = Property(name="info", type=StringType)
debugSeq_CodeBlock.attributes={debugSeq_CodeBlock_info}

# debugSeq_Block class attributes and methods
debugSeq_Block_atomic: Property = Property(name="atomic", type=StringType)
debugSeq_Block.attributes={debugSeq_Block_atomic}

# CodeBlock class attributes and methods

# debugSeq_Control class attributes and methods
debugSeq_Control_timeout: Property = Property(name="timeout", type=StringType)
debugSeq_Control.attributes={debugSeq_Control_timeout}

# Parameter class attributes and methods

# debugSeq_Parameter class attributes and methods

# debugSeq_Assignment class attributes and methods
debugSeq_Assignment_op: Property = Property(name="op", type=StringType)
debugSeq_Assignment.attributes={debugSeq_Assignment_op}

# Expression class attributes and methods

# debugSeq_Ternary class attributes and methods

# debugSeq_Sequences class attributes and methods

# debugSeq_Statement class attributes and methods

# debugSeq_VariableDeclaration class attributes and methods
debugSeq_VariableDeclaration_name: Property = Property(name="name", type=StringType)
debugSeq_VariableDeclaration.attributes={debugSeq_VariableDeclaration_name}

# Statement class attributes and methods

# debugSeq_Expression class attributes and methods

# debugSeq_Sequence class attributes and methods
debugSeq_Sequence_name: Property = Property(name="name", type=StringType)
debugSeq_Sequence_disable: Property = Property(name="disable", type=StringType)
debugSeq_Sequence_pname: Property = Property(name="pname", type=StringType)
debugSeq_Sequence_info: Property = Property(name="info", type=StringType)
debugSeq_Sequence.attributes={debugSeq_Sequence_name, debugSeq_Sequence_pname, debugSeq_Sequence_disable, debugSeq_Sequence_info}

# debugSeq_BitXor class attributes and methods

# debugSeq_BitAnd class attributes and methods

# debugSeq_Equality class attributes and methods
debugSeq_Equality_op: Property = Property(name="op", type=StringType)
debugSeq_Equality.attributes={debugSeq_Equality_op}

# debugSeq_Or class attributes and methods

# debugSeq_And class attributes and methods

# debugSeq_BitOr class attributes and methods

# debugSeq_Shift class attributes and methods
debugSeq_Shift_op: Property = Property(name="op", type=StringType)
debugSeq_Shift.attributes={debugSeq_Shift_op}

# debugSeq_Plus class attributes and methods

# debugSeq_Comparison class attributes and methods
debugSeq_Comparison_op: Property = Property(name="op", type=StringType)
debugSeq_Comparison.attributes={debugSeq_Comparison_op}

# debugSeq_SequenceCall class attributes and methods
debugSeq_SequenceCall_seqname: Property = Property(name="seqname", type=StringType)
debugSeq_SequenceCall.attributes={debugSeq_SequenceCall_seqname}

# debugSeq_Query class attributes and methods
debugSeq_Query_message: Property = Property(name="message", type=StringType)
debugSeq_Query.attributes={debugSeq_Query_message}

# debugSeq_Div class attributes and methods

# debugSeq_Rem class attributes and methods

# debugSeq_Minus class attributes and methods

# debugSeq_Not class attributes and methods

# debugSeq_BitNot class attributes and methods

# debugSeq_Mul class attributes and methods

# debugSeq_Read8 class attributes and methods

# debugSeq_Read16 class attributes and methods

# debugSeq_Read32 class attributes and methods

# debugSeq_Read64 class attributes and methods

# debugSeq_QueryValue class attributes and methods
debugSeq_QueryValue_message: Property = Property(name="message", type=StringType)
debugSeq_QueryValue.attributes={debugSeq_QueryValue_message}

# debugSeq_Message class attributes and methods
debugSeq_Message_format: Property = Property(name="format", type=StringType)
debugSeq_Message.attributes={debugSeq_Message_format}

# debugSeq_LoadDebugInfo class attributes and methods
debugSeq_LoadDebugInfo_path: Property = Property(name="path", type=StringType)
debugSeq_LoadDebugInfo.attributes={debugSeq_LoadDebugInfo_path}

# debugSeq_Write64 class attributes and methods

# debugSeq_WriteAP class attributes and methods

# debugSeq_ReadAP class attributes and methods

# debugSeq_ReadDP class attributes and methods

# debugSeq_Write8 class attributes and methods

# debugSeq_Write16 class attributes and methods

# debugSeq_Write32 class attributes and methods

# debugSeq_DapSwjClock class attributes and methods

# debugSeq_WriteDP class attributes and methods

# debugSeq_DapDelay class attributes and methods

# debugSeq_DapWriteABORT class attributes and methods

# debugSeq_DapSwjPins class attributes and methods

# debugSeq_IntConstant class attributes and methods
debugSeq_IntConstant_value: Property = Property(name="value", type=StringType)
debugSeq_IntConstant.attributes={debugSeq_IntConstant_value}

# debugSeq_StringConstant class attributes and methods
debugSeq_StringConstant_value: Property = Property(name="value", type=StringType)
debugSeq_StringConstant.attributes={debugSeq_StringConstant_value}

# debugSeq_VariableRef class attributes and methods

# debugSeq_DapSwjSequence class attributes and methods

# debugSeq_DapJtagSequence class attributes and methods

# Relationships
debugvars0: BinaryAssociation = BinaryAssociation(
    name="debugvars0",
    ends={
        Property(name="debugSeq_DebugVars", type=debugSeq_DebugSeqModel, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_DebugSeqModel", type=debugSeq_DebugVars, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
codeblocks8: BinaryAssociation = BinaryAssociation(
    name="codeblocks8",
    ends={
        Property(name="debugSeq_CodeBlock", type=debugSeq_Sequence, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Sequence9", type=debugSeq_CodeBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements10: BinaryAssociation = BinaryAssociation(
    name="statements10",
    ends={
        Property(name="debugSeq_Statement11", type=debugSeq_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Block", type=debugSeq_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
if12: BinaryAssociation = BinaryAssociation(
    name="if12",
    ends={
        Property(name="debugSeq_Expression13", type=debugSeq_Control, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Control", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
while14: BinaryAssociation = BinaryAssociation(
    name="while14",
    ends={
        Property(name="debugSeq_Expression16", type=debugSeq_Control, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Control15", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
codeblocks17: BinaryAssociation = BinaryAssociation(
    name="codeblocks17",
    ends={
        Property(name="debugSeq_CodeBlock19", type=debugSeq_Control, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Control18", type=debugSeq_CodeBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left20: BinaryAssociation = BinaryAssociation(
    name="left20",
    ends={
        Property(name="debugSeq_Expression21", type=debugSeq_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Assignment", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right22: BinaryAssociation = BinaryAssociation(
    name="right22",
    ends={
        Property(name="debugSeq_Expression24", type=debugSeq_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Assignment23", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequences1: BinaryAssociation = BinaryAssociation(
    name="sequences1",
    ends={
        Property(name="debugSeq_Sequences", type=debugSeq_DebugSeqModel, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_DebugSeqModel2", type=debugSeq_Sequences, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements3: BinaryAssociation = BinaryAssociation(
    name="statements3",
    ends={
        Property(name="debugSeq_Statement", type=debugSeq_DebugVars, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_DebugVars4", type=debugSeq_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value5: BinaryAssociation = BinaryAssociation(
    name="value5",
    ends={
        Property(name="debugSeq_Expression", type=debugSeq_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_VariableDeclaration", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequences6: BinaryAssociation = BinaryAssociation(
    name="sequences6",
    ends={
        Property(name="debugSeq_Sequence", type=debugSeq_Sequences, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Sequences7", type=debugSeq_Sequence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left43: BinaryAssociation = BinaryAssociation(
    name="left43",
    ends={
        Property(name="debugSeq_Expression44", type=debugSeq_BitOr, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_BitOr", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right45: BinaryAssociation = BinaryAssociation(
    name="right45",
    ends={
        Property(name="debugSeq_Expression47", type=debugSeq_BitOr, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_BitOr46", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left48: BinaryAssociation = BinaryAssociation(
    name="left48",
    ends={
        Property(name="debugSeq_Expression49", type=debugSeq_BitXor, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_BitXor", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right50: BinaryAssociation = BinaryAssociation(
    name="right50",
    ends={
        Property(name="debugSeq_Expression52", type=debugSeq_BitXor, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_BitXor51", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left53: BinaryAssociation = BinaryAssociation(
    name="left53",
    ends={
        Property(name="debugSeq_Expression54", type=debugSeq_BitAnd, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_BitAnd", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right55: BinaryAssociation = BinaryAssociation(
    name="right55",
    ends={
        Property(name="debugSeq_Expression57", type=debugSeq_BitAnd, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_BitAnd56", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left58: BinaryAssociation = BinaryAssociation(
    name="left58",
    ends={
        Property(name="debugSeq_Expression59", type=debugSeq_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Equality", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right60: BinaryAssociation = BinaryAssociation(
    name="right60",
    ends={
        Property(name="debugSeq_Expression62", type=debugSeq_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Equality61", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left25: BinaryAssociation = BinaryAssociation(
    name="left25",
    ends={
        Property(name="debugSeq_Expression26", type=debugSeq_Ternary, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Ternary", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp127: BinaryAssociation = BinaryAssociation(
    name="exp127",
    ends={
        Property(name="debugSeq_Expression29", type=debugSeq_Ternary, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Ternary28", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp230: BinaryAssociation = BinaryAssociation(
    name="exp230",
    ends={
        Property(name="debugSeq_Expression32", type=debugSeq_Ternary, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Ternary31", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left33: BinaryAssociation = BinaryAssociation(
    name="left33",
    ends={
        Property(name="debugSeq_Expression34", type=debugSeq_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Or", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right35: BinaryAssociation = BinaryAssociation(
    name="right35",
    ends={
        Property(name="debugSeq_Expression37", type=debugSeq_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Or36", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left38: BinaryAssociation = BinaryAssociation(
    name="left38",
    ends={
        Property(name="debugSeq_Expression39", type=debugSeq_And, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_And", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right40: BinaryAssociation = BinaryAssociation(
    name="right40",
    ends={
        Property(name="debugSeq_Expression42", type=debugSeq_And, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_And41", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left68: BinaryAssociation = BinaryAssociation(
    name="left68",
    ends={
        Property(name="debugSeq_Expression69", type=debugSeq_Shift, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Shift", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right70: BinaryAssociation = BinaryAssociation(
    name="right70",
    ends={
        Property(name="debugSeq_Expression72", type=debugSeq_Shift, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Shift71", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left73: BinaryAssociation = BinaryAssociation(
    name="left73",
    ends={
        Property(name="debugSeq_Expression74", type=debugSeq_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Plus", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right75: BinaryAssociation = BinaryAssociation(
    name="right75",
    ends={
        Property(name="debugSeq_Expression77", type=debugSeq_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Plus76", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left63: BinaryAssociation = BinaryAssociation(
    name="left63",
    ends={
        Property(name="debugSeq_Expression64", type=debugSeq_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Comparison", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right65: BinaryAssociation = BinaryAssociation(
    name="right65",
    ends={
        Property(name="debugSeq_Expression67", type=debugSeq_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Comparison66", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left83: BinaryAssociation = BinaryAssociation(
    name="left83",
    ends={
        Property(name="debugSeq_Expression84", type=debugSeq_Mul, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Mul", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right85: BinaryAssociation = BinaryAssociation(
    name="right85",
    ends={
        Property(name="debugSeq_Expression87", type=debugSeq_Mul, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Mul86", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type102: BinaryAssociation = BinaryAssociation(
    name="type102",
    ends={
        Property(name="debugSeq_Expression103", type=debugSeq_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Query", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left88: BinaryAssociation = BinaryAssociation(
    name="left88",
    ends={
        Property(name="debugSeq_Expression89", type=debugSeq_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Div", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right90: BinaryAssociation = BinaryAssociation(
    name="right90",
    ends={
        Property(name="debugSeq_Expression92", type=debugSeq_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Div91", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left93: BinaryAssociation = BinaryAssociation(
    name="left93",
    ends={
        Property(name="debugSeq_Expression94", type=debugSeq_Rem, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Rem", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right95: BinaryAssociation = BinaryAssociation(
    name="right95",
    ends={
        Property(name="debugSeq_Expression97", type=debugSeq_Rem, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Rem96", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left78: BinaryAssociation = BinaryAssociation(
    name="left78",
    ends={
        Property(name="debugSeq_Expression79", type=debugSeq_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Minus", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression98: BinaryAssociation = BinaryAssociation(
    name="expression98",
    ends={
        Property(name="debugSeq_Expression99", type=debugSeq_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Not", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right80: BinaryAssociation = BinaryAssociation(
    name="right80",
    ends={
        Property(name="debugSeq_Expression82", type=debugSeq_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Minus81", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression100: BinaryAssociation = BinaryAssociation(
    name="expression100",
    ends={
        Property(name="debugSeq_Expression101", type=debugSeq_BitNot, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_BitNot", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addr113: BinaryAssociation = BinaryAssociation(
    name="addr113",
    ends={
        Property(name="debugSeq_Expression114", type=debugSeq_Read8, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Read8", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addr115: BinaryAssociation = BinaryAssociation(
    name="addr115",
    ends={
        Property(name="debugSeq_Expression116", type=debugSeq_Read16, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Read16", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addr117: BinaryAssociation = BinaryAssociation(
    name="addr117",
    ends={
        Property(name="debugSeq_Expression118", type=debugSeq_Read32, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Read32", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
default104: BinaryAssociation = BinaryAssociation(
    name="default104",
    ends={
        Property(name="debugSeq_Expression106", type=debugSeq_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Query105", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
default107: BinaryAssociation = BinaryAssociation(
    name="default107",
    ends={
        Property(name="debugSeq_Expression108", type=debugSeq_QueryValue, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_QueryValue", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type109: BinaryAssociation = BinaryAssociation(
    name="type109",
    ends={
        Property(name="debugSeq_Expression110", type=debugSeq_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Message", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters111: BinaryAssociation = BinaryAssociation(
    name="parameters111",
    ends={
        Property(name="debugSeq_Parameter", type=debugSeq_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Message112", type=debugSeq_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
val137: BinaryAssociation = BinaryAssociation(
    name="val137",
    ends={
        Property(name="debugSeq_Expression139", type=debugSeq_Write32, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Write32138", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addr140: BinaryAssociation = BinaryAssociation(
    name="addr140",
    ends={
        Property(name="debugSeq_Expression141", type=debugSeq_Write64, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Write64", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
val142: BinaryAssociation = BinaryAssociation(
    name="val142",
    ends={
        Property(name="debugSeq_Expression144", type=debugSeq_Write64, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Write64143", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addr145: BinaryAssociation = BinaryAssociation(
    name="addr145",
    ends={
        Property(name="debugSeq_Expression146", type=debugSeq_WriteAP, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_WriteAP", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addr119: BinaryAssociation = BinaryAssociation(
    name="addr119",
    ends={
        Property(name="debugSeq_Expression120", type=debugSeq_Read64, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Read64", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addr121: BinaryAssociation = BinaryAssociation(
    name="addr121",
    ends={
        Property(name="debugSeq_Expression122", type=debugSeq_ReadAP, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_ReadAP", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addr123: BinaryAssociation = BinaryAssociation(
    name="addr123",
    ends={
        Property(name="debugSeq_Expression124", type=debugSeq_ReadDP, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_ReadDP", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addr125: BinaryAssociation = BinaryAssociation(
    name="addr125",
    ends={
        Property(name="debugSeq_Expression126", type=debugSeq_Write8, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Write8", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
val127: BinaryAssociation = BinaryAssociation(
    name="val127",
    ends={
        Property(name="debugSeq_Expression129", type=debugSeq_Write8, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Write8128", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addr130: BinaryAssociation = BinaryAssociation(
    name="addr130",
    ends={
        Property(name="debugSeq_Expression131", type=debugSeq_Write16, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Write16", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
val132: BinaryAssociation = BinaryAssociation(
    name="val132",
    ends={
        Property(name="debugSeq_Expression134", type=debugSeq_Write16, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Write16133", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addr135: BinaryAssociation = BinaryAssociation(
    name="addr135",
    ends={
        Property(name="debugSeq_Expression136", type=debugSeq_Write32, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_Write32", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pinselect161: BinaryAssociation = BinaryAssociation(
    name="pinselect161",
    ends={
        Property(name="debugSeq_Expression163", type=debugSeq_DapSwjPins, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_DapSwjPins162", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pinwait164: BinaryAssociation = BinaryAssociation(
    name="pinwait164",
    ends={
        Property(name="debugSeq_Expression166", type=debugSeq_DapSwjPins, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_DapSwjPins165", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value167: BinaryAssociation = BinaryAssociation(
    name="value167",
    ends={
        Property(name="debugSeq_Expression168", type=debugSeq_DapSwjClock, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_DapSwjClock", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
val147: BinaryAssociation = BinaryAssociation(
    name="val147",
    ends={
        Property(name="debugSeq_Expression149", type=debugSeq_WriteAP, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_WriteAP148", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addr150: BinaryAssociation = BinaryAssociation(
    name="addr150",
    ends={
        Property(name="debugSeq_Expression151", type=debugSeq_WriteDP, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_WriteDP", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
val152: BinaryAssociation = BinaryAssociation(
    name="val152",
    ends={
        Property(name="debugSeq_Expression154", type=debugSeq_WriteDP, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_WriteDP153", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
delay155: BinaryAssociation = BinaryAssociation(
    name="delay155",
    ends={
        Property(name="debugSeq_Expression156", type=debugSeq_DapDelay, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_DapDelay", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value157: BinaryAssociation = BinaryAssociation(
    name="value157",
    ends={
        Property(name="debugSeq_Expression158", type=debugSeq_DapWriteABORT, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_DapWriteABORT", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pinout159: BinaryAssociation = BinaryAssociation(
    name="pinout159",
    ends={
        Property(name="debugSeq_Expression160", type=debugSeq_DapSwjPins, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_DapSwjPins", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable182: BinaryAssociation = BinaryAssociation(
    name="variable182",
    ends={
        Property(name="debugSeq_VariableDeclaration183", type=debugSeq_VariableRef, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_VariableRef", type=debugSeq_VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
cnt169: BinaryAssociation = BinaryAssociation(
    name="cnt169",
    ends={
        Property(name="debugSeq_Expression170", type=debugSeq_DapSwjSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_DapSwjSequence", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
val171: BinaryAssociation = BinaryAssociation(
    name="val171",
    ends={
        Property(name="debugSeq_Expression173", type=debugSeq_DapSwjSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_DapSwjSequence172", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cnt174: BinaryAssociation = BinaryAssociation(
    name="cnt174",
    ends={
        Property(name="debugSeq_Expression175", type=debugSeq_DapJtagSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_DapJtagSequence", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tms176: BinaryAssociation = BinaryAssociation(
    name="tms176",
    ends={
        Property(name="debugSeq_Expression178", type=debugSeq_DapJtagSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_DapJtagSequence177", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tdi179: BinaryAssociation = BinaryAssociation(
    name="tdi179",
    ends={
        Property(name="debugSeq_Expression181", type=debugSeq_DapJtagSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="debugSeq_DapJtagSequence180", type=debugSeq_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_debugSeq_Block_CodeBlock = Generalization(general=CodeBlock, specific=debugSeq_Block)
gen_debugSeq_Control_CodeBlock = Generalization(general=CodeBlock, specific=debugSeq_Control)
gen_debugSeq_Expression_Statement = Generalization(general=Statement, specific=debugSeq_Expression)
gen_debugSeq_Expression_Parameter = Generalization(general=Parameter_, specific=debugSeq_Expression)
gen_debugSeq_Assignment_Expression = Generalization(general=Expression, specific=debugSeq_Assignment)
gen_debugSeq_Ternary_Expression = Generalization(general=Expression, specific=debugSeq_Ternary)
gen_debugSeq_VariableDeclaration_Statement = Generalization(general=Statement, specific=debugSeq_VariableDeclaration)
gen_debugSeq_BitXor_Expression = Generalization(general=Expression, specific=debugSeq_BitXor)
gen_debugSeq_BitAnd_Expression = Generalization(general=Expression, specific=debugSeq_BitAnd)
gen_debugSeq_Equality_Expression = Generalization(general=Expression, specific=debugSeq_Equality)
gen_debugSeq_Or_Expression = Generalization(general=Expression, specific=debugSeq_Or)
gen_debugSeq_And_Expression = Generalization(general=Expression, specific=debugSeq_And)
gen_debugSeq_BitOr_Expression = Generalization(general=Expression, specific=debugSeq_BitOr)
gen_debugSeq_Shift_Expression = Generalization(general=Expression, specific=debugSeq_Shift)
gen_debugSeq_Plus_Expression = Generalization(general=Expression, specific=debugSeq_Plus)
gen_debugSeq_Comparison_Expression = Generalization(general=Expression, specific=debugSeq_Comparison)
gen_debugSeq_SequenceCall_Expression = Generalization(general=Expression, specific=debugSeq_SequenceCall)
gen_debugSeq_Query_Expression = Generalization(general=Expression, specific=debugSeq_Query)
gen_debugSeq_Div_Expression = Generalization(general=Expression, specific=debugSeq_Div)
gen_debugSeq_Rem_Expression = Generalization(general=Expression, specific=debugSeq_Rem)
gen_debugSeq_Minus_Expression = Generalization(general=Expression, specific=debugSeq_Minus)
gen_debugSeq_Not_Expression = Generalization(general=Expression, specific=debugSeq_Not)
gen_debugSeq_BitNot_Expression = Generalization(general=Expression, specific=debugSeq_BitNot)
gen_debugSeq_Mul_Expression = Generalization(general=Expression, specific=debugSeq_Mul)
gen_debugSeq_Read8_Expression = Generalization(general=Expression, specific=debugSeq_Read8)
gen_debugSeq_Read16_Expression = Generalization(general=Expression, specific=debugSeq_Read16)
gen_debugSeq_Read32_Expression = Generalization(general=Expression, specific=debugSeq_Read32)
gen_debugSeq_Read64_Expression = Generalization(general=Expression, specific=debugSeq_Read64)
gen_debugSeq_QueryValue_Expression = Generalization(general=Expression, specific=debugSeq_QueryValue)
gen_debugSeq_Message_Expression = Generalization(general=Expression, specific=debugSeq_Message)
gen_debugSeq_LoadDebugInfo_Expression = Generalization(general=Expression, specific=debugSeq_LoadDebugInfo)
gen_debugSeq_Write64_Expression = Generalization(general=Expression, specific=debugSeq_Write64)
gen_debugSeq_WriteAP_Expression = Generalization(general=Expression, specific=debugSeq_WriteAP)
gen_debugSeq_ReadAP_Expression = Generalization(general=Expression, specific=debugSeq_ReadAP)
gen_debugSeq_ReadDP_Expression = Generalization(general=Expression, specific=debugSeq_ReadDP)
gen_debugSeq_Write8_Expression = Generalization(general=Expression, specific=debugSeq_Write8)
gen_debugSeq_Write16_Expression = Generalization(general=Expression, specific=debugSeq_Write16)
gen_debugSeq_Write32_Expression = Generalization(general=Expression, specific=debugSeq_Write32)
gen_debugSeq_DapSwjClock_Expression = Generalization(general=Expression, specific=debugSeq_DapSwjClock)
gen_debugSeq_WriteDP_Expression = Generalization(general=Expression, specific=debugSeq_WriteDP)
gen_debugSeq_DapDelay_Expression = Generalization(general=Expression, specific=debugSeq_DapDelay)
gen_debugSeq_DapWriteABORT_Expression = Generalization(general=Expression, specific=debugSeq_DapWriteABORT)
gen_debugSeq_DapSwjPins_Expression = Generalization(general=Expression, specific=debugSeq_DapSwjPins)
gen_debugSeq_IntConstant_Expression = Generalization(general=Expression, specific=debugSeq_IntConstant)
gen_debugSeq_StringConstant_Expression = Generalization(general=Expression, specific=debugSeq_StringConstant)
gen_debugSeq_VariableRef_Expression = Generalization(general=Expression, specific=debugSeq_VariableRef)
gen_debugSeq_DapSwjSequence_Expression = Generalization(general=Expression, specific=debugSeq_DapSwjSequence)
gen_debugSeq_DapJtagSequence_Expression = Generalization(general=Expression, specific=debugSeq_DapJtagSequence)

# Domain Model
domain_model = DomainModel(
    name="debugSeq",
    types={debugSeq_DebugSeqModel, debugSeq_DebugVars, debugSeq_CodeBlock, debugSeq_Block, CodeBlock, debugSeq_Control, Parameter_, debugSeq_Parameter, debugSeq_Assignment, Expression, debugSeq_Ternary, debugSeq_Sequences, debugSeq_Statement, debugSeq_VariableDeclaration, Statement, debugSeq_Expression, debugSeq_Sequence, debugSeq_BitXor, debugSeq_BitAnd, debugSeq_Equality, debugSeq_Or, debugSeq_And, debugSeq_BitOr, debugSeq_Shift, debugSeq_Plus, debugSeq_Comparison, debugSeq_SequenceCall, debugSeq_Query, debugSeq_Div, debugSeq_Rem, debugSeq_Minus, debugSeq_Not, debugSeq_BitNot, debugSeq_Mul, debugSeq_Read8, debugSeq_Read16, debugSeq_Read32, debugSeq_Read64, debugSeq_QueryValue, debugSeq_Message, debugSeq_LoadDebugInfo, debugSeq_Write64, debugSeq_WriteAP, debugSeq_ReadAP, debugSeq_ReadDP, debugSeq_Write8, debugSeq_Write16, debugSeq_Write32, debugSeq_DapSwjClock, debugSeq_WriteDP, debugSeq_DapDelay, debugSeq_DapWriteABORT, debugSeq_DapSwjPins, debugSeq_IntConstant, debugSeq_StringConstant, debugSeq_VariableRef, debugSeq_DapSwjSequence, debugSeq_DapJtagSequence},
    associations={debugvars0, codeblocks8, statements10, if12, while14, codeblocks17, left20, right22, sequences1, statements3, value5, sequences6, left43, right45, left48, right50, left53, right55, left58, right60, left25, exp127, exp230, left33, right35, left38, right40, left68, right70, left73, right75, left63, right65, left83, right85, type102, left88, right90, left93, right95, left78, expression98, right80, expression100, addr113, addr115, addr117, default104, default107, type109, parameters111, val137, addr140, val142, addr145, addr119, addr121, addr123, addr125, val127, addr130, val132, addr135, pinselect161, pinwait164, value167, val147, addr150, val152, delay155, value157, pinout159, variable182, cnt169, val171, cnt174, tms176, tdi179},
    generalizations={gen_debugSeq_Block_CodeBlock, gen_debugSeq_Control_CodeBlock, gen_debugSeq_Expression_Statement, gen_debugSeq_Expression_Parameter, gen_debugSeq_Assignment_Expression, gen_debugSeq_Ternary_Expression, gen_debugSeq_VariableDeclaration_Statement, gen_debugSeq_BitXor_Expression, gen_debugSeq_BitAnd_Expression, gen_debugSeq_Equality_Expression, gen_debugSeq_Or_Expression, gen_debugSeq_And_Expression, gen_debugSeq_BitOr_Expression, gen_debugSeq_Shift_Expression, gen_debugSeq_Plus_Expression, gen_debugSeq_Comparison_Expression, gen_debugSeq_SequenceCall_Expression, gen_debugSeq_Query_Expression, gen_debugSeq_Div_Expression, gen_debugSeq_Rem_Expression, gen_debugSeq_Minus_Expression, gen_debugSeq_Not_Expression, gen_debugSeq_BitNot_Expression, gen_debugSeq_Mul_Expression, gen_debugSeq_Read8_Expression, gen_debugSeq_Read16_Expression, gen_debugSeq_Read32_Expression, gen_debugSeq_Read64_Expression, gen_debugSeq_QueryValue_Expression, gen_debugSeq_Message_Expression, gen_debugSeq_LoadDebugInfo_Expression, gen_debugSeq_Write64_Expression, gen_debugSeq_WriteAP_Expression, gen_debugSeq_ReadAP_Expression, gen_debugSeq_ReadDP_Expression, gen_debugSeq_Write8_Expression, gen_debugSeq_Write16_Expression, gen_debugSeq_Write32_Expression, gen_debugSeq_DapSwjClock_Expression, gen_debugSeq_WriteDP_Expression, gen_debugSeq_DapDelay_Expression, gen_debugSeq_DapWriteABORT_Expression, gen_debugSeq_DapSwjPins_Expression, gen_debugSeq_IntConstant_Expression, gen_debugSeq_StringConstant_Expression, gen_debugSeq_VariableRef_Expression, gen_debugSeq_DapSwjSequence_Expression, gen_debugSeq_DapJtagSequence_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)