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
Direction: Enumeration = Enumeration(
    name="Direction",
    literals={
            EnumerationLiteral(name="inout"),
			EnumerationLiteral(name="in"),
			EnumerationLiteral(name="out")
    }
)

Modifier: Enumeration = Enumeration(
    name="Modifier",
    literals={
            EnumerationLiteral(name="LIFO"),
			EnumerationLiteral(name="FIFO")
    }
)

FunctionLocation: Enumeration = Enumeration(
    name="FunctionLocation",
    literals={
            EnumerationLiteral(name="remote"),
			EnumerationLiteral(name="local")
    }
)

SIPHeader: Enumeration = Enumeration(
    name="SIPHeader",
    literals={
            EnumerationLiteral(name="CALL_ID"),
			EnumerationLiteral(name="CONTACT"),
			EnumerationLiteral(name="CSEQ"),
			EnumerationLiteral(name="EVENT"),
			EnumerationLiteral(name="FROM"),
			EnumerationLiteral(name="MAX_FORWARDS"),
			EnumerationLiteral(name="SUBSCRIPTION_STATE"),
			EnumerationLiteral(name="TO"),
			EnumerationLiteral(name="VIA")
    }
)

SuccessKind: Enumeration = Enumeration(
    name="SuccessKind",
    literals={
            EnumerationLiteral(name="OK"),
			EnumerationLiteral(name="ACCEPTED")
    }
)

ClientErrorKind: Enumeration = Enumeration(
    name="ClientErrorKind",
    literals={
            EnumerationLiteral(name="ADDRESS_INCOMPLETE"),
			EnumerationLiteral(name="AMBIGUOUS"),
			EnumerationLiteral(name="BAD_EXTENSION"),
			EnumerationLiteral(name="BAD_REQUEST"),
			EnumerationLiteral(name="BUSY_HERE"),
			EnumerationLiteral(name="CALL_OR_TRANSACTION_DOES_NOT_EXIST"),
			EnumerationLiteral(name="EXTENSION_REQUIRED"),
			EnumerationLiteral(name="FORBIDDEN"),
			EnumerationLiteral(name="GONE"),
			EnumerationLiteral(name="INTERVAL_TOO_BRIEF"),
			EnumerationLiteral(name="LOOP_DETECTED"),
			EnumerationLiteral(name="METHOD_NOT_ALLOWED"),
			EnumerationLiteral(name="NOT_ACCEPTABLE_HERE"),
			EnumerationLiteral(name="NOT_ACCEPTABLE"),
			EnumerationLiteral(name="NOT_FOUND"),
			EnumerationLiteral(name="PAYMENT_REQUIRED"),
			EnumerationLiteral(name="PROXY_AUTHENTICATION_REQUIRED"),
			EnumerationLiteral(name="REQUESTURI_TOO_LONG"),
			EnumerationLiteral(name="REQUEST_ENTITY_TOO_LARGE"),
			EnumerationLiteral(name="REQUEST_PENDING"),
			EnumerationLiteral(name="REQUEST_TERMINATED"),
			EnumerationLiteral(name="REQUEST_TIMEOUT"),
			EnumerationLiteral(name="TEMPORARILY_UNAVAILABLE"),
			EnumerationLiteral(name="TOO_MANY_HOPS"),
			EnumerationLiteral(name="UNAUTHORIZED"),
			EnumerationLiteral(name="UNDECIPHERABLE"),
			EnumerationLiteral(name="UNSUPPORTED_MEDIA_TYPE"),
			EnumerationLiteral(name="UNSUPPORTED_URI_SCHEME")
    }
)

SIPMethod: Enumeration = Enumeration(
    name="SIPMethod",
    literals={
            EnumerationLiteral(name="ACK"),
			EnumerationLiteral(name="BYE"),
			EnumerationLiteral(name="CANCEL"),
			EnumerationLiteral(name="INVITE"),
			EnumerationLiteral(name="NOTIFY"),
			EnumerationLiteral(name="OPTIONS"),
			EnumerationLiteral(name="REACK"),
			EnumerationLiteral(name="REGISTER"),
			EnumerationLiteral(name="REINVITE"),
			EnumerationLiteral(name="REREGISTER"),
			EnumerationLiteral(name="RESUBSCRIBE"),
			EnumerationLiteral(name="SUBSCRIBE")
    }
)

ControlMethod: Enumeration = Enumeration(
    name="ControlMethod",
    literals={
            EnumerationLiteral(name="deploy"),
			EnumerationLiteral(name="undeploy"),
			EnumerationLiteral(name="uninvite"),
			EnumerationLiteral(name="unregister"),
			EnumerationLiteral(name="unsubscribe")
    }
)

PrimitiveType: Enumeration = Enumeration(
    name="PrimitiveType",
    literals={
            EnumerationLiteral(name="void"),
			EnumerationLiteral(name="bool"),
			EnumerationLiteral(name="int"),
			EnumerationLiteral(name="request"),
			EnumerationLiteral(name="response"),
			EnumerationLiteral(name="string"),
			EnumerationLiteral(name="time"),
			EnumerationLiteral(name="uri")
    }
)

RedirectionErrorKind: Enumeration = Enumeration(
    name="RedirectionErrorKind",
    literals={
            EnumerationLiteral(name="ALTERNATIVE_SERVICE"),
			EnumerationLiteral(name="MOVED_PERMANENTLY"),
			EnumerationLiteral(name="MOVED_TEMPORARILY"),
			EnumerationLiteral(name="MULTIPLE_CHOICES"),
			EnumerationLiteral(name="USE_PROXY")
    }
)

ServerErrorKind: Enumeration = Enumeration(
    name="ServerErrorKind",
    literals={
            EnumerationLiteral(name="BAD_GATEWAY"),
			EnumerationLiteral(name="MESSAGE_TOO_LARGE"),
			EnumerationLiteral(name="NOT_IMPLEMENTED"),
			EnumerationLiteral(name="SERVER_INTERNAL_ERROR"),
			EnumerationLiteral(name="SERVER_TIMEOUT"),
			EnumerationLiteral(name="SERVICE_UNAVAILABLE"),
			EnumerationLiteral(name="VERSION_NOT_SUPPORTED")
    }
)

GlobalErrorKind: Enumeration = Enumeration(
    name="GlobalErrorKind",
    literals={
            EnumerationLiteral(name="BUSY_EVERYWHERE"),
			EnumerationLiteral(name="DECLINE"),
			EnumerationLiteral(name="DOES_NOT_EXIST_ANYWHERE"),
			EnumerationLiteral(name="NOT_ACCEPTABLE")
    }
)

# Classes
jointPackage_CPL2SPL_JointMM = Class(name="jointPackage::CPL2SPL::JointMM")
SrcReject = Class(name="SrcReject")
jointPackage_CPL2SPL_SrcAddressSwitch = Class(name="jointPackage::CPL2SPL::SrcAddressSwitch")
SrcSwitch = Class(name="SrcSwitch")
SrcSwitchedAddress = Class(name="SrcSwitchedAddress")
jointPackage_CPL2SPL_SrcStringSwitch = Class(name="jointPackage::CPL2SPL::SrcStringSwitch")
SrcSwitchedString = Class(name="SrcSwitchedString")
jointPackage_CPL2SPL_SrcLanguageSwitch = Class(name="jointPackage::CPL2SPL::SrcLanguageSwitch")
SrcSwitchedLanguage = Class(name="SrcSwitchedLanguage")
jointPackage_CPL2SPL_SrcTimeSwitch = Class(name="jointPackage::CPL2SPL::SrcTimeSwitch")
SrcSwitchedTime = Class(name="SrcSwitchedTime")
jointPackage_CPL2SPL_SrcPrioritySwitch = Class(name="jointPackage::CPL2SPL::SrcPrioritySwitch")
SrcSwitchedPriority = Class(name="SrcSwitchedPriority")
TrgServerErrorResponse = Class(name="TrgServerErrorResponse")
jointPackage_CPL2SPL_SrcCPLModel = Class(name="jointPackage::CPL2SPL::SrcCPLModel")
SrcElement = Class(name="SrcElement")
jointPackage_CPL2SPL_SrcCPL = Class(name="jointPackage::CPL2SPL::SrcCPL")
SrcSubAction = Class(name="SrcSubAction")
SrcOutgoing = Class(name="SrcOutgoing")
SrcIncoming = Class(name="SrcIncoming")
SrcDefault = Class(name="SrcDefault")
jointPackage_CPL2SPL_SrcRedirect = Class(name="jointPackage::CPL2SPL::SrcRedirect")
jointPackage_CPL2SPL_SrcReject = Class(name="jointPackage::CPL2SPL::SrcReject")
jointPackage_CPL2SPL_SrcElement = Class(name="jointPackage::CPL2SPL::SrcElement", is_abstract=True)
jointPackage_CPL2SPL_SrcNodeContainer = Class(name="jointPackage::CPL2SPL::SrcNodeContainer", is_abstract=True)
SrcNode = Class(name="SrcNode")
jointPackage_CPL2SPL_SrcSubAction = Class(name="jointPackage::CPL2SPL::SrcSubAction")
SrcNodeContainer = Class(name="SrcNodeContainer")
jointPackage_CPL2SPL_SrcOutgoing = Class(name="jointPackage::CPL2SPL::SrcOutgoing")
jointPackage_CPL2SPL_SrcIncoming = Class(name="jointPackage::CPL2SPL::SrcIncoming")
jointPackage_CPL2SPL_SrcNotPresent = Class(name="jointPackage::CPL2SPL::SrcNotPresent")
jointPackage_CPL2SPL_SrcOtherwise = Class(name="jointPackage::CPL2SPL::SrcOtherwise")
jointPackage_CPL2SPL_SrcSwitchedAddress = Class(name="jointPackage::CPL2SPL::SrcSwitchedAddress")
jointPackage_CPL2SPL_SrcProxy = Class(name="jointPackage::CPL2SPL::SrcProxy")
SrcSignallingAction = Class(name="SrcSignallingAction")
SrcBusy = Class(name="SrcBusy")
SrcNoAnswer = Class(name="SrcNoAnswer")
SrcRedirection = Class(name="SrcRedirection")
SrcFailure = Class(name="SrcFailure")
jointPackage_CPL2SPL_SrcSwitchedPriority = Class(name="jointPackage::CPL2SPL::SrcSwitchedPriority")
jointPackage_CPL2SPL_SrcBusy = Class(name="jointPackage::CPL2SPL::SrcBusy")
jointPackage_CPL2SPL_SrcSwitchedString = Class(name="jointPackage::CPL2SPL::SrcSwitchedString")
jointPackage_CPL2SPL_SrcSwitchedLanguage = Class(name="jointPackage::CPL2SPL::SrcSwitchedLanguage")
jointPackage_CPL2SPL_SrcSwitchedTime = Class(name="jointPackage::CPL2SPL::SrcSwitchedTime")
jointPackage_CPL2SPL_SrcSubCall = Class(name="jointPackage::CPL2SPL::SrcSubCall")
jointPackage_CPL2SPL_SrcAction = Class(name="jointPackage::CPL2SPL::SrcAction", is_abstract=True)
jointPackage_CPL2SPL_SrcSignallingAction = Class(name="jointPackage::CPL2SPL::SrcSignallingAction", is_abstract=True)
SrcAction = Class(name="SrcAction")
jointPackage_CPL2SPL_TrgProgram = Class(name="jointPackage::CPL2SPL::TrgProgram")
TrgLocatedElement = Class(name="TrgLocatedElement")
TrgService = Class(name="TrgService")
jointPackage_CPL2SPL_TrgStructureProperty = Class(name="jointPackage::CPL2SPL::TrgStructureProperty")
TrgTypeExpression = Class(name="TrgTypeExpression")
jointPackage_CPL2SPL_TrgClientErrorResponse = Class(name="jointPackage::CPL2SPL::TrgClientErrorResponse")
TrgErrorResponse = Class(name="TrgErrorResponse")
jointPackage_CPL2SPL_TrgGlobalErrorResponse = Class(name="jointPackage::CPL2SPL::TrgGlobalErrorResponse")
jointPackage_CPL2SPL_SrcNoAnswer = Class(name="jointPackage::CPL2SPL::SrcNoAnswer")
jointPackage_CPL2SPL_SrcRedirection = Class(name="jointPackage::CPL2SPL::SrcRedirection")
jointPackage_CPL2SPL_SrcFailure = Class(name="jointPackage::CPL2SPL::SrcFailure")
jointPackage_CPL2SPL_SrcDefault = Class(name="jointPackage::CPL2SPL::SrcDefault")
jointPackage_CPL2SPL_SrcNode = Class(name="jointPackage::CPL2SPL::SrcNode", is_abstract=True)
jointPackage_CPL2SPL_SrcSwitch = Class(name="jointPackage::CPL2SPL::SrcSwitch", is_abstract=True)
SrcNotPresent = Class(name="SrcNotPresent")
SrcOtherwise = Class(name="SrcOtherwise")
jointPackage_CPL2SPL_SrcLocation = Class(name="jointPackage::CPL2SPL::SrcLocation")
jointPackage_CPL2SPL_TrgSession = Class(name="jointPackage::CPL2SPL::TrgSession", is_abstract=True)
jointPackage_CPL2SPL_TrgRegistration = Class(name="jointPackage::CPL2SPL::TrgRegistration")
jointPackage_CPL2SPL_TrgDialog = Class(name="jointPackage::CPL2SPL::TrgDialog")
TrgMethod = Class(name="TrgMethod")
jointPackage_CPL2SPL_TrgEvent = Class(name="jointPackage::CPL2SPL::TrgEvent")
jointPackage_CPL2SPL_TrgMethod = Class(name="jointPackage::CPL2SPL::TrgMethod")
jointPackage_CPL2SPL_TrgRedirectionErrorResponse = Class(name="jointPackage::CPL2SPL::TrgRedirectionErrorResponse")
jointPackage_CPL2SPL_TrgServerErrorResponse = Class(name="jointPackage::CPL2SPL::TrgServerErrorResponse")
jointPackage_CPL2SPL_TrgLocatedElement = Class(name="jointPackage::CPL2SPL::TrgLocatedElement", is_abstract=True)
jointPackage_CPL2SPL_TrgService = Class(name="jointPackage::CPL2SPL::TrgService")
TrgDeclaration = Class(name="TrgDeclaration")
TrgSession = Class(name="TrgSession")
jointPackage_CPL2SPL_TrgMethodName = Class(name="jointPackage::CPL2SPL::TrgMethodName", is_abstract=True)
jointPackage_CPL2SPL_TrgSIPMethodName = Class(name="jointPackage::CPL2SPL::TrgSIPMethodName")
jointPackage_CPL2SPL_TrgControlMethodName = Class(name="jointPackage::CPL2SPL::TrgControlMethodName")
jointPackage_CPL2SPL_TrgBranch = Class(name="jointPackage::CPL2SPL::TrgBranch")
jointPackage_CPL2SPL_TrgDefaultBranch = Class(name="jointPackage::CPL2SPL::TrgDefaultBranch")
jointPackage_CPL2SPL_TrgNamedBranch = Class(name="jointPackage::CPL2SPL::TrgNamedBranch")
jointPackage_CPL2SPL_TrgTypeExpression = Class(name="jointPackage::CPL2SPL::TrgTypeExpression", is_abstract=True)
jointPackage_CPL2SPL_TrgSimpleType = Class(name="jointPackage::CPL2SPL::TrgSimpleType")
jointPackage_CPL2SPL_TrgSequenceType = Class(name="jointPackage::CPL2SPL::TrgSequenceType")
jointPackage_CPL2SPL_TrgDefinedType = Class(name="jointPackage::CPL2SPL::TrgDefinedType")
jointPackage_CPL2SPL_TrgDeclaration = Class(name="jointPackage::CPL2SPL::TrgDeclaration", is_abstract=True)
TrgMethodName = Class(name="TrgMethodName")
TrgArgument = Class(name="TrgArgument")
TrgStatement = Class(name="TrgStatement")
TrgBranch = Class(name="TrgBranch")
jointPackage_CPL2SPL_TrgArgument = Class(name="jointPackage::CPL2SPL::TrgArgument")
TrgVariableDeclaration = Class(name="TrgVariableDeclaration")
jointPackage_CPL2SPL_TrgRemoteFunctionDeclaration = Class(name="jointPackage::CPL2SPL::TrgRemoteFunctionDeclaration")
TrgFunctionDeclaration = Class(name="TrgFunctionDeclaration")
jointPackage_CPL2SPL_TrgLocalFunctionDeclaration = Class(name="jointPackage::CPL2SPL::TrgLocalFunctionDeclaration")
jointPackage_CPL2SPL_TrgStructureDeclaration = Class(name="jointPackage::CPL2SPL::TrgStructureDeclaration")
jointPackage_CPL2SPL_TrgFunctionCall = Class(name="jointPackage::CPL2SPL::TrgFunctionCall")
jointPackage_CPL2SPL_TrgVariableDeclaration = Class(name="jointPackage::CPL2SPL::TrgVariableDeclaration")
TrgExpression = Class(name="TrgExpression")
jointPackage_CPL2SPL_TrgFunctionDeclaration = Class(name="jointPackage::CPL2SPL::TrgFunctionDeclaration", is_abstract=True)
TrgPlace = Class(name="TrgPlace")
jointPackage_CPL2SPL_TrgDeclarationStat = Class(name="jointPackage::CPL2SPL::TrgDeclarationStat")
jointPackage_CPL2SPL_TrgReturnStat = Class(name="jointPackage::CPL2SPL::TrgReturnStat")
TrgNamedBranch = Class(name="TrgNamedBranch")
jointPackage_CPL2SPL_TrgIfStat = Class(name="jointPackage::CPL2SPL::TrgIfStat")
jointPackage_CPL2SPL_TrgStatement = Class(name="jointPackage::CPL2SPL::TrgStatement", is_abstract=True)
jointPackage_CPL2SPL_TrgCompoundStat = Class(name="jointPackage::CPL2SPL::TrgCompoundStat")
jointPackage_CPL2SPL_TrgSetStat = Class(name="jointPackage::CPL2SPL::TrgSetStat")
jointPackage_CPL2SPL_TrgForeachStat = Class(name="jointPackage::CPL2SPL::TrgForeachStat")
jointPackage_CPL2SPL_TrgSelectStat = Class(name="jointPackage::CPL2SPL::TrgSelectStat")
TrgSelectCase = Class(name="TrgSelectCase")
TrgSelectDefault = Class(name="TrgSelectDefault")
jointPackage_CPL2SPL_TrgFunctionCallStat = Class(name="jointPackage::CPL2SPL::TrgFunctionCallStat")
jointPackage_CPL2SPL_TrgWhenStat = Class(name="jointPackage::CPL2SPL::TrgWhenStat")
TrgVariable = Class(name="TrgVariable")
TrgWhenHeader = Class(name="TrgWhenHeader")
TrgConstant = Class(name="TrgConstant")
jointPackage_CPL2SPL_TrgSelectMember = Class(name="jointPackage::CPL2SPL::TrgSelectMember", is_abstract=True)
jointPackage_CPL2SPL_TrgSelectDefault = Class(name="jointPackage::CPL2SPL::TrgSelectDefault")
TrgSelectMember = Class(name="TrgSelectMember")
jointPackage_CPL2SPL_TrgSelectCase = Class(name="jointPackage::CPL2SPL::TrgSelectCase")
jointPackage_CPL2SPL_TrgExpression = Class(name="jointPackage::CPL2SPL::TrgExpression", is_abstract=True)
jointPackage_CPL2SPL_TrgConstantExp = Class(name="jointPackage::CPL2SPL::TrgConstantExp")
TrgFunctionCall = Class(name="TrgFunctionCall")
jointPackage_CPL2SPL_TrgContinueStat = Class(name="jointPackage::CPL2SPL::TrgContinueStat")
jointPackage_CPL2SPL_TrgBreakStat = Class(name="jointPackage::CPL2SPL::TrgBreakStat")
jointPackage_CPL2SPL_TrgPushStat = Class(name="jointPackage::CPL2SPL::TrgPushStat")
jointPackage_CPL2SPL_TrgWhenHeader = Class(name="jointPackage::CPL2SPL::TrgWhenHeader")
jointPackage_CPL2SPL_TrgForwardExp = Class(name="jointPackage::CPL2SPL::TrgForwardExp")
jointPackage_CPL2SPL_TrgWithExp = Class(name="jointPackage::CPL2SPL::TrgWithExp")
jointPackage_CPL2SPL_TrgOperatorExp = Class(name="jointPackage::CPL2SPL::TrgOperatorExp")
jointPackage_CPL2SPL_TrgReasonExp = Class(name="jointPackage::CPL2SPL::TrgReasonExp")
jointPackage_CPL2SPL_TrgBODYExp = Class(name="jointPackage::CPL2SPL::TrgBODYExp")
jointPackage_CPL2SPL_TrgRequestURIExp = Class(name="jointPackage::CPL2SPL::TrgRequestURIExp")
jointPackage_CPL2SPL_TrgPopExp = Class(name="jointPackage::CPL2SPL::TrgPopExp")
jointPackage_CPL2SPL_TrgFunctionCallExp = Class(name="jointPackage::CPL2SPL::TrgFunctionCallExp")
TrgMessageField = Class(name="TrgMessageField")
jointPackage_CPL2SPL_TrgBlockExp = Class(name="jointPackage::CPL2SPL::TrgBlockExp")
jointPackage_CPL2SPL_TrgVariablePlace = Class(name="jointPackage::CPL2SPL::TrgVariablePlace", is_abstract=True)
jointPackage_CPL2SPL_TrgPropertyCallPlace = Class(name="jointPackage::CPL2SPL::TrgPropertyCallPlace")
TrgVariablePlace = Class(name="TrgVariablePlace")
jointPackage_CPL2SPL_TrgVariable = Class(name="jointPackage::CPL2SPL::TrgVariable")
jointPackage_CPL2SPL_TrgMessageField = Class(name="jointPackage::CPL2SPL::TrgMessageField", is_abstract=True)
jointPackage_CPL2SPL_TrgPlace = Class(name="jointPackage::CPL2SPL::TrgPlace", is_abstract=True)
jointPackage_CPL2SPL_TrgSIPHeaderPlace = Class(name="jointPackage::CPL2SPL::TrgSIPHeaderPlace")
jointPackage_CPL2SPL_TrgBooleanConstant = Class(name="jointPackage::CPL2SPL::TrgBooleanConstant")
jointPackage_CPL2SPL_TrgIntegerConstant = Class(name="jointPackage::CPL2SPL::TrgIntegerConstant")
jointPackage_CPL2SPL_TrgStringConstant = Class(name="jointPackage::CPL2SPL::TrgStringConstant")
jointPackage_CPL2SPL_TrgURIConstant = Class(name="jointPackage::CPL2SPL::TrgURIConstant")
jointPackage_CPL2SPL_TrgSequenceConstant = Class(name="jointPackage::CPL2SPL::TrgSequenceConstant")
jointPackage_CPL2SPL_TrgResponseConstant = Class(name="jointPackage::CPL2SPL::TrgResponseConstant")
TrgResponse = Class(name="TrgResponse")
jointPackage_CPL2SPL_TrgResponse = Class(name="jointPackage::CPL2SPL::TrgResponse", is_abstract=True)
jointPackage_CPL2SPL_TrgSuccessResponse = Class(name="jointPackage::CPL2SPL::TrgSuccessResponse")
jointPackage_CPL2SPL_TrgErrorResponse = Class(name="jointPackage::CPL2SPL::TrgErrorResponse")
jointPackage_CPL2SPL_TrgReasonMessageField = Class(name="jointPackage::CPL2SPL::TrgReasonMessageField")
jointPackage_CPL2SPL_TrgHeadedMessageField = Class(name="jointPackage::CPL2SPL::TrgHeadedMessageField")
jointPackage_CPL2SPL_TrgConstant = Class(name="jointPackage::CPL2SPL::TrgConstant", is_abstract=True)

# jointPackage_CPL2SPL_JointMM class attributes and methods

# SrcReject class attributes and methods

# jointPackage_CPL2SPL_SrcAddressSwitch class attributes and methods
jointPackage_CPL2SPL_SrcAddressSwitch_field: Property = Property(name="field", type=StringType)
jointPackage_CPL2SPL_SrcAddressSwitch_subField: Property = Property(name="subField", type=StringType)
jointPackage_CPL2SPL_SrcAddressSwitch.attributes={jointPackage_CPL2SPL_SrcAddressSwitch_subField, jointPackage_CPL2SPL_SrcAddressSwitch_field}

# SrcSwitch class attributes and methods

# SrcSwitchedAddress class attributes and methods

# jointPackage_CPL2SPL_SrcStringSwitch class attributes and methods
jointPackage_CPL2SPL_SrcStringSwitch_field: Property = Property(name="field", type=StringType)
jointPackage_CPL2SPL_SrcStringSwitch.attributes={jointPackage_CPL2SPL_SrcStringSwitch_field}

# SrcSwitchedString class attributes and methods

# jointPackage_CPL2SPL_SrcLanguageSwitch class attributes and methods

# SrcSwitchedLanguage class attributes and methods

# jointPackage_CPL2SPL_SrcTimeSwitch class attributes and methods
jointPackage_CPL2SPL_SrcTimeSwitch_tzid: Property = Property(name="tzid", type=StringType)
jointPackage_CPL2SPL_SrcTimeSwitch_tzurl: Property = Property(name="tzurl", type=StringType)
jointPackage_CPL2SPL_SrcTimeSwitch.attributes={jointPackage_CPL2SPL_SrcTimeSwitch_tzurl, jointPackage_CPL2SPL_SrcTimeSwitch_tzid}

# SrcSwitchedTime class attributes and methods

# jointPackage_CPL2SPL_SrcPrioritySwitch class attributes and methods

# SrcSwitchedPriority class attributes and methods

# TrgServerErrorResponse class attributes and methods

# jointPackage_CPL2SPL_SrcCPLModel class attributes and methods

# SrcElement class attributes and methods

# jointPackage_CPL2SPL_SrcCPL class attributes and methods

# SrcSubAction class attributes and methods

# SrcOutgoing class attributes and methods

# SrcIncoming class attributes and methods

# SrcDefault class attributes and methods

# jointPackage_CPL2SPL_SrcRedirect class attributes and methods
jointPackage_CPL2SPL_SrcRedirect_permanent: Property = Property(name="permanent", type=StringType)
jointPackage_CPL2SPL_SrcRedirect.attributes={jointPackage_CPL2SPL_SrcRedirect_permanent}

# jointPackage_CPL2SPL_SrcReject class attributes and methods
jointPackage_CPL2SPL_SrcReject_status: Property = Property(name="status", type=StringType)
jointPackage_CPL2SPL_SrcReject_reason: Property = Property(name="reason", type=StringType)
jointPackage_CPL2SPL_SrcReject.attributes={jointPackage_CPL2SPL_SrcReject_status, jointPackage_CPL2SPL_SrcReject_reason}

# jointPackage_CPL2SPL_SrcElement class attributes and methods

# jointPackage_CPL2SPL_SrcNodeContainer class attributes and methods

# SrcNode class attributes and methods

# jointPackage_CPL2SPL_SrcSubAction class attributes and methods
jointPackage_CPL2SPL_SrcSubAction_id: Property = Property(name="id", type=StringType)
jointPackage_CPL2SPL_SrcSubAction.attributes={jointPackage_CPL2SPL_SrcSubAction_id}

# SrcNodeContainer class attributes and methods

# jointPackage_CPL2SPL_SrcOutgoing class attributes and methods

# jointPackage_CPL2SPL_SrcIncoming class attributes and methods

# jointPackage_CPL2SPL_SrcNotPresent class attributes and methods

# jointPackage_CPL2SPL_SrcOtherwise class attributes and methods

# jointPackage_CPL2SPL_SrcSwitchedAddress class attributes and methods
jointPackage_CPL2SPL_SrcSwitchedAddress_is: Property = Property(name="is", type=StringType)
jointPackage_CPL2SPL_SrcSwitchedAddress_contains: Property = Property(name="contains", type=StringType)
jointPackage_CPL2SPL_SrcSwitchedAddress_subDomainOf: Property = Property(name="subDomainOf", type=StringType)
jointPackage_CPL2SPL_SrcSwitchedAddress.attributes={jointPackage_CPL2SPL_SrcSwitchedAddress_subDomainOf, jointPackage_CPL2SPL_SrcSwitchedAddress_contains, jointPackage_CPL2SPL_SrcSwitchedAddress_is}

# jointPackage_CPL2SPL_SrcProxy class attributes and methods
jointPackage_CPL2SPL_SrcProxy_timeout: Property = Property(name="timeout", type=StringType)
jointPackage_CPL2SPL_SrcProxy_recurse: Property = Property(name="recurse", type=StringType)
jointPackage_CPL2SPL_SrcProxy_ordering: Property = Property(name="ordering", type=StringType)
jointPackage_CPL2SPL_SrcProxy.attributes={jointPackage_CPL2SPL_SrcProxy_timeout, jointPackage_CPL2SPL_SrcProxy_recurse, jointPackage_CPL2SPL_SrcProxy_ordering}

# SrcSignallingAction class attributes and methods

# SrcBusy class attributes and methods

# SrcNoAnswer class attributes and methods

# SrcRedirection class attributes and methods

# SrcFailure class attributes and methods

# jointPackage_CPL2SPL_SrcSwitchedPriority class attributes and methods
jointPackage_CPL2SPL_SrcSwitchedPriority_less: Property = Property(name="less", type=StringType)
jointPackage_CPL2SPL_SrcSwitchedPriority_greater: Property = Property(name="greater", type=StringType)
jointPackage_CPL2SPL_SrcSwitchedPriority_equal: Property = Property(name="equal", type=StringType)
jointPackage_CPL2SPL_SrcSwitchedPriority.attributes={jointPackage_CPL2SPL_SrcSwitchedPriority_equal, jointPackage_CPL2SPL_SrcSwitchedPriority_greater, jointPackage_CPL2SPL_SrcSwitchedPriority_less}

# jointPackage_CPL2SPL_SrcBusy class attributes and methods

# jointPackage_CPL2SPL_SrcSwitchedString class attributes and methods
jointPackage_CPL2SPL_SrcSwitchedString_is: Property = Property(name="is", type=StringType)
jointPackage_CPL2SPL_SrcSwitchedString_contains: Property = Property(name="contains", type=StringType)
jointPackage_CPL2SPL_SrcSwitchedString.attributes={jointPackage_CPL2SPL_SrcSwitchedString_is, jointPackage_CPL2SPL_SrcSwitchedString_contains}

# jointPackage_CPL2SPL_SrcSwitchedLanguage class attributes and methods
jointPackage_CPL2SPL_SrcSwitchedLanguage_matches: Property = Property(name="matches", type=StringType)
jointPackage_CPL2SPL_SrcSwitchedLanguage.attributes={jointPackage_CPL2SPL_SrcSwitchedLanguage_matches}

# jointPackage_CPL2SPL_SrcSwitchedTime class attributes and methods
jointPackage_CPL2SPL_SrcSwitchedTime_duration: Property = Property(name="duration", type=StringType)
jointPackage_CPL2SPL_SrcSwitchedTime_freq: Property = Property(name="freq", type=StringType)
jointPackage_CPL2SPL_SrcSwitchedTime_until: Property = Property(name="until", type=StringType)
jointPackage_CPL2SPL_SrcSwitchedTime_count: Property = Property(name="count", type=StringType)
jointPackage_CPL2SPL_SrcSwitchedTime_interval: Property = Property(name="interval", type=StringType)
jointPackage_CPL2SPL_SrcSwitchedTime_bySecond: Property = Property(name="bySecond", type=StringType)
jointPackage_CPL2SPL_SrcSwitchedTime_byMinute: Property = Property(name="byMinute", type=StringType)
jointPackage_CPL2SPL_SrcSwitchedTime_byHour: Property = Property(name="byHour", type=StringType)
jointPackage_CPL2SPL_SrcSwitchedTime_byDay: Property = Property(name="byDay", type=StringType)
jointPackage_CPL2SPL_SrcSwitchedTime_byMonthDay: Property = Property(name="byMonthDay", type=StringType)
jointPackage_CPL2SPL_SrcSwitchedTime_byYearDay: Property = Property(name="byYearDay", type=StringType)
jointPackage_CPL2SPL_SrcSwitchedTime_byWeekNo: Property = Property(name="byWeekNo", type=StringType)
jointPackage_CPL2SPL_SrcSwitchedTime_byMonth: Property = Property(name="byMonth", type=StringType)
jointPackage_CPL2SPL_SrcSwitchedTime_wkst: Property = Property(name="wkst", type=StringType)
jointPackage_CPL2SPL_SrcSwitchedTime_bySetPos: Property = Property(name="bySetPos", type=StringType)
jointPackage_CPL2SPL_SrcSwitchedTime_dtstart: Property = Property(name="dtstart", type=StringType)
jointPackage_CPL2SPL_SrcSwitchedTime_dtend: Property = Property(name="dtend", type=StringType)
jointPackage_CPL2SPL_SrcSwitchedTime.attributes={jointPackage_CPL2SPL_SrcSwitchedTime_dtstart, jointPackage_CPL2SPL_SrcSwitchedTime_byYearDay, jointPackage_CPL2SPL_SrcSwitchedTime_byMonth, jointPackage_CPL2SPL_SrcSwitchedTime_freq, jointPackage_CPL2SPL_SrcSwitchedTime_dtend, jointPackage_CPL2SPL_SrcSwitchedTime_byWeekNo, jointPackage_CPL2SPL_SrcSwitchedTime_byMinute, jointPackage_CPL2SPL_SrcSwitchedTime_byDay, jointPackage_CPL2SPL_SrcSwitchedTime_count, jointPackage_CPL2SPL_SrcSwitchedTime_byMonthDay, jointPackage_CPL2SPL_SrcSwitchedTime_byHour, jointPackage_CPL2SPL_SrcSwitchedTime_bySetPos, jointPackage_CPL2SPL_SrcSwitchedTime_until, jointPackage_CPL2SPL_SrcSwitchedTime_wkst, jointPackage_CPL2SPL_SrcSwitchedTime_interval, jointPackage_CPL2SPL_SrcSwitchedTime_bySecond, jointPackage_CPL2SPL_SrcSwitchedTime_duration}

# jointPackage_CPL2SPL_SrcSubCall class attributes and methods
jointPackage_CPL2SPL_SrcSubCall_ref: Property = Property(name="ref", type=StringType)
jointPackage_CPL2SPL_SrcSubCall.attributes={jointPackage_CPL2SPL_SrcSubCall_ref}

# jointPackage_CPL2SPL_SrcAction class attributes and methods

# jointPackage_CPL2SPL_SrcSignallingAction class attributes and methods

# SrcAction class attributes and methods

# jointPackage_CPL2SPL_TrgProgram class attributes and methods

# TrgLocatedElement class attributes and methods

# TrgService class attributes and methods

# jointPackage_CPL2SPL_TrgStructureProperty class attributes and methods
jointPackage_CPL2SPL_TrgStructureProperty_name: Property = Property(name="name", type=StringType)
jointPackage_CPL2SPL_TrgStructureProperty.attributes={jointPackage_CPL2SPL_TrgStructureProperty_name}

# TrgTypeExpression class attributes and methods

# jointPackage_CPL2SPL_TrgClientErrorResponse class attributes and methods
jointPackage_CPL2SPL_TrgClientErrorResponse_errorKind: Property = Property(name="errorKind", type=StringType)
jointPackage_CPL2SPL_TrgClientErrorResponse.attributes={jointPackage_CPL2SPL_TrgClientErrorResponse_errorKind}

# TrgErrorResponse class attributes and methods

# jointPackage_CPL2SPL_TrgGlobalErrorResponse class attributes and methods
jointPackage_CPL2SPL_TrgGlobalErrorResponse_errorKind: Property = Property(name="errorKind", type=StringType)
jointPackage_CPL2SPL_TrgGlobalErrorResponse.attributes={jointPackage_CPL2SPL_TrgGlobalErrorResponse_errorKind}

# jointPackage_CPL2SPL_SrcNoAnswer class attributes and methods

# jointPackage_CPL2SPL_SrcRedirection class attributes and methods

# jointPackage_CPL2SPL_SrcFailure class attributes and methods

# jointPackage_CPL2SPL_SrcDefault class attributes and methods

# jointPackage_CPL2SPL_SrcNode class attributes and methods

# jointPackage_CPL2SPL_SrcSwitch class attributes and methods

# SrcNotPresent class attributes and methods

# SrcOtherwise class attributes and methods

# jointPackage_CPL2SPL_SrcLocation class attributes and methods
jointPackage_CPL2SPL_SrcLocation_url: Property = Property(name="url", type=StringType)
jointPackage_CPL2SPL_SrcLocation_priority: Property = Property(name="priority", type=StringType)
jointPackage_CPL2SPL_SrcLocation_clear: Property = Property(name="clear", type=StringType)
jointPackage_CPL2SPL_SrcLocation.attributes={jointPackage_CPL2SPL_SrcLocation_clear, jointPackage_CPL2SPL_SrcLocation_priority, jointPackage_CPL2SPL_SrcLocation_url}

# jointPackage_CPL2SPL_TrgSession class attributes and methods

# jointPackage_CPL2SPL_TrgRegistration class attributes and methods

# jointPackage_CPL2SPL_TrgDialog class attributes and methods

# TrgMethod class attributes and methods

# jointPackage_CPL2SPL_TrgEvent class attributes and methods
jointPackage_CPL2SPL_TrgEvent_eventId: Property = Property(name="eventId", type=StringType)
jointPackage_CPL2SPL_TrgEvent.attributes={jointPackage_CPL2SPL_TrgEvent_eventId}

# jointPackage_CPL2SPL_TrgMethod class attributes and methods
jointPackage_CPL2SPL_TrgMethod_direction: Property = Property(name="direction", type=StringType)
jointPackage_CPL2SPL_TrgMethod.attributes={jointPackage_CPL2SPL_TrgMethod_direction}

# jointPackage_CPL2SPL_TrgRedirectionErrorResponse class attributes and methods
jointPackage_CPL2SPL_TrgRedirectionErrorResponse_errorKind: Property = Property(name="errorKind", type=StringType)
jointPackage_CPL2SPL_TrgRedirectionErrorResponse.attributes={jointPackage_CPL2SPL_TrgRedirectionErrorResponse_errorKind}

# jointPackage_CPL2SPL_TrgServerErrorResponse class attributes and methods
jointPackage_CPL2SPL_TrgServerErrorResponse_errorKind: Property = Property(name="errorKind", type=StringType)
jointPackage_CPL2SPL_TrgServerErrorResponse.attributes={jointPackage_CPL2SPL_TrgServerErrorResponse_errorKind}

# jointPackage_CPL2SPL_TrgLocatedElement class attributes and methods
jointPackage_CPL2SPL_TrgLocatedElement_location: Property = Property(name="location", type=StringType)
jointPackage_CPL2SPL_TrgLocatedElement_commentsBefore: Property = Property(name="commentsBefore", type=StringType)
jointPackage_CPL2SPL_TrgLocatedElement_commentsAfter: Property = Property(name="commentsAfter", type=StringType)
jointPackage_CPL2SPL_TrgLocatedElement.attributes={jointPackage_CPL2SPL_TrgLocatedElement_commentsAfter, jointPackage_CPL2SPL_TrgLocatedElement_commentsBefore, jointPackage_CPL2SPL_TrgLocatedElement_location}

# jointPackage_CPL2SPL_TrgService class attributes and methods
jointPackage_CPL2SPL_TrgService_name: Property = Property(name="name", type=StringType)
jointPackage_CPL2SPL_TrgService.attributes={jointPackage_CPL2SPL_TrgService_name}

# TrgDeclaration class attributes and methods

# TrgSession class attributes and methods

# jointPackage_CPL2SPL_TrgMethodName class attributes and methods

# jointPackage_CPL2SPL_TrgSIPMethodName class attributes and methods
jointPackage_CPL2SPL_TrgSIPMethodName_name: Property = Property(name="name", type=StringType)
jointPackage_CPL2SPL_TrgSIPMethodName.attributes={jointPackage_CPL2SPL_TrgSIPMethodName_name}

# jointPackage_CPL2SPL_TrgControlMethodName class attributes and methods
jointPackage_CPL2SPL_TrgControlMethodName_name: Property = Property(name="name", type=StringType)
jointPackage_CPL2SPL_TrgControlMethodName.attributes={jointPackage_CPL2SPL_TrgControlMethodName_name}

# jointPackage_CPL2SPL_TrgBranch class attributes and methods

# jointPackage_CPL2SPL_TrgDefaultBranch class attributes and methods

# jointPackage_CPL2SPL_TrgNamedBranch class attributes and methods
jointPackage_CPL2SPL_TrgNamedBranch_name: Property = Property(name="name", type=StringType)
jointPackage_CPL2SPL_TrgNamedBranch.attributes={jointPackage_CPL2SPL_TrgNamedBranch_name}

# jointPackage_CPL2SPL_TrgTypeExpression class attributes and methods

# jointPackage_CPL2SPL_TrgSimpleType class attributes and methods
jointPackage_CPL2SPL_TrgSimpleType_type: Property = Property(name="type", type=StringType)
jointPackage_CPL2SPL_TrgSimpleType.attributes={jointPackage_CPL2SPL_TrgSimpleType_type}

# jointPackage_CPL2SPL_TrgSequenceType class attributes and methods
jointPackage_CPL2SPL_TrgSequenceType_modifier: Property = Property(name="modifier", type=StringType)
jointPackage_CPL2SPL_TrgSequenceType_type: Property = Property(name="type", type=StringType)
jointPackage_CPL2SPL_TrgSequenceType_size: Property = Property(name="size", type=IntegerType)
jointPackage_CPL2SPL_TrgSequenceType.attributes={jointPackage_CPL2SPL_TrgSequenceType_type, jointPackage_CPL2SPL_TrgSequenceType_modifier, jointPackage_CPL2SPL_TrgSequenceType_size}

# jointPackage_CPL2SPL_TrgDefinedType class attributes and methods
jointPackage_CPL2SPL_TrgDefinedType_typeName: Property = Property(name="typeName", type=StringType)
jointPackage_CPL2SPL_TrgDefinedType.attributes={jointPackage_CPL2SPL_TrgDefinedType_typeName}

# jointPackage_CPL2SPL_TrgDeclaration class attributes and methods
jointPackage_CPL2SPL_TrgDeclaration_name: Property = Property(name="name", type=StringType)
jointPackage_CPL2SPL_TrgDeclaration.attributes={jointPackage_CPL2SPL_TrgDeclaration_name}

# TrgMethodName class attributes and methods

# TrgArgument class attributes and methods

# TrgStatement class attributes and methods

# TrgBranch class attributes and methods

# jointPackage_CPL2SPL_TrgArgument class attributes and methods

# TrgVariableDeclaration class attributes and methods

# jointPackage_CPL2SPL_TrgRemoteFunctionDeclaration class attributes and methods
jointPackage_CPL2SPL_TrgRemoteFunctionDeclaration_functionLocation: Property = Property(name="functionLocation", type=StringType)
jointPackage_CPL2SPL_TrgRemoteFunctionDeclaration.attributes={jointPackage_CPL2SPL_TrgRemoteFunctionDeclaration_functionLocation}

# TrgFunctionDeclaration class attributes and methods

# jointPackage_CPL2SPL_TrgLocalFunctionDeclaration class attributes and methods

# jointPackage_CPL2SPL_TrgStructureDeclaration class attributes and methods

# jointPackage_CPL2SPL_TrgFunctionCall class attributes and methods

# jointPackage_CPL2SPL_TrgVariableDeclaration class attributes and methods

# TrgExpression class attributes and methods

# jointPackage_CPL2SPL_TrgFunctionDeclaration class attributes and methods

# TrgPlace class attributes and methods

# jointPackage_CPL2SPL_TrgDeclarationStat class attributes and methods

# jointPackage_CPL2SPL_TrgReturnStat class attributes and methods

# TrgNamedBranch class attributes and methods

# jointPackage_CPL2SPL_TrgIfStat class attributes and methods

# jointPackage_CPL2SPL_TrgStatement class attributes and methods

# jointPackage_CPL2SPL_TrgCompoundStat class attributes and methods

# jointPackage_CPL2SPL_TrgSetStat class attributes and methods

# jointPackage_CPL2SPL_TrgForeachStat class attributes and methods
jointPackage_CPL2SPL_TrgForeachStat_iteratorName: Property = Property(name="iteratorName", type=StringType)
jointPackage_CPL2SPL_TrgForeachStat.attributes={jointPackage_CPL2SPL_TrgForeachStat_iteratorName}

# jointPackage_CPL2SPL_TrgSelectStat class attributes and methods

# TrgSelectCase class attributes and methods

# TrgSelectDefault class attributes and methods

# jointPackage_CPL2SPL_TrgFunctionCallStat class attributes and methods

# jointPackage_CPL2SPL_TrgWhenStat class attributes and methods

# TrgVariable class attributes and methods

# TrgWhenHeader class attributes and methods

# TrgConstant class attributes and methods

# jointPackage_CPL2SPL_TrgSelectMember class attributes and methods

# jointPackage_CPL2SPL_TrgSelectDefault class attributes and methods

# TrgSelectMember class attributes and methods

# jointPackage_CPL2SPL_TrgSelectCase class attributes and methods

# jointPackage_CPL2SPL_TrgExpression class attributes and methods

# jointPackage_CPL2SPL_TrgConstantExp class attributes and methods

# TrgFunctionCall class attributes and methods

# jointPackage_CPL2SPL_TrgContinueStat class attributes and methods

# jointPackage_CPL2SPL_TrgBreakStat class attributes and methods

# jointPackage_CPL2SPL_TrgPushStat class attributes and methods

# jointPackage_CPL2SPL_TrgWhenHeader class attributes and methods
jointPackage_CPL2SPL_TrgWhenHeader_headerId: Property = Property(name="headerId", type=StringType)
jointPackage_CPL2SPL_TrgWhenHeader.attributes={jointPackage_CPL2SPL_TrgWhenHeader_headerId}

# jointPackage_CPL2SPL_TrgForwardExp class attributes and methods
jointPackage_CPL2SPL_TrgForwardExp_isParallel: Property = Property(name="isParallel", type=BooleanType)
jointPackage_CPL2SPL_TrgForwardExp.attributes={jointPackage_CPL2SPL_TrgForwardExp_isParallel}

# jointPackage_CPL2SPL_TrgWithExp class attributes and methods

# jointPackage_CPL2SPL_TrgOperatorExp class attributes and methods
jointPackage_CPL2SPL_TrgOperatorExp_opName: Property = Property(name="opName", type=StringType)
jointPackage_CPL2SPL_TrgOperatorExp.attributes={jointPackage_CPL2SPL_TrgOperatorExp_opName}

# jointPackage_CPL2SPL_TrgReasonExp class attributes and methods

# jointPackage_CPL2SPL_TrgBODYExp class attributes and methods

# jointPackage_CPL2SPL_TrgRequestURIExp class attributes and methods

# jointPackage_CPL2SPL_TrgPopExp class attributes and methods

# jointPackage_CPL2SPL_TrgFunctionCallExp class attributes and methods

# TrgMessageField class attributes and methods

# jointPackage_CPL2SPL_TrgBlockExp class attributes and methods

# jointPackage_CPL2SPL_TrgVariablePlace class attributes and methods

# jointPackage_CPL2SPL_TrgPropertyCallPlace class attributes and methods
jointPackage_CPL2SPL_TrgPropertyCallPlace_propName: Property = Property(name="propName", type=StringType)
jointPackage_CPL2SPL_TrgPropertyCallPlace.attributes={jointPackage_CPL2SPL_TrgPropertyCallPlace_propName}

# TrgVariablePlace class attributes and methods

# jointPackage_CPL2SPL_TrgVariable class attributes and methods

# jointPackage_CPL2SPL_TrgMessageField class attributes and methods

# jointPackage_CPL2SPL_TrgPlace class attributes and methods

# jointPackage_CPL2SPL_TrgSIPHeaderPlace class attributes and methods
jointPackage_CPL2SPL_TrgSIPHeaderPlace_header: Property = Property(name="header", type=StringType)
jointPackage_CPL2SPL_TrgSIPHeaderPlace.attributes={jointPackage_CPL2SPL_TrgSIPHeaderPlace_header}

# jointPackage_CPL2SPL_TrgBooleanConstant class attributes and methods
jointPackage_CPL2SPL_TrgBooleanConstant_value: Property = Property(name="value", type=BooleanType)
jointPackage_CPL2SPL_TrgBooleanConstant.attributes={jointPackage_CPL2SPL_TrgBooleanConstant_value}

# jointPackage_CPL2SPL_TrgIntegerConstant class attributes and methods
jointPackage_CPL2SPL_TrgIntegerConstant_value: Property = Property(name="value", type=IntegerType)
jointPackage_CPL2SPL_TrgIntegerConstant.attributes={jointPackage_CPL2SPL_TrgIntegerConstant_value}

# jointPackage_CPL2SPL_TrgStringConstant class attributes and methods
jointPackage_CPL2SPL_TrgStringConstant_value: Property = Property(name="value", type=StringType)
jointPackage_CPL2SPL_TrgStringConstant.attributes={jointPackage_CPL2SPL_TrgStringConstant_value}

# jointPackage_CPL2SPL_TrgURIConstant class attributes and methods
jointPackage_CPL2SPL_TrgURIConstant_uri: Property = Property(name="uri", type=StringType)
jointPackage_CPL2SPL_TrgURIConstant.attributes={jointPackage_CPL2SPL_TrgURIConstant_uri}

# jointPackage_CPL2SPL_TrgSequenceConstant class attributes and methods

# jointPackage_CPL2SPL_TrgResponseConstant class attributes and methods

# TrgResponse class attributes and methods

# jointPackage_CPL2SPL_TrgResponse class attributes and methods

# jointPackage_CPL2SPL_TrgSuccessResponse class attributes and methods
jointPackage_CPL2SPL_TrgSuccessResponse_successKind: Property = Property(name="successKind", type=StringType)
jointPackage_CPL2SPL_TrgSuccessResponse.attributes={jointPackage_CPL2SPL_TrgSuccessResponse_successKind}

# jointPackage_CPL2SPL_TrgErrorResponse class attributes and methods

# jointPackage_CPL2SPL_TrgReasonMessageField class attributes and methods

# jointPackage_CPL2SPL_TrgHeadedMessageField class attributes and methods
jointPackage_CPL2SPL_TrgHeadedMessageField_headerId: Property = Property(name="headerId", type=StringType)
jointPackage_CPL2SPL_TrgHeadedMessageField.attributes={jointPackage_CPL2SPL_TrgHeadedMessageField_headerId}

# jointPackage_CPL2SPL_TrgConstant class attributes and methods

# Relationships
sourceRoot0: BinaryAssociation = BinaryAssociation(
    name="sourceRoot0",
    ends={
        Property(name="SrcReject", type=jointPackage_CPL2SPL_JointMM, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_JointMM", type=SrcReject, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
addresses9: BinaryAssociation = BinaryAssociation(
    name="addresses9",
    ends={
        Property(name="SrcSwitchedAddress", type=jointPackage_CPL2SPL_SrcAddressSwitch, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_SrcAddressSwitch", type=SrcSwitchedAddress, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
strings10: BinaryAssociation = BinaryAssociation(
    name="strings10",
    ends={
        Property(name="SrcSwitchedString", type=jointPackage_CPL2SPL_SrcStringSwitch, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_SrcStringSwitch", type=SrcSwitchedString, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
languages11: BinaryAssociation = BinaryAssociation(
    name="languages11",
    ends={
        Property(name="SrcSwitchedLanguage", type=jointPackage_CPL2SPL_SrcLanguageSwitch, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_SrcLanguageSwitch", type=SrcSwitchedLanguage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
times12: BinaryAssociation = BinaryAssociation(
    name="times12",
    ends={
        Property(name="SrcSwitchedTime", type=jointPackage_CPL2SPL_SrcTimeSwitch, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_SrcTimeSwitch", type=SrcSwitchedTime, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
priorities13: BinaryAssociation = BinaryAssociation(
    name="priorities13",
    ends={
        Property(name="SrcSwitchedPriority", type=jointPackage_CPL2SPL_SrcPrioritySwitch, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_SrcPrioritySwitch", type=SrcSwitchedPriority, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetRoot1: BinaryAssociation = BinaryAssociation(
    name="targetRoot1",
    ends={
        Property(name="TrgServerErrorResponse", type=jointPackage_CPL2SPL_JointMM, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_JointMM2", type=TrgServerErrorResponse, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elements3: BinaryAssociation = BinaryAssociation(
    name="elements3",
    ends={
        Property(name="SrcElement", type=jointPackage_CPL2SPL_SrcCPLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_SrcCPLModel", type=SrcElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subActions4: BinaryAssociation = BinaryAssociation(
    name="subActions4",
    ends={
        Property(name="SrcSubAction", type=jointPackage_CPL2SPL_SrcCPL, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_SrcCPL", type=SrcSubAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing5: BinaryAssociation = BinaryAssociation(
    name="outgoing5",
    ends={
        Property(name="SrcOutgoing", type=jointPackage_CPL2SPL_SrcCPL, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_SrcCPL6", type=SrcOutgoing, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
incoming7: BinaryAssociation = BinaryAssociation(
    name="incoming7",
    ends={
        Property(name="SrcIncoming", type=jointPackage_CPL2SPL_SrcCPL, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_SrcCPL8", type=SrcIncoming, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
default21: BinaryAssociation = BinaryAssociation(
    name="default21",
    ends={
        Property(name="SrcDefault", type=jointPackage_CPL2SPL_SrcProxy, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_SrcProxy22", type=SrcDefault, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contents23: BinaryAssociation = BinaryAssociation(
    name="contents23",
    ends={
        Property(name="SrcNode", type=jointPackage_CPL2SPL_SrcNodeContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_SrcNodeContainer", type=SrcNode, multiplicity=Multiplicity(0, 1))
    }
)
busy14: BinaryAssociation = BinaryAssociation(
    name="busy14",
    ends={
        Property(name="SrcBusy", type=jointPackage_CPL2SPL_SrcProxy, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_SrcProxy", type=SrcBusy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
noAnswer15: BinaryAssociation = BinaryAssociation(
    name="noAnswer15",
    ends={
        Property(name="SrcNoAnswer", type=jointPackage_CPL2SPL_SrcProxy, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_SrcProxy16", type=SrcNoAnswer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
redirection17: BinaryAssociation = BinaryAssociation(
    name="redirection17",
    ends={
        Property(name="SrcRedirection", type=jointPackage_CPL2SPL_SrcProxy, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_SrcProxy18", type=SrcRedirection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
failure19: BinaryAssociation = BinaryAssociation(
    name="failure19",
    ends={
        Property(name="SrcFailure", type=jointPackage_CPL2SPL_SrcProxy, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_SrcProxy20", type=SrcFailure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
service27: BinaryAssociation = BinaryAssociation(
    name="service27",
    ends={
        Property(name="TrgService", type=jointPackage_CPL2SPL_TrgProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgProgram", type=TrgService, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type28: BinaryAssociation = BinaryAssociation(
    name="type28",
    ends={
        Property(name="TrgTypeExpression", type=jointPackage_CPL2SPL_TrgStructureProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgStructureProperty", type=TrgTypeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
notPresent24: BinaryAssociation = BinaryAssociation(
    name="notPresent24",
    ends={
        Property(name="SrcNotPresent", type=jointPackage_CPL2SPL_SrcSwitch, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_SrcSwitch", type=SrcNotPresent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
otherwise25: BinaryAssociation = BinaryAssociation(
    name="otherwise25",
    ends={
        Property(name="SrcOtherwise", type=jointPackage_CPL2SPL_SrcSwitch, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_SrcSwitch26", type=SrcOtherwise, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sessions30: BinaryAssociation = BinaryAssociation(
    name="sessions30",
    ends={
        Property(name="TrgSession", type=jointPackage_CPL2SPL_TrgService, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgService31", type=TrgSession, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declarations32: BinaryAssociation = BinaryAssociation(
    name="declarations32",
    ends={
        Property(name="TrgDeclaration33", type=jointPackage_CPL2SPL_TrgRegistration, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgRegistration", type=TrgDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sessions34: BinaryAssociation = BinaryAssociation(
    name="sessions34",
    ends={
        Property(name="TrgSession36", type=jointPackage_CPL2SPL_TrgRegistration, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgRegistration35", type=TrgSession, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declarations37: BinaryAssociation = BinaryAssociation(
    name="declarations37",
    ends={
        Property(name="TrgDeclaration38", type=jointPackage_CPL2SPL_TrgDialog, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgDialog", type=TrgDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods39: BinaryAssociation = BinaryAssociation(
    name="methods39",
    ends={
        Property(name="TrgMethod", type=jointPackage_CPL2SPL_TrgDialog, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgDialog40", type=TrgMethod, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
declarations41: BinaryAssociation = BinaryAssociation(
    name="declarations41",
    ends={
        Property(name="TrgDeclaration42", type=jointPackage_CPL2SPL_TrgEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgEvent", type=TrgDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods43: BinaryAssociation = BinaryAssociation(
    name="methods43",
    ends={
        Property(name="TrgMethod45", type=jointPackage_CPL2SPL_TrgEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgEvent44", type=TrgMethod, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
type46: BinaryAssociation = BinaryAssociation(
    name="type46",
    ends={
        Property(name="TrgTypeExpression47", type=jointPackage_CPL2SPL_TrgMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgMethod", type=TrgTypeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
declarations29: BinaryAssociation = BinaryAssociation(
    name="declarations29",
    ends={
        Property(name="TrgDeclaration", type=jointPackage_CPL2SPL_TrgService, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgService", type=TrgDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements56: BinaryAssociation = BinaryAssociation(
    name="statements56",
    ends={
        Property(name="TrgStatement57", type=jointPackage_CPL2SPL_TrgBranch, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgBranch", type=TrgStatement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
methodName48: BinaryAssociation = BinaryAssociation(
    name="methodName48",
    ends={
        Property(name="TrgMethodName", type=jointPackage_CPL2SPL_TrgMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgMethod49", type=TrgMethodName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments50: BinaryAssociation = BinaryAssociation(
    name="arguments50",
    ends={
        Property(name="TrgArgument", type=jointPackage_CPL2SPL_TrgMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgMethod51", type=TrgArgument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements52: BinaryAssociation = BinaryAssociation(
    name="statements52",
    ends={
        Property(name="TrgStatement", type=jointPackage_CPL2SPL_TrgMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgMethod53", type=TrgStatement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
branches54: BinaryAssociation = BinaryAssociation(
    name="branches54",
    ends={
        Property(name="TrgBranch", type=jointPackage_CPL2SPL_TrgMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgMethod55", type=TrgBranch, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
arguments64: BinaryAssociation = BinaryAssociation(
    name="arguments64",
    ends={
        Property(name="TrgArgument66", type=jointPackage_CPL2SPL_TrgFunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgFunctionDeclaration65", type=TrgArgument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements67: BinaryAssociation = BinaryAssociation(
    name="statements67",
    ends={
        Property(name="TrgStatement68", type=jointPackage_CPL2SPL_TrgLocalFunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgLocalFunctionDeclaration", type=TrgStatement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
properties69: BinaryAssociation = BinaryAssociation(
    name="properties69",
    ends={
        Property(name="TrgArgument70", type=jointPackage_CPL2SPL_TrgStructureDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgStructureDeclaration", type=TrgArgument, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
function71: BinaryAssociation = BinaryAssociation(
    name="function71",
    ends={
        Property(name="TrgFunctionDeclaration", type=jointPackage_CPL2SPL_TrgFunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgFunctionCall", type=TrgFunctionDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
type58: BinaryAssociation = BinaryAssociation(
    name="type58",
    ends={
        Property(name="TrgTypeExpression59", type=jointPackage_CPL2SPL_TrgVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgVariableDeclaration", type=TrgTypeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initExp60: BinaryAssociation = BinaryAssociation(
    name="initExp60",
    ends={
        Property(name="TrgExpression", type=jointPackage_CPL2SPL_TrgVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgVariableDeclaration61", type=TrgExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target77: BinaryAssociation = BinaryAssociation(
    name="target77",
    ends={
        Property(name="TrgPlace", type=jointPackage_CPL2SPL_TrgSetStat, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgSetStat", type=TrgPlace, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnType62: BinaryAssociation = BinaryAssociation(
    name="returnType62",
    ends={
        Property(name="TrgTypeExpression63", type=jointPackage_CPL2SPL_TrgFunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgFunctionDeclaration", type=TrgTypeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
setValue78: BinaryAssociation = BinaryAssociation(
    name="setValue78",
    ends={
        Property(name="TrgExpression80", type=jointPackage_CPL2SPL_TrgSetStat, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgSetStat79", type=TrgExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
declaration81: BinaryAssociation = BinaryAssociation(
    name="declaration81",
    ends={
        Property(name="TrgDeclaration82", type=jointPackage_CPL2SPL_TrgDeclarationStat, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgDeclarationStat", type=TrgDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnedValue83: BinaryAssociation = BinaryAssociation(
    name="returnedValue83",
    ends={
        Property(name="TrgExpression84", type=jointPackage_CPL2SPL_TrgReturnStat, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgReturnStat", type=TrgExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
branch85: BinaryAssociation = BinaryAssociation(
    name="branch85",
    ends={
        Property(name="TrgNamedBranch", type=jointPackage_CPL2SPL_TrgReturnStat, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgReturnStat86", type=TrgNamedBranch, multiplicity=Multiplicity(0, 1))
    }
)
condition87: BinaryAssociation = BinaryAssociation(
    name="condition87",
    ends={
        Property(name="TrgExpression88", type=jointPackage_CPL2SPL_TrgIfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgIfStat", type=TrgExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenStatements89: BinaryAssociation = BinaryAssociation(
    name="thenStatements89",
    ends={
        Property(name="TrgStatement91", type=jointPackage_CPL2SPL_TrgIfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgIfStat90", type=TrgStatement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elseStatements92: BinaryAssociation = BinaryAssociation(
    name="elseStatements92",
    ends={
        Property(name="TrgStatement94", type=jointPackage_CPL2SPL_TrgIfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgIfStat93", type=TrgStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters72: BinaryAssociation = BinaryAssociation(
    name="parameters72",
    ends={
        Property(name="TrgExpression74", type=jointPackage_CPL2SPL_TrgFunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgFunctionCall73", type=TrgExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements75: BinaryAssociation = BinaryAssociation(
    name="statements75",
    ends={
        Property(name="TrgStatement76", type=jointPackage_CPL2SPL_TrgCompoundStat, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgCompoundStat", type=TrgStatement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elseStatements101: BinaryAssociation = BinaryAssociation(
    name="elseStatements101",
    ends={
        Property(name="TrgStatement103", type=jointPackage_CPL2SPL_TrgWhenStat, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgWhenStat102", type=TrgStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sequenceExp104: BinaryAssociation = BinaryAssociation(
    name="sequenceExp104",
    ends={
        Property(name="TrgExpression105", type=jointPackage_CPL2SPL_TrgForeachStat, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgForeachStat", type=TrgExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements106: BinaryAssociation = BinaryAssociation(
    name="statements106",
    ends={
        Property(name="TrgStatement108", type=jointPackage_CPL2SPL_TrgForeachStat, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgForeachStat107", type=TrgStatement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
matchedExp109: BinaryAssociation = BinaryAssociation(
    name="matchedExp109",
    ends={
        Property(name="TrgExpression110", type=jointPackage_CPL2SPL_TrgSelectStat, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgSelectStat", type=TrgExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
selectCases111: BinaryAssociation = BinaryAssociation(
    name="selectCases111",
    ends={
        Property(name="TrgSelectCase", type=jointPackage_CPL2SPL_TrgSelectStat, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgSelectStat112", type=TrgSelectCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
selectDefault113: BinaryAssociation = BinaryAssociation(
    name="selectDefault113",
    ends={
        Property(name="TrgSelectDefault", type=jointPackage_CPL2SPL_TrgSelectStat, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgSelectStat114", type=TrgSelectDefault, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
idExp95: BinaryAssociation = BinaryAssociation(
    name="idExp95",
    ends={
        Property(name="TrgVariable", type=jointPackage_CPL2SPL_TrgWhenStat, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgWhenStat", type=TrgVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
whenHeaders96: BinaryAssociation = BinaryAssociation(
    name="whenHeaders96",
    ends={
        Property(name="TrgWhenHeader", type=jointPackage_CPL2SPL_TrgWhenStat, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgWhenStat97", type=TrgWhenHeader, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
statements98: BinaryAssociation = BinaryAssociation(
    name="statements98",
    ends={
        Property(name="TrgStatement100", type=jointPackage_CPL2SPL_TrgWhenStat, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgWhenStat99", type=TrgStatement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
value121: BinaryAssociation = BinaryAssociation(
    name="value121",
    ends={
        Property(name="TrgConstant", type=jointPackage_CPL2SPL_TrgWhenHeader, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgWhenHeader", type=TrgConstant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements122: BinaryAssociation = BinaryAssociation(
    name="statements122",
    ends={
        Property(name="TrgStatement123", type=jointPackage_CPL2SPL_TrgSelectMember, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgSelectMember", type=TrgStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values124: BinaryAssociation = BinaryAssociation(
    name="values124",
    ends={
        Property(name="TrgConstant125", type=jointPackage_CPL2SPL_TrgSelectCase, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgSelectCase", type=TrgConstant, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
value126: BinaryAssociation = BinaryAssociation(
    name="value126",
    ends={
        Property(name="TrgConstant127", type=jointPackage_CPL2SPL_TrgConstantExp, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgConstantExp", type=TrgConstant, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
functionCall115: BinaryAssociation = BinaryAssociation(
    name="functionCall115",
    ends={
        Property(name="TrgFunctionCall", type=jointPackage_CPL2SPL_TrgFunctionCallStat, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgFunctionCallStat", type=TrgFunctionCall, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target116: BinaryAssociation = BinaryAssociation(
    name="target116",
    ends={
        Property(name="TrgPlace117", type=jointPackage_CPL2SPL_TrgPushStat, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgPushStat", type=TrgPlace, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
pushedValue118: BinaryAssociation = BinaryAssociation(
    name="pushedValue118",
    ends={
        Property(name="TrgExpression120", type=jointPackage_CPL2SPL_TrgPushStat, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgPushStat119", type=TrgExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightExp130: BinaryAssociation = BinaryAssociation(
    name="rightExp130",
    ends={
        Property(name="TrgExpression132", type=jointPackage_CPL2SPL_TrgOperatorExp, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgOperatorExp131", type=TrgExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp133: BinaryAssociation = BinaryAssociation(
    name="exp133",
    ends={
        Property(name="TrgExpression134", type=jointPackage_CPL2SPL_TrgForwardExp, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgForwardExp", type=TrgExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp135: BinaryAssociation = BinaryAssociation(
    name="exp135",
    ends={
        Property(name="TrgExpression136", type=jointPackage_CPL2SPL_TrgWithExp, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgWithExp", type=TrgExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftExp128: BinaryAssociation = BinaryAssociation(
    name="leftExp128",
    ends={
        Property(name="TrgExpression129", type=jointPackage_CPL2SPL_TrgOperatorExp, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgOperatorExp", type=TrgExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source141: BinaryAssociation = BinaryAssociation(
    name="source141",
    ends={
        Property(name="TrgPlace142", type=jointPackage_CPL2SPL_TrgPopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgPopExp", type=TrgPlace, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
msgFields137: BinaryAssociation = BinaryAssociation(
    name="msgFields137",
    ends={
        Property(name="TrgMessageField", type=jointPackage_CPL2SPL_TrgWithExp, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgWithExp138", type=TrgMessageField, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
exp139: BinaryAssociation = BinaryAssociation(
    name="exp139",
    ends={
        Property(name="TrgExpression140", type=jointPackage_CPL2SPL_TrgBlockExp, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgBlockExp", type=TrgExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source145: BinaryAssociation = BinaryAssociation(
    name="source145",
    ends={
        Property(name="TrgVariablePlace", type=jointPackage_CPL2SPL_TrgPropertyCallPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgPropertyCallPlace", type=TrgVariablePlace, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source146: BinaryAssociation = BinaryAssociation(
    name="source146",
    ends={
        Property(name="TrgDeclaration147", type=jointPackage_CPL2SPL_TrgVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgVariable", type=TrgDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
functionCall143: BinaryAssociation = BinaryAssociation(
    name="functionCall143",
    ends={
        Property(name="TrgFunctionCall144", type=jointPackage_CPL2SPL_TrgFunctionCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgFunctionCallExp", type=TrgFunctionCall, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values150: BinaryAssociation = BinaryAssociation(
    name="values150",
    ends={
        Property(name="TrgConstant151", type=jointPackage_CPL2SPL_TrgSequenceConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgSequenceConstant", type=TrgConstant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
response152: BinaryAssociation = BinaryAssociation(
    name="response152",
    ends={
        Property(name="TrgResponse", type=jointPackage_CPL2SPL_TrgResponseConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgResponseConstant", type=TrgResponse, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exp148: BinaryAssociation = BinaryAssociation(
    name="exp148",
    ends={
        Property(name="TrgExpression149", type=jointPackage_CPL2SPL_TrgMessageField, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_CPL2SPL_TrgMessageField", type=TrgExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_jointPackage_CPL2SPL_SrcAddressSwitch_SrcSwitch = Generalization(general=SrcSwitch, specific=jointPackage_CPL2SPL_SrcAddressSwitch)
gen_jointPackage_CPL2SPL_SrcStringSwitch_SrcSwitch = Generalization(general=SrcSwitch, specific=jointPackage_CPL2SPL_SrcStringSwitch)
gen_jointPackage_CPL2SPL_SrcLanguageSwitch_SrcSwitch = Generalization(general=SrcSwitch, specific=jointPackage_CPL2SPL_SrcLanguageSwitch)
gen_jointPackage_CPL2SPL_SrcTimeSwitch_SrcSwitch = Generalization(general=SrcSwitch, specific=jointPackage_CPL2SPL_SrcTimeSwitch)
gen_jointPackage_CPL2SPL_SrcPrioritySwitch_SrcSwitch = Generalization(general=SrcSwitch, specific=jointPackage_CPL2SPL_SrcPrioritySwitch)
gen_jointPackage_CPL2SPL_SrcCPL_SrcElement = Generalization(general=SrcElement, specific=jointPackage_CPL2SPL_SrcCPL)
gen_jointPackage_CPL2SPL_SrcRedirect_SrcSignallingAction = Generalization(general=SrcSignallingAction, specific=jointPackage_CPL2SPL_SrcRedirect)
gen_jointPackage_CPL2SPL_SrcReject_SrcSignallingAction = Generalization(general=SrcSignallingAction, specific=jointPackage_CPL2SPL_SrcReject)
gen_jointPackage_CPL2SPL_SrcNodeContainer_SrcElement = Generalization(general=SrcElement, specific=jointPackage_CPL2SPL_SrcNodeContainer)
gen_jointPackage_CPL2SPL_SrcSubAction_SrcNodeContainer = Generalization(general=SrcNodeContainer, specific=jointPackage_CPL2SPL_SrcSubAction)
gen_jointPackage_CPL2SPL_SrcOutgoing_SrcNodeContainer = Generalization(general=SrcNodeContainer, specific=jointPackage_CPL2SPL_SrcOutgoing)
gen_jointPackage_CPL2SPL_SrcIncoming_SrcNodeContainer = Generalization(general=SrcNodeContainer, specific=jointPackage_CPL2SPL_SrcIncoming)
gen_jointPackage_CPL2SPL_SrcNotPresent_SrcNodeContainer = Generalization(general=SrcNodeContainer, specific=jointPackage_CPL2SPL_SrcNotPresent)
gen_jointPackage_CPL2SPL_SrcOtherwise_SrcNodeContainer = Generalization(general=SrcNodeContainer, specific=jointPackage_CPL2SPL_SrcOtherwise)
gen_jointPackage_CPL2SPL_SrcSwitchedAddress_SrcNodeContainer = Generalization(general=SrcNodeContainer, specific=jointPackage_CPL2SPL_SrcSwitchedAddress)
gen_jointPackage_CPL2SPL_SrcProxy_SrcSignallingAction = Generalization(general=SrcSignallingAction, specific=jointPackage_CPL2SPL_SrcProxy)
gen_jointPackage_CPL2SPL_SrcSwitchedPriority_SrcNodeContainer = Generalization(general=SrcNodeContainer, specific=jointPackage_CPL2SPL_SrcSwitchedPriority)
gen_jointPackage_CPL2SPL_SrcBusy_SrcNodeContainer = Generalization(general=SrcNodeContainer, specific=jointPackage_CPL2SPL_SrcBusy)
gen_jointPackage_CPL2SPL_SrcSwitchedString_SrcNodeContainer = Generalization(general=SrcNodeContainer, specific=jointPackage_CPL2SPL_SrcSwitchedString)
gen_jointPackage_CPL2SPL_SrcSwitchedLanguage_SrcNodeContainer = Generalization(general=SrcNodeContainer, specific=jointPackage_CPL2SPL_SrcSwitchedLanguage)
gen_jointPackage_CPL2SPL_SrcSwitchedTime_SrcNodeContainer = Generalization(general=SrcNodeContainer, specific=jointPackage_CPL2SPL_SrcSwitchedTime)
gen_jointPackage_CPL2SPL_SrcSubCall_SrcNode = Generalization(general=SrcNode, specific=jointPackage_CPL2SPL_SrcSubCall)
gen_jointPackage_CPL2SPL_SrcAction_SrcNode = Generalization(general=SrcNode, specific=jointPackage_CPL2SPL_SrcAction)
gen_jointPackage_CPL2SPL_SrcSignallingAction_SrcAction = Generalization(general=SrcAction, specific=jointPackage_CPL2SPL_SrcSignallingAction)
gen_jointPackage_CPL2SPL_TrgProgram_TrgLocatedElement = Generalization(general=TrgLocatedElement, specific=jointPackage_CPL2SPL_TrgProgram)
gen_jointPackage_CPL2SPL_TrgStructureProperty_TrgLocatedElement = Generalization(general=TrgLocatedElement, specific=jointPackage_CPL2SPL_TrgStructureProperty)
gen_jointPackage_CPL2SPL_TrgClientErrorResponse_TrgErrorResponse = Generalization(general=TrgErrorResponse, specific=jointPackage_CPL2SPL_TrgClientErrorResponse)
gen_jointPackage_CPL2SPL_TrgGlobalErrorResponse_TrgErrorResponse = Generalization(general=TrgErrorResponse, specific=jointPackage_CPL2SPL_TrgGlobalErrorResponse)
gen_jointPackage_CPL2SPL_SrcNoAnswer_SrcNodeContainer = Generalization(general=SrcNodeContainer, specific=jointPackage_CPL2SPL_SrcNoAnswer)
gen_jointPackage_CPL2SPL_SrcRedirection_SrcNodeContainer = Generalization(general=SrcNodeContainer, specific=jointPackage_CPL2SPL_SrcRedirection)
gen_jointPackage_CPL2SPL_SrcFailure_SrcNodeContainer = Generalization(general=SrcNodeContainer, specific=jointPackage_CPL2SPL_SrcFailure)
gen_jointPackage_CPL2SPL_SrcDefault_SrcNodeContainer = Generalization(general=SrcNodeContainer, specific=jointPackage_CPL2SPL_SrcDefault)
gen_jointPackage_CPL2SPL_SrcNode_SrcElement = Generalization(general=SrcElement, specific=jointPackage_CPL2SPL_SrcNode)
gen_jointPackage_CPL2SPL_SrcSwitch_SrcNode = Generalization(general=SrcNode, specific=jointPackage_CPL2SPL_SrcSwitch)
gen_jointPackage_CPL2SPL_SrcLocation_SrcNode = Generalization(general=SrcNode, specific=jointPackage_CPL2SPL_SrcLocation)
gen_jointPackage_CPL2SPL_SrcLocation_SrcNodeContainer = Generalization(general=SrcNodeContainer, specific=jointPackage_CPL2SPL_SrcLocation)
gen_jointPackage_CPL2SPL_TrgSession_TrgLocatedElement = Generalization(general=TrgLocatedElement, specific=jointPackage_CPL2SPL_TrgSession)
gen_jointPackage_CPL2SPL_TrgRegistration_TrgSession = Generalization(general=TrgSession, specific=jointPackage_CPL2SPL_TrgRegistration)
gen_jointPackage_CPL2SPL_TrgDialog_TrgSession = Generalization(general=TrgSession, specific=jointPackage_CPL2SPL_TrgDialog)
gen_jointPackage_CPL2SPL_TrgEvent_TrgSession = Generalization(general=TrgSession, specific=jointPackage_CPL2SPL_TrgEvent)
gen_jointPackage_CPL2SPL_TrgMethod_TrgSession = Generalization(general=TrgSession, specific=jointPackage_CPL2SPL_TrgMethod)
gen_jointPackage_CPL2SPL_TrgRedirectionErrorResponse_TrgErrorResponse = Generalization(general=TrgErrorResponse, specific=jointPackage_CPL2SPL_TrgRedirectionErrorResponse)
gen_jointPackage_CPL2SPL_TrgServerErrorResponse_TrgErrorResponse = Generalization(general=TrgErrorResponse, specific=jointPackage_CPL2SPL_TrgServerErrorResponse)
gen_jointPackage_CPL2SPL_TrgService_TrgLocatedElement = Generalization(general=TrgLocatedElement, specific=jointPackage_CPL2SPL_TrgService)
gen_jointPackage_CPL2SPL_TrgMethodName_TrgLocatedElement = Generalization(general=TrgLocatedElement, specific=jointPackage_CPL2SPL_TrgMethodName)
gen_jointPackage_CPL2SPL_TrgSIPMethodName_TrgMethodName = Generalization(general=TrgMethodName, specific=jointPackage_CPL2SPL_TrgSIPMethodName)
gen_jointPackage_CPL2SPL_TrgControlMethodName_TrgMethodName = Generalization(general=TrgMethodName, specific=jointPackage_CPL2SPL_TrgControlMethodName)
gen_jointPackage_CPL2SPL_TrgBranch_TrgLocatedElement = Generalization(general=TrgLocatedElement, specific=jointPackage_CPL2SPL_TrgBranch)
gen_jointPackage_CPL2SPL_TrgDefaultBranch_TrgBranch = Generalization(general=TrgBranch, specific=jointPackage_CPL2SPL_TrgDefaultBranch)
gen_jointPackage_CPL2SPL_TrgNamedBranch_TrgBranch = Generalization(general=TrgBranch, specific=jointPackage_CPL2SPL_TrgNamedBranch)
gen_jointPackage_CPL2SPL_TrgTypeExpression_TrgLocatedElement = Generalization(general=TrgLocatedElement, specific=jointPackage_CPL2SPL_TrgTypeExpression)
gen_jointPackage_CPL2SPL_TrgSimpleType_TrgTypeExpression = Generalization(general=TrgTypeExpression, specific=jointPackage_CPL2SPL_TrgSimpleType)
gen_jointPackage_CPL2SPL_TrgSequenceType_TrgTypeExpression = Generalization(general=TrgTypeExpression, specific=jointPackage_CPL2SPL_TrgSequenceType)
gen_jointPackage_CPL2SPL_TrgDefinedType_TrgTypeExpression = Generalization(general=TrgTypeExpression, specific=jointPackage_CPL2SPL_TrgDefinedType)
gen_jointPackage_CPL2SPL_TrgDeclaration_TrgLocatedElement = Generalization(general=TrgLocatedElement, specific=jointPackage_CPL2SPL_TrgDeclaration)
gen_jointPackage_CPL2SPL_TrgArgument_TrgVariableDeclaration = Generalization(general=TrgVariableDeclaration, specific=jointPackage_CPL2SPL_TrgArgument)
gen_jointPackage_CPL2SPL_TrgRemoteFunctionDeclaration_TrgFunctionDeclaration = Generalization(general=TrgFunctionDeclaration, specific=jointPackage_CPL2SPL_TrgRemoteFunctionDeclaration)
gen_jointPackage_CPL2SPL_TrgLocalFunctionDeclaration_TrgFunctionDeclaration = Generalization(general=TrgFunctionDeclaration, specific=jointPackage_CPL2SPL_TrgLocalFunctionDeclaration)
gen_jointPackage_CPL2SPL_TrgStructureDeclaration_TrgDeclaration = Generalization(general=TrgDeclaration, specific=jointPackage_CPL2SPL_TrgStructureDeclaration)
gen_jointPackage_CPL2SPL_TrgFunctionCall_TrgLocatedElement = Generalization(general=TrgLocatedElement, specific=jointPackage_CPL2SPL_TrgFunctionCall)
gen_jointPackage_CPL2SPL_TrgVariableDeclaration_TrgDeclaration = Generalization(general=TrgDeclaration, specific=jointPackage_CPL2SPL_TrgVariableDeclaration)
gen_jointPackage_CPL2SPL_TrgFunctionDeclaration_TrgDeclaration = Generalization(general=TrgDeclaration, specific=jointPackage_CPL2SPL_TrgFunctionDeclaration)
gen_jointPackage_CPL2SPL_TrgDeclarationStat_TrgStatement = Generalization(general=TrgStatement, specific=jointPackage_CPL2SPL_TrgDeclarationStat)
gen_jointPackage_CPL2SPL_TrgReturnStat_TrgStatement = Generalization(general=TrgStatement, specific=jointPackage_CPL2SPL_TrgReturnStat)
gen_jointPackage_CPL2SPL_TrgIfStat_TrgStatement = Generalization(general=TrgStatement, specific=jointPackage_CPL2SPL_TrgIfStat)
gen_jointPackage_CPL2SPL_TrgStatement_TrgLocatedElement = Generalization(general=TrgLocatedElement, specific=jointPackage_CPL2SPL_TrgStatement)
gen_jointPackage_CPL2SPL_TrgCompoundStat_TrgStatement = Generalization(general=TrgStatement, specific=jointPackage_CPL2SPL_TrgCompoundStat)
gen_jointPackage_CPL2SPL_TrgSetStat_TrgStatement = Generalization(general=TrgStatement, specific=jointPackage_CPL2SPL_TrgSetStat)
gen_jointPackage_CPL2SPL_TrgForeachStat_TrgStatement = Generalization(general=TrgStatement, specific=jointPackage_CPL2SPL_TrgForeachStat)
gen_jointPackage_CPL2SPL_TrgSelectStat_TrgStatement = Generalization(general=TrgStatement, specific=jointPackage_CPL2SPL_TrgSelectStat)
gen_jointPackage_CPL2SPL_TrgFunctionCallStat_TrgStatement = Generalization(general=TrgStatement, specific=jointPackage_CPL2SPL_TrgFunctionCallStat)
gen_jointPackage_CPL2SPL_TrgWhenStat_TrgStatement = Generalization(general=TrgStatement, specific=jointPackage_CPL2SPL_TrgWhenStat)
gen_jointPackage_CPL2SPL_TrgSelectMember_TrgLocatedElement = Generalization(general=TrgLocatedElement, specific=jointPackage_CPL2SPL_TrgSelectMember)
gen_jointPackage_CPL2SPL_TrgSelectDefault_TrgSelectMember = Generalization(general=TrgSelectMember, specific=jointPackage_CPL2SPL_TrgSelectDefault)
gen_jointPackage_CPL2SPL_TrgSelectCase_TrgSelectMember = Generalization(general=TrgSelectMember, specific=jointPackage_CPL2SPL_TrgSelectCase)
gen_jointPackage_CPL2SPL_TrgExpression_TrgLocatedElement = Generalization(general=TrgLocatedElement, specific=jointPackage_CPL2SPL_TrgExpression)
gen_jointPackage_CPL2SPL_TrgConstantExp_TrgExpression = Generalization(general=TrgExpression, specific=jointPackage_CPL2SPL_TrgConstantExp)
gen_jointPackage_CPL2SPL_TrgContinueStat_TrgStatement = Generalization(general=TrgStatement, specific=jointPackage_CPL2SPL_TrgContinueStat)
gen_jointPackage_CPL2SPL_TrgBreakStat_TrgStatement = Generalization(general=TrgStatement, specific=jointPackage_CPL2SPL_TrgBreakStat)
gen_jointPackage_CPL2SPL_TrgPushStat_TrgStatement = Generalization(general=TrgStatement, specific=jointPackage_CPL2SPL_TrgPushStat)
gen_jointPackage_CPL2SPL_TrgWhenHeader_TrgVariableDeclaration = Generalization(general=TrgVariableDeclaration, specific=jointPackage_CPL2SPL_TrgWhenHeader)
gen_jointPackage_CPL2SPL_TrgForwardExp_TrgExpression = Generalization(general=TrgExpression, specific=jointPackage_CPL2SPL_TrgForwardExp)
gen_jointPackage_CPL2SPL_TrgWithExp_TrgExpression = Generalization(general=TrgExpression, specific=jointPackage_CPL2SPL_TrgWithExp)
gen_jointPackage_CPL2SPL_TrgOperatorExp_TrgExpression = Generalization(general=TrgExpression, specific=jointPackage_CPL2SPL_TrgOperatorExp)
gen_jointPackage_CPL2SPL_TrgReasonExp_TrgExpression = Generalization(general=TrgExpression, specific=jointPackage_CPL2SPL_TrgReasonExp)
gen_jointPackage_CPL2SPL_TrgBODYExp_TrgExpression = Generalization(general=TrgExpression, specific=jointPackage_CPL2SPL_TrgBODYExp)
gen_jointPackage_CPL2SPL_TrgRequestURIExp_TrgExpression = Generalization(general=TrgExpression, specific=jointPackage_CPL2SPL_TrgRequestURIExp)
gen_jointPackage_CPL2SPL_TrgPopExp_TrgExpression = Generalization(general=TrgExpression, specific=jointPackage_CPL2SPL_TrgPopExp)
gen_jointPackage_CPL2SPL_TrgFunctionCallExp_TrgExpression = Generalization(general=TrgExpression, specific=jointPackage_CPL2SPL_TrgFunctionCallExp)
gen_jointPackage_CPL2SPL_TrgBlockExp_TrgExpression = Generalization(general=TrgExpression, specific=jointPackage_CPL2SPL_TrgBlockExp)
gen_jointPackage_CPL2SPL_TrgVariablePlace_TrgPlace = Generalization(general=TrgPlace, specific=jointPackage_CPL2SPL_TrgVariablePlace)
gen_jointPackage_CPL2SPL_TrgPropertyCallPlace_TrgVariablePlace = Generalization(general=TrgVariablePlace, specific=jointPackage_CPL2SPL_TrgPropertyCallPlace)
gen_jointPackage_CPL2SPL_TrgVariable_TrgVariablePlace = Generalization(general=TrgVariablePlace, specific=jointPackage_CPL2SPL_TrgVariable)
gen_jointPackage_CPL2SPL_TrgMessageField_TrgLocatedElement = Generalization(general=TrgLocatedElement, specific=jointPackage_CPL2SPL_TrgMessageField)
gen_jointPackage_CPL2SPL_TrgPlace_TrgExpression = Generalization(general=TrgExpression, specific=jointPackage_CPL2SPL_TrgPlace)
gen_jointPackage_CPL2SPL_TrgSIPHeaderPlace_TrgPlace = Generalization(general=TrgPlace, specific=jointPackage_CPL2SPL_TrgSIPHeaderPlace)
gen_jointPackage_CPL2SPL_TrgBooleanConstant_TrgConstant = Generalization(general=TrgConstant, specific=jointPackage_CPL2SPL_TrgBooleanConstant)
gen_jointPackage_CPL2SPL_TrgIntegerConstant_TrgConstant = Generalization(general=TrgConstant, specific=jointPackage_CPL2SPL_TrgIntegerConstant)
gen_jointPackage_CPL2SPL_TrgStringConstant_TrgConstant = Generalization(general=TrgConstant, specific=jointPackage_CPL2SPL_TrgStringConstant)
gen_jointPackage_CPL2SPL_TrgURIConstant_TrgConstant = Generalization(general=TrgConstant, specific=jointPackage_CPL2SPL_TrgURIConstant)
gen_jointPackage_CPL2SPL_TrgSequenceConstant_TrgConstant = Generalization(general=TrgConstant, specific=jointPackage_CPL2SPL_TrgSequenceConstant)
gen_jointPackage_CPL2SPL_TrgResponseConstant_TrgConstant = Generalization(general=TrgConstant, specific=jointPackage_CPL2SPL_TrgResponseConstant)
gen_jointPackage_CPL2SPL_TrgResponse_TrgLocatedElement = Generalization(general=TrgLocatedElement, specific=jointPackage_CPL2SPL_TrgResponse)
gen_jointPackage_CPL2SPL_TrgSuccessResponse_TrgResponse = Generalization(general=TrgResponse, specific=jointPackage_CPL2SPL_TrgSuccessResponse)
gen_jointPackage_CPL2SPL_TrgErrorResponse_TrgResponse = Generalization(general=TrgResponse, specific=jointPackage_CPL2SPL_TrgErrorResponse)
gen_jointPackage_CPL2SPL_TrgReasonMessageField_TrgMessageField = Generalization(general=TrgMessageField, specific=jointPackage_CPL2SPL_TrgReasonMessageField)
gen_jointPackage_CPL2SPL_TrgHeadedMessageField_TrgMessageField = Generalization(general=TrgMessageField, specific=jointPackage_CPL2SPL_TrgHeadedMessageField)
gen_jointPackage_CPL2SPL_TrgConstant_TrgLocatedElement = Generalization(general=TrgLocatedElement, specific=jointPackage_CPL2SPL_TrgConstant)

# Domain Model
domain_model = DomainModel(
    name="jointPackage_CPL2SPL",
    types={jointPackage_CPL2SPL_JointMM, SrcReject, jointPackage_CPL2SPL_SrcAddressSwitch, SrcSwitch, SrcSwitchedAddress, jointPackage_CPL2SPL_SrcStringSwitch, SrcSwitchedString, jointPackage_CPL2SPL_SrcLanguageSwitch, SrcSwitchedLanguage, jointPackage_CPL2SPL_SrcTimeSwitch, SrcSwitchedTime, jointPackage_CPL2SPL_SrcPrioritySwitch, SrcSwitchedPriority, TrgServerErrorResponse, jointPackage_CPL2SPL_SrcCPLModel, SrcElement, jointPackage_CPL2SPL_SrcCPL, SrcSubAction, SrcOutgoing, SrcIncoming, SrcDefault, jointPackage_CPL2SPL_SrcRedirect, jointPackage_CPL2SPL_SrcReject, jointPackage_CPL2SPL_SrcElement, jointPackage_CPL2SPL_SrcNodeContainer, SrcNode, jointPackage_CPL2SPL_SrcSubAction, SrcNodeContainer, jointPackage_CPL2SPL_SrcOutgoing, jointPackage_CPL2SPL_SrcIncoming, jointPackage_CPL2SPL_SrcNotPresent, jointPackage_CPL2SPL_SrcOtherwise, jointPackage_CPL2SPL_SrcSwitchedAddress, jointPackage_CPL2SPL_SrcProxy, SrcSignallingAction, SrcBusy, SrcNoAnswer, SrcRedirection, SrcFailure, jointPackage_CPL2SPL_SrcSwitchedPriority, jointPackage_CPL2SPL_SrcBusy, jointPackage_CPL2SPL_SrcSwitchedString, jointPackage_CPL2SPL_SrcSwitchedLanguage, jointPackage_CPL2SPL_SrcSwitchedTime, jointPackage_CPL2SPL_SrcSubCall, jointPackage_CPL2SPL_SrcAction, jointPackage_CPL2SPL_SrcSignallingAction, SrcAction, jointPackage_CPL2SPL_TrgProgram, TrgLocatedElement, TrgService, jointPackage_CPL2SPL_TrgStructureProperty, TrgTypeExpression, jointPackage_CPL2SPL_TrgClientErrorResponse, TrgErrorResponse, jointPackage_CPL2SPL_TrgGlobalErrorResponse, jointPackage_CPL2SPL_SrcNoAnswer, jointPackage_CPL2SPL_SrcRedirection, jointPackage_CPL2SPL_SrcFailure, jointPackage_CPL2SPL_SrcDefault, jointPackage_CPL2SPL_SrcNode, jointPackage_CPL2SPL_SrcSwitch, SrcNotPresent, SrcOtherwise, jointPackage_CPL2SPL_SrcLocation, jointPackage_CPL2SPL_TrgSession, jointPackage_CPL2SPL_TrgRegistration, jointPackage_CPL2SPL_TrgDialog, TrgMethod, jointPackage_CPL2SPL_TrgEvent, jointPackage_CPL2SPL_TrgMethod, jointPackage_CPL2SPL_TrgRedirectionErrorResponse, jointPackage_CPL2SPL_TrgServerErrorResponse, jointPackage_CPL2SPL_TrgLocatedElement, jointPackage_CPL2SPL_TrgService, TrgDeclaration, TrgSession, jointPackage_CPL2SPL_TrgMethodName, jointPackage_CPL2SPL_TrgSIPMethodName, jointPackage_CPL2SPL_TrgControlMethodName, jointPackage_CPL2SPL_TrgBranch, jointPackage_CPL2SPL_TrgDefaultBranch, jointPackage_CPL2SPL_TrgNamedBranch, jointPackage_CPL2SPL_TrgTypeExpression, jointPackage_CPL2SPL_TrgSimpleType, jointPackage_CPL2SPL_TrgSequenceType, jointPackage_CPL2SPL_TrgDefinedType, jointPackage_CPL2SPL_TrgDeclaration, TrgMethodName, TrgArgument, TrgStatement, TrgBranch, jointPackage_CPL2SPL_TrgArgument, TrgVariableDeclaration, jointPackage_CPL2SPL_TrgRemoteFunctionDeclaration, TrgFunctionDeclaration, jointPackage_CPL2SPL_TrgLocalFunctionDeclaration, jointPackage_CPL2SPL_TrgStructureDeclaration, jointPackage_CPL2SPL_TrgFunctionCall, jointPackage_CPL2SPL_TrgVariableDeclaration, TrgExpression, jointPackage_CPL2SPL_TrgFunctionDeclaration, TrgPlace, jointPackage_CPL2SPL_TrgDeclarationStat, jointPackage_CPL2SPL_TrgReturnStat, TrgNamedBranch, jointPackage_CPL2SPL_TrgIfStat, jointPackage_CPL2SPL_TrgStatement, jointPackage_CPL2SPL_TrgCompoundStat, jointPackage_CPL2SPL_TrgSetStat, jointPackage_CPL2SPL_TrgForeachStat, jointPackage_CPL2SPL_TrgSelectStat, TrgSelectCase, TrgSelectDefault, jointPackage_CPL2SPL_TrgFunctionCallStat, jointPackage_CPL2SPL_TrgWhenStat, TrgVariable, TrgWhenHeader, TrgConstant, jointPackage_CPL2SPL_TrgSelectMember, jointPackage_CPL2SPL_TrgSelectDefault, TrgSelectMember, jointPackage_CPL2SPL_TrgSelectCase, jointPackage_CPL2SPL_TrgExpression, jointPackage_CPL2SPL_TrgConstantExp, TrgFunctionCall, jointPackage_CPL2SPL_TrgContinueStat, jointPackage_CPL2SPL_TrgBreakStat, jointPackage_CPL2SPL_TrgPushStat, jointPackage_CPL2SPL_TrgWhenHeader, jointPackage_CPL2SPL_TrgForwardExp, jointPackage_CPL2SPL_TrgWithExp, jointPackage_CPL2SPL_TrgOperatorExp, jointPackage_CPL2SPL_TrgReasonExp, jointPackage_CPL2SPL_TrgBODYExp, jointPackage_CPL2SPL_TrgRequestURIExp, jointPackage_CPL2SPL_TrgPopExp, jointPackage_CPL2SPL_TrgFunctionCallExp, TrgMessageField, jointPackage_CPL2SPL_TrgBlockExp, jointPackage_CPL2SPL_TrgVariablePlace, jointPackage_CPL2SPL_TrgPropertyCallPlace, TrgVariablePlace, jointPackage_CPL2SPL_TrgVariable, jointPackage_CPL2SPL_TrgMessageField, jointPackage_CPL2SPL_TrgPlace, jointPackage_CPL2SPL_TrgSIPHeaderPlace, jointPackage_CPL2SPL_TrgBooleanConstant, jointPackage_CPL2SPL_TrgIntegerConstant, jointPackage_CPL2SPL_TrgStringConstant, jointPackage_CPL2SPL_TrgURIConstant, jointPackage_CPL2SPL_TrgSequenceConstant, jointPackage_CPL2SPL_TrgResponseConstant, TrgResponse, jointPackage_CPL2SPL_TrgResponse, jointPackage_CPL2SPL_TrgSuccessResponse, jointPackage_CPL2SPL_TrgErrorResponse, jointPackage_CPL2SPL_TrgReasonMessageField, jointPackage_CPL2SPL_TrgHeadedMessageField, jointPackage_CPL2SPL_TrgConstant, Direction, Modifier, FunctionLocation, SIPHeader, SuccessKind, ClientErrorKind, SIPMethod, ControlMethod, PrimitiveType, RedirectionErrorKind, ServerErrorKind, GlobalErrorKind},
    associations={sourceRoot0, addresses9, strings10, languages11, times12, priorities13, targetRoot1, elements3, subActions4, outgoing5, incoming7, default21, contents23, busy14, noAnswer15, redirection17, failure19, service27, type28, notPresent24, otherwise25, sessions30, declarations32, sessions34, declarations37, methods39, declarations41, methods43, type46, declarations29, statements56, methodName48, arguments50, statements52, branches54, arguments64, statements67, properties69, function71, type58, initExp60, target77, returnType62, setValue78, declaration81, returnedValue83, branch85, condition87, thenStatements89, elseStatements92, parameters72, statements75, elseStatements101, sequenceExp104, statements106, matchedExp109, selectCases111, selectDefault113, idExp95, whenHeaders96, statements98, value121, statements122, values124, value126, functionCall115, target116, pushedValue118, rightExp130, exp133, exp135, leftExp128, source141, msgFields137, exp139, source145, source146, functionCall143, values150, response152, exp148},
    generalizations={gen_jointPackage_CPL2SPL_SrcAddressSwitch_SrcSwitch, gen_jointPackage_CPL2SPL_SrcStringSwitch_SrcSwitch, gen_jointPackage_CPL2SPL_SrcLanguageSwitch_SrcSwitch, gen_jointPackage_CPL2SPL_SrcTimeSwitch_SrcSwitch, gen_jointPackage_CPL2SPL_SrcPrioritySwitch_SrcSwitch, gen_jointPackage_CPL2SPL_SrcCPL_SrcElement, gen_jointPackage_CPL2SPL_SrcRedirect_SrcSignallingAction, gen_jointPackage_CPL2SPL_SrcReject_SrcSignallingAction, gen_jointPackage_CPL2SPL_SrcNodeContainer_SrcElement, gen_jointPackage_CPL2SPL_SrcSubAction_SrcNodeContainer, gen_jointPackage_CPL2SPL_SrcOutgoing_SrcNodeContainer, gen_jointPackage_CPL2SPL_SrcIncoming_SrcNodeContainer, gen_jointPackage_CPL2SPL_SrcNotPresent_SrcNodeContainer, gen_jointPackage_CPL2SPL_SrcOtherwise_SrcNodeContainer, gen_jointPackage_CPL2SPL_SrcSwitchedAddress_SrcNodeContainer, gen_jointPackage_CPL2SPL_SrcProxy_SrcSignallingAction, gen_jointPackage_CPL2SPL_SrcSwitchedPriority_SrcNodeContainer, gen_jointPackage_CPL2SPL_SrcBusy_SrcNodeContainer, gen_jointPackage_CPL2SPL_SrcSwitchedString_SrcNodeContainer, gen_jointPackage_CPL2SPL_SrcSwitchedLanguage_SrcNodeContainer, gen_jointPackage_CPL2SPL_SrcSwitchedTime_SrcNodeContainer, gen_jointPackage_CPL2SPL_SrcSubCall_SrcNode, gen_jointPackage_CPL2SPL_SrcAction_SrcNode, gen_jointPackage_CPL2SPL_SrcSignallingAction_SrcAction, gen_jointPackage_CPL2SPL_TrgProgram_TrgLocatedElement, gen_jointPackage_CPL2SPL_TrgStructureProperty_TrgLocatedElement, gen_jointPackage_CPL2SPL_TrgClientErrorResponse_TrgErrorResponse, gen_jointPackage_CPL2SPL_TrgGlobalErrorResponse_TrgErrorResponse, gen_jointPackage_CPL2SPL_SrcNoAnswer_SrcNodeContainer, gen_jointPackage_CPL2SPL_SrcRedirection_SrcNodeContainer, gen_jointPackage_CPL2SPL_SrcFailure_SrcNodeContainer, gen_jointPackage_CPL2SPL_SrcDefault_SrcNodeContainer, gen_jointPackage_CPL2SPL_SrcNode_SrcElement, gen_jointPackage_CPL2SPL_SrcSwitch_SrcNode, gen_jointPackage_CPL2SPL_SrcLocation_SrcNode, gen_jointPackage_CPL2SPL_SrcLocation_SrcNodeContainer, gen_jointPackage_CPL2SPL_TrgSession_TrgLocatedElement, gen_jointPackage_CPL2SPL_TrgRegistration_TrgSession, gen_jointPackage_CPL2SPL_TrgDialog_TrgSession, gen_jointPackage_CPL2SPL_TrgEvent_TrgSession, gen_jointPackage_CPL2SPL_TrgMethod_TrgSession, gen_jointPackage_CPL2SPL_TrgRedirectionErrorResponse_TrgErrorResponse, gen_jointPackage_CPL2SPL_TrgServerErrorResponse_TrgErrorResponse, gen_jointPackage_CPL2SPL_TrgService_TrgLocatedElement, gen_jointPackage_CPL2SPL_TrgMethodName_TrgLocatedElement, gen_jointPackage_CPL2SPL_TrgSIPMethodName_TrgMethodName, gen_jointPackage_CPL2SPL_TrgControlMethodName_TrgMethodName, gen_jointPackage_CPL2SPL_TrgBranch_TrgLocatedElement, gen_jointPackage_CPL2SPL_TrgDefaultBranch_TrgBranch, gen_jointPackage_CPL2SPL_TrgNamedBranch_TrgBranch, gen_jointPackage_CPL2SPL_TrgTypeExpression_TrgLocatedElement, gen_jointPackage_CPL2SPL_TrgSimpleType_TrgTypeExpression, gen_jointPackage_CPL2SPL_TrgSequenceType_TrgTypeExpression, gen_jointPackage_CPL2SPL_TrgDefinedType_TrgTypeExpression, gen_jointPackage_CPL2SPL_TrgDeclaration_TrgLocatedElement, gen_jointPackage_CPL2SPL_TrgArgument_TrgVariableDeclaration, gen_jointPackage_CPL2SPL_TrgRemoteFunctionDeclaration_TrgFunctionDeclaration, gen_jointPackage_CPL2SPL_TrgLocalFunctionDeclaration_TrgFunctionDeclaration, gen_jointPackage_CPL2SPL_TrgStructureDeclaration_TrgDeclaration, gen_jointPackage_CPL2SPL_TrgFunctionCall_TrgLocatedElement, gen_jointPackage_CPL2SPL_TrgVariableDeclaration_TrgDeclaration, gen_jointPackage_CPL2SPL_TrgFunctionDeclaration_TrgDeclaration, gen_jointPackage_CPL2SPL_TrgDeclarationStat_TrgStatement, gen_jointPackage_CPL2SPL_TrgReturnStat_TrgStatement, gen_jointPackage_CPL2SPL_TrgIfStat_TrgStatement, gen_jointPackage_CPL2SPL_TrgStatement_TrgLocatedElement, gen_jointPackage_CPL2SPL_TrgCompoundStat_TrgStatement, gen_jointPackage_CPL2SPL_TrgSetStat_TrgStatement, gen_jointPackage_CPL2SPL_TrgForeachStat_TrgStatement, gen_jointPackage_CPL2SPL_TrgSelectStat_TrgStatement, gen_jointPackage_CPL2SPL_TrgFunctionCallStat_TrgStatement, gen_jointPackage_CPL2SPL_TrgWhenStat_TrgStatement, gen_jointPackage_CPL2SPL_TrgSelectMember_TrgLocatedElement, gen_jointPackage_CPL2SPL_TrgSelectDefault_TrgSelectMember, gen_jointPackage_CPL2SPL_TrgSelectCase_TrgSelectMember, gen_jointPackage_CPL2SPL_TrgExpression_TrgLocatedElement, gen_jointPackage_CPL2SPL_TrgConstantExp_TrgExpression, gen_jointPackage_CPL2SPL_TrgContinueStat_TrgStatement, gen_jointPackage_CPL2SPL_TrgBreakStat_TrgStatement, gen_jointPackage_CPL2SPL_TrgPushStat_TrgStatement, gen_jointPackage_CPL2SPL_TrgWhenHeader_TrgVariableDeclaration, gen_jointPackage_CPL2SPL_TrgForwardExp_TrgExpression, gen_jointPackage_CPL2SPL_TrgWithExp_TrgExpression, gen_jointPackage_CPL2SPL_TrgOperatorExp_TrgExpression, gen_jointPackage_CPL2SPL_TrgReasonExp_TrgExpression, gen_jointPackage_CPL2SPL_TrgBODYExp_TrgExpression, gen_jointPackage_CPL2SPL_TrgRequestURIExp_TrgExpression, gen_jointPackage_CPL2SPL_TrgPopExp_TrgExpression, gen_jointPackage_CPL2SPL_TrgFunctionCallExp_TrgExpression, gen_jointPackage_CPL2SPL_TrgBlockExp_TrgExpression, gen_jointPackage_CPL2SPL_TrgVariablePlace_TrgPlace, gen_jointPackage_CPL2SPL_TrgPropertyCallPlace_TrgVariablePlace, gen_jointPackage_CPL2SPL_TrgVariable_TrgVariablePlace, gen_jointPackage_CPL2SPL_TrgMessageField_TrgLocatedElement, gen_jointPackage_CPL2SPL_TrgPlace_TrgExpression, gen_jointPackage_CPL2SPL_TrgSIPHeaderPlace_TrgPlace, gen_jointPackage_CPL2SPL_TrgBooleanConstant_TrgConstant, gen_jointPackage_CPL2SPL_TrgIntegerConstant_TrgConstant, gen_jointPackage_CPL2SPL_TrgStringConstant_TrgConstant, gen_jointPackage_CPL2SPL_TrgURIConstant_TrgConstant, gen_jointPackage_CPL2SPL_TrgSequenceConstant_TrgConstant, gen_jointPackage_CPL2SPL_TrgResponseConstant_TrgConstant, gen_jointPackage_CPL2SPL_TrgResponse_TrgLocatedElement, gen_jointPackage_CPL2SPL_TrgSuccessResponse_TrgResponse, gen_jointPackage_CPL2SPL_TrgErrorResponse_TrgResponse, gen_jointPackage_CPL2SPL_TrgReasonMessageField_TrgMessageField, gen_jointPackage_CPL2SPL_TrgHeadedMessageField_TrgMessageField, gen_jointPackage_CPL2SPL_TrgConstant_TrgLocatedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)