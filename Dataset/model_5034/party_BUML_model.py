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
party_Party = Class(name="party::Party", is_abstract=True)
Tagged = Class(name="Tagged")
party_ContactInfo = Class(name="party::ContactInfo", is_abstract=True)
party_Identity = Class(name="party::Identity")
party_Organization = Class(name="party::Organization")
party_Tagged = Class(name="party::Tagged", is_abstract=True)
party_Tag = Class(name="party::Tag")
DateEffectiveObject = Class(name="DateEffectiveObject")
party_Phone = Class(name="party::Phone")
ContactInfo = Class(name="ContactInfo")
party_Web = Class(name="party::Web")
URL = Class(name="URL")
party_EMail = Class(name="party::EMail")
party_Address = Class(name="party::Address", is_abstract=True)
party_Custom = Class(name="party::Custom")
party_USAddress = Class(name="party::USAddress")
Address = Class(name="Address")
party_DateEffectiveObject = Class(name="party::DateEffectiveObject", is_abstract=True)
Party = Class(name="Party")
party_MatrixRelationship = Class(name="party::MatrixRelationship")
party_Person = Class(name="party::Person")
party_Role = Class(name="party::Role")
party_CommonObject = Class(name="party::CommonObject", is_abstract=True)
party_URL = Class(name="party::URL", is_abstract=True)

# party_Party class attributes and methods
party_Party_name: Property = Property(name="name", type=StringType)
party_Party_uid: Property = Property(name="uid", type=StringType)
party_Party_m_getPath: Method = Method(name="getPath", parameters={}, type=StringType)
party_Party_m_setExternalParent: Method = Method(name="setExternalParent", parameters={Parameter(name='externalParent')})
party_Party.attributes={party_Party_uid, party_Party_name}
party_Party.methods={party_Party_m_getPath, party_Party_m_setExternalParent}

# Tagged class attributes and methods

# party_ContactInfo class attributes and methods
party_ContactInfo_category: Property = Property(name="category", type=StringType)
party_ContactInfo.attributes={party_ContactInfo_category}

# party_Identity class attributes and methods
party_Identity_type: Property = Property(name="type", type=StringType)
party_Identity_value: Property = Property(name="value", type=StringType)
party_Identity_comment: Property = Property(name="comment", type=StringType)
party_Identity.attributes={party_Identity_comment, party_Identity_type, party_Identity_value}

# party_Organization class attributes and methods
party_Organization_organizationType: Property = Property(name="organizationType", type=StringType)
party_Organization.attributes={party_Organization_organizationType}

# party_Tagged class attributes and methods
party_Tagged_comment: Property = Property(name="comment", type=StringType)
party_Tagged.attributes={party_Tagged_comment}

# party_Tag class attributes and methods
party_Tag_name: Property = Property(name="name", type=StringType)
party_Tag_value: Property = Property(name="value", type=StringType)
party_Tag_comment: Property = Property(name="comment", type=StringType)
party_Tag.attributes={party_Tag_value, party_Tag_name, party_Tag_comment}

# DateEffectiveObject class attributes and methods

# party_Phone class attributes and methods
party_Phone_countryCode: Property = Property(name="countryCode", type=StringType)
party_Phone_areaCode: Property = Property(name="areaCode", type=IntegerType)
party_Phone_number: Property = Property(name="number", type=StringType)
party_Phone.attributes={party_Phone_number, party_Phone_areaCode, party_Phone_countryCode}

# ContactInfo class attributes and methods

# party_Web class attributes and methods

# URL class attributes and methods

# party_EMail class attributes and methods

# party_Address class attributes and methods
party_Address_country: Property = Property(name="country", type=StringType)
party_Address.attributes={party_Address_country}

# party_Custom class attributes and methods
party_Custom_location: Property = Property(name="location", type=StringType)
party_Custom.attributes={party_Custom_location}

# party_USAddress class attributes and methods
party_USAddress_recipient: Property = Property(name="recipient", type=StringType)
party_USAddress_street1: Property = Property(name="street1", type=StringType)
party_USAddress_street2: Property = Property(name="street2", type=StringType)
party_USAddress_city: Property = Property(name="city", type=StringType)
party_USAddress_state: Property = Property(name="state", type=StringType)
party_USAddress_zip: Property = Property(name="zip", type=StringType)
party_USAddress.attributes={party_USAddress_recipient, party_USAddress_city, party_USAddress_street2, party_USAddress_street1, party_USAddress_state, party_USAddress_zip}

# Address class attributes and methods

# party_DateEffectiveObject class attributes and methods
party_DateEffectiveObject_start: Property = Property(name="start", type=DateType)
party_DateEffectiveObject_end: Property = Property(name="end", type=DateType)
party_DateEffectiveObject_m_isEffectiveNow: Method = Method(name="isEffectiveNow", parameters={}, type=BooleanType)
party_DateEffectiveObject_m_isEffective: Method = Method(name="isEffective", parameters={Parameter(name='date')}, type=BooleanType)
party_DateEffectiveObject.attributes={party_DateEffectiveObject_end, party_DateEffectiveObject_start}
party_DateEffectiveObject.methods={party_DateEffectiveObject_m_isEffectiveNow, party_DateEffectiveObject_m_isEffective}

# Party class attributes and methods

# party_MatrixRelationship class attributes and methods
party_MatrixRelationship_name: Property = Property(name="name", type=StringType)
party_MatrixRelationship.attributes={party_MatrixRelationship_name}

# party_Person class attributes and methods
party_Person_title: Property = Property(name="title", type=StringType)
party_Person.attributes={party_Person_title}

# party_Role class attributes and methods
party_Role_name: Property = Property(name="name", type=StringType)
party_Role.attributes={party_Role_name}

# party_CommonObject class attributes and methods

# party_URL class attributes and methods
party_URL_address: Property = Property(name="address", type=StringType)
party_URL.attributes={party_URL_address}

# Relationships
contactInfo0: BinaryAssociation = BinaryAssociation(
    name="contactInfo0",
    ends={
        Property(name="ContactInfo", type=party_Party, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=party_ContactInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identity1: BinaryAssociation = BinaryAssociation(
    name="identity1",
    ends={
        Property(name="party_Identity", type=party_Party, multiplicity=Multiplicity(1, 1)),
        Property(name="party_Party", type=party_Identity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent2: BinaryAssociation = BinaryAssociation(
    name="parent2",
    ends={
        Property(name="Organization", type=party_Party, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=party_Organization, multiplicity=Multiplicity(0, 1))
    }
)
tags3: BinaryAssociation = BinaryAssociation(
    name="tags3",
    ends={
        Property(name="party_Tag", type=party_Tagged, multiplicity=Multiplicity(1, 1)),
        Property(name="party_Tagged", type=party_Tag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner4: BinaryAssociation = BinaryAssociation(
    name="owner4",
    ends={
        Property(name="Party", type=party_ContactInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="contactInfo", type=party_Party, multiplicity=Multiplicity(1, 1))
    }
)
children5: BinaryAssociation = BinaryAssociation(
    name="children5",
    ends={
        Property(name="Party6", type=party_Organization, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=party_Party, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
externalChildren7: BinaryAssociation = BinaryAssociation(
    name="externalChildren7",
    ends={
        Property(name="party_Party8", type=party_Organization, multiplicity=Multiplicity(1, 1)),
        Property(name="party_Organization", type=party_Party, multiplicity=Multiplicity(0, 9999))
    }
)
matrixedChildren9: BinaryAssociation = BinaryAssociation(
    name="matrixedChildren9",
    ends={
        Property(name="party_MatrixRelationship", type=party_Organization, multiplicity=Multiplicity(1, 1)),
        Property(name="party_Organization10", type=party_MatrixRelationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
party11: BinaryAssociation = BinaryAssociation(
    name="party11",
    ends={
        Property(name="party_Party12", type=party_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="party_Role", type=party_Party, multiplicity=Multiplicity(0, 9999))
    }
)
owner13: BinaryAssociation = BinaryAssociation(
    name="owner13",
    ends={
        Property(name="CommonObject", type=party_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="roles", type=party_CommonObject, multiplicity=Multiplicity(0, 1))
    }
)
target16: BinaryAssociation = BinaryAssociation(
    name="target16",
    ends={
        Property(name="party_Party18", type=party_MatrixRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="party_MatrixRelationship17", type=party_Party, multiplicity=Multiplicity(1, 1))
    }
)
roles14: BinaryAssociation = BinaryAssociation(
    name="roles14",
    ends={
        Property(name="Role", type=party_CommonObject, multiplicity=Multiplicity(1, 1)),
        Property(name="owner15", type=party_Role, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_party_Party_Tagged = Generalization(general=Tagged, specific=party_Party)
gen_party_ContactInfo_DateEffectiveObject = Generalization(general=DateEffectiveObject, specific=party_ContactInfo)
gen_party_Phone_ContactInfo = Generalization(general=ContactInfo, specific=party_Phone)
gen_party_Web_URL = Generalization(general=URL, specific=party_Web)
gen_party_EMail_URL = Generalization(general=URL, specific=party_EMail)
gen_party_Address_ContactInfo = Generalization(general=ContactInfo, specific=party_Address)
gen_party_Custom_ContactInfo = Generalization(general=ContactInfo, specific=party_Custom)
gen_party_USAddress_Address = Generalization(general=Address, specific=party_USAddress)
gen_party_DateEffectiveObject_Tagged = Generalization(general=Tagged, specific=party_DateEffectiveObject)
gen_party_Organization_Party = Generalization(general=Party, specific=party_Organization)
gen_party_Person_Party = Generalization(general=Party, specific=party_Person)
gen_party_Role_DateEffectiveObject = Generalization(general=DateEffectiveObject, specific=party_Role)
gen_party_URL_ContactInfo = Generalization(general=ContactInfo, specific=party_URL)
gen_party_MatrixRelationship_DateEffectiveObject = Generalization(general=DateEffectiveObject, specific=party_MatrixRelationship)

# Domain Model
domain_model = DomainModel(
    name="party",
    types={party_Party, Tagged, party_ContactInfo, party_Identity, party_Organization, party_Tagged, party_Tag, DateEffectiveObject, party_Phone, ContactInfo, party_Web, URL, party_EMail, party_Address, party_Custom, party_USAddress, Address, party_DateEffectiveObject, Party, party_MatrixRelationship, party_Person, party_Role, party_CommonObject, party_URL},
    associations={contactInfo0, identity1, parent2, tags3, owner4, children5, externalChildren7, matrixedChildren9, party11, owner13, target16, roles14},
    generalizations={gen_party_Party_Tagged, gen_party_ContactInfo_DateEffectiveObject, gen_party_Phone_ContactInfo, gen_party_Web_URL, gen_party_EMail_URL, gen_party_Address_ContactInfo, gen_party_Custom_ContactInfo, gen_party_USAddress_Address, gen_party_DateEffectiveObject_Tagged, gen_party_Organization_Party, gen_party_Person_Party, gen_party_Role_DateEffectiveObject, gen_party_URL_ContactInfo, gen_party_MatrixRelationship_DateEffectiveObject},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)