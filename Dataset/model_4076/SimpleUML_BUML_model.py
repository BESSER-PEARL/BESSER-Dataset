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
SimpleUML_Package = Class(name="SimpleUML::Package")
SimpleUML_Class = Class(name="SimpleUML::Class")
NamedElement = Class(name="NamedElement")
SimpleUML_Feature = Class(name="SimpleUML::Feature")
SimpleUML_NamedElement = Class(name="SimpleUML::NamedElement")

# SimpleUML_Package class attributes and methods

# SimpleUML_Class class attributes and methods

# NamedElement class attributes and methods

# SimpleUML_Feature class attributes and methods
SimpleUML_Feature_isMultivalued: Property = Property(name="isMultivalued", type=BooleanType)
SimpleUML_Feature.attributes={SimpleUML_Feature_isMultivalued}

# SimpleUML_NamedElement class attributes and methods
SimpleUML_NamedElement_name: Property = Property(name="name", type=StringType)
SimpleUML_NamedElement.attributes={SimpleUML_NamedElement_name}

# Relationships
classes0: BinaryAssociation = BinaryAssociation(
    name="classes0",
    ends={
        Property(name="Class", type=SimpleUML_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="pkg", type=SimpleUML_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features1: BinaryAssociation = BinaryAssociation(
    name="features1",
    ends={
        Property(name="SimpleUML_Feature", type=SimpleUML_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleUML_Class", type=SimpleUML_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pkg2: BinaryAssociation = BinaryAssociation(
    name="pkg2",
    ends={
        Property(name="Package", type=SimpleUML_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="classes", type=SimpleUML_Package, multiplicity=Multiplicity(1, 1))
    }
)
type3: BinaryAssociation = BinaryAssociation(
    name="type3",
    ends={
        Property(name="SimpleUML_Class5", type=SimpleUML_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleUML_Feature4", type=SimpleUML_Class, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_SimpleUML_Class_NamedElement = Generalization(general=NamedElement, specific=SimpleUML_Class)
gen_SimpleUML_Feature_NamedElement = Generalization(general=NamedElement, specific=SimpleUML_Feature)

# Domain Model
domain_model = DomainModel(
    name="SimpleUML",
    types={SimpleUML_Package, SimpleUML_Class, NamedElement, SimpleUML_Feature, SimpleUML_NamedElement},
    associations={classes0, features1, pkg2, type3},
    generalizations={gen_SimpleUML_Class_NamedElement, gen_SimpleUML_Feature_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)