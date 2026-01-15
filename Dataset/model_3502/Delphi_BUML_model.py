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
delphi_ident = Class(name="delphi::ident")
delphi_program = Class(name="delphi::program")
file = Class(name="file")
delphi_identList = Class(name="delphi::identList")
delphi_programBlock = Class(name="delphi::programBlock")
delphi_unit = Class(name="delphi::unit")
delphi_interfaceSection = Class(name="delphi::interfaceSection")
delphi_implementationSection = Class(name="delphi::implementationSection")
delphi_initSection = Class(name="delphi::initSection")
delphi_packageDecl = Class(name="delphi::packageDecl")
delphi_requiresClause = Class(name="delphi::requiresClause")
delphi_containsClause = Class(name="delphi::containsClause")
delphi_mainRule = Class(name="delphi::mainRule")
CSTrace = Class(name="CSTrace")
delphi_file = Class(name="delphi::file")
delphi_block = Class(name="delphi::block")
delphi_interfaceDecl = Class(name="delphi::interfaceDecl")
delphi_exportedHeading = Class(name="delphi::exportedHeading")
interfaceDecl = Class(name="interfaceDecl")
delphi_procedureHeading = Class(name="delphi::procedureHeading")
delphi_directive = Class(name="delphi::directive")
delphi_functionHeading = Class(name="delphi::functionHeading")
delphi_declSection = Class(name="delphi::declSection")
delphi_library = Class(name="delphi::library")
delphi_usesClause = Class(name="delphi::usesClause")
delphi_compoundStmt = Class(name="delphi::compoundStmt")
delphi_exportsItem = Class(name="delphi::exportsItem")
delphi_constExpr = Class(name="delphi::constExpr")
delphi_labelDeclSection = Class(name="delphi::labelDeclSection")
declSection = Class(name="declSection")
delphi_constSection = Class(name="delphi::constSection")
delphi_constantDecl = Class(name="delphi::constantDecl")
delphi_exportsStmt = Class(name="delphi::exportsStmt")
delphi_type = Class(name="delphi::type")
delphi_restrictedType = Class(name="delphi::restrictedType")
delphi_arrayConstant = Class(name="delphi::arrayConstant")
delphi_recordConstant = Class(name="delphi::recordConstant")
delphi_recordFieldConstant = Class(name="delphi::recordFieldConstant")
delphi_typeId = Class(name="delphi::typeId")
delphi_typedConstant = Class(name="delphi::typedConstant")
delphi_typeSection = Class(name="delphi::typeSection")
delphi_typeDecl = Class(name="delphi::typeDecl")
delphi_simpleType = Class(name="delphi::simpleType")
delphi_realType = Class(name="delphi::realType")
simpleType = Class(name="simpleType")
delphi_ordinalType = Class(name="delphi::ordinalType")
delphi_ordIdent = Class(name="delphi::ordIdent")
ordinalType = Class(name="ordinalType")
delphi_variantType = Class(name="delphi::variantType")
delphi_subrangeType = Class(name="delphi::subrangeType")
delphi_enumeratedType = Class(name="delphi::enumeratedType")
delphi_enumeratedTypeElement = Class(name="delphi::enumeratedTypeElement")
delphi_stringType = Class(name="delphi::stringType")
delphi_classRefType = Class(name="delphi::classRefType")
type = Class(name="type")
delphi_recType = Class(name="delphi::recType")
delphi_fieldList = Class(name="delphi::fieldList")
delphi_fieldDecl = Class(name="delphi::fieldDecl")
delphi_variantSection = Class(name="delphi::variantSection")
delphi_recVariant = Class(name="delphi::recVariant")
delphi_strucType = Class(name="delphi::strucType")
delphi_arrayType = Class(name="delphi::arrayType")
strucType = Class(name="strucType")
delphi_fileType = Class(name="delphi::fileType")
delphi_pointerType = Class(name="delphi::pointerType")
delphi_procedureType = Class(name="delphi::procedureType")
delphi_varSection = Class(name="delphi::varSection")
delphi_varDecl = Class(name="delphi::varDecl")
delphi_setType = Class(name="delphi::setType")
delphi_expression = Class(name="delphi::expression")
delphi_simpleExpression = Class(name="delphi::simpleExpression")
expression = Class(name="expression")
delphi_term = Class(name="delphi::term")
simpleExpression = Class(name="simpleExpression")
delphi_factor = Class(name="delphi::factor")
term = Class(name="term")
delphi_designator = Class(name="delphi::designator")
delphi_exprList = Class(name="delphi::exprList")
delphi_setConstructor = Class(name="delphi::setConstructor")
delphi_relOp = Class(name="delphi::relOp")
delphi_addOp = Class(name="delphi::addOp")
delphi_mulOp = Class(name="delphi::mulOp")
delphi_designatorSubPart = Class(name="delphi::designatorSubPart")
delphi_designatorPart = Class(name="delphi::designatorPart")
delphi_stmtList = Class(name="delphi::stmtList")
delphi_statement = Class(name="delphi::statement")
delphi_unlabelledStatement = Class(name="delphi::unlabelledStatement")
delphi_simpleStatement = Class(name="delphi::simpleStatement")
unlabelledStatement = Class(name="unlabelledStatement")
delphi_structStmt = Class(name="delphi::structStmt")
structStmt = Class(name="structStmt")
delphi_conditionalStmt = Class(name="delphi::conditionalStmt")
delphi_ifStmt = Class(name="delphi::ifStmt")
conditionalStmt = Class(name="conditionalStmt")
delphi_reservedWord = Class(name="delphi::reservedWord")
delphi_setElement = Class(name="delphi::setElement")
delphi_caseLabel = Class(name="delphi::caseLabel")
delphi_loopStmt = Class(name="delphi::loopStmt")
delphi_repeatStmt = Class(name="delphi::repeatStmt")
loopStmt = Class(name="loopStmt")
delphi_whileStmt = Class(name="delphi::whileStmt")
delphi_forStmt = Class(name="delphi::forStmt")
delphi_qualId = Class(name="delphi::qualId")
delphi_caseStmt = Class(name="delphi::caseStmt")
delphi_caseSelector = Class(name="delphi::caseSelector")
delphi_exceptionBlock = Class(name="delphi::exceptionBlock")
delphi_procedureDecl = Class(name="delphi::procedureDecl")
procedureDeclSection = Class(name="procedureDeclSection")
delphi_functionDecl = Class(name="delphi::functionDecl")
methodHeading = Class(name="methodHeading")
delphi_withStmt = Class(name="delphi::withStmt")
delphi_formalParameters = Class(name="delphi::formalParameters")
delphi_tryStmt = Class(name="delphi::tryStmt")
delphi_raiseStmt = Class(name="delphi::raiseStmt")
delphi_assemblerStmt = Class(name="delphi::assemblerStmt")
delphi_procedureDeclSection = Class(name="delphi::procedureDeclSection")
delphi_constructorHeading = Class(name="delphi::constructorHeading")
delphi_destructorHeading = Class(name="delphi::destructorHeading")
delphi_formalParm = Class(name="delphi::formalParm")
delphi_parameter = Class(name="delphi::parameter")
delphi_objectType = Class(name="delphi::objectType")
restrictedType = Class(name="restrictedType")
delphi_objHeritage = Class(name="delphi::objHeritage")
delphi_objFieldList = Class(name="delphi::objFieldList")
delphi_methodList = Class(name="delphi::methodList")
delphi_methodHeading = Class(name="delphi::methodHeading")
delphi_classProperty = Class(name="delphi::classProperty")
delphi_propertyList = Class(name="delphi::propertyList")
delphi_classType = Class(name="delphi::classType")
delphi_classHeritage = Class(name="delphi::classHeritage")
delphi_classFieldList = Class(name="delphi::classFieldList")
delphi_classMethodList = Class(name="delphi::classMethodList")
delphi_classPropertyList = Class(name="delphi::classPropertyList")
delphi_classField = Class(name="delphi::classField")
delphi_classMethod = Class(name="delphi::classMethod")
delphi_propertyInterface = Class(name="delphi::propertyInterface")
delphi_propertySpecifiers = Class(name="delphi::propertySpecifiers")
delphi_propertyParameterList = Class(name="delphi::propertyParameterList")
objFieldList = Class(name="objFieldList")
classHeritage = Class(name="classHeritage")
delphi_interfaceType = Class(name="delphi::interfaceType")
delphi_interfaceHeritage = Class(name="delphi::interfaceHeritage")
delphi_relExp = Class(name="delphi::relExp")
delphi_unitId = Class(name="delphi::unitId")
pointerType = Class(name="pointerType")
delphi_recordConstExpr = Class(name="delphi::recordConstExpr")
delphi_simpleFactor = Class(name="delphi::simpleFactor")
factor = Class(name="factor")
delphi_adOp = Class(name="delphi::adOp")
addOp = Class(name="addOp")
delphi_assignmentStmnt = Class(name="delphi::assignmentStmnt")
simpleStatement = Class(name="simpleStatement")
delphi_addExp = Class(name="delphi::addExp")
delphi_multExp = Class(name="delphi::multExp")
delphi_ReservedId = Class(name="delphi::ReservedId")
delphi_MineID = Class(name="delphi::MineID")
delphi_ConstExp = Class(name="delphi::ConstExp")
constExpr = Class(name="constExpr")
delphi_callStmnt = Class(name="delphi::callStmnt")
delphi_inheritedStamnt = Class(name="delphi::inheritedStamnt")
delphi_gotoStmnt = Class(name="delphi::gotoStmnt")
delphi_parameterList = Class(name="delphi::parameterList")
parameter = Class(name="parameter")
delphi_parameterSimple = Class(name="delphi::parameterSimple")
delphi_MultipleId = Class(name="delphi::MultipleId")
ident = Class(name="ident")
delphi_MultipleConstExp = Class(name="delphi::MultipleConstExp")
delphi_RecordConstExp = Class(name="delphi::RecordConstExp")
delphi_CSTrace = Class(name="delphi::CSTrace", is_abstract=True)
delphi_Visitable = Class(name="delphi::Visitable")

# delphi_ident class attributes and methods

# delphi_program class attributes and methods

# file class attributes and methods

# delphi_identList class attributes and methods

# delphi_programBlock class attributes and methods

# delphi_unit class attributes and methods
delphi_unit_port: Property = Property(name="port", type=StringType)
delphi_unit.attributes={delphi_unit_port}

# delphi_interfaceSection class attributes and methods

# delphi_implementationSection class attributes and methods

# delphi_initSection class attributes and methods

# delphi_packageDecl class attributes and methods

# delphi_requiresClause class attributes and methods

# delphi_containsClause class attributes and methods

# delphi_mainRule class attributes and methods

# CSTrace class attributes and methods

# delphi_file class attributes and methods

# delphi_block class attributes and methods

# delphi_interfaceDecl class attributes and methods

# delphi_exportedHeading class attributes and methods

# interfaceDecl class attributes and methods

# delphi_procedureHeading class attributes and methods

# delphi_directive class attributes and methods
delphi_directive_dir: Property = Property(name="dir", type=StringType)
delphi_directive.attributes={delphi_directive_dir}

# delphi_functionHeading class attributes and methods

# delphi_declSection class attributes and methods

# delphi_library class attributes and methods

# delphi_usesClause class attributes and methods

# delphi_compoundStmt class attributes and methods

# delphi_exportsItem class attributes and methods

# delphi_constExpr class attributes and methods

# delphi_labelDeclSection class attributes and methods
delphi_labelDeclSection_id: Property = Property(name="id", type=StringType)
delphi_labelDeclSection.attributes={delphi_labelDeclSection_id}

# declSection class attributes and methods

# delphi_constSection class attributes and methods

# delphi_constantDecl class attributes and methods
delphi_constantDecl_port: Property = Property(name="port", type=StringType)
delphi_constantDecl.attributes={delphi_constantDecl_port}

# delphi_exportsStmt class attributes and methods

# delphi_type class attributes and methods

# delphi_restrictedType class attributes and methods

# delphi_arrayConstant class attributes and methods

# delphi_recordConstant class attributes and methods

# delphi_recordFieldConstant class attributes and methods

# delphi_typeId class attributes and methods

# delphi_typedConstant class attributes and methods

# delphi_typeSection class attributes and methods

# delphi_typeDecl class attributes and methods
delphi_typeDecl_port: Property = Property(name="port", type=StringType)
delphi_typeDecl.attributes={delphi_typeDecl_port}

# delphi_simpleType class attributes and methods

# delphi_realType class attributes and methods

# simpleType class attributes and methods

# delphi_ordinalType class attributes and methods

# delphi_ordIdent class attributes and methods

# ordinalType class attributes and methods

# delphi_variantType class attributes and methods

# delphi_subrangeType class attributes and methods

# delphi_enumeratedType class attributes and methods

# delphi_enumeratedTypeElement class attributes and methods

# delphi_stringType class attributes and methods

# delphi_classRefType class attributes and methods

# type class attributes and methods

# delphi_recType class attributes and methods

# delphi_fieldList class attributes and methods

# delphi_fieldDecl class attributes and methods
delphi_fieldDecl_port: Property = Property(name="port", type=StringType)
delphi_fieldDecl.attributes={delphi_fieldDecl_port}

# delphi_variantSection class attributes and methods

# delphi_recVariant class attributes and methods

# delphi_strucType class attributes and methods
delphi_strucType_port: Property = Property(name="port", type=StringType)
delphi_strucType.attributes={delphi_strucType_port}

# delphi_arrayType class attributes and methods

# strucType class attributes and methods

# delphi_fileType class attributes and methods

# delphi_pointerType class attributes and methods

# delphi_procedureType class attributes and methods

# delphi_varSection class attributes and methods

# delphi_varDecl class attributes and methods

# delphi_setType class attributes and methods

# delphi_expression class attributes and methods

# delphi_simpleExpression class attributes and methods

# expression class attributes and methods

# delphi_term class attributes and methods

# simpleExpression class attributes and methods

# delphi_factor class attributes and methods
delphi_factor_number: Property = Property(name="number", type=StringType)
delphi_factor_string: Property = Property(name="string", type=StringType)
delphi_factor.attributes={delphi_factor_string, delphi_factor_number}

# term class attributes and methods

# delphi_designator class attributes and methods

# delphi_exprList class attributes and methods

# delphi_setConstructor class attributes and methods

# delphi_relOp class attributes and methods
delphi_relOp_op: Property = Property(name="op", type=StringType)
delphi_relOp.attributes={delphi_relOp_op}

# delphi_addOp class attributes and methods

# delphi_mulOp class attributes and methods
delphi_mulOp_op: Property = Property(name="op", type=StringType)
delphi_mulOp.attributes={delphi_mulOp_op}

# delphi_designatorSubPart class attributes and methods

# delphi_designatorPart class attributes and methods
delphi_designatorPart_id: Property = Property(name="id", type=StringType)
delphi_designatorPart_id2: Property = Property(name="id2", type=StringType)
delphi_designatorPart.attributes={delphi_designatorPart_id2, delphi_designatorPart_id}

# delphi_stmtList class attributes and methods

# delphi_statement class attributes and methods
delphi_statement_labelId: Property = Property(name="labelId", type=StringType)
delphi_statement.attributes={delphi_statement_labelId}

# delphi_unlabelledStatement class attributes and methods

# delphi_simpleStatement class attributes and methods

# unlabelledStatement class attributes and methods

# delphi_structStmt class attributes and methods

# structStmt class attributes and methods

# delphi_conditionalStmt class attributes and methods

# delphi_ifStmt class attributes and methods

# conditionalStmt class attributes and methods

# delphi_reservedWord class attributes and methods
delphi_reservedWord_id: Property = Property(name="id", type=StringType)
delphi_reservedWord.attributes={delphi_reservedWord_id}

# delphi_setElement class attributes and methods

# delphi_caseLabel class attributes and methods

# delphi_loopStmt class attributes and methods

# delphi_repeatStmt class attributes and methods

# loopStmt class attributes and methods

# delphi_whileStmt class attributes and methods

# delphi_forStmt class attributes and methods

# delphi_qualId class attributes and methods

# delphi_caseStmt class attributes and methods

# delphi_caseSelector class attributes and methods

# delphi_exceptionBlock class attributes and methods

# delphi_procedureDecl class attributes and methods

# procedureDeclSection class attributes and methods

# delphi_functionDecl class attributes and methods

# methodHeading class attributes and methods

# delphi_withStmt class attributes and methods

# delphi_formalParameters class attributes and methods

# delphi_tryStmt class attributes and methods

# delphi_raiseStmt class attributes and methods
delphi_raiseStmt_raise: Property = Property(name="raise", type=StringType)
delphi_raiseStmt_at: Property = Property(name="at", type=StringType)
delphi_raiseStmt.attributes={delphi_raiseStmt_at, delphi_raiseStmt_raise}

# delphi_assemblerStmt class attributes and methods

# delphi_procedureDeclSection class attributes and methods
delphi_procedureDeclSection_port: Property = Property(name="port", type=StringType)
delphi_procedureDeclSection.attributes={delphi_procedureDeclSection_port}

# delphi_constructorHeading class attributes and methods

# delphi_destructorHeading class attributes and methods

# delphi_formalParm class attributes and methods

# delphi_parameter class attributes and methods

# delphi_objectType class attributes and methods

# restrictedType class attributes and methods

# delphi_objHeritage class attributes and methods

# delphi_objFieldList class attributes and methods

# delphi_methodList class attributes and methods

# delphi_methodHeading class attributes and methods

# delphi_classProperty class attributes and methods
delphi_classProperty_visibility: Property = Property(name="visibility", type=StringType)
delphi_classProperty.attributes={delphi_classProperty_visibility}

# delphi_propertyList class attributes and methods
delphi_propertyList_port: Property = Property(name="port", type=StringType)
delphi_propertyList.attributes={delphi_propertyList_port}

# delphi_classType class attributes and methods
delphi_classType_visibility: Property = Property(name="visibility", type=StringType)
delphi_classType.attributes={delphi_classType_visibility}

# delphi_classHeritage class attributes and methods

# delphi_classFieldList class attributes and methods

# delphi_classMethodList class attributes and methods

# delphi_classPropertyList class attributes and methods

# delphi_classField class attributes and methods
delphi_classField_visibility: Property = Property(name="visibility", type=StringType)
delphi_classField.attributes={delphi_classField_visibility}

# delphi_classMethod class attributes and methods
delphi_classMethod_visibility: Property = Property(name="visibility", type=StringType)
delphi_classMethod.attributes={delphi_classMethod_visibility}

# delphi_propertyInterface class attributes and methods

# delphi_propertySpecifiers class attributes and methods

# delphi_propertyParameterList class attributes and methods

# objFieldList class attributes and methods

# classHeritage class attributes and methods

# delphi_interfaceType class attributes and methods

# delphi_interfaceHeritage class attributes and methods

# delphi_relExp class attributes and methods

# delphi_unitId class attributes and methods
delphi_unitId_id: Property = Property(name="id", type=StringType)
delphi_unitId.attributes={delphi_unitId_id}

# pointerType class attributes and methods

# delphi_recordConstExpr class attributes and methods

# delphi_simpleFactor class attributes and methods

# factor class attributes and methods

# delphi_adOp class attributes and methods
delphi_adOp_op: Property = Property(name="op", type=StringType)
delphi_adOp.attributes={delphi_adOp_op}

# addOp class attributes and methods

# delphi_assignmentStmnt class attributes and methods
delphi_assignmentStmnt_operator: Property = Property(name="operator", type=StringType)
delphi_assignmentStmnt.attributes={delphi_assignmentStmnt_operator}

# simpleStatement class attributes and methods

# delphi_addExp class attributes and methods

# delphi_multExp class attributes and methods

# delphi_ReservedId class attributes and methods

# delphi_MineID class attributes and methods
delphi_MineID_first: Property = Property(name="first", type=StringType)
delphi_MineID_second: Property = Property(name="second", type=StringType)
delphi_MineID.attributes={delphi_MineID_second, delphi_MineID_first}

# delphi_ConstExp class attributes and methods

# constExpr class attributes and methods

# delphi_callStmnt class attributes and methods

# delphi_inheritedStamnt class attributes and methods

# delphi_gotoStmnt class attributes and methods
delphi_gotoStmnt_label: Property = Property(name="label", type=StringType)
delphi_gotoStmnt.attributes={delphi_gotoStmnt_label}

# delphi_parameterList class attributes and methods

# parameter class attributes and methods

# delphi_parameterSimple class attributes and methods

# delphi_MultipleId class attributes and methods
delphi_MultipleId_id: Property = Property(name="id", type=StringType)
delphi_MultipleId.attributes={delphi_MultipleId_id}

# ident class attributes and methods

# delphi_MultipleConstExp class attributes and methods

# delphi_RecordConstExp class attributes and methods

# delphi_CSTrace class attributes and methods

# delphi_Visitable class attributes and methods

# Relationships
file0: BinaryAssociation = BinaryAssociation(
    name="file0",
    ends={
        Property(name="delphi_mainRule", type=delphi_file, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="delphi_file", type=delphi_mainRule, multiplicity=Multiplicity(1, 1))
    }
)
id1: BinaryAssociation = BinaryAssociation(
    name="id1",
    ends={
        Property(name="delphi_ident", type=delphi_file, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_file2", type=delphi_ident, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
paramsList3: BinaryAssociation = BinaryAssociation(
    name="paramsList3",
    ends={
        Property(name="delphi_identList", type=delphi_program, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_program", type=delphi_identList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block4: BinaryAssociation = BinaryAssociation(
    name="block4",
    ends={
        Property(name="delphi_programBlock", type=delphi_program, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_program5", type=delphi_programBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interfaceSect6: BinaryAssociation = BinaryAssociation(
    name="interfaceSect6",
    ends={
        Property(name="delphi_interfaceSection", type=delphi_unit, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_unit", type=delphi_interfaceSection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
implementationSect7: BinaryAssociation = BinaryAssociation(
    name="implementationSect7",
    ends={
        Property(name="delphi_implementationSection", type=delphi_unit, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_unit8", type=delphi_implementationSection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initSect9: BinaryAssociation = BinaryAssociation(
    name="initSect9",
    ends={
        Property(name="delphi_initSection", type=delphi_unit, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_unit10", type=delphi_initSection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requires11: BinaryAssociation = BinaryAssociation(
    name="requires11",
    ends={
        Property(name="delphi_requiresClause", type=delphi_packageDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_packageDecl", type=delphi_requiresClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contains12: BinaryAssociation = BinaryAssociation(
    name="contains12",
    ends={
        Property(name="delphi_containsClause", type=delphi_packageDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_packageDecl13", type=delphi_containsClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block18: BinaryAssociation = BinaryAssociation(
    name="block18",
    ends={
        Property(name="delphi_block", type=delphi_programBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_programBlock19", type=delphi_block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
idList20: BinaryAssociation = BinaryAssociation(
    name="idList20",
    ends={
        Property(name="delphi_identList22", type=delphi_usesClause, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_usesClause21", type=delphi_identList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
uses23: BinaryAssociation = BinaryAssociation(
    name="uses23",
    ends={
        Property(name="delphi_usesClause25", type=delphi_interfaceSection, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_interfaceSection24", type=delphi_usesClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interfaceDecl26: BinaryAssociation = BinaryAssociation(
    name="interfaceDecl26",
    ends={
        Property(name="delphi_interfaceDecl", type=delphi_interfaceSection, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_interfaceSection27", type=delphi_interfaceDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pHeading28: BinaryAssociation = BinaryAssociation(
    name="pHeading28",
    ends={
        Property(name="delphi_procedureHeading", type=delphi_exportedHeading, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_exportedHeading", type=delphi_procedureHeading, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
directive29: BinaryAssociation = BinaryAssociation(
    name="directive29",
    ends={
        Property(name="delphi_directive", type=delphi_exportedHeading, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_exportedHeading30", type=delphi_directive, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fHeading31: BinaryAssociation = BinaryAssociation(
    name="fHeading31",
    ends={
        Property(name="delphi_functionHeading", type=delphi_exportedHeading, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_exportedHeading32", type=delphi_functionHeading, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
uses33: BinaryAssociation = BinaryAssociation(
    name="uses33",
    ends={
        Property(name="delphi_usesClause35", type=delphi_implementationSection, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_implementationSection34", type=delphi_usesClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declSect36: BinaryAssociation = BinaryAssociation(
    name="declSect36",
    ends={
        Property(name="delphi_declSection", type=delphi_implementationSection, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_implementationSection37", type=delphi_declSection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pBlock14: BinaryAssociation = BinaryAssociation(
    name="pBlock14",
    ends={
        Property(name="delphi_programBlock15", type=delphi_library, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_library", type=delphi_programBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
uses16: BinaryAssociation = BinaryAssociation(
    name="uses16",
    ends={
        Property(name="delphi_usesClause", type=delphi_programBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_programBlock17", type=delphi_usesClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
compound46: BinaryAssociation = BinaryAssociation(
    name="compound46",
    ends={
        Property(name="delphi_compoundStmt", type=delphi_block, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_block47", type=delphi_compoundStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id48: BinaryAssociation = BinaryAssociation(
    name="id48",
    ends={
        Property(name="delphi_ident49", type=delphi_exportsItem, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_exportsItem", type=delphi_ident, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constExp50: BinaryAssociation = BinaryAssociation(
    name="constExp50",
    ends={
        Property(name="delphi_constExpr", type=delphi_exportsItem, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_exportsItem51", type=delphi_constExpr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items52: BinaryAssociation = BinaryAssociation(
    name="items52",
    ends={
        Property(name="delphi_exportsItem54", type=delphi_exportsStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_exportsStmt53", type=delphi_exportsItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constantDecl55: BinaryAssociation = BinaryAssociation(
    name="constantDecl55",
    ends={
        Property(name="delphi_constantDecl", type=delphi_constSection, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_constSection", type=delphi_constantDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
id56: BinaryAssociation = BinaryAssociation(
    name="id56",
    ends={
        Property(name="delphi_ident58", type=delphi_constantDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_constantDecl57", type=delphi_ident, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
const59: BinaryAssociation = BinaryAssociation(
    name="const59",
    ends={
        Property(name="delphi_constExpr61", type=delphi_constantDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_constantDecl60", type=delphi_constExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exports38: BinaryAssociation = BinaryAssociation(
    name="exports38",
    ends={
        Property(name="delphi_exportsStmt", type=delphi_implementationSection, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_implementationSection39", type=delphi_exportsStmt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declSect40: BinaryAssociation = BinaryAssociation(
    name="declSect40",
    ends={
        Property(name="delphi_declSection42", type=delphi_block, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_block41", type=delphi_declSection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exports43: BinaryAssociation = BinaryAssociation(
    name="exports43",
    ends={
        Property(name="delphi_exportsStmt45", type=delphi_block, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_block44", type=delphi_exportsStmt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
id67: BinaryAssociation = BinaryAssociation(
    name="id67",
    ends={
        Property(name="delphi_ident69", type=delphi_typeDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_typeDecl68", type=delphi_ident, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type70: BinaryAssociation = BinaryAssociation(
    name="type70",
    ends={
        Property(name="delphi_type", type=delphi_typeDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_typeDecl71", type=delphi_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
restrictedType72: BinaryAssociation = BinaryAssociation(
    name="restrictedType72",
    ends={
        Property(name="delphi_restrictedType", type=delphi_typeDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_typeDecl73", type=delphi_restrictedType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
const74: BinaryAssociation = BinaryAssociation(
    name="const74",
    ends={
        Property(name="delphi_constExpr76", type=delphi_typedConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_typedConstant75", type=delphi_constExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
array77: BinaryAssociation = BinaryAssociation(
    name="array77",
    ends={
        Property(name="delphi_arrayConstant", type=delphi_typedConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_typedConstant78", type=delphi_arrayConstant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
record79: BinaryAssociation = BinaryAssociation(
    name="record79",
    ends={
        Property(name="delphi_recordConstant", type=delphi_typedConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_typedConstant80", type=delphi_recordConstant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typedConstant81: BinaryAssociation = BinaryAssociation(
    name="typedConstant81",
    ends={
        Property(name="delphi_typedConstant83", type=delphi_arrayConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_arrayConstant82", type=delphi_typedConstant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
recordField84: BinaryAssociation = BinaryAssociation(
    name="recordField84",
    ends={
        Property(name="delphi_recordFieldConstant", type=delphi_recordConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_recordConstant85", type=delphi_recordFieldConstant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
id86: BinaryAssociation = BinaryAssociation(
    name="id86",
    ends={
        Property(name="delphi_ident88", type=delphi_recordFieldConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_recordFieldConstant87", type=delphi_ident, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeRef62: BinaryAssociation = BinaryAssociation(
    name="typeRef62",
    ends={
        Property(name="delphi_typeId", type=delphi_constantDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_constantDecl63", type=delphi_typeId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typedConstat64: BinaryAssociation = BinaryAssociation(
    name="typedConstat64",
    ends={
        Property(name="delphi_typedConstant", type=delphi_constantDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_constantDecl65", type=delphi_typedConstant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeDecl66: BinaryAssociation = BinaryAssociation(
    name="typeDecl66",
    ends={
        Property(name="delphi_typeDecl", type=delphi_typeSection, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_typeSection", type=delphi_typeDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
first94: BinaryAssociation = BinaryAssociation(
    name="first94",
    ends={
        Property(name="delphi_constExpr95", type=delphi_subrangeType, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_subrangeType", type=delphi_constExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
last96: BinaryAssociation = BinaryAssociation(
    name="last96",
    ends={
        Property(name="delphi_constExpr98", type=delphi_subrangeType, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_subrangeType97", type=delphi_constExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
element99: BinaryAssociation = BinaryAssociation(
    name="element99",
    ends={
        Property(name="delphi_enumeratedTypeElement", type=delphi_enumeratedType, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_enumeratedType", type=delphi_enumeratedTypeElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
id100: BinaryAssociation = BinaryAssociation(
    name="id100",
    ends={
        Property(name="delphi_ident102", type=delphi_enumeratedTypeElement, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_enumeratedTypeElement101", type=delphi_ident, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
literalExp103: BinaryAssociation = BinaryAssociation(
    name="literalExp103",
    ends={
        Property(name="delphi_constExpr105", type=delphi_enumeratedTypeElement, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_enumeratedTypeElement104", type=delphi_constExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constExp106: BinaryAssociation = BinaryAssociation(
    name="constExp106",
    ends={
        Property(name="delphi_constExpr107", type=delphi_stringType, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_stringType", type=delphi_constExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typedConstant89: BinaryAssociation = BinaryAssociation(
    name="typedConstant89",
    ends={
        Property(name="delphi_typedConstant91", type=delphi_recordFieldConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_recordFieldConstant90", type=delphi_typedConstant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeRef92: BinaryAssociation = BinaryAssociation(
    name="typeRef92",
    ends={
        Property(name="delphi_typeId93", type=delphi_classRefType, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_classRefType", type=delphi_typeId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ordinalTyp109: BinaryAssociation = BinaryAssociation(
    name="ordinalTyp109",
    ends={
        Property(name="delphi_arrayType110", type=delphi_ordinalType, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="delphi_ordinalType111", type=delphi_arrayType, multiplicity=Multiplicity(1, 1))
    }
)
type112: BinaryAssociation = BinaryAssociation(
    name="type112",
    ends={
        Property(name="delphi_type114", type=delphi_arrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_arrayType113", type=delphi_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fields115: BinaryAssociation = BinaryAssociation(
    name="fields115",
    ends={
        Property(name="delphi_fieldList", type=delphi_recType, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_recType", type=delphi_fieldList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
field116: BinaryAssociation = BinaryAssociation(
    name="field116",
    ends={
        Property(name="delphi_fieldDecl", type=delphi_fieldList, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_fieldList117", type=delphi_fieldDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variantSect118: BinaryAssociation = BinaryAssociation(
    name="variantSect118",
    ends={
        Property(name="delphi_variantSection", type=delphi_fieldList, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_fieldList119", type=delphi_variantSection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
idList120: BinaryAssociation = BinaryAssociation(
    name="idList120",
    ends={
        Property(name="delphi_identList122", type=delphi_fieldDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_fieldDecl121", type=delphi_identList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type123: BinaryAssociation = BinaryAssociation(
    name="type123",
    ends={
        Property(name="delphi_type125", type=delphi_fieldDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_fieldDecl124", type=delphi_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id126: BinaryAssociation = BinaryAssociation(
    name="id126",
    ends={
        Property(name="delphi_ident128", type=delphi_variantSection, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_variantSection127", type=delphi_ident, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeRef129: BinaryAssociation = BinaryAssociation(
    name="typeRef129",
    ends={
        Property(name="delphi_typeId131", type=delphi_variantSection, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_variantSection130", type=delphi_typeId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
recVariants132: BinaryAssociation = BinaryAssociation(
    name="recVariants132",
    ends={
        Property(name="delphi_recVariant", type=delphi_variantSection, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_variantSection133", type=delphi_recVariant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ordinalType108: BinaryAssociation = BinaryAssociation(
    name="ordinalType108",
    ends={
        Property(name="delphi_ordinalType", type=delphi_arrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_arrayType", type=delphi_ordinalType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ordinal140: BinaryAssociation = BinaryAssociation(
    name="ordinal140",
    ends={
        Property(name="delphi_ordinalType141", type=delphi_setType, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_setType", type=delphi_ordinalType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeRef142: BinaryAssociation = BinaryAssociation(
    name="typeRef142",
    ends={
        Property(name="delphi_typeId143", type=delphi_fileType, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_fileType", type=delphi_typeId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pHeading144: BinaryAssociation = BinaryAssociation(
    name="pHeading144",
    ends={
        Property(name="delphi_procedureHeading145", type=delphi_procedureType, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_procedureType", type=delphi_procedureHeading, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fHeading146: BinaryAssociation = BinaryAssociation(
    name="fHeading146",
    ends={
        Property(name="delphi_functionHeading148", type=delphi_procedureType, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_procedureType147", type=delphi_functionHeading, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
varDecls149: BinaryAssociation = BinaryAssociation(
    name="varDecls149",
    ends={
        Property(name="delphi_varDecl", type=delphi_varSection, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_varSection", type=delphi_varDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
idList150: BinaryAssociation = BinaryAssociation(
    name="idList150",
    ends={
        Property(name="delphi_identList152", type=delphi_varDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_varDecl151", type=delphi_identList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type153: BinaryAssociation = BinaryAssociation(
    name="type153",
    ends={
        Property(name="delphi_type155", type=delphi_varDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_varDecl154", type=delphi_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constExp134: BinaryAssociation = BinaryAssociation(
    name="constExp134",
    ends={
        Property(name="delphi_constExpr136", type=delphi_recVariant, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_recVariant135", type=delphi_constExpr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fieldList137: BinaryAssociation = BinaryAssociation(
    name="fieldList137",
    ends={
        Property(name="delphi_fieldList139", type=delphi_recVariant, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_recVariant138", type=delphi_fieldList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
designator165: BinaryAssociation = BinaryAssociation(
    name="designator165",
    ends={
        Property(name="delphi_designator", type=delphi_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_factor", type=delphi_designator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expList166: BinaryAssociation = BinaryAssociation(
    name="expList166",
    ends={
        Property(name="delphi_exprList", type=delphi_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_factor167", type=delphi_exprList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
absId156: BinaryAssociation = BinaryAssociation(
    name="absId156",
    ends={
        Property(name="delphi_ident158", type=delphi_varDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_varDecl157", type=delphi_ident, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
absConst159: BinaryAssociation = BinaryAssociation(
    name="absConst159",
    ends={
        Property(name="delphi_constExpr161", type=delphi_varDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_varDecl160", type=delphi_constExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
absIniti162: BinaryAssociation = BinaryAssociation(
    name="absIniti162",
    ends={
        Property(name="delphi_constExpr164", type=delphi_varDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_varDecl163", type=delphi_constExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
setConstuctor173: BinaryAssociation = BinaryAssociation(
    name="setConstuctor173",
    ends={
        Property(name="delphi_setConstructor", type=delphi_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_factor174", type=delphi_setConstructor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeRef175: BinaryAssociation = BinaryAssociation(
    name="typeRef175",
    ends={
        Property(name="delphi_typeId177", type=delphi_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_factor176", type=delphi_typeId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subpart178: BinaryAssociation = BinaryAssociation(
    name="subpart178",
    ends={
        Property(name="delphi_designatorSubPart", type=delphi_designator, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_designator179", type=delphi_designatorSubPart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
designator181: BinaryAssociation = BinaryAssociation(
    name="designator181",
    ends={
        Property(name="delphi_designator182", type=delphi_designator, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_designator180", type=delphi_designator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
part183: BinaryAssociation = BinaryAssociation(
    name="part183",
    ends={
        Property(name="delphi_designatorPart", type=delphi_designatorSubPart, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_designatorSubPart184", type=delphi_designatorPart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprList185: BinaryAssociation = BinaryAssociation(
    name="exprList185",
    ends={
        Property(name="delphi_exprList187", type=delphi_designatorSubPart, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_designatorSubPart186", type=delphi_exprList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedExp168: BinaryAssociation = BinaryAssociation(
    name="nestedExp168",
    ends={
        Property(name="delphi_expression", type=delphi_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_factor169", type=delphi_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp170: BinaryAssociation = BinaryAssociation(
    name="exp170",
    ends={
        Property(name="delphi_expression172", type=delphi_factor, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_factor171", type=delphi_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
first192: BinaryAssociation = BinaryAssociation(
    name="first192",
    ends={
        Property(name="delphi_expression194", type=delphi_setElement, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_setElement193", type=delphi_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
last195: BinaryAssociation = BinaryAssociation(
    name="last195",
    ends={
        Property(name="delphi_expression197", type=delphi_setElement, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_setElement196", type=delphi_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exps198: BinaryAssociation = BinaryAssociation(
    name="exps198",
    ends={
        Property(name="delphi_expression200", type=delphi_exprList, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_exprList199", type=delphi_expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statments201: BinaryAssociation = BinaryAssociation(
    name="statments201",
    ends={
        Property(name="delphi_statement", type=delphi_stmtList, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_stmtList", type=delphi_statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement202: BinaryAssociation = BinaryAssociation(
    name="statement202",
    ends={
        Property(name="delphi_unlabelledStatement", type=delphi_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_statement203", type=delphi_unlabelledStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stamtList204: BinaryAssociation = BinaryAssociation(
    name="stamtList204",
    ends={
        Property(name="delphi_stmtList206", type=delphi_compoundStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_compoundStmt205", type=delphi_stmtList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition207: BinaryAssociation = BinaryAssociation(
    name="condition207",
    ends={
        Property(name="delphi_expression208", type=delphi_ifStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_ifStmt", type=delphi_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reservedWord188: BinaryAssociation = BinaryAssociation(
    name="reservedWord188",
    ends={
        Property(name="delphi_reservedWord", type=delphi_designatorPart, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_designatorPart189", type=delphi_reservedWord, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
element190: BinaryAssociation = BinaryAssociation(
    name="element190",
    ends={
        Property(name="delphi_setElement", type=delphi_setConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_setConstructor191", type=delphi_setElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
default219: BinaryAssociation = BinaryAssociation(
    name="default219",
    ends={
        Property(name="delphi_stmtList221", type=delphi_caseStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_caseStmt220", type=delphi_stmtList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
labels222: BinaryAssociation = BinaryAssociation(
    name="labels222",
    ends={
        Property(name="delphi_caseLabel", type=delphi_caseSelector, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_caseSelector223", type=delphi_caseLabel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stmt224: BinaryAssociation = BinaryAssociation(
    name="stmt224",
    ends={
        Property(name="delphi_statement226", type=delphi_caseSelector, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_caseSelector225", type=delphi_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
first227: BinaryAssociation = BinaryAssociation(
    name="first227",
    ends={
        Property(name="delphi_constExpr229", type=delphi_caseLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_caseLabel228", type=delphi_constExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
last230: BinaryAssociation = BinaryAssociation(
    name="last230",
    ends={
        Property(name="delphi_constExpr232", type=delphi_caseLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_caseLabel231", type=delphi_constExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stmt233: BinaryAssociation = BinaryAssociation(
    name="stmt233",
    ends={
        Property(name="delphi_statement234", type=delphi_loopStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_loopStmt", type=delphi_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition235: BinaryAssociation = BinaryAssociation(
    name="condition235",
    ends={
        Property(name="delphi_expression237", type=delphi_loopStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_loopStmt236", type=delphi_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
varId238: BinaryAssociation = BinaryAssociation(
    name="varId238",
    ends={
        Property(name="delphi_qualId", type=delphi_forStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_forStmt", type=delphi_qualId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
varInit239: BinaryAssociation = BinaryAssociation(
    name="varInit239",
    ends={
        Property(name="delphi_expression241", type=delphi_forStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_forStmt240", type=delphi_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then209: BinaryAssociation = BinaryAssociation(
    name="then209",
    ends={
        Property(name="delphi_statement211", type=delphi_ifStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_ifStmt210", type=delphi_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
else212: BinaryAssociation = BinaryAssociation(
    name="else212",
    ends={
        Property(name="delphi_statement214", type=delphi_ifStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_ifStmt213", type=delphi_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression215: BinaryAssociation = BinaryAssociation(
    name="expression215",
    ends={
        Property(name="delphi_expression216", type=delphi_caseStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_caseStmt", type=delphi_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cases217: BinaryAssociation = BinaryAssociation(
    name="cases217",
    ends={
        Property(name="delphi_caseSelector", type=delphi_caseStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_caseStmt218", type=delphi_caseSelector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stmtList247: BinaryAssociation = BinaryAssociation(
    name="stmtList247",
    ends={
        Property(name="delphi_stmtList248", type=delphi_tryStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_tryStmt", type=delphi_stmtList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exception249: BinaryAssociation = BinaryAssociation(
    name="exception249",
    ends={
        Property(name="delphi_exceptionBlock", type=delphi_tryStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_tryStmt250", type=delphi_exceptionBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
final251: BinaryAssociation = BinaryAssociation(
    name="final251",
    ends={
        Property(name="delphi_stmtList253", type=delphi_tryStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_tryStmt252", type=delphi_stmtList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exceptionId254: BinaryAssociation = BinaryAssociation(
    name="exceptionId254",
    ends={
        Property(name="delphi_ident256", type=delphi_exceptionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_exceptionBlock255", type=delphi_ident, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
heading271: BinaryAssociation = BinaryAssociation(
    name="heading271",
    ends={
        Property(name="delphi_procedureHeading272", type=delphi_procedureDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_procedureDecl", type=delphi_procedureHeading, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
heading273: BinaryAssociation = BinaryAssociation(
    name="heading273",
    ends={
        Property(name="delphi_functionHeading274", type=delphi_functionDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_functionDecl", type=delphi_functionHeading, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type275: BinaryAssociation = BinaryAssociation(
    name="type275",
    ends={
        Property(name="delphi_type277", type=delphi_functionHeading, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_functionHeading276", type=delphi_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vars242: BinaryAssociation = BinaryAssociation(
    name="vars242",
    ends={
        Property(name="delphi_identList243", type=delphi_withStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_withStmt", type=delphi_identList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stmt244: BinaryAssociation = BinaryAssociation(
    name="stmt244",
    ends={
        Property(name="delphi_statement246", type=delphi_withStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_withStmt245", type=delphi_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type257: BinaryAssociation = BinaryAssociation(
    name="type257",
    ends={
        Property(name="delphi_type259", type=delphi_exceptionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_exceptionBlock258", type=delphi_type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
doStmt260: BinaryAssociation = BinaryAssociation(
    name="doStmt260",
    ends={
        Property(name="delphi_statement262", type=delphi_exceptionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_exceptionBlock261", type=delphi_statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseStmts263: BinaryAssociation = BinaryAssociation(
    name="elseStmts263",
    ends={
        Property(name="delphi_stmtList265", type=delphi_exceptionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_exceptionBlock264", type=delphi_stmtList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
directive266: BinaryAssociation = BinaryAssociation(
    name="directive266",
    ends={
        Property(name="delphi_directive267", type=delphi_procedureDeclSection, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_procedureDeclSection", type=delphi_directive, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block268: BinaryAssociation = BinaryAssociation(
    name="block268",
    ends={
        Property(name="delphi_block270", type=delphi_procedureDeclSection, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_procedureDeclSection269", type=delphi_block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id300: BinaryAssociation = BinaryAssociation(
    name="id300",
    ends={
        Property(name="delphi_ident302", type=delphi_methodHeading, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_methodHeading301", type=delphi_ident, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParams303: BinaryAssociation = BinaryAssociation(
    name="formalParams303",
    ends={
        Property(name="delphi_formalParameters305", type=delphi_methodHeading, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_methodHeading304", type=delphi_formalParameters, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stmtList306: BinaryAssociation = BinaryAssociation(
    name="stmtList306",
    ends={
        Property(name="delphi_stmtList308", type=delphi_initSection, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_initSection307", type=delphi_stmtList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
params278: BinaryAssociation = BinaryAssociation(
    name="params278",
    ends={
        Property(name="delphi_formalParm", type=delphi_formalParameters, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_formalParameters", type=delphi_formalParm, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
param279: BinaryAssociation = BinaryAssociation(
    name="param279",
    ends={
        Property(name="delphi_parameter", type=delphi_formalParm, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_formalParm280", type=delphi_parameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type281: BinaryAssociation = BinaryAssociation(
    name="type281",
    ends={
        Property(name="delphi_type283", type=delphi_parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_parameter282", type=delphi_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
messageExp284: BinaryAssociation = BinaryAssociation(
    name="messageExp284",
    ends={
        Property(name="delphi_constExpr286", type=delphi_directive, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_directive285", type=delphi_constExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
heritage287: BinaryAssociation = BinaryAssociation(
    name="heritage287",
    ends={
        Property(name="delphi_objHeritage", type=delphi_objectType, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_objectType", type=delphi_objHeritage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fieldList288: BinaryAssociation = BinaryAssociation(
    name="fieldList288",
    ends={
        Property(name="delphi_objFieldList", type=delphi_objectType, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_objectType289", type=delphi_objFieldList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
methodList290: BinaryAssociation = BinaryAssociation(
    name="methodList290",
    ends={
        Property(name="delphi_methodList", type=delphi_objectType, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_objectType291", type=delphi_methodList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id292: BinaryAssociation = BinaryAssociation(
    name="id292",
    ends={
        Property(name="delphi_qualId294", type=delphi_objHeritage, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_objHeritage293", type=delphi_qualId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
heading295: BinaryAssociation = BinaryAssociation(
    name="heading295",
    ends={
        Property(name="delphi_methodHeading", type=delphi_methodList, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_methodList296", type=delphi_methodHeading, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
directive297: BinaryAssociation = BinaryAssociation(
    name="directive297",
    ends={
        Property(name="delphi_directive299", type=delphi_methodList, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_methodList298", type=delphi_directive, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property329: BinaryAssociation = BinaryAssociation(
    name="property329",
    ends={
        Property(name="delphi_classProperty", type=delphi_classPropertyList, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_classPropertyList330", type=delphi_classProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
propList331: BinaryAssociation = BinaryAssociation(
    name="propList331",
    ends={
        Property(name="delphi_propertyList", type=delphi_classProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_classProperty332", type=delphi_propertyList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
endStmtList309: BinaryAssociation = BinaryAssociation(
    name="endStmtList309",
    ends={
        Property(name="delphi_stmtList311", type=delphi_initSection, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_initSection310", type=delphi_stmtList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
heritage312: BinaryAssociation = BinaryAssociation(
    name="heritage312",
    ends={
        Property(name="delphi_classHeritage", type=delphi_classType, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_classType", type=delphi_classHeritage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fieldList313: BinaryAssociation = BinaryAssociation(
    name="fieldList313",
    ends={
        Property(name="delphi_classFieldList", type=delphi_classType, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_classType314", type=delphi_classFieldList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
methodList315: BinaryAssociation = BinaryAssociation(
    name="methodList315",
    ends={
        Property(name="delphi_classMethodList", type=delphi_classType, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_classType316", type=delphi_classMethodList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propList317: BinaryAssociation = BinaryAssociation(
    name="propList317",
    ends={
        Property(name="delphi_classPropertyList", type=delphi_classType, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_classType318", type=delphi_classPropertyList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
field319: BinaryAssociation = BinaryAssociation(
    name="field319",
    ends={
        Property(name="delphi_classField", type=delphi_classFieldList, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_classFieldList320", type=delphi_classField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fieldList321: BinaryAssociation = BinaryAssociation(
    name="fieldList321",
    ends={
        Property(name="delphi_objFieldList323", type=delphi_classField, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_classField322", type=delphi_objFieldList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
metod324: BinaryAssociation = BinaryAssociation(
    name="metod324",
    ends={
        Property(name="delphi_classMethod", type=delphi_classMethodList, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_classMethodList325", type=delphi_classMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methodList326: BinaryAssociation = BinaryAssociation(
    name="methodList326",
    ends={
        Property(name="delphi_methodList328", type=delphi_classMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_classMethod327", type=delphi_methodList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
index351: BinaryAssociation = BinaryAssociation(
    name="index351",
    ends={
        Property(name="delphi_constExpr353", type=delphi_propertySpecifiers, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_propertySpecifiers352", type=delphi_constExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
readId354: BinaryAssociation = BinaryAssociation(
    name="readId354",
    ends={
        Property(name="delphi_ident356", type=delphi_propertySpecifiers, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_propertySpecifiers355", type=delphi_ident, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
writeId357: BinaryAssociation = BinaryAssociation(
    name="writeId357",
    ends={
        Property(name="delphi_ident359", type=delphi_propertySpecifiers, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_propertySpecifiers358", type=delphi_ident, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
storeId360: BinaryAssociation = BinaryAssociation(
    name="storeId360",
    ends={
        Property(name="delphi_ident362", type=delphi_propertySpecifiers, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_propertySpecifiers361", type=delphi_ident, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id333: BinaryAssociation = BinaryAssociation(
    name="id333",
    ends={
        Property(name="delphi_ident335", type=delphi_propertyList, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_propertyList334", type=delphi_ident, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interface336: BinaryAssociation = BinaryAssociation(
    name="interface336",
    ends={
        Property(name="delphi_propertyInterface", type=delphi_propertyList, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_propertyList337", type=delphi_propertyInterface, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specifiers338: BinaryAssociation = BinaryAssociation(
    name="specifiers338",
    ends={
        Property(name="delphi_propertySpecifiers", type=delphi_propertyList, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_propertyList339", type=delphi_propertySpecifiers, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
paramList340: BinaryAssociation = BinaryAssociation(
    name="paramList340",
    ends={
        Property(name="delphi_propertyParameterList", type=delphi_propertyInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_propertyInterface341", type=delphi_propertyParameterList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id342: BinaryAssociation = BinaryAssociation(
    name="id342",
    ends={
        Property(name="delphi_ident344", type=delphi_propertyInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_propertyInterface343", type=delphi_ident, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
idList345: BinaryAssociation = BinaryAssociation(
    name="idList345",
    ends={
        Property(name="delphi_identList347", type=delphi_propertyParameterList, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_propertyParameterList346", type=delphi_identList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeRef348: BinaryAssociation = BinaryAssociation(
    name="typeRef348",
    ends={
        Property(name="delphi_typeId350", type=delphi_propertyParameterList, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_propertyParameterList349", type=delphi_typeId, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
idList385: BinaryAssociation = BinaryAssociation(
    name="idList385",
    ends={
        Property(name="delphi_identList387", type=delphi_containsClause, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_containsClause386", type=delphi_identList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type388: BinaryAssociation = BinaryAssociation(
    name="type388",
    ends={
        Property(name="delphi_type390", type=delphi_identList, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_identList389", type=delphi_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ids391: BinaryAssociation = BinaryAssociation(
    name="ids391",
    ends={
        Property(name="delphi_ident393", type=delphi_identList, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_identList392", type=delphi_ident, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
storeExp363: BinaryAssociation = BinaryAssociation(
    name="storeExp363",
    ends={
        Property(name="delphi_constExpr365", type=delphi_propertySpecifiers, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_propertySpecifiers364", type=delphi_constExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaulExp366: BinaryAssociation = BinaryAssociation(
    name="defaulExp366",
    ends={
        Property(name="delphi_constExpr368", type=delphi_propertySpecifiers, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_propertySpecifiers367", type=delphi_constExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
implement369: BinaryAssociation = BinaryAssociation(
    name="implement369",
    ends={
        Property(name="delphi_typeId371", type=delphi_propertySpecifiers, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_propertySpecifiers370", type=delphi_typeId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
heritage372: BinaryAssociation = BinaryAssociation(
    name="heritage372",
    ends={
        Property(name="delphi_interfaceHeritage", type=delphi_interfaceType, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_interfaceType", type=delphi_interfaceHeritage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
methodList373: BinaryAssociation = BinaryAssociation(
    name="methodList373",
    ends={
        Property(name="delphi_classMethodList375", type=delphi_interfaceType, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_interfaceType374", type=delphi_classMethodList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propList376: BinaryAssociation = BinaryAssociation(
    name="propList376",
    ends={
        Property(name="delphi_classPropertyList378", type=delphi_interfaceType, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_interfaceType377", type=delphi_classPropertyList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
idList379: BinaryAssociation = BinaryAssociation(
    name="idList379",
    ends={
        Property(name="delphi_identList381", type=delphi_interfaceHeritage, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_interfaceHeritage380", type=delphi_identList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
idList382: BinaryAssociation = BinaryAssociation(
    name="idList382",
    ends={
        Property(name="delphi_identList384", type=delphi_requiresClause, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_requiresClause383", type=delphi_identList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constExp407: BinaryAssociation = BinaryAssociation(
    name="constExp407",
    ends={
        Property(name="delphi_constExpr409", type=delphi_recordConstExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_recordConstExpr408", type=delphi_constExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left410: BinaryAssociation = BinaryAssociation(
    name="left410",
    ends={
        Property(name="delphi_expression411", type=delphi_relExp, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_relExp", type=delphi_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unitId394: BinaryAssociation = BinaryAssociation(
    name="unitId394",
    ends={
        Property(name="delphi_unitId", type=delphi_qualId, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_qualId395", type=delphi_unitId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id396: BinaryAssociation = BinaryAssociation(
    name="id396",
    ends={
        Property(name="delphi_ident398", type=delphi_qualId, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_qualId397", type=delphi_ident, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unitId399: BinaryAssociation = BinaryAssociation(
    name="unitId399",
    ends={
        Property(name="delphi_unitId401", type=delphi_typeId, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_typeId400", type=delphi_unitId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id402: BinaryAssociation = BinaryAssociation(
    name="id402",
    ends={
        Property(name="delphi_qualId404", type=delphi_typeId, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_typeId403", type=delphi_qualId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id405: BinaryAssociation = BinaryAssociation(
    name="id405",
    ends={
        Property(name="delphi_ident406", type=delphi_recordConstExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_recordConstExpr", type=delphi_ident, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
designator429: BinaryAssociation = BinaryAssociation(
    name="designator429",
    ends={
        Property(name="delphi_designator430", type=delphi_assignmentStmnt, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_assignmentStmnt", type=delphi_designator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp431: BinaryAssociation = BinaryAssociation(
    name="exp431",
    ends={
        Property(name="delphi_expression433", type=delphi_assignmentStmnt, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_assignmentStmnt432", type=delphi_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
relOp412: BinaryAssociation = BinaryAssociation(
    name="relOp412",
    ends={
        Property(name="delphi_relOp", type=delphi_relExp, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_relExp413", type=delphi_relOp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right414: BinaryAssociation = BinaryAssociation(
    name="right414",
    ends={
        Property(name="delphi_simpleExpression", type=delphi_relExp, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_relExp415", type=delphi_simpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left416: BinaryAssociation = BinaryAssociation(
    name="left416",
    ends={
        Property(name="delphi_simpleExpression417", type=delphi_addExp, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_addExp", type=delphi_simpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addOp418: BinaryAssociation = BinaryAssociation(
    name="addOp418",
    ends={
        Property(name="delphi_addOp", type=delphi_addExp, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_addExp419", type=delphi_addOp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right420: BinaryAssociation = BinaryAssociation(
    name="right420",
    ends={
        Property(name="delphi_term", type=delphi_addExp, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_addExp421", type=delphi_term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left422: BinaryAssociation = BinaryAssociation(
    name="left422",
    ends={
        Property(name="delphi_term423", type=delphi_multExp, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_multExp", type=delphi_term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multOp424: BinaryAssociation = BinaryAssociation(
    name="multOp424",
    ends={
        Property(name="delphi_mulOp", type=delphi_multExp, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_multExp425", type=delphi_mulOp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right426: BinaryAssociation = BinaryAssociation(
    name="right426",
    ends={
        Property(name="delphi_factor428", type=delphi_multExp, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_multExp427", type=delphi_factor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reservedWord446: BinaryAssociation = BinaryAssociation(
    name="reservedWord446",
    ends={
        Property(name="delphi_reservedWord447", type=delphi_ReservedId, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_ReservedId", type=delphi_reservedWord, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp448: BinaryAssociation = BinaryAssociation(
    name="exp448",
    ends={
        Property(name="delphi_expression449", type=delphi_ConstExp, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_ConstExp", type=delphi_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
designator434: BinaryAssociation = BinaryAssociation(
    name="designator434",
    ends={
        Property(name="delphi_designator435", type=delphi_callStmnt, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_callStmnt", type=delphi_designator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args436: BinaryAssociation = BinaryAssociation(
    name="args436",
    ends={
        Property(name="delphi_exprList438", type=delphi_callStmnt, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_callStmnt437", type=delphi_exprList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
idList439: BinaryAssociation = BinaryAssociation(
    name="idList439",
    ends={
        Property(name="delphi_identList440", type=delphi_parameterList, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_parameterList", type=delphi_identList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
if441: BinaryAssociation = BinaryAssociation(
    name="if441",
    ends={
        Property(name="delphi_ident442", type=delphi_parameterSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_parameterSimple", type=delphi_ident, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExp443: BinaryAssociation = BinaryAssociation(
    name="initExp443",
    ends={
        Property(name="delphi_constExpr445", type=delphi_parameterSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_parameterSimple444", type=delphi_constExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exps450: BinaryAssociation = BinaryAssociation(
    name="exps450",
    ends={
        Property(name="delphi_constExpr451", type=delphi_MultipleConstExp, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_MultipleConstExp", type=delphi_constExpr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exps452: BinaryAssociation = BinaryAssociation(
    name="exps452",
    ends={
        Property(name="delphi_recordConstExpr453", type=delphi_RecordConstExp, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_RecordConstExp", type=delphi_recordConstExpr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ast454: BinaryAssociation = BinaryAssociation(
    name="ast454",
    ends={
        Property(name="delphi_Visitable", type=delphi_CSTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="delphi_CSTrace", type=delphi_Visitable, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_delphi_file_CSTrace = Generalization(general=CSTrace, specific=delphi_file)
gen_delphi_program_file = Generalization(general=file, specific=delphi_program)
gen_delphi_unit_file = Generalization(general=file, specific=delphi_unit)
gen_delphi_packageDecl_file = Generalization(general=file, specific=delphi_packageDecl)
gen_delphi_mainRule_CSTrace = Generalization(general=CSTrace, specific=delphi_mainRule)
gen_delphi_usesClause_CSTrace = Generalization(general=CSTrace, specific=delphi_usesClause)
gen_delphi_interfaceSection_CSTrace = Generalization(general=CSTrace, specific=delphi_interfaceSection)
gen_delphi_interfaceDecl_CSTrace = Generalization(general=CSTrace, specific=delphi_interfaceDecl)
gen_delphi_exportedHeading_interfaceDecl = Generalization(general=interfaceDecl, specific=delphi_exportedHeading)
gen_delphi_implementationSection_CSTrace = Generalization(general=CSTrace, specific=delphi_implementationSection)
gen_delphi_library_file = Generalization(general=file, specific=delphi_library)
gen_delphi_programBlock_CSTrace = Generalization(general=CSTrace, specific=delphi_programBlock)
gen_delphi_exportsItem_CSTrace = Generalization(general=CSTrace, specific=delphi_exportsItem)
gen_delphi_exportsStmt_CSTrace = Generalization(general=CSTrace, specific=delphi_exportsStmt)
gen_delphi_declSection_CSTrace = Generalization(general=CSTrace, specific=delphi_declSection)
gen_delphi_labelDeclSection_declSection = Generalization(general=declSection, specific=delphi_labelDeclSection)
gen_delphi_constSection_interfaceDecl = Generalization(general=interfaceDecl, specific=delphi_constSection)
gen_delphi_constSection_declSection = Generalization(general=declSection, specific=delphi_constSection)
gen_delphi_constantDecl_CSTrace = Generalization(general=CSTrace, specific=delphi_constantDecl)
gen_delphi_block_CSTrace = Generalization(general=CSTrace, specific=delphi_block)
gen_delphi_typeDecl_CSTrace = Generalization(general=CSTrace, specific=delphi_typeDecl)
gen_delphi_typedConstant_CSTrace = Generalization(general=CSTrace, specific=delphi_typedConstant)
gen_delphi_arrayConstant_CSTrace = Generalization(general=CSTrace, specific=delphi_arrayConstant)
gen_delphi_recordConstant_CSTrace = Generalization(general=CSTrace, specific=delphi_recordConstant)
gen_delphi_recordFieldConstant_CSTrace = Generalization(general=CSTrace, specific=delphi_recordFieldConstant)
gen_delphi_typeSection_interfaceDecl = Generalization(general=interfaceDecl, specific=delphi_typeSection)
gen_delphi_typeSection_declSection = Generalization(general=declSection, specific=delphi_typeSection)
gen_delphi_simpleType_type = Generalization(general=type, specific=delphi_simpleType)
gen_delphi_realType_simpleType = Generalization(general=simpleType, specific=delphi_realType)
gen_delphi_ordinalType_simpleType = Generalization(general=simpleType, specific=delphi_ordinalType)
gen_delphi_ordIdent_ordinalType = Generalization(general=ordinalType, specific=delphi_ordIdent)
gen_delphi_variantType_type = Generalization(general=type, specific=delphi_variantType)
gen_delphi_subrangeType_ordinalType = Generalization(general=ordinalType, specific=delphi_subrangeType)
gen_delphi_enumeratedType_ordinalType = Generalization(general=ordinalType, specific=delphi_enumeratedType)
gen_delphi_enumeratedTypeElement_CSTrace = Generalization(general=CSTrace, specific=delphi_enumeratedTypeElement)
gen_delphi_stringType_type = Generalization(general=type, specific=delphi_stringType)
gen_delphi_type_CSTrace = Generalization(general=CSTrace, specific=delphi_type)
gen_delphi_restrictedType_CSTrace = Generalization(general=CSTrace, specific=delphi_restrictedType)
gen_delphi_classRefType_type = Generalization(general=type, specific=delphi_classRefType)
gen_delphi_recType_strucType = Generalization(general=strucType, specific=delphi_recType)
gen_delphi_fieldList_CSTrace = Generalization(general=CSTrace, specific=delphi_fieldList)
gen_delphi_fieldDecl_CSTrace = Generalization(general=CSTrace, specific=delphi_fieldDecl)
gen_delphi_variantSection_CSTrace = Generalization(general=CSTrace, specific=delphi_variantSection)
gen_delphi_strucType_type = Generalization(general=type, specific=delphi_strucType)
gen_delphi_arrayType_strucType = Generalization(general=strucType, specific=delphi_arrayType)
gen_delphi_fileType_strucType = Generalization(general=strucType, specific=delphi_fileType)
gen_delphi_pointerType_type = Generalization(general=type, specific=delphi_pointerType)
gen_delphi_procedureType_type = Generalization(general=type, specific=delphi_procedureType)
gen_delphi_varSection_interfaceDecl = Generalization(general=interfaceDecl, specific=delphi_varSection)
gen_delphi_varSection_declSection = Generalization(general=declSection, specific=delphi_varSection)
gen_delphi_varDecl_CSTrace = Generalization(general=CSTrace, specific=delphi_varDecl)
gen_delphi_recVariant_CSTrace = Generalization(general=CSTrace, specific=delphi_recVariant)
gen_delphi_setType_strucType = Generalization(general=strucType, specific=delphi_setType)
gen_delphi_expression_CSTrace = Generalization(general=CSTrace, specific=delphi_expression)
gen_delphi_simpleExpression_expression = Generalization(general=expression, specific=delphi_simpleExpression)
gen_delphi_term_simpleExpression = Generalization(general=simpleExpression, specific=delphi_term)
gen_delphi_factor_term = Generalization(general=term, specific=delphi_factor)
gen_delphi_relOp_CSTrace = Generalization(general=CSTrace, specific=delphi_relOp)
gen_delphi_addOp_CSTrace = Generalization(general=CSTrace, specific=delphi_addOp)
gen_delphi_mulOp_CSTrace = Generalization(general=CSTrace, specific=delphi_mulOp)
gen_delphi_designator_CSTrace = Generalization(general=CSTrace, specific=delphi_designator)
gen_delphi_designatorSubPart_CSTrace = Generalization(general=CSTrace, specific=delphi_designatorSubPart)
gen_delphi_designatorPart_CSTrace = Generalization(general=CSTrace, specific=delphi_designatorPart)
gen_delphi_setElement_CSTrace = Generalization(general=CSTrace, specific=delphi_setElement)
gen_delphi_exprList_CSTrace = Generalization(general=CSTrace, specific=delphi_exprList)
gen_delphi_stmtList_CSTrace = Generalization(general=CSTrace, specific=delphi_stmtList)
gen_delphi_statement_CSTrace = Generalization(general=CSTrace, specific=delphi_statement)
gen_delphi_unlabelledStatement_CSTrace = Generalization(general=CSTrace, specific=delphi_unlabelledStatement)
gen_delphi_simpleStatement_unlabelledStatement = Generalization(general=unlabelledStatement, specific=delphi_simpleStatement)
gen_delphi_structStmt_unlabelledStatement = Generalization(general=unlabelledStatement, specific=delphi_structStmt)
gen_delphi_compoundStmt_structStmt = Generalization(general=structStmt, specific=delphi_compoundStmt)
gen_delphi_conditionalStmt_structStmt = Generalization(general=structStmt, specific=delphi_conditionalStmt)
gen_delphi_ifStmt_conditionalStmt = Generalization(general=conditionalStmt, specific=delphi_ifStmt)
gen_delphi_setConstructor_CSTrace = Generalization(general=CSTrace, specific=delphi_setConstructor)
gen_delphi_caseSelector_CSTrace = Generalization(general=CSTrace, specific=delphi_caseSelector)
gen_delphi_caseLabel_CSTrace = Generalization(general=CSTrace, specific=delphi_caseLabel)
gen_delphi_loopStmt_structStmt = Generalization(general=structStmt, specific=delphi_loopStmt)
gen_delphi_repeatStmt_loopStmt = Generalization(general=loopStmt, specific=delphi_repeatStmt)
gen_delphi_whileStmt_loopStmt = Generalization(general=loopStmt, specific=delphi_whileStmt)
gen_delphi_forStmt_loopStmt = Generalization(general=loopStmt, specific=delphi_forStmt)
gen_delphi_caseStmt_conditionalStmt = Generalization(general=conditionalStmt, specific=delphi_caseStmt)
gen_delphi_exceptionBlock_CSTrace = Generalization(general=CSTrace, specific=delphi_exceptionBlock)
gen_delphi_procedureDecl_procedureDeclSection = Generalization(general=procedureDeclSection, specific=delphi_procedureDecl)
gen_delphi_functionDecl_procedureDeclSection = Generalization(general=procedureDeclSection, specific=delphi_functionDecl)
gen_delphi_functionHeading_methodHeading = Generalization(general=methodHeading, specific=delphi_functionHeading)
gen_delphi_procedureHeading_methodHeading = Generalization(general=methodHeading, specific=delphi_procedureHeading)
gen_delphi_withStmt_structStmt = Generalization(general=structStmt, specific=delphi_withStmt)
gen_delphi_tryStmt_structStmt = Generalization(general=structStmt, specific=delphi_tryStmt)
gen_delphi_raiseStmt_structStmt = Generalization(general=structStmt, specific=delphi_raiseStmt)
gen_delphi_assemblerStmt_structStmt = Generalization(general=structStmt, specific=delphi_assemblerStmt)
gen_delphi_procedureDeclSection_declSection = Generalization(general=declSection, specific=delphi_procedureDeclSection)
gen_delphi_methodHeading_CSTrace = Generalization(general=CSTrace, specific=delphi_methodHeading)
gen_delphi_constructorHeading_methodHeading = Generalization(general=methodHeading, specific=delphi_constructorHeading)
gen_delphi_destructorHeading_methodHeading = Generalization(general=methodHeading, specific=delphi_destructorHeading)
gen_delphi_objFieldList_CSTrace = Generalization(general=CSTrace, specific=delphi_objFieldList)
gen_delphi_initSection_CSTrace = Generalization(general=CSTrace, specific=delphi_initSection)
gen_delphi_formalParameters_CSTrace = Generalization(general=CSTrace, specific=delphi_formalParameters)
gen_delphi_formalParm_CSTrace = Generalization(general=CSTrace, specific=delphi_formalParm)
gen_delphi_parameter_CSTrace = Generalization(general=CSTrace, specific=delphi_parameter)
gen_delphi_directive_CSTrace = Generalization(general=CSTrace, specific=delphi_directive)
gen_delphi_objectType_restrictedType = Generalization(general=restrictedType, specific=delphi_objectType)
gen_delphi_objHeritage_CSTrace = Generalization(general=CSTrace, specific=delphi_objHeritage)
gen_delphi_methodList_CSTrace = Generalization(general=CSTrace, specific=delphi_methodList)
gen_delphi_classPropertyList_CSTrace = Generalization(general=CSTrace, specific=delphi_classPropertyList)
gen_delphi_classProperty_CSTrace = Generalization(general=CSTrace, specific=delphi_classProperty)
gen_delphi_propertyList_CSTrace = Generalization(general=CSTrace, specific=delphi_propertyList)
gen_delphi_classType_restrictedType = Generalization(general=restrictedType, specific=delphi_classType)
gen_delphi_classHeritage_CSTrace = Generalization(general=CSTrace, specific=delphi_classHeritage)
gen_delphi_classFieldList_CSTrace = Generalization(general=CSTrace, specific=delphi_classFieldList)
gen_delphi_classField_CSTrace = Generalization(general=CSTrace, specific=delphi_classField)
gen_delphi_classMethodList_CSTrace = Generalization(general=CSTrace, specific=delphi_classMethodList)
gen_delphi_classMethod_CSTrace = Generalization(general=CSTrace, specific=delphi_classMethod)
gen_delphi_propertyInterface_CSTrace = Generalization(general=CSTrace, specific=delphi_propertyInterface)
gen_delphi_propertyParameterList_CSTrace = Generalization(general=CSTrace, specific=delphi_propertyParameterList)
gen_delphi_propertySpecifiers_CSTrace = Generalization(general=CSTrace, specific=delphi_propertySpecifiers)
gen_delphi_identList_objFieldList = Generalization(general=objFieldList, specific=delphi_identList)
gen_delphi_identList_classHeritage = Generalization(general=classHeritage, specific=delphi_identList)
gen_delphi_interfaceType_restrictedType = Generalization(general=restrictedType, specific=delphi_interfaceType)
gen_delphi_interfaceHeritage_CSTrace = Generalization(general=CSTrace, specific=delphi_interfaceHeritage)
gen_delphi_requiresClause_CSTrace = Generalization(general=CSTrace, specific=delphi_requiresClause)
gen_delphi_containsClause_CSTrace = Generalization(general=CSTrace, specific=delphi_containsClause)
gen_delphi_unitId_CSTrace = Generalization(general=CSTrace, specific=delphi_unitId)
gen_delphi_relExp_expression = Generalization(general=expression, specific=delphi_relExp)
gen_delphi_qualId_CSTrace = Generalization(general=CSTrace, specific=delphi_qualId)
gen_delphi_typeId_type = Generalization(general=type, specific=delphi_typeId)
gen_delphi_typeId_pointerType = Generalization(general=pointerType, specific=delphi_typeId)
gen_delphi_ident_CSTrace = Generalization(general=CSTrace, specific=delphi_ident)
gen_delphi_reservedWord_CSTrace = Generalization(general=CSTrace, specific=delphi_reservedWord)
gen_delphi_constExpr_CSTrace = Generalization(general=CSTrace, specific=delphi_constExpr)
gen_delphi_recordConstExpr_CSTrace = Generalization(general=CSTrace, specific=delphi_recordConstExpr)
gen_delphi_simpleFactor_factor = Generalization(general=factor, specific=delphi_simpleFactor)
gen_delphi_adOp_addOp = Generalization(general=addOp, specific=delphi_adOp)
gen_delphi_assignmentStmnt_simpleStatement = Generalization(general=simpleStatement, specific=delphi_assignmentStmnt)
gen_delphi_addExp_simpleExpression = Generalization(general=simpleExpression, specific=delphi_addExp)
gen_delphi_multExp_term = Generalization(general=term, specific=delphi_multExp)
gen_delphi_ReservedId_ident = Generalization(general=ident, specific=delphi_ReservedId)
gen_delphi_MineID_ident = Generalization(general=ident, specific=delphi_MineID)
gen_delphi_ConstExp_constExpr = Generalization(general=constExpr, specific=delphi_ConstExp)
gen_delphi_callStmnt_simpleStatement = Generalization(general=simpleStatement, specific=delphi_callStmnt)
gen_delphi_inheritedStamnt_simpleStatement = Generalization(general=simpleStatement, specific=delphi_inheritedStamnt)
gen_delphi_gotoStmnt_simpleStatement = Generalization(general=simpleStatement, specific=delphi_gotoStmnt)
gen_delphi_parameterList_parameter = Generalization(general=parameter, specific=delphi_parameterList)
gen_delphi_parameterSimple_parameter = Generalization(general=parameter, specific=delphi_parameterSimple)
gen_delphi_MultipleId_ident = Generalization(general=ident, specific=delphi_MultipleId)
gen_delphi_MultipleConstExp_constExpr = Generalization(general=constExpr, specific=delphi_MultipleConstExp)
gen_delphi_RecordConstExp_constExpr = Generalization(general=constExpr, specific=delphi_RecordConstExp)

# Domain Model
domain_model = DomainModel(
    name="delphi",
    types={delphi_ident, delphi_program, file, delphi_identList, delphi_programBlock, delphi_unit, delphi_interfaceSection, delphi_implementationSection, delphi_initSection, delphi_packageDecl, delphi_requiresClause, delphi_containsClause, delphi_mainRule, CSTrace, delphi_file, delphi_block, delphi_interfaceDecl, delphi_exportedHeading, interfaceDecl, delphi_procedureHeading, delphi_directive, delphi_functionHeading, delphi_declSection, delphi_library, delphi_usesClause, delphi_compoundStmt, delphi_exportsItem, delphi_constExpr, delphi_labelDeclSection, declSection, delphi_constSection, delphi_constantDecl, delphi_exportsStmt, delphi_type, delphi_restrictedType, delphi_arrayConstant, delphi_recordConstant, delphi_recordFieldConstant, delphi_typeId, delphi_typedConstant, delphi_typeSection, delphi_typeDecl, delphi_simpleType, delphi_realType, simpleType, delphi_ordinalType, delphi_ordIdent, ordinalType, delphi_variantType, delphi_subrangeType, delphi_enumeratedType, delphi_enumeratedTypeElement, delphi_stringType, delphi_classRefType, type, delphi_recType, delphi_fieldList, delphi_fieldDecl, delphi_variantSection, delphi_recVariant, delphi_strucType, delphi_arrayType, strucType, delphi_fileType, delphi_pointerType, delphi_procedureType, delphi_varSection, delphi_varDecl, delphi_setType, delphi_expression, delphi_simpleExpression, expression, delphi_term, simpleExpression, delphi_factor, term, delphi_designator, delphi_exprList, delphi_setConstructor, delphi_relOp, delphi_addOp, delphi_mulOp, delphi_designatorSubPart, delphi_designatorPart, delphi_stmtList, delphi_statement, delphi_unlabelledStatement, delphi_simpleStatement, unlabelledStatement, delphi_structStmt, structStmt, delphi_conditionalStmt, delphi_ifStmt, conditionalStmt, delphi_reservedWord, delphi_setElement, delphi_caseLabel, delphi_loopStmt, delphi_repeatStmt, loopStmt, delphi_whileStmt, delphi_forStmt, delphi_qualId, delphi_caseStmt, delphi_caseSelector, delphi_exceptionBlock, delphi_procedureDecl, procedureDeclSection, delphi_functionDecl, methodHeading, delphi_withStmt, delphi_formalParameters, delphi_tryStmt, delphi_raiseStmt, delphi_assemblerStmt, delphi_procedureDeclSection, delphi_constructorHeading, delphi_destructorHeading, delphi_formalParm, delphi_parameter, delphi_objectType, restrictedType, delphi_objHeritage, delphi_objFieldList, delphi_methodList, delphi_methodHeading, delphi_classProperty, delphi_propertyList, delphi_classType, delphi_classHeritage, delphi_classFieldList, delphi_classMethodList, delphi_classPropertyList, delphi_classField, delphi_classMethod, delphi_propertyInterface, delphi_propertySpecifiers, delphi_propertyParameterList, objFieldList, classHeritage, delphi_interfaceType, delphi_interfaceHeritage, delphi_relExp, delphi_unitId, pointerType, delphi_recordConstExpr, delphi_simpleFactor, factor, delphi_adOp, addOp, delphi_assignmentStmnt, simpleStatement, delphi_addExp, delphi_multExp, delphi_ReservedId, delphi_MineID, delphi_ConstExp, constExpr, delphi_callStmnt, delphi_inheritedStamnt, delphi_gotoStmnt, delphi_parameterList, parameter, delphi_parameterSimple, delphi_MultipleId, ident, delphi_MultipleConstExp, delphi_RecordConstExp, delphi_CSTrace, delphi_Visitable},
    associations={file0, id1, paramsList3, block4, interfaceSect6, implementationSect7, initSect9, requires11, contains12, block18, idList20, uses23, interfaceDecl26, pHeading28, directive29, fHeading31, uses33, declSect36, pBlock14, uses16, compound46, id48, constExp50, items52, constantDecl55, id56, const59, exports38, declSect40, exports43, id67, type70, restrictedType72, const74, array77, record79, typedConstant81, recordField84, id86, typeRef62, typedConstat64, typeDecl66, first94, last96, element99, id100, literalExp103, constExp106, typedConstant89, typeRef92, ordinalTyp109, type112, fields115, field116, variantSect118, idList120, type123, id126, typeRef129, recVariants132, ordinalType108, ordinal140, typeRef142, pHeading144, fHeading146, varDecls149, idList150, type153, constExp134, fieldList137, designator165, expList166, absId156, absConst159, absIniti162, setConstuctor173, typeRef175, subpart178, designator181, part183, exprList185, nestedExp168, exp170, first192, last195, exps198, statments201, statement202, stamtList204, condition207, reservedWord188, element190, default219, labels222, stmt224, first227, last230, stmt233, condition235, varId238, varInit239, then209, else212, expression215, cases217, stmtList247, exception249, final251, exceptionId254, heading271, heading273, type275, vars242, stmt244, type257, doStmt260, elseStmts263, directive266, block268, id300, formalParams303, stmtList306, params278, param279, type281, messageExp284, heritage287, fieldList288, methodList290, id292, heading295, directive297, property329, propList331, endStmtList309, heritage312, fieldList313, methodList315, propList317, field319, fieldList321, metod324, methodList326, index351, readId354, writeId357, storeId360, id333, interface336, specifiers338, paramList340, id342, idList345, typeRef348, idList385, type388, ids391, storeExp363, defaulExp366, implement369, heritage372, methodList373, propList376, idList379, idList382, constExp407, left410, unitId394, id396, unitId399, id402, id405, designator429, exp431, relOp412, right414, left416, addOp418, right420, left422, multOp424, right426, reservedWord446, exp448, designator434, args436, idList439, if441, initExp443, exps450, exps452, ast454},
    generalizations={gen_delphi_file_CSTrace, gen_delphi_program_file, gen_delphi_unit_file, gen_delphi_packageDecl_file, gen_delphi_mainRule_CSTrace, gen_delphi_usesClause_CSTrace, gen_delphi_interfaceSection_CSTrace, gen_delphi_interfaceDecl_CSTrace, gen_delphi_exportedHeading_interfaceDecl, gen_delphi_implementationSection_CSTrace, gen_delphi_library_file, gen_delphi_programBlock_CSTrace, gen_delphi_exportsItem_CSTrace, gen_delphi_exportsStmt_CSTrace, gen_delphi_declSection_CSTrace, gen_delphi_labelDeclSection_declSection, gen_delphi_constSection_interfaceDecl, gen_delphi_constSection_declSection, gen_delphi_constantDecl_CSTrace, gen_delphi_block_CSTrace, gen_delphi_typeDecl_CSTrace, gen_delphi_typedConstant_CSTrace, gen_delphi_arrayConstant_CSTrace, gen_delphi_recordConstant_CSTrace, gen_delphi_recordFieldConstant_CSTrace, gen_delphi_typeSection_interfaceDecl, gen_delphi_typeSection_declSection, gen_delphi_simpleType_type, gen_delphi_realType_simpleType, gen_delphi_ordinalType_simpleType, gen_delphi_ordIdent_ordinalType, gen_delphi_variantType_type, gen_delphi_subrangeType_ordinalType, gen_delphi_enumeratedType_ordinalType, gen_delphi_enumeratedTypeElement_CSTrace, gen_delphi_stringType_type, gen_delphi_type_CSTrace, gen_delphi_restrictedType_CSTrace, gen_delphi_classRefType_type, gen_delphi_recType_strucType, gen_delphi_fieldList_CSTrace, gen_delphi_fieldDecl_CSTrace, gen_delphi_variantSection_CSTrace, gen_delphi_strucType_type, gen_delphi_arrayType_strucType, gen_delphi_fileType_strucType, gen_delphi_pointerType_type, gen_delphi_procedureType_type, gen_delphi_varSection_interfaceDecl, gen_delphi_varSection_declSection, gen_delphi_varDecl_CSTrace, gen_delphi_recVariant_CSTrace, gen_delphi_setType_strucType, gen_delphi_expression_CSTrace, gen_delphi_simpleExpression_expression, gen_delphi_term_simpleExpression, gen_delphi_factor_term, gen_delphi_relOp_CSTrace, gen_delphi_addOp_CSTrace, gen_delphi_mulOp_CSTrace, gen_delphi_designator_CSTrace, gen_delphi_designatorSubPart_CSTrace, gen_delphi_designatorPart_CSTrace, gen_delphi_setElement_CSTrace, gen_delphi_exprList_CSTrace, gen_delphi_stmtList_CSTrace, gen_delphi_statement_CSTrace, gen_delphi_unlabelledStatement_CSTrace, gen_delphi_simpleStatement_unlabelledStatement, gen_delphi_structStmt_unlabelledStatement, gen_delphi_compoundStmt_structStmt, gen_delphi_conditionalStmt_structStmt, gen_delphi_ifStmt_conditionalStmt, gen_delphi_setConstructor_CSTrace, gen_delphi_caseSelector_CSTrace, gen_delphi_caseLabel_CSTrace, gen_delphi_loopStmt_structStmt, gen_delphi_repeatStmt_loopStmt, gen_delphi_whileStmt_loopStmt, gen_delphi_forStmt_loopStmt, gen_delphi_caseStmt_conditionalStmt, gen_delphi_exceptionBlock_CSTrace, gen_delphi_procedureDecl_procedureDeclSection, gen_delphi_functionDecl_procedureDeclSection, gen_delphi_functionHeading_methodHeading, gen_delphi_procedureHeading_methodHeading, gen_delphi_withStmt_structStmt, gen_delphi_tryStmt_structStmt, gen_delphi_raiseStmt_structStmt, gen_delphi_assemblerStmt_structStmt, gen_delphi_procedureDeclSection_declSection, gen_delphi_methodHeading_CSTrace, gen_delphi_constructorHeading_methodHeading, gen_delphi_destructorHeading_methodHeading, gen_delphi_objFieldList_CSTrace, gen_delphi_initSection_CSTrace, gen_delphi_formalParameters_CSTrace, gen_delphi_formalParm_CSTrace, gen_delphi_parameter_CSTrace, gen_delphi_directive_CSTrace, gen_delphi_objectType_restrictedType, gen_delphi_objHeritage_CSTrace, gen_delphi_methodList_CSTrace, gen_delphi_classPropertyList_CSTrace, gen_delphi_classProperty_CSTrace, gen_delphi_propertyList_CSTrace, gen_delphi_classType_restrictedType, gen_delphi_classHeritage_CSTrace, gen_delphi_classFieldList_CSTrace, gen_delphi_classField_CSTrace, gen_delphi_classMethodList_CSTrace, gen_delphi_classMethod_CSTrace, gen_delphi_propertyInterface_CSTrace, gen_delphi_propertyParameterList_CSTrace, gen_delphi_propertySpecifiers_CSTrace, gen_delphi_identList_objFieldList, gen_delphi_identList_classHeritage, gen_delphi_interfaceType_restrictedType, gen_delphi_interfaceHeritage_CSTrace, gen_delphi_requiresClause_CSTrace, gen_delphi_containsClause_CSTrace, gen_delphi_unitId_CSTrace, gen_delphi_relExp_expression, gen_delphi_qualId_CSTrace, gen_delphi_typeId_type, gen_delphi_typeId_pointerType, gen_delphi_ident_CSTrace, gen_delphi_reservedWord_CSTrace, gen_delphi_constExpr_CSTrace, gen_delphi_recordConstExpr_CSTrace, gen_delphi_simpleFactor_factor, gen_delphi_adOp_addOp, gen_delphi_assignmentStmnt_simpleStatement, gen_delphi_addExp_simpleExpression, gen_delphi_multExp_term, gen_delphi_ReservedId_ident, gen_delphi_MineID_ident, gen_delphi_ConstExp_constExpr, gen_delphi_callStmnt_simpleStatement, gen_delphi_inheritedStamnt_simpleStatement, gen_delphi_gotoStmnt_simpleStatement, gen_delphi_parameterList_parameter, gen_delphi_parameterSimple_parameter, gen_delphi_MultipleId_ident, gen_delphi_MultipleConstExp_constExpr, gen_delphi_RecordConstExp_constExpr},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)