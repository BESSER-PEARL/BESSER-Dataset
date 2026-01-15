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
SimpleUML_Class = Class(name="SimpleUML::Class")
NamedElement = Class(name="NamedElement")
SimpleUML_Property = Class(name="SimpleUML::Property")
SimpleUML_NamedElement = Class(name="SimpleUML::NamedElement", is_abstract=True)
SimpleUML_Package = Class(name="SimpleUML::Package")

# SimpleUML_Class class attributes and methods

# NamedElement class attributes and methods

# SimpleUML_Property class attributes and methods
SimpleUML_Property_primitiveType: Property = Property(name="primitiveType", type=StringType)
SimpleUML_Property_isContainment: Property = Property(name="isContainment", type=BooleanType)
SimpleUML_Property.attributes={SimpleUML_Property_primitiveType, SimpleUML_Property_isContainment}

# SimpleUML_NamedElement class attributes and methods
SimpleUML_NamedElement_name: Property = Property(name="name", type=StringType)
SimpleUML_NamedElement.attributes={SimpleUML_NamedElement_name}

# SimpleUML_Package class attributes and methods

# Relationships
ownedProperty0: BinaryAssociation = BinaryAssociation(
    name="ownedProperty0",
    ends={
        Property(name="SimpleUML_Property", type=SimpleUML_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleUML_Class", type=SimpleUML_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClasses2: BinaryAssociation = BinaryAssociation(
    name="superClasses2",
    ends={
        Property(name="SimpleUML_Class3", type=SimpleUML_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleUML_Class1", type=SimpleUML_Class, multiplicity=Multiplicity(0, 9999))
    }
)
complexType4: BinaryAssociation = BinaryAssociation(
    name="complexType4",
    ends={
        Property(name="SimpleUML_Class6", type=SimpleUML_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleUML_Property5", type=SimpleUML_Class, multiplicity=Multiplicity(0, 1))
    }
)
ownedElements7: BinaryAssociation = BinaryAssociation(
    name="ownedElements7",
    ends={
        Property(name="SimpleUML_Class8", type=SimpleUML_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleUML_Package", type=SimpleUML_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_SimpleUML_Class_NamedElement = Generalization(general=NamedElement, specific=SimpleUML_Class)
gen_SimpleUML_Property_NamedElement = Generalization(general=NamedElement, specific=SimpleUML_Property)
gen_SimpleUML_Package_NamedElement = Generalization(general=NamedElement, specific=SimpleUML_Package)

# Domain Model
domain_model = DomainModel(
    name="SimpleUML",
    types={SimpleUML_Class, NamedElement, SimpleUML_Property, SimpleUML_NamedElement, SimpleUML_Package},
    associations={ownedProperty0, superClasses2, complexType4, ownedElements7},
    generalizations={gen_SimpleUML_Class_NamedElement, gen_SimpleUML_Property_NamedElement, gen_SimpleUML_Package_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)