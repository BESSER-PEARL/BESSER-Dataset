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
dsl_Process = Class(name="dsl::Process")
dsl_Try = Class(name="dsl::Try")
dsl_Catch = Class(name="dsl::Catch")
dsl_Finally = Class(name="dsl::Finally")
dsl_Action = Class(name="dsl::Action")
dsl_Expression = Class(name="dsl::Expression")
dsl_ExecJava = Class(name="dsl::ExecJava")
Action = Class(name="Action")
dsl_FirebaseDatabasePut = Class(name="dsl::FirebaseDatabasePut")
dsl_FirebaseReactiveNotification = Class(name="dsl::FirebaseReactiveNotification")
dsl_SmsLeadSms = Class(name="dsl::SmsLeadSms")
dsl_Abort = Class(name="dsl::Abort")
dsl_GooglecontactPUT = Class(name="dsl::GooglecontactPUT")
dsl_GooglecalPUT = Class(name="dsl::GooglecalPUT")
dsl_FBCLead = Class(name="dsl::FBCLead")
dsl_FBFormDownload = Class(name="dsl::FBFormDownload")
dsl_Dropfile = Class(name="dsl::Dropfile")
dsl_GooglecontactSelectAll = Class(name="dsl::GooglecontactSelectAll")
dsl_SendMail = Class(name="dsl::SendMail")
dsl_RestPart = Class(name="dsl::RestPart")
dsl_TrelloGET = Class(name="dsl::TrelloGET")
dsl_TrelloPUT = Class(name="dsl::TrelloPUT")
dsl_Fetch = Class(name="dsl::Fetch")
dsl_Callprocess = Class(name="dsl::Callprocess")
dsl_Doozle = Class(name="dsl::Doozle")
dsl_Rest = Class(name="dsl::Rest")
dsl_SlackPUT = Class(name="dsl::SlackPUT")
dsl_Copydata = Class(name="dsl::Copydata")
dsl_WriteCsv = Class(name="dsl::WriteCsv")
dsl_LoadCsv = Class(name="dsl::LoadCsv")
dsl_Transform = Class(name="dsl::Transform")
dsl_Updatedaudit = Class(name="dsl::Updatedaudit")
dsl_ClickSendSms = Class(name="dsl::ClickSendSms")

# dsl_Process class attributes and methods
dsl_Process_name: Property = Property(name="name", type=StringType)
dsl_Process.attributes={dsl_Process_name}

# dsl_Try class attributes and methods
dsl_Try_name: Property = Property(name="name", type=StringType)
dsl_Try.attributes={dsl_Try_name}

# dsl_Catch class attributes and methods
dsl_Catch_name: Property = Property(name="name", type=StringType)
dsl_Catch.attributes={dsl_Catch_name}

# dsl_Finally class attributes and methods
dsl_Finally_name: Property = Property(name="name", type=StringType)
dsl_Finally.attributes={dsl_Finally_name}

# dsl_Action class attributes and methods
dsl_Action_name: Property = Property(name="name", type=StringType)
dsl_Action.attributes={dsl_Action_name}

# dsl_Expression class attributes and methods
dsl_Expression_lhs: Property = Property(name="lhs", type=StringType)
dsl_Expression_operator: Property = Property(name="operator", type=StringType)
dsl_Expression_rhs: Property = Property(name="rhs", type=StringType)
dsl_Expression.attributes={dsl_Expression_operator, dsl_Expression_rhs, dsl_Expression_lhs}

# dsl_ExecJava class attributes and methods
dsl_ExecJava_classFqn: Property = Property(name="classFqn", type=StringType)
dsl_ExecJava_dbSrc: Property = Property(name="dbSrc", type=StringType)
dsl_ExecJava_value: Property = Property(name="value", type=StringType)
dsl_ExecJava.attributes={dsl_ExecJava_dbSrc, dsl_ExecJava_value, dsl_ExecJava_classFqn}

# Action class attributes and methods

# dsl_FirebaseDatabasePut class attributes and methods
dsl_FirebaseDatabasePut_url: Property = Property(name="url", type=StringType)
dsl_FirebaseDatabasePut_fbjson: Property = Property(name="fbjson", type=StringType)
dsl_FirebaseDatabasePut_groupPath: Property = Property(name="groupPath", type=StringType)
dsl_FirebaseDatabasePut_dbSrc: Property = Property(name="dbSrc", type=StringType)
dsl_FirebaseDatabasePut_classFqn: Property = Property(name="classFqn", type=StringType)
dsl_FirebaseDatabasePut_value: Property = Property(name="value", type=StringType)
dsl_FirebaseDatabasePut.attributes={dsl_FirebaseDatabasePut_dbSrc, dsl_FirebaseDatabasePut_groupPath, dsl_FirebaseDatabasePut_classFqn, dsl_FirebaseDatabasePut_url, dsl_FirebaseDatabasePut_fbjson, dsl_FirebaseDatabasePut_value}

# dsl_FirebaseReactiveNotification class attributes and methods
dsl_FirebaseReactiveNotification_url: Property = Property(name="url", type=StringType)
dsl_FirebaseReactiveNotification_fbjson: Property = Property(name="fbjson", type=StringType)
dsl_FirebaseReactiveNotification_groupPath: Property = Property(name="groupPath", type=StringType)
dsl_FirebaseReactiveNotification_classFqn: Property = Property(name="classFqn", type=StringType)
dsl_FirebaseReactiveNotification_dbSrc: Property = Property(name="dbSrc", type=StringType)
dsl_FirebaseReactiveNotification.attributes={dsl_FirebaseReactiveNotification_url, dsl_FirebaseReactiveNotification_fbjson, dsl_FirebaseReactiveNotification_classFqn, dsl_FirebaseReactiveNotification_groupPath, dsl_FirebaseReactiveNotification_dbSrc}

# dsl_SmsLeadSms class attributes and methods
dsl_SmsLeadSms_url: Property = Property(name="url", type=StringType)
dsl_SmsLeadSms_sender: Property = Property(name="sender", type=StringType)
dsl_SmsLeadSms_account: Property = Property(name="account", type=StringType)
dsl_SmsLeadSms_privateKey: Property = Property(name="privateKey", type=StringType)
dsl_SmsLeadSms_dbSrc: Property = Property(name="dbSrc", type=StringType)
dsl_SmsLeadSms_value: Property = Property(name="value", type=StringType)
dsl_SmsLeadSms_dryrunNumber: Property = Property(name="dryrunNumber", type=StringType)
dsl_SmsLeadSms.attributes={dsl_SmsLeadSms_url, dsl_SmsLeadSms_dbSrc, dsl_SmsLeadSms_privateKey, dsl_SmsLeadSms_value, dsl_SmsLeadSms_account, dsl_SmsLeadSms_sender, dsl_SmsLeadSms_dryrunNumber}

# dsl_Abort class attributes and methods
dsl_Abort_value: Property = Property(name="value", type=StringType)
dsl_Abort.attributes={dsl_Abort_value}

# dsl_GooglecontactPUT class attributes and methods
dsl_GooglecontactPUT_account: Property = Property(name="account", type=StringType)
dsl_GooglecontactPUT_privateKey: Property = Property(name="privateKey", type=StringType)
dsl_GooglecontactPUT_ptwelveFile: Property = Property(name="ptwelveFile", type=StringType)
dsl_GooglecontactPUT_project: Property = Property(name="project", type=StringType)
dsl_GooglecontactPUT_impersonatedUser: Property = Property(name="impersonatedUser", type=StringType)
dsl_GooglecontactPUT_dbSrc: Property = Property(name="dbSrc", type=StringType)
dsl_GooglecontactPUT_value: Property = Property(name="value", type=StringType)
dsl_GooglecontactPUT.attributes={dsl_GooglecontactPUT_privateKey, dsl_GooglecontactPUT_project, dsl_GooglecontactPUT_value, dsl_GooglecontactPUT_account, dsl_GooglecontactPUT_impersonatedUser, dsl_GooglecontactPUT_dbSrc, dsl_GooglecontactPUT_ptwelveFile}

# dsl_GooglecalPUT class attributes and methods
dsl_GooglecalPUT_account: Property = Property(name="account", type=StringType)
dsl_GooglecalPUT_privateKey: Property = Property(name="privateKey", type=StringType)
dsl_GooglecalPUT_ptwelveFile: Property = Property(name="ptwelveFile", type=StringType)
dsl_GooglecalPUT_project: Property = Property(name="project", type=StringType)
dsl_GooglecalPUT_impersonatedUser: Property = Property(name="impersonatedUser", type=StringType)
dsl_GooglecalPUT_dbSrc: Property = Property(name="dbSrc", type=StringType)
dsl_GooglecalPUT_value: Property = Property(name="value", type=StringType)
dsl_GooglecalPUT.attributes={dsl_GooglecalPUT_value, dsl_GooglecalPUT_project, dsl_GooglecalPUT_dbSrc, dsl_GooglecalPUT_account, dsl_GooglecalPUT_ptwelveFile, dsl_GooglecalPUT_privateKey, dsl_GooglecalPUT_impersonatedUser}

# dsl_FBCLead class attributes and methods
dsl_FBCLead_accessToken: Property = Property(name="accessToken", type=StringType)
dsl_FBCLead_appSecret: Property = Property(name="appSecret", type=StringType)
dsl_FBCLead_accountId: Property = Property(name="accountId", type=StringType)
dsl_FBCLead_campaignId: Property = Property(name="campaignId", type=StringType)
dsl_FBCLead_target: Property = Property(name="target", type=StringType)
dsl_FBCLead_value: Property = Property(name="value", type=StringType)
dsl_FBCLead.attributes={dsl_FBCLead_accessToken, dsl_FBCLead_target, dsl_FBCLead_campaignId, dsl_FBCLead_value, dsl_FBCLead_accountId, dsl_FBCLead_appSecret}

# dsl_FBFormDownload class attributes and methods
dsl_FBFormDownload_accessToken: Property = Property(name="accessToken", type=StringType)
dsl_FBFormDownload_appSecret: Property = Property(name="appSecret", type=StringType)
dsl_FBFormDownload_accountId: Property = Property(name="accountId", type=StringType)
dsl_FBFormDownload_formId: Property = Property(name="formId", type=StringType)
dsl_FBFormDownload_target: Property = Property(name="target", type=StringType)
dsl_FBFormDownload_value: Property = Property(name="value", type=StringType)
dsl_FBFormDownload.attributes={dsl_FBFormDownload_target, dsl_FBFormDownload_accessToken, dsl_FBFormDownload_accountId, dsl_FBFormDownload_appSecret, dsl_FBFormDownload_value, dsl_FBFormDownload_formId}

# dsl_Dropfile class attributes and methods
dsl_Dropfile_target: Property = Property(name="target", type=StringType)
dsl_Dropfile.attributes={dsl_Dropfile_target}

# dsl_GooglecontactSelectAll class attributes and methods
dsl_GooglecontactSelectAll_account: Property = Property(name="account", type=StringType)
dsl_GooglecontactSelectAll_privateKey: Property = Property(name="privateKey", type=StringType)
dsl_GooglecontactSelectAll_ptwelveFile: Property = Property(name="ptwelveFile", type=StringType)
dsl_GooglecontactSelectAll_project: Property = Property(name="project", type=StringType)
dsl_GooglecontactSelectAll_impersonatedUser: Property = Property(name="impersonatedUser", type=StringType)
dsl_GooglecontactSelectAll_dbSrc: Property = Property(name="dbSrc", type=StringType)
dsl_GooglecontactSelectAll_value: Property = Property(name="value", type=StringType)
dsl_GooglecontactSelectAll.attributes={dsl_GooglecontactSelectAll_ptwelveFile, dsl_GooglecontactSelectAll_dbSrc, dsl_GooglecontactSelectAll_project, dsl_GooglecontactSelectAll_impersonatedUser, dsl_GooglecontactSelectAll_account, dsl_GooglecontactSelectAll_value, dsl_GooglecontactSelectAll_privateKey}

# dsl_SendMail class attributes and methods
dsl_SendMail_impersonatedUser: Property = Property(name="impersonatedUser", type=StringType)
dsl_SendMail_dbSrc: Property = Property(name="dbSrc", type=StringType)
dsl_SendMail_value: Property = Property(name="value", type=StringType)
dsl_SendMail_dryrunMail: Property = Property(name="dryrunMail", type=StringType)
dsl_SendMail_privateKey: Property = Property(name="privateKey", type=StringType)
dsl_SendMail.attributes={dsl_SendMail_dbSrc, dsl_SendMail_impersonatedUser, dsl_SendMail_privateKey, dsl_SendMail_value, dsl_SendMail_dryrunMail}

# dsl_RestPart class attributes and methods
dsl_RestPart_partName: Property = Property(name="partName", type=StringType)
dsl_RestPart_partData: Property = Property(name="partData", type=StringType)
dsl_RestPart.attributes={dsl_RestPart_partName, dsl_RestPart_partData}

# dsl_TrelloGET class attributes and methods
dsl_TrelloGET_authtoken: Property = Property(name="authtoken", type=StringType)
dsl_TrelloGET_key: Property = Property(name="key", type=StringType)
dsl_TrelloGET_useraccount: Property = Property(name="useraccount", type=StringType)
dsl_TrelloGET_board: Property = Property(name="board", type=StringType)
dsl_TrelloGET_target: Property = Property(name="target", type=StringType)
dsl_TrelloGET_value: Property = Property(name="value", type=StringType)
dsl_TrelloGET.attributes={dsl_TrelloGET_useraccount, dsl_TrelloGET_value, dsl_TrelloGET_authtoken, dsl_TrelloGET_key, dsl_TrelloGET_board, dsl_TrelloGET_target}

# dsl_TrelloPUT class attributes and methods
dsl_TrelloPUT_authtoken: Property = Property(name="authtoken", type=StringType)
dsl_TrelloPUT_key: Property = Property(name="key", type=StringType)
dsl_TrelloPUT_useraccount: Property = Property(name="useraccount", type=StringType)
dsl_TrelloPUT_list: Property = Property(name="list", type=StringType)
dsl_TrelloPUT_source: Property = Property(name="source", type=StringType)
dsl_TrelloPUT_value: Property = Property(name="value", type=StringType)
dsl_TrelloPUT.attributes={dsl_TrelloPUT_authtoken, dsl_TrelloPUT_useraccount, dsl_TrelloPUT_list, dsl_TrelloPUT_value, dsl_TrelloPUT_source, dsl_TrelloPUT_key}

# dsl_Fetch class attributes and methods
dsl_Fetch_source: Property = Property(name="source", type=StringType)
dsl_Fetch_value: Property = Property(name="value", type=StringType)
dsl_Fetch.attributes={dsl_Fetch_value, dsl_Fetch_source}

# dsl_Callprocess class attributes and methods
dsl_Callprocess_target: Property = Property(name="target", type=StringType)
dsl_Callprocess_source: Property = Property(name="source", type=StringType)
dsl_Callprocess_datasource: Property = Property(name="datasource", type=StringType)
dsl_Callprocess_value: Property = Property(name="value", type=StringType)
dsl_Callprocess.attributes={dsl_Callprocess_source, dsl_Callprocess_target, dsl_Callprocess_value, dsl_Callprocess_datasource}

# dsl_Doozle class attributes and methods
dsl_Doozle_target: Property = Property(name="target", type=StringType)
dsl_Doozle_on: Property = Property(name="on", type=StringType)
dsl_Doozle_value: Property = Property(name="value", type=StringType)
dsl_Doozle.attributes={dsl_Doozle_target, dsl_Doozle_value, dsl_Doozle_on}

# dsl_Rest class attributes and methods
dsl_Rest_urldata: Property = Property(name="urldata", type=StringType)
dsl_Rest_headerdatafrom: Property = Property(name="headerdatafrom", type=StringType)
dsl_Rest_headerdata: Property = Property(name="headerdata", type=StringType)
dsl_Rest_postdatafrom: Property = Property(name="postdatafrom", type=StringType)
dsl_Rest_parentName: Property = Property(name="parentName", type=StringType)
dsl_Rest_parentdata: Property = Property(name="parentdata", type=StringType)
dsl_Rest_ackdatato: Property = Property(name="ackdatato", type=StringType)
dsl_Rest_ackdata: Property = Property(name="ackdata", type=StringType)
dsl_Rest_authtoken: Property = Property(name="authtoken", type=StringType)
dsl_Rest_url: Property = Property(name="url", type=StringType)
dsl_Rest_method: Property = Property(name="method", type=StringType)
dsl_Rest_resourcedatafrom: Property = Property(name="resourcedatafrom", type=StringType)
dsl_Rest.attributes={dsl_Rest_parentName, dsl_Rest_headerdatafrom, dsl_Rest_postdatafrom, dsl_Rest_url, dsl_Rest_method, dsl_Rest_ackdata, dsl_Rest_resourcedatafrom, dsl_Rest_headerdata, dsl_Rest_parentdata, dsl_Rest_authtoken, dsl_Rest_ackdatato, dsl_Rest_urldata}

# dsl_SlackPUT class attributes and methods
dsl_SlackPUT_team: Property = Property(name="team", type=StringType)
dsl_SlackPUT_channel: Property = Property(name="channel", type=StringType)
dsl_SlackPUT_value: Property = Property(name="value", type=StringType)
dsl_SlackPUT.attributes={dsl_SlackPUT_value, dsl_SlackPUT_team, dsl_SlackPUT_channel}

# dsl_Copydata class attributes and methods
dsl_Copydata_source: Property = Property(name="source", type=StringType)
dsl_Copydata_to: Property = Property(name="to", type=StringType)
dsl_Copydata_value: Property = Property(name="value", type=StringType)
dsl_Copydata.attributes={dsl_Copydata_to, dsl_Copydata_source, dsl_Copydata_value}

# dsl_WriteCsv class attributes and methods
dsl_WriteCsv_source: Property = Property(name="source", type=StringType)
dsl_WriteCsv_to: Property = Property(name="to", type=StringType)
dsl_WriteCsv_delim: Property = Property(name="delim", type=StringType)
dsl_WriteCsv_value: Property = Property(name="value", type=StringType)
dsl_WriteCsv.attributes={dsl_WriteCsv_to, dsl_WriteCsv_source, dsl_WriteCsv_delim, dsl_WriteCsv_value}

# dsl_LoadCsv class attributes and methods
dsl_LoadCsv_source: Property = Property(name="source", type=StringType)
dsl_LoadCsv_to: Property = Property(name="to", type=StringType)
dsl_LoadCsv_delim: Property = Property(name="delim", type=StringType)
dsl_LoadCsv_value: Property = Property(name="value", type=StringType)
dsl_LoadCsv.attributes={dsl_LoadCsv_source, dsl_LoadCsv_value, dsl_LoadCsv_delim, dsl_LoadCsv_to}

# dsl_Transform class attributes and methods
dsl_Transform_on: Property = Property(name="on", type=StringType)
dsl_Transform_value: Property = Property(name="value", type=StringType)
dsl_Transform.attributes={dsl_Transform_value, dsl_Transform_on}

# dsl_Updatedaudit class attributes and methods
dsl_Updatedaudit_logsink: Property = Property(name="logsink", type=StringType)
dsl_Updatedaudit_datasource: Property = Property(name="datasource", type=StringType)
dsl_Updatedaudit_value: Property = Property(name="value", type=StringType)
dsl_Updatedaudit.attributes={dsl_Updatedaudit_value, dsl_Updatedaudit_datasource, dsl_Updatedaudit_logsink}

# dsl_ClickSendSms class attributes and methods
dsl_ClickSendSms_value: Property = Property(name="value", type=StringType)
dsl_ClickSendSms_userid: Property = Property(name="userid", type=StringType)
dsl_ClickSendSms_securityKey: Property = Property(name="securityKey", type=StringType)
dsl_ClickSendSms_target: Property = Property(name="target", type=StringType)
dsl_ClickSendSms.attributes={dsl_ClickSendSms_value, dsl_ClickSendSms_userid, dsl_ClickSendSms_securityKey, dsl_ClickSendSms_target}

# Relationships
try0: BinaryAssociation = BinaryAssociation(
    name="try0",
    ends={
        Property(name="dsl_Try", type=dsl_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Process", type=dsl_Try, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
catch1: BinaryAssociation = BinaryAssociation(
    name="catch1",
    ends={
        Property(name="dsl_Catch", type=dsl_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Process2", type=dsl_Catch, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
finally3: BinaryAssociation = BinaryAssociation(
    name="finally3",
    ends={
        Property(name="dsl_Finally", type=dsl_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Process4", type=dsl_Finally, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action5: BinaryAssociation = BinaryAssociation(
    name="action5",
    ends={
        Property(name="dsl_Action", type=dsl_Try, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Try6", type=dsl_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition13: BinaryAssociation = BinaryAssociation(
    name="condition13",
    ends={
        Property(name="dsl_Expression", type=dsl_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Action14", type=dsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action7: BinaryAssociation = BinaryAssociation(
    name="action7",
    ends={
        Property(name="dsl_Action9", type=dsl_Finally, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Finally8", type=dsl_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action10: BinaryAssociation = BinaryAssociation(
    name="action10",
    ends={
        Property(name="dsl_Action12", type=dsl_Catch, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Catch11", type=dsl_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parts15: BinaryAssociation = BinaryAssociation(
    name="parts15",
    ends={
        Property(name="dsl_RestPart", type=dsl_Rest, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Rest", type=dsl_RestPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_dsl_ExecJava_Action = Generalization(general=Action, specific=dsl_ExecJava)
gen_dsl_FirebaseDatabasePut_Action = Generalization(general=Action, specific=dsl_FirebaseDatabasePut)
gen_dsl_FirebaseReactiveNotification_Action = Generalization(general=Action, specific=dsl_FirebaseReactiveNotification)
gen_dsl_SmsLeadSms_Action = Generalization(general=Action, specific=dsl_SmsLeadSms)
gen_dsl_Abort_Action = Generalization(general=Action, specific=dsl_Abort)
gen_dsl_GooglecontactPUT_Action = Generalization(general=Action, specific=dsl_GooglecontactPUT)
gen_dsl_GooglecalPUT_Action = Generalization(general=Action, specific=dsl_GooglecalPUT)
gen_dsl_FBCLead_Action = Generalization(general=Action, specific=dsl_FBCLead)
gen_dsl_FBFormDownload_Action = Generalization(general=Action, specific=dsl_FBFormDownload)
gen_dsl_Dropfile_Action = Generalization(general=Action, specific=dsl_Dropfile)
gen_dsl_GooglecontactSelectAll_Action = Generalization(general=Action, specific=dsl_GooglecontactSelectAll)
gen_dsl_SendMail_Action = Generalization(general=Action, specific=dsl_SendMail)
gen_dsl_TrelloGET_Action = Generalization(general=Action, specific=dsl_TrelloGET)
gen_dsl_TrelloPUT_Action = Generalization(general=Action, specific=dsl_TrelloPUT)
gen_dsl_Fetch_Action = Generalization(general=Action, specific=dsl_Fetch)
gen_dsl_Callprocess_Action = Generalization(general=Action, specific=dsl_Callprocess)
gen_dsl_Doozle_Action = Generalization(general=Action, specific=dsl_Doozle)
gen_dsl_Rest_Action = Generalization(general=Action, specific=dsl_Rest)
gen_dsl_SlackPUT_Action = Generalization(general=Action, specific=dsl_SlackPUT)
gen_dsl_Copydata_Action = Generalization(general=Action, specific=dsl_Copydata)
gen_dsl_WriteCsv_Action = Generalization(general=Action, specific=dsl_WriteCsv)
gen_dsl_LoadCsv_Action = Generalization(general=Action, specific=dsl_LoadCsv)
gen_dsl_Transform_Action = Generalization(general=Action, specific=dsl_Transform)
gen_dsl_Updatedaudit_Action = Generalization(general=Action, specific=dsl_Updatedaudit)
gen_dsl_ClickSendSms_Action = Generalization(general=Action, specific=dsl_ClickSendSms)

# Domain Model
domain_model = DomainModel(
    name="dsl",
    types={dsl_Process, dsl_Try, dsl_Catch, dsl_Finally, dsl_Action, dsl_Expression, dsl_ExecJava, Action, dsl_FirebaseDatabasePut, dsl_FirebaseReactiveNotification, dsl_SmsLeadSms, dsl_Abort, dsl_GooglecontactPUT, dsl_GooglecalPUT, dsl_FBCLead, dsl_FBFormDownload, dsl_Dropfile, dsl_GooglecontactSelectAll, dsl_SendMail, dsl_RestPart, dsl_TrelloGET, dsl_TrelloPUT, dsl_Fetch, dsl_Callprocess, dsl_Doozle, dsl_Rest, dsl_SlackPUT, dsl_Copydata, dsl_WriteCsv, dsl_LoadCsv, dsl_Transform, dsl_Updatedaudit, dsl_ClickSendSms},
    associations={try0, catch1, finally3, action5, condition13, action7, action10, parts15},
    generalizations={gen_dsl_ExecJava_Action, gen_dsl_FirebaseDatabasePut_Action, gen_dsl_FirebaseReactiveNotification_Action, gen_dsl_SmsLeadSms_Action, gen_dsl_Abort_Action, gen_dsl_GooglecontactPUT_Action, gen_dsl_GooglecalPUT_Action, gen_dsl_FBCLead_Action, gen_dsl_FBFormDownload_Action, gen_dsl_Dropfile_Action, gen_dsl_GooglecontactSelectAll_Action, gen_dsl_SendMail_Action, gen_dsl_TrelloGET_Action, gen_dsl_TrelloPUT_Action, gen_dsl_Fetch_Action, gen_dsl_Callprocess_Action, gen_dsl_Doozle_Action, gen_dsl_Rest_Action, gen_dsl_SlackPUT_Action, gen_dsl_Copydata_Action, gen_dsl_WriteCsv_Action, gen_dsl_LoadCsv_Action, gen_dsl_Transform_Action, gen_dsl_Updatedaudit_Action, gen_dsl_ClickSendSms_Action},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)