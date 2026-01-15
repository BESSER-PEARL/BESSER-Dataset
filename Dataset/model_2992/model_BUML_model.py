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
model_Revision = Class(name="model::Revision")
model_Discussion = Class(name="model::Discussion")
model_VersionHistory = Class(name="model::VersionHistory")
model_Article = Class(name="model::Article")
Content = Class(name="Content")
model_Media = Class(name="model::Media")
model_Content = Class(name="model::Content")
Node = Class(name="Node")
model_Node = Class(name="model::Node", is_abstract=True)
model_User = Class(name="model::User")
model_Role = Class(name="model::Role", is_abstract=True)
model_MetaData = Class(name="model::MetaData")
model_Internal = Class(name="model::Internal")
model_AutoConfirmedUser = Class(name="model::AutoConfirmedUser")
RegisteredUser = Class(name="RegisteredUser")
model_Administrator = Class(name="model::Administrator")
AutoConfirmedUser = Class(name="AutoConfirmedUser")
model_SysOp = Class(name="model::SysOp")
Administrator = Class(name="Administrator")
model_RegisteredUser = Class(name="model::RegisteredUser")
UnregisteredUser = Class(name="UnregisteredUser")
model_Talk = Class(name="model::Talk")
model_WikiProject = Class(name="model::WikiProject")
Internal = Class(name="Internal")
model_UnregisteredUser = Class(name="model::UnregisteredUser")
Role = Class(name="Role")

# model_Revision class attributes and methods
model_Revision_creationDate: Property = Property(name="creationDate", type=StringType)
model_Revision_content: Property = Property(name="content", type=StringType)
model_Revision.attributes={model_Revision_content, model_Revision_creationDate}

# model_Discussion class attributes and methods
model_Discussion_discussions: Property = Property(name="discussions", type=StringType)
model_Discussion_m_renderHTML: Method = Method(name="renderHTML", parameters={})
model_Discussion_m_add: Method = Method(name="add", parameters={})
model_Discussion.attributes={model_Discussion_discussions}
model_Discussion.methods={model_Discussion_m_renderHTML, model_Discussion_m_add}

# model_VersionHistory class attributes and methods
model_VersionHistory_m_renderHTML: Method = Method(name="renderHTML", parameters={})
model_VersionHistory.methods={model_VersionHistory_m_renderHTML}

# model_Article class attributes and methods
model_Article_typePrefix: Property = Property(name="typePrefix", type=StringType)
model_Article_content: Property = Property(name="content", type=StringType)
model_Article.attributes={model_Article_content, model_Article_typePrefix}

# Content class attributes and methods

# model_Media class attributes and methods
model_Media_typePrefix: Property = Property(name="typePrefix", type=StringType)
model_Media_m_addContentToFileUsage: Method = Method(name="addContentToFileUsage", parameters={})
model_Media_m_removeContent: Method = Method(name="removeContent", parameters={})
model_Media_m_getFileUsage: Method = Method(name="getFileUsage", parameters={})
model_Media_m_addMetaData: Method = Method(name="addMetaData", parameters={})
model_Media_m_removeMetaData: Method = Method(name="removeMetaData", parameters={})
model_Media_m_getMetaData: Method = Method(name="getMetaData", parameters={})
model_Media.attributes={model_Media_typePrefix}
model_Media.methods={model_Media_m_removeContent, model_Media_m_addMetaData, model_Media_m_getMetaData, model_Media_m_removeMetaData, model_Media_m_getFileUsage, model_Media_m_addContentToFileUsage}

# model_Content class attributes and methods
model_Content_m_createNewRevision: Method = Method(name="createNewRevision", parameters={}, type=StringType)
model_Content_m_addDiscussionItem: Method = Method(name="addDiscussionItem", parameters={})
model_Content_m_renderHTML: Method = Method(name="renderHTML", parameters={})
model_Content_m_render: Method = Method(name="render", parameters={})
model_Content.methods={model_Content_m_renderHTML, model_Content_m_createNewRevision, model_Content_m_addDiscussionItem, model_Content_m_render}

# Node class attributes and methods

# model_Node class attributes and methods
model_Node_nodeName: Property = Property(name="nodeName", type=StringType)
model_Node_nodePrefix: Property = Property(name="nodePrefix", type=StringType)
model_Node_m_getURI: Method = Method(name="getURI", parameters={}, type=StringType)
model_Node_m_renderHTML: Method = Method(name="renderHTML", parameters={}, type=StringType)
model_Node_m_getTypePrefix: Method = Method(name="getTypePrefix", parameters={}, type=StringType)
model_Node_m_render: Method = Method(name="render", parameters={})
model_Node.attributes={model_Node_nodeName, model_Node_nodePrefix}
model_Node.methods={model_Node_m_getURI, model_Node_m_render, model_Node_m_renderHTML, model_Node_m_getTypePrefix}

# model_User class attributes and methods
model_User_isBlocked: Property = Property(name="isBlocked", type=StringType)
model_User_isReader: Property = Property(name="isReader", type=StringType)
model_User_isEditor: Property = Property(name="isEditor", type=StringType)
model_User_typePrefix: Property = Property(name="typePrefix", type=StringType)
model_User.attributes={model_User_isEditor, model_User_typePrefix, model_User_isReader, model_User_isBlocked}

# model_Role class attributes and methods

# model_MetaData class attributes and methods
model_MetaData_key: Property = Property(name="key", type=StringType)
model_MetaData_value: Property = Property(name="value", type=StringType)
model_MetaData.attributes={model_MetaData_key, model_MetaData_value}

# model_Internal class attributes and methods
model_Internal_typePrefix: Property = Property(name="typePrefix", type=StringType)
model_Internal_content: Property = Property(name="content", type=StringType)
model_Internal.attributes={model_Internal_typePrefix, model_Internal_content}

# model_AutoConfirmedUser class attributes and methods
model_AutoConfirmedUser_m_createArticle: Method = Method(name="createArticle", parameters={})
model_AutoConfirmedUser_m_moveArticle: Method = Method(name="moveArticle", parameters={})
model_AutoConfirmedUser_m_uploadMedia: Method = Method(name="uploadMedia", parameters={})
model_AutoConfirmedUser_m_moveMedia: Method = Method(name="moveMedia", parameters={})
model_AutoConfirmedUser.methods={model_AutoConfirmedUser_m_moveArticle, model_AutoConfirmedUser_m_uploadMedia, model_AutoConfirmedUser_m_moveMedia, model_AutoConfirmedUser_m_createArticle}

# RegisteredUser class attributes and methods

# model_Administrator class attributes and methods
model_Administrator_m_blockUser: Method = Method(name="blockUser", parameters={})
model_Administrator_m_deleteContent: Method = Method(name="deleteContent", parameters={})
model_Administrator.methods={model_Administrator_m_deleteContent, model_Administrator_m_blockUser}

# AutoConfirmedUser class attributes and methods

# model_SysOp class attributes and methods
model_SysOp_m_makeAdmin: Method = Method(name="makeAdmin", parameters={})
model_SysOp_m_removeAdmin: Method = Method(name="removeAdmin", parameters={})
model_SysOp_m_blockAdmin: Method = Method(name="blockAdmin", parameters={})
model_SysOp.methods={model_SysOp_m_removeAdmin, model_SysOp_m_makeAdmin, model_SysOp_m_blockAdmin}

# Administrator class attributes and methods

# model_RegisteredUser class attributes and methods

# UnregisteredUser class attributes and methods

# model_Talk class attributes and methods

# model_WikiProject class attributes and methods

# Internal class attributes and methods

# model_UnregisteredUser class attributes and methods
model_UnregisteredUser_m_changeMode: Method = Method(name="changeMode", parameters={}, type=StringType)
model_UnregisteredUser.methods={model_UnregisteredUser_m_changeMode}

# Role class attributes and methods

# Relationships
revisions0: BinaryAssociation = BinaryAssociation(
    name="revisions0",
    ends={
        Property(name="model_Revision", type=model_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Content", type=model_Revision, multiplicity=Multiplicity(1, 9999))
    }
)
discussionPage1: BinaryAssociation = BinaryAssociation(
    name="discussionPage1",
    ends={
        Property(name="model_Discussion", type=model_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Content2", type=model_Discussion, multiplicity=Multiplicity(1, 1))
    }
)
currentRevision3: BinaryAssociation = BinaryAssociation(
    name="currentRevision3",
    ends={
        Property(name="model_Revision5", type=model_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Content4", type=model_Revision, multiplicity=Multiplicity(1, 1))
    }
)
versionHistoryPage6: BinaryAssociation = BinaryAssociation(
    name="versionHistoryPage6",
    ends={
        Property(name="model_VersionHistory", type=model_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Content7", type=model_VersionHistory, multiplicity=Multiplicity(1, 1))
    }
)
role11: BinaryAssociation = BinaryAssociation(
    name="role11",
    ends={
        Property(name="model_Role", type=model_User, multiplicity=Multiplicity(1, 1)),
        Property(name="model_User", type=model_Role, multiplicity=Multiplicity(0, 1))
    }
)
usage8: BinaryAssociation = BinaryAssociation(
    name="usage8",
    ends={
        Property(name="model_Article", type=model_Media, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Media", type=model_Article, multiplicity=Multiplicity(1, 9999))
    }
)
meta9: BinaryAssociation = BinaryAssociation(
    name="meta9",
    ends={
        Property(name="model_MetaData", type=model_Media, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Media10", type=model_MetaData, multiplicity=Multiplicity(0, 9999))
    }
)
talkPage15: BinaryAssociation = BinaryAssociation(
    name="talkPage15",
    ends={
        Property(name="model_Talk", type=model_RegisteredUser, multiplicity=Multiplicity(1, 1)),
        Property(name="model_RegisteredUser", type=model_Talk, multiplicity=Multiplicity(0, 1))
    }
)
author12: BinaryAssociation = BinaryAssociation(
    name="author12",
    ends={
        Property(name="model_User14", type=model_Revision, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Revision13", type=model_User, multiplicity=Multiplicity(1, 1))
    }
)
member16: BinaryAssociation = BinaryAssociation(
    name="member16",
    ends={
        Property(name="model_User17", type=model_WikiProject, multiplicity=Multiplicity(1, 1)),
        Property(name="model_WikiProject", type=model_User, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_model_Article_Content = Generalization(general=Content, specific=model_Article)
gen_model_Media_Content = Generalization(general=Content, specific=model_Media)
gen_model_Content_Node = Generalization(general=Node, specific=model_Content)
gen_model_User_Node = Generalization(general=Node, specific=model_User)
gen_model_Internal_Content = Generalization(general=Content, specific=model_Internal)
gen_model_AutoConfirmedUser_RegisteredUser = Generalization(general=RegisteredUser, specific=model_AutoConfirmedUser)
gen_model_Administrator_AutoConfirmedUser = Generalization(general=AutoConfirmedUser, specific=model_Administrator)
gen_model_SysOp_Administrator = Generalization(general=Administrator, specific=model_SysOp)
gen_model_RegisteredUser_UnregisteredUser = Generalization(general=UnregisteredUser, specific=model_RegisteredUser)
gen_model_WikiProject_Internal = Generalization(general=Internal, specific=model_WikiProject)
gen_model_UnregisteredUser_Role = Generalization(general=Role, specific=model_UnregisteredUser)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_Revision, model_Discussion, model_VersionHistory, model_Article, Content, model_Media, model_Content, Node, model_Node, model_User, model_Role, model_MetaData, model_Internal, model_AutoConfirmedUser, RegisteredUser, model_Administrator, AutoConfirmedUser, model_SysOp, Administrator, model_RegisteredUser, UnregisteredUser, model_Talk, model_WikiProject, Internal, model_UnregisteredUser, Role},
    associations={revisions0, discussionPage1, currentRevision3, versionHistoryPage6, role11, usage8, meta9, talkPage15, author12, member16},
    generalizations={gen_model_Article_Content, gen_model_Media_Content, gen_model_Content_Node, gen_model_User_Node, gen_model_Internal_Content, gen_model_AutoConfirmedUser_RegisteredUser, gen_model_Administrator_AutoConfirmedUser, gen_model_SysOp_Administrator, gen_model_RegisteredUser_UnregisteredUser, gen_model_WikiProject_Internal, gen_model_UnregisteredUser_Role},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)