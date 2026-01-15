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
Sex: Enumeration = Enumeration(
    name="Sex",
    literals={
            EnumerationLiteral(name="MALE"),
			EnumerationLiteral(name="FEMALE")
    }
)

# Classes
model_ETypes = Class(name="model::ETypes")
model_User = Class(name="model::User")
model_Address = Class(name="model::Address")
model_PrimaryObject = Class(name="model::PrimaryObject")
model_TargetObject = Class(name="model::TargetObject")
model_ObjectWithMap = Class(name="model::ObjectWithMap")
model_EStringToStringMapEntry = Class(name="model::EStringToStringMapEntry")
model_Container = Class(name="model::Container")
model_AbstractType = Class(name="model::AbstractType", is_abstract=True)
model_ConcreteTypeOne = Class(name="model::ConcreteTypeOne")
AbstractType = Class(name="AbstractType")
model_ConcreteTypeTwo = Class(name="model::ConcreteTypeTwo")
model_Node = Class(name="model::Node")

# model_ETypes class attributes and methods
model_ETypes_eString: Property = Property(name="eString", type=StringType)
model_ETypes_eStrings: Property = Property(name="eStrings", type=StringType)
model_ETypes_eBoolean: Property = Property(name="eBoolean", type=BooleanType)
model_ETypes_eBooleans: Property = Property(name="eBooleans", type=StringType)
model_ETypes_eInt: Property = Property(name="eInt", type=IntegerType)
model_ETypes_eInts: Property = Property(name="eInts", type=IntegerType)
model_ETypes_doubleValue: Property = Property(name="doubleValue", type=StringType)
model_ETypes_eDouble: Property = Property(name="eDouble", type=FloatType)
model_ETypes_eDoubles: Property = Property(name="eDoubles", type=StringType)
model_ETypes_eByte: Property = Property(name="eByte", type=StringType)
model_ETypes_eByteArray: Property = Property(name="eByteArray", type=StringType)
model_ETypes_eChar: Property = Property(name="eChar", type=StringType)
model_ETypes_eDate: Property = Property(name="eDate", type=DateType)
model_ETypes_eFloat: Property = Property(name="eFloat", type=FloatType)
model_ETypes_eLong: Property = Property(name="eLong", type=StringType)
model_ETypes_eShort: Property = Property(name="eShort", type=StringType)
model_ETypes_uris: Property = Property(name="uris", type=StringType)
model_ETypes.attributes={model_ETypes_eByteArray, model_ETypes_eStrings, model_ETypes_eFloat, model_ETypes_eShort, model_ETypes_eString, model_ETypes_eBoolean, model_ETypes_eInts, model_ETypes_doubleValue, model_ETypes_eInt, model_ETypes_eDouble, model_ETypes_eDoubles, model_ETypes_eLong, model_ETypes_eDate, model_ETypes_eByte, model_ETypes_eChar, model_ETypes_eBooleans, model_ETypes_uris}

# model_User class attributes and methods
model_User_userId: Property = Property(name="userId", type=StringType)
model_User_name: Property = Property(name="name", type=StringType)
model_User_birthDate: Property = Property(name="birthDate", type=DateType)
model_User_sex: Property = Property(name="sex", type=StringType)
model_User.attributes={model_User_birthDate, model_User_name, model_User_userId, model_User_sex}

# model_Address class attributes and methods
model_Address_street: Property = Property(name="street", type=StringType)
model_Address_number: Property = Property(name="number", type=StringType)
model_Address_addId: Property = Property(name="addId", type=StringType)
model_Address_city: Property = Property(name="city", type=StringType)
model_Address.attributes={model_Address_addId, model_Address_city, model_Address_street, model_Address_number}

# model_PrimaryObject class attributes and methods
model_PrimaryObject_featureMapReferenceCollection: Property = Property(name="featureMapReferenceCollection", type=StringType)
model_PrimaryObject_name: Property = Property(name="name", type=StringType)
model_PrimaryObject_idAttribute: Property = Property(name="idAttribute", type=StringType)
model_PrimaryObject_unsettableAttribute: Property = Property(name="unsettableAttribute", type=StringType)
model_PrimaryObject_unsettableAttributeWithNonNullDefault: Property = Property(name="unsettableAttributeWithNonNullDefault", type=StringType)
model_PrimaryObject_featureMapAttributeType1: Property = Property(name="featureMapAttributeType1", type=StringType)
model_PrimaryObject_featureMapAttributeType2: Property = Property(name="featureMapAttributeType2", type=StringType)
model_PrimaryObject_featureMapAttributeCollection: Property = Property(name="featureMapAttributeCollection", type=StringType)
model_PrimaryObject.attributes={model_PrimaryObject_name, model_PrimaryObject_featureMapAttributeCollection, model_PrimaryObject_featureMapAttributeType2, model_PrimaryObject_idAttribute, model_PrimaryObject_featureMapAttributeType1, model_PrimaryObject_unsettableAttribute, model_PrimaryObject_featureMapReferenceCollection, model_PrimaryObject_unsettableAttributeWithNonNullDefault}

# model_TargetObject class attributes and methods
model_TargetObject_singleAttribute: Property = Property(name="singleAttribute", type=StringType)
model_TargetObject_arrayAttribute: Property = Property(name="arrayAttribute", type=StringType)
model_TargetObject.attributes={model_TargetObject_arrayAttribute, model_TargetObject_singleAttribute}

# model_ObjectWithMap class attributes and methods

# model_EStringToStringMapEntry class attributes and methods

# model_Container class attributes and methods

# model_AbstractType class attributes and methods
model_AbstractType_name: Property = Property(name="name", type=StringType)
model_AbstractType.attributes={model_AbstractType_name}

# model_ConcreteTypeOne class attributes and methods
model_ConcreteTypeOne_propTypeOne: Property = Property(name="propTypeOne", type=StringType)
model_ConcreteTypeOne.attributes={model_ConcreteTypeOne_propTypeOne}

# AbstractType class attributes and methods

# model_ConcreteTypeTwo class attributes and methods
model_ConcreteTypeTwo_propTypeTwo: Property = Property(name="propTypeTwo", type=StringType)
model_ConcreteTypeTwo.attributes={model_ConcreteTypeTwo_propTypeTwo}

# model_Node class attributes and methods
model_Node_label: Property = Property(name="label", type=StringType)
model_Node.attributes={model_Node_label}

# Relationships
friends1: BinaryAssociation = BinaryAssociation(
    name="friends1",
    ends={
        Property(name="model_User", type=model_User, multiplicity=Multiplicity(1, 1)),
        Property(name="model_User0", type=model_User, multiplicity=Multiplicity(0, 9999))
    }
)
uniqueFriend3: BinaryAssociation = BinaryAssociation(
    name="uniqueFriend3",
    ends={
        Property(name="model_User4", type=model_User, multiplicity=Multiplicity(1, 1)),
        Property(name="model_User2", type=model_User, multiplicity=Multiplicity(0, 1))
    }
)
address5: BinaryAssociation = BinaryAssociation(
    name="address5",
    ends={
        Property(name="model_Address", type=model_User, multiplicity=Multiplicity(1, 1)),
        Property(name="model_User6", type=model_Address, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
singleNonContainmentReferenceNoProxies29: BinaryAssociation = BinaryAssociation(
    name="singleNonContainmentReferenceNoProxies29",
    ends={
        Property(name="model_TargetObject31", type=model_PrimaryObject, multiplicity=Multiplicity(1, 1)),
        Property(name="model_PrimaryObject30", type=model_TargetObject, multiplicity=Multiplicity(0, 1))
    }
)
featureMapReferenceType132: BinaryAssociation = BinaryAssociation(
    name="featureMapReferenceType132",
    ends={
        Property(name="model_TargetObject34", type=model_PrimaryObject, multiplicity=Multiplicity(1, 1)),
        Property(name="model_PrimaryObject33", type=model_TargetObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featureMapReferenceType235: BinaryAssociation = BinaryAssociation(
    name="featureMapReferenceType235",
    ends={
        Property(name="model_TargetObject37", type=model_PrimaryObject, multiplicity=Multiplicity(1, 1)),
        Property(name="model_PrimaryObject36", type=model_TargetObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unsettableReference7: BinaryAssociation = BinaryAssociation(
    name="unsettableReference7",
    ends={
        Property(name="model_TargetObject", type=model_PrimaryObject, multiplicity=Multiplicity(1, 1)),
        Property(name="model_PrimaryObject", type=model_TargetObject, multiplicity=Multiplicity(0, 1))
    }
)
containmentReferenceSameCollectioin9: BinaryAssociation = BinaryAssociation(
    name="containmentReferenceSameCollectioin9",
    ends={
        Property(name="model_PrimaryObject10", type=model_PrimaryObject, multiplicity=Multiplicity(1, 1)),
        Property(name="model_PrimaryObject8", type=model_PrimaryObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
singleNonContainmentReference11: BinaryAssociation = BinaryAssociation(
    name="singleNonContainmentReference11",
    ends={
        Property(name="model_TargetObject13", type=model_PrimaryObject, multiplicity=Multiplicity(1, 1)),
        Property(name="model_PrimaryObject12", type=model_TargetObject, multiplicity=Multiplicity(0, 1))
    }
)
multipleNonContainmentReference14: BinaryAssociation = BinaryAssociation(
    name="multipleNonContainmentReference14",
    ends={
        Property(name="model_TargetObject16", type=model_PrimaryObject, multiplicity=Multiplicity(1, 1)),
        Property(name="model_PrimaryObject15", type=model_TargetObject, multiplicity=Multiplicity(0, 9999))
    }
)
singleContainmentReferenceNoProxies17: BinaryAssociation = BinaryAssociation(
    name="singleContainmentReferenceNoProxies17",
    ends={
        Property(name="model_TargetObject19", type=model_PrimaryObject, multiplicity=Multiplicity(1, 1)),
        Property(name="model_PrimaryObject18", type=model_TargetObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multipleContainmentReferenceNoProxies20: BinaryAssociation = BinaryAssociation(
    name="multipleContainmentReferenceNoProxies20",
    ends={
        Property(name="model_TargetObject22", type=model_PrimaryObject, multiplicity=Multiplicity(1, 1)),
        Property(name="model_PrimaryObject21", type=model_TargetObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
singleContainmentReferenceProxies23: BinaryAssociation = BinaryAssociation(
    name="singleContainmentReferenceProxies23",
    ends={
        Property(name="model_TargetObject25", type=model_PrimaryObject, multiplicity=Multiplicity(1, 1)),
        Property(name="model_PrimaryObject24", type=model_TargetObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multipleContainmentReferenceProxies26: BinaryAssociation = BinaryAssociation(
    name="multipleContainmentReferenceProxies26",
    ends={
        Property(name="model_TargetObject28", type=model_PrimaryObject, multiplicity=Multiplicity(1, 1)),
        Property(name="model_PrimaryObject27", type=model_TargetObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uniqueChild53: BinaryAssociation = BinaryAssociation(
    name="uniqueChild53",
    ends={
        Property(name="model_Node54", type=model_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Node52", type=model_Node, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries55: BinaryAssociation = BinaryAssociation(
    name="entries55",
    ends={
        Property(name="model_EStringToStringMapEntry", type=model_ObjectWithMap, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ObjectWithMap", type=model_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependencies56: BinaryAssociation = BinaryAssociation(
    name="dependencies56",
    ends={
        Property(name="model_EStringToStringMapEntry58", type=model_ObjectWithMap, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ObjectWithMap57", type=model_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements38: BinaryAssociation = BinaryAssociation(
    name="elements38",
    ends={
        Property(name="model_AbstractType", type=model_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Container", type=model_AbstractType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refProperty40: BinaryAssociation = BinaryAssociation(
    name="refProperty40",
    ends={
        Property(name="model_AbstractType41", type=model_AbstractType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_AbstractType39", type=model_AbstractType, multiplicity=Multiplicity(0, 9999))
    }
)
target43: BinaryAssociation = BinaryAssociation(
    name="target43",
    ends={
        Property(name="Node", type=model_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=model_Node, multiplicity=Multiplicity(0, 1))
    }
)
source45: BinaryAssociation = BinaryAssociation(
    name="source45",
    ends={
        Property(name="Node46", type=model_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=model_Node, multiplicity=Multiplicity(0, 1))
    }
)
manyRef48: BinaryAssociation = BinaryAssociation(
    name="manyRef48",
    ends={
        Property(name="model_Node", type=model_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Node47", type=model_Node, multiplicity=Multiplicity(0, 9999))
    }
)
child50: BinaryAssociation = BinaryAssociation(
    name="child50",
    ends={
        Property(name="model_Node51", type=model_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Node49", type=model_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_model_ConcreteTypeOne_AbstractType = Generalization(general=AbstractType, specific=model_ConcreteTypeOne)
gen_model_ConcreteTypeTwo_AbstractType = Generalization(general=AbstractType, specific=model_ConcreteTypeTwo)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_ETypes, model_User, model_Address, model_PrimaryObject, model_TargetObject, model_ObjectWithMap, model_EStringToStringMapEntry, model_Container, model_AbstractType, model_ConcreteTypeOne, AbstractType, model_ConcreteTypeTwo, model_Node, Sex},
    associations={friends1, uniqueFriend3, address5, singleNonContainmentReferenceNoProxies29, featureMapReferenceType132, featureMapReferenceType235, unsettableReference7, containmentReferenceSameCollectioin9, singleNonContainmentReference11, multipleNonContainmentReference14, singleContainmentReferenceNoProxies17, multipleContainmentReferenceNoProxies20, singleContainmentReferenceProxies23, multipleContainmentReferenceProxies26, uniqueChild53, entries55, dependencies56, elements38, refProperty40, target43, source45, manyRef48, child50},
    generalizations={gen_model_ConcreteTypeOne_AbstractType, gen_model_ConcreteTypeTwo_AbstractType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)