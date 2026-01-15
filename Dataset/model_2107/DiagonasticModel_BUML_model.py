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
OperatorTypeEnum: Enumeration = Enumeration(
    name="OperatorTypeEnum",
    literals={
            EnumerationLiteral(name="eq"),
			EnumerationLiteral(name="ne"),
			EnumerationLiteral(name="gt"),
			EnumerationLiteral(name="lt"),
			EnumerationLiteral(name="bt")
    }
)

SignalTypeEnum: Enumeration = Enumeration(
    name="SignalTypeEnum",
    literals={
            EnumerationLiteral(name="SIGNAL"),
			EnumerationLiteral(name="ENVIRONMENT"),
			EnumerationLiteral(name="SYSTEM"),
			EnumerationLiteral(name="UNDEFINED")
    }
)

CreationModeEnum: Enumeration = Enumeration(
    name="CreationModeEnum",
    literals={
            EnumerationLiteral(name="IMPORTED"),
			EnumerationLiteral(name="USER_DEFINED")
    }
)

ExecutionStatueTypeEnum: Enumeration = Enumeration(
    name="ExecutionStatueTypeEnum",
    literals={
            EnumerationLiteral(name="NOT_EXECUTED"),
			EnumerationLiteral(name="PASS"),
			EnumerationLiteral(name="FAIL")
    }
)

TraceabilityArtifactEnum: Enumeration = Enumeration(
    name="TraceabilityArtifactEnum",
    literals={
            EnumerationLiteral(name="REQUIREMENT"),
			EnumerationLiteral(name="TEST"),
			EnumerationLiteral(name="BUG"),
			EnumerationLiteral(name="OTHERS")
    }
)

# Classes
DiagonosticModel_TestGroup = Class(name="DiagonosticModel::TestGroup")
DiagonosticModel_TestSpecification = Class(name="DiagonosticModel::TestSpecification")
DiagonosticModel_TestCase = Class(name="DiagonosticModel::TestCase")
DiagonosticModel_ExternalReference = Class(name="DiagonosticModel::ExternalReference")
DiagonosticModel_CAPLTestCase = Class(name="DiagonosticModel::CAPLTestCase")
DiagonosticModel_Variant = Class(name="DiagonosticModel::Variant")
DiagonosticModel_ImportArtifact = Class(name="DiagonosticModel::ImportArtifact")
DiagonosticModel_TracebilityArtifact = Class(name="DiagonosticModel::TracebilityArtifact")
DiagonosticModel_TestStep = Class(name="DiagonosticModel::TestStep", is_abstract=True)
DiagonosticModel_SetAction = Class(name="DiagonosticModel::SetAction")
DiagonosticModel_SignalType = Class(name="DiagonosticModel::SignalType")
DiagonosticModel_WaitAction = Class(name="DiagonosticModel::WaitAction")
Action = Class(name="Action")
DiagonosticModel_CheckAction = Class(name="DiagonosticModel::CheckAction")
DiagonosticModel_DiagnosticRequest = Class(name="DiagonosticModel::DiagnosticRequest")
DiagonosticModel_DiagnosticResponse = Class(name="DiagonosticModel::DiagnosticResponse")
DiagonosticModel_CAPLParam = Class(name="DiagonosticModel::CAPLParam")
DiagonosticModel_DiagnosticService = Class(name="DiagonosticModel::DiagnosticService")
DiagonosticModel_CAPLTestStep = Class(name="DiagonosticModel::CAPLTestStep")
DiagonosticModel_DiagnosticParam = Class(name="DiagonosticModel::DiagnosticParam")
DiagonosticModel_DiagnosticParamValueType = Class(name="DiagonosticModel::DiagnosticParamValueType", is_abstract=True)
DiagonosticModel_Action = Class(name="DiagonosticModel::Action", is_abstract=True)
TestStep = Class(name="TestStep")
DiagonosticModel_BlockAction = Class(name="DiagonosticModel::BlockAction")
DiagonosticModel_ForLoop = Class(name="DiagonosticModel::ForLoop")
BlockAction = Class(name="BlockAction")
DiagonosticModel_Var = Class(name="DiagonosticModel::Var")
DiagnosticParamValueType = Class(name="DiagnosticParamValueType")
DiagonosticModel_OneOf = Class(name="DiagonosticModel::OneOf")
DiagonosticModel_Range = Class(name="DiagonosticModel::Range")
DiagonosticModel_WhileLoop = Class(name="DiagonosticModel::WhileLoop")

# DiagonosticModel_TestGroup class attributes and methods
DiagonosticModel_TestGroup_name: Property = Property(name="name", type=StringType)
DiagonosticModel_TestGroup_description: Property = Property(name="description", type=StringType)
DiagonosticModel_TestGroup.attributes={DiagonosticModel_TestGroup_name, DiagonosticModel_TestGroup_description}

# DiagonosticModel_TestSpecification class attributes and methods
DiagonosticModel_TestSpecification_name: Property = Property(name="name", type=StringType)
DiagonosticModel_TestSpecification_version: Property = Property(name="version", type=StringType)
DiagonosticModel_TestSpecification_description: Property = Property(name="description", type=StringType)
DiagonosticModel_TestSpecification_functionName: Property = Property(name="functionName", type=StringType)
DiagonosticModel_TestSpecification_functionVersion: Property = Property(name="functionVersion", type=StringType)
DiagonosticModel_TestSpecification_author: Property = Property(name="author", type=StringType)
DiagonosticModel_TestSpecification_m_getSignals: Method = Method(name="getSignals", parameters={}, type=StringType)
DiagonosticModel_TestSpecification.attributes={DiagonosticModel_TestSpecification_version, DiagonosticModel_TestSpecification_functionName, DiagonosticModel_TestSpecification_description, DiagonosticModel_TestSpecification_name, DiagonosticModel_TestSpecification_author, DiagonosticModel_TestSpecification_functionVersion}
DiagonosticModel_TestSpecification.methods={DiagonosticModel_TestSpecification_m_getSignals}

# DiagonosticModel_TestCase class attributes and methods
DiagonosticModel_TestCase_requirementID: Property = Property(name="requirementID", type=StringType)
DiagonosticModel_TestCase_executionStatus: Property = Property(name="executionStatus", type=StringType)
DiagonosticModel_TestCase_skip: Property = Property(name="skip", type=BooleanType)
DiagonosticModel_TestCase_name: Property = Property(name="name", type=StringType)
DiagonosticModel_TestCase_id: Property = Property(name="id", type=StringType)
DiagonosticModel_TestCase_description: Property = Property(name="description", type=StringType)
DiagonosticModel_TestCase.attributes={DiagonosticModel_TestCase_skip, DiagonosticModel_TestCase_requirementID, DiagonosticModel_TestCase_name, DiagonosticModel_TestCase_description, DiagonosticModel_TestCase_executionStatus, DiagonosticModel_TestCase_id}

# DiagonosticModel_ExternalReference class attributes and methods
DiagonosticModel_ExternalReference_title: Property = Property(name="title", type=StringType)
DiagonosticModel_ExternalReference_url: Property = Property(name="url", type=StringType)
DiagonosticModel_ExternalReference_owner: Property = Property(name="owner", type=StringType)
DiagonosticModel_ExternalReference_type: Property = Property(name="type", type=StringType)
DiagonosticModel_ExternalReference.attributes={DiagonosticModel_ExternalReference_owner, DiagonosticModel_ExternalReference_type, DiagonosticModel_ExternalReference_url, DiagonosticModel_ExternalReference_title}

# DiagonosticModel_CAPLTestCase class attributes and methods
DiagonosticModel_CAPLTestCase_name: Property = Property(name="name", type=StringType)
DiagonosticModel_CAPLTestCase.attributes={DiagonosticModel_CAPLTestCase_name}

# DiagonosticModel_Variant class attributes and methods
DiagonosticModel_Variant_name: Property = Property(name="name", type=StringType)
DiagonosticModel_Variant_description: Property = Property(name="description", type=StringType)
DiagonosticModel_Variant.attributes={DiagonosticModel_Variant_name, DiagonosticModel_Variant_description}

# DiagonosticModel_ImportArtifact class attributes and methods
DiagonosticModel_ImportArtifact_path: Property = Property(name="path", type=StringType)
DiagonosticModel_ImportArtifact.attributes={DiagonosticModel_ImportArtifact_path}

# DiagonosticModel_TracebilityArtifact class attributes and methods
DiagonosticModel_TracebilityArtifact_type: Property = Property(name="type", type=StringType)
DiagonosticModel_TracebilityArtifact_url: Property = Property(name="url", type=StringType)
DiagonosticModel_TracebilityArtifact.attributes={DiagonosticModel_TracebilityArtifact_type, DiagonosticModel_TracebilityArtifact_url}

# DiagonosticModel_TestStep class attributes and methods
DiagonosticModel_TestStep_title: Property = Property(name="title", type=StringType)
DiagonosticModel_TestStep.attributes={DiagonosticModel_TestStep_title}

# DiagonosticModel_SetAction class attributes and methods

# DiagonosticModel_SignalType class attributes and methods
DiagonosticModel_SignalType_name: Property = Property(name="name", type=StringType)
DiagonosticModel_SignalType_type: Property = Property(name="type", type=StringType)
DiagonosticModel_SignalType_MessageName: Property = Property(name="MessageName", type=StringType)
DiagonosticModel_SignalType_node: Property = Property(name="node", type=StringType)
DiagonosticModel_SignalType_namespace: Property = Property(name="namespace", type=StringType)
DiagonosticModel_SignalType_creationMode: Property = Property(name="creationMode", type=StringType)
DiagonosticModel_SignalType_lookupValues: Property = Property(name="lookupValues", type=StringType)
DiagonosticModel_SignalType.attributes={DiagonosticModel_SignalType_namespace, DiagonosticModel_SignalType_MessageName, DiagonosticModel_SignalType_node, DiagonosticModel_SignalType_type, DiagonosticModel_SignalType_creationMode, DiagonosticModel_SignalType_lookupValues, DiagonosticModel_SignalType_name}

# DiagonosticModel_WaitAction class attributes and methods

# Action class attributes and methods

# DiagonosticModel_CheckAction class attributes and methods
DiagonosticModel_CheckAction_operator: Property = Property(name="operator", type=StringType)
DiagonosticModel_CheckAction.attributes={DiagonosticModel_CheckAction_operator}

# DiagonosticModel_DiagnosticRequest class attributes and methods

# DiagonosticModel_DiagnosticResponse class attributes and methods
DiagonosticModel_DiagnosticResponse_primitive: Property = Property(name="primitive", type=StringType)
DiagonosticModel_DiagnosticResponse.attributes={DiagonosticModel_DiagnosticResponse_primitive}

# DiagonosticModel_CAPLParam class attributes and methods
DiagonosticModel_CAPLParam_name: Property = Property(name="name", type=StringType)
DiagonosticModel_CAPLParam_type: Property = Property(name="type", type=StringType)
DiagonosticModel_CAPLParam_value: Property = Property(name="value", type=StringType)
DiagonosticModel_CAPLParam.attributes={DiagonosticModel_CAPLParam_name, DiagonosticModel_CAPLParam_type, DiagonosticModel_CAPLParam_value}

# DiagonosticModel_DiagnosticService class attributes and methods
DiagonosticModel_DiagnosticService_result: Property = Property(name="result", type=StringType)
DiagonosticModel_DiagnosticService_ecu: Property = Property(name="ecu", type=StringType)
DiagonosticModel_DiagnosticService_service: Property = Property(name="service", type=StringType)
DiagonosticModel_DiagnosticService.attributes={DiagonosticModel_DiagnosticService_result, DiagonosticModel_DiagnosticService_service, DiagonosticModel_DiagnosticService_ecu}

# DiagonosticModel_CAPLTestStep class attributes and methods

# DiagonosticModel_DiagnosticParam class attributes and methods
DiagonosticModel_DiagnosticParam_copyToVar: Property = Property(name="copyToVar", type=StringType)
DiagonosticModel_DiagnosticParam_qualifier: Property = Property(name="qualifier", type=StringType)
DiagonosticModel_DiagnosticParam.attributes={DiagonosticModel_DiagnosticParam_copyToVar, DiagonosticModel_DiagnosticParam_qualifier}

# DiagonosticModel_DiagnosticParamValueType class attributes and methods

# DiagonosticModel_Action class attributes and methods
DiagonosticModel_Action_value: Property = Property(name="value", type=StringType)
DiagonosticModel_Action_wait: Property = Property(name="wait", type=FloatType)
DiagonosticModel_Action_valueTo: Property = Property(name="valueTo", type=StringType)
DiagonosticModel_Action.attributes={DiagonosticModel_Action_wait, DiagonosticModel_Action_value, DiagonosticModel_Action_valueTo}

# TestStep class attributes and methods

# DiagonosticModel_BlockAction class attributes and methods

# DiagonosticModel_ForLoop class attributes and methods
DiagonosticModel_ForLoop_loopVar: Property = Property(name="loopVar", type=StringType)
DiagonosticModel_ForLoop_stopValue: Property = Property(name="stopValue", type=IntegerType)
DiagonosticModel_ForLoop_startValue: Property = Property(name="startValue", type=IntegerType)
DiagonosticModel_ForLoop.attributes={DiagonosticModel_ForLoop_loopVar, DiagonosticModel_ForLoop_startValue, DiagonosticModel_ForLoop_stopValue}

# BlockAction class attributes and methods

# DiagonosticModel_Var class attributes and methods
DiagonosticModel_Var_name: Property = Property(name="name", type=StringType)
DiagonosticModel_Var.attributes={DiagonosticModel_Var_name}

# DiagnosticParamValueType class attributes and methods

# DiagonosticModel_OneOf class attributes and methods
DiagonosticModel_OneOf_values: Property = Property(name="values", type=StringType)
DiagonosticModel_OneOf.attributes={DiagonosticModel_OneOf_values}

# DiagonosticModel_Range class attributes and methods
DiagonosticModel_Range_from: Property = Property(name="from", type=IntegerType)
DiagonosticModel_Range_to: Property = Property(name="to", type=IntegerType)
DiagonosticModel_Range.attributes={DiagonosticModel_Range_to, DiagonosticModel_Range_from}

# DiagonosticModel_WhileLoop class attributes and methods
DiagonosticModel_WhileLoop_value: Property = Property(name="value", type=StringType)
DiagonosticModel_WhileLoop_valueTo: Property = Property(name="valueTo", type=StringType)
DiagonosticModel_WhileLoop_operator: Property = Property(name="operator", type=StringType)
DiagonosticModel_WhileLoop.attributes={DiagonosticModel_WhileLoop_value, DiagonosticModel_WhileLoop_operator, DiagonosticModel_WhileLoop_valueTo}

# Relationships
testGroups0: BinaryAssociation = BinaryAssociation(
    name="testGroups0",
    ends={
        Property(name="DiagonosticModel_TestGroup", type=DiagonosticModel_TestSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="DiagonosticModel_TestSpecification", type=DiagonosticModel_TestGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
testCases7: BinaryAssociation = BinaryAssociation(
    name="testCases7",
    ends={
        Property(name="DiagonosticModel_TestCase", type=DiagonosticModel_TestGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="DiagonosticModel_TestGroup8", type=DiagonosticModel_TestCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
externalreference9: BinaryAssociation = BinaryAssociation(
    name="externalreference9",
    ends={
        Property(name="DiagonosticModel_ExternalReference", type=DiagonosticModel_TestGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="DiagonosticModel_TestGroup10", type=DiagonosticModel_ExternalReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
testGroups12: BinaryAssociation = BinaryAssociation(
    name="testGroups12",
    ends={
        Property(name="DiagonosticModel_TestGroup13", type=DiagonosticModel_TestGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="DiagonosticModel_TestGroup11", type=DiagonosticModel_TestGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
capltestcases14: BinaryAssociation = BinaryAssociation(
    name="capltestcases14",
    ends={
        Property(name="DiagonosticModel_CAPLTestCase16", type=DiagonosticModel_TestGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="DiagonosticModel_TestGroup15", type=DiagonosticModel_CAPLTestCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
capltestcases1: BinaryAssociation = BinaryAssociation(
    name="capltestcases1",
    ends={
        Property(name="DiagonosticModel_CAPLTestCase", type=DiagonosticModel_TestSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="DiagonosticModel_TestSpecification2", type=DiagonosticModel_CAPLTestCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variants3: BinaryAssociation = BinaryAssociation(
    name="variants3",
    ends={
        Property(name="DiagonosticModel_Variant", type=DiagonosticModel_TestSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="DiagonosticModel_TestSpecification4", type=DiagonosticModel_Variant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importArtifacts5: BinaryAssociation = BinaryAssociation(
    name="importArtifacts5",
    ends={
        Property(name="DiagonosticModel_ImportArtifact", type=DiagonosticModel_TestSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="DiagonosticModel_TestSpecification6", type=DiagonosticModel_ImportArtifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postConditions25: BinaryAssociation = BinaryAssociation(
    name="postConditions25",
    ends={
        Property(name="DiagonosticModel_TestStep27", type=DiagonosticModel_TestCase, multiplicity=Multiplicity(1, 1)),
        Property(name="DiagonosticModel_TestCase26", type=DiagonosticModel_TestStep, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
externalreference28: BinaryAssociation = BinaryAssociation(
    name="externalreference28",
    ends={
        Property(name="DiagonosticModel_ExternalReference30", type=DiagonosticModel_TestCase, multiplicity=Multiplicity(1, 1)),
        Property(name="DiagonosticModel_TestCase29", type=DiagonosticModel_ExternalReference, multiplicity=Multiplicity(0, 1))
    }
)
traceabilityArtifacts31: BinaryAssociation = BinaryAssociation(
    name="traceabilityArtifacts31",
    ends={
        Property(name="DiagonosticModel_TracebilityArtifact", type=DiagonosticModel_TestCase, multiplicity=Multiplicity(1, 1)),
        Property(name="DiagonosticModel_TestCase32", type=DiagonosticModel_TracebilityArtifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nextStep34: BinaryAssociation = BinaryAssociation(
    name="nextStep34",
    ends={
        Property(name="DiagonosticModel_TestStep35", type=DiagonosticModel_TestStep, multiplicity=Multiplicity(1, 1)),
        Property(name="DiagonosticModel_TestStep33", type=DiagonosticModel_TestStep, multiplicity=Multiplicity(0, 1))
    }
)
testSteps17: BinaryAssociation = BinaryAssociation(
    name="testSteps17",
    ends={
        Property(name="DiagonosticModel_TestStep", type=DiagonosticModel_TestCase, multiplicity=Multiplicity(1, 1)),
        Property(name="DiagonosticModel_TestCase18", type=DiagonosticModel_TestStep, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variants19: BinaryAssociation = BinaryAssociation(
    name="variants19",
    ends={
        Property(name="DiagonosticModel_Variant21", type=DiagonosticModel_TestCase, multiplicity=Multiplicity(1, 1)),
        Property(name="DiagonosticModel_TestCase20", type=DiagonosticModel_Variant, multiplicity=Multiplicity(0, 9999))
    }
)
preConditions22: BinaryAssociation = BinaryAssociation(
    name="preConditions22",
    ends={
        Property(name="DiagonosticModel_TestStep24", type=DiagonosticModel_TestCase, multiplicity=Multiplicity(1, 1)),
        Property(name="DiagonosticModel_TestCase23", type=DiagonosticModel_TestStep, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key36: BinaryAssociation = BinaryAssociation(
    name="key36",
    ends={
        Property(name="DiagonosticModel_SignalType", type=DiagonosticModel_TestStep, multiplicity=Multiplicity(1, 1)),
        Property(name="DiagonosticModel_TestStep37", type=DiagonosticModel_SignalType, multiplicity=Multiplicity(0, 1))
    }
)
diagrequest38: BinaryAssociation = BinaryAssociation(
    name="diagrequest38",
    ends={
        Property(name="DiagonosticModel_DiagnosticRequest", type=DiagonosticModel_DiagnosticService, multiplicity=Multiplicity(1, 1)),
        Property(name="DiagonosticModel_DiagnosticService", type=DiagonosticModel_DiagnosticRequest, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
diagresponse39: BinaryAssociation = BinaryAssociation(
    name="diagresponse39",
    ends={
        Property(name="DiagonosticModel_DiagnosticResponse", type=DiagonosticModel_DiagnosticService, multiplicity=Multiplicity(1, 1)),
        Property(name="DiagonosticModel_DiagnosticService40", type=DiagonosticModel_DiagnosticResponse, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters41: BinaryAssociation = BinaryAssociation(
    name="parameters41",
    ends={
        Property(name="DiagonosticModel_CAPLParam", type=DiagonosticModel_CAPLTestCase, multiplicity=Multiplicity(1, 1)),
        Property(name="DiagonosticModel_CAPLTestCase42", type=DiagonosticModel_CAPLParam, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters43: BinaryAssociation = BinaryAssociation(
    name="parameters43",
    ends={
        Property(name="DiagonosticModel_CAPLParam44", type=DiagonosticModel_CAPLTestStep, multiplicity=Multiplicity(1, 1)),
        Property(name="DiagonosticModel_CAPLTestStep", type=DiagonosticModel_CAPLParam, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signalType45: BinaryAssociation = BinaryAssociation(
    name="signalType45",
    ends={
        Property(name="DiagonosticModel_SignalType47", type=DiagonosticModel_ImportArtifact, multiplicity=Multiplicity(1, 1)),
        Property(name="DiagonosticModel_ImportArtifact46", type=DiagonosticModel_SignalType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
diagparam48: BinaryAssociation = BinaryAssociation(
    name="diagparam48",
    ends={
        Property(name="DiagonosticModel_DiagnosticParam", type=DiagonosticModel_DiagnosticRequest, multiplicity=Multiplicity(1, 1)),
        Property(name="DiagonosticModel_DiagnosticRequest49", type=DiagonosticModel_DiagnosticParam, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
valueTypes53: BinaryAssociation = BinaryAssociation(
    name="valueTypes53",
    ends={
        Property(name="DiagonosticModel_DiagnosticParamValueType", type=DiagonosticModel_DiagnosticParam, multiplicity=Multiplicity(1, 1)),
        Property(name="DiagonosticModel_DiagnosticParam54", type=DiagonosticModel_DiagnosticParamValueType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
testSteps55: BinaryAssociation = BinaryAssociation(
    name="testSteps55",
    ends={
        Property(name="DiagonosticModel_TestStep56", type=DiagonosticModel_BlockAction, multiplicity=Multiplicity(1, 1)),
        Property(name="DiagonosticModel_BlockAction", type=DiagonosticModel_TestStep, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
diagparam50: BinaryAssociation = BinaryAssociation(
    name="diagparam50",
    ends={
        Property(name="DiagonosticModel_DiagnosticParam52", type=DiagonosticModel_DiagnosticResponse, multiplicity=Multiplicity(1, 1)),
        Property(name="DiagonosticModel_DiagnosticResponse51", type=DiagonosticModel_DiagnosticParam, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_DiagonosticModel_SetAction_Action = Generalization(general=Action, specific=DiagonosticModel_SetAction)
gen_DiagonosticModel_WaitAction_Action = Generalization(general=Action, specific=DiagonosticModel_WaitAction)
gen_DiagonosticModel_CheckAction_Action = Generalization(general=Action, specific=DiagonosticModel_CheckAction)
gen_DiagonosticModel_DiagnosticService_Action = Generalization(general=Action, specific=DiagonosticModel_DiagnosticService)
gen_DiagonosticModel_CAPLTestStep_Action = Generalization(general=Action, specific=DiagonosticModel_CAPLTestStep)
gen_DiagonosticModel_Action_TestStep = Generalization(general=TestStep, specific=DiagonosticModel_Action)
gen_DiagonosticModel_BlockAction_TestStep = Generalization(general=TestStep, specific=DiagonosticModel_BlockAction)
gen_DiagonosticModel_ForLoop_BlockAction = Generalization(general=BlockAction, specific=DiagonosticModel_ForLoop)
gen_DiagonosticModel_Var_DiagnosticParamValueType = Generalization(general=DiagnosticParamValueType, specific=DiagonosticModel_Var)
gen_DiagonosticModel_OneOf_DiagnosticParamValueType = Generalization(general=DiagnosticParamValueType, specific=DiagonosticModel_OneOf)
gen_DiagonosticModel_Range_DiagnosticParamValueType = Generalization(general=DiagnosticParamValueType, specific=DiagonosticModel_Range)
gen_DiagonosticModel_WhileLoop_BlockAction = Generalization(general=BlockAction, specific=DiagonosticModel_WhileLoop)

# Domain Model
domain_model = DomainModel(
    name="DiagonosticModel",
    types={DiagonosticModel_TestGroup, DiagonosticModel_TestSpecification, DiagonosticModel_TestCase, DiagonosticModel_ExternalReference, DiagonosticModel_CAPLTestCase, DiagonosticModel_Variant, DiagonosticModel_ImportArtifact, DiagonosticModel_TracebilityArtifact, DiagonosticModel_TestStep, DiagonosticModel_SetAction, DiagonosticModel_SignalType, DiagonosticModel_WaitAction, Action, DiagonosticModel_CheckAction, DiagonosticModel_DiagnosticRequest, DiagonosticModel_DiagnosticResponse, DiagonosticModel_CAPLParam, DiagonosticModel_DiagnosticService, DiagonosticModel_CAPLTestStep, DiagonosticModel_DiagnosticParam, DiagonosticModel_DiagnosticParamValueType, DiagonosticModel_Action, TestStep, DiagonosticModel_BlockAction, DiagonosticModel_ForLoop, BlockAction, DiagonosticModel_Var, DiagnosticParamValueType, DiagonosticModel_OneOf, DiagonosticModel_Range, DiagonosticModel_WhileLoop, OperatorTypeEnum, SignalTypeEnum, CreationModeEnum, ExecutionStatueTypeEnum, TraceabilityArtifactEnum},
    associations={testGroups0, testCases7, externalreference9, testGroups12, capltestcases14, capltestcases1, variants3, importArtifacts5, postConditions25, externalreference28, traceabilityArtifacts31, nextStep34, testSteps17, variants19, preConditions22, key36, diagrequest38, diagresponse39, parameters41, parameters43, signalType45, diagparam48, valueTypes53, testSteps55, diagparam50},
    generalizations={gen_DiagonosticModel_SetAction_Action, gen_DiagonosticModel_WaitAction_Action, gen_DiagonosticModel_CheckAction_Action, gen_DiagonosticModel_DiagnosticService_Action, gen_DiagonosticModel_CAPLTestStep_Action, gen_DiagonosticModel_Action_TestStep, gen_DiagonosticModel_BlockAction_TestStep, gen_DiagonosticModel_ForLoop_BlockAction, gen_DiagonosticModel_Var_DiagnosticParamValueType, gen_DiagonosticModel_OneOf_DiagnosticParamValueType, gen_DiagonosticModel_Range_DiagnosticParamValueType, gen_DiagonosticModel_WhileLoop_BlockAction},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)