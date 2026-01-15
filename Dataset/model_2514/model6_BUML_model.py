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
MyEnum: Enumeration = Enumeration(
    name="MyEnum",
    literals={
            EnumerationLiteral(name="ZERO"),
			EnumerationLiteral(name="ONE"),
			EnumerationLiteral(name="TWO"),
			EnumerationLiteral(name="THREE")
    }
)

# Classes
model6_Root = Class(name="model6::Root")
model6_BaseObject = Class(name="model6::BaseObject")
model6_ReferenceObject = Class(name="model6::ReferenceObject")
BaseObject = Class(name="BaseObject")
model6_ContainmentObject = Class(name="model6::ContainmentObject")
model6_UnorderedList = Class(name="model6::UnorderedList")
model6_PropertiesMap = Class(name="model6::PropertiesMap")
model6_PropertiesMapEntry = Class(name="model6::PropertiesMapEntry")
model6_PropertiesMapEntryValue = Class(name="model6::PropertiesMapEntryValue")
model6_A = Class(name="model6::A")
model6_D = Class(name="model6::D")
model6_B = Class(name="model6::B")
model6_C = Class(name="model6::C")
model6_EObject = Class(name="model6::EObject")
model6_E = Class(name="model6::E")
model6_F = Class(name="model6::F")
model6_G = Class(name="model6::G")
model6_MyEnumList = Class(name="model6::MyEnumList")
model6_MyEnumListUnsettable = Class(name="model6::MyEnumListUnsettable")

# model6_Root class attributes and methods

# model6_BaseObject class attributes and methods
model6_BaseObject_attributeOptional: Property = Property(name="attributeOptional", type=StringType)
model6_BaseObject_attributeRequired: Property = Property(name="attributeRequired", type=StringType)
model6_BaseObject_attributeList: Property = Property(name="attributeList", type=StringType)
model6_BaseObject.attributes={model6_BaseObject_attributeList, model6_BaseObject_attributeOptional, model6_BaseObject_attributeRequired}

# model6_ReferenceObject class attributes and methods

# BaseObject class attributes and methods

# model6_ContainmentObject class attributes and methods

# model6_UnorderedList class attributes and methods

# model6_PropertiesMap class attributes and methods
model6_PropertiesMap_label: Property = Property(name="label", type=StringType)
model6_PropertiesMap.attributes={model6_PropertiesMap_label}

# model6_PropertiesMapEntry class attributes and methods
model6_PropertiesMapEntry_key: Property = Property(name="key", type=StringType)
model6_PropertiesMapEntry.attributes={model6_PropertiesMapEntry_key}

# model6_PropertiesMapEntryValue class attributes and methods
model6_PropertiesMapEntryValue_label: Property = Property(name="label", type=StringType)
model6_PropertiesMapEntryValue.attributes={model6_PropertiesMapEntryValue_label}

# model6_A class attributes and methods

# model6_D class attributes and methods

# model6_B class attributes and methods

# model6_C class attributes and methods

# model6_EObject class attributes and methods

# model6_E class attributes and methods

# model6_F class attributes and methods

# model6_G class attributes and methods
model6_G_dummy: Property = Property(name="dummy", type=StringType)
model6_G_m_isAttributeModified: Method = Method(name="isAttributeModified", parameters={}, type=BooleanType)
model6_G_m_isReferenceModified: Method = Method(name="isReferenceModified", parameters={}, type=BooleanType)
model6_G_m_isListModified: Method = Method(name="isListModified", parameters={}, type=BooleanType)
model6_G.attributes={model6_G_dummy}
model6_G.methods={model6_G_m_isAttributeModified, model6_G_m_isReferenceModified, model6_G_m_isListModified}

# model6_MyEnumList class attributes and methods
model6_MyEnumList_myEnum: Property = Property(name="myEnum", type=StringType)
model6_MyEnumList.attributes={model6_MyEnumList_myEnum}

# model6_MyEnumListUnsettable class attributes and methods
model6_MyEnumListUnsettable_myEnum: Property = Property(name="myEnum", type=StringType)
model6_MyEnumListUnsettable.attributes={model6_MyEnumListUnsettable_myEnum}

# Relationships
listD7: BinaryAssociation = BinaryAssociation(
    name="listD7",
    ends={
        Property(name="model6_Root8", type=model6_BaseObject, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="model6_BaseObject9", type=model6_Root, multiplicity=Multiplicity(1, 1))
    }
)
listA0: BinaryAssociation = BinaryAssociation(
    name="listA0",
    ends={
        Property(name="model6_BaseObject", type=model6_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="model6_Root", type=model6_BaseObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listB1: BinaryAssociation = BinaryAssociation(
    name="listB1",
    ends={
        Property(name="model6_BaseObject3", type=model6_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="model6_Root2", type=model6_BaseObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listC4: BinaryAssociation = BinaryAssociation(
    name="listC4",
    ends={
        Property(name="model6_BaseObject6", type=model6_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="model6_Root5", type=model6_BaseObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referenced23: BinaryAssociation = BinaryAssociation(
    name="referenced23",
    ends={
        Property(name="model6_UnorderedList24", type=model6_UnorderedList, multiplicity=Multiplicity(1, 1)),
        Property(name="model6_UnorderedList22", type=model6_UnorderedList, multiplicity=Multiplicity(0, 9999))
    }
)
referenceOptional10: BinaryAssociation = BinaryAssociation(
    name="referenceOptional10",
    ends={
        Property(name="model6_BaseObject11", type=model6_ReferenceObject, multiplicity=Multiplicity(1, 1)),
        Property(name="model6_ReferenceObject", type=model6_BaseObject, multiplicity=Multiplicity(0, 1))
    }
)
referenceList12: BinaryAssociation = BinaryAssociation(
    name="referenceList12",
    ends={
        Property(name="model6_BaseObject14", type=model6_ReferenceObject, multiplicity=Multiplicity(1, 1)),
        Property(name="model6_ReferenceObject13", type=model6_BaseObject, multiplicity=Multiplicity(0, 9999))
    }
)
containmentOptional15: BinaryAssociation = BinaryAssociation(
    name="containmentOptional15",
    ends={
        Property(name="model6_BaseObject16", type=model6_ContainmentObject, multiplicity=Multiplicity(1, 1)),
        Property(name="model6_ContainmentObject", type=model6_BaseObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containmentList17: BinaryAssociation = BinaryAssociation(
    name="containmentList17",
    ends={
        Property(name="model6_BaseObject19", type=model6_ContainmentObject, multiplicity=Multiplicity(1, 1)),
        Property(name="model6_ContainmentObject18", type=model6_BaseObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contained21: BinaryAssociation = BinaryAssociation(
    name="contained21",
    ends={
        Property(name="model6_UnorderedList", type=model6_UnorderedList, multiplicity=Multiplicity(1, 1)),
        Property(name="model6_UnorderedList20", type=model6_UnorderedList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedC34: BinaryAssociation = BinaryAssociation(
    name="ownedC34",
    ends={
        Property(name="model6_B35", type=model6_C, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="model6_C", type=model6_B, multiplicity=Multiplicity(1, 1))
    }
)
persistentMap25: BinaryAssociation = BinaryAssociation(
    name="persistentMap25",
    ends={
        Property(name="model6_PropertiesMapEntry", type=model6_PropertiesMap, multiplicity=Multiplicity(1, 1)),
        Property(name="model6_PropertiesMap", type=model6_PropertiesMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transientMap26: BinaryAssociation = BinaryAssociation(
    name="transientMap26",
    ends={
        Property(name="model6_PropertiesMapEntry28", type=model6_PropertiesMap, multiplicity=Multiplicity(1, 1)),
        Property(name="model6_PropertiesMap27", type=model6_PropertiesMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value29: BinaryAssociation = BinaryAssociation(
    name="value29",
    ends={
        Property(name="model6_PropertiesMapEntryValue", type=model6_PropertiesMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="model6_PropertiesMapEntry30", type=model6_PropertiesMapEntryValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedDs31: BinaryAssociation = BinaryAssociation(
    name="ownedDs31",
    ends={
        Property(name="model6_D", type=model6_A, multiplicity=Multiplicity(1, 1)),
        Property(name="model6_A", type=model6_D, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBs32: BinaryAssociation = BinaryAssociation(
    name="ownedBs32",
    ends={
        Property(name="model6_B", type=model6_A, multiplicity=Multiplicity(1, 1)),
        Property(name="model6_A33", type=model6_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
data36: BinaryAssociation = BinaryAssociation(
    name="data36",
    ends={
        Property(name="model6_EObject", type=model6_D, multiplicity=Multiplicity(1, 1)),
        Property(name="model6_D37", type=model6_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedAs38: BinaryAssociation = BinaryAssociation(
    name="ownedAs38",
    ends={
        Property(name="model6_A39", type=model6_E, multiplicity=Multiplicity(1, 1)),
        Property(name="model6_E", type=model6_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEs40: BinaryAssociation = BinaryAssociation(
    name="ownedEs40",
    ends={
        Property(name="model6_E41", type=model6_F, multiplicity=Multiplicity(1, 1)),
        Property(name="model6_F", type=model6_E, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reference42: BinaryAssociation = BinaryAssociation(
    name="reference42",
    ends={
        Property(name="model6_BaseObject43", type=model6_G, multiplicity=Multiplicity(1, 1)),
        Property(name="model6_G", type=model6_BaseObject, multiplicity=Multiplicity(1, 1))
    }
)
list44: BinaryAssociation = BinaryAssociation(
    name="list44",
    ends={
        Property(name="model6_BaseObject46", type=model6_G, multiplicity=Multiplicity(1, 1)),
        Property(name="model6_G45", type=model6_BaseObject, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_model6_ReferenceObject_BaseObject = Generalization(general=BaseObject, specific=model6_ReferenceObject)
gen_model6_ContainmentObject_BaseObject = Generalization(general=BaseObject, specific=model6_ContainmentObject)

# Domain Model
domain_model = DomainModel(
    name="model6",
    types={model6_Root, model6_BaseObject, model6_ReferenceObject, BaseObject, model6_ContainmentObject, model6_UnorderedList, model6_PropertiesMap, model6_PropertiesMapEntry, model6_PropertiesMapEntryValue, model6_A, model6_D, model6_B, model6_C, model6_EObject, model6_E, model6_F, model6_G, model6_MyEnumList, model6_MyEnumListUnsettable, MyEnum},
    associations={listD7, listA0, listB1, listC4, referenced23, referenceOptional10, referenceList12, containmentOptional15, containmentList17, contained21, ownedC34, persistentMap25, transientMap26, value29, ownedDs31, ownedBs32, data36, ownedAs38, ownedEs40, reference42, list44},
    generalizations={gen_model6_ReferenceObject_BaseObject, gen_model6_ContainmentObject_BaseObject},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)