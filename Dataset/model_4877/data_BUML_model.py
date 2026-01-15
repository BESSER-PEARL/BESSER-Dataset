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
data_Person = Class(name="data::Person")
InformationObject = Class(name="InformationObject")
data_Organisation = Class(name="data::Organisation")
data_Content = Class(name="data::Content")
data_Ranking = Class(name="data::Ranking", is_abstract=True)
data_InformationObject = Class(name="data::InformationObject", is_abstract=True)
Item = Class(name="Item")
data_Category = Class(name="data::Category")
data_Tag = Class(name="data::Tag")
data_Image = Class(name="data::Image")
data_StarRanking = Class(name="data::StarRanking")
data_ThumbRanking = Class(name="data::ThumbRanking")
data_ViewRanking = Class(name="data::ViewRanking")
data_Connection = Class(name="data::Connection")
data_Binary = Class(name="data::Binary")
data_MetaInformation = Class(name="data::MetaInformation")
data_Document = Class(name="data::Document")
data_Transformation = Class(name="data::Transformation")
data_Video = Class(name="data::Video")
data_DataSet = Class(name="data::DataSet")
data_Item = Class(name="data::Item", is_abstract=True)
data_Mashup = Class(name="data::Mashup")
data_MetaTag = Class(name="data::MetaTag")
data_Identifier = Class(name="data::Identifier")
data_Extension = Class(name="data::Extension", is_abstract=True)
data_Classification = Class(name="data::Classification", is_abstract=True)
Classification = Class(name="Classification")
data_Phone = Class(name="data::Phone")
MetaInformation = Class(name="MetaInformation")
data_InstantMessenger = Class(name="data::InstantMessenger")
data_Email = Class(name="data::Email")
data_WebSite = Class(name="data::WebSite")
Extension = Class(name="Extension")
data_Attachment = Class(name="data::Attachment", is_abstract=True)
data_Location = Class(name="data::Location")
data_IndoorLocation = Class(name="data::IndoorLocation")
Attachment = Class(name="Attachment")
Ranking = Class(name="Ranking")
data_WebAccount = Class(name="data::WebAccount")
data_Event = Class(name="data::Event")

# data_Person class attributes and methods
data_Person_lastname: Property = Property(name="lastname", type=StringType)
data_Person_firstname: Property = Property(name="firstname", type=StringType)
data_Person_dateOfBirth: Property = Property(name="dateOfBirth", type=DateType)
data_Person_title: Property = Property(name="title", type=StringType)
data_Person_m_getContents: Method = Method(name="getContents", parameters={}, type=StringType)
data_Person_m_addAuthoredContent: Method = Method(name="addAuthoredContent", parameters={Parameter(name='authoredContent')}, type=StringType)
data_Person_m_parseFirstName: Method = Method(name="parseFirstName", parameters={}, type=StringType)
data_Person_m_parseLastName: Method = Method(name="parseLastName", parameters={}, type=StringType)
data_Person_m_getOrganisations: Method = Method(name="getOrganisations", parameters={}, type=StringType)
data_Person_m_addContributedContent: Method = Method(name="addContributedContent", parameters={Parameter(name='contributedContent')}, type=StringType)
data_Person.attributes={data_Person_title, data_Person_firstname, data_Person_lastname, data_Person_dateOfBirth}
data_Person.methods={data_Person_m_parseLastName, data_Person_m_parseFirstName, data_Person_m_getOrganisations, data_Person_m_addContributedContent, data_Person_m_getContents, data_Person_m_addAuthoredContent}

# InformationObject class attributes and methods

# data_Organisation class attributes and methods
data_Organisation_m_getPersons: Method = Method(name="getPersons", parameters={}, type=StringType)
data_Organisation_m_getContents: Method = Method(name="getContents", parameters={}, type=StringType)
data_Organisation_m_addParticipant: Method = Method(name="addParticipant", parameters={Parameter(name='participant')}, type=StringType)
data_Organisation.methods={data_Organisation_m_getPersons, data_Organisation_m_getContents, data_Organisation_m_addParticipant}

# data_Content class attributes and methods
data_Content_locale: Property = Property(name="locale", type=StringType)
data_Content_m_getOrganisations: Method = Method(name="getOrganisations", parameters={}, type=StringType)
data_Content_m_getPersons: Method = Method(name="getPersons", parameters={}, type=StringType)
data_Content_m_comment: Method = Method(name="comment", parameters={Parameter(name='comment')}, type=StringType)
data_Content_m_addContributor: Method = Method(name="addContributor", parameters={Parameter(name='contributor')}, type=StringType)
data_Content_m_attachDocument: Method = Method(name="attachDocument", parameters={Parameter(name='fileUrl')}, type=StringType)
data_Content.attributes={data_Content_locale}
data_Content.methods={data_Content_m_getOrganisations, data_Content_m_getPersons, data_Content_m_comment, data_Content_m_addContributor, data_Content_m_attachDocument}

# data_Ranking class attributes and methods
data_Ranking_date: Property = Property(name="date", type=DateType)
data_Ranking.attributes={data_Ranking_date}

# data_InformationObject class attributes and methods
data_InformationObject_name: Property = Property(name="name", type=StringType)
data_InformationObject_m_tag: Method = Method(name="tag", parameters={Parameter(name='name')}, type=StringType)
data_InformationObject_m_categorize: Method = Method(name="categorize", parameters={Parameter(name='name')}, type=StringType)
data_InformationObject_m_attachImage: Method = Method(name="attachImage", parameters={Parameter(name='imageUrl')}, type=StringType)
data_InformationObject_m_getAttachments: Method = Method(name="getAttachments", parameters={}, type=StringType)
data_InformationObject_m_starRank: Method = Method(name="starRank", parameters={Parameter(name='stars'), Parameter(name='ofStars')}, type=StringType)
data_InformationObject_m_view: Method = Method(name="view", parameters={}, type=StringType)
data_InformationObject_m_thumbsUp: Method = Method(name="thumbsUp", parameters={}, type=StringType)
data_InformationObject_m_thumbsDown: Method = Method(name="thumbsDown", parameters={}, type=StringType)
data_InformationObject_m_getThumbsUp: Method = Method(name="getThumbsUp", parameters={}, type=StringType)
data_InformationObject_m_getThumbsDown: Method = Method(name="getThumbsDown", parameters={}, type=StringType)
data_InformationObject_m_getInformationObjectsConnectedFrom: Method = Method(name="getInformationObjectsConnectedFrom", parameters={}, type=InformationObject)
data_InformationObject_m_getThumbsUpCount: Method = Method(name="getThumbsUpCount", parameters={}, type=StringType)
data_InformationObject_m_getThumbsDownCount: Method = Method(name="getThumbsDownCount", parameters={}, type=StringType)
data_InformationObject_m_getThumbsCount: Method = Method(name="getThumbsCount", parameters={}, type=StringType)
data_InformationObject_m_getViewsCount: Method = Method(name="getViewsCount", parameters={}, type=StringType)
data_InformationObject_m_getStarRanking: Method = Method(name="getStarRanking", parameters={}, type=StringType)
data_InformationObject_m_extend: Method = Method(name="extend", parameters={Parameter(name='metaInformation')}, type=StringType)
data_InformationObject_m_getWebAccounts: Method = Method(name="getWebAccounts", parameters={}, type=StringType)
data_InformationObject_m_getWebSites: Method = Method(name="getWebSites", parameters={}, type=StringType)
data_InformationObject_m_getPhones: Method = Method(name="getPhones", parameters={}, type=StringType)
data_InformationObject_m_getLocations: Method = Method(name="getLocations", parameters={}, type=StringType)
data_InformationObject_m_getEmails: Method = Method(name="getEmails", parameters={}, type=StringType)
data_InformationObject_m_getInstantMessengers: Method = Method(name="getInstantMessengers", parameters={}, type=StringType)
data_InformationObject_m_addEmailAddress: Method = Method(name="addEmailAddress", parameters={Parameter(name='emailAdress')}, type=StringType)
data_InformationObject_m_addWebSite: Method = Method(name="addWebSite", parameters={Parameter(name='url')}, type=StringType)
data_InformationObject_m_getInformationObjectsWithCommonTags: Method = Method(name="getInformationObjectsWithCommonTags", parameters={}, type=InformationObject)
data_InformationObject_m_addWebAccount: Method = Method(name="addWebAccount", parameters={Parameter(name='username')}, type=StringType)
data_InformationObject_m_hasImages: Method = Method(name="hasImages", parameters={}, type=StringType)
data_InformationObject_m_getInformationObjectsConnectedTo: Method = Method(name="getInformationObjectsConnectedTo", parameters={}, type=InformationObject)
data_InformationObject_m_getInformationObjectsConnected: Method = Method(name="getInformationObjectsConnected", parameters={}, type=InformationObject)
data_InformationObject_m_connectTo: Method = Method(name="connectTo", parameters={Parameter(name='informationObject')}, type=StringType)
data_InformationObject_m_connectToWithMetaTag: Method = Method(name="connectToWithMetaTag", parameters={Parameter(name='metaTag'), Parameter(name='informationObject')}, type=StringType)
data_InformationObject_m_getInformationObjectsConnectedToWithMetaTag: Method = Method(name="getInformationObjectsConnectedToWithMetaTag", parameters={Parameter(name='metaTag')}, type=InformationObject)
data_InformationObject_m_getInformationObjectsConnectedFromWithMetaTag: Method = Method(name="getInformationObjectsConnectedFromWithMetaTag", parameters={Parameter(name='metaTag')}, type=InformationObject)
data_InformationObject_m_getInformationObjectsConnectedWithMetaTag: Method = Method(name="getInformationObjectsConnectedWithMetaTag", parameters={Parameter(name='metaTag')}, type=InformationObject)
data_InformationObject_m_getConnectionsFrom: Method = Method(name="getConnectionsFrom", parameters={Parameter(name='informationObject')}, type=StringType)
data_InformationObject_m_getConnectionsTo: Method = Method(name="getConnectionsTo", parameters={Parameter(name='informationObject')}, type=StringType)
data_InformationObject_m_connectToWithValueAndMetaTag: Method = Method(name="connectToWithValueAndMetaTag", parameters={Parameter(name='value'), Parameter(name='informationObject'), Parameter(name='metaTag')}, type=StringType)
data_InformationObject_m_getConnectionTo: Method = Method(name="getConnectionTo", parameters={Parameter(name='informationObject'), Parameter(name='value')}, type=StringType)
data_InformationObject_m_getConnectionFrom: Method = Method(name="getConnectionFrom", parameters={Parameter(name='informationObject'), Parameter(name='value')}, type=StringType)
data_InformationObject_m_getAttachmentWithUrl: Method = Method(name="getAttachmentWithUrl", parameters={Parameter(name='url')}, type=StringType)
data_InformationObject_m_getAttachedImageWithUrl: Method = Method(name="getAttachedImageWithUrl", parameters={Parameter(name='url')}, type=StringType)
data_InformationObject_m_addPhone: Method = Method(name="addPhone", parameters={Parameter(name='phoneNumber')}, type=StringType)
data_InformationObject_m_getContentsWithCommonTags: Method = Method(name="getContentsWithCommonTags", parameters={}, type=StringType)
data_InformationObject_m_getPersonsWithCommonTags: Method = Method(name="getPersonsWithCommonTags", parameters={}, type=StringType)
data_InformationObject_m_unTag: Method = Method(name="unTag", parameters={Parameter(name='name')}, type=StringType)
data_InformationObject_m_unCategorize: Method = Method(name="unCategorize", parameters={Parameter(name='name')}, type=StringType)
data_InformationObject_m_getSlugName: Method = Method(name="getSlugName", parameters={}, type=StringType)
data_InformationObject_m_getConnectionsToWithMetaTag: Method = Method(name="getConnectionsToWithMetaTag", parameters={Parameter(name='informationObject'), Parameter(name='metaTag')}, type=StringType)
data_InformationObject_m_getConnectionsFromWithMetaTag: Method = Method(name="getConnectionsFromWithMetaTag", parameters={Parameter(name='metaTag'), Parameter(name='informationObject')}, type=StringType)
data_InformationObject_m_getOrganisationsWithCommonTags: Method = Method(name="getOrganisationsWithCommonTags", parameters={}, type=StringType)
data_InformationObject.attributes={data_InformationObject_name}
data_InformationObject.methods={data_InformationObject_m_getEmails, data_InformationObject_m_getPhones, data_InformationObject_m_getConnectionsTo, data_InformationObject_m_getConnectionFrom, data_InformationObject_m_getWebSites, data_InformationObject_m_thumbsUp, data_InformationObject_m_getInformationObjectsConnected, data_InformationObject_m_getLocations, data_InformationObject_m_tag, data_InformationObject_m_getPersonsWithCommonTags, data_InformationObject_m_extend, data_InformationObject_m_connectToWithMetaTag, data_InformationObject_m_getThumbsDownCount, data_InformationObject_m_getInformationObjectsConnectedWithMetaTag, data_InformationObject_m_getThumbsUpCount, data_InformationObject_m_getOrganisationsWithCommonTags, data_InformationObject_m_getThumbsUp, data_InformationObject_m_hasImages, data_InformationObject_m_getInformationObjectsConnectedToWithMetaTag, data_InformationObject_m_starRank, data_InformationObject_m_getConnectionTo, data_InformationObject_m_getWebAccounts, data_InformationObject_m_unCategorize, data_InformationObject_m_connectTo, data_InformationObject_m_getInformationObjectsConnectedTo, data_InformationObject_m_getSlugName, data_InformationObject_m_getThumbsCount, data_InformationObject_m_addWebAccount, data_InformationObject_m_addPhone, data_InformationObject_m_getAttachments, data_InformationObject_m_getInstantMessengers, data_InformationObject_m_getConnectionsToWithMetaTag, data_InformationObject_m_getInformationObjectsWithCommonTags, data_InformationObject_m_unTag, data_InformationObject_m_thumbsDown, data_InformationObject_m_addEmailAddress, data_InformationObject_m_getAttachedImageWithUrl, data_InformationObject_m_getStarRanking, data_InformationObject_m_view, data_InformationObject_m_getConnectionsFromWithMetaTag, data_InformationObject_m_attachImage, data_InformationObject_m_connectToWithValueAndMetaTag, data_InformationObject_m_getContentsWithCommonTags, data_InformationObject_m_getInformationObjectsConnectedFromWithMetaTag, data_InformationObject_m_getThumbsDown, data_InformationObject_m_getConnectionsFrom, data_InformationObject_m_addWebSite, data_InformationObject_m_getInformationObjectsConnectedFrom, data_InformationObject_m_categorize, data_InformationObject_m_getAttachmentWithUrl, data_InformationObject_m_getViewsCount}

# Item class attributes and methods

# data_Category class attributes and methods

# data_Tag class attributes and methods

# data_Image class attributes and methods

# data_StarRanking class attributes and methods
data_StarRanking_normalizedValue: Property = Property(name="normalizedValue", type=StringType)
data_StarRanking.attributes={data_StarRanking_normalizedValue}

# data_ThumbRanking class attributes and methods
data_ThumbRanking_m_isThumbUp: Method = Method(name="isThumbUp", parameters={}, type=StringType)
data_ThumbRanking_m_isThumbDown: Method = Method(name="isThumbDown", parameters={}, type=StringType)
data_ThumbRanking.methods={data_ThumbRanking_m_isThumbDown, data_ThumbRanking_m_isThumbUp}

# data_ViewRanking class attributes and methods

# data_Connection class attributes and methods

# data_Binary class attributes and methods
data_Binary_bytes: Property = Property(name="bytes", type=StringType)
data_Binary.attributes={data_Binary_bytes}

# data_MetaInformation class attributes and methods

# data_Document class attributes and methods

# data_Transformation class attributes and methods

# data_Video class attributes and methods

# data_DataSet class attributes and methods
data_DataSet_cacheFolder: Property = Property(name="cacheFolder", type=StringType)
data_DataSet_cacheFileAttachements: Property = Property(name="cacheFileAttachements", type=StringType)
data_DataSet_lastModified: Property = Property(name="lastModified", type=DateType)
data_DataSet_logLevel: Property = Property(name="logLevel", type=StringType)
data_DataSet_identCounter: Property = Property(name="identCounter", type=StringType)
data_DataSet_identPrefix: Property = Property(name="identPrefix", type=StringType)
data_DataSet_created: Property = Property(name="created", type=DateType)
data_DataSet_m_getCategory: Method = Method(name="getCategory", parameters={Parameter(name='name')}, type=StringType)
data_DataSet_m_add: Method = Method(name="add", parameters={Parameter(name='item')}, type=Item)
data_DataSet_m_getItemsWithStringValue: Method = Method(name="getItemsWithStringValue", parameters={Parameter(name='stringValue')}, type=Item)
data_DataSet_m_getPersonsWithName: Method = Method(name="getPersonsWithName", parameters={Parameter(name='name')}, type=StringType)
data_DataSet_m_getPersonsWithLastname: Method = Method(name="getPersonsWithLastname", parameters={Parameter(name='lastname')}, type=StringType)
data_DataSet_m_getPersonsWithFirstName: Method = Method(name="getPersonsWithFirstName", parameters={Parameter(name='firstname')}, type=StringType)
data_DataSet_m_getTag: Method = Method(name="getTag", parameters={Parameter(name='name')}, type=StringType)
data_DataSet_m_getMetaTag: Method = Method(name="getMetaTag", parameters={Parameter(name='name')}, type=StringType)
data_DataSet_m_getAllPersons: Method = Method(name="getAllPersons", parameters={}, type=StringType)
data_DataSet_m_getAllContents: Method = Method(name="getAllContents", parameters={}, type=StringType)
data_DataSet_m_getAllOrganisations: Method = Method(name="getAllOrganisations", parameters={}, type=StringType)
data_DataSet_m_getInformationObjectsWithAllTags: Method = Method(name="getInformationObjectsWithAllTags", parameters={Parameter(name='tags')}, type=InformationObject)
data_DataSet_m_getAllTags: Method = Method(name="getAllTags", parameters={}, type=StringType)
data_DataSet_m_getAllCategories: Method = Method(name="getAllCategories", parameters={}, type=StringType)
data_DataSet_m_getItemsModifiedSince: Method = Method(name="getItemsModifiedSince", parameters={Parameter(name='date')}, type=Item)
data_DataSet_m_getAllMetaTags: Method = Method(name="getAllMetaTags", parameters={}, type=StringType)
data_DataSet_m_getAllConnections: Method = Method(name="getAllConnections", parameters={}, type=StringType)
data_DataSet_m_log: Method = Method(name="log", parameters={Parameter(name='message')})
data_DataSet_m_log: Method = Method(name="log", parameters={Parameter(name='level'), Parameter(name='message')})
data_DataSet_m_getContentWithIdent: Method = Method(name="getContentWithIdent", parameters={Parameter(name='ident')}, type=StringType)
data_DataSet_m_getPersonWithIdent: Method = Method(name="getPersonWithIdent", parameters={Parameter(name='ident')}, type=StringType)
data_DataSet_m_getOrganisationWithIdent: Method = Method(name="getOrganisationWithIdent", parameters={Parameter(name='ident')}, type=StringType)
data_DataSet_m_getAttachmentWithIdent: Method = Method(name="getAttachmentWithIdent", parameters={Parameter(name='ident')}, type=StringType)
data_DataSet_m_getInformationObjectsWithAllCategories: Method = Method(name="getInformationObjectsWithAllCategories", parameters={Parameter(name='categories')}, type=InformationObject)
data_DataSet_m_getInformationObjectsWithOneOfCategories: Method = Method(name="getInformationObjectsWithOneOfCategories", parameters={Parameter(name='categories')}, type=InformationObject)
data_DataSet_m_getContentsWithAllCategories: Method = Method(name="getContentsWithAllCategories", parameters={Parameter(name='categories')}, type=StringType)
data_DataSet_m_getContentsWithOneOfCategories: Method = Method(name="getContentsWithOneOfCategories", parameters={Parameter(name='categories')}, type=StringType)
data_DataSet_m_getPersonsWithAllCategories: Method = Method(name="getPersonsWithAllCategories", parameters={Parameter(name='categories')}, type=StringType)
data_DataSet_m_getPersonsWithOneOfCategories: Method = Method(name="getPersonsWithOneOfCategories", parameters={Parameter(name='categories')}, type=StringType)
data_DataSet_m_getOrganisationsWithAllCategories: Method = Method(name="getOrganisationsWithAllCategories", parameters={Parameter(name='categories')}, type=StringType)
data_DataSet_m_getOrganisationsWithOneOfCategories: Method = Method(name="getOrganisationsWithOneOfCategories", parameters={Parameter(name='categories')}, type=StringType)
data_DataSet_m_getContents: Method = Method(name="getContents", parameters={}, type=StringType)
data_DataSet_m_getInformationObjectsWithOneOfTags: Method = Method(name="getInformationObjectsWithOneOfTags", parameters={Parameter(name='tags')}, type=InformationObject)
data_DataSet_m_getOrganisationsWithAllTags: Method = Method(name="getOrganisationsWithAllTags", parameters={Parameter(name='tags')}, type=StringType)
data_DataSet_m_getOrganisationsWithOneOfTags: Method = Method(name="getOrganisationsWithOneOfTags", parameters={Parameter(name='tags')}, type=StringType)
data_DataSet_m_getPersonsWithAllTags: Method = Method(name="getPersonsWithAllTags", parameters={Parameter(name='tags')}, type=StringType)
data_DataSet_m_getPersonsWithOneOfTags: Method = Method(name="getPersonsWithOneOfTags", parameters={Parameter(name='tags')}, type=StringType)
data_DataSet_m_getContentsWithAllTags: Method = Method(name="getContentsWithAllTags", parameters={Parameter(name='tags')}, type=StringType)
data_DataSet_m_getContentsWithOneOfTags: Method = Method(name="getContentsWithOneOfTags", parameters={Parameter(name='tags')}, type=StringType)
data_DataSet_m_getContentsWithName: Method = Method(name="getContentsWithName", parameters={Parameter(name='name')}, type=StringType)
data_DataSet_m_getOrganisationsWithName: Method = Method(name="getOrganisationsWithName", parameters={Parameter(name='name')}, type=StringType)
data_DataSet_m_getItemsWithAllMetaTags: Method = Method(name="getItemsWithAllMetaTags", parameters={Parameter(name='tags')}, type=Item)
data_DataSet_m_getItemsWithOneOfMetaTags: Method = Method(name="getItemsWithOneOfMetaTags", parameters={Parameter(name='tags')}, type=Item)
data_DataSet_m_getPersons: Method = Method(name="getPersons", parameters={}, type=StringType)
data_DataSet_m_getOrganisations: Method = Method(name="getOrganisations", parameters={}, type=StringType)
data_DataSet_m_getStarRankings: Method = Method(name="getStarRankings", parameters={}, type=StringType)
data_DataSet_m_getInformationObjects: Method = Method(name="getInformationObjects", parameters={}, type=InformationObject)
data_DataSet_m_getTags: Method = Method(name="getTags", parameters={}, type=StringType)
data_DataSet_m_getMetaTags: Method = Method(name="getMetaTags", parameters={}, type=StringType)
data_DataSet_m_getAttachments: Method = Method(name="getAttachments", parameters={}, type=StringType)
data_DataSet_m_getBinaries: Method = Method(name="getBinaries", parameters={}, type=StringType)
data_DataSet_m_getCategories: Method = Method(name="getCategories", parameters={}, type=StringType)
data_DataSet_m_getClassifications: Method = Method(name="getClassifications", parameters={}, type=StringType)
data_DataSet_m_getConnections: Method = Method(name="getConnections", parameters={}, type=StringType)
data_DataSet_m_getDocuments: Method = Method(name="getDocuments", parameters={}, type=StringType)
data_DataSet_m_getEmails: Method = Method(name="getEmails", parameters={}, type=StringType)
data_DataSet_m_getExtensions: Method = Method(name="getExtensions", parameters={}, type=StringType)
data_DataSet_m_getImages: Method = Method(name="getImages", parameters={}, type=StringType)
data_DataSet_m_getInstantMessengers: Method = Method(name="getInstantMessengers", parameters={}, type=StringType)
data_DataSet_m_getLocations: Method = Method(name="getLocations", parameters={}, type=StringType)
data_DataSet_m_getMetaInformations: Method = Method(name="getMetaInformations", parameters={}, type=StringType)
data_DataSet_m_getPhones: Method = Method(name="getPhones", parameters={}, type=StringType)
data_DataSet_m_getRankings: Method = Method(name="getRankings", parameters={}, type=StringType)
data_DataSet_m_getContentWithIdentifier: Method = Method(name="getContentWithIdentifier", parameters={Parameter(name='key'), Parameter(name='value')}, type=StringType)
data_DataSet_m_getThumbRankings: Method = Method(name="getThumbRankings", parameters={}, type=StringType)
data_DataSet_m_getTransformations: Method = Method(name="getTransformations", parameters={}, type=StringType)
data_DataSet_m_getVideos: Method = Method(name="getVideos", parameters={}, type=StringType)
data_DataSet_m_getViewRankings: Method = Method(name="getViewRankings", parameters={}, type=StringType)
data_DataSet_m_getWebAccounts: Method = Method(name="getWebAccounts", parameters={}, type=StringType)
data_DataSet_m_getWebSites: Method = Method(name="getWebSites", parameters={}, type=StringType)
data_DataSet_m_getInformationObjectsWithAllMetaTags: Method = Method(name="getInformationObjectsWithAllMetaTags", parameters={Parameter(name='tags')}, type=InformationObject)
data_DataSet_m_getInformationObjectsWithOneOfMetaTags: Method = Method(name="getInformationObjectsWithOneOfMetaTags", parameters={Parameter(name='tags')}, type=InformationObject)
data_DataSet_m_getIdentifiers: Method = Method(name="getIdentifiers", parameters={}, type=StringType)
data_DataSet_m_getIdentifiersWithKey: Method = Method(name="getIdentifiersWithKey", parameters={Parameter(name='key')}, type=StringType)
data_DataSet_m_getIdentifierWithKeyValue: Method = Method(name="getIdentifierWithKeyValue", parameters={Parameter(name='value'), Parameter(name='key')}, type=StringType)
data_DataSet_m_getItemWithIdentifier: Method = Method(name="getItemWithIdentifier", parameters={Parameter(name='value'), Parameter(name='key')}, type=Item)
data_DataSet_m_getPersonWithIdentifier: Method = Method(name="getPersonWithIdentifier", parameters={Parameter(name='key'), Parameter(name='value')}, type=StringType)
data_DataSet_m_getOrganisationWithIdentifier: Method = Method(name="getOrganisationWithIdentifier", parameters={Parameter(name='key'), Parameter(name='value')}, type=StringType)
data_DataSet_m_getLocationWithIdentifier: Method = Method(name="getLocationWithIdentifier", parameters={Parameter(name='value'), Parameter(name='key')}, type=StringType)
data_DataSet_m_getIndoorLocationWithIdentifier: Method = Method(name="getIndoorLocationWithIdentifier", parameters={Parameter(name='value'), Parameter(name='key')}, type=StringType)
data_DataSet_m_getImageWithIdentifier: Method = Method(name="getImageWithIdentifier", parameters={Parameter(name='key'), Parameter(name='value')}, type=StringType)
data_DataSet_m_getEmptyItemWithIdent: Method = Method(name="getEmptyItemWithIdent", parameters={Parameter(name='ident')}, type=Item)
data_DataSet_m_getTagsWithMoreThanXInformationObjects: Method = Method(name="getTagsWithMoreThanXInformationObjects", parameters={Parameter(name='x')}, type=StringType)
data_DataSet_m_getItemsCreatedSince: Method = Method(name="getItemsCreatedSince", parameters={Parameter(name='date')}, type=Item)
data_DataSet_m_searchItems: Method = Method(name="searchItems", parameters={Parameter(name='term')}, type=Item)
data_DataSet_m_searchInformationObjects: Method = Method(name="searchInformationObjects", parameters={Parameter(name='term')}, type=InformationObject)
data_DataSet_m_getInformationObjectsWithAttachment: Method = Method(name="getInformationObjectsWithAttachment", parameters={Parameter(name='attachment')}, type=InformationObject)
data_DataSet_m_getPersonsWithAttachment: Method = Method(name="getPersonsWithAttachment", parameters={Parameter(name='attachment')}, type=StringType)
data_DataSet_m_getOrganisationsWithAttachment: Method = Method(name="getOrganisationsWithAttachment", parameters={Parameter(name='attachment')}, type=StringType)
data_DataSet_m_getContentsWithAttachment: Method = Method(name="getContentsWithAttachment", parameters={Parameter(name='attachment')}, type=StringType)
data_DataSet_m_getEqualItem: Method = Method(name="getEqualItem", parameters={Parameter(name='item')}, type=Item)
data_DataSet_m_hasEqualItem: Method = Method(name="hasEqualItem", parameters={Parameter(name='item')}, type=StringType)
data_DataSet_m_getItemsWithIdent: Method = Method(name="getItemsWithIdent", parameters={Parameter(name='ident')}, type=Item)
data_DataSet_m_getAttachmentsWithCachedFileName: Method = Method(name="getAttachmentsWithCachedFileName", parameters={Parameter(name='cachedFileName')}, type=StringType)
data_DataSet_m_getEventsAfter: Method = Method(name="getEventsAfter", parameters={Parameter(name='date')}, type=StringType)
data_DataSet_m_getEventsBefore: Method = Method(name="getEventsBefore", parameters={Parameter(name='date')}, type=StringType)
data_DataSet_m_getEventsBetweenDates: Method = Method(name="getEventsBetweenDates", parameters={Parameter(name='after'), Parameter(name='before')}, type=StringType)
data_DataSet_m_getSpicynodesRepresentation: Method = Method(name="getSpicynodesRepresentation", parameters={}, type=StringType)
data_DataSet_m_getConnectionsBetweenInformationObjectsOfDifferentCategories: Method = Method(name="getConnectionsBetweenInformationObjectsOfDifferentCategories", parameters={}, type=StringType)
data_DataSet_m_getRandomXInformationObjects: Method = Method(name="getRandomXInformationObjects", parameters={Parameter(name='x')}, type=InformationObject)
data_DataSet_m_getInformationObjectsModifiedSince: Method = Method(name="getInformationObjectsModifiedSince", parameters={Parameter(name='date')}, type=InformationObject)
data_DataSet_m_getRandomXContents: Method = Method(name="getRandomXContents", parameters={Parameter(name='x')}, type=StringType)
data_DataSet_m_getRandomXPersons: Method = Method(name="getRandomXPersons", parameters={Parameter(name='x')}, type=StringType)
data_DataSet_m_getRandomXOrganisations: Method = Method(name="getRandomXOrganisations", parameters={Parameter(name='x')}, type=StringType)
data_DataSet_m_forceAdd: Method = Method(name="forceAdd", parameters={Parameter(name='item')}, type=Item)
data_DataSet_m_getIdentsOfExistingItems: Method = Method(name="getIdentsOfExistingItems", parameters={}, type=StringType)
data_DataSet_m_getCategoryWithSlug: Method = Method(name="getCategoryWithSlug", parameters={Parameter(name='slug')}, type=StringType)
data_DataSet_m_rebuildIndexes: Method = Method(name="rebuildIndexes", parameters={})
data_DataSet_m_getContentsWithAllMetaTags: Method = Method(name="getContentsWithAllMetaTags", parameters={Parameter(name='tags')}, type=StringType)
data_DataSet_m_getContentsWithOneOfMetaTags: Method = Method(name="getContentsWithOneOfMetaTags", parameters={Parameter(name='tags')}, type=StringType)
data_DataSet_m_getPersonsWithAllMetaTags: Method = Method(name="getPersonsWithAllMetaTags", parameters={Parameter(name='tags')}, type=StringType)
data_DataSet_m_getPersonsWithOneOfMetaTags: Method = Method(name="getPersonsWithOneOfMetaTags", parameters={Parameter(name='tags')}, type=StringType)
data_DataSet_m_getOrganisationsWithAllMetaTags: Method = Method(name="getOrganisationsWithAllMetaTags", parameters={Parameter(name='tags')}, type=StringType)
data_DataSet_m_getEvents: Method = Method(name="getEvents", parameters={}, type=StringType)
data_DataSet_m_searchByQuery: Method = Method(name="searchByQuery", parameters={Parameter(name='query')}, type=Item)
data_DataSet_m_getOrganisationsWithOneOfMetaTags: Method = Method(name="getOrganisationsWithOneOfMetaTags", parameters={Parameter(name='tags')}, type=StringType)
data_DataSet.attributes={data_DataSet_lastModified, data_DataSet_cacheFileAttachements, data_DataSet_created, data_DataSet_cacheFolder, data_DataSet_logLevel, data_DataSet_identPrefix, data_DataSet_identCounter}
data_DataSet.methods={data_DataSet_m_getExtensions, data_DataSet_m_getPersonsWithOneOfTags, data_DataSet_m_getMetaInformations, data_DataSet_m_getInformationObjectsWithAttachment, data_DataSet_m_getTransformations, data_DataSet_m_getItemsCreatedSince, data_DataSet_m_getContentsWithAllMetaTags, data_DataSet_m_getImageWithIdentifier, data_DataSet_m_getAllConnections, data_DataSet_m_hasEqualItem, data_DataSet_m_getOrganisationsWithOneOfMetaTags, data_DataSet_m_getIdentifiers, data_DataSet_m_getCategoryWithSlug, data_DataSet_m_getOrganisationsWithAllMetaTags, data_DataSet_m_getContentsWithOneOfTags, data_DataSet_m_getAllContents, data_DataSet_m_getInformationObjectsWithOneOfMetaTags, data_DataSet_m_getThumbRankings, data_DataSet_m_getAllOrganisations, data_DataSet_m_getInstantMessengers, data_DataSet_m_getVideos, data_DataSet_m_getPhones, data_DataSet_m_getContentWithIdent, data_DataSet_m_getItemsModifiedSince, data_DataSet_m_getEventsAfter, data_DataSet_m_searchItems, data_DataSet_m_getContentsWithAllTags, data_DataSet_m_add, data_DataSet_m_getPersonWithIdentifier, data_DataSet_m_getAllPersons, data_DataSet_m_rebuildIndexes, data_DataSet_m_getRandomXOrganisations, data_DataSet_m_getEqualItem, data_DataSet_m_getWebAccounts, data_DataSet_m_forceAdd, data_DataSet_m_getOrganisationsWithOneOfTags, data_DataSet_m_getAttachments, data_DataSet_m_getAllMetaTags, data_DataSet_m_getOrganisationsWithAttachment, data_DataSet_m_getPersonsWithFirstName, data_DataSet_m_getOrganisationWithIdentifier, data_DataSet_m_getImages, data_DataSet_m_getContentWithIdentifier, data_DataSet_m_getCategory, data_DataSet_m_getIdentsOfExistingItems, data_DataSet_m_getPersonsWithName, data_DataSet_m_getAttachmentWithIdent, data_DataSet_m_getItemsWithStringValue, data_DataSet_m_getWebSites, data_DataSet_m_getItemsWithAllMetaTags, data_DataSet_m_getBinaries, data_DataSet_m_getContentsWithName, data_DataSet_m_getInformationObjectsWithAllMetaTags, data_DataSet_m_getPersonsWithOneOfCategories, data_DataSet_m_getOrganisationWithIdent, data_DataSet_m_getInformationObjectsWithAllCategories, data_DataSet_m_getPersonsWithAllMetaTags, data_DataSet_m_getRankings, data_DataSet_m_getAllTags, data_DataSet_m_getPersonsWithLastname, data_DataSet_m_getEventsBetweenDates, data_DataSet_m_getAttachmentsWithCachedFileName, data_DataSet_m_getSpicynodesRepresentation, data_DataSet_m_getIndoorLocationWithIdentifier, data_DataSet_m_getContentsWithOneOfCategories, data_DataSet_m_getTags, data_DataSet_m_log, data_DataSet_m_getOrganisations, data_DataSet_m_getEventsBefore, data_DataSet_m_getClassifications, data_DataSet_m_getLocationWithIdentifier, data_DataSet_m_getPersonsWithAllCategories, data_DataSet_m_getRandomXContents, data_DataSet_m_getMetaTags, data_DataSet_m_getDocuments, data_DataSet_m_getPersonsWithAllTags, data_DataSet_m_getInformationObjectsModifiedSince, data_DataSet_m_getOrganisationsWithAllTags, data_DataSet_m_getCategories, data_DataSet_m_getItemsWithIdent, data_DataSet_m_getItemsWithOneOfMetaTags, data_DataSet_m_getOrganisationsWithName, data_DataSet_m_getItemWithIdentifier, data_DataSet_m_getInformationObjectsWithOneOfCategories, data_DataSet_m_getContentsWithAttachment, data_DataSet_m_getIdentifierWithKeyValue, data_DataSet_m_getLocations, data_DataSet_m_getPersonsWithOneOfMetaTags, data_DataSet_m_getEmails, data_DataSet_m_getEvents, data_DataSet_m_getPersons, data_DataSet_m_getContentsWithOneOfMetaTags, data_DataSet_m_getInformationObjectsWithOneOfTags, data_DataSet_m_getOrganisationsWithAllCategories, data_DataSet_m_getIdentifiersWithKey, data_DataSet_m_getContentsWithAllCategories, data_DataSet_m_getStarRankings, data_DataSet_m_log, data_DataSet_m_getAllCategories, data_DataSet_m_searchByQuery, data_DataSet_m_getConnectionsBetweenInformationObjectsOfDifferentCategories, data_DataSet_m_getConnections, data_DataSet_m_getMetaTag, data_DataSet_m_searchInformationObjects, data_DataSet_m_getPersonsWithAttachment, data_DataSet_m_getViewRankings, data_DataSet_m_getInformationObjectsWithAllTags, data_DataSet_m_getTag, data_DataSet_m_getPersonWithIdent, data_DataSet_m_getInformationObjects, data_DataSet_m_getEmptyItemWithIdent, data_DataSet_m_getTagsWithMoreThanXInformationObjects, data_DataSet_m_getRandomXInformationObjects, data_DataSet_m_getRandomXPersons, data_DataSet_m_getOrganisationsWithOneOfCategories, data_DataSet_m_getContents}

# data_Item class attributes and methods
data_Item_ident: Property = Property(name="ident", type=StringType)
data_Item_uri: Property = Property(name="uri", type=StringType)
data_Item_stringValue: Property = Property(name="stringValue", type=StringType)
data_Item_lastModified: Property = Property(name="lastModified", type=DateType)
data_Item_created: Property = Property(name="created", type=DateType)
data_Item_m_delete: Method = Method(name="delete", parameters={})
data_Item_m_log: Method = Method(name="log", parameters={Parameter(name='message')})
data_Item_m_log: Method = Method(name="log", parameters={Parameter(name='level'), Parameter(name='message')})
data_Item_m_metaTag: Method = Method(name="metaTag", parameters={Parameter(name='name')}, type=StringType)
data_Item_m_identifyBy: Method = Method(name="identifyBy", parameters={Parameter(name='key'), Parameter(name='value')}, type=StringType)
data_Item_m_getIdentifier: Method = Method(name="getIdentifier", parameters={Parameter(name='key')}, type=StringType)
data_Item_m_hasMetaTag: Method = Method(name="hasMetaTag", parameters={Parameter(name='tag')}, type=StringType)
data_Item_m_matchesSearch: Method = Method(name="matchesSearch", parameters={Parameter(name='term')}, type=StringType)
data_Item_m_isEqualItem: Method = Method(name="isEqualItem", parameters={Parameter(name='item')}, type=StringType)
data_Item_m_getCreatedPrettyInLanguage: Method = Method(name="getCreatedPrettyInLanguage", parameters={Parameter(name='language')}, type=StringType)
data_Item_m_getCreatedPretty: Method = Method(name="getCreatedPretty", parameters={}, type=StringType)
data_Item_m_getLastModifiedPrettyInLanguage: Method = Method(name="getLastModifiedPrettyInLanguage", parameters={Parameter(name='language')}, type=StringType)
data_Item_m_getLastModifiedPretty: Method = Method(name="getLastModifiedPretty", parameters={}, type=StringType)
data_Item_m_deleteOnDeleteOf: Method = Method(name="deleteOnDeleteOf", parameters={Parameter(name='item')}, type=Item)
data_Item_m_deleteIfEmptyOnDelete: Method = Method(name="deleteIfEmptyOnDelete", parameters={})
data_Item_m_update: Method = Method(name="update", parameters={Parameter(name='item')}, type=Item)
data_Item_m_forceUpdate: Method = Method(name="forceUpdate", parameters={Parameter(name='item')}, type=Item)
data_Item_m_unMetaTag: Method = Method(name="unMetaTag", parameters={Parameter(name='name')}, type=StringType)
data_Item_m_removeIdentifier: Method = Method(name="removeIdentifier", parameters={Parameter(name='key')}, type=StringType)
data_Item.attributes={data_Item_stringValue, data_Item_ident, data_Item_created, data_Item_uri, data_Item_lastModified}
data_Item.methods={data_Item_m_deleteIfEmptyOnDelete, data_Item_m_getLastModifiedPrettyInLanguage, data_Item_m_log, data_Item_m_hasMetaTag, data_Item_m_forceUpdate, data_Item_m_removeIdentifier, data_Item_m_getIdentifier, data_Item_m_delete, data_Item_m_getCreatedPrettyInLanguage, data_Item_m_matchesSearch, data_Item_m_log, data_Item_m_isEqualItem, data_Item_m_update, data_Item_m_identifyBy, data_Item_m_getCreatedPretty, data_Item_m_unMetaTag, data_Item_m_getLastModifiedPretty, data_Item_m_deleteOnDeleteOf, data_Item_m_metaTag}

# data_Mashup class attributes and methods

# data_MetaTag class attributes and methods
data_MetaTag_name: Property = Property(name="name", type=StringType)
data_MetaTag_m_getWebAccounts: Method = Method(name="getWebAccounts", parameters={}, type=StringType)
data_MetaTag_m_getInformationObjects: Method = Method(name="getInformationObjects", parameters={}, type=InformationObject)
data_MetaTag_m_getExtensions: Method = Method(name="getExtensions", parameters={}, type=StringType)
data_MetaTag_m_getCount: Method = Method(name="getCount", parameters={}, type=StringType)
data_MetaTag_m_getInformationObjectsCount: Method = Method(name="getInformationObjectsCount", parameters={}, type=StringType)
data_MetaTag.attributes={data_MetaTag_name}
data_MetaTag.methods={data_MetaTag_m_getCount, data_MetaTag_m_getWebAccounts, data_MetaTag_m_getInformationObjectsCount, data_MetaTag_m_getInformationObjects, data_MetaTag_m_getExtensions}

# data_Identifier class attributes and methods
data_Identifier_key: Property = Property(name="key", type=StringType)
data_Identifier_value: Property = Property(name="value", type=StringType)
data_Identifier.attributes={data_Identifier_value, data_Identifier_key}

# data_Extension class attributes and methods
data_Extension_m_tag: Method = Method(name="tag", parameters={Parameter(name='name')}, type=StringType)
data_Extension.methods={data_Extension_m_tag}

# data_Classification class attributes and methods
data_Classification_name: Property = Property(name="name", type=StringType)
data_Classification_m_getPersons: Method = Method(name="getPersons", parameters={}, type=StringType)
data_Classification_m_getContents: Method = Method(name="getContents", parameters={}, type=StringType)
data_Classification_m_getOrganisations: Method = Method(name="getOrganisations", parameters={}, type=StringType)
data_Classification_m_getCount: Method = Method(name="getCount", parameters={}, type=StringType)
data_Classification_m_getPersonsCount: Method = Method(name="getPersonsCount", parameters={}, type=StringType)
data_Classification_m_getContentsCount: Method = Method(name="getContentsCount", parameters={}, type=StringType)
data_Classification_m_getOrganisationsCount: Method = Method(name="getOrganisationsCount", parameters={}, type=StringType)
data_Classification_m_getSlug: Method = Method(name="getSlug", parameters={}, type=StringType)
data_Classification.attributes={data_Classification_name}
data_Classification.methods={data_Classification_m_getContents, data_Classification_m_getSlug, data_Classification_m_getCount, data_Classification_m_getOrganisations, data_Classification_m_getPersonsCount, data_Classification_m_getPersons, data_Classification_m_getContentsCount, data_Classification_m_getOrganisationsCount}

# Classification class attributes and methods

# data_Phone class attributes and methods
data_Phone_areaCode: Property = Property(name="areaCode", type=StringType)
data_Phone_countryCode: Property = Property(name="countryCode", type=StringType)
data_Phone_number: Property = Property(name="number", type=StringType)
data_Phone.attributes={data_Phone_countryCode, data_Phone_number, data_Phone_areaCode}

# MetaInformation class attributes and methods

# data_InstantMessenger class attributes and methods
data_InstantMessenger_username: Property = Property(name="username", type=StringType)
data_InstantMessenger.attributes={data_InstantMessenger_username}

# data_Email class attributes and methods
data_Email_adress: Property = Property(name="adress", type=StringType)
data_Email.attributes={data_Email_adress}

# data_WebSite class attributes and methods
data_WebSite_adress: Property = Property(name="adress", type=StringType)
data_WebSite_title: Property = Property(name="title", type=StringType)
data_WebSite.attributes={data_WebSite_title, data_WebSite_adress}

# Extension class attributes and methods

# data_Attachment class attributes and methods
data_Attachment_fileUrl: Property = Property(name="fileUrl", type=StringType)
data_Attachment_cachedFileUrl: Property = Property(name="cachedFileUrl", type=StringType)
data_Attachment_cachedOnly: Property = Property(name="cachedOnly", type=StringType)
data_Attachment_fileExtension: Property = Property(name="fileExtension", type=StringType)
data_Attachment_fileIdentifier: Property = Property(name="fileIdentifier", type=StringType)
data_Attachment_cachedFileName: Property = Property(name="cachedFileName", type=StringType)
data_Attachment_m_getOriginalFileUrl: Method = Method(name="getOriginalFileUrl", parameters={}, type=StringType)
data_Attachment.attributes={data_Attachment_cachedFileName, data_Attachment_fileUrl, data_Attachment_cachedOnly, data_Attachment_fileIdentifier, data_Attachment_fileExtension, data_Attachment_cachedFileUrl}
data_Attachment.methods={data_Attachment_m_getOriginalFileUrl}

# data_Location class attributes and methods
data_Location_street: Property = Property(name="street", type=StringType)
data_Location_houseNumber: Property = Property(name="houseNumber", type=StringType)
data_Location_zipCode: Property = Property(name="zipCode", type=StringType)
data_Location_country: Property = Property(name="country", type=StringType)
data_Location_longitude: Property = Property(name="longitude", type=StringType)
data_Location_latitude: Property = Property(name="latitude", type=StringType)
data_Location_city: Property = Property(name="city", type=StringType)
data_Location_state: Property = Property(name="state", type=StringType)
data_Location.attributes={data_Location_zipCode, data_Location_street, data_Location_latitude, data_Location_houseNumber, data_Location_city, data_Location_state, data_Location_longitude, data_Location_country}

# data_IndoorLocation class attributes and methods
data_IndoorLocation_name: Property = Property(name="name", type=StringType)
data_IndoorLocation.attributes={data_IndoorLocation_name}

# Attachment class attributes and methods

# Ranking class attributes and methods

# data_WebAccount class attributes and methods
data_WebAccount_username: Property = Property(name="username", type=StringType)
data_WebAccount.attributes={data_WebAccount_username}

# data_Event class attributes and methods
data_Event_date: Property = Property(name="date", type=DateType)
data_Event_m_getDatePrettyInLanguage: Method = Method(name="getDatePrettyInLanguage", parameters={Parameter(name='language')}, type=StringType)
data_Event_m_getDatePretty: Method = Method(name="getDatePretty", parameters={}, type=StringType)
data_Event.attributes={data_Event_date}
data_Event.methods={data_Event_m_getDatePrettyInLanguage, data_Event_m_getDatePretty}

# Relationships
leaderOf0: BinaryAssociation = BinaryAssociation(
    name="leaderOf0",
    ends={
        Property(name="Organisation", type=data_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="leader", type=data_Organisation, multiplicity=Multiplicity(0, 9999))
    }
)
participates1: BinaryAssociation = BinaryAssociation(
    name="participates1",
    ends={
        Property(name="Organisation2", type=data_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="participants", type=data_Organisation, multiplicity=Multiplicity(0, 9999))
    }
)
authored3: BinaryAssociation = BinaryAssociation(
    name="authored3",
    ends={
        Property(name="Content", type=data_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="author", type=data_Content, multiplicity=Multiplicity(0, 9999))
    }
)
contributed4: BinaryAssociation = BinaryAssociation(
    name="contributed4",
    ends={
        Property(name="Content5", type=data_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="contributors", type=data_Content, multiplicity=Multiplicity(0, 9999))
    }
)
persons7: BinaryAssociation = BinaryAssociation(
    name="persons7",
    ends={
        Property(name="data_Person", type=data_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="data_Person6", type=data_Person, multiplicity=Multiplicity(0, 9999))
    }
)
ranked8: BinaryAssociation = BinaryAssociation(
    name="ranked8",
    ends={
        Property(name="Ranking", type=data_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="ranker", type=data_Ranking, multiplicity=Multiplicity(0, 9999))
    }
)
categories9: BinaryAssociation = BinaryAssociation(
    name="categories9",
    ends={
        Property(name="Category", type=data_InformationObject, multiplicity=Multiplicity(1, 1)),
        Property(name="categorized", type=data_Category, multiplicity=Multiplicity(0, 9999))
    }
)
tags10: BinaryAssociation = BinaryAssociation(
    name="tags10",
    ends={
        Property(name="Tag", type=data_InformationObject, multiplicity=Multiplicity(1, 1)),
        Property(name="tagged", type=data_Tag, multiplicity=Multiplicity(0, 9999))
    }
)
images11: BinaryAssociation = BinaryAssociation(
    name="images11",
    ends={
        Property(name="data_Image", type=data_InformationObject, multiplicity=Multiplicity(1, 1)),
        Property(name="data_InformationObject", type=data_Image, multiplicity=Multiplicity(0, 9999))
    }
)
starRankings12: BinaryAssociation = BinaryAssociation(
    name="starRankings12",
    ends={
        Property(name="StarRanking", type=data_InformationObject, multiplicity=Multiplicity(1, 1)),
        Property(name="rankedInformationObject", type=data_StarRanking, multiplicity=Multiplicity(0, 9999))
    }
)
thumbRankings13: BinaryAssociation = BinaryAssociation(
    name="thumbRankings13",
    ends={
        Property(name="ThumbRanking", type=data_InformationObject, multiplicity=Multiplicity(1, 1)),
        Property(name="rankedInformationObject14", type=data_ThumbRanking, multiplicity=Multiplicity(0, 9999))
    }
)
viewRankings15: BinaryAssociation = BinaryAssociation(
    name="viewRankings15",
    ends={
        Property(name="ViewRanking", type=data_InformationObject, multiplicity=Multiplicity(1, 1)),
        Property(name="rankedInformationObject16", type=data_ViewRanking, multiplicity=Multiplicity(0, 9999))
    }
)
connectedTo17: BinaryAssociation = BinaryAssociation(
    name="connectedTo17",
    ends={
        Property(name="Connection", type=data_InformationObject, multiplicity=Multiplicity(1, 1)),
        Property(name="from", type=data_Connection, multiplicity=Multiplicity(0, 9999))
    }
)
connectedBy18: BinaryAssociation = BinaryAssociation(
    name="connectedBy18",
    ends={
        Property(name="Connection19", type=data_InformationObject, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=data_Connection, multiplicity=Multiplicity(0, 9999))
    }
)
binaries20: BinaryAssociation = BinaryAssociation(
    name="binaries20",
    ends={
        Property(name="data_Binary", type=data_InformationObject, multiplicity=Multiplicity(1, 1)),
        Property(name="data_InformationObject21", type=data_Binary, multiplicity=Multiplicity(0, 9999))
    }
)
mainCategory22: BinaryAssociation = BinaryAssociation(
    name="mainCategory22",
    ends={
        Property(name="Category23", type=data_InformationObject, multiplicity=Multiplicity(1, 1)),
        Property(name="mainCategorized", type=data_Category, multiplicity=Multiplicity(0, 1))
    }
)
metaInformations24: BinaryAssociation = BinaryAssociation(
    name="metaInformations24",
    ends={
        Property(name="MetaInformation", type=data_InformationObject, multiplicity=Multiplicity(1, 1)),
        Property(name="informationObjects", type=data_MetaInformation, multiplicity=Multiplicity(0, 9999))
    }
)
contents26: BinaryAssociation = BinaryAssociation(
    name="contents26",
    ends={
        Property(name="Content27", type=data_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="parentContent", type=data_Content, multiplicity=Multiplicity(0, 9999))
    }
)
contributors28: BinaryAssociation = BinaryAssociation(
    name="contributors28",
    ends={
        Property(name="Person", type=data_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="contributed", type=data_Person, multiplicity=Multiplicity(0, 9999))
    }
)
author29: BinaryAssociation = BinaryAssociation(
    name="author29",
    ends={
        Property(name="Person30", type=data_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="authored", type=data_Person, multiplicity=Multiplicity(0, 1))
    }
)
documents31: BinaryAssociation = BinaryAssociation(
    name="documents31",
    ends={
        Property(name="data_Document", type=data_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="data_Content", type=data_Document, multiplicity=Multiplicity(0, 9999))
    }
)
parentContent33: BinaryAssociation = BinaryAssociation(
    name="parentContent33",
    ends={
        Property(name="Content34", type=data_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="contents", type=data_Content, multiplicity=Multiplicity(0, 1))
    }
)
transformations35: BinaryAssociation = BinaryAssociation(
    name="transformations35",
    ends={
        Property(name="Transformation", type=data_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="transformed", type=data_Transformation, multiplicity=Multiplicity(0, 9999))
    }
)
videos36: BinaryAssociation = BinaryAssociation(
    name="videos36",
    ends={
        Property(name="data_Video", type=data_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="data_Content37", type=data_Video, multiplicity=Multiplicity(0, 9999))
    }
)
items38: BinaryAssociation = BinaryAssociation(
    name="items38",
    ends={
        Property(name="Item", type=data_DataSet, multiplicity=Multiplicity(1, 1)),
        Property(name="dataSet", type=data_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
setUp39: BinaryAssociation = BinaryAssociation(
    name="setUp39",
    ends={
        Property(name="data_Mashup", type=data_DataSet, multiplicity=Multiplicity(1, 1)),
        Property(name="data_DataSet", type=data_Mashup, multiplicity=Multiplicity(0, 1))
    }
)
dataSet40: BinaryAssociation = BinaryAssociation(
    name="dataSet40",
    ends={
        Property(name="DataSet", type=data_Item, multiplicity=Multiplicity(1, 1)),
        Property(name="items", type=data_DataSet, multiplicity=Multiplicity(0, 1))
    }
)
identifiedBy42: BinaryAssociation = BinaryAssociation(
    name="identifiedBy42",
    ends={
        Property(name="Identifier", type=data_Item, multiplicity=Multiplicity(1, 1)),
        Property(name="identified", type=data_Identifier, multiplicity=Multiplicity(0, 9999))
    }
)
deleteOnDelete44: BinaryAssociation = BinaryAssociation(
    name="deleteOnDelete44",
    ends={
        Property(name="Item45", type=data_Item, multiplicity=Multiplicity(1, 1)),
        Property(name="deletedIfDeleted", type=data_Item, multiplicity=Multiplicity(0, 9999))
    }
)
deletedIfDeleted47: BinaryAssociation = BinaryAssociation(
    name="deletedIfDeleted47",
    ends={
        Property(name="Item48", type=data_Item, multiplicity=Multiplicity(1, 1)),
        Property(name="deleteOnDelete", type=data_Item, multiplicity=Multiplicity(0, 9999))
    }
)
metaTags41: BinaryAssociation = BinaryAssociation(
    name="metaTags41",
    ends={
        Property(name="MetaTag", type=data_Item, multiplicity=Multiplicity(1, 1)),
        Property(name="metaTagged", type=data_MetaTag, multiplicity=Multiplicity(0, 9999))
    }
)
categorized49: BinaryAssociation = BinaryAssociation(
    name="categorized49",
    ends={
        Property(name="InformationObject", type=data_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="categories", type=data_InformationObject, multiplicity=Multiplicity(0, 9999))
    }
)
parentCategory51: BinaryAssociation = BinaryAssociation(
    name="parentCategory51",
    ends={
        Property(name="Category53", type=data_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="categories52", type=data_Category, multiplicity=Multiplicity(0, 1))
    }
)
categories55: BinaryAssociation = BinaryAssociation(
    name="categories55",
    ends={
        Property(name="Category56", type=data_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="parentCategory", type=data_Category, multiplicity=Multiplicity(0, 9999))
    }
)
mainCategorized57: BinaryAssociation = BinaryAssociation(
    name="mainCategorized57",
    ends={
        Property(name="InformationObject58", type=data_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="mainCategory", type=data_InformationObject, multiplicity=Multiplicity(0, 9999))
    }
)
tagged59: BinaryAssociation = BinaryAssociation(
    name="tagged59",
    ends={
        Property(name="InformationObject60", type=data_Tag, multiplicity=Multiplicity(1, 1)),
        Property(name="tags", type=data_InformationObject, multiplicity=Multiplicity(0, 9999))
    }
)
parentOrganisation62: BinaryAssociation = BinaryAssociation(
    name="parentOrganisation62",
    ends={
        Property(name="Organisation63", type=data_Organisation, multiplicity=Multiplicity(1, 1)),
        Property(name="organisations", type=data_Organisation, multiplicity=Multiplicity(0, 1))
    }
)
leader64: BinaryAssociation = BinaryAssociation(
    name="leader64",
    ends={
        Property(name="Person65", type=data_Organisation, multiplicity=Multiplicity(1, 1)),
        Property(name="leaderOf", type=data_Person, multiplicity=Multiplicity(0, 1))
    }
)
participants66: BinaryAssociation = BinaryAssociation(
    name="participants66",
    ends={
        Property(name="Person67", type=data_Organisation, multiplicity=Multiplicity(1, 1)),
        Property(name="participates", type=data_Person, multiplicity=Multiplicity(0, 9999))
    }
)
organisations69: BinaryAssociation = BinaryAssociation(
    name="organisations69",
    ends={
        Property(name="Organisation70", type=data_Organisation, multiplicity=Multiplicity(1, 1)),
        Property(name="parentOrganisation", type=data_Organisation, multiplicity=Multiplicity(0, 9999))
    }
)
metaTagged71: BinaryAssociation = BinaryAssociation(
    name="metaTagged71",
    ends={
        Property(name="Item72", type=data_MetaTag, multiplicity=Multiplicity(1, 1)),
        Property(name="metaTags", type=data_Item, multiplicity=Multiplicity(0, 9999))
    }
)
ranker73: BinaryAssociation = BinaryAssociation(
    name="ranker73",
    ends={
        Property(name="Person74", type=data_Ranking, multiplicity=Multiplicity(1, 1)),
        Property(name="ranked", type=data_Person, multiplicity=Multiplicity(0, 1))
    }
)
indoorLocations75: BinaryAssociation = BinaryAssociation(
    name="indoorLocations75",
    ends={
        Property(name="IndoorLocation", type=data_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="location", type=data_IndoorLocation, multiplicity=Multiplicity(0, 9999))
    }
)
rankedInformationObject78: BinaryAssociation = BinaryAssociation(
    name="rankedInformationObject78",
    ends={
        Property(name="InformationObject79", type=data_ViewRanking, multiplicity=Multiplicity(1, 1)),
        Property(name="viewRankings", type=data_InformationObject, multiplicity=Multiplicity(0, 1))
    }
)
rankedInformationObject80: BinaryAssociation = BinaryAssociation(
    name="rankedInformationObject80",
    ends={
        Property(name="InformationObject81", type=data_ThumbRanking, multiplicity=Multiplicity(1, 1)),
        Property(name="thumbRankings", type=data_InformationObject, multiplicity=Multiplicity(0, 1))
    }
)
transformed82: BinaryAssociation = BinaryAssociation(
    name="transformed82",
    ends={
        Property(name="Content83", type=data_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="transformations", type=data_Content, multiplicity=Multiplicity(0, 9999))
    }
)
from84: BinaryAssociation = BinaryAssociation(
    name="from84",
    ends={
        Property(name="InformationObject85", type=data_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="connectedTo", type=data_InformationObject, multiplicity=Multiplicity(0, 1))
    }
)
to86: BinaryAssociation = BinaryAssociation(
    name="to86",
    ends={
        Property(name="InformationObject87", type=data_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="connectedBy", type=data_InformationObject, multiplicity=Multiplicity(0, 1))
    }
)
informationObjects88: BinaryAssociation = BinaryAssociation(
    name="informationObjects88",
    ends={
        Property(name="InformationObject89", type=data_MetaInformation, multiplicity=Multiplicity(1, 1)),
        Property(name="metaInformations", type=data_InformationObject, multiplicity=Multiplicity(0, 9999))
    }
)
location90: BinaryAssociation = BinaryAssociation(
    name="location90",
    ends={
        Property(name="Location", type=data_IndoorLocation, multiplicity=Multiplicity(1, 1)),
        Property(name="indoorLocations", type=data_Location, multiplicity=Multiplicity(0, 1))
    }
)
rankedInformationObject76: BinaryAssociation = BinaryAssociation(
    name="rankedInformationObject76",
    ends={
        Property(name="InformationObject77", type=data_StarRanking, multiplicity=Multiplicity(1, 1)),
        Property(name="starRankings", type=data_InformationObject, multiplicity=Multiplicity(0, 1))
    }
)
indoorLocations96: BinaryAssociation = BinaryAssociation(
    name="indoorLocations96",
    ends={
        Property(name="IndoorLocation97", type=data_IndoorLocation, multiplicity=Multiplicity(1, 1)),
        Property(name="parentIndoorLocation", type=data_IndoorLocation, multiplicity=Multiplicity(0, 9999))
    }
)
identified98: BinaryAssociation = BinaryAssociation(
    name="identified98",
    ends={
        Property(name="Item99", type=data_Identifier, multiplicity=Multiplicity(1, 1)),
        Property(name="identifiedBy", type=data_Item, multiplicity=Multiplicity(1, 1))
    }
)
parentIndoorLocation92: BinaryAssociation = BinaryAssociation(
    name="parentIndoorLocation92",
    ends={
        Property(name="IndoorLocation94", type=data_IndoorLocation, multiplicity=Multiplicity(1, 1)),
        Property(name="indoorLocations93", type=data_IndoorLocation, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_data_Person_InformationObject = Generalization(general=InformationObject, specific=data_Person)
gen_data_InformationObject_Item = Generalization(general=Item, specific=data_InformationObject)
gen_data_Content_InformationObject = Generalization(general=InformationObject, specific=data_Content)
gen_data_Extension_Item = Generalization(general=Item, specific=data_Extension)
gen_data_Classification_Item = Generalization(general=Item, specific=data_Classification)
gen_data_Category_Classification = Generalization(general=Classification, specific=data_Category)
gen_data_Tag_Classification = Generalization(general=Classification, specific=data_Tag)
gen_data_Organisation_InformationObject = Generalization(general=InformationObject, specific=data_Organisation)
gen_data_MetaTag_Item = Generalization(general=Item, specific=data_MetaTag)
gen_data_Phone_MetaInformation = Generalization(general=MetaInformation, specific=data_Phone)
gen_data_InstantMessenger_MetaInformation = Generalization(general=MetaInformation, specific=data_InstantMessenger)
gen_data_Email_MetaInformation = Generalization(general=MetaInformation, specific=data_Email)
gen_data_WebSite_MetaInformation = Generalization(general=MetaInformation, specific=data_WebSite)
gen_data_Ranking_Extension = Generalization(general=Extension, specific=data_Ranking)
gen_data_Attachment_Extension = Generalization(general=Extension, specific=data_Attachment)
gen_data_Location_MetaInformation = Generalization(general=MetaInformation, specific=data_Location)
gen_data_Image_Attachment = Generalization(general=Attachment, specific=data_Image)
gen_data_Document_Attachment = Generalization(general=Attachment, specific=data_Document)
gen_data_StarRanking_Ranking = Generalization(general=Ranking, specific=data_StarRanking)
gen_data_WebAccount_MetaInformation = Generalization(general=MetaInformation, specific=data_WebAccount)
gen_data_ViewRanking_Ranking = Generalization(general=Ranking, specific=data_ViewRanking)
gen_data_ThumbRanking_Ranking = Generalization(general=Ranking, specific=data_ThumbRanking)
gen_data_Transformation_Attachment = Generalization(general=Attachment, specific=data_Transformation)
gen_data_Video_Attachment = Generalization(general=Attachment, specific=data_Video)
gen_data_Connection_Extension = Generalization(general=Extension, specific=data_Connection)
gen_data_Binary_Attachment = Generalization(general=Attachment, specific=data_Binary)
gen_data_MetaInformation_Extension = Generalization(general=Extension, specific=data_MetaInformation)
gen_data_IndoorLocation_MetaInformation = Generalization(general=MetaInformation, specific=data_IndoorLocation)
gen_data_Identifier_Item = Generalization(general=Item, specific=data_Identifier)
gen_data_Event_MetaInformation = Generalization(general=MetaInformation, specific=data_Event)

# Domain Model
domain_model = DomainModel(
    name="data",
    types={data_Person, InformationObject, data_Organisation, data_Content, data_Ranking, data_InformationObject, Item, data_Category, data_Tag, data_Image, data_StarRanking, data_ThumbRanking, data_ViewRanking, data_Connection, data_Binary, data_MetaInformation, data_Document, data_Transformation, data_Video, data_DataSet, data_Item, data_Mashup, data_MetaTag, data_Identifier, data_Extension, data_Classification, Classification, data_Phone, MetaInformation, data_InstantMessenger, data_Email, data_WebSite, Extension, data_Attachment, data_Location, data_IndoorLocation, Attachment, Ranking, data_WebAccount, data_Event},
    associations={leaderOf0, participates1, authored3, contributed4, persons7, ranked8, categories9, tags10, images11, starRankings12, thumbRankings13, viewRankings15, connectedTo17, connectedBy18, binaries20, mainCategory22, metaInformations24, contents26, contributors28, author29, documents31, parentContent33, transformations35, videos36, items38, setUp39, dataSet40, identifiedBy42, deleteOnDelete44, deletedIfDeleted47, metaTags41, categorized49, parentCategory51, categories55, mainCategorized57, tagged59, parentOrganisation62, leader64, participants66, organisations69, metaTagged71, ranker73, indoorLocations75, rankedInformationObject78, rankedInformationObject80, transformed82, from84, to86, informationObjects88, location90, rankedInformationObject76, indoorLocations96, identified98, parentIndoorLocation92},
    generalizations={gen_data_Person_InformationObject, gen_data_InformationObject_Item, gen_data_Content_InformationObject, gen_data_Extension_Item, gen_data_Classification_Item, gen_data_Category_Classification, gen_data_Tag_Classification, gen_data_Organisation_InformationObject, gen_data_MetaTag_Item, gen_data_Phone_MetaInformation, gen_data_InstantMessenger_MetaInformation, gen_data_Email_MetaInformation, gen_data_WebSite_MetaInformation, gen_data_Ranking_Extension, gen_data_Attachment_Extension, gen_data_Location_MetaInformation, gen_data_Image_Attachment, gen_data_Document_Attachment, gen_data_StarRanking_Ranking, gen_data_WebAccount_MetaInformation, gen_data_ViewRanking_Ranking, gen_data_ThumbRanking_Ranking, gen_data_Transformation_Attachment, gen_data_Video_Attachment, gen_data_Connection_Extension, gen_data_Binary_Attachment, gen_data_MetaInformation_Extension, gen_data_IndoorLocation_MetaInformation, gen_data_Identifier_Item, gen_data_Event_MetaInformation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)