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
VisibilityKind: Enumeration = Enumeration(
    name="VisibilityKind",
    literals={
            EnumerationLiteral(name="public"),
			EnumerationLiteral(name="private"),
			EnumerationLiteral(name="protected"),
			EnumerationLiteral(name="none")
    }
)

# Classes
javasimplified_NamedElement = Class(name="javasimplified::NamedElement", is_abstract=True)
javasimplified_Method = Class(name="javasimplified::Method")
NamedElement = Class(name="NamedElement")
javasimplified_Class = Class(name="javasimplified::Class")
javasimplified_Variable = Class(name="javasimplified::Variable")
Statement = Class(name="Statement")
javasimplified_Parameter = Class(name="javasimplified::Parameter")
javasimplified_Type = Class(name="javasimplified::Type")
javasimplified_Modifier = Class(name="javasimplified::Modifier")
javasimplified_Statement = Class(name="javasimplified::Statement", is_abstract=True)
javasimplified_ImportDeclaration = Class(name="javasimplified::ImportDeclaration")
javasimplified_Interface = Class(name="javasimplified::Interface")
javasimplified_Comment = Class(name="javasimplified::Comment")
Type = Class(name="Type")
javasimplified_PrimitiveType = Class(name="javasimplified::PrimitiveType")
javasimplified_Package = Class(name="javasimplified::Package")
javasimplified_Model = Class(name="javasimplified::Model")
javasimplified_IfStatement = Class(name="javasimplified::IfStatement")
javasimplified_WhileStatement = Class(name="javasimplified::WhileStatement")
javasimplified_ForStatement = Class(name="javasimplified::ForStatement")
javasimplified_Expression = Class(name="javasimplified::Expression", is_abstract=True)
javasimplified_ReturnStatement = Class(name="javasimplified::ReturnStatement")
javasimplified_Assignment = Class(name="javasimplified::Assignment")
Expression = Class(name="Expression")
javasimplified_TryStatement = Class(name="javasimplified::TryStatement")
javasimplified_CatchStatment = Class(name="javasimplified::CatchStatment")
javasimplified_ThrowStatement = Class(name="javasimplified::ThrowStatement")
javasimplified_Block = Class(name="javasimplified::Block")
javasimplified_CastExpression = Class(name="javasimplified::CastExpression")
javasimplified_BooleanLiteral = Class(name="javasimplified::BooleanLiteral")
javasimplified_ExpressionStatement = Class(name="javasimplified::ExpressionStatement")
javasimplified_StringLiteral = Class(name="javasimplified::StringLiteral")
javasimplified_ThisExpression = Class(name="javasimplified::ThisExpression")
javasimplified_VariableAccess = Class(name="javasimplified::VariableAccess")
javasimplified_NumberLiteral = Class(name="javasimplified::NumberLiteral")
javasimplified_NullLiteral = Class(name="javasimplified::NullLiteral")
javasimplified_ClassInstanceCreation = Class(name="javasimplified::ClassInstanceCreation")
javasimplified_ArrayAccess = Class(name="javasimplified::ArrayAccess")
javasimplified_InstanceOfExpression = Class(name="javasimplified::InstanceOfExpression")
javasimplified_ArrayCreation = Class(name="javasimplified::ArrayCreation")

# javasimplified_NamedElement class attributes and methods
javasimplified_NamedElement_name: Property = Property(name="name", type=StringType)
javasimplified_NamedElement.attributes={javasimplified_NamedElement_name}

# javasimplified_Method class attributes and methods
javasimplified_Method_visibility: Property = Property(name="visibility", type=StringType)
javasimplified_Method.attributes={javasimplified_Method_visibility}

# NamedElement class attributes and methods

# javasimplified_Class class attributes and methods
javasimplified_Class_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
javasimplified_Class.attributes={javasimplified_Class_isAbstract}

# javasimplified_Variable class attributes and methods
javasimplified_Variable_name: Property = Property(name="name", type=StringType)
javasimplified_Variable.attributes={javasimplified_Variable_name}

# Statement class attributes and methods

# javasimplified_Parameter class attributes and methods

# javasimplified_Type class attributes and methods

# javasimplified_Modifier class attributes and methods
javasimplified_Modifier_visibility: Property = Property(name="visibility", type=StringType)
javasimplified_Modifier_isStatic: Property = Property(name="isStatic", type=BooleanType)
javasimplified_Modifier_isVolatile: Property = Property(name="isVolatile", type=BooleanType)
javasimplified_Modifier_isSynchronized: Property = Property(name="isSynchronized", type=BooleanType)
javasimplified_Modifier_isFinal: Property = Property(name="isFinal", type=BooleanType)
javasimplified_Modifier.attributes={javasimplified_Modifier_visibility, javasimplified_Modifier_isStatic, javasimplified_Modifier_isSynchronized, javasimplified_Modifier_isFinal, javasimplified_Modifier_isVolatile}

# javasimplified_Statement class attributes and methods

# javasimplified_ImportDeclaration class attributes and methods

# javasimplified_Interface class attributes and methods

# javasimplified_Comment class attributes and methods

# Type class attributes and methods

# javasimplified_PrimitiveType class attributes and methods

# javasimplified_Package class attributes and methods

# javasimplified_Model class attributes and methods

# javasimplified_IfStatement class attributes and methods

# javasimplified_WhileStatement class attributes and methods

# javasimplified_ForStatement class attributes and methods

# javasimplified_Expression class attributes and methods

# javasimplified_ReturnStatement class attributes and methods

# javasimplified_Assignment class attributes and methods

# Expression class attributes and methods

# javasimplified_TryStatement class attributes and methods

# javasimplified_CatchStatment class attributes and methods

# javasimplified_ThrowStatement class attributes and methods

# javasimplified_Block class attributes and methods

# javasimplified_CastExpression class attributes and methods

# javasimplified_BooleanLiteral class attributes and methods
javasimplified_BooleanLiteral_value: Property = Property(name="value", type=BooleanType)
javasimplified_BooleanLiteral.attributes={javasimplified_BooleanLiteral_value}

# javasimplified_ExpressionStatement class attributes and methods

# javasimplified_StringLiteral class attributes and methods
javasimplified_StringLiteral_value: Property = Property(name="value", type=StringType)
javasimplified_StringLiteral.attributes={javasimplified_StringLiteral_value}

# javasimplified_ThisExpression class attributes and methods

# javasimplified_VariableAccess class attributes and methods

# javasimplified_NumberLiteral class attributes and methods
javasimplified_NumberLiteral_value: Property = Property(name="value", type=StringType)
javasimplified_NumberLiteral.attributes={javasimplified_NumberLiteral_value}

# javasimplified_NullLiteral class attributes and methods

# javasimplified_ClassInstanceCreation class attributes and methods

# javasimplified_ArrayAccess class attributes and methods

# javasimplified_InstanceOfExpression class attributes and methods

# javasimplified_ArrayCreation class attributes and methods

# Relationships
class0: BinaryAssociation = BinaryAssociation(
    name="class0",
    ends={
        Property(name="javasimplified_Class", type=javasimplified_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_Method", type=javasimplified_Class, multiplicity=Multiplicity(0, 1))
    }
)
type9: BinaryAssociation = BinaryAssociation(
    name="type9",
    ends={
        Property(name="javasimplified_Type10", type=javasimplified_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_Variable", type=javasimplified_Type, multiplicity=Multiplicity(0, 1))
    }
)
class11: BinaryAssociation = BinaryAssociation(
    name="class11",
    ends={
        Property(name="Class", type=javasimplified_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="variables", type=javasimplified_Class, multiplicity=Multiplicity(0, 1))
    }
)
modifier12: BinaryAssociation = BinaryAssociation(
    name="modifier12",
    ends={
        Property(name="javasimplified_Modifier14", type=javasimplified_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_Variable13", type=javasimplified_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
params1: BinaryAssociation = BinaryAssociation(
    name="params1",
    ends={
        Property(name="javasimplified_Parameter", type=javasimplified_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_Method2", type=javasimplified_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType3: BinaryAssociation = BinaryAssociation(
    name="returnType3",
    ends={
        Property(name="javasimplified_Type", type=javasimplified_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_Method4", type=javasimplified_Type, multiplicity=Multiplicity(0, 1))
    }
)
modifier5: BinaryAssociation = BinaryAssociation(
    name="modifier5",
    ends={
        Property(name="javasimplified_Modifier", type=javasimplified_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_Method6", type=javasimplified_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements7: BinaryAssociation = BinaryAssociation(
    name="statements7",
    ends={
        Property(name="javasimplified_Statement", type=javasimplified_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_Method8", type=javasimplified_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass24: BinaryAssociation = BinaryAssociation(
    name="superClass24",
    ends={
        Property(name="javasimplified_Class25", type=javasimplified_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_Class23", type=javasimplified_Class, multiplicity=Multiplicity(0, 1))
    }
)
methods26: BinaryAssociation = BinaryAssociation(
    name="methods26",
    ends={
        Property(name="javasimplified_Method28", type=javasimplified_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_Class27", type=javasimplified_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports29: BinaryAssociation = BinaryAssociation(
    name="imports29",
    ends={
        Property(name="javasimplified_ImportDeclaration", type=javasimplified_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_Class30", type=javasimplified_ImportDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifier31: BinaryAssociation = BinaryAssociation(
    name="modifier31",
    ends={
        Property(name="javasimplified_Modifier33", type=javasimplified_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_Class32", type=javasimplified_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type15: BinaryAssociation = BinaryAssociation(
    name="type15",
    ends={
        Property(name="javasimplified_Type17", type=javasimplified_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_Parameter16", type=javasimplified_Type, multiplicity=Multiplicity(0, 1))
    }
)
class18: BinaryAssociation = BinaryAssociation(
    name="class18",
    ends={
        Property(name="Class19", type=javasimplified_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="comments", type=javasimplified_Class, multiplicity=Multiplicity(1, 1))
    }
)
variables20: BinaryAssociation = BinaryAssociation(
    name="variables20",
    ends={
        Property(name="Variable", type=javasimplified_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class", type=javasimplified_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
comments21: BinaryAssociation = BinaryAssociation(
    name="comments21",
    ends={
        Property(name="Comment", type=javasimplified_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class22", type=javasimplified_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedElement43: BinaryAssociation = BinaryAssociation(
    name="importedElement43",
    ends={
        Property(name="javasimplified_NamedElement", type=javasimplified_ImportDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_ImportDeclaration44", type=javasimplified_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
implements34: BinaryAssociation = BinaryAssociation(
    name="implements34",
    ends={
        Property(name="javasimplified_Interface", type=javasimplified_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_Class35", type=javasimplified_Interface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedElems36: BinaryAssociation = BinaryAssociation(
    name="ownedElems36",
    ends={
        Property(name="javasimplified_Class37", type=javasimplified_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_Package", type=javasimplified_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package39: BinaryAssociation = BinaryAssociation(
    name="package39",
    ends={
        Property(name="javasimplified_Package40", type=javasimplified_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_Package38", type=javasimplified_Package, multiplicity=Multiplicity(0, 1))
    }
)
packs41: BinaryAssociation = BinaryAssociation(
    name="packs41",
    ends={
        Property(name="javasimplified_Package42", type=javasimplified_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_Model", type=javasimplified_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression55: BinaryAssociation = BinaryAssociation(
    name="expression55",
    ends={
        Property(name="javasimplified_Expression56", type=javasimplified_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_IfStatement", type=javasimplified_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body57: BinaryAssociation = BinaryAssociation(
    name="body57",
    ends={
        Property(name="javasimplified_Statement59", type=javasimplified_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_IfStatement58", type=javasimplified_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
else60: BinaryAssociation = BinaryAssociation(
    name="else60",
    ends={
        Property(name="javasimplified_Statement62", type=javasimplified_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_IfStatement61", type=javasimplified_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body63: BinaryAssociation = BinaryAssociation(
    name="body63",
    ends={
        Property(name="javasimplified_Statement64", type=javasimplified_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_WhileStatement", type=javasimplified_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body45: BinaryAssociation = BinaryAssociation(
    name="body45",
    ends={
        Property(name="javasimplified_Statement46", type=javasimplified_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_ForStatement", type=javasimplified_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression47: BinaryAssociation = BinaryAssociation(
    name="expression47",
    ends={
        Property(name="javasimplified_Expression", type=javasimplified_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_ForStatement48", type=javasimplified_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
updaters49: BinaryAssociation = BinaryAssociation(
    name="updaters49",
    ends={
        Property(name="javasimplified_Expression51", type=javasimplified_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_ForStatement50", type=javasimplified_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializers52: BinaryAssociation = BinaryAssociation(
    name="initializers52",
    ends={
        Property(name="javasimplified_Expression54", type=javasimplified_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_ForStatement53", type=javasimplified_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression74: BinaryAssociation = BinaryAssociation(
    name="expression74",
    ends={
        Property(name="javasimplified_Expression75", type=javasimplified_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_ReturnStatement", type=javasimplified_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftHandSide76: BinaryAssociation = BinaryAssociation(
    name="leftHandSide76",
    ends={
        Property(name="javasimplified_Expression77", type=javasimplified_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_Assignment", type=javasimplified_Expression, multiplicity=Multiplicity(1, 1))
    }
)
rightHandSide78: BinaryAssociation = BinaryAssociation(
    name="rightHandSide78",
    ends={
        Property(name="javasimplified_Expression80", type=javasimplified_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_Assignment79", type=javasimplified_Expression, multiplicity=Multiplicity(1, 1))
    }
)
expression65: BinaryAssociation = BinaryAssociation(
    name="expression65",
    ends={
        Property(name="javasimplified_Expression67", type=javasimplified_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_WhileStatement66", type=javasimplified_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body68: BinaryAssociation = BinaryAssociation(
    name="body68",
    ends={
        Property(name="javasimplified_Statement69", type=javasimplified_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_TryStatement", type=javasimplified_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
catchClauses70: BinaryAssociation = BinaryAssociation(
    name="catchClauses70",
    ends={
        Property(name="javasimplified_CatchStatment", type=javasimplified_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_TryStatement71", type=javasimplified_CatchStatment, multiplicity=Multiplicity(0, 9999))
    }
)
expression72: BinaryAssociation = BinaryAssociation(
    name="expression72",
    ends={
        Property(name="javasimplified_Expression73", type=javasimplified_ThrowStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_ThrowStatement", type=javasimplified_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exception86: BinaryAssociation = BinaryAssociation(
    name="exception86",
    ends={
        Property(name="javasimplified_Parameter88", type=javasimplified_CatchStatment, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_CatchStatment87", type=javasimplified_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
statements89: BinaryAssociation = BinaryAssociation(
    name="statements89",
    ends={
        Property(name="javasimplified_Statement90", type=javasimplified_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_Block", type=javasimplified_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression91: BinaryAssociation = BinaryAssociation(
    name="expression91",
    ends={
        Property(name="javasimplified_Expression92", type=javasimplified_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_CastExpression", type=javasimplified_Expression, multiplicity=Multiplicity(1, 1))
    }
)
type93: BinaryAssociation = BinaryAssociation(
    name="type93",
    ends={
        Property(name="javasimplified_Type95", type=javasimplified_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_CastExpression94", type=javasimplified_Type, multiplicity=Multiplicity(1, 1))
    }
)
expression81: BinaryAssociation = BinaryAssociation(
    name="expression81",
    ends={
        Property(name="javasimplified_Expression82", type=javasimplified_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_ExpressionStatement", type=javasimplified_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body83: BinaryAssociation = BinaryAssociation(
    name="body83",
    ends={
        Property(name="javasimplified_Statement85", type=javasimplified_CatchStatment, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_CatchStatment84", type=javasimplified_Statement, multiplicity=Multiplicity(1, 1))
    }
)
expression100: BinaryAssociation = BinaryAssociation(
    name="expression100",
    ends={
        Property(name="javasimplified_Expression102", type=javasimplified_VariableAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_VariableAccess101", type=javasimplified_Expression, multiplicity=Multiplicity(1, 1))
    }
)
type96: BinaryAssociation = BinaryAssociation(
    name="type96",
    ends={
        Property(name="javasimplified_Type97", type=javasimplified_ThisExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_ThisExpression", type=javasimplified_Type, multiplicity=Multiplicity(1, 1))
    }
)
variable98: BinaryAssociation = BinaryAssociation(
    name="variable98",
    ends={
        Property(name="javasimplified_Variable99", type=javasimplified_VariableAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_VariableAccess", type=javasimplified_Variable, multiplicity=Multiplicity(1, 1))
    }
)
expression103: BinaryAssociation = BinaryAssociation(
    name="expression103",
    ends={
        Property(name="javasimplified_Expression104", type=javasimplified_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_ClassInstanceCreation", type=javasimplified_Expression, multiplicity=Multiplicity(1, 1))
    }
)
type105: BinaryAssociation = BinaryAssociation(
    name="type105",
    ends={
        Property(name="javasimplified_Type107", type=javasimplified_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_ClassInstanceCreation106", type=javasimplified_Type, multiplicity=Multiplicity(1, 1))
    }
)
array113: BinaryAssociation = BinaryAssociation(
    name="array113",
    ends={
        Property(name="javasimplified_Expression114", type=javasimplified_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_ArrayAccess", type=javasimplified_Expression, multiplicity=Multiplicity(1, 1))
    }
)
leftOperand108: BinaryAssociation = BinaryAssociation(
    name="leftOperand108",
    ends={
        Property(name="javasimplified_Expression109", type=javasimplified_InstanceOfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_InstanceOfExpression", type=javasimplified_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightOperand110: BinaryAssociation = BinaryAssociation(
    name="rightOperand110",
    ends={
        Property(name="javasimplified_Type112", type=javasimplified_InstanceOfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_InstanceOfExpression111", type=javasimplified_Type, multiplicity=Multiplicity(1, 1))
    }
)
type120: BinaryAssociation = BinaryAssociation(
    name="type120",
    ends={
        Property(name="javasimplified_Type122", type=javasimplified_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_ArrayCreation121", type=javasimplified_Type, multiplicity=Multiplicity(1, 1))
    }
)
initializars123: BinaryAssociation = BinaryAssociation(
    name="initializars123",
    ends={
        Property(name="javasimplified_Expression125", type=javasimplified_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_ArrayCreation124", type=javasimplified_Expression, multiplicity=Multiplicity(0, 9999))
    }
)
index115: BinaryAssociation = BinaryAssociation(
    name="index115",
    ends={
        Property(name="javasimplified_Expression117", type=javasimplified_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_ArrayAccess116", type=javasimplified_Expression, multiplicity=Multiplicity(1, 1))
    }
)
dimensions118: BinaryAssociation = BinaryAssociation(
    name="dimensions118",
    ends={
        Property(name="javasimplified_Expression119", type=javasimplified_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="javasimplified_ArrayCreation", type=javasimplified_Expression, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_javasimplified_Method_NamedElement = Generalization(general=NamedElement, specific=javasimplified_Method)
gen_javasimplified_Variable_Statement = Generalization(general=Statement, specific=javasimplified_Variable)
gen_javasimplified_Parameter_NamedElement = Generalization(general=NamedElement, specific=javasimplified_Parameter)
gen_javasimplified_Class_Type = Generalization(general=Type, specific=javasimplified_Class)
gen_javasimplified_Type_NamedElement = Generalization(general=NamedElement, specific=javasimplified_Type)
gen_javasimplified_PrimitiveType_Type = Generalization(general=Type, specific=javasimplified_PrimitiveType)
gen_javasimplified_Interface_Type = Generalization(general=Type, specific=javasimplified_Interface)
gen_javasimplified_Package_NamedElement = Generalization(general=NamedElement, specific=javasimplified_Package)
gen_javasimplified_Model_NamedElement = Generalization(general=NamedElement, specific=javasimplified_Model)
gen_javasimplified_IfStatement_Statement = Generalization(general=Statement, specific=javasimplified_IfStatement)
gen_javasimplified_WhileStatement_Statement = Generalization(general=Statement, specific=javasimplified_WhileStatement)
gen_javasimplified_ForStatement_Statement = Generalization(general=Statement, specific=javasimplified_ForStatement)
gen_javasimplified_ReturnStatement_Statement = Generalization(general=Statement, specific=javasimplified_ReturnStatement)
gen_javasimplified_Assignment_Expression = Generalization(general=Expression, specific=javasimplified_Assignment)
gen_javasimplified_TryStatement_Statement = Generalization(general=Statement, specific=javasimplified_TryStatement)
gen_javasimplified_ThrowStatement_Statement = Generalization(general=Statement, specific=javasimplified_ThrowStatement)
gen_javasimplified_Block_Statement = Generalization(general=Statement, specific=javasimplified_Block)
gen_javasimplified_CastExpression_Expression = Generalization(general=Expression, specific=javasimplified_CastExpression)
gen_javasimplified_BooleanLiteral_Expression = Generalization(general=Expression, specific=javasimplified_BooleanLiteral)
gen_javasimplified_ExpressionStatement_Statement = Generalization(general=Statement, specific=javasimplified_ExpressionStatement)
gen_javasimplified_CatchStatment_Statement = Generalization(general=Statement, specific=javasimplified_CatchStatment)
gen_javasimplified_StringLiteral_Expression = Generalization(general=Expression, specific=javasimplified_StringLiteral)
gen_javasimplified_ThisExpression_Expression = Generalization(general=Expression, specific=javasimplified_ThisExpression)
gen_javasimplified_VariableAccess_Expression = Generalization(general=Expression, specific=javasimplified_VariableAccess)
gen_javasimplified_NumberLiteral_Expression = Generalization(general=Expression, specific=javasimplified_NumberLiteral)
gen_javasimplified_NullLiteral_Expression = Generalization(general=Expression, specific=javasimplified_NullLiteral)
gen_javasimplified_ClassInstanceCreation_Expression = Generalization(general=Expression, specific=javasimplified_ClassInstanceCreation)
gen_javasimplified_ArrayAccess_Expression = Generalization(general=Expression, specific=javasimplified_ArrayAccess)
gen_javasimplified_InstanceOfExpression_Expression = Generalization(general=Expression, specific=javasimplified_InstanceOfExpression)
gen_javasimplified_ArrayCreation_Expression = Generalization(general=Expression, specific=javasimplified_ArrayCreation)

# Domain Model
domain_model = DomainModel(
    name="javasimplified",
    types={javasimplified_NamedElement, javasimplified_Method, NamedElement, javasimplified_Class, javasimplified_Variable, Statement, javasimplified_Parameter, javasimplified_Type, javasimplified_Modifier, javasimplified_Statement, javasimplified_ImportDeclaration, javasimplified_Interface, javasimplified_Comment, Type, javasimplified_PrimitiveType, javasimplified_Package, javasimplified_Model, javasimplified_IfStatement, javasimplified_WhileStatement, javasimplified_ForStatement, javasimplified_Expression, javasimplified_ReturnStatement, javasimplified_Assignment, Expression, javasimplified_TryStatement, javasimplified_CatchStatment, javasimplified_ThrowStatement, javasimplified_Block, javasimplified_CastExpression, javasimplified_BooleanLiteral, javasimplified_ExpressionStatement, javasimplified_StringLiteral, javasimplified_ThisExpression, javasimplified_VariableAccess, javasimplified_NumberLiteral, javasimplified_NullLiteral, javasimplified_ClassInstanceCreation, javasimplified_ArrayAccess, javasimplified_InstanceOfExpression, javasimplified_ArrayCreation, VisibilityKind},
    associations={class0, type9, class11, modifier12, params1, returnType3, modifier5, statements7, superClass24, methods26, imports29, modifier31, type15, class18, variables20, comments21, importedElement43, implements34, ownedElems36, package39, packs41, expression55, body57, else60, body63, body45, expression47, updaters49, initializers52, expression74, leftHandSide76, rightHandSide78, expression65, body68, catchClauses70, expression72, exception86, statements89, expression91, type93, expression81, body83, expression100, type96, variable98, expression103, type105, array113, leftOperand108, rightOperand110, type120, initializars123, index115, dimensions118},
    generalizations={gen_javasimplified_Method_NamedElement, gen_javasimplified_Variable_Statement, gen_javasimplified_Parameter_NamedElement, gen_javasimplified_Class_Type, gen_javasimplified_Type_NamedElement, gen_javasimplified_PrimitiveType_Type, gen_javasimplified_Interface_Type, gen_javasimplified_Package_NamedElement, gen_javasimplified_Model_NamedElement, gen_javasimplified_IfStatement_Statement, gen_javasimplified_WhileStatement_Statement, gen_javasimplified_ForStatement_Statement, gen_javasimplified_ReturnStatement_Statement, gen_javasimplified_Assignment_Expression, gen_javasimplified_TryStatement_Statement, gen_javasimplified_ThrowStatement_Statement, gen_javasimplified_Block_Statement, gen_javasimplified_CastExpression_Expression, gen_javasimplified_BooleanLiteral_Expression, gen_javasimplified_ExpressionStatement_Statement, gen_javasimplified_CatchStatment_Statement, gen_javasimplified_StringLiteral_Expression, gen_javasimplified_ThisExpression_Expression, gen_javasimplified_VariableAccess_Expression, gen_javasimplified_NumberLiteral_Expression, gen_javasimplified_NullLiteral_Expression, gen_javasimplified_ClassInstanceCreation_Expression, gen_javasimplified_ArrayAccess_Expression, gen_javasimplified_InstanceOfExpression_Expression, gen_javasimplified_ArrayCreation_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)