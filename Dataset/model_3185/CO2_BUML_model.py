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
co2_CO2System = Class(name="co2::CO2System")
co2_PackageDeclaration = Class(name="co2::PackageDeclaration")
co2_HonestyDeclaration = Class(name="co2::HonestyDeclaration")
co2_ContractsAndProcessesDeclaration = Class(name="co2::ContractsAndProcessesDeclaration")
co2_Import = Class(name="co2::Import")
co2_ProcessDefinition = Class(name="co2::ProcessDefinition")
co2_Variable = Class(name="co2::Variable")
co2_ParallelProcesses = Class(name="co2::ParallelProcesses")
Process = Class(name="Process")
co2_DelimitedProcess = Class(name="co2::DelimitedProcess")
co2_Process = Class(name="co2::Process")
co2_ContractDefinition = Class(name="co2::ContractDefinition")
co2_EmptyProcess = Class(name="co2::EmptyProcess")
co2_Sum = Class(name="co2::Sum")
co2_Prefix = Class(name="co2::Prefix")
co2_IfThenElse = Class(name="co2::IfThenElse")
co2_Expression = Class(name="co2::Expression")
co2_ProcessCall = Class(name="co2::ProcessCall")
co2_Tell = Class(name="co2::Tell")
Prefix = Class(name="Prefix")
co2_VariableDeclaration = Class(name="co2::VariableDeclaration")
co2_Contract = Class(name="co2::Contract")
co2_Retract = Class(name="co2::Retract")
co2_DoOutput = Class(name="co2::DoOutput")
co2_IntAction = Class(name="co2::IntAction")
co2_ExtAction = Class(name="co2::ExtAction")
co2_Ask = Class(name="co2::Ask")
co2_Tau = Class(name="co2::Tau")
co2_TellAndReturn = Class(name="co2::TellAndReturn")
co2_Session = Class(name="co2::Session")
co2_DoInput = Class(name="co2::DoInput")
co2_TimeoutProcess = Class(name="co2::TimeoutProcess")
co2_SendGroup = Class(name="co2::SendGroup")
co2_Send = Class(name="co2::Send")
SendGroup = Class(name="SendGroup")
co2_TellAndWait = Class(name="co2::TellAndWait")
co2_ReceiveGroup = Class(name="co2::ReceiveGroup")
co2_Receive = Class(name="co2::Receive")
ReceiveGroup = Class(name="ReceiveGroup")
co2_Input = Class(name="co2::Input")
co2_Case = Class(name="co2::Case")
co2_NumberLiteral = Class(name="co2::NumberLiteral")
Expression = Class(name="Expression")
co2_StringLiteral = Class(name="co2::StringLiteral")
co2_SwitchCase = Class(name="co2::SwitchCase")
co2_Placeholder = Class(name="co2::Placeholder")
co2_Type = Class(name="co2::Type")
VariableDeclaration = Class(name="VariableDeclaration")
co2_BooleanLiteral = Class(name="co2::BooleanLiteral")
co2_IntSum = Class(name="co2::IntSum")
co2_ExtSum = Class(name="co2::ExtSum")
co2_Action = Class(name="co2::Action")
co2_ActionType = Class(name="co2::ActionType")
Action = Class(name="Action")
co2_RetractedProcess = Class(name="co2::RetractedProcess")
co2_EmptyContract = Class(name="co2::EmptyContract")
Contract = Class(name="Contract")
co2_OrExpression = Class(name="co2::OrExpression")
co2_AndExpression = Class(name="co2::AndExpression")
co2_Comparison = Class(name="co2::Comparison")
co2_Equals = Class(name="co2::Equals")
co2_Plus = Class(name="co2::Plus")
co2_Minus = Class(name="co2::Minus")
co2_MultiOrDiv = Class(name="co2::MultiOrDiv")
co2_ArithmeticSigned = Class(name="co2::ArithmeticSigned")
co2_VariableReference = Class(name="co2::VariableReference")
co2_IntPlaceholder = Class(name="co2::IntPlaceholder")
Placeholder = Class(name="Placeholder")
co2_BoolPlaceholder = Class(name="co2::BoolPlaceholder")
co2_StringPlaceholder = Class(name="co2::StringPlaceholder")
co2_IntType = Class(name="co2::IntType")
Type = Class(name="Type")
co2_StringType = Class(name="co2::StringType")
co2_BooleanType = Class(name="co2::BooleanType")
co2_SessionType = Class(name="co2::SessionType")
co2_ContractReference = Class(name="co2::ContractReference")
co2_BooleanNegation = Class(name="co2::BooleanNegation")
co2_StringActionType = Class(name="co2::StringActionType")
co2_UnitActionType = Class(name="co2::UnitActionType")
ActionType = Class(name="ActionType")
co2_IntActionType = Class(name="co2::IntActionType")

# co2_CO2System class attributes and methods

# co2_PackageDeclaration class attributes and methods
co2_PackageDeclaration_single: Property = Property(name="single", type=BooleanType)
co2_PackageDeclaration_name: Property = Property(name="name", type=StringType)
co2_PackageDeclaration.attributes={co2_PackageDeclaration_name, co2_PackageDeclaration_single}

# co2_HonestyDeclaration class attributes and methods

# co2_ContractsAndProcessesDeclaration class attributes and methods

# co2_Import class attributes and methods
co2_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
co2_Import.attributes={co2_Import_importedNamespace}

# co2_ProcessDefinition class attributes and methods
co2_ProcessDefinition_withoutRestrictions: Property = Property(name="withoutRestrictions", type=BooleanType)
co2_ProcessDefinition_name: Property = Property(name="name", type=StringType)
co2_ProcessDefinition.attributes={co2_ProcessDefinition_withoutRestrictions, co2_ProcessDefinition_name}

# co2_Variable class attributes and methods

# co2_ParallelProcesses class attributes and methods

# Process class attributes and methods

# co2_DelimitedProcess class attributes and methods

# co2_Process class attributes and methods

# co2_ContractDefinition class attributes and methods
co2_ContractDefinition_name: Property = Property(name="name", type=StringType)
co2_ContractDefinition.attributes={co2_ContractDefinition_name}

# co2_EmptyProcess class attributes and methods
co2_EmptyProcess_value: Property = Property(name="value", type=StringType)
co2_EmptyProcess.attributes={co2_EmptyProcess_value}

# co2_Sum class attributes and methods

# co2_Prefix class attributes and methods

# co2_IfThenElse class attributes and methods

# co2_Expression class attributes and methods

# co2_ProcessCall class attributes and methods

# co2_Tell class attributes and methods

# Prefix class attributes and methods

# co2_VariableDeclaration class attributes and methods
co2_VariableDeclaration_name: Property = Property(name="name", type=StringType)
co2_VariableDeclaration.attributes={co2_VariableDeclaration_name}

# co2_Contract class attributes and methods

# co2_Retract class attributes and methods

# co2_DoOutput class attributes and methods

# co2_IntAction class attributes and methods

# co2_ExtAction class attributes and methods

# co2_Ask class attributes and methods
co2_Ask_formula: Property = Property(name="formula", type=StringType)
co2_Ask.attributes={co2_Ask_formula}

# co2_Tau class attributes and methods

# co2_TellAndReturn class attributes and methods

# co2_Session class attributes and methods

# co2_DoInput class attributes and methods

# co2_TimeoutProcess class attributes and methods

# co2_SendGroup class attributes and methods

# co2_Send class attributes and methods

# SendGroup class attributes and methods

# co2_TellAndWait class attributes and methods
co2_TellAndWait_timeout: Property = Property(name="timeout", type=BooleanType)
co2_TellAndWait.attributes={co2_TellAndWait_timeout}

# co2_ReceiveGroup class attributes and methods

# co2_Receive class attributes and methods
co2_Receive_timeout: Property = Property(name="timeout", type=BooleanType)
co2_Receive.attributes={co2_Receive_timeout}

# ReceiveGroup class attributes and methods

# co2_Input class attributes and methods

# co2_Case class attributes and methods

# co2_NumberLiteral class attributes and methods
co2_NumberLiteral_value: Property = Property(name="value", type=IntegerType)
co2_NumberLiteral.attributes={co2_NumberLiteral_value}

# Expression class attributes and methods

# co2_StringLiteral class attributes and methods
co2_StringLiteral_value: Property = Property(name="value", type=StringType)
co2_StringLiteral.attributes={co2_StringLiteral_value}

# co2_SwitchCase class attributes and methods
co2_SwitchCase_default: Property = Property(name="default", type=BooleanType)
co2_SwitchCase.attributes={co2_SwitchCase_default}

# co2_Placeholder class attributes and methods

# co2_Type class attributes and methods
co2_Type_value: Property = Property(name="value", type=StringType)
co2_Type.attributes={co2_Type_value}

# VariableDeclaration class attributes and methods

# co2_BooleanLiteral class attributes and methods
co2_BooleanLiteral_value: Property = Property(name="value", type=StringType)
co2_BooleanLiteral.attributes={co2_BooleanLiteral_value}

# co2_IntSum class attributes and methods

# co2_ExtSum class attributes and methods

# co2_Action class attributes and methods
co2_Action_name: Property = Property(name="name", type=StringType)
co2_Action.attributes={co2_Action_name}

# co2_ActionType class attributes and methods
co2_ActionType_value: Property = Property(name="value", type=StringType)
co2_ActionType.attributes={co2_ActionType_value}

# Action class attributes and methods

# co2_RetractedProcess class attributes and methods

# co2_EmptyContract class attributes and methods
co2_EmptyContract_value: Property = Property(name="value", type=StringType)
co2_EmptyContract.attributes={co2_EmptyContract_value}

# Contract class attributes and methods

# co2_OrExpression class attributes and methods

# co2_AndExpression class attributes and methods

# co2_Comparison class attributes and methods
co2_Comparison_op: Property = Property(name="op", type=StringType)
co2_Comparison.attributes={co2_Comparison_op}

# co2_Equals class attributes and methods
co2_Equals_op: Property = Property(name="op", type=StringType)
co2_Equals.attributes={co2_Equals_op}

# co2_Plus class attributes and methods

# co2_Minus class attributes and methods

# co2_MultiOrDiv class attributes and methods
co2_MultiOrDiv_op: Property = Property(name="op", type=StringType)
co2_MultiOrDiv.attributes={co2_MultiOrDiv_op}

# co2_ArithmeticSigned class attributes and methods

# co2_VariableReference class attributes and methods

# co2_IntPlaceholder class attributes and methods

# Placeholder class attributes and methods

# co2_BoolPlaceholder class attributes and methods

# co2_StringPlaceholder class attributes and methods

# co2_IntType class attributes and methods

# Type class attributes and methods

# co2_StringType class attributes and methods

# co2_BooleanType class attributes and methods

# co2_SessionType class attributes and methods

# co2_ContractReference class attributes and methods

# co2_BooleanNegation class attributes and methods

# co2_StringActionType class attributes and methods

# co2_UnitActionType class attributes and methods

# ActionType class attributes and methods

# co2_IntActionType class attributes and methods

# Relationships
package0: BinaryAssociation = BinaryAssociation(
    name="package0",
    ends={
        Property(name="co2_PackageDeclaration", type=co2_CO2System, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_CO2System", type=co2_PackageDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
honesty1: BinaryAssociation = BinaryAssociation(
    name="honesty1",
    ends={
        Property(name="co2_HonestyDeclaration", type=co2_CO2System, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_CO2System2", type=co2_HonestyDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contractsAndProcessesDeclaration3: BinaryAssociation = BinaryAssociation(
    name="contractsAndProcessesDeclaration3",
    ends={
        Property(name="co2_ContractsAndProcessesDeclaration", type=co2_CO2System, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_CO2System4", type=co2_ContractsAndProcessesDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
processes5: BinaryAssociation = BinaryAssociation(
    name="processes5",
    ends={
        Property(name="co2_ProcessDefinition", type=co2_HonestyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_HonestyDeclaration6", type=co2_ProcessDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
processes9: BinaryAssociation = BinaryAssociation(
    name="processes9",
    ends={
        Property(name="co2_ProcessDefinition11", type=co2_ContractsAndProcessesDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_ContractsAndProcessesDeclaration10", type=co2_ProcessDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
params12: BinaryAssociation = BinaryAssociation(
    name="params12",
    ends={
        Property(name="co2_Variable", type=co2_ProcessDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_ProcessDefinition13", type=co2_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
process14: BinaryAssociation = BinaryAssociation(
    name="process14",
    ends={
        Property(name="co2_ParallelProcesses", type=co2_ProcessDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_ProcessDefinition15", type=co2_ParallelProcesses, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
processes16: BinaryAssociation = BinaryAssociation(
    name="processes16",
    ends={
        Property(name="co2_DelimitedProcess", type=co2_ParallelProcesses, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_ParallelProcesses17", type=co2_DelimitedProcess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
freeNames18: BinaryAssociation = BinaryAssociation(
    name="freeNames18",
    ends={
        Property(name="co2_Variable20", type=co2_DelimitedProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_DelimitedProcess19", type=co2_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
process21: BinaryAssociation = BinaryAssociation(
    name="process21",
    ends={
        Property(name="co2_Process", type=co2_DelimitedProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_DelimitedProcess22", type=co2_Process, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contracts7: BinaryAssociation = BinaryAssociation(
    name="contracts7",
    ends={
        Property(name="co2_ContractDefinition", type=co2_ContractsAndProcessesDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_ContractsAndProcessesDeclaration8", type=co2_ContractDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
prefixes23: BinaryAssociation = BinaryAssociation(
    name="prefixes23",
    ends={
        Property(name="co2_Prefix", type=co2_Sum, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_Sum", type=co2_Prefix, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
if24: BinaryAssociation = BinaryAssociation(
    name="if24",
    ends={
        Property(name="co2_Expression", type=co2_IfThenElse, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_IfThenElse", type=co2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then25: BinaryAssociation = BinaryAssociation(
    name="then25",
    ends={
        Property(name="co2_Process27", type=co2_IfThenElse, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_IfThenElse26", type=co2_Process, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
else28: BinaryAssociation = BinaryAssociation(
    name="else28",
    ends={
        Property(name="co2_Process30", type=co2_IfThenElse, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_IfThenElse29", type=co2_Process, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reference31: BinaryAssociation = BinaryAssociation(
    name="reference31",
    ends={
        Property(name="co2_ProcessDefinition32", type=co2_ProcessCall, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_ProcessCall", type=co2_ProcessDefinition, multiplicity=Multiplicity(0, 1))
    }
)
session39: BinaryAssociation = BinaryAssociation(
    name="session39",
    ends={
        Property(name="co2_VariableDeclaration", type=co2_Tell, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_Tell", type=co2_VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
contract40: BinaryAssociation = BinaryAssociation(
    name="contract40",
    ends={
        Property(name="co2_Contract", type=co2_Tell, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_Tell41", type=co2_Contract, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contractReference42: BinaryAssociation = BinaryAssociation(
    name="contractReference42",
    ends={
        Property(name="co2_ContractDefinition44", type=co2_Tell, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_Tell43", type=co2_ContractDefinition, multiplicity=Multiplicity(0, 1))
    }
)
session45: BinaryAssociation = BinaryAssociation(
    name="session45",
    ends={
        Property(name="co2_VariableDeclaration46", type=co2_Retract, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_Retract", type=co2_VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
session47: BinaryAssociation = BinaryAssociation(
    name="session47",
    ends={
        Property(name="co2_VariableDeclaration48", type=co2_DoOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_DoOutput", type=co2_VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
actionName49: BinaryAssociation = BinaryAssociation(
    name="actionName49",
    ends={
        Property(name="co2_IntAction", type=co2_DoOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_DoOutput50", type=co2_IntAction, multiplicity=Multiplicity(0, 1))
    }
)
params33: BinaryAssociation = BinaryAssociation(
    name="params33",
    ends={
        Property(name="co2_Expression35", type=co2_ProcessCall, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_ProcessCall34", type=co2_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value51: BinaryAssociation = BinaryAssociation(
    name="value51",
    ends={
        Property(name="co2_Expression53", type=co2_DoOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_DoOutput52", type=co2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
next36: BinaryAssociation = BinaryAssociation(
    name="next36",
    ends={
        Property(name="co2_Process38", type=co2_Prefix, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_Prefix37", type=co2_Process, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
session54: BinaryAssociation = BinaryAssociation(
    name="session54",
    ends={
        Property(name="co2_VariableDeclaration55", type=co2_DoInput, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_DoInput", type=co2_VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
actionName56: BinaryAssociation = BinaryAssociation(
    name="actionName56",
    ends={
        Property(name="co2_ExtAction", type=co2_DoInput, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_DoInput57", type=co2_ExtAction, multiplicity=Multiplicity(0, 1))
    }
)
variable58: BinaryAssociation = BinaryAssociation(
    name="variable58",
    ends={
        Property(name="co2_Variable60", type=co2_DoInput, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_DoInput59", type=co2_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
session61: BinaryAssociation = BinaryAssociation(
    name="session61",
    ends={
        Property(name="co2_VariableDeclaration62", type=co2_Ask, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_Ask", type=co2_VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
session63: BinaryAssociation = BinaryAssociation(
    name="session63",
    ends={
        Property(name="co2_Session", type=co2_TellAndReturn, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_TellAndReturn", type=co2_Session, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
process64: BinaryAssociation = BinaryAssociation(
    name="process64",
    ends={
        Property(name="co2_Process66", type=co2_TellAndReturn, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_TellAndReturn65", type=co2_Process, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
session67: BinaryAssociation = BinaryAssociation(
    name="session67",
    ends={
        Property(name="co2_Session68", type=co2_TellAndWait, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_TellAndWait", type=co2_Session, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
process69: BinaryAssociation = BinaryAssociation(
    name="process69",
    ends={
        Property(name="co2_Process71", type=co2_TellAndWait, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_TellAndWait70", type=co2_Process, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timeoutValue72: BinaryAssociation = BinaryAssociation(
    name="timeoutValue72",
    ends={
        Property(name="co2_TimeoutProcess", type=co2_TellAndWait, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_TellAndWait73", type=co2_TimeoutProcess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value74: BinaryAssociation = BinaryAssociation(
    name="value74",
    ends={
        Property(name="co2_Expression76", type=co2_TimeoutProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_TimeoutProcess75", type=co2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tProcess77: BinaryAssociation = BinaryAssociation(
    name="tProcess77",
    ends={
        Property(name="co2_Process79", type=co2_TimeoutProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_TimeoutProcess78", type=co2_Process, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
next80: BinaryAssociation = BinaryAssociation(
    name="next80",
    ends={
        Property(name="co2_Process81", type=co2_Send, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_Send", type=co2_Process, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action82: BinaryAssociation = BinaryAssociation(
    name="action82",
    ends={
        Property(name="co2_IntAction84", type=co2_Send, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_Send83", type=co2_IntAction, multiplicity=Multiplicity(0, 1))
    }
)
value85: BinaryAssociation = BinaryAssociation(
    name="value85",
    ends={
        Property(name="co2_Send86", type=co2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="co2_Expression87", type=co2_Send, multiplicity=Multiplicity(1, 1))
    }
)
session88: BinaryAssociation = BinaryAssociation(
    name="session88",
    ends={
        Property(name="co2_VariableDeclaration90", type=co2_Send, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_Send89", type=co2_VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
inputs91: BinaryAssociation = BinaryAssociation(
    name="inputs91",
    ends={
        Property(name="co2_Input", type=co2_Receive, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_Receive", type=co2_Input, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timeoutValue92: BinaryAssociation = BinaryAssociation(
    name="timeoutValue92",
    ends={
        Property(name="co2_TimeoutProcess94", type=co2_Receive, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_Receive93", type=co2_TimeoutProcess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
next95: BinaryAssociation = BinaryAssociation(
    name="next95",
    ends={
        Property(name="co2_Process97", type=co2_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_Input96", type=co2_Process, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actions98: BinaryAssociation = BinaryAssociation(
    name="actions98",
    ends={
        Property(name="co2_ExtAction100", type=co2_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_Input99", type=co2_ExtAction, multiplicity=Multiplicity(0, 9999))
    }
)
variable101: BinaryAssociation = BinaryAssociation(
    name="variable101",
    ends={
        Property(name="co2_Variable103", type=co2_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_Input102", type=co2_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
session104: BinaryAssociation = BinaryAssociation(
    name="session104",
    ends={
        Property(name="co2_VariableDeclaration106", type=co2_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_Input105", type=co2_VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
exp107: BinaryAssociation = BinaryAssociation(
    name="exp107",
    ends={
        Property(name="co2_Expression108", type=co2_SwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_SwitchCase", type=co2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cases109: BinaryAssociation = BinaryAssociation(
    name="cases109",
    ends={
        Property(name="co2_Case", type=co2_SwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_SwitchCase110", type=co2_Case, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultProc111: BinaryAssociation = BinaryAssociation(
    name="defaultProc111",
    ends={
        Property(name="co2_Process113", type=co2_SwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_SwitchCase112", type=co2_Process, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
match114: BinaryAssociation = BinaryAssociation(
    name="match114",
    ends={
        Property(name="co2_Expression116", type=co2_Case, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_Case115", type=co2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
caseProc117: BinaryAssociation = BinaryAssociation(
    name="caseProc117",
    ends={
        Property(name="co2_Process119", type=co2_Case, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_Case118", type=co2_Process, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type120: BinaryAssociation = BinaryAssociation(
    name="type120",
    ends={
        Property(name="co2_Type", type=co2_Placeholder, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_Placeholder", type=co2_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type121: BinaryAssociation = BinaryAssociation(
    name="type121",
    ends={
        Property(name="co2_Type123", type=co2_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_Variable122", type=co2_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contract124: BinaryAssociation = BinaryAssociation(
    name="contract124",
    ends={
        Property(name="co2_Contract126", type=co2_Session, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_Session125", type=co2_Contract, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contractReference127: BinaryAssociation = BinaryAssociation(
    name="contractReference127",
    ends={
        Property(name="co2_ContractDefinition129", type=co2_Session, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_Session128", type=co2_ContractDefinition, multiplicity=Multiplicity(0, 1))
    }
)
contract130: BinaryAssociation = BinaryAssociation(
    name="contract130",
    ends={
        Property(name="co2_Contract132", type=co2_ContractDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_ContractDefinition131", type=co2_Contract, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actions133: BinaryAssociation = BinaryAssociation(
    name="actions133",
    ends={
        Property(name="co2_IntAction134", type=co2_IntSum, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_IntSum", type=co2_IntAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actions135: BinaryAssociation = BinaryAssociation(
    name="actions135",
    ends={
        Property(name="co2_ExtAction136", type=co2_ExtSum, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_ExtSum", type=co2_ExtAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type137: BinaryAssociation = BinaryAssociation(
    name="type137",
    ends={
        Property(name="co2_ActionType", type=co2_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_Action", type=co2_ActionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
next138: BinaryAssociation = BinaryAssociation(
    name="next138",
    ends={
        Property(name="co2_Contract140", type=co2_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_Action139", type=co2_Contract, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left143: BinaryAssociation = BinaryAssociation(
    name="left143",
    ends={
        Property(name="co2_Expression144", type=co2_OrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_OrExpression", type=co2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right145: BinaryAssociation = BinaryAssociation(
    name="right145",
    ends={
        Property(name="co2_Expression147", type=co2_OrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_OrExpression146", type=co2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left148: BinaryAssociation = BinaryAssociation(
    name="left148",
    ends={
        Property(name="co2_Expression149", type=co2_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_AndExpression", type=co2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right150: BinaryAssociation = BinaryAssociation(
    name="right150",
    ends={
        Property(name="co2_Expression152", type=co2_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_AndExpression151", type=co2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left153: BinaryAssociation = BinaryAssociation(
    name="left153",
    ends={
        Property(name="co2_Expression154", type=co2_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_Comparison", type=co2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right155: BinaryAssociation = BinaryAssociation(
    name="right155",
    ends={
        Property(name="co2_Expression157", type=co2_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_Comparison156", type=co2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
process141: BinaryAssociation = BinaryAssociation(
    name="process141",
    ends={
        Property(name="co2_Process142", type=co2_RetractedProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_RetractedProcess", type=co2_Process, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right160: BinaryAssociation = BinaryAssociation(
    name="right160",
    ends={
        Property(name="co2_Expression162", type=co2_Equals, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_Equals161", type=co2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left163: BinaryAssociation = BinaryAssociation(
    name="left163",
    ends={
        Property(name="co2_Expression164", type=co2_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_Plus", type=co2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right165: BinaryAssociation = BinaryAssociation(
    name="right165",
    ends={
        Property(name="co2_Expression167", type=co2_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_Plus166", type=co2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left168: BinaryAssociation = BinaryAssociation(
    name="left168",
    ends={
        Property(name="co2_Expression169", type=co2_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_Minus", type=co2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right170: BinaryAssociation = BinaryAssociation(
    name="right170",
    ends={
        Property(name="co2_Expression172", type=co2_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_Minus171", type=co2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left173: BinaryAssociation = BinaryAssociation(
    name="left173",
    ends={
        Property(name="co2_Expression174", type=co2_MultiOrDiv, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_MultiOrDiv", type=co2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right175: BinaryAssociation = BinaryAssociation(
    name="right175",
    ends={
        Property(name="co2_Expression177", type=co2_MultiOrDiv, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_MultiOrDiv176", type=co2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left158: BinaryAssociation = BinaryAssociation(
    name="left158",
    ends={
        Property(name="co2_Expression159", type=co2_Equals, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_Equals", type=co2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression178: BinaryAssociation = BinaryAssociation(
    name="expression178",
    ends={
        Property(name="co2_BooleanNegation", type=co2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="co2_Expression179", type=co2_BooleanNegation, multiplicity=Multiplicity(1, 1))
    }
)
expression180: BinaryAssociation = BinaryAssociation(
    name="expression180",
    ends={
        Property(name="co2_Expression181", type=co2_ArithmeticSigned, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_ArithmeticSigned", type=co2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref182: BinaryAssociation = BinaryAssociation(
    name="ref182",
    ends={
        Property(name="co2_VariableDeclaration183", type=co2_VariableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_VariableReference", type=co2_VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
ref184: BinaryAssociation = BinaryAssociation(
    name="ref184",
    ends={
        Property(name="co2_ContractDefinition185", type=co2_ContractReference, multiplicity=Multiplicity(1, 1)),
        Property(name="co2_ContractReference", type=co2_ContractDefinition, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_co2_ParallelProcesses_Process = Generalization(general=Process, specific=co2_ParallelProcesses)
gen_co2_EmptyProcess_Process = Generalization(general=Process, specific=co2_EmptyProcess)
gen_co2_Sum_Process = Generalization(general=Process, specific=co2_Sum)
gen_co2_IfThenElse_Process = Generalization(general=Process, specific=co2_IfThenElse)
gen_co2_ProcessCall_Process = Generalization(general=Process, specific=co2_ProcessCall)
gen_co2_Tell_Prefix = Generalization(general=Prefix, specific=co2_Tell)
gen_co2_Retract_Prefix = Generalization(general=Prefix, specific=co2_Retract)
gen_co2_DoOutput_Prefix = Generalization(general=Prefix, specific=co2_DoOutput)
gen_co2_Ask_Prefix = Generalization(general=Prefix, specific=co2_Ask)
gen_co2_Tau_Prefix = Generalization(general=Prefix, specific=co2_Tau)
gen_co2_TellAndReturn_Process = Generalization(general=Process, specific=co2_TellAndReturn)
gen_co2_DoInput_Prefix = Generalization(general=Prefix, specific=co2_DoInput)
gen_co2_SendGroup_Process = Generalization(general=Process, specific=co2_SendGroup)
gen_co2_Send_SendGroup = Generalization(general=SendGroup, specific=co2_Send)
gen_co2_TellAndWait_Process = Generalization(general=Process, specific=co2_TellAndWait)
gen_co2_ReceiveGroup_Process = Generalization(general=Process, specific=co2_ReceiveGroup)
gen_co2_Receive_ReceiveGroup = Generalization(general=ReceiveGroup, specific=co2_Receive)
gen_co2_NumberLiteral_Expression = Generalization(general=Expression, specific=co2_NumberLiteral)
gen_co2_StringLiteral_Expression = Generalization(general=Expression, specific=co2_StringLiteral)
gen_co2_SwitchCase_Process = Generalization(general=Process, specific=co2_SwitchCase)
gen_co2_Placeholder_Expression = Generalization(general=Expression, specific=co2_Placeholder)
gen_co2_Variable_VariableDeclaration = Generalization(general=VariableDeclaration, specific=co2_Variable)
gen_co2_Session_VariableDeclaration = Generalization(general=VariableDeclaration, specific=co2_Session)
gen_co2_BooleanLiteral_Expression = Generalization(general=Expression, specific=co2_BooleanLiteral)
gen_co2_EmptyContract_Contract = Generalization(general=Contract, specific=co2_EmptyContract)
gen_co2_IntSum_Contract = Generalization(general=Contract, specific=co2_IntSum)
gen_co2_ExtSum_Contract = Generalization(general=Contract, specific=co2_ExtSum)
gen_co2_IntAction_Action = Generalization(general=Action, specific=co2_IntAction)
gen_co2_ExtAction_Action = Generalization(general=Action, specific=co2_ExtAction)
gen_co2_RetractedProcess_Process = Generalization(general=Process, specific=co2_RetractedProcess)
gen_co2_OrExpression_Expression = Generalization(general=Expression, specific=co2_OrExpression)
gen_co2_AndExpression_Expression = Generalization(general=Expression, specific=co2_AndExpression)
gen_co2_Comparison_Expression = Generalization(general=Expression, specific=co2_Comparison)
gen_co2_Equals_Expression = Generalization(general=Expression, specific=co2_Equals)
gen_co2_Plus_Expression = Generalization(general=Expression, specific=co2_Plus)
gen_co2_Minus_Expression = Generalization(general=Expression, specific=co2_Minus)
gen_co2_MultiOrDiv_Expression = Generalization(general=Expression, specific=co2_MultiOrDiv)
gen_co2_ArithmeticSigned_Expression = Generalization(general=Expression, specific=co2_ArithmeticSigned)
gen_co2_VariableReference_Expression = Generalization(general=Expression, specific=co2_VariableReference)
gen_co2_IntPlaceholder_Placeholder = Generalization(general=Placeholder, specific=co2_IntPlaceholder)
gen_co2_BoolPlaceholder_Placeholder = Generalization(general=Placeholder, specific=co2_BoolPlaceholder)
gen_co2_StringPlaceholder_Placeholder = Generalization(general=Placeholder, specific=co2_StringPlaceholder)
gen_co2_IntType_Type = Generalization(general=Type, specific=co2_IntType)
gen_co2_StringType_Type = Generalization(general=Type, specific=co2_StringType)
gen_co2_BooleanType_Type = Generalization(general=Type, specific=co2_BooleanType)
gen_co2_SessionType_Type = Generalization(general=Type, specific=co2_SessionType)
gen_co2_ContractReference_Contract = Generalization(general=Contract, specific=co2_ContractReference)
gen_co2_BooleanNegation_Expression = Generalization(general=Expression, specific=co2_BooleanNegation)
gen_co2_StringActionType_ActionType = Generalization(general=ActionType, specific=co2_StringActionType)
gen_co2_UnitActionType_ActionType = Generalization(general=ActionType, specific=co2_UnitActionType)
gen_co2_IntActionType_ActionType = Generalization(general=ActionType, specific=co2_IntActionType)

# Domain Model
domain_model = DomainModel(
    name="co2",
    types={co2_CO2System, co2_PackageDeclaration, co2_HonestyDeclaration, co2_ContractsAndProcessesDeclaration, co2_Import, co2_ProcessDefinition, co2_Variable, co2_ParallelProcesses, Process, co2_DelimitedProcess, co2_Process, co2_ContractDefinition, co2_EmptyProcess, co2_Sum, co2_Prefix, co2_IfThenElse, co2_Expression, co2_ProcessCall, co2_Tell, Prefix, co2_VariableDeclaration, co2_Contract, co2_Retract, co2_DoOutput, co2_IntAction, co2_ExtAction, co2_Ask, co2_Tau, co2_TellAndReturn, co2_Session, co2_DoInput, co2_TimeoutProcess, co2_SendGroup, co2_Send, SendGroup, co2_TellAndWait, co2_ReceiveGroup, co2_Receive, ReceiveGroup, co2_Input, co2_Case, co2_NumberLiteral, Expression, co2_StringLiteral, co2_SwitchCase, co2_Placeholder, co2_Type, VariableDeclaration, co2_BooleanLiteral, co2_IntSum, co2_ExtSum, co2_Action, co2_ActionType, Action, co2_RetractedProcess, co2_EmptyContract, Contract, co2_OrExpression, co2_AndExpression, co2_Comparison, co2_Equals, co2_Plus, co2_Minus, co2_MultiOrDiv, co2_ArithmeticSigned, co2_VariableReference, co2_IntPlaceholder, Placeholder, co2_BoolPlaceholder, co2_StringPlaceholder, co2_IntType, Type, co2_StringType, co2_BooleanType, co2_SessionType, co2_ContractReference, co2_BooleanNegation, co2_StringActionType, co2_UnitActionType, ActionType, co2_IntActionType},
    associations={package0, honesty1, contractsAndProcessesDeclaration3, processes5, processes9, params12, process14, processes16, freeNames18, process21, contracts7, prefixes23, if24, then25, else28, reference31, session39, contract40, contractReference42, session45, session47, actionName49, params33, value51, next36, session54, actionName56, variable58, session61, session63, process64, session67, process69, timeoutValue72, value74, tProcess77, next80, action82, value85, session88, inputs91, timeoutValue92, next95, actions98, variable101, session104, exp107, cases109, defaultProc111, match114, caseProc117, type120, type121, contract124, contractReference127, contract130, actions133, actions135, type137, next138, left143, right145, left148, right150, left153, right155, process141, right160, left163, right165, left168, right170, left173, right175, left158, expression178, expression180, ref182, ref184},
    generalizations={gen_co2_ParallelProcesses_Process, gen_co2_EmptyProcess_Process, gen_co2_Sum_Process, gen_co2_IfThenElse_Process, gen_co2_ProcessCall_Process, gen_co2_Tell_Prefix, gen_co2_Retract_Prefix, gen_co2_DoOutput_Prefix, gen_co2_Ask_Prefix, gen_co2_Tau_Prefix, gen_co2_TellAndReturn_Process, gen_co2_DoInput_Prefix, gen_co2_SendGroup_Process, gen_co2_Send_SendGroup, gen_co2_TellAndWait_Process, gen_co2_ReceiveGroup_Process, gen_co2_Receive_ReceiveGroup, gen_co2_NumberLiteral_Expression, gen_co2_StringLiteral_Expression, gen_co2_SwitchCase_Process, gen_co2_Placeholder_Expression, gen_co2_Variable_VariableDeclaration, gen_co2_Session_VariableDeclaration, gen_co2_BooleanLiteral_Expression, gen_co2_EmptyContract_Contract, gen_co2_IntSum_Contract, gen_co2_ExtSum_Contract, gen_co2_IntAction_Action, gen_co2_ExtAction_Action, gen_co2_RetractedProcess_Process, gen_co2_OrExpression_Expression, gen_co2_AndExpression_Expression, gen_co2_Comparison_Expression, gen_co2_Equals_Expression, gen_co2_Plus_Expression, gen_co2_Minus_Expression, gen_co2_MultiOrDiv_Expression, gen_co2_ArithmeticSigned_Expression, gen_co2_VariableReference_Expression, gen_co2_IntPlaceholder_Placeholder, gen_co2_BoolPlaceholder_Placeholder, gen_co2_StringPlaceholder_Placeholder, gen_co2_IntType_Type, gen_co2_StringType_Type, gen_co2_BooleanType_Type, gen_co2_SessionType_Type, gen_co2_ContractReference_Contract, gen_co2_BooleanNegation_Expression, gen_co2_StringActionType_ActionType, gen_co2_UnitActionType_ActionType, gen_co2_IntActionType_ActionType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)