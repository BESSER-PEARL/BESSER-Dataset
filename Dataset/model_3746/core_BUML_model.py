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
OutputType: Enumeration = Enumeration(
    name="OutputType",
    literals={
            EnumerationLiteral(name="Default"),
			EnumerationLiteral(name="Error"),
			EnumerationLiteral(name="Choice")
    }
)

DynamicValueType: Enumeration = Enumeration(
    name="DynamicValueType",
    literals={
            EnumerationLiteral(name="LiteralText"),
			EnumerationLiteral(name="ScriptText"),
			EnumerationLiteral(name="VariableName"),
			EnumerationLiteral(name="Custom")
    }
)

DebugLevel: Enumeration = Enumeration(
    name="DebugLevel",
    literals={
            EnumerationLiteral(name="Debug"),
			EnumerationLiteral(name="Warn"),
			EnumerationLiteral(name="Error"),
			EnumerationLiteral(name="Info")
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
ProductIdentifiable = Class(name="ProductIdentifiable")
ThreadSensitive = Class(name="ThreadSensitive")
PlatformDisposition = Class(name="PlatformDisposition")
Output = Class(name="Output")
Saflet = Class(name="Saflet")
core_ProductIdentifiable = Class(name="core_ProductIdentifiable", is_abstract=True)
core_ThreadSensitive = Class(name="core_ThreadSensitive")
core_PlatformDisposition = Class(name="core_PlatformDisposition", is_abstract=True)
core_actionstep_ActionStep = Class(name="core_actionstep_ActionStep", is_abstract=True)
core_actionstep_CaseItem = Class(name="core_actionstep_CaseItem")
Item = Class(name="Item")
core_actionstep_InputItem = Class(name="core_actionstep_InputItem")
CaseItem = Class(name="CaseItem")
core_actionstep_ParameterizedActionstep = Class(name="core_actionstep_ParameterizedActionstep", is_abstract=True)
InputItem = Class(name="InputItem")
OutputParameter = Class(name="OutputParameter")
core_actionstep_ParameterizedInitiator = Class(name="core_actionstep_ParameterizedInitiator", is_abstract=True)
initiator_Initiator = Class(name="initiator_Initiator")
actionstep_ParameterizedActionstep = Class(name="actionstep_ParameterizedActionstep")
core_actionstep_Assignment = Class(name="core_actionstep_Assignment")
ActionStep = Class(name="ActionStep")
DynamicValue = Class(name="DynamicValue")
core_actionstep_IfThen = Class(name="core_actionstep_IfThen")
core_actionstep_Output = Class(name="core_actionstep_Output")
core_actionstep_Choice = Class(name="core_actionstep_Choice")
core_actionstep_DynamicValue = Class(name="core_actionstep_DynamicValue")
actionstep_core_EObject = Class(name="actionstep_core_EObject")
actionstep_core_EStringToStringMapEntry = Class(name="actionstep_core_EStringToStringMapEntry")
core_actionstep_OpenDBConnection = Class(name="core_actionstep_OpenDBConnection")
actionstep_ActionStep = Class(name="actionstep_ActionStep")
actionstep_Heavyweight = Class(name="actionstep_Heavyweight")
DBConnectionId = Class(name="DBConnectionId")
core_actionstep_ExecuteScript = Class(name="core_actionstep_ExecuteScript")
core_actionstep_InvokeSaflet = Class(name="core_actionstep_InvokeSaflet")
core_actionstep_DebugLog = Class(name="core_actionstep_DebugLog")
core_actionstep_SetQueryParam = Class(name="core_actionstep_SetQueryParam")
DBQueryParamId = Class(name="DBQueryParamId")
core_actionstep_ExecuteUpdate = Class(name="core_actionstep_ExecuteUpdate")
core_actionstep_CloseDBConnection = Class(name="core_actionstep_CloseDBConnection")
core_actionstep_OpenQuery = Class(name="core_actionstep_OpenQuery")
DBQueryId = Class(name="DBQueryId")
core_actionstep_GetColValues = Class(name="core_actionstep_GetColValues")
GetColMapping = Class(name="GetColMapping")
core_actionstep_SetColValue = Class(name="core_actionstep_SetColValue")
core_actionstep_ExecuteQuery = Class(name="core_actionstep_ExecuteQuery")
DBResultSetId = Class(name="DBResultSetId")
core_actionstep_NextRow = Class(name="core_actionstep_NextRow")
core_actionstep_GetColValue = Class(name="core_actionstep_GetColValue")
core_actionstep_SetColValues = Class(name="core_actionstep_SetColValues")
SetColMapping = Class(name="SetColMapping")
core_actionstep_UpdatetRow = Class(name="core_actionstep_UpdatetRow")
core_actionstep_MoveToRow = Class(name="core_actionstep_MoveToRow")
core_actionstep_MoveToInsertRow = Class(name="core_actionstep_MoveToInsertRow")
core_actionstep_InsertRow = Class(name="core_actionstep_InsertRow")
core_actionstep_MoveToFirstRow = Class(name="core_actionstep_MoveToFirstRow")
core_actionstep_PreviousRow = Class(name="core_actionstep_PreviousRow")
core_actionstep_DBConnectionId = Class(name="core_actionstep_DBConnectionId")
core_actionstep_DBQueryId = Class(name="core_actionstep_DBQueryId")
core_actionstep_MoveToLastRow = Class(name="core_actionstep_MoveToLastRow")
core_actionstep_DeleteRow = Class(name="core_actionstep_DeleteRow")
core_actionstep_SetColMapping = Class(name="core_actionstep_SetColMapping")
core_actionstep_DBQueryParamId = Class(name="core_actionstep_DBQueryParamId")
core_actionstep_DBResultSetId = Class(name="core_actionstep_DBResultSetId")
core_actionstep_GetColMapping = Class(name="core_actionstep_GetColMapping")
core_actionstep_RunQuery = Class(name="core_actionstep_RunQuery")
QueryParamMapping = Class(name="QueryParamMapping")
core_actionstep_QueryParamMapping = Class(name="core_actionstep_QueryParamMapping")
core_actionstep_Item = Class(name="core_actionstep_Item")
core_scripting_SafletScriptEnvironment = Class(name="core_scripting_SafletScriptEnvironment", is_abstract=True)
SafletScript = Class(name="SafletScript")
ScriptScope = Class(name="ScriptScope")
SafletScriptFactory = Class(name="SafletScriptFactory")
ScriptScopeFactory = Class(name="ScriptScopeFactory")
core_scripting_SafletScriptFactory = Class(name="core_scripting_SafletScriptFactory", is_abstract=True)
core_scripting_RhinoSafletScript = Class(name="core_scripting_RhinoSafletScript")
core_scripting_RhinoSafletScriptEnvironment = Class(name="core_scripting_RhinoSafletScriptEnvironment")
SafletScriptEnvironment = Class(name="SafletScriptEnvironment")
core_scripting_RhinoSafletScriptFactory = Class(name="core_scripting_RhinoSafletScriptFactory")
core_scripting_RhinoScriptScope = Class(name="core_scripting_RhinoScriptScope")
core_scripting_RhinoScriptScopeFactory = Class(name="core_scripting_RhinoScriptScopeFactory")
core_scripting_ScriptScope = Class(name="core_scripting_ScriptScope", is_abstract=True)
core_actionstep_Heavyweight = Class(name="core_actionstep_Heavyweight", is_abstract=True)
core_actionstep_OutputParameter = Class(name="core_actionstep_OutputParameter")
core_actionstep_Finally = Class(name="core_actionstep_Finally")
core_scripting_SafletScript = Class(name="core_scripting_SafletScript", is_abstract=True)
Initiator = Class(name="Initiator")
SafletContext = Class(name="SafletContext")
core_scripting_ScriptScopeFactory = Class(name="core_scripting_ScriptScopeFactory", is_abstract=True)
core_saflet_Saflet = Class(name="core_saflet_Saflet", is_abstract=True)
saflet_core_Variable = Class(name="saflet_core_Variable")
core_saflet_SafletEnvironment = Class(name="core_saflet_SafletEnvironment", is_abstract=True)
SafletEnvironment = Class(name="SafletEnvironment")
Finally = Class(name="Finally")
core_saflet_SafletContext = Class(name="core_saflet_SafletContext", is_abstract=True)
core_call_SafiCall = Class(name="core_call_SafiCall", is_abstract=True)
core_call_CallSource1 = Class(name="core_call_CallSource1", is_abstract=True)
SafiCall = Class(name="SafiCall")
core_call_CallSource2 = Class(name="core_call_CallSource2", is_abstract=True)
CallSource1 = Class(name="CallSource1")
core_call_CallConsumer1 = Class(name="core_call_CallConsumer1", is_abstract=True)
core_call_CallConsumer2 = Class(name="core_call_CallConsumer2", is_abstract=True)
CallConsumer1 = Class(name="CallConsumer1")
core_initiator_Initiator = Class(name="core_initiator_Initiator", is_abstract=True)
core_initiator_InitiatorInfo = Class(name="core_initiator_InitiatorInfo", is_abstract=True)

# ProductIdentifiable class attributes and methods

# ThreadSensitive class attributes and methods

# PlatformDisposition class attributes and methods

# Output class attributes and methods

# Saflet class attributes and methods

# core_ProductIdentifiable class attributes and methods
core_ProductIdentifiable_productId: Property = Property(name="productId", type=StringType)
core_ProductIdentifiable.attributes={core_ProductIdentifiable_productId}

# core_ThreadSensitive class attributes and methods
core_ThreadSensitive_m_cleanup: Method = Method(name="cleanup", parameters={})
core_ThreadSensitive.methods={core_ThreadSensitive_m_cleanup}

# core_PlatformDisposition class attributes and methods
core_PlatformDisposition_platformID: Property = Property(name="platformID", type=StringType)
core_PlatformDisposition_platformDependant: Property = Property(name="platformDependant", type=BooleanType)
core_PlatformDisposition.attributes={core_PlatformDisposition_platformDependant, core_PlatformDisposition_platformID}

# core_actionstep_ActionStep class attributes and methods
core_actionstep_ActionStep_paused: Property = Property(name="paused", type=BooleanType)
core_actionstep_ActionStep_active: Property = Property(name="active", type=BooleanType)
core_actionstep_ActionStep_name: Property = Property(name="name", type=StringType)
core_actionstep_ActionStep_m_beginProcessing: Method = Method(name="beginProcessing", parameters={Parameter(name='core_context', type=StringType)})
core_actionstep_ActionStep_m_executeScript: Method = Method(name="executeScript", parameters={Parameter(name='core_scriptName', type=StringType), Parameter(name='core_scriptText', type=StringType)}, type=StringType)
core_actionstep_ActionStep_m_handleException: Method = Method(name="handleException", parameters={Parameter(name='core_context', type=StringType), Parameter(name='core_e', type=StringType)})
core_actionstep_ActionStep_m_resolveDynamicValue: Method = Method(name="resolveDynamicValue", parameters={Parameter(name='core_dynamicValue', type=StringType), Parameter(name='core_context', type=StringType)}, type=StringType)
core_actionstep_ActionStep_m_createDefaultOutputs: Method = Method(name="createDefaultOutputs", parameters={})
core_actionstep_ActionStep.attributes={core_actionstep_ActionStep_name, core_actionstep_ActionStep_paused, core_actionstep_ActionStep_active}
core_actionstep_ActionStep.methods={core_actionstep_ActionStep_m_executeScript, core_actionstep_ActionStep_m_beginProcessing, core_actionstep_ActionStep_m_handleException, core_actionstep_ActionStep_m_createDefaultOutputs, core_actionstep_ActionStep_m_resolveDynamicValue}

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

# core_actionstep_Assignment class attributes and methods

# ActionStep class attributes and methods

# DynamicValue class attributes and methods

# core_actionstep_IfThen class attributes and methods

# core_actionstep_Output class attributes and methods
core_actionstep_Output_name: Property = Property(name="name", type=StringType)
core_actionstep_Output_outputType: Property = Property(name="outputType", type=StringType)
core_actionstep_Output.attributes={core_actionstep_Output_outputType, core_actionstep_Output_name}

# core_actionstep_Choice class attributes and methods

# core_actionstep_DynamicValue class attributes and methods
core_actionstep_DynamicValue_text: Property = Property(name="text", type=StringType)
core_actionstep_DynamicValue_type: Property = Property(name="type", type=StringType)
core_actionstep_DynamicValue.attributes={core_actionstep_DynamicValue_text, core_actionstep_DynamicValue_type}

# actionstep_core_EObject class attributes and methods

# actionstep_core_EStringToStringMapEntry class attributes and methods

# core_actionstep_OpenDBConnection class attributes and methods

# actionstep_ActionStep class attributes and methods

# actionstep_Heavyweight class attributes and methods

# DBConnectionId class attributes and methods

# core_actionstep_ExecuteScript class attributes and methods

# core_actionstep_InvokeSaflet class attributes and methods
core_actionstep_InvokeSaflet_labelText: Property = Property(name="labelText", type=StringType)
core_actionstep_InvokeSaflet.attributes={core_actionstep_InvokeSaflet_labelText}

# core_actionstep_DebugLog class attributes and methods
core_actionstep_DebugLog_debugLevel: Property = Property(name="debugLevel", type=StringType)
core_actionstep_DebugLog.attributes={core_actionstep_DebugLog_debugLevel}

# core_actionstep_SetQueryParam class attributes and methods
core_actionstep_SetQueryParam_paramDatatype: Property = Property(name="paramDatatype", type=StringType)
core_actionstep_SetQueryParam.attributes={core_actionstep_SetQueryParam_paramDatatype}

# DBQueryParamId class attributes and methods

# core_actionstep_ExecuteUpdate class attributes and methods

# core_actionstep_CloseDBConnection class attributes and methods

# core_actionstep_OpenQuery class attributes and methods
core_actionstep_OpenQuery_useCache: Property = Property(name="useCache", type=BooleanType)
core_actionstep_OpenQuery_scrollable: Property = Property(name="scrollable", type=BooleanType)
core_actionstep_OpenQuery_readOnly: Property = Property(name="readOnly", type=BooleanType)
core_actionstep_OpenQuery_scrollMode: Property = Property(name="scrollMode", type=StringType)
core_actionstep_OpenQuery_holdabilityMode: Property = Property(name="holdabilityMode", type=StringType)
core_actionstep_OpenQuery.attributes={core_actionstep_OpenQuery_scrollMode, core_actionstep_OpenQuery_scrollable, core_actionstep_OpenQuery_readOnly, core_actionstep_OpenQuery_holdabilityMode, core_actionstep_OpenQuery_useCache}

# DBQueryId class attributes and methods

# core_actionstep_GetColValues class attributes and methods

# GetColMapping class attributes and methods

# core_actionstep_SetColValue class attributes and methods
core_actionstep_SetColValue_setAsDatatype: Property = Property(name="setAsDatatype", type=StringType)
core_actionstep_SetColValue.attributes={core_actionstep_SetColValue_setAsDatatype}

# core_actionstep_ExecuteQuery class attributes and methods
core_actionstep_ExecuteQuery_resultSetName: Property = Property(name="resultSetName", type=StringType)
core_actionstep_ExecuteQuery.attributes={core_actionstep_ExecuteQuery_resultSetName}

# DBResultSetId class attributes and methods

# core_actionstep_NextRow class attributes and methods

# core_actionstep_GetColValue class attributes and methods
core_actionstep_GetColValue_getAsDatatype: Property = Property(name="getAsDatatype", type=StringType)
core_actionstep_GetColValue.attributes={core_actionstep_GetColValue_getAsDatatype}

# core_actionstep_SetColValues class attributes and methods

# SetColMapping class attributes and methods

# core_actionstep_UpdatetRow class attributes and methods

# core_actionstep_MoveToRow class attributes and methods

# core_actionstep_MoveToInsertRow class attributes and methods

# core_actionstep_InsertRow class attributes and methods

# core_actionstep_MoveToFirstRow class attributes and methods

# core_actionstep_PreviousRow class attributes and methods

# core_actionstep_DBConnectionId class attributes and methods
core_actionstep_DBConnectionId_id: Property = Property(name="id", type=StringType)
core_actionstep_DBConnectionId_jdbcConnection: Property = Property(name="jdbcConnection", type=StringType)
core_actionstep_DBConnectionId.attributes={core_actionstep_DBConnectionId_jdbcConnection, core_actionstep_DBConnectionId_id}

# core_actionstep_DBQueryId class attributes and methods
core_actionstep_DBQueryId_id: Property = Property(name="id", type=StringType)
core_actionstep_DBQueryId_jdbcStatement: Property = Property(name="jdbcStatement", type=StringType)
core_actionstep_DBQueryId.attributes={core_actionstep_DBQueryId_id, core_actionstep_DBQueryId_jdbcStatement}

# core_actionstep_MoveToLastRow class attributes and methods

# core_actionstep_DeleteRow class attributes and methods

# core_actionstep_SetColMapping class attributes and methods
core_actionstep_SetColMapping_setAsDatatype: Property = Property(name="setAsDatatype", type=StringType)
core_actionstep_SetColMapping.attributes={core_actionstep_SetColMapping_setAsDatatype}

# core_actionstep_DBQueryParamId class attributes and methods
core_actionstep_DBQueryParamId_id: Property = Property(name="id", type=StringType)
core_actionstep_DBQueryParamId_index: Property = Property(name="index", type=IntegerType)
core_actionstep_DBQueryParamId.attributes={core_actionstep_DBQueryParamId_id, core_actionstep_DBQueryParamId_index}

# core_actionstep_DBResultSetId class attributes and methods
core_actionstep_DBResultSetId_name: Property = Property(name="name", type=StringType)
core_actionstep_DBResultSetId_id: Property = Property(name="id", type=StringType)
core_actionstep_DBResultSetId_jDBCResultSet: Property = Property(name="jDBCResultSet", type=StringType)
core_actionstep_DBResultSetId.attributes={core_actionstep_DBResultSetId_jDBCResultSet, core_actionstep_DBResultSetId_name, core_actionstep_DBResultSetId_id}

# core_actionstep_GetColMapping class attributes and methods
core_actionstep_GetColMapping_getAsDatatype: Property = Property(name="getAsDatatype", type=StringType)
core_actionstep_GetColMapping.attributes={core_actionstep_GetColMapping_getAsDatatype}

# core_actionstep_RunQuery class attributes and methods
core_actionstep_RunQuery_resultSetName: Property = Property(name="resultSetName", type=StringType)
core_actionstep_RunQuery_scrollable: Property = Property(name="scrollable", type=BooleanType)
core_actionstep_RunQuery_readOnly: Property = Property(name="readOnly", type=BooleanType)
core_actionstep_RunQuery_m_refreshParams: Method = Method(name="refreshParams", parameters={Parameter(name='core_qry', type=StringType)})
core_actionstep_RunQuery.attributes={core_actionstep_RunQuery_readOnly, core_actionstep_RunQuery_resultSetName, core_actionstep_RunQuery_scrollable}
core_actionstep_RunQuery.methods={core_actionstep_RunQuery_m_refreshParams}

# QueryParamMapping class attributes and methods

# core_actionstep_QueryParamMapping class attributes and methods
core_actionstep_QueryParamMapping_setAsDatatype: Property = Property(name="setAsDatatype", type=StringType)
core_actionstep_QueryParamMapping.attributes={core_actionstep_QueryParamMapping_setAsDatatype}

# core_actionstep_Item class attributes and methods
core_actionstep_Item_labelText: Property = Property(name="labelText", type=StringType)
core_actionstep_Item.attributes={core_actionstep_Item_labelText}

# core_scripting_SafletScriptEnvironment class attributes and methods

# SafletScript class attributes and methods

# ScriptScope class attributes and methods

# SafletScriptFactory class attributes and methods

# ScriptScopeFactory class attributes and methods

# core_scripting_SafletScriptFactory class attributes and methods
core_scripting_SafletScriptFactory_m_getSafletScript: Method = Method(name="getSafletScript", parameters={Parameter(name='core_scriptText', type=StringType), Parameter(name='core_name', type=StringType)}, type=StringType)
core_scripting_SafletScriptFactory.methods={core_scripting_SafletScriptFactory_m_getSafletScript}

# core_scripting_RhinoSafletScript class attributes and methods
core_scripting_RhinoSafletScript_rhinoScript: Property = Property(name="rhinoScript", type=StringType)
core_scripting_RhinoSafletScript.attributes={core_scripting_RhinoSafletScript_rhinoScript}

# core_scripting_RhinoSafletScriptEnvironment class attributes and methods

# SafletScriptEnvironment class attributes and methods

# core_scripting_RhinoSafletScriptFactory class attributes and methods

# core_scripting_RhinoScriptScope class attributes and methods

# core_scripting_RhinoScriptScopeFactory class attributes and methods

# core_scripting_ScriptScope class attributes and methods
core_scripting_ScriptScope_scopeObject: Property = Property(name="scopeObject", type=StringType)
core_scripting_ScriptScope_m_exposeObjectToScript: Method = Method(name="exposeObjectToScript", parameters={Parameter(name='core_name', type=StringType), Parameter(name='core_value', type=StringType)})
core_scripting_ScriptScope_m_removeObjectFromScope: Method = Method(name="removeObjectFromScope", parameters={Parameter(name='core_name', type=StringType)})
core_scripting_ScriptScope_m_getScopedObject: Method = Method(name="getScopedObject", parameters={Parameter(name='core_name', type=StringType)}, type=StringType)
core_scripting_ScriptScope_m_updateVariablesFromScope: Method = Method(name="updateVariablesFromScope", parameters={Parameter(name='core_safletEnvironment', type=StringType), Parameter(name='core_isDebug', type=StringType), Parameter(name='core_variables', type=StringType)})
core_scripting_ScriptScope.attributes={core_scripting_ScriptScope_scopeObject}
core_scripting_ScriptScope.methods={core_scripting_ScriptScope_m_updateVariablesFromScope, core_scripting_ScriptScope_m_getScopedObject, core_scripting_ScriptScope_m_exposeObjectToScript, core_scripting_ScriptScope_m_removeObjectFromScope}

# core_actionstep_Heavyweight class attributes and methods

# core_actionstep_OutputParameter class attributes and methods

# core_actionstep_Finally class attributes and methods

# core_scripting_SafletScript class attributes and methods
core_scripting_SafletScript_name: Property = Property(name="name", type=StringType)
core_scripting_SafletScript_scriptText: Property = Property(name="scriptText", type=StringType)
core_scripting_SafletScript_m_execute: Method = Method(name="execute", parameters={Parameter(name='core_scope', type=StringType)}, type=StringType)
core_scripting_SafletScript.attributes={core_scripting_SafletScript_name, core_scripting_SafletScript_scriptText}
core_scripting_SafletScript.methods={core_scripting_SafletScript_m_execute}

# Initiator class attributes and methods

# SafletContext class attributes and methods

# core_scripting_ScriptScopeFactory class attributes and methods

# core_saflet_Saflet class attributes and methods
core_saflet_Saflet_active: Property = Property(name="active", type=BooleanType)
core_saflet_Saflet_name: Property = Property(name="name", type=StringType)
core_saflet_Saflet_version: Property = Property(name="version", type=StringType)
core_saflet_Saflet_description: Property = Property(name="description", type=StringType)
core_saflet_Saflet_id: Property = Property(name="id", type=IntegerType)
core_saflet_Saflet_m_getActionStep: Method = Method(name="getActionStep", parameters={Parameter(name='core_name', type=StringType)}, type=StringType)
core_saflet_Saflet_m_addActionStep: Method = Method(name="addActionStep", parameters={Parameter(name='core_actionstep', type=StringType)})
core_saflet_Saflet_m_getScript: Method = Method(name="getScript", parameters={Parameter(name='core_name', type=StringType)}, type=StringType)
core_saflet_Saflet_m_addScript: Method = Method(name="addScript", parameters={Parameter(name='core_name', type=StringType), Parameter(name='core_scriptText', type=StringType)}, type=StringType)
core_saflet_Saflet_m_initializeScriptableObjects: Method = Method(name="initializeScriptableObjects", parameters={})
core_saflet_Saflet_m_init: Method = Method(name="init", parameters={})
core_saflet_Saflet.attributes={core_saflet_Saflet_name, core_saflet_Saflet_active, core_saflet_Saflet_id, core_saflet_Saflet_version, core_saflet_Saflet_description}
core_saflet_Saflet.methods={core_saflet_Saflet_m_addActionStep, core_saflet_Saflet_m_addScript, core_saflet_Saflet_m_getActionStep, core_saflet_Saflet_m_getScript, core_saflet_Saflet_m_initializeScriptableObjects, core_saflet_Saflet_m_init}

# saflet_core_Variable class attributes and methods

# core_saflet_SafletEnvironment class attributes and methods
core_saflet_SafletEnvironment_m_getSaflet: Method = Method(name="getSaflet", parameters={Parameter(name='core_path', type=StringType), Parameter(name='core_coreServerId', type=StringType)}, type=StringType)
core_saflet_SafletEnvironment_m_getGlobalExecutor: Method = Method(name="getGlobalExecutor", parameters={}, type=StringType)
core_saflet_SafletEnvironment_m_getGlobalVariableValue: Method = Method(name="getGlobalVariableValue", parameters={Parameter(name='core_name', type=StringType)}, type=StringType)
core_saflet_SafletEnvironment_m_setGlobalVariableValue: Method = Method(name="setGlobalVariableValue", parameters={Parameter(name='core_value', type=StringType), Parameter(name='core_name', type=StringType)})
core_saflet_SafletEnvironment_m_getGlobalVariable: Method = Method(name="getGlobalVariable", parameters={Parameter(name='core_name', type=StringType)}, type=StringType)
core_saflet_SafletEnvironment.methods={core_saflet_SafletEnvironment_m_setGlobalVariableValue, core_saflet_SafletEnvironment_m_getGlobalVariableValue, core_saflet_SafletEnvironment_m_getGlobalExecutor, core_saflet_SafletEnvironment_m_getSaflet, core_saflet_SafletEnvironment_m_getGlobalVariable}

# SafletEnvironment class attributes and methods

# Finally class attributes and methods

# core_saflet_SafletContext class attributes and methods
core_saflet_SafletContext_exceptions: Property = Property(name="exceptions", type=StringType)
core_saflet_SafletContext_sessionVariables: Property = Property(name="sessionVariables", type=StringType)
core_saflet_SafletContext_m_getVariableRawValue: Method = Method(name="getVariableRawValue", parameters={Parameter(name='core_name', type=StringType)}, type=StringType)
core_saflet_SafletContext_m_setVariableRawValue: Method = Method(name="setVariableRawValue", parameters={Parameter(name='core_value', type=StringType), Parameter(name='core_name', type=StringType)})
core_saflet_SafletContext_m_addOrUpdateVariable: Method = Method(name="addOrUpdateVariable", parameters={Parameter(name='core_v', type=StringType)})
core_saflet_SafletContext_m_removeVariable: Method = Method(name="removeVariable", parameters={Parameter(name='core_name', type=StringType)}, type=StringType)
core_saflet_SafletContext_m_addException: Method = Method(name="addException", parameters={Parameter(name='core_e', type=StringType)})
core_saflet_SafletContext_m_merge: Method = Method(name="merge", parameters={Parameter(name='core_context', type=StringType)})
core_saflet_SafletContext_m_getSessionVar: Method = Method(name="getSessionVar", parameters={Parameter(name='core_name', type=StringType)}, type=StringType)
core_saflet_SafletContext_m_setSessionVar: Method = Method(name="setSessionVar", parameters={Parameter(name='core_name', type=StringType), Parameter(name='core_value', type=StringType)})
core_saflet_SafletContext_m_preHandoffPrep: Method = Method(name="preHandoffPrep", parameters={Parameter(name='core_call', type=StringType)})
core_saflet_SafletContext_m_init: Method = Method(name="init", parameters={})
core_saflet_SafletContext_m_getVariable: Method = Method(name="getVariable", parameters={Parameter(name='core_name', type=StringType)}, type=StringType)
core_saflet_SafletContext.attributes={core_saflet_SafletContext_exceptions, core_saflet_SafletContext_sessionVariables}
core_saflet_SafletContext.methods={core_saflet_SafletContext_m_init, core_saflet_SafletContext_m_merge, core_saflet_SafletContext_m_preHandoffPrep, core_saflet_SafletContext_m_removeVariable, core_saflet_SafletContext_m_setSessionVar, core_saflet_SafletContext_m_getVariable, core_saflet_SafletContext_m_addOrUpdateVariable, core_saflet_SafletContext_m_getVariableRawValue, core_saflet_SafletContext_m_setVariableRawValue, core_saflet_SafletContext_m_getSessionVar, core_saflet_SafletContext_m_addException}

# core_call_SafiCall class attributes and methods
core_call_SafiCall_uuid: Property = Property(name="uuid", type=StringType)
core_call_SafiCall_name: Property = Property(name="name", type=StringType)
core_call_SafiCall.attributes={core_call_SafiCall_uuid, core_call_SafiCall_name}

# core_call_CallSource1 class attributes and methods

# SafiCall class attributes and methods

# core_call_CallSource2 class attributes and methods

# CallSource1 class attributes and methods

# core_call_CallConsumer1 class attributes and methods

# core_call_CallConsumer2 class attributes and methods

# CallConsumer1 class attributes and methods

# core_initiator_Initiator class attributes and methods
core_initiator_Initiator_m_acceptsRequest: Method = Method(name="acceptsRequest", parameters={Parameter(name='core_context', type=StringType)}, type=BooleanType)
core_initiator_Initiator_m_initialize: Method = Method(name="initialize", parameters={Parameter(name='core_context', type=StringType)})
core_initiator_Initiator_m_beginProcessing: Method = Method(name="beginProcessing", parameters={})
core_initiator_Initiator.methods={core_initiator_Initiator_m_initialize, core_initiator_Initiator_m_acceptsRequest, core_initiator_Initiator_m_beginProcessing}

# core_initiator_InitiatorInfo class attributes and methods

# Relationships
outputs0: BinaryAssociation = BinaryAssociation(
    name="outputs0",
    ends={
        Property(name="Output", type=core_actionstep_ActionStep, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=Output, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
saflet1: BinaryAssociation = BinaryAssociation(
    name="saflet1",
    ends={
        Property(name="Saflet", type=core_actionstep_ActionStep, multiplicity=Multiplicity(1, 1)),
        Property(name="actionsteps", type=Saflet, multiplicity=Multiplicity(0, 1))
    }
)
dynamicValue11: BinaryAssociation = BinaryAssociation(
    name="dynamicValue11",
    ends={
        Property(name="DynamicValue12", type=core_actionstep_CaseItem, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_CaseItem", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
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
defaultOutput2: BinaryAssociation = BinaryAssociation(
    name="defaultOutput2",
    ends={
        Property(name="Output3", type=core_actionstep_ActionStep, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_ActionStep", type=Output, multiplicity=Multiplicity(0, 1))
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
booleanExpression23: BinaryAssociation = BinaryAssociation(
    name="booleanExpression23",
    ends={
        Property(name="DynamicValue24", type=core_actionstep_IfThen, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_IfThen", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
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
        Property(name="ActionStep27", type=core_actionstep_Output, multiplicity=Multiplicity(1, 1)),
        Property(name="outputs", type=ActionStep, multiplicity=Multiplicity(0, 1))
    }
)
choices16: BinaryAssociation = BinaryAssociation(
    name="choices16",
    ends={
        Property(name="CaseItem", type=core_actionstep_Choice, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_Choice", type=CaseItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value17: BinaryAssociation = BinaryAssociation(
    name="value17",
    ends={
        Property(name="DynamicValue19", type=core_actionstep_Choice, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_Choice18", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
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
message32: BinaryAssociation = BinaryAssociation(
    name="message32",
    ends={
        Property(name="DynamicValue33", type=core_actionstep_DebugLog, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_DebugLog", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
logFilename34: BinaryAssociation = BinaryAssociation(
    name="logFilename34",
    ends={
        Property(name="DynamicValue36", type=core_actionstep_DebugLog, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_DebugLog35", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
connection37: BinaryAssociation = BinaryAssociation(
    name="connection37",
    ends={
        Property(name="DBConnectionId", type=core_actionstep_OpenDBConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_OpenDBConnection", type=DBConnectionId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scriptText28: BinaryAssociation = BinaryAssociation(
    name="scriptText28",
    ends={
        Property(name="DynamicValue29", type=core_actionstep_ExecuteScript, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_ExecuteScript", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetSafletPath30: BinaryAssociation = BinaryAssociation(
    name="targetSafletPath30",
    ends={
        Property(name="DynamicValue31", type=core_actionstep_InvokeSaflet, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_InvokeSaflet", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value44: BinaryAssociation = BinaryAssociation(
    name="value44",
    ends={
        Property(name="DynamicValue45", type=core_actionstep_SetQueryParam, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_SetQueryParam", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter46: BinaryAssociation = BinaryAssociation(
    name="parameter46",
    ends={
        Property(name="DBQueryParamId", type=core_actionstep_SetQueryParam, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_SetQueryParam47", type=DBQueryParamId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
query48: BinaryAssociation = BinaryAssociation(
    name="query48",
    ends={
        Property(name="DBQueryId50", type=core_actionstep_SetQueryParam, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_SetQueryParam49", type=DBQueryId, multiplicity=Multiplicity(0, 1))
    }
)
query51: BinaryAssociation = BinaryAssociation(
    name="query51",
    ends={
        Property(name="DBQueryId52", type=core_actionstep_ExecuteUpdate, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_ExecuteUpdate", type=DBQueryId, multiplicity=Multiplicity(0, 1))
    }
)
rowsUpdatedVar53: BinaryAssociation = BinaryAssociation(
    name="rowsUpdatedVar53",
    ends={
        Property(name="DynamicValue55", type=core_actionstep_ExecuteUpdate, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_ExecuteUpdate54", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
connection38: BinaryAssociation = BinaryAssociation(
    name="connection38",
    ends={
        Property(name="DBConnectionId39", type=core_actionstep_CloseDBConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_CloseDBConnection", type=DBConnectionId, multiplicity=Multiplicity(0, 1))
    }
)
query40: BinaryAssociation = BinaryAssociation(
    name="query40",
    ends={
        Property(name="DBQueryId", type=core_actionstep_OpenQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_OpenQuery", type=DBQueryId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
connection41: BinaryAssociation = BinaryAssociation(
    name="connection41",
    ends={
        Property(name="DBConnectionId43", type=core_actionstep_OpenQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_OpenQuery42", type=DBConnectionId, multiplicity=Multiplicity(0, 1))
    }
)
resultSet62: BinaryAssociation = BinaryAssociation(
    name="resultSet62",
    ends={
        Property(name="DBResultSetId63", type=core_actionstep_GetColValue, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_GetColValue", type=DBResultSetId, multiplicity=Multiplicity(0, 1))
    }
)
variableName64: BinaryAssociation = BinaryAssociation(
    name="variableName64",
    ends={
        Property(name="DynamicValue66", type=core_actionstep_GetColValue, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_GetColValue65", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
column67: BinaryAssociation = BinaryAssociation(
    name="column67",
    ends={
        Property(name="DynamicValue69", type=core_actionstep_GetColValue, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_GetColValue68", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resultSet70: BinaryAssociation = BinaryAssociation(
    name="resultSet70",
    ends={
        Property(name="DBResultSetId71", type=core_actionstep_GetColValues, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_GetColValues", type=DBResultSetId, multiplicity=Multiplicity(0, 1))
    }
)
columnMappings72: BinaryAssociation = BinaryAssociation(
    name="columnMappings72",
    ends={
        Property(name="GetColMapping", type=core_actionstep_GetColValues, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_GetColValues73", type=GetColMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resultSet74: BinaryAssociation = BinaryAssociation(
    name="resultSet74",
    ends={
        Property(name="DBResultSetId75", type=core_actionstep_SetColValue, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_SetColValue", type=DBResultSetId, multiplicity=Multiplicity(0, 1))
    }
)
query56: BinaryAssociation = BinaryAssociation(
    name="query56",
    ends={
        Property(name="DBQueryId57", type=core_actionstep_ExecuteQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_ExecuteQuery", type=DBQueryId, multiplicity=Multiplicity(0, 1))
    }
)
resultSet58: BinaryAssociation = BinaryAssociation(
    name="resultSet58",
    ends={
        Property(name="DBResultSetId", type=core_actionstep_ExecuteQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_ExecuteQuery59", type=DBResultSetId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resultSet60: BinaryAssociation = BinaryAssociation(
    name="resultSet60",
    ends={
        Property(name="DBResultSetId61", type=core_actionstep_NextRow, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_NextRow", type=DBResultSetId, multiplicity=Multiplicity(0, 1))
    }
)
resultSet82: BinaryAssociation = BinaryAssociation(
    name="resultSet82",
    ends={
        Property(name="DBResultSetId83", type=core_actionstep_SetColValues, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_SetColValues", type=DBResultSetId, multiplicity=Multiplicity(0, 1))
    }
)
columnMappings84: BinaryAssociation = BinaryAssociation(
    name="columnMappings84",
    ends={
        Property(name="SetColMapping", type=core_actionstep_SetColValues, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_SetColValues85", type=SetColMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resultSet86: BinaryAssociation = BinaryAssociation(
    name="resultSet86",
    ends={
        Property(name="DBResultSetId87", type=core_actionstep_UpdatetRow, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_UpdatetRow", type=DBResultSetId, multiplicity=Multiplicity(0, 1))
    }
)
resultSet88: BinaryAssociation = BinaryAssociation(
    name="resultSet88",
    ends={
        Property(name="DBResultSetId89", type=core_actionstep_MoveToRow, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_MoveToRow", type=DBResultSetId, multiplicity=Multiplicity(0, 1))
    }
)
rowNum90: BinaryAssociation = BinaryAssociation(
    name="rowNum90",
    ends={
        Property(name="DynamicValue92", type=core_actionstep_MoveToRow, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_MoveToRow91", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
column76: BinaryAssociation = BinaryAssociation(
    name="column76",
    ends={
        Property(name="DynamicValue78", type=core_actionstep_SetColValue, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_SetColValue77", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value79: BinaryAssociation = BinaryAssociation(
    name="value79",
    ends={
        Property(name="DynamicValue81", type=core_actionstep_SetColValue, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_SetColValue80", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resultSet95: BinaryAssociation = BinaryAssociation(
    name="resultSet95",
    ends={
        Property(name="DBResultSetId96", type=core_actionstep_DeleteRow, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_DeleteRow", type=DBResultSetId, multiplicity=Multiplicity(0, 1))
    }
)
resultSet97: BinaryAssociation = BinaryAssociation(
    name="resultSet97",
    ends={
        Property(name="DBResultSetId98", type=core_actionstep_MoveToInsertRow, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_MoveToInsertRow", type=DBResultSetId, multiplicity=Multiplicity(0, 1))
    }
)
resultSet99: BinaryAssociation = BinaryAssociation(
    name="resultSet99",
    ends={
        Property(name="DBResultSetId100", type=core_actionstep_InsertRow, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_InsertRow", type=DBResultSetId, multiplicity=Multiplicity(0, 1))
    }
)
resultSet101: BinaryAssociation = BinaryAssociation(
    name="resultSet101",
    ends={
        Property(name="DBResultSetId102", type=core_actionstep_MoveToFirstRow, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_MoveToFirstRow", type=DBResultSetId, multiplicity=Multiplicity(0, 1))
    }
)
resultSet103: BinaryAssociation = BinaryAssociation(
    name="resultSet103",
    ends={
        Property(name="DBResultSetId104", type=core_actionstep_PreviousRow, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_PreviousRow", type=DBResultSetId, multiplicity=Multiplicity(0, 1))
    }
)
resultSet93: BinaryAssociation = BinaryAssociation(
    name="resultSet93",
    ends={
        Property(name="DBResultSetId94", type=core_actionstep_MoveToLastRow, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_MoveToLastRow", type=DBResultSetId, multiplicity=Multiplicity(0, 1))
    }
)
column107: BinaryAssociation = BinaryAssociation(
    name="column107",
    ends={
        Property(name="DynamicValue109", type=core_actionstep_GetColMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_GetColMapping108", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
column110: BinaryAssociation = BinaryAssociation(
    name="column110",
    ends={
        Property(name="DynamicValue111", type=core_actionstep_SetColMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_SetColMapping", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableName105: BinaryAssociation = BinaryAssociation(
    name="variableName105",
    ends={
        Property(name="DynamicValue106", type=core_actionstep_GetColMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_GetColMapping", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value112: BinaryAssociation = BinaryAssociation(
    name="value112",
    ends={
        Property(name="DynamicValue114", type=core_actionstep_SetColMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_SetColMapping113", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
connection115: BinaryAssociation = BinaryAssociation(
    name="connection115",
    ends={
        Property(name="DBConnectionId116", type=core_actionstep_RunQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_RunQuery", type=DBConnectionId, multiplicity=Multiplicity(0, 1))
    }
)
query117: BinaryAssociation = BinaryAssociation(
    name="query117",
    ends={
        Property(name="DBQueryId119", type=core_actionstep_RunQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_RunQuery118", type=DBQueryId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
paramMappings120: BinaryAssociation = BinaryAssociation(
    name="paramMappings120",
    ends={
        Property(name="QueryParamMapping", type=core_actionstep_RunQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_RunQuery121", type=QueryParamMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sql128: BinaryAssociation = BinaryAssociation(
    name="sql128",
    ends={
        Property(name="DynamicValue130", type=core_actionstep_RunQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_RunQuery129", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
queryParam131: BinaryAssociation = BinaryAssociation(
    name="queryParam131",
    ends={
        Property(name="DBQueryParamId132", type=core_actionstep_QueryParamMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_QueryParamMapping", type=DBQueryParamId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value133: BinaryAssociation = BinaryAssociation(
    name="value133",
    ends={
        Property(name="DynamicValue135", type=core_actionstep_QueryParamMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_QueryParamMapping134", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parentActionStep136: BinaryAssociation = BinaryAssociation(
    name="parentActionStep136",
    ends={
        Property(name="ActionStep137", type=core_actionstep_Item, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_Item", type=ActionStep, multiplicity=Multiplicity(0, 1))
    }
)
targetActionStep138: BinaryAssociation = BinaryAssociation(
    name="targetActionStep138",
    ends={
        Property(name="ActionStep140", type=core_actionstep_Item, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_Item139", type=ActionStep, multiplicity=Multiplicity(0, 1))
    }
)
resultSet122: BinaryAssociation = BinaryAssociation(
    name="resultSet122",
    ends={
        Property(name="DBResultSetId124", type=core_actionstep_RunQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_RunQuery123", type=DBResultSetId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rowsUpdatedVar125: BinaryAssociation = BinaryAssociation(
    name="rowsUpdatedVar125",
    ends={
        Property(name="DynamicValue127", type=core_actionstep_RunQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="core_actionstep_RunQuery126", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sharedSafletScript141: BinaryAssociation = BinaryAssociation(
    name="sharedSafletScript141",
    ends={
        Property(name="SafletScript", type=core_scripting_SafletScriptEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="core_scripting_SafletScriptEnvironment", type=SafletScript, multiplicity=Multiplicity(0, 1))
    }
)
sharedScriptScope142: BinaryAssociation = BinaryAssociation(
    name="sharedScriptScope142",
    ends={
        Property(name="ScriptScope", type=core_scripting_SafletScriptEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="core_scripting_SafletScriptEnvironment143", type=ScriptScope, multiplicity=Multiplicity(0, 1))
    }
)
safletScriptFactory144: BinaryAssociation = BinaryAssociation(
    name="safletScriptFactory144",
    ends={
        Property(name="SafletScriptFactory", type=core_scripting_SafletScriptEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="core_scripting_SafletScriptEnvironment145", type=SafletScriptFactory, multiplicity=Multiplicity(0, 1))
    }
)
scriptScopeFactory146: BinaryAssociation = BinaryAssociation(
    name="scriptScopeFactory146",
    ends={
        Property(name="ScriptScopeFactory", type=core_scripting_SafletScriptEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="core_scripting_SafletScriptEnvironment147", type=ScriptScopeFactory, multiplicity=Multiplicity(0, 1))
    }
)
safletScript148: BinaryAssociation = BinaryAssociation(
    name="safletScript148",
    ends={
        Property(name="SafletScript149", type=core_scripting_SafletScriptFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="core_scripting_SafletScriptFactory", type=SafletScript, multiplicity=Multiplicity(0, 1))
    }
)
initiator155: BinaryAssociation = BinaryAssociation(
    name="initiator155",
    ends={
        Property(name="Initiator", type=core_saflet_Saflet, multiplicity=Multiplicity(1, 1)),
        Property(name="core_saflet_Saflet", type=Initiator, multiplicity=Multiplicity(0, 1))
    }
)
safletContext156: BinaryAssociation = BinaryAssociation(
    name="safletContext156",
    ends={
        Property(name="SafletContext", type=core_saflet_Saflet, multiplicity=Multiplicity(1, 1)),
        Property(name="core_saflet_Saflet157", type=SafletContext, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
safletScope158: BinaryAssociation = BinaryAssociation(
    name="safletScope158",
    ends={
        Property(name="ScriptScope160", type=core_saflet_Saflet, multiplicity=Multiplicity(1, 1)),
        Property(name="core_saflet_Saflet159", type=ScriptScope, multiplicity=Multiplicity(0, 1))
    }
)
actionsteps161: BinaryAssociation = BinaryAssociation(
    name="actionsteps161",
    ends={
        Property(name="ActionStep162", type=core_saflet_Saflet, multiplicity=Multiplicity(1, 1)),
        Property(name="saflet", type=ActionStep, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scriptScope150: BinaryAssociation = BinaryAssociation(
    name="scriptScope150",
    ends={
        Property(name="ScriptScope151", type=core_scripting_ScriptScopeFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="core_scripting_ScriptScopeFactory", type=ScriptScope, multiplicity=Multiplicity(0, 1))
    }
)
globalScriptScope152: BinaryAssociation = BinaryAssociation(
    name="globalScriptScope152",
    ends={
        Property(name="ScriptScope154", type=core_scripting_ScriptScopeFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="core_scripting_ScriptScopeFactory153", type=ScriptScope, multiplicity=Multiplicity(0, 1))
    }
)
parentSaflet169: BinaryAssociation = BinaryAssociation(
    name="parentSaflet169",
    ends={
        Property(name="Saflet170", type=core_saflet_SafletContext, multiplicity=Multiplicity(1, 1)),
        Property(name="core_saflet_SafletContext", type=Saflet, multiplicity=Multiplicity(0, 1))
    }
)
variables171: BinaryAssociation = BinaryAssociation(
    name="variables171",
    ends={
        Property(name="saflet_core_Variable", type=core_saflet_SafletContext, multiplicity=Multiplicity(1, 1)),
        Property(name="core_saflet_SafletContext172", type=saflet_core_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scriptingEnvironment163: BinaryAssociation = BinaryAssociation(
    name="scriptingEnvironment163",
    ends={
        Property(name="SafletScriptEnvironment", type=core_saflet_Saflet, multiplicity=Multiplicity(1, 1)),
        Property(name="core_saflet_Saflet164", type=SafletScriptEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
safletEnvironment165: BinaryAssociation = BinaryAssociation(
    name="safletEnvironment165",
    ends={
        Property(name="SafletEnvironment", type=core_saflet_Saflet, multiplicity=Multiplicity(1, 1)),
        Property(name="core_saflet_Saflet166", type=SafletEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
finally_167: BinaryAssociation = BinaryAssociation(
    name="finally_167",
    ends={
        Property(name="Finally", type=core_saflet_Saflet, multiplicity=Multiplicity(1, 1)),
        Property(name="core_saflet_Saflet168", type=Finally, multiplicity=Multiplicity(0, 1))
    }
)
newCall1173: BinaryAssociation = BinaryAssociation(
    name="newCall1173",
    ends={
        Property(name="SafiCall", type=core_call_CallSource1, multiplicity=Multiplicity(1, 1)),
        Property(name="core_call_CallSource1", type=SafiCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
newCall2174: BinaryAssociation = BinaryAssociation(
    name="newCall2174",
    ends={
        Property(name="SafiCall175", type=core_call_CallSource2, multiplicity=Multiplicity(1, 1)),
        Property(name="core_call_CallSource2", type=SafiCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
call1176: BinaryAssociation = BinaryAssociation(
    name="call1176",
    ends={
        Property(name="SafiCall177", type=core_call_CallConsumer1, multiplicity=Multiplicity(1, 1)),
        Property(name="core_call_CallConsumer1", type=SafiCall, multiplicity=Multiplicity(0, 1))
    }
)
call2178: BinaryAssociation = BinaryAssociation(
    name="call2178",
    ends={
        Property(name="SafiCall179", type=core_call_CallConsumer2, multiplicity=Multiplicity(1, 1)),
        Property(name="core_call_CallConsumer2", type=SafiCall, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_core_actionstep_ActionStep_ProductIdentifiable = Generalization(general=ProductIdentifiable, specific=core_actionstep_ActionStep)
gen_core_actionstep_ActionStep_ThreadSensitive = Generalization(general=ThreadSensitive, specific=core_actionstep_ActionStep)
gen_core_actionstep_ActionStep_PlatformDisposition = Generalization(general=PlatformDisposition, specific=core_actionstep_ActionStep)
gen_core_actionstep_CaseItem_Item = Generalization(general=Item, specific=core_actionstep_CaseItem)
gen_core_actionstep_InputItem_CaseItem = Generalization(general=CaseItem, specific=core_actionstep_InputItem)
gen_core_actionstep_ParameterizedActionstep_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_ParameterizedActionstep)
gen_core_actionstep_ParameterizedInitiator_initiator_Initiator = Generalization(general=initiator_Initiator, specific=core_actionstep_ParameterizedInitiator)
gen_core_actionstep_ParameterizedInitiator_actionstep_ParameterizedActionstep = Generalization(general=actionstep_ParameterizedActionstep, specific=core_actionstep_ParameterizedInitiator)
gen_core_actionstep_Assignment_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_Assignment)
gen_core_actionstep_IfThen_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_IfThen)
gen_core_actionstep_Choice_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_Choice)
gen_core_actionstep_DynamicValue_ThreadSensitive = Generalization(general=ThreadSensitive, specific=core_actionstep_DynamicValue)
gen_core_actionstep_OpenDBConnection_actionstep_ActionStep = Generalization(general=actionstep_ActionStep, specific=core_actionstep_OpenDBConnection)
gen_core_actionstep_OpenDBConnection_actionstep_Heavyweight = Generalization(general=actionstep_Heavyweight, specific=core_actionstep_OpenDBConnection)
gen_core_actionstep_ExecuteScript_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_ExecuteScript)
gen_core_actionstep_InvokeSaflet_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_InvokeSaflet)
gen_core_actionstep_DebugLog_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_DebugLog)
gen_core_actionstep_SetQueryParam_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_SetQueryParam)
gen_core_actionstep_ExecuteUpdate_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_ExecuteUpdate)
gen_core_actionstep_CloseDBConnection_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_CloseDBConnection)
gen_core_actionstep_OpenQuery_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_OpenQuery)
gen_core_actionstep_GetColValues_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_GetColValues)
gen_core_actionstep_SetColValue_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_SetColValue)
gen_core_actionstep_ExecuteQuery_actionstep_ActionStep = Generalization(general=actionstep_ActionStep, specific=core_actionstep_ExecuteQuery)
gen_core_actionstep_ExecuteQuery_actionstep_Heavyweight = Generalization(general=actionstep_Heavyweight, specific=core_actionstep_ExecuteQuery)
gen_core_actionstep_NextRow_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_NextRow)
gen_core_actionstep_GetColValue_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_GetColValue)
gen_core_actionstep_SetColValues_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_SetColValues)
gen_core_actionstep_UpdatetRow_actionstep_ActionStep = Generalization(general=actionstep_ActionStep, specific=core_actionstep_UpdatetRow)
gen_core_actionstep_UpdatetRow_actionstep_Heavyweight = Generalization(general=actionstep_Heavyweight, specific=core_actionstep_UpdatetRow)
gen_core_actionstep_MoveToRow_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_MoveToRow)
gen_core_actionstep_MoveToInsertRow_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_MoveToInsertRow)
gen_core_actionstep_InsertRow_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_InsertRow)
gen_core_actionstep_MoveToFirstRow_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_MoveToFirstRow)
gen_core_actionstep_PreviousRow_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_PreviousRow)
gen_core_actionstep_DBConnectionId_ThreadSensitive = Generalization(general=ThreadSensitive, specific=core_actionstep_DBConnectionId)
gen_core_actionstep_DBQueryId_ThreadSensitive = Generalization(general=ThreadSensitive, specific=core_actionstep_DBQueryId)
gen_core_actionstep_MoveToLastRow_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_MoveToLastRow)
gen_core_actionstep_DeleteRow_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_DeleteRow)
gen_core_actionstep_SetColMapping_Item = Generalization(general=Item, specific=core_actionstep_SetColMapping)
gen_core_actionstep_DBResultSetId_ThreadSensitive = Generalization(general=ThreadSensitive, specific=core_actionstep_DBResultSetId)
gen_core_actionstep_GetColMapping_Item = Generalization(general=Item, specific=core_actionstep_GetColMapping)
gen_core_actionstep_RunQuery_actionstep_ActionStep = Generalization(general=actionstep_ActionStep, specific=core_actionstep_RunQuery)
gen_core_actionstep_RunQuery_actionstep_Heavyweight = Generalization(general=actionstep_Heavyweight, specific=core_actionstep_RunQuery)
gen_core_actionstep_QueryParamMapping_Item = Generalization(general=Item, specific=core_actionstep_QueryParamMapping)
gen_core_actionstep_Item_ThreadSensitive = Generalization(general=ThreadSensitive, specific=core_actionstep_Item)
gen_core_scripting_RhinoSafletScript_SafletScript = Generalization(general=SafletScript, specific=core_scripting_RhinoSafletScript)
gen_core_scripting_RhinoSafletScriptEnvironment_SafletScriptEnvironment = Generalization(general=SafletScriptEnvironment, specific=core_scripting_RhinoSafletScriptEnvironment)
gen_core_scripting_RhinoSafletScriptFactory_SafletScriptFactory = Generalization(general=SafletScriptFactory, specific=core_scripting_RhinoSafletScriptFactory)
gen_core_scripting_RhinoScriptScope_ScriptScope = Generalization(general=ScriptScope, specific=core_scripting_RhinoScriptScope)
gen_core_scripting_RhinoScriptScopeFactory_ScriptScopeFactory = Generalization(general=ScriptScopeFactory, specific=core_scripting_RhinoScriptScopeFactory)
gen_core_actionstep_OutputParameter_InputItem = Generalization(general=InputItem, specific=core_actionstep_OutputParameter)
gen_core_actionstep_Finally_ActionStep = Generalization(general=ActionStep, specific=core_actionstep_Finally)
gen_core_saflet_Saflet_ThreadSensitive = Generalization(general=ThreadSensitive, specific=core_saflet_Saflet)
gen_core_saflet_Saflet_PlatformDisposition = Generalization(general=PlatformDisposition, specific=core_saflet_Saflet)
gen_core_saflet_SafletEnvironment_ThreadSensitive = Generalization(general=ThreadSensitive, specific=core_saflet_SafletEnvironment)
gen_core_saflet_SafletContext_ThreadSensitive = Generalization(general=ThreadSensitive, specific=core_saflet_SafletContext)
gen_core_call_SafiCall_ThreadSensitive = Generalization(general=ThreadSensitive, specific=core_call_SafiCall)
gen_core_call_SafiCall_PlatformDisposition = Generalization(general=PlatformDisposition, specific=core_call_SafiCall)
gen_core_call_CallSource2_CallSource1 = Generalization(general=CallSource1, specific=core_call_CallSource2)
gen_core_call_CallConsumer2_CallConsumer1 = Generalization(general=CallConsumer1, specific=core_call_CallConsumer2)
gen_core_initiator_Initiator_ActionStep = Generalization(general=ActionStep, specific=core_initiator_Initiator)

# Domain Model
domain_model = DomainModel(
    name="core",
    types={ProductIdentifiable, ThreadSensitive, PlatformDisposition, Output, Saflet, core_ProductIdentifiable, core_ThreadSensitive, core_PlatformDisposition, core_actionstep_ActionStep, core_actionstep_CaseItem, Item, core_actionstep_InputItem, CaseItem, core_actionstep_ParameterizedActionstep, InputItem, OutputParameter, core_actionstep_ParameterizedInitiator, initiator_Initiator, actionstep_ParameterizedActionstep, core_actionstep_Assignment, ActionStep, DynamicValue, core_actionstep_IfThen, core_actionstep_Output, core_actionstep_Choice, core_actionstep_DynamicValue, actionstep_core_EObject, actionstep_core_EStringToStringMapEntry, core_actionstep_OpenDBConnection, actionstep_ActionStep, actionstep_Heavyweight, DBConnectionId, core_actionstep_ExecuteScript, core_actionstep_InvokeSaflet, core_actionstep_DebugLog, core_actionstep_SetQueryParam, DBQueryParamId, core_actionstep_ExecuteUpdate, core_actionstep_CloseDBConnection, core_actionstep_OpenQuery, DBQueryId, core_actionstep_GetColValues, GetColMapping, core_actionstep_SetColValue, core_actionstep_ExecuteQuery, DBResultSetId, core_actionstep_NextRow, core_actionstep_GetColValue, core_actionstep_SetColValues, SetColMapping, core_actionstep_UpdatetRow, core_actionstep_MoveToRow, core_actionstep_MoveToInsertRow, core_actionstep_InsertRow, core_actionstep_MoveToFirstRow, core_actionstep_PreviousRow, core_actionstep_DBConnectionId, core_actionstep_DBQueryId, core_actionstep_MoveToLastRow, core_actionstep_DeleteRow, core_actionstep_SetColMapping, core_actionstep_DBQueryParamId, core_actionstep_DBResultSetId, core_actionstep_GetColMapping, core_actionstep_RunQuery, QueryParamMapping, core_actionstep_QueryParamMapping, core_actionstep_Item, core_scripting_SafletScriptEnvironment, SafletScript, ScriptScope, SafletScriptFactory, ScriptScopeFactory, core_scripting_SafletScriptFactory, core_scripting_RhinoSafletScript, core_scripting_RhinoSafletScriptEnvironment, SafletScriptEnvironment, core_scripting_RhinoSafletScriptFactory, core_scripting_RhinoScriptScope, core_scripting_RhinoScriptScopeFactory, core_scripting_ScriptScope, core_actionstep_Heavyweight, core_actionstep_OutputParameter, core_actionstep_Finally, core_scripting_SafletScript, Initiator, SafletContext, core_scripting_ScriptScopeFactory, core_saflet_Saflet, saflet_core_Variable, core_saflet_SafletEnvironment, SafletEnvironment, Finally, core_saflet_SafletContext, core_call_SafiCall, core_call_CallSource1, SafiCall, core_call_CallSource2, CallSource1, core_call_CallConsumer1, core_call_CallConsumer2, CallConsumer1, core_initiator_Initiator, core_initiator_InitiatorInfo, OutputType, DynamicValueType, DebugLevel, InputType},
    associations={outputs0, saflet1, dynamicValue11, inputs13, outputParameters14, defaultOutput2, errorOutput4, value7, variableName8, booleanExpression23, target25, parent26, choices16, value17, payload20, data21, message32, logFilename34, connection37, scriptText28, targetSafletPath30, value44, parameter46, query48, query51, rowsUpdatedVar53, connection38, query40, connection41, resultSet62, variableName64, column67, resultSet70, columnMappings72, resultSet74, query56, resultSet58, resultSet60, resultSet82, columnMappings84, resultSet86, resultSet88, rowNum90, column76, value79, resultSet95, resultSet97, resultSet99, resultSet101, resultSet103, resultSet93, column107, column110, variableName105, value112, connection115, query117, paramMappings120, sql128, queryParam131, value133, parentActionStep136, targetActionStep138, resultSet122, rowsUpdatedVar125, sharedSafletScript141, sharedScriptScope142, safletScriptFactory144, scriptScopeFactory146, safletScript148, initiator155, safletContext156, safletScope158, actionsteps161, scriptScope150, globalScriptScope152, parentSaflet169, variables171, scriptingEnvironment163, safletEnvironment165, finally_167, newCall1173, newCall2174, call1176, call2178},
    generalizations={gen_core_actionstep_ActionStep_ProductIdentifiable, gen_core_actionstep_ActionStep_ThreadSensitive, gen_core_actionstep_ActionStep_PlatformDisposition, gen_core_actionstep_CaseItem_Item, gen_core_actionstep_InputItem_CaseItem, gen_core_actionstep_ParameterizedActionstep_ActionStep, gen_core_actionstep_ParameterizedInitiator_initiator_Initiator, gen_core_actionstep_ParameterizedInitiator_actionstep_ParameterizedActionstep, gen_core_actionstep_Assignment_ActionStep, gen_core_actionstep_IfThen_ActionStep, gen_core_actionstep_Choice_ActionStep, gen_core_actionstep_DynamicValue_ThreadSensitive, gen_core_actionstep_OpenDBConnection_actionstep_ActionStep, gen_core_actionstep_OpenDBConnection_actionstep_Heavyweight, gen_core_actionstep_ExecuteScript_ActionStep, gen_core_actionstep_InvokeSaflet_ActionStep, gen_core_actionstep_DebugLog_ActionStep, gen_core_actionstep_SetQueryParam_ActionStep, gen_core_actionstep_ExecuteUpdate_ActionStep, gen_core_actionstep_CloseDBConnection_ActionStep, gen_core_actionstep_OpenQuery_ActionStep, gen_core_actionstep_GetColValues_ActionStep, gen_core_actionstep_SetColValue_ActionStep, gen_core_actionstep_ExecuteQuery_actionstep_ActionStep, gen_core_actionstep_ExecuteQuery_actionstep_Heavyweight, gen_core_actionstep_NextRow_ActionStep, gen_core_actionstep_GetColValue_ActionStep, gen_core_actionstep_SetColValues_ActionStep, gen_core_actionstep_UpdatetRow_actionstep_ActionStep, gen_core_actionstep_UpdatetRow_actionstep_Heavyweight, gen_core_actionstep_MoveToRow_ActionStep, gen_core_actionstep_MoveToInsertRow_ActionStep, gen_core_actionstep_InsertRow_ActionStep, gen_core_actionstep_MoveToFirstRow_ActionStep, gen_core_actionstep_PreviousRow_ActionStep, gen_core_actionstep_DBConnectionId_ThreadSensitive, gen_core_actionstep_DBQueryId_ThreadSensitive, gen_core_actionstep_MoveToLastRow_ActionStep, gen_core_actionstep_DeleteRow_ActionStep, gen_core_actionstep_SetColMapping_Item, gen_core_actionstep_DBResultSetId_ThreadSensitive, gen_core_actionstep_GetColMapping_Item, gen_core_actionstep_RunQuery_actionstep_ActionStep, gen_core_actionstep_RunQuery_actionstep_Heavyweight, gen_core_actionstep_QueryParamMapping_Item, gen_core_actionstep_Item_ThreadSensitive, gen_core_scripting_RhinoSafletScript_SafletScript, gen_core_scripting_RhinoSafletScriptEnvironment_SafletScriptEnvironment, gen_core_scripting_RhinoSafletScriptFactory_SafletScriptFactory, gen_core_scripting_RhinoScriptScope_ScriptScope, gen_core_scripting_RhinoScriptScopeFactory_ScriptScopeFactory, gen_core_actionstep_OutputParameter_InputItem, gen_core_actionstep_Finally_ActionStep, gen_core_saflet_Saflet_ThreadSensitive, gen_core_saflet_Saflet_PlatformDisposition, gen_core_saflet_SafletEnvironment_ThreadSensitive, gen_core_saflet_SafletContext_ThreadSensitive, gen_core_call_SafiCall_ThreadSensitive, gen_core_call_SafiCall_PlatformDisposition, gen_core_call_CallSource2_CallSource1, gen_core_call_CallConsumer2_CallConsumer1, gen_core_initiator_Initiator_ActionStep},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)