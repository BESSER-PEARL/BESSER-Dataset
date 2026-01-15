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
BindingDatatype: Enumeration = Enumeration(
    name="BindingDatatype",
    literals={
            EnumerationLiteral(name="early"),
			EnumerationLiteral(name="late")
    }
)

BooleanDatatype: Enumeration = Enumeration(
    name="BooleanDatatype",
    literals={
            EnumerationLiteral(name="true"),
			EnumerationLiteral(name="false")
    }
)

AssignTypeDatatype: Enumeration = Enumeration(
    name="AssignTypeDatatype",
    literals={
            EnumerationLiteral(name="lastchild"),
			EnumerationLiteral(name="previoussibling"),
			EnumerationLiteral(name="nextsibling"),
			EnumerationLiteral(name="replace"),
			EnumerationLiteral(name="delete"),
			EnumerationLiteral(name="addattribute"),
			EnumerationLiteral(name="replacechildren"),
			EnumerationLiteral(name="firstchild")
    }
)

ExmodeDatatype: Enumeration = Enumeration(
    name="ExmodeDatatype",
    literals={
            EnumerationLiteral(name="lax"),
			EnumerationLiteral(name="strict")
    }
)

HistoryTypeDatatype: Enumeration = Enumeration(
    name="HistoryTypeDatatype",
    literals={
            EnumerationLiteral(name="shallow"),
			EnumerationLiteral(name="deep")
    }
)

TransitionTypeDatatype: Enumeration = Enumeration(
    name="TransitionTypeDatatype",
    literals={
            EnumerationLiteral(name="internal"),
			EnumerationLiteral(name="external")
    }
)

# Classes
scxml_DocumentRoot = Class(name="scxml::DocumentRoot")
scxml_EStringToStringMapEntry = Class(name="scxml::EStringToStringMapEntry")
scxml_ScxmlContentType = Class(name="scxml::ScxmlContentType")
scxml_ScxmlDataType = Class(name="scxml::ScxmlDataType")
scxml_ScxmlDatamodelType = Class(name="scxml::ScxmlDatamodelType")
scxml_ScxmlAssignType = Class(name="scxml::ScxmlAssignType")
scxml_ScxmlCancelType = Class(name="scxml::ScxmlCancelType")
scxml_ScxmlElseifType = Class(name="scxml::ScxmlElseifType")
scxml_ScxmlFinalType = Class(name="scxml::ScxmlFinalType")
scxml_ScxmlFinalizeType = Class(name="scxml::ScxmlFinalizeType")
scxml_ScxmlDonedataType = Class(name="scxml::ScxmlDonedataType")
scxml_ScxmlElseType = Class(name="scxml::ScxmlElseType")
scxml_ScxmlHistoryType = Class(name="scxml::ScxmlHistoryType")
scxml_ScxmlIfType = Class(name="scxml::ScxmlIfType")
scxml_ScxmlForeachType = Class(name="scxml::ScxmlForeachType")
scxml_ScxmlInvokeType = Class(name="scxml::ScxmlInvokeType")
scxml_ScxmlLogType = Class(name="scxml::ScxmlLogType")
scxml_ScxmlInitialType = Class(name="scxml::ScxmlInitialType")
scxml_ScxmlParallelType = Class(name="scxml::ScxmlParallelType")
scxml_ScxmlParamType = Class(name="scxml::ScxmlParamType")
scxml_ScxmlRaiseType = Class(name="scxml::ScxmlRaiseType")
scxml_ScxmlOnentryType = Class(name="scxml::ScxmlOnentryType")
scxml_ScxmlOnexitType = Class(name="scxml::ScxmlOnexitType")
scxml_ScxmlSendType = Class(name="scxml::ScxmlSendType")
scxml_ScxmlStateType = Class(name="scxml::ScxmlStateType")
scxml_ScxmlTransitionType = Class(name="scxml::ScxmlTransitionType")
scxml_ScxmlScriptType = Class(name="scxml::ScxmlScriptType")
scxml_ScxmlScxmlType = Class(name="scxml::ScxmlScxmlType")

# scxml_DocumentRoot class attributes and methods
scxml_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
scxml_DocumentRoot.attributes={scxml_DocumentRoot_mixed}

# scxml_EStringToStringMapEntry class attributes and methods

# scxml_ScxmlContentType class attributes and methods
scxml_ScxmlContentType_mixed: Property = Property(name="mixed", type=StringType)
scxml_ScxmlContentType_any: Property = Property(name="any", type=StringType)
scxml_ScxmlContentType_expr: Property = Property(name="expr", type=StringType)
scxml_ScxmlContentType_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
scxml_ScxmlContentType.attributes={scxml_ScxmlContentType_any, scxml_ScxmlContentType_expr, scxml_ScxmlContentType_anyAttribute, scxml_ScxmlContentType_mixed}

# scxml_ScxmlDataType class attributes and methods
scxml_ScxmlDataType_expr: Property = Property(name="expr", type=StringType)
scxml_ScxmlDataType_mixed: Property = Property(name="mixed", type=StringType)
scxml_ScxmlDataType_any: Property = Property(name="any", type=StringType)
scxml_ScxmlDataType_id: Property = Property(name="id", type=StringType)
scxml_ScxmlDataType_src: Property = Property(name="src", type=StringType)
scxml_ScxmlDataType_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
scxml_ScxmlDataType.attributes={scxml_ScxmlDataType_mixed, scxml_ScxmlDataType_expr, scxml_ScxmlDataType_src, scxml_ScxmlDataType_id, scxml_ScxmlDataType_anyAttribute, scxml_ScxmlDataType_any}

# scxml_ScxmlDatamodelType class attributes and methods
scxml_ScxmlDatamodelType_scxmlExtraContent: Property = Property(name="scxmlExtraContent", type=StringType)
scxml_ScxmlDatamodelType_any: Property = Property(name="any", type=StringType)
scxml_ScxmlDatamodelType_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
scxml_ScxmlDatamodelType.attributes={scxml_ScxmlDatamodelType_any, scxml_ScxmlDatamodelType_scxmlExtraContent, scxml_ScxmlDatamodelType_anyAttribute}

# scxml_ScxmlAssignType class attributes and methods
scxml_ScxmlAssignType_expr: Property = Property(name="expr", type=StringType)
scxml_ScxmlAssignType_location: Property = Property(name="location", type=StringType)
scxml_ScxmlAssignType_type: Property = Property(name="type", type=StringType)
scxml_ScxmlAssignType_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
scxml_ScxmlAssignType_mixed: Property = Property(name="mixed", type=StringType)
scxml_ScxmlAssignType_any: Property = Property(name="any", type=StringType)
scxml_ScxmlAssignType_attr: Property = Property(name="attr", type=StringType)
scxml_ScxmlAssignType.attributes={scxml_ScxmlAssignType_any, scxml_ScxmlAssignType_expr, scxml_ScxmlAssignType_location, scxml_ScxmlAssignType_mixed, scxml_ScxmlAssignType_anyAttribute, scxml_ScxmlAssignType_attr, scxml_ScxmlAssignType_type}

# scxml_ScxmlCancelType class attributes and methods
scxml_ScxmlCancelType_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
scxml_ScxmlCancelType_scxmlExtraContent: Property = Property(name="scxmlExtraContent", type=StringType)
scxml_ScxmlCancelType_any: Property = Property(name="any", type=StringType)
scxml_ScxmlCancelType_sendid: Property = Property(name="sendid", type=StringType)
scxml_ScxmlCancelType_sendidexpr: Property = Property(name="sendidexpr", type=StringType)
scxml_ScxmlCancelType.attributes={scxml_ScxmlCancelType_scxmlExtraContent, scxml_ScxmlCancelType_sendidexpr, scxml_ScxmlCancelType_anyAttribute, scxml_ScxmlCancelType_sendid, scxml_ScxmlCancelType_any}

# scxml_ScxmlElseifType class attributes and methods
scxml_ScxmlElseifType_cond: Property = Property(name="cond", type=StringType)
scxml_ScxmlElseifType_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
scxml_ScxmlElseifType.attributes={scxml_ScxmlElseifType_anyAttribute, scxml_ScxmlElseifType_cond}

# scxml_ScxmlFinalType class attributes and methods
scxml_ScxmlFinalType_scxmlFinalMix: Property = Property(name="scxmlFinalMix", type=StringType)
scxml_ScxmlFinalType_any: Property = Property(name="any", type=StringType)
scxml_ScxmlFinalType_id: Property = Property(name="id", type=StringType)
scxml_ScxmlFinalType_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
scxml_ScxmlFinalType.attributes={scxml_ScxmlFinalType_anyAttribute, scxml_ScxmlFinalType_id, scxml_ScxmlFinalType_scxmlFinalMix, scxml_ScxmlFinalType_any}

# scxml_ScxmlFinalizeType class attributes and methods
scxml_ScxmlFinalizeType_scxmlCoreExecutablecontent: Property = Property(name="scxmlCoreExecutablecontent", type=StringType)
scxml_ScxmlFinalizeType_any: Property = Property(name="any", type=StringType)
scxml_ScxmlFinalizeType_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
scxml_ScxmlFinalizeType.attributes={scxml_ScxmlFinalizeType_anyAttribute, scxml_ScxmlFinalizeType_scxmlCoreExecutablecontent, scxml_ScxmlFinalizeType_any}

# scxml_ScxmlDonedataType class attributes and methods
scxml_ScxmlDonedataType_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
scxml_ScxmlDonedataType.attributes={scxml_ScxmlDonedataType_anyAttribute}

# scxml_ScxmlElseType class attributes and methods
scxml_ScxmlElseType_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
scxml_ScxmlElseType.attributes={scxml_ScxmlElseType_anyAttribute}

# scxml_ScxmlHistoryType class attributes and methods
scxml_ScxmlHistoryType_scxmlExtraContent1: Property = Property(name="scxmlExtraContent1", type=StringType)
scxml_ScxmlHistoryType_scxmlExtraContent: Property = Property(name="scxmlExtraContent", type=StringType)
scxml_ScxmlHistoryType_any: Property = Property(name="any", type=StringType)
scxml_ScxmlHistoryType_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
scxml_ScxmlHistoryType_any1: Property = Property(name="any1", type=StringType)
scxml_ScxmlHistoryType_id: Property = Property(name="id", type=StringType)
scxml_ScxmlHistoryType_type: Property = Property(name="type", type=StringType)
scxml_ScxmlHistoryType.attributes={scxml_ScxmlHistoryType_any1, scxml_ScxmlHistoryType_scxmlExtraContent1, scxml_ScxmlHistoryType_any, scxml_ScxmlHistoryType_type, scxml_ScxmlHistoryType_scxmlExtraContent, scxml_ScxmlHistoryType_id, scxml_ScxmlHistoryType_anyAttribute}

# scxml_ScxmlIfType class attributes and methods
scxml_ScxmlIfType_scxmlCoreExecutablecontent: Property = Property(name="scxmlCoreExecutablecontent", type=StringType)
scxml_ScxmlIfType_any: Property = Property(name="any", type=StringType)
scxml_ScxmlIfType_scxmlCoreExecutablecontent1: Property = Property(name="scxmlCoreExecutablecontent1", type=StringType)
scxml_ScxmlIfType_any1: Property = Property(name="any1", type=StringType)
scxml_ScxmlIfType_scxmlCoreExecutablecontent2: Property = Property(name="scxmlCoreExecutablecontent2", type=StringType)
scxml_ScxmlIfType_any2: Property = Property(name="any2", type=StringType)
scxml_ScxmlIfType_cond: Property = Property(name="cond", type=StringType)
scxml_ScxmlIfType_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
scxml_ScxmlIfType.attributes={scxml_ScxmlIfType_scxmlCoreExecutablecontent1, scxml_ScxmlIfType_cond, scxml_ScxmlIfType_scxmlCoreExecutablecontent, scxml_ScxmlIfType_any1, scxml_ScxmlIfType_scxmlCoreExecutablecontent2, scxml_ScxmlIfType_any, scxml_ScxmlIfType_anyAttribute, scxml_ScxmlIfType_any2}

# scxml_ScxmlForeachType class attributes and methods
scxml_ScxmlForeachType_scxmlCoreExecutablecontent: Property = Property(name="scxmlCoreExecutablecontent", type=StringType)
scxml_ScxmlForeachType_any: Property = Property(name="any", type=StringType)
scxml_ScxmlForeachType_item: Property = Property(name="item", type=StringType)
scxml_ScxmlForeachType_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
scxml_ScxmlForeachType_array: Property = Property(name="array", type=StringType)
scxml_ScxmlForeachType_index: Property = Property(name="index", type=StringType)
scxml_ScxmlForeachType.attributes={scxml_ScxmlForeachType_array, scxml_ScxmlForeachType_item, scxml_ScxmlForeachType_scxmlCoreExecutablecontent, scxml_ScxmlForeachType_any, scxml_ScxmlForeachType_index, scxml_ScxmlForeachType_anyAttribute}

# scxml_ScxmlInvokeType class attributes and methods
scxml_ScxmlInvokeType_scxmlInvokeMix: Property = Property(name="scxmlInvokeMix", type=StringType)
scxml_ScxmlInvokeType_any: Property = Property(name="any", type=StringType)
scxml_ScxmlInvokeType_autoforward: Property = Property(name="autoforward", type=StringType)
scxml_ScxmlInvokeType_id: Property = Property(name="id", type=StringType)
scxml_ScxmlInvokeType_idlocation: Property = Property(name="idlocation", type=StringType)
scxml_ScxmlInvokeType_namelist: Property = Property(name="namelist", type=StringType)
scxml_ScxmlInvokeType_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
scxml_ScxmlInvokeType_src: Property = Property(name="src", type=StringType)
scxml_ScxmlInvokeType_srcexpr: Property = Property(name="srcexpr", type=StringType)
scxml_ScxmlInvokeType_type: Property = Property(name="type", type=StringType)
scxml_ScxmlInvokeType_typeexpr: Property = Property(name="typeexpr", type=StringType)
scxml_ScxmlInvokeType.attributes={scxml_ScxmlInvokeType_namelist, scxml_ScxmlInvokeType_any, scxml_ScxmlInvokeType_srcexpr, scxml_ScxmlInvokeType_typeexpr, scxml_ScxmlInvokeType_anyAttribute, scxml_ScxmlInvokeType_idlocation, scxml_ScxmlInvokeType_id, scxml_ScxmlInvokeType_type, scxml_ScxmlInvokeType_src, scxml_ScxmlInvokeType_autoforward, scxml_ScxmlInvokeType_scxmlInvokeMix}

# scxml_ScxmlLogType class attributes and methods
scxml_ScxmlLogType_scxmlExtraContent: Property = Property(name="scxmlExtraContent", type=StringType)
scxml_ScxmlLogType_any: Property = Property(name="any", type=StringType)
scxml_ScxmlLogType_expr: Property = Property(name="expr", type=StringType)
scxml_ScxmlLogType_label: Property = Property(name="label", type=StringType)
scxml_ScxmlLogType_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
scxml_ScxmlLogType.attributes={scxml_ScxmlLogType_anyAttribute, scxml_ScxmlLogType_expr, scxml_ScxmlLogType_scxmlExtraContent, scxml_ScxmlLogType_any, scxml_ScxmlLogType_label}

# scxml_ScxmlInitialType class attributes and methods
scxml_ScxmlInitialType_scxmlExtraContent: Property = Property(name="scxmlExtraContent", type=StringType)
scxml_ScxmlInitialType_scxmlExtraContent1: Property = Property(name="scxmlExtraContent1", type=StringType)
scxml_ScxmlInitialType_any1: Property = Property(name="any1", type=StringType)
scxml_ScxmlInitialType_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
scxml_ScxmlInitialType_any: Property = Property(name="any", type=StringType)
scxml_ScxmlInitialType.attributes={scxml_ScxmlInitialType_anyAttribute, scxml_ScxmlInitialType_any1, scxml_ScxmlInitialType_scxmlExtraContent, scxml_ScxmlInitialType_scxmlExtraContent1, scxml_ScxmlInitialType_any}

# scxml_ScxmlParallelType class attributes and methods
scxml_ScxmlParallelType_scxmlParallelMix: Property = Property(name="scxmlParallelMix", type=StringType)
scxml_ScxmlParallelType_id: Property = Property(name="id", type=StringType)
scxml_ScxmlParallelType_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
scxml_ScxmlParallelType_any: Property = Property(name="any", type=StringType)
scxml_ScxmlParallelType.attributes={scxml_ScxmlParallelType_any, scxml_ScxmlParallelType_anyAttribute, scxml_ScxmlParallelType_scxmlParallelMix, scxml_ScxmlParallelType_id}

# scxml_ScxmlParamType class attributes and methods
scxml_ScxmlParamType_scxmlExtraContent: Property = Property(name="scxmlExtraContent", type=StringType)
scxml_ScxmlParamType_any: Property = Property(name="any", type=StringType)
scxml_ScxmlParamType_expr: Property = Property(name="expr", type=StringType)
scxml_ScxmlParamType_location: Property = Property(name="location", type=StringType)
scxml_ScxmlParamType_name: Property = Property(name="name", type=StringType)
scxml_ScxmlParamType_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
scxml_ScxmlParamType.attributes={scxml_ScxmlParamType_scxmlExtraContent, scxml_ScxmlParamType_name, scxml_ScxmlParamType_anyAttribute, scxml_ScxmlParamType_location, scxml_ScxmlParamType_expr, scxml_ScxmlParamType_any}

# scxml_ScxmlRaiseType class attributes and methods
scxml_ScxmlRaiseType_event: Property = Property(name="event", type=StringType)
scxml_ScxmlRaiseType_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
scxml_ScxmlRaiseType.attributes={scxml_ScxmlRaiseType_event, scxml_ScxmlRaiseType_anyAttribute}

# scxml_ScxmlOnentryType class attributes and methods
scxml_ScxmlOnentryType_any: Property = Property(name="any", type=StringType)
scxml_ScxmlOnentryType_scxmlCoreExecutablecontent: Property = Property(name="scxmlCoreExecutablecontent", type=StringType)
scxml_ScxmlOnentryType_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
scxml_ScxmlOnentryType.attributes={scxml_ScxmlOnentryType_any, scxml_ScxmlOnentryType_anyAttribute, scxml_ScxmlOnentryType_scxmlCoreExecutablecontent}

# scxml_ScxmlOnexitType class attributes and methods
scxml_ScxmlOnexitType_scxmlCoreExecutablecontent: Property = Property(name="scxmlCoreExecutablecontent", type=StringType)
scxml_ScxmlOnexitType_any: Property = Property(name="any", type=StringType)
scxml_ScxmlOnexitType_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
scxml_ScxmlOnexitType.attributes={scxml_ScxmlOnexitType_scxmlCoreExecutablecontent, scxml_ScxmlOnexitType_any, scxml_ScxmlOnexitType_anyAttribute}

# scxml_ScxmlSendType class attributes and methods
scxml_ScxmlSendType_scxmlSendMix: Property = Property(name="scxmlSendMix", type=StringType)
scxml_ScxmlSendType_any: Property = Property(name="any", type=StringType)
scxml_ScxmlSendType_delay: Property = Property(name="delay", type=StringType)
scxml_ScxmlSendType_idlocation: Property = Property(name="idlocation", type=StringType)
scxml_ScxmlSendType_namelist: Property = Property(name="namelist", type=StringType)
scxml_ScxmlSendType_target: Property = Property(name="target", type=StringType)
scxml_ScxmlSendType_targetexpr: Property = Property(name="targetexpr", type=StringType)
scxml_ScxmlSendType_type: Property = Property(name="type", type=StringType)
scxml_ScxmlSendType_typeexpr: Property = Property(name="typeexpr", type=StringType)
scxml_ScxmlSendType_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
scxml_ScxmlSendType_delayexpr: Property = Property(name="delayexpr", type=StringType)
scxml_ScxmlSendType_event: Property = Property(name="event", type=StringType)
scxml_ScxmlSendType_eventexpr: Property = Property(name="eventexpr", type=StringType)
scxml_ScxmlSendType_id: Property = Property(name="id", type=StringType)
scxml_ScxmlSendType.attributes={scxml_ScxmlSendType_typeexpr, scxml_ScxmlSendType_targetexpr, scxml_ScxmlSendType_target, scxml_ScxmlSendType_event, scxml_ScxmlSendType_idlocation, scxml_ScxmlSendType_namelist, scxml_ScxmlSendType_type, scxml_ScxmlSendType_delayexpr, scxml_ScxmlSendType_delay, scxml_ScxmlSendType_scxmlSendMix, scxml_ScxmlSendType_eventexpr, scxml_ScxmlSendType_id, scxml_ScxmlSendType_anyAttribute, scxml_ScxmlSendType_any}

# scxml_ScxmlStateType class attributes and methods
scxml_ScxmlStateType_scxmlStateMix: Property = Property(name="scxmlStateMix", type=StringType)
scxml_ScxmlStateType_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
scxml_ScxmlStateType_any: Property = Property(name="any", type=StringType)
scxml_ScxmlStateType_id: Property = Property(name="id", type=StringType)
scxml_ScxmlStateType_initial1: Property = Property(name="initial1", type=StringType)
scxml_ScxmlStateType.attributes={scxml_ScxmlStateType_scxmlStateMix, scxml_ScxmlStateType_anyAttribute, scxml_ScxmlStateType_any, scxml_ScxmlStateType_initial1, scxml_ScxmlStateType_id}

# scxml_ScxmlTransitionType class attributes and methods
scxml_ScxmlTransitionType_scxmlCoreExecutablecontent: Property = Property(name="scxmlCoreExecutablecontent", type=StringType)
scxml_ScxmlTransitionType_any: Property = Property(name="any", type=StringType)
scxml_ScxmlTransitionType_cond: Property = Property(name="cond", type=StringType)
scxml_ScxmlTransitionType_type: Property = Property(name="type", type=StringType)
scxml_ScxmlTransitionType_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
scxml_ScxmlTransitionType_event: Property = Property(name="event", type=StringType)
scxml_ScxmlTransitionType_target: Property = Property(name="target", type=StringType)
scxml_ScxmlTransitionType.attributes={scxml_ScxmlTransitionType_cond, scxml_ScxmlTransitionType_type, scxml_ScxmlTransitionType_scxmlCoreExecutablecontent, scxml_ScxmlTransitionType_any, scxml_ScxmlTransitionType_event, scxml_ScxmlTransitionType_anyAttribute, scxml_ScxmlTransitionType_target}

# scxml_ScxmlScriptType class attributes and methods
scxml_ScxmlScriptType_mixed: Property = Property(name="mixed", type=StringType)
scxml_ScxmlScriptType_scxmlExtraContent: Property = Property(name="scxmlExtraContent", type=StringType)
scxml_ScxmlScriptType_any: Property = Property(name="any", type=StringType)
scxml_ScxmlScriptType_src: Property = Property(name="src", type=StringType)
scxml_ScxmlScriptType_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
scxml_ScxmlScriptType.attributes={scxml_ScxmlScriptType_mixed, scxml_ScxmlScriptType_anyAttribute, scxml_ScxmlScriptType_any, scxml_ScxmlScriptType_src, scxml_ScxmlScriptType_scxmlExtraContent}

# scxml_ScxmlScxmlType class attributes and methods
scxml_ScxmlScxmlType_scxmlScxmlMix: Property = Property(name="scxmlScxmlMix", type=StringType)
scxml_ScxmlScxmlType_any: Property = Property(name="any", type=StringType)
scxml_ScxmlScxmlType_binding: Property = Property(name="binding", type=StringType)
scxml_ScxmlScxmlType_datamodel1: Property = Property(name="datamodel1", type=StringType)
scxml_ScxmlScxmlType_exmode: Property = Property(name="exmode", type=StringType)
scxml_ScxmlScxmlType_initial: Property = Property(name="initial", type=StringType)
scxml_ScxmlScxmlType_name: Property = Property(name="name", type=StringType)
scxml_ScxmlScxmlType_version: Property = Property(name="version", type=StringType)
scxml_ScxmlScxmlType_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
scxml_ScxmlScxmlType.attributes={scxml_ScxmlScxmlType_scxmlScxmlMix, scxml_ScxmlScxmlType_datamodel1, scxml_ScxmlScxmlType_name, scxml_ScxmlScxmlType_initial, scxml_ScxmlScxmlType_binding, scxml_ScxmlScxmlType_exmode, scxml_ScxmlScxmlType_version, scxml_ScxmlScxmlType_anyAttribute, scxml_ScxmlScxmlType_any}

# Relationships
xMLNSPrefixMap0: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap0",
    ends={
        Property(name="scxml_EStringToStringMapEntry", type=scxml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_DocumentRoot", type=scxml_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cancel6: BinaryAssociation = BinaryAssociation(
    name="cancel6",
    ends={
        Property(name="scxml_ScxmlCancelType", type=scxml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_DocumentRoot7", type=scxml_ScxmlCancelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content8: BinaryAssociation = BinaryAssociation(
    name="content8",
    ends={
        Property(name="scxml_ScxmlContentType", type=scxml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_DocumentRoot9", type=scxml_ScxmlContentType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
data10: BinaryAssociation = BinaryAssociation(
    name="data10",
    ends={
        Property(name="scxml_ScxmlDataType", type=scxml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_DocumentRoot11", type=scxml_ScxmlDataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datamodel12: BinaryAssociation = BinaryAssociation(
    name="datamodel12",
    ends={
        Property(name="scxml_ScxmlDatamodelType", type=scxml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_DocumentRoot13", type=scxml_ScxmlDatamodelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation1: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation1",
    ends={
        Property(name="scxml_EStringToStringMapEntry3", type=scxml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_DocumentRoot2", type=scxml_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assign4: BinaryAssociation = BinaryAssociation(
    name="assign4",
    ends={
        Property(name="scxml_ScxmlAssignType", type=scxml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_DocumentRoot5", type=scxml_ScxmlAssignType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseif18: BinaryAssociation = BinaryAssociation(
    name="elseif18",
    ends={
        Property(name="scxml_ScxmlElseifType", type=scxml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_DocumentRoot19", type=scxml_ScxmlElseifType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
final20: BinaryAssociation = BinaryAssociation(
    name="final20",
    ends={
        Property(name="scxml_ScxmlFinalType", type=scxml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_DocumentRoot21", type=scxml_ScxmlFinalType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
finalize22: BinaryAssociation = BinaryAssociation(
    name="finalize22",
    ends={
        Property(name="scxml_ScxmlFinalizeType", type=scxml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_DocumentRoot23", type=scxml_ScxmlFinalizeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
donedata14: BinaryAssociation = BinaryAssociation(
    name="donedata14",
    ends={
        Property(name="scxml_ScxmlDonedataType", type=scxml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_DocumentRoot15", type=scxml_ScxmlDonedataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
else16: BinaryAssociation = BinaryAssociation(
    name="else16",
    ends={
        Property(name="scxml_ScxmlElseType", type=scxml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_DocumentRoot17", type=scxml_ScxmlElseType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
history26: BinaryAssociation = BinaryAssociation(
    name="history26",
    ends={
        Property(name="scxml_ScxmlHistoryType", type=scxml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_DocumentRoot27", type=scxml_ScxmlHistoryType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
if28: BinaryAssociation = BinaryAssociation(
    name="if28",
    ends={
        Property(name="scxml_ScxmlIfType", type=scxml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_DocumentRoot29", type=scxml_ScxmlIfType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foreach24: BinaryAssociation = BinaryAssociation(
    name="foreach24",
    ends={
        Property(name="scxml_ScxmlForeachType", type=scxml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_DocumentRoot25", type=scxml_ScxmlForeachType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
invoke32: BinaryAssociation = BinaryAssociation(
    name="invoke32",
    ends={
        Property(name="scxml_ScxmlInvokeType", type=scxml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_DocumentRoot33", type=scxml_ScxmlInvokeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
log34: BinaryAssociation = BinaryAssociation(
    name="log34",
    ends={
        Property(name="scxml_ScxmlLogType", type=scxml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_DocumentRoot35", type=scxml_ScxmlLogType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initial30: BinaryAssociation = BinaryAssociation(
    name="initial30",
    ends={
        Property(name="scxml_ScxmlInitialType", type=scxml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_DocumentRoot31", type=scxml_ScxmlInitialType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parallel40: BinaryAssociation = BinaryAssociation(
    name="parallel40",
    ends={
        Property(name="scxml_ScxmlParallelType", type=scxml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_DocumentRoot41", type=scxml_ScxmlParallelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
param42: BinaryAssociation = BinaryAssociation(
    name="param42",
    ends={
        Property(name="scxml_ScxmlParamType", type=scxml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_DocumentRoot43", type=scxml_ScxmlParamType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
raise44: BinaryAssociation = BinaryAssociation(
    name="raise44",
    ends={
        Property(name="scxml_ScxmlRaiseType", type=scxml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_DocumentRoot45", type=scxml_ScxmlRaiseType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
onentry36: BinaryAssociation = BinaryAssociation(
    name="onentry36",
    ends={
        Property(name="scxml_ScxmlOnentryType", type=scxml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_DocumentRoot37", type=scxml_ScxmlOnentryType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
onexit38: BinaryAssociation = BinaryAssociation(
    name="onexit38",
    ends={
        Property(name="scxml_ScxmlOnexitType", type=scxml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_DocumentRoot39", type=scxml_ScxmlOnexitType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
send50: BinaryAssociation = BinaryAssociation(
    name="send50",
    ends={
        Property(name="scxml_ScxmlSendType", type=scxml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_DocumentRoot51", type=scxml_ScxmlSendType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state52: BinaryAssociation = BinaryAssociation(
    name="state52",
    ends={
        Property(name="scxml_ScxmlStateType", type=scxml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_DocumentRoot53", type=scxml_ScxmlStateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition54: BinaryAssociation = BinaryAssociation(
    name="transition54",
    ends={
        Property(name="scxml_ScxmlTransitionType", type=scxml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_DocumentRoot55", type=scxml_ScxmlTransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script46: BinaryAssociation = BinaryAssociation(
    name="script46",
    ends={
        Property(name="scxml_ScxmlScriptType", type=scxml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_DocumentRoot47", type=scxml_ScxmlScriptType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scxml48: BinaryAssociation = BinaryAssociation(
    name="scxml48",
    ends={
        Property(name="scxml_ScxmlScxmlType", type=scxml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_DocumentRoot49", type=scxml_ScxmlScxmlType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
data56: BinaryAssociation = BinaryAssociation(
    name="data56",
    ends={
        Property(name="scxml_ScxmlDataType58", type=scxml_ScxmlDatamodelType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlDatamodelType57", type=scxml_ScxmlDataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content59: BinaryAssociation = BinaryAssociation(
    name="content59",
    ends={
        Property(name="scxml_ScxmlContentType61", type=scxml_ScxmlDonedataType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlDonedataType60", type=scxml_ScxmlContentType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
param62: BinaryAssociation = BinaryAssociation(
    name="param62",
    ends={
        Property(name="scxml_ScxmlParamType64", type=scxml_ScxmlDonedataType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlDonedataType63", type=scxml_ScxmlParamType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
raise65: BinaryAssociation = BinaryAssociation(
    name="raise65",
    ends={
        Property(name="scxml_ScxmlRaiseType67", type=scxml_ScxmlFinalizeType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlFinalizeType66", type=scxml_ScxmlRaiseType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
if68: BinaryAssociation = BinaryAssociation(
    name="if68",
    ends={
        Property(name="scxml_ScxmlIfType70", type=scxml_ScxmlFinalizeType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlFinalizeType69", type=scxml_ScxmlIfType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foreach71: BinaryAssociation = BinaryAssociation(
    name="foreach71",
    ends={
        Property(name="scxml_ScxmlForeachType73", type=scxml_ScxmlFinalizeType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlFinalizeType72", type=scxml_ScxmlForeachType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
send74: BinaryAssociation = BinaryAssociation(
    name="send74",
    ends={
        Property(name="scxml_ScxmlSendType76", type=scxml_ScxmlFinalizeType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlFinalizeType75", type=scxml_ScxmlSendType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script77: BinaryAssociation = BinaryAssociation(
    name="script77",
    ends={
        Property(name="scxml_ScxmlScriptType79", type=scxml_ScxmlFinalizeType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlFinalizeType78", type=scxml_ScxmlScriptType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assign80: BinaryAssociation = BinaryAssociation(
    name="assign80",
    ends={
        Property(name="scxml_ScxmlAssignType82", type=scxml_ScxmlFinalizeType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlFinalizeType81", type=scxml_ScxmlAssignType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
log83: BinaryAssociation = BinaryAssociation(
    name="log83",
    ends={
        Property(name="scxml_ScxmlLogType85", type=scxml_ScxmlFinalizeType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlFinalizeType84", type=scxml_ScxmlLogType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cancel86: BinaryAssociation = BinaryAssociation(
    name="cancel86",
    ends={
        Property(name="scxml_ScxmlCancelType88", type=scxml_ScxmlFinalizeType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlFinalizeType87", type=scxml_ScxmlCancelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
onentry89: BinaryAssociation = BinaryAssociation(
    name="onentry89",
    ends={
        Property(name="scxml_ScxmlOnentryType91", type=scxml_ScxmlFinalType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlFinalType90", type=scxml_ScxmlOnentryType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
onexit92: BinaryAssociation = BinaryAssociation(
    name="onexit92",
    ends={
        Property(name="scxml_ScxmlOnexitType94", type=scxml_ScxmlFinalType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlFinalType93", type=scxml_ScxmlOnexitType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
donedata95: BinaryAssociation = BinaryAssociation(
    name="donedata95",
    ends={
        Property(name="scxml_ScxmlDonedataType97", type=scxml_ScxmlFinalType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlFinalType96", type=scxml_ScxmlDonedataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
raise98: BinaryAssociation = BinaryAssociation(
    name="raise98",
    ends={
        Property(name="scxml_ScxmlRaiseType100", type=scxml_ScxmlForeachType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlForeachType99", type=scxml_ScxmlRaiseType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
if101: BinaryAssociation = BinaryAssociation(
    name="if101",
    ends={
        Property(name="scxml_ScxmlIfType103", type=scxml_ScxmlForeachType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlForeachType102", type=scxml_ScxmlIfType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foreach105: BinaryAssociation = BinaryAssociation(
    name="foreach105",
    ends={
        Property(name="scxml_ScxmlForeachType106", type=scxml_ScxmlForeachType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlForeachType104", type=scxml_ScxmlForeachType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
send107: BinaryAssociation = BinaryAssociation(
    name="send107",
    ends={
        Property(name="scxml_ScxmlSendType109", type=scxml_ScxmlForeachType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlForeachType108", type=scxml_ScxmlSendType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script110: BinaryAssociation = BinaryAssociation(
    name="script110",
    ends={
        Property(name="scxml_ScxmlScriptType112", type=scxml_ScxmlForeachType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlForeachType111", type=scxml_ScxmlScriptType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assign113: BinaryAssociation = BinaryAssociation(
    name="assign113",
    ends={
        Property(name="scxml_ScxmlAssignType115", type=scxml_ScxmlForeachType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlForeachType114", type=scxml_ScxmlAssignType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
log116: BinaryAssociation = BinaryAssociation(
    name="log116",
    ends={
        Property(name="scxml_ScxmlLogType118", type=scxml_ScxmlForeachType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlForeachType117", type=scxml_ScxmlLogType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cancel119: BinaryAssociation = BinaryAssociation(
    name="cancel119",
    ends={
        Property(name="scxml_ScxmlCancelType121", type=scxml_ScxmlForeachType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlForeachType120", type=scxml_ScxmlCancelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition122: BinaryAssociation = BinaryAssociation(
    name="transition122",
    ends={
        Property(name="scxml_ScxmlTransitionType124", type=scxml_ScxmlHistoryType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlHistoryType123", type=scxml_ScxmlTransitionType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
raise125: BinaryAssociation = BinaryAssociation(
    name="raise125",
    ends={
        Property(name="scxml_ScxmlRaiseType127", type=scxml_ScxmlIfType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlIfType126", type=scxml_ScxmlRaiseType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
if129: BinaryAssociation = BinaryAssociation(
    name="if129",
    ends={
        Property(name="scxml_ScxmlIfType130", type=scxml_ScxmlIfType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlIfType128", type=scxml_ScxmlIfType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
send134: BinaryAssociation = BinaryAssociation(
    name="send134",
    ends={
        Property(name="scxml_ScxmlSendType136", type=scxml_ScxmlIfType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlIfType135", type=scxml_ScxmlSendType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script137: BinaryAssociation = BinaryAssociation(
    name="script137",
    ends={
        Property(name="scxml_ScxmlScriptType139", type=scxml_ScxmlIfType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlIfType138", type=scxml_ScxmlScriptType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assign140: BinaryAssociation = BinaryAssociation(
    name="assign140",
    ends={
        Property(name="scxml_ScxmlAssignType142", type=scxml_ScxmlIfType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlIfType141", type=scxml_ScxmlAssignType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foreach131: BinaryAssociation = BinaryAssociation(
    name="foreach131",
    ends={
        Property(name="scxml_ScxmlForeachType133", type=scxml_ScxmlIfType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlIfType132", type=scxml_ScxmlForeachType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseif149: BinaryAssociation = BinaryAssociation(
    name="elseif149",
    ends={
        Property(name="scxml_ScxmlElseifType151", type=scxml_ScxmlIfType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlIfType150", type=scxml_ScxmlElseifType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
raise1152: BinaryAssociation = BinaryAssociation(
    name="raise1152",
    ends={
        Property(name="scxml_ScxmlRaiseType154", type=scxml_ScxmlIfType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlIfType153", type=scxml_ScxmlRaiseType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
log143: BinaryAssociation = BinaryAssociation(
    name="log143",
    ends={
        Property(name="scxml_ScxmlLogType145", type=scxml_ScxmlIfType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlIfType144", type=scxml_ScxmlLogType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cancel146: BinaryAssociation = BinaryAssociation(
    name="cancel146",
    ends={
        Property(name="scxml_ScxmlCancelType148", type=scxml_ScxmlIfType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlIfType147", type=scxml_ScxmlCancelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foreach1158: BinaryAssociation = BinaryAssociation(
    name="foreach1158",
    ends={
        Property(name="scxml_ScxmlForeachType160", type=scxml_ScxmlIfType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlIfType159", type=scxml_ScxmlForeachType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
send1161: BinaryAssociation = BinaryAssociation(
    name="send1161",
    ends={
        Property(name="scxml_ScxmlSendType163", type=scxml_ScxmlIfType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlIfType162", type=scxml_ScxmlSendType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script1164: BinaryAssociation = BinaryAssociation(
    name="script1164",
    ends={
        Property(name="scxml_ScxmlScriptType166", type=scxml_ScxmlIfType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlIfType165", type=scxml_ScxmlScriptType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
if1156: BinaryAssociation = BinaryAssociation(
    name="if1156",
    ends={
        Property(name="scxml_ScxmlIfType157", type=scxml_ScxmlIfType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlIfType155", type=scxml_ScxmlIfType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cancel1173: BinaryAssociation = BinaryAssociation(
    name="cancel1173",
    ends={
        Property(name="scxml_ScxmlCancelType175", type=scxml_ScxmlIfType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlIfType174", type=scxml_ScxmlCancelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
else176: BinaryAssociation = BinaryAssociation(
    name="else176",
    ends={
        Property(name="scxml_ScxmlElseType178", type=scxml_ScxmlIfType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlIfType177", type=scxml_ScxmlElseType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assign1167: BinaryAssociation = BinaryAssociation(
    name="assign1167",
    ends={
        Property(name="scxml_ScxmlAssignType169", type=scxml_ScxmlIfType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlIfType168", type=scxml_ScxmlAssignType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
log1170: BinaryAssociation = BinaryAssociation(
    name="log1170",
    ends={
        Property(name="scxml_ScxmlLogType172", type=scxml_ScxmlIfType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlIfType171", type=scxml_ScxmlLogType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foreach2185: BinaryAssociation = BinaryAssociation(
    name="foreach2185",
    ends={
        Property(name="scxml_ScxmlForeachType187", type=scxml_ScxmlIfType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlIfType186", type=scxml_ScxmlForeachType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
send2188: BinaryAssociation = BinaryAssociation(
    name="send2188",
    ends={
        Property(name="scxml_ScxmlSendType190", type=scxml_ScxmlIfType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlIfType189", type=scxml_ScxmlSendType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script2191: BinaryAssociation = BinaryAssociation(
    name="script2191",
    ends={
        Property(name="scxml_ScxmlScriptType193", type=scxml_ScxmlIfType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlIfType192", type=scxml_ScxmlScriptType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
raise2179: BinaryAssociation = BinaryAssociation(
    name="raise2179",
    ends={
        Property(name="scxml_ScxmlRaiseType181", type=scxml_ScxmlIfType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlIfType180", type=scxml_ScxmlRaiseType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
if2183: BinaryAssociation = BinaryAssociation(
    name="if2183",
    ends={
        Property(name="scxml_ScxmlIfType184", type=scxml_ScxmlIfType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlIfType182", type=scxml_ScxmlIfType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cancel2200: BinaryAssociation = BinaryAssociation(
    name="cancel2200",
    ends={
        Property(name="scxml_ScxmlCancelType202", type=scxml_ScxmlIfType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlIfType201", type=scxml_ScxmlCancelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assign2194: BinaryAssociation = BinaryAssociation(
    name="assign2194",
    ends={
        Property(name="scxml_ScxmlAssignType196", type=scxml_ScxmlIfType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlIfType195", type=scxml_ScxmlAssignType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
log2197: BinaryAssociation = BinaryAssociation(
    name="log2197",
    ends={
        Property(name="scxml_ScxmlLogType199", type=scxml_ScxmlIfType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlIfType198", type=scxml_ScxmlLogType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content206: BinaryAssociation = BinaryAssociation(
    name="content206",
    ends={
        Property(name="scxml_ScxmlContentType208", type=scxml_ScxmlInvokeType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlInvokeType207", type=scxml_ScxmlContentType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition203: BinaryAssociation = BinaryAssociation(
    name="transition203",
    ends={
        Property(name="scxml_ScxmlTransitionType205", type=scxml_ScxmlInitialType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlInitialType204", type=scxml_ScxmlTransitionType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
finalize212: BinaryAssociation = BinaryAssociation(
    name="finalize212",
    ends={
        Property(name="scxml_ScxmlInvokeType213", type=scxml_ScxmlFinalizeType, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="scxml_ScxmlFinalizeType214", type=scxml_ScxmlInvokeType, multiplicity=Multiplicity(1, 1))
    }
)
param209: BinaryAssociation = BinaryAssociation(
    name="param209",
    ends={
        Property(name="scxml_ScxmlParamType211", type=scxml_ScxmlInvokeType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlInvokeType210", type=scxml_ScxmlParamType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
raise215: BinaryAssociation = BinaryAssociation(
    name="raise215",
    ends={
        Property(name="scxml_ScxmlRaiseType217", type=scxml_ScxmlOnentryType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlOnentryType216", type=scxml_ScxmlRaiseType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
if218: BinaryAssociation = BinaryAssociation(
    name="if218",
    ends={
        Property(name="scxml_ScxmlIfType220", type=scxml_ScxmlOnentryType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlOnentryType219", type=scxml_ScxmlIfType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
send224: BinaryAssociation = BinaryAssociation(
    name="send224",
    ends={
        Property(name="scxml_ScxmlSendType226", type=scxml_ScxmlOnentryType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlOnentryType225", type=scxml_ScxmlSendType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script227: BinaryAssociation = BinaryAssociation(
    name="script227",
    ends={
        Property(name="scxml_ScxmlScriptType229", type=scxml_ScxmlOnentryType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlOnentryType228", type=scxml_ScxmlScriptType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foreach221: BinaryAssociation = BinaryAssociation(
    name="foreach221",
    ends={
        Property(name="scxml_ScxmlForeachType223", type=scxml_ScxmlOnentryType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlOnentryType222", type=scxml_ScxmlForeachType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
log233: BinaryAssociation = BinaryAssociation(
    name="log233",
    ends={
        Property(name="scxml_ScxmlLogType235", type=scxml_ScxmlOnentryType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlOnentryType234", type=scxml_ScxmlLogType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cancel236: BinaryAssociation = BinaryAssociation(
    name="cancel236",
    ends={
        Property(name="scxml_ScxmlCancelType238", type=scxml_ScxmlOnentryType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlOnentryType237", type=scxml_ScxmlCancelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assign230: BinaryAssociation = BinaryAssociation(
    name="assign230",
    ends={
        Property(name="scxml_ScxmlAssignType232", type=scxml_ScxmlOnentryType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlOnentryType231", type=scxml_ScxmlAssignType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
raise239: BinaryAssociation = BinaryAssociation(
    name="raise239",
    ends={
        Property(name="scxml_ScxmlRaiseType241", type=scxml_ScxmlOnexitType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlOnexitType240", type=scxml_ScxmlRaiseType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
if242: BinaryAssociation = BinaryAssociation(
    name="if242",
    ends={
        Property(name="scxml_ScxmlIfType244", type=scxml_ScxmlOnexitType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlOnexitType243", type=scxml_ScxmlIfType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foreach245: BinaryAssociation = BinaryAssociation(
    name="foreach245",
    ends={
        Property(name="scxml_ScxmlForeachType247", type=scxml_ScxmlOnexitType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlOnexitType246", type=scxml_ScxmlForeachType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script251: BinaryAssociation = BinaryAssociation(
    name="script251",
    ends={
        Property(name="scxml_ScxmlScriptType253", type=scxml_ScxmlOnexitType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlOnexitType252", type=scxml_ScxmlScriptType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assign254: BinaryAssociation = BinaryAssociation(
    name="assign254",
    ends={
        Property(name="scxml_ScxmlAssignType256", type=scxml_ScxmlOnexitType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlOnexitType255", type=scxml_ScxmlAssignType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
log257: BinaryAssociation = BinaryAssociation(
    name="log257",
    ends={
        Property(name="scxml_ScxmlLogType259", type=scxml_ScxmlOnexitType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlOnexitType258", type=scxml_ScxmlLogType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
send248: BinaryAssociation = BinaryAssociation(
    name="send248",
    ends={
        Property(name="scxml_ScxmlSendType250", type=scxml_ScxmlOnexitType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlOnexitType249", type=scxml_ScxmlSendType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
onentry263: BinaryAssociation = BinaryAssociation(
    name="onentry263",
    ends={
        Property(name="scxml_ScxmlOnentryType265", type=scxml_ScxmlParallelType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlParallelType264", type=scxml_ScxmlOnentryType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
onexit266: BinaryAssociation = BinaryAssociation(
    name="onexit266",
    ends={
        Property(name="scxml_ScxmlOnexitType268", type=scxml_ScxmlParallelType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlParallelType267", type=scxml_ScxmlOnexitType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cancel260: BinaryAssociation = BinaryAssociation(
    name="cancel260",
    ends={
        Property(name="scxml_ScxmlCancelType262", type=scxml_ScxmlOnexitType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlOnexitType261", type=scxml_ScxmlCancelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parallel276: BinaryAssociation = BinaryAssociation(
    name="parallel276",
    ends={
        Property(name="scxml_ScxmlParallelType277", type=scxml_ScxmlParallelType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlParallelType275", type=scxml_ScxmlParallelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
history278: BinaryAssociation = BinaryAssociation(
    name="history278",
    ends={
        Property(name="scxml_ScxmlHistoryType280", type=scxml_ScxmlParallelType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlParallelType279", type=scxml_ScxmlHistoryType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datamodel281: BinaryAssociation = BinaryAssociation(
    name="datamodel281",
    ends={
        Property(name="scxml_ScxmlDatamodelType283", type=scxml_ScxmlParallelType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlParallelType282", type=scxml_ScxmlDatamodelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition269: BinaryAssociation = BinaryAssociation(
    name="transition269",
    ends={
        Property(name="scxml_ScxmlTransitionType271", type=scxml_ScxmlParallelType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlParallelType270", type=scxml_ScxmlTransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state272: BinaryAssociation = BinaryAssociation(
    name="state272",
    ends={
        Property(name="scxml_ScxmlStateType274", type=scxml_ScxmlParallelType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlParallelType273", type=scxml_ScxmlStateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
invoke284: BinaryAssociation = BinaryAssociation(
    name="invoke284",
    ends={
        Property(name="scxml_ScxmlInvokeType286", type=scxml_ScxmlParallelType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlParallelType285", type=scxml_ScxmlInvokeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state287: BinaryAssociation = BinaryAssociation(
    name="state287",
    ends={
        Property(name="scxml_ScxmlStateType289", type=scxml_ScxmlScxmlType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlScxmlType288", type=scxml_ScxmlStateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parallel290: BinaryAssociation = BinaryAssociation(
    name="parallel290",
    ends={
        Property(name="scxml_ScxmlParallelType292", type=scxml_ScxmlScxmlType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlScxmlType291", type=scxml_ScxmlParallelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
final293: BinaryAssociation = BinaryAssociation(
    name="final293",
    ends={
        Property(name="scxml_ScxmlFinalType295", type=scxml_ScxmlScxmlType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlScxmlType294", type=scxml_ScxmlFinalType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datamodel296: BinaryAssociation = BinaryAssociation(
    name="datamodel296",
    ends={
        Property(name="scxml_ScxmlDatamodelType298", type=scxml_ScxmlScxmlType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlScxmlType297", type=scxml_ScxmlDatamodelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script299: BinaryAssociation = BinaryAssociation(
    name="script299",
    ends={
        Property(name="scxml_ScxmlScriptType301", type=scxml_ScxmlScxmlType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlScxmlType300", type=scxml_ScxmlScriptType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content302: BinaryAssociation = BinaryAssociation(
    name="content302",
    ends={
        Property(name="scxml_ScxmlContentType304", type=scxml_ScxmlSendType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlSendType303", type=scxml_ScxmlContentType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
param305: BinaryAssociation = BinaryAssociation(
    name="param305",
    ends={
        Property(name="scxml_ScxmlParamType307", type=scxml_ScxmlSendType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlSendType306", type=scxml_ScxmlParamType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
onexit311: BinaryAssociation = BinaryAssociation(
    name="onexit311",
    ends={
        Property(name="scxml_ScxmlOnexitType313", type=scxml_ScxmlStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlStateType312", type=scxml_ScxmlOnexitType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition314: BinaryAssociation = BinaryAssociation(
    name="transition314",
    ends={
        Property(name="scxml_ScxmlTransitionType316", type=scxml_ScxmlStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlStateType315", type=scxml_ScxmlTransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initial317: BinaryAssociation = BinaryAssociation(
    name="initial317",
    ends={
        Property(name="scxml_ScxmlInitialType319", type=scxml_ScxmlStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlStateType318", type=scxml_ScxmlInitialType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state321: BinaryAssociation = BinaryAssociation(
    name="state321",
    ends={
        Property(name="scxml_ScxmlStateType322", type=scxml_ScxmlStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlStateType320", type=scxml_ScxmlStateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
onentry308: BinaryAssociation = BinaryAssociation(
    name="onentry308",
    ends={
        Property(name="scxml_ScxmlOnentryType310", type=scxml_ScxmlStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlStateType309", type=scxml_ScxmlOnentryType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
final326: BinaryAssociation = BinaryAssociation(
    name="final326",
    ends={
        Property(name="scxml_ScxmlFinalType328", type=scxml_ScxmlStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlStateType327", type=scxml_ScxmlFinalType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
history329: BinaryAssociation = BinaryAssociation(
    name="history329",
    ends={
        Property(name="scxml_ScxmlHistoryType331", type=scxml_ScxmlStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlStateType330", type=scxml_ScxmlHistoryType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datamodel332: BinaryAssociation = BinaryAssociation(
    name="datamodel332",
    ends={
        Property(name="scxml_ScxmlDatamodelType334", type=scxml_ScxmlStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlStateType333", type=scxml_ScxmlDatamodelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
invoke335: BinaryAssociation = BinaryAssociation(
    name="invoke335",
    ends={
        Property(name="scxml_ScxmlInvokeType337", type=scxml_ScxmlStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlStateType336", type=scxml_ScxmlInvokeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parallel323: BinaryAssociation = BinaryAssociation(
    name="parallel323",
    ends={
        Property(name="scxml_ScxmlParallelType325", type=scxml_ScxmlStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlStateType324", type=scxml_ScxmlParallelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
raise338: BinaryAssociation = BinaryAssociation(
    name="raise338",
    ends={
        Property(name="scxml_ScxmlRaiseType340", type=scxml_ScxmlTransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlTransitionType339", type=scxml_ScxmlRaiseType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foreach344: BinaryAssociation = BinaryAssociation(
    name="foreach344",
    ends={
        Property(name="scxml_ScxmlForeachType346", type=scxml_ScxmlTransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlTransitionType345", type=scxml_ScxmlForeachType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
send347: BinaryAssociation = BinaryAssociation(
    name="send347",
    ends={
        Property(name="scxml_ScxmlSendType349", type=scxml_ScxmlTransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlTransitionType348", type=scxml_ScxmlSendType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script350: BinaryAssociation = BinaryAssociation(
    name="script350",
    ends={
        Property(name="scxml_ScxmlScriptType352", type=scxml_ScxmlTransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlTransitionType351", type=scxml_ScxmlScriptType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assign353: BinaryAssociation = BinaryAssociation(
    name="assign353",
    ends={
        Property(name="scxml_ScxmlAssignType355", type=scxml_ScxmlTransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlTransitionType354", type=scxml_ScxmlAssignType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
if341: BinaryAssociation = BinaryAssociation(
    name="if341",
    ends={
        Property(name="scxml_ScxmlIfType343", type=scxml_ScxmlTransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlTransitionType342", type=scxml_ScxmlIfType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cancel359: BinaryAssociation = BinaryAssociation(
    name="cancel359",
    ends={
        Property(name="scxml_ScxmlCancelType361", type=scxml_ScxmlTransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlTransitionType360", type=scxml_ScxmlCancelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
log356: BinaryAssociation = BinaryAssociation(
    name="log356",
    ends={
        Property(name="scxml_ScxmlLogType358", type=scxml_ScxmlTransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlTransitionType357", type=scxml_ScxmlLogType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="scxml",
    types={scxml_DocumentRoot, scxml_EStringToStringMapEntry, scxml_ScxmlContentType, scxml_ScxmlDataType, scxml_ScxmlDatamodelType, scxml_ScxmlAssignType, scxml_ScxmlCancelType, scxml_ScxmlElseifType, scxml_ScxmlFinalType, scxml_ScxmlFinalizeType, scxml_ScxmlDonedataType, scxml_ScxmlElseType, scxml_ScxmlHistoryType, scxml_ScxmlIfType, scxml_ScxmlForeachType, scxml_ScxmlInvokeType, scxml_ScxmlLogType, scxml_ScxmlInitialType, scxml_ScxmlParallelType, scxml_ScxmlParamType, scxml_ScxmlRaiseType, scxml_ScxmlOnentryType, scxml_ScxmlOnexitType, scxml_ScxmlSendType, scxml_ScxmlStateType, scxml_ScxmlTransitionType, scxml_ScxmlScriptType, scxml_ScxmlScxmlType, BindingDatatype, BooleanDatatype, AssignTypeDatatype, ExmodeDatatype, HistoryTypeDatatype, TransitionTypeDatatype},
    associations={xMLNSPrefixMap0, cancel6, content8, data10, datamodel12, xSISchemaLocation1, assign4, elseif18, final20, finalize22, donedata14, else16, history26, if28, foreach24, invoke32, log34, initial30, parallel40, param42, raise44, onentry36, onexit38, send50, state52, transition54, script46, scxml48, data56, content59, param62, raise65, if68, foreach71, send74, script77, assign80, log83, cancel86, onentry89, onexit92, donedata95, raise98, if101, foreach105, send107, script110, assign113, log116, cancel119, transition122, raise125, if129, send134, script137, assign140, foreach131, elseif149, raise1152, log143, cancel146, foreach1158, send1161, script1164, if1156, cancel1173, else176, assign1167, log1170, foreach2185, send2188, script2191, raise2179, if2183, cancel2200, assign2194, log2197, content206, transition203, finalize212, param209, raise215, if218, send224, script227, foreach221, log233, cancel236, assign230, raise239, if242, foreach245, script251, assign254, log257, send248, onentry263, onexit266, cancel260, parallel276, history278, datamodel281, transition269, state272, invoke284, state287, parallel290, final293, datamodel296, script299, content302, param305, onexit311, transition314, initial317, state321, onentry308, final326, history329, datamodel332, invoke335, parallel323, raise338, foreach344, send347, script350, assign353, if341, cancel359, log356},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)