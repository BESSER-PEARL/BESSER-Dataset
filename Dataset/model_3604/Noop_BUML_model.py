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
AssignmentType: Enumeration = Enumeration(
    name="AssignmentType",
    literals={
            EnumerationLiteral(name="ASSIGN"),
			EnumerationLiteral(name="ADD_ASSIGN"),
			EnumerationLiteral(name="SUB_ASSIGN"),
			EnumerationLiteral(name="MUL_ASSIGN"),
			EnumerationLiteral(name="DIV_ASSIGN"),
			EnumerationLiteral(name="MOD_ASSIGN"),
			EnumerationLiteral(name="BOR_ASSIGN"),
			EnumerationLiteral(name="BAN_ASSIGN"),
			EnumerationLiteral(name="XOR_ASSIGN"),
			EnumerationLiteral(name="BLS_ASSIGN"),
			EnumerationLiteral(name="BRS_ASSIGN")
    }
)

StorageType: Enumeration = Enumeration(
    name="StorageType",
    literals={
            EnumerationLiteral(name="INESPRG"),
			EnumerationLiteral(name="INESCHR"),
			EnumerationLiteral(name="INESMAPPER"),
			EnumerationLiteral(name="PRGROM"),
			EnumerationLiteral(name="CHRROM"),
			EnumerationLiteral(name="INESMIR"),
			EnumerationLiteral(name="ZP"),
			EnumerationLiteral(name="INLINE"),
			EnumerationLiteral(name="RESET"),
			EnumerationLiteral(name="NMI"),
			EnumerationLiteral(name="IRQ"),
			EnumerationLiteral(name="MMC3CFG")
    }
)

# Classes
noop_NoopClass = Class(name="noop::NoopClass")
noop_Member = Class(name="noop::Member")
noop_Storage = Class(name="noop::Storage")
noop_Expression = Class(name="noop::Expression")
noop_Variable = Class(name="noop::Variable")
Member = Class(name="Member")
Statement = Class(name="Statement")
noop_Length = Class(name="noop::Length")
noop_Method = Class(name="noop::Method")
noop_Block = Class(name="noop::Block")
noop_Statement = Class(name="noop::Statement")
noop_ReturnStatement = Class(name="noop::ReturnStatement")
noop_IfStatement = Class(name="noop::IfStatement")
noop_ElseStatement = Class(name="noop::ElseStatement")
noop_ForStatement = Class(name="noop::ForStatement")
noop_ForeverStatement = Class(name="noop::ForeverStatement")
noop_ContinueStatement = Class(name="noop::ContinueStatement")
noop_BreakStatement = Class(name="noop::BreakStatement")
noop_AsmStatement = Class(name="noop::AsmStatement")
noop_Constructor = Class(name="noop::Constructor")
noop_ConstructorField = Class(name="noop::ConstructorField")
noop_Index = Class(name="noop::Index")
noop_BOrExpression = Class(name="noop::BOrExpression")
noop_AssignmentExpression = Class(name="noop::AssignmentExpression")
Expression = Class(name="Expression")
noop_BXorExpression = Class(name="noop::BXorExpression")
noop_OrExpression = Class(name="noop::OrExpression")
noop_AndExpression = Class(name="noop::AndExpression")
noop_DifferExpression = Class(name="noop::DifferExpression")
noop_GtExpression = Class(name="noop::GtExpression")
noop_BAndExpression = Class(name="noop::BAndExpression")
noop_EqualsExpression = Class(name="noop::EqualsExpression")
noop_LtExpression = Class(name="noop::LtExpression")
noop_LeExpression = Class(name="noop::LeExpression")
noop_InstanceOfExpression = Class(name="noop::InstanceOfExpression")
noop_GeExpression = Class(name="noop::GeExpression")
noop_RShiftExpression = Class(name="noop::RShiftExpression")
noop_AddExpression = Class(name="noop::AddExpression")
noop_LShiftExpression = Class(name="noop::LShiftExpression")
noop_MulExpression = Class(name="noop::MulExpression")
noop_DivExpression = Class(name="noop::DivExpression")
noop_SubExpression = Class(name="noop::SubExpression")
noop_CastExpression = Class(name="noop::CastExpression")
noop_ComplementExpression = Class(name="noop::ComplementExpression")
noop_NotExpression = Class(name="noop::NotExpression")
noop_ModExpression = Class(name="noop::ModExpression")
noop_DecExpression = Class(name="noop::DecExpression")
noop_IncExpression = Class(name="noop::IncExpression")
noop_MemberSelect = Class(name="noop::MemberSelect")
noop_SigNegExpression = Class(name="noop::SigNegExpression")
noop_SigPosExpression = Class(name="noop::SigPosExpression")
noop_ByteLiteral = Class(name="noop::ByteLiteral")
noop_BoolLiteral = Class(name="noop::BoolLiteral")
noop_StringLiteral = Class(name="noop::StringLiteral")
noop_ArrayLiteral = Class(name="noop::ArrayLiteral")
noop_This = Class(name="noop::This")
noop_MemberRef = Class(name="noop::MemberRef")
noop_Super = Class(name="noop::Super")
noop_NewInstance = Class(name="noop::NewInstance")

# noop_NoopClass class attributes and methods
noop_NoopClass_name: Property = Property(name="name", type=StringType)
noop_NoopClass.attributes={noop_NoopClass_name}

# noop_Member class attributes and methods
noop_Member_name: Property = Property(name="name", type=StringType)
noop_Member.attributes={noop_Member_name}

# noop_Storage class attributes and methods
noop_Storage_type: Property = Property(name="type", type=StringType)
noop_Storage.attributes={noop_Storage_type}

# noop_Expression class attributes and methods

# noop_Variable class attributes and methods

# Member class attributes and methods

# Statement class attributes and methods

# noop_Length class attributes and methods

# noop_Method class attributes and methods

# noop_Block class attributes and methods

# noop_Statement class attributes and methods

# noop_ReturnStatement class attributes and methods
noop_ReturnStatement_name: Property = Property(name="name", type=StringType)
noop_ReturnStatement.attributes={noop_ReturnStatement_name}

# noop_IfStatement class attributes and methods
noop_IfStatement_name: Property = Property(name="name", type=StringType)
noop_IfStatement.attributes={noop_IfStatement_name}

# noop_ElseStatement class attributes and methods
noop_ElseStatement_name: Property = Property(name="name", type=StringType)
noop_ElseStatement.attributes={noop_ElseStatement_name}

# noop_ForStatement class attributes and methods
noop_ForStatement_name: Property = Property(name="name", type=StringType)
noop_ForStatement.attributes={noop_ForStatement_name}

# noop_ForeverStatement class attributes and methods
noop_ForeverStatement_name: Property = Property(name="name", type=StringType)
noop_ForeverStatement.attributes={noop_ForeverStatement_name}

# noop_ContinueStatement class attributes and methods
noop_ContinueStatement_name: Property = Property(name="name", type=StringType)
noop_ContinueStatement.attributes={noop_ContinueStatement_name}

# noop_BreakStatement class attributes and methods
noop_BreakStatement_name: Property = Property(name="name", type=StringType)
noop_BreakStatement.attributes={noop_BreakStatement_name}

# noop_AsmStatement class attributes and methods
noop_AsmStatement_codes: Property = Property(name="codes", type=StringType)
noop_AsmStatement.attributes={noop_AsmStatement_codes}

# noop_Constructor class attributes and methods

# noop_ConstructorField class attributes and methods

# noop_Index class attributes and methods

# noop_BOrExpression class attributes and methods

# noop_AssignmentExpression class attributes and methods
noop_AssignmentExpression_assignment: Property = Property(name="assignment", type=StringType)
noop_AssignmentExpression.attributes={noop_AssignmentExpression_assignment}

# Expression class attributes and methods

# noop_BXorExpression class attributes and methods

# noop_OrExpression class attributes and methods

# noop_AndExpression class attributes and methods

# noop_DifferExpression class attributes and methods

# noop_GtExpression class attributes and methods

# noop_BAndExpression class attributes and methods

# noop_EqualsExpression class attributes and methods

# noop_LtExpression class attributes and methods

# noop_LeExpression class attributes and methods

# noop_InstanceOfExpression class attributes and methods

# noop_GeExpression class attributes and methods

# noop_RShiftExpression class attributes and methods

# noop_AddExpression class attributes and methods

# noop_LShiftExpression class attributes and methods

# noop_MulExpression class attributes and methods

# noop_DivExpression class attributes and methods

# noop_SubExpression class attributes and methods

# noop_CastExpression class attributes and methods

# noop_ComplementExpression class attributes and methods

# noop_NotExpression class attributes and methods

# noop_ModExpression class attributes and methods

# noop_DecExpression class attributes and methods

# noop_IncExpression class attributes and methods

# noop_MemberSelect class attributes and methods
noop_MemberSelect_hasArgs: Property = Property(name="hasArgs", type=BooleanType)
noop_MemberSelect.attributes={noop_MemberSelect_hasArgs}

# noop_SigNegExpression class attributes and methods

# noop_SigPosExpression class attributes and methods

# noop_ByteLiteral class attributes and methods
noop_ByteLiteral_value: Property = Property(name="value", type=StringType)
noop_ByteLiteral.attributes={noop_ByteLiteral_value}

# noop_BoolLiteral class attributes and methods
noop_BoolLiteral_value: Property = Property(name="value", type=BooleanType)
noop_BoolLiteral.attributes={noop_BoolLiteral_value}

# noop_StringLiteral class attributes and methods
noop_StringLiteral_value: Property = Property(name="value", type=StringType)
noop_StringLiteral.attributes={noop_StringLiteral_value}

# noop_ArrayLiteral class attributes and methods

# noop_This class attributes and methods

# noop_MemberRef class attributes and methods
noop_MemberRef_hasArgs: Property = Property(name="hasArgs", type=BooleanType)
noop_MemberRef.attributes={noop_MemberRef_hasArgs}

# noop_Super class attributes and methods

# noop_NewInstance class attributes and methods

# Relationships
superClass1: BinaryAssociation = BinaryAssociation(
    name="superClass1",
    ends={
        Property(name="noop_NoopClass", type=noop_NoopClass, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_NoopClass0", type=noop_NoopClass, multiplicity=Multiplicity(0, 1))
    }
)
members2: BinaryAssociation = BinaryAssociation(
    name="members2",
    ends={
        Property(name="noop_Member", type=noop_NoopClass, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_NoopClass3", type=noop_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
storage4: BinaryAssociation = BinaryAssociation(
    name="storage4",
    ends={
        Property(name="noop_Storage", type=noop_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_Member5", type=noop_Storage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value21: BinaryAssociation = BinaryAssociation(
    name="value21",
    ends={
        Property(name="noop_Expression22", type=noop_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_ReturnStatement", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
location6: BinaryAssociation = BinaryAssociation(
    name="location6",
    ends={
        Property(name="noop_Expression", type=noop_Storage, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_Storage7", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value8: BinaryAssociation = BinaryAssociation(
    name="value8",
    ends={
        Property(name="noop_Expression9", type=noop_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_Variable", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type10: BinaryAssociation = BinaryAssociation(
    name="type10",
    ends={
        Property(name="noop_NoopClass12", type=noop_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_Variable11", type=noop_NoopClass, multiplicity=Multiplicity(0, 1))
    }
)
dimension13: BinaryAssociation = BinaryAssociation(
    name="dimension13",
    ends={
        Property(name="noop_Length", type=noop_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_Variable14", type=noop_Length, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
params15: BinaryAssociation = BinaryAssociation(
    name="params15",
    ends={
        Property(name="noop_Variable16", type=noop_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_Method", type=noop_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body17: BinaryAssociation = BinaryAssociation(
    name="body17",
    ends={
        Property(name="noop_Block", type=noop_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_Method18", type=noop_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements19: BinaryAssociation = BinaryAssociation(
    name="statements19",
    ends={
        Property(name="noop_Statement", type=noop_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_Block20", type=noop_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition41: BinaryAssociation = BinaryAssociation(
    name="condition41",
    ends={
        Property(name="noop_Expression43", type=noop_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_ForStatement42", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition23: BinaryAssociation = BinaryAssociation(
    name="condition23",
    ends={
        Property(name="noop_Expression24", type=noop_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_IfStatement", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body25: BinaryAssociation = BinaryAssociation(
    name="body25",
    ends={
        Property(name="noop_Block27", type=noop_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_IfStatement26", type=noop_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
else28: BinaryAssociation = BinaryAssociation(
    name="else28",
    ends={
        Property(name="noop_ElseStatement", type=noop_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_IfStatement29", type=noop_ElseStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body30: BinaryAssociation = BinaryAssociation(
    name="body30",
    ends={
        Property(name="noop_Block32", type=noop_ElseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_ElseStatement31", type=noop_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
if33: BinaryAssociation = BinaryAssociation(
    name="if33",
    ends={
        Property(name="noop_IfStatement35", type=noop_ElseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_ElseStatement34", type=noop_IfStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables36: BinaryAssociation = BinaryAssociation(
    name="variables36",
    ends={
        Property(name="noop_Variable37", type=noop_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_ForStatement", type=noop_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assignments38: BinaryAssociation = BinaryAssociation(
    name="assignments38",
    ends={
        Property(name="noop_Expression40", type=noop_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_ForStatement39", type=noop_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fields54: BinaryAssociation = BinaryAssociation(
    name="fields54",
    ends={
        Property(name="noop_Constructor", type=noop_ConstructorField, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="noop_ConstructorField", type=noop_Constructor, multiplicity=Multiplicity(1, 1))
    }
)
expressions44: BinaryAssociation = BinaryAssociation(
    name="expressions44",
    ends={
        Property(name="noop_Expression46", type=noop_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_ForStatement45", type=noop_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body47: BinaryAssociation = BinaryAssociation(
    name="body47",
    ends={
        Property(name="noop_Block49", type=noop_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_ForStatement48", type=noop_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body50: BinaryAssociation = BinaryAssociation(
    name="body50",
    ends={
        Property(name="noop_Block51", type=noop_ForeverStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_ForeverStatement", type=noop_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vars52: BinaryAssociation = BinaryAssociation(
    name="vars52",
    ends={
        Property(name="noop_Expression53", type=noop_AsmStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_AsmStatement", type=noop_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable55: BinaryAssociation = BinaryAssociation(
    name="variable55",
    ends={
        Property(name="noop_Variable57", type=noop_ConstructorField, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_ConstructorField56", type=noop_Variable, multiplicity=Multiplicity(0, 1))
    }
)
value58: BinaryAssociation = BinaryAssociation(
    name="value58",
    ends={
        Property(name="noop_Expression60", type=noop_ConstructorField, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_ConstructorField59", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value61: BinaryAssociation = BinaryAssociation(
    name="value61",
    ends={
        Property(name="noop_Expression62", type=noop_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_Index", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value63: BinaryAssociation = BinaryAssociation(
    name="value63",
    ends={
        Property(name="noop_Expression65", type=noop_Length, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_Length64", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right78: BinaryAssociation = BinaryAssociation(
    name="right78",
    ends={
        Property(name="noop_Expression80", type=noop_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_AndExpression79", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left81: BinaryAssociation = BinaryAssociation(
    name="left81",
    ends={
        Property(name="noop_Expression82", type=noop_BOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_BOrExpression", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right83: BinaryAssociation = BinaryAssociation(
    name="right83",
    ends={
        Property(name="noop_Expression85", type=noop_BOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_BOrExpression84", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left66: BinaryAssociation = BinaryAssociation(
    name="left66",
    ends={
        Property(name="noop_Expression67", type=noop_AssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_AssignmentExpression", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left86: BinaryAssociation = BinaryAssociation(
    name="left86",
    ends={
        Property(name="noop_Expression87", type=noop_BXorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_BXorExpression", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right88: BinaryAssociation = BinaryAssociation(
    name="right88",
    ends={
        Property(name="noop_Expression90", type=noop_BXorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_BXorExpression89", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right68: BinaryAssociation = BinaryAssociation(
    name="right68",
    ends={
        Property(name="noop_Expression70", type=noop_AssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_AssignmentExpression69", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left71: BinaryAssociation = BinaryAssociation(
    name="left71",
    ends={
        Property(name="noop_Expression72", type=noop_OrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_OrExpression", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right73: BinaryAssociation = BinaryAssociation(
    name="right73",
    ends={
        Property(name="noop_Expression75", type=noop_OrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_OrExpression74", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left76: BinaryAssociation = BinaryAssociation(
    name="left76",
    ends={
        Property(name="noop_Expression77", type=noop_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_AndExpression", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left96: BinaryAssociation = BinaryAssociation(
    name="left96",
    ends={
        Property(name="noop_EqualsExpression", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="noop_Expression97", type=noop_EqualsExpression, multiplicity=Multiplicity(1, 1))
    }
)
right98: BinaryAssociation = BinaryAssociation(
    name="right98",
    ends={
        Property(name="noop_Expression100", type=noop_EqualsExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_EqualsExpression99", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left101: BinaryAssociation = BinaryAssociation(
    name="left101",
    ends={
        Property(name="noop_Expression102", type=noop_DifferExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_DifferExpression", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right103: BinaryAssociation = BinaryAssociation(
    name="right103",
    ends={
        Property(name="noop_Expression105", type=noop_DifferExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_DifferExpression104", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left106: BinaryAssociation = BinaryAssociation(
    name="left106",
    ends={
        Property(name="noop_Expression107", type=noop_GtExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_GtExpression", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left91: BinaryAssociation = BinaryAssociation(
    name="left91",
    ends={
        Property(name="noop_Expression92", type=noop_BAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_BAndExpression", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right93: BinaryAssociation = BinaryAssociation(
    name="right93",
    ends={
        Property(name="noop_Expression95", type=noop_BAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_BAndExpression94", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left116: BinaryAssociation = BinaryAssociation(
    name="left116",
    ends={
        Property(name="noop_Expression117", type=noop_LtExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_LtExpression", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right118: BinaryAssociation = BinaryAssociation(
    name="right118",
    ends={
        Property(name="noop_Expression120", type=noop_LtExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_LtExpression119", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left121: BinaryAssociation = BinaryAssociation(
    name="left121",
    ends={
        Property(name="noop_Expression122", type=noop_LeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_LeExpression", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right123: BinaryAssociation = BinaryAssociation(
    name="right123",
    ends={
        Property(name="noop_Expression125", type=noop_LeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_LeExpression124", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right108: BinaryAssociation = BinaryAssociation(
    name="right108",
    ends={
        Property(name="noop_Expression110", type=noop_GtExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_GtExpression109", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left111: BinaryAssociation = BinaryAssociation(
    name="left111",
    ends={
        Property(name="noop_Expression112", type=noop_GeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_GeExpression", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right113: BinaryAssociation = BinaryAssociation(
    name="right113",
    ends={
        Property(name="noop_Expression115", type=noop_GeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_GeExpression114", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right133: BinaryAssociation = BinaryAssociation(
    name="right133",
    ends={
        Property(name="noop_Expression135", type=noop_LShiftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_LShiftExpression134", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left136: BinaryAssociation = BinaryAssociation(
    name="left136",
    ends={
        Property(name="noop_Expression137", type=noop_RShiftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_RShiftExpression", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right138: BinaryAssociation = BinaryAssociation(
    name="right138",
    ends={
        Property(name="noop_Expression140", type=noop_RShiftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_RShiftExpression139", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left141: BinaryAssociation = BinaryAssociation(
    name="left141",
    ends={
        Property(name="noop_Expression142", type=noop_AddExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_AddExpression", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left126: BinaryAssociation = BinaryAssociation(
    name="left126",
    ends={
        Property(name="noop_Expression127", type=noop_InstanceOfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_InstanceOfExpression", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type128: BinaryAssociation = BinaryAssociation(
    name="type128",
    ends={
        Property(name="noop_NoopClass130", type=noop_InstanceOfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_InstanceOfExpression129", type=noop_NoopClass, multiplicity=Multiplicity(0, 1))
    }
)
left131: BinaryAssociation = BinaryAssociation(
    name="left131",
    ends={
        Property(name="noop_Expression132", type=noop_LShiftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_LShiftExpression", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left151: BinaryAssociation = BinaryAssociation(
    name="left151",
    ends={
        Property(name="noop_Expression152", type=noop_MulExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_MulExpression", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right153: BinaryAssociation = BinaryAssociation(
    name="right153",
    ends={
        Property(name="noop_Expression155", type=noop_MulExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_MulExpression154", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left156: BinaryAssociation = BinaryAssociation(
    name="left156",
    ends={
        Property(name="noop_Expression157", type=noop_DivExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_DivExpression", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right158: BinaryAssociation = BinaryAssociation(
    name="right158",
    ends={
        Property(name="noop_Expression160", type=noop_DivExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_DivExpression159", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right143: BinaryAssociation = BinaryAssociation(
    name="right143",
    ends={
        Property(name="noop_Expression145", type=noop_AddExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_AddExpression144", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left146: BinaryAssociation = BinaryAssociation(
    name="left146",
    ends={
        Property(name="noop_Expression147", type=noop_SubExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_SubExpression", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right148: BinaryAssociation = BinaryAssociation(
    name="right148",
    ends={
        Property(name="noop_Expression150", type=noop_SubExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_SubExpression149", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left166: BinaryAssociation = BinaryAssociation(
    name="left166",
    ends={
        Property(name="noop_Expression167", type=noop_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_CastExpression", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type168: BinaryAssociation = BinaryAssociation(
    name="type168",
    ends={
        Property(name="noop_NoopClass170", type=noop_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_CastExpression169", type=noop_NoopClass, multiplicity=Multiplicity(0, 1))
    }
)
dimension171: BinaryAssociation = BinaryAssociation(
    name="dimension171",
    ends={
        Property(name="noop_Index173", type=noop_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_CastExpression172", type=noop_Index, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
right174: BinaryAssociation = BinaryAssociation(
    name="right174",
    ends={
        Property(name="noop_Expression175", type=noop_ComplementExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_ComplementExpression", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right176: BinaryAssociation = BinaryAssociation(
    name="right176",
    ends={
        Property(name="noop_Expression177", type=noop_NotExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_NotExpression", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left161: BinaryAssociation = BinaryAssociation(
    name="left161",
    ends={
        Property(name="noop_Expression162", type=noop_ModExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_ModExpression", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right163: BinaryAssociation = BinaryAssociation(
    name="right163",
    ends={
        Property(name="noop_Expression165", type=noop_ModExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_ModExpression164", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right180: BinaryAssociation = BinaryAssociation(
    name="right180",
    ends={
        Property(name="noop_SigPosExpression", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="noop_Expression181", type=noop_SigPosExpression, multiplicity=Multiplicity(1, 1))
    }
)
right182: BinaryAssociation = BinaryAssociation(
    name="right182",
    ends={
        Property(name="noop_Expression183", type=noop_DecExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_DecExpression", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right184: BinaryAssociation = BinaryAssociation(
    name="right184",
    ends={
        Property(name="noop_Expression185", type=noop_IncExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_IncExpression", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
receiver186: BinaryAssociation = BinaryAssociation(
    name="receiver186",
    ends={
        Property(name="noop_Expression187", type=noop_MemberSelect, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_MemberSelect", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right178: BinaryAssociation = BinaryAssociation(
    name="right178",
    ends={
        Property(name="noop_Expression179", type=noop_SigNegExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_SigNegExpression", type=noop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
indexes194: BinaryAssociation = BinaryAssociation(
    name="indexes194",
    ends={
        Property(name="noop_Index196", type=noop_MemberSelect, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_MemberSelect195", type=noop_Index, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values197: BinaryAssociation = BinaryAssociation(
    name="values197",
    ends={
        Property(name="noop_Expression198", type=noop_ArrayLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_ArrayLiteral", type=noop_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
member188: BinaryAssociation = BinaryAssociation(
    name="member188",
    ends={
        Property(name="noop_Member190", type=noop_MemberSelect, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_MemberSelect189", type=noop_Member, multiplicity=Multiplicity(0, 1))
    }
)
args191: BinaryAssociation = BinaryAssociation(
    name="args191",
    ends={
        Property(name="noop_Expression193", type=noop_MemberSelect, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_MemberSelect192", type=noop_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dimension204: BinaryAssociation = BinaryAssociation(
    name="dimension204",
    ends={
        Property(name="noop_NewInstance205", type=noop_Index, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="noop_Index206", type=noop_NewInstance, multiplicity=Multiplicity(1, 1))
    }
)
member207: BinaryAssociation = BinaryAssociation(
    name="member207",
    ends={
        Property(name="noop_Member208", type=noop_MemberRef, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_MemberRef", type=noop_Member, multiplicity=Multiplicity(0, 1))
    }
)
args209: BinaryAssociation = BinaryAssociation(
    name="args209",
    ends={
        Property(name="noop_Expression211", type=noop_MemberRef, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_MemberRef210", type=noop_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
indexes212: BinaryAssociation = BinaryAssociation(
    name="indexes212",
    ends={
        Property(name="noop_Index214", type=noop_MemberRef, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_MemberRef213", type=noop_Index, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type199: BinaryAssociation = BinaryAssociation(
    name="type199",
    ends={
        Property(name="noop_NoopClass200", type=noop_NewInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_NewInstance", type=noop_NoopClass, multiplicity=Multiplicity(0, 1))
    }
)
constructor201: BinaryAssociation = BinaryAssociation(
    name="constructor201",
    ends={
        Property(name="noop_Constructor203", type=noop_NewInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="noop_NewInstance202", type=noop_Constructor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_noop_Variable_Member = Generalization(general=Member, specific=noop_Variable)
gen_noop_Variable_Statement = Generalization(general=Statement, specific=noop_Variable)
gen_noop_Method_Member = Generalization(general=Member, specific=noop_Method)
gen_noop_ReturnStatement_Statement = Generalization(general=Statement, specific=noop_ReturnStatement)
gen_noop_IfStatement_Statement = Generalization(general=Statement, specific=noop_IfStatement)
gen_noop_ForStatement_Statement = Generalization(general=Statement, specific=noop_ForStatement)
gen_noop_ForeverStatement_Statement = Generalization(general=Statement, specific=noop_ForeverStatement)
gen_noop_ContinueStatement_Statement = Generalization(general=Statement, specific=noop_ContinueStatement)
gen_noop_BreakStatement_Statement = Generalization(general=Statement, specific=noop_BreakStatement)
gen_noop_AsmStatement_Statement = Generalization(general=Statement, specific=noop_AsmStatement)
gen_noop_Expression_Statement = Generalization(general=Statement, specific=noop_Expression)
gen_noop_BOrExpression_Expression = Generalization(general=Expression, specific=noop_BOrExpression)
gen_noop_AssignmentExpression_Expression = Generalization(general=Expression, specific=noop_AssignmentExpression)
gen_noop_BXorExpression_Expression = Generalization(general=Expression, specific=noop_BXorExpression)
gen_noop_OrExpression_Expression = Generalization(general=Expression, specific=noop_OrExpression)
gen_noop_AndExpression_Expression = Generalization(general=Expression, specific=noop_AndExpression)
gen_noop_DifferExpression_Expression = Generalization(general=Expression, specific=noop_DifferExpression)
gen_noop_GtExpression_Expression = Generalization(general=Expression, specific=noop_GtExpression)
gen_noop_BAndExpression_Expression = Generalization(general=Expression, specific=noop_BAndExpression)
gen_noop_EqualsExpression_Expression = Generalization(general=Expression, specific=noop_EqualsExpression)
gen_noop_LtExpression_Expression = Generalization(general=Expression, specific=noop_LtExpression)
gen_noop_LeExpression_Expression = Generalization(general=Expression, specific=noop_LeExpression)
gen_noop_GeExpression_Expression = Generalization(general=Expression, specific=noop_GeExpression)
gen_noop_RShiftExpression_Expression = Generalization(general=Expression, specific=noop_RShiftExpression)
gen_noop_AddExpression_Expression = Generalization(general=Expression, specific=noop_AddExpression)
gen_noop_InstanceOfExpression_Expression = Generalization(general=Expression, specific=noop_InstanceOfExpression)
gen_noop_LShiftExpression_Expression = Generalization(general=Expression, specific=noop_LShiftExpression)
gen_noop_MulExpression_Expression = Generalization(general=Expression, specific=noop_MulExpression)
gen_noop_DivExpression_Expression = Generalization(general=Expression, specific=noop_DivExpression)
gen_noop_SubExpression_Expression = Generalization(general=Expression, specific=noop_SubExpression)
gen_noop_CastExpression_Expression = Generalization(general=Expression, specific=noop_CastExpression)
gen_noop_ComplementExpression_Expression = Generalization(general=Expression, specific=noop_ComplementExpression)
gen_noop_NotExpression_Expression = Generalization(general=Expression, specific=noop_NotExpression)
gen_noop_ModExpression_Expression = Generalization(general=Expression, specific=noop_ModExpression)
gen_noop_DecExpression_Expression = Generalization(general=Expression, specific=noop_DecExpression)
gen_noop_IncExpression_Expression = Generalization(general=Expression, specific=noop_IncExpression)
gen_noop_MemberSelect_Expression = Generalization(general=Expression, specific=noop_MemberSelect)
gen_noop_SigNegExpression_Expression = Generalization(general=Expression, specific=noop_SigNegExpression)
gen_noop_SigPosExpression_Expression = Generalization(general=Expression, specific=noop_SigPosExpression)
gen_noop_ByteLiteral_Expression = Generalization(general=Expression, specific=noop_ByteLiteral)
gen_noop_BoolLiteral_Expression = Generalization(general=Expression, specific=noop_BoolLiteral)
gen_noop_StringLiteral_Expression = Generalization(general=Expression, specific=noop_StringLiteral)
gen_noop_ArrayLiteral_Expression = Generalization(general=Expression, specific=noop_ArrayLiteral)
gen_noop_MemberRef_Expression = Generalization(general=Expression, specific=noop_MemberRef)
gen_noop_This_Expression = Generalization(general=Expression, specific=noop_This)
gen_noop_Super_Expression = Generalization(general=Expression, specific=noop_Super)
gen_noop_NewInstance_Expression = Generalization(general=Expression, specific=noop_NewInstance)

# Domain Model
domain_model = DomainModel(
    name="noop",
    types={noop_NoopClass, noop_Member, noop_Storage, noop_Expression, noop_Variable, Member, Statement, noop_Length, noop_Method, noop_Block, noop_Statement, noop_ReturnStatement, noop_IfStatement, noop_ElseStatement, noop_ForStatement, noop_ForeverStatement, noop_ContinueStatement, noop_BreakStatement, noop_AsmStatement, noop_Constructor, noop_ConstructorField, noop_Index, noop_BOrExpression, noop_AssignmentExpression, Expression, noop_BXorExpression, noop_OrExpression, noop_AndExpression, noop_DifferExpression, noop_GtExpression, noop_BAndExpression, noop_EqualsExpression, noop_LtExpression, noop_LeExpression, noop_InstanceOfExpression, noop_GeExpression, noop_RShiftExpression, noop_AddExpression, noop_LShiftExpression, noop_MulExpression, noop_DivExpression, noop_SubExpression, noop_CastExpression, noop_ComplementExpression, noop_NotExpression, noop_ModExpression, noop_DecExpression, noop_IncExpression, noop_MemberSelect, noop_SigNegExpression, noop_SigPosExpression, noop_ByteLiteral, noop_BoolLiteral, noop_StringLiteral, noop_ArrayLiteral, noop_This, noop_MemberRef, noop_Super, noop_NewInstance, AssignmentType, StorageType},
    associations={superClass1, members2, storage4, value21, location6, value8, type10, dimension13, params15, body17, statements19, condition41, condition23, body25, else28, body30, if33, variables36, assignments38, fields54, expressions44, body47, body50, vars52, variable55, value58, value61, value63, right78, left81, right83, left66, left86, right88, right68, left71, right73, left76, left96, right98, left101, right103, left106, left91, right93, left116, right118, left121, right123, right108, left111, right113, right133, left136, right138, left141, left126, type128, left131, left151, right153, left156, right158, right143, left146, right148, left166, type168, dimension171, right174, right176, left161, right163, right180, right182, right184, receiver186, right178, indexes194, values197, member188, args191, dimension204, member207, args209, indexes212, type199, constructor201},
    generalizations={gen_noop_Variable_Member, gen_noop_Variable_Statement, gen_noop_Method_Member, gen_noop_ReturnStatement_Statement, gen_noop_IfStatement_Statement, gen_noop_ForStatement_Statement, gen_noop_ForeverStatement_Statement, gen_noop_ContinueStatement_Statement, gen_noop_BreakStatement_Statement, gen_noop_AsmStatement_Statement, gen_noop_Expression_Statement, gen_noop_BOrExpression_Expression, gen_noop_AssignmentExpression_Expression, gen_noop_BXorExpression_Expression, gen_noop_OrExpression_Expression, gen_noop_AndExpression_Expression, gen_noop_DifferExpression_Expression, gen_noop_GtExpression_Expression, gen_noop_BAndExpression_Expression, gen_noop_EqualsExpression_Expression, gen_noop_LtExpression_Expression, gen_noop_LeExpression_Expression, gen_noop_GeExpression_Expression, gen_noop_RShiftExpression_Expression, gen_noop_AddExpression_Expression, gen_noop_InstanceOfExpression_Expression, gen_noop_LShiftExpression_Expression, gen_noop_MulExpression_Expression, gen_noop_DivExpression_Expression, gen_noop_SubExpression_Expression, gen_noop_CastExpression_Expression, gen_noop_ComplementExpression_Expression, gen_noop_NotExpression_Expression, gen_noop_ModExpression_Expression, gen_noop_DecExpression_Expression, gen_noop_IncExpression_Expression, gen_noop_MemberSelect_Expression, gen_noop_SigNegExpression_Expression, gen_noop_SigPosExpression_Expression, gen_noop_ByteLiteral_Expression, gen_noop_BoolLiteral_Expression, gen_noop_StringLiteral_Expression, gen_noop_ArrayLiteral_Expression, gen_noop_MemberRef_Expression, gen_noop_This_Expression, gen_noop_Super_Expression, gen_noop_NewInstance_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)