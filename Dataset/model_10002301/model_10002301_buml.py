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
JObject = Class(name="JObject")
JMember = Class(name="JMember")
JBool = Class(name="JBool")
JNum = Class(name="JNum")
JStr = Class(name="JStr")
JNull = Class(name="JNull")
JArray = Class(name="JArray")
JValue_Interface = Class(name="JValue_Interface")
State_Interface = Class(name="State_Interface")
Wait = Class(name="Wait")
Protraction = Class(name="Protraction")
Retraction = Class(name="Retraction")
Contexte = Class(name="Contexte")
JValueVisitor_Interface = Class(name="JValueVisitor_Interface")
JValueJSONPrintVisitor = Class(name="JValueJSONPrintVisitor")

# JObject class attributes and methods

# JMember class attributes and methods
JMember_nom: Property = Property(name="nom", type=StringType)
JMember.attributes={JMember_nom}

# JBool class attributes and methods
JBool_value: Property = Property(name="value", type=BooleanType)
JBool.attributes={JBool_value}

# JNum class attributes and methods
JNum_value: Property = Property(name="value", type=IntegerType)
JNum.attributes={JNum_value}

# JStr class attributes and methods
JStr_value: Property = Property(name="value", type=StringType)
JStr.attributes={JStr_value}

# JNull class attributes and methods
JNull_value: Property = Property(name="value", type=StringType)
JNull.attributes={JNull_value}

# JArray class attributes and methods
JArray_value: Property = Property(name="value", type=StringType)
JArray.attributes={JArray_value}

# JValue_Interface class attributes and methods

# State_Interface class attributes and methods

# Wait class attributes and methods

# Protraction class attributes and methods

# Retraction class attributes and methods

# Contexte class attributes and methods

# JValueVisitor_Interface class attributes and methods

# JValueJSONPrintVisitor class attributes and methods

# Relationships
JObject_JMember: BinaryAssociation = BinaryAssociation(
    name="JObject_JMember",
    ends={
        Property(name="JObject_JMember_00", type=JMember, multiplicity=Multiplicity(0, 9999)),
        Property(name="JObject_JMember_11", type=JObject, multiplicity=Multiplicity(1, 1))
    }
)
JMember_JValue: BinaryAssociation = BinaryAssociation(
    name="JMember_JValue",
    ends={
        Property(name="jValue2", type=JValue_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="jMember3", type=JMember, multiplicity=Multiplicity(0, 1))
    }
)
JArray_JValue: BinaryAssociation = BinaryAssociation(
    name="JArray_JValue",
    ends={
        Property(name="value4", type=JValue_Interface, multiplicity=Multiplicity(0, 9999)),
        Property(name="jArray5", type=JArray, multiplicity=Multiplicity(0, 1))
    }
)
Contexte_State: BinaryAssociation = BinaryAssociation(
    name="Contexte_State",
    ends={
        Property(name="state6", type=State_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="contexte7", type=Contexte, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="a53add74_589c_429d_989a_a697b115620e",
    types={JObject, JMember, JBool, JNum, JStr, JNull, JArray, JValue_Interface, State_Interface, Wait, Protraction, Retraction, Contexte, JValueVisitor_Interface, JValueJSONPrintVisitor},
    associations={JObject_JMember, JMember_JValue, JArray_JValue, Contexte_State},
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