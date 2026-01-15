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
ObjectType2: Enumeration = Enumeration(
    name="ObjectType2",
    literals={
            EnumerationLiteral(name="MISC"),
			EnumerationLiteral(name="SEQUENTIAL"),
			EnumerationLiteral(name="VERSIONING"),
			EnumerationLiteral(name="group"),
			EnumerationLiteral(name="argument"),
			EnumerationLiteral(name="template")
    }
)

ObjectType3: Enumeration = Enumeration(
    name="ObjectType3",
    literals={
            EnumerationLiteral(name="template"),
			EnumerationLiteral(name="argument"),
			EnumerationLiteral(name="collection"),
			EnumerationLiteral(name="person"),
			EnumerationLiteral(name="exhibit"),
			EnumerationLiteral(name="memo"),
			EnumerationLiteral(name="group"),
			EnumerationLiteral(name="discoveryMethod")
    }
)

ObjectType: Enumeration = Enumeration(
    name="ObjectType",
    literals={
            EnumerationLiteral(name="template"),
			EnumerationLiteral(name="argument"),
			EnumerationLiteral(name="collection"),
			EnumerationLiteral(name="person"),
			EnumerationLiteral(name="exhibit"),
			EnumerationLiteral(name="memo"),
			EnumerationLiteral(name="group"),
			EnumerationLiteral(name="discoveryMethod")
    }
)

ObjectType1: Enumeration = Enumeration(
    name="ObjectType1",
    literals={
            EnumerationLiteral(name="discoveryMethod"),
			EnumerationLiteral(name="template"),
			EnumerationLiteral(name="argument"),
			EnumerationLiteral(name="collection"),
			EnumerationLiteral(name="person"),
			EnumerationLiteral(name="exhibit"),
			EnumerationLiteral(name="memo"),
			EnumerationLiteral(name="group")
    }
)

Type: Enumeration = Enumeration(
    name="Type",
    literals={
            EnumerationLiteral(name="Url"),
			EnumerationLiteral(name="Template"),
			EnumerationLiteral(name="Urldir")
    }
)

# Classes
aml_AggregationRule = Class(name="aml::AggregationRule")
aml_EObject = Class(name="aml::EObject")
aml_Parameter = Class(name="aml::Parameter")
aml_AmlDocument = Class(name="aml::AmlDocument")
aml_Template = Class(name="aml::Template")
aml_Argument = Class(name="aml::Argument")
aml_Exhibit = Class(name="aml::Exhibit")
aml_Collection = Class(name="aml::Collection")
aml_Person = Class(name="aml::Person")
aml_Memo = Class(name="aml::Memo")
aml_DiscoveryMethod = Class(name="aml::DiscoveryMethod")
aml_Annotation = Class(name="aml::Annotation")
aml_Flag = Class(name="aml::Flag")
aml_Answer = Class(name="aml::Answer")
aml_Belief = Class(name="aml::Belief")
aml_Witness = Class(name="aml::Witness")
aml_Evidence = Class(name="aml::Evidence")
aml_ArgumentTemplate = Class(name="aml::ArgumentTemplate")
aml_MetaData = Class(name="aml::MetaData")
aml_CreatingTool = Class(name="aml::CreatingTool")
aml_Choice = Class(name="aml::Choice")
aml_CollectionItem = Class(name="aml::CollectionItem")
aml_Question = Class(name="aml::Question")
aml_Coverage = Class(name="aml::Coverage")
aml_NationState = Class(name="aml::NationState")
aml_Creator = Class(name="aml::Creator")
aml_DocumentRoot = Class(name="aml::DocumentRoot")
aml_Dependent = Class(name="aml::Dependent")
aml_EStringToStringMapEntry = Class(name="aml::EStringToStringMapEntry")
aml_End = Class(name="aml::End")
aml_EvidenceExhibit = Class(name="aml::EvidenceExhibit")
aml_Interval = Class(name="aml::Interval")
aml_List = Class(name="aml::List")
aml_QuestionRelationships = Class(name="aml::QuestionRelationships")
aml_Period = Class(name="aml::Period")
aml_Publisher = Class(name="aml::Publisher")
aml_Reader = Class(name="aml::Reader")
aml_Relevance = Class(name="aml::Relevance")
aml_Reliability = Class(name="aml::Reliability")
aml_Start = Class(name="aml::Start")
aml_Value = Class(name="aml::Value")

# aml_AggregationRule class attributes and methods

# aml_EObject class attributes and methods

# aml_Parameter class attributes and methods
aml_Parameter_symbol: Property = Property(name="symbol", type=StringType)
aml_Parameter.attributes={aml_Parameter_symbol}

# aml_AmlDocument class attributes and methods
aml_AmlDocument_group: Property = Property(name="group", type=StringType)
aml_AmlDocument_version: Property = Property(name="version", type=StringType)
aml_AmlDocument.attributes={aml_AmlDocument_group, aml_AmlDocument_version}

# aml_Template class attributes and methods
aml_Template_id: Property = Property(name="id", type=StringType)
aml_Template.attributes={aml_Template_id}

# aml_Argument class attributes and methods
aml_Argument_id: Property = Property(name="id", type=StringType)
aml_Argument.attributes={aml_Argument_id}

# aml_Exhibit class attributes and methods
aml_Exhibit_id: Property = Property(name="id", type=StringType)
aml_Exhibit.attributes={aml_Exhibit_id}

# aml_Collection class attributes and methods
aml_Collection_group: Property = Property(name="group", type=StringType)
aml_Collection_label: Property = Property(name="label", type=StringType)
aml_Collection_id: Property = Property(name="id", type=StringType)
aml_Collection_label1: Property = Property(name="label1", type=StringType)
aml_Collection_objectType: Property = Property(name="objectType", type=StringType)
aml_Collection.attributes={aml_Collection_objectType, aml_Collection_label1, aml_Collection_id, aml_Collection_label, aml_Collection_group}

# aml_Person class attributes and methods
aml_Person_firstName: Property = Property(name="firstName", type=StringType)
aml_Person_middleName: Property = Property(name="middleName", type=StringType)
aml_Person_lastName: Property = Property(name="lastName", type=StringType)
aml_Person_nickName: Property = Property(name="nickName", type=StringType)
aml_Person_organization: Property = Property(name="organization", type=StringType)
aml_Person_department: Property = Property(name="department", type=StringType)
aml_Person_email: Property = Property(name="email", type=StringType)
aml_Person_description: Property = Property(name="description", type=StringType)
aml_Person_id: Property = Property(name="id", type=StringType)
aml_Person.attributes={aml_Person_email, aml_Person_department, aml_Person_firstName, aml_Person_id, aml_Person_nickName, aml_Person_description, aml_Person_organization, aml_Person_middleName, aml_Person_lastName}

# aml_Memo class attributes and methods
aml_Memo_subject: Property = Property(name="subject", type=StringType)
aml_Memo_body: Property = Property(name="body", type=StringType)
aml_Memo_id: Property = Property(name="id", type=StringType)
aml_Memo_type: Property = Property(name="type", type=StringType)
aml_Memo.attributes={aml_Memo_subject, aml_Memo_id, aml_Memo_body, aml_Memo_type}

# aml_DiscoveryMethod class attributes and methods
aml_DiscoveryMethod_label: Property = Property(name="label", type=StringType)
aml_DiscoveryMethod_type: Property = Property(name="type", type=StringType)
aml_DiscoveryMethod_url: Property = Property(name="url", type=StringType)
aml_DiscoveryMethod_autoTrigger: Property = Property(name="autoTrigger", type=StringType)
aml_DiscoveryMethod_description: Property = Property(name="description", type=StringType)
aml_DiscoveryMethod_id: Property = Property(name="id", type=StringType)
aml_DiscoveryMethod_importType: Property = Property(name="importType", type=StringType)
aml_DiscoveryMethod.attributes={aml_DiscoveryMethod_url, aml_DiscoveryMethod_autoTrigger, aml_DiscoveryMethod_type, aml_DiscoveryMethod_description, aml_DiscoveryMethod_label, aml_DiscoveryMethod_importType, aml_DiscoveryMethod_id}

# aml_Annotation class attributes and methods
aml_Annotation_mixed: Property = Property(name="mixed", type=StringType)
aml_Annotation_group: Property = Property(name="group", type=StringType)
aml_Annotation_id: Property = Property(name="id", type=StringType)
aml_Annotation.attributes={aml_Annotation_mixed, aml_Annotation_id, aml_Annotation_group}

# aml_Flag class attributes and methods
aml_Flag_flagType: Property = Property(name="flagType", type=StringType)
aml_Flag_label: Property = Property(name="label", type=StringType)
aml_Flag_description: Property = Property(name="description", type=StringType)
aml_Flag.attributes={aml_Flag_flagType, aml_Flag_label, aml_Flag_description}

# aml_Answer class attributes and methods
aml_Answer_group: Property = Property(name="group", type=StringType)
aml_Answer_rationale: Property = Property(name="rationale", type=StringType)
aml_Answer_questionId: Property = Property(name="questionId", type=StringType)
aml_Answer.attributes={aml_Answer_questionId, aml_Answer_group, aml_Answer_rationale}

# aml_Belief class attributes and methods
aml_Belief_description: Property = Property(name="description", type=StringType)
aml_Belief_label: Property = Property(name="label", type=StringType)
aml_Belief_ordinal: Property = Property(name="ordinal", type=StringType)
aml_Belief_symbol: Property = Property(name="symbol", type=StringType)
aml_Belief.attributes={aml_Belief_ordinal, aml_Belief_symbol, aml_Belief_description, aml_Belief_label}

# aml_Witness class attributes and methods
aml_Witness_description: Property = Property(name="description", type=StringType)
aml_Witness_idRef: Property = Property(name="idRef", type=StringType)
aml_Witness_timestamp: Property = Property(name="timestamp", type=StringType)
aml_Witness.attributes={aml_Witness_timestamp, aml_Witness_idRef, aml_Witness_description}

# aml_Evidence class attributes and methods
aml_Evidence_id: Property = Property(name="id", type=StringType)
aml_Evidence_label: Property = Property(name="label", type=StringType)
aml_Evidence_ordinal: Property = Property(name="ordinal", type=StringType)
aml_Evidence.attributes={aml_Evidence_id, aml_Evidence_label, aml_Evidence_ordinal}

# aml_ArgumentTemplate class attributes and methods
aml_ArgumentTemplate_idRef: Property = Property(name="idRef", type=StringType)
aml_ArgumentTemplate_value: Property = Property(name="value", type=StringType)
aml_ArgumentTemplate.attributes={aml_ArgumentTemplate_value, aml_ArgumentTemplate_idRef}

# aml_MetaData class attributes and methods
aml_MetaData_group: Property = Property(name="group", type=StringType)
aml_MetaData_title: Property = Property(name="title", type=StringType)
aml_MetaData_securityMarking: Property = Property(name="securityMarking", type=StringType)
aml_MetaData_subject: Property = Property(name="subject", type=StringType)
aml_MetaData_description: Property = Property(name="description", type=StringType)
aml_MetaData_date: Property = Property(name="date", type=StringType)
aml_MetaData.attributes={aml_MetaData_group, aml_MetaData_securityMarking, aml_MetaData_subject, aml_MetaData_title, aml_MetaData_date, aml_MetaData_description}

# aml_CreatingTool class attributes and methods
aml_CreatingTool_version: Property = Property(name="version", type=StringType)
aml_CreatingTool_label: Property = Property(name="label", type=StringType)
aml_CreatingTool_toolType: Property = Property(name="toolType", type=StringType)
aml_CreatingTool.attributes={aml_CreatingTool_version, aml_CreatingTool_toolType, aml_CreatingTool_label}

# aml_Choice class attributes and methods
aml_Choice_label: Property = Property(name="label", type=StringType)
aml_Choice_description: Property = Property(name="description", type=StringType)
aml_Choice_ordinal: Property = Property(name="ordinal", type=StringType)
aml_Choice_symbol: Property = Property(name="symbol", type=StringType)
aml_Choice.attributes={aml_Choice_label, aml_Choice_symbol, aml_Choice_ordinal, aml_Choice_description}

# aml_CollectionItem class attributes and methods
aml_CollectionItem_idRef: Property = Property(name="idRef", type=StringType)
aml_CollectionItem_objectType: Property = Property(name="objectType", type=StringType)
aml_CollectionItem_ordinal: Property = Property(name="ordinal", type=StringType)
aml_CollectionItem.attributes={aml_CollectionItem_ordinal, aml_CollectionItem_objectType, aml_CollectionItem_idRef}

# aml_Question class attributes and methods
aml_Question_group: Property = Property(name="group", type=StringType)
aml_Question_label: Property = Property(name="label", type=StringType)
aml_Question_amplification: Property = Property(name="amplification", type=StringType)
aml_Question_description: Property = Property(name="description", type=StringType)
aml_Question_id: Property = Property(name="id", type=StringType)
aml_Question.attributes={aml_Question_amplification, aml_Question_label, aml_Question_description, aml_Question_id, aml_Question_group}

# aml_Coverage class attributes and methods
aml_Coverage_mixed: Property = Property(name="mixed", type=StringType)
aml_Coverage_group: Property = Property(name="group", type=StringType)
aml_Coverage.attributes={aml_Coverage_group, aml_Coverage_mixed}

# aml_NationState class attributes and methods
aml_NationState_perspective: Property = Property(name="perspective", type=StringType)
aml_NationState_group: Property = Property(name="group", type=StringType)
aml_NationState_actor: Property = Property(name="actor", type=StringType)
aml_NationState_region: Property = Property(name="region", type=StringType)
aml_NationState_event: Property = Property(name="event", type=StringType)
aml_NationState.attributes={aml_NationState_actor, aml_NationState_perspective, aml_NationState_group, aml_NationState_region, aml_NationState_event}

# aml_Creator class attributes and methods
aml_Creator_description: Property = Property(name="description", type=StringType)
aml_Creator_idRef: Property = Property(name="idRef", type=StringType)
aml_Creator_objectType: Property = Property(name="objectType", type=StringType)
aml_Creator.attributes={aml_Creator_description, aml_Creator_objectType, aml_Creator_idRef}

# aml_DocumentRoot class attributes and methods
aml_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
aml_DocumentRoot_actor: Property = Property(name="actor", type=StringType)
aml_DocumentRoot_department: Property = Property(name="department", type=StringType)
aml_DocumentRoot_body: Property = Property(name="body", type=StringType)
aml_DocumentRoot_date: Property = Property(name="date", type=StringType)
aml_DocumentRoot_description: Property = Property(name="description", type=StringType)
aml_DocumentRoot_email: Property = Property(name="email", type=StringType)
aml_DocumentRoot_event: Property = Property(name="event", type=StringType)
aml_DocumentRoot_firstName: Property = Property(name="firstName", type=StringType)
aml_DocumentRoot_label: Property = Property(name="label", type=StringType)
aml_DocumentRoot_lastName: Property = Property(name="lastName", type=StringType)
aml_DocumentRoot_middleName: Property = Property(name="middleName", type=StringType)
aml_DocumentRoot_nickName: Property = Property(name="nickName", type=StringType)
aml_DocumentRoot_organization: Property = Property(name="organization", type=StringType)
aml_DocumentRoot_perspective: Property = Property(name="perspective", type=StringType)
aml_DocumentRoot_securityMarking: Property = Property(name="securityMarking", type=StringType)
aml_DocumentRoot_rationale: Property = Property(name="rationale", type=StringType)
aml_DocumentRoot_region: Property = Property(name="region", type=StringType)
aml_DocumentRoot_subject: Property = Property(name="subject", type=StringType)
aml_DocumentRoot_symbol: Property = Property(name="symbol", type=StringType)
aml_DocumentRoot_title: Property = Property(name="title", type=StringType)
aml_DocumentRoot_label1: Property = Property(name="label1", type=StringType)
aml_DocumentRoot_url: Property = Property(name="url", type=StringType)
aml_DocumentRoot_description1: Property = Property(name="description1", type=StringType)
aml_DocumentRoot_id: Property = Property(name="id", type=StringType)
aml_DocumentRoot_idRef: Property = Property(name="idRef", type=StringType)
aml_DocumentRoot.attributes={aml_DocumentRoot_middleName, aml_DocumentRoot_title, aml_DocumentRoot_description1, aml_DocumentRoot_symbol, aml_DocumentRoot_mixed, aml_DocumentRoot_region, aml_DocumentRoot_event, aml_DocumentRoot_date, aml_DocumentRoot_lastName, aml_DocumentRoot_subject, aml_DocumentRoot_label1, aml_DocumentRoot_rationale, aml_DocumentRoot_body, aml_DocumentRoot_nickName, aml_DocumentRoot_label, aml_DocumentRoot_url, aml_DocumentRoot_description, aml_DocumentRoot_idRef, aml_DocumentRoot_id, aml_DocumentRoot_email, aml_DocumentRoot_perspective, aml_DocumentRoot_department, aml_DocumentRoot_securityMarking, aml_DocumentRoot_firstName, aml_DocumentRoot_organization, aml_DocumentRoot_actor}

# aml_Dependent class attributes and methods
aml_Dependent_idRef: Property = Property(name="idRef", type=StringType)
aml_Dependent_ordinal: Property = Property(name="ordinal", type=StringType)
aml_Dependent.attributes={aml_Dependent_ordinal, aml_Dependent_idRef}

# aml_EStringToStringMapEntry class attributes and methods

# aml_End class attributes and methods
aml_End_value: Property = Property(name="value", type=StringType)
aml_End_scheme: Property = Property(name="scheme", type=StringType)
aml_End.attributes={aml_End_scheme, aml_End_value}

# aml_EvidenceExhibit class attributes and methods
aml_EvidenceExhibit_value: Property = Property(name="value", type=StringType)
aml_EvidenceExhibit_idRef: Property = Property(name="idRef", type=StringType)
aml_EvidenceExhibit_questionId: Property = Property(name="questionId", type=StringType)
aml_EvidenceExhibit.attributes={aml_EvidenceExhibit_idRef, aml_EvidenceExhibit_value, aml_EvidenceExhibit_questionId}

# aml_Interval class attributes and methods
aml_Interval_max: Property = Property(name="max", type=StringType)
aml_Interval_min: Property = Property(name="min", type=StringType)
aml_Interval.attributes={aml_Interval_max, aml_Interval_min}

# aml_List class attributes and methods
aml_List_group: Property = Property(name="group", type=StringType)
aml_List.attributes={aml_List_group}

# aml_QuestionRelationships class attributes and methods

# aml_Period class attributes and methods
aml_Period_label: Property = Property(name="label", type=StringType)
aml_Period_group: Property = Property(name="group", type=StringType)
aml_Period.attributes={aml_Period_group, aml_Period_label}

# aml_Publisher class attributes and methods
aml_Publisher_description: Property = Property(name="description", type=StringType)
aml_Publisher_idRef: Property = Property(name="idRef", type=StringType)
aml_Publisher_objectType: Property = Property(name="objectType", type=StringType)
aml_Publisher.attributes={aml_Publisher_description, aml_Publisher_objectType, aml_Publisher_idRef}

# aml_Reader class attributes and methods
aml_Reader_description: Property = Property(name="description", type=StringType)
aml_Reader_idRef: Property = Property(name="idRef", type=StringType)
aml_Reader_objectType: Property = Property(name="objectType", type=StringType)
aml_Reader.attributes={aml_Reader_objectType, aml_Reader_description, aml_Reader_idRef}

# aml_Relevance class attributes and methods
aml_Relevance_description: Property = Property(name="description", type=StringType)
aml_Relevance_label: Property = Property(name="label", type=StringType)
aml_Relevance_ordinal: Property = Property(name="ordinal", type=StringType)
aml_Relevance_symbol: Property = Property(name="symbol", type=StringType)
aml_Relevance.attributes={aml_Relevance_symbol, aml_Relevance_ordinal, aml_Relevance_description, aml_Relevance_label}

# aml_Reliability class attributes and methods
aml_Reliability_description: Property = Property(name="description", type=StringType)
aml_Reliability_label: Property = Property(name="label", type=StringType)
aml_Reliability_ordinal: Property = Property(name="ordinal", type=StringType)
aml_Reliability_symbol: Property = Property(name="symbol", type=StringType)
aml_Reliability.attributes={aml_Reliability_ordinal, aml_Reliability_symbol, aml_Reliability_label, aml_Reliability_description}

# aml_Start class attributes and methods
aml_Start_value: Property = Property(name="value", type=StringType)
aml_Start_scheme: Property = Property(name="scheme", type=StringType)
aml_Start.attributes={aml_Start_value, aml_Start_scheme}

# aml_Value class attributes and methods
aml_Value_type: Property = Property(name="type", type=StringType)
aml_Value_unit: Property = Property(name="unit", type=StringType)
aml_Value_mixed: Property = Property(name="mixed", type=StringType)
aml_Value_group: Property = Property(name="group", type=StringType)
aml_Value.attributes={aml_Value_unit, aml_Value_type, aml_Value_group, aml_Value_mixed}

# Relationships
method0: BinaryAssociation = BinaryAssociation(
    name="method0",
    ends={
        Property(name="aml_EObject", type=aml_AggregationRule, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_AggregationRule", type=aml_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter1: BinaryAssociation = BinaryAssociation(
    name="parameter1",
    ends={
        Property(name="aml_Parameter", type=aml_AggregationRule, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_AggregationRule2", type=aml_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
template3: BinaryAssociation = BinaryAssociation(
    name="template3",
    ends={
        Property(name="aml_Template", type=aml_AmlDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_AmlDocument", type=aml_Template, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument4: BinaryAssociation = BinaryAssociation(
    name="argument4",
    ends={
        Property(name="aml_Argument", type=aml_AmlDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_AmlDocument5", type=aml_Argument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exhibit6: BinaryAssociation = BinaryAssociation(
    name="exhibit6",
    ends={
        Property(name="aml_Exhibit", type=aml_AmlDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_AmlDocument7", type=aml_Exhibit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collection8: BinaryAssociation = BinaryAssociation(
    name="collection8",
    ends={
        Property(name="aml_Collection", type=aml_AmlDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_AmlDocument9", type=aml_Collection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
person10: BinaryAssociation = BinaryAssociation(
    name="person10",
    ends={
        Property(name="aml_Person", type=aml_AmlDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_AmlDocument11", type=aml_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
memo12: BinaryAssociation = BinaryAssociation(
    name="memo12",
    ends={
        Property(name="aml_Memo", type=aml_AmlDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_AmlDocument13", type=aml_Memo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
discoveryMethod14: BinaryAssociation = BinaryAssociation(
    name="discoveryMethod14",
    ends={
        Property(name="aml_DiscoveryMethod", type=aml_AmlDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_AmlDocument15", type=aml_DiscoveryMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
memo16: BinaryAssociation = BinaryAssociation(
    name="memo16",
    ends={
        Property(name="aml_Memo17", type=aml_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Annotation", type=aml_Memo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
flag18: BinaryAssociation = BinaryAssociation(
    name="flag18",
    ends={
        Property(name="aml_Flag", type=aml_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Annotation19", type=aml_Flag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
belief20: BinaryAssociation = BinaryAssociation(
    name="belief20",
    ends={
        Property(name="aml_Belief", type=aml_Answer, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Answer", type=aml_Belief, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
witness21: BinaryAssociation = BinaryAssociation(
    name="witness21",
    ends={
        Property(name="aml_Witness", type=aml_Answer, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Answer22", type=aml_Witness, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotation23: BinaryAssociation = BinaryAssociation(
    name="annotation23",
    ends={
        Property(name="aml_Annotation25", type=aml_Answer, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Answer24", type=aml_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
aggregationRule26: BinaryAssociation = BinaryAssociation(
    name="aggregationRule26",
    ends={
        Property(name="aml_AggregationRule28", type=aml_Answer, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Answer27", type=aml_AggregationRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
evidence29: BinaryAssociation = BinaryAssociation(
    name="evidence29",
    ends={
        Property(name="aml_Evidence", type=aml_Answer, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Answer30", type=aml_Evidence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
discoveryMethod31: BinaryAssociation = BinaryAssociation(
    name="discoveryMethod31",
    ends={
        Property(name="aml_DiscoveryMethod33", type=aml_Answer, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Answer32", type=aml_DiscoveryMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metaData34: BinaryAssociation = BinaryAssociation(
    name="metaData34",
    ends={
        Property(name="aml_MetaData", type=aml_Argument, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Argument35", type=aml_MetaData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
creatingTool36: BinaryAssociation = BinaryAssociation(
    name="creatingTool36",
    ends={
        Property(name="aml_CreatingTool", type=aml_Argument, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Argument37", type=aml_CreatingTool, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotation38: BinaryAssociation = BinaryAssociation(
    name="annotation38",
    ends={
        Property(name="aml_Annotation40", type=aml_Argument, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Argument39", type=aml_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argumentTemplate41: BinaryAssociation = BinaryAssociation(
    name="argumentTemplate41",
    ends={
        Property(name="aml_ArgumentTemplate", type=aml_Argument, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Argument42", type=aml_ArgumentTemplate, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
answer43: BinaryAssociation = BinaryAssociation(
    name="answer43",
    ends={
        Property(name="aml_Answer45", type=aml_Argument, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Argument44", type=aml_Answer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argumentTemplate57: BinaryAssociation = BinaryAssociation(
    name="argumentTemplate57",
    ends={
        Property(name="aml_ArgumentTemplate59", type=aml_Collection, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Collection58", type=aml_ArgumentTemplate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
metaData46: BinaryAssociation = BinaryAssociation(
    name="metaData46",
    ends={
        Property(name="aml_MetaData48", type=aml_Collection, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Collection47", type=aml_MetaData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
creatingTool49: BinaryAssociation = BinaryAssociation(
    name="creatingTool49",
    ends={
        Property(name="aml_CreatingTool51", type=aml_Collection, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Collection50", type=aml_CreatingTool, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotation52: BinaryAssociation = BinaryAssociation(
    name="annotation52",
    ends={
        Property(name="aml_Annotation54", type=aml_Collection, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Collection53", type=aml_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
question55: BinaryAssociation = BinaryAssociation(
    name="question55",
    ends={
        Property(name="aml_Question", type=aml_Collection, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Collection56", type=aml_Question, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
collectionItem60: BinaryAssociation = BinaryAssociation(
    name="collectionItem60",
    ends={
        Property(name="aml_CollectionItem", type=aml_Collection, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Collection61", type=aml_CollectionItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nationState62: BinaryAssociation = BinaryAssociation(
    name="nationState62",
    ends={
        Property(name="aml_NationState", type=aml_Coverage, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Coverage", type=aml_NationState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argumentTemplate63: BinaryAssociation = BinaryAssociation(
    name="argumentTemplate63",
    ends={
        Property(name="aml_ArgumentTemplate65", type=aml_DiscoveryMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DiscoveryMethod64", type=aml_ArgumentTemplate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotation66: BinaryAssociation = BinaryAssociation(
    name="annotation66",
    ends={
        Property(name="aml_Annotation68", type=aml_DiscoveryMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DiscoveryMethod67", type=aml_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argumentTemplate91: BinaryAssociation = BinaryAssociation(
    name="argumentTemplate91",
    ends={
        Property(name="aml_ArgumentTemplate93", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot92", type=aml_ArgumentTemplate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
belief94: BinaryAssociation = BinaryAssociation(
    name="belief94",
    ends={
        Property(name="aml_Belief96", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot95", type=aml_Belief, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xMLNSPrefixMap69: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap69",
    ends={
        Property(name="aml_EStringToStringMapEntry", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot", type=aml_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation70: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation70",
    ends={
        Property(name="aml_EStringToStringMapEntry72", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot71", type=aml_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
aggregationRule73: BinaryAssociation = BinaryAssociation(
    name="aggregationRule73",
    ends={
        Property(name="aml_AggregationRule75", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot74", type=aml_AggregationRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
amlDocument76: BinaryAssociation = BinaryAssociation(
    name="amlDocument76",
    ends={
        Property(name="aml_AmlDocument78", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot77", type=aml_AmlDocument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotation79: BinaryAssociation = BinaryAssociation(
    name="annotation79",
    ends={
        Property(name="aml_Annotation81", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot80", type=aml_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
answer82: BinaryAssociation = BinaryAssociation(
    name="answer82",
    ends={
        Property(name="aml_Answer84", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot83", type=aml_Answer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
archive85: BinaryAssociation = BinaryAssociation(
    name="archive85",
    ends={
        Property(name="aml_EObject87", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot86", type=aml_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument88: BinaryAssociation = BinaryAssociation(
    name="argument88",
    ends={
        Property(name="aml_Argument90", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot89", type=aml_Argument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependent116: BinaryAssociation = BinaryAssociation(
    name="dependent116",
    ends={
        Property(name="aml_Dependent", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot117", type=aml_Dependent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
choice97: BinaryAssociation = BinaryAssociation(
    name="choice97",
    ends={
        Property(name="aml_Choice", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot98", type=aml_Choice, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collection99: BinaryAssociation = BinaryAssociation(
    name="collection99",
    ends={
        Property(name="aml_Collection101", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot100", type=aml_Collection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collectionItem102: BinaryAssociation = BinaryAssociation(
    name="collectionItem102",
    ends={
        Property(name="aml_CollectionItem104", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot103", type=aml_CollectionItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contributor105: BinaryAssociation = BinaryAssociation(
    name="contributor105",
    ends={
        Property(name="aml_EObject107", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot106", type=aml_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
coverage108: BinaryAssociation = BinaryAssociation(
    name="coverage108",
    ends={
        Property(name="aml_Coverage110", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot109", type=aml_Coverage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
creatingTool111: BinaryAssociation = BinaryAssociation(
    name="creatingTool111",
    ends={
        Property(name="aml_CreatingTool113", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot112", type=aml_CreatingTool, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
creator114: BinaryAssociation = BinaryAssociation(
    name="creator114",
    ends={
        Property(name="aml_Creator", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot115", type=aml_Creator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
flag131: BinaryAssociation = BinaryAssociation(
    name="flag131",
    ends={
        Property(name="aml_Flag133", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot132", type=aml_Flag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
format134: BinaryAssociation = BinaryAssociation(
    name="format134",
    ends={
        Property(name="aml_EObject136", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot135", type=aml_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
discoveryMethod118: BinaryAssociation = BinaryAssociation(
    name="discoveryMethod118",
    ends={
        Property(name="aml_DiscoveryMethod120", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot119", type=aml_DiscoveryMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
end121: BinaryAssociation = BinaryAssociation(
    name="end121",
    ends={
        Property(name="aml_End", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot122", type=aml_End, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
evidence123: BinaryAssociation = BinaryAssociation(
    name="evidence123",
    ends={
        Property(name="aml_Evidence125", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot124", type=aml_Evidence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
evidenceExhibit126: BinaryAssociation = BinaryAssociation(
    name="evidenceExhibit126",
    ends={
        Property(name="aml_EvidenceExhibit", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot127", type=aml_EvidenceExhibit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exhibit128: BinaryAssociation = BinaryAssociation(
    name="exhibit128",
    ends={
        Property(name="aml_Exhibit130", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot129", type=aml_Exhibit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metaData153: BinaryAssociation = BinaryAssociation(
    name="metaData153",
    ends={
        Property(name="aml_MetaData155", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot154", type=aml_MetaData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method156: BinaryAssociation = BinaryAssociation(
    name="method156",
    ends={
        Property(name="aml_EObject158", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot157", type=aml_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identifier137: BinaryAssociation = BinaryAssociation(
    name="identifier137",
    ends={
        Property(name="aml_EObject139", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot138", type=aml_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
image140: BinaryAssociation = BinaryAssociation(
    name="image140",
    ends={
        Property(name="aml_EObject142", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot141", type=aml_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interval143: BinaryAssociation = BinaryAssociation(
    name="interval143",
    ends={
        Property(name="aml_Interval", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot144", type=aml_Interval, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
language145: BinaryAssociation = BinaryAssociation(
    name="language145",
    ends={
        Property(name="aml_EObject147", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot146", type=aml_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
list148: BinaryAssociation = BinaryAssociation(
    name="list148",
    ends={
        Property(name="aml_List", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot149", type=aml_List, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
memo150: BinaryAssociation = BinaryAssociation(
    name="memo150",
    ends={
        Property(name="aml_Memo152", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot151", type=aml_Memo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
question172: BinaryAssociation = BinaryAssociation(
    name="question172",
    ends={
        Property(name="aml_Question174", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot173", type=aml_Question, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
questionRelationships175: BinaryAssociation = BinaryAssociation(
    name="questionRelationships175",
    ends={
        Property(name="aml_QuestionRelationships", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot176", type=aml_QuestionRelationships, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nationState159: BinaryAssociation = BinaryAssociation(
    name="nationState159",
    ends={
        Property(name="aml_NationState161", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot160", type=aml_NationState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter162: BinaryAssociation = BinaryAssociation(
    name="parameter162",
    ends={
        Property(name="aml_Parameter164", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot163", type=aml_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
period165: BinaryAssociation = BinaryAssociation(
    name="period165",
    ends={
        Property(name="aml_Period", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot166", type=aml_Period, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
person167: BinaryAssociation = BinaryAssociation(
    name="person167",
    ends={
        Property(name="aml_Person169", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot168", type=aml_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
publisher170: BinaryAssociation = BinaryAssociation(
    name="publisher170",
    ends={
        Property(name="aml_Publisher", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot171", type=aml_Publisher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source189: BinaryAssociation = BinaryAssociation(
    name="source189",
    ends={
        Property(name="aml_EObject191", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot190", type=aml_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reader177: BinaryAssociation = BinaryAssociation(
    name="reader177",
    ends={
        Property(name="aml_Reader", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot178", type=aml_Reader, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relation179: BinaryAssociation = BinaryAssociation(
    name="relation179",
    ends={
        Property(name="aml_EObject181", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot180", type=aml_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relevance182: BinaryAssociation = BinaryAssociation(
    name="relevance182",
    ends={
        Property(name="aml_Relevance", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot183", type=aml_Relevance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reliability184: BinaryAssociation = BinaryAssociation(
    name="reliability184",
    ends={
        Property(name="aml_Reliability", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot185", type=aml_Reliability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rights186: BinaryAssociation = BinaryAssociation(
    name="rights186",
    ends={
        Property(name="aml_EObject188", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot187", type=aml_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type197: BinaryAssociation = BinaryAssociation(
    name="type197",
    ends={
        Property(name="aml_EObject199", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot198", type=aml_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
start192: BinaryAssociation = BinaryAssociation(
    name="start192",
    ends={
        Property(name="aml_Start", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot193", type=aml_Start, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
template194: BinaryAssociation = BinaryAssociation(
    name="template194",
    ends={
        Property(name="aml_Template196", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot195", type=aml_Template, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value200: BinaryAssociation = BinaryAssociation(
    name="value200",
    ends={
        Property(name="aml_Value", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot201", type=aml_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
witness202: BinaryAssociation = BinaryAssociation(
    name="witness202",
    ends={
        Property(name="aml_Witness204", type=aml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_DocumentRoot203", type=aml_Witness, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotation217: BinaryAssociation = BinaryAssociation(
    name="annotation217",
    ends={
        Property(name="aml_Annotation219", type=aml_Evidence, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Evidence218", type=aml_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
evidenceExhibit205: BinaryAssociation = BinaryAssociation(
    name="evidenceExhibit205",
    ends={
        Property(name="aml_EvidenceExhibit207", type=aml_Evidence, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Evidence206", type=aml_EvidenceExhibit, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
relevance208: BinaryAssociation = BinaryAssociation(
    name="relevance208",
    ends={
        Property(name="aml_Relevance210", type=aml_Evidence, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Evidence209", type=aml_Relevance, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reliability211: BinaryAssociation = BinaryAssociation(
    name="reliability211",
    ends={
        Property(name="aml_Reliability213", type=aml_Evidence, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Evidence212", type=aml_Reliability, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
witness214: BinaryAssociation = BinaryAssociation(
    name="witness214",
    ends={
        Property(name="aml_Witness216", type=aml_Evidence, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Evidence215", type=aml_Witness, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
archive220: BinaryAssociation = BinaryAssociation(
    name="archive220",
    ends={
        Property(name="aml_EObject222", type=aml_Exhibit, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Exhibit221", type=aml_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
metaData223: BinaryAssociation = BinaryAssociation(
    name="metaData223",
    ends={
        Property(name="aml_MetaData225", type=aml_Exhibit, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Exhibit224", type=aml_MetaData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotation226: BinaryAssociation = BinaryAssociation(
    name="annotation226",
    ends={
        Property(name="aml_Annotation228", type=aml_Exhibit, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Exhibit227", type=aml_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
witness229: BinaryAssociation = BinaryAssociation(
    name="witness229",
    ends={
        Property(name="aml_Witness231", type=aml_Flag, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Flag230", type=aml_Witness, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
li232: BinaryAssociation = BinaryAssociation(
    name="li232",
    ends={
        Property(name="aml_EObject234", type=aml_List, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_List233", type=aml_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
creator235: BinaryAssociation = BinaryAssociation(
    name="creator235",
    ends={
        Property(name="aml_Creator237", type=aml_Memo, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Memo236", type=aml_Creator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
reader238: BinaryAssociation = BinaryAssociation(
    name="reader238",
    ends={
        Property(name="aml_Reader240", type=aml_Memo, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Memo239", type=aml_Reader, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
format256: BinaryAssociation = BinaryAssociation(
    name="format256",
    ends={
        Property(name="aml_EObject258", type=aml_MetaData, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_MetaData257", type=aml_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identifier259: BinaryAssociation = BinaryAssociation(
    name="identifier259",
    ends={
        Property(name="aml_EObject261", type=aml_MetaData, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_MetaData260", type=aml_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
creator241: BinaryAssociation = BinaryAssociation(
    name="creator241",
    ends={
        Property(name="aml_Creator243", type=aml_MetaData, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_MetaData242", type=aml_Creator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reader244: BinaryAssociation = BinaryAssociation(
    name="reader244",
    ends={
        Property(name="aml_Reader246", type=aml_MetaData, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_MetaData245", type=aml_Reader, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
publisher247: BinaryAssociation = BinaryAssociation(
    name="publisher247",
    ends={
        Property(name="aml_Publisher249", type=aml_MetaData, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_MetaData248", type=aml_Publisher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contributor250: BinaryAssociation = BinaryAssociation(
    name="contributor250",
    ends={
        Property(name="aml_EObject252", type=aml_MetaData, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_MetaData251", type=aml_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type253: BinaryAssociation = BinaryAssociation(
    name="type253",
    ends={
        Property(name="aml_EObject255", type=aml_MetaData, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_MetaData254", type=aml_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
period280: BinaryAssociation = BinaryAssociation(
    name="period280",
    ends={
        Property(name="aml_Period282", type=aml_NationState, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_NationState281", type=aml_Period, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source262: BinaryAssociation = BinaryAssociation(
    name="source262",
    ends={
        Property(name="aml_EObject264", type=aml_MetaData, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_MetaData263", type=aml_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
language265: BinaryAssociation = BinaryAssociation(
    name="language265",
    ends={
        Property(name="aml_EObject267", type=aml_MetaData, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_MetaData266", type=aml_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relation268: BinaryAssociation = BinaryAssociation(
    name="relation268",
    ends={
        Property(name="aml_EObject270", type=aml_MetaData, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_MetaData269", type=aml_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
coverage271: BinaryAssociation = BinaryAssociation(
    name="coverage271",
    ends={
        Property(name="aml_Coverage273", type=aml_MetaData, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_MetaData272", type=aml_Coverage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rights274: BinaryAssociation = BinaryAssociation(
    name="rights274",
    ends={
        Property(name="aml_EObject276", type=aml_MetaData, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_MetaData275", type=aml_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
image277: BinaryAssociation = BinaryAssociation(
    name="image277",
    ends={
        Property(name="aml_EObject279", type=aml_MetaData, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_MetaData278", type=aml_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value283: BinaryAssociation = BinaryAssociation(
    name="value283",
    ends={
        Property(name="aml_Value285", type=aml_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Parameter284", type=aml_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
start286: BinaryAssociation = BinaryAssociation(
    name="start286",
    ends={
        Property(name="aml_Start288", type=aml_Period, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Period287", type=aml_Start, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
end289: BinaryAssociation = BinaryAssociation(
    name="end289",
    ends={
        Property(name="aml_End291", type=aml_Period, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Period290", type=aml_End, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type295: BinaryAssociation = BinaryAssociation(
    name="type295",
    ends={
        Property(name="aml_EObject297", type=aml_Question, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Question296", type=aml_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependent292: BinaryAssociation = BinaryAssociation(
    name="dependent292",
    ends={
        Property(name="aml_Dependent294", type=aml_QuestionRelationships, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_QuestionRelationships293", type=aml_Dependent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
choice298: BinaryAssociation = BinaryAssociation(
    name="choice298",
    ends={
        Property(name="aml_Choice300", type=aml_Question, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Question299", type=aml_Choice, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
questionRelationships301: BinaryAssociation = BinaryAssociation(
    name="questionRelationships301",
    ends={
        Property(name="aml_QuestionRelationships303", type=aml_Question, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Question302", type=aml_QuestionRelationships, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
aggregationRule304: BinaryAssociation = BinaryAssociation(
    name="aggregationRule304",
    ends={
        Property(name="aml_AggregationRule306", type=aml_Question, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Question305", type=aml_AggregationRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
discoveryMethod307: BinaryAssociation = BinaryAssociation(
    name="discoveryMethod307",
    ends={
        Property(name="aml_DiscoveryMethod309", type=aml_Question, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Question308", type=aml_DiscoveryMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotation310: BinaryAssociation = BinaryAssociation(
    name="annotation310",
    ends={
        Property(name="aml_Annotation312", type=aml_Question, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Question311", type=aml_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metaData313: BinaryAssociation = BinaryAssociation(
    name="metaData313",
    ends={
        Property(name="aml_MetaData315", type=aml_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Template314", type=aml_MetaData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
creatingTool316: BinaryAssociation = BinaryAssociation(
    name="creatingTool316",
    ends={
        Property(name="aml_CreatingTool318", type=aml_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Template317", type=aml_CreatingTool, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotation319: BinaryAssociation = BinaryAssociation(
    name="annotation319",
    ends={
        Property(name="aml_Annotation321", type=aml_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Template320", type=aml_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
question322: BinaryAssociation = BinaryAssociation(
    name="question322",
    ends={
        Property(name="aml_Question324", type=aml_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Template323", type=aml_Question, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interval325: BinaryAssociation = BinaryAssociation(
    name="interval325",
    ends={
        Property(name="aml_Interval327", type=aml_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Value326", type=aml_Interval, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
list328: BinaryAssociation = BinaryAssociation(
    name="list328",
    ends={
        Property(name="aml_List330", type=aml_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="aml_Value329", type=aml_List, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="aml",
    types={aml_AggregationRule, aml_EObject, aml_Parameter, aml_AmlDocument, aml_Template, aml_Argument, aml_Exhibit, aml_Collection, aml_Person, aml_Memo, aml_DiscoveryMethod, aml_Annotation, aml_Flag, aml_Answer, aml_Belief, aml_Witness, aml_Evidence, aml_ArgumentTemplate, aml_MetaData, aml_CreatingTool, aml_Choice, aml_CollectionItem, aml_Question, aml_Coverage, aml_NationState, aml_Creator, aml_DocumentRoot, aml_Dependent, aml_EStringToStringMapEntry, aml_End, aml_EvidenceExhibit, aml_Interval, aml_List, aml_QuestionRelationships, aml_Period, aml_Publisher, aml_Reader, aml_Relevance, aml_Reliability, aml_Start, aml_Value, ObjectType2, ObjectType3, ObjectType, ObjectType1, Type},
    associations={method0, parameter1, template3, argument4, exhibit6, collection8, person10, memo12, discoveryMethod14, memo16, flag18, belief20, witness21, annotation23, aggregationRule26, evidence29, discoveryMethod31, metaData34, creatingTool36, annotation38, argumentTemplate41, answer43, argumentTemplate57, metaData46, creatingTool49, annotation52, question55, collectionItem60, nationState62, argumentTemplate63, annotation66, argumentTemplate91, belief94, xMLNSPrefixMap69, xSISchemaLocation70, aggregationRule73, amlDocument76, annotation79, answer82, archive85, argument88, dependent116, choice97, collection99, collectionItem102, contributor105, coverage108, creatingTool111, creator114, flag131, format134, discoveryMethod118, end121, evidence123, evidenceExhibit126, exhibit128, metaData153, method156, identifier137, image140, interval143, language145, list148, memo150, question172, questionRelationships175, nationState159, parameter162, period165, person167, publisher170, source189, reader177, relation179, relevance182, reliability184, rights186, type197, start192, template194, value200, witness202, annotation217, evidenceExhibit205, relevance208, reliability211, witness214, archive220, metaData223, annotation226, witness229, li232, creator235, reader238, format256, identifier259, creator241, reader244, publisher247, contributor250, type253, period280, source262, language265, relation268, coverage271, rights274, image277, value283, start286, end289, type295, dependent292, choice298, questionRelationships301, aggregationRule304, discoveryMethod307, annotation310, metaData313, creatingTool316, annotation319, question322, interval325, list328},
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