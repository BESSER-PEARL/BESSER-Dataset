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
uml_Association = Class(name="uml::Association")
NamedElement = Class(name="NamedElement")
uml_Class = Class(name="uml::Class")
uml_Attribute = Class(name="uml::Attribute")
uml_UMLSpecification = Class(name="uml::UMLSpecification")
uml_NamedElement = Class(name="uml::NamedElement", is_abstract=True)

# uml_Association class attributes and methods

# NamedElement class attributes and methods

# uml_Class class attributes and methods

# uml_Attribute class attributes and methods

# uml_UMLSpecification class attributes and methods

# uml_NamedElement class attributes and methods
uml_NamedElement_name: Property = Property(name="name", type=StringType)
uml_NamedElement.attributes={uml_NamedElement_name}

# Relationships
src0: BinaryAssociation = BinaryAssociation(
    name="src0",
    ends={
        Property(name="uml_Class", type=uml_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Association", type=uml_Class, multiplicity=Multiplicity(0, 1))
    }
)
dst1: BinaryAssociation = BinaryAssociation(
    name="dst1",
    ends={
        Property(name="uml_Class3", type=uml_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Association2", type=uml_Class, multiplicity=Multiplicity(0, 1))
    }
)
attrs7: BinaryAssociation = BinaryAssociation(
    name="attrs7",
    ends={
        Property(name="uml_Attribute", type=uml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Class8", type=uml_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type9: BinaryAssociation = BinaryAssociation(
    name="type9",
    ends={
        Property(name="uml_Class11", type=uml_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Attribute10", type=uml_Class, multiplicity=Multiplicity(0, 1))
    }
)
classes12: BinaryAssociation = BinaryAssociation(
    name="classes12",
    ends={
        Property(name="uml_Class13", type=uml_UMLSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_UMLSpecification", type=uml_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associations14: BinaryAssociation = BinaryAssociation(
    name="associations14",
    ends={
        Property(name="uml_Association16", type=uml_UMLSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_UMLSpecification15", type=uml_Association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent5: BinaryAssociation = BinaryAssociation(
    name="parent5",
    ends={
        Property(name="uml_Class6", type=uml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Class4", type=uml_Class, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_uml_Association_NamedElement = Generalization(general=NamedElement, specific=uml_Association)
gen_uml_Class_NamedElement = Generalization(general=NamedElement, specific=uml_Class)
gen_uml_Attribute_NamedElement = Generalization(general=NamedElement, specific=uml_Attribute)
gen_uml_UMLSpecification_NamedElement = Generalization(general=NamedElement, specific=uml_UMLSpecification)

# Domain Model
domain_model = DomainModel(
    name="uml",
    types={uml_Association, NamedElement, uml_Class, uml_Attribute, uml_UMLSpecification, uml_NamedElement},
    associations={src0, dst1, attrs7, type9, classes12, associations14, parent5},
    generalizations={gen_uml_Association_NamedElement, gen_uml_Class_NamedElement, gen_uml_Attribute_NamedElement, gen_uml_UMLSpecification_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)