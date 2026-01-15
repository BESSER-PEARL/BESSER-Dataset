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
AccessLevel: Enumeration = Enumeration(
    name="AccessLevel",
    literals={
            EnumerationLiteral(name="PRIVATE"),
			EnumerationLiteral(name="PROTECTED"),
			EnumerationLiteral(name="PUBLIC")
    }
)

# Classes
miniJava_TypeDeclaration = Class(name="miniJava::TypeDeclaration")
miniJava_State = Class(name="miniJava::State")
miniJava_Program = Class(name="miniJava::Program")
miniJava_Import = Class(name="miniJava::Import")
TypedDeclaration = Class(name="TypedDeclaration")
miniJava_Method = Class(name="miniJava::Method")
Member = Class(name="Member")
miniJava_Parameter = Class(name="miniJava::Parameter")
miniJava_Block = Class(name="miniJava::Block")
Symbol = Class(name="Symbol")
miniJava_Field = Class(name="miniJava::Field")
miniJava_Expression = Class(name="miniJava::Expression")
NamedElement = Class(name="NamedElement")
miniJava_Interface = Class(name="miniJava::Interface")
miniJava_Member = Class(name="miniJava::Member")
miniJava_Class = Class(name="miniJava::Class")
TypeDeclaration = Class(name="TypeDeclaration")
miniJava_PrintStatement = Class(name="miniJava::PrintStatement")
miniJava_Return = Class(name="miniJava::Return")
miniJava_IfStatement = Class(name="miniJava::IfStatement")
miniJava_WhileStatement = Class(name="miniJava::WhileStatement")
Statement = Class(name="Statement")
miniJava_Statement = Class(name="miniJava::Statement")
miniJava_SingleTypeRef = Class(name="miniJava::SingleTypeRef")
TypeRef = Class(name="TypeRef")
miniJava_ClassRef = Class(name="miniJava::ClassRef")
SingleTypeRef = Class(name="SingleTypeRef")
miniJava_NamedElement = Class(name="miniJava::NamedElement")
miniJava_TypedDeclaration = Class(name="miniJava::TypedDeclaration")
miniJava_Symbol = Class(name="miniJava::Symbol")
miniJava_VariableDeclaration = Class(name="miniJava::VariableDeclaration")
Assignee = Class(name="Assignee")
miniJava_Assignee = Class(name="miniJava::Assignee")
miniJava_ForStatement = Class(name="miniJava::ForStatement")
miniJava_Assignment = Class(name="miniJava::Assignment")
miniJava_TypeRef = Class(name="miniJava::TypeRef")
miniJava_IntegerTypeRef = Class(name="miniJava::IntegerTypeRef")
miniJava_BooleanTypeRef = Class(name="miniJava::BooleanTypeRef")
miniJava_StringTypeRef = Class(name="miniJava::StringTypeRef")
miniJava_VoidTypeRef = Class(name="miniJava::VoidTypeRef")
miniJava_Or = Class(name="miniJava::Or")
Expression = Class(name="Expression")
miniJava_And = Class(name="miniJava::And")
miniJava_Equality = Class(name="miniJava::Equality")
miniJava_ArrayTypeRef = Class(name="miniJava::ArrayTypeRef")
miniJava_SuperiorOrEqual = Class(name="miniJava::SuperiorOrEqual")
miniJava_InferiorOrEqual = Class(name="miniJava::InferiorOrEqual")
miniJava_Superior = Class(name="miniJava::Superior")
miniJava_Inferior = Class(name="miniJava::Inferior")
miniJava_Inequality = Class(name="miniJava::Inequality")
miniJava_Multiplication = Class(name="miniJava::Multiplication")
miniJava_Division = Class(name="miniJava::Division")
miniJava_Plus = Class(name="miniJava::Plus")
miniJava_Minus = Class(name="miniJava::Minus")
miniJava_ArrayLength = Class(name="miniJava::ArrayLength")
miniJava_Not = Class(name="miniJava::Not")
miniJava_ArrayAccess = Class(name="miniJava::ArrayAccess")
miniJava_FieldAccess = Class(name="miniJava::FieldAccess")
miniJava_MethodCall = Class(name="miniJava::MethodCall")
miniJava_Neg = Class(name="miniJava::Neg")
miniJava_BoolConstant = Class(name="miniJava::BoolConstant")
miniJava_This = Class(name="miniJava::This")
miniJava_Super = Class(name="miniJava::Super")
miniJava_Null = Class(name="miniJava::Null")
miniJava_NewObject = Class(name="miniJava::NewObject")
miniJava_StringConstant = Class(name="miniJava::StringConstant")
miniJava_IntConstant = Class(name="miniJava::IntConstant")
miniJava_SymbolRef = Class(name="miniJava::SymbolRef")
miniJava_NewArray = Class(name="miniJava::NewArray")
miniJava_SymbolBinding = Class(name="miniJava::SymbolBinding")
miniJava_Context = Class(name="miniJava::Context")
miniJava_IntegerValue = Class(name="miniJava::IntegerValue")
Value = Class(name="Value")
miniJava_Value = Class(name="miniJava::Value")
miniJava_StringValue = Class(name="miniJava::StringValue")
miniJava_BooleanValue = Class(name="miniJava::BooleanValue")
miniJava_FieldBinding = Class(name="miniJava::FieldBinding")
miniJava_OutputStream = Class(name="miniJava::OutputStream")
miniJava_ArrayInstance = Class(name="miniJava::ArrayInstance")
miniJava_Call = Class(name="miniJava::Call")
miniJava_Frame = Class(name="miniJava::Frame")
miniJava_ObjectInstance = Class(name="miniJava::ObjectInstance")
miniJava_NullValue = Class(name="miniJava::NullValue")
miniJava_NewCall = Class(name="miniJava::NewCall")
Call = Class(name="Call")
miniJava_MethodCall2 = Class(name="miniJava::MethodCall2")
miniJava_ArrayRefValue = Class(name="miniJava::ArrayRefValue")
miniJava_ObjectRefValue = Class(name="miniJava::ObjectRefValue")

# miniJava_TypeDeclaration class attributes and methods
miniJava_TypeDeclaration_accessLevel: Property = Property(name="accessLevel", type=StringType)
miniJava_TypeDeclaration.attributes={miniJava_TypeDeclaration_accessLevel}

# miniJava_State class attributes and methods
miniJava_State_m_findCurrentFrame: Method = Method(name="findCurrentFrame", parameters={}, type=StringType)
miniJava_State_m_findCurrentContext: Method = Method(name="findCurrentContext", parameters={}, type=StringType)
miniJava_State_m_println: Method = Method(name="println", parameters={Parameter(name='string')})
miniJava_State_m_pushNewContext: Method = Method(name="pushNewContext", parameters={})
miniJava_State_m_popCurrentContext: Method = Method(name="popCurrentContext", parameters={})
miniJava_State_m_pushNewFrame: Method = Method(name="pushNewFrame", parameters={Parameter(name='newContext'), Parameter(name='c'), Parameter(name='receiver')})
miniJava_State_m_popCurrentFrame: Method = Method(name="popCurrentFrame", parameters={})
miniJava_State.methods={miniJava_State_m_pushNewFrame, miniJava_State_m_println, miniJava_State_m_popCurrentContext, miniJava_State_m_findCurrentFrame, miniJava_State_m_popCurrentFrame, miniJava_State_m_findCurrentContext, miniJava_State_m_pushNewContext}

# miniJava_Program class attributes and methods
miniJava_Program_name: Property = Property(name="name", type=StringType)
miniJava_Program_m_main: Method = Method(name="main", parameters={})
miniJava_Program_m_initialize: Method = Method(name="initialize", parameters={Parameter(name='args')})
miniJava_Program_m_execute: Method = Method(name="execute", parameters={}, type=StringType)
miniJava_Program.attributes={miniJava_Program_name}
miniJava_Program.methods={miniJava_Program_m_main, miniJava_Program_m_initialize, miniJava_Program_m_execute}

# miniJava_Import class attributes and methods
miniJava_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
miniJava_Import.attributes={miniJava_Import_importedNamespace}

# TypedDeclaration class attributes and methods

# miniJava_Method class attributes and methods
miniJava_Method_abstract: Property = Property(name="abstract", type=BooleanType)
miniJava_Method_static: Property = Property(name="static", type=BooleanType)
miniJava_Method_m_call: Method = Method(name="call", parameters={Parameter(name='state')})
miniJava_Method_m_findOverride: Method = Method(name="findOverride", parameters={Parameter(name='c')}, type=StringType)
miniJava_Method.attributes={miniJava_Method_abstract, miniJava_Method_static}
miniJava_Method.methods={miniJava_Method_m_call, miniJava_Method_m_findOverride}

# Member class attributes and methods

# miniJava_Parameter class attributes and methods
miniJava_Parameter_m_compare: Method = Method(name="compare", parameters={Parameter(name='other')})
miniJava_Parameter.methods={miniJava_Parameter_m_compare}

# miniJava_Block class attributes and methods
miniJava_Block_m_evaluateStatementKeepContext: Method = Method(name="evaluateStatementKeepContext", parameters={Parameter(name='state')})
miniJava_Block_m_evaluateStatement: Method = Method(name="evaluateStatement", parameters={Parameter(name='state')})
miniJava_Block.methods={miniJava_Block_m_evaluateStatementKeepContext, miniJava_Block_m_evaluateStatement}

# Symbol class attributes and methods

# miniJava_Field class attributes and methods

# miniJava_Expression class attributes and methods
miniJava_Expression_m_evaluateStatement: Method = Method(name="evaluateStatement", parameters={Parameter(name='state')})
miniJava_Expression_m_evaluateExpression: Method = Method(name="evaluateExpression", parameters={Parameter(name='state')}, type=StringType)
miniJava_Expression.methods={miniJava_Expression_m_evaluateExpression, miniJava_Expression_m_evaluateStatement}

# NamedElement class attributes and methods

# miniJava_Interface class attributes and methods

# miniJava_Member class attributes and methods
miniJava_Member_access: Property = Property(name="access", type=StringType)
miniJava_Member.attributes={miniJava_Member_access}

# miniJava_Class class attributes and methods
miniJava_Class_abstract: Property = Property(name="abstract", type=BooleanType)
miniJava_Class.attributes={miniJava_Class_abstract}

# TypeDeclaration class attributes and methods

# miniJava_PrintStatement class attributes and methods
miniJava_PrintStatement_m_evaluateStatement: Method = Method(name="evaluateStatement", parameters={Parameter(name='state')})
miniJava_PrintStatement.methods={miniJava_PrintStatement_m_evaluateStatement}

# miniJava_Return class attributes and methods
miniJava_Return_m_evaluateStatement: Method = Method(name="evaluateStatement", parameters={Parameter(name='state')})
miniJava_Return.methods={miniJava_Return_m_evaluateStatement}

# miniJava_IfStatement class attributes and methods
miniJava_IfStatement_m_evaluateStatement: Method = Method(name="evaluateStatement", parameters={Parameter(name='state')})
miniJava_IfStatement.methods={miniJava_IfStatement_m_evaluateStatement}

# miniJava_WhileStatement class attributes and methods
miniJava_WhileStatement_m_evaluateStatement: Method = Method(name="evaluateStatement", parameters={Parameter(name='state')})
miniJava_WhileStatement.methods={miniJava_WhileStatement_m_evaluateStatement}

# Statement class attributes and methods

# miniJava_Statement class attributes and methods
miniJava_Statement_m_evaluateStatement: Method = Method(name="evaluateStatement", parameters={Parameter(name='state')})
miniJava_Statement.methods={miniJava_Statement_m_evaluateStatement}

# miniJava_SingleTypeRef class attributes and methods

# TypeRef class attributes and methods

# miniJava_ClassRef class attributes and methods
miniJava_ClassRef_m_compare: Method = Method(name="compare", parameters={Parameter(name='other')})
miniJava_ClassRef.methods={miniJava_ClassRef_m_compare}

# SingleTypeRef class attributes and methods

# miniJava_NamedElement class attributes and methods
miniJava_NamedElement_name: Property = Property(name="name", type=StringType)
miniJava_NamedElement.attributes={miniJava_NamedElement_name}

# miniJava_TypedDeclaration class attributes and methods

# miniJava_Symbol class attributes and methods

# miniJava_VariableDeclaration class attributes and methods

# Assignee class attributes and methods

# miniJava_Assignee class attributes and methods

# miniJava_ForStatement class attributes and methods
miniJava_ForStatement_m_evaluateStatement: Method = Method(name="evaluateStatement", parameters={Parameter(name='state')})
miniJava_ForStatement.methods={miniJava_ForStatement_m_evaluateStatement}

# miniJava_Assignment class attributes and methods
miniJava_Assignment_m_evaluateStatement: Method = Method(name="evaluateStatement", parameters={Parameter(name='state')})
miniJava_Assignment.methods={miniJava_Assignment_m_evaluateStatement}

# miniJava_TypeRef class attributes and methods
miniJava_TypeRef_m_compare: Method = Method(name="compare", parameters={Parameter(name='other')})
miniJava_TypeRef.methods={miniJava_TypeRef_m_compare}

# miniJava_IntegerTypeRef class attributes and methods

# miniJava_BooleanTypeRef class attributes and methods

# miniJava_StringTypeRef class attributes and methods

# miniJava_VoidTypeRef class attributes and methods

# miniJava_Or class attributes and methods
miniJava_Or_m_evaluateExpression: Method = Method(name="evaluateExpression", parameters={Parameter(name='state')}, type=StringType)
miniJava_Or.methods={miniJava_Or_m_evaluateExpression}

# Expression class attributes and methods

# miniJava_And class attributes and methods
miniJava_And_m_evaluateExpression: Method = Method(name="evaluateExpression", parameters={Parameter(name='state')}, type=StringType)
miniJava_And.methods={miniJava_And_m_evaluateExpression}

# miniJava_Equality class attributes and methods
miniJava_Equality_m_evaluateExpression: Method = Method(name="evaluateExpression", parameters={Parameter(name='state')}, type=StringType)
miniJava_Equality.methods={miniJava_Equality_m_evaluateExpression}

# miniJava_ArrayTypeRef class attributes and methods

# miniJava_SuperiorOrEqual class attributes and methods
miniJava_SuperiorOrEqual_m_evaluateExpression: Method = Method(name="evaluateExpression", parameters={Parameter(name='state')}, type=StringType)
miniJava_SuperiorOrEqual.methods={miniJava_SuperiorOrEqual_m_evaluateExpression}

# miniJava_InferiorOrEqual class attributes and methods
miniJava_InferiorOrEqual_m_evaluateExpression: Method = Method(name="evaluateExpression", parameters={Parameter(name='state')}, type=StringType)
miniJava_InferiorOrEqual.methods={miniJava_InferiorOrEqual_m_evaluateExpression}

# miniJava_Superior class attributes and methods
miniJava_Superior_m_evaluateExpression: Method = Method(name="evaluateExpression", parameters={Parameter(name='state')}, type=StringType)
miniJava_Superior.methods={miniJava_Superior_m_evaluateExpression}

# miniJava_Inferior class attributes and methods
miniJava_Inferior_m_evaluateExpression: Method = Method(name="evaluateExpression", parameters={Parameter(name='state')}, type=StringType)
miniJava_Inferior.methods={miniJava_Inferior_m_evaluateExpression}

# miniJava_Inequality class attributes and methods
miniJava_Inequality_m_evaluateExpression: Method = Method(name="evaluateExpression", parameters={Parameter(name='state')}, type=StringType)
miniJava_Inequality.methods={miniJava_Inequality_m_evaluateExpression}

# miniJava_Multiplication class attributes and methods
miniJava_Multiplication_m_evaluateExpression: Method = Method(name="evaluateExpression", parameters={Parameter(name='state')}, type=StringType)
miniJava_Multiplication.methods={miniJava_Multiplication_m_evaluateExpression}

# miniJava_Division class attributes and methods
miniJava_Division_m_evaluateExpression: Method = Method(name="evaluateExpression", parameters={Parameter(name='state')}, type=StringType)
miniJava_Division.methods={miniJava_Division_m_evaluateExpression}

# miniJava_Plus class attributes and methods
miniJava_Plus_m_evaluateExpression: Method = Method(name="evaluateExpression", parameters={Parameter(name='state')}, type=StringType)
miniJava_Plus.methods={miniJava_Plus_m_evaluateExpression}

# miniJava_Minus class attributes and methods
miniJava_Minus_m_evaluateExpression: Method = Method(name="evaluateExpression", parameters={Parameter(name='state')}, type=StringType)
miniJava_Minus.methods={miniJava_Minus_m_evaluateExpression}

# miniJava_ArrayLength class attributes and methods
miniJava_ArrayLength_m_evaluateExpression: Method = Method(name="evaluateExpression", parameters={Parameter(name='state')}, type=StringType)
miniJava_ArrayLength.methods={miniJava_ArrayLength_m_evaluateExpression}

# miniJava_Not class attributes and methods
miniJava_Not_m_evaluateExpression: Method = Method(name="evaluateExpression", parameters={Parameter(name='state')}, type=StringType)
miniJava_Not.methods={miniJava_Not_m_evaluateExpression}

# miniJava_ArrayAccess class attributes and methods
miniJava_ArrayAccess_m_evaluateExpression: Method = Method(name="evaluateExpression", parameters={Parameter(name='state')}, type=StringType)
miniJava_ArrayAccess.methods={miniJava_ArrayAccess_m_evaluateExpression}

# miniJava_FieldAccess class attributes and methods
miniJava_FieldAccess_m_evaluateExpression: Method = Method(name="evaluateExpression", parameters={Parameter(name='state')}, type=StringType)
miniJava_FieldAccess.methods={miniJava_FieldAccess_m_evaluateExpression}

# miniJava_MethodCall class attributes and methods
miniJava_MethodCall_m_evaluateExpression: Method = Method(name="evaluateExpression", parameters={Parameter(name='state')}, type=StringType)
miniJava_MethodCall.methods={miniJava_MethodCall_m_evaluateExpression}

# miniJava_Neg class attributes and methods
miniJava_Neg_m_evaluateExpression: Method = Method(name="evaluateExpression", parameters={Parameter(name='state')}, type=StringType)
miniJava_Neg.methods={miniJava_Neg_m_evaluateExpression}

# miniJava_BoolConstant class attributes and methods
miniJava_BoolConstant_value: Property = Property(name="value", type=StringType)
miniJava_BoolConstant_m_evaluateExpression: Method = Method(name="evaluateExpression", parameters={Parameter(name='state')}, type=StringType)
miniJava_BoolConstant.attributes={miniJava_BoolConstant_value}
miniJava_BoolConstant.methods={miniJava_BoolConstant_m_evaluateExpression}

# miniJava_This class attributes and methods
miniJava_This_m_evaluateExpression: Method = Method(name="evaluateExpression", parameters={Parameter(name='state')}, type=StringType)
miniJava_This.methods={miniJava_This_m_evaluateExpression}

# miniJava_Super class attributes and methods

# miniJava_Null class attributes and methods
miniJava_Null_m_evaluateExpression: Method = Method(name="evaluateExpression", parameters={Parameter(name='state')}, type=StringType)
miniJava_Null.methods={miniJava_Null_m_evaluateExpression}

# miniJava_NewObject class attributes and methods
miniJava_NewObject_m_evaluateExpression: Method = Method(name="evaluateExpression", parameters={Parameter(name='state')}, type=StringType)
miniJava_NewObject.methods={miniJava_NewObject_m_evaluateExpression}

# miniJava_StringConstant class attributes and methods
miniJava_StringConstant_value: Property = Property(name="value", type=StringType)
miniJava_StringConstant_m_evaluateExpression: Method = Method(name="evaluateExpression", parameters={Parameter(name='state')}, type=StringType)
miniJava_StringConstant.attributes={miniJava_StringConstant_value}
miniJava_StringConstant.methods={miniJava_StringConstant_m_evaluateExpression}

# miniJava_IntConstant class attributes and methods
miniJava_IntConstant_value: Property = Property(name="value", type=IntegerType)
miniJava_IntConstant_m_evaluateExpression: Method = Method(name="evaluateExpression", parameters={Parameter(name='state')}, type=StringType)
miniJava_IntConstant.attributes={miniJava_IntConstant_value}
miniJava_IntConstant.methods={miniJava_IntConstant_m_evaluateExpression}

# miniJava_SymbolRef class attributes and methods
miniJava_SymbolRef_m_evaluateExpression: Method = Method(name="evaluateExpression", parameters={Parameter(name='state')}, type=StringType)
miniJava_SymbolRef.methods={miniJava_SymbolRef_m_evaluateExpression}

# miniJava_NewArray class attributes and methods
miniJava_NewArray_m_evaluateExpression: Method = Method(name="evaluateExpression", parameters={Parameter(name='state')}, type=StringType)
miniJava_NewArray.methods={miniJava_NewArray_m_evaluateExpression}

# miniJava_SymbolBinding class attributes and methods

# miniJava_Context class attributes and methods
miniJava_Context_m_createChildContext: Method = Method(name="createChildContext", parameters={}, type=StringType)
miniJava_Context_m_findBinding: Method = Method(name="findBinding", parameters={Parameter(name='symbol')}, type=StringType)
miniJava_Context_m_findCurrentContext: Method = Method(name="findCurrentContext", parameters={}, type=StringType)
miniJava_Context.methods={miniJava_Context_m_createChildContext, miniJava_Context_m_findBinding, miniJava_Context_m_findCurrentContext}

# miniJava_IntegerValue class attributes and methods
miniJava_IntegerValue_value: Property = Property(name="value", type=StringType)
miniJava_IntegerValue_m_copy: Method = Method(name="copy", parameters={}, type=Value)
miniJava_IntegerValue_m_customToString: Method = Method(name="customToString", parameters={})
miniJava_IntegerValue.attributes={miniJava_IntegerValue_value}
miniJava_IntegerValue.methods={miniJava_IntegerValue_m_customToString, miniJava_IntegerValue_m_copy}

# Value class attributes and methods

# miniJava_Value class attributes and methods
miniJava_Value_m_customToString: Method = Method(name="customToString", parameters={})
miniJava_Value_m_copy: Method = Method(name="copy", parameters={}, type=StringType)
miniJava_Value.methods={miniJava_Value_m_copy, miniJava_Value_m_customToString}

# miniJava_StringValue class attributes and methods
miniJava_StringValue_value: Property = Property(name="value", type=StringType)
miniJava_StringValue_m_copy: Method = Method(name="copy", parameters={}, type=Value)
miniJava_StringValue_m_customToString: Method = Method(name="customToString", parameters={})
miniJava_StringValue.attributes={miniJava_StringValue_value}
miniJava_StringValue.methods={miniJava_StringValue_m_copy, miniJava_StringValue_m_customToString}

# miniJava_BooleanValue class attributes and methods
miniJava_BooleanValue_value: Property = Property(name="value", type=BooleanType)
miniJava_BooleanValue_m_customToString: Method = Method(name="customToString", parameters={})
miniJava_BooleanValue_m_copy: Method = Method(name="copy", parameters={}, type=Value)
miniJava_BooleanValue.attributes={miniJava_BooleanValue_value}
miniJava_BooleanValue.methods={miniJava_BooleanValue_m_customToString, miniJava_BooleanValue_m_copy}

# miniJava_FieldBinding class attributes and methods

# miniJava_OutputStream class attributes and methods
miniJava_OutputStream_stream: Property = Property(name="stream", type=StringType)
miniJava_OutputStream.attributes={miniJava_OutputStream_stream}

# miniJava_ArrayInstance class attributes and methods
miniJava_ArrayInstance_size: Property = Property(name="size", type=StringType)
miniJava_ArrayInstance.attributes={miniJava_ArrayInstance_size}

# miniJava_Call class attributes and methods

# miniJava_Frame class attributes and methods
miniJava_Frame_m_findCurrentFrame: Method = Method(name="findCurrentFrame", parameters={}, type=StringType)
miniJava_Frame_m_findCurrentContext: Method = Method(name="findCurrentContext", parameters={}, type=StringType)
miniJava_Frame.methods={miniJava_Frame_m_findCurrentContext, miniJava_Frame_m_findCurrentFrame}

# miniJava_ObjectInstance class attributes and methods

# miniJava_NullValue class attributes and methods
miniJava_NullValue_m_copy: Method = Method(name="copy", parameters={}, type=Value)
miniJava_NullValue.methods={miniJava_NullValue_m_copy}

# miniJava_NewCall class attributes and methods

# Call class attributes and methods

# miniJava_MethodCall2 class attributes and methods

# miniJava_ArrayRefValue class attributes and methods
miniJava_ArrayRefValue_m_copy: Method = Method(name="copy", parameters={}, type=Value)
miniJava_ArrayRefValue.methods={miniJava_ArrayRefValue_m_copy}

# miniJava_ObjectRefValue class attributes and methods
miniJava_ObjectRefValue_m_copy: Method = Method(name="copy", parameters={}, type=Value)
miniJava_ObjectRefValue_m_customToString: Method = Method(name="customToString", parameters={})
miniJava_ObjectRefValue.methods={miniJava_ObjectRefValue_m_customToString, miniJava_ObjectRefValue_m_copy}

# Relationships
classes1: BinaryAssociation = BinaryAssociation(
    name="classes1",
    ends={
        Property(name="miniJava_TypeDeclaration", type=miniJava_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Program2", type=miniJava_TypeDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state3: BinaryAssociation = BinaryAssociation(
    name="state3",
    ends={
        Property(name="miniJava_State", type=miniJava_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Program4", type=miniJava_State, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="miniJava_Import", type=miniJava_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Program", type=miniJava_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass10: BinaryAssociation = BinaryAssociation(
    name="superClass10",
    ends={
        Property(name="miniJava_Class", type=miniJava_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Class9", type=miniJava_Class, multiplicity=Multiplicity(0, 1))
    }
)
params11: BinaryAssociation = BinaryAssociation(
    name="params11",
    ends={
        Property(name="miniJava_Parameter", type=miniJava_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Method", type=miniJava_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body12: BinaryAssociation = BinaryAssociation(
    name="body12",
    ends={
        Property(name="miniJava_Block", type=miniJava_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Method13", type=miniJava_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultValue14: BinaryAssociation = BinaryAssociation(
    name="defaultValue14",
    ends={
        Property(name="miniJava_Expression", type=miniJava_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Field", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
implements5: BinaryAssociation = BinaryAssociation(
    name="implements5",
    ends={
        Property(name="miniJava_Interface", type=miniJava_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_TypeDeclaration6", type=miniJava_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
members7: BinaryAssociation = BinaryAssociation(
    name="members7",
    ends={
        Property(name="miniJava_Member", type=miniJava_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_TypeDeclaration8", type=miniJava_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression17: BinaryAssociation = BinaryAssociation(
    name="expression17",
    ends={
        Property(name="miniJava_Expression18", type=miniJava_PrintStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_PrintStatement", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression19: BinaryAssociation = BinaryAssociation(
    name="expression19",
    ends={
        Property(name="miniJava_Expression20", type=miniJava_Return, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Return", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression21: BinaryAssociation = BinaryAssociation(
    name="expression21",
    ends={
        Property(name="miniJava_Expression22", type=miniJava_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_IfStatement", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenBlock23: BinaryAssociation = BinaryAssociation(
    name="thenBlock23",
    ends={
        Property(name="miniJava_Block25", type=miniJava_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_IfStatement24", type=miniJava_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseBlock26: BinaryAssociation = BinaryAssociation(
    name="elseBlock26",
    ends={
        Property(name="miniJava_Block28", type=miniJava_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_IfStatement27", type=miniJava_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition29: BinaryAssociation = BinaryAssociation(
    name="condition29",
    ends={
        Property(name="miniJava_Expression30", type=miniJava_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_WhileStatement", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block31: BinaryAssociation = BinaryAssociation(
    name="block31",
    ends={
        Property(name="miniJava_Block33", type=miniJava_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_WhileStatement32", type=miniJava_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements15: BinaryAssociation = BinaryAssociation(
    name="statements15",
    ends={
        Property(name="miniJava_Statement", type=miniJava_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Block16", type=miniJava_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencedClass44: BinaryAssociation = BinaryAssociation(
    name="referencedClass44",
    ends={
        Property(name="miniJava_TypeDeclaration45", type=miniJava_ClassRef, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ClassRef", type=miniJava_TypeDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
typeRef46: BinaryAssociation = BinaryAssociation(
    name="typeRef46",
    ends={
        Property(name="miniJava_TypeRef", type=miniJava_TypedDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_TypedDeclaration", type=miniJava_TypeRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignee47: BinaryAssociation = BinaryAssociation(
    name="assignee47",
    ends={
        Property(name="miniJava_Assignee", type=miniJava_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Assignment48", type=miniJava_Assignee, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration34: BinaryAssociation = BinaryAssociation(
    name="declaration34",
    ends={
        Property(name="miniJava_Assignment", type=miniJava_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ForStatement", type=miniJava_Assignment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition35: BinaryAssociation = BinaryAssociation(
    name="condition35",
    ends={
        Property(name="miniJava_Expression37", type=miniJava_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ForStatement36", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
progression38: BinaryAssociation = BinaryAssociation(
    name="progression38",
    ends={
        Property(name="miniJava_Assignment40", type=miniJava_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ForStatement39", type=miniJava_Assignment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block41: BinaryAssociation = BinaryAssociation(
    name="block41",
    ends={
        Property(name="miniJava_Block43", type=miniJava_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ForStatement42", type=miniJava_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeRef52: BinaryAssociation = BinaryAssociation(
    name="typeRef52",
    ends={
        Property(name="miniJava_SingleTypeRef", type=miniJava_ArrayTypeRef, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ArrayTypeRef", type=miniJava_SingleTypeRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left53: BinaryAssociation = BinaryAssociation(
    name="left53",
    ends={
        Property(name="miniJava_Expression54", type=miniJava_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Or", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right55: BinaryAssociation = BinaryAssociation(
    name="right55",
    ends={
        Property(name="miniJava_Expression57", type=miniJava_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Or56", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left58: BinaryAssociation = BinaryAssociation(
    name="left58",
    ends={
        Property(name="miniJava_Expression59", type=miniJava_And, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_And", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right60: BinaryAssociation = BinaryAssociation(
    name="right60",
    ends={
        Property(name="miniJava_Expression62", type=miniJava_And, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_And61", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value49: BinaryAssociation = BinaryAssociation(
    name="value49",
    ends={
        Property(name="miniJava_Expression51", type=miniJava_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Assignment50", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left73: BinaryAssociation = BinaryAssociation(
    name="left73",
    ends={
        Property(name="miniJava_Expression74", type=miniJava_SuperiorOrEqual, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_SuperiorOrEqual", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right75: BinaryAssociation = BinaryAssociation(
    name="right75",
    ends={
        Property(name="miniJava_Expression77", type=miniJava_SuperiorOrEqual, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_SuperiorOrEqual76", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left78: BinaryAssociation = BinaryAssociation(
    name="left78",
    ends={
        Property(name="miniJava_Expression79", type=miniJava_InferiorOrEqual, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_InferiorOrEqual", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right80: BinaryAssociation = BinaryAssociation(
    name="right80",
    ends={
        Property(name="miniJava_Expression82", type=miniJava_InferiorOrEqual, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_InferiorOrEqual81", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left83: BinaryAssociation = BinaryAssociation(
    name="left83",
    ends={
        Property(name="miniJava_Expression84", type=miniJava_Superior, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Superior", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right85: BinaryAssociation = BinaryAssociation(
    name="right85",
    ends={
        Property(name="miniJava_Expression87", type=miniJava_Superior, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Superior86", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left63: BinaryAssociation = BinaryAssociation(
    name="left63",
    ends={
        Property(name="miniJava_Expression64", type=miniJava_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Equality", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right65: BinaryAssociation = BinaryAssociation(
    name="right65",
    ends={
        Property(name="miniJava_Expression67", type=miniJava_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Equality66", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left68: BinaryAssociation = BinaryAssociation(
    name="left68",
    ends={
        Property(name="miniJava_Expression69", type=miniJava_Inequality, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Inequality", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right70: BinaryAssociation = BinaryAssociation(
    name="right70",
    ends={
        Property(name="miniJava_Expression72", type=miniJava_Inequality, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Inequality71", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left98: BinaryAssociation = BinaryAssociation(
    name="left98",
    ends={
        Property(name="miniJava_Expression99", type=miniJava_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Minus", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right100: BinaryAssociation = BinaryAssociation(
    name="right100",
    ends={
        Property(name="miniJava_Expression102", type=miniJava_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Minus101", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left103: BinaryAssociation = BinaryAssociation(
    name="left103",
    ends={
        Property(name="miniJava_Expression104", type=miniJava_Multiplication, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Multiplication", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right105: BinaryAssociation = BinaryAssociation(
    name="right105",
    ends={
        Property(name="miniJava_Expression107", type=miniJava_Multiplication, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Multiplication106", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left108: BinaryAssociation = BinaryAssociation(
    name="left108",
    ends={
        Property(name="miniJava_Expression109", type=miniJava_Division, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Division", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left88: BinaryAssociation = BinaryAssociation(
    name="left88",
    ends={
        Property(name="miniJava_Expression89", type=miniJava_Inferior, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Inferior", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right90: BinaryAssociation = BinaryAssociation(
    name="right90",
    ends={
        Property(name="miniJava_Expression92", type=miniJava_Inferior, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Inferior91", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left93: BinaryAssociation = BinaryAssociation(
    name="left93",
    ends={
        Property(name="miniJava_Expression94", type=miniJava_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Plus", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right95: BinaryAssociation = BinaryAssociation(
    name="right95",
    ends={
        Property(name="miniJava_Expression97", type=miniJava_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Plus96", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object113: BinaryAssociation = BinaryAssociation(
    name="object113",
    ends={
        Property(name="miniJava_Expression114", type=miniJava_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ArrayAccess", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
index115: BinaryAssociation = BinaryAssociation(
    name="index115",
    ends={
        Property(name="miniJava_Expression117", type=miniJava_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ArrayAccess116", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
array118: BinaryAssociation = BinaryAssociation(
    name="array118",
    ends={
        Property(name="miniJava_Expression119", type=miniJava_ArrayLength, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ArrayLength", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression120: BinaryAssociation = BinaryAssociation(
    name="expression120",
    ends={
        Property(name="miniJava_Expression121", type=miniJava_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Not", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right110: BinaryAssociation = BinaryAssociation(
    name="right110",
    ends={
        Property(name="miniJava_Expression112", type=miniJava_Division, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Division111", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
receiver124: BinaryAssociation = BinaryAssociation(
    name="receiver124",
    ends={
        Property(name="miniJava_Expression125", type=miniJava_FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_FieldAccess", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
field126: BinaryAssociation = BinaryAssociation(
    name="field126",
    ends={
        Property(name="miniJava_Field128", type=miniJava_FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_FieldAccess127", type=miniJava_Field, multiplicity=Multiplicity(0, 1))
    }
)
receiver129: BinaryAssociation = BinaryAssociation(
    name="receiver129",
    ends={
        Property(name="miniJava_Expression130", type=miniJava_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_MethodCall", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
method131: BinaryAssociation = BinaryAssociation(
    name="method131",
    ends={
        Property(name="miniJava_Method133", type=miniJava_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_MethodCall132", type=miniJava_Method, multiplicity=Multiplicity(0, 1))
    }
)
args134: BinaryAssociation = BinaryAssociation(
    name="args134",
    ends={
        Property(name="miniJava_Expression136", type=miniJava_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_MethodCall135", type=miniJava_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression122: BinaryAssociation = BinaryAssociation(
    name="expression122",
    ends={
        Property(name="miniJava_Expression123", type=miniJava_Neg, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Neg", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type137: BinaryAssociation = BinaryAssociation(
    name="type137",
    ends={
        Property(name="miniJava_Class138", type=miniJava_NewObject, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_NewObject", type=miniJava_Class, multiplicity=Multiplicity(0, 1))
    }
)
type142: BinaryAssociation = BinaryAssociation(
    name="type142",
    ends={
        Property(name="miniJava_TypeRef143", type=miniJava_NewArray, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_NewArray", type=miniJava_TypeRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
size144: BinaryAssociation = BinaryAssociation(
    name="size144",
    ends={
        Property(name="miniJava_Expression146", type=miniJava_NewArray, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_NewArray145", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args139: BinaryAssociation = BinaryAssociation(
    name="args139",
    ends={
        Property(name="miniJava_Expression141", type=miniJava_NewObject, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_NewObject140", type=miniJava_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindings148: BinaryAssociation = BinaryAssociation(
    name="bindings148",
    ends={
        Property(name="miniJava_SymbolBinding", type=miniJava_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Context", type=miniJava_SymbolBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentContext150: BinaryAssociation = BinaryAssociation(
    name="parentContext150",
    ends={
        Property(name="151", type=miniJava_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=miniJava_Context, multiplicity=Multiplicity(0, 1))
    }
)
childContext153: BinaryAssociation = BinaryAssociation(
    name="childContext153",
    ends={
        Property(name="155", type=miniJava_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="154", type=miniJava_Context, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
symbol147: BinaryAssociation = BinaryAssociation(
    name="symbol147",
    ends={
        Property(name="miniJava_Symbol", type=miniJava_SymbolRef, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_SymbolRef", type=miniJava_Symbol, multiplicity=Multiplicity(0, 1))
    }
)
value156: BinaryAssociation = BinaryAssociation(
    name="value156",
    ends={
        Property(name="miniJava_Value", type=miniJava_SymbolBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_SymbolBinding157", type=miniJava_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
symbol158: BinaryAssociation = BinaryAssociation(
    name="symbol158",
    ends={
        Property(name="miniJava_Symbol160", type=miniJava_SymbolBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_SymbolBinding159", type=miniJava_Symbol, multiplicity=Multiplicity(1, 1))
    }
)
value163: BinaryAssociation = BinaryAssociation(
    name="value163",
    ends={
        Property(name="miniJava_Value165", type=miniJava_FieldBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_FieldBinding164", type=miniJava_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
field161: BinaryAssociation = BinaryAssociation(
    name="field161",
    ends={
        Property(name="miniJava_Field162", type=miniJava_FieldBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_FieldBinding", type=miniJava_Field, multiplicity=Multiplicity(1, 1))
    }
)
outputStream170: BinaryAssociation = BinaryAssociation(
    name="outputStream170",
    ends={
        Property(name="miniJava_OutputStream", type=miniJava_State, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_State171", type=miniJava_OutputStream, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arraysHeap172: BinaryAssociation = BinaryAssociation(
    name="arraysHeap172",
    ends={
        Property(name="miniJava_ArrayInstance", type=miniJava_State, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_State173", type=miniJava_ArrayInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
call174: BinaryAssociation = BinaryAssociation(
    name="call174",
    ends={
        Property(name="miniJava_Call", type=miniJava_Frame, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Frame175", type=miniJava_Call, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
instance176: BinaryAssociation = BinaryAssociation(
    name="instance176",
    ends={
        Property(name="miniJava_ObjectInstance178", type=miniJava_Frame, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Frame177", type=miniJava_ObjectInstance, multiplicity=Multiplicity(0, 1))
    }
)
childFrame180: BinaryAssociation = BinaryAssociation(
    name="childFrame180",
    ends={
        Property(name="182", type=miniJava_Frame, multiplicity=Multiplicity(1, 1)),
        Property(name="181", type=miniJava_Frame, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parentFrame184: BinaryAssociation = BinaryAssociation(
    name="parentFrame184",
    ends={
        Property(name="186", type=miniJava_Frame, multiplicity=Multiplicity(1, 1)),
        Property(name="185", type=miniJava_Frame, multiplicity=Multiplicity(0, 1))
    }
)
rootFrame166: BinaryAssociation = BinaryAssociation(
    name="rootFrame166",
    ends={
        Property(name="miniJava_Frame", type=miniJava_State, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_State167", type=miniJava_Frame, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
objectsHeap168: BinaryAssociation = BinaryAssociation(
    name="objectsHeap168",
    ends={
        Property(name="miniJava_ObjectInstance", type=miniJava_State, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_State169", type=miniJava_ObjectInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
new193: BinaryAssociation = BinaryAssociation(
    name="new193",
    ends={
        Property(name="miniJava_NewObject194", type=miniJava_NewCall, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_NewCall", type=miniJava_NewObject, multiplicity=Multiplicity(1, 1))
    }
)
methodcall195: BinaryAssociation = BinaryAssociation(
    name="methodcall195",
    ends={
        Property(name="miniJava_MethodCall196", type=miniJava_MethodCall2, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_MethodCall2", type=miniJava_MethodCall, multiplicity=Multiplicity(1, 1))
    }
)
fieldbindings197: BinaryAssociation = BinaryAssociation(
    name="fieldbindings197",
    ends={
        Property(name="miniJava_FieldBinding199", type=miniJava_ObjectInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ObjectInstance198", type=miniJava_FieldBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type200: BinaryAssociation = BinaryAssociation(
    name="type200",
    ends={
        Property(name="miniJava_Class202", type=miniJava_ObjectInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ObjectInstance201", type=miniJava_Class, multiplicity=Multiplicity(1, 1))
    }
)
rootContext187: BinaryAssociation = BinaryAssociation(
    name="rootContext187",
    ends={
        Property(name="miniJava_Context189", type=miniJava_Frame, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Frame188", type=miniJava_Context, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnValue190: BinaryAssociation = BinaryAssociation(
    name="returnValue190",
    ends={
        Property(name="miniJava_Value192", type=miniJava_Frame, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Frame191", type=miniJava_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
instance206: BinaryAssociation = BinaryAssociation(
    name="instance206",
    ends={
        Property(name="miniJava_ObjectInstance207", type=miniJava_ObjectRefValue, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ObjectRefValue", type=miniJava_ObjectInstance, multiplicity=Multiplicity(0, 1))
    }
)
instance208: BinaryAssociation = BinaryAssociation(
    name="instance208",
    ends={
        Property(name="miniJava_ArrayInstance209", type=miniJava_ArrayRefValue, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ArrayRefValue", type=miniJava_ArrayInstance, multiplicity=Multiplicity(0, 1))
    }
)
value203: BinaryAssociation = BinaryAssociation(
    name="value203",
    ends={
        Property(name="miniJava_Value205", type=miniJava_ArrayInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ArrayInstance204", type=miniJava_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_miniJava_Interface_TypeDeclaration = Generalization(general=TypeDeclaration, specific=miniJava_Interface)
gen_miniJava_Member_TypedDeclaration = Generalization(general=TypedDeclaration, specific=miniJava_Member)
gen_miniJava_Method_Member = Generalization(general=Member, specific=miniJava_Method)
gen_miniJava_Parameter_Symbol = Generalization(general=Symbol, specific=miniJava_Parameter)
gen_miniJava_Field_Member = Generalization(general=Member, specific=miniJava_Field)
gen_miniJava_TypeDeclaration_NamedElement = Generalization(general=NamedElement, specific=miniJava_TypeDeclaration)
gen_miniJava_Class_TypeDeclaration = Generalization(general=TypeDeclaration, specific=miniJava_Class)
gen_miniJava_PrintStatement_Statement = Generalization(general=Statement, specific=miniJava_PrintStatement)
gen_miniJava_Return_Statement = Generalization(general=Statement, specific=miniJava_Return)
gen_miniJava_IfStatement_Statement = Generalization(general=Statement, specific=miniJava_IfStatement)
gen_miniJava_WhileStatement_Statement = Generalization(general=Statement, specific=miniJava_WhileStatement)
gen_miniJava_Block_Statement = Generalization(general=Statement, specific=miniJava_Block)
gen_miniJava_SingleTypeRef_TypeRef = Generalization(general=TypeRef, specific=miniJava_SingleTypeRef)
gen_miniJava_ClassRef_SingleTypeRef = Generalization(general=SingleTypeRef, specific=miniJava_ClassRef)
gen_miniJava_TypedDeclaration_NamedElement = Generalization(general=NamedElement, specific=miniJava_TypedDeclaration)
gen_miniJava_Symbol_TypedDeclaration = Generalization(general=TypedDeclaration, specific=miniJava_Symbol)
gen_miniJava_VariableDeclaration_Symbol = Generalization(general=Symbol, specific=miniJava_VariableDeclaration)
gen_miniJava_VariableDeclaration_Assignee = Generalization(general=Assignee, specific=miniJava_VariableDeclaration)
gen_miniJava_Assignment_Statement = Generalization(general=Statement, specific=miniJava_Assignment)
gen_miniJava_ForStatement_Statement = Generalization(general=Statement, specific=miniJava_ForStatement)
gen_miniJava_IntegerTypeRef_SingleTypeRef = Generalization(general=SingleTypeRef, specific=miniJava_IntegerTypeRef)
gen_miniJava_BooleanTypeRef_SingleTypeRef = Generalization(general=SingleTypeRef, specific=miniJava_BooleanTypeRef)
gen_miniJava_StringTypeRef_SingleTypeRef = Generalization(general=SingleTypeRef, specific=miniJava_StringTypeRef)
gen_miniJava_VoidTypeRef_SingleTypeRef = Generalization(general=SingleTypeRef, specific=miniJava_VoidTypeRef)
gen_miniJava_Or_Expression = Generalization(general=Expression, specific=miniJava_Or)
gen_miniJava_And_Expression = Generalization(general=Expression, specific=miniJava_And)
gen_miniJava_Equality_Expression = Generalization(general=Expression, specific=miniJava_Equality)
gen_miniJava_Expression_Statement = Generalization(general=Statement, specific=miniJava_Expression)
gen_miniJava_Expression_Assignee = Generalization(general=Assignee, specific=miniJava_Expression)
gen_miniJava_ArrayTypeRef_TypeRef = Generalization(general=TypeRef, specific=miniJava_ArrayTypeRef)
gen_miniJava_SuperiorOrEqual_Expression = Generalization(general=Expression, specific=miniJava_SuperiorOrEqual)
gen_miniJava_InferiorOrEqual_Expression = Generalization(general=Expression, specific=miniJava_InferiorOrEqual)
gen_miniJava_Superior_Expression = Generalization(general=Expression, specific=miniJava_Superior)
gen_miniJava_Inferior_Expression = Generalization(general=Expression, specific=miniJava_Inferior)
gen_miniJava_Inequality_Expression = Generalization(general=Expression, specific=miniJava_Inequality)
gen_miniJava_Multiplication_Expression = Generalization(general=Expression, specific=miniJava_Multiplication)
gen_miniJava_Division_Expression = Generalization(general=Expression, specific=miniJava_Division)
gen_miniJava_Plus_Expression = Generalization(general=Expression, specific=miniJava_Plus)
gen_miniJava_Minus_Expression = Generalization(general=Expression, specific=miniJava_Minus)
gen_miniJava_ArrayLength_Expression = Generalization(general=Expression, specific=miniJava_ArrayLength)
gen_miniJava_Not_Expression = Generalization(general=Expression, specific=miniJava_Not)
gen_miniJava_ArrayAccess_Expression = Generalization(general=Expression, specific=miniJava_ArrayAccess)
gen_miniJava_FieldAccess_Expression = Generalization(general=Expression, specific=miniJava_FieldAccess)
gen_miniJava_MethodCall_Expression = Generalization(general=Expression, specific=miniJava_MethodCall)
gen_miniJava_Neg_Expression = Generalization(general=Expression, specific=miniJava_Neg)
gen_miniJava_BoolConstant_Expression = Generalization(general=Expression, specific=miniJava_BoolConstant)
gen_miniJava_This_Expression = Generalization(general=Expression, specific=miniJava_This)
gen_miniJava_Super_Expression = Generalization(general=Expression, specific=miniJava_Super)
gen_miniJava_Null_Expression = Generalization(general=Expression, specific=miniJava_Null)
gen_miniJava_NewObject_Expression = Generalization(general=Expression, specific=miniJava_NewObject)
gen_miniJava_StringConstant_Expression = Generalization(general=Expression, specific=miniJava_StringConstant)
gen_miniJava_IntConstant_Expression = Generalization(general=Expression, specific=miniJava_IntConstant)
gen_miniJava_SymbolRef_Expression = Generalization(general=Expression, specific=miniJava_SymbolRef)
gen_miniJava_NewArray_Expression = Generalization(general=Expression, specific=miniJava_NewArray)
gen_miniJava_IntegerValue_Value = Generalization(general=Value, specific=miniJava_IntegerValue)
gen_miniJava_StringValue_Value = Generalization(general=Value, specific=miniJava_StringValue)
gen_miniJava_BooleanValue_Value = Generalization(general=Value, specific=miniJava_BooleanValue)
gen_miniJava_NullValue_Value = Generalization(general=Value, specific=miniJava_NullValue)
gen_miniJava_NewCall_Call = Generalization(general=Call, specific=miniJava_NewCall)
gen_miniJava_MethodCall2_Call = Generalization(general=Call, specific=miniJava_MethodCall2)
gen_miniJava_ArrayRefValue_Value = Generalization(general=Value, specific=miniJava_ArrayRefValue)
gen_miniJava_ObjectRefValue_Value = Generalization(general=Value, specific=miniJava_ObjectRefValue)

# Domain Model
domain_model = DomainModel(
    name="miniJava",
    types={miniJava_TypeDeclaration, miniJava_State, miniJava_Program, miniJava_Import, TypedDeclaration, miniJava_Method, Member, miniJava_Parameter, miniJava_Block, Symbol, miniJava_Field, miniJava_Expression, NamedElement, miniJava_Interface, miniJava_Member, miniJava_Class, TypeDeclaration, miniJava_PrintStatement, miniJava_Return, miniJava_IfStatement, miniJava_WhileStatement, Statement, miniJava_Statement, miniJava_SingleTypeRef, TypeRef, miniJava_ClassRef, SingleTypeRef, miniJava_NamedElement, miniJava_TypedDeclaration, miniJava_Symbol, miniJava_VariableDeclaration, Assignee, miniJava_Assignee, miniJava_ForStatement, miniJava_Assignment, miniJava_TypeRef, miniJava_IntegerTypeRef, miniJava_BooleanTypeRef, miniJava_StringTypeRef, miniJava_VoidTypeRef, miniJava_Or, Expression, miniJava_And, miniJava_Equality, miniJava_ArrayTypeRef, miniJava_SuperiorOrEqual, miniJava_InferiorOrEqual, miniJava_Superior, miniJava_Inferior, miniJava_Inequality, miniJava_Multiplication, miniJava_Division, miniJava_Plus, miniJava_Minus, miniJava_ArrayLength, miniJava_Not, miniJava_ArrayAccess, miniJava_FieldAccess, miniJava_MethodCall, miniJava_Neg, miniJava_BoolConstant, miniJava_This, miniJava_Super, miniJava_Null, miniJava_NewObject, miniJava_StringConstant, miniJava_IntConstant, miniJava_SymbolRef, miniJava_NewArray, miniJava_SymbolBinding, miniJava_Context, miniJava_IntegerValue, Value, miniJava_Value, miniJava_StringValue, miniJava_BooleanValue, miniJava_FieldBinding, miniJava_OutputStream, miniJava_ArrayInstance, miniJava_Call, miniJava_Frame, miniJava_ObjectInstance, miniJava_NullValue, miniJava_NewCall, Call, miniJava_MethodCall2, miniJava_ArrayRefValue, miniJava_ObjectRefValue, AccessLevel},
    associations={classes1, state3, imports0, superClass10, params11, body12, defaultValue14, implements5, members7, expression17, expression19, expression21, thenBlock23, elseBlock26, condition29, block31, statements15, referencedClass44, typeRef46, assignee47, declaration34, condition35, progression38, block41, typeRef52, left53, right55, left58, right60, value49, left73, right75, left78, right80, left83, right85, left63, right65, left68, right70, left98, right100, left103, right105, left108, left88, right90, left93, right95, object113, index115, array118, expression120, right110, receiver124, field126, receiver129, method131, args134, expression122, type137, type142, size144, args139, bindings148, parentContext150, childContext153, symbol147, value156, symbol158, value163, field161, outputStream170, arraysHeap172, call174, instance176, childFrame180, parentFrame184, rootFrame166, objectsHeap168, new193, methodcall195, fieldbindings197, type200, rootContext187, returnValue190, instance206, instance208, value203},
    generalizations={gen_miniJava_Interface_TypeDeclaration, gen_miniJava_Member_TypedDeclaration, gen_miniJava_Method_Member, gen_miniJava_Parameter_Symbol, gen_miniJava_Field_Member, gen_miniJava_TypeDeclaration_NamedElement, gen_miniJava_Class_TypeDeclaration, gen_miniJava_PrintStatement_Statement, gen_miniJava_Return_Statement, gen_miniJava_IfStatement_Statement, gen_miniJava_WhileStatement_Statement, gen_miniJava_Block_Statement, gen_miniJava_SingleTypeRef_TypeRef, gen_miniJava_ClassRef_SingleTypeRef, gen_miniJava_TypedDeclaration_NamedElement, gen_miniJava_Symbol_TypedDeclaration, gen_miniJava_VariableDeclaration_Symbol, gen_miniJava_VariableDeclaration_Assignee, gen_miniJava_Assignment_Statement, gen_miniJava_ForStatement_Statement, gen_miniJava_IntegerTypeRef_SingleTypeRef, gen_miniJava_BooleanTypeRef_SingleTypeRef, gen_miniJava_StringTypeRef_SingleTypeRef, gen_miniJava_VoidTypeRef_SingleTypeRef, gen_miniJava_Or_Expression, gen_miniJava_And_Expression, gen_miniJava_Equality_Expression, gen_miniJava_Expression_Statement, gen_miniJava_Expression_Assignee, gen_miniJava_ArrayTypeRef_TypeRef, gen_miniJava_SuperiorOrEqual_Expression, gen_miniJava_InferiorOrEqual_Expression, gen_miniJava_Superior_Expression, gen_miniJava_Inferior_Expression, gen_miniJava_Inequality_Expression, gen_miniJava_Multiplication_Expression, gen_miniJava_Division_Expression, gen_miniJava_Plus_Expression, gen_miniJava_Minus_Expression, gen_miniJava_ArrayLength_Expression, gen_miniJava_Not_Expression, gen_miniJava_ArrayAccess_Expression, gen_miniJava_FieldAccess_Expression, gen_miniJava_MethodCall_Expression, gen_miniJava_Neg_Expression, gen_miniJava_BoolConstant_Expression, gen_miniJava_This_Expression, gen_miniJava_Super_Expression, gen_miniJava_Null_Expression, gen_miniJava_NewObject_Expression, gen_miniJava_StringConstant_Expression, gen_miniJava_IntConstant_Expression, gen_miniJava_SymbolRef_Expression, gen_miniJava_NewArray_Expression, gen_miniJava_IntegerValue_Value, gen_miniJava_StringValue_Value, gen_miniJava_BooleanValue_Value, gen_miniJava_NullValue_Value, gen_miniJava_NewCall_Call, gen_miniJava_MethodCall2_Call, gen_miniJava_ArrayRefValue_Value, gen_miniJava_ObjectRefValue_Value},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)