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
			EnumerationLiteral(name="PROTECTED"),
			EnumerationLiteral(name="INTERNAL"),
			EnumerationLiteral(name="PRIVATE")
    }
)

# Classes
aS3_annotationField = Class(name="aS3::annotationField")
aS3_Expression = Class(name="aS3::Expression")
aS3_Model = Class(name="aS3::Model")
aS3_Package = Class(name="aS3::Package")
aS3_Imports = Class(name="aS3::Imports")
aS3_EObject = Class(name="aS3::EObject")
aS3_directive = Class(name="aS3::directive")
aS3_Import = Class(name="aS3::Import")
aS3_Uses = Class(name="aS3::Uses")
aS3_Annotation = Class(name="aS3::Annotation")
aS3_annotationFields = Class(name="aS3::annotationFields")
aS3_Member = Class(name="aS3::Member")
aS3_Interface = Class(name="aS3::Interface")
aS3_InterfaceMethod = Class(name="aS3::InterfaceMethod")
aS3_Modifier = Class(name="aS3::Modifier")
aS3_AccessorRole = Class(name="aS3::AccessorRole")
aS3_Parameter = Class(name="aS3::Parameter")
aS3_functionExpression = Class(name="aS3::functionExpression")
aS3_functionCommon = Class(name="aS3::functionCommon")
aS3_functionSignature = Class(name="aS3::functionSignature")
aS3_Block = Class(name="aS3::Block")
aS3_Class = Class(name="aS3::Class")
aS3_MethodBody = Class(name="aS3::MethodBody")
aS3_Statement = Class(name="aS3::Statement")
aS3_MemberVariableDeclaration = Class(name="aS3::MemberVariableDeclaration")
aS3_Method = Class(name="aS3::Method")
aS3_fieldName = Class(name="aS3::fieldName")
aS3_element = Class(name="aS3::element")
aS3_assignmentExpression = Class(name="aS3::assignmentExpression")
aS3_VariableDeclaration = Class(name="aS3::VariableDeclaration")
Statement = Class(name="Statement")
forInClauseDecl = Class(name="forInClauseDecl")
aS3_exprOrObjectLiteral = Class(name="aS3::exprOrObjectLiteral")
aS3_objectLiteral = Class(name="aS3::objectLiteral")
exprOrObjectLiteral = Class(name="exprOrObjectLiteral")
aS3_fieldList = Class(name="aS3::fieldList")
aS3_literalField = Class(name="aS3::literalField")
aS3_brackets = Class(name="aS3::brackets")
aS3_identi = Class(name="aS3::identi")
aS3_qualifiedIdent = Class(name="aS3::qualifiedIdent")
propertyIdentifier = Class(name="propertyIdentifier")
catchBlock = Class(name="catchBlock")
aS3_typeExpression = Class(name="aS3::typeExpression")
aS3_identifier = Class(name="aS3::identifier")
aS3_propOrIdent = Class(name="aS3::propOrIdent")
aS3_propertyIdentifier = Class(name="aS3::propertyIdentifier")
qualifier = Class(name="qualifier")
aS3_qualifier = Class(name="aS3::qualifier")
aS3_simpleQualifiedIdentifier = Class(name="aS3::simpleQualifiedIdentifier")
nonAttributeQualifiedIdentifier = Class(name="nonAttributeQualifiedIdentifier")
aS3_conditionalExpression = Class(name="aS3::conditionalExpression")
assignmentExpression = Class(name="assignmentExpression")
aS3_expressionQualifiedIdentifier = Class(name="aS3::expressionQualifiedIdentifier")
aS3_nonAttributeQualifiedIdentifier = Class(name="aS3::nonAttributeQualifiedIdentifier")
qualifiedIdentifier = Class(name="qualifiedIdentifier")
aS3_qualifiedIdentifier = Class(name="aS3::qualifiedIdentifier")
aS3_namespaceName = Class(name="aS3::namespaceName")
qualifiedIdent = Class(name="qualifiedIdent")
aS3_arrayLiteral = Class(name="aS3::arrayLiteral")
aS3_elementList = Class(name="aS3::elementList")
aS3_nonemptyElementList = Class(name="aS3::nonemptyElementList")
elementList = Class(name="elementList")
Condition = Class(name="Condition")
DefaultXMLNamespaceStatement = Class(name="DefaultXMLNamespaceStatement")
ThrowStatement = Class(name="ThrowStatement")
CaseStatement = Class(name="CaseStatement")
aS3_switchStatementList = Class(name="aS3::switchStatementList")
aS3_expressionList = Class(name="aS3::expressionList")
brackets = Class(name="brackets")
ExpressionStatement = Class(name="ExpressionStatement")
forInClauseTail = Class(name="forInClauseTail")
element = Class(name="element")
nonemptyElementList = Class(name="nonemptyElementList")
Expression = Class(name="Expression")
encapsulatedExpression = Class(name="encapsulatedExpression")
parameterDefault = Class(name="parameterDefault")
aS3_conditionalSubExpression = Class(name="aS3::conditionalSubExpression")
aS3_logicalOrExpression = Class(name="aS3::logicalOrExpression")
conditionalExpression = Class(name="conditionalExpression")
aS3_logicalAndExpression = Class(name="aS3::logicalAndExpression")
aS3_bitwiseOrExpression = Class(name="aS3::bitwiseOrExpression")
aS3_bitwiseXorExpression = Class(name="aS3::bitwiseXorExpression")
aS3_bitwiseAndExpression = Class(name="aS3::bitwiseAndExpression")
aS3_equalityExpression = Class(name="aS3::equalityExpression")
aS3_relationalExpression = Class(name="aS3::relationalExpression")
aS3_shiftExpression = Class(name="aS3::shiftExpression")
aS3_additiveExpression = Class(name="aS3::additiveExpression")
aS3_multiplicativeExpression = Class(name="aS3::multiplicativeExpression")
aS3_unaryExpression = Class(name="aS3::unaryExpression")
unaryExpressionNotPlusMinus = Class(name="unaryExpressionNotPlusMinus")
aS3_unaryExpressionNotPlusMinus = Class(name="aS3::unaryExpressionNotPlusMinus")
aS3_postfixExpression = Class(name="aS3::postfixExpression")
aS3_primaryExpression = Class(name="aS3::primaryExpression")
aS3_e4xAttributeIdentifier = Class(name="aS3::e4xAttributeIdentifier")
aS3_arguments = Class(name="aS3::arguments")
aS3_newExpression = Class(name="aS3::newExpression")
aS3_encapsulatedExpression = Class(name="aS3::encapsulatedExpression")
expressionQualifiedIdentifier = Class(name="expressionQualifiedIdentifier")
aS3_regexpLiteral = Class(name="aS3::regexpLiteral")
aS3_fullNewSubexpression = Class(name="aS3::fullNewSubexpression")
aS3_Condition = Class(name="aS3::Condition")
SwitchStatement = Class(name="SwitchStatement")
aS3_switchBlock = Class(name="aS3::switchBlock")
aS3_DefaultXMLNamespaceStatement = Class(name="aS3::DefaultXMLNamespaceStatement")
aS3_ExpressionStatement = Class(name="aS3::ExpressionStatement")
aS3_parameterDeclarationList = Class(name="aS3::parameterDeclarationList")
aS3_parameterDeclaration = Class(name="aS3::parameterDeclaration")
aS3_basicParameterDeclaration = Class(name="aS3::basicParameterDeclaration")
parameterDeclaration = Class(name="parameterDeclaration")
aS3_parameterDefault = Class(name="aS3::parameterDefault")
aS3_parameterRestDeclaration = Class(name="aS3::parameterRestDeclaration")
finallyBlock = Class(name="finallyBlock")
aS3_ReturnStatement = Class(name="aS3::ReturnStatement")
aS3_IfStatement = Class(name="aS3::IfStatement")
aS3_ThrowStatement = Class(name="aS3::ThrowStatement")
aS3_TryStatement = Class(name="aS3::TryStatement")
aS3_finallyBlock = Class(name="aS3::finallyBlock")
aS3_catchBlock = Class(name="aS3::catchBlock")
aS3_SwitchStatement = Class(name="aS3::SwitchStatement")
aS3_CaseStatement = Class(name="aS3::CaseStatement")
aS3_DefaultStatement = Class(name="aS3::DefaultStatement")
aS3_ForEachStatement = Class(name="aS3::ForEachStatement")
aS3_forInClause = Class(name="aS3::forInClause")
aS3_ForStatement = Class(name="aS3::ForStatement")
aS3_traditionalForClause = Class(name="aS3::traditionalForClause")
aS3_forInit = Class(name="aS3::forInit")
aS3_forCond = Class(name="aS3::forCond")
aS3_forIter = Class(name="aS3::forIter")
aS3_forInClauseDecl = Class(name="aS3::forInClauseDecl")
aS3_forInClauseTail = Class(name="aS3::forInClauseTail")
aS3_WhileStatement = Class(name="aS3::WhileStatement")
aS3_DoWhileStatement = Class(name="aS3::DoWhileStatement")
aS3_WithStatement = Class(name="aS3::WithStatement")
aS3_XmlConstant = Class(name="aS3::XmlConstant")
aS3_RegexpConstant = Class(name="aS3::RegexpConstant")
aS3_NumberConstant = Class(name="aS3::NumberConstant")
aS3_StringConstant = Class(name="aS3::StringConstant")
aS3_BoolConstant = Class(name="aS3::BoolConstant")
aS3_Undefined = Class(name="aS3::Undefined")
aS3_This = Class(name="aS3::This")
aS3_Null = Class(name="aS3::Null")
aS3_SymbolRef = Class(name="aS3::SymbolRef")

# aS3_annotationField class attributes and methods
aS3_annotationField_name: Property = Property(name="name", type=StringType)
aS3_annotationField.attributes={aS3_annotationField_name}

# aS3_Expression class attributes and methods

# aS3_Model class attributes and methods

# aS3_Package class attributes and methods
aS3_Package_name: Property = Property(name="name", type=StringType)
aS3_Package.attributes={aS3_Package_name}

# aS3_Imports class attributes and methods

# aS3_EObject class attributes and methods

# aS3_directive class attributes and methods

# aS3_Import class attributes and methods
aS3_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
aS3_Import.attributes={aS3_Import_importedNamespace}

# aS3_Uses class attributes and methods
aS3_Uses_anytype: Property = Property(name="anytype", type=StringType)
aS3_Uses_type: Property = Property(name="type", type=StringType)
aS3_Uses.attributes={aS3_Uses_anytype, aS3_Uses_type}

# aS3_Annotation class attributes and methods
aS3_Annotation_name: Property = Property(name="name", type=StringType)
aS3_Annotation.attributes={aS3_Annotation_name}

# aS3_annotationFields class attributes and methods

# aS3_Member class attributes and methods

# aS3_Interface class attributes and methods
aS3_Interface_access: Property = Property(name="access", type=StringType)
aS3_Interface_name: Property = Property(name="name", type=StringType)
aS3_Interface.attributes={aS3_Interface_access, aS3_Interface_name}

# aS3_InterfaceMethod class attributes and methods
aS3_InterfaceMethod_name: Property = Property(name="name", type=StringType)
aS3_InterfaceMethod_anytype: Property = Property(name="anytype", type=StringType)
aS3_InterfaceMethod.attributes={aS3_InterfaceMethod_name, aS3_InterfaceMethod_anytype}

# aS3_Modifier class attributes and methods
aS3_Modifier_static: Property = Property(name="static", type=BooleanType)
aS3_Modifier_final: Property = Property(name="final", type=BooleanType)
aS3_Modifier_native: Property = Property(name="native", type=BooleanType)
aS3_Modifier_dynamic: Property = Property(name="dynamic", type=BooleanType)
aS3_Modifier_access: Property = Property(name="access", type=StringType)
aS3_Modifier.attributes={aS3_Modifier_access, aS3_Modifier_native, aS3_Modifier_dynamic, aS3_Modifier_static, aS3_Modifier_final}

# aS3_AccessorRole class attributes and methods
aS3_AccessorRole_accessor: Property = Property(name="accessor", type=StringType)
aS3_AccessorRole.attributes={aS3_AccessorRole_accessor}

# aS3_Parameter class attributes and methods
aS3_Parameter_name: Property = Property(name="name", type=StringType)
aS3_Parameter_anytype: Property = Property(name="anytype", type=StringType)
aS3_Parameter.attributes={aS3_Parameter_anytype, aS3_Parameter_name}

# aS3_functionExpression class attributes and methods
aS3_functionExpression_name: Property = Property(name="name", type=StringType)
aS3_functionExpression.attributes={aS3_functionExpression_name}

# aS3_functionCommon class attributes and methods

# aS3_functionSignature class attributes and methods

# aS3_Block class attributes and methods

# aS3_Class class attributes and methods
aS3_Class_name: Property = Property(name="name", type=StringType)
aS3_Class.attributes={aS3_Class_name}

# aS3_MethodBody class attributes and methods

# aS3_Statement class attributes and methods

# aS3_MemberVariableDeclaration class attributes and methods
aS3_MemberVariableDeclaration_name: Property = Property(name="name", type=StringType)
aS3_MemberVariableDeclaration_anytype: Property = Property(name="anytype", type=StringType)
aS3_MemberVariableDeclaration.attributes={aS3_MemberVariableDeclaration_name, aS3_MemberVariableDeclaration_anytype}

# aS3_Method class attributes and methods
aS3_Method_name: Property = Property(name="name", type=StringType)
aS3_Method_anytype: Property = Property(name="anytype", type=StringType)
aS3_Method.attributes={aS3_Method_anytype, aS3_Method_name}

# aS3_fieldName class attributes and methods
aS3_fieldName_number: Property = Property(name="number", type=StringType)
aS3_fieldName_name: Property = Property(name="name", type=StringType)
aS3_fieldName.attributes={aS3_fieldName_number, aS3_fieldName_name}

# aS3_element class attributes and methods

# aS3_assignmentExpression class attributes and methods

# aS3_VariableDeclaration class attributes and methods
aS3_VariableDeclaration_name: Property = Property(name="name", type=StringType)
aS3_VariableDeclaration_anytype: Property = Property(name="anytype", type=StringType)
aS3_VariableDeclaration.attributes={aS3_VariableDeclaration_name, aS3_VariableDeclaration_anytype}

# Statement class attributes and methods

# forInClauseDecl class attributes and methods

# aS3_exprOrObjectLiteral class attributes and methods

# aS3_objectLiteral class attributes and methods

# exprOrObjectLiteral class attributes and methods

# aS3_fieldList class attributes and methods

# aS3_literalField class attributes and methods

# aS3_brackets class attributes and methods

# aS3_identi class attributes and methods
aS3_identi_i: Property = Property(name="i", type=StringType)
aS3_identi.attributes={aS3_identi_i}

# aS3_qualifiedIdent class attributes and methods

# propertyIdentifier class attributes and methods

# catchBlock class attributes and methods

# aS3_typeExpression class attributes and methods

# aS3_identifier class attributes and methods

# aS3_propOrIdent class attributes and methods

# aS3_propertyIdentifier class attributes and methods

# qualifier class attributes and methods

# aS3_qualifier class attributes and methods
aS3_qualifier_level: Property = Property(name="level", type=StringType)
aS3_qualifier.attributes={aS3_qualifier_level}

# aS3_simpleQualifiedIdentifier class attributes and methods

# nonAttributeQualifiedIdentifier class attributes and methods

# aS3_conditionalExpression class attributes and methods
aS3_conditionalExpression_op: Property = Property(name="op", type=StringType)
aS3_conditionalExpression.attributes={aS3_conditionalExpression_op}

# assignmentExpression class attributes and methods

# aS3_expressionQualifiedIdentifier class attributes and methods

# aS3_nonAttributeQualifiedIdentifier class attributes and methods

# qualifiedIdentifier class attributes and methods

# aS3_qualifiedIdentifier class attributes and methods

# aS3_namespaceName class attributes and methods
aS3_namespaceName_level: Property = Property(name="level", type=StringType)
aS3_namespaceName.attributes={aS3_namespaceName_level}

# qualifiedIdent class attributes and methods

# aS3_arrayLiteral class attributes and methods

# aS3_elementList class attributes and methods

# aS3_nonemptyElementList class attributes and methods

# elementList class attributes and methods

# Condition class attributes and methods

# DefaultXMLNamespaceStatement class attributes and methods

# ThrowStatement class attributes and methods

# CaseStatement class attributes and methods

# aS3_switchStatementList class attributes and methods

# aS3_expressionList class attributes and methods

# brackets class attributes and methods

# ExpressionStatement class attributes and methods

# forInClauseTail class attributes and methods

# element class attributes and methods

# nonemptyElementList class attributes and methods

# Expression class attributes and methods

# encapsulatedExpression class attributes and methods

# parameterDefault class attributes and methods

# aS3_conditionalSubExpression class attributes and methods

# aS3_logicalOrExpression class attributes and methods
aS3_logicalOrExpression_o: Property = Property(name="o", type=StringType)
aS3_logicalOrExpression.attributes={aS3_logicalOrExpression_o}

# conditionalExpression class attributes and methods

# aS3_logicalAndExpression class attributes and methods
aS3_logicalAndExpression_o: Property = Property(name="o", type=StringType)
aS3_logicalAndExpression.attributes={aS3_logicalAndExpression_o}

# aS3_bitwiseOrExpression class attributes and methods
aS3_bitwiseOrExpression_o: Property = Property(name="o", type=StringType)
aS3_bitwiseOrExpression.attributes={aS3_bitwiseOrExpression_o}

# aS3_bitwiseXorExpression class attributes and methods
aS3_bitwiseXorExpression_o: Property = Property(name="o", type=StringType)
aS3_bitwiseXorExpression.attributes={aS3_bitwiseXorExpression_o}

# aS3_bitwiseAndExpression class attributes and methods
aS3_bitwiseAndExpression_o: Property = Property(name="o", type=StringType)
aS3_bitwiseAndExpression.attributes={aS3_bitwiseAndExpression_o}

# aS3_equalityExpression class attributes and methods
aS3_equalityExpression_o: Property = Property(name="o", type=StringType)
aS3_equalityExpression.attributes={aS3_equalityExpression_o}

# aS3_relationalExpression class attributes and methods
aS3_relationalExpression_o: Property = Property(name="o", type=StringType)
aS3_relationalExpression.attributes={aS3_relationalExpression_o}

# aS3_shiftExpression class attributes and methods
aS3_shiftExpression_o: Property = Property(name="o", type=StringType)
aS3_shiftExpression.attributes={aS3_shiftExpression_o}

# aS3_additiveExpression class attributes and methods
aS3_additiveExpression_o: Property = Property(name="o", type=StringType)
aS3_additiveExpression.attributes={aS3_additiveExpression_o}

# aS3_multiplicativeExpression class attributes and methods
aS3_multiplicativeExpression_o: Property = Property(name="o", type=StringType)
aS3_multiplicativeExpression.attributes={aS3_multiplicativeExpression_o}

# aS3_unaryExpression class attributes and methods

# unaryExpressionNotPlusMinus class attributes and methods

# aS3_unaryExpressionNotPlusMinus class attributes and methods
aS3_unaryExpressionNotPlusMinus_in: Property = Property(name="in", type=StringType)
aS3_unaryExpressionNotPlusMinus_de: Property = Property(name="de", type=StringType)
aS3_unaryExpressionNotPlusMinus.attributes={aS3_unaryExpressionNotPlusMinus_in, aS3_unaryExpressionNotPlusMinus_de}

# aS3_postfixExpression class attributes and methods

# aS3_primaryExpression class attributes and methods

# aS3_e4xAttributeIdentifier class attributes and methods

# aS3_arguments class attributes and methods

# aS3_newExpression class attributes and methods

# aS3_encapsulatedExpression class attributes and methods

# expressionQualifiedIdentifier class attributes and methods

# aS3_regexpLiteral class attributes and methods
aS3_regexpLiteral_s: Property = Property(name="s", type=StringType)
aS3_regexpLiteral.attributes={aS3_regexpLiteral_s}

# aS3_fullNewSubexpression class attributes and methods
aS3_fullNewSubexpression_fnsd: Property = Property(name="fnsd", type=StringType)
aS3_fullNewSubexpression.attributes={aS3_fullNewSubexpression_fnsd}

# aS3_Condition class attributes and methods

# SwitchStatement class attributes and methods

# aS3_switchBlock class attributes and methods

# aS3_DefaultXMLNamespaceStatement class attributes and methods

# aS3_ExpressionStatement class attributes and methods

# aS3_parameterDeclarationList class attributes and methods

# aS3_parameterDeclaration class attributes and methods

# aS3_basicParameterDeclaration class attributes and methods

# parameterDeclaration class attributes and methods

# aS3_parameterDefault class attributes and methods

# aS3_parameterRestDeclaration class attributes and methods

# finallyBlock class attributes and methods

# aS3_ReturnStatement class attributes and methods

# aS3_IfStatement class attributes and methods

# aS3_ThrowStatement class attributes and methods

# aS3_TryStatement class attributes and methods

# aS3_finallyBlock class attributes and methods

# aS3_catchBlock class attributes and methods

# aS3_SwitchStatement class attributes and methods

# aS3_CaseStatement class attributes and methods

# aS3_DefaultStatement class attributes and methods

# aS3_ForEachStatement class attributes and methods

# aS3_forInClause class attributes and methods

# aS3_ForStatement class attributes and methods

# aS3_traditionalForClause class attributes and methods

# aS3_forInit class attributes and methods

# aS3_forCond class attributes and methods

# aS3_forIter class attributes and methods

# aS3_forInClauseDecl class attributes and methods

# aS3_forInClauseTail class attributes and methods

# aS3_WhileStatement class attributes and methods

# aS3_DoWhileStatement class attributes and methods

# aS3_WithStatement class attributes and methods

# aS3_XmlConstant class attributes and methods
aS3_XmlConstant_value: Property = Property(name="value", type=StringType)
aS3_XmlConstant.attributes={aS3_XmlConstant_value}

# aS3_RegexpConstant class attributes and methods

# aS3_NumberConstant class attributes and methods
aS3_NumberConstant_value: Property = Property(name="value", type=StringType)
aS3_NumberConstant.attributes={aS3_NumberConstant_value}

# aS3_StringConstant class attributes and methods
aS3_StringConstant_value: Property = Property(name="value", type=StringType)
aS3_StringConstant.attributes={aS3_StringConstant_value}

# aS3_BoolConstant class attributes and methods
aS3_BoolConstant_value: Property = Property(name="value", type=StringType)
aS3_BoolConstant.attributes={aS3_BoolConstant_value}

# aS3_Undefined class attributes and methods

# aS3_This class attributes and methods

# aS3_Null class attributes and methods

# aS3_SymbolRef class attributes and methods

# Relationships
annonFields24: BinaryAssociation = BinaryAssociation(
    name="annonFields24",
    ends={
        Property(name="aS3_annotationField", type=aS3_annotationFields, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_annotationFields25", type=aS3_annotationField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr26: BinaryAssociation = BinaryAssociation(
    name="expr26",
    ends={
        Property(name="aS3_Expression", type=aS3_annotationField, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_annotationField27", type=aS3_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
package0: BinaryAssociation = BinaryAssociation(
    name="package0",
    ends={
        Property(name="aS3_Package", type=aS3_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_Model", type=aS3_Package, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
imp1: BinaryAssociation = BinaryAssociation(
    name="imp1",
    ends={
        Property(name="aS3_Imports", type=aS3_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_Model2", type=aS3_Imports, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
members3: BinaryAssociation = BinaryAssociation(
    name="members3",
    ends={
        Property(name="aS3_EObject", type=aS3_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_Model4", type=aS3_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classes5: BinaryAssociation = BinaryAssociation(
    name="classes5",
    ends={
        Property(name="aS3_EObject7", type=aS3_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_Model6", type=aS3_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imp8: BinaryAssociation = BinaryAssociation(
    name="imp8",
    ends={
        Property(name="aS3_Imports10", type=aS3_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_Package9", type=aS3_Imports, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
directives11: BinaryAssociation = BinaryAssociation(
    name="directives11",
    ends={
        Property(name="aS3_directive", type=aS3_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_Package12", type=aS3_directive, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members13: BinaryAssociation = BinaryAssociation(
    name="members13",
    ends={
        Property(name="aS3_EObject15", type=aS3_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_Package14", type=aS3_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classes16: BinaryAssociation = BinaryAssociation(
    name="classes16",
    ends={
        Property(name="aS3_EObject18", type=aS3_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_Package17", type=aS3_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports19: BinaryAssociation = BinaryAssociation(
    name="imports19",
    ends={
        Property(name="aS3_Import", type=aS3_Imports, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_Imports20", type=aS3_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uses21: BinaryAssociation = BinaryAssociation(
    name="uses21",
    ends={
        Property(name="aS3_Uses", type=aS3_directive, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_directive22", type=aS3_Uses, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annonFields23: BinaryAssociation = BinaryAssociation(
    name="annonFields23",
    ends={
        Property(name="aS3_annotationFields", type=aS3_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_Annotation", type=aS3_annotationFields, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superclass58: BinaryAssociation = BinaryAssociation(
    name="superclass58",
    ends={
        Property(name="aS3_Class59", type=aS3_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_Class57", type=aS3_Class, multiplicity=Multiplicity(0, 1))
    }
)
types60: BinaryAssociation = BinaryAssociation(
    name="types60",
    ends={
        Property(name="aS3_Interface62", type=aS3_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_Class61", type=aS3_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
members63: BinaryAssociation = BinaryAssociation(
    name="members63",
    ends={
        Property(name="aS3_Member", type=aS3_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_Class64", type=aS3_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations28: BinaryAssociation = BinaryAssociation(
    name="annotations28",
    ends={
        Property(name="aS3_Annotation29", type=aS3_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_Interface", type=aS3_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superclass31: BinaryAssociation = BinaryAssociation(
    name="superclass31",
    ends={
        Property(name="aS3_Interface32", type=aS3_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_Interface30", type=aS3_Interface, multiplicity=Multiplicity(0, 1))
    }
)
members33: BinaryAssociation = BinaryAssociation(
    name="members33",
    ends={
        Property(name="aS3_InterfaceMethod", type=aS3_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_Interface34", type=aS3_InterfaceMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations35: BinaryAssociation = BinaryAssociation(
    name="annotations35",
    ends={
        Property(name="aS3_Annotation37", type=aS3_InterfaceMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_InterfaceMethod36", type=aS3_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifier38: BinaryAssociation = BinaryAssociation(
    name="modifier38",
    ends={
        Property(name="aS3_Modifier", type=aS3_InterfaceMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_InterfaceMethod39", type=aS3_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accessor40: BinaryAssociation = BinaryAssociation(
    name="accessor40",
    ends={
        Property(name="aS3_AccessorRole", type=aS3_InterfaceMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_InterfaceMethod41", type=aS3_AccessorRole, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
params42: BinaryAssociation = BinaryAssociation(
    name="params42",
    ends={
        Property(name="aS3_Parameter", type=aS3_InterfaceMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_InterfaceMethod43", type=aS3_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type44: BinaryAssociation = BinaryAssociation(
    name="type44",
    ends={
        Property(name="aS3_EObject46", type=aS3_InterfaceMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_InterfaceMethod45", type=aS3_EObject, multiplicity=Multiplicity(0, 1))
    }
)
func47: BinaryAssociation = BinaryAssociation(
    name="func47",
    ends={
        Property(name="aS3_functionCommon", type=aS3_functionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_functionExpression", type=aS3_functionCommon, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sig48: BinaryAssociation = BinaryAssociation(
    name="sig48",
    ends={
        Property(name="aS3_functionSignature", type=aS3_functionCommon, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_functionCommon49", type=aS3_functionSignature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block50: BinaryAssociation = BinaryAssociation(
    name="block50",
    ends={
        Property(name="aS3_Block", type=aS3_functionCommon, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_functionCommon51", type=aS3_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations52: BinaryAssociation = BinaryAssociation(
    name="annotations52",
    ends={
        Property(name="aS3_Annotation53", type=aS3_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_Class", type=aS3_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifier54: BinaryAssociation = BinaryAssociation(
    name="modifier54",
    ends={
        Property(name="aS3_Modifier56", type=aS3_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_Class55", type=aS3_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements87: BinaryAssociation = BinaryAssociation(
    name="statements87",
    ends={
        Property(name="aS3_Statement", type=aS3_MethodBody, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_MethodBody", type=aS3_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
var65: BinaryAssociation = BinaryAssociation(
    name="var65",
    ends={
        Property(name="aS3_MemberVariableDeclaration", type=aS3_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_Member66", type=aS3_MemberVariableDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
meth67: BinaryAssociation = BinaryAssociation(
    name="meth67",
    ends={
        Property(name="aS3_Method", type=aS3_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_Member68", type=aS3_Method, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations69: BinaryAssociation = BinaryAssociation(
    name="annotations69",
    ends={
        Property(name="aS3_Annotation71", type=aS3_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_Method70", type=aS3_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifier72: BinaryAssociation = BinaryAssociation(
    name="modifier72",
    ends={
        Property(name="aS3_Modifier74", type=aS3_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_Method73", type=aS3_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accessor75: BinaryAssociation = BinaryAssociation(
    name="accessor75",
    ends={
        Property(name="aS3_AccessorRole77", type=aS3_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_Method76", type=aS3_AccessorRole, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
params78: BinaryAssociation = BinaryAssociation(
    name="params78",
    ends={
        Property(name="aS3_Parameter80", type=aS3_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_Method79", type=aS3_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type81: BinaryAssociation = BinaryAssociation(
    name="type81",
    ends={
        Property(name="aS3_EObject83", type=aS3_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_Method82", type=aS3_EObject, multiplicity=Multiplicity(0, 1))
    }
)
body84: BinaryAssociation = BinaryAssociation(
    name="body84",
    ends={
        Property(name="aS3_Block86", type=aS3_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_Method85", type=aS3_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lf110: BinaryAssociation = BinaryAssociation(
    name="lf110",
    ends={
        Property(name="aS3_literalField", type=aS3_fieldList, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_fieldList111", type=aS3_literalField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fields112: BinaryAssociation = BinaryAssociation(
    name="fields112",
    ends={
        Property(name="aS3_literalField114", type=aS3_fieldList, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_fieldList113", type=aS3_literalField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name115: BinaryAssociation = BinaryAssociation(
    name="name115",
    ends={
        Property(name="aS3_fieldName", type=aS3_literalField, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_literalField116", type=aS3_fieldName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations88: BinaryAssociation = BinaryAssociation(
    name="annotations88",
    ends={
        Property(name="aS3_Annotation90", type=aS3_MemberVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_MemberVariableDeclaration89", type=aS3_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifier91: BinaryAssociation = BinaryAssociation(
    name="modifier91",
    ends={
        Property(name="aS3_Modifier93", type=aS3_MemberVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_MemberVariableDeclaration92", type=aS3_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type94: BinaryAssociation = BinaryAssociation(
    name="type94",
    ends={
        Property(name="aS3_EObject96", type=aS3_MemberVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_MemberVariableDeclaration95", type=aS3_EObject, multiplicity=Multiplicity(0, 1))
    }
)
Expression97: BinaryAssociation = BinaryAssociation(
    name="Expression97",
    ends={
        Property(name="aS3_assignmentExpression", type=aS3_MemberVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_MemberVariableDeclaration98", type=aS3_assignmentExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type99: BinaryAssociation = BinaryAssociation(
    name="type99",
    ends={
        Property(name="aS3_EObject100", type=aS3_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_VariableDeclaration", type=aS3_EObject, multiplicity=Multiplicity(0, 1))
    }
)
Expression101: BinaryAssociation = BinaryAssociation(
    name="Expression101",
    ends={
        Property(name="aS3_assignmentExpression103", type=aS3_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_VariableDeclaration102", type=aS3_assignmentExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type104: BinaryAssociation = BinaryAssociation(
    name="type104",
    ends={
        Property(name="aS3_EObject106", type=aS3_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_Parameter105", type=aS3_EObject, multiplicity=Multiplicity(0, 1))
    }
)
lit107: BinaryAssociation = BinaryAssociation(
    name="lit107",
    ends={
        Property(name="aS3_exprOrObjectLiteral", type=aS3_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_Parameter108", type=aS3_exprOrObjectLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fields109: BinaryAssociation = BinaryAssociation(
    name="fields109",
    ends={
        Property(name="aS3_fieldList", type=aS3_objectLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_objectLiteral", type=aS3_fieldList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
proId132: BinaryAssociation = BinaryAssociation(
    name="proId132",
    ends={
        Property(name="aS3_propertyIdentifier", type=aS3_simpleQualifiedIdentifier, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_simpleQualifiedIdentifier", type=aS3_propertyIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qual133: BinaryAssociation = BinaryAssociation(
    name="qual133",
    ends={
        Property(name="aS3_qualifier", type=aS3_simpleQualifiedIdentifier, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_simpleQualifiedIdentifier134", type=aS3_qualifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
piden135: BinaryAssociation = BinaryAssociation(
    name="piden135",
    ends={
        Property(name="aS3_propertyIdentifier137", type=aS3_simpleQualifiedIdentifier, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_simpleQualifiedIdentifier136", type=aS3_propertyIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
el117: BinaryAssociation = BinaryAssociation(
    name="el117",
    ends={
        Property(name="aS3_element", type=aS3_literalField, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_literalField118", type=aS3_element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identi119: BinaryAssociation = BinaryAssociation(
    name="identi119",
    ends={
        Property(name="aS3_identi", type=aS3_fieldName, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_fieldName120", type=aS3_identi, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ide121: BinaryAssociation = BinaryAssociation(
    name="ide121",
    ends={
        Property(name="aS3_identi122", type=aS3_qualifiedIdent, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_qualifiedIdent", type=aS3_identi, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type123: BinaryAssociation = BinaryAssociation(
    name="type123",
    ends={
        Property(name="aS3_typeExpression", type=aS3_identi, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_identi124", type=aS3_typeExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block125: BinaryAssociation = BinaryAssociation(
    name="block125",
    ends={
        Property(name="aS3_Block127", type=aS3_identi, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_identi126", type=aS3_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qual128: BinaryAssociation = BinaryAssociation(
    name="qual128",
    ends={
        Property(name="aS3_qualifiedIdent129", type=aS3_identifier, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_identifier", type=aS3_qualifiedIdent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
poi130: BinaryAssociation = BinaryAssociation(
    name="poi130",
    ends={
        Property(name="aS3_propOrIdent", type=aS3_identifier, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_identifier131", type=aS3_propOrIdent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bra138: BinaryAssociation = BinaryAssociation(
    name="bra138",
    ends={
        Property(name="aS3_brackets", type=aS3_simpleQualifiedIdentifier, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_simpleQualifiedIdentifier139", type=aS3_brackets, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
list140: BinaryAssociation = BinaryAssociation(
    name="list140",
    ends={
        Property(name="aS3_elementList", type=aS3_arrayLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_arrayLiteral", type=aS3_elementList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
l141: BinaryAssociation = BinaryAssociation(
    name="l141",
    ends={
        Property(name="aS3_switchStatementList", type=aS3_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_Expression142", type=aS3_switchStatementList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr143: BinaryAssociation = BinaryAssociation(
    name="expr143",
    ends={
        Property(name="aS3_assignmentExpression144", type=aS3_expressionList, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_expressionList", type=aS3_assignmentExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr145: BinaryAssociation = BinaryAssociation(
    name="expr145",
    ends={
        Property(name="aS3_EObject147", type=aS3_assignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_assignmentExpression146", type=aS3_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
aexpr148: BinaryAssociation = BinaryAssociation(
    name="aexpr148",
    ends={
        Property(name="aS3_Expression149", type=aS3_conditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_conditionalExpression", type=aS3_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr1150: BinaryAssociation = BinaryAssociation(
    name="expr1150",
    ends={
        Property(name="aS3_assignmentExpression151", type=aS3_conditionalSubExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_conditionalSubExpression", type=aS3_assignmentExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr2152: BinaryAssociation = BinaryAssociation(
    name="expr2152",
    ends={
        Property(name="aS3_assignmentExpression154", type=aS3_conditionalSubExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_conditionalSubExpression153", type=aS3_assignmentExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cond155: BinaryAssociation = BinaryAssociation(
    name="cond155",
    ends={
        Property(name="aS3_conditionalSubExpression156", type=aS3_logicalOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_logicalOrExpression", type=aS3_conditionalSubExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr157: BinaryAssociation = BinaryAssociation(
    name="expr157",
    ends={
        Property(name="aS3_bitwiseOrExpression", type=aS3_logicalAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_logicalAndExpression", type=aS3_bitwiseOrExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr170: BinaryAssociation = BinaryAssociation(
    name="expr170",
    ends={
        Property(name="aS3_additiveExpression171", type=aS3_multiplicativeExpression, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="aS3_multiplicativeExpression", type=aS3_additiveExpression, multiplicity=Multiplicity(1, 1))
    }
)
expr158: BinaryAssociation = BinaryAssociation(
    name="expr158",
    ends={
        Property(name="aS3_bitwiseXorExpression", type=aS3_bitwiseOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_bitwiseOrExpression159", type=aS3_bitwiseXorExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr160: BinaryAssociation = BinaryAssociation(
    name="expr160",
    ends={
        Property(name="aS3_bitwiseAndExpression", type=aS3_bitwiseXorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_bitwiseXorExpression161", type=aS3_bitwiseAndExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr162: BinaryAssociation = BinaryAssociation(
    name="expr162",
    ends={
        Property(name="aS3_equalityExpression", type=aS3_bitwiseAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_bitwiseAndExpression163", type=aS3_equalityExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr164: BinaryAssociation = BinaryAssociation(
    name="expr164",
    ends={
        Property(name="aS3_relationalExpression", type=aS3_equalityExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_equalityExpression165", type=aS3_relationalExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr166: BinaryAssociation = BinaryAssociation(
    name="expr166",
    ends={
        Property(name="aS3_shiftExpression", type=aS3_relationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_relationalExpression167", type=aS3_shiftExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr168: BinaryAssociation = BinaryAssociation(
    name="expr168",
    ends={
        Property(name="aS3_additiveExpression", type=aS3_shiftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_shiftExpression169", type=aS3_additiveExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr172: BinaryAssociation = BinaryAssociation(
    name="expr172",
    ends={
        Property(name="aS3_unaryExpression", type=aS3_multiplicativeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_multiplicativeExpression173", type=aS3_unaryExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr175: BinaryAssociation = BinaryAssociation(
    name="expr175",
    ends={
        Property(name="aS3_unaryExpression176", type=aS3_unaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_unaryExpression174", type=aS3_unaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
uaem178: BinaryAssociation = BinaryAssociation(
    name="uaem178",
    ends={
        Property(name="aS3_unaryExpression179", type=aS3_unaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_unaryExpression177", type=aS3_unaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
uaep181: BinaryAssociation = BinaryAssociation(
    name="uaep181",
    ends={
        Property(name="aS3_unaryExpression182", type=aS3_unaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_unaryExpression180", type=aS3_unaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
uaenpm183: BinaryAssociation = BinaryAssociation(
    name="uaenpm183",
    ends={
        Property(name="aS3_unaryExpressionNotPlusMinus", type=aS3_unaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_unaryExpression184", type=aS3_unaryExpressionNotPlusMinus, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
peexpr185: BinaryAssociation = BinaryAssociation(
    name="peexpr185",
    ends={
        Property(name="aS3_primaryExpression", type=aS3_postfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_postfixExpression", type=aS3_primaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pepoi186: BinaryAssociation = BinaryAssociation(
    name="pepoi186",
    ends={
        Property(name="aS3_propOrIdent188", type=aS3_postfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_postfixExpression187", type=aS3_propOrIdent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr189: BinaryAssociation = BinaryAssociation(
    name="expr189",
    ends={
        Property(name="aS3_Expression191", type=aS3_postfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_postfixExpression190", type=aS3_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pewi192: BinaryAssociation = BinaryAssociation(
    name="pewi192",
    ends={
        Property(name="aS3_qualifiedIdentifier", type=aS3_postfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_postfixExpression193", type=aS3_qualifiedIdentifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
e4x194: BinaryAssociation = BinaryAssociation(
    name="e4x194",
    ends={
        Property(name="aS3_e4xAttributeIdentifier", type=aS3_postfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_postfixExpression195", type=aS3_e4xAttributeIdentifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
args196: BinaryAssociation = BinaryAssociation(
    name="args196",
    ends={
        Property(name="aS3_arguments", type=aS3_postfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_postfixExpression197", type=aS3_arguments, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exprList198: BinaryAssociation = BinaryAssociation(
    name="exprList198",
    ends={
        Property(name="aS3_expressionList200", type=aS3_arguments, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_arguments199", type=aS3_expressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qual201: BinaryAssociation = BinaryAssociation(
    name="qual201",
    ends={
        Property(name="aS3_qualifiedIdent203", type=aS3_e4xAttributeIdentifier, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_e4xAttributeIdentifier202", type=aS3_qualifiedIdent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr204: BinaryAssociation = BinaryAssociation(
    name="expr204",
    ends={
        Property(name="aS3_Expression206", type=aS3_e4xAttributeIdentifier, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_e4xAttributeIdentifier205", type=aS3_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propId229: BinaryAssociation = BinaryAssociation(
    name="propId229",
    ends={
        Property(name="aS3_qualifiedIdent231", type=aS3_propOrIdent, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_propOrIdent230", type=aS3_qualifiedIdent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superExpr207: BinaryAssociation = BinaryAssociation(
    name="superExpr207",
    ends={
        Property(name="aS3_Expression209", type=aS3_primaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_primaryExpression208", type=aS3_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
con210: BinaryAssociation = BinaryAssociation(
    name="con210",
    ends={
        Property(name="aS3_Expression212", type=aS3_primaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_primaryExpression211", type=aS3_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lit213: BinaryAssociation = BinaryAssociation(
    name="lit213",
    ends={
        Property(name="aS3_EObject215", type=aS3_primaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_primaryExpression214", type=aS3_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fexpr216: BinaryAssociation = BinaryAssociation(
    name="fexpr216",
    ends={
        Property(name="aS3_functionExpression218", type=aS3_primaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_primaryExpression217", type=aS3_functionExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nexpr219: BinaryAssociation = BinaryAssociation(
    name="nexpr219",
    ends={
        Property(name="aS3_newExpression", type=aS3_primaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_primaryExpression220", type=aS3_newExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
encexpr221: BinaryAssociation = BinaryAssociation(
    name="encexpr221",
    ends={
        Property(name="aS3_encapsulatedExpression", type=aS3_primaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_primaryExpression222", type=aS3_encapsulatedExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
e4x223: BinaryAssociation = BinaryAssociation(
    name="e4x223",
    ends={
        Property(name="aS3_e4xAttributeIdentifier225", type=aS3_primaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_primaryExpression224", type=aS3_e4xAttributeIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qual226: BinaryAssociation = BinaryAssociation(
    name="qual226",
    ends={
        Property(name="aS3_qualifiedIdent228", type=aS3_primaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_primaryExpression227", type=aS3_qualifiedIdent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type232: BinaryAssociation = BinaryAssociation(
    name="type232",
    ends={
        Property(name="aS3_EObject234", type=aS3_newExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_newExpression233", type=aS3_EObject, multiplicity=Multiplicity(0, 1))
    }
)
args235: BinaryAssociation = BinaryAssociation(
    name="args235",
    ends={
        Property(name="aS3_arguments237", type=aS3_newExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_newExpression236", type=aS3_arguments, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr238: BinaryAssociation = BinaryAssociation(
    name="expr238",
    ends={
        Property(name="aS3_primaryExpression239", type=aS3_fullNewSubexpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_fullNewSubexpression", type=aS3_primaryExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
quali240: BinaryAssociation = BinaryAssociation(
    name="quali240",
    ends={
        Property(name="aS3_qualifiedIdent242", type=aS3_fullNewSubexpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_fullNewSubexpression241", type=aS3_qualifiedIdent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
brack243: BinaryAssociation = BinaryAssociation(
    name="brack243",
    ends={
        Property(name="aS3_brackets245", type=aS3_fullNewSubexpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_fullNewSubexpression244", type=aS3_brackets, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
switch272: BinaryAssociation = BinaryAssociation(
    name="switch272",
    ends={
        Property(name="aS3_switchBlock", type=aS3_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_Condition", type=aS3_switchBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assert273: BinaryAssociation = BinaryAssociation(
    name="assert273",
    ends={
        Property(name="aS3_Condition275", type=aS3_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_Statement274", type=aS3_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pden246: BinaryAssociation = BinaryAssociation(
    name="pden246",
    ends={
        Property(name="aS3_propertyIdentifier248", type=aS3_encapsulatedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_encapsulatedExpression247", type=aS3_propertyIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bra249: BinaryAssociation = BinaryAssociation(
    name="bra249",
    ends={
        Property(name="aS3_brackets251", type=aS3_encapsulatedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_encapsulatedExpression250", type=aS3_brackets, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
param252: BinaryAssociation = BinaryAssociation(
    name="param252",
    ends={
        Property(name="aS3_parameterDeclarationList", type=aS3_functionSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_functionSignature253", type=aS3_parameterDeclarationList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type254: BinaryAssociation = BinaryAssociation(
    name="type254",
    ends={
        Property(name="aS3_typeExpression256", type=aS3_functionSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_functionSignature255", type=aS3_typeExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identi257: BinaryAssociation = BinaryAssociation(
    name="identi257",
    ends={
        Property(name="aS3_EObject259", type=aS3_typeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_typeExpression258", type=aS3_EObject, multiplicity=Multiplicity(0, 1))
    }
)
params260: BinaryAssociation = BinaryAssociation(
    name="params260",
    ends={
        Property(name="aS3_Parameter262", type=aS3_parameterDeclarationList, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_parameterDeclarationList261", type=aS3_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name263: BinaryAssociation = BinaryAssociation(
    name="name263",
    ends={
        Property(name="aS3_identi264", type=aS3_parameterDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_parameterDeclaration", type=aS3_identi, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type265: BinaryAssociation = BinaryAssociation(
    name="type265",
    ends={
        Property(name="aS3_typeExpression266", type=aS3_basicParameterDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_basicParameterDeclaration", type=aS3_typeExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
param267: BinaryAssociation = BinaryAssociation(
    name="param267",
    ends={
        Property(name="aS3_parameterDefault", type=aS3_basicParameterDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_basicParameterDeclaration268", type=aS3_parameterDefault, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements269: BinaryAssociation = BinaryAssociation(
    name="statements269",
    ends={
        Property(name="aS3_Statement271", type=aS3_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_Block270", type=aS3_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cond276: BinaryAssociation = BinaryAssociation(
    name="cond276",
    ends={
        Property(name="aS3_Condition277", type=aS3_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_IfStatement", type=aS3_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement278: BinaryAssociation = BinaryAssociation(
    name="statement278",
    ends={
        Property(name="aS3_Statement280", type=aS3_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_IfStatement279", type=aS3_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
else281: BinaryAssociation = BinaryAssociation(
    name="else281",
    ends={
        Property(name="aS3_Statement283", type=aS3_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_IfStatement282", type=aS3_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block284: BinaryAssociation = BinaryAssociation(
    name="block284",
    ends={
        Property(name="aS3_Block285", type=aS3_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_TryStatement", type=aS3_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
finally286: BinaryAssociation = BinaryAssociation(
    name="finally286",
    ends={
        Property(name="aS3_finallyBlock", type=aS3_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_TryStatement287", type=aS3_finallyBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
catch288: BinaryAssociation = BinaryAssociation(
    name="catch288",
    ends={
        Property(name="aS3_catchBlock", type=aS3_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_TryStatement289", type=aS3_catchBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr290: BinaryAssociation = BinaryAssociation(
    name="expr290",
    ends={
        Property(name="aS3_Expression291", type=aS3_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_ReturnStatement", type=aS3_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
case292: BinaryAssociation = BinaryAssociation(
    name="case292",
    ends={
        Property(name="aS3_CaseStatement", type=aS3_switchBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_switchBlock293", type=aS3_CaseStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
def294: BinaryAssociation = BinaryAssociation(
    name="def294",
    ends={
        Property(name="aS3_DefaultStatement", type=aS3_switchBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_switchBlock295", type=aS3_DefaultStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
l296: BinaryAssociation = BinaryAssociation(
    name="l296",
    ends={
        Property(name="aS3_switchStatementList298", type=aS3_DefaultStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_DefaultStatement297", type=aS3_switchStatementList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fsstate308: BinaryAssociation = BinaryAssociation(
    name="fsstate308",
    ends={
        Property(name="aS3_Statement310", type=aS3_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_ForStatement309", type=aS3_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements299: BinaryAssociation = BinaryAssociation(
    name="statements299",
    ends={
        Property(name="aS3_Statement301", type=aS3_switchStatementList, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_switchStatementList300", type=aS3_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fesfor302: BinaryAssociation = BinaryAssociation(
    name="fesfor302",
    ends={
        Property(name="aS3_forInClause", type=aS3_ForEachStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_ForEachStatement", type=aS3_forInClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fes303: BinaryAssociation = BinaryAssociation(
    name="fes303",
    ends={
        Property(name="aS3_Statement305", type=aS3_ForEachStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_ForEachStatement304", type=aS3_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
forIn306: BinaryAssociation = BinaryAssociation(
    name="forIn306",
    ends={
        Property(name="aS3_forInClause307", type=aS3_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_ForStatement", type=aS3_forInClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ficdecl319: BinaryAssociation = BinaryAssociation(
    name="ficdecl319",
    ends={
        Property(name="aS3_forInClauseDecl", type=aS3_forInClause, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_forInClause320", type=aS3_forInClauseDecl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
traditionalForClause311: BinaryAssociation = BinaryAssociation(
    name="traditionalForClause311",
    ends={
        Property(name="aS3_traditionalForClause", type=aS3_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_ForStatement312", type=aS3_traditionalForClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
a313: BinaryAssociation = BinaryAssociation(
    name="a313",
    ends={
        Property(name="aS3_forInit", type=aS3_traditionalForClause, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_traditionalForClause314", type=aS3_forInit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
b315: BinaryAssociation = BinaryAssociation(
    name="b315",
    ends={
        Property(name="aS3_forCond", type=aS3_traditionalForClause, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_traditionalForClause316", type=aS3_forCond, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
c317: BinaryAssociation = BinaryAssociation(
    name="c317",
    ends={
        Property(name="aS3_forIter", type=aS3_traditionalForClause, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_traditionalForClause318", type=aS3_forIter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fiexpr332: BinaryAssociation = BinaryAssociation(
    name="fiexpr332",
    ends={
        Property(name="aS3_expressionList334", type=aS3_forIter, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_forIter333", type=aS3_expressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fictail321: BinaryAssociation = BinaryAssociation(
    name="fictail321",
    ends={
        Property(name="aS3_forInClauseTail", type=aS3_forInClause, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_forInClause322", type=aS3_forInClauseTail, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
decl323: BinaryAssociation = BinaryAssociation(
    name="decl323",
    ends={
        Property(name="aS3_VariableDeclaration325", type=aS3_forInit, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_forInit324", type=aS3_VariableDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr326: BinaryAssociation = BinaryAssociation(
    name="expr326",
    ends={
        Property(name="aS3_expressionList328", type=aS3_forInit, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_forInit327", type=aS3_expressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr329: BinaryAssociation = BinaryAssociation(
    name="expr329",
    ends={
        Property(name="aS3_expressionList331", type=aS3_forCond, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_forCond330", type=aS3_expressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cond335: BinaryAssociation = BinaryAssociation(
    name="cond335",
    ends={
        Property(name="aS3_Condition336", type=aS3_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_WhileStatement", type=aS3_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement337: BinaryAssociation = BinaryAssociation(
    name="statement337",
    ends={
        Property(name="aS3_Statement339", type=aS3_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_WhileStatement338", type=aS3_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
state340: BinaryAssociation = BinaryAssociation(
    name="state340",
    ends={
        Property(name="aS3_Statement341", type=aS3_DoWhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_DoWhileStatement", type=aS3_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value350: BinaryAssociation = BinaryAssociation(
    name="value350",
    ends={
        Property(name="aS3_regexpLiteral", type=aS3_RegexpConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_RegexpConstant", type=aS3_regexpLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cond342: BinaryAssociation = BinaryAssociation(
    name="cond342",
    ends={
        Property(name="aS3_Condition344", type=aS3_DoWhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_DoWhileStatement343", type=aS3_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cond345: BinaryAssociation = BinaryAssociation(
    name="cond345",
    ends={
        Property(name="aS3_Condition346", type=aS3_WithStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_WithStatement", type=aS3_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement347: BinaryAssociation = BinaryAssociation(
    name="statement347",
    ends={
        Property(name="aS3_Statement349", type=aS3_WithStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_WithStatement348", type=aS3_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
symbol351: BinaryAssociation = BinaryAssociation(
    name="symbol351",
    ends={
        Property(name="aS3_EObject352", type=aS3_SymbolRef, multiplicity=Multiplicity(1, 1)),
        Property(name="aS3_SymbolRef", type=aS3_EObject, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_aS3_VariableDeclaration_Statement = Generalization(general=Statement, specific=aS3_VariableDeclaration)
gen_aS3_VariableDeclaration_forInClauseDecl = Generalization(general=forInClauseDecl, specific=aS3_VariableDeclaration)
gen_aS3_objectLiteral_exprOrObjectLiteral = Generalization(general=exprOrObjectLiteral, specific=aS3_objectLiteral)
gen_aS3_identi_propertyIdentifier = Generalization(general=propertyIdentifier, specific=aS3_identi)
gen_aS3_identi_catchBlock = Generalization(general=catchBlock, specific=aS3_identi)
gen_aS3_identi_forInClauseDecl = Generalization(general=forInClauseDecl, specific=aS3_identi)
gen_aS3_propertyIdentifier_qualifier = Generalization(general=qualifier, specific=aS3_propertyIdentifier)
gen_aS3_simpleQualifiedIdentifier_nonAttributeQualifiedIdentifier = Generalization(general=nonAttributeQualifiedIdentifier, specific=aS3_simpleQualifiedIdentifier)
gen_aS3_conditionalExpression_assignmentExpression = Generalization(general=assignmentExpression, specific=aS3_conditionalExpression)
gen_aS3_expressionQualifiedIdentifier_nonAttributeQualifiedIdentifier = Generalization(general=nonAttributeQualifiedIdentifier, specific=aS3_expressionQualifiedIdentifier)
gen_aS3_nonAttributeQualifiedIdentifier_qualifiedIdentifier = Generalization(general=qualifiedIdentifier, specific=aS3_nonAttributeQualifiedIdentifier)
gen_aS3_namespaceName_qualifiedIdent = Generalization(general=qualifiedIdent, specific=aS3_namespaceName)
gen_aS3_nonemptyElementList_elementList = Generalization(general=elementList, specific=aS3_nonemptyElementList)
gen_aS3_Expression_exprOrObjectLiteral = Generalization(general=exprOrObjectLiteral, specific=aS3_Expression)
gen_aS3_Expression_Condition = Generalization(general=Condition, specific=aS3_Expression)
gen_aS3_Expression_DefaultXMLNamespaceStatement = Generalization(general=DefaultXMLNamespaceStatement, specific=aS3_Expression)
gen_aS3_Expression_ThrowStatement = Generalization(general=ThrowStatement, specific=aS3_Expression)
gen_aS3_Expression_CaseStatement = Generalization(general=CaseStatement, specific=aS3_Expression)
gen_aS3_expressionList_brackets = Generalization(general=brackets, specific=aS3_expressionList)
gen_aS3_expressionList_ExpressionStatement = Generalization(general=ExpressionStatement, specific=aS3_expressionList)
gen_aS3_expressionList_forInClauseTail = Generalization(general=forInClauseTail, specific=aS3_expressionList)
gen_aS3_assignmentExpression_element = Generalization(general=element, specific=aS3_assignmentExpression)
gen_aS3_assignmentExpression_nonemptyElementList = Generalization(general=nonemptyElementList, specific=aS3_assignmentExpression)
gen_aS3_assignmentExpression_Expression = Generalization(general=Expression, specific=aS3_assignmentExpression)
gen_aS3_assignmentExpression_encapsulatedExpression = Generalization(general=encapsulatedExpression, specific=aS3_assignmentExpression)
gen_aS3_assignmentExpression_parameterDefault = Generalization(general=parameterDefault, specific=aS3_assignmentExpression)
gen_aS3_logicalOrExpression_conditionalExpression = Generalization(general=conditionalExpression, specific=aS3_logicalOrExpression)
gen_aS3_unaryExpression_unaryExpressionNotPlusMinus = Generalization(general=unaryExpressionNotPlusMinus, specific=aS3_unaryExpression)
gen_aS3_postfixExpression_unaryExpressionNotPlusMinus = Generalization(general=unaryExpressionNotPlusMinus, specific=aS3_postfixExpression)
gen_aS3_e4xAttributeIdentifier_qualifiedIdentifier = Generalization(general=qualifiedIdentifier, specific=aS3_e4xAttributeIdentifier)
gen_aS3_encapsulatedExpression_expressionQualifiedIdentifier = Generalization(general=expressionQualifiedIdentifier, specific=aS3_encapsulatedExpression)
gen_aS3_Condition_SwitchStatement = Generalization(general=SwitchStatement, specific=aS3_Condition)
gen_aS3_DefaultXMLNamespaceStatement_Statement = Generalization(general=Statement, specific=aS3_DefaultXMLNamespaceStatement)
gen_aS3_ExpressionStatement_Statement = Generalization(general=Statement, specific=aS3_ExpressionStatement)
gen_aS3_basicParameterDeclaration_parameterDeclaration = Generalization(general=parameterDeclaration, specific=aS3_basicParameterDeclaration)
gen_aS3_parameterRestDeclaration_parameterDeclaration = Generalization(general=parameterDeclaration, specific=aS3_parameterRestDeclaration)
gen_aS3_Block_Statement = Generalization(general=Statement, specific=aS3_Block)
gen_aS3_Block_finallyBlock = Generalization(general=finallyBlock, specific=aS3_Block)
gen_aS3_ReturnStatement_Statement = Generalization(general=Statement, specific=aS3_ReturnStatement)
gen_aS3_IfStatement_Statement = Generalization(general=Statement, specific=aS3_IfStatement)
gen_aS3_ThrowStatement_Statement = Generalization(general=Statement, specific=aS3_ThrowStatement)
gen_aS3_TryStatement_Statement = Generalization(general=Statement, specific=aS3_TryStatement)
gen_aS3_SwitchStatement_Statement = Generalization(general=Statement, specific=aS3_SwitchStatement)
gen_aS3_ForEachStatement_Statement = Generalization(general=Statement, specific=aS3_ForEachStatement)
gen_aS3_ForStatement_Statement = Generalization(general=Statement, specific=aS3_ForStatement)
gen_aS3_WhileStatement_Statement = Generalization(general=Statement, specific=aS3_WhileStatement)
gen_aS3_DoWhileStatement_Statement = Generalization(general=Statement, specific=aS3_DoWhileStatement)
gen_aS3_WithStatement_Statement = Generalization(general=Statement, specific=aS3_WithStatement)
gen_aS3_XmlConstant_Expression = Generalization(general=Expression, specific=aS3_XmlConstant)
gen_aS3_RegexpConstant_Expression = Generalization(general=Expression, specific=aS3_RegexpConstant)
gen_aS3_NumberConstant_Expression = Generalization(general=Expression, specific=aS3_NumberConstant)
gen_aS3_StringConstant_Expression = Generalization(general=Expression, specific=aS3_StringConstant)
gen_aS3_BoolConstant_Expression = Generalization(general=Expression, specific=aS3_BoolConstant)
gen_aS3_Undefined_Expression = Generalization(general=Expression, specific=aS3_Undefined)
gen_aS3_This_Expression = Generalization(general=Expression, specific=aS3_This)
gen_aS3_Null_Expression = Generalization(general=Expression, specific=aS3_Null)
gen_aS3_SymbolRef_Expression = Generalization(general=Expression, specific=aS3_SymbolRef)

# Domain Model
domain_model = DomainModel(
    name="aS3",
    types={aS3_annotationField, aS3_Expression, aS3_Model, aS3_Package, aS3_Imports, aS3_EObject, aS3_directive, aS3_Import, aS3_Uses, aS3_Annotation, aS3_annotationFields, aS3_Member, aS3_Interface, aS3_InterfaceMethod, aS3_Modifier, aS3_AccessorRole, aS3_Parameter, aS3_functionExpression, aS3_functionCommon, aS3_functionSignature, aS3_Block, aS3_Class, aS3_MethodBody, aS3_Statement, aS3_MemberVariableDeclaration, aS3_Method, aS3_fieldName, aS3_element, aS3_assignmentExpression, aS3_VariableDeclaration, Statement, forInClauseDecl, aS3_exprOrObjectLiteral, aS3_objectLiteral, exprOrObjectLiteral, aS3_fieldList, aS3_literalField, aS3_brackets, aS3_identi, aS3_qualifiedIdent, propertyIdentifier, catchBlock, aS3_typeExpression, aS3_identifier, aS3_propOrIdent, aS3_propertyIdentifier, qualifier, aS3_qualifier, aS3_simpleQualifiedIdentifier, nonAttributeQualifiedIdentifier, aS3_conditionalExpression, assignmentExpression, aS3_expressionQualifiedIdentifier, aS3_nonAttributeQualifiedIdentifier, qualifiedIdentifier, aS3_qualifiedIdentifier, aS3_namespaceName, qualifiedIdent, aS3_arrayLiteral, aS3_elementList, aS3_nonemptyElementList, elementList, Condition, DefaultXMLNamespaceStatement, ThrowStatement, CaseStatement, aS3_switchStatementList, aS3_expressionList, brackets, ExpressionStatement, forInClauseTail, element, nonemptyElementList, Expression, encapsulatedExpression, parameterDefault, aS3_conditionalSubExpression, aS3_logicalOrExpression, conditionalExpression, aS3_logicalAndExpression, aS3_bitwiseOrExpression, aS3_bitwiseXorExpression, aS3_bitwiseAndExpression, aS3_equalityExpression, aS3_relationalExpression, aS3_shiftExpression, aS3_additiveExpression, aS3_multiplicativeExpression, aS3_unaryExpression, unaryExpressionNotPlusMinus, aS3_unaryExpressionNotPlusMinus, aS3_postfixExpression, aS3_primaryExpression, aS3_e4xAttributeIdentifier, aS3_arguments, aS3_newExpression, aS3_encapsulatedExpression, expressionQualifiedIdentifier, aS3_regexpLiteral, aS3_fullNewSubexpression, aS3_Condition, SwitchStatement, aS3_switchBlock, aS3_DefaultXMLNamespaceStatement, aS3_ExpressionStatement, aS3_parameterDeclarationList, aS3_parameterDeclaration, aS3_basicParameterDeclaration, parameterDeclaration, aS3_parameterDefault, aS3_parameterRestDeclaration, finallyBlock, aS3_ReturnStatement, aS3_IfStatement, aS3_ThrowStatement, aS3_TryStatement, aS3_finallyBlock, aS3_catchBlock, aS3_SwitchStatement, aS3_CaseStatement, aS3_DefaultStatement, aS3_ForEachStatement, aS3_forInClause, aS3_ForStatement, aS3_traditionalForClause, aS3_forInit, aS3_forCond, aS3_forIter, aS3_forInClauseDecl, aS3_forInClauseTail, aS3_WhileStatement, aS3_DoWhileStatement, aS3_WithStatement, aS3_XmlConstant, aS3_RegexpConstant, aS3_NumberConstant, aS3_StringConstant, aS3_BoolConstant, aS3_Undefined, aS3_This, aS3_Null, aS3_SymbolRef, AccessLevel},
    associations={annonFields24, expr26, package0, imp1, members3, classes5, imp8, directives11, members13, classes16, imports19, uses21, annonFields23, superclass58, types60, members63, annotations28, superclass31, members33, annotations35, modifier38, accessor40, params42, type44, func47, sig48, block50, annotations52, modifier54, statements87, var65, meth67, annotations69, modifier72, accessor75, params78, type81, body84, lf110, fields112, name115, annotations88, modifier91, type94, Expression97, type99, Expression101, type104, lit107, fields109, proId132, qual133, piden135, el117, identi119, ide121, type123, block125, qual128, poi130, bra138, list140, l141, expr143, expr145, aexpr148, expr1150, expr2152, cond155, expr157, expr170, expr158, expr160, expr162, expr164, expr166, expr168, expr172, expr175, uaem178, uaep181, uaenpm183, peexpr185, pepoi186, expr189, pewi192, e4x194, args196, exprList198, qual201, expr204, propId229, superExpr207, con210, lit213, fexpr216, nexpr219, encexpr221, e4x223, qual226, type232, args235, expr238, quali240, brack243, switch272, assert273, pden246, bra249, param252, type254, identi257, params260, name263, type265, param267, statements269, cond276, statement278, else281, block284, finally286, catch288, expr290, case292, def294, l296, fsstate308, statements299, fesfor302, fes303, forIn306, ficdecl319, traditionalForClause311, a313, b315, c317, fiexpr332, fictail321, decl323, expr326, expr329, cond335, statement337, state340, value350, cond342, cond345, statement347, symbol351},
    generalizations={gen_aS3_VariableDeclaration_Statement, gen_aS3_VariableDeclaration_forInClauseDecl, gen_aS3_objectLiteral_exprOrObjectLiteral, gen_aS3_identi_propertyIdentifier, gen_aS3_identi_catchBlock, gen_aS3_identi_forInClauseDecl, gen_aS3_propertyIdentifier_qualifier, gen_aS3_simpleQualifiedIdentifier_nonAttributeQualifiedIdentifier, gen_aS3_conditionalExpression_assignmentExpression, gen_aS3_expressionQualifiedIdentifier_nonAttributeQualifiedIdentifier, gen_aS3_nonAttributeQualifiedIdentifier_qualifiedIdentifier, gen_aS3_namespaceName_qualifiedIdent, gen_aS3_nonemptyElementList_elementList, gen_aS3_Expression_exprOrObjectLiteral, gen_aS3_Expression_Condition, gen_aS3_Expression_DefaultXMLNamespaceStatement, gen_aS3_Expression_ThrowStatement, gen_aS3_Expression_CaseStatement, gen_aS3_expressionList_brackets, gen_aS3_expressionList_ExpressionStatement, gen_aS3_expressionList_forInClauseTail, gen_aS3_assignmentExpression_element, gen_aS3_assignmentExpression_nonemptyElementList, gen_aS3_assignmentExpression_Expression, gen_aS3_assignmentExpression_encapsulatedExpression, gen_aS3_assignmentExpression_parameterDefault, gen_aS3_logicalOrExpression_conditionalExpression, gen_aS3_unaryExpression_unaryExpressionNotPlusMinus, gen_aS3_postfixExpression_unaryExpressionNotPlusMinus, gen_aS3_e4xAttributeIdentifier_qualifiedIdentifier, gen_aS3_encapsulatedExpression_expressionQualifiedIdentifier, gen_aS3_Condition_SwitchStatement, gen_aS3_DefaultXMLNamespaceStatement_Statement, gen_aS3_ExpressionStatement_Statement, gen_aS3_basicParameterDeclaration_parameterDeclaration, gen_aS3_parameterRestDeclaration_parameterDeclaration, gen_aS3_Block_Statement, gen_aS3_Block_finallyBlock, gen_aS3_ReturnStatement_Statement, gen_aS3_IfStatement_Statement, gen_aS3_ThrowStatement_Statement, gen_aS3_TryStatement_Statement, gen_aS3_SwitchStatement_Statement, gen_aS3_ForEachStatement_Statement, gen_aS3_ForStatement_Statement, gen_aS3_WhileStatement_Statement, gen_aS3_DoWhileStatement_Statement, gen_aS3_WithStatement_Statement, gen_aS3_XmlConstant_Expression, gen_aS3_RegexpConstant_Expression, gen_aS3_NumberConstant_Expression, gen_aS3_StringConstant_Expression, gen_aS3_BoolConstant_Expression, gen_aS3_Undefined_Expression, gen_aS3_This_Expression, gen_aS3_Null_Expression, gen_aS3_SymbolRef_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)