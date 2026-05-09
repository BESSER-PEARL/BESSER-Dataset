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
Language: Enumeration = Enumeration(
    name="Language",
    literals={
            EnumerationLiteral(name="Java"),
			EnumerationLiteral(name="Python"),
			EnumerationLiteral(name="C_Sharp"),
			EnumerationLiteral(name="Scala"),
			EnumerationLiteral(name="PHP"),
			EnumerationLiteral(name="C_Cpp"),
			EnumerationLiteral(name="Ruby"),
			EnumerationLiteral(name="Other")
    }
)

HttpMethod: Enumeration = Enumeration(
    name="HttpMethod",
    literals={
            EnumerationLiteral(name="GET"),
			EnumerationLiteral(name="HEAD"),
			EnumerationLiteral(name="POST"),
			EnumerationLiteral(name="PUT"),
			EnumerationLiteral(name="DELETE"),
			EnumerationLiteral(name="OPTIONS"),
			EnumerationLiteral(name="TRACE"),
			EnumerationLiteral(name="CONNECT"),
			EnumerationLiteral(name="PATCH")
    }
)

UrlPattern: Enumeration = Enumeration(
    name="UrlPattern",
    literals={
            EnumerationLiteral(name="ANT")
    }
)

TaskStatus: Enumeration = Enumeration(
    name="TaskStatus",
    literals={
            EnumerationLiteral(name="todo"),
			EnumerationLiteral(name="in_progress"),
			EnumerationLiteral(name="skipped"),
			EnumerationLiteral(name="done")
    }
)

# Classes
assessment_Findings = Class(name="assessment_Findings")
assessment_Tasks = Class(name="assessment_Tasks")
assessment_Application = Class(name="assessment_Application")
assessment_Accounts = Class(name="assessment_Accounts")
assessment_Entitlements = Class(name="assessment_Entitlements")
assessment_Controllers = Class(name="assessment_Controllers")
assessment_Models = Class(name="assessment_Models")
assessment_Scm = Class(name="assessment_Scm")
assessment_Views = Class(name="assessment_Views")
assessment_Http = Class(name="assessment_Http")
GraphNode = Class(name="GraphNode")
assessment_Node = Class(name="assessment_Node", is_abstract=True)
Label = Class(name="Label")
Notes = Class(name="Notes")
assessment_GraphNode = Class(name="assessment_GraphNode", is_abstract=True)
assessment_Task = Class(name="assessment_Task")
assessment_Finding = Class(name="assessment_Finding")
assessment_Assessment = Class(name="assessment_Assessment")
assessment_Applications = Class(name="assessment_Applications")
assessment_Account = Class(name="assessment_Account")
assessment_Entitlement = Class(name="assessment_Entitlement")
assessment_Sinks = Class(name="assessment_Sinks")
assessment_Resources = Class(name="assessment_Resources")
assessment_Sink = Class(name="assessment_Sink")
Node = Class(name="Node")
assessment_Controller = Class(name="assessment_Controller")
assessment_View = Class(name="assessment_View")
assessment_Model = Class(name="assessment_Model")
assessment_Generic = Class(name="assessment_Generic")
assessment_Control = Class(name="assessment_Control")
assessment_Label = Class(name="assessment_Label", is_abstract=True)
assessment_Contents = Class(name="assessment_Contents", is_abstract=True)
assessment_Snippet = Class(name="assessment_Snippet")
Contents = Class(name="Contents")
assessment_Resource = Class(name="assessment_Resource")
assessment_Url = Class(name="assessment_Url")
assessment_Graph = Class(name="assessment_Graph", is_abstract=True)
assessment_Notes = Class(name="assessment_Notes", is_abstract=True)

# assessment_Findings class attributes and methods

# assessment_Tasks class attributes and methods

# assessment_Application class attributes and methods
assessment_Application_internalURL: Property = Property(name="internalURL", type=StringType)
assessment_Application_externalURL: Property = Property(name="externalURL", type=StringType)
assessment_Application.attributes={assessment_Application_externalURL, assessment_Application_internalURL}

# assessment_Accounts class attributes and methods

# assessment_Entitlements class attributes and methods

# assessment_Controllers class attributes and methods

# assessment_Models class attributes and methods

# assessment_Scm class attributes and methods
assessment_Scm_repository: Property = Property(name="repository", type=StringType)
assessment_Scm_branchTag: Property = Property(name="branchTag", type=StringType)
assessment_Scm.attributes={assessment_Scm_branchTag, assessment_Scm_repository}

# assessment_Views class attributes and methods

# assessment_Http class attributes and methods
assessment_Http_request: Property = Property(name="request", type=StringType)
assessment_Http_response: Property = Property(name="response", type=StringType)
assessment_Http.attributes={assessment_Http_request, assessment_Http_response}

# GraphNode class attributes and methods

# assessment_Node class attributes and methods

# Label class attributes and methods

# Notes class attributes and methods

# assessment_GraphNode class attributes and methods

# assessment_Task class attributes and methods
assessment_Task_status: Property = Property(name="status", type=StringType)
assessment_Task.attributes={assessment_Task_status}

# assessment_Finding class attributes and methods
assessment_Finding_reproducer: Property = Property(name="reproducer", type=StringType)
assessment_Finding_remediation: Property = Property(name="remediation", type=StringType)
assessment_Finding_references: Property = Property(name="references", type=StringType)
assessment_Finding.attributes={assessment_Finding_reproducer, assessment_Finding_references, assessment_Finding_remediation}

# assessment_Assessment class attributes and methods

# assessment_Applications class attributes and methods

# assessment_Account class attributes and methods
assessment_Account_email: Property = Property(name="email", type=StringType)
assessment_Account_password: Property = Property(name="password", type=StringType)
assessment_Account.attributes={assessment_Account_email, assessment_Account_password}

# assessment_Entitlement class attributes and methods

# assessment_Sinks class attributes and methods

# assessment_Resources class attributes and methods

# assessment_Sink class attributes and methods
assessment_Sink_cwes: Property = Property(name="cwes", type=IntegerType)
assessment_Sink.attributes={assessment_Sink_cwes}

# Node class attributes and methods

# assessment_Controller class attributes and methods

# assessment_View class attributes and methods

# assessment_Model class attributes and methods

# assessment_Generic class attributes and methods

# assessment_Control class attributes and methods

# assessment_Label class attributes and methods
assessment_Label_label: Property = Property(name="label", type=StringType)
assessment_Label.attributes={assessment_Label_label}

# assessment_Contents class attributes and methods
assessment_Contents_contents: Property = Property(name="contents", type=StringType)
assessment_Contents.attributes={assessment_Contents_contents}

# assessment_Snippet class attributes and methods
assessment_Snippet_lineEnd: Property = Property(name="lineEnd", type=IntegerType)
assessment_Snippet_columnStart: Property = Property(name="columnStart", type=IntegerType)
assessment_Snippet_columnEnd: Property = Property(name="columnEnd", type=IntegerType)
assessment_Snippet_lineStart: Property = Property(name="lineStart", type=IntegerType)
assessment_Snippet.attributes={assessment_Snippet_lineStart, assessment_Snippet_columnStart, assessment_Snippet_columnEnd, assessment_Snippet_lineEnd}

# Contents class attributes and methods

# assessment_Resource class attributes and methods

# assessment_Url class attributes and methods
assessment_Url_pattern: Property = Property(name="pattern", type=StringType)
assessment_Url_patternType: Property = Property(name="patternType", type=StringType)
assessment_Url.attributes={assessment_Url_pattern, assessment_Url_patternType}

# assessment_Graph class attributes and methods

# assessment_Notes class attributes and methods
assessment_Notes_notes: Property = Property(name="notes", type=StringType)
assessment_Notes.attributes={assessment_Notes_notes}

# Relationships
findings13: BinaryAssociation = BinaryAssociation(
    name="findings13",
    ends={
        Property(name="Findings", type=assessment_Assessment, multiplicity=Multiplicity(1, 1)),
        Property(name="assessment14", type=assessment_Findings, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tasks15: BinaryAssociation = BinaryAssociation(
    name="tasks15",
    ends={
        Property(name="Tasks", type=assessment_Assessment, multiplicity=Multiplicity(1, 1)),
        Property(name="assessment16", type=assessment_Tasks, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accounts17: BinaryAssociation = BinaryAssociation(
    name="accounts17",
    ends={
        Property(name="assessment_Accounts", type=assessment_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="assessment_Application", type=assessment_Accounts, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entitlements18: BinaryAssociation = BinaryAssociation(
    name="entitlements18",
    ends={
        Property(name="assessment_Entitlements", type=assessment_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="assessment_Application19", type=assessment_Entitlements, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
controllers20: BinaryAssociation = BinaryAssociation(
    name="controllers20",
    ends={
        Property(name="Controllers", type=assessment_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="application", type=assessment_Controllers, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
models21: BinaryAssociation = BinaryAssociation(
    name="models21",
    ends={
        Property(name="Models", type=assessment_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="application22", type=assessment_Models, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scm23: BinaryAssociation = BinaryAssociation(
    name="scm23",
    ends={
        Property(name="Scm", type=assessment_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="application24", type=assessment_Scm, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
views25: BinaryAssociation = BinaryAssociation(
    name="views25",
    ends={
        Property(name="Views", type=assessment_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="application26", type=assessment_Views, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children0: BinaryAssociation = BinaryAssociation(
    name="children0",
    ends={
        Property(name="assessment_GraphNode", type=assessment_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="assessment_Node", type=assessment_GraphNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent2: BinaryAssociation = BinaryAssociation(
    name="parent2",
    ends={
        Property(name="assessment_Node3", type=assessment_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="assessment_Node1", type=assessment_Node, multiplicity=Multiplicity(0, 1))
    }
)
refersTo5: BinaryAssociation = BinaryAssociation(
    name="refersTo5",
    ends={
        Property(name="Node", type=assessment_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="referredBy", type=assessment_Node, multiplicity=Multiplicity(0, 9999))
    }
)
referredBy7: BinaryAssociation = BinaryAssociation(
    name="referredBy7",
    ends={
        Property(name="Node8", type=assessment_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="refersTo", type=assessment_Node, multiplicity=Multiplicity(0, 9999))
    }
)
tasks9: BinaryAssociation = BinaryAssociation(
    name="tasks9",
    ends={
        Property(name="Task", type=assessment_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="affects", type=assessment_Task, multiplicity=Multiplicity(0, 9999))
    }
)
findings10: BinaryAssociation = BinaryAssociation(
    name="findings10",
    ends={
        Property(name="Finding", type=assessment_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="affects11", type=assessment_Finding, multiplicity=Multiplicity(0, 9999))
    }
)
applications12: BinaryAssociation = BinaryAssociation(
    name="applications12",
    ends={
        Property(name="Applications", type=assessment_Assessment, multiplicity=Multiplicity(1, 1)),
        Property(name="assessment", type=assessment_Applications, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
findings40: BinaryAssociation = BinaryAssociation(
    name="findings40",
    ends={
        Property(name="Findings41", type=assessment_Finding, multiplicity=Multiplicity(1, 1)),
        Property(name="findings", type=assessment_Findings, multiplicity=Multiplicity(0, 1))
    }
)
affects42: BinaryAssociation = BinaryAssociation(
    name="affects42",
    ends={
        Property(name="Node44", type=assessment_Finding, multiplicity=Multiplicity(1, 1)),
        Property(name="findings43", type=assessment_Node, multiplicity=Multiplicity(0, 9999))
    }
)
accounts45: BinaryAssociation = BinaryAssociation(
    name="accounts45",
    ends={
        Property(name="Accounts", type=assessment_Account, multiplicity=Multiplicity(1, 1)),
        Property(name="accounts", type=assessment_Accounts, multiplicity=Multiplicity(0, 1))
    }
)
entitlements46: BinaryAssociation = BinaryAssociation(
    name="entitlements46",
    ends={
        Property(name="Entitlement", type=assessment_Account, multiplicity=Multiplicity(1, 1)),
        Property(name="accounts47", type=assessment_Entitlement, multiplicity=Multiplicity(0, 9999))
    }
)
accounts48: BinaryAssociation = BinaryAssociation(
    name="accounts48",
    ends={
        Property(name="Account", type=assessment_Entitlement, multiplicity=Multiplicity(1, 1)),
        Property(name="entitlements", type=assessment_Account, multiplicity=Multiplicity(0, 9999))
    }
)
entitlements49: BinaryAssociation = BinaryAssociation(
    name="entitlements49",
    ends={
        Property(name="Entitlements", type=assessment_Entitlement, multiplicity=Multiplicity(1, 1)),
        Property(name="entitlements50", type=assessment_Entitlements, multiplicity=Multiplicity(0, 1))
    }
)
sinks27: BinaryAssociation = BinaryAssociation(
    name="sinks27",
    ends={
        Property(name="assessment_Sinks", type=assessment_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="assessment_Application28", type=assessment_Sinks, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resources29: BinaryAssociation = BinaryAssociation(
    name="resources29",
    ends={
        Property(name="Resources", type=assessment_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="application30", type=assessment_Resources, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
applications31: BinaryAssociation = BinaryAssociation(
    name="applications31",
    ends={
        Property(name="Applications32", type=assessment_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="applications", type=assessment_Applications, multiplicity=Multiplicity(0, 1))
    }
)
sinks33: BinaryAssociation = BinaryAssociation(
    name="sinks33",
    ends={
        Property(name="Sinks", type=assessment_Sink, multiplicity=Multiplicity(1, 1)),
        Property(name="sinks", type=assessment_Sinks, multiplicity=Multiplicity(0, 1))
    }
)
controllers34: BinaryAssociation = BinaryAssociation(
    name="controllers34",
    ends={
        Property(name="Controllers35", type=assessment_Controller, multiplicity=Multiplicity(1, 1)),
        Property(name="controllers", type=assessment_Controllers, multiplicity=Multiplicity(0, 1))
    }
)
views36: BinaryAssociation = BinaryAssociation(
    name="views36",
    ends={
        Property(name="Views37", type=assessment_View, multiplicity=Multiplicity(1, 1)),
        Property(name="views", type=assessment_Views, multiplicity=Multiplicity(0, 1))
    }
)
models38: BinaryAssociation = BinaryAssociation(
    name="models38",
    ends={
        Property(name="Models39", type=assessment_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="models", type=assessment_Models, multiplicity=Multiplicity(0, 1))
    }
)
resources58: BinaryAssociation = BinaryAssociation(
    name="resources58",
    ends={
        Property(name="Resources59", type=assessment_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="resources", type=assessment_Resources, multiplicity=Multiplicity(0, 1))
    }
)
snippets60: BinaryAssociation = BinaryAssociation(
    name="snippets60",
    ends={
        Property(name="Snippet", type=assessment_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="resource", type=assessment_Snippet, multiplicity=Multiplicity(0, 9999))
    }
)
tasks51: BinaryAssociation = BinaryAssociation(
    name="tasks51",
    ends={
        Property(name="Tasks52", type=assessment_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="tasks", type=assessment_Tasks, multiplicity=Multiplicity(0, 1))
    }
)
affects53: BinaryAssociation = BinaryAssociation(
    name="affects53",
    ends={
        Property(name="Node55", type=assessment_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="tasks54", type=assessment_Node, multiplicity=Multiplicity(0, 9999))
    }
)
application56: BinaryAssociation = BinaryAssociation(
    name="application56",
    ends={
        Property(name="Application", type=assessment_Scm, multiplicity=Multiplicity(1, 1)),
        Property(name="scm", type=assessment_Application, multiplicity=Multiplicity(0, 1))
    }
)
resource57: BinaryAssociation = BinaryAssociation(
    name="resource57",
    ends={
        Property(name="Resource", type=assessment_Snippet, multiplicity=Multiplicity(1, 1)),
        Property(name="snippets", type=assessment_Resource, multiplicity=Multiplicity(0, 1))
    }
)
application89: BinaryAssociation = BinaryAssociation(
    name="application89",
    ends={
        Property(name="Application91", type=assessment_Models, multiplicity=Multiplicity(1, 1)),
        Property(name="models90", type=assessment_Application, multiplicity=Multiplicity(0, 1))
    }
)
models92: BinaryAssociation = BinaryAssociation(
    name="models92",
    ends={
        Property(name="Model", type=assessment_Models, multiplicity=Multiplicity(1, 1)),
        Property(name="models93", type=assessment_Model, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
application94: BinaryAssociation = BinaryAssociation(
    name="application94",
    ends={
        Property(name="Application96", type=assessment_Views, multiplicity=Multiplicity(1, 1)),
        Property(name="views95", type=assessment_Application, multiplicity=Multiplicity(0, 1))
    }
)
views97: BinaryAssociation = BinaryAssociation(
    name="views97",
    ends={
        Property(name="View", type=assessment_Views, multiplicity=Multiplicity(1, 1)),
        Property(name="views98", type=assessment_View, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
application99: BinaryAssociation = BinaryAssociation(
    name="application99",
    ends={
        Property(name="assessment_Application101", type=assessment_Sinks, multiplicity=Multiplicity(1, 1)),
        Property(name="assessment_Sinks100", type=assessment_Application, multiplicity=Multiplicity(0, 1))
    }
)
sinks102: BinaryAssociation = BinaryAssociation(
    name="sinks102",
    ends={
        Property(name="Sink", type=assessment_Sinks, multiplicity=Multiplicity(1, 1)),
        Property(name="sinks103", type=assessment_Sink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
application104: BinaryAssociation = BinaryAssociation(
    name="application104",
    ends={
        Property(name="Application106", type=assessment_Resources, multiplicity=Multiplicity(1, 1)),
        Property(name="resources105", type=assessment_Application, multiplicity=Multiplicity(0, 1))
    }
)
resources107: BinaryAssociation = BinaryAssociation(
    name="resources107",
    ends={
        Property(name="Resource109", type=assessment_Resources, multiplicity=Multiplicity(1, 1)),
        Property(name="resources108", type=assessment_Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assessment110: BinaryAssociation = BinaryAssociation(
    name="assessment110",
    ends={
        Property(name="Assessment112", type=assessment_Tasks, multiplicity=Multiplicity(1, 1)),
        Property(name="tasks111", type=assessment_Assessment, multiplicity=Multiplicity(0, 1))
    }
)
tasks113: BinaryAssociation = BinaryAssociation(
    name="tasks113",
    ends={
        Property(name="Task115", type=assessment_Tasks, multiplicity=Multiplicity(1, 1)),
        Property(name="tasks114", type=assessment_Task, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
applications61: BinaryAssociation = BinaryAssociation(
    name="applications61",
    ends={
        Property(name="Application63", type=assessment_Applications, multiplicity=Multiplicity(1, 1)),
        Property(name="applications62", type=assessment_Application, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assessment64: BinaryAssociation = BinaryAssociation(
    name="assessment64",
    ends={
        Property(name="Assessment", type=assessment_Applications, multiplicity=Multiplicity(1, 1)),
        Property(name="applications65", type=assessment_Assessment, multiplicity=Multiplicity(0, 1))
    }
)
findings66: BinaryAssociation = BinaryAssociation(
    name="findings66",
    ends={
        Property(name="Finding68", type=assessment_Findings, multiplicity=Multiplicity(1, 1)),
        Property(name="findings67", type=assessment_Finding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assessment69: BinaryAssociation = BinaryAssociation(
    name="assessment69",
    ends={
        Property(name="Assessment71", type=assessment_Findings, multiplicity=Multiplicity(1, 1)),
        Property(name="findings70", type=assessment_Assessment, multiplicity=Multiplicity(0, 1))
    }
)
application72: BinaryAssociation = BinaryAssociation(
    name="application72",
    ends={
        Property(name="assessment_Application74", type=assessment_Accounts, multiplicity=Multiplicity(1, 1)),
        Property(name="assessment_Accounts73", type=assessment_Application, multiplicity=Multiplicity(0, 1))
    }
)
accounts75: BinaryAssociation = BinaryAssociation(
    name="accounts75",
    ends={
        Property(name="Account77", type=assessment_Accounts, multiplicity=Multiplicity(1, 1)),
        Property(name="accounts76", type=assessment_Account, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
application78: BinaryAssociation = BinaryAssociation(
    name="application78",
    ends={
        Property(name="Application80", type=assessment_Controllers, multiplicity=Multiplicity(1, 1)),
        Property(name="controllers79", type=assessment_Application, multiplicity=Multiplicity(0, 1))
    }
)
controllers81: BinaryAssociation = BinaryAssociation(
    name="controllers81",
    ends={
        Property(name="Controller", type=assessment_Controllers, multiplicity=Multiplicity(1, 1)),
        Property(name="controllers82", type=assessment_Controller, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
application83: BinaryAssociation = BinaryAssociation(
    name="application83",
    ends={
        Property(name="assessment_Application85", type=assessment_Entitlements, multiplicity=Multiplicity(1, 1)),
        Property(name="assessment_Entitlements84", type=assessment_Application, multiplicity=Multiplicity(0, 1))
    }
)
entitlements86: BinaryAssociation = BinaryAssociation(
    name="entitlements86",
    ends={
        Property(name="Entitlement88", type=assessment_Entitlements, multiplicity=Multiplicity(1, 1)),
        Property(name="entitlements87", type=assessment_Entitlement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_assessment_Application_Label = Generalization(general=Label, specific=assessment_Application)
gen_assessment_Application_Notes = Generalization(general=Notes, specific=assessment_Application)
gen_assessment_Http_GraphNode = Generalization(general=GraphNode, specific=assessment_Http)
gen_assessment_Node_Label = Generalization(general=Label, specific=assessment_Node)
gen_assessment_Node_Notes = Generalization(general=Notes, specific=assessment_Node)
gen_assessment_Assessment_Label = Generalization(general=Label, specific=assessment_Assessment)
gen_assessment_Assessment_Notes = Generalization(general=Notes, specific=assessment_Assessment)
gen_assessment_Finding_Label = Generalization(general=Label, specific=assessment_Finding)
gen_assessment_Finding_Notes = Generalization(general=Notes, specific=assessment_Finding)
gen_assessment_Account_Node = Generalization(general=Node, specific=assessment_Account)
gen_assessment_Entitlement_Node = Generalization(general=Node, specific=assessment_Entitlement)
gen_assessment_Task_Label = Generalization(general=Label, specific=assessment_Task)
gen_assessment_Task_Notes = Generalization(general=Notes, specific=assessment_Task)
gen_assessment_Sink_Node = Generalization(general=Node, specific=assessment_Sink)
gen_assessment_Controller_Node = Generalization(general=Node, specific=assessment_Controller)
gen_assessment_View_Node = Generalization(general=Node, specific=assessment_View)
gen_assessment_Model_Node = Generalization(general=Node, specific=assessment_Model)
gen_assessment_Generic_GraphNode = Generalization(general=GraphNode, specific=assessment_Generic)
gen_assessment_GraphNode_Node = Generalization(general=Node, specific=assessment_GraphNode)
gen_assessment_Control_GraphNode = Generalization(general=GraphNode, specific=assessment_Control)
gen_assessment_Resource_Label = Generalization(general=Label, specific=assessment_Resource)
gen_assessment_Resource_Notes = Generalization(general=Notes, specific=assessment_Resource)
gen_assessment_Resource_Contents = Generalization(general=Contents, specific=assessment_Resource)
gen_assessment_Snippet_GraphNode = Generalization(general=GraphNode, specific=assessment_Snippet)
gen_assessment_Snippet_Contents = Generalization(general=Contents, specific=assessment_Snippet)

# Domain Model
domain_model = DomainModel(
    name="assessment",
    types={assessment_Findings, assessment_Tasks, assessment_Application, assessment_Accounts, assessment_Entitlements, assessment_Controllers, assessment_Models, assessment_Scm, assessment_Views, assessment_Http, GraphNode, assessment_Node, Label, Notes, assessment_GraphNode, assessment_Task, assessment_Finding, assessment_Assessment, assessment_Applications, assessment_Account, assessment_Entitlement, assessment_Sinks, assessment_Resources, assessment_Sink, Node, assessment_Controller, assessment_View, assessment_Model, assessment_Generic, assessment_Control, assessment_Label, assessment_Contents, assessment_Snippet, Contents, assessment_Resource, assessment_Url, assessment_Graph, assessment_Notes, Language, HttpMethod, UrlPattern, TaskStatus},
    associations={findings13, tasks15, accounts17, entitlements18, controllers20, models21, scm23, views25, children0, parent2, refersTo5, referredBy7, tasks9, findings10, applications12, findings40, affects42, accounts45, entitlements46, accounts48, entitlements49, sinks27, resources29, applications31, sinks33, controllers34, views36, models38, resources58, snippets60, tasks51, affects53, application56, resource57, application89, models92, application94, views97, application99, sinks102, application104, resources107, assessment110, tasks113, applications61, assessment64, findings66, assessment69, application72, accounts75, application78, controllers81, application83, entitlements86},
    generalizations={gen_assessment_Application_Label, gen_assessment_Application_Notes, gen_assessment_Http_GraphNode, gen_assessment_Node_Label, gen_assessment_Node_Notes, gen_assessment_Assessment_Label, gen_assessment_Assessment_Notes, gen_assessment_Finding_Label, gen_assessment_Finding_Notes, gen_assessment_Account_Node, gen_assessment_Entitlement_Node, gen_assessment_Task_Label, gen_assessment_Task_Notes, gen_assessment_Sink_Node, gen_assessment_Controller_Node, gen_assessment_View_Node, gen_assessment_Model_Node, gen_assessment_Generic_GraphNode, gen_assessment_GraphNode_Node, gen_assessment_Control_GraphNode, gen_assessment_Resource_Label, gen_assessment_Resource_Notes, gen_assessment_Resource_Contents, gen_assessment_Snippet_GraphNode, gen_assessment_Snippet_Contents},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)