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
EType: Enumeration = Enumeration(
    name="EType",
    literals={
            EnumerationLiteral(name="integer"),
			EnumerationLiteral(name="string")
    }
)

EVisibility: Enumeration = Enumeration(
    name="EVisibility",
    literals={
            EnumerationLiteral(name="public"),
			EnumerationLiteral(name="protected"),
			EnumerationLiteral(name="private")
    }
)

EReturnType: Enumeration = Enumeration(
    name="EReturnType",
    literals={
            EnumerationLiteral(name="void"),
			EnumerationLiteral(name="integer"),
			EnumerationLiteral(name="string")
    }
)

# Classes
NamedElement = Class(name="NamedElement")
myumlclassdiagram_Class = Class(name="myumlclassdiagram::Class")
myumlclassdiagram_Attribute = Class(name="myumlclassdiagram::Attribute")
myumlclassdiagram_Method = Class(name="myumlclassdiagram::Method")
myumlclassdiagram_NamedElement = Class(name="myumlclassdiagram::NamedElement", is_abstract=True)
myumlclassdiagram_Package = Class(name="myumlclassdiagram::Package")
myumlclassdiagram_Parameter = Class(name="myumlclassdiagram::Parameter")

# NamedElement class attributes and methods

# myumlclassdiagram_Class class attributes and methods
myumlclassdiagram_Class_Visibility: Property = Property(name="Visibility", type=StringType)
myumlclassdiagram_Class.attributes={myumlclassdiagram_Class_Visibility}

# myumlclassdiagram_Attribute class attributes and methods
myumlclassdiagram_Attribute_Type: Property = Property(name="Type", type=StringType)
myumlclassdiagram_Attribute_Visibility: Property = Property(name="Visibility", type=StringType)
myumlclassdiagram_Attribute.attributes={myumlclassdiagram_Attribute_Visibility, myumlclassdiagram_Attribute_Type}

# myumlclassdiagram_Method class attributes and methods
myumlclassdiagram_Method_Returns: Property = Property(name="Returns", type=StringType)
myumlclassdiagram_Method_Visibility: Property = Property(name="Visibility", type=StringType)
myumlclassdiagram_Method.attributes={myumlclassdiagram_Method_Visibility, myumlclassdiagram_Method_Returns}

# myumlclassdiagram_NamedElement class attributes and methods
myumlclassdiagram_NamedElement_Name: Property = Property(name="Name", type=StringType)
myumlclassdiagram_NamedElement.attributes={myumlclassdiagram_NamedElement_Name}

# myumlclassdiagram_Package class attributes and methods

# myumlclassdiagram_Parameter class attributes and methods
myumlclassdiagram_Parameter_Type: Property = Property(name="Type", type=StringType)
myumlclassdiagram_Parameter.attributes={myumlclassdiagram_Parameter_Type}

# Relationships
Classes0: BinaryAssociation = BinaryAssociation(
    name="Classes0",
    ends={
        Property(name="myumlclassdiagram_Class", type=myumlclassdiagram_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="myumlclassdiagram_Package", type=myumlclassdiagram_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Attributes1: BinaryAssociation = BinaryAssociation(
    name="Attributes1",
    ends={
        Property(name="Attribute", type=myumlclassdiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Owner", type=myumlclassdiagram_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Methods2: BinaryAssociation = BinaryAssociation(
    name="Methods2",
    ends={
        Property(name="Method", type=myumlclassdiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Owner3", type=myumlclassdiagram_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Owner4: BinaryAssociation = BinaryAssociation(
    name="Owner4",
    ends={
        Property(name="Class", type=myumlclassdiagram_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="Attributes", type=myumlclassdiagram_Class, multiplicity=Multiplicity(1, 1))
    }
)
Parameters5: BinaryAssociation = BinaryAssociation(
    name="Parameters5",
    ends={
        Property(name="Parameter", type=myumlclassdiagram_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="Owner6", type=myumlclassdiagram_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Owner7: BinaryAssociation = BinaryAssociation(
    name="Owner7",
    ends={
        Property(name="Class8", type=myumlclassdiagram_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="Methods", type=myumlclassdiagram_Class, multiplicity=Multiplicity(1, 1))
    }
)
Owner9: BinaryAssociation = BinaryAssociation(
    name="Owner9",
    ends={
        Property(name="Method10", type=myumlclassdiagram_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameters", type=myumlclassdiagram_Method, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_myumlclassdiagram_Package_NamedElement = Generalization(general=NamedElement, specific=myumlclassdiagram_Package)
gen_myumlclassdiagram_Class_NamedElement = Generalization(general=NamedElement, specific=myumlclassdiagram_Class)
gen_myumlclassdiagram_Attribute_NamedElement = Generalization(general=NamedElement, specific=myumlclassdiagram_Attribute)
gen_myumlclassdiagram_Method_NamedElement = Generalization(general=NamedElement, specific=myumlclassdiagram_Method)
gen_myumlclassdiagram_Parameter_NamedElement = Generalization(general=NamedElement, specific=myumlclassdiagram_Parameter)

# Domain Model
domain_model = DomainModel(
    name="myumlclassdiagram",
    types={NamedElement, myumlclassdiagram_Class, myumlclassdiagram_Attribute, myumlclassdiagram_Method, myumlclassdiagram_NamedElement, myumlclassdiagram_Package, myumlclassdiagram_Parameter, EType, EVisibility, EReturnType},
    associations={Classes0, Attributes1, Methods2, Owner4, Parameters5, Owner7, Owner9},
    generalizations={gen_myumlclassdiagram_Package_NamedElement, gen_myumlclassdiagram_Class_NamedElement, gen_myumlclassdiagram_Attribute_NamedElement, gen_myumlclassdiagram_Method_NamedElement, gen_myumlclassdiagram_Parameter_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)