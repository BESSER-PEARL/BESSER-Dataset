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
swrtj_Program = Class(name="swrtj::Program")
swrtj_Block = Class(name="swrtj::Block")
swrtj_BaseRecord = Class(name="swrtj::BaseRecord")
swrtj_File = Class(name="swrtj::File")
swrtj_Import = Class(name="swrtj::Import")
swrtj_Element = Class(name="swrtj::Element")
swrtj_Interface = Class(name="swrtj::Interface")
Element = Class(name="Element")
swrtj_Method = Class(name="swrtj::Method")
swrtj_Record = Class(name="swrtj::Record")
swrtj_RecordExpression = Class(name="swrtj::RecordExpression")
swrtj_Trait = Class(name="swrtj::Trait")
swrtj_TraitExpression = Class(name="swrtj::TraitExpression")
swrtj_Class = Class(name="swrtj::Class")
swrtj_Constructor = Class(name="swrtj::Constructor")
swrtj_MethodName = Class(name="swrtj::MethodName")
swrtj_Parameter = Class(name="swrtj::Parameter")
swrtj_RecordOperation = Class(name="swrtj::RecordOperation")
swrtj_AnonimousRecord = Class(name="swrtj::AnonimousRecord")
BaseRecord = Class(name="BaseRecord")
swrtj_Field = Class(name="swrtj::Field")
swrtj_RecordName = Class(name="swrtj::RecordName")
swrtj_NestedRecordExpression = Class(name="swrtj::NestedRecordExpression")
swrtj_BaseTrait = Class(name="swrtj::BaseTrait")
swrtj_TraitOperation = Class(name="swrtj::TraitOperation")
swrtj_AnonimousTrait = Class(name="swrtj::AnonimousTrait")
BaseTrait = Class(name="BaseTrait")
swrtj_TraitElement = Class(name="swrtj::TraitElement")
swrtj_TraitName = Class(name="swrtj::TraitName")
swrtj_NestedTraitExpression = Class(name="swrtj::NestedTraitExpression")
TraitElement = Class(name="TraitElement")
swrtj_Type = Class(name="swrtj::Type")
swrtj_FieldName = Class(name="swrtj::FieldName")
swrtj_BooleanOperator = Class(name="swrtj::BooleanOperator")
swrtj_AtomicBooleanExpression = Class(name="swrtj::AtomicBooleanExpression")
swrtj_SimpleComparation = Class(name="swrtj::SimpleComparation")
AtomicBooleanExpression = Class(name="AtomicBooleanExpression")
swrtj_ReturnStatement = Class(name="swrtj::ReturnStatement")
swrtj_GenericExpression = Class(name="swrtj::GenericExpression")
swrtj_Statement = Class(name="swrtj::Statement")
swrtj_ExpressionStatement = Class(name="swrtj::ExpressionStatement")
Statement = Class(name="Statement")
swrtj_IfThenElseStatement = Class(name="swrtj::IfThenElseStatement")
swrtj_WhileStatement = Class(name="swrtj::WhileStatement")
swrtj_CompareOperator = Class(name="swrtj::CompareOperator")
swrtj_NestedBooleanExpression = Class(name="swrtj::NestedBooleanExpression")
swrtj_DottedExpression = Class(name="swrtj::DottedExpression")
swrtj_Start = Class(name="swrtj::Start")
swrtj_Message = Class(name="swrtj::Message")
swrtj_Null = Class(name="swrtj::Null")
Start = Class(name="Start")
swrtj_BooleanConstant = Class(name="swrtj::BooleanConstant")
swrtj_Input = Class(name="swrtj::Input")
swrtj_Number = Class(name="swrtj::Number")
swrtj_StringConstant = Class(name="swrtj::StringConstant")
swrtj_This = Class(name="swrtj::This")
swrtj_Args = Class(name="swrtj::Args")
swrtj_Output = Class(name="swrtj::Output")
swrtj_ConstructorInvocation = Class(name="swrtj::ConstructorInvocation")
swrtj_Cast = Class(name="swrtj::Cast")
swrtj_ParameterReference = Class(name="swrtj::ParameterReference")
swrtj_MethodInvocation = Class(name="swrtj::MethodInvocation")
Message = Class(name="Message")
swrtj_FieldAccess = Class(name="swrtj::FieldAccess")
swrtj_NestedExpression = Class(name="swrtj::NestedExpression")
swrtj_RecordExclude = Class(name="swrtj::RecordExclude")
RecordOperation = Class(name="RecordOperation")
swrtj_RecordRename = Class(name="swrtj::RecordRename")
swrtj_ParameterAssignment = Class(name="swrtj::ParameterAssignment")
swrtj_TraitExclude = Class(name="swrtj::TraitExclude")
TraitOperation = Class(name="TraitOperation")
swrtj_TraitAlias = Class(name="swrtj::TraitAlias")
swrtj_TraitFieldRename = Class(name="swrtj::TraitFieldRename")
swrtj_FieldDeclaration = Class(name="swrtj::FieldDeclaration")
Field = Class(name="Field")
swrtj_RequiredField = Class(name="swrtj::RequiredField")
swrtj_RequiredMethod = Class(name="swrtj::RequiredMethod")
Method_ = Class(name="Method")
swrtj_ProvidedMethod = Class(name="swrtj::ProvidedMethod")
swrtj_TraitMethodRename = Class(name="swrtj::TraitMethodRename")
swrtj_LocalParameter = Class(name="swrtj::LocalParameter")
swrtj_Expression = Class(name="swrtj::Expression")
swrtj_FormalParameter = Class(name="swrtj::FormalParameter")
Parameter_ = Class(name="Parameter")
swrtj_BooleanExpression = Class(name="swrtj::BooleanExpression")
GenericExpression = Class(name="GenericExpression")

# swrtj_Program class attributes and methods

# swrtj_Block class attributes and methods

# swrtj_BaseRecord class attributes and methods

# swrtj_File class attributes and methods

# swrtj_Import class attributes and methods
swrtj_Import_importURI: Property = Property(name="importURI", type=StringType)
swrtj_Import.attributes={swrtj_Import_importURI}

# swrtj_Element class attributes and methods
swrtj_Element_construct: Property = Property(name="construct", type=StringType)
swrtj_Element_name: Property = Property(name="name", type=StringType)
swrtj_Element.attributes={swrtj_Element_construct, swrtj_Element_name}

# swrtj_Interface class attributes and methods

# Element class attributes and methods

# swrtj_Method class attributes and methods

# swrtj_Record class attributes and methods

# swrtj_RecordExpression class attributes and methods

# swrtj_Trait class attributes and methods

# swrtj_TraitExpression class attributes and methods

# swrtj_Class class attributes and methods

# swrtj_Constructor class attributes and methods
swrtj_Constructor_name: Property = Property(name="name", type=StringType)
swrtj_Constructor.attributes={swrtj_Constructor_name}

# swrtj_MethodName class attributes and methods
swrtj_MethodName_name: Property = Property(name="name", type=StringType)
swrtj_MethodName.attributes={swrtj_MethodName_name}

# swrtj_Parameter class attributes and methods
swrtj_Parameter_name: Property = Property(name="name", type=StringType)
swrtj_Parameter.attributes={swrtj_Parameter_name}

# swrtj_RecordOperation class attributes and methods

# swrtj_AnonimousRecord class attributes and methods

# BaseRecord class attributes and methods

# swrtj_Field class attributes and methods

# swrtj_RecordName class attributes and methods

# swrtj_NestedRecordExpression class attributes and methods

# swrtj_BaseTrait class attributes and methods

# swrtj_TraitOperation class attributes and methods

# swrtj_AnonimousTrait class attributes and methods

# BaseTrait class attributes and methods

# swrtj_TraitElement class attributes and methods

# swrtj_TraitName class attributes and methods

# swrtj_NestedTraitExpression class attributes and methods

# TraitElement class attributes and methods

# swrtj_Type class attributes and methods
swrtj_Type_primitiveType: Property = Property(name="primitiveType", type=StringType)
swrtj_Type.attributes={swrtj_Type_primitiveType}

# swrtj_FieldName class attributes and methods
swrtj_FieldName_name: Property = Property(name="name", type=StringType)
swrtj_FieldName.attributes={swrtj_FieldName_name}

# swrtj_BooleanOperator class attributes and methods
swrtj_BooleanOperator_operator: Property = Property(name="operator", type=StringType)
swrtj_BooleanOperator.attributes={swrtj_BooleanOperator_operator}

# swrtj_AtomicBooleanExpression class attributes and methods
swrtj_AtomicBooleanExpression_negated: Property = Property(name="negated", type=BooleanType)
swrtj_AtomicBooleanExpression.attributes={swrtj_AtomicBooleanExpression_negated}

# swrtj_SimpleComparation class attributes and methods

# AtomicBooleanExpression class attributes and methods

# swrtj_ReturnStatement class attributes and methods

# swrtj_GenericExpression class attributes and methods

# swrtj_Statement class attributes and methods

# swrtj_ExpressionStatement class attributes and methods

# Statement class attributes and methods

# swrtj_IfThenElseStatement class attributes and methods

# swrtj_WhileStatement class attributes and methods

# swrtj_CompareOperator class attributes and methods
swrtj_CompareOperator_operator: Property = Property(name="operator", type=StringType)
swrtj_CompareOperator.attributes={swrtj_CompareOperator_operator}

# swrtj_NestedBooleanExpression class attributes and methods

# swrtj_DottedExpression class attributes and methods

# swrtj_Start class attributes and methods

# swrtj_Message class attributes and methods

# swrtj_Null class attributes and methods
swrtj_Null_null: Property = Property(name="null", type=BooleanType)
swrtj_Null.attributes={swrtj_Null_null}

# Start class attributes and methods

# swrtj_BooleanConstant class attributes and methods
swrtj_BooleanConstant_value: Property = Property(name="value", type=StringType)
swrtj_BooleanConstant.attributes={swrtj_BooleanConstant_value}

# swrtj_Input class attributes and methods
swrtj_Input_input: Property = Property(name="input", type=BooleanType)
swrtj_Input.attributes={swrtj_Input_input}

# swrtj_Number class attributes and methods
swrtj_Number_value: Property = Property(name="value", type=IntegerType)
swrtj_Number.attributes={swrtj_Number_value}

# swrtj_StringConstant class attributes and methods
swrtj_StringConstant_value: Property = Property(name="value", type=StringType)
swrtj_StringConstant.attributes={swrtj_StringConstant_value}

# swrtj_This class attributes and methods
swrtj_This_this: Property = Property(name="this", type=BooleanType)
swrtj_This.attributes={swrtj_This_this}

# swrtj_Args class attributes and methods
swrtj_Args_args: Property = Property(name="args", type=BooleanType)
swrtj_Args.attributes={swrtj_Args_args}

# swrtj_Output class attributes and methods
swrtj_Output_output: Property = Property(name="output", type=BooleanType)
swrtj_Output.attributes={swrtj_Output_output}

# swrtj_ConstructorInvocation class attributes and methods

# swrtj_Cast class attributes and methods

# swrtj_ParameterReference class attributes and methods

# swrtj_MethodInvocation class attributes and methods

# Message class attributes and methods

# swrtj_FieldAccess class attributes and methods

# swrtj_NestedExpression class attributes and methods

# swrtj_RecordExclude class attributes and methods

# RecordOperation class attributes and methods

# swrtj_RecordRename class attributes and methods

# swrtj_ParameterAssignment class attributes and methods

# swrtj_TraitExclude class attributes and methods

# TraitOperation class attributes and methods

# swrtj_TraitAlias class attributes and methods

# swrtj_TraitFieldRename class attributes and methods

# swrtj_FieldDeclaration class attributes and methods
swrtj_FieldDeclaration_modifier: Property = Property(name="modifier", type=StringType)
swrtj_FieldDeclaration.attributes={swrtj_FieldDeclaration_modifier}

# Field class attributes and methods

# swrtj_RequiredField class attributes and methods

# swrtj_RequiredMethod class attributes and methods

# Method class attributes and methods

# swrtj_ProvidedMethod class attributes and methods
swrtj_ProvidedMethod_isSynchronized: Property = Property(name="isSynchronized", type=BooleanType)
swrtj_ProvidedMethod.attributes={swrtj_ProvidedMethod_isSynchronized}

# swrtj_TraitMethodRename class attributes and methods

# swrtj_LocalParameter class attributes and methods

# swrtj_Expression class attributes and methods
swrtj_Expression_sign: Property = Property(name="sign", type=StringType)
swrtj_Expression_operatorList: Property = Property(name="operatorList", type=StringType)
swrtj_Expression.attributes={swrtj_Expression_sign, swrtj_Expression_operatorList}

# swrtj_FormalParameter class attributes and methods

# Parameter class attributes and methods

# swrtj_BooleanExpression class attributes and methods

# GenericExpression class attributes and methods

# Relationships
block19: BinaryAssociation = BinaryAssociation(
    name="block19",
    ends={
        Property(name="swrtj_Block", type=swrtj_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_Program", type=swrtj_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
recordList20: BinaryAssociation = BinaryAssociation(
    name="recordList20",
    ends={
        Property(name="swrtj_BaseRecord", type=swrtj_RecordExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_RecordExpression21", type=swrtj_BaseRecord, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importList0: BinaryAssociation = BinaryAssociation(
    name="importList0",
    ends={
        Property(name="swrtj_Import", type=swrtj_File, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_File", type=swrtj_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elementList1: BinaryAssociation = BinaryAssociation(
    name="elementList1",
    ends={
        Property(name="swrtj_Element", type=swrtj_File, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_File2", type=swrtj_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extendsList4: BinaryAssociation = BinaryAssociation(
    name="extendsList4",
    ends={
        Property(name="swrtj_Interface", type=swrtj_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_Interface3", type=swrtj_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
requiredMethodList5: BinaryAssociation = BinaryAssociation(
    name="requiredMethodList5",
    ends={
        Property(name="swrtj_Method", type=swrtj_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_Interface6", type=swrtj_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression7: BinaryAssociation = BinaryAssociation(
    name="expression7",
    ends={
        Property(name="swrtj_RecordExpression", type=swrtj_Record, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_Record", type=swrtj_RecordExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression8: BinaryAssociation = BinaryAssociation(
    name="expression8",
    ends={
        Property(name="swrtj_TraitExpression", type=swrtj_Trait, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_Trait", type=swrtj_TraitExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
implementsList9: BinaryAssociation = BinaryAssociation(
    name="implementsList9",
    ends={
        Property(name="swrtj_Interface10", type=swrtj_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_Class", type=swrtj_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
recordExpression11: BinaryAssociation = BinaryAssociation(
    name="recordExpression11",
    ends={
        Property(name="swrtj_RecordExpression13", type=swrtj_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_Class12", type=swrtj_RecordExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
traitExpression14: BinaryAssociation = BinaryAssociation(
    name="traitExpression14",
    ends={
        Property(name="swrtj_TraitExpression16", type=swrtj_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_Class15", type=swrtj_TraitExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constructorList17: BinaryAssociation = BinaryAssociation(
    name="constructorList17",
    ends={
        Property(name="swrtj_Constructor", type=swrtj_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_Class18", type=swrtj_Constructor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType42: BinaryAssociation = BinaryAssociation(
    name="returnType42",
    ends={
        Property(name="swrtj_Type44", type=swrtj_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_Method43", type=swrtj_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
methodRef45: BinaryAssociation = BinaryAssociation(
    name="methodRef45",
    ends={
        Property(name="swrtj_MethodName", type=swrtj_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_Method46", type=swrtj_MethodName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterList47: BinaryAssociation = BinaryAssociation(
    name="parameterList47",
    ends={
        Property(name="swrtj_Parameter", type=swrtj_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_Method48", type=swrtj_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operationList22: BinaryAssociation = BinaryAssociation(
    name="operationList22",
    ends={
        Property(name="swrtj_RecordOperation", type=swrtj_BaseRecord, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_BaseRecord23", type=swrtj_RecordOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declarationList24: BinaryAssociation = BinaryAssociation(
    name="declarationList24",
    ends={
        Property(name="swrtj_Field", type=swrtj_AnonimousRecord, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_AnonimousRecord", type=swrtj_Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
record25: BinaryAssociation = BinaryAssociation(
    name="record25",
    ends={
        Property(name="swrtj_Record26", type=swrtj_RecordName, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_RecordName", type=swrtj_Record, multiplicity=Multiplicity(0, 1))
    }
)
expression27: BinaryAssociation = BinaryAssociation(
    name="expression27",
    ends={
        Property(name="swrtj_RecordExpression28", type=swrtj_NestedRecordExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_NestedRecordExpression", type=swrtj_RecordExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
traitList29: BinaryAssociation = BinaryAssociation(
    name="traitList29",
    ends={
        Property(name="swrtj_BaseTrait", type=swrtj_TraitExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_TraitExpression30", type=swrtj_BaseTrait, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operationList31: BinaryAssociation = BinaryAssociation(
    name="operationList31",
    ends={
        Property(name="swrtj_TraitOperation", type=swrtj_BaseTrait, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_BaseTrait32", type=swrtj_TraitOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definitionList33: BinaryAssociation = BinaryAssociation(
    name="definitionList33",
    ends={
        Property(name="swrtj_TraitElement", type=swrtj_AnonimousTrait, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_AnonimousTrait", type=swrtj_TraitElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trait34: BinaryAssociation = BinaryAssociation(
    name="trait34",
    ends={
        Property(name="swrtj_Trait35", type=swrtj_TraitName, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_TraitName", type=swrtj_Trait, multiplicity=Multiplicity(0, 1))
    }
)
expression36: BinaryAssociation = BinaryAssociation(
    name="expression36",
    ends={
        Property(name="swrtj_TraitExpression37", type=swrtj_NestedTraitExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_NestedTraitExpression", type=swrtj_TraitExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type38: BinaryAssociation = BinaryAssociation(
    name="type38",
    ends={
        Property(name="swrtj_Type", type=swrtj_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_Field39", type=swrtj_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fieldRef40: BinaryAssociation = BinaryAssociation(
    name="fieldRef40",
    ends={
        Property(name="swrtj_FieldName", type=swrtj_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_Field41", type=swrtj_FieldName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whileBlock79: BinaryAssociation = BinaryAssociation(
    name="whileBlock79",
    ends={
        Property(name="swrtj_WhileStatement80", type=swrtj_Block, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="swrtj_Block81", type=swrtj_WhileStatement, multiplicity=Multiplicity(1, 1))
    }
)
parameterList49: BinaryAssociation = BinaryAssociation(
    name="parameterList49",
    ends={
        Property(name="swrtj_Parameter51", type=swrtj_Constructor, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_Constructor50", type=swrtj_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block52: BinaryAssociation = BinaryAssociation(
    name="block52",
    ends={
        Property(name="swrtj_Block54", type=swrtj_Constructor, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_Constructor53", type=swrtj_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression55: BinaryAssociation = BinaryAssociation(
    name="expression55",
    ends={
        Property(name="swrtj_GenericExpression", type=swrtj_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_ReturnStatement", type=swrtj_GenericExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type56: BinaryAssociation = BinaryAssociation(
    name="type56",
    ends={
        Property(name="swrtj_Type58", type=swrtj_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_Parameter57", type=swrtj_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interfaceType59: BinaryAssociation = BinaryAssociation(
    name="interfaceType59",
    ends={
        Property(name="swrtj_Interface61", type=swrtj_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_Type60", type=swrtj_Interface, multiplicity=Multiplicity(0, 1))
    }
)
parameterList62: BinaryAssociation = BinaryAssociation(
    name="parameterList62",
    ends={
        Property(name="swrtj_Parameter64", type=swrtj_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_Block63", type=swrtj_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statementList65: BinaryAssociation = BinaryAssociation(
    name="statementList65",
    ends={
        Property(name="swrtj_Statement", type=swrtj_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_Block66", type=swrtj_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression67: BinaryAssociation = BinaryAssociation(
    name="expression67",
    ends={
        Property(name="swrtj_GenericExpression68", type=swrtj_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_ExpressionStatement", type=swrtj_GenericExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condiction69: BinaryAssociation = BinaryAssociation(
    name="condiction69",
    ends={
        Property(name="swrtj_GenericExpression70", type=swrtj_IfThenElseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_IfThenElseStatement", type=swrtj_GenericExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trueBranch71: BinaryAssociation = BinaryAssociation(
    name="trueBranch71",
    ends={
        Property(name="swrtj_Block73", type=swrtj_IfThenElseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_IfThenElseStatement72", type=swrtj_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
falseBranch74: BinaryAssociation = BinaryAssociation(
    name="falseBranch74",
    ends={
        Property(name="swrtj_Block76", type=swrtj_IfThenElseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_IfThenElseStatement75", type=swrtj_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condiction77: BinaryAssociation = BinaryAssociation(
    name="condiction77",
    ends={
        Property(name="swrtj_GenericExpression78", type=swrtj_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_WhileStatement", type=swrtj_GenericExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftExpression82: BinaryAssociation = BinaryAssociation(
    name="leftExpression82",
    ends={
        Property(name="swrtj_GenericExpression83", type=swrtj_SimpleComparation, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_SimpleComparation", type=swrtj_GenericExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
compare84: BinaryAssociation = BinaryAssociation(
    name="compare84",
    ends={
        Property(name="swrtj_CompareOperator", type=swrtj_SimpleComparation, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_SimpleComparation85", type=swrtj_CompareOperator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightExpression86: BinaryAssociation = BinaryAssociation(
    name="rightExpression86",
    ends={
        Property(name="swrtj_GenericExpression88", type=swrtj_SimpleComparation, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_SimpleComparation87", type=swrtj_GenericExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nestedExpression89: BinaryAssociation = BinaryAssociation(
    name="nestedExpression89",
    ends={
        Property(name="swrtj_GenericExpression90", type=swrtj_NestedBooleanExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_NestedBooleanExpression", type=swrtj_GenericExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
start91: BinaryAssociation = BinaryAssociation(
    name="start91",
    ends={
        Property(name="swrtj_Start", type=swrtj_DottedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_DottedExpression", type=swrtj_Start, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
receiver93: BinaryAssociation = BinaryAssociation(
    name="receiver93",
    ends={
        Property(name="swrtj_DottedExpression94", type=swrtj_DottedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_DottedExpression92", type=swrtj_DottedExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
message95: BinaryAssociation = BinaryAssociation(
    name="message95",
    ends={
        Property(name="swrtj_Message", type=swrtj_DottedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_DottedExpression96", type=swrtj_Message, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value97: BinaryAssociation = BinaryAssociation(
    name="value97",
    ends={
        Property(name="swrtj_GenericExpression99", type=swrtj_DottedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_DottedExpression98", type=swrtj_GenericExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classRef102: BinaryAssociation = BinaryAssociation(
    name="classRef102",
    ends={
        Property(name="swrtj_Class103", type=swrtj_ConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_ConstructorInvocation", type=swrtj_Class, multiplicity=Multiplicity(0, 1))
    }
)
argumentList104: BinaryAssociation = BinaryAssociation(
    name="argumentList104",
    ends={
        Property(name="swrtj_GenericExpression106", type=swrtj_ConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_ConstructorInvocation105", type=swrtj_GenericExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type107: BinaryAssociation = BinaryAssociation(
    name="type107",
    ends={
        Property(name="swrtj_Type108", type=swrtj_Cast, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_Cast", type=swrtj_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter100: BinaryAssociation = BinaryAssociation(
    name="parameter100",
    ends={
        Property(name="swrtj_Parameter101", type=swrtj_ParameterReference, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_ParameterReference", type=swrtj_Parameter, multiplicity=Multiplicity(0, 1))
    }
)
expression112: BinaryAssociation = BinaryAssociation(
    name="expression112",
    ends={
        Property(name="swrtj_GenericExpression113", type=swrtj_NestedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_NestedExpression", type=swrtj_GenericExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
method114: BinaryAssociation = BinaryAssociation(
    name="method114",
    ends={
        Property(name="swrtj_MethodName115", type=swrtj_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_MethodInvocation", type=swrtj_MethodName, multiplicity=Multiplicity(0, 1))
    }
)
argumentList116: BinaryAssociation = BinaryAssociation(
    name="argumentList116",
    ends={
        Property(name="swrtj_GenericExpression118", type=swrtj_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_MethodInvocation117", type=swrtj_GenericExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
start109: BinaryAssociation = BinaryAssociation(
    name="start109",
    ends={
        Property(name="swrtj_Start111", type=swrtj_Cast, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_Cast110", type=swrtj_Start, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter121: BinaryAssociation = BinaryAssociation(
    name="parameter121",
    ends={
        Property(name="swrtj_Parameter122", type=swrtj_ParameterAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_ParameterAssignment", type=swrtj_Parameter, multiplicity=Multiplicity(0, 1))
    }
)
value123: BinaryAssociation = BinaryAssociation(
    name="value123",
    ends={
        Property(name="swrtj_GenericExpression125", type=swrtj_ParameterAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_ParameterAssignment124", type=swrtj_GenericExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
field126: BinaryAssociation = BinaryAssociation(
    name="field126",
    ends={
        Property(name="swrtj_FieldName127", type=swrtj_RecordExclude, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_RecordExclude", type=swrtj_FieldName, multiplicity=Multiplicity(0, 1))
    }
)
field119: BinaryAssociation = BinaryAssociation(
    name="field119",
    ends={
        Property(name="swrtj_FieldName120", type=swrtj_FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_FieldAccess", type=swrtj_FieldName, multiplicity=Multiplicity(0, 1))
    }
)
method133: BinaryAssociation = BinaryAssociation(
    name="method133",
    ends={
        Property(name="swrtj_MethodName134", type=swrtj_TraitExclude, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_TraitExclude", type=swrtj_MethodName, multiplicity=Multiplicity(0, 1))
    }
)
originalMethod135: BinaryAssociation = BinaryAssociation(
    name="originalMethod135",
    ends={
        Property(name="swrtj_MethodName136", type=swrtj_TraitAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_TraitAlias", type=swrtj_MethodName, multiplicity=Multiplicity(0, 1))
    }
)
newMethod137: BinaryAssociation = BinaryAssociation(
    name="newMethod137",
    ends={
        Property(name="swrtj_MethodName139", type=swrtj_TraitAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_TraitAlias138", type=swrtj_MethodName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
originalField128: BinaryAssociation = BinaryAssociation(
    name="originalField128",
    ends={
        Property(name="swrtj_FieldName129", type=swrtj_RecordRename, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_RecordRename", type=swrtj_FieldName, multiplicity=Multiplicity(0, 1))
    }
)
newField130: BinaryAssociation = BinaryAssociation(
    name="newField130",
    ends={
        Property(name="swrtj_FieldName132", type=swrtj_RecordRename, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_RecordRename131", type=swrtj_FieldName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
newMethod142: BinaryAssociation = BinaryAssociation(
    name="newMethod142",
    ends={
        Property(name="swrtj_MethodName144", type=swrtj_TraitMethodRename, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_TraitMethodRename143", type=swrtj_MethodName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
originalField145: BinaryAssociation = BinaryAssociation(
    name="originalField145",
    ends={
        Property(name="swrtj_FieldName146", type=swrtj_TraitFieldRename, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_TraitFieldRename", type=swrtj_FieldName, multiplicity=Multiplicity(0, 1))
    }
)
newField147: BinaryAssociation = BinaryAssociation(
    name="newField147",
    ends={
        Property(name="swrtj_FieldName149", type=swrtj_TraitFieldRename, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_TraitFieldRename148", type=swrtj_FieldName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
originalMethod140: BinaryAssociation = BinaryAssociation(
    name="originalMethod140",
    ends={
        Property(name="swrtj_MethodName141", type=swrtj_TraitMethodRename, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_TraitMethodRename", type=swrtj_MethodName, multiplicity=Multiplicity(0, 1))
    }
)
atomicList155: BinaryAssociation = BinaryAssociation(
    name="atomicList155",
    ends={
        Property(name="swrtj_AtomicBooleanExpression", type=swrtj_BooleanExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_BooleanExpression", type=swrtj_AtomicBooleanExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
booleanOperatorList156: BinaryAssociation = BinaryAssociation(
    name="booleanOperatorList156",
    ends={
        Property(name="swrtj_BooleanOperator", type=swrtj_BooleanExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_BooleanExpression157", type=swrtj_BooleanOperator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value158: BinaryAssociation = BinaryAssociation(
    name="value158",
    ends={
        Property(name="swrtj_GenericExpression159", type=swrtj_LocalParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_LocalParameter", type=swrtj_GenericExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
termList160: BinaryAssociation = BinaryAssociation(
    name="termList160",
    ends={
        Property(name="swrtj_DottedExpression161", type=swrtj_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_Expression", type=swrtj_DottedExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block150: BinaryAssociation = BinaryAssociation(
    name="block150",
    ends={
        Property(name="swrtj_Block151", type=swrtj_ProvidedMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_ProvidedMethod", type=swrtj_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnStatement152: BinaryAssociation = BinaryAssociation(
    name="returnStatement152",
    ends={
        Property(name="swrtj_ReturnStatement154", type=swrtj_ProvidedMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="swrtj_ProvidedMethod153", type=swrtj_ReturnStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_swrtj_Program_Element = Generalization(general=Element, specific=swrtj_Program)
gen_swrtj_Interface_Element = Generalization(general=Element, specific=swrtj_Interface)
gen_swrtj_Record_Element = Generalization(general=Element, specific=swrtj_Record)
gen_swrtj_Trait_Element = Generalization(general=Element, specific=swrtj_Trait)
gen_swrtj_Class_Element = Generalization(general=Element, specific=swrtj_Class)
gen_swrtj_Method_TraitElement = Generalization(general=TraitElement, specific=swrtj_Method)
gen_swrtj_AnonimousRecord_BaseRecord = Generalization(general=BaseRecord, specific=swrtj_AnonimousRecord)
gen_swrtj_RecordName_BaseRecord = Generalization(general=BaseRecord, specific=swrtj_RecordName)
gen_swrtj_NestedRecordExpression_BaseRecord = Generalization(general=BaseRecord, specific=swrtj_NestedRecordExpression)
gen_swrtj_AnonimousTrait_BaseTrait = Generalization(general=BaseTrait, specific=swrtj_AnonimousTrait)
gen_swrtj_TraitName_BaseTrait = Generalization(general=BaseTrait, specific=swrtj_TraitName)
gen_swrtj_NestedTraitExpression_BaseTrait = Generalization(general=BaseTrait, specific=swrtj_NestedTraitExpression)
gen_swrtj_Field_TraitElement = Generalization(general=TraitElement, specific=swrtj_Field)
gen_swrtj_SimpleComparation_AtomicBooleanExpression = Generalization(general=AtomicBooleanExpression, specific=swrtj_SimpleComparation)
gen_swrtj_ExpressionStatement_Statement = Generalization(general=Statement, specific=swrtj_ExpressionStatement)
gen_swrtj_IfThenElseStatement_Statement = Generalization(general=Statement, specific=swrtj_IfThenElseStatement)
gen_swrtj_WhileStatement_Statement = Generalization(general=Statement, specific=swrtj_WhileStatement)
gen_swrtj_NestedBooleanExpression_AtomicBooleanExpression = Generalization(general=AtomicBooleanExpression, specific=swrtj_NestedBooleanExpression)
gen_swrtj_Null_Start = Generalization(general=Start, specific=swrtj_Null)
gen_swrtj_BooleanConstant_Start = Generalization(general=Start, specific=swrtj_BooleanConstant)
gen_swrtj_Input_Start = Generalization(general=Start, specific=swrtj_Input)
gen_swrtj_Number_Start = Generalization(general=Start, specific=swrtj_Number)
gen_swrtj_StringConstant_Start = Generalization(general=Start, specific=swrtj_StringConstant)
gen_swrtj_This_Start = Generalization(general=Start, specific=swrtj_This)
gen_swrtj_Args_Start = Generalization(general=Start, specific=swrtj_Args)
gen_swrtj_Output_Start = Generalization(general=Start, specific=swrtj_Output)
gen_swrtj_ConstructorInvocation_Start = Generalization(general=Start, specific=swrtj_ConstructorInvocation)
gen_swrtj_Cast_Start = Generalization(general=Start, specific=swrtj_Cast)
gen_swrtj_ParameterReference_Start = Generalization(general=Start, specific=swrtj_ParameterReference)
gen_swrtj_MethodInvocation_Message = Generalization(general=Message, specific=swrtj_MethodInvocation)
gen_swrtj_FieldAccess_Message = Generalization(general=Message, specific=swrtj_FieldAccess)
gen_swrtj_NestedExpression_Start = Generalization(general=Start, specific=swrtj_NestedExpression)
gen_swrtj_RecordExclude_RecordOperation = Generalization(general=RecordOperation, specific=swrtj_RecordExclude)
gen_swrtj_RecordRename_RecordOperation = Generalization(general=RecordOperation, specific=swrtj_RecordRename)
gen_swrtj_ParameterAssignment_Start = Generalization(general=Start, specific=swrtj_ParameterAssignment)
gen_swrtj_TraitExclude_TraitOperation = Generalization(general=TraitOperation, specific=swrtj_TraitExclude)
gen_swrtj_TraitAlias_TraitOperation = Generalization(general=TraitOperation, specific=swrtj_TraitAlias)
gen_swrtj_TraitFieldRename_TraitOperation = Generalization(general=TraitOperation, specific=swrtj_TraitFieldRename)
gen_swrtj_FieldDeclaration_Field = Generalization(general=Field, specific=swrtj_FieldDeclaration)
gen_swrtj_RequiredField_Field = Generalization(general=Field, specific=swrtj_RequiredField)
gen_swrtj_RequiredMethod_Method = Generalization(general=Method_, specific=swrtj_RequiredMethod)
gen_swrtj_ProvidedMethod_Method = Generalization(general=Method_, specific=swrtj_ProvidedMethod)
gen_swrtj_TraitMethodRename_TraitOperation = Generalization(general=TraitOperation, specific=swrtj_TraitMethodRename)
gen_swrtj_LocalParameter_Parameter = Generalization(general=Parameter_, specific=swrtj_LocalParameter)
gen_swrtj_Expression_GenericExpression = Generalization(general=GenericExpression, specific=swrtj_Expression)
gen_swrtj_FormalParameter_Parameter = Generalization(general=Parameter_, specific=swrtj_FormalParameter)
gen_swrtj_BooleanExpression_GenericExpression = Generalization(general=GenericExpression, specific=swrtj_BooleanExpression)

# Domain Model
domain_model = DomainModel(
    name="swrtj",
    types={swrtj_Program, swrtj_Block, swrtj_BaseRecord, swrtj_File, swrtj_Import, swrtj_Element, swrtj_Interface, Element, swrtj_Method, swrtj_Record, swrtj_RecordExpression, swrtj_Trait, swrtj_TraitExpression, swrtj_Class, swrtj_Constructor, swrtj_MethodName, swrtj_Parameter, swrtj_RecordOperation, swrtj_AnonimousRecord, BaseRecord, swrtj_Field, swrtj_RecordName, swrtj_NestedRecordExpression, swrtj_BaseTrait, swrtj_TraitOperation, swrtj_AnonimousTrait, BaseTrait, swrtj_TraitElement, swrtj_TraitName, swrtj_NestedTraitExpression, TraitElement, swrtj_Type, swrtj_FieldName, swrtj_BooleanOperator, swrtj_AtomicBooleanExpression, swrtj_SimpleComparation, AtomicBooleanExpression, swrtj_ReturnStatement, swrtj_GenericExpression, swrtj_Statement, swrtj_ExpressionStatement, Statement, swrtj_IfThenElseStatement, swrtj_WhileStatement, swrtj_CompareOperator, swrtj_NestedBooleanExpression, swrtj_DottedExpression, swrtj_Start, swrtj_Message, swrtj_Null, Start, swrtj_BooleanConstant, swrtj_Input, swrtj_Number, swrtj_StringConstant, swrtj_This, swrtj_Args, swrtj_Output, swrtj_ConstructorInvocation, swrtj_Cast, swrtj_ParameterReference, swrtj_MethodInvocation, Message, swrtj_FieldAccess, swrtj_NestedExpression, swrtj_RecordExclude, RecordOperation, swrtj_RecordRename, swrtj_ParameterAssignment, swrtj_TraitExclude, TraitOperation, swrtj_TraitAlias, swrtj_TraitFieldRename, swrtj_FieldDeclaration, Field, swrtj_RequiredField, swrtj_RequiredMethod, Method_, swrtj_ProvidedMethod, swrtj_TraitMethodRename, swrtj_LocalParameter, swrtj_Expression, swrtj_FormalParameter, Parameter_, swrtj_BooleanExpression, GenericExpression},
    associations={block19, recordList20, importList0, elementList1, extendsList4, requiredMethodList5, expression7, expression8, implementsList9, recordExpression11, traitExpression14, constructorList17, returnType42, methodRef45, parameterList47, operationList22, declarationList24, record25, expression27, traitList29, operationList31, definitionList33, trait34, expression36, type38, fieldRef40, whileBlock79, parameterList49, block52, expression55, type56, interfaceType59, parameterList62, statementList65, expression67, condiction69, trueBranch71, falseBranch74, condiction77, leftExpression82, compare84, rightExpression86, nestedExpression89, start91, receiver93, message95, value97, classRef102, argumentList104, type107, parameter100, expression112, method114, argumentList116, start109, parameter121, value123, field126, field119, method133, originalMethod135, newMethod137, originalField128, newField130, newMethod142, originalField145, newField147, originalMethod140, atomicList155, booleanOperatorList156, value158, termList160, block150, returnStatement152},
    generalizations={gen_swrtj_Program_Element, gen_swrtj_Interface_Element, gen_swrtj_Record_Element, gen_swrtj_Trait_Element, gen_swrtj_Class_Element, gen_swrtj_Method_TraitElement, gen_swrtj_AnonimousRecord_BaseRecord, gen_swrtj_RecordName_BaseRecord, gen_swrtj_NestedRecordExpression_BaseRecord, gen_swrtj_AnonimousTrait_BaseTrait, gen_swrtj_TraitName_BaseTrait, gen_swrtj_NestedTraitExpression_BaseTrait, gen_swrtj_Field_TraitElement, gen_swrtj_SimpleComparation_AtomicBooleanExpression, gen_swrtj_ExpressionStatement_Statement, gen_swrtj_IfThenElseStatement_Statement, gen_swrtj_WhileStatement_Statement, gen_swrtj_NestedBooleanExpression_AtomicBooleanExpression, gen_swrtj_Null_Start, gen_swrtj_BooleanConstant_Start, gen_swrtj_Input_Start, gen_swrtj_Number_Start, gen_swrtj_StringConstant_Start, gen_swrtj_This_Start, gen_swrtj_Args_Start, gen_swrtj_Output_Start, gen_swrtj_ConstructorInvocation_Start, gen_swrtj_Cast_Start, gen_swrtj_ParameterReference_Start, gen_swrtj_MethodInvocation_Message, gen_swrtj_FieldAccess_Message, gen_swrtj_NestedExpression_Start, gen_swrtj_RecordExclude_RecordOperation, gen_swrtj_RecordRename_RecordOperation, gen_swrtj_ParameterAssignment_Start, gen_swrtj_TraitExclude_TraitOperation, gen_swrtj_TraitAlias_TraitOperation, gen_swrtj_TraitFieldRename_TraitOperation, gen_swrtj_FieldDeclaration_Field, gen_swrtj_RequiredField_Field, gen_swrtj_RequiredMethod_Method, gen_swrtj_ProvidedMethod_Method, gen_swrtj_TraitMethodRename_TraitOperation, gen_swrtj_LocalParameter_Parameter, gen_swrtj_Expression_GenericExpression, gen_swrtj_FormalParameter_Parameter, gen_swrtj_BooleanExpression_GenericExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)