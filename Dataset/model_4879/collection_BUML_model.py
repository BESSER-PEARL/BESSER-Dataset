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
collection_ItemsCollection = Class(name="collection::ItemsCollection", is_abstract=True)
collection_Item = Class(name="collection::Item")
collection_DataSet = Class(name="collection::DataSet")
collection_SmartInformationObjectCollection = Class(name="collection::SmartInformationObjectCollection")
ItemsCollection = Class(name="ItemsCollection")
collection_MetaTag = Class(name="collection::MetaTag")
collection_Category = Class(name="collection::Category")
collection_Person = Class(name="collection::Person")
collection_Organisation = Class(name="collection::Organisation")
collection_ManualCollection = Class(name="collection::ManualCollection")
collection_RemoteCollection = Class(name="collection::RemoteCollection")
collection_Tag = Class(name="collection::Tag")

# collection_ItemsCollection class attributes and methods

# collection_Item class attributes and methods

# collection_DataSet class attributes and methods

# collection_SmartInformationObjectCollection class attributes and methods
collection_SmartInformationObjectCollection_includePersons: Property = Property(name="includePersons", type=StringType)
collection_SmartInformationObjectCollection_includeOrganisations: Property = Property(name="includeOrganisations", type=StringType)
collection_SmartInformationObjectCollection_includeContents: Property = Property(name="includeContents", type=StringType)
collection_SmartInformationObjectCollection_minimumAge: Property = Property(name="minimumAge", type=DateType)
collection_SmartInformationObjectCollection_m_addPositive: Method = Method(name="addPositive", parameters={Parameter(name='item')}, type=StringType)
collection_SmartInformationObjectCollection_m_addNegative: Method = Method(name="addNegative", parameters={Parameter(name='item')}, type=StringType)
collection_SmartInformationObjectCollection_m_remove: Method = Method(name="remove", parameters={Parameter(name='item')}, type=StringType)
collection_SmartInformationObjectCollection.attributes={collection_SmartInformationObjectCollection_includePersons, collection_SmartInformationObjectCollection_includeContents, collection_SmartInformationObjectCollection_minimumAge, collection_SmartInformationObjectCollection_includeOrganisations}
collection_SmartInformationObjectCollection.methods={collection_SmartInformationObjectCollection_m_remove, collection_SmartInformationObjectCollection_m_addPositive, collection_SmartInformationObjectCollection_m_addNegative}

# ItemsCollection class attributes and methods

# collection_MetaTag class attributes and methods

# collection_Category class attributes and methods

# collection_Person class attributes and methods

# collection_Organisation class attributes and methods

# collection_ManualCollection class attributes and methods
collection_ManualCollection_m_addItem: Method = Method(name="addItem", parameters={Parameter(name='item')}, type=StringType)
collection_ManualCollection_m_removeItem: Method = Method(name="removeItem", parameters={Parameter(name='item')}, type=StringType)
collection_ManualCollection.methods={collection_ManualCollection_m_addItem, collection_ManualCollection_m_removeItem}

# collection_RemoteCollection class attributes and methods
collection_RemoteCollection_remoteURL: Property = Property(name="remoteURL", type=StringType)
collection_RemoteCollection.attributes={collection_RemoteCollection_remoteURL}

# collection_Tag class attributes and methods

# Relationships
items0: BinaryAssociation = BinaryAssociation(
    name="items0",
    ends={
        Property(name="collection_Item", type=collection_ItemsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="collection_ItemsCollection", type=collection_Item, multiplicity=Multiplicity(0, 9999))
    }
)
dataSet1: BinaryAssociation = BinaryAssociation(
    name="dataSet1",
    ends={
        Property(name="collection_DataSet", type=collection_ItemsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="collection_ItemsCollection2", type=collection_DataSet, multiplicity=Multiplicity(1, 1))
    }
)
positiveMetaTags7: BinaryAssociation = BinaryAssociation(
    name="positiveMetaTags7",
    ends={
        Property(name="collection_MetaTag", type=collection_SmartInformationObjectCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="collection_SmartInformationObjectCollection8", type=collection_MetaTag, multiplicity=Multiplicity(0, 9999))
    }
)
positiveCategories9: BinaryAssociation = BinaryAssociation(
    name="positiveCategories9",
    ends={
        Property(name="collection_Category", type=collection_SmartInformationObjectCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="collection_SmartInformationObjectCollection10", type=collection_Category, multiplicity=Multiplicity(0, 9999))
    }
)
positivePersons11: BinaryAssociation = BinaryAssociation(
    name="positivePersons11",
    ends={
        Property(name="collection_Person", type=collection_SmartInformationObjectCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="collection_SmartInformationObjectCollection12", type=collection_Person, multiplicity=Multiplicity(0, 9999))
    }
)
negativeMetaTags13: BinaryAssociation = BinaryAssociation(
    name="negativeMetaTags13",
    ends={
        Property(name="collection_MetaTag15", type=collection_SmartInformationObjectCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="collection_SmartInformationObjectCollection14", type=collection_MetaTag, multiplicity=Multiplicity(0, 9999))
    }
)
negativeCategories16: BinaryAssociation = BinaryAssociation(
    name="negativeCategories16",
    ends={
        Property(name="collection_Category18", type=collection_SmartInformationObjectCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="collection_SmartInformationObjectCollection17", type=collection_Category, multiplicity=Multiplicity(0, 9999))
    }
)
negativePersons19: BinaryAssociation = BinaryAssociation(
    name="negativePersons19",
    ends={
        Property(name="collection_Person21", type=collection_SmartInformationObjectCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="collection_SmartInformationObjectCollection20", type=collection_Person, multiplicity=Multiplicity(0, 9999))
    }
)
positiveOrganisations22: BinaryAssociation = BinaryAssociation(
    name="positiveOrganisations22",
    ends={
        Property(name="collection_Organisation", type=collection_SmartInformationObjectCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="collection_SmartInformationObjectCollection23", type=collection_Organisation, multiplicity=Multiplicity(0, 9999))
    }
)
negativeOrganisations24: BinaryAssociation = BinaryAssociation(
    name="negativeOrganisations24",
    ends={
        Property(name="collection_Organisation26", type=collection_SmartInformationObjectCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="collection_SmartInformationObjectCollection25", type=collection_Organisation, multiplicity=Multiplicity(0, 9999))
    }
)
positiveTags3: BinaryAssociation = BinaryAssociation(
    name="positiveTags3",
    ends={
        Property(name="collection_Tag", type=collection_SmartInformationObjectCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="collection_SmartInformationObjectCollection", type=collection_Tag, multiplicity=Multiplicity(0, 9999))
    }
)
negativeTags4: BinaryAssociation = BinaryAssociation(
    name="negativeTags4",
    ends={
        Property(name="collection_Tag6", type=collection_SmartInformationObjectCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="collection_SmartInformationObjectCollection5", type=collection_Tag, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_collection_SmartInformationObjectCollection_ItemsCollection = Generalization(general=ItemsCollection, specific=collection_SmartInformationObjectCollection)
gen_collection_ManualCollection_ItemsCollection = Generalization(general=ItemsCollection, specific=collection_ManualCollection)
gen_collection_RemoteCollection_ItemsCollection = Generalization(general=ItemsCollection, specific=collection_RemoteCollection)

# Domain Model
domain_model = DomainModel(
    name="collection",
    types={collection_ItemsCollection, collection_Item, collection_DataSet, collection_SmartInformationObjectCollection, ItemsCollection, collection_MetaTag, collection_Category, collection_Person, collection_Organisation, collection_ManualCollection, collection_RemoteCollection, collection_Tag},
    associations={items0, dataSet1, positiveMetaTags7, positiveCategories9, positivePersons11, negativeMetaTags13, negativeCategories16, negativePersons19, positiveOrganisations22, negativeOrganisations24, positiveTags3, negativeTags4},
    generalizations={gen_collection_SmartInformationObjectCollection_ItemsCollection, gen_collection_ManualCollection_ItemsCollection, gen_collection_RemoteCollection_ItemsCollection},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)