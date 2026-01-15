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
SWMLTypes: Enumeration = Enumeration(
    name="SWMLTypes",
    literals={
            EnumerationLiteral(name="String"),
			EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="Float"),
			EnumerationLiteral(name="Email"),
			EnumerationLiteral(name="Boolean")
    }
)

# Classes
sWML_WebModel = Class(name="sWML::WebModel")
sWML_HypertextLayer = Class(name="sWML::HypertextLayer")
sWML_ContentLayer = Class(name="sWML::ContentLayer")
sWML_IndexPage = Class(name="sWML::IndexPage")
sWML_Class = Class(name="sWML::Class")
sWML_Attribute = Class(name="sWML::Attribute")

# sWML_WebModel class attributes and methods
sWML_WebModel_name: Property = Property(name="name", type=StringType)
sWML_WebModel.attributes={sWML_WebModel_name}

# sWML_HypertextLayer class attributes and methods

# sWML_ContentLayer class attributes and methods

# sWML_IndexPage class attributes and methods
sWML_IndexPage_name: Property = Property(name="name", type=StringType)
sWML_IndexPage_size: Property = Property(name="size", type=IntegerType)
sWML_IndexPage.attributes={sWML_IndexPage_size, sWML_IndexPage_name}

# sWML_Class class attributes and methods
sWML_Class_name: Property = Property(name="name", type=StringType)
sWML_Class.attributes={sWML_Class_name}

# sWML_Attribute class attributes and methods
sWML_Attribute_name: Property = Property(name="name", type=StringType)
sWML_Attribute_type: Property = Property(name="type", type=StringType)
sWML_Attribute.attributes={sWML_Attribute_name, sWML_Attribute_type}

# Relationships
hypertext0: BinaryAssociation = BinaryAssociation(
    name="hypertext0",
    ends={
        Property(name="sWML_HypertextLayer", type=sWML_WebModel, multiplicity=Multiplicity(1, 1)),
        Property(name="sWML_WebModel", type=sWML_HypertextLayer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
content1: BinaryAssociation = BinaryAssociation(
    name="content1",
    ends={
        Property(name="sWML_ContentLayer", type=sWML_WebModel, multiplicity=Multiplicity(1, 1)),
        Property(name="sWML_WebModel2", type=sWML_ContentLayer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pages3: BinaryAssociation = BinaryAssociation(
    name="pages3",
    ends={
        Property(name="sWML_IndexPage", type=sWML_HypertextLayer, multiplicity=Multiplicity(1, 1)),
        Property(name="sWML_HypertextLayer4", type=sWML_IndexPage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
displayedClass5: BinaryAssociation = BinaryAssociation(
    name="displayedClass5",
    ends={
        Property(name="sWML_Class", type=sWML_IndexPage, multiplicity=Multiplicity(1, 1)),
        Property(name="sWML_IndexPage6", type=sWML_Class, multiplicity=Multiplicity(0, 1))
    }
)
classes7: BinaryAssociation = BinaryAssociation(
    name="classes7",
    ends={
        Property(name="sWML_Class9", type=sWML_ContentLayer, multiplicity=Multiplicity(1, 1)),
        Property(name="sWML_ContentLayer8", type=sWML_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes10: BinaryAssociation = BinaryAssociation(
    name="attributes10",
    ends={
        Property(name="sWML_Attribute", type=sWML_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="sWML_Class11", type=sWML_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="sWML",
    types={sWML_WebModel, sWML_HypertextLayer, sWML_ContentLayer, sWML_IndexPage, sWML_Class, sWML_Attribute, SWMLTypes},
    associations={hypertext0, content1, pages3, displayedClass5, classes7, attributes10},
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