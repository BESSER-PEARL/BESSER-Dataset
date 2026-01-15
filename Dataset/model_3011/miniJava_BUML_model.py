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
miniJava_Program = Class(name="miniJava::Program")
miniJava_Import = Class(name="miniJava::Import")
miniJava_TypeDeclaration = Class(name="miniJava::TypeDeclaration")
miniJava_State = Class(name="miniJava::State")
NamedElement = Class(name="NamedElement")
miniJava_Interface = Class(name="miniJava::Interface")
miniJava_Member = Class(name="miniJava::Member")
miniJava_Clazz = Class(name="miniJava::Clazz")
TypeDeclaration = Class(name="TypeDeclaration")
TypedDeclaration = Class(name="TypedDeclaration")
miniJava_Field = Class(name="miniJava::Field")
miniJava_Expression = Class(name="miniJava::Expression")
Statement = Class(name="Statement")
miniJava_Statement = Class(name="miniJava::Statement")
miniJava_PrintStatement = Class(name="miniJava::PrintStatement")
miniJava_Return = Class(name="miniJava::Return")
miniJava_IfStatement = Class(name="miniJava::IfStatement")
miniJava_WhileStatement = Class(name="miniJava::WhileStatement")
miniJava_ForStatement = Class(name="miniJava::ForStatement")
miniJava_Assignment = Class(name="miniJava::Assignment")
miniJava_Method = Class(name="miniJava::Method")
Member = Class(name="Member")
miniJava_Parameter = Class(name="miniJava::Parameter")
miniJava_Block = Class(name="miniJava::Block")
miniJava_ClazzToMethodMap = Class(name="miniJava::ClazzToMethodMap")
Symbol = Class(name="Symbol")
miniJava_NamedElement = Class(name="miniJava::NamedElement")
miniJava_TypedDeclaration = Class(name="miniJava::TypedDeclaration")
miniJava_Symbol = Class(name="miniJava::Symbol")
miniJava_VariableDeclaration = Class(name="miniJava::VariableDeclaration")
Assignee = Class(name="Assignee")
miniJava_Assignee = Class(name="miniJava::Assignee")
miniJava_ArrayTypeRef = Class(name="miniJava::ArrayTypeRef")
miniJava_IntegerTypeRef = Class(name="miniJava::IntegerTypeRef")
miniJava_BooleanTypeRef = Class(name="miniJava::BooleanTypeRef")
miniJava_StringTypeRef = Class(name="miniJava::StringTypeRef")
miniJava_VoidTypeRef = Class(name="miniJava::VoidTypeRef")
miniJava_Or = Class(name="miniJava::Or")
Expression = Class(name="Expression")
miniJava_And = Class(name="miniJava::And")
miniJava_TypeRef = Class(name="miniJava::TypeRef")
miniJava_SingleTypeRef = Class(name="miniJava::SingleTypeRef")
TypeRef = Class(name="TypeRef")
miniJava_ClassRef = Class(name="miniJava::ClassRef")
SingleTypeRef = Class(name="SingleTypeRef")
miniJava_SuperiorOrEqual = Class(name="miniJava::SuperiorOrEqual")
miniJava_InferiorOrEqual = Class(name="miniJava::InferiorOrEqual")
miniJava_Superior = Class(name="miniJava::Superior")
miniJava_Inferior = Class(name="miniJava::Inferior")
miniJava_Equality = Class(name="miniJava::Equality")
miniJava_Inequality = Class(name="miniJava::Inequality")
miniJava_Plus = Class(name="miniJava::Plus")
miniJava_Minus = Class(name="miniJava::Minus")
miniJava_Multiplication = Class(name="miniJava::Multiplication")
miniJava_Division = Class(name="miniJava::Division")
miniJava_Not = Class(name="miniJava::Not")
miniJava_Neg = Class(name="miniJava::Neg")
miniJava_FieldAccess = Class(name="miniJava::FieldAccess")
miniJava_MethodCall = Class(name="miniJava::MethodCall")
miniJava_StringConstant = Class(name="miniJava::StringConstant")
miniJava_IntConstant = Class(name="miniJava::IntConstant")
miniJava_BoolConstant = Class(name="miniJava::BoolConstant")
miniJava_This = Class(name="miniJava::This")
miniJava_ArrayAccess = Class(name="miniJava::ArrayAccess")
miniJava_ArrayLength = Class(name="miniJava::ArrayLength")
miniJava_SymbolRef = Class(name="miniJava::SymbolRef")
miniJava_Context = Class(name="miniJava::Context")
miniJava_SymbolBinding = Class(name="miniJava::SymbolBinding")
miniJava_SymbolToSymbolBindingMap = Class(name="miniJava::SymbolToSymbolBindingMap")
miniJava_Value = Class(name="miniJava::Value")
miniJava_IntegerValue = Class(name="miniJava::IntegerValue")
Value = Class(name="Value")
miniJava_FieldBinding = Class(name="miniJava::FieldBinding")
miniJava_StringValue = Class(name="miniJava::StringValue")
miniJava_Super = Class(name="miniJava::Super")
miniJava_Null = Class(name="miniJava::Null")
miniJava_NewObject = Class(name="miniJava::NewObject")
miniJava_NewArray = Class(name="miniJava::NewArray")
miniJava_BooleanValue = Class(name="miniJava::BooleanValue")
miniJava_OutputStream = Class(name="miniJava::OutputStream")
miniJava_Frame = Class(name="miniJava::Frame")
miniJava_ObjectInstance = Class(name="miniJava::ObjectInstance")
miniJava_ArrayInstance = Class(name="miniJava::ArrayInstance")
miniJava_Call = Class(name="miniJava::Call", is_abstract=True)
miniJava_NullValue = Class(name="miniJava::NullValue")
miniJava_NewCall = Class(name="miniJava::NewCall")
Call = Class(name="Call")
miniJava_MethodCall2 = Class(name="miniJava::MethodCall2")
miniJava_ObjectRefValue = Class(name="miniJava::ObjectRefValue")
miniJava_ArrayRefValue = Class(name="miniJava::ArrayRefValue")
miniJava_Modulo = Class(name="miniJava::Modulo")

# miniJava_Program class attributes and methods
miniJava_Program_name: Property = Property(name="name", type=StringType)
miniJava_Program.attributes={miniJava_Program_name}

# miniJava_Import class attributes and methods
miniJava_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
miniJava_Import.attributes={miniJava_Import_importedNamespace}

# miniJava_TypeDeclaration class attributes and methods
miniJava_TypeDeclaration_accessLevel: Property = Property(name="accessLevel", type=StringType)
miniJava_TypeDeclaration.attributes={miniJava_TypeDeclaration_accessLevel}

# miniJava_State class attributes and methods

# NamedElement class attributes and methods

# miniJava_Interface class attributes and methods

# miniJava_Member class attributes and methods
miniJava_Member_access: Property = Property(name="access", type=StringType)
miniJava_Member.attributes={miniJava_Member_access}

# miniJava_Clazz class attributes and methods
miniJava_Clazz_isabstract: Property = Property(name="isabstract", type=BooleanType)
miniJava_Clazz.attributes={miniJava_Clazz_isabstract}

# TypeDeclaration class attributes and methods

# TypedDeclaration class attributes and methods

# miniJava_Field class attributes and methods

# miniJava_Expression class attributes and methods

# Statement class attributes and methods

# miniJava_Statement class attributes and methods

# miniJava_PrintStatement class attributes and methods

# miniJava_Return class attributes and methods

# miniJava_IfStatement class attributes and methods

# miniJava_WhileStatement class attributes and methods

# miniJava_ForStatement class attributes and methods

# miniJava_Assignment class attributes and methods

# miniJava_Method class attributes and methods
miniJava_Method_isabstract: Property = Property(name="isabstract", type=BooleanType)
miniJava_Method_isstatic: Property = Property(name="isstatic", type=BooleanType)
miniJava_Method.attributes={miniJava_Method_isstatic, miniJava_Method_isabstract}

# Member class attributes and methods

# miniJava_Parameter class attributes and methods

# miniJava_Block class attributes and methods

# miniJava_ClazzToMethodMap class attributes and methods

# Symbol class attributes and methods

# miniJava_NamedElement class attributes and methods
miniJava_NamedElement_name: Property = Property(name="name", type=StringType)
miniJava_NamedElement.attributes={miniJava_NamedElement_name}

# miniJava_TypedDeclaration class attributes and methods

# miniJava_Symbol class attributes and methods

# miniJava_VariableDeclaration class attributes and methods

# Assignee class attributes and methods

# miniJava_Assignee class attributes and methods

# miniJava_ArrayTypeRef class attributes and methods

# miniJava_IntegerTypeRef class attributes and methods

# miniJava_BooleanTypeRef class attributes and methods

# miniJava_StringTypeRef class attributes and methods

# miniJava_VoidTypeRef class attributes and methods

# miniJava_Or class attributes and methods

# Expression class attributes and methods

# miniJava_And class attributes and methods

# miniJava_TypeRef class attributes and methods

# miniJava_SingleTypeRef class attributes and methods

# TypeRef class attributes and methods

# miniJava_ClassRef class attributes and methods

# SingleTypeRef class attributes and methods

# miniJava_SuperiorOrEqual class attributes and methods

# miniJava_InferiorOrEqual class attributes and methods

# miniJava_Superior class attributes and methods

# miniJava_Inferior class attributes and methods

# miniJava_Equality class attributes and methods

# miniJava_Inequality class attributes and methods

# miniJava_Plus class attributes and methods

# miniJava_Minus class attributes and methods

# miniJava_Multiplication class attributes and methods

# miniJava_Division class attributes and methods

# miniJava_Not class attributes and methods

# miniJava_Neg class attributes and methods

# miniJava_FieldAccess class attributes and methods

# miniJava_MethodCall class attributes and methods

# miniJava_StringConstant class attributes and methods
miniJava_StringConstant_value: Property = Property(name="value", type=StringType)
miniJava_StringConstant.attributes={miniJava_StringConstant_value}

# miniJava_IntConstant class attributes and methods
miniJava_IntConstant_value: Property = Property(name="value", type=IntegerType)
miniJava_IntConstant.attributes={miniJava_IntConstant_value}

# miniJava_BoolConstant class attributes and methods
miniJava_BoolConstant_value: Property = Property(name="value", type=StringType)
miniJava_BoolConstant.attributes={miniJava_BoolConstant_value}

# miniJava_This class attributes and methods

# miniJava_ArrayAccess class attributes and methods

# miniJava_ArrayLength class attributes and methods

# miniJava_SymbolRef class attributes and methods

# miniJava_Context class attributes and methods

# miniJava_SymbolBinding class attributes and methods

# miniJava_SymbolToSymbolBindingMap class attributes and methods

# miniJava_Value class attributes and methods

# miniJava_IntegerValue class attributes and methods
miniJava_IntegerValue_value: Property = Property(name="value", type=IntegerType)
miniJava_IntegerValue.attributes={miniJava_IntegerValue_value}

# Value class attributes and methods

# miniJava_FieldBinding class attributes and methods

# miniJava_StringValue class attributes and methods
miniJava_StringValue_value: Property = Property(name="value", type=StringType)
miniJava_StringValue.attributes={miniJava_StringValue_value}

# miniJava_Super class attributes and methods

# miniJava_Null class attributes and methods

# miniJava_NewObject class attributes and methods

# miniJava_NewArray class attributes and methods

# miniJava_BooleanValue class attributes and methods
miniJava_BooleanValue_value: Property = Property(name="value", type=BooleanType)
miniJava_BooleanValue.attributes={miniJava_BooleanValue_value}

# miniJava_OutputStream class attributes and methods
miniJava_OutputStream_stream: Property = Property(name="stream", type=StringType)
miniJava_OutputStream.attributes={miniJava_OutputStream_stream}

# miniJava_Frame class attributes and methods

# miniJava_ObjectInstance class attributes and methods

# miniJava_ArrayInstance class attributes and methods
miniJava_ArrayInstance_size: Property = Property(name="size", type=IntegerType)
miniJava_ArrayInstance.attributes={miniJava_ArrayInstance_size}

# miniJava_Call class attributes and methods

# miniJava_NullValue class attributes and methods

# miniJava_NewCall class attributes and methods

# Call class attributes and methods

# miniJava_MethodCall2 class attributes and methods

# miniJava_ObjectRefValue class attributes and methods

# miniJava_ArrayRefValue class attributes and methods

# miniJava_Modulo class attributes and methods

# Relationships
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="miniJava_Import", type=miniJava_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Program", type=miniJava_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
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
        Property(name="miniJava_Program4", type=miniJava_State, multiplicity=Multiplicity(0, 1))
    }
)
implementz5: BinaryAssociation = BinaryAssociation(
    name="implementz5",
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
superClass10: BinaryAssociation = BinaryAssociation(
    name="superClass10",
    ends={
        Property(name="miniJava_Clazz", type=miniJava_Clazz, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Clazz9", type=miniJava_Clazz, multiplicity=Multiplicity(0, 1))
    }
)
defaultValue16: BinaryAssociation = BinaryAssociation(
    name="defaultValue16",
    ends={
        Property(name="miniJava_Expression", type=miniJava_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Field", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements17: BinaryAssociation = BinaryAssociation(
    name="statements17",
    ends={
        Property(name="miniJava_Statement", type=miniJava_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Block18", type=miniJava_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression19: BinaryAssociation = BinaryAssociation(
    name="expression19",
    ends={
        Property(name="miniJava_Expression20", type=miniJava_PrintStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_PrintStatement", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression21: BinaryAssociation = BinaryAssociation(
    name="expression21",
    ends={
        Property(name="miniJava_Expression22", type=miniJava_Return, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Return", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression23: BinaryAssociation = BinaryAssociation(
    name="expression23",
    ends={
        Property(name="miniJava_Expression24", type=miniJava_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_IfStatement", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenBlock25: BinaryAssociation = BinaryAssociation(
    name="thenBlock25",
    ends={
        Property(name="miniJava_Block27", type=miniJava_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_IfStatement26", type=miniJava_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseBlock28: BinaryAssociation = BinaryAssociation(
    name="elseBlock28",
    ends={
        Property(name="miniJava_Block30", type=miniJava_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_IfStatement29", type=miniJava_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition31: BinaryAssociation = BinaryAssociation(
    name="condition31",
    ends={
        Property(name="miniJava_Expression32", type=miniJava_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_WhileStatement", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block33: BinaryAssociation = BinaryAssociation(
    name="block33",
    ends={
        Property(name="miniJava_Block35", type=miniJava_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_WhileStatement34", type=miniJava_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration36: BinaryAssociation = BinaryAssociation(
    name="declaration36",
    ends={
        Property(name="miniJava_Assignment", type=miniJava_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ForStatement", type=miniJava_Assignment, multiplicity=Multiplicity(0, 1), is_composite=True)
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
cache14: BinaryAssociation = BinaryAssociation(
    name="cache14",
    ends={
        Property(name="miniJava_ClazzToMethodMap", type=miniJava_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Method15", type=miniJava_ClazzToMethodMap, multiplicity=Multiplicity(0, 9999))
    }
)
typeRef48: BinaryAssociation = BinaryAssociation(
    name="typeRef48",
    ends={
        Property(name="miniJava_TypeRef", type=miniJava_TypedDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_TypedDeclaration", type=miniJava_TypeRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignee49: BinaryAssociation = BinaryAssociation(
    name="assignee49",
    ends={
        Property(name="miniJava_Assignee", type=miniJava_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Assignment50", type=miniJava_Assignee, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value51: BinaryAssociation = BinaryAssociation(
    name="value51",
    ends={
        Property(name="miniJava_Expression53", type=miniJava_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Assignment52", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeRef54: BinaryAssociation = BinaryAssociation(
    name="typeRef54",
    ends={
        Property(name="miniJava_SingleTypeRef", type=miniJava_ArrayTypeRef, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ArrayTypeRef", type=miniJava_SingleTypeRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left55: BinaryAssociation = BinaryAssociation(
    name="left55",
    ends={
        Property(name="miniJava_Expression56", type=miniJava_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Or", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right57: BinaryAssociation = BinaryAssociation(
    name="right57",
    ends={
        Property(name="miniJava_Expression59", type=miniJava_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Or58", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left60: BinaryAssociation = BinaryAssociation(
    name="left60",
    ends={
        Property(name="miniJava_Expression61", type=miniJava_And, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_And", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition37: BinaryAssociation = BinaryAssociation(
    name="condition37",
    ends={
        Property(name="miniJava_Expression39", type=miniJava_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ForStatement38", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
progression40: BinaryAssociation = BinaryAssociation(
    name="progression40",
    ends={
        Property(name="miniJava_Assignment42", type=miniJava_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ForStatement41", type=miniJava_Assignment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block43: BinaryAssociation = BinaryAssociation(
    name="block43",
    ends={
        Property(name="miniJava_Block45", type=miniJava_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ForStatement44", type=miniJava_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referencedClass46: BinaryAssociation = BinaryAssociation(
    name="referencedClass46",
    ends={
        Property(name="miniJava_TypeDeclaration47", type=miniJava_ClassRef, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ClassRef", type=miniJava_TypeDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
right72: BinaryAssociation = BinaryAssociation(
    name="right72",
    ends={
        Property(name="miniJava_Expression74", type=miniJava_Inequality, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Inequality73", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left75: BinaryAssociation = BinaryAssociation(
    name="left75",
    ends={
        Property(name="miniJava_Expression76", type=miniJava_SuperiorOrEqual, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_SuperiorOrEqual", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right77: BinaryAssociation = BinaryAssociation(
    name="right77",
    ends={
        Property(name="miniJava_Expression79", type=miniJava_SuperiorOrEqual, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_SuperiorOrEqual78", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left80: BinaryAssociation = BinaryAssociation(
    name="left80",
    ends={
        Property(name="miniJava_Expression81", type=miniJava_InferiorOrEqual, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_InferiorOrEqual", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right82: BinaryAssociation = BinaryAssociation(
    name="right82",
    ends={
        Property(name="miniJava_Expression84", type=miniJava_InferiorOrEqual, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_InferiorOrEqual83", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left85: BinaryAssociation = BinaryAssociation(
    name="left85",
    ends={
        Property(name="miniJava_Expression86", type=miniJava_Superior, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Superior", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right87: BinaryAssociation = BinaryAssociation(
    name="right87",
    ends={
        Property(name="miniJava_Expression89", type=miniJava_Superior, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Superior88", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left90: BinaryAssociation = BinaryAssociation(
    name="left90",
    ends={
        Property(name="miniJava_Expression91", type=miniJava_Inferior, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Inferior", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right62: BinaryAssociation = BinaryAssociation(
    name="right62",
    ends={
        Property(name="miniJava_Expression64", type=miniJava_And, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_And63", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left65: BinaryAssociation = BinaryAssociation(
    name="left65",
    ends={
        Property(name="miniJava_Expression66", type=miniJava_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Equality", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right67: BinaryAssociation = BinaryAssociation(
    name="right67",
    ends={
        Property(name="miniJava_Expression69", type=miniJava_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Equality68", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left70: BinaryAssociation = BinaryAssociation(
    name="left70",
    ends={
        Property(name="miniJava_Expression71", type=miniJava_Inequality, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Inequality", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right92: BinaryAssociation = BinaryAssociation(
    name="right92",
    ends={
        Property(name="miniJava_Expression94", type=miniJava_Inferior, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Inferior93", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left95: BinaryAssociation = BinaryAssociation(
    name="left95",
    ends={
        Property(name="miniJava_Expression96", type=miniJava_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Plus", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right97: BinaryAssociation = BinaryAssociation(
    name="right97",
    ends={
        Property(name="miniJava_Expression99", type=miniJava_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Plus98", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left100: BinaryAssociation = BinaryAssociation(
    name="left100",
    ends={
        Property(name="miniJava_Expression101", type=miniJava_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Minus", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right102: BinaryAssociation = BinaryAssociation(
    name="right102",
    ends={
        Property(name="miniJava_Expression104", type=miniJava_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Minus103", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left105: BinaryAssociation = BinaryAssociation(
    name="left105",
    ends={
        Property(name="miniJava_Expression106", type=miniJava_Multiplication, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Multiplication", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right107: BinaryAssociation = BinaryAssociation(
    name="right107",
    ends={
        Property(name="miniJava_Expression109", type=miniJava_Multiplication, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Multiplication108", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left110: BinaryAssociation = BinaryAssociation(
    name="left110",
    ends={
        Property(name="miniJava_Expression111", type=miniJava_Division, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Division", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right112: BinaryAssociation = BinaryAssociation(
    name="right112",
    ends={
        Property(name="miniJava_Expression114", type=miniJava_Division, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Division113", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression122: BinaryAssociation = BinaryAssociation(
    name="expression122",
    ends={
        Property(name="miniJava_Expression123", type=miniJava_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Not", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression124: BinaryAssociation = BinaryAssociation(
    name="expression124",
    ends={
        Property(name="miniJava_Expression125", type=miniJava_Neg, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Neg", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
receiver126: BinaryAssociation = BinaryAssociation(
    name="receiver126",
    ends={
        Property(name="miniJava_Expression127", type=miniJava_FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_FieldAccess", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
field128: BinaryAssociation = BinaryAssociation(
    name="field128",
    ends={
        Property(name="miniJava_Field130", type=miniJava_FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_FieldAccess129", type=miniJava_Field, multiplicity=Multiplicity(0, 1))
    }
)
receiver131: BinaryAssociation = BinaryAssociation(
    name="receiver131",
    ends={
        Property(name="miniJava_Expression132", type=miniJava_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_MethodCall", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
method133: BinaryAssociation = BinaryAssociation(
    name="method133",
    ends={
        Property(name="miniJava_Method135", type=miniJava_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_MethodCall134", type=miniJava_Method, multiplicity=Multiplicity(0, 1))
    }
)
args136: BinaryAssociation = BinaryAssociation(
    name="args136",
    ends={
        Property(name="miniJava_Expression138", type=miniJava_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_MethodCall137", type=miniJava_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
object115: BinaryAssociation = BinaryAssociation(
    name="object115",
    ends={
        Property(name="miniJava_Expression116", type=miniJava_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ArrayAccess", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
index117: BinaryAssociation = BinaryAssociation(
    name="index117",
    ends={
        Property(name="miniJava_Expression119", type=miniJava_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ArrayAccess118", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
array120: BinaryAssociation = BinaryAssociation(
    name="array120",
    ends={
        Property(name="miniJava_Expression121", type=miniJava_ArrayLength, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ArrayLength", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
size146: BinaryAssociation = BinaryAssociation(
    name="size146",
    ends={
        Property(name="miniJava_Expression148", type=miniJava_NewArray, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_NewArray147", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
symbol149: BinaryAssociation = BinaryAssociation(
    name="symbol149",
    ends={
        Property(name="miniJava_Symbol", type=miniJava_SymbolRef, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_SymbolRef", type=miniJava_Symbol, multiplicity=Multiplicity(0, 1))
    }
)
bindings150: BinaryAssociation = BinaryAssociation(
    name="bindings150",
    ends={
        Property(name="miniJava_SymbolBinding", type=miniJava_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Context", type=miniJava_SymbolBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentContext152: BinaryAssociation = BinaryAssociation(
    name="parentContext152",
    ends={
        Property(name="Context", type=miniJava_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="childContext", type=miniJava_Context, multiplicity=Multiplicity(0, 1))
    }
)
childContext154: BinaryAssociation = BinaryAssociation(
    name="childContext154",
    ends={
        Property(name="Context155", type=miniJava_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="parentContext", type=miniJava_Context, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cache156: BinaryAssociation = BinaryAssociation(
    name="cache156",
    ends={
        Property(name="miniJava_SymbolToSymbolBindingMap", type=miniJava_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Context157", type=miniJava_SymbolToSymbolBindingMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value158: BinaryAssociation = BinaryAssociation(
    name="value158",
    ends={
        Property(name="miniJava_Value", type=miniJava_SymbolBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_SymbolBinding159", type=miniJava_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
symbol160: BinaryAssociation = BinaryAssociation(
    name="symbol160",
    ends={
        Property(name="miniJava_Symbol162", type=miniJava_SymbolBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_SymbolBinding161", type=miniJava_Symbol, multiplicity=Multiplicity(1, 1))
    }
)
field163: BinaryAssociation = BinaryAssociation(
    name="field163",
    ends={
        Property(name="miniJava_Field164", type=miniJava_FieldBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_FieldBinding", type=miniJava_Field, multiplicity=Multiplicity(1, 1))
    }
)
value165: BinaryAssociation = BinaryAssociation(
    name="value165",
    ends={
        Property(name="miniJava_Value167", type=miniJava_FieldBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_FieldBinding166", type=miniJava_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type139: BinaryAssociation = BinaryAssociation(
    name="type139",
    ends={
        Property(name="miniJava_Clazz140", type=miniJava_NewObject, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_NewObject", type=miniJava_Clazz, multiplicity=Multiplicity(0, 1))
    }
)
args141: BinaryAssociation = BinaryAssociation(
    name="args141",
    ends={
        Property(name="miniJava_Expression143", type=miniJava_NewObject, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_NewObject142", type=miniJava_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type144: BinaryAssociation = BinaryAssociation(
    name="type144",
    ends={
        Property(name="miniJava_TypeRef145", type=miniJava_NewArray, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_NewArray", type=miniJava_TypeRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rootFrame168: BinaryAssociation = BinaryAssociation(
    name="rootFrame168",
    ends={
        Property(name="miniJava_Frame", type=miniJava_State, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_State169", type=miniJava_Frame, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
objectsHeap170: BinaryAssociation = BinaryAssociation(
    name="objectsHeap170",
    ends={
        Property(name="miniJava_ObjectInstance", type=miniJava_State, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_State171", type=miniJava_ObjectInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputStream172: BinaryAssociation = BinaryAssociation(
    name="outputStream172",
    ends={
        Property(name="miniJava_OutputStream", type=miniJava_State, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_State173", type=miniJava_OutputStream, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contextCache176: BinaryAssociation = BinaryAssociation(
    name="contextCache176",
    ends={
        Property(name="miniJava_State177", type=miniJava_Context, multiplicity=Multiplicity(0, 1)),
        Property(name="miniJava_Context178", type=miniJava_State, multiplicity=Multiplicity(1, 1))
    }
)
frameCache179: BinaryAssociation = BinaryAssociation(
    name="frameCache179",
    ends={
        Property(name="miniJava_Frame181", type=miniJava_State, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_State180", type=miniJava_Frame, multiplicity=Multiplicity(0, 1))
    }
)
call182: BinaryAssociation = BinaryAssociation(
    name="call182",
    ends={
        Property(name="miniJava_Call", type=miniJava_Frame, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Frame183", type=miniJava_Call, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
instance184: BinaryAssociation = BinaryAssociation(
    name="instance184",
    ends={
        Property(name="miniJava_ObjectInstance186", type=miniJava_Frame, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Frame185", type=miniJava_ObjectInstance, multiplicity=Multiplicity(0, 1))
    }
)
childFrame188: BinaryAssociation = BinaryAssociation(
    name="childFrame188",
    ends={
        Property(name="Frame", type=miniJava_Frame, multiplicity=Multiplicity(1, 1)),
        Property(name="parentFrame", type=miniJava_Frame, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parentFrame190: BinaryAssociation = BinaryAssociation(
    name="parentFrame190",
    ends={
        Property(name="Frame191", type=miniJava_Frame, multiplicity=Multiplicity(1, 1)),
        Property(name="childFrame", type=miniJava_Frame, multiplicity=Multiplicity(0, 1))
    }
)
rootContext192: BinaryAssociation = BinaryAssociation(
    name="rootContext192",
    ends={
        Property(name="miniJava_Context194", type=miniJava_Frame, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Frame193", type=miniJava_Context, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arraysHeap174: BinaryAssociation = BinaryAssociation(
    name="arraysHeap174",
    ends={
        Property(name="miniJava_ArrayInstance", type=miniJava_State, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_State175", type=miniJava_ArrayInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
newz198: BinaryAssociation = BinaryAssociation(
    name="newz198",
    ends={
        Property(name="miniJava_NewObject199", type=miniJava_NewCall, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_NewCall", type=miniJava_NewObject, multiplicity=Multiplicity(1, 1))
    }
)
methodcall200: BinaryAssociation = BinaryAssociation(
    name="methodcall200",
    ends={
        Property(name="miniJava_MethodCall201", type=miniJava_MethodCall2, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_MethodCall2", type=miniJava_MethodCall, multiplicity=Multiplicity(1, 1))
    }
)
fieldbindings202: BinaryAssociation = BinaryAssociation(
    name="fieldbindings202",
    ends={
        Property(name="miniJava_FieldBinding204", type=miniJava_ObjectInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ObjectInstance203", type=miniJava_FieldBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnValue195: BinaryAssociation = BinaryAssociation(
    name="returnValue195",
    ends={
        Property(name="miniJava_Value197", type=miniJava_Frame, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Frame196", type=miniJava_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value208: BinaryAssociation = BinaryAssociation(
    name="value208",
    ends={
        Property(name="miniJava_Value210", type=miniJava_ArrayInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ArrayInstance209", type=miniJava_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instance211: BinaryAssociation = BinaryAssociation(
    name="instance211",
    ends={
        Property(name="miniJava_ObjectInstance212", type=miniJava_ObjectRefValue, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ObjectRefValue", type=miniJava_ObjectInstance, multiplicity=Multiplicity(0, 1))
    }
)
instance213: BinaryAssociation = BinaryAssociation(
    name="instance213",
    ends={
        Property(name="miniJava_ArrayInstance214", type=miniJava_ArrayRefValue, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ArrayRefValue", type=miniJava_ArrayInstance, multiplicity=Multiplicity(0, 1))
    }
)
key215: BinaryAssociation = BinaryAssociation(
    name="key215",
    ends={
        Property(name="miniJava_Symbol217", type=miniJava_SymbolToSymbolBindingMap, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_SymbolToSymbolBindingMap216", type=miniJava_Symbol, multiplicity=Multiplicity(0, 1))
    }
)
value218: BinaryAssociation = BinaryAssociation(
    name="value218",
    ends={
        Property(name="miniJava_SymbolBinding220", type=miniJava_SymbolToSymbolBindingMap, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_SymbolToSymbolBindingMap219", type=miniJava_SymbolBinding, multiplicity=Multiplicity(0, 1))
    }
)
type205: BinaryAssociation = BinaryAssociation(
    name="type205",
    ends={
        Property(name="miniJava_Clazz207", type=miniJava_ObjectInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ObjectInstance206", type=miniJava_Clazz, multiplicity=Multiplicity(1, 1))
    }
)
left227: BinaryAssociation = BinaryAssociation(
    name="left227",
    ends={
        Property(name="miniJava_Expression228", type=miniJava_Modulo, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Modulo", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right229: BinaryAssociation = BinaryAssociation(
    name="right229",
    ends={
        Property(name="miniJava_Expression231", type=miniJava_Modulo, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Modulo230", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
key221: BinaryAssociation = BinaryAssociation(
    name="key221",
    ends={
        Property(name="miniJava_Clazz223", type=miniJava_ClazzToMethodMap, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ClazzToMethodMap222", type=miniJava_Clazz, multiplicity=Multiplicity(0, 1))
    }
)
value224: BinaryAssociation = BinaryAssociation(
    name="value224",
    ends={
        Property(name="miniJava_Method226", type=miniJava_ClazzToMethodMap, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ClazzToMethodMap225", type=miniJava_Method, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_miniJava_TypeDeclaration_NamedElement = Generalization(general=NamedElement, specific=miniJava_TypeDeclaration)
gen_miniJava_Clazz_TypeDeclaration = Generalization(general=TypeDeclaration, specific=miniJava_Clazz)
gen_miniJava_Interface_TypeDeclaration = Generalization(general=TypeDeclaration, specific=miniJava_Interface)
gen_miniJava_Member_TypedDeclaration = Generalization(general=TypedDeclaration, specific=miniJava_Member)
gen_miniJava_Field_Member = Generalization(general=Member, specific=miniJava_Field)
gen_miniJava_Block_Statement = Generalization(general=Statement, specific=miniJava_Block)
gen_miniJava_PrintStatement_Statement = Generalization(general=Statement, specific=miniJava_PrintStatement)
gen_miniJava_Return_Statement = Generalization(general=Statement, specific=miniJava_Return)
gen_miniJava_IfStatement_Statement = Generalization(general=Statement, specific=miniJava_IfStatement)
gen_miniJava_WhileStatement_Statement = Generalization(general=Statement, specific=miniJava_WhileStatement)
gen_miniJava_ForStatement_Statement = Generalization(general=Statement, specific=miniJava_ForStatement)
gen_miniJava_Method_Member = Generalization(general=Member, specific=miniJava_Method)
gen_miniJava_Parameter_Symbol = Generalization(general=Symbol, specific=miniJava_Parameter)
gen_miniJava_TypedDeclaration_NamedElement = Generalization(general=NamedElement, specific=miniJava_TypedDeclaration)
gen_miniJava_Symbol_TypedDeclaration = Generalization(general=TypedDeclaration, specific=miniJava_Symbol)
gen_miniJava_VariableDeclaration_Symbol = Generalization(general=Symbol, specific=miniJava_VariableDeclaration)
gen_miniJava_VariableDeclaration_Assignee = Generalization(general=Assignee, specific=miniJava_VariableDeclaration)
gen_miniJava_Assignment_Statement = Generalization(general=Statement, specific=miniJava_Assignment)
gen_miniJava_Expression_Statement = Generalization(general=Statement, specific=miniJava_Expression)
gen_miniJava_Expression_Assignee = Generalization(general=Assignee, specific=miniJava_Expression)
gen_miniJava_ArrayTypeRef_TypeRef = Generalization(general=TypeRef, specific=miniJava_ArrayTypeRef)
gen_miniJava_IntegerTypeRef_SingleTypeRef = Generalization(general=SingleTypeRef, specific=miniJava_IntegerTypeRef)
gen_miniJava_BooleanTypeRef_SingleTypeRef = Generalization(general=SingleTypeRef, specific=miniJava_BooleanTypeRef)
gen_miniJava_StringTypeRef_SingleTypeRef = Generalization(general=SingleTypeRef, specific=miniJava_StringTypeRef)
gen_miniJava_VoidTypeRef_SingleTypeRef = Generalization(general=SingleTypeRef, specific=miniJava_VoidTypeRef)
gen_miniJava_Or_Expression = Generalization(general=Expression, specific=miniJava_Or)
gen_miniJava_And_Expression = Generalization(general=Expression, specific=miniJava_And)
gen_miniJava_SingleTypeRef_TypeRef = Generalization(general=TypeRef, specific=miniJava_SingleTypeRef)
gen_miniJava_ClassRef_SingleTypeRef = Generalization(general=SingleTypeRef, specific=miniJava_ClassRef)
gen_miniJava_SuperiorOrEqual_Expression = Generalization(general=Expression, specific=miniJava_SuperiorOrEqual)
gen_miniJava_InferiorOrEqual_Expression = Generalization(general=Expression, specific=miniJava_InferiorOrEqual)
gen_miniJava_Superior_Expression = Generalization(general=Expression, specific=miniJava_Superior)
gen_miniJava_Inferior_Expression = Generalization(general=Expression, specific=miniJava_Inferior)
gen_miniJava_Equality_Expression = Generalization(general=Expression, specific=miniJava_Equality)
gen_miniJava_Inequality_Expression = Generalization(general=Expression, specific=miniJava_Inequality)
gen_miniJava_Plus_Expression = Generalization(general=Expression, specific=miniJava_Plus)
gen_miniJava_Minus_Expression = Generalization(general=Expression, specific=miniJava_Minus)
gen_miniJava_Multiplication_Expression = Generalization(general=Expression, specific=miniJava_Multiplication)
gen_miniJava_Division_Expression = Generalization(general=Expression, specific=miniJava_Division)
gen_miniJava_Not_Expression = Generalization(general=Expression, specific=miniJava_Not)
gen_miniJava_Neg_Expression = Generalization(general=Expression, specific=miniJava_Neg)
gen_miniJava_FieldAccess_Expression = Generalization(general=Expression, specific=miniJava_FieldAccess)
gen_miniJava_MethodCall_Expression = Generalization(general=Expression, specific=miniJava_MethodCall)
gen_miniJava_StringConstant_Expression = Generalization(general=Expression, specific=miniJava_StringConstant)
gen_miniJava_IntConstant_Expression = Generalization(general=Expression, specific=miniJava_IntConstant)
gen_miniJava_BoolConstant_Expression = Generalization(general=Expression, specific=miniJava_BoolConstant)
gen_miniJava_This_Expression = Generalization(general=Expression, specific=miniJava_This)
gen_miniJava_ArrayAccess_Expression = Generalization(general=Expression, specific=miniJava_ArrayAccess)
gen_miniJava_ArrayLength_Expression = Generalization(general=Expression, specific=miniJava_ArrayLength)
gen_miniJava_SymbolRef_Expression = Generalization(general=Expression, specific=miniJava_SymbolRef)
gen_miniJava_IntegerValue_Value = Generalization(general=Value, specific=miniJava_IntegerValue)
gen_miniJava_StringValue_Value = Generalization(general=Value, specific=miniJava_StringValue)
gen_miniJava_Super_Expression = Generalization(general=Expression, specific=miniJava_Super)
gen_miniJava_Null_Expression = Generalization(general=Expression, specific=miniJava_Null)
gen_miniJava_NewObject_Expression = Generalization(general=Expression, specific=miniJava_NewObject)
gen_miniJava_NewArray_Expression = Generalization(general=Expression, specific=miniJava_NewArray)
gen_miniJava_BooleanValue_Value = Generalization(general=Value, specific=miniJava_BooleanValue)
gen_miniJava_NullValue_Value = Generalization(general=Value, specific=miniJava_NullValue)
gen_miniJava_NewCall_Call = Generalization(general=Call, specific=miniJava_NewCall)
gen_miniJava_MethodCall2_Call = Generalization(general=Call, specific=miniJava_MethodCall2)
gen_miniJava_ObjectRefValue_Value = Generalization(general=Value, specific=miniJava_ObjectRefValue)
gen_miniJava_ArrayRefValue_Value = Generalization(general=Value, specific=miniJava_ArrayRefValue)
gen_miniJava_Modulo_Expression = Generalization(general=Expression, specific=miniJava_Modulo)

# Domain Model
domain_model = DomainModel(
    name="miniJava",
    types={miniJava_Program, miniJava_Import, miniJava_TypeDeclaration, miniJava_State, NamedElement, miniJava_Interface, miniJava_Member, miniJava_Clazz, TypeDeclaration, TypedDeclaration, miniJava_Field, miniJava_Expression, Statement, miniJava_Statement, miniJava_PrintStatement, miniJava_Return, miniJava_IfStatement, miniJava_WhileStatement, miniJava_ForStatement, miniJava_Assignment, miniJava_Method, Member, miniJava_Parameter, miniJava_Block, miniJava_ClazzToMethodMap, Symbol, miniJava_NamedElement, miniJava_TypedDeclaration, miniJava_Symbol, miniJava_VariableDeclaration, Assignee, miniJava_Assignee, miniJava_ArrayTypeRef, miniJava_IntegerTypeRef, miniJava_BooleanTypeRef, miniJava_StringTypeRef, miniJava_VoidTypeRef, miniJava_Or, Expression, miniJava_And, miniJava_TypeRef, miniJava_SingleTypeRef, TypeRef, miniJava_ClassRef, SingleTypeRef, miniJava_SuperiorOrEqual, miniJava_InferiorOrEqual, miniJava_Superior, miniJava_Inferior, miniJava_Equality, miniJava_Inequality, miniJava_Plus, miniJava_Minus, miniJava_Multiplication, miniJava_Division, miniJava_Not, miniJava_Neg, miniJava_FieldAccess, miniJava_MethodCall, miniJava_StringConstant, miniJava_IntConstant, miniJava_BoolConstant, miniJava_This, miniJava_ArrayAccess, miniJava_ArrayLength, miniJava_SymbolRef, miniJava_Context, miniJava_SymbolBinding, miniJava_SymbolToSymbolBindingMap, miniJava_Value, miniJava_IntegerValue, Value, miniJava_FieldBinding, miniJava_StringValue, miniJava_Super, miniJava_Null, miniJava_NewObject, miniJava_NewArray, miniJava_BooleanValue, miniJava_OutputStream, miniJava_Frame, miniJava_ObjectInstance, miniJava_ArrayInstance, miniJava_Call, miniJava_NullValue, miniJava_NewCall, Call, miniJava_MethodCall2, miniJava_ObjectRefValue, miniJava_ArrayRefValue, miniJava_Modulo, AccessLevel},
    associations={imports0, classes1, state3, implementz5, members7, superClass10, defaultValue16, statements17, expression19, expression21, expression23, thenBlock25, elseBlock28, condition31, block33, declaration36, params11, body12, cache14, typeRef48, assignee49, value51, typeRef54, left55, right57, left60, condition37, progression40, block43, referencedClass46, right72, left75, right77, left80, right82, left85, right87, left90, right62, left65, right67, left70, right92, left95, right97, left100, right102, left105, right107, left110, right112, expression122, expression124, receiver126, field128, receiver131, method133, args136, object115, index117, array120, size146, symbol149, bindings150, parentContext152, childContext154, cache156, value158, symbol160, field163, value165, type139, args141, type144, rootFrame168, objectsHeap170, outputStream172, contextCache176, frameCache179, call182, instance184, childFrame188, parentFrame190, rootContext192, arraysHeap174, newz198, methodcall200, fieldbindings202, returnValue195, value208, instance211, instance213, key215, value218, type205, left227, right229, key221, value224},
    generalizations={gen_miniJava_TypeDeclaration_NamedElement, gen_miniJava_Clazz_TypeDeclaration, gen_miniJava_Interface_TypeDeclaration, gen_miniJava_Member_TypedDeclaration, gen_miniJava_Field_Member, gen_miniJava_Block_Statement, gen_miniJava_PrintStatement_Statement, gen_miniJava_Return_Statement, gen_miniJava_IfStatement_Statement, gen_miniJava_WhileStatement_Statement, gen_miniJava_ForStatement_Statement, gen_miniJava_Method_Member, gen_miniJava_Parameter_Symbol, gen_miniJava_TypedDeclaration_NamedElement, gen_miniJava_Symbol_TypedDeclaration, gen_miniJava_VariableDeclaration_Symbol, gen_miniJava_VariableDeclaration_Assignee, gen_miniJava_Assignment_Statement, gen_miniJava_Expression_Statement, gen_miniJava_Expression_Assignee, gen_miniJava_ArrayTypeRef_TypeRef, gen_miniJava_IntegerTypeRef_SingleTypeRef, gen_miniJava_BooleanTypeRef_SingleTypeRef, gen_miniJava_StringTypeRef_SingleTypeRef, gen_miniJava_VoidTypeRef_SingleTypeRef, gen_miniJava_Or_Expression, gen_miniJava_And_Expression, gen_miniJava_SingleTypeRef_TypeRef, gen_miniJava_ClassRef_SingleTypeRef, gen_miniJava_SuperiorOrEqual_Expression, gen_miniJava_InferiorOrEqual_Expression, gen_miniJava_Superior_Expression, gen_miniJava_Inferior_Expression, gen_miniJava_Equality_Expression, gen_miniJava_Inequality_Expression, gen_miniJava_Plus_Expression, gen_miniJava_Minus_Expression, gen_miniJava_Multiplication_Expression, gen_miniJava_Division_Expression, gen_miniJava_Not_Expression, gen_miniJava_Neg_Expression, gen_miniJava_FieldAccess_Expression, gen_miniJava_MethodCall_Expression, gen_miniJava_StringConstant_Expression, gen_miniJava_IntConstant_Expression, gen_miniJava_BoolConstant_Expression, gen_miniJava_This_Expression, gen_miniJava_ArrayAccess_Expression, gen_miniJava_ArrayLength_Expression, gen_miniJava_SymbolRef_Expression, gen_miniJava_IntegerValue_Value, gen_miniJava_StringValue_Value, gen_miniJava_Super_Expression, gen_miniJava_Null_Expression, gen_miniJava_NewObject_Expression, gen_miniJava_NewArray_Expression, gen_miniJava_BooleanValue_Value, gen_miniJava_NullValue_Value, gen_miniJava_NewCall_Call, gen_miniJava_MethodCall2_Call, gen_miniJava_ObjectRefValue_Value, gen_miniJava_ArrayRefValue_Value, gen_miniJava_Modulo_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)