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
SimpleUml_Property = Class(name="SimpleUml::Property")
SimpleUml_Class = Class(name="SimpleUml::Class")
NamedElement = Class(name="NamedElement")
SimpleUml_NamedElement = Class(name="SimpleUml::NamedElement", is_abstract=True)
SimpleUml_Package = Class(name="SimpleUml::Package")

# SimpleUml_Property class attributes and methods
SimpleUml_Property_primitiveType: Property = Property(name="primitiveType", type=StringType)
SimpleUml_Property_isContainment: Property = Property(name="isContainment", type=BooleanType)
SimpleUml_Property.attributes={SimpleUml_Property_primitiveType, SimpleUml_Property_isContainment}

# SimpleUml_Class class attributes and methods

# NamedElement class attributes and methods

# SimpleUml_NamedElement class attributes and methods
SimpleUml_NamedElement_name: Property = Property(name="name", type=StringType)
SimpleUml_NamedElement.attributes={SimpleUml_NamedElement_name}

# SimpleUml_Package class attributes and methods

# Relationships
ownedProperty0: BinaryAssociation = BinaryAssociation(
    name="ownedProperty0",
    ends={
        Property(name="SimpleUml_Property", type=SimpleUml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleUml_Class", type=SimpleUml_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClasses2: BinaryAssociation = BinaryAssociation(
    name="superClasses2",
    ends={
        Property(name="SimpleUml_Class3", type=SimpleUml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleUml_Class1", type=SimpleUml_Class, multiplicity=Multiplicity(0, 9999))
    }
)
complexType4: BinaryAssociation = BinaryAssociation(
    name="complexType4",
    ends={
        Property(name="SimpleUml_Class6", type=SimpleUml_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleUml_Property5", type=SimpleUml_Class, multiplicity=Multiplicity(0, 1))
    }
)
ownedElements7: BinaryAssociation = BinaryAssociation(
    name="ownedElements7",
    ends={
        Property(name="SimpleUml_Class8", type=SimpleUml_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleUml_Package", type=SimpleUml_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_SimpleUml_Property_NamedElement = Generalization(general=NamedElement, specific=SimpleUml_Property)
gen_SimpleUml_Class_NamedElement = Generalization(general=NamedElement, specific=SimpleUml_Class)
gen_SimpleUml_Package_NamedElement = Generalization(general=NamedElement, specific=SimpleUml_Package)

# Domain Model
domain_model = DomainModel(
    name="SimpleUml",
    types={SimpleUml_Property, SimpleUml_Class, NamedElement, SimpleUml_NamedElement, SimpleUml_Package},
    associations={ownedProperty0, superClasses2, complexType4, ownedElements7},
    generalizations={gen_SimpleUml_Property_NamedElement, gen_SimpleUml_Class_NamedElement, gen_SimpleUml_Package_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)