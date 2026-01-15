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
DynamicValueType: Enumeration = Enumeration(
    name="DynamicValueType",
    literals={
            EnumerationLiteral(name="LiteralText"),
			EnumerationLiteral(name="ScriptText"),
			EnumerationLiteral(name="VariableName"),
			EnumerationLiteral(name="Custom")
    }
)

OutputType: Enumeration = Enumeration(
    name="OutputType",
    literals={
            EnumerationLiteral(name="Default"),
			EnumerationLiteral(name="Error"),
			EnumerationLiteral(name="Choice")
    }
)

DebugLevel: Enumeration = Enumeration(
    name="DebugLevel",
    literals={
            EnumerationLiteral(name="Warn"),
			EnumerationLiteral(name="Error"),
			EnumerationLiteral(name="Info"),
			EnumerationLiteral(name="Debug")
    }
)

InputType: Enumeration = Enumeration(
    name="InputType",
    literals={
            EnumerationLiteral(name="Value"),
			EnumerationLiteral(name="Variable")
    }
)

# Classes
core_actionstep_ActionStep = Class(name="core::actionstep::ActionStep", is_abstract=True)
ProductIdentifiable = Class(name="ProductIdentifiable")
ThreadSensitive = Class(name="ThreadSensitive")
PlatformDisposition = Class(name="PlatformDisposition")
core_ProductIdentifiable = Class(name="core::ProductIdentifiable", is_abstract=True)
core_ThreadSensitive = Class(name="core::ThreadSensitive")
core_PlatformDisposition = Class(name="core::PlatformDisposition", is_abstract=True)
Output = Class(name="Output")
Saflet = Class(name="Saflet")
core_actionstep_Assignment = Class(name="core::actionstep::Assignment")
ActionStep = Class(name="ActionStep")
DynamicValue = Class(name="DynamicValue")
core_actionstep_CaseItem = Class(name="core::actionstep::CaseItem")
Item = Class(name="Item")
core_actionstep_InputItem = Class(name="core::actionstep::InputItem")
CaseItem = Class(name="CaseItem")
core_actionstep_ParameterizedActionstep = Class(name="core::actionstep::ParameterizedActionstep", is_abstract=True)
InputItem = Class(name="InputItem")
OutputParameter = Class(name="OutputParameter")
core_actionstep_ParameterizedInitiator = Class(name="core::actionstep::ParameterizedInitiator", is_abstract=True)
initiator_Initiator = Class(name="initiator::Initiator")
actionstep_ParameterizedActionstep = Class(name="actionstep::ParameterizedActionstep")
core_actionstep_Choice = Class(name="core::actionstep::Choice")
core_actionstep_Output = Class(name="core::actionstep::Output")
core_actionstep_DynamicValue = Class(name="core::actionstep::DynamicValue")
actionstep_core_EObject = Class(name="actionstep::core::EObject")
actionstep_core_EStringToStringMapEntry = Class(name="actionstep::core::EStringToStringMapEntry")
core_actionstep_IfThen = Class(name="core::actionstep::IfThen")
core_actionstep_ExecuteScript = Class(name="core::actionstep::ExecuteScript")
core_actionstep_InvokeSaflet = Class(name="core::actionstep::InvokeSaflet")
core_actionstep_OpenDBConnection = Class(name="core::actionstep::OpenDBConnection")
actionstep_ActionStep = Class(name="actionstep::ActionStep")
core_actionstep_DebugLog = Class(name="core::actionstep::DebugLog")
actionstep_Heavyweight = Class(name="actionstep::Heavyweight")
DBConnectionId = Class(name="DBConnectionId")
core_actionstep_CloseDBConnection = Class(name="core::actionstep::CloseDBConnection")
core_actionstep_OpenQuery = Class(name="core::actionstep::OpenQuery")
DBQueryId = Class(name="DBQueryId")
core_actionstep_SetQueryParam = Class(name="core::actionstep::SetQueryParam")
DBQueryParamId = Class(name="DBQueryParamId")
core_actionstep_ExecuteUpdate = Class(name="core::actionstep::ExecuteUpdate")
core_actionstep_ExecuteQuery = Class(name="core::actionstep::ExecuteQuery")
DBResultSetId = Class(name="DBResultSetId")
core_actionstep_NextRow = Class(name="core::actionstep::NextRow")
core_actionstep_GetColValue = Class(name="core::actionstep::GetColValue")
core_actionstep_GetColValues = Class(name="core::actionstep::GetColValues")
GetColMapping = Class(name="GetColMapping")
core_actionstep_SetColValue = Class(name="core::actionstep::SetColValue")
core_actionstep_MoveToRow = Class(name="core::actionstep::MoveToRow")
core_actionstep_SetColValues = Class(name="core::actionstep::SetColValues")
SetColMapping = Class(name="SetColMapping")
core_actionstep_UpdatetRow = Class(name="core::actionstep::UpdatetRow")
core_actionstep_DeleteRow = Class(name="core::actionstep::DeleteRow")
core_actionstep_MoveToLastRow = Class(name="core::actionstep::MoveToLastRow")
core_actionstep_PreviousRow = Class(name="core::actionstep::PreviousRow")
core_actionstep_MoveToInsertRow = Class(name="core::actionstep::MoveToInsertRow")
core_actionstep_InsertRow = Class(name="core::actionstep::InsertRow")
core_actionstep_MoveToFirstRow = Class(name="core::actionstep::MoveToFirstRow")
core_actionstep_DBConnectionId = Class(name="core::actionstep::DBConnectionId")
core_actionstep_DBQueryId = Class(name="core::actionstep::DBQueryId")
core_actionstep_DBQueryParamId = Class(name="core::actionstep::DBQueryParamId")
core_actionstep_DBResultSetId = Class(name="core::actionstep::DBResultSetId")
core_actionstep_GetColMapping = Class(name="core::actionstep::GetColMapping")
core_actionstep_SetColMapping = Class(name="core::actionstep::SetColMapping")
core_actionstep_RunQuery = Class(name="core::actionstep::RunQuery")
QueryParamMapping = Class(name="QueryParamMapping")
core_actionstep_QueryParamMapping = Class(name="core::actionstep::QueryParamMapping")
core_actionstep_Item = Class(name="core::actionstep::Item")
core_actionstep_Heavyweight = Class(name="core::actionstep::Heavyweight", is_abstract=True)
core_actionstep_OutputParameter = Class(name="core::actionstep::OutputParameter")
SafletScript = Class(name="SafletScript")
core_actionstep_Finally = Class(name="core::actionstep::Finally")
ScriptScope = Class(name="ScriptScope")
SafletScriptFactory = Class(name="SafletScriptFactory")
ScriptScopeFactory = Class(name="ScriptScopeFactory")
core_scripting_SafletScriptFactory = Class(name="core::scripting::SafletScriptFactory", is_abstract=True)
core_scripting_SafletScript = Class(name="core::scripting::SafletScript", is_abstract=True)
core_scripting_SafletScriptEnvironment = Class(name="core::scripting::SafletScriptEnvironment", is_abstract=True)
core_scripting_RhinoScriptScope = Class(name="core::scripting::RhinoScriptScope")
core_scripting_RhinoScriptScopeFactory = Class(name="core::scripting::RhinoScriptScopeFactory")
core_scripting_ScriptScope = Class(name="core::scripting::ScriptScope", is_abstract=True)
core_scripting_RhinoSafletScript = Class(name="core::scripting::RhinoSafletScript")
core_scripting_RhinoSafletScriptEnvironment = Class(name="core::scripting::RhinoSafletScriptEnvironment")
SafletScriptEnvironment = Class(name="SafletScriptEnvironment")
core_scripting_RhinoSafletScriptFactory = Class(name="core::scripting::RhinoSafletScriptFactory")
core_saflet_Saflet = Class(name="core::saflet::Saflet", is_abstract=True)
Initiator = Class(name="Initiator")
core_scripting_ScriptScopeFactory = Class(name="core::scripting::ScriptScopeFactory", is_abstract=True)
SafletEnvironment = Class(name="SafletEnvironment")
SafletContext = Class(name="SafletContext")
Finally = Class(name="Finally")
core_saflet_SafletContext = Class(name="core::saflet::SafletContext", is_abstract=True)
saflet_core_Variable = Class(name="saflet::core::Variable")
core_saflet_SafletEnvironment = Class(name="core::saflet::SafletEnvironment", is_abstract=True)
core_initiator_Initiator = Class(name="core::initiator::Initiator", is_abstract=True)
core_initiator_InitiatorInfo = Class(name="core::initiator::InitiatorInfo", is_abstract=True)
core_call_SafiCall = Class(name="core::call::SafiCall", is_abstract=True)
core_call_CallConsumer1 = Class(name="core::call::CallConsumer1", is_abstract=True)
core_call_CallConsumer2 = Class(name="core::call::CallConsumer2", is_abstract=True)
CallConsumer1 = Class(name="CallConsumer1")
core_call_CallSource1 = Class(name="core::call::CallSource1", is_abstract=True)
SafiCall = Class(name="SafiCall")
core_call_CallSource2 = Class(name="core::call::CallSource2", is_abstract=True)
CallSource1 = Class(name="CallSource1")

# core_actionstep_ActionStep class attributes and methods
core_actionstep_ActionStep_paused: Property = Property(name="paused", type=BooleanType)
core_actionstep_ActionStep_active: Property = Property(name="active", type=BooleanType)
core_actionstep_ActionStep_name: Property = Property(name="name", type=StringType)
core_actionstep_ActionStep_m_beginProcessing: Method = Method(name="beginProcessing", parameters={Parameter(name='context')})
core_actionstep_ActionStep_m_executeScript: Method = Method(name="executeScript", parameters={Parameter(name='scriptName'), Parameter(name='scriptText')}, type=StringType)
core_actionstep_ActionStep_m_handleException: Method = Method(name="handleException", parameters={Parameter(name='e'), Parameter(name='context')})
core_actionstep_ActionStep_m_resolveDynamicValue: Method = Method(name="resolveDynamicValue", parameters={Parameter(name='dynamicValue'), Parameter(name='context')}, type=StringType)
core_actionstep_ActionStep_m_createDefaultOutputs: Method = Method(name="createDefaultOutputs", parameters={})
core_actionstep_ActionStep.attributes={core_actionstep_ActionStep_name, core_actionstep_ActionStep_paused, core_actionstep_ActionStep_active}
core_actionstep_ActionStep.methods={core_actionstep_ActionStep_m_resolveDynamicValue, core_actionstep_ActionStep_m_handleException, core_actionstep_ActionStep_m_createDefaultOutputs, core_actionstep_ActionStep_m_executeScript, core_actionstep_ActionStep_m_beginProcessing}

# ProductIdentifiable class attributes and methods

# ThreadSensitive class attributes and methods

# PlatformDisposition class attributes and methods

# core_ProductIdentifiable class attributes and methods
core_ProductIdentifiable_productId: Property = Property(name="productId", type=StringType)
core_ProductIdentifiable.attributes={core_ProductIdentifiable_productId}

# core_ThreadSensitive class attributes and methods
core_ThreadSensitive_m_cleanup: Method = Method(name="cleanup", parameters={})
core_ThreadSensitive.methods={core_ThreadSensitive_m_cleanup}

# core_PlatformDisposition class attributes and methods
core_PlatformDisposition_platformID: Property = Property(name="platformID", type=StringType)
core_PlatformDisposition_platformDependant: Property = Property(name="platformDependant", type=BooleanType)
core_PlatformDisposition.attributes={core_PlatformDisposition_platformID, core_PlatformDisposition_platformDependant}

# Output class attributes and methods

# Saflet class attributes and methods

# core_actionstep_Assignment class attributes and methods

# ActionStep class attributes and methods

# DynamicValue class attributes and methods

# core_actionstep_CaseItem class attributes and methods

# Item class attributes and methods

# core_actionstep_InputItem class attributes and methods
core_actionstep_InputItem_parameterName: Property = Property(name="parameterName", type=StringType)
core_actionstep_InputItem_required: Property = Property(name="required", type=BooleanType)
core_actionstep_InputItem.attributes={core_actionstep_InputItem_parameterName, core_actionstep_InputItem_required}

# CaseItem class attributes and methods

# core_actionstep_ParameterizedActionstep class attributes and methods

# InputItem class attributes and methods

# OutputParameter class attributes and methods

# core_actionstep_ParameterizedInitiator class attributes and methods
core_actionstep_ParameterizedInitiator_m_getOutputMap: Method = Method(name="getOutputMap", parameters={})
core_actionstep_ParameterizedInitiator.methods={core_actionstep_ParameterizedInitiator_m_getOutputMap}

# initiator_Initiator class attributes and methods

# actionstep_ParameterizedActionstep class attributes and methods

# core_actionstep_Choice class attributes and methods

# core_actionstep_Output class attributes and methods
core_actionstep_Output_name: Property = Property(name="name", type=StringType)
core_actionstep_Output_outputType: Property = Property(name="outputType", type=StringType)
core_actionstep_Output.attributes={core_actionstep_Output_outputType, core_actionstep_Output_name}

# core_actionstep_DynamicValue class attributes and methods
core_actionstep_DynamicValue_text: Property = Property(name="text", type=StringType)
core_actionstep_DynamicValue_type: Property = Property(name="type", type=StringType)
core_actionstep_DynamicValue.attributes={core_actionstep_DynamicValue_text, core_actionstep_DynamicValue_type}

# actionstep_core_EObject class attributes and methods

# actionstep_core_EStringToStringMapEntry class attributes and methods

# core_actionstep_IfThen class attributes and methods

# core_actionstep_ExecuteScript class attributes and methods

# core_actionstep_InvokeSaflet class attributes and methods
core_actionstep_InvokeSaflet_labelText: Property = Property(name="labelText", type=StringType)
core_actionstep_InvokeSaflet.attributes={core_actionstep_InvokeSaflet_labelText}

# core_actionstep_OpenDBConnection class attributes and methods

# actionstep_ActionStep class attributes and methods

# core_actionstep_DebugLog class attributes and methods
core_actionstep_DebugLog_debugLevel: Property = Property(name="debugLevel", type=StringType)
core_actionstep_DebugLog.attributes={core_actionstep_DebugLog_debugLevel}

# actionstep_Heavyweight class attributes and methods

# DBConnectionId class attributes and methods

# core_actionstep_CloseDBConnection class attributes and methods

# core_actionstep_OpenQuery class attributes and methods
core_actionstep_OpenQuery_useCache: Property = Property(name="useCache", type=BooleanType)
core_actionstep_OpenQuery_scrollable: Property = Property(name="scrollable", type=BooleanType)
core_actionstep_OpenQuery_readOnly: Property = Property(name="readOnly", type=BooleanType)
core_actionstep_OpenQuery_scrollMode: Property = Property(name="scrollMode", type=StringType)
core_actionstep_OpenQuery_holdabilityMode: Property = Property(name="holdabilityMode", type=StringType)
core_actionstep_OpenQuery.attributes={core_actionstep_OpenQuery_readOnly, core_actionstep_OpenQuery_useCache, core_actionstep_OpenQuery_scrollable, core_actionstep_OpenQuery_scrollMode, core_actionstep_OpenQuery_holdabilityMode}

# DBQueryId class attributes and methods

# core_actionstep_SetQueryParam class attributes and methods
core_actionstep_SetQueryParam_paramDatatype: Property = Property(name="paramDatatype", type=StringType)
core_actionstep_SetQueryParam.attributes={core_actionstep_SetQueryParam_paramDatatype}

# DBQueryParamId class attributes and methods

# core_actionstep_ExecuteUpdate class attributes and methods

# core_actionstep_ExecuteQuery class attributes and methods
core_actionstep_ExecuteQuery_resultSetName: Property = Property(name="resultSetName", type=StringType)
core_actionstep_ExecuteQuery.attributes={core_actionstep_ExecuteQuery_resultSetName}

# DBResultSetId class attributes and methods

# core_actionstep_NextRow class attributes and methods

# core_actionstep_GetColValue class attributes and methods
core_actionstep_GetColValue_getAsDatatype: Property = Property(name="getAsDatatype", type=StringType)
core_actionstep_GetColValue.attributes={core_actionstep_GetColValue_getAsDatatype}

# core_actionstep_GetColValues class attributes and methods

# GetColMapping class attributes and methods

# core_actionstep_SetColValue class attributes and methods
core_actionstep_SetColValue_setAsDatatype: Property = Property(name="setAsDatatype", type=StringType)
core_actionstep_SetColValue.attributes={core_actionstep_SetColValue_setAsDatatype}

# core_actionstep_MoveToRow class attributes and methods

# core_actionstep_SetColValues class attributes and methods

# SetColMapping class attributes and methods

# core_actionstep_UpdatetRow class attributes and methods

# core_actionstep_DeleteRow class attributes and methods

# core_actionstep_MoveToLastRow class attributes and methods

# core_actionstep_PreviousRow class attributes and methods

# core_actionstep_MoveToInsertRow class attributes and methods

# core_actionstep_InsertRow class attributes and methods

# core_actionstep_MoveToFirstRow class attributes and methods

# core_actionstep_DBConnectionId class attributes and methods
core_actionstep_DBConnectionId_id: Property = Property(name="id", type=StringType)
core_actionstep_DBConnectionId_jdbcConnection: Property = Property(name="jdbcConnection", type=StringType)
core_actionstep_DBConnectionId.attributes={core_actionstep_DBConnectionId_id, core_actionstep_DBConnectionId_jdbcConnection}

# core_actionstep_DBQueryId class attributes and methods
core_actionstep_DBQueryId_id: Property = Property(name="id", type=StringType)
core_actionstep_DBQueryId_jdbcStatement: Property = Property(name="jdbcStatement", type=StringType)
core_actionstep_DBQueryId.attributes={core_actionstep_DBQueryId_jdbcStatement, core_actionstep_DBQueryId_id}

# core_actionstep_DBQueryParamId class attributes and methods
core_actionstep_DBQueryParamId_id: Property = Property(name="id", type=StringType)
core_actionstep_DBQueryParamId_index: Property = Property(name="index", type=IntegerType)
core_actionstep_DBQueryParamId.attributes={core_actionstep_DBQueryParamId_id, core_actionstep_DBQueryParamId_index}

# core_actionstep_DBResultSetId class attributes and methods
core_actionstep_DBResultSetId_name: Property = Property(name="name", type=StringType)
core_actionstep_DBResultSetId_id: Property = Property(name="id", type=StringType)
core_actionstep_DBResultSetId_jDBCResultSet: Property = Property(name="jDBCResultSet", type=StringType)
core_actionstep_DBResultSetId.attributes={core_actionstep_DBResultSetId_id, core_actionstep_DBResultSetId_jDBCResultSet, core_actionstep_DBResultSetId_name}

# core_actionstep_GetColMapping class attributes and methods
core_actionstep_GetColMapping_getAsDatatype: Property = Property(name="getAsDatatype", type=StringType)
core_actionstep_GetColMapping.attributes={core_actionstep_GetColMapping_getAsDatatype}

# core_actionstep_SetColMapping class attributes and methods
core_actionstep_SetColMapping_setAsDatatype: Property = Property(name="setAsDatatype", type=StringType)
core_actionstep_SetColMapping.attributes={core_actionstep_SetColMapping_setAsDatatype}

# core_actionstep_RunQuery class attributes and methods
core_actionstep_RunQuery_resultSetName: Property = Property(name="resultSetName", type=StringType)
core_actionstep_RunQuery_scrollable: Property = Property(name="scrollable", type=BooleanType)
core_actionstep_RunQuery_readOnly: Property = Property(name="readOnly", type=BooleanType)
core_actionstep_RunQuery_m_refreshParams: Method = Method(name="refreshParams", parameters={Parameter(name='qry')})
core_actionstep_RunQuery.attributes={core_actionstep_RunQuery_readOnly, core_actionstep_RunQuery_scrollable, core_actionstep_RunQuery_resultSetName}
core_actionstep_RunQuery.methods={core_actionstep_RunQuery_m_refreshParams}

# QueryParamMapping class attributes and methods

# core_actionstep_QueryParamMapping class attributes and methods
core_actionstep_QueryParamMapping_setAsDatatype: Property = Property(name="setAsDatatype", type=StringType)
core_actionstep_QueryParamMapping.attributes={core_actionstep_QueryParamMapping_setAsDatatype}

# core_actionstep_Item class attributes and methods
core_actionstep_Item_labelText: Property = Property(name="labelText", type=StringType)
core_actionstep_Item.attributes={core_actionstep_Item_labelText}

# core_actionstep_Heavyweight class attributes and methods

# core_actionstep_OutputParameter class attributes and methods

# SafletScript class attributes and methods

# core_actionstep_Finally class attributes and methods

# ScriptScope class attributes and methods

# SafletScriptFactory class attributes and methods

# ScriptScopeFactory class attributes and methods

# core_scripting_SafletScriptFactory class attributes and methods
core_scripting_SafletScriptFactory_m_getSafletScript: Method = Method(name="getSafletScript", parameters={Parameter(name='name'), Parameter(name='scriptText')}, type=StringType)
core_scripting_SafletScriptFactory.methods={core_scripting_SafletScriptFactory_m_getSafletScript}

# core_scripting_SafletScript class attributes and methods
core_scripting_SafletScript_name: Property = Property(name="name", type=StringType)
core_scripting_SafletScript_scriptText: Property = Property(name="scriptText", type=StringType)
core_scripting_SafletScript_m_execute: Method = Method(name="execute", parameters={Parameter(name='scope')}, type=StringType)
core_scripting_SafletScript.attributes={core_scripting_SafletScript_name, core_scripting_SafletScript_scriptText}
core_scripting_SafletScript.methods={core_scripting_SafletScript_m_execute}

# core_scripting_SafletScriptEnvironment class attributes and methods

# core_scripting_RhinoScriptScope class attributes and methods

# core_scripting_RhinoScriptScopeFactory class attributes and methods

# core_scripting_ScriptScope class attributes and methods
core_scripting_ScriptScope_scopeObject: Property = Property(name="scopeObject", type=StringType)
core_scripting_ScriptScope_m_exposeObjectToScript: Method = Method(name="exposeObjectToScript", parameters={Parameter(name='value'), Parameter(name='name')})
core_scripting_ScriptScope_m_removeObjectFromScope: Method = Method(name="removeObjectFromScope", parameters={Parameter(name='name')})
core_scripting_ScriptScope_m_getScopedObject: Method = Method(name="getScopedObject", parameters={Parameter(name='name')}, type=StringType)
core_scripting_ScriptScope_m_updateVariablesFromScope: Method = Method(name="updateVariablesFromScope", parameters={Parameter(name='safletEnvironment'), Parameter(name='variables'), Parameter(name='isDebug')})
core_scripting_ScriptScope.attributes={core_scripting_ScriptScope_scopeObject}
core_scripting_ScriptScope.methods={core_scripting_ScriptScope_m_removeObjectFromScope, core_scripting_ScriptScope_m_getScopedObject, core_scripting_ScriptScope_m_updateVariablesFromScope, core_scripting_ScriptScope_m_exposeObjectToScript}

# core_scripting_RhinoSafletScript class attributes and methods
core_scripting_RhinoSafletScript_rhinoScript: Property = Property(name="rhinoScript", type=StringType)
core_scripting_RhinoSafletScript.attributes={core_scripting_RhinoSafletScript_rhinoScript}

# core_scripting_RhinoSafletScriptEnvironment class attributes and methods

# SafletScriptEnvironment class attributes and methods

# core_scripting_RhinoSafletScriptFactory class attributes and methods

# core_saflet_Saflet class attributes and methods
core_saflet_Saflet_version: Property = Property(name="version", type=StringType)
core_saflet_Saflet_description: Property = Property(name="description", type=StringType)
core_saflet_Saflet_id: Property = Property(name="id", type=IntegerType)
core_saflet_Saflet_active: Property = Property(name="active", type=BooleanType)
core_saflet_Saflet_name: Property = Property(name="name", type=StringType)
core_saflet_Saflet_m_getActionStep: Method = Method(name="getActionStep", parameters={Parameter(name='name')}, type=StringType)
core_saflet_Saflet_m_addActionStep: Method = Method(name="addActionStep", parameters={Parameter(name='actionstep')})
core_saflet_Saflet_m_getScript: Method = Method(name="getScript", parameters={Parameter(name='name')}, type=StringType)
core_saflet_Saflet_m_addScript: Method = Method(name="addScript", parameters={Parameter(name='scriptText'), Parameter(name='name')}, type=StringType)
core_saflet_Saflet_m_initializeScriptableObjects: Method = Method(name="initializeScriptableObjects", parameters={})
core_saflet_Saflet_m_init: Method = Method(name="init", parameters={})
core_saflet_Saflet.attributes={core_saflet_Saflet_version, core_saflet_Saflet_id, core_saflet_Saflet_active, core_saflet_Saflet_description, core_saflet_Saflet_name}
core_saflet_Saflet.methods={core_saflet_Saflet_m_getActionStep, core_saflet_Saflet_m_addActionStep, core_saflet_Saflet_m_initializeScriptableObjects, core_saflet_Saflet_m_getScript, core_saflet_Saflet_m_init, core_saflet_Saflet_m_addScript}

# Initiator class attributes and methods

# core_scripting_ScriptScopeFactory class attributes and methods

# SafletEnvironment class attributes and methods

# SafletContext class attributes and methods

# Finally class attributes and methods

# core_saflet_SafletContext class attributes and methods
core_saflet_SafletContext_sessionVariables: Property = Property(name="sessionVariables", type=StringType)
core_saflet_SafletContext_exceptions: Property = Property(name="exceptions", type=StringType)
core_saflet_SafletContext_m_getVariableRawValue: Method = Method(name="getVariableRawValue", parameters={Parameter(name='name')}, type=StringType)
core_saflet_SafletContext_m_setVariableRawValue: Method = Method(name="setVariableRawValue", parameters={Parameter(name='value'), Parameter(name='name')})
core_saflet_SafletContext_m_addOrUpdateVariable: Method = Method(name="addOrUpdateVariable", parameters={Parameter(name='v')})
core_saflet_SafletContext_m_removeVariable: Method = Method(name="removeVariable", parameters={Parameter(name='name')}, type=StringType)
core_saflet_SafletContext_m_addException: Method = Method(name="addException", parameters={Parameter(name='e')})
core_saflet_SafletContext_m_merge: Method = Method(name="merge", parameters={Parameter(name='context')})
core_saflet_SafletContext_m_getSessionVar: Method = Method(name="getSessionVar", parameters={Parameter(name='name')}, type=StringType)
core_saflet_SafletContext_m_setSessionVar: Method = Method(name="setSessionVar", parameters={Parameter(name='name'), Parameter(name='value')})
core_saflet_SafletContext_m_init: Method = Method(name="init", parameters={})
core_saflet_SafletContext_m_getVariable: Method = Method(name="getVariable", parameters={Parameter(name='name')}, type=StringType)
core_saflet_SafletContext_m_preHandoffPrep: Method = Method(name="preHandoffPrep", parameters={Parameter(name='call')})
core_saflet_SafletContext.attributes={core_saflet_SafletContext_exceptions, core_saflet_SafletContext_sessionVariables}
core_saflet_SafletContext.methods={core_saflet_SafletContext_m_getVariable, core_saflet_SafletContext_m_removeVariable, core_saflet_SafletContext_m_merge, core_saflet_SafletContext_m_preHandoffPrep, core_saflet_SafletContext_m_init, core_saflet_SafletContext_m_setSessionVar, core_saflet_SafletContext_m_getVariableRawValue, core_saflet_SafletContext_m_getSessionVar, core_saflet_SafletContext_m_addOrUpdateVariable, core_saflet_SafletContext_m_addException, core_saflet_SafletContext_m_setVariableRawValue}

# saflet_core_Variable class attributes and methods

# core_saflet_SafletEnvironment class attributes and methods
core_saflet_SafletEnvironment_m_getSaflet: Method = Method(name="getSaflet", parameters={Parameter(name='path'), Parameter(name='coreServerId')}, type=StringType)
core_saflet_SafletEnvironment_m_getGlobalExecutor: Method = Method(name="getGlobalExecutor", parameters={}, type=StringType)
core_saflet_SafletEnvironment_m_getGlobalVariableValue: Method = Method(name="getGlobalVariableValue", parameters={Parameter(name='name')}, type=StringType)
core_saflet_SafletEnvironment_m_setGlobalVariableValue: Method = Method(name="setGlobalVariableValue", parameters={Parameter(name='name'), Parameter(name='value')})
core_saflet_SafletEnvironment_m_getGlobalVariable: Method = Method(name="getGlobalVariable", parameters={Parameter(name='name')}, type=StringType)
core_saflet_SafletEnvironment.methods={core_saflet_SafletEnvironment_m_setGlobalVariableValue, core_saflet_SafletEnvironment_m_getSaflet, core_saflet_SafletEnvironment_m_getGlobalVariableValue, core_saflet_SafletEnvironment_m_getGlobalVariable, core_saflet_SafletEnvironment_m_getGlobalExecutor}

# core_initiator_Initiator class attributes and methods
core_initiator_Initiator_m_acceptsRequest: Method = Method(name="acceptsRequest", parameters={Parameter(name='context')}, type=BooleanType)
core_initiator_Initiator_m_initialize: Method = Method(name="initialize", parameters={Parameter(name='context')})
core_initiator_Initiator_m_beginProcessing: Method = Method(name="beginProcessing", parameters={})
core_initiator_Initiator.methods={core_initiator_Initiator_m_beginProcessing, core_initiator_Initiator_m_initialize, core_initiator_Initiator_m_acceptsRequest}

# core_initiator_InitiatorInfo class attributes and methods

# core_call_SafiCall class attributes and methods
core_call_SafiCall_uuid: Property = Property(name="uuid", type=StringType)
core_call_SafiCall_name: Property = Property(name="name", type=StringType)
core_call_SafiCall.attributes={core_call_SafiCall_uuid, core_call_SafiCall_name}

# core_call_CallConsumer1 class attributes and methods

# core_call_CallConsumer2 class attributes and methods

# CallConsumer1 class attributes and methods

# core_call_CallSource1 class attributes and methods

# SafiCall class attributes and methods

# core_call_CallSource2 class attributes and methods

# CallSource1 class attributes and methods

# Relationships
saflet1: BinaryAssociation = BinaryAssociation(
    name="saflet1",
    ends={
        Property(name="Saflet", type=Saflet, multiplicity=Multiplicity(0, 1)),
        Property(name="saflet", type=core_actionstep_ActionStep, multiplicity=Multiplicity(1, 1))
    }
)
defaultOutput2: BinaryAssociation = BinaryAssociation(
    name="defaultOutput2",
    ends={
        Property(name="Output3", type=core_actionstep_ActionStep, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_ActionStep", type=Output, multiplicity=Multiplicity(0, 1))
    }
)
outputs0: BinaryAssociation = BinaryAssociation(
    name="outputs0",
    ends={
        Property(name="actionstep", type=core_actionstep_ActionStep, multiplicity=Multiplicity(1, 1)),
        Property(name="Output", type=Output, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
errorOutput4: BinaryAssociation = BinaryAssociation(
    name="errorOutput4",
    ends={
        Property(name="Output6", type=core_actionstep_ActionStep, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_ActionStep5", type=Output, multiplicity=Multiplicity(0, 1))
    }
)
value7: BinaryAssociation = BinaryAssociation(
    name="value7",
    ends={
        Property(name="DynamicValue", type=core_actionstep_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_Assignment", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableName8: BinaryAssociation = BinaryAssociation(
    name="variableName8",
    ends={
        Property(name="DynamicValue10", type=core_actionstep_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_Assignment9", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dynamicValue11: BinaryAssociation = BinaryAssociation(
    name="dynamicValue11",
    ends={
        Property(name="DynamicValue12", type=core_actionstep_CaseItem, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_CaseItem", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value17: BinaryAssociation = BinaryAssociation(
    name="value17",
    ends={
        Property(name="DynamicValue19", type=core_actionstep_Choice, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_Choice18", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inputs13: BinaryAssociation = BinaryAssociation(
    name="inputs13",
    ends={
        Property(name="InputItem", type=core_actionstep_ParameterizedActionstep, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_ParameterizedActionstep", type=InputItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputParameters14: BinaryAssociation = BinaryAssociation(
    name="outputParameters14",
    ends={
        Property(name="OutputParameter", type=core_actionstep_ParameterizedActionstep, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_ParameterizedActionstep15", type=OutputParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
choices16: BinaryAssociation = BinaryAssociation(
    name="choices16",
    ends={
        Property(name="CaseItem", type=core_actionstep_Choice, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_Choice", type=CaseItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
payload20: BinaryAssociation = BinaryAssociation(
    name="payload20",
    ends={
        Property(name="actionstep_core_EObject", type=core_actionstep_DynamicValue, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_DynamicValue", type=actionstep_core_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
data21: BinaryAssociation = BinaryAssociation(
    name="data21",
    ends={
        Property(name="actionstep_core_EStringToStringMapEntry", type=core_actionstep_DynamicValue, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_DynamicValue22", type=actionstep_core_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
booleanExpression23: BinaryAssociation = BinaryAssociation(
    name="booleanExpression23",
    ends={
        Property(name="DynamicValue24", type=core_actionstep_IfThen, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_IfThen", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetSafletPath31: BinaryAssociation = BinaryAssociation(
    name="targetSafletPath31",
    ends={
        Property(name="DynamicValue32", type=core_actionstep_InvokeSaflet, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_InvokeSaflet", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target25: BinaryAssociation = BinaryAssociation(
    name="target25",
    ends={
        Property(name="ActionStep", type=core_actionstep_Output, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_Output", type=ActionStep, multiplicity=Multiplicity(0, 1))
    }
)
parent26: BinaryAssociation = BinaryAssociation(
    name="parent26",
    ends={
        Property(name="actionstep28", type=core_actionstep_Output, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionStep27", type=ActionStep, multiplicity=Multiplicity(0, 1))
    }
)
scriptText29: BinaryAssociation = BinaryAssociation(
    name="scriptText29",
    ends={
        Property(name="DynamicValue30", type=core_actionstep_ExecuteScript, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_ExecuteScript", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
message33: BinaryAssociation = BinaryAssociation(
    name="message33",
    ends={
        Property(name="DynamicValue34", type=core_actionstep_DebugLog, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_DebugLog", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
logFilename35: BinaryAssociation = BinaryAssociation(
    name="logFilename35",
    ends={
        Property(name="DynamicValue37", type=core_actionstep_DebugLog, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_DebugLog36", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
connection42: BinaryAssociation = BinaryAssociation(
    name="connection42",
    ends={
        Property(name="core_actionstep_OpenQuery43", type=DBConnectionId, multiplicity=Multiplicity(0, 1)),
        Property(name="DBConnectionId44", type=core_actionstep_OpenQuery, multiplicity=Multiplicity(1, 1))
    }
)
connection38: BinaryAssociation = BinaryAssociation(
    name="connection38",
    ends={
        Property(name="DBConnectionId", type=core_actionstep_OpenDBConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_OpenDBConnection", type=DBConnectionId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
connection39: BinaryAssociation = BinaryAssociation(
    name="connection39",
    ends={
        Property(name="DBConnectionId40", type=core_actionstep_CloseDBConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_CloseDBConnection", type=DBConnectionId, multiplicity=Multiplicity(0, 1))
    }
)
query41: BinaryAssociation = BinaryAssociation(
    name="query41",
    ends={
        Property(name="DBQueryId", type=core_actionstep_OpenQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_OpenQuery", type=DBQueryId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value45: BinaryAssociation = BinaryAssociation(
    name="value45",
    ends={
        Property(name="DynamicValue46", type=core_actionstep_SetQueryParam, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_SetQueryParam", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter47: BinaryAssociation = BinaryAssociation(
    name="parameter47",
    ends={
        Property(name="DBQueryParamId", type=core_actionstep_SetQueryParam, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_SetQueryParam48", type=DBQueryParamId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
query57: BinaryAssociation = BinaryAssociation(
    name="query57",
    ends={
        Property(name="DBQueryId58", type=core_actionstep_ExecuteQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_ExecuteQuery", type=DBQueryId, multiplicity=Multiplicity(0, 1))
    }
)
query49: BinaryAssociation = BinaryAssociation(
    name="query49",
    ends={
        Property(name="DBQueryId51", type=core_actionstep_SetQueryParam, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_SetQueryParam50", type=DBQueryId, multiplicity=Multiplicity(0, 1))
    }
)
query52: BinaryAssociation = BinaryAssociation(
    name="query52",
    ends={
        Property(name="DBQueryId53", type=core_actionstep_ExecuteUpdate, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_ExecuteUpdate", type=DBQueryId, multiplicity=Multiplicity(0, 1))
    }
)
rowsUpdatedVar54: BinaryAssociation = BinaryAssociation(
    name="rowsUpdatedVar54",
    ends={
        Property(name="DynamicValue56", type=core_actionstep_ExecuteUpdate, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_ExecuteUpdate55", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableName65: BinaryAssociation = BinaryAssociation(
    name="variableName65",
    ends={
        Property(name="DynamicValue67", type=core_actionstep_GetColValue, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_GetColValue66", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resultSet59: BinaryAssociation = BinaryAssociation(
    name="resultSet59",
    ends={
        Property(name="DBResultSetId", type=core_actionstep_ExecuteQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_ExecuteQuery60", type=DBResultSetId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resultSet61: BinaryAssociation = BinaryAssociation(
    name="resultSet61",
    ends={
        Property(name="DBResultSetId62", type=core_actionstep_NextRow, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_NextRow", type=DBResultSetId, multiplicity=Multiplicity(0, 1))
    }
)
resultSet63: BinaryAssociation = BinaryAssociation(
    name="resultSet63",
    ends={
        Property(name="DBResultSetId64", type=core_actionstep_GetColValue, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_GetColValue", type=DBResultSetId, multiplicity=Multiplicity(0, 1))
    }
)
resultSet71: BinaryAssociation = BinaryAssociation(
    name="resultSet71",
    ends={
        Property(name="DBResultSetId72", type=core_actionstep_GetColValues, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_GetColValues", type=DBResultSetId, multiplicity=Multiplicity(0, 1))
    }
)
column68: BinaryAssociation = BinaryAssociation(
    name="column68",
    ends={
        Property(name="DynamicValue70", type=core_actionstep_GetColValue, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_GetColValue69", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value80: BinaryAssociation = BinaryAssociation(
    name="value80",
    ends={
        Property(name="DynamicValue82", type=core_actionstep_SetColValue, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_SetColValue81", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
columnMappings73: BinaryAssociation = BinaryAssociation(
    name="columnMappings73",
    ends={
        Property(name="GetColMapping", type=core_actionstep_GetColValues, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_GetColValues74", type=GetColMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resultSet75: BinaryAssociation = BinaryAssociation(
    name="resultSet75",
    ends={
        Property(name="DBResultSetId76", type=core_actionstep_SetColValue, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_SetColValue", type=DBResultSetId, multiplicity=Multiplicity(0, 1))
    }
)
column77: BinaryAssociation = BinaryAssociation(
    name="column77",
    ends={
        Property(name="DynamicValue79", type=core_actionstep_SetColValue, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_SetColValue78", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resultSet83: BinaryAssociation = BinaryAssociation(
    name="resultSet83",
    ends={
        Property(name="DBResultSetId84", type=core_actionstep_SetColValues, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_SetColValues", type=DBResultSetId, multiplicity=Multiplicity(0, 1))
    }
)
columnMappings85: BinaryAssociation = BinaryAssociation(
    name="columnMappings85",
    ends={
        Property(name="SetColMapping", type=core_actionstep_SetColValues, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_SetColValues86", type=SetColMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resultSet87: BinaryAssociation = BinaryAssociation(
    name="resultSet87",
    ends={
        Property(name="DBResultSetId88", type=core_actionstep_UpdatetRow, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_UpdatetRow", type=DBResultSetId, multiplicity=Multiplicity(0, 1))
    }
)
resultSet96: BinaryAssociation = BinaryAssociation(
    name="resultSet96",
    ends={
        Property(name="DBResultSetId97", type=core_actionstep_DeleteRow, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_DeleteRow", type=DBResultSetId, multiplicity=Multiplicity(0, 1))
    }
)
resultSet89: BinaryAssociation = BinaryAssociation(
    name="resultSet89",
    ends={
        Property(name="DBResultSetId90", type=core_actionstep_MoveToRow, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_MoveToRow", type=DBResultSetId, multiplicity=Multiplicity(0, 1))
    }
)
rowNum91: BinaryAssociation = BinaryAssociation(
    name="rowNum91",
    ends={
        Property(name="DynamicValue93", type=core_actionstep_MoveToRow, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_MoveToRow92", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resultSet94: BinaryAssociation = BinaryAssociation(
    name="resultSet94",
    ends={
        Property(name="DBResultSetId95", type=core_actionstep_MoveToLastRow, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_MoveToLastRow", type=DBResultSetId, multiplicity=Multiplicity(0, 1))
    }
)
resultSet98: BinaryAssociation = BinaryAssociation(
    name="resultSet98",
    ends={
        Property(name="DBResultSetId99", type=core_actionstep_MoveToInsertRow, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_MoveToInsertRow", type=DBResultSetId, multiplicity=Multiplicity(0, 1))
    }
)
resultSet100: BinaryAssociation = BinaryAssociation(
    name="resultSet100",
    ends={
        Property(name="DBResultSetId101", type=core_actionstep_InsertRow, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_InsertRow", type=DBResultSetId, multiplicity=Multiplicity(0, 1))
    }
)
resultSet102: BinaryAssociation = BinaryAssociation(
    name="resultSet102",
    ends={
        Property(name="DBResultSetId103", type=core_actionstep_MoveToFirstRow, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_MoveToFirstRow", type=DBResultSetId, multiplicity=Multiplicity(0, 1))
    }
)
resultSet104: BinaryAssociation = BinaryAssociation(
    name="resultSet104",
    ends={
        Property(name="DBResultSetId105", type=core_actionstep_PreviousRow, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_PreviousRow", type=DBResultSetId, multiplicity=Multiplicity(0, 1))
    }
)
column111: BinaryAssociation = BinaryAssociation(
    name="column111",
    ends={
        Property(name="DynamicValue112", type=core_actionstep_SetColMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_SetColMapping", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableName106: BinaryAssociation = BinaryAssociation(
    name="variableName106",
    ends={
        Property(name="DynamicValue107", type=core_actionstep_GetColMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_GetColMapping", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
column108: BinaryAssociation = BinaryAssociation(
    name="column108",
    ends={
        Property(name="DynamicValue110", type=core_actionstep_GetColMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_GetColMapping109", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
query118: BinaryAssociation = BinaryAssociation(
    name="query118",
    ends={
        Property(name="DBQueryId120", type=core_actionstep_RunQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_RunQuery119", type=DBQueryId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value113: BinaryAssociation = BinaryAssociation(
    name="value113",
    ends={
        Property(name="DynamicValue115", type=core_actionstep_SetColMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_SetColMapping114", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
connection116: BinaryAssociation = BinaryAssociation(
    name="connection116",
    ends={
        Property(name="DBConnectionId117", type=core_actionstep_RunQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_RunQuery", type=DBConnectionId, multiplicity=Multiplicity(0, 1))
    }
)
sql129: BinaryAssociation = BinaryAssociation(
    name="sql129",
    ends={
        Property(name="DynamicValue131", type=core_actionstep_RunQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_RunQuery130", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
paramMappings121: BinaryAssociation = BinaryAssociation(
    name="paramMappings121",
    ends={
        Property(name="QueryParamMapping", type=core_actionstep_RunQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_RunQuery122", type=QueryParamMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resultSet123: BinaryAssociation = BinaryAssociation(
    name="resultSet123",
    ends={
        Property(name="DBResultSetId125", type=core_actionstep_RunQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_RunQuery124", type=DBResultSetId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rowsUpdatedVar126: BinaryAssociation = BinaryAssociation(
    name="rowsUpdatedVar126",
    ends={
        Property(name="DynamicValue128", type=core_actionstep_RunQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_RunQuery127", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parentActionStep137: BinaryAssociation = BinaryAssociation(
    name="parentActionStep137",
    ends={
        Property(name="ActionStep138", type=core_actionstep_Item, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_Item", type=ActionStep, multiplicity=Multiplicity(0, 1))
    }
)
queryParam132: BinaryAssociation = BinaryAssociation(
    name="queryParam132",
    ends={
        Property(name="DBQueryParamId133", type=core_actionstep_QueryParamMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_QueryParamMapping", type=DBQueryParamId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value134: BinaryAssociation = BinaryAssociation(
    name="value134",
    ends={
        Property(name="DynamicValue136", type=core_actionstep_QueryParamMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_QueryParamMapping135", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetActionStep139: BinaryAssociation = BinaryAssociation(
    name="targetActionStep139",
    ends={
        Property(name="ActionStep141", type=core_actionstep_Item, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_Item140", type=ActionStep, multiplicity=Multiplicity(0, 1))
    }
)
sharedSafletScript142: BinaryAssociation = BinaryAssociation(
    name="sharedSafletScript142",
    ends={
        Property(name="SafletScript", type=core_scripting_SafletScriptEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="core_scripting_SafletScriptEnvironment", type=SafletScript, multiplicity=Multiplicity(0, 1))
    }
)
sharedScriptScope143: BinaryAssociation = BinaryAssociation(
    name="sharedScriptScope143",
    ends={
        Property(name="ScriptScope", type=core_scripting_SafletScriptEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="core_scripting_SafletScriptEnvironment144", type=ScriptScope, multiplicity=Multiplicity(0, 1))
    }
)
safletScriptFactory145: BinaryAssociation = BinaryAssociation(
    name="safletScriptFactory145",
    ends={
        Property(name="SafletScriptFactory", type=core_scripting_SafletScriptEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="core_scripting_SafletScriptEnvironment146", type=SafletScriptFactory, multiplicity=Multiplicity(0, 1))
    }
)
scriptScopeFactory147: BinaryAssociation = BinaryAssociation(
    name="scriptScopeFactory147",
    ends={
        Property(name="ScriptScopeFactory", type=core_scripting_SafletScriptEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="core_scripting_SafletScriptEnvironment148", type=ScriptScopeFactory, multiplicity=Multiplicity(0, 1))
    }
)
safletScript149: BinaryAssociation = BinaryAssociation(
    name="safletScript149",
    ends={
        Property(name="SafletScript150", type=core_scripting_SafletScriptFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="core_scripting_SafletScriptFactory", type=SafletScript, multiplicity=Multiplicity(0, 1))
    }
)
initiator156: BinaryAssociation = BinaryAssociation(
    name="initiator156",
    ends={
        Property(name="Initiator", type=core_saflet_Saflet, multiplicity=Multiplicity(1, 1)),
        Property(name="core_saflet_Saflet", type=Initiator, multiplicity=Multiplicity(0, 1))
    }
)
scriptScope151: BinaryAssociation = BinaryAssociation(
    name="scriptScope151",
    ends={
        Property(name="ScriptScope152", type=core_scripting_ScriptScopeFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="core_scripting_ScriptScopeFactory", type=ScriptScope, multiplicity=Multiplicity(0, 1))
    }
)
globalScriptScope153: BinaryAssociation = BinaryAssociation(
    name="globalScriptScope153",
    ends={
        Property(name="ScriptScope155", type=core_scripting_ScriptScopeFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="core_scripting_ScriptScopeFactory154", type=ScriptScope, multiplicity=Multiplicity(0, 1))
    }
)
safletScope159: BinaryAssociation = BinaryAssociation(
    name="safletScope159",
    ends={
        Property(name="ScriptScope161", type=core_saflet_Saflet, multiplicity=Multiplicity(1, 1)),
        Property(name="core_saflet_Saflet160", type=ScriptScope, multiplicity=Multiplicity(0, 1))
    }
)
actionsteps162: BinaryAssociation = BinaryAssociation(
    name="actionsteps162",
    ends={
        Property(name="actionstep164", type=core_saflet_Saflet, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionStep163", type=ActionStep, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scriptingEnvironment165: BinaryAssociation = BinaryAssociation(
    name="scriptingEnvironment165",
    ends={
        Property(name="SafletScriptEnvironment", type=core_saflet_Saflet, multiplicity=Multiplicity(1, 1)),
        Property(name="core_saflet_Saflet166", type=SafletScriptEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
safletEnvironment167: BinaryAssociation = BinaryAssociation(
    name="safletEnvironment167",
    ends={
        Property(name="SafletEnvironment", type=core_saflet_Saflet, multiplicity=Multiplicity(1, 1)),
        Property(name="core_saflet_Saflet168", type=SafletEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
safletContext157: BinaryAssociation = BinaryAssociation(
    name="safletContext157",
    ends={
        Property(name="SafletContext", type=core_saflet_Saflet, multiplicity=Multiplicity(1, 1)),
        Property(name="core_saflet_Saflet158", type=SafletContext, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
finally169: BinaryAssociation = BinaryAssociation(
    name="finally169",
    ends={
        Property(name="Finally", type=core_saflet_Saflet, multiplicity=Multiplicity(1, 1)),
        Property(name="core_saflet_Saflet170", type=Finally, multiplicity=Multiplicity(0, 1))
    }
)
parentSaflet171: BinaryAssociation = BinaryAssociation(
    name="parentSaflet171",
    ends={
        Property(name="Saflet172", type=core_saflet_SafletContext, multiplicity=Multiplicity(1, 1)),
        Property(name="core_saflet_SafletContext", type=Saflet, multiplicity=Multiplicity(0, 1))
    }
)
variables173: BinaryAssociation = BinaryAssociation(
    name="variables173",
    ends={
        Property(name="saflet_core_Variable", type=core_saflet_SafletContext, multiplicity=Multiplicity(1, 1)),
        Property(name="core_saflet_SafletContext174", type=saflet_core_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
newCall2176: BinaryAssociation = BinaryAssociation(
    name="newCall2176",
    ends={
        Property(name="SafiCall177", type=core_call_CallSource2, multiplicity=Multiplicity(1, 1)),
        Property(name="core_call_CallSource2", type=SafiCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
call1178: BinaryAssociation = BinaryAssociation(
    name="call1178",
    ends={
        Property(name="SafiCall179", type=core_call_CallConsumer1, multiplicity=Multiplicity(1, 1)),
        Property(name="core_call_CallConsumer1", type=SafiCall, multiplicity=Multiplicity(0, 1))
    }
)
call2180: BinaryAssociation = BinaryAssociation(
    name="call2180",
    ends={
        Property(name="SafiCall181", type=core_call_CallConsumer2, multiplicity=Multiplicity(1, 1)),
        Property(name="core_call_CallConsumer2", type=SafiCall, multiplicity=Multiplicity(0, 1))
    }
)
newCall1175: BinaryAssociation = BinaryAssociation(
    name="newCall1175",
    ends={
        Property(name="SafiCall", type=core_call_CallSource1, multiplicity=Multiplicity(1, 1)),
        Property(name="core_call_CallSource1", type=SafiCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_core_actionstep_ActionStep_ProductIdentifiable = Generalization(general=ProductIdentifiable, specific=core_actionstep_ActionStep)
gen_core_actionstep_ActionStep_ThreadSensitive = Generalization(general=ThreadSensitive, specific=core_actionstep_ActionStep)
gen_core_actionstep_ActionStep_PlatformDisposition = Generalization(general=PlatformDisposition, specific=core_actionstep_ActionStep)
gen_core_actionstep_Assignment_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_Assignment)
gen_core_actionstep_CaseItem_Item = Generalization(general=Item, specific=core_actionstep_CaseItem)
gen_core_actionstep_InputItem_CaseItem = Generalization(general=CaseItem, specific=core_actionstep_InputItem)
gen_core_actionstep_ParameterizedActionstep_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_ParameterizedActionstep)
gen_core_actionstep_ParameterizedInitiator_initiator_Initiator = Generalization(general=initiator_Initiator, specific=core_actionstep_ParameterizedInitiator)
gen_core_actionstep_ParameterizedInitiator_actionstep_ParameterizedActionstep = Generalization(general=actionstep_ParameterizedActionstep, specific=core_actionstep_ParameterizedInitiator)
gen_core_actionstep_Choice_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_Choice)
gen_core_actionstep_DynamicValue_ThreadSensitive = Generalization(general=ThreadSensitive, specific=core_actionstep_DynamicValue)
gen_core_actionstep_IfThen_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_IfThen)
gen_core_actionstep_ExecuteScript_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_ExecuteScript)
gen_core_actionstep_InvokeSaflet_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_InvokeSaflet)
gen_core_actionstep_OpenDBConnection_actionstep_ActionStep = Generalization(general=actionstep_ActionStep, specific=core_actionstep_OpenDBConnection)
gen_core_actionstep_DebugLog_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_DebugLog)
gen_core_actionstep_OpenDBConnection_actionstep_Heavyweight = Generalization(general=actionstep_Heavyweight, specific=core_actionstep_OpenDBConnection)
gen_core_actionstep_CloseDBConnection_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_CloseDBConnection)
gen_core_actionstep_OpenQuery_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_OpenQuery)
gen_core_actionstep_SetQueryParam_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_SetQueryParam)
gen_core_actionstep_ExecuteUpdate_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_ExecuteUpdate)
gen_core_actionstep_ExecuteQuery_actionstep_ActionStep = Generalization(general=actionstep_ActionStep, specific=core_actionstep_ExecuteQuery)
gen_core_actionstep_ExecuteQuery_actionstep_Heavyweight = Generalization(general=actionstep_Heavyweight, specific=core_actionstep_ExecuteQuery)
gen_core_actionstep_NextRow_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_NextRow)
gen_core_actionstep_GetColValue_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_GetColValue)
gen_core_actionstep_GetColValues_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_GetColValues)
gen_core_actionstep_SetColValue_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_SetColValue)
gen_core_actionstep_MoveToRow_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_MoveToRow)
gen_core_actionstep_SetColValues_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_SetColValues)
gen_core_actionstep_UpdatetRow_actionstep_ActionStep = Generalization(general=actionstep_ActionStep, specific=core_actionstep_UpdatetRow)
gen_core_actionstep_UpdatetRow_actionstep_Heavyweight = Generalization(general=actionstep_Heavyweight, specific=core_actionstep_UpdatetRow)
gen_core_actionstep_DeleteRow_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_DeleteRow)
gen_core_actionstep_MoveToLastRow_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_MoveToLastRow)
gen_core_actionstep_MoveToInsertRow_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_MoveToInsertRow)
gen_core_actionstep_InsertRow_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_InsertRow)
gen_core_actionstep_MoveToFirstRow_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_MoveToFirstRow)
gen_core_actionstep_PreviousRow_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_PreviousRow)
gen_core_actionstep_DBConnectionId_ThreadSensitive = Generalization(general=ThreadSensitive, specific=core_actionstep_DBConnectionId)
gen_core_actionstep_DBQueryId_ThreadSensitive = Generalization(general=ThreadSensitive, specific=core_actionstep_DBQueryId)
gen_core_actionstep_DBResultSetId_ThreadSensitive = Generalization(general=ThreadSensitive, specific=core_actionstep_DBResultSetId)
gen_core_actionstep_GetColMapping_Item = Generalization(general=Item, specific=core_actionstep_GetColMapping)
gen_core_actionstep_SetColMapping_Item = Generalization(general=Item, specific=core_actionstep_SetColMapping)
gen_core_actionstep_RunQuery_actionstep_ActionStep = Generalization(general=actionstep_ActionStep, specific=core_actionstep_RunQuery)
gen_core_actionstep_RunQuery_actionstep_Heavyweight = Generalization(general=actionstep_Heavyweight, specific=core_actionstep_RunQuery)
gen_core_actionstep_QueryParamMapping_Item = Generalization(general=Item, specific=core_actionstep_QueryParamMapping)
gen_core_actionstep_Item_ThreadSensitive = Generalization(general=ThreadSensitive, specific=core_actionstep_Item)
gen_core_actionstep_OutputParameter_InputItem = Generalization(general=InputItem, specific=core_actionstep_OutputParameter)
gen_core_actionstep_Finally_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_Finally)
gen_core_scripting_RhinoScriptScope_ScriptScope = Generalization(general=ScriptScope, specific=core_scripting_RhinoScriptScope)
gen_core_scripting_RhinoScriptScopeFactory_ScriptScopeFactory = Generalization(general=ScriptScopeFactory, specific=core_scripting_RhinoScriptScopeFactory)
gen_core_scripting_RhinoSafletScript_SafletScript = Generalization(general=SafletScript, specific=core_scripting_RhinoSafletScript)
gen_core_scripting_RhinoSafletScriptEnvironment_SafletScriptEnvironment = Generalization(general=SafletScriptEnvironment, specific=core_scripting_RhinoSafletScriptEnvironment)
gen_core_scripting_RhinoSafletScriptFactory_SafletScriptFactory = Generalization(general=SafletScriptFactory, specific=core_scripting_RhinoSafletScriptFactory)
gen_core_saflet_Saflet_ThreadSensitive = Generalization(general=ThreadSensitive, specific=core_saflet_Saflet)
gen_core_saflet_Saflet_PlatformDisposition = Generalization(general=PlatformDisposition, specific=core_saflet_Saflet)
gen_core_saflet_SafletContext_ThreadSensitive = Generalization(general=ThreadSensitive, specific=core_saflet_SafletContext)
gen_core_saflet_SafletEnvironment_ThreadSensitive = Generalization(general=ThreadSensitive, specific=core_saflet_SafletEnvironment)
gen_core_initiator_Initiator_ActionStep = Generalization(general=ActionStep, specific=core_initiator_Initiator)
gen_core_call_SafiCall_ThreadSensitive = Generalization(general=ThreadSensitive, specific=core_call_SafiCall)
gen_core_call_SafiCall_PlatformDisposition = Generalization(general=PlatformDisposition, specific=core_call_SafiCall)
gen_core_call_CallConsumer2_CallConsumer1 = Generalization(general=CallConsumer1, specific=core_call_CallConsumer2)
gen_core_call_CallSource2_CallSource1 = Generalization(general=CallSource1, specific=core_call_CallSource2)

# Domain Model
domain_model = DomainModel(
    name="core",
    types={core_actionstep_ActionStep, ProductIdentifiable, ThreadSensitive, PlatformDisposition, core_ProductIdentifiable, core_ThreadSensitive, core_PlatformDisposition, Output, Saflet, core_actionstep_Assignment, ActionStep, DynamicValue, core_actionstep_CaseItem, Item, core_actionstep_InputItem, CaseItem, core_actionstep_ParameterizedActionstep, InputItem, OutputParameter, core_actionstep_ParameterizedInitiator, initiator_Initiator, actionstep_ParameterizedActionstep, core_actionstep_Choice, core_actionstep_Output, core_actionstep_DynamicValue, actionstep_core_EObject, actionstep_core_EStringToStringMapEntry, core_actionstep_IfThen, core_actionstep_ExecuteScript, core_actionstep_InvokeSaflet, core_actionstep_OpenDBConnection, actionstep_ActionStep, core_actionstep_DebugLog, actionstep_Heavyweight, DBConnectionId, core_actionstep_CloseDBConnection, core_actionstep_OpenQuery, DBQueryId, core_actionstep_SetQueryParam, DBQueryParamId, core_actionstep_ExecuteUpdate, core_actionstep_ExecuteQuery, DBResultSetId, core_actionstep_NextRow, core_actionstep_GetColValue, core_actionstep_GetColValues, GetColMapping, core_actionstep_SetColValue, core_actionstep_MoveToRow, core_actionstep_SetColValues, SetColMapping, core_actionstep_UpdatetRow, core_actionstep_DeleteRow, core_actionstep_MoveToLastRow, core_actionstep_PreviousRow, core_actionstep_MoveToInsertRow, core_actionstep_InsertRow, core_actionstep_MoveToFirstRow, core_actionstep_DBConnectionId, core_actionstep_DBQueryId, core_actionstep_DBQueryParamId, core_actionstep_DBResultSetId, core_actionstep_GetColMapping, core_actionstep_SetColMapping, core_actionstep_RunQuery, QueryParamMapping, core_actionstep_QueryParamMapping, core_actionstep_Item, core_actionstep_Heavyweight, core_actionstep_OutputParameter, SafletScript, core_actionstep_Finally, ScriptScope, SafletScriptFactory, ScriptScopeFactory, core_scripting_SafletScriptFactory, core_scripting_SafletScript, core_scripting_SafletScriptEnvironment, core_scripting_RhinoScriptScope, core_scripting_RhinoScriptScopeFactory, core_scripting_ScriptScope, core_scripting_RhinoSafletScript, core_scripting_RhinoSafletScriptEnvironment, SafletScriptEnvironment, core_scripting_RhinoSafletScriptFactory, core_saflet_Saflet, Initiator, core_scripting_ScriptScopeFactory, SafletEnvironment, SafletContext, Finally, core_saflet_SafletContext, saflet_core_Variable, core_saflet_SafletEnvironment, core_initiator_Initiator, core_initiator_InitiatorInfo, core_call_SafiCall, core_call_CallConsumer1, core_call_CallConsumer2, CallConsumer1, core_call_CallSource1, SafiCall, core_call_CallSource2, CallSource1, DynamicValueType, OutputType, DebugLevel, InputType},
    associations={saflet1, defaultOutput2, outputs0, errorOutput4, value7, variableName8, dynamicValue11, value17, inputs13, outputParameters14, choices16, payload20, data21, booleanExpression23, targetSafletPath31, target25, parent26, scriptText29, message33, logFilename35, connection42, connection38, connection39, query41, value45, parameter47, query57, query49, query52, rowsUpdatedVar54, variableName65, resultSet59, resultSet61, resultSet63, resultSet71, column68, value80, columnMappings73, resultSet75, column77, resultSet83, columnMappings85, resultSet87, resultSet96, resultSet89, rowNum91, resultSet94, resultSet98, resultSet100, resultSet102, resultSet104, column111, variableName106, column108, query118, value113, connection116, sql129, paramMappings121, resultSet123, rowsUpdatedVar126, parentActionStep137, queryParam132, value134, targetActionStep139, sharedSafletScript142, sharedScriptScope143, safletScriptFactory145, scriptScopeFactory147, safletScript149, initiator156, scriptScope151, globalScriptScope153, safletScope159, actionsteps162, scriptingEnvironment165, safletEnvironment167, safletContext157, finally169, parentSaflet171, variables173, newCall2176, call1178, call2180, newCall1175},
    generalizations={gen_core_actionstep_ActionStep_ProductIdentifiable, gen_core_actionstep_ActionStep_ThreadSensitive, gen_core_actionstep_ActionStep_PlatformDisposition, gen_core_actionstep_Assignment_ActionStep, gen_core_actionstep_CaseItem_Item, gen_core_actionstep_InputItem_CaseItem, gen_core_actionstep_ParameterizedActionstep_ActionStep, gen_core_actionstep_ParameterizedInitiator_initiator_Initiator, gen_core_actionstep_ParameterizedInitiator_actionstep_ParameterizedActionstep, gen_core_actionstep_Choice_ActionStep, gen_core_actionstep_DynamicValue_ThreadSensitive, gen_core_actionstep_IfThen_ActionStep, gen_core_actionstep_ExecuteScript_ActionStep, gen_core_actionstep_InvokeSaflet_ActionStep, gen_core_actionstep_OpenDBConnection_actionstep_ActionStep, gen_core_actionstep_DebugLog_ActionStep, gen_core_actionstep_OpenDBConnection_actionstep_Heavyweight, gen_core_actionstep_CloseDBConnection_ActionStep, gen_core_actionstep_OpenQuery_ActionStep, gen_core_actionstep_SetQueryParam_ActionStep, gen_core_actionstep_ExecuteUpdate_ActionStep, gen_core_actionstep_ExecuteQuery_actionstep_ActionStep, gen_core_actionstep_ExecuteQuery_actionstep_Heavyweight, gen_core_actionstep_NextRow_ActionStep, gen_core_actionstep_GetColValue_ActionStep, gen_core_actionstep_GetColValues_ActionStep, gen_core_actionstep_SetColValue_ActionStep, gen_core_actionstep_MoveToRow_ActionStep, gen_core_actionstep_SetColValues_ActionStep, gen_core_actionstep_UpdatetRow_actionstep_ActionStep, gen_core_actionstep_UpdatetRow_actionstep_Heavyweight, gen_core_actionstep_DeleteRow_ActionStep, gen_core_actionstep_MoveToLastRow_ActionStep, gen_core_actionstep_MoveToInsertRow_ActionStep, gen_core_actionstep_InsertRow_ActionStep, gen_core_actionstep_MoveToFirstRow_ActionStep, gen_core_actionstep_PreviousRow_ActionStep, gen_core_actionstep_DBConnectionId_ThreadSensitive, gen_core_actionstep_DBQueryId_ThreadSensitive, gen_core_actionstep_DBResultSetId_ThreadSensitive, gen_core_actionstep_GetColMapping_Item, gen_core_actionstep_SetColMapping_Item, gen_core_actionstep_RunQuery_actionstep_ActionStep, gen_core_actionstep_RunQuery_actionstep_Heavyweight, gen_core_actionstep_QueryParamMapping_Item, gen_core_actionstep_Item_ThreadSensitive, gen_core_actionstep_OutputParameter_InputItem, gen_core_actionstep_Finally_ActionStep, gen_core_scripting_RhinoScriptScope_ScriptScope, gen_core_scripting_RhinoScriptScopeFactory_ScriptScopeFactory, gen_core_scripting_RhinoSafletScript_SafletScript, gen_core_scripting_RhinoSafletScriptEnvironment_SafletScriptEnvironment, gen_core_scripting_RhinoSafletScriptFactory_SafletScriptFactory, gen_core_saflet_Saflet_ThreadSensitive, gen_core_saflet_Saflet_PlatformDisposition, gen_core_saflet_SafletContext_ThreadSensitive, gen_core_saflet_SafletEnvironment_ThreadSensitive, gen_core_initiator_Initiator_ActionStep, gen_core_call_SafiCall_ThreadSensitive, gen_core_call_SafiCall_PlatformDisposition, gen_core_call_CallConsumer2_CallConsumer1, gen_core_call_CallSource2_CallSource1},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)