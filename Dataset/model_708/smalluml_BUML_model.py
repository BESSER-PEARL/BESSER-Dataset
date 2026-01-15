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
smalluml_Class = Class(name="smalluml::Class")
NamedElement = Class(name="NamedElement")
smalluml_Attribute = Class(name="smalluml::Attribute")
smalluml_Operation = Class(name="smalluml::Operation")
smalluml_Element = Class(name="smalluml::Element")
smalluml_NamedElement = Class(name="smalluml::NamedElement")
Element = Class(name="Element")
Type = Class(name="Type")
smalluml_Type = Class(name="smalluml::Type")
smalluml_BooleanV = Class(name="smalluml::BooleanV")
smalluml_StringV = Class(name="smalluml::StringV")
smalluml_RealV = Class(name="smalluml::RealV")
smalluml_IntegerV = Class(name="smalluml::IntegerV")
smalluml_Enumeration = Class(name="smalluml::Enumeration")
smalluml_Association = Class(name="smalluml::Association")
smalluml_Cardinalite = Class(name="smalluml::Cardinalite")
smalluml_Package = Class(name="smalluml::Package")

# smalluml_Class class attributes and methods

# NamedElement class attributes and methods

# smalluml_Attribute class attributes and methods

# smalluml_Operation class attributes and methods

# smalluml_Element class attributes and methods

# smalluml_NamedElement class attributes and methods
smalluml_NamedElement_Name: Property = Property(name="Name", type=StringType)
smalluml_NamedElement.attributes={smalluml_NamedElement_Name}

# Element class attributes and methods

# Type class attributes and methods

# smalluml_Type class attributes and methods

# smalluml_BooleanV class attributes and methods
smalluml_BooleanV_Value: Property = Property(name="Value", type=StringType)
smalluml_BooleanV.attributes={smalluml_BooleanV_Value}

# smalluml_StringV class attributes and methods
smalluml_StringV_Value: Property = Property(name="Value", type=StringType)
smalluml_StringV.attributes={smalluml_StringV_Value}

# smalluml_RealV class attributes and methods
smalluml_RealV_Value: Property = Property(name="Value", type=StringType)
smalluml_RealV.attributes={smalluml_RealV_Value}

# smalluml_IntegerV class attributes and methods
smalluml_IntegerV_Value: Property = Property(name="Value", type=StringType)
smalluml_IntegerV.attributes={smalluml_IntegerV_Value}

# smalluml_Enumeration class attributes and methods
smalluml_Enumeration_enumValue: Property = Property(name="enumValue", type=StringType)
smalluml_Enumeration.attributes={smalluml_Enumeration_enumValue}

# smalluml_Association class attributes and methods

# smalluml_Cardinalite class attributes and methods
smalluml_Cardinalite_lowerBound: Property = Property(name="lowerBound", type=StringType)
smalluml_Cardinalite_upperBound: Property = Property(name="upperBound", type=StringType)
smalluml_Cardinalite.attributes={smalluml_Cardinalite_upperBound, smalluml_Cardinalite_lowerBound}

# smalluml_Package class attributes and methods

# Relationships
Operations0: BinaryAssociation = BinaryAssociation(
    name="Operations0",
    ends={
        Property(name="smalluml_Operation", type=smalluml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Class", type=smalluml_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Attributes1: BinaryAssociation = BinaryAssociation(
    name="Attributes1",
    ends={
        Property(name="smalluml_Attribute", type=smalluml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Class2", type=smalluml_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
SuperClass4: BinaryAssociation = BinaryAssociation(
    name="SuperClass4",
    ends={
        Property(name="smalluml_Class5", type=smalluml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Class3", type=smalluml_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Type6: BinaryAssociation = BinaryAssociation(
    name="Type6",
    ends={
        Property(name="smalluml_Type", type=smalluml_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Attribute7", type=smalluml_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
To10: BinaryAssociation = BinaryAssociation(
    name="To10",
    ends={
        Property(name="smalluml_Class12", type=smalluml_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Association11", type=smalluml_Class, multiplicity=Multiplicity(1, 1))
    }
)
cardFrom13: BinaryAssociation = BinaryAssociation(
    name="cardFrom13",
    ends={
        Property(name="smalluml_Cardinalite", type=smalluml_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Association14", type=smalluml_Cardinalite, multiplicity=Multiplicity(0, 1))
    }
)
From8: BinaryAssociation = BinaryAssociation(
    name="From8",
    ends={
        Property(name="smalluml_Class9", type=smalluml_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Association", type=smalluml_Class, multiplicity=Multiplicity(1, 1))
    }
)
cardTo15: BinaryAssociation = BinaryAssociation(
    name="cardTo15",
    ends={
        Property(name="smalluml_Association16", type=smalluml_Cardinalite, multiplicity=Multiplicity(0, 1)),
        Property(name="smalluml_Cardinalite17", type=smalluml_Association, multiplicity=Multiplicity(1, 1))
    }
)
listElements18: BinaryAssociation = BinaryAssociation(
    name="listElements18",
    ends={
        Property(name="smalluml_Element", type=smalluml_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Package", type=smalluml_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_smalluml_Class_NamedElement = Generalization(general=NamedElement, specific=smalluml_Class)
gen_smalluml_NamedElement_Element = Generalization(general=Element, specific=smalluml_NamedElement)
gen_smalluml_Operation_NamedElement = Generalization(general=NamedElement, specific=smalluml_Operation)
gen_smalluml_Attribute_Type = Generalization(general=Type, specific=smalluml_Attribute)
gen_smalluml_Type_NamedElement = Generalization(general=NamedElement, specific=smalluml_Type)
gen_smalluml_BooleanV_Type = Generalization(general=Type, specific=smalluml_BooleanV)
gen_smalluml_StringV_Type = Generalization(general=Type, specific=smalluml_StringV)
gen_smalluml_RealV_Type = Generalization(general=Type, specific=smalluml_RealV)
gen_smalluml_IntegerV_Type = Generalization(general=Type, specific=smalluml_IntegerV)
gen_smalluml_Enumeration_NamedElement = Generalization(general=NamedElement, specific=smalluml_Enumeration)
gen_smalluml_Cardinalite_NamedElement = Generalization(general=NamedElement, specific=smalluml_Cardinalite)

# Domain Model
domain_model = DomainModel(
    name="smalluml",
    types={smalluml_Class, NamedElement, smalluml_Attribute, smalluml_Operation, smalluml_Element, smalluml_NamedElement, Element, Type, smalluml_Type, smalluml_BooleanV, smalluml_StringV, smalluml_RealV, smalluml_IntegerV, smalluml_Enumeration, smalluml_Association, smalluml_Cardinalite, smalluml_Package},
    associations={Operations0, Attributes1, SuperClass4, Type6, To10, cardFrom13, From8, cardTo15, listElements18},
    generalizations={gen_smalluml_Class_NamedElement, gen_smalluml_NamedElement_Element, gen_smalluml_Operation_NamedElement, gen_smalluml_Attribute_Type, gen_smalluml_Type_NamedElement, gen_smalluml_BooleanV_Type, gen_smalluml_StringV_Type, gen_smalluml_RealV_Type, gen_smalluml_IntegerV_Type, gen_smalluml_Enumeration_NamedElement, gen_smalluml_Cardinalite_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)