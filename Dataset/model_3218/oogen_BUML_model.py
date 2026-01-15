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
OOBaseType: Enumeration = Enumeration(
    name="OOBaseType",
    literals={
            EnumerationLiteral(name="INT"),
			EnumerationLiteral(name="LONG"),
			EnumerationLiteral(name="DOUBLE"),
			EnumerationLiteral(name="STRING"),
			EnumerationLiteral(name="OBJECT"),
			EnumerationLiteral(name="BYTE"),
			EnumerationLiteral(name="BOOLEAN")
    }
)

OOVisibility: Enumeration = Enumeration(
    name="OOVisibility",
    literals={
            EnumerationLiteral(name="PRIVATE"),
			EnumerationLiteral(name="PACKAGE"),
			EnumerationLiteral(name="PROTECTED"),
			EnumerationLiteral(name="PUBLIC")
    }
)

OOCollectionType: Enumeration = Enumeration(
    name="OOCollectionType",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="SET"),
			EnumerationLiteral(name="LIST")
    }
)

OOLanguage: Enumeration = Enumeration(
    name="OOLanguage",
    literals={
            EnumerationLiteral(name="JAVA"),
			EnumerationLiteral(name="CPP")
    }
)

# Classes
oogen_OOPackage = Class(name="oogen::OOPackage")
oogen_OOClass = Class(name="oogen::OOClass")
oogen_OOEnumeration = Class(name="oogen::OOEnumeration")
OOCommentOwner = Class(name="OOCommentOwner")
oogen_OOMember = Class(name="oogen::OOMember")
oogen_OOMethod = Class(name="oogen::OOMethod")
oogen_OOConstructor = Class(name="oogen::OOConstructor")
OOVariable = Class(name="OOVariable")
oogen_OOVariable = Class(name="oogen::OOVariable")
OOStatement = Class(name="OOStatement")
oogen_OOType = Class(name="oogen::OOType")
oogen_OOExpression = Class(name="oogen::OOExpression")
oogen_OOStatement = Class(name="oogen::OOStatement")
oogen_OOModel = Class(name="oogen::OOModel")
oogen_OOAdditionExpression = Class(name="oogen::OOAdditionExpression")
OOTwoOperandAssignableExpression = Class(name="OOTwoOperandAssignableExpression")
oogen_OOReturn = Class(name="oogen::OOReturn")
oogen_OOArithmeticExpression = Class(name="oogen::OOArithmeticExpression")
OOExpression = Class(name="OOExpression")
oogen_OOIndexing = Class(name="oogen::OOIndexing")
oogen_OOAssignmentExpression = Class(name="oogen::OOAssignmentExpression")
oogen_OOTwoOperandArithmeticExpression = Class(name="oogen::OOTwoOperandArithmeticExpression")
OOArithmeticExpression = Class(name="OOArithmeticExpression")
oogen_OOOneOperandLogicalExpression = Class(name="oogen::OOOneOperandLogicalExpression")
oogen_OOSubtractionExpression = Class(name="oogen::OOSubtractionExpression")
oogen_OODivisionExpression = Class(name="oogen::OODivisionExpression")
oogen_OOIntegerDivisionExpression = Class(name="oogen::OOIntegerDivisionExpression")
oogen_OOMultiplicationExpression = Class(name="oogen::OOMultiplicationExpression")
oogen_OOPowerExpression = Class(name="oogen::OOPowerExpression")
OOTwoOperandArithmeticExpression = Class(name="OOTwoOperandArithmeticExpression")
oogen_OORootExpression = Class(name="oogen::OORootExpression")
oogen_OOBitwiseOrExpression = Class(name="oogen::OOBitwiseOrExpression")
oogen_OOBitwiseXorExpression = Class(name="oogen::OOBitwiseXorExpression")
oogen_OOBitwiseAndExpression = Class(name="oogen::OOBitwiseAndExpression")
oogen_OOLogicalExpression = Class(name="oogen::OOLogicalExpression")
oogen_OOAndExpression = Class(name="oogen::OOAndExpression")
OOTwoOperandLogicalExpression = Class(name="OOTwoOperandLogicalExpression")
oogen_OOOrExpression = Class(name="oogen::OOOrExpression")
oogen_OOXorExpression = Class(name="oogen::OOXorExpression")
oogen_OONotExpression = Class(name="oogen::OONotExpression")
OOOneOperandLogicalExpression = Class(name="OOOneOperandLogicalExpression")
oogen_OOTwoOperandLogicalExpression = Class(name="oogen::OOTwoOperandLogicalExpression")
OOLogicalExpression = Class(name="OOLogicalExpression")
OOCompoundStatement = Class(name="OOCompoundStatement")
oogen_OODoubleLiteral = Class(name="oogen::OODoubleLiteral")
oogen_OOFloatLiteral = Class(name="oogen::OOFloatLiteral")
oogen_OOIntegerLiteral = Class(name="oogen::OOIntegerLiteral")
oogen_OOLongLiteral = Class(name="oogen::OOLongLiteral")
oogen_OOIf = Class(name="oogen::OOIf")
OOConditionalStatement = Class(name="OOConditionalStatement")
oogen_OOFor = Class(name="oogen::OOFor")
oogen_OOConditionalStatement = Class(name="oogen::OOConditionalStatement")
oogen_OOTypeCast = Class(name="oogen::OOTypeCast")
oogen_OOWhile = Class(name="oogen::OOWhile")
oogen_OODoWhile = Class(name="oogen::OODoWhile")
oogen_OOEmptyStatement = Class(name="oogen::OOEmptyStatement")
oogen_OOForEach = Class(name="oogen::OOForEach")
oogen_OOBitWiseLeftShift = Class(name="oogen::OOBitWiseLeftShift")
oogen_OOBitWiseRightShift = Class(name="oogen::OOBitWiseRightShift")
oogen_OOBitWiseComplement = Class(name="oogen::OOBitWiseComplement")
OOOneOperandArithmeticExpression = Class(name="OOOneOperandArithmeticExpression")
oogen_OOLanguageSpecificExpression = Class(name="oogen::OOLanguageSpecificExpression")
oogen_OOLanguageSpecificSnippet = Class(name="oogen::OOLanguageSpecificSnippet")
oogen_OOGreaterThanExpression = Class(name="oogen::OOGreaterThanExpression")
oogen_OOLessThanExpression = Class(name="oogen::OOLessThanExpression")
oogen_OONotEqualsExpression = Class(name="oogen::OONotEqualsExpression")
oogen_OOBoolLiteral = Class(name="oogen::OOBoolLiteral")
oogen_OONewClass = Class(name="oogen::OONewClass")
oogen_OOEqualsExpression = Class(name="oogen::OOEqualsExpression")
OOComparatorExpression = Class(name="OOComparatorExpression")
oogen_OOComparatorExpression = Class(name="oogen::OOComparatorExpression")
oogen_OOLogicalLiteral = Class(name="oogen::OOLogicalLiteral")
oogen_OOGreaterEqualsExpression = Class(name="oogen::OOGreaterEqualsExpression")
oogen_OOLessEqualsExpression = Class(name="oogen::OOLessEqualsExpression")
oogen_OOCompoundStatement = Class(name="oogen::OOCompoundStatement")
oogen_OOSwitch = Class(name="oogen::OOSwitch")
oogen_OOCase = Class(name="oogen::OOCase")
oogen_OODefault = Class(name="oogen::OODefault")
oogen_OOTernaryOperator = Class(name="oogen::OOTernaryOperator")
oogen_OOTwoOperandAssignableExpression = Class(name="oogen::OOTwoOperandAssignableExpression")
oogen_OOBreak = Class(name="oogen::OOBreak")
oogen_OOModuloExpression = Class(name="oogen::OOModuloExpression")
oogen_OOContinue = Class(name="oogen::OOContinue")
oogen_OOVariableDeclarationList = Class(name="oogen::OOVariableDeclarationList")
oogen_OOOneOperandArithmeticExpression = Class(name="oogen::OOOneOperandArithmeticExpression")
oogen_OOBracketedExpression = Class(name="oogen::OOBracketedExpression")
oogen_OOPostfixIncrementExpression = Class(name="oogen::OOPostfixIncrementExpression")
oogen_OOPrefixIncrementExpression = Class(name="oogen::OOPrefixIncrementExpression")
oogen_OOPostfixDecrementExpression = Class(name="oogen::OOPostfixDecrementExpression")
oogen_OOPrefixDecrementExpression = Class(name="oogen::OOPrefixDecrementExpression")
oogen_OOPlusExpression = Class(name="oogen::OOPlusExpression")
oogen_OOMinusExpression = Class(name="oogen::OOMinusExpression")
oogen_OOFieldReferenceExpression = Class(name="oogen::OOFieldReferenceExpression")
oogen_OOVariableReferenceExpression = Class(name="oogen::OOVariableReferenceExpression")
oogen_OOInitializerList = Class(name="oogen::OOInitializerList")
oogen_OOThisLiteral = Class(name="oogen::OOThisLiteral")
oogen_OONullLiteral = Class(name="oogen::OONullLiteral")
oogen_OOFunctionCallExpression = Class(name="oogen::OOFunctionCallExpression")
oogen_OOStringLiteral = Class(name="oogen::OOStringLiteral")
oogen_OONewArray = Class(name="oogen::OONewArray")
oogen_OOComment = Class(name="oogen::OOComment")
oogen_OOCommentOwner = Class(name="oogen::OOCommentOwner")
oogen_OOEmptyExpression = Class(name="oogen::OOEmptyExpression")

# oogen_OOPackage class attributes and methods
oogen_OOPackage_name: Property = Property(name="name", type=StringType)
oogen_OOPackage.attributes={oogen_OOPackage_name}

# oogen_OOClass class attributes and methods
oogen_OOClass_name: Property = Property(name="name", type=StringType)
oogen_OOClass_keep: Property = Property(name="keep", type=BooleanType)
oogen_OOClass_languages: Property = Property(name="languages", type=StringType)
oogen_OOClass.attributes={oogen_OOClass_keep, oogen_OOClass_languages, oogen_OOClass_name}

# oogen_OOEnumeration class attributes and methods
oogen_OOEnumeration_name: Property = Property(name="name", type=StringType)
oogen_OOEnumeration_options: Property = Property(name="options", type=StringType)
oogen_OOEnumeration.attributes={oogen_OOEnumeration_name, oogen_OOEnumeration_options}

# OOCommentOwner class attributes and methods

# oogen_OOMember class attributes and methods
oogen_OOMember_visibility: Property = Property(name="visibility", type=StringType)
oogen_OOMember_static: Property = Property(name="static", type=BooleanType)
oogen_OOMember_languages: Property = Property(name="languages", type=StringType)
oogen_OOMember.attributes={oogen_OOMember_languages, oogen_OOMember_static, oogen_OOMember_visibility}

# oogen_OOMethod class attributes and methods
oogen_OOMethod_visibility: Property = Property(name="visibility", type=StringType)
oogen_OOMethod_name: Property = Property(name="name", type=StringType)
oogen_OOMethod_static: Property = Property(name="static", type=BooleanType)
oogen_OOMethod_languages: Property = Property(name="languages", type=StringType)
oogen_OOMethod.attributes={oogen_OOMethod_languages, oogen_OOMethod_static, oogen_OOMethod_name, oogen_OOMethod_visibility}

# oogen_OOConstructor class attributes and methods
oogen_OOConstructor_visibility: Property = Property(name="visibility", type=StringType)
oogen_OOConstructor_className: Property = Property(name="className", type=StringType)
oogen_OOConstructor.attributes={oogen_OOConstructor_className, oogen_OOConstructor_visibility}

# OOVariable class attributes and methods

# oogen_OOVariable class attributes and methods
oogen_OOVariable_name: Property = Property(name="name", type=StringType)
oogen_OOVariable_transient: Property = Property(name="transient", type=BooleanType)
oogen_OOVariable.attributes={oogen_OOVariable_name, oogen_OOVariable_transient}

# OOStatement class attributes and methods

# oogen_OOType class attributes and methods
oogen_OOType_baseType: Property = Property(name="baseType", type=StringType)
oogen_OOType_arrayDimensions: Property = Property(name="arrayDimensions", type=IntegerType)
oogen_OOType_collectionType: Property = Property(name="collectionType", type=StringType)
oogen_OOType_numberOfIndirections: Property = Property(name="numberOfIndirections", type=IntegerType)
oogen_OOType.attributes={oogen_OOType_baseType, oogen_OOType_arrayDimensions, oogen_OOType_collectionType, oogen_OOType_numberOfIndirections}

# oogen_OOExpression class attributes and methods

# oogen_OOStatement class attributes and methods

# oogen_OOModel class attributes and methods

# oogen_OOAdditionExpression class attributes and methods

# OOTwoOperandAssignableExpression class attributes and methods

# oogen_OOReturn class attributes and methods

# oogen_OOArithmeticExpression class attributes and methods

# OOExpression class attributes and methods

# oogen_OOIndexing class attributes and methods

# oogen_OOAssignmentExpression class attributes and methods

# oogen_OOTwoOperandArithmeticExpression class attributes and methods

# OOArithmeticExpression class attributes and methods

# oogen_OOOneOperandLogicalExpression class attributes and methods

# oogen_OOSubtractionExpression class attributes and methods

# oogen_OODivisionExpression class attributes and methods

# oogen_OOIntegerDivisionExpression class attributes and methods

# oogen_OOMultiplicationExpression class attributes and methods

# oogen_OOPowerExpression class attributes and methods

# OOTwoOperandArithmeticExpression class attributes and methods

# oogen_OORootExpression class attributes and methods

# oogen_OOBitwiseOrExpression class attributes and methods

# oogen_OOBitwiseXorExpression class attributes and methods

# oogen_OOBitwiseAndExpression class attributes and methods

# oogen_OOLogicalExpression class attributes and methods

# oogen_OOAndExpression class attributes and methods

# OOTwoOperandLogicalExpression class attributes and methods

# oogen_OOOrExpression class attributes and methods

# oogen_OOXorExpression class attributes and methods

# oogen_OONotExpression class attributes and methods

# OOOneOperandLogicalExpression class attributes and methods

# oogen_OOTwoOperandLogicalExpression class attributes and methods

# OOLogicalExpression class attributes and methods

# OOCompoundStatement class attributes and methods

# oogen_OODoubleLiteral class attributes and methods
oogen_OODoubleLiteral_value: Property = Property(name="value", type=FloatType)
oogen_OODoubleLiteral.attributes={oogen_OODoubleLiteral_value}

# oogen_OOFloatLiteral class attributes and methods
oogen_OOFloatLiteral_value: Property = Property(name="value", type=FloatType)
oogen_OOFloatLiteral.attributes={oogen_OOFloatLiteral_value}

# oogen_OOIntegerLiteral class attributes and methods
oogen_OOIntegerLiteral_value: Property = Property(name="value", type=IntegerType)
oogen_OOIntegerLiteral.attributes={oogen_OOIntegerLiteral_value}

# oogen_OOLongLiteral class attributes and methods
oogen_OOLongLiteral_value: Property = Property(name="value", type=StringType)
oogen_OOLongLiteral.attributes={oogen_OOLongLiteral_value}

# oogen_OOIf class attributes and methods

# OOConditionalStatement class attributes and methods

# oogen_OOFor class attributes and methods

# oogen_OOConditionalStatement class attributes and methods

# oogen_OOTypeCast class attributes and methods

# oogen_OOWhile class attributes and methods

# oogen_OODoWhile class attributes and methods

# oogen_OOEmptyStatement class attributes and methods

# oogen_OOForEach class attributes and methods

# oogen_OOBitWiseLeftShift class attributes and methods

# oogen_OOBitWiseRightShift class attributes and methods

# oogen_OOBitWiseComplement class attributes and methods

# OOOneOperandArithmeticExpression class attributes and methods

# oogen_OOLanguageSpecificExpression class attributes and methods

# oogen_OOLanguageSpecificSnippet class attributes and methods
oogen_OOLanguageSpecificSnippet_code: Property = Property(name="code", type=StringType)
oogen_OOLanguageSpecificSnippet_lang: Property = Property(name="lang", type=StringType)
oogen_OOLanguageSpecificSnippet.attributes={oogen_OOLanguageSpecificSnippet_lang, oogen_OOLanguageSpecificSnippet_code}

# oogen_OOGreaterThanExpression class attributes and methods

# oogen_OOLessThanExpression class attributes and methods

# oogen_OONotEqualsExpression class attributes and methods

# oogen_OOBoolLiteral class attributes and methods
oogen_OOBoolLiteral_value: Property = Property(name="value", type=BooleanType)
oogen_OOBoolLiteral.attributes={oogen_OOBoolLiteral_value}

# oogen_OONewClass class attributes and methods
oogen_OONewClass_className: Property = Property(name="className", type=StringType)
oogen_OONewClass.attributes={oogen_OONewClass_className}

# oogen_OOEqualsExpression class attributes and methods

# OOComparatorExpression class attributes and methods

# oogen_OOComparatorExpression class attributes and methods

# oogen_OOLogicalLiteral class attributes and methods
oogen_OOLogicalLiteral_value: Property = Property(name="value", type=BooleanType)
oogen_OOLogicalLiteral.attributes={oogen_OOLogicalLiteral_value}

# oogen_OOGreaterEqualsExpression class attributes and methods

# oogen_OOLessEqualsExpression class attributes and methods

# oogen_OOCompoundStatement class attributes and methods

# oogen_OOSwitch class attributes and methods

# oogen_OOCase class attributes and methods

# oogen_OODefault class attributes and methods

# oogen_OOTernaryOperator class attributes and methods

# oogen_OOTwoOperandAssignableExpression class attributes and methods
oogen_OOTwoOperandAssignableExpression_assigned: Property = Property(name="assigned", type=BooleanType)
oogen_OOTwoOperandAssignableExpression.attributes={oogen_OOTwoOperandAssignableExpression_assigned}

# oogen_OOBreak class attributes and methods

# oogen_OOModuloExpression class attributes and methods

# oogen_OOContinue class attributes and methods

# oogen_OOVariableDeclarationList class attributes and methods

# oogen_OOOneOperandArithmeticExpression class attributes and methods

# oogen_OOBracketedExpression class attributes and methods

# oogen_OOPostfixIncrementExpression class attributes and methods

# oogen_OOPrefixIncrementExpression class attributes and methods

# oogen_OOPostfixDecrementExpression class attributes and methods

# oogen_OOPrefixDecrementExpression class attributes and methods

# oogen_OOPlusExpression class attributes and methods

# oogen_OOMinusExpression class attributes and methods

# oogen_OOFieldReferenceExpression class attributes and methods
oogen_OOFieldReferenceExpression_fieldName: Property = Property(name="fieldName", type=StringType)
oogen_OOFieldReferenceExpression.attributes={oogen_OOFieldReferenceExpression_fieldName}

# oogen_OOVariableReferenceExpression class attributes and methods

# oogen_OOInitializerList class attributes and methods

# oogen_OOThisLiteral class attributes and methods

# oogen_OONullLiteral class attributes and methods

# oogen_OOFunctionCallExpression class attributes and methods
oogen_OOFunctionCallExpression_functionName: Property = Property(name="functionName", type=StringType)
oogen_OOFunctionCallExpression.attributes={oogen_OOFunctionCallExpression_functionName}

# oogen_OOStringLiteral class attributes and methods
oogen_OOStringLiteral_value: Property = Property(name="value", type=StringType)
oogen_OOStringLiteral.attributes={oogen_OOStringLiteral_value}

# oogen_OONewArray class attributes and methods

# oogen_OOComment class attributes and methods
oogen_OOComment_text: Property = Property(name="text", type=StringType)
oogen_OOComment_isBlockComment: Property = Property(name="isBlockComment", type=BooleanType)
oogen_OOComment.attributes={oogen_OOComment_isBlockComment, oogen_OOComment_text}

# oogen_OOCommentOwner class attributes and methods

# oogen_OOEmptyExpression class attributes and methods

# Relationships
classes0: BinaryAssociation = BinaryAssociation(
    name="classes0",
    ends={
        Property(name="OOClass", type=oogen_OOPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=oogen_OOClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enums1: BinaryAssociation = BinaryAssociation(
    name="enums1",
    ends={
        Property(name="oogen_OOEnumeration", type=oogen_OOPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOPackage", type=oogen_OOEnumeration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members2: BinaryAssociation = BinaryAssociation(
    name="members2",
    ends={
        Property(name="oogen_OOMember", type=oogen_OOClass, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOClass", type=oogen_OOMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package3: BinaryAssociation = BinaryAssociation(
    name="package3",
    ends={
        Property(name="OOPackage", type=oogen_OOClass, multiplicity=Multiplicity(1, 1)),
        Property(name="classes", type=oogen_OOPackage, multiplicity=Multiplicity(0, 1))
    }
)
methods4: BinaryAssociation = BinaryAssociation(
    name="methods4",
    ends={
        Property(name="oogen_OOMethod", type=oogen_OOClass, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOClass5", type=oogen_OOMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constructors6: BinaryAssociation = BinaryAssociation(
    name="constructors6",
    ends={
        Property(name="oogen_OOConstructor", type=oogen_OOClass, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOClass7", type=oogen_OOConstructor, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
type8: BinaryAssociation = BinaryAssociation(
    name="type8",
    ends={
        Property(name="oogen_OOType", type=oogen_OOVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOVariable", type=oogen_OOType, multiplicity=Multiplicity(1, 1))
    }
)
initializerExpression9: BinaryAssociation = BinaryAssociation(
    name="initializerExpression9",
    ends={
        Property(name="oogen_OOExpression", type=oogen_OOVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOVariable10", type=oogen_OOExpression, multiplicity=Multiplicity(0, 1))
    }
)
classType11: BinaryAssociation = BinaryAssociation(
    name="classType11",
    ends={
        Property(name="oogen_OOClass13", type=oogen_OOType, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOType12", type=oogen_OOClass, multiplicity=Multiplicity(0, 1))
    }
)
arraySizeExpressions14: BinaryAssociation = BinaryAssociation(
    name="arraySizeExpressions14",
    ends={
        Property(name="oogen_OOExpression16", type=oogen_OOType, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOType15", type=oogen_OOExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumType17: BinaryAssociation = BinaryAssociation(
    name="enumType17",
    ends={
        Property(name="oogen_OOEnumeration19", type=oogen_OOType, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOType18", type=oogen_OOEnumeration, multiplicity=Multiplicity(0, 1))
    }
)
globalFunctions36: BinaryAssociation = BinaryAssociation(
    name="globalFunctions36",
    ends={
        Property(name="oogen_OOMethod38", type=oogen_OOModel, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOModel37", type=oogen_OOMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters20: BinaryAssociation = BinaryAssociation(
    name="parameters20",
    ends={
        Property(name="oogen_OOVariable22", type=oogen_OOMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOMethod21", type=oogen_OOVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType23: BinaryAssociation = BinaryAssociation(
    name="returnType23",
    ends={
        Property(name="oogen_OOType25", type=oogen_OOMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOMethod24", type=oogen_OOType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements26: BinaryAssociation = BinaryAssociation(
    name="statements26",
    ends={
        Property(name="oogen_OOStatement", type=oogen_OOMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOMethod27", type=oogen_OOStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
oopackage28: BinaryAssociation = BinaryAssociation(
    name="oopackage28",
    ends={
        Property(name="oogen_OOPackage29", type=oogen_OOModel, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOModel", type=oogen_OOPackage, multiplicity=Multiplicity(0, 1))
    }
)
packages30: BinaryAssociation = BinaryAssociation(
    name="packages30",
    ends={
        Property(name="oogen_OOPackage32", type=oogen_OOModel, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOModel31", type=oogen_OOPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalVariables33: BinaryAssociation = BinaryAssociation(
    name="globalVariables33",
    ends={
        Property(name="oogen_OOVariable35", type=oogen_OOModel, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOModel34", type=oogen_OOVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leftSide53: BinaryAssociation = BinaryAssociation(
    name="leftSide53",
    ends={
        Property(name="oogen_OOExpression55", type=oogen_OOTwoOperandArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOTwoOperandArithmeticExpression54", type=oogen_OOExpression, multiplicity=Multiplicity(1, 1))
    }
)
returnedExpresssion39: BinaryAssociation = BinaryAssociation(
    name="returnedExpresssion39",
    ends={
        Property(name="oogen_OOExpression40", type=oogen_OOReturn, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOReturn", type=oogen_OOExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
indexExpression41: BinaryAssociation = BinaryAssociation(
    name="indexExpression41",
    ends={
        Property(name="oogen_OOExpression42", type=oogen_OOIndexing, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOIndexing", type=oogen_OOExpression, multiplicity=Multiplicity(1, 1))
    }
)
collectionExpression43: BinaryAssociation = BinaryAssociation(
    name="collectionExpression43",
    ends={
        Property(name="oogen_OOExpression45", type=oogen_OOIndexing, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOIndexing44", type=oogen_OOExpression, multiplicity=Multiplicity(1, 1))
    }
)
leftSide46: BinaryAssociation = BinaryAssociation(
    name="leftSide46",
    ends={
        Property(name="oogen_OOExpression47", type=oogen_OOAssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOAssignmentExpression", type=oogen_OOExpression, multiplicity=Multiplicity(1, 1))
    }
)
rightSide48: BinaryAssociation = BinaryAssociation(
    name="rightSide48",
    ends={
        Property(name="oogen_OOExpression50", type=oogen_OOAssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOAssignmentExpression49", type=oogen_OOExpression, multiplicity=Multiplicity(1, 1))
    }
)
rightSide51: BinaryAssociation = BinaryAssociation(
    name="rightSide51",
    ends={
        Property(name="oogen_OOExpression52", type=oogen_OOTwoOperandArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOTwoOperandArithmeticExpression", type=oogen_OOExpression, multiplicity=Multiplicity(1, 1))
    }
)
operand61: BinaryAssociation = BinaryAssociation(
    name="operand61",
    ends={
        Property(name="oogen_OOExpression62", type=oogen_OOOneOperandLogicalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOOneOperandLogicalExpression", type=oogen_OOExpression, multiplicity=Multiplicity(1, 1))
    }
)
leftSide56: BinaryAssociation = BinaryAssociation(
    name="leftSide56",
    ends={
        Property(name="oogen_OOExpression57", type=oogen_OOTwoOperandLogicalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOTwoOperandLogicalExpression", type=oogen_OOExpression, multiplicity=Multiplicity(1, 1))
    }
)
rightSide58: BinaryAssociation = BinaryAssociation(
    name="rightSide58",
    ends={
        Property(name="oogen_OOExpression60", type=oogen_OOTwoOperandLogicalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOTwoOperandLogicalExpression59", type=oogen_OOExpression, multiplicity=Multiplicity(1, 1))
    }
)
condition73: BinaryAssociation = BinaryAssociation(
    name="condition73",
    ends={
        Property(name="oogen_OOExpression74", type=oogen_OOConditionalStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOConditionalStatement", type=oogen_OOExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseStatements63: BinaryAssociation = BinaryAssociation(
    name="elseStatements63",
    ends={
        Property(name="oogen_OOStatement64", type=oogen_OOIf, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOIf", type=oogen_OOStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseIf66: BinaryAssociation = BinaryAssociation(
    name="elseIf66",
    ends={
        Property(name="oogen_OOIf67", type=oogen_OOIf, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOIf65", type=oogen_OOIf, multiplicity=Multiplicity(0, 1))
    }
)
initStatement68: BinaryAssociation = BinaryAssociation(
    name="initStatement68",
    ends={
        Property(name="oogen_OOStatement69", type=oogen_OOFor, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOFor", type=oogen_OOStatement, multiplicity=Multiplicity(1, 1))
    }
)
incrementExpression70: BinaryAssociation = BinaryAssociation(
    name="incrementExpression70",
    ends={
        Property(name="oogen_OOExpression72", type=oogen_OOFor, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOFor71", type=oogen_OOExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
traversedVariable75: BinaryAssociation = BinaryAssociation(
    name="traversedVariable75",
    ends={
        Property(name="oogen_OOVariable76", type=oogen_OOForEach, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOForEach", type=oogen_OOVariable, multiplicity=Multiplicity(1, 1))
    }
)
loopVariable77: BinaryAssociation = BinaryAssociation(
    name="loopVariable77",
    ends={
        Property(name="oogen_OOVariable79", type=oogen_OOForEach, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOForEach78", type=oogen_OOVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bodyStatements80: BinaryAssociation = BinaryAssociation(
    name="bodyStatements80",
    ends={
        Property(name="oogen_OOStatement82", type=oogen_OOForEach, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOForEach81", type=oogen_OOStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
snippets83: BinaryAssociation = BinaryAssociation(
    name="snippets83",
    ends={
        Property(name="oogen_OOLanguageSpecificSnippet", type=oogen_OOLanguageSpecificExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOLanguageSpecificExpression", type=oogen_OOLanguageSpecificSnippet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type84: BinaryAssociation = BinaryAssociation(
    name="type84",
    ends={
        Property(name="oogen_OOType85", type=oogen_OOTypeCast, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOTypeCast", type=oogen_OOType, multiplicity=Multiplicity(1, 1))
    }
)
expression86: BinaryAssociation = BinaryAssociation(
    name="expression86",
    ends={
        Property(name="oogen_OOExpression88", type=oogen_OOTypeCast, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOTypeCast87", type=oogen_OOExpression, multiplicity=Multiplicity(1, 1))
    }
)
constructorParameterExpressions89: BinaryAssociation = BinaryAssociation(
    name="constructorParameterExpressions89",
    ends={
        Property(name="oogen_OOExpression90", type=oogen_OONewClass, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OONewClass", type=oogen_OOExpression, multiplicity=Multiplicity(0, 9999))
    }
)
leftSide91: BinaryAssociation = BinaryAssociation(
    name="leftSide91",
    ends={
        Property(name="oogen_OOExpression92", type=oogen_OOComparatorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOComparatorExpression", type=oogen_OOExpression, multiplicity=Multiplicity(1, 1))
    }
)
rightSide93: BinaryAssociation = BinaryAssociation(
    name="rightSide93",
    ends={
        Property(name="oogen_OOExpression95", type=oogen_OOComparatorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOComparatorExpression94", type=oogen_OOExpression, multiplicity=Multiplicity(1, 1))
    }
)
bodyStatements96: BinaryAssociation = BinaryAssociation(
    name="bodyStatements96",
    ends={
        Property(name="oogen_OOStatement97", type=oogen_OOCompoundStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOCompoundStatement", type=oogen_OOStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controllerExpression98: BinaryAssociation = BinaryAssociation(
    name="controllerExpression98",
    ends={
        Property(name="oogen_OOExpression99", type=oogen_OOSwitch, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOSwitch", type=oogen_OOExpression, multiplicity=Multiplicity(1, 1))
    }
)
caseStatements100: BinaryAssociation = BinaryAssociation(
    name="caseStatements100",
    ends={
        Property(name="oogen_OOCase", type=oogen_OOSwitch, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOSwitch101", type=oogen_OOCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultStatement102: BinaryAssociation = BinaryAssociation(
    name="defaultStatement102",
    ends={
        Property(name="oogen_OODefault", type=oogen_OOSwitch, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOSwitch103", type=oogen_OODefault, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression104: BinaryAssociation = BinaryAssociation(
    name="expression104",
    ends={
        Property(name="oogen_OOExpression106", type=oogen_OOCase, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOCase105", type=oogen_OOExpression, multiplicity=Multiplicity(1, 1))
    }
)
variableDeclarations107: BinaryAssociation = BinaryAssociation(
    name="variableDeclarations107",
    ends={
        Property(name="oogen_OOVariable108", type=oogen_OOVariableDeclarationList, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOVariableDeclarationList", type=oogen_OOVariable, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
operand109: BinaryAssociation = BinaryAssociation(
    name="operand109",
    ends={
        Property(name="oogen_OOExpression110", type=oogen_OOOneOperandArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOOneOperandArithmeticExpression", type=oogen_OOExpression, multiplicity=Multiplicity(1, 1))
    }
)
argumentExpressions125: BinaryAssociation = BinaryAssociation(
    name="argumentExpressions125",
    ends={
        Property(name="oogen_OOExpression126", type=oogen_OOFunctionCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOFunctionCallExpression", type=oogen_OOExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition111: BinaryAssociation = BinaryAssociation(
    name="condition111",
    ends={
        Property(name="oogen_OOExpression112", type=oogen_OOTernaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOTernaryOperator", type=oogen_OOExpression, multiplicity=Multiplicity(1, 1))
    }
)
positiveBranch113: BinaryAssociation = BinaryAssociation(
    name="positiveBranch113",
    ends={
        Property(name="oogen_OOExpression115", type=oogen_OOTernaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOTernaryOperator114", type=oogen_OOExpression, multiplicity=Multiplicity(1, 1))
    }
)
negativeBranch116: BinaryAssociation = BinaryAssociation(
    name="negativeBranch116",
    ends={
        Property(name="oogen_OOExpression118", type=oogen_OOTernaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOTernaryOperator117", type=oogen_OOExpression, multiplicity=Multiplicity(1, 1))
    }
)
fieldOwner119: BinaryAssociation = BinaryAssociation(
    name="fieldOwner119",
    ends={
        Property(name="oogen_OOExpression120", type=oogen_OOFieldReferenceExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOFieldReferenceExpression", type=oogen_OOExpression, multiplicity=Multiplicity(1, 1))
    }
)
variable121: BinaryAssociation = BinaryAssociation(
    name="variable121",
    ends={
        Property(name="oogen_OOVariable122", type=oogen_OOVariableReferenceExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOVariableReferenceExpression", type=oogen_OOVariable, multiplicity=Multiplicity(1, 1))
    }
)
initializerExpressions123: BinaryAssociation = BinaryAssociation(
    name="initializerExpressions123",
    ends={
        Property(name="oogen_OOExpression124", type=oogen_OOInitializerList, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOInitializerList", type=oogen_OOExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ownerExpression127: BinaryAssociation = BinaryAssociation(
    name="ownerExpression127",
    ends={
        Property(name="oogen_OOExpression129", type=oogen_OOFunctionCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOFunctionCallExpression128", type=oogen_OOExpression, multiplicity=Multiplicity(0, 1))
    }
)
parameters130: BinaryAssociation = BinaryAssociation(
    name="parameters130",
    ends={
        Property(name="oogen_OOVariable132", type=oogen_OOConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOConstructor131", type=oogen_OOVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements133: BinaryAssociation = BinaryAssociation(
    name="statements133",
    ends={
        Property(name="oogen_OOStatement135", type=oogen_OOConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOConstructor134", type=oogen_OOStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arrayType136: BinaryAssociation = BinaryAssociation(
    name="arrayType136",
    ends={
        Property(name="oogen_OOType137", type=oogen_OONewArray, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OONewArray", type=oogen_OOType, multiplicity=Multiplicity(1, 1))
    }
)
initializerList138: BinaryAssociation = BinaryAssociation(
    name="initializerList138",
    ends={
        Property(name="oogen_OOInitializerList140", type=oogen_OONewArray, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OONewArray139", type=oogen_OOInitializerList, multiplicity=Multiplicity(0, 1))
    }
)
beforeComments141: BinaryAssociation = BinaryAssociation(
    name="beforeComments141",
    ends={
        Property(name="oogen_OOComment", type=oogen_OOCommentOwner, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOCommentOwner", type=oogen_OOComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
afterComments142: BinaryAssociation = BinaryAssociation(
    name="afterComments142",
    ends={
        Property(name="oogen_OOComment144", type=oogen_OOCommentOwner, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOCommentOwner143", type=oogen_OOComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package145: BinaryAssociation = BinaryAssociation(
    name="package145",
    ends={
        Property(name="oogen_OOPackage147", type=oogen_OOEnumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="oogen_OOEnumeration146", type=oogen_OOPackage, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_oogen_OOClass_OOCommentOwner = Generalization(general=OOCommentOwner, specific=oogen_OOClass)
gen_oogen_OOMember_OOVariable = Generalization(general=OOVariable, specific=oogen_OOMember)
gen_oogen_OOMethod_OOCommentOwner = Generalization(general=OOCommentOwner, specific=oogen_OOMethod)
gen_oogen_OOVariable_OOStatement = Generalization(general=OOStatement, specific=oogen_OOVariable)
gen_oogen_OOAdditionExpression_OOTwoOperandAssignableExpression = Generalization(general=OOTwoOperandAssignableExpression, specific=oogen_OOAdditionExpression)
gen_oogen_OOStatement_OOCommentOwner = Generalization(general=OOCommentOwner, specific=oogen_OOStatement)
gen_oogen_OOExpression_OOStatement = Generalization(general=OOStatement, specific=oogen_OOExpression)
gen_oogen_OOReturn_OOStatement = Generalization(general=OOStatement, specific=oogen_OOReturn)
gen_oogen_OOArithmeticExpression_OOExpression = Generalization(general=OOExpression, specific=oogen_OOArithmeticExpression)
gen_oogen_OOIndexing_OOExpression = Generalization(general=OOExpression, specific=oogen_OOIndexing)
gen_oogen_OOAssignmentExpression_OOExpression = Generalization(general=OOExpression, specific=oogen_OOAssignmentExpression)
gen_oogen_OOTwoOperandArithmeticExpression_OOArithmeticExpression = Generalization(general=OOArithmeticExpression, specific=oogen_OOTwoOperandArithmeticExpression)
gen_oogen_OOOneOperandLogicalExpression_OOLogicalExpression = Generalization(general=OOLogicalExpression, specific=oogen_OOOneOperandLogicalExpression)
gen_oogen_OOSubtractionExpression_OOTwoOperandAssignableExpression = Generalization(general=OOTwoOperandAssignableExpression, specific=oogen_OOSubtractionExpression)
gen_oogen_OODivisionExpression_OOTwoOperandAssignableExpression = Generalization(general=OOTwoOperandAssignableExpression, specific=oogen_OODivisionExpression)
gen_oogen_OOIntegerDivisionExpression_OOTwoOperandAssignableExpression = Generalization(general=OOTwoOperandAssignableExpression, specific=oogen_OOIntegerDivisionExpression)
gen_oogen_OOMultiplicationExpression_OOTwoOperandAssignableExpression = Generalization(general=OOTwoOperandAssignableExpression, specific=oogen_OOMultiplicationExpression)
gen_oogen_OOPowerExpression_OOTwoOperandArithmeticExpression = Generalization(general=OOTwoOperandArithmeticExpression, specific=oogen_OOPowerExpression)
gen_oogen_OORootExpression_OOTwoOperandArithmeticExpression = Generalization(general=OOTwoOperandArithmeticExpression, specific=oogen_OORootExpression)
gen_oogen_OOBitwiseOrExpression_OOTwoOperandAssignableExpression = Generalization(general=OOTwoOperandAssignableExpression, specific=oogen_OOBitwiseOrExpression)
gen_oogen_OOBitwiseXorExpression_OOTwoOperandAssignableExpression = Generalization(general=OOTwoOperandAssignableExpression, specific=oogen_OOBitwiseXorExpression)
gen_oogen_OOBitwiseAndExpression_OOTwoOperandAssignableExpression = Generalization(general=OOTwoOperandAssignableExpression, specific=oogen_OOBitwiseAndExpression)
gen_oogen_OOLogicalExpression_OOExpression = Generalization(general=OOExpression, specific=oogen_OOLogicalExpression)
gen_oogen_OOAndExpression_OOTwoOperandLogicalExpression = Generalization(general=OOTwoOperandLogicalExpression, specific=oogen_OOAndExpression)
gen_oogen_OOOrExpression_OOTwoOperandLogicalExpression = Generalization(general=OOTwoOperandLogicalExpression, specific=oogen_OOOrExpression)
gen_oogen_OOXorExpression_OOTwoOperandLogicalExpression = Generalization(general=OOTwoOperandLogicalExpression, specific=oogen_OOXorExpression)
gen_oogen_OONotExpression_OOOneOperandLogicalExpression = Generalization(general=OOOneOperandLogicalExpression, specific=oogen_OONotExpression)
gen_oogen_OOTwoOperandLogicalExpression_OOLogicalExpression = Generalization(general=OOLogicalExpression, specific=oogen_OOTwoOperandLogicalExpression)
gen_oogen_OOConditionalStatement_OOCompoundStatement = Generalization(general=OOCompoundStatement, specific=oogen_OOConditionalStatement)
gen_oogen_OODoubleLiteral_OOArithmeticExpression = Generalization(general=OOArithmeticExpression, specific=oogen_OODoubleLiteral)
gen_oogen_OOFloatLiteral_OOArithmeticExpression = Generalization(general=OOArithmeticExpression, specific=oogen_OOFloatLiteral)
gen_oogen_OOIntegerLiteral_OOArithmeticExpression = Generalization(general=OOArithmeticExpression, specific=oogen_OOIntegerLiteral)
gen_oogen_OOLongLiteral_OOArithmeticExpression = Generalization(general=OOArithmeticExpression, specific=oogen_OOLongLiteral)
gen_oogen_OOIf_OOConditionalStatement = Generalization(general=OOConditionalStatement, specific=oogen_OOIf)
gen_oogen_OOFor_OOConditionalStatement = Generalization(general=OOConditionalStatement, specific=oogen_OOFor)
gen_oogen_OOConditionalStatement_OOStatement = Generalization(general=OOStatement, specific=oogen_OOConditionalStatement)
gen_oogen_OOTypeCast_OOExpression = Generalization(general=OOExpression, specific=oogen_OOTypeCast)
gen_oogen_OOWhile_OOConditionalStatement = Generalization(general=OOConditionalStatement, specific=oogen_OOWhile)
gen_oogen_OODoWhile_OOConditionalStatement = Generalization(general=OOConditionalStatement, specific=oogen_OODoWhile)
gen_oogen_OOEmptyStatement_OOStatement = Generalization(general=OOStatement, specific=oogen_OOEmptyStatement)
gen_oogen_OOForEach_OOStatement = Generalization(general=OOStatement, specific=oogen_OOForEach)
gen_oogen_OOBitWiseLeftShift_OOTwoOperandAssignableExpression = Generalization(general=OOTwoOperandAssignableExpression, specific=oogen_OOBitWiseLeftShift)
gen_oogen_OOBitWiseRightShift_OOTwoOperandAssignableExpression = Generalization(general=OOTwoOperandAssignableExpression, specific=oogen_OOBitWiseRightShift)
gen_oogen_OOBitWiseComplement_OOOneOperandArithmeticExpression = Generalization(general=OOOneOperandArithmeticExpression, specific=oogen_OOBitWiseComplement)
gen_oogen_OOLanguageSpecificExpression_OOExpression = Generalization(general=OOExpression, specific=oogen_OOLanguageSpecificExpression)
gen_oogen_OOLanguageSpecificExpression_OOLogicalExpression = Generalization(general=OOLogicalExpression, specific=oogen_OOLanguageSpecificExpression)
gen_oogen_OOGreaterThanExpression_OOComparatorExpression = Generalization(general=OOComparatorExpression, specific=oogen_OOGreaterThanExpression)
gen_oogen_OOLessThanExpression_OOComparatorExpression = Generalization(general=OOComparatorExpression, specific=oogen_OOLessThanExpression)
gen_oogen_OONotEqualsExpression_OOComparatorExpression = Generalization(general=OOComparatorExpression, specific=oogen_OONotEqualsExpression)
gen_oogen_OOBoolLiteral_OOExpression = Generalization(general=OOExpression, specific=oogen_OOBoolLiteral)
gen_oogen_OONewClass_OOExpression = Generalization(general=OOExpression, specific=oogen_OONewClass)
gen_oogen_OOEqualsExpression_OOComparatorExpression = Generalization(general=OOComparatorExpression, specific=oogen_OOEqualsExpression)
gen_oogen_OOComparatorExpression_OOLogicalExpression = Generalization(general=OOLogicalExpression, specific=oogen_OOComparatorExpression)
gen_oogen_OOLogicalLiteral_OOLogicalExpression = Generalization(general=OOLogicalExpression, specific=oogen_OOLogicalLiteral)
gen_oogen_OODefault_OOCompoundStatement = Generalization(general=OOCompoundStatement, specific=oogen_OODefault)
gen_oogen_OOGreaterEqualsExpression_OOComparatorExpression = Generalization(general=OOComparatorExpression, specific=oogen_OOGreaterEqualsExpression)
gen_oogen_OOLessEqualsExpression_OOComparatorExpression = Generalization(general=OOComparatorExpression, specific=oogen_OOLessEqualsExpression)
gen_oogen_OOCompoundStatement_OOStatement = Generalization(general=OOStatement, specific=oogen_OOCompoundStatement)
gen_oogen_OOSwitch_OOStatement = Generalization(general=OOStatement, specific=oogen_OOSwitch)
gen_oogen_OOCase_OOCompoundStatement = Generalization(general=OOCompoundStatement, specific=oogen_OOCase)
gen_oogen_OOTernaryOperator_OOLogicalExpression = Generalization(general=OOLogicalExpression, specific=oogen_OOTernaryOperator)
gen_oogen_OOTwoOperandAssignableExpression_OOTwoOperandArithmeticExpression = Generalization(general=OOTwoOperandArithmeticExpression, specific=oogen_OOTwoOperandAssignableExpression)
gen_oogen_OOBreak_OOStatement = Generalization(general=OOStatement, specific=oogen_OOBreak)
gen_oogen_OOModuloExpression_OOTwoOperandAssignableExpression = Generalization(general=OOTwoOperandAssignableExpression, specific=oogen_OOModuloExpression)
gen_oogen_OOContinue_OOStatement = Generalization(general=OOStatement, specific=oogen_OOContinue)
gen_oogen_OOVariableDeclarationList_OOStatement = Generalization(general=OOStatement, specific=oogen_OOVariableDeclarationList)
gen_oogen_OOOneOperandArithmeticExpression_OOArithmeticExpression = Generalization(general=OOArithmeticExpression, specific=oogen_OOOneOperandArithmeticExpression)
gen_oogen_OOBracketedExpression_OOOneOperandArithmeticExpression = Generalization(general=OOOneOperandArithmeticExpression, specific=oogen_OOBracketedExpression)
gen_oogen_OOPostfixIncrementExpression_OOOneOperandArithmeticExpression = Generalization(general=OOOneOperandArithmeticExpression, specific=oogen_OOPostfixIncrementExpression)
gen_oogen_OOPrefixIncrementExpression_OOOneOperandArithmeticExpression = Generalization(general=OOOneOperandArithmeticExpression, specific=oogen_OOPrefixIncrementExpression)
gen_oogen_OOPostfixDecrementExpression_OOOneOperandArithmeticExpression = Generalization(general=OOOneOperandArithmeticExpression, specific=oogen_OOPostfixDecrementExpression)
gen_oogen_OOPrefixDecrementExpression_OOOneOperandArithmeticExpression = Generalization(general=OOOneOperandArithmeticExpression, specific=oogen_OOPrefixDecrementExpression)
gen_oogen_OOPlusExpression_OOOneOperandArithmeticExpression = Generalization(general=OOOneOperandArithmeticExpression, specific=oogen_OOPlusExpression)
gen_oogen_OOMinusExpression_OOOneOperandArithmeticExpression = Generalization(general=OOOneOperandArithmeticExpression, specific=oogen_OOMinusExpression)
gen_oogen_OOFieldReferenceExpression_OOExpression = Generalization(general=OOExpression, specific=oogen_OOFieldReferenceExpression)
gen_oogen_OOVariableReferenceExpression_OOExpression = Generalization(general=OOExpression, specific=oogen_OOVariableReferenceExpression)
gen_oogen_OOInitializerList_OOExpression = Generalization(general=OOExpression, specific=oogen_OOInitializerList)
gen_oogen_OOThisLiteral_OOExpression = Generalization(general=OOExpression, specific=oogen_OOThisLiteral)
gen_oogen_OONullLiteral_OOExpression = Generalization(general=OOExpression, specific=oogen_OONullLiteral)
gen_oogen_OOFunctionCallExpression_OOExpression = Generalization(general=OOExpression, specific=oogen_OOFunctionCallExpression)
gen_oogen_OOStringLiteral_OOExpression = Generalization(general=OOExpression, specific=oogen_OOStringLiteral)
gen_oogen_OONewArray_OOExpression = Generalization(general=OOExpression, specific=oogen_OONewArray)
gen_oogen_OOEnumeration_OOCommentOwner = Generalization(general=OOCommentOwner, specific=oogen_OOEnumeration)
gen_oogen_OOEmptyExpression_OOExpression = Generalization(general=OOExpression, specific=oogen_OOEmptyExpression)

# Domain Model
domain_model = DomainModel(
    name="oogen",
    types={oogen_OOPackage, oogen_OOClass, oogen_OOEnumeration, OOCommentOwner, oogen_OOMember, oogen_OOMethod, oogen_OOConstructor, OOVariable, oogen_OOVariable, OOStatement, oogen_OOType, oogen_OOExpression, oogen_OOStatement, oogen_OOModel, oogen_OOAdditionExpression, OOTwoOperandAssignableExpression, oogen_OOReturn, oogen_OOArithmeticExpression, OOExpression, oogen_OOIndexing, oogen_OOAssignmentExpression, oogen_OOTwoOperandArithmeticExpression, OOArithmeticExpression, oogen_OOOneOperandLogicalExpression, oogen_OOSubtractionExpression, oogen_OODivisionExpression, oogen_OOIntegerDivisionExpression, oogen_OOMultiplicationExpression, oogen_OOPowerExpression, OOTwoOperandArithmeticExpression, oogen_OORootExpression, oogen_OOBitwiseOrExpression, oogen_OOBitwiseXorExpression, oogen_OOBitwiseAndExpression, oogen_OOLogicalExpression, oogen_OOAndExpression, OOTwoOperandLogicalExpression, oogen_OOOrExpression, oogen_OOXorExpression, oogen_OONotExpression, OOOneOperandLogicalExpression, oogen_OOTwoOperandLogicalExpression, OOLogicalExpression, OOCompoundStatement, oogen_OODoubleLiteral, oogen_OOFloatLiteral, oogen_OOIntegerLiteral, oogen_OOLongLiteral, oogen_OOIf, OOConditionalStatement, oogen_OOFor, oogen_OOConditionalStatement, oogen_OOTypeCast, oogen_OOWhile, oogen_OODoWhile, oogen_OOEmptyStatement, oogen_OOForEach, oogen_OOBitWiseLeftShift, oogen_OOBitWiseRightShift, oogen_OOBitWiseComplement, OOOneOperandArithmeticExpression, oogen_OOLanguageSpecificExpression, oogen_OOLanguageSpecificSnippet, oogen_OOGreaterThanExpression, oogen_OOLessThanExpression, oogen_OONotEqualsExpression, oogen_OOBoolLiteral, oogen_OONewClass, oogen_OOEqualsExpression, OOComparatorExpression, oogen_OOComparatorExpression, oogen_OOLogicalLiteral, oogen_OOGreaterEqualsExpression, oogen_OOLessEqualsExpression, oogen_OOCompoundStatement, oogen_OOSwitch, oogen_OOCase, oogen_OODefault, oogen_OOTernaryOperator, oogen_OOTwoOperandAssignableExpression, oogen_OOBreak, oogen_OOModuloExpression, oogen_OOContinue, oogen_OOVariableDeclarationList, oogen_OOOneOperandArithmeticExpression, oogen_OOBracketedExpression, oogen_OOPostfixIncrementExpression, oogen_OOPrefixIncrementExpression, oogen_OOPostfixDecrementExpression, oogen_OOPrefixDecrementExpression, oogen_OOPlusExpression, oogen_OOMinusExpression, oogen_OOFieldReferenceExpression, oogen_OOVariableReferenceExpression, oogen_OOInitializerList, oogen_OOThisLiteral, oogen_OONullLiteral, oogen_OOFunctionCallExpression, oogen_OOStringLiteral, oogen_OONewArray, oogen_OOComment, oogen_OOCommentOwner, oogen_OOEmptyExpression, OOBaseType, OOVisibility, OOCollectionType, OOLanguage},
    associations={classes0, enums1, members2, package3, methods4, constructors6, type8, initializerExpression9, classType11, arraySizeExpressions14, enumType17, globalFunctions36, parameters20, returnType23, statements26, oopackage28, packages30, globalVariables33, leftSide53, returnedExpresssion39, indexExpression41, collectionExpression43, leftSide46, rightSide48, rightSide51, operand61, leftSide56, rightSide58, condition73, elseStatements63, elseIf66, initStatement68, incrementExpression70, traversedVariable75, loopVariable77, bodyStatements80, snippets83, type84, expression86, constructorParameterExpressions89, leftSide91, rightSide93, bodyStatements96, controllerExpression98, caseStatements100, defaultStatement102, expression104, variableDeclarations107, operand109, argumentExpressions125, condition111, positiveBranch113, negativeBranch116, fieldOwner119, variable121, initializerExpressions123, ownerExpression127, parameters130, statements133, arrayType136, initializerList138, beforeComments141, afterComments142, package145},
    generalizations={gen_oogen_OOClass_OOCommentOwner, gen_oogen_OOMember_OOVariable, gen_oogen_OOMethod_OOCommentOwner, gen_oogen_OOVariable_OOStatement, gen_oogen_OOAdditionExpression_OOTwoOperandAssignableExpression, gen_oogen_OOStatement_OOCommentOwner, gen_oogen_OOExpression_OOStatement, gen_oogen_OOReturn_OOStatement, gen_oogen_OOArithmeticExpression_OOExpression, gen_oogen_OOIndexing_OOExpression, gen_oogen_OOAssignmentExpression_OOExpression, gen_oogen_OOTwoOperandArithmeticExpression_OOArithmeticExpression, gen_oogen_OOOneOperandLogicalExpression_OOLogicalExpression, gen_oogen_OOSubtractionExpression_OOTwoOperandAssignableExpression, gen_oogen_OODivisionExpression_OOTwoOperandAssignableExpression, gen_oogen_OOIntegerDivisionExpression_OOTwoOperandAssignableExpression, gen_oogen_OOMultiplicationExpression_OOTwoOperandAssignableExpression, gen_oogen_OOPowerExpression_OOTwoOperandArithmeticExpression, gen_oogen_OORootExpression_OOTwoOperandArithmeticExpression, gen_oogen_OOBitwiseOrExpression_OOTwoOperandAssignableExpression, gen_oogen_OOBitwiseXorExpression_OOTwoOperandAssignableExpression, gen_oogen_OOBitwiseAndExpression_OOTwoOperandAssignableExpression, gen_oogen_OOLogicalExpression_OOExpression, gen_oogen_OOAndExpression_OOTwoOperandLogicalExpression, gen_oogen_OOOrExpression_OOTwoOperandLogicalExpression, gen_oogen_OOXorExpression_OOTwoOperandLogicalExpression, gen_oogen_OONotExpression_OOOneOperandLogicalExpression, gen_oogen_OOTwoOperandLogicalExpression_OOLogicalExpression, gen_oogen_OOConditionalStatement_OOCompoundStatement, gen_oogen_OODoubleLiteral_OOArithmeticExpression, gen_oogen_OOFloatLiteral_OOArithmeticExpression, gen_oogen_OOIntegerLiteral_OOArithmeticExpression, gen_oogen_OOLongLiteral_OOArithmeticExpression, gen_oogen_OOIf_OOConditionalStatement, gen_oogen_OOFor_OOConditionalStatement, gen_oogen_OOConditionalStatement_OOStatement, gen_oogen_OOTypeCast_OOExpression, gen_oogen_OOWhile_OOConditionalStatement, gen_oogen_OODoWhile_OOConditionalStatement, gen_oogen_OOEmptyStatement_OOStatement, gen_oogen_OOForEach_OOStatement, gen_oogen_OOBitWiseLeftShift_OOTwoOperandAssignableExpression, gen_oogen_OOBitWiseRightShift_OOTwoOperandAssignableExpression, gen_oogen_OOBitWiseComplement_OOOneOperandArithmeticExpression, gen_oogen_OOLanguageSpecificExpression_OOExpression, gen_oogen_OOLanguageSpecificExpression_OOLogicalExpression, gen_oogen_OOGreaterThanExpression_OOComparatorExpression, gen_oogen_OOLessThanExpression_OOComparatorExpression, gen_oogen_OONotEqualsExpression_OOComparatorExpression, gen_oogen_OOBoolLiteral_OOExpression, gen_oogen_OONewClass_OOExpression, gen_oogen_OOEqualsExpression_OOComparatorExpression, gen_oogen_OOComparatorExpression_OOLogicalExpression, gen_oogen_OOLogicalLiteral_OOLogicalExpression, gen_oogen_OODefault_OOCompoundStatement, gen_oogen_OOGreaterEqualsExpression_OOComparatorExpression, gen_oogen_OOLessEqualsExpression_OOComparatorExpression, gen_oogen_OOCompoundStatement_OOStatement, gen_oogen_OOSwitch_OOStatement, gen_oogen_OOCase_OOCompoundStatement, gen_oogen_OOTernaryOperator_OOLogicalExpression, gen_oogen_OOTwoOperandAssignableExpression_OOTwoOperandArithmeticExpression, gen_oogen_OOBreak_OOStatement, gen_oogen_OOModuloExpression_OOTwoOperandAssignableExpression, gen_oogen_OOContinue_OOStatement, gen_oogen_OOVariableDeclarationList_OOStatement, gen_oogen_OOOneOperandArithmeticExpression_OOArithmeticExpression, gen_oogen_OOBracketedExpression_OOOneOperandArithmeticExpression, gen_oogen_OOPostfixIncrementExpression_OOOneOperandArithmeticExpression, gen_oogen_OOPrefixIncrementExpression_OOOneOperandArithmeticExpression, gen_oogen_OOPostfixDecrementExpression_OOOneOperandArithmeticExpression, gen_oogen_OOPrefixDecrementExpression_OOOneOperandArithmeticExpression, gen_oogen_OOPlusExpression_OOOneOperandArithmeticExpression, gen_oogen_OOMinusExpression_OOOneOperandArithmeticExpression, gen_oogen_OOFieldReferenceExpression_OOExpression, gen_oogen_OOVariableReferenceExpression_OOExpression, gen_oogen_OOInitializerList_OOExpression, gen_oogen_OOThisLiteral_OOExpression, gen_oogen_OONullLiteral_OOExpression, gen_oogen_OOFunctionCallExpression_OOExpression, gen_oogen_OOStringLiteral_OOExpression, gen_oogen_OONewArray_OOExpression, gen_oogen_OOEnumeration_OOCommentOwner, gen_oogen_OOEmptyExpression_OOExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)