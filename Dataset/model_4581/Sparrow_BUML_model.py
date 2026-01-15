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
sparrow_Process = Class(name="sparrow::Process")
sparrow_Try = Class(name="sparrow::Try")
sparrow_Catch = Class(name="sparrow::Catch")
sparrow_Finally = Class(name="sparrow::Finally")
sparrow_Doozle = Class(name="sparrow::Doozle")
sparrow_Rest = Class(name="sparrow::Rest")
sparrow_RestPart = Class(name="sparrow::RestPart")
sparrow_Action = Class(name="sparrow::Action")
sparrow_Expression = Class(name="sparrow::Expression")
sparrow_FBCLead = Class(name="sparrow::FBCLead")
Action = Class(name="Action")
sparrow_Dropfile = Class(name="sparrow::Dropfile")
sparrow_Sms = Class(name="sparrow::Sms")
sparrow_SlackPUT = Class(name="sparrow::SlackPUT")
sparrow_GooglecalPUT = Class(name="sparrow::GooglecalPUT")
sparrow_Copydata = Class(name="sparrow::Copydata")
sparrow_WriteCsv = Class(name="sparrow::WriteCsv")
sparrow_TrelloGET = Class(name="sparrow::TrelloGET")
sparrow_TrelloPUT = Class(name="sparrow::TrelloPUT")
sparrow_Fetch = Class(name="sparrow::Fetch")
sparrow_Callprocess = Class(name="sparrow::Callprocess")
sparrow_Updatedaudit = Class(name="sparrow::Updatedaudit")
sparrow_LoadCsv = Class(name="sparrow::LoadCsv")
sparrow_Transform = Class(name="sparrow::Transform")

# sparrow_Process class attributes and methods
sparrow_Process_name: Property = Property(name="name", type=StringType)
sparrow_Process.attributes={sparrow_Process_name}

# sparrow_Try class attributes and methods
sparrow_Try_name: Property = Property(name="name", type=StringType)
sparrow_Try.attributes={sparrow_Try_name}

# sparrow_Catch class attributes and methods
sparrow_Catch_name: Property = Property(name="name", type=StringType)
sparrow_Catch.attributes={sparrow_Catch_name}

# sparrow_Finally class attributes and methods
sparrow_Finally_name: Property = Property(name="name", type=StringType)
sparrow_Finally.attributes={sparrow_Finally_name}

# sparrow_Doozle class attributes and methods
sparrow_Doozle_target: Property = Property(name="target", type=StringType)
sparrow_Doozle_on: Property = Property(name="on", type=StringType)
sparrow_Doozle_value: Property = Property(name="value", type=StringType)
sparrow_Doozle.attributes={sparrow_Doozle_value, sparrow_Doozle_on, sparrow_Doozle_target}

# sparrow_Rest class attributes and methods
sparrow_Rest_authtoken: Property = Property(name="authtoken", type=StringType)
sparrow_Rest_url: Property = Property(name="url", type=StringType)
sparrow_Rest_method: Property = Property(name="method", type=StringType)
sparrow_Rest_resourcedatafrom: Property = Property(name="resourcedatafrom", type=StringType)
sparrow_Rest_urldata: Property = Property(name="urldata", type=StringType)
sparrow_Rest_headerdatafrom: Property = Property(name="headerdatafrom", type=StringType)
sparrow_Rest_headerdata: Property = Property(name="headerdata", type=StringType)
sparrow_Rest_postdatafrom: Property = Property(name="postdatafrom", type=StringType)
sparrow_Rest_parentName: Property = Property(name="parentName", type=StringType)
sparrow_Rest_parentdata: Property = Property(name="parentdata", type=StringType)
sparrow_Rest_ackdatato: Property = Property(name="ackdatato", type=StringType)
sparrow_Rest_ackdata: Property = Property(name="ackdata", type=StringType)
sparrow_Rest.attributes={sparrow_Rest_method, sparrow_Rest_headerdatafrom, sparrow_Rest_parentName, sparrow_Rest_postdatafrom, sparrow_Rest_resourcedatafrom, sparrow_Rest_url, sparrow_Rest_headerdata, sparrow_Rest_authtoken, sparrow_Rest_ackdata, sparrow_Rest_parentdata, sparrow_Rest_urldata, sparrow_Rest_ackdatato}

# sparrow_RestPart class attributes and methods
sparrow_RestPart_partName: Property = Property(name="partName", type=StringType)
sparrow_RestPart_partData: Property = Property(name="partData", type=StringType)
sparrow_RestPart.attributes={sparrow_RestPart_partName, sparrow_RestPart_partData}

# sparrow_Action class attributes and methods
sparrow_Action_name: Property = Property(name="name", type=StringType)
sparrow_Action.attributes={sparrow_Action_name}

# sparrow_Expression class attributes and methods
sparrow_Expression_lhs: Property = Property(name="lhs", type=StringType)
sparrow_Expression_operator: Property = Property(name="operator", type=StringType)
sparrow_Expression_rhs: Property = Property(name="rhs", type=StringType)
sparrow_Expression.attributes={sparrow_Expression_rhs, sparrow_Expression_lhs, sparrow_Expression_operator}

# sparrow_FBCLead class attributes and methods
sparrow_FBCLead_accessToken: Property = Property(name="accessToken", type=StringType)
sparrow_FBCLead_appSecret: Property = Property(name="appSecret", type=StringType)
sparrow_FBCLead_accountId: Property = Property(name="accountId", type=StringType)
sparrow_FBCLead_campaignId: Property = Property(name="campaignId", type=StringType)
sparrow_FBCLead_target: Property = Property(name="target", type=StringType)
sparrow_FBCLead_value: Property = Property(name="value", type=StringType)
sparrow_FBCLead.attributes={sparrow_FBCLead_target, sparrow_FBCLead_accountId, sparrow_FBCLead_campaignId, sparrow_FBCLead_accessToken, sparrow_FBCLead_value, sparrow_FBCLead_appSecret}

# Action class attributes and methods

# sparrow_Dropfile class attributes and methods
sparrow_Dropfile_target: Property = Property(name="target", type=StringType)
sparrow_Dropfile.attributes={sparrow_Dropfile_target}

# sparrow_Sms class attributes and methods
sparrow_Sms_target: Property = Property(name="target", type=StringType)
sparrow_Sms_value: Property = Property(name="value", type=StringType)
sparrow_Sms.attributes={sparrow_Sms_target, sparrow_Sms_value}

# sparrow_SlackPUT class attributes and methods
sparrow_SlackPUT_team: Property = Property(name="team", type=StringType)
sparrow_SlackPUT_channel: Property = Property(name="channel", type=StringType)
sparrow_SlackPUT_value: Property = Property(name="value", type=StringType)
sparrow_SlackPUT.attributes={sparrow_SlackPUT_team, sparrow_SlackPUT_value, sparrow_SlackPUT_channel}

# sparrow_GooglecalPUT class attributes and methods
sparrow_GooglecalPUT_authstore: Property = Property(name="authstore", type=StringType)
sparrow_GooglecalPUT_key: Property = Property(name="key", type=StringType)
sparrow_GooglecalPUT_useraccount: Property = Property(name="useraccount", type=StringType)
sparrow_GooglecalPUT_source: Property = Property(name="source", type=StringType)
sparrow_GooglecalPUT_value: Property = Property(name="value", type=StringType)
sparrow_GooglecalPUT.attributes={sparrow_GooglecalPUT_useraccount, sparrow_GooglecalPUT_value, sparrow_GooglecalPUT_source, sparrow_GooglecalPUT_key, sparrow_GooglecalPUT_authstore}

# sparrow_Copydata class attributes and methods
sparrow_Copydata_source: Property = Property(name="source", type=StringType)
sparrow_Copydata_to: Property = Property(name="to", type=StringType)
sparrow_Copydata_value: Property = Property(name="value", type=StringType)
sparrow_Copydata.attributes={sparrow_Copydata_source, sparrow_Copydata_value, sparrow_Copydata_to}

# sparrow_WriteCsv class attributes and methods
sparrow_WriteCsv_source: Property = Property(name="source", type=StringType)
sparrow_WriteCsv_to: Property = Property(name="to", type=StringType)
sparrow_WriteCsv_delim: Property = Property(name="delim", type=StringType)
sparrow_WriteCsv_value: Property = Property(name="value", type=StringType)
sparrow_WriteCsv.attributes={sparrow_WriteCsv_source, sparrow_WriteCsv_value, sparrow_WriteCsv_delim, sparrow_WriteCsv_to}

# sparrow_TrelloGET class attributes and methods
sparrow_TrelloGET_authtoken: Property = Property(name="authtoken", type=StringType)
sparrow_TrelloGET_key: Property = Property(name="key", type=StringType)
sparrow_TrelloGET_useraccount: Property = Property(name="useraccount", type=StringType)
sparrow_TrelloGET_board: Property = Property(name="board", type=StringType)
sparrow_TrelloGET_target: Property = Property(name="target", type=StringType)
sparrow_TrelloGET_value: Property = Property(name="value", type=StringType)
sparrow_TrelloGET.attributes={sparrow_TrelloGET_value, sparrow_TrelloGET_key, sparrow_TrelloGET_useraccount, sparrow_TrelloGET_target, sparrow_TrelloGET_board, sparrow_TrelloGET_authtoken}

# sparrow_TrelloPUT class attributes and methods
sparrow_TrelloPUT_authtoken: Property = Property(name="authtoken", type=StringType)
sparrow_TrelloPUT_key: Property = Property(name="key", type=StringType)
sparrow_TrelloPUT_useraccount: Property = Property(name="useraccount", type=StringType)
sparrow_TrelloPUT_list: Property = Property(name="list", type=StringType)
sparrow_TrelloPUT_source: Property = Property(name="source", type=StringType)
sparrow_TrelloPUT_value: Property = Property(name="value", type=StringType)
sparrow_TrelloPUT.attributes={sparrow_TrelloPUT_useraccount, sparrow_TrelloPUT_source, sparrow_TrelloPUT_key, sparrow_TrelloPUT_value, sparrow_TrelloPUT_authtoken, sparrow_TrelloPUT_list}

# sparrow_Fetch class attributes and methods
sparrow_Fetch_source: Property = Property(name="source", type=StringType)
sparrow_Fetch_value: Property = Property(name="value", type=StringType)
sparrow_Fetch.attributes={sparrow_Fetch_source, sparrow_Fetch_value}

# sparrow_Callprocess class attributes and methods
sparrow_Callprocess_target: Property = Property(name="target", type=StringType)
sparrow_Callprocess_source: Property = Property(name="source", type=StringType)
sparrow_Callprocess_datasource: Property = Property(name="datasource", type=StringType)
sparrow_Callprocess_value: Property = Property(name="value", type=StringType)
sparrow_Callprocess.attributes={sparrow_Callprocess_value, sparrow_Callprocess_datasource, sparrow_Callprocess_target, sparrow_Callprocess_source}

# sparrow_Updatedaudit class attributes and methods
sparrow_Updatedaudit_value: Property = Property(name="value", type=StringType)
sparrow_Updatedaudit_logsink: Property = Property(name="logsink", type=StringType)
sparrow_Updatedaudit.attributes={sparrow_Updatedaudit_value, sparrow_Updatedaudit_logsink}

# sparrow_LoadCsv class attributes and methods
sparrow_LoadCsv_source: Property = Property(name="source", type=StringType)
sparrow_LoadCsv_to: Property = Property(name="to", type=StringType)
sparrow_LoadCsv_delim: Property = Property(name="delim", type=StringType)
sparrow_LoadCsv_value: Property = Property(name="value", type=StringType)
sparrow_LoadCsv.attributes={sparrow_LoadCsv_delim, sparrow_LoadCsv_value, sparrow_LoadCsv_to, sparrow_LoadCsv_source}

# sparrow_Transform class attributes and methods
sparrow_Transform_on: Property = Property(name="on", type=StringType)
sparrow_Transform_value: Property = Property(name="value", type=StringType)
sparrow_Transform.attributes={sparrow_Transform_value, sparrow_Transform_on}

# Relationships
try0: BinaryAssociation = BinaryAssociation(
    name="try0",
    ends={
        Property(name="sparrow_Try", type=sparrow_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="sparrow_Process", type=sparrow_Try, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
catch1: BinaryAssociation = BinaryAssociation(
    name="catch1",
    ends={
        Property(name="sparrow_Catch", type=sparrow_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="sparrow_Process2", type=sparrow_Catch, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
finally3: BinaryAssociation = BinaryAssociation(
    name="finally3",
    ends={
        Property(name="sparrow_Finally", type=sparrow_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="sparrow_Process4", type=sparrow_Finally, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parts15: BinaryAssociation = BinaryAssociation(
    name="parts15",
    ends={
        Property(name="sparrow_RestPart", type=sparrow_Rest, multiplicity=Multiplicity(1, 1)),
        Property(name="sparrow_Rest", type=sparrow_RestPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action5: BinaryAssociation = BinaryAssociation(
    name="action5",
    ends={
        Property(name="sparrow_Action", type=sparrow_Try, multiplicity=Multiplicity(1, 1)),
        Property(name="sparrow_Try6", type=sparrow_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action7: BinaryAssociation = BinaryAssociation(
    name="action7",
    ends={
        Property(name="sparrow_Action9", type=sparrow_Finally, multiplicity=Multiplicity(1, 1)),
        Property(name="sparrow_Finally8", type=sparrow_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action10: BinaryAssociation = BinaryAssociation(
    name="action10",
    ends={
        Property(name="sparrow_Action12", type=sparrow_Catch, multiplicity=Multiplicity(1, 1)),
        Property(name="sparrow_Catch11", type=sparrow_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition13: BinaryAssociation = BinaryAssociation(
    name="condition13",
    ends={
        Property(name="sparrow_Expression", type=sparrow_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="sparrow_Action14", type=sparrow_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_sparrow_Doozle_Action = Generalization(general=Action, specific=sparrow_Doozle)
gen_sparrow_Rest_Action = Generalization(general=Action, specific=sparrow_Rest)
gen_sparrow_FBCLead_Action = Generalization(general=Action, specific=sparrow_FBCLead)
gen_sparrow_Dropfile_Action = Generalization(general=Action, specific=sparrow_Dropfile)
gen_sparrow_Sms_Action = Generalization(general=Action, specific=sparrow_Sms)
gen_sparrow_SlackPUT_Action = Generalization(general=Action, specific=sparrow_SlackPUT)
gen_sparrow_GooglecalPUT_Action = Generalization(general=Action, specific=sparrow_GooglecalPUT)
gen_sparrow_Copydata_Action = Generalization(general=Action, specific=sparrow_Copydata)
gen_sparrow_WriteCsv_Action = Generalization(general=Action, specific=sparrow_WriteCsv)
gen_sparrow_TrelloGET_Action = Generalization(general=Action, specific=sparrow_TrelloGET)
gen_sparrow_TrelloPUT_Action = Generalization(general=Action, specific=sparrow_TrelloPUT)
gen_sparrow_Fetch_Action = Generalization(general=Action, specific=sparrow_Fetch)
gen_sparrow_Callprocess_Action = Generalization(general=Action, specific=sparrow_Callprocess)
gen_sparrow_Updatedaudit_Action = Generalization(general=Action, specific=sparrow_Updatedaudit)
gen_sparrow_LoadCsv_Action = Generalization(general=Action, specific=sparrow_LoadCsv)
gen_sparrow_Transform_Action = Generalization(general=Action, specific=sparrow_Transform)

# Domain Model
domain_model = DomainModel(
    name="sparrow",
    types={sparrow_Process, sparrow_Try, sparrow_Catch, sparrow_Finally, sparrow_Doozle, sparrow_Rest, sparrow_RestPart, sparrow_Action, sparrow_Expression, sparrow_FBCLead, Action, sparrow_Dropfile, sparrow_Sms, sparrow_SlackPUT, sparrow_GooglecalPUT, sparrow_Copydata, sparrow_WriteCsv, sparrow_TrelloGET, sparrow_TrelloPUT, sparrow_Fetch, sparrow_Callprocess, sparrow_Updatedaudit, sparrow_LoadCsv, sparrow_Transform},
    associations={try0, catch1, finally3, parts15, action5, action7, action10, condition13},
    generalizations={gen_sparrow_Doozle_Action, gen_sparrow_Rest_Action, gen_sparrow_FBCLead_Action, gen_sparrow_Dropfile_Action, gen_sparrow_Sms_Action, gen_sparrow_SlackPUT_Action, gen_sparrow_GooglecalPUT_Action, gen_sparrow_Copydata_Action, gen_sparrow_WriteCsv_Action, gen_sparrow_TrelloGET_Action, gen_sparrow_TrelloPUT_Action, gen_sparrow_Fetch_Action, gen_sparrow_Callprocess_Action, gen_sparrow_Updatedaudit_Action, gen_sparrow_LoadCsv_Action, gen_sparrow_Transform_Action},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)