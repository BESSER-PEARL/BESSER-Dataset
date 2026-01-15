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
FIELD_FORMAT: Enumeration = Enumeration(
    name="FIELD_FORMAT",
    literals={
            EnumerationLiteral(name="AU"),
			EnumerationLiteral(name="BMP"),
			EnumerationLiteral(name="JPEG"),
			EnumerationLiteral(name="MJPEG"),
			EnumerationLiteral(name="MPEG1"),
			EnumerationLiteral(name="MPEG2"),
			EnumerationLiteral(name="MP2"),
			EnumerationLiteral(name="MP3"),
			EnumerationLiteral(name="MP4"),
			EnumerationLiteral(name="RAW"),
			EnumerationLiteral(name="WAV"),
			EnumerationLiteral(name="JAUS_MESSAGE"),
			EnumerationLiteral(name="XML"),
			EnumerationLiteral(name="RNC"),
			EnumerationLiteral(name="RNG"),
			EnumerationLiteral(name="XSD"),
			EnumerationLiteral(name="USER_DEFINED")
    }
)

UNIT: Enumeration = Enumeration(
    name="UNIT",
    literals={
            EnumerationLiteral(name="CUBIC_METER"),
			EnumerationLiteral(name="METER_PER_SEC"),
			EnumerationLiteral(name="METER_PER_SEC_SQR"),
			EnumerationLiteral(name="RECIPROCAL_METER"),
			EnumerationLiteral(name="KG_PER_CUBIC_METER"),
			EnumerationLiteral(name="CUBICMETERPERKG"),
			EnumerationLiteral(name="AMPPERSQRMETER"),
			EnumerationLiteral(name="AMP_PER_METER"),
			EnumerationLiteral(name="MOLE_PER_CUBIC_METER"),
			EnumerationLiteral(name="CANDELA_PER_SQUARE_METER"),
			EnumerationLiteral(name="RADIAN"),
			EnumerationLiteral(name="STE_RAD"),
			EnumerationLiteral(name="HRZ"),
			EnumerationLiteral(name="NEWTON"),
			EnumerationLiteral(name="PASCAL"),
			EnumerationLiteral(name="JOULE"),
			EnumerationLiteral(name="WATT"),
			EnumerationLiteral(name="COULOMB"),
			EnumerationLiteral(name="VOLT"),
			EnumerationLiteral(name="FARAD"),
			EnumerationLiteral(name="OHM"),
			EnumerationLiteral(name="SIEMENS"),
			EnumerationLiteral(name="WEBER"),
			EnumerationLiteral(name="TESLA"),
			EnumerationLiteral(name="HENRY"),
			EnumerationLiteral(name="CELSIUS"),
			EnumerationLiteral(name="LUMEN"),
			EnumerationLiteral(name="LUX"),
			EnumerationLiteral(name="BECQUEREL"),
			EnumerationLiteral(name="SIEVERT"),
			EnumerationLiteral(name="KATAL"),
			EnumerationLiteral(name="PASCAL_SEC"),
			EnumerationLiteral(name="NEWTON_METER"),
			EnumerationLiteral(name="NEWTON_PER_METER"),
			EnumerationLiteral(name="RAD_PER_SEC"),
			EnumerationLiteral(name="RAD_PER_SEC_SQR"),
			EnumerationLiteral(name="WATT_PER_SQR_METER"),
			EnumerationLiteral(name="JOULE_PER_KELVIN"),
			EnumerationLiteral(name="METER"),
			EnumerationLiteral(name="KG"),
			EnumerationLiteral(name="SEC"),
			EnumerationLiteral(name="AMP"),
			EnumerationLiteral(name="KELVIN"),
			EnumerationLiteral(name="MOLE"),
			EnumerationLiteral(name="CANDELA"),
			EnumerationLiteral(name="ONE"),
			EnumerationLiteral(name="SQR_METER"),
			EnumerationLiteral(name="GRAY_PER_SEC"),
			EnumerationLiteral(name="WATT_PER_SQR_METER_STERAD"),
			EnumerationLiteral(name="KATAL_PER_CUBIC_METER"),
			EnumerationLiteral(name="MIN"),
			EnumerationLiteral(name="HOUR"),
			EnumerationLiteral(name="DAY"),
			EnumerationLiteral(name="DEGREE"),
			EnumerationLiteral(name="LTR"),
			EnumerationLiteral(name="MTON"),
			EnumerationLiteral(name="NEPER"),
			EnumerationLiteral(name="BEL"),
			EnumerationLiteral(name="NMILE"),
			EnumerationLiteral(name="KNOT"),
			EnumerationLiteral(name="ARE"),
			EnumerationLiteral(name="HECTARE"),
			EnumerationLiteral(name="BAR"),
			EnumerationLiteral(name="ANGSROM"),
			EnumerationLiteral(name="BARN"),
			EnumerationLiteral(name="CURIE"),
			EnumerationLiteral(name="ROENTGEN"),
			EnumerationLiteral(name="RAD"),
			EnumerationLiteral(name="REM"),
			EnumerationLiteral(name="JOULE_PER_KG"),
			EnumerationLiteral(name="WATT_PER_METER_KELVIN"),
			EnumerationLiteral(name="JOULES_PER_CUBIC_METER"),
			EnumerationLiteral(name="VOLT_PER_METER"),
			EnumerationLiteral(name="COULOMB_PER_CUBIC_METER"),
			EnumerationLiteral(name="COULOMB_PER_SQR_METER"),
			EnumerationLiteral(name="FARAD_PER_METER"),
			EnumerationLiteral(name="HENRY_PER_METER"),
			EnumerationLiteral(name="JOULE_PER_MOLE"),
			EnumerationLiteral(name="JOULE_PER_MOLE_KELVIN"),
			EnumerationLiteral(name="COULOMB_PER_KG")
    }
)

# Classes
cjsidl_declaredTypeSet = Class(name="cjsidl::declaredTypeSet")
cjsidl_messageSet = Class(name="cjsidl::messageSet")
cjsidl_internalEventSet = Class(name="cjsidl::internalEventSet")
cjsidl_protocolBehavior = Class(name="cjsidl::protocolBehavior")
cjsidl_jaus = Class(name="cjsidl::jaus")
cjsidl_EObject = Class(name="cjsidl::EObject")
cjsidl_serviceDef = Class(name="cjsidl::serviceDef")
cjsidl_description = Class(name="cjsidl::description")
cjsidl_references = Class(name="cjsidl::references")
cjsidl_declaredConstSet = Class(name="cjsidl::declaredConstSet")
cjsidl_scopedTypeId = Class(name="cjsidl::scopedTypeId")
cjsidl_messages = Class(name="cjsidl::messages")
cjsidl_refAttr = Class(name="cjsidl::refAttr")
cjsidl_declaredConstSetRef = Class(name="cjsidl::declaredConstSetRef")
cjsidl_constDef = Class(name="cjsidl::constDef")
cjsidl_declaredTypeSetRef = Class(name="cjsidl::declaredTypeSetRef")
cjsidl_typeDef = Class(name="cjsidl::typeDef")
cjsidl_typeReference = Class(name="cjsidl::typeReference")
cjsidl_state = Class(name="cjsidl::state")
cjsidl_messageDef = Class(name="cjsidl::messageDef")
cjsidl_messageRef = Class(name="cjsidl::messageRef")
cjsidl_messageScopedRef = Class(name="cjsidl::messageScopedRef")
cjsidl_eventDef = Class(name="cjsidl::eventDef")
cjsidl_stateMachine = Class(name="cjsidl::stateMachine")
cjsidl_startState = Class(name="cjsidl::startState")
cjsidl_transParams = Class(name="cjsidl::transParams")
cjsidl_transParam = Class(name="cjsidl::transParam")
cjsidl_defaultState = Class(name="cjsidl::defaultState")
cjsidl_entry = Class(name="cjsidl::entry")
cjsidl_exit = Class(name="cjsidl::exit")
cjsidl_transition = Class(name="cjsidl::transition")
cjsidl_defaultTransition = Class(name="cjsidl::defaultTransition")
cjsidl_actionList = Class(name="cjsidl::actionList")
cjsidl_sendActionList = Class(name="cjsidl::sendActionList")
cjsidl_internalTransition = Class(name="cjsidl::internalTransition")
cjsidl_simpleTransition = Class(name="cjsidl::simpleTransition")
cjsidl_nextState = Class(name="cjsidl::nextState")
cjsidl_pushTransition = Class(name="cjsidl::pushTransition")
cjsidl_scopedEventType = Class(name="cjsidl::scopedEventType")
cjsidl_guard = Class(name="cjsidl::guard")
cjsidl_popTransition = Class(name="cjsidl::popTransition")
cjsidl_guardParam = Class(name="cjsidl::guardParam")
cjsidl_guardAction = Class(name="cjsidl::guardAction")
cjsidl_action = Class(name="cjsidl::action")
cjsidl_fixedLenString = Class(name="cjsidl::fixedLenString")
cjsidl_varLenString = Class(name="cjsidl::varLenString")
cjsidl_varLenField = Class(name="cjsidl::varLenField")
cjsidl_varFormatField = Class(name="cjsidl::varFormatField")
cjsidl_headerDef = Class(name="cjsidl::headerDef")
cjsidl_simpleNumericType = Class(name="cjsidl::simpleNumericType")
cjsidl_arrayDef = Class(name="cjsidl::arrayDef")
cjsidl_recordDef = Class(name="cjsidl::recordDef")
cjsidl_listDef = Class(name="cjsidl::listDef")
cjsidl_variantDef = Class(name="cjsidl::variantDef")
cjsidl_sequenceDef = Class(name="cjsidl::sequenceDef")
cjsidl_fixedFieldDef = Class(name="cjsidl::fixedFieldDef")
cjsidl_varField = Class(name="cjsidl::varField")
cjsidl_bitfieldDef = Class(name="cjsidl::bitfieldDef")
cjsidl_headerRef = Class(name="cjsidl::headerRef")
cjsidl_headerScopedRef = Class(name="cjsidl::headerScopedRef")
cjsidl_bodyRef = Class(name="cjsidl::bodyRef")
cjsidl_bodyScopedRef = Class(name="cjsidl::bodyScopedRef")
cjsidl_bodyDef = Class(name="cjsidl::bodyDef")
cjsidl_footerDef = Class(name="cjsidl::footerDef")
cjsidl_containerRef = Class(name="cjsidl::containerRef")
cjsidl_scopedType = Class(name="cjsidl::scopedType")
cjsidl_declaredEventDef = Class(name="cjsidl::declaredEventDef")
cjsidl_footerRef = Class(name="cjsidl::footerRef")
cjsidl_footerScopedRef = Class(name="cjsidl::footerScopedRef")
cjsidl_containerDef = Class(name="cjsidl::containerDef")
cjsidl_constReference = Class(name="cjsidl::constReference")
cjsidl_scopedConstId = Class(name="cjsidl::scopedConstId")
cjsidl_valueSetDef = Class(name="cjsidl::valueSetDef")
cjsidl_scaledRangeDef = Class(name="cjsidl::scaledRangeDef")
cjsidl_taggedUnitsEnum = Class(name="cjsidl::taggedUnitsEnum")
cjsidl_valueSpec = Class(name="cjsidl::valueSpec")
cjsidl_valueRange = Class(name="cjsidl::valueRange")
cjsidl_formatEnumDef = Class(name="cjsidl::formatEnumDef")
cjsidl_subField = Class(name="cjsidl::subField")
containerDef = Class(name="containerDef")
cjsidl_taggedItemDef = Class(name="cjsidl::taggedItemDef")

# cjsidl_declaredTypeSet class attributes and methods
cjsidl_declaredTypeSet_typeName: Property = Property(name="typeName", type=StringType)
cjsidl_declaredTypeSet_name: Property = Property(name="name", type=StringType)
cjsidl_declaredTypeSet_version: Property = Property(name="version", type=StringType)
cjsidl_declaredTypeSet.attributes={cjsidl_declaredTypeSet_version, cjsidl_declaredTypeSet_name, cjsidl_declaredTypeSet_typeName}

# cjsidl_messageSet class attributes and methods
cjsidl_messageSet_comment: Property = Property(name="comment", type=StringType)
cjsidl_messageSet_inputComment: Property = Property(name="inputComment", type=StringType)
cjsidl_messageSet_outputComment: Property = Property(name="outputComment", type=StringType)
cjsidl_messageSet.attributes={cjsidl_messageSet_comment, cjsidl_messageSet_outputComment, cjsidl_messageSet_inputComment}

# cjsidl_internalEventSet class attributes and methods
cjsidl_internalEventSet_comment: Property = Property(name="comment", type=StringType)
cjsidl_internalEventSet.attributes={cjsidl_internalEventSet_comment}

# cjsidl_protocolBehavior class attributes and methods
cjsidl_protocolBehavior_comment: Property = Property(name="comment", type=StringType)
cjsidl_protocolBehavior_stateless: Property = Property(name="stateless", type=StringType)
cjsidl_protocolBehavior.attributes={cjsidl_protocolBehavior_comment, cjsidl_protocolBehavior_stateless}

# cjsidl_jaus class attributes and methods

# cjsidl_EObject class attributes and methods

# cjsidl_serviceDef class attributes and methods
cjsidl_serviceDef_serviceName: Property = Property(name="serviceName", type=StringType)
cjsidl_serviceDef_name: Property = Property(name="name", type=StringType)
cjsidl_serviceDef_serviceVersion: Property = Property(name="serviceVersion", type=StringType)
cjsidl_serviceDef_assumpt: Property = Property(name="assumpt", type=StringType)
cjsidl_serviceDef.attributes={cjsidl_serviceDef_assumpt, cjsidl_serviceDef_name, cjsidl_serviceDef_serviceName, cjsidl_serviceDef_serviceVersion}

# cjsidl_description class attributes and methods
cjsidl_description_content: Property = Property(name="content", type=StringType)
cjsidl_description.attributes={cjsidl_description_content}

# cjsidl_references class attributes and methods

# cjsidl_declaredConstSet class attributes and methods
cjsidl_declaredConstSet_constName: Property = Property(name="constName", type=StringType)
cjsidl_declaredConstSet_name: Property = Property(name="name", type=StringType)
cjsidl_declaredConstSet_constSetVersion: Property = Property(name="constSetVersion", type=StringType)
cjsidl_declaredConstSet.attributes={cjsidl_declaredConstSet_constSetVersion, cjsidl_declaredConstSet_constName, cjsidl_declaredConstSet_name}

# cjsidl_scopedTypeId class attributes and methods
cjsidl_scopedTypeId_comment: Property = Property(name="comment", type=StringType)
cjsidl_scopedTypeId_optional: Property = Property(name="optional", type=StringType)
cjsidl_scopedTypeId_scopedName: Property = Property(name="scopedName", type=StringType)
cjsidl_scopedTypeId.attributes={cjsidl_scopedTypeId_comment, cjsidl_scopedTypeId_scopedName, cjsidl_scopedTypeId_optional}

# cjsidl_messages class attributes and methods

# cjsidl_refAttr class attributes and methods
cjsidl_refAttr_comment: Property = Property(name="comment", type=StringType)
cjsidl_refAttr_name: Property = Property(name="name", type=StringType)
cjsidl_refAttr.attributes={cjsidl_refAttr_name, cjsidl_refAttr_comment}

# cjsidl_declaredConstSetRef class attributes and methods
cjsidl_declaredConstSetRef_comment: Property = Property(name="comment", type=StringType)
cjsidl_declaredConstSetRef_name: Property = Property(name="name", type=StringType)
cjsidl_declaredConstSetRef.attributes={cjsidl_declaredConstSetRef_comment, cjsidl_declaredConstSetRef_name}

# cjsidl_constDef class attributes and methods
cjsidl_constDef_comment: Property = Property(name="comment", type=StringType)
cjsidl_constDef_name: Property = Property(name="name", type=StringType)
cjsidl_constDef_constValue: Property = Property(name="constValue", type=StringType)
cjsidl_constDef_fieldUnits: Property = Property(name="fieldUnits", type=StringType)
cjsidl_constDef.attributes={cjsidl_constDef_constValue, cjsidl_constDef_fieldUnits, cjsidl_constDef_name, cjsidl_constDef_comment}

# cjsidl_declaredTypeSetRef class attributes and methods
cjsidl_declaredTypeSetRef_comment: Property = Property(name="comment", type=StringType)
cjsidl_declaredTypeSetRef_name: Property = Property(name="name", type=StringType)
cjsidl_declaredTypeSetRef.attributes={cjsidl_declaredTypeSetRef_name, cjsidl_declaredTypeSetRef_comment}

# cjsidl_typeDef class attributes and methods

# cjsidl_typeReference class attributes and methods
cjsidl_typeReference_optional: Property = Property(name="optional", type=StringType)
cjsidl_typeReference_name: Property = Property(name="name", type=StringType)
cjsidl_typeReference_comment: Property = Property(name="comment", type=StringType)
cjsidl_typeReference.attributes={cjsidl_typeReference_comment, cjsidl_typeReference_optional, cjsidl_typeReference_name}

# cjsidl_state class attributes and methods
cjsidl_state_comment: Property = Property(name="comment", type=StringType)
cjsidl_state_initial: Property = Property(name="initial", type=StringType)
cjsidl_state_name: Property = Property(name="name", type=StringType)
cjsidl_state.attributes={cjsidl_state_initial, cjsidl_state_comment, cjsidl_state_name}

# cjsidl_messageDef class attributes and methods
cjsidl_messageDef_command: Property = Property(name="command", type=StringType)
cjsidl_messageDef_messageID: Property = Property(name="messageID", type=StringType)
cjsidl_messageDef_name: Property = Property(name="name", type=StringType)
cjsidl_messageDef.attributes={cjsidl_messageDef_name, cjsidl_messageDef_command, cjsidl_messageDef_messageID}

# cjsidl_messageRef class attributes and methods
cjsidl_messageRef_comment: Property = Property(name="comment", type=StringType)
cjsidl_messageRef_name: Property = Property(name="name", type=StringType)
cjsidl_messageRef.attributes={cjsidl_messageRef_comment, cjsidl_messageRef_name}

# cjsidl_messageScopedRef class attributes and methods
cjsidl_messageScopedRef_comment: Property = Property(name="comment", type=StringType)
cjsidl_messageScopedRef_name: Property = Property(name="name", type=StringType)
cjsidl_messageScopedRef.attributes={cjsidl_messageScopedRef_name, cjsidl_messageScopedRef_comment}

# cjsidl_eventDef class attributes and methods
cjsidl_eventDef_name: Property = Property(name="name", type=StringType)
cjsidl_eventDef.attributes={cjsidl_eventDef_name}

# cjsidl_stateMachine class attributes and methods
cjsidl_stateMachine_comment: Property = Property(name="comment", type=StringType)
cjsidl_stateMachine_name: Property = Property(name="name", type=StringType)
cjsidl_stateMachine.attributes={cjsidl_stateMachine_name, cjsidl_stateMachine_comment}

# cjsidl_startState class attributes and methods
cjsidl_startState_comment: Property = Property(name="comment", type=StringType)
cjsidl_startState.attributes={cjsidl_startState_comment}

# cjsidl_transParams class attributes and methods

# cjsidl_transParam class attributes and methods
cjsidl_transParam_comment: Property = Property(name="comment", type=StringType)
cjsidl_transParam_unsignedType: Property = Property(name="unsignedType", type=StringType)
cjsidl_transParam_name: Property = Property(name="name", type=StringType)
cjsidl_transParam.attributes={cjsidl_transParam_unsignedType, cjsidl_transParam_name, cjsidl_transParam_comment}

# cjsidl_defaultState class attributes and methods
cjsidl_defaultState_comment: Property = Property(name="comment", type=StringType)
cjsidl_defaultState.attributes={cjsidl_defaultState_comment}

# cjsidl_entry class attributes and methods
cjsidl_entry_comment: Property = Property(name="comment", type=StringType)
cjsidl_entry.attributes={cjsidl_entry_comment}

# cjsidl_exit class attributes and methods
cjsidl_exit_comment: Property = Property(name="comment", type=StringType)
cjsidl_exit.attributes={cjsidl_exit_comment}

# cjsidl_transition class attributes and methods
cjsidl_transition_comment: Property = Property(name="comment", type=StringType)
cjsidl_transition_type: Property = Property(name="type", type=StringType)
cjsidl_transition_name: Property = Property(name="name", type=StringType)
cjsidl_transition.attributes={cjsidl_transition_comment, cjsidl_transition_type, cjsidl_transition_name}

# cjsidl_defaultTransition class attributes and methods
cjsidl_defaultTransition_comment: Property = Property(name="comment", type=StringType)
cjsidl_defaultTransition_type: Property = Property(name="type", type=StringType)
cjsidl_defaultTransition.attributes={cjsidl_defaultTransition_type, cjsidl_defaultTransition_comment}

# cjsidl_actionList class attributes and methods

# cjsidl_sendActionList class attributes and methods

# cjsidl_internalTransition class attributes and methods
cjsidl_internalTransition_comment: Property = Property(name="comment", type=StringType)
cjsidl_internalTransition.attributes={cjsidl_internalTransition_comment}

# cjsidl_simpleTransition class attributes and methods
cjsidl_simpleTransition_comment: Property = Property(name="comment", type=StringType)
cjsidl_simpleTransition.attributes={cjsidl_simpleTransition_comment}

# cjsidl_nextState class attributes and methods
cjsidl_nextState_comment: Property = Property(name="comment", type=StringType)
cjsidl_nextState.attributes={cjsidl_nextState_comment}

# cjsidl_pushTransition class attributes and methods
cjsidl_pushTransition_comment: Property = Property(name="comment", type=StringType)
cjsidl_pushTransition.attributes={cjsidl_pushTransition_comment}

# cjsidl_scopedEventType class attributes and methods

# cjsidl_guard class attributes and methods
cjsidl_guard_comment: Property = Property(name="comment", type=StringType)
cjsidl_guard_equiv: Property = Property(name="equiv", type=StringType)
cjsidl_guard_logicalOperator: Property = Property(name="logicalOperator", type=StringType)
cjsidl_guard.attributes={cjsidl_guard_equiv, cjsidl_guard_logicalOperator, cjsidl_guard_comment}

# cjsidl_popTransition class attributes and methods
cjsidl_popTransition_comment: Property = Property(name="comment", type=StringType)
cjsidl_popTransition.attributes={cjsidl_popTransition_comment}

# cjsidl_guardParam class attributes and methods
cjsidl_guardParam_guardConst: Property = Property(name="guardConst", type=StringType)
cjsidl_guardParam.attributes={cjsidl_guardParam_guardConst}

# cjsidl_guardAction class attributes and methods
cjsidl_guardAction_not: Property = Property(name="not", type=StringType)
cjsidl_guardAction_name: Property = Property(name="name", type=StringType)
cjsidl_guardAction.attributes={cjsidl_guardAction_name, cjsidl_guardAction_not}

# cjsidl_action class attributes and methods
cjsidl_action_comment: Property = Property(name="comment", type=StringType)
cjsidl_action_name: Property = Property(name="name", type=StringType)
cjsidl_action.attributes={cjsidl_action_name, cjsidl_action_comment}

# cjsidl_fixedLenString class attributes and methods
cjsidl_fixedLenString_comment: Property = Property(name="comment", type=StringType)
cjsidl_fixedLenString_optional: Property = Property(name="optional", type=StringType)
cjsidl_fixedLenString_name: Property = Property(name="name", type=StringType)
cjsidl_fixedLenString_upperLim: Property = Property(name="upperLim", type=StringType)
cjsidl_fixedLenString.attributes={cjsidl_fixedLenString_upperLim, cjsidl_fixedLenString_name, cjsidl_fixedLenString_optional, cjsidl_fixedLenString_comment}

# cjsidl_varLenString class attributes and methods
cjsidl_varLenString_comment: Property = Property(name="comment", type=StringType)
cjsidl_varLenString_optional: Property = Property(name="optional", type=StringType)
cjsidl_varLenString_name: Property = Property(name="name", type=StringType)
cjsidl_varLenString_lowerLim: Property = Property(name="lowerLim", type=StringType)
cjsidl_varLenString_upperLim: Property = Property(name="upperLim", type=StringType)
cjsidl_varLenString.attributes={cjsidl_varLenString_optional, cjsidl_varLenString_upperLim, cjsidl_varLenString_comment, cjsidl_varLenString_name, cjsidl_varLenString_lowerLim}

# cjsidl_varLenField class attributes and methods
cjsidl_varLenField_comment: Property = Property(name="comment", type=StringType)
cjsidl_varLenField_optional: Property = Property(name="optional", type=StringType)
cjsidl_varLenField_fieldFormat: Property = Property(name="fieldFormat", type=StringType)
cjsidl_varLenField_name: Property = Property(name="name", type=StringType)
cjsidl_varLenField_countComment: Property = Property(name="countComment", type=StringType)
cjsidl_varLenField_lowerLim: Property = Property(name="lowerLim", type=StringType)
cjsidl_varLenField_upperLim: Property = Property(name="upperLim", type=StringType)
cjsidl_varLenField.attributes={cjsidl_varLenField_upperLim, cjsidl_varLenField_lowerLim, cjsidl_varLenField_countComment, cjsidl_varLenField_comment, cjsidl_varLenField_optional, cjsidl_varLenField_fieldFormat, cjsidl_varLenField_name}

# cjsidl_varFormatField class attributes and methods
cjsidl_varFormatField_comment: Property = Property(name="comment", type=StringType)
cjsidl_varFormatField_optional: Property = Property(name="optional", type=StringType)
cjsidl_varFormatField_name: Property = Property(name="name", type=StringType)
cjsidl_varFormatField_countComment: Property = Property(name="countComment", type=StringType)
cjsidl_varFormatField_units: Property = Property(name="units", type=StringType)
cjsidl_varFormatField.attributes={cjsidl_varFormatField_comment, cjsidl_varFormatField_units, cjsidl_varFormatField_name, cjsidl_varFormatField_optional, cjsidl_varFormatField_countComment}

# cjsidl_headerDef class attributes and methods
cjsidl_headerDef_comment: Property = Property(name="comment", type=StringType)
cjsidl_headerDef_name: Property = Property(name="name", type=StringType)
cjsidl_headerDef.attributes={cjsidl_headerDef_comment, cjsidl_headerDef_name}

# cjsidl_simpleNumericType class attributes and methods
cjsidl_simpleNumericType_type: Property = Property(name="type", type=StringType)
cjsidl_simpleNumericType.attributes={cjsidl_simpleNumericType_type}

# cjsidl_arrayDef class attributes and methods
cjsidl_arrayDef_comment: Property = Property(name="comment", type=StringType)
cjsidl_arrayDef_optional: Property = Property(name="optional", type=StringType)
cjsidl_arrayDef_name: Property = Property(name="name", type=StringType)
cjsidl_arrayDef_arraySize: Property = Property(name="arraySize", type=StringType)
cjsidl_arrayDef.attributes={cjsidl_arrayDef_name, cjsidl_arrayDef_optional, cjsidl_arrayDef_comment, cjsidl_arrayDef_arraySize}

# cjsidl_recordDef class attributes and methods

# cjsidl_listDef class attributes and methods
cjsidl_listDef_countComment: Property = Property(name="countComment", type=StringType)
cjsidl_listDef_minCount: Property = Property(name="minCount", type=StringType)
cjsidl_listDef_maxCount: Property = Property(name="maxCount", type=StringType)
cjsidl_listDef.attributes={cjsidl_listDef_minCount, cjsidl_listDef_maxCount, cjsidl_listDef_countComment}

# cjsidl_variantDef class attributes and methods
cjsidl_variantDef_vtagComment: Property = Property(name="vtagComment", type=StringType)
cjsidl_variantDef_minCount: Property = Property(name="minCount", type=StringType)
cjsidl_variantDef_maxCount: Property = Property(name="maxCount", type=StringType)
cjsidl_variantDef.attributes={cjsidl_variantDef_vtagComment, cjsidl_variantDef_maxCount, cjsidl_variantDef_minCount}

# cjsidl_sequenceDef class attributes and methods

# cjsidl_fixedFieldDef class attributes and methods
cjsidl_fixedFieldDef_comment: Property = Property(name="comment", type=StringType)
cjsidl_fixedFieldDef_optional: Property = Property(name="optional", type=StringType)
cjsidl_fixedFieldDef_name: Property = Property(name="name", type=StringType)
cjsidl_fixedFieldDef_fieldUnit: Property = Property(name="fieldUnit", type=StringType)
cjsidl_fixedFieldDef.attributes={cjsidl_fixedFieldDef_name, cjsidl_fixedFieldDef_comment, cjsidl_fixedFieldDef_fieldUnit, cjsidl_fixedFieldDef_optional}

# cjsidl_varField class attributes and methods
cjsidl_varField_comment: Property = Property(name="comment", type=StringType)
cjsidl_varField_optional: Property = Property(name="optional", type=StringType)
cjsidl_varField_name: Property = Property(name="name", type=StringType)
cjsidl_varField.attributes={cjsidl_varField_name, cjsidl_varField_optional, cjsidl_varField_comment}

# cjsidl_bitfieldDef class attributes and methods
cjsidl_bitfieldDef_comment: Property = Property(name="comment", type=StringType)
cjsidl_bitfieldDef_optional: Property = Property(name="optional", type=StringType)
cjsidl_bitfieldDef_type: Property = Property(name="type", type=StringType)
cjsidl_bitfieldDef_name: Property = Property(name="name", type=StringType)
cjsidl_bitfieldDef.attributes={cjsidl_bitfieldDef_comment, cjsidl_bitfieldDef_name, cjsidl_bitfieldDef_type, cjsidl_bitfieldDef_optional}

# cjsidl_headerRef class attributes and methods
cjsidl_headerRef_comment: Property = Property(name="comment", type=StringType)
cjsidl_headerRef_name: Property = Property(name="name", type=StringType)
cjsidl_headerRef.attributes={cjsidl_headerRef_comment, cjsidl_headerRef_name}

# cjsidl_headerScopedRef class attributes and methods

# cjsidl_bodyRef class attributes and methods
cjsidl_bodyRef_comment: Property = Property(name="comment", type=StringType)
cjsidl_bodyRef_name: Property = Property(name="name", type=StringType)
cjsidl_bodyRef.attributes={cjsidl_bodyRef_name, cjsidl_bodyRef_comment}

# cjsidl_bodyScopedRef class attributes and methods

# cjsidl_bodyDef class attributes and methods
cjsidl_bodyDef_comment: Property = Property(name="comment", type=StringType)
cjsidl_bodyDef_name: Property = Property(name="name", type=StringType)
cjsidl_bodyDef.attributes={cjsidl_bodyDef_comment, cjsidl_bodyDef_name}

# cjsidl_footerDef class attributes and methods
cjsidl_footerDef_comment: Property = Property(name="comment", type=StringType)
cjsidl_footerDef_name: Property = Property(name="name", type=StringType)
cjsidl_footerDef.attributes={cjsidl_footerDef_comment, cjsidl_footerDef_name}

# cjsidl_containerRef class attributes and methods
cjsidl_containerRef_comment: Property = Property(name="comment", type=StringType)
cjsidl_containerRef_optional: Property = Property(name="optional", type=StringType)
cjsidl_containerRef_name: Property = Property(name="name", type=StringType)
cjsidl_containerRef.attributes={cjsidl_containerRef_name, cjsidl_containerRef_comment, cjsidl_containerRef_optional}

# cjsidl_scopedType class attributes and methods

# cjsidl_declaredEventDef class attributes and methods
cjsidl_declaredEventDef_comment: Property = Property(name="comment", type=StringType)
cjsidl_declaredEventDef_name: Property = Property(name="name", type=StringType)
cjsidl_declaredEventDef.attributes={cjsidl_declaredEventDef_name, cjsidl_declaredEventDef_comment}

# cjsidl_footerRef class attributes and methods
cjsidl_footerRef_comment: Property = Property(name="comment", type=StringType)
cjsidl_footerRef_name: Property = Property(name="name", type=StringType)
cjsidl_footerRef.attributes={cjsidl_footerRef_name, cjsidl_footerRef_comment}

# cjsidl_footerScopedRef class attributes and methods

# cjsidl_containerDef class attributes and methods
cjsidl_containerDef_comment: Property = Property(name="comment", type=StringType)
cjsidl_containerDef_optional: Property = Property(name="optional", type=StringType)
cjsidl_containerDef_name: Property = Property(name="name", type=StringType)
cjsidl_containerDef.attributes={cjsidl_containerDef_optional, cjsidl_containerDef_comment, cjsidl_containerDef_name}

# cjsidl_constReference class attributes and methods
cjsidl_constReference_comment: Property = Property(name="comment", type=StringType)
cjsidl_constReference.attributes={cjsidl_constReference_comment}

# cjsidl_scopedConstId class attributes and methods

# cjsidl_valueSetDef class attributes and methods
cjsidl_valueSetDef_offset: Property = Property(name="offset", type=StringType)
cjsidl_valueSetDef.attributes={cjsidl_valueSetDef_offset}

# cjsidl_scaledRangeDef class attributes and methods
cjsidl_scaledRangeDef_interp: Property = Property(name="interp", type=StringType)
cjsidl_scaledRangeDef_lowerLim: Property = Property(name="lowerLim", type=StringType)
cjsidl_scaledRangeDef_upperLim: Property = Property(name="upperLim", type=StringType)
cjsidl_scaledRangeDef_function: Property = Property(name="function", type=StringType)
cjsidl_scaledRangeDef.attributes={cjsidl_scaledRangeDef_upperLim, cjsidl_scaledRangeDef_interp, cjsidl_scaledRangeDef_function, cjsidl_scaledRangeDef_lowerLim}

# cjsidl_taggedUnitsEnum class attributes and methods
cjsidl_taggedUnitsEnum_fieldUnit: Property = Property(name="fieldUnit", type=StringType)
cjsidl_taggedUnitsEnum_const_tag: Property = Property(name="const_tag", type=StringType)
cjsidl_taggedUnitsEnum_name: Property = Property(name="name", type=StringType)
cjsidl_taggedUnitsEnum.attributes={cjsidl_taggedUnitsEnum_const_tag, cjsidl_taggedUnitsEnum_name, cjsidl_taggedUnitsEnum_fieldUnit}

# cjsidl_valueSpec class attributes and methods
cjsidl_valueSpec_comment: Property = Property(name="comment", type=StringType)
cjsidl_valueSpec_name: Property = Property(name="name", type=StringType)
cjsidl_valueSpec_value: Property = Property(name="value", type=StringType)
cjsidl_valueSpec.attributes={cjsidl_valueSpec_name, cjsidl_valueSpec_comment, cjsidl_valueSpec_value}

# cjsidl_valueRange class attributes and methods
cjsidl_valueRange_upperLim: Property = Property(name="upperLim", type=StringType)
cjsidl_valueRange_upperLimit_type: Property = Property(name="upperLimit_type", type=StringType)
cjsidl_valueRange_comment: Property = Property(name="comment", type=StringType)
cjsidl_valueRange_lowerLimit_type: Property = Property(name="lowerLimit_type", type=StringType)
cjsidl_valueRange_lowerLim: Property = Property(name="lowerLim", type=StringType)
cjsidl_valueRange.attributes={cjsidl_valueRange_lowerLimit_type, cjsidl_valueRange_upperLimit_type, cjsidl_valueRange_upperLim, cjsidl_valueRange_comment, cjsidl_valueRange_lowerLim}

# cjsidl_formatEnumDef class attributes and methods
cjsidl_formatEnumDef_index: Property = Property(name="index", type=StringType)
cjsidl_formatEnumDef_fieldFormat: Property = Property(name="fieldFormat", type=StringType)
cjsidl_formatEnumDef_fieldFormatStr: Property = Property(name="fieldFormatStr", type=StringType)
cjsidl_formatEnumDef.attributes={cjsidl_formatEnumDef_fieldFormatStr, cjsidl_formatEnumDef_index, cjsidl_formatEnumDef_fieldFormat}

# cjsidl_subField class attributes and methods
cjsidl_subField_comment: Property = Property(name="comment", type=StringType)
cjsidl_subField_name: Property = Property(name="name", type=StringType)
cjsidl_subField_fromIndex: Property = Property(name="fromIndex", type=StringType)
cjsidl_subField_toIndex: Property = Property(name="toIndex", type=StringType)
cjsidl_subField.attributes={cjsidl_subField_comment, cjsidl_subField_fromIndex, cjsidl_subField_toIndex, cjsidl_subField_name}

# containerDef class attributes and methods

# cjsidl_taggedItemDef class attributes and methods

# Relationships
typeSet6: BinaryAssociation = BinaryAssociation(
    name="typeSet6",
    ends={
        Property(name="cjsidl_declaredTypeSet", type=cjsidl_serviceDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_serviceDef7", type=cjsidl_declaredTypeSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
messageSet8: BinaryAssociation = BinaryAssociation(
    name="messageSet8",
    ends={
        Property(name="cjsidl_messageSet", type=cjsidl_serviceDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_serviceDef9", type=cjsidl_messageSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
internalEventSet10: BinaryAssociation = BinaryAssociation(
    name="internalEventSet10",
    ends={
        Property(name="cjsidl_internalEventSet", type=cjsidl_serviceDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_serviceDef11", type=cjsidl_internalEventSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
protocolBehavior12: BinaryAssociation = BinaryAssociation(
    name="protocolBehavior12",
    ends={
        Property(name="cjsidl_protocolBehavior", type=cjsidl_serviceDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_serviceDef13", type=cjsidl_protocolBehavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
set0: BinaryAssociation = BinaryAssociation(
    name="set0",
    ends={
        Property(name="cjsidl_EObject", type=cjsidl_jaus, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_jaus", type=cjsidl_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
descr1: BinaryAssociation = BinaryAssociation(
    name="descr1",
    ends={
        Property(name="cjsidl_description", type=cjsidl_serviceDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_serviceDef", type=cjsidl_description, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refs2: BinaryAssociation = BinaryAssociation(
    name="refs2",
    ends={
        Property(name="cjsidl_references", type=cjsidl_serviceDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_serviceDef3", type=cjsidl_references, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constSet4: BinaryAssociation = BinaryAssociation(
    name="constSet4",
    ends={
        Property(name="cjsidl_declaredConstSet", type=cjsidl_serviceDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_serviceDef5", type=cjsidl_declaredConstSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeRef36: BinaryAssociation = BinaryAssociation(
    name="typeRef36",
    ends={
        Property(name="cjsidl_typeReference", type=cjsidl_declaredTypeSet, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_declaredTypeSet37", type=cjsidl_typeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scopedRef38: BinaryAssociation = BinaryAssociation(
    name="scopedRef38",
    ends={
        Property(name="cjsidl_scopedTypeId", type=cjsidl_declaredTypeSet, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_declaredTypeSet39", type=cjsidl_scopedTypeId, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputSet40: BinaryAssociation = BinaryAssociation(
    name="inputSet40",
    ends={
        Property(name="cjsidl_messages", type=cjsidl_messageSet, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_messageSet41", type=cjsidl_messages, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outputSet42: BinaryAssociation = BinaryAssociation(
    name="outputSet42",
    ends={
        Property(name="cjsidl_messages44", type=cjsidl_messageSet, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_messageSet43", type=cjsidl_messages, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refInherit14: BinaryAssociation = BinaryAssociation(
    name="refInherit14",
    ends={
        Property(name="cjsidl_refAttr", type=cjsidl_references, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_references15", type=cjsidl_refAttr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refClient16: BinaryAssociation = BinaryAssociation(
    name="refClient16",
    ends={
        Property(name="cjsidl_refAttr18", type=cjsidl_references, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_references17", type=cjsidl_refAttr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedNamespace19: BinaryAssociation = BinaryAssociation(
    name="importedNamespace19",
    ends={
        Property(name="cjsidl_serviceDef21", type=cjsidl_refAttr, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_refAttr20", type=cjsidl_serviceDef, multiplicity=Multiplicity(0, 1))
    }
)
declaredConstSetRef22: BinaryAssociation = BinaryAssociation(
    name="declaredConstSetRef22",
    ends={
        Property(name="cjsidl_declaredConstSetRef", type=cjsidl_declaredConstSet, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_declaredConstSet23", type=cjsidl_declaredConstSetRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constDef24: BinaryAssociation = BinaryAssociation(
    name="constDef24",
    ends={
        Property(name="cjsidl_constDef", type=cjsidl_declaredConstSet, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_declaredConstSet25", type=cjsidl_constDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedNamespace26: BinaryAssociation = BinaryAssociation(
    name="importedNamespace26",
    ends={
        Property(name="cjsidl_declaredConstSet28", type=cjsidl_declaredConstSetRef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_declaredConstSetRef27", type=cjsidl_declaredConstSet, multiplicity=Multiplicity(0, 1))
    }
)
declaredConstSetRef29: BinaryAssociation = BinaryAssociation(
    name="declaredConstSetRef29",
    ends={
        Property(name="cjsidl_declaredConstSetRef31", type=cjsidl_declaredTypeSet, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_declaredTypeSet30", type=cjsidl_declaredConstSetRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaredTypeSetRef32: BinaryAssociation = BinaryAssociation(
    name="declaredTypeSetRef32",
    ends={
        Property(name="cjsidl_declaredTypeSetRef", type=cjsidl_declaredTypeSet, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_declaredTypeSet33", type=cjsidl_declaredTypeSetRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeDef34: BinaryAssociation = BinaryAssociation(
    name="typeDef34",
    ends={
        Property(name="cjsidl_typeDef", type=cjsidl_declaredTypeSet, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_declaredTypeSet35", type=cjsidl_typeDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scoped70: BinaryAssociation = BinaryAssociation(
    name="scoped70",
    ends={
        Property(name="cjsidl_state", type=cjsidl_startState, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_startState", type=cjsidl_state, multiplicity=Multiplicity(0, 9999))
    }
)
state71: BinaryAssociation = BinaryAssociation(
    name="state71",
    ends={
        Property(name="cjsidl_state73", type=cjsidl_startState, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_startState72", type=cjsidl_state, multiplicity=Multiplicity(0, 1))
    }
)
scoped74: BinaryAssociation = BinaryAssociation(
    name="scoped74",
    ends={
        Property(name="cjsidl_refAttr76", type=cjsidl_stateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_stateMachine75", type=cjsidl_refAttr, multiplicity=Multiplicity(0, 9999))
    }
)
startState77: BinaryAssociation = BinaryAssociation(
    name="startState77",
    ends={
        Property(name="cjsidl_startState79", type=cjsidl_stateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_stateMachine78", type=cjsidl_startState, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
messageDefs45: BinaryAssociation = BinaryAssociation(
    name="messageDefs45",
    ends={
        Property(name="cjsidl_messageDef", type=cjsidl_messages, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_messages46", type=cjsidl_messageDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeRefs47: BinaryAssociation = BinaryAssociation(
    name="typeRefs47",
    ends={
        Property(name="cjsidl_messageRef", type=cjsidl_messages, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_messages48", type=cjsidl_messageRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scopedRefs49: BinaryAssociation = BinaryAssociation(
    name="scopedRefs49",
    ends={
        Property(name="cjsidl_messageScopedRef", type=cjsidl_messages, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_messages50", type=cjsidl_messageScopedRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defs51: BinaryAssociation = BinaryAssociation(
    name="defs51",
    ends={
        Property(name="cjsidl_EObject53", type=cjsidl_internalEventSet, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_internalEventSet52", type=cjsidl_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
descr54: BinaryAssociation = BinaryAssociation(
    name="descr54",
    ends={
        Property(name="cjsidl_description55", type=cjsidl_eventDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_eventDef", type=cjsidl_description, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
header56: BinaryAssociation = BinaryAssociation(
    name="header56",
    ends={
        Property(name="cjsidl_EObject58", type=cjsidl_eventDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_eventDef57", type=cjsidl_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body59: BinaryAssociation = BinaryAssociation(
    name="body59",
    ends={
        Property(name="cjsidl_EObject61", type=cjsidl_eventDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_eventDef60", type=cjsidl_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
footer62: BinaryAssociation = BinaryAssociation(
    name="footer62",
    ends={
        Property(name="cjsidl_EObject64", type=cjsidl_eventDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_eventDef63", type=cjsidl_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref65: BinaryAssociation = BinaryAssociation(
    name="ref65",
    ends={
        Property(name="cjsidl_messageDef67", type=cjsidl_messageRef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_messageRef66", type=cjsidl_messageDef, multiplicity=Multiplicity(0, 1))
    }
)
stateMachine68: BinaryAssociation = BinaryAssociation(
    name="stateMachine68",
    ends={
        Property(name="cjsidl_stateMachine", type=cjsidl_protocolBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_protocolBehavior69", type=cjsidl_stateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sendActions107: BinaryAssociation = BinaryAssociation(
    name="sendActions107",
    ends={
        Property(name="cjsidl_sendActionList", type=cjsidl_entry, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_entry108", type=cjsidl_sendActionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actions109: BinaryAssociation = BinaryAssociation(
    name="actions109",
    ends={
        Property(name="cjsidl_actionList111", type=cjsidl_exit, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_exit110", type=cjsidl_actionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sendActions112: BinaryAssociation = BinaryAssociation(
    name="sendActions112",
    ends={
        Property(name="cjsidl_sendActionList114", type=cjsidl_exit, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_exit113", type=cjsidl_sendActionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
params115: BinaryAssociation = BinaryAssociation(
    name="params115",
    ends={
        Property(name="cjsidl_transParam", type=cjsidl_transParams, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_transParams", type=cjsidl_transParam, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultState80: BinaryAssociation = BinaryAssociation(
    name="defaultState80",
    ends={
        Property(name="cjsidl_defaultState", type=cjsidl_stateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_stateMachine81", type=cjsidl_defaultState, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
states82: BinaryAssociation = BinaryAssociation(
    name="states82",
    ends={
        Property(name="cjsidl_state84", type=cjsidl_stateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_stateMachine83", type=cjsidl_state, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entryAction85: BinaryAssociation = BinaryAssociation(
    name="entryAction85",
    ends={
        Property(name="cjsidl_entry", type=cjsidl_state, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_state86", type=cjsidl_entry, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exitAction87: BinaryAssociation = BinaryAssociation(
    name="exitAction87",
    ends={
        Property(name="cjsidl_exit", type=cjsidl_state, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_state88", type=cjsidl_exit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transitions89: BinaryAssociation = BinaryAssociation(
    name="transitions89",
    ends={
        Property(name="cjsidl_transition", type=cjsidl_state, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_state90", type=cjsidl_transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultTransition91: BinaryAssociation = BinaryAssociation(
    name="defaultTransition91",
    ends={
        Property(name="cjsidl_defaultTransition", type=cjsidl_state, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_state92", type=cjsidl_defaultTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultState93: BinaryAssociation = BinaryAssociation(
    name="defaultState93",
    ends={
        Property(name="cjsidl_defaultState95", type=cjsidl_state, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_state94", type=cjsidl_defaultState, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subState97: BinaryAssociation = BinaryAssociation(
    name="subState97",
    ends={
        Property(name="cjsidl_state98", type=cjsidl_state, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_state96", type=cjsidl_state, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition99: BinaryAssociation = BinaryAssociation(
    name="transition99",
    ends={
        Property(name="cjsidl_transition101", type=cjsidl_defaultState, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_defaultState100", type=cjsidl_transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultTransition102: BinaryAssociation = BinaryAssociation(
    name="defaultTransition102",
    ends={
        Property(name="cjsidl_defaultTransition104", type=cjsidl_defaultState, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_defaultState103", type=cjsidl_defaultTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actions105: BinaryAssociation = BinaryAssociation(
    name="actions105",
    ends={
        Property(name="cjsidl_actionList", type=cjsidl_entry, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_entry106", type=cjsidl_actionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
destination147: BinaryAssociation = BinaryAssociation(
    name="destination147",
    ends={
        Property(name="cjsidl_defaultTransition148", type=cjsidl_EObject, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="cjsidl_EObject149", type=cjsidl_defaultTransition, multiplicity=Multiplicity(1, 1))
    }
)
nextState150: BinaryAssociation = BinaryAssociation(
    name="nextState150",
    ends={
        Property(name="cjsidl_nextState", type=cjsidl_simpleTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_simpleTransition", type=cjsidl_nextState, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nextState151: BinaryAssociation = BinaryAssociation(
    name="nextState151",
    ends={
        Property(name="cjsidl_nextState152", type=cjsidl_pushTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_pushTransition", type=cjsidl_nextState, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type116: BinaryAssociation = BinaryAssociation(
    name="type116",
    ends={
        Property(name="cjsidl_EObject118", type=cjsidl_transParam, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_transParam117", type=cjsidl_EObject, multiplicity=Multiplicity(0, 1))
    }
)
scopedEventType119: BinaryAssociation = BinaryAssociation(
    name="scopedEventType119",
    ends={
        Property(name="cjsidl_scopedEventType", type=cjsidl_transParam, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_transParam120", type=cjsidl_scopedEventType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scoped121: BinaryAssociation = BinaryAssociation(
    name="scoped121",
    ends={
        Property(name="cjsidl_refAttr123", type=cjsidl_transition, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_transition122", type=cjsidl_refAttr, multiplicity=Multiplicity(0, 9999))
    }
)
params124: BinaryAssociation = BinaryAssociation(
    name="params124",
    ends={
        Property(name="cjsidl_transParams126", type=cjsidl_transition, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_transition125", type=cjsidl_transParams, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transGuard127: BinaryAssociation = BinaryAssociation(
    name="transGuard127",
    ends={
        Property(name="cjsidl_guard", type=cjsidl_transition, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_transition128", type=cjsidl_guard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actions129: BinaryAssociation = BinaryAssociation(
    name="actions129",
    ends={
        Property(name="cjsidl_actionList131", type=cjsidl_transition, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_transition130", type=cjsidl_actionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sendActions132: BinaryAssociation = BinaryAssociation(
    name="sendActions132",
    ends={
        Property(name="cjsidl_sendActionList134", type=cjsidl_transition, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_transition133", type=cjsidl_sendActionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
destination135: BinaryAssociation = BinaryAssociation(
    name="destination135",
    ends={
        Property(name="cjsidl_EObject137", type=cjsidl_transition, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_transition136", type=cjsidl_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transGuard138: BinaryAssociation = BinaryAssociation(
    name="transGuard138",
    ends={
        Property(name="cjsidl_guard140", type=cjsidl_defaultTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_defaultTransition139", type=cjsidl_guard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actions141: BinaryAssociation = BinaryAssociation(
    name="actions141",
    ends={
        Property(name="cjsidl_actionList143", type=cjsidl_defaultTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_defaultTransition142", type=cjsidl_actionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sendActions144: BinaryAssociation = BinaryAssociation(
    name="sendActions144",
    ends={
        Property(name="cjsidl_sendActionList146", type=cjsidl_defaultTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_defaultTransition145", type=cjsidl_sendActionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actions177: BinaryAssociation = BinaryAssociation(
    name="actions177",
    ends={
        Property(name="cjsidl_actionList178", type=cjsidl_action, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="cjsidl_action", type=cjsidl_actionList, multiplicity=Multiplicity(1, 1))
    }
)
actions179: BinaryAssociation = BinaryAssociation(
    name="actions179",
    ends={
        Property(name="cjsidl_action181", type=cjsidl_sendActionList, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_sendActionList180", type=cjsidl_action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
param182: BinaryAssociation = BinaryAssociation(
    name="param182",
    ends={
        Property(name="cjsidl_guardParam184", type=cjsidl_action, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_action183", type=cjsidl_guardParam, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
simpleTransition153: BinaryAssociation = BinaryAssociation(
    name="simpleTransition153",
    ends={
        Property(name="cjsidl_simpleTransition155", type=cjsidl_pushTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_pushTransition154", type=cjsidl_simpleTransition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
secondaryTransition156: BinaryAssociation = BinaryAssociation(
    name="secondaryTransition156",
    ends={
        Property(name="cjsidl_transition157", type=cjsidl_popTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_popTransition", type=cjsidl_transition, multiplicity=Multiplicity(0, 1))
    }
)
param158: BinaryAssociation = BinaryAssociation(
    name="param158",
    ends={
        Property(name="cjsidl_guardParam", type=cjsidl_popTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_popTransition159", type=cjsidl_guardParam, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
firstState160: BinaryAssociation = BinaryAssociation(
    name="firstState160",
    ends={
        Property(name="cjsidl_state162", type=cjsidl_nextState, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_nextState161", type=cjsidl_state, multiplicity=Multiplicity(0, 1))
    }
)
scoped163: BinaryAssociation = BinaryAssociation(
    name="scoped163",
    ends={
        Property(name="cjsidl_state165", type=cjsidl_nextState, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_nextState164", type=cjsidl_state, multiplicity=Multiplicity(0, 9999))
    }
)
nextState166: BinaryAssociation = BinaryAssociation(
    name="nextState166",
    ends={
        Property(name="cjsidl_state168", type=cjsidl_nextState, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_nextState167", type=cjsidl_state, multiplicity=Multiplicity(0, 1))
    }
)
guardAction169: BinaryAssociation = BinaryAssociation(
    name="guardAction169",
    ends={
        Property(name="cjsidl_guardAction", type=cjsidl_guard, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_guard170", type=cjsidl_guardAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
param171: BinaryAssociation = BinaryAssociation(
    name="param171",
    ends={
        Property(name="cjsidl_guardParam173", type=cjsidl_guardAction, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_guardAction172", type=cjsidl_guardParam, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter174: BinaryAssociation = BinaryAssociation(
    name="parameter174",
    ends={
        Property(name="cjsidl_transParam176", type=cjsidl_guardParam, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_guardParam175", type=cjsidl_transParam, multiplicity=Multiplicity(0, 1))
    }
)
fixedLenString209: BinaryAssociation = BinaryAssociation(
    name="fixedLenString209",
    ends={
        Property(name="cjsidl_fixedLenString", type=cjsidl_typeDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_typeDef210", type=cjsidl_fixedLenString, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
varLenString211: BinaryAssociation = BinaryAssociation(
    name="varLenString211",
    ends={
        Property(name="cjsidl_varLenString", type=cjsidl_typeDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_typeDef212", type=cjsidl_varLenString, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
varLenField213: BinaryAssociation = BinaryAssociation(
    name="varLenField213",
    ends={
        Property(name="cjsidl_varLenField", type=cjsidl_typeDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_typeDef214", type=cjsidl_varLenField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
varFormatField215: BinaryAssociation = BinaryAssociation(
    name="varFormatField215",
    ends={
        Property(name="cjsidl_varFormatField", type=cjsidl_typeDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_typeDef216", type=cjsidl_varFormatField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
headerDef217: BinaryAssociation = BinaryAssociation(
    name="headerDef217",
    ends={
        Property(name="cjsidl_headerDef", type=cjsidl_typeDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_typeDef218", type=cjsidl_headerDef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constType185: BinaryAssociation = BinaryAssociation(
    name="constType185",
    ends={
        Property(name="cjsidl_simpleNumericType", type=cjsidl_constDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_constDef186", type=cjsidl_simpleNumericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
importedNamespace187: BinaryAssociation = BinaryAssociation(
    name="importedNamespace187",
    ends={
        Property(name="cjsidl_declaredTypeSet189", type=cjsidl_declaredTypeSetRef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_declaredTypeSetRef188", type=cjsidl_declaredTypeSet, multiplicity=Multiplicity(0, 1))
    }
)
messageDef190: BinaryAssociation = BinaryAssociation(
    name="messageDef190",
    ends={
        Property(name="cjsidl_messageDef192", type=cjsidl_typeDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_typeDef191", type=cjsidl_messageDef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arrayDef193: BinaryAssociation = BinaryAssociation(
    name="arrayDef193",
    ends={
        Property(name="cjsidl_arrayDef", type=cjsidl_typeDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_typeDef194", type=cjsidl_arrayDef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
recordDef195: BinaryAssociation = BinaryAssociation(
    name="recordDef195",
    ends={
        Property(name="cjsidl_recordDef", type=cjsidl_typeDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_typeDef196", type=cjsidl_recordDef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
listDef197: BinaryAssociation = BinaryAssociation(
    name="listDef197",
    ends={
        Property(name="cjsidl_listDef", type=cjsidl_typeDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_typeDef198", type=cjsidl_listDef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variantDef199: BinaryAssociation = BinaryAssociation(
    name="variantDef199",
    ends={
        Property(name="cjsidl_variantDef", type=cjsidl_typeDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_typeDef200", type=cjsidl_variantDef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequenceDef201: BinaryAssociation = BinaryAssociation(
    name="sequenceDef201",
    ends={
        Property(name="cjsidl_sequenceDef", type=cjsidl_typeDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_typeDef202", type=cjsidl_sequenceDef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fixedFieldDef203: BinaryAssociation = BinaryAssociation(
    name="fixedFieldDef203",
    ends={
        Property(name="cjsidl_fixedFieldDef", type=cjsidl_typeDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_typeDef204", type=cjsidl_fixedFieldDef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
varField205: BinaryAssociation = BinaryAssociation(
    name="varField205",
    ends={
        Property(name="cjsidl_varField", type=cjsidl_typeDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_typeDef206", type=cjsidl_varField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bitfieldDef207: BinaryAssociation = BinaryAssociation(
    name="bitfieldDef207",
    ends={
        Property(name="cjsidl_bitfieldDef", type=cjsidl_typeDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_typeDef208", type=cjsidl_bitfieldDef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeRef244: BinaryAssociation = BinaryAssociation(
    name="typeRef244",
    ends={
        Property(name="cjsidl_headerDef245", type=cjsidl_headerRef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_headerRef", type=cjsidl_headerDef, multiplicity=Multiplicity(0, 1))
    }
)
scopedRef246: BinaryAssociation = BinaryAssociation(
    name="scopedRef246",
    ends={
        Property(name="cjsidl_headerScopedRef", type=cjsidl_headerRef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_headerRef247", type=cjsidl_headerScopedRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeRef248: BinaryAssociation = BinaryAssociation(
    name="typeRef248",
    ends={
        Property(name="cjsidl_bodyDef249", type=cjsidl_bodyRef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_bodyRef", type=cjsidl_bodyDef, multiplicity=Multiplicity(0, 1))
    }
)
bodyDef219: BinaryAssociation = BinaryAssociation(
    name="bodyDef219",
    ends={
        Property(name="cjsidl_bodyDef", type=cjsidl_typeDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_typeDef220", type=cjsidl_bodyDef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
footerDef221: BinaryAssociation = BinaryAssociation(
    name="footerDef221",
    ends={
        Property(name="cjsidl_footerDef", type=cjsidl_typeDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_typeDef222", type=cjsidl_footerDef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
descr223: BinaryAssociation = BinaryAssociation(
    name="descr223",
    ends={
        Property(name="cjsidl_description225", type=cjsidl_messageDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_messageDef224", type=cjsidl_description, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
header226: BinaryAssociation = BinaryAssociation(
    name="header226",
    ends={
        Property(name="cjsidl_EObject228", type=cjsidl_messageDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_messageDef227", type=cjsidl_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body229: BinaryAssociation = BinaryAssociation(
    name="body229",
    ends={
        Property(name="cjsidl_EObject231", type=cjsidl_messageDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_messageDef230", type=cjsidl_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
footer232: BinaryAssociation = BinaryAssociation(
    name="footer232",
    ends={
        Property(name="cjsidl_EObject234", type=cjsidl_messageDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_messageDef233", type=cjsidl_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
recordListSequenceVariant235: BinaryAssociation = BinaryAssociation(
    name="recordListSequenceVariant235",
    ends={
        Property(name="cjsidl_EObject237", type=cjsidl_headerDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_headerDef236", type=cjsidl_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
recordListSequenceVariant238: BinaryAssociation = BinaryAssociation(
    name="recordListSequenceVariant238",
    ends={
        Property(name="cjsidl_EObject240", type=cjsidl_bodyDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_bodyDef239", type=cjsidl_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
recordListSequenceVariant241: BinaryAssociation = BinaryAssociation(
    name="recordListSequenceVariant241",
    ends={
        Property(name="cjsidl_EObject243", type=cjsidl_footerDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_footerDef242", type=cjsidl_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type283: BinaryAssociation = BinaryAssociation(
    name="type283",
    ends={
        Property(name="cjsidl_containerDef", type=cjsidl_containerRef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_containerRef", type=cjsidl_containerDef, multiplicity=Multiplicity(0, 1))
    }
)
typeScoped284: BinaryAssociation = BinaryAssociation(
    name="typeScoped284",
    ends={
        Property(name="cjsidl_scopedType", type=cjsidl_containerRef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_containerRef285", type=cjsidl_scopedType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scopedRef250: BinaryAssociation = BinaryAssociation(
    name="scopedRef250",
    ends={
        Property(name="cjsidl_bodyScopedRef", type=cjsidl_bodyRef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_bodyRef251", type=cjsidl_bodyScopedRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeRef252: BinaryAssociation = BinaryAssociation(
    name="typeRef252",
    ends={
        Property(name="cjsidl_footerDef253", type=cjsidl_footerRef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_footerRef", type=cjsidl_footerDef, multiplicity=Multiplicity(0, 1))
    }
)
scopedRef254: BinaryAssociation = BinaryAssociation(
    name="scopedRef254",
    ends={
        Property(name="cjsidl_footerScopedRef", type=cjsidl_footerRef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_footerRef255", type=cjsidl_footerScopedRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name256: BinaryAssociation = BinaryAssociation(
    name="name256",
    ends={
        Property(name="cjsidl_EObject258", type=cjsidl_headerScopedRef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_headerScopedRef257", type=cjsidl_EObject, multiplicity=Multiplicity(0, 1))
    }
)
names259: BinaryAssociation = BinaryAssociation(
    name="names259",
    ends={
        Property(name="cjsidl_EObject261", type=cjsidl_headerScopedRef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_headerScopedRef260", type=cjsidl_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
type262: BinaryAssociation = BinaryAssociation(
    name="type262",
    ends={
        Property(name="cjsidl_headerDef264", type=cjsidl_headerScopedRef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_headerScopedRef263", type=cjsidl_headerDef, multiplicity=Multiplicity(0, 1))
    }
)
name265: BinaryAssociation = BinaryAssociation(
    name="name265",
    ends={
        Property(name="cjsidl_EObject267", type=cjsidl_bodyScopedRef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_bodyScopedRef266", type=cjsidl_EObject, multiplicity=Multiplicity(0, 1))
    }
)
names268: BinaryAssociation = BinaryAssociation(
    name="names268",
    ends={
        Property(name="cjsidl_EObject270", type=cjsidl_bodyScopedRef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_bodyScopedRef269", type=cjsidl_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
type271: BinaryAssociation = BinaryAssociation(
    name="type271",
    ends={
        Property(name="cjsidl_bodyDef273", type=cjsidl_bodyScopedRef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_bodyScopedRef272", type=cjsidl_bodyDef, multiplicity=Multiplicity(0, 1))
    }
)
name274: BinaryAssociation = BinaryAssociation(
    name="name274",
    ends={
        Property(name="cjsidl_EObject276", type=cjsidl_footerScopedRef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_footerScopedRef275", type=cjsidl_EObject, multiplicity=Multiplicity(0, 1))
    }
)
names277: BinaryAssociation = BinaryAssociation(
    name="names277",
    ends={
        Property(name="cjsidl_EObject279", type=cjsidl_footerScopedRef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_footerScopedRef278", type=cjsidl_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
type280: BinaryAssociation = BinaryAssociation(
    name="type280",
    ends={
        Property(name="cjsidl_footerDef282", type=cjsidl_footerScopedRef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_footerScopedRef281", type=cjsidl_footerDef, multiplicity=Multiplicity(0, 1))
    }
)
upperLimRef301: BinaryAssociation = BinaryAssociation(
    name="upperLimRef301",
    ends={
        Property(name="cjsidl_constReference303", type=cjsidl_varLenString, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_varLenString302", type=cjsidl_constReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
upperLimScoped304: BinaryAssociation = BinaryAssociation(
    name="upperLimScoped304",
    ends={
        Property(name="cjsidl_scopedConstId306", type=cjsidl_varLenString, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_varLenString305", type=cjsidl_scopedConstId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type307: BinaryAssociation = BinaryAssociation(
    name="type307",
    ends={
        Property(name="cjsidl_simpleNumericType309", type=cjsidl_fixedFieldDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_fixedFieldDef308", type=cjsidl_simpleNumericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
valueRange310: BinaryAssociation = BinaryAssociation(
    name="valueRange310",
    ends={
        Property(name="cjsidl_EObject312", type=cjsidl_fixedFieldDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_fixedFieldDef311", type=cjsidl_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type286: BinaryAssociation = BinaryAssociation(
    name="type286",
    ends={
        Property(name="cjsidl_eventDef287", type=cjsidl_declaredEventDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_declaredEventDef", type=cjsidl_eventDef, multiplicity=Multiplicity(0, 1))
    }
)
scopedEventType288: BinaryAssociation = BinaryAssociation(
    name="scopedEventType288",
    ends={
        Property(name="cjsidl_scopedEventType290", type=cjsidl_declaredEventDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_declaredEventDef289", type=cjsidl_scopedEventType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
upperLimRef291: BinaryAssociation = BinaryAssociation(
    name="upperLimRef291",
    ends={
        Property(name="cjsidl_constReference", type=cjsidl_fixedLenString, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_fixedLenString292", type=cjsidl_constReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
upperLimScoped293: BinaryAssociation = BinaryAssociation(
    name="upperLimScoped293",
    ends={
        Property(name="cjsidl_scopedConstId", type=cjsidl_fixedLenString, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_fixedLenString294", type=cjsidl_scopedConstId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lowerLimRef295: BinaryAssociation = BinaryAssociation(
    name="lowerLimRef295",
    ends={
        Property(name="cjsidl_constReference297", type=cjsidl_varLenString, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_varLenString296", type=cjsidl_constReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lowerLimScoped298: BinaryAssociation = BinaryAssociation(
    name="lowerLimScoped298",
    ends={
        Property(name="cjsidl_scopedConstId300", type=cjsidl_varLenString, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_varLenString299", type=cjsidl_scopedConstId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type333: BinaryAssociation = BinaryAssociation(
    name="type333",
    ends={
        Property(name="cjsidl_simpleNumericType335", type=cjsidl_taggedUnitsEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_taggedUnitsEnum334", type=cjsidl_simpleNumericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
valueSetDef336: BinaryAssociation = BinaryAssociation(
    name="valueSetDef336",
    ends={
        Property(name="cjsidl_valueSetDef", type=cjsidl_taggedUnitsEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_taggedUnitsEnum337", type=cjsidl_valueSetDef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scaledRangeDef338: BinaryAssociation = BinaryAssociation(
    name="scaledRangeDef338",
    ends={
        Property(name="cjsidl_scaledRangeDef", type=cjsidl_taggedUnitsEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_taggedUnitsEnum339", type=cjsidl_scaledRangeDef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vtagField313: BinaryAssociation = BinaryAssociation(
    name="vtagField313",
    ends={
        Property(name="cjsidl_taggedUnitsEnum", type=cjsidl_varField, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_varField314", type=cjsidl_taggedUnitsEnum, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lowerLimRef315: BinaryAssociation = BinaryAssociation(
    name="lowerLimRef315",
    ends={
        Property(name="cjsidl_constReference317", type=cjsidl_varLenField, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_varLenField316", type=cjsidl_constReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lowerLimScoped318: BinaryAssociation = BinaryAssociation(
    name="lowerLimScoped318",
    ends={
        Property(name="cjsidl_scopedConstId320", type=cjsidl_varLenField, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_varLenField319", type=cjsidl_scopedConstId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
upperLimRef321: BinaryAssociation = BinaryAssociation(
    name="upperLimRef321",
    ends={
        Property(name="cjsidl_constReference323", type=cjsidl_varLenField, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_varLenField322", type=cjsidl_constReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
upperLimScoped324: BinaryAssociation = BinaryAssociation(
    name="upperLimScoped324",
    ends={
        Property(name="cjsidl_scopedConstId326", type=cjsidl_varLenField, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_varLenField325", type=cjsidl_scopedConstId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tag327: BinaryAssociation = BinaryAssociation(
    name="tag327",
    ends={
        Property(name="cjsidl_constReference329", type=cjsidl_taggedUnitsEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_taggedUnitsEnum328", type=cjsidl_constReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scopedTag330: BinaryAssociation = BinaryAssociation(
    name="scopedTag330",
    ends={
        Property(name="cjsidl_scopedConstId332", type=cjsidl_taggedUnitsEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_taggedUnitsEnum331", type=cjsidl_scopedConstId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lowerLimScoped358: BinaryAssociation = BinaryAssociation(
    name="lowerLimScoped358",
    ends={
        Property(name="cjsidl_scopedConstId360", type=cjsidl_valueRange, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_valueRange359", type=cjsidl_scopedConstId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
upperLimRef361: BinaryAssociation = BinaryAssociation(
    name="upperLimRef361",
    ends={
        Property(name="cjsidl_constReference363", type=cjsidl_valueRange, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_valueRange362", type=cjsidl_constReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
upperLimScoped364: BinaryAssociation = BinaryAssociation(
    name="upperLimScoped364",
    ends={
        Property(name="cjsidl_scopedConstId366", type=cjsidl_valueRange, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_valueRange365", type=cjsidl_scopedConstId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
countRange340: BinaryAssociation = BinaryAssociation(
    name="countRange340",
    ends={
        Property(name="cjsidl_valueRange", type=cjsidl_varFormatField, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_varFormatField341", type=cjsidl_valueRange, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formatField342: BinaryAssociation = BinaryAssociation(
    name="formatField342",
    ends={
        Property(name="cjsidl_formatEnumDef", type=cjsidl_varFormatField, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_varFormatField343", type=cjsidl_formatEnumDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constRef344: BinaryAssociation = BinaryAssociation(
    name="constRef344",
    ends={
        Property(name="cjsidl_constReference346", type=cjsidl_formatEnumDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_formatEnumDef345", type=cjsidl_constReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constScopedRef347: BinaryAssociation = BinaryAssociation(
    name="constScopedRef347",
    ends={
        Property(name="cjsidl_scopedConstId349", type=cjsidl_formatEnumDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_formatEnumDef348", type=cjsidl_scopedConstId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value350: BinaryAssociation = BinaryAssociation(
    name="value350",
    ends={
        Property(name="cjsidl_EObject352", type=cjsidl_valueSetDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_valueSetDef351", type=cjsidl_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subField353: BinaryAssociation = BinaryAssociation(
    name="subField353",
    ends={
        Property(name="cjsidl_subField", type=cjsidl_bitfieldDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_bitfieldDef354", type=cjsidl_subField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lowerLimRef355: BinaryAssociation = BinaryAssociation(
    name="lowerLimRef355",
    ends={
        Property(name="cjsidl_constReference357", type=cjsidl_valueRange, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_valueRange356", type=cjsidl_constReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
minCountRef382: BinaryAssociation = BinaryAssociation(
    name="minCountRef382",
    ends={
        Property(name="cjsidl_constReference384", type=cjsidl_listDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_listDef383", type=cjsidl_constReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
minCountScoped385: BinaryAssociation = BinaryAssociation(
    name="minCountScoped385",
    ends={
        Property(name="cjsidl_scopedConstId387", type=cjsidl_listDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_listDef386", type=cjsidl_scopedConstId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lowerLimRef367: BinaryAssociation = BinaryAssociation(
    name="lowerLimRef367",
    ends={
        Property(name="cjsidl_constReference369", type=cjsidl_scaledRangeDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_scaledRangeDef368", type=cjsidl_constReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lowerLimScoped370: BinaryAssociation = BinaryAssociation(
    name="lowerLimScoped370",
    ends={
        Property(name="cjsidl_scopedConstId372", type=cjsidl_scaledRangeDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_scaledRangeDef371", type=cjsidl_scopedConstId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
upperLimRef373: BinaryAssociation = BinaryAssociation(
    name="upperLimRef373",
    ends={
        Property(name="cjsidl_constReference375", type=cjsidl_scaledRangeDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_scaledRangeDef374", type=cjsidl_constReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
upperLimScoped376: BinaryAssociation = BinaryAssociation(
    name="upperLimScoped376",
    ends={
        Property(name="cjsidl_scopedConstId378", type=cjsidl_scaledRangeDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_scaledRangeDef377", type=cjsidl_scopedConstId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
valueSet379: BinaryAssociation = BinaryAssociation(
    name="valueSet379",
    ends={
        Property(name="cjsidl_valueSetDef381", type=cjsidl_subField, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_subField380", type=cjsidl_valueSetDef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerDef414: BinaryAssociation = BinaryAssociation(
    name="containerDef414",
    ends={
        Property(name="cjsidl_containerDef416", type=cjsidl_taggedItemDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_taggedItemDef415", type=cjsidl_containerDef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerRef417: BinaryAssociation = BinaryAssociation(
    name="containerRef417",
    ends={
        Property(name="cjsidl_containerRef419", type=cjsidl_taggedItemDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_taggedItemDef418", type=cjsidl_containerRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerTypeList420: BinaryAssociation = BinaryAssociation(
    name="containerTypeList420",
    ends={
        Property(name="cjsidl_EObject422", type=cjsidl_sequenceDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_sequenceDef421", type=cjsidl_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
maxCountRef388: BinaryAssociation = BinaryAssociation(
    name="maxCountRef388",
    ends={
        Property(name="cjsidl_constReference390", type=cjsidl_listDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_listDef389", type=cjsidl_constReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
maxCountScoped391: BinaryAssociation = BinaryAssociation(
    name="maxCountScoped391",
    ends={
        Property(name="cjsidl_scopedConstId393", type=cjsidl_listDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_listDef392", type=cjsidl_scopedConstId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerRef394: BinaryAssociation = BinaryAssociation(
    name="containerRef394",
    ends={
        Property(name="cjsidl_containerRef396", type=cjsidl_listDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_listDef395", type=cjsidl_containerRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerDef397: BinaryAssociation = BinaryAssociation(
    name="containerDef397",
    ends={
        Property(name="cjsidl_containerDef399", type=cjsidl_listDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_listDef398", type=cjsidl_containerDef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
minCountRef400: BinaryAssociation = BinaryAssociation(
    name="minCountRef400",
    ends={
        Property(name="cjsidl_constReference402", type=cjsidl_variantDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_variantDef401", type=cjsidl_constReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
minCountScoped403: BinaryAssociation = BinaryAssociation(
    name="minCountScoped403",
    ends={
        Property(name="cjsidl_scopedConstId405", type=cjsidl_variantDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_variantDef404", type=cjsidl_scopedConstId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
maxCountRef406: BinaryAssociation = BinaryAssociation(
    name="maxCountRef406",
    ends={
        Property(name="cjsidl_constReference408", type=cjsidl_variantDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_variantDef407", type=cjsidl_constReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
maxCountScoped409: BinaryAssociation = BinaryAssociation(
    name="maxCountScoped409",
    ends={
        Property(name="cjsidl_scopedConstId411", type=cjsidl_variantDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_variantDef410", type=cjsidl_scopedConstId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
itemList412: BinaryAssociation = BinaryAssociation(
    name="itemList412",
    ends={
        Property(name="cjsidl_taggedItemDef", type=cjsidl_variantDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_variantDef413", type=cjsidl_taggedItemDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type456: BinaryAssociation = BinaryAssociation(
    name="type456",
    ends={
        Property(name="cjsidl_EObject458", type=cjsidl_typeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_typeReference457", type=cjsidl_EObject, multiplicity=Multiplicity(0, 1))
    }
)
arrayDef423: BinaryAssociation = BinaryAssociation(
    name="arrayDef423",
    ends={
        Property(name="cjsidl_arrayDef425", type=cjsidl_recordDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_recordDef424", type=cjsidl_arrayDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fieldDef426: BinaryAssociation = BinaryAssociation(
    name="fieldDef426",
    ends={
        Property(name="cjsidl_fixedFieldDef428", type=cjsidl_recordDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_recordDef427", type=cjsidl_fixedFieldDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variableFieldDef429: BinaryAssociation = BinaryAssociation(
    name="variableFieldDef429",
    ends={
        Property(name="cjsidl_varField431", type=cjsidl_recordDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_recordDef430", type=cjsidl_varField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bitfieldDef432: BinaryAssociation = BinaryAssociation(
    name="bitfieldDef432",
    ends={
        Property(name="cjsidl_bitfieldDef434", type=cjsidl_recordDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_recordDef433", type=cjsidl_bitfieldDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fixedLengthStringDef435: BinaryAssociation = BinaryAssociation(
    name="fixedLengthStringDef435",
    ends={
        Property(name="cjsidl_fixedLenString437", type=cjsidl_recordDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_recordDef436", type=cjsidl_fixedLenString, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variableLengthStringDef438: BinaryAssociation = BinaryAssociation(
    name="variableLengthStringDef438",
    ends={
        Property(name="cjsidl_varLenString440", type=cjsidl_recordDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_recordDef439", type=cjsidl_varLenString, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variableLengthFieldDef441: BinaryAssociation = BinaryAssociation(
    name="variableLengthFieldDef441",
    ends={
        Property(name="cjsidl_varLenField443", type=cjsidl_recordDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_recordDef442", type=cjsidl_varLenField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
varFormatField444: BinaryAssociation = BinaryAssociation(
    name="varFormatField444",
    ends={
        Property(name="cjsidl_varFormatField446", type=cjsidl_recordDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_recordDef445", type=cjsidl_varFormatField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeReference447: BinaryAssociation = BinaryAssociation(
    name="typeReference447",
    ends={
        Property(name="cjsidl_typeReference449", type=cjsidl_recordDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_recordDef448", type=cjsidl_typeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scopedRef450: BinaryAssociation = BinaryAssociation(
    name="scopedRef450",
    ends={
        Property(name="cjsidl_scopedTypeId452", type=cjsidl_recordDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_recordDef451", type=cjsidl_scopedTypeId, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constVal453: BinaryAssociation = BinaryAssociation(
    name="constVal453",
    ends={
        Property(name="cjsidl_constDef455", type=cjsidl_constReference, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_constReference454", type=cjsidl_constDef, multiplicity=Multiplicity(0, 1))
    }
)
type489: BinaryAssociation = BinaryAssociation(
    name="type489",
    ends={
        Property(name="cjsidl_EObject491", type=cjsidl_scopedEventType, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_scopedEventType490", type=cjsidl_EObject, multiplicity=Multiplicity(0, 1))
    }
)
ref492: BinaryAssociation = BinaryAssociation(
    name="ref492",
    ends={
        Property(name="cjsidl_scopedType494", type=cjsidl_scopedTypeId, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_scopedTypeId493", type=cjsidl_scopedType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeRef459: BinaryAssociation = BinaryAssociation(
    name="typeRef459",
    ends={
        Property(name="cjsidl_EObject461", type=cjsidl_arrayDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_arrayDef460", type=cjsidl_EObject, multiplicity=Multiplicity(0, 1))
    }
)
scopedType462: BinaryAssociation = BinaryAssociation(
    name="scopedType462",
    ends={
        Property(name="cjsidl_scopedType464", type=cjsidl_arrayDef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_arrayDef463", type=cjsidl_scopedType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scope465: BinaryAssociation = BinaryAssociation(
    name="scope465",
    ends={
        Property(name="cjsidl_EObject467", type=cjsidl_messageScopedRef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_messageScopedRef466", type=cjsidl_EObject, multiplicity=Multiplicity(0, 1))
    }
)
scopes468: BinaryAssociation = BinaryAssociation(
    name="scopes468",
    ends={
        Property(name="cjsidl_EObject470", type=cjsidl_messageScopedRef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_messageScopedRef469", type=cjsidl_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
ref471: BinaryAssociation = BinaryAssociation(
    name="ref471",
    ends={
        Property(name="cjsidl_messageDef473", type=cjsidl_messageScopedRef, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_messageScopedRef472", type=cjsidl_messageDef, multiplicity=Multiplicity(0, 1))
    }
)
name474: BinaryAssociation = BinaryAssociation(
    name="name474",
    ends={
        Property(name="cjsidl_EObject476", type=cjsidl_scopedType, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_scopedType475", type=cjsidl_EObject, multiplicity=Multiplicity(0, 1))
    }
)
names477: BinaryAssociation = BinaryAssociation(
    name="names477",
    ends={
        Property(name="cjsidl_EObject479", type=cjsidl_scopedType, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_scopedType478", type=cjsidl_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
type480: BinaryAssociation = BinaryAssociation(
    name="type480",
    ends={
        Property(name="cjsidl_EObject482", type=cjsidl_scopedType, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_scopedType481", type=cjsidl_EObject, multiplicity=Multiplicity(0, 1))
    }
)
name483: BinaryAssociation = BinaryAssociation(
    name="name483",
    ends={
        Property(name="cjsidl_EObject485", type=cjsidl_scopedEventType, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_scopedEventType484", type=cjsidl_EObject, multiplicity=Multiplicity(0, 1))
    }
)
names486: BinaryAssociation = BinaryAssociation(
    name="names486",
    ends={
        Property(name="cjsidl_EObject488", type=cjsidl_scopedEventType, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_scopedEventType487", type=cjsidl_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
name495: BinaryAssociation = BinaryAssociation(
    name="name495",
    ends={
        Property(name="cjsidl_EObject497", type=cjsidl_scopedConstId, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_scopedConstId496", type=cjsidl_EObject, multiplicity=Multiplicity(0, 1))
    }
)
names498: BinaryAssociation = BinaryAssociation(
    name="names498",
    ends={
        Property(name="cjsidl_EObject500", type=cjsidl_scopedConstId, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_scopedConstId499", type=cjsidl_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
type501: BinaryAssociation = BinaryAssociation(
    name="type501",
    ends={
        Property(name="cjsidl_constDef503", type=cjsidl_scopedConstId, multiplicity=Multiplicity(1, 1)),
        Property(name="cjsidl_scopedConstId502", type=cjsidl_constDef, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_cjsidl_listDef_containerDef = Generalization(general=containerDef, specific=cjsidl_listDef)
gen_cjsidl_sequenceDef_containerDef = Generalization(general=containerDef, specific=cjsidl_sequenceDef)
gen_cjsidl_recordDef_containerDef = Generalization(general=containerDef, specific=cjsidl_recordDef)
gen_cjsidl_variantDef_containerDef = Generalization(general=containerDef, specific=cjsidl_variantDef)

# Domain Model
domain_model = DomainModel(
    name="cjsidl",
    types={cjsidl_declaredTypeSet, cjsidl_messageSet, cjsidl_internalEventSet, cjsidl_protocolBehavior, cjsidl_jaus, cjsidl_EObject, cjsidl_serviceDef, cjsidl_description, cjsidl_references, cjsidl_declaredConstSet, cjsidl_scopedTypeId, cjsidl_messages, cjsidl_refAttr, cjsidl_declaredConstSetRef, cjsidl_constDef, cjsidl_declaredTypeSetRef, cjsidl_typeDef, cjsidl_typeReference, cjsidl_state, cjsidl_messageDef, cjsidl_messageRef, cjsidl_messageScopedRef, cjsidl_eventDef, cjsidl_stateMachine, cjsidl_startState, cjsidl_transParams, cjsidl_transParam, cjsidl_defaultState, cjsidl_entry, cjsidl_exit, cjsidl_transition, cjsidl_defaultTransition, cjsidl_actionList, cjsidl_sendActionList, cjsidl_internalTransition, cjsidl_simpleTransition, cjsidl_nextState, cjsidl_pushTransition, cjsidl_scopedEventType, cjsidl_guard, cjsidl_popTransition, cjsidl_guardParam, cjsidl_guardAction, cjsidl_action, cjsidl_fixedLenString, cjsidl_varLenString, cjsidl_varLenField, cjsidl_varFormatField, cjsidl_headerDef, cjsidl_simpleNumericType, cjsidl_arrayDef, cjsidl_recordDef, cjsidl_listDef, cjsidl_variantDef, cjsidl_sequenceDef, cjsidl_fixedFieldDef, cjsidl_varField, cjsidl_bitfieldDef, cjsidl_headerRef, cjsidl_headerScopedRef, cjsidl_bodyRef, cjsidl_bodyScopedRef, cjsidl_bodyDef, cjsidl_footerDef, cjsidl_containerRef, cjsidl_scopedType, cjsidl_declaredEventDef, cjsidl_footerRef, cjsidl_footerScopedRef, cjsidl_containerDef, cjsidl_constReference, cjsidl_scopedConstId, cjsidl_valueSetDef, cjsidl_scaledRangeDef, cjsidl_taggedUnitsEnum, cjsidl_valueSpec, cjsidl_valueRange, cjsidl_formatEnumDef, cjsidl_subField, containerDef, cjsidl_taggedItemDef, FIELD_FORMAT, UNIT},
    associations={typeSet6, messageSet8, internalEventSet10, protocolBehavior12, set0, descr1, refs2, constSet4, typeRef36, scopedRef38, inputSet40, outputSet42, refInherit14, refClient16, importedNamespace19, declaredConstSetRef22, constDef24, importedNamespace26, declaredConstSetRef29, declaredTypeSetRef32, typeDef34, scoped70, state71, scoped74, startState77, messageDefs45, typeRefs47, scopedRefs49, defs51, descr54, header56, body59, footer62, ref65, stateMachine68, sendActions107, actions109, sendActions112, params115, defaultState80, states82, entryAction85, exitAction87, transitions89, defaultTransition91, defaultState93, subState97, transition99, defaultTransition102, actions105, destination147, nextState150, nextState151, type116, scopedEventType119, scoped121, params124, transGuard127, actions129, sendActions132, destination135, transGuard138, actions141, sendActions144, actions177, actions179, param182, simpleTransition153, secondaryTransition156, param158, firstState160, scoped163, nextState166, guardAction169, param171, parameter174, fixedLenString209, varLenString211, varLenField213, varFormatField215, headerDef217, constType185, importedNamespace187, messageDef190, arrayDef193, recordDef195, listDef197, variantDef199, sequenceDef201, fixedFieldDef203, varField205, bitfieldDef207, typeRef244, scopedRef246, typeRef248, bodyDef219, footerDef221, descr223, header226, body229, footer232, recordListSequenceVariant235, recordListSequenceVariant238, recordListSequenceVariant241, type283, typeScoped284, scopedRef250, typeRef252, scopedRef254, name256, names259, type262, name265, names268, type271, name274, names277, type280, upperLimRef301, upperLimScoped304, type307, valueRange310, type286, scopedEventType288, upperLimRef291, upperLimScoped293, lowerLimRef295, lowerLimScoped298, type333, valueSetDef336, scaledRangeDef338, vtagField313, lowerLimRef315, lowerLimScoped318, upperLimRef321, upperLimScoped324, tag327, scopedTag330, lowerLimScoped358, upperLimRef361, upperLimScoped364, countRange340, formatField342, constRef344, constScopedRef347, value350, subField353, lowerLimRef355, minCountRef382, minCountScoped385, lowerLimRef367, lowerLimScoped370, upperLimRef373, upperLimScoped376, valueSet379, containerDef414, containerRef417, containerTypeList420, maxCountRef388, maxCountScoped391, containerRef394, containerDef397, minCountRef400, minCountScoped403, maxCountRef406, maxCountScoped409, itemList412, type456, arrayDef423, fieldDef426, variableFieldDef429, bitfieldDef432, fixedLengthStringDef435, variableLengthStringDef438, variableLengthFieldDef441, varFormatField444, typeReference447, scopedRef450, constVal453, type489, ref492, typeRef459, scopedType462, scope465, scopes468, ref471, name474, names477, type480, name483, names486, name495, names498, type501},
    generalizations={gen_cjsidl_listDef_containerDef, gen_cjsidl_sequenceDef_containerDef, gen_cjsidl_recordDef_containerDef, gen_cjsidl_variantDef_containerDef},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)