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
BSPrimitiveType: Enumeration = Enumeration(
    name="BSPrimitiveType",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="STRING"),
			EnumerationLiteral(name="TAGGED_STRING"),
			EnumerationLiteral(name="NUMBER"),
			EnumerationLiteral(name="OBJECT"),
			EnumerationLiteral(name="VOID")
    }
)

# Classes
blorqueScript_BSMember = Class(name="blorqueScript::BSMember")
blorqueScript_BSFile = Class(name="blorqueScript::BSFile")
blorqueScript_BSImport = Class(name="blorqueScript::BSImport")
blorqueScript_BSClass = Class(name="blorqueScript::BSClass")
blorqueScript_BSReturn = Class(name="blorqueScript::BSReturn")
BSStatement = Class(name="BSStatement")
BSSymbol = Class(name="BSSymbol")
blorqueScript_BSField = Class(name="blorqueScript::BSField")
BSMember = Class(name="BSMember")
blorqueScript_BSMethod = Class(name="blorqueScript::BSMethod")
blorqueScript_BSParameter = Class(name="blorqueScript::BSParameter")
blorqueScript_BSMethodBody = Class(name="blorqueScript::BSMethodBody")
BSBlock = Class(name="BSBlock")
blorqueScript_BSStatement = Class(name="blorqueScript::BSStatement")
blorqueScript_BSWhileLoop = Class(name="blorqueScript::BSWhileLoop")
blorqueScript_BSExpression = Class(name="blorqueScript::BSExpression")
blorqueScript_BSBreak = Class(name="blorqueScript::BSBreak")
blorqueScript_BSContinue = Class(name="blorqueScript::BSContinue")
blorqueScript_BSVariableDeclaration = Class(name="blorqueScript::BSVariableDeclaration")
blorqueScript_BSIfStatement = Class(name="blorqueScript::BSIfStatement")
blorqueScript_BSIfBlock = Class(name="blorqueScript::BSIfBlock")
blorqueScript_BSSwitchBlock = Class(name="blorqueScript::BSSwitchBlock")
blorqueScript_BSLoopBlock = Class(name="blorqueScript::BSLoopBlock")
blorqueScript_BSForLoop = Class(name="blorqueScript::BSForLoop")
blorqueScript_BSSwitchStatement = Class(name="blorqueScript::BSSwitchStatement")
blorqueScript_BSCase = Class(name="blorqueScript::BSCase")
blorqueScript_BSCaseBlock = Class(name="blorqueScript::BSCaseBlock")
blorqueScript_BSBlock = Class(name="blorqueScript::BSBlock")
blorqueScript_BSSymbol = Class(name="blorqueScript::BSSymbol")
blorqueScript_BSAssignmentExpression = Class(name="blorqueScript::BSAssignmentExpression")
BSExpression = Class(name="BSExpression")
blorqueScript_BSBooleanAndExpression = Class(name="blorqueScript::BSBooleanAndExpression")
blorqueScript_BSTernaryExpression = Class(name="blorqueScript::BSTernaryExpression")
blorqueScript_BSBooleanOrExpression = Class(name="blorqueScript::BSBooleanOrExpression")
blorqueScript_BSBitwiseAndExpression = Class(name="blorqueScript::BSBitwiseAndExpression")
blorqueScript_BSBitwiseOrExpression = Class(name="blorqueScript::BSBitwiseOrExpression")
blorqueScript_BSBitwiseXorExpression = Class(name="blorqueScript::BSBitwiseXorExpression")
blorqueScript_BSEqualityExpression = Class(name="blorqueScript::BSEqualityExpression")
blorqueScript_BSOrderedRelationExpression = Class(name="blorqueScript::BSOrderedRelationExpression")
blorqueScript_BSBitwiseShiftExpression = Class(name="blorqueScript::BSBitwiseShiftExpression")
blorqueScript_BSPlusMinusOrStringConcatExpression = Class(name="blorqueScript::BSPlusMinusOrStringConcatExpression")
blorqueScript_BSMulDivOrModExpression = Class(name="blorqueScript::BSMulDivOrModExpression")
blorqueScript_BSCastExpression = Class(name="blorqueScript::BSCastExpression")
blorqueScript_BSNewExpression = Class(name="blorqueScript::BSNewExpression")
blorqueScript_BSUnaryModifierExpression = Class(name="blorqueScript::BSUnaryModifierExpression")
blorqueScript_BSMemberSelectionExpression = Class(name="blorqueScript::BSMemberSelectionExpression")
blorqueScript_BSMethodInvokationExpression = Class(name="blorqueScript::BSMethodInvokationExpression")
blorqueScript_BSStringConstant = Class(name="blorqueScript::BSStringConstant")
blorqueScript_BSArrayAccessExpression = Class(name="blorqueScript::BSArrayAccessExpression")
blorqueScript_BSPostfixArithmeticExpression = Class(name="blorqueScript::BSPostfixArithmeticExpression")
blorqueScript_BSSymbolRef = Class(name="blorqueScript::BSSymbolRef")
blorqueScript_BSHexadecimalConstant = Class(name="blorqueScript::BSHexadecimalConstant")
blorqueScript_BSNumberConstant = Class(name="blorqueScript::BSNumberConstant")
blorqueScript_BSRealConstant = Class(name="blorqueScript::BSRealConstant")
blorqueScript_BSBooleanConstant = Class(name="blorqueScript::BSBooleanConstant")
blorqueScript_BSNullLiteral = Class(name="blorqueScript::BSNullLiteral")
blorqueScript_BSThisLiteral = Class(name="blorqueScript::BSThisLiteral")
blorqueScript_BSClientLiteral = Class(name="blorqueScript::BSClientLiteral")
blorqueScript_BSParentLiteral = Class(name="blorqueScript::BSParentLiteral")
blorqueScript_BSParentheticalExpression = Class(name="blorqueScript::BSParentheticalExpression")

# blorqueScript_BSMember class attributes and methods
blorqueScript_BSMember_isArray: Property = Property(name="isArray", type=BooleanType)
blorqueScript_BSMember.attributes={blorqueScript_BSMember_isArray}

# blorqueScript_BSFile class attributes and methods
blorqueScript_BSFile_name: Property = Property(name="name", type=StringType)
blorqueScript_BSFile.attributes={blorqueScript_BSFile_name}

# blorqueScript_BSImport class attributes and methods
blorqueScript_BSImport_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
blorqueScript_BSImport.attributes={blorqueScript_BSImport_importedNamespace}

# blorqueScript_BSClass class attributes and methods
blorqueScript_BSClass_name: Property = Property(name="name", type=StringType)
blorqueScript_BSClass.attributes={blorqueScript_BSClass_name}

# blorqueScript_BSReturn class attributes and methods

# BSStatement class attributes and methods

# BSSymbol class attributes and methods

# blorqueScript_BSField class attributes and methods

# BSMember class attributes and methods

# blorqueScript_BSMethod class attributes and methods

# blorqueScript_BSParameter class attributes and methods
blorqueScript_BSParameter_isArray: Property = Property(name="isArray", type=BooleanType)
blorqueScript_BSParameter.attributes={blorqueScript_BSParameter_isArray}

# blorqueScript_BSMethodBody class attributes and methods

# BSBlock class attributes and methods

# blorqueScript_BSStatement class attributes and methods

# blorqueScript_BSWhileLoop class attributes and methods

# blorqueScript_BSExpression class attributes and methods

# blorqueScript_BSBreak class attributes and methods

# blorqueScript_BSContinue class attributes and methods

# blorqueScript_BSVariableDeclaration class attributes and methods

# blorqueScript_BSIfStatement class attributes and methods

# blorqueScript_BSIfBlock class attributes and methods

# blorqueScript_BSSwitchBlock class attributes and methods

# blorqueScript_BSLoopBlock class attributes and methods

# blorqueScript_BSForLoop class attributes and methods

# blorqueScript_BSSwitchStatement class attributes and methods
blorqueScript_BSSwitchStatement_stringSwitch: Property = Property(name="stringSwitch", type=BooleanType)
blorqueScript_BSSwitchStatement.attributes={blorqueScript_BSSwitchStatement_stringSwitch}

# blorqueScript_BSCase class attributes and methods

# blorqueScript_BSCaseBlock class attributes and methods

# blorqueScript_BSBlock class attributes and methods

# blorqueScript_BSSymbol class attributes and methods
blorqueScript_BSSymbol_pType: Property = Property(name="pType", type=StringType)
blorqueScript_BSSymbol_name: Property = Property(name="name", type=StringType)
blorqueScript_BSSymbol.attributes={blorqueScript_BSSymbol_pType, blorqueScript_BSSymbol_name}

# blorqueScript_BSAssignmentExpression class attributes and methods
blorqueScript_BSAssignmentExpression_assignmentOperator: Property = Property(name="assignmentOperator", type=StringType)
blorqueScript_BSAssignmentExpression.attributes={blorqueScript_BSAssignmentExpression_assignmentOperator}

# BSExpression class attributes and methods

# blorqueScript_BSBooleanAndExpression class attributes and methods

# blorqueScript_BSTernaryExpression class attributes and methods

# blorqueScript_BSBooleanOrExpression class attributes and methods

# blorqueScript_BSBitwiseAndExpression class attributes and methods

# blorqueScript_BSBitwiseOrExpression class attributes and methods

# blorqueScript_BSBitwiseXorExpression class attributes and methods

# blorqueScript_BSEqualityExpression class attributes and methods
blorqueScript_BSEqualityExpression_operator: Property = Property(name="operator", type=StringType)
blorqueScript_BSEqualityExpression.attributes={blorqueScript_BSEqualityExpression_operator}

# blorqueScript_BSOrderedRelationExpression class attributes and methods
blorqueScript_BSOrderedRelationExpression_operator: Property = Property(name="operator", type=StringType)
blorqueScript_BSOrderedRelationExpression.attributes={blorqueScript_BSOrderedRelationExpression_operator}

# blorqueScript_BSBitwiseShiftExpression class attributes and methods
blorqueScript_BSBitwiseShiftExpression_operator: Property = Property(name="operator", type=StringType)
blorqueScript_BSBitwiseShiftExpression.attributes={blorqueScript_BSBitwiseShiftExpression_operator}

# blorqueScript_BSPlusMinusOrStringConcatExpression class attributes and methods
blorqueScript_BSPlusMinusOrStringConcatExpression_operator: Property = Property(name="operator", type=StringType)
blorqueScript_BSPlusMinusOrStringConcatExpression.attributes={blorqueScript_BSPlusMinusOrStringConcatExpression_operator}

# blorqueScript_BSMulDivOrModExpression class attributes and methods
blorqueScript_BSMulDivOrModExpression_operator: Property = Property(name="operator", type=StringType)
blorqueScript_BSMulDivOrModExpression.attributes={blorqueScript_BSMulDivOrModExpression_operator}

# blorqueScript_BSCastExpression class attributes and methods
blorqueScript_BSCastExpression_pType: Property = Property(name="pType", type=StringType)
blorqueScript_BSCastExpression_isArray: Property = Property(name="isArray", type=BooleanType)
blorqueScript_BSCastExpression.attributes={blorqueScript_BSCastExpression_isArray, blorqueScript_BSCastExpression_pType}

# blorqueScript_BSNewExpression class attributes and methods
blorqueScript_BSNewExpression_isArray: Property = Property(name="isArray", type=BooleanType)
blorqueScript_BSNewExpression.attributes={blorqueScript_BSNewExpression_isArray}

# blorqueScript_BSUnaryModifierExpression class attributes and methods
blorqueScript_BSUnaryModifierExpression_operator: Property = Property(name="operator", type=StringType)
blorqueScript_BSUnaryModifierExpression.attributes={blorqueScript_BSUnaryModifierExpression_operator}

# blorqueScript_BSMemberSelectionExpression class attributes and methods

# blorqueScript_BSMethodInvokationExpression class attributes and methods

# blorqueScript_BSStringConstant class attributes and methods
blorqueScript_BSStringConstant_value: Property = Property(name="value", type=StringType)
blorqueScript_BSStringConstant.attributes={blorqueScript_BSStringConstant_value}

# blorqueScript_BSArrayAccessExpression class attributes and methods

# blorqueScript_BSPostfixArithmeticExpression class attributes and methods
blorqueScript_BSPostfixArithmeticExpression_operator: Property = Property(name="operator", type=StringType)
blorqueScript_BSPostfixArithmeticExpression.attributes={blorqueScript_BSPostfixArithmeticExpression_operator}

# blorqueScript_BSSymbolRef class attributes and methods

# blorqueScript_BSHexadecimalConstant class attributes and methods
blorqueScript_BSHexadecimalConstant_value: Property = Property(name="value", type=StringType)
blorqueScript_BSHexadecimalConstant.attributes={blorqueScript_BSHexadecimalConstant_value}

# blorqueScript_BSNumberConstant class attributes and methods
blorqueScript_BSNumberConstant_value: Property = Property(name="value", type=IntegerType)
blorqueScript_BSNumberConstant.attributes={blorqueScript_BSNumberConstant_value}

# blorqueScript_BSRealConstant class attributes and methods
blorqueScript_BSRealConstant_right: Property = Property(name="right", type=IntegerType)
blorqueScript_BSRealConstant.attributes={blorqueScript_BSRealConstant_right}

# blorqueScript_BSBooleanConstant class attributes and methods
blorqueScript_BSBooleanConstant_value: Property = Property(name="value", type=StringType)
blorqueScript_BSBooleanConstant.attributes={blorqueScript_BSBooleanConstant_value}

# blorqueScript_BSNullLiteral class attributes and methods

# blorqueScript_BSThisLiteral class attributes and methods

# blorqueScript_BSClientLiteral class attributes and methods

# blorqueScript_BSParentLiteral class attributes and methods

# blorqueScript_BSParentheticalExpression class attributes and methods

# Relationships
members6: BinaryAssociation = BinaryAssociation(
    name="members6",
    ends={
        Property(name="blorqueScript_BSMember", type=blorqueScript_BSClass, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSClass7", type=blorqueScript_BSMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="blorqueScript_BSImport", type=blorqueScript_BSFile, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSFile", type=blorqueScript_BSImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classes1: BinaryAssociation = BinaryAssociation(
    name="classes1",
    ends={
        Property(name="blorqueScript_BSClass", type=blorqueScript_BSFile, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSFile2", type=blorqueScript_BSClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superclass4: BinaryAssociation = BinaryAssociation(
    name="superclass4",
    ends={
        Property(name="blorqueScript_BSClass5", type=blorqueScript_BSClass, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSClass3", type=blorqueScript_BSClass, multiplicity=Multiplicity(0, 1))
    }
)
statements11: BinaryAssociation = BinaryAssociation(
    name="statements11",
    ends={
        Property(name="blorqueScript_BSStatement", type=blorqueScript_BSMethodBody, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSMethodBody12", type=blorqueScript_BSStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
params8: BinaryAssociation = BinaryAssociation(
    name="params8",
    ends={
        Property(name="blorqueScript_BSParameter", type=blorqueScript_BSMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSMethod", type=blorqueScript_BSParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body9: BinaryAssociation = BinaryAssociation(
    name="body9",
    ends={
        Property(name="blorqueScript_BSMethodBody", type=blorqueScript_BSMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSMethod10", type=blorqueScript_BSMethodBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseBlock20: BinaryAssociation = BinaryAssociation(
    name="elseBlock20",
    ends={
        Property(name="blorqueScript_BSIfStatement21", type=blorqueScript_BSIfBlock, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="blorqueScript_BSIfBlock22", type=blorqueScript_BSIfStatement, multiplicity=Multiplicity(1, 1))
    }
)
expression13: BinaryAssociation = BinaryAssociation(
    name="expression13",
    ends={
        Property(name="blorqueScript_BSExpression", type=blorqueScript_BSReturn, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSReturn", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression14: BinaryAssociation = BinaryAssociation(
    name="expression14",
    ends={
        Property(name="blorqueScript_BSExpression15", type=blorqueScript_BSVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSVariableDeclaration", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression16: BinaryAssociation = BinaryAssociation(
    name="expression16",
    ends={
        Property(name="blorqueScript_BSExpression17", type=blorqueScript_BSIfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSIfStatement", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenBlock18: BinaryAssociation = BinaryAssociation(
    name="thenBlock18",
    ends={
        Property(name="blorqueScript_BSIfBlock", type=blorqueScript_BSIfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSIfStatement19", type=blorqueScript_BSIfBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression38: BinaryAssociation = BinaryAssociation(
    name="expression38",
    ends={
        Property(name="blorqueScript_BSExpression39", type=blorqueScript_BSSwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSSwitchStatement", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression23: BinaryAssociation = BinaryAssociation(
    name="expression23",
    ends={
        Property(name="blorqueScript_BSExpression24", type=blorqueScript_BSWhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSWhileLoop", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block25: BinaryAssociation = BinaryAssociation(
    name="block25",
    ends={
        Property(name="blorqueScript_BSLoopBlock", type=blorqueScript_BSWhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSWhileLoop26", type=blorqueScript_BSLoopBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left27: BinaryAssociation = BinaryAssociation(
    name="left27",
    ends={
        Property(name="blorqueScript_BSExpression28", type=blorqueScript_BSForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSForLoop", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
middle29: BinaryAssociation = BinaryAssociation(
    name="middle29",
    ends={
        Property(name="blorqueScript_BSExpression31", type=blorqueScript_BSForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSForLoop30", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right32: BinaryAssociation = BinaryAssociation(
    name="right32",
    ends={
        Property(name="blorqueScript_BSExpression34", type=blorqueScript_BSForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSForLoop33", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block35: BinaryAssociation = BinaryAssociation(
    name="block35",
    ends={
        Property(name="blorqueScript_BSLoopBlock37", type=blorqueScript_BSForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSForLoop36", type=blorqueScript_BSLoopBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block53: BinaryAssociation = BinaryAssociation(
    name="block53",
    ends={
        Property(name="blorqueScript_BSCase54", type=blorqueScript_BSCaseBlock, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="blorqueScript_BSCaseBlock", type=blorqueScript_BSCase, multiplicity=Multiplicity(1, 1))
    }
)
block40: BinaryAssociation = BinaryAssociation(
    name="block40",
    ends={
        Property(name="blorqueScript_BSSwitchBlock", type=blorqueScript_BSSwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSSwitchStatement41", type=blorqueScript_BSSwitchBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements42: BinaryAssociation = BinaryAssociation(
    name="statements42",
    ends={
        Property(name="blorqueScript_BSStatement44", type=blorqueScript_BSIfBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSIfBlock43", type=blorqueScript_BSStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements45: BinaryAssociation = BinaryAssociation(
    name="statements45",
    ends={
        Property(name="blorqueScript_BSStatement47", type=blorqueScript_BSLoopBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSLoopBlock46", type=blorqueScript_BSStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cases48: BinaryAssociation = BinaryAssociation(
    name="cases48",
    ends={
        Property(name="blorqueScript_BSCase", type=blorqueScript_BSSwitchBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSSwitchBlock49", type=blorqueScript_BSCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression50: BinaryAssociation = BinaryAssociation(
    name="expression50",
    ends={
        Property(name="blorqueScript_BSExpression52", type=blorqueScript_BSCase, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSCase51", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left60: BinaryAssociation = BinaryAssociation(
    name="left60",
    ends={
        Property(name="blorqueScript_BSExpression61", type=blorqueScript_BSAssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSAssignmentExpression", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements55: BinaryAssociation = BinaryAssociation(
    name="statements55",
    ends={
        Property(name="blorqueScript_BSStatement57", type=blorqueScript_BSCaseBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSCaseBlock56", type=blorqueScript_BSStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rType58: BinaryAssociation = BinaryAssociation(
    name="rType58",
    ends={
        Property(name="blorqueScript_BSClass59", type=blorqueScript_BSSymbol, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSSymbol", type=blorqueScript_BSClass, multiplicity=Multiplicity(0, 1))
    }
)
left78: BinaryAssociation = BinaryAssociation(
    name="left78",
    ends={
        Property(name="blorqueScript_BSExpression79", type=blorqueScript_BSBooleanAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSBooleanAndExpression", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right62: BinaryAssociation = BinaryAssociation(
    name="right62",
    ends={
        Property(name="blorqueScript_BSExpression64", type=blorqueScript_BSAssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSAssignmentExpression63", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left65: BinaryAssociation = BinaryAssociation(
    name="left65",
    ends={
        Property(name="blorqueScript_BSExpression66", type=blorqueScript_BSTernaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSTernaryExpression", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
middle67: BinaryAssociation = BinaryAssociation(
    name="middle67",
    ends={
        Property(name="blorqueScript_BSExpression69", type=blorqueScript_BSTernaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSTernaryExpression68", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right70: BinaryAssociation = BinaryAssociation(
    name="right70",
    ends={
        Property(name="blorqueScript_BSExpression72", type=blorqueScript_BSTernaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSTernaryExpression71", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left73: BinaryAssociation = BinaryAssociation(
    name="left73",
    ends={
        Property(name="blorqueScript_BSExpression74", type=blorqueScript_BSBooleanOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSBooleanOrExpression", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right75: BinaryAssociation = BinaryAssociation(
    name="right75",
    ends={
        Property(name="blorqueScript_BSExpression77", type=blorqueScript_BSBooleanOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSBooleanOrExpression76", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left93: BinaryAssociation = BinaryAssociation(
    name="left93",
    ends={
        Property(name="blorqueScript_BSExpression94", type=blorqueScript_BSBitwiseAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSBitwiseAndExpression", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right80: BinaryAssociation = BinaryAssociation(
    name="right80",
    ends={
        Property(name="blorqueScript_BSExpression82", type=blorqueScript_BSBooleanAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSBooleanAndExpression81", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left83: BinaryAssociation = BinaryAssociation(
    name="left83",
    ends={
        Property(name="blorqueScript_BSExpression84", type=blorqueScript_BSBitwiseOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSBitwiseOrExpression", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right85: BinaryAssociation = BinaryAssociation(
    name="right85",
    ends={
        Property(name="blorqueScript_BSExpression87", type=blorqueScript_BSBitwiseOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSBitwiseOrExpression86", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left88: BinaryAssociation = BinaryAssociation(
    name="left88",
    ends={
        Property(name="blorqueScript_BSExpression89", type=blorqueScript_BSBitwiseXorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSBitwiseXorExpression", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right90: BinaryAssociation = BinaryAssociation(
    name="right90",
    ends={
        Property(name="blorqueScript_BSExpression92", type=blorqueScript_BSBitwiseXorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSBitwiseXorExpression91", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left103: BinaryAssociation = BinaryAssociation(
    name="left103",
    ends={
        Property(name="blorqueScript_BSOrderedRelationExpression", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="blorqueScript_BSExpression104", type=blorqueScript_BSOrderedRelationExpression, multiplicity=Multiplicity(1, 1))
    }
)
right95: BinaryAssociation = BinaryAssociation(
    name="right95",
    ends={
        Property(name="blorqueScript_BSExpression97", type=blorqueScript_BSBitwiseAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSBitwiseAndExpression96", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left98: BinaryAssociation = BinaryAssociation(
    name="left98",
    ends={
        Property(name="blorqueScript_BSExpression99", type=blorqueScript_BSEqualityExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSEqualityExpression", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right100: BinaryAssociation = BinaryAssociation(
    name="right100",
    ends={
        Property(name="blorqueScript_BSExpression102", type=blorqueScript_BSEqualityExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSEqualityExpression101", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right115: BinaryAssociation = BinaryAssociation(
    name="right115",
    ends={
        Property(name="blorqueScript_BSExpression117", type=blorqueScript_BSPlusMinusOrStringConcatExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSPlusMinusOrStringConcatExpression116", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right105: BinaryAssociation = BinaryAssociation(
    name="right105",
    ends={
        Property(name="blorqueScript_BSExpression107", type=blorqueScript_BSOrderedRelationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSOrderedRelationExpression106", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left108: BinaryAssociation = BinaryAssociation(
    name="left108",
    ends={
        Property(name="blorqueScript_BSExpression109", type=blorqueScript_BSBitwiseShiftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSBitwiseShiftExpression", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right110: BinaryAssociation = BinaryAssociation(
    name="right110",
    ends={
        Property(name="blorqueScript_BSExpression112", type=blorqueScript_BSBitwiseShiftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSBitwiseShiftExpression111", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left113: BinaryAssociation = BinaryAssociation(
    name="left113",
    ends={
        Property(name="blorqueScript_BSExpression114", type=blorqueScript_BSPlusMinusOrStringConcatExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSPlusMinusOrStringConcatExpression", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args127: BinaryAssociation = BinaryAssociation(
    name="args127",
    ends={
        Property(name="blorqueScript_BSExpression129", type=blorqueScript_BSNewExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSNewExpression128", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left118: BinaryAssociation = BinaryAssociation(
    name="left118",
    ends={
        Property(name="blorqueScript_BSExpression119", type=blorqueScript_BSMulDivOrModExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSMulDivOrModExpression", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right120: BinaryAssociation = BinaryAssociation(
    name="right120",
    ends={
        Property(name="blorqueScript_BSExpression122", type=blorqueScript_BSMulDivOrModExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSMulDivOrModExpression121", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
castExpr123: BinaryAssociation = BinaryAssociation(
    name="castExpr123",
    ends={
        Property(name="blorqueScript_BSExpression124", type=blorqueScript_BSCastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSCastExpression", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rType125: BinaryAssociation = BinaryAssociation(
    name="rType125",
    ends={
        Property(name="blorqueScript_BSClass126", type=blorqueScript_BSNewExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSNewExpression", type=blorqueScript_BSClass, multiplicity=Multiplicity(0, 1))
    }
)
receiver137: BinaryAssociation = BinaryAssociation(
    name="receiver137",
    ends={
        Property(name="blorqueScript_BSExpression138", type=blorqueScript_BSMethodInvokationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSMethodInvokationExpression", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
receiver130: BinaryAssociation = BinaryAssociation(
    name="receiver130",
    ends={
        Property(name="blorqueScript_BSExpression131", type=blorqueScript_BSUnaryModifierExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSUnaryModifierExpression", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
receiver132: BinaryAssociation = BinaryAssociation(
    name="receiver132",
    ends={
        Property(name="blorqueScript_BSExpression133", type=blorqueScript_BSMemberSelectionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSMemberSelectionExpression", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
member134: BinaryAssociation = BinaryAssociation(
    name="member134",
    ends={
        Property(name="blorqueScript_BSExpression136", type=blorqueScript_BSMemberSelectionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSMemberSelectionExpression135", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args139: BinaryAssociation = BinaryAssociation(
    name="args139",
    ends={
        Property(name="blorqueScript_BSExpression141", type=blorqueScript_BSMethodInvokationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSMethodInvokationExpression140", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
receiver142: BinaryAssociation = BinaryAssociation(
    name="receiver142",
    ends={
        Property(name="blorqueScript_BSExpression143", type=blorqueScript_BSArrayAccessExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSArrayAccessExpression", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args144: BinaryAssociation = BinaryAssociation(
    name="args144",
    ends={
        Property(name="blorqueScript_BSExpression146", type=blorqueScript_BSArrayAccessExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSArrayAccessExpression145", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
receiver147: BinaryAssociation = BinaryAssociation(
    name="receiver147",
    ends={
        Property(name="blorqueScript_BSExpression148", type=blorqueScript_BSPostfixArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSPostfixArithmeticExpression", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
symbol150: BinaryAssociation = BinaryAssociation(
    name="symbol150",
    ends={
        Property(name="blorqueScript_BSSymbol151", type=blorqueScript_BSSymbolRef, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSSymbolRef", type=blorqueScript_BSSymbol, multiplicity=Multiplicity(0, 1))
    }
)
left149: BinaryAssociation = BinaryAssociation(
    name="left149",
    ends={
        Property(name="blorqueScript_BSNumberConstant", type=blorqueScript_BSRealConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSRealConstant", type=blorqueScript_BSNumberConstant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression152: BinaryAssociation = BinaryAssociation(
    name="expression152",
    ends={
        Property(name="blorqueScript_BSExpression153", type=blorqueScript_BSParentheticalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="blorqueScript_BSParentheticalExpression", type=blorqueScript_BSExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_blorqueScript_BSReturn_BSStatement = Generalization(general=BSStatement, specific=blorqueScript_BSReturn)
gen_blorqueScript_BSMember_BSSymbol = Generalization(general=BSSymbol, specific=blorqueScript_BSMember)
gen_blorqueScript_BSField_BSMember = Generalization(general=BSMember, specific=blorqueScript_BSField)
gen_blorqueScript_BSMethod_BSMember = Generalization(general=BSMember, specific=blorqueScript_BSMethod)
gen_blorqueScript_BSParameter_BSSymbol = Generalization(general=BSSymbol, specific=blorqueScript_BSParameter)
gen_blorqueScript_BSMethodBody_BSBlock = Generalization(general=BSBlock, specific=blorqueScript_BSMethodBody)
gen_blorqueScript_BSWhileLoop_BSStatement = Generalization(general=BSStatement, specific=blorqueScript_BSWhileLoop)
gen_blorqueScript_BSBreak_BSStatement = Generalization(general=BSStatement, specific=blorqueScript_BSBreak)
gen_blorqueScript_BSContinue_BSStatement = Generalization(general=BSStatement, specific=blorqueScript_BSContinue)
gen_blorqueScript_BSVariableDeclaration_BSStatement = Generalization(general=BSStatement, specific=blorqueScript_BSVariableDeclaration)
gen_blorqueScript_BSVariableDeclaration_BSSymbol = Generalization(general=BSSymbol, specific=blorqueScript_BSVariableDeclaration)
gen_blorqueScript_BSIfStatement_BSStatement = Generalization(general=BSStatement, specific=blorqueScript_BSIfStatement)
gen_blorqueScript_BSForLoop_BSStatement = Generalization(general=BSStatement, specific=blorqueScript_BSForLoop)
gen_blorqueScript_BSSwitchStatement_BSStatement = Generalization(general=BSStatement, specific=blorqueScript_BSSwitchStatement)
gen_blorqueScript_BSCaseBlock_BSBlock = Generalization(general=BSBlock, specific=blorqueScript_BSCaseBlock)
gen_blorqueScript_BSIfBlock_BSBlock = Generalization(general=BSBlock, specific=blorqueScript_BSIfBlock)
gen_blorqueScript_BSLoopBlock_BSBlock = Generalization(general=BSBlock, specific=blorqueScript_BSLoopBlock)
gen_blorqueScript_BSSwitchBlock_BSBlock = Generalization(general=BSBlock, specific=blorqueScript_BSSwitchBlock)
gen_blorqueScript_BSExpression_BSStatement = Generalization(general=BSStatement, specific=blorqueScript_BSExpression)
gen_blorqueScript_BSAssignmentExpression_BSExpression = Generalization(general=BSExpression, specific=blorqueScript_BSAssignmentExpression)
gen_blorqueScript_BSBooleanAndExpression_BSExpression = Generalization(general=BSExpression, specific=blorqueScript_BSBooleanAndExpression)
gen_blorqueScript_BSTernaryExpression_BSExpression = Generalization(general=BSExpression, specific=blorqueScript_BSTernaryExpression)
gen_blorqueScript_BSBooleanOrExpression_BSExpression = Generalization(general=BSExpression, specific=blorqueScript_BSBooleanOrExpression)
gen_blorqueScript_BSBitwiseAndExpression_BSExpression = Generalization(general=BSExpression, specific=blorqueScript_BSBitwiseAndExpression)
gen_blorqueScript_BSBitwiseOrExpression_BSExpression = Generalization(general=BSExpression, specific=blorqueScript_BSBitwiseOrExpression)
gen_blorqueScript_BSBitwiseXorExpression_BSExpression = Generalization(general=BSExpression, specific=blorqueScript_BSBitwiseXorExpression)
gen_blorqueScript_BSEqualityExpression_BSExpression = Generalization(general=BSExpression, specific=blorqueScript_BSEqualityExpression)
gen_blorqueScript_BSOrderedRelationExpression_BSExpression = Generalization(general=BSExpression, specific=blorqueScript_BSOrderedRelationExpression)
gen_blorqueScript_BSBitwiseShiftExpression_BSExpression = Generalization(general=BSExpression, specific=blorqueScript_BSBitwiseShiftExpression)
gen_blorqueScript_BSPlusMinusOrStringConcatExpression_BSExpression = Generalization(general=BSExpression, specific=blorqueScript_BSPlusMinusOrStringConcatExpression)
gen_blorqueScript_BSMulDivOrModExpression_BSExpression = Generalization(general=BSExpression, specific=blorqueScript_BSMulDivOrModExpression)
gen_blorqueScript_BSCastExpression_BSExpression = Generalization(general=BSExpression, specific=blorqueScript_BSCastExpression)
gen_blorqueScript_BSNewExpression_BSExpression = Generalization(general=BSExpression, specific=blorqueScript_BSNewExpression)
gen_blorqueScript_BSUnaryModifierExpression_BSExpression = Generalization(general=BSExpression, specific=blorqueScript_BSUnaryModifierExpression)
gen_blorqueScript_BSMemberSelectionExpression_BSExpression = Generalization(general=BSExpression, specific=blorqueScript_BSMemberSelectionExpression)
gen_blorqueScript_BSMethodInvokationExpression_BSExpression = Generalization(general=BSExpression, specific=blorqueScript_BSMethodInvokationExpression)
gen_blorqueScript_BSStringConstant_BSExpression = Generalization(general=BSExpression, specific=blorqueScript_BSStringConstant)
gen_blorqueScript_BSArrayAccessExpression_BSExpression = Generalization(general=BSExpression, specific=blorqueScript_BSArrayAccessExpression)
gen_blorqueScript_BSPostfixArithmeticExpression_BSExpression = Generalization(general=BSExpression, specific=blorqueScript_BSPostfixArithmeticExpression)
gen_blorqueScript_BSSymbolRef_BSExpression = Generalization(general=BSExpression, specific=blorqueScript_BSSymbolRef)
gen_blorqueScript_BSHexadecimalConstant_BSExpression = Generalization(general=BSExpression, specific=blorqueScript_BSHexadecimalConstant)
gen_blorqueScript_BSNumberConstant_BSExpression = Generalization(general=BSExpression, specific=blorqueScript_BSNumberConstant)
gen_blorqueScript_BSRealConstant_BSExpression = Generalization(general=BSExpression, specific=blorqueScript_BSRealConstant)
gen_blorqueScript_BSBooleanConstant_BSExpression = Generalization(general=BSExpression, specific=blorqueScript_BSBooleanConstant)
gen_blorqueScript_BSNullLiteral_BSExpression = Generalization(general=BSExpression, specific=blorqueScript_BSNullLiteral)
gen_blorqueScript_BSThisLiteral_BSExpression = Generalization(general=BSExpression, specific=blorqueScript_BSThisLiteral)
gen_blorqueScript_BSClientLiteral_BSExpression = Generalization(general=BSExpression, specific=blorqueScript_BSClientLiteral)
gen_blorqueScript_BSParentLiteral_BSExpression = Generalization(general=BSExpression, specific=blorqueScript_BSParentLiteral)
gen_blorqueScript_BSParentheticalExpression_BSExpression = Generalization(general=BSExpression, specific=blorqueScript_BSParentheticalExpression)

# Domain Model
domain_model = DomainModel(
    name="blorqueScript",
    types={blorqueScript_BSMember, blorqueScript_BSFile, blorqueScript_BSImport, blorqueScript_BSClass, blorqueScript_BSReturn, BSStatement, BSSymbol, blorqueScript_BSField, BSMember, blorqueScript_BSMethod, blorqueScript_BSParameter, blorqueScript_BSMethodBody, BSBlock, blorqueScript_BSStatement, blorqueScript_BSWhileLoop, blorqueScript_BSExpression, blorqueScript_BSBreak, blorqueScript_BSContinue, blorqueScript_BSVariableDeclaration, blorqueScript_BSIfStatement, blorqueScript_BSIfBlock, blorqueScript_BSSwitchBlock, blorqueScript_BSLoopBlock, blorqueScript_BSForLoop, blorqueScript_BSSwitchStatement, blorqueScript_BSCase, blorqueScript_BSCaseBlock, blorqueScript_BSBlock, blorqueScript_BSSymbol, blorqueScript_BSAssignmentExpression, BSExpression, blorqueScript_BSBooleanAndExpression, blorqueScript_BSTernaryExpression, blorqueScript_BSBooleanOrExpression, blorqueScript_BSBitwiseAndExpression, blorqueScript_BSBitwiseOrExpression, blorqueScript_BSBitwiseXorExpression, blorqueScript_BSEqualityExpression, blorqueScript_BSOrderedRelationExpression, blorqueScript_BSBitwiseShiftExpression, blorqueScript_BSPlusMinusOrStringConcatExpression, blorqueScript_BSMulDivOrModExpression, blorqueScript_BSCastExpression, blorqueScript_BSNewExpression, blorqueScript_BSUnaryModifierExpression, blorqueScript_BSMemberSelectionExpression, blorqueScript_BSMethodInvokationExpression, blorqueScript_BSStringConstant, blorqueScript_BSArrayAccessExpression, blorqueScript_BSPostfixArithmeticExpression, blorqueScript_BSSymbolRef, blorqueScript_BSHexadecimalConstant, blorqueScript_BSNumberConstant, blorqueScript_BSRealConstant, blorqueScript_BSBooleanConstant, blorqueScript_BSNullLiteral, blorqueScript_BSThisLiteral, blorqueScript_BSClientLiteral, blorqueScript_BSParentLiteral, blorqueScript_BSParentheticalExpression, BSPrimitiveType},
    associations={members6, imports0, classes1, superclass4, statements11, params8, body9, elseBlock20, expression13, expression14, expression16, thenBlock18, expression38, expression23, block25, left27, middle29, right32, block35, block53, block40, statements42, statements45, cases48, expression50, left60, statements55, rType58, left78, right62, left65, middle67, right70, left73, right75, left93, right80, left83, right85, left88, right90, left103, right95, left98, right100, right115, right105, left108, right110, left113, args127, left118, right120, castExpr123, rType125, receiver137, receiver130, receiver132, member134, args139, receiver142, args144, receiver147, symbol150, left149, expression152},
    generalizations={gen_blorqueScript_BSReturn_BSStatement, gen_blorqueScript_BSMember_BSSymbol, gen_blorqueScript_BSField_BSMember, gen_blorqueScript_BSMethod_BSMember, gen_blorqueScript_BSParameter_BSSymbol, gen_blorqueScript_BSMethodBody_BSBlock, gen_blorqueScript_BSWhileLoop_BSStatement, gen_blorqueScript_BSBreak_BSStatement, gen_blorqueScript_BSContinue_BSStatement, gen_blorqueScript_BSVariableDeclaration_BSStatement, gen_blorqueScript_BSVariableDeclaration_BSSymbol, gen_blorqueScript_BSIfStatement_BSStatement, gen_blorqueScript_BSForLoop_BSStatement, gen_blorqueScript_BSSwitchStatement_BSStatement, gen_blorqueScript_BSCaseBlock_BSBlock, gen_blorqueScript_BSIfBlock_BSBlock, gen_blorqueScript_BSLoopBlock_BSBlock, gen_blorqueScript_BSSwitchBlock_BSBlock, gen_blorqueScript_BSExpression_BSStatement, gen_blorqueScript_BSAssignmentExpression_BSExpression, gen_blorqueScript_BSBooleanAndExpression_BSExpression, gen_blorqueScript_BSTernaryExpression_BSExpression, gen_blorqueScript_BSBooleanOrExpression_BSExpression, gen_blorqueScript_BSBitwiseAndExpression_BSExpression, gen_blorqueScript_BSBitwiseOrExpression_BSExpression, gen_blorqueScript_BSBitwiseXorExpression_BSExpression, gen_blorqueScript_BSEqualityExpression_BSExpression, gen_blorqueScript_BSOrderedRelationExpression_BSExpression, gen_blorqueScript_BSBitwiseShiftExpression_BSExpression, gen_blorqueScript_BSPlusMinusOrStringConcatExpression_BSExpression, gen_blorqueScript_BSMulDivOrModExpression_BSExpression, gen_blorqueScript_BSCastExpression_BSExpression, gen_blorqueScript_BSNewExpression_BSExpression, gen_blorqueScript_BSUnaryModifierExpression_BSExpression, gen_blorqueScript_BSMemberSelectionExpression_BSExpression, gen_blorqueScript_BSMethodInvokationExpression_BSExpression, gen_blorqueScript_BSStringConstant_BSExpression, gen_blorqueScript_BSArrayAccessExpression_BSExpression, gen_blorqueScript_BSPostfixArithmeticExpression_BSExpression, gen_blorqueScript_BSSymbolRef_BSExpression, gen_blorqueScript_BSHexadecimalConstant_BSExpression, gen_blorqueScript_BSNumberConstant_BSExpression, gen_blorqueScript_BSRealConstant_BSExpression, gen_blorqueScript_BSBooleanConstant_BSExpression, gen_blorqueScript_BSNullLiteral_BSExpression, gen_blorqueScript_BSThisLiteral_BSExpression, gen_blorqueScript_BSClientLiteral_BSExpression, gen_blorqueScript_BSParentLiteral_BSExpression, gen_blorqueScript_BSParentheticalExpression_BSExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)