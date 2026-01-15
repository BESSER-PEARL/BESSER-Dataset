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
smalluml_Type = Class(name="smalluml::Type", is_abstract=True)
NamedElement = Class(name="NamedElement")
smalluml_NamedElement = Class(name="smalluml::NamedElement", is_abstract=True)
smalluml_Enumeration = Class(name="smalluml::Enumeration")
Type = Class(name="Type")
smalluml_EnumerationElement = Class(name="smalluml::EnumerationElement")
smalluml_Class = Class(name="smalluml::Class")
smalluml_Attribute = Class(name="smalluml::Attribute")
smalluml_Method = Class(name="smalluml::Method")
smalluml_Relation = Class(name="smalluml::Relation")
smalluml_Cardinality = Class(name="smalluml::Cardinality")
smalluml_Package = Class(name="smalluml::Package")
smalluml_ConcreteType = Class(name="smalluml::ConcreteType")

# smalluml_Type class attributes and methods

# NamedElement class attributes and methods

# smalluml_NamedElement class attributes and methods
smalluml_NamedElement_name: Property = Property(name="name", type=StringType)
smalluml_NamedElement.attributes={smalluml_NamedElement_name}

# smalluml_Enumeration class attributes and methods

# Type class attributes and methods

# smalluml_EnumerationElement class attributes and methods
smalluml_EnumerationElement_value: Property = Property(name="value", type=StringType)
smalluml_EnumerationElement.attributes={smalluml_EnumerationElement_value}

# smalluml_Class class attributes and methods
smalluml_Class_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
smalluml_Class.attributes={smalluml_Class_isAbstract}

# smalluml_Attribute class attributes and methods

# smalluml_Method class attributes and methods

# smalluml_Relation class attributes and methods

# smalluml_Cardinality class attributes and methods
smalluml_Cardinality_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
smalluml_Cardinality_upperBound: Property = Property(name="upperBound", type=IntegerType)
smalluml_Cardinality.attributes={smalluml_Cardinality_lowerBound, smalluml_Cardinality_upperBound}

# smalluml_Package class attributes and methods

# smalluml_ConcreteType class attributes and methods

# Relationships
parameters9: BinaryAssociation = BinaryAssociation(
    name="parameters9",
    ends={
        Property(name="smalluml_Attribute11", type=smalluml_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Method10", type=smalluml_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value0: BinaryAssociation = BinaryAssociation(
    name="value0",
    ends={
        Property(name="smalluml_EnumerationElement", type=smalluml_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Enumeration", type=smalluml_EnumerationElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
attributes1: BinaryAssociation = BinaryAssociation(
    name="attributes1",
    ends={
        Property(name="smalluml_Attribute", type=smalluml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Class", type=smalluml_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods2: BinaryAssociation = BinaryAssociation(
    name="methods2",
    ends={
        Property(name="smalluml_Method", type=smalluml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Class3", type=smalluml_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parents5: BinaryAssociation = BinaryAssociation(
    name="parents5",
    ends={
        Property(name="smalluml_Class6", type=smalluml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Class4", type=smalluml_Class, multiplicity=Multiplicity(0, 9999))
    }
)
typedValue7: BinaryAssociation = BinaryAssociation(
    name="typedValue7",
    ends={
        Property(name="smalluml_Type", type=smalluml_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Attribute8", type=smalluml_Type, multiplicity=Multiplicity(1, 1))
    }
)
types27: BinaryAssociation = BinaryAssociation(
    name="types27",
    ends={
        Property(name="smalluml_Type29", type=smalluml_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Package28", type=smalluml_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnTypedValue12: BinaryAssociation = BinaryAssociation(
    name="returnTypedValue12",
    ends={
        Property(name="smalluml_Type14", type=smalluml_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Method13", type=smalluml_Type, multiplicity=Multiplicity(1, 1))
    }
)
cardinality15: BinaryAssociation = BinaryAssociation(
    name="cardinality15",
    ends={
        Property(name="smalluml_Cardinality", type=smalluml_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Relation", type=smalluml_Cardinality, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
from16: BinaryAssociation = BinaryAssociation(
    name="from16",
    ends={
        Property(name="smalluml_Class18", type=smalluml_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Relation17", type=smalluml_Class, multiplicity=Multiplicity(1, 1))
    }
)
to19: BinaryAssociation = BinaryAssociation(
    name="to19",
    ends={
        Property(name="smalluml_Class21", type=smalluml_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Relation20", type=smalluml_Class, multiplicity=Multiplicity(1, 1))
    }
)
class22: BinaryAssociation = BinaryAssociation(
    name="class22",
    ends={
        Property(name="smalluml_Class23", type=smalluml_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Package", type=smalluml_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relation24: BinaryAssociation = BinaryAssociation(
    name="relation24",
    ends={
        Property(name="smalluml_Relation26", type=smalluml_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Package25", type=smalluml_Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_smalluml_Type_NamedElement = Generalization(general=NamedElement, specific=smalluml_Type)
gen_smalluml_Enumeration_Type = Generalization(general=Type, specific=smalluml_Enumeration)
gen_smalluml_Class_NamedElement = Generalization(general=NamedElement, specific=smalluml_Class)
gen_smalluml_Attribute_NamedElement = Generalization(general=NamedElement, specific=smalluml_Attribute)
gen_smalluml_Method_NamedElement = Generalization(general=NamedElement, specific=smalluml_Method)
gen_smalluml_Relation_NamedElement = Generalization(general=NamedElement, specific=smalluml_Relation)
gen_smalluml_ConcreteType_Type = Generalization(general=Type, specific=smalluml_ConcreteType)

# Domain Model
domain_model = DomainModel(
    name="smalluml",
    types={smalluml_Type, NamedElement, smalluml_NamedElement, smalluml_Enumeration, Type, smalluml_EnumerationElement, smalluml_Class, smalluml_Attribute, smalluml_Method, smalluml_Relation, smalluml_Cardinality, smalluml_Package, smalluml_ConcreteType},
    associations={parameters9, value0, attributes1, methods2, parents5, typedValue7, types27, returnTypedValue12, cardinality15, from16, to19, class22, relation24},
    generalizations={gen_smalluml_Type_NamedElement, gen_smalluml_Enumeration_Type, gen_smalluml_Class_NamedElement, gen_smalluml_Attribute_NamedElement, gen_smalluml_Method_NamedElement, gen_smalluml_Relation_NamedElement, gen_smalluml_ConcreteType_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)