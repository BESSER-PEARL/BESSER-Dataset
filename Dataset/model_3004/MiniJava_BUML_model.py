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
            EnumerationLiteral(name="PUBLIC"),
			EnumerationLiteral(name="PRIVATE"),
			EnumerationLiteral(name="PROTECTED")
    }
)

# Classes
miniJava_Program = Class(name="miniJava::Program")
miniJava_Import = Class(name="miniJava::Import")
miniJava_TypeDeclaration = Class(name="miniJava::TypeDeclaration")
NamedElement = Class(name="NamedElement")
miniJava_Interface = Class(name="miniJava::Interface")
miniJava_Member = Class(name="miniJava::Member")
miniJava_Class = Class(name="miniJava::Class")
TypeDeclaration = Class(name="TypeDeclaration")
Statement = Class(name="Statement")
miniJava_Statement = Class(name="miniJava::Statement")
TypedDeclaration = Class(name="TypedDeclaration")
miniJava_Method = Class(name="miniJava::Method")
Member = Class(name="Member")
miniJava_Parameter = Class(name="miniJava::Parameter")
miniJava_Block = Class(name="miniJava::Block")
Symbol = Class(name="Symbol")
miniJava_Field = Class(name="miniJava::Field")
miniJava_Expression = Class(name="miniJava::Expression")
miniJava_ForStatement = Class(name="miniJava::ForStatement")
miniJava_PrintStatement = Class(name="miniJava::PrintStatement")
miniJava_Return = Class(name="miniJava::Return")
miniJava_IfStatement = Class(name="miniJava::IfStatement")
miniJava_WhileStatement = Class(name="miniJava::WhileStatement")
miniJava_Symbol = Class(name="miniJava::Symbol")
miniJava_VariableDeclaration = Class(name="miniJava::VariableDeclaration")
Assignee = Class(name="Assignee")
miniJava_Assignment = Class(name="miniJava::Assignment")
miniJava_TypeRef = Class(name="miniJava::TypeRef")
miniJava_SingleTypeRef = Class(name="miniJava::SingleTypeRef")
TypeRef = Class(name="TypeRef")
miniJava_ClassRef = Class(name="miniJava::ClassRef")
SingleTypeRef = Class(name="SingleTypeRef")
miniJava_NamedElement = Class(name="miniJava::NamedElement")
miniJava_TypedDeclaration = Class(name="miniJava::TypedDeclaration")
miniJava_Assignee = Class(name="miniJava::Assignee")
miniJava_ArrayTypeRef = Class(name="miniJava::ArrayTypeRef")
miniJava_IntegerTypeRef = Class(name="miniJava::IntegerTypeRef")
miniJava_And = Class(name="miniJava::And")
miniJava_Equality = Class(name="miniJava::Equality")
miniJava_Inequality = Class(name="miniJava::Inequality")
miniJava_BooleanTypeRef = Class(name="miniJava::BooleanTypeRef")
miniJava_StringTypeRef = Class(name="miniJava::StringTypeRef")
miniJava_VoidTypeRef = Class(name="miniJava::VoidTypeRef")
miniJava_Or = Class(name="miniJava::Or")
Expression = Class(name="Expression")
miniJava_InferiorOrEqual = Class(name="miniJava::InferiorOrEqual")
miniJava_Superior = Class(name="miniJava::Superior")
miniJava_Inferior = Class(name="miniJava::Inferior")
miniJava_SuperiorOrEqual = Class(name="miniJava::SuperiorOrEqual")
miniJava_Plus = Class(name="miniJava::Plus")
miniJava_Minus = Class(name="miniJava::Minus")
miniJava_Multiplication = Class(name="miniJava::Multiplication")
miniJava_Division = Class(name="miniJava::Division")
miniJava_ArrayAccess = Class(name="miniJava::ArrayAccess")
miniJava_ArrayLength = Class(name="miniJava::ArrayLength")
miniJava_Not = Class(name="miniJava::Not")
miniJava_Neg = Class(name="miniJava::Neg")
miniJava_MethodCall = Class(name="miniJava::MethodCall")
miniJava_StringConstant = Class(name="miniJava::StringConstant")
miniJava_IntConstant = Class(name="miniJava::IntConstant")
miniJava_BoolConstant = Class(name="miniJava::BoolConstant")
miniJava_FieldAccess = Class(name="miniJava::FieldAccess")
miniJava_Super = Class(name="miniJava::Super")
miniJava_Null = Class(name="miniJava::Null")
miniJava_NewObject = Class(name="miniJava::NewObject")
miniJava_NewArray = Class(name="miniJava::NewArray")
miniJava_SymbolRef = Class(name="miniJava::SymbolRef")
miniJava_This = Class(name="miniJava::This")

# miniJava_Program class attributes and methods
miniJava_Program_name: Property = Property(name="name", type=StringType)
miniJava_Program.attributes={miniJava_Program_name}

# miniJava_Import class attributes and methods
miniJava_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
miniJava_Import.attributes={miniJava_Import_importedNamespace}

# miniJava_TypeDeclaration class attributes and methods
miniJava_TypeDeclaration_accessLevel: Property = Property(name="accessLevel", type=StringType)
miniJava_TypeDeclaration.attributes={miniJava_TypeDeclaration_accessLevel}

# NamedElement class attributes and methods

# miniJava_Interface class attributes and methods

# miniJava_Member class attributes and methods
miniJava_Member_access: Property = Property(name="access", type=StringType)
miniJava_Member.attributes={miniJava_Member_access}

# miniJava_Class class attributes and methods
miniJava_Class_abstract: Property = Property(name="abstract", type=BooleanType)
miniJava_Class.attributes={miniJava_Class_abstract}

# TypeDeclaration class attributes and methods

# Statement class attributes and methods

# miniJava_Statement class attributes and methods

# TypedDeclaration class attributes and methods

# miniJava_Method class attributes and methods
miniJava_Method_abstract: Property = Property(name="abstract", type=BooleanType)
miniJava_Method_static: Property = Property(name="static", type=BooleanType)
miniJava_Method.attributes={miniJava_Method_static, miniJava_Method_abstract}

# Member class attributes and methods

# miniJava_Parameter class attributes and methods

# miniJava_Block class attributes and methods

# Symbol class attributes and methods

# miniJava_Field class attributes and methods

# miniJava_Expression class attributes and methods

# miniJava_ForStatement class attributes and methods

# miniJava_PrintStatement class attributes and methods

# miniJava_Return class attributes and methods

# miniJava_IfStatement class attributes and methods

# miniJava_WhileStatement class attributes and methods

# miniJava_Symbol class attributes and methods

# miniJava_VariableDeclaration class attributes and methods

# Assignee class attributes and methods

# miniJava_Assignment class attributes and methods

# miniJava_TypeRef class attributes and methods

# miniJava_SingleTypeRef class attributes and methods

# TypeRef class attributes and methods

# miniJava_ClassRef class attributes and methods

# SingleTypeRef class attributes and methods

# miniJava_NamedElement class attributes and methods
miniJava_NamedElement_name: Property = Property(name="name", type=StringType)
miniJava_NamedElement.attributes={miniJava_NamedElement_name}

# miniJava_TypedDeclaration class attributes and methods

# miniJava_Assignee class attributes and methods

# miniJava_ArrayTypeRef class attributes and methods

# miniJava_IntegerTypeRef class attributes and methods

# miniJava_And class attributes and methods

# miniJava_Equality class attributes and methods

# miniJava_Inequality class attributes and methods

# miniJava_BooleanTypeRef class attributes and methods

# miniJava_StringTypeRef class attributes and methods

# miniJava_VoidTypeRef class attributes and methods

# miniJava_Or class attributes and methods

# Expression class attributes and methods

# miniJava_InferiorOrEqual class attributes and methods

# miniJava_Superior class attributes and methods

# miniJava_Inferior class attributes and methods

# miniJava_SuperiorOrEqual class attributes and methods

# miniJava_Plus class attributes and methods

# miniJava_Minus class attributes and methods

# miniJava_Multiplication class attributes and methods

# miniJava_Division class attributes and methods

# miniJava_ArrayAccess class attributes and methods

# miniJava_ArrayLength class attributes and methods

# miniJava_Not class attributes and methods

# miniJava_Neg class attributes and methods

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

# miniJava_FieldAccess class attributes and methods

# miniJava_Super class attributes and methods

# miniJava_Null class attributes and methods

# miniJava_NewObject class attributes and methods

# miniJava_NewArray class attributes and methods

# miniJava_SymbolRef class attributes and methods

# miniJava_This class attributes and methods

# Relationships
superClass8: BinaryAssociation = BinaryAssociation(
    name="superClass8",
    ends={
        Property(name="miniJava_Class", type=miniJava_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Class7", type=miniJava_Class, multiplicity=Multiplicity(0, 1))
    }
)
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
implements3: BinaryAssociation = BinaryAssociation(
    name="implements3",
    ends={
        Property(name="miniJava_Interface", type=miniJava_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_TypeDeclaration4", type=miniJava_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
members5: BinaryAssociation = BinaryAssociation(
    name="members5",
    ends={
        Property(name="miniJava_Member", type=miniJava_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_TypeDeclaration6", type=miniJava_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
params9: BinaryAssociation = BinaryAssociation(
    name="params9",
    ends={
        Property(name="miniJava_Parameter", type=miniJava_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Method", type=miniJava_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body10: BinaryAssociation = BinaryAssociation(
    name="body10",
    ends={
        Property(name="miniJava_Block", type=miniJava_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Method11", type=miniJava_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultValue12: BinaryAssociation = BinaryAssociation(
    name="defaultValue12",
    ends={
        Property(name="miniJava_Expression", type=miniJava_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Field", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block29: BinaryAssociation = BinaryAssociation(
    name="block29",
    ends={
        Property(name="miniJava_Block31", type=miniJava_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_WhileStatement30", type=miniJava_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements13: BinaryAssociation = BinaryAssociation(
    name="statements13",
    ends={
        Property(name="miniJava_Statement", type=miniJava_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Block14", type=miniJava_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression15: BinaryAssociation = BinaryAssociation(
    name="expression15",
    ends={
        Property(name="miniJava_Expression16", type=miniJava_PrintStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_PrintStatement", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression17: BinaryAssociation = BinaryAssociation(
    name="expression17",
    ends={
        Property(name="miniJava_Expression18", type=miniJava_Return, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Return", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression19: BinaryAssociation = BinaryAssociation(
    name="expression19",
    ends={
        Property(name="miniJava_Expression20", type=miniJava_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_IfStatement", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenBlock21: BinaryAssociation = BinaryAssociation(
    name="thenBlock21",
    ends={
        Property(name="miniJava_Block23", type=miniJava_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_IfStatement22", type=miniJava_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseBlock24: BinaryAssociation = BinaryAssociation(
    name="elseBlock24",
    ends={
        Property(name="miniJava_Block26", type=miniJava_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_IfStatement25", type=miniJava_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition27: BinaryAssociation = BinaryAssociation(
    name="condition27",
    ends={
        Property(name="miniJava_Expression28", type=miniJava_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_WhileStatement", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration32: BinaryAssociation = BinaryAssociation(
    name="declaration32",
    ends={
        Property(name="miniJava_Assignment", type=miniJava_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ForStatement", type=miniJava_Assignment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition33: BinaryAssociation = BinaryAssociation(
    name="condition33",
    ends={
        Property(name="miniJava_Expression35", type=miniJava_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ForStatement34", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
progression36: BinaryAssociation = BinaryAssociation(
    name="progression36",
    ends={
        Property(name="miniJava_Assignment38", type=miniJava_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ForStatement37", type=miniJava_Assignment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block39: BinaryAssociation = BinaryAssociation(
    name="block39",
    ends={
        Property(name="miniJava_Block41", type=miniJava_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ForStatement40", type=miniJava_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referencedClass42: BinaryAssociation = BinaryAssociation(
    name="referencedClass42",
    ends={
        Property(name="miniJava_TypeDeclaration43", type=miniJava_ClassRef, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ClassRef", type=miniJava_TypeDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
typeRef44: BinaryAssociation = BinaryAssociation(
    name="typeRef44",
    ends={
        Property(name="miniJava_TypeRef", type=miniJava_TypedDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_TypedDeclaration", type=miniJava_TypeRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignee45: BinaryAssociation = BinaryAssociation(
    name="assignee45",
    ends={
        Property(name="miniJava_Assignee", type=miniJava_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Assignment46", type=miniJava_Assignee, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value47: BinaryAssociation = BinaryAssociation(
    name="value47",
    ends={
        Property(name="miniJava_Expression49", type=miniJava_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Assignment48", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left51: BinaryAssociation = BinaryAssociation(
    name="left51",
    ends={
        Property(name="miniJava_Expression52", type=miniJava_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Or", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeRef50: BinaryAssociation = BinaryAssociation(
    name="typeRef50",
    ends={
        Property(name="miniJava_SingleTypeRef", type=miniJava_ArrayTypeRef, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ArrayTypeRef", type=miniJava_SingleTypeRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right53: BinaryAssociation = BinaryAssociation(
    name="right53",
    ends={
        Property(name="miniJava_Expression55", type=miniJava_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Or54", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left56: BinaryAssociation = BinaryAssociation(
    name="left56",
    ends={
        Property(name="miniJava_Expression57", type=miniJava_And, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_And", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right58: BinaryAssociation = BinaryAssociation(
    name="right58",
    ends={
        Property(name="miniJava_Expression60", type=miniJava_And, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_And59", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left61: BinaryAssociation = BinaryAssociation(
    name="left61",
    ends={
        Property(name="miniJava_Expression62", type=miniJava_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Equality", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right63: BinaryAssociation = BinaryAssociation(
    name="right63",
    ends={
        Property(name="miniJava_Expression65", type=miniJava_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Equality64", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left66: BinaryAssociation = BinaryAssociation(
    name="left66",
    ends={
        Property(name="miniJava_Expression67", type=miniJava_Inequality, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Inequality", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left71: BinaryAssociation = BinaryAssociation(
    name="left71",
    ends={
        Property(name="miniJava_Expression72", type=miniJava_SuperiorOrEqual, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_SuperiorOrEqual", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right73: BinaryAssociation = BinaryAssociation(
    name="right73",
    ends={
        Property(name="miniJava_Expression75", type=miniJava_SuperiorOrEqual, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_SuperiorOrEqual74", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left76: BinaryAssociation = BinaryAssociation(
    name="left76",
    ends={
        Property(name="miniJava_Expression77", type=miniJava_InferiorOrEqual, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_InferiorOrEqual", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right78: BinaryAssociation = BinaryAssociation(
    name="right78",
    ends={
        Property(name="miniJava_Expression80", type=miniJava_InferiorOrEqual, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_InferiorOrEqual79", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left81: BinaryAssociation = BinaryAssociation(
    name="left81",
    ends={
        Property(name="miniJava_Expression82", type=miniJava_Superior, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Superior", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right83: BinaryAssociation = BinaryAssociation(
    name="right83",
    ends={
        Property(name="miniJava_Expression85", type=miniJava_Superior, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Superior84", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left86: BinaryAssociation = BinaryAssociation(
    name="left86",
    ends={
        Property(name="miniJava_Expression87", type=miniJava_Inferior, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Inferior", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right68: BinaryAssociation = BinaryAssociation(
    name="right68",
    ends={
        Property(name="miniJava_Expression70", type=miniJava_Inequality, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Inequality69", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left91: BinaryAssociation = BinaryAssociation(
    name="left91",
    ends={
        Property(name="miniJava_Expression92", type=miniJava_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Plus", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right93: BinaryAssociation = BinaryAssociation(
    name="right93",
    ends={
        Property(name="miniJava_Expression95", type=miniJava_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Plus94", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left96: BinaryAssociation = BinaryAssociation(
    name="left96",
    ends={
        Property(name="miniJava_Expression97", type=miniJava_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Minus", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right98: BinaryAssociation = BinaryAssociation(
    name="right98",
    ends={
        Property(name="miniJava_Expression100", type=miniJava_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Minus99", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left101: BinaryAssociation = BinaryAssociation(
    name="left101",
    ends={
        Property(name="miniJava_Expression102", type=miniJava_Multiplication, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Multiplication", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right103: BinaryAssociation = BinaryAssociation(
    name="right103",
    ends={
        Property(name="miniJava_Expression105", type=miniJava_Multiplication, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Multiplication104", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right88: BinaryAssociation = BinaryAssociation(
    name="right88",
    ends={
        Property(name="miniJava_Expression90", type=miniJava_Inferior, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Inferior89", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right108: BinaryAssociation = BinaryAssociation(
    name="right108",
    ends={
        Property(name="miniJava_Expression110", type=miniJava_Division, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Division109", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object111: BinaryAssociation = BinaryAssociation(
    name="object111",
    ends={
        Property(name="miniJava_Expression112", type=miniJava_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ArrayAccess", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
index113: BinaryAssociation = BinaryAssociation(
    name="index113",
    ends={
        Property(name="miniJava_Expression115", type=miniJava_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ArrayAccess114", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
array116: BinaryAssociation = BinaryAssociation(
    name="array116",
    ends={
        Property(name="miniJava_Expression117", type=miniJava_ArrayLength, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_ArrayLength", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression118: BinaryAssociation = BinaryAssociation(
    name="expression118",
    ends={
        Property(name="miniJava_Expression119", type=miniJava_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Not", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression120: BinaryAssociation = BinaryAssociation(
    name="expression120",
    ends={
        Property(name="miniJava_Expression121", type=miniJava_Neg, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Neg", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left106: BinaryAssociation = BinaryAssociation(
    name="left106",
    ends={
        Property(name="miniJava_Expression107", type=miniJava_Division, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_Division", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
receiver122: BinaryAssociation = BinaryAssociation(
    name="receiver122",
    ends={
        Property(name="miniJava_Expression123", type=miniJava_FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_FieldAccess", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
field124: BinaryAssociation = BinaryAssociation(
    name="field124",
    ends={
        Property(name="miniJava_Field126", type=miniJava_FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_FieldAccess125", type=miniJava_Field, multiplicity=Multiplicity(0, 1))
    }
)
receiver127: BinaryAssociation = BinaryAssociation(
    name="receiver127",
    ends={
        Property(name="miniJava_Expression128", type=miniJava_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_MethodCall", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
method129: BinaryAssociation = BinaryAssociation(
    name="method129",
    ends={
        Property(name="miniJava_Method131", type=miniJava_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_MethodCall130", type=miniJava_Method, multiplicity=Multiplicity(0, 1))
    }
)
args132: BinaryAssociation = BinaryAssociation(
    name="args132",
    ends={
        Property(name="miniJava_Expression134", type=miniJava_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_MethodCall133", type=miniJava_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type135: BinaryAssociation = BinaryAssociation(
    name="type135",
    ends={
        Property(name="miniJava_Class136", type=miniJava_NewObject, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_NewObject", type=miniJava_Class, multiplicity=Multiplicity(0, 1))
    }
)
args137: BinaryAssociation = BinaryAssociation(
    name="args137",
    ends={
        Property(name="miniJava_Expression139", type=miniJava_NewObject, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_NewObject138", type=miniJava_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type140: BinaryAssociation = BinaryAssociation(
    name="type140",
    ends={
        Property(name="miniJava_TypeRef141", type=miniJava_NewArray, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_NewArray", type=miniJava_TypeRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
size142: BinaryAssociation = BinaryAssociation(
    name="size142",
    ends={
        Property(name="miniJava_Expression144", type=miniJava_NewArray, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_NewArray143", type=miniJava_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
symbol145: BinaryAssociation = BinaryAssociation(
    name="symbol145",
    ends={
        Property(name="miniJava_Symbol", type=miniJava_SymbolRef, multiplicity=Multiplicity(1, 1)),
        Property(name="miniJava_SymbolRef", type=miniJava_Symbol, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_miniJava_TypeDeclaration_NamedElement = Generalization(general=NamedElement, specific=miniJava_TypeDeclaration)
gen_miniJava_Class_TypeDeclaration = Generalization(general=TypeDeclaration, specific=miniJava_Class)
gen_miniJava_Block_Statement = Generalization(general=Statement, specific=miniJava_Block)
gen_miniJava_Interface_TypeDeclaration = Generalization(general=TypeDeclaration, specific=miniJava_Interface)
gen_miniJava_Member_TypedDeclaration = Generalization(general=TypedDeclaration, specific=miniJava_Member)
gen_miniJava_Method_Member = Generalization(general=Member, specific=miniJava_Method)
gen_miniJava_Parameter_Symbol = Generalization(general=Symbol, specific=miniJava_Parameter)
gen_miniJava_Field_Member = Generalization(general=Member, specific=miniJava_Field)
gen_miniJava_ForStatement_Statement = Generalization(general=Statement, specific=miniJava_ForStatement)
gen_miniJava_PrintStatement_Statement = Generalization(general=Statement, specific=miniJava_PrintStatement)
gen_miniJava_Return_Statement = Generalization(general=Statement, specific=miniJava_Return)
gen_miniJava_IfStatement_Statement = Generalization(general=Statement, specific=miniJava_IfStatement)
gen_miniJava_WhileStatement_Statement = Generalization(general=Statement, specific=miniJava_WhileStatement)
gen_miniJava_Symbol_TypedDeclaration = Generalization(general=TypedDeclaration, specific=miniJava_Symbol)
gen_miniJava_VariableDeclaration_Symbol = Generalization(general=Symbol, specific=miniJava_VariableDeclaration)
gen_miniJava_VariableDeclaration_Assignee = Generalization(general=Assignee, specific=miniJava_VariableDeclaration)
gen_miniJava_SingleTypeRef_TypeRef = Generalization(general=TypeRef, specific=miniJava_SingleTypeRef)
gen_miniJava_ClassRef_SingleTypeRef = Generalization(general=SingleTypeRef, specific=miniJava_ClassRef)
gen_miniJava_TypedDeclaration_NamedElement = Generalization(general=NamedElement, specific=miniJava_TypedDeclaration)
gen_miniJava_Assignment_Statement = Generalization(general=Statement, specific=miniJava_Assignment)
gen_miniJava_Expression_Statement = Generalization(general=Statement, specific=miniJava_Expression)
gen_miniJava_Expression_Assignee = Generalization(general=Assignee, specific=miniJava_Expression)
gen_miniJava_ArrayTypeRef_TypeRef = Generalization(general=TypeRef, specific=miniJava_ArrayTypeRef)
gen_miniJava_IntegerTypeRef_SingleTypeRef = Generalization(general=SingleTypeRef, specific=miniJava_IntegerTypeRef)
gen_miniJava_And_Expression = Generalization(general=Expression, specific=miniJava_And)
gen_miniJava_Equality_Expression = Generalization(general=Expression, specific=miniJava_Equality)
gen_miniJava_Inequality_Expression = Generalization(general=Expression, specific=miniJava_Inequality)
gen_miniJava_BooleanTypeRef_SingleTypeRef = Generalization(general=SingleTypeRef, specific=miniJava_BooleanTypeRef)
gen_miniJava_StringTypeRef_SingleTypeRef = Generalization(general=SingleTypeRef, specific=miniJava_StringTypeRef)
gen_miniJava_VoidTypeRef_SingleTypeRef = Generalization(general=SingleTypeRef, specific=miniJava_VoidTypeRef)
gen_miniJava_Or_Expression = Generalization(general=Expression, specific=miniJava_Or)
gen_miniJava_InferiorOrEqual_Expression = Generalization(general=Expression, specific=miniJava_InferiorOrEqual)
gen_miniJava_Superior_Expression = Generalization(general=Expression, specific=miniJava_Superior)
gen_miniJava_Inferior_Expression = Generalization(general=Expression, specific=miniJava_Inferior)
gen_miniJava_SuperiorOrEqual_Expression = Generalization(general=Expression, specific=miniJava_SuperiorOrEqual)
gen_miniJava_Plus_Expression = Generalization(general=Expression, specific=miniJava_Plus)
gen_miniJava_Minus_Expression = Generalization(general=Expression, specific=miniJava_Minus)
gen_miniJava_Multiplication_Expression = Generalization(general=Expression, specific=miniJava_Multiplication)
gen_miniJava_Division_Expression = Generalization(general=Expression, specific=miniJava_Division)
gen_miniJava_ArrayAccess_Expression = Generalization(general=Expression, specific=miniJava_ArrayAccess)
gen_miniJava_ArrayLength_Expression = Generalization(general=Expression, specific=miniJava_ArrayLength)
gen_miniJava_Not_Expression = Generalization(general=Expression, specific=miniJava_Not)
gen_miniJava_Neg_Expression = Generalization(general=Expression, specific=miniJava_Neg)
gen_miniJava_MethodCall_Expression = Generalization(general=Expression, specific=miniJava_MethodCall)
gen_miniJava_StringConstant_Expression = Generalization(general=Expression, specific=miniJava_StringConstant)
gen_miniJava_IntConstant_Expression = Generalization(general=Expression, specific=miniJava_IntConstant)
gen_miniJava_FieldAccess_Expression = Generalization(general=Expression, specific=miniJava_FieldAccess)
gen_miniJava_This_Expression = Generalization(general=Expression, specific=miniJava_This)
gen_miniJava_Super_Expression = Generalization(general=Expression, specific=miniJava_Super)
gen_miniJava_Null_Expression = Generalization(general=Expression, specific=miniJava_Null)
gen_miniJava_NewObject_Expression = Generalization(general=Expression, specific=miniJava_NewObject)
gen_miniJava_NewArray_Expression = Generalization(general=Expression, specific=miniJava_NewArray)
gen_miniJava_SymbolRef_Expression = Generalization(general=Expression, specific=miniJava_SymbolRef)
gen_miniJava_BoolConstant_Expression = Generalization(general=Expression, specific=miniJava_BoolConstant)

# Domain Model
domain_model = DomainModel(
    name="miniJava",
    types={miniJava_Program, miniJava_Import, miniJava_TypeDeclaration, NamedElement, miniJava_Interface, miniJava_Member, miniJava_Class, TypeDeclaration, Statement, miniJava_Statement, TypedDeclaration, miniJava_Method, Member, miniJava_Parameter, miniJava_Block, Symbol, miniJava_Field, miniJava_Expression, miniJava_ForStatement, miniJava_PrintStatement, miniJava_Return, miniJava_IfStatement, miniJava_WhileStatement, miniJava_Symbol, miniJava_VariableDeclaration, Assignee, miniJava_Assignment, miniJava_TypeRef, miniJava_SingleTypeRef, TypeRef, miniJava_ClassRef, SingleTypeRef, miniJava_NamedElement, miniJava_TypedDeclaration, miniJava_Assignee, miniJava_ArrayTypeRef, miniJava_IntegerTypeRef, miniJava_And, miniJava_Equality, miniJava_Inequality, miniJava_BooleanTypeRef, miniJava_StringTypeRef, miniJava_VoidTypeRef, miniJava_Or, Expression, miniJava_InferiorOrEqual, miniJava_Superior, miniJava_Inferior, miniJava_SuperiorOrEqual, miniJava_Plus, miniJava_Minus, miniJava_Multiplication, miniJava_Division, miniJava_ArrayAccess, miniJava_ArrayLength, miniJava_Not, miniJava_Neg, miniJava_MethodCall, miniJava_StringConstant, miniJava_IntConstant, miniJava_BoolConstant, miniJava_FieldAccess, miniJava_Super, miniJava_Null, miniJava_NewObject, miniJava_NewArray, miniJava_SymbolRef, miniJava_This, AccessLevel},
    associations={superClass8, imports0, classes1, implements3, members5, params9, body10, defaultValue12, block29, statements13, expression15, expression17, expression19, thenBlock21, elseBlock24, condition27, declaration32, condition33, progression36, block39, referencedClass42, typeRef44, assignee45, value47, left51, typeRef50, right53, left56, right58, left61, right63, left66, left71, right73, left76, right78, left81, right83, left86, right68, left91, right93, left96, right98, left101, right103, right88, right108, object111, index113, array116, expression118, expression120, left106, receiver122, field124, receiver127, method129, args132, type135, args137, type140, size142, symbol145},
    generalizations={gen_miniJava_TypeDeclaration_NamedElement, gen_miniJava_Class_TypeDeclaration, gen_miniJava_Block_Statement, gen_miniJava_Interface_TypeDeclaration, gen_miniJava_Member_TypedDeclaration, gen_miniJava_Method_Member, gen_miniJava_Parameter_Symbol, gen_miniJava_Field_Member, gen_miniJava_ForStatement_Statement, gen_miniJava_PrintStatement_Statement, gen_miniJava_Return_Statement, gen_miniJava_IfStatement_Statement, gen_miniJava_WhileStatement_Statement, gen_miniJava_Symbol_TypedDeclaration, gen_miniJava_VariableDeclaration_Symbol, gen_miniJava_VariableDeclaration_Assignee, gen_miniJava_SingleTypeRef_TypeRef, gen_miniJava_ClassRef_SingleTypeRef, gen_miniJava_TypedDeclaration_NamedElement, gen_miniJava_Assignment_Statement, gen_miniJava_Expression_Statement, gen_miniJava_Expression_Assignee, gen_miniJava_ArrayTypeRef_TypeRef, gen_miniJava_IntegerTypeRef_SingleTypeRef, gen_miniJava_And_Expression, gen_miniJava_Equality_Expression, gen_miniJava_Inequality_Expression, gen_miniJava_BooleanTypeRef_SingleTypeRef, gen_miniJava_StringTypeRef_SingleTypeRef, gen_miniJava_VoidTypeRef_SingleTypeRef, gen_miniJava_Or_Expression, gen_miniJava_InferiorOrEqual_Expression, gen_miniJava_Superior_Expression, gen_miniJava_Inferior_Expression, gen_miniJava_SuperiorOrEqual_Expression, gen_miniJava_Plus_Expression, gen_miniJava_Minus_Expression, gen_miniJava_Multiplication_Expression, gen_miniJava_Division_Expression, gen_miniJava_ArrayAccess_Expression, gen_miniJava_ArrayLength_Expression, gen_miniJava_Not_Expression, gen_miniJava_Neg_Expression, gen_miniJava_MethodCall_Expression, gen_miniJava_StringConstant_Expression, gen_miniJava_IntConstant_Expression, gen_miniJava_FieldAccess_Expression, gen_miniJava_This_Expression, gen_miniJava_Super_Expression, gen_miniJava_Null_Expression, gen_miniJava_NewObject_Expression, gen_miniJava_NewArray_Expression, gen_miniJava_SymbolRef_Expression, gen_miniJava_BoolConstant_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)