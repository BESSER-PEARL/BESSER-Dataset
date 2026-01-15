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
CVQualifier: Enumeration = Enumeration(
    name="CVQualifier",
    literals={
            EnumerationLiteral(name="const"),
			EnumerationLiteral(name="volatile"),
			EnumerationLiteral(name="unqualified")
    }
)

PrimitiveType: Enumeration = Enumeration(
    name="PrimitiveType",
    literals={
            EnumerationLiteral(name="int8"),
			EnumerationLiteral(name="int16"),
			EnumerationLiteral(name="int32"),
			EnumerationLiteral(name="uint8"),
			EnumerationLiteral(name="uint16"),
			EnumerationLiteral(name="uint32"),
			EnumerationLiteral(name="char"),
			EnumerationLiteral(name="float"),
			EnumerationLiteral(name="double"),
			EnumerationLiteral(name="void"),
			EnumerationLiteral(name="long")
    }
)

LinkageSpec: Enumeration = Enumeration(
    name="LinkageSpec",
    literals={
            EnumerationLiteral(name="unspecified"),
			EnumerationLiteral(name="extern"),
			EnumerationLiteral(name="static")
    }
)

Operator: Enumeration = Enumeration(
    name="Operator",
    literals={
            EnumerationLiteral(name="add"),
			EnumerationLiteral(name="subtract"),
			EnumerationLiteral(name="assign"),
			EnumerationLiteral(name="bitwise_or"),
			EnumerationLiteral(name="bitwise_and"),
			EnumerationLiteral(name="assign_add")
    }
)

Pointer: Enumeration = Enumeration(
    name="Pointer",
    literals={
            EnumerationLiteral(name="pointer"),
			EnumerationLiteral(name="const_pointer"),
			EnumerationLiteral(name="invalid"),
			EnumerationLiteral(name="volatile_pointer"),
			EnumerationLiteral(name="const_volatile_pointer")
    }
)

ElementKind: Enumeration = Enumeration(
    name="ElementKind",
    literals={
            EnumerationLiteral(name="default"),
			EnumerationLiteral(name="headerOnly"),
			EnumerationLiteral(name="implOnly")
    }
)

BooleanOperator: Enumeration = Enumeration(
    name="BooleanOperator",
    literals={
            EnumerationLiteral(name="and"),
			EnumerationLiteral(name="or"),
			EnumerationLiteral(name="less_than"),
			EnumerationLiteral(name="greater_than"),
			EnumerationLiteral(name="less_than_equal"),
			EnumerationLiteral(name="greater_than_equal"),
			EnumerationLiteral(name="equivalent"),
			EnumerationLiteral(name="not_equivalent")
    }
)

# Classes
langc_NamedElement = Class(name="langc::NamedElement", is_abstract=True)
UserElement = Class(name="UserElement")
BindableValue = Class(name="BindableValue")
langc_Name = Class(name="langc::Name")
langc_BuiltInType = Class(name="langc::BuiltInType")
Element = Class(name="Element")
langc_Function = Class(name="langc::Function")
NamedElement = Class(name="NamedElement")
langc_ElementReference = Class(name="langc::ElementReference")
langc_NamedReference = Class(name="langc::NamedReference")
langc_FunctionImplementation = Class(name="langc::FunctionImplementation")
langc_Element = Class(name="langc::Element", is_abstract=True)
langc_Expression = Class(name="langc::Expression")
langc_FunctionCall = Class(name="langc::FunctionCall")
Expression = Class(name="Expression")
langc_ElementAccess = Class(name="langc::ElementAccess")
langc_ElementList = Class(name="langc::ElementList")
langc_UserElement = Class(name="langc::UserElement", is_abstract=True)
langc_Struct = Class(name="langc::Struct")
Structure = Class(name="Structure")
langc_Union = Class(name="langc::Union")
langc_Directive = Class(name="langc::Directive", is_abstract=True)
langc_Literal = Class(name="langc::Literal", is_abstract=True)
langc_IntegralLiteral = Class(name="langc::IntegralLiteral")
Literal = Class(name="Literal")
langc_CharacterLiteral = Class(name="langc::CharacterLiteral")
langc_FloatingLiteral = Class(name="langc::FloatingLiteral")
langc_Statement = Class(name="langc::Statement", is_abstract=True)
langc_ExpressionStatement = Class(name="langc::ExpressionStatement")
Statement = Class(name="Statement")
langc_ReturnStatement = Class(name="langc::ReturnStatement")
ExpressionStatement = Class(name="ExpressionStatement")
langc_CodeBlock = Class(name="langc::CodeBlock")
langc_FileName = Class(name="langc::FileName")
langc_DependencyList = Class(name="langc::DependencyList")
langc_Structure = Class(name="langc::Structure", is_abstract=True)
langc_FunctionPointer = Class(name="langc::FunctionPointer")
langc_FunctionAddress = Class(name="langc::FunctionAddress")
langc_VariableDeclaration = Class(name="langc::VariableDeclaration")
langc_Typedef = Class(name="langc::Typedef")
langc_MemberAccess = Class(name="langc::MemberAccess")
ElementAccess = Class(name="ElementAccess")
langc_BinaryOperation = Class(name="langc::BinaryOperation")
langc_FolderName = Class(name="langc::FolderName")
langc_Enum = Class(name="langc::Enum")
langc_Enumerator = Class(name="langc::Enumerator")
langc_FileDependency = Class(name="langc::FileDependency", is_abstract=True)
Dependency = Class(name="Dependency")
langc_SystemInclude = Class(name="langc::SystemInclude")
FileDependency = Class(name="FileDependency")
langc_UserInclude = Class(name="langc::UserInclude")
Name = Class(name="Name")
langc_CastExpr = Class(name="langc::CastExpr")
langc_Dependency = Class(name="langc::Dependency", is_abstract=True)
langc_ExpressionBlob = Class(name="langc::ExpressionBlob")
langc_SubSystem = Class(name="langc::SubSystem")
langc_SystemFileName = Class(name="langc::SystemFileName")
FileName = Class(name="FileName")
langc_SwitchClause = Class(name="langc::SwitchClause")
CodeBlock = Class(name="CodeBlock")
langc_LabeledClause = Class(name="langc::LabeledClause")
SwitchClause = Class(name="SwitchClause")
langc_SwitchStatement = Class(name="langc::SwitchStatement")
langc_BreakStatement = Class(name="langc::BreakStatement")
langc_AddressOfExpr = Class(name="langc::AddressOfExpr")
langc_DereferenceExpr = Class(name="langc::DereferenceExpr")
langc_WhileStatement = Class(name="langc::WhileStatement")
langc_Macro = Class(name="langc::Macro")
Directive = Class(name="Directive")
langc_StringLiteral = Class(name="langc::StringLiteral")
langc_VariableDeclarationStatement = Class(name="langc::VariableDeclarationStatement")
langc_SizeofType = Class(name="langc::SizeofType")
Sizeof = Class(name="Sizeof")
langc_BindableValue = Class(name="langc::BindableValue", is_abstract=True)
langc_IndexExpr = Class(name="langc::IndexExpr")
langc_LogicalComparison = Class(name="langc::LogicalComparison")
langc_SizeofExpr = Class(name="langc::SizeofExpr")
langc_Sizeof = Class(name="langc::Sizeof", is_abstract=True)
langc_System = Class(name="langc::System")
langc_LinkableArtifact = Class(name="langc::LinkableArtifact")
langc_CodeBlob = Class(name="langc::CodeBlob")
langc_BlockInitializer = Class(name="langc::BlockInitializer")
langc_ConditionalStatement = Class(name="langc::ConditionalStatement")
langc_DependencyBlob = Class(name="langc::DependencyBlob")

# langc_NamedElement class attributes and methods

# UserElement class attributes and methods

# BindableValue class attributes and methods

# langc_Name class attributes and methods
langc_Name_name: Property = Property(name="name", type=StringType)
langc_Name.attributes={langc_Name_name}

# langc_BuiltInType class attributes and methods
langc_BuiltInType_type: Property = Property(name="type", type=StringType)
langc_BuiltInType.attributes={langc_BuiltInType_type}

# Element class attributes and methods

# langc_Function class attributes and methods
langc_Function_linkage: Property = Property(name="linkage", type=StringType)
langc_Function.attributes={langc_Function_linkage}

# NamedElement class attributes and methods

# langc_ElementReference class attributes and methods
langc_ElementReference_cvQualifier: Property = Property(name="cvQualifier", type=StringType)
langc_ElementReference_pointerSpec: Property = Property(name="pointerSpec", type=StringType)
langc_ElementReference.attributes={langc_ElementReference_cvQualifier, langc_ElementReference_pointerSpec}

# langc_NamedReference class attributes and methods

# langc_FunctionImplementation class attributes and methods

# langc_Element class attributes and methods

# langc_Expression class attributes and methods
langc_Expression_precendence: Property = Property(name="precendence", type=IntegerType)
langc_Expression.attributes={langc_Expression_precendence}

# langc_FunctionCall class attributes and methods

# Expression class attributes and methods

# langc_ElementAccess class attributes and methods

# langc_ElementList class attributes and methods

# langc_UserElement class attributes and methods
langc_UserElement_kind: Property = Property(name="kind", type=StringType)
langc_UserElement.attributes={langc_UserElement_kind}

# langc_Struct class attributes and methods

# Structure class attributes and methods

# langc_Union class attributes and methods

# langc_Directive class attributes and methods

# langc_Literal class attributes and methods
langc_Literal_primitiveType: Property = Property(name="primitiveType", type=StringType)
langc_Literal.attributes={langc_Literal_primitiveType}

# langc_IntegralLiteral class attributes and methods
langc_IntegralLiteral_value: Property = Property(name="value", type=StringType)
langc_IntegralLiteral_bytes: Property = Property(name="bytes", type=StringType)
langc_IntegralLiteral_signed: Property = Property(name="signed", type=BooleanType)
langc_IntegralLiteral.attributes={langc_IntegralLiteral_value, langc_IntegralLiteral_signed, langc_IntegralLiteral_bytes}

# Literal class attributes and methods

# langc_CharacterLiteral class attributes and methods
langc_CharacterLiteral_value: Property = Property(name="value", type=StringType)
langc_CharacterLiteral.attributes={langc_CharacterLiteral_value}

# langc_FloatingLiteral class attributes and methods
langc_FloatingLiteral_value: Property = Property(name="value", type=FloatType)
langc_FloatingLiteral.attributes={langc_FloatingLiteral_value}

# langc_Statement class attributes and methods

# langc_ExpressionStatement class attributes and methods

# Statement class attributes and methods

# langc_ReturnStatement class attributes and methods

# ExpressionStatement class attributes and methods

# langc_CodeBlock class attributes and methods
langc_CodeBlock_forceBraces: Property = Property(name="forceBraces", type=BooleanType)
langc_CodeBlock.attributes={langc_CodeBlock_forceBraces}

# langc_FileName class attributes and methods
langc_FileName_hasObjectCode: Property = Property(name="hasObjectCode", type=BooleanType)
langc_FileName.attributes={langc_FileName_hasObjectCode}

# langc_DependencyList class attributes and methods

# langc_Structure class attributes and methods

# langc_FunctionPointer class attributes and methods

# langc_FunctionAddress class attributes and methods

# langc_VariableDeclaration class attributes and methods
langc_VariableDeclaration_linkage: Property = Property(name="linkage", type=StringType)
langc_VariableDeclaration.attributes={langc_VariableDeclaration_linkage}

# langc_Typedef class attributes and methods

# langc_MemberAccess class attributes and methods

# ElementAccess class attributes and methods

# langc_BinaryOperation class attributes and methods
langc_BinaryOperation_operator: Property = Property(name="operator", type=StringType)
langc_BinaryOperation.attributes={langc_BinaryOperation_operator}

# langc_FolderName class attributes and methods
langc_FolderName_api: Property = Property(name="api", type=BooleanType)
langc_FolderName.attributes={langc_FolderName_api}

# langc_Enum class attributes and methods

# langc_Enumerator class attributes and methods

# langc_FileDependency class attributes and methods

# Dependency class attributes and methods

# langc_SystemInclude class attributes and methods

# FileDependency class attributes and methods

# langc_UserInclude class attributes and methods

# Name class attributes and methods

# langc_CastExpr class attributes and methods

# langc_Dependency class attributes and methods

# langc_ExpressionBlob class attributes and methods
langc_ExpressionBlob_text: Property = Property(name="text", type=StringType)
langc_ExpressionBlob.attributes={langc_ExpressionBlob_text}

# langc_SubSystem class attributes and methods
langc_SubSystem_name: Property = Property(name="name", type=StringType)
langc_SubSystem.attributes={langc_SubSystem_name}

# langc_SystemFileName class attributes and methods

# FileName class attributes and methods

# langc_SwitchClause class attributes and methods
langc_SwitchClause_fallthrough: Property = Property(name="fallthrough", type=BooleanType)
langc_SwitchClause.attributes={langc_SwitchClause_fallthrough}

# CodeBlock class attributes and methods

# langc_LabeledClause class attributes and methods

# SwitchClause class attributes and methods

# langc_SwitchStatement class attributes and methods

# langc_BreakStatement class attributes and methods

# langc_AddressOfExpr class attributes and methods

# langc_DereferenceExpr class attributes and methods

# langc_WhileStatement class attributes and methods

# langc_Macro class attributes and methods

# Directive class attributes and methods

# langc_StringLiteral class attributes and methods
langc_StringLiteral_value: Property = Property(name="value", type=StringType)
langc_StringLiteral.attributes={langc_StringLiteral_value}

# langc_VariableDeclarationStatement class attributes and methods

# langc_SizeofType class attributes and methods

# Sizeof class attributes and methods

# langc_BindableValue class attributes and methods

# langc_IndexExpr class attributes and methods

# langc_LogicalComparison class attributes and methods
langc_LogicalComparison_operator: Property = Property(name="operator", type=StringType)
langc_LogicalComparison.attributes={langc_LogicalComparison_operator}

# langc_SizeofExpr class attributes and methods

# langc_Sizeof class attributes and methods

# langc_System class attributes and methods

# langc_LinkableArtifact class attributes and methods
langc_LinkableArtifact_name: Property = Property(name="name", type=StringType)
langc_LinkableArtifact.attributes={langc_LinkableArtifact_name}

# langc_CodeBlob class attributes and methods
langc_CodeBlob_markerComment: Property = Property(name="markerComment", type=StringType)
langc_CodeBlob_text: Property = Property(name="text", type=StringType)
langc_CodeBlob.attributes={langc_CodeBlob_text, langc_CodeBlob_markerComment}

# langc_BlockInitializer class attributes and methods

# langc_ConditionalStatement class attributes and methods

# langc_DependencyBlob class attributes and methods
langc_DependencyBlob_text: Property = Property(name="text", type=StringType)
langc_DependencyBlob_markerComment: Property = Property(name="markerComment", type=StringType)
langc_DependencyBlob.attributes={langc_DependencyBlob_text, langc_DependencyBlob_markerComment}

# Relationships
name0: BinaryAssociation = BinaryAssociation(
    name="name0",
    ends={
        Property(name="langc_Name", type=langc_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_NamedElement", type=langc_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parent2: BinaryAssociation = BinaryAssociation(
    name="parent2",
    ends={
        Property(name="langc_Name3", type=langc_Name, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_Name1", type=langc_Name, multiplicity=Multiplicity(0, 1))
    }
)
returnType4: BinaryAssociation = BinaryAssociation(
    name="returnType4",
    ends={
        Property(name="langc_ElementReference", type=langc_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_Function", type=langc_ElementReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters5: BinaryAssociation = BinaryAssociation(
    name="parameters5",
    ends={
        Property(name="langc_NamedReference", type=langc_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_Function6", type=langc_NamedReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultImpl7: BinaryAssociation = BinaryAssociation(
    name="defaultImpl7",
    ends={
        Property(name="langc_FunctionImplementation", type=langc_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_Function8", type=langc_FunctionImplementation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name9: BinaryAssociation = BinaryAssociation(
    name="name9",
    ends={
        Property(name="langc_Name11", type=langc_NamedReference, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_NamedReference10", type=langc_Name, multiplicity=Multiplicity(1, 1))
    }
)
type12: BinaryAssociation = BinaryAssociation(
    name="type12",
    ends={
        Property(name="langc_ElementReference14", type=langc_NamedReference, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_NamedReference13", type=langc_ElementReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
element15: BinaryAssociation = BinaryAssociation(
    name="element15",
    ends={
        Property(name="langc_Element", type=langc_ElementReference, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_ElementReference16", type=langc_Element, multiplicity=Multiplicity(1, 1))
    }
)
arrayBounds17: BinaryAssociation = BinaryAssociation(
    name="arrayBounds17",
    ends={
        Property(name="langc_Expression", type=langc_ElementReference, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_ElementReference18", type=langc_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type19: BinaryAssociation = BinaryAssociation(
    name="type19",
    ends={
        Property(name="langc_ElementReference21", type=langc_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_Expression20", type=langc_ElementReference, multiplicity=Multiplicity(1, 1))
    }
)
function22: BinaryAssociation = BinaryAssociation(
    name="function22",
    ends={
        Property(name="langc_Function23", type=langc_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_FunctionCall", type=langc_Function, multiplicity=Multiplicity(1, 1))
    }
)
arguments24: BinaryAssociation = BinaryAssociation(
    name="arguments24",
    ends={
        Property(name="langc_Expression26", type=langc_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_FunctionCall25", type=langc_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name27: BinaryAssociation = BinaryAssociation(
    name="name27",
    ends={
        Property(name="langc_Name28", type=langc_ElementAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_ElementAccess", type=langc_Name, multiplicity=Multiplicity(1, 1))
    }
)
elements29: BinaryAssociation = BinaryAssociation(
    name="elements29",
    ends={
        Property(name="langc_UserElement", type=langc_ElementList, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_ElementList", type=langc_UserElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defnIncludes37: BinaryAssociation = BinaryAssociation(
    name="defnIncludes37",
    ends={
        Property(name="langc_DependencyList39", type=langc_ElementList, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_ElementList38", type=langc_DependencyList, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
publicDirectives40: BinaryAssociation = BinaryAssociation(
    name="publicDirectives40",
    ends={
        Property(name="langc_Directive", type=langc_ElementList, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_ElementList41", type=langc_Directive, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
privateDirectives42: BinaryAssociation = BinaryAssociation(
    name="privateDirectives42",
    ends={
        Property(name="langc_Directive44", type=langc_ElementList, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_ElementList43", type=langc_Directive, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr45: BinaryAssociation = BinaryAssociation(
    name="expr45",
    ends={
        Property(name="langc_Expression46", type=langc_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_ExpressionStatement", type=langc_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name30: BinaryAssociation = BinaryAssociation(
    name="name30",
    ends={
        Property(name="langc_FileName", type=langc_ElementList, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_ElementList31", type=langc_FileName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
types32: BinaryAssociation = BinaryAssociation(
    name="types32",
    ends={
        Property(name="langc_Element34", type=langc_ElementList, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_ElementList33", type=langc_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declIncludes35: BinaryAssociation = BinaryAssociation(
    name="declIncludes35",
    ends={
        Property(name="langc_DependencyList", type=langc_ElementList, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_ElementList36", type=langc_DependencyList, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs50: BinaryAssociation = BinaryAssociation(
    name="rhs50",
    ends={
        Property(name="langc_Expression52", type=langc_BinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_BinaryOperation51", type=langc_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
members53: BinaryAssociation = BinaryAssociation(
    name="members53",
    ends={
        Property(name="langc_NamedReference54", type=langc_Structure, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_Structure", type=langc_NamedReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType55: BinaryAssociation = BinaryAssociation(
    name="returnType55",
    ends={
        Property(name="langc_ElementReference56", type=langc_FunctionPointer, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_FunctionPointer", type=langc_ElementReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters57: BinaryAssociation = BinaryAssociation(
    name="parameters57",
    ends={
        Property(name="langc_ElementReference59", type=langc_FunctionPointer, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_FunctionPointer58", type=langc_ElementReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
function60: BinaryAssociation = BinaryAssociation(
    name="function60",
    ends={
        Property(name="langc_Function61", type=langc_FunctionAddress, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_FunctionAddress", type=langc_Function, multiplicity=Multiplicity(1, 1))
    }
)
element62: BinaryAssociation = BinaryAssociation(
    name="element62",
    ends={
        Property(name="langc_ElementReference63", type=langc_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_VariableDeclaration", type=langc_ElementReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initializer64: BinaryAssociation = BinaryAssociation(
    name="initializer64",
    ends={
        Property(name="langc_Expression66", type=langc_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_VariableDeclaration65", type=langc_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
element67: BinaryAssociation = BinaryAssociation(
    name="element67",
    ends={
        Property(name="langc_ElementReference68", type=langc_Typedef, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_Typedef", type=langc_ElementReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
container69: BinaryAssociation = BinaryAssociation(
    name="container69",
    ends={
        Property(name="langc_Expression70", type=langc_MemberAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_MemberAccess", type=langc_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements47: BinaryAssociation = BinaryAssociation(
    name="statements47",
    ends={
        Property(name="langc_Statement", type=langc_CodeBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_CodeBlock", type=langc_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lhs48: BinaryAssociation = BinaryAssociation(
    name="lhs48",
    ends={
        Property(name="langc_Expression49", type=langc_BinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_BinaryOperation", type=langc_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
files71: BinaryAssociation = BinaryAssociation(
    name="files71",
    ends={
        Property(name="langc_ElementList72", type=langc_SubSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_SubSystem", type=langc_ElementList, multiplicity=Multiplicity(0, 9999))
    }
)
folders73: BinaryAssociation = BinaryAssociation(
    name="folders73",
    ends={
        Property(name="langc_FolderName", type=langc_SubSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_SubSystem74", type=langc_FolderName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
publicFolders75: BinaryAssociation = BinaryAssociation(
    name="publicFolders75",
    ends={
        Property(name="langc_FolderName77", type=langc_SubSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_SubSystem76", type=langc_FolderName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumerators78: BinaryAssociation = BinaryAssociation(
    name="enumerators78",
    ends={
        Property(name="langc_Enumerator", type=langc_Enum, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_Enum", type=langc_Enumerator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value79: BinaryAssociation = BinaryAssociation(
    name="value79",
    ends={
        Property(name="langc_IntegralLiteral", type=langc_Enumerator, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_Enumerator80", type=langc_IntegralLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name81: BinaryAssociation = BinaryAssociation(
    name="name81",
    ends={
        Property(name="langc_Name83", type=langc_Enumerator, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_Enumerator82", type=langc_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
filename84: BinaryAssociation = BinaryAssociation(
    name="filename84",
    ends={
        Property(name="langc_FileName85", type=langc_FileDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_FileDependency", type=langc_FileName, multiplicity=Multiplicity(1, 1))
    }
)
targetType86: BinaryAssociation = BinaryAssociation(
    name="targetType86",
    ends={
        Property(name="langc_ElementReference87", type=langc_CastExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_CastExpr", type=langc_ElementReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr88: BinaryAssociation = BinaryAssociation(
    name="expr88",
    ends={
        Property(name="langc_Expression90", type=langc_CastExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_CastExpr89", type=langc_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
defn91: BinaryAssociation = BinaryAssociation(
    name="defn91",
    ends={
        Property(name="langc_FileName93", type=langc_UserElement, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_UserElement92", type=langc_FileName, multiplicity=Multiplicity(0, 1))
    }
)
labels98: BinaryAssociation = BinaryAssociation(
    name="labels98",
    ends={
        Property(name="langc_Expression99", type=langc_LabeledClause, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_LabeledClause", type=langc_Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
clauses100: BinaryAssociation = BinaryAssociation(
    name="clauses100",
    ends={
        Property(name="langc_SwitchClause", type=langc_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_SwitchStatement", type=langc_SwitchClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition101: BinaryAssociation = BinaryAssociation(
    name="condition101",
    ends={
        Property(name="langc_Expression103", type=langc_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_SwitchStatement102", type=langc_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr104: BinaryAssociation = BinaryAssociation(
    name="expr104",
    ends={
        Property(name="langc_Expression105", type=langc_AddressOfExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_AddressOfExpr", type=langc_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr106: BinaryAssociation = BinaryAssociation(
    name="expr106",
    ends={
        Property(name="langc_Expression107", type=langc_DereferenceExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_DereferenceExpr", type=langc_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition108: BinaryAssociation = BinaryAssociation(
    name="condition108",
    ends={
        Property(name="langc_Expression109", type=langc_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_WhileStatement", type=langc_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters110: BinaryAssociation = BinaryAssociation(
    name="parameters110",
    ends={
        Property(name="langc_Name111", type=langc_Macro, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_Macro", type=langc_Name, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
replacement112: BinaryAssociation = BinaryAssociation(
    name="replacement112",
    ends={
        Property(name="langc_Expression114", type=langc_Macro, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_Macro113", type=langc_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name115: BinaryAssociation = BinaryAssociation(
    name="name115",
    ends={
        Property(name="langc_Name117", type=langc_Macro, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_Macro116", type=langc_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dependencies94: BinaryAssociation = BinaryAssociation(
    name="dependencies94",
    ends={
        Property(name="langc_Dependency", type=langc_DependencyList, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_DependencyList95", type=langc_Dependency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element96: BinaryAssociation = BinaryAssociation(
    name="element96",
    ends={
        Property(name="langc_ElementReference97", type=langc_SizeofType, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_SizeofType", type=langc_ElementReference, multiplicity=Multiplicity(1, 1))
    }
)
index122: BinaryAssociation = BinaryAssociation(
    name="index122",
    ends={
        Property(name="langc_Expression123", type=langc_IndexExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_IndexExpr", type=langc_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
array124: BinaryAssociation = BinaryAssociation(
    name="array124",
    ends={
        Property(name="langc_Expression126", type=langc_IndexExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_IndexExpr125", type=langc_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs127: BinaryAssociation = BinaryAssociation(
    name="lhs127",
    ends={
        Property(name="langc_Expression128", type=langc_LogicalComparison, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_LogicalComparison", type=langc_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs129: BinaryAssociation = BinaryAssociation(
    name="rhs129",
    ends={
        Property(name="langc_Expression131", type=langc_LogicalComparison, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_LogicalComparison130", type=langc_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr132: BinaryAssociation = BinaryAssociation(
    name="expr132",
    ends={
        Property(name="langc_Expression133", type=langc_SizeofExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_SizeofExpr", type=langc_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body134: BinaryAssociation = BinaryAssociation(
    name="body134",
    ends={
        Property(name="langc_CodeBlock136", type=langc_FunctionImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_FunctionImplementation135", type=langc_CodeBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
function137: BinaryAssociation = BinaryAssociation(
    name="function137",
    ends={
        Property(name="langc_Function139", type=langc_FunctionImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_FunctionImplementation138", type=langc_Function, multiplicity=Multiplicity(1, 1))
    }
)
subSystems140: BinaryAssociation = BinaryAssociation(
    name="subSystems140",
    ends={
        Property(name="langc_SubSystem141", type=langc_System, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_System", type=langc_SubSystem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
publicFolders142: BinaryAssociation = BinaryAssociation(
    name="publicFolders142",
    ends={
        Property(name="langc_FolderName144", type=langc_System, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_System143", type=langc_FolderName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
artifacts145: BinaryAssociation = BinaryAssociation(
    name="artifacts145",
    ends={
        Property(name="langc_LinkableArtifact", type=langc_System, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_System146", type=langc_LinkableArtifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable118: BinaryAssociation = BinaryAssociation(
    name="variable118",
    ends={
        Property(name="langc_VariableDeclaration119", type=langc_VariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_VariableDeclarationStatement", type=langc_VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exprs120: BinaryAssociation = BinaryAssociation(
    name="exprs120",
    ends={
        Property(name="langc_Expression121", type=langc_BlockInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_BlockInitializer", type=langc_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionImplementations148: BinaryAssociation = BinaryAssociation(
    name="functionImplementations148",
    ends={
        Property(name="langc_FunctionImplementation150", type=langc_LinkableArtifact, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_LinkableArtifact149", type=langc_FunctionImplementation, multiplicity=Multiplicity(0, 9999))
    }
)
rootElements151: BinaryAssociation = BinaryAssociation(
    name="rootElements151",
    ends={
        Property(name="langc_UserElement153", type=langc_LinkableArtifact, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_LinkableArtifact152", type=langc_UserElement, multiplicity=Multiplicity(0, 9999))
    }
)
condition154: BinaryAssociation = BinaryAssociation(
    name="condition154",
    ends={
        Property(name="langc_Expression155", type=langc_ConditionalStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_ConditionalStatement", type=langc_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dependencies147: BinaryAssociation = BinaryAssociation(
    name="dependencies147",
    ends={
        Property(name="langc_DependencyBlob", type=langc_CodeBlob, multiplicity=Multiplicity(1, 1)),
        Property(name="langc_CodeBlob", type=langc_DependencyBlob, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_langc_NamedElement_UserElement = Generalization(general=UserElement, specific=langc_NamedElement)
gen_langc_NamedElement_BindableValue = Generalization(general=BindableValue, specific=langc_NamedElement)
gen_langc_BuiltInType_Element = Generalization(general=Element, specific=langc_BuiltInType)
gen_langc_Function_NamedElement = Generalization(general=NamedElement, specific=langc_Function)
gen_langc_ElementReference_BindableValue = Generalization(general=BindableValue, specific=langc_ElementReference)
gen_langc_FunctionCall_Expression = Generalization(general=Expression, specific=langc_FunctionCall)
gen_langc_ElementAccess_Expression = Generalization(general=Expression, specific=langc_ElementAccess)
gen_langc_Struct_Structure = Generalization(general=Structure, specific=langc_Struct)
gen_langc_Union_Structure = Generalization(general=Structure, specific=langc_Union)
gen_langc_Literal_Expression = Generalization(general=Expression, specific=langc_Literal)
gen_langc_IntegralLiteral_Literal = Generalization(general=Literal, specific=langc_IntegralLiteral)
gen_langc_CharacterLiteral_Literal = Generalization(general=Literal, specific=langc_CharacterLiteral)
gen_langc_FloatingLiteral_Literal = Generalization(general=Literal, specific=langc_FloatingLiteral)
gen_langc_ExpressionStatement_Statement = Generalization(general=Statement, specific=langc_ExpressionStatement)
gen_langc_ReturnStatement_ExpressionStatement = Generalization(general=ExpressionStatement, specific=langc_ReturnStatement)
gen_langc_CodeBlock_Statement = Generalization(general=Statement, specific=langc_CodeBlock)
gen_langc_Structure_NamedElement = Generalization(general=NamedElement, specific=langc_Structure)
gen_langc_FunctionPointer_UserElement = Generalization(general=UserElement, specific=langc_FunctionPointer)
gen_langc_FunctionAddress_Expression = Generalization(general=Expression, specific=langc_FunctionAddress)
gen_langc_VariableDeclaration_NamedElement = Generalization(general=NamedElement, specific=langc_VariableDeclaration)
gen_langc_Typedef_NamedElement = Generalization(general=NamedElement, specific=langc_Typedef)
gen_langc_MemberAccess_ElementAccess = Generalization(general=ElementAccess, specific=langc_MemberAccess)
gen_langc_BinaryOperation_Expression = Generalization(general=Expression, specific=langc_BinaryOperation)
gen_langc_Enum_NamedElement = Generalization(general=NamedElement, specific=langc_Enum)
gen_langc_Enumerator_BindableValue = Generalization(general=BindableValue, specific=langc_Enumerator)
gen_langc_FileDependency_Dependency = Generalization(general=Dependency, specific=langc_FileDependency)
gen_langc_SystemInclude_FileDependency = Generalization(general=FileDependency, specific=langc_SystemInclude)
gen_langc_UserInclude_FileDependency = Generalization(general=FileDependency, specific=langc_UserInclude)
gen_langc_FileName_Name = Generalization(general=Name, specific=langc_FileName)
gen_langc_FolderName_Name = Generalization(general=Name, specific=langc_FolderName)
gen_langc_CastExpr_Expression = Generalization(general=Expression, specific=langc_CastExpr)
gen_langc_UserElement_Element = Generalization(general=Element, specific=langc_UserElement)
gen_langc_ExpressionBlob_Expression = Generalization(general=Expression, specific=langc_ExpressionBlob)
gen_langc_SystemFileName_FileName = Generalization(general=FileName, specific=langc_SystemFileName)
gen_langc_SwitchClause_CodeBlock = Generalization(general=CodeBlock, specific=langc_SwitchClause)
gen_langc_LabeledClause_SwitchClause = Generalization(general=SwitchClause, specific=langc_LabeledClause)
gen_langc_SwitchStatement_Statement = Generalization(general=Statement, specific=langc_SwitchStatement)
gen_langc_BreakStatement_Statement = Generalization(general=Statement, specific=langc_BreakStatement)
gen_langc_AddressOfExpr_Expression = Generalization(general=Expression, specific=langc_AddressOfExpr)
gen_langc_DereferenceExpr_Expression = Generalization(general=Expression, specific=langc_DereferenceExpr)
gen_langc_WhileStatement_CodeBlock = Generalization(general=CodeBlock, specific=langc_WhileStatement)
gen_langc_Macro_Directive = Generalization(general=Directive, specific=langc_Macro)
gen_langc_Macro_BindableValue = Generalization(general=BindableValue, specific=langc_Macro)
gen_langc_StringLiteral_Expression = Generalization(general=Expression, specific=langc_StringLiteral)
gen_langc_VariableDeclarationStatement_Statement = Generalization(general=Statement, specific=langc_VariableDeclarationStatement)
gen_langc_SizeofType_Sizeof = Generalization(general=Sizeof, specific=langc_SizeofType)
gen_langc_IndexExpr_Expression = Generalization(general=Expression, specific=langc_IndexExpr)
gen_langc_LogicalComparison_Expression = Generalization(general=Expression, specific=langc_LogicalComparison)
gen_langc_SizeofExpr_Sizeof = Generalization(general=Sizeof, specific=langc_SizeofExpr)
gen_langc_Sizeof_Expression = Generalization(general=Expression, specific=langc_Sizeof)
gen_langc_FunctionImplementation_UserElement = Generalization(general=UserElement, specific=langc_FunctionImplementation)
gen_langc_CodeBlob_CodeBlock = Generalization(general=CodeBlock, specific=langc_CodeBlob)
gen_langc_BlockInitializer_Expression = Generalization(general=Expression, specific=langc_BlockInitializer)
gen_langc_DependencyBlob_Dependency = Generalization(general=Dependency, specific=langc_DependencyBlob)
gen_langc_ConditionalStatement_CodeBlock = Generalization(general=CodeBlock, specific=langc_ConditionalStatement)

# Domain Model
domain_model = DomainModel(
    name="langc",
    types={langc_NamedElement, UserElement, BindableValue, langc_Name, langc_BuiltInType, Element, langc_Function, NamedElement, langc_ElementReference, langc_NamedReference, langc_FunctionImplementation, langc_Element, langc_Expression, langc_FunctionCall, Expression, langc_ElementAccess, langc_ElementList, langc_UserElement, langc_Struct, Structure, langc_Union, langc_Directive, langc_Literal, langc_IntegralLiteral, Literal, langc_CharacterLiteral, langc_FloatingLiteral, langc_Statement, langc_ExpressionStatement, Statement, langc_ReturnStatement, ExpressionStatement, langc_CodeBlock, langc_FileName, langc_DependencyList, langc_Structure, langc_FunctionPointer, langc_FunctionAddress, langc_VariableDeclaration, langc_Typedef, langc_MemberAccess, ElementAccess, langc_BinaryOperation, langc_FolderName, langc_Enum, langc_Enumerator, langc_FileDependency, Dependency, langc_SystemInclude, FileDependency, langc_UserInclude, Name, langc_CastExpr, langc_Dependency, langc_ExpressionBlob, langc_SubSystem, langc_SystemFileName, FileName, langc_SwitchClause, CodeBlock, langc_LabeledClause, SwitchClause, langc_SwitchStatement, langc_BreakStatement, langc_AddressOfExpr, langc_DereferenceExpr, langc_WhileStatement, langc_Macro, Directive, langc_StringLiteral, langc_VariableDeclarationStatement, langc_SizeofType, Sizeof, langc_BindableValue, langc_IndexExpr, langc_LogicalComparison, langc_SizeofExpr, langc_Sizeof, langc_System, langc_LinkableArtifact, langc_CodeBlob, langc_BlockInitializer, langc_ConditionalStatement, langc_DependencyBlob, CVQualifier, PrimitiveType, LinkageSpec, Operator, Pointer, ElementKind, BooleanOperator},
    associations={name0, parent2, returnType4, parameters5, defaultImpl7, name9, type12, element15, arrayBounds17, type19, function22, arguments24, name27, elements29, defnIncludes37, publicDirectives40, privateDirectives42, expr45, name30, types32, declIncludes35, rhs50, members53, returnType55, parameters57, function60, element62, initializer64, element67, container69, statements47, lhs48, files71, folders73, publicFolders75, enumerators78, value79, name81, filename84, targetType86, expr88, defn91, labels98, clauses100, condition101, expr104, expr106, condition108, parameters110, replacement112, name115, dependencies94, element96, index122, array124, lhs127, rhs129, expr132, body134, function137, subSystems140, publicFolders142, artifacts145, variable118, exprs120, functionImplementations148, rootElements151, condition154, dependencies147},
    generalizations={gen_langc_NamedElement_UserElement, gen_langc_NamedElement_BindableValue, gen_langc_BuiltInType_Element, gen_langc_Function_NamedElement, gen_langc_ElementReference_BindableValue, gen_langc_FunctionCall_Expression, gen_langc_ElementAccess_Expression, gen_langc_Struct_Structure, gen_langc_Union_Structure, gen_langc_Literal_Expression, gen_langc_IntegralLiteral_Literal, gen_langc_CharacterLiteral_Literal, gen_langc_FloatingLiteral_Literal, gen_langc_ExpressionStatement_Statement, gen_langc_ReturnStatement_ExpressionStatement, gen_langc_CodeBlock_Statement, gen_langc_Structure_NamedElement, gen_langc_FunctionPointer_UserElement, gen_langc_FunctionAddress_Expression, gen_langc_VariableDeclaration_NamedElement, gen_langc_Typedef_NamedElement, gen_langc_MemberAccess_ElementAccess, gen_langc_BinaryOperation_Expression, gen_langc_Enum_NamedElement, gen_langc_Enumerator_BindableValue, gen_langc_FileDependency_Dependency, gen_langc_SystemInclude_FileDependency, gen_langc_UserInclude_FileDependency, gen_langc_FileName_Name, gen_langc_FolderName_Name, gen_langc_CastExpr_Expression, gen_langc_UserElement_Element, gen_langc_ExpressionBlob_Expression, gen_langc_SystemFileName_FileName, gen_langc_SwitchClause_CodeBlock, gen_langc_LabeledClause_SwitchClause, gen_langc_SwitchStatement_Statement, gen_langc_BreakStatement_Statement, gen_langc_AddressOfExpr_Expression, gen_langc_DereferenceExpr_Expression, gen_langc_WhileStatement_CodeBlock, gen_langc_Macro_Directive, gen_langc_Macro_BindableValue, gen_langc_StringLiteral_Expression, gen_langc_VariableDeclarationStatement_Statement, gen_langc_SizeofType_Sizeof, gen_langc_IndexExpr_Expression, gen_langc_LogicalComparison_Expression, gen_langc_SizeofExpr_Sizeof, gen_langc_Sizeof_Expression, gen_langc_FunctionImplementation_UserElement, gen_langc_CodeBlob_CodeBlock, gen_langc_BlockInitializer_Expression, gen_langc_DependencyBlob_Dependency, gen_langc_ConditionalStatement_CodeBlock},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)