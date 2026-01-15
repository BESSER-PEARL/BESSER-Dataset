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
classes_Element = Class(name="classes::Element", is_abstract=True)
classes_NamedElement = Class(name="classes::NamedElement", is_abstract=True)
Element = Class(name="Element")
classes_Namespace = Class(name="classes::Namespace", is_abstract=True)
classes_Package = Class(name="classes::Package")
NamedElement = Class(name="NamedElement")
Namespace = Class(name="Namespace")
classes_Class = Class(name="classes::Class")
classes_Root = Class(name="classes::Root")

# classes_Element class attributes and methods

# classes_NamedElement class attributes and methods
classes_NamedElement_name: Property = Property(name="name", type=StringType)
classes_NamedElement.attributes={classes_NamedElement_name}

# Element class attributes and methods

# classes_Namespace class attributes and methods

# classes_Package class attributes and methods

# NamedElement class attributes and methods

# Namespace class attributes and methods

# classes_Class class attributes and methods

# classes_Root class attributes and methods

# Relationships
ownedClasses0: BinaryAssociation = BinaryAssociation(
    name="ownedClasses0",
    ends={
        Property(name="classes_Class", type=classes_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Package", type=classes_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedPackages2: BinaryAssociation = BinaryAssociation(
    name="ownedPackages2",
    ends={
        Property(name="classes_Package3", type=classes_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Package1", type=classes_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass5: BinaryAssociation = BinaryAssociation(
    name="superClass5",
    ends={
        Property(name="classes_Class6", type=classes_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Class4", type=classes_Class, multiplicity=Multiplicity(0, 1))
    }
)
ownedPackages7: BinaryAssociation = BinaryAssociation(
    name="ownedPackages7",
    ends={
        Property(name="classes_Package8", type=classes_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Root", type=classes_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_classes_NamedElement_Element = Generalization(general=Element, specific=classes_NamedElement)
gen_classes_Namespace_Element = Generalization(general=Element, specific=classes_Namespace)
gen_classes_Package_NamedElement = Generalization(general=NamedElement, specific=classes_Package)
gen_classes_Package_Namespace = Generalization(general=Namespace, specific=classes_Package)
gen_classes_Class_NamedElement = Generalization(general=NamedElement, specific=classes_Class)
gen_classes_Root_Element = Generalization(general=Element, specific=classes_Root)

# Domain Model
domain_model = DomainModel(
    name="classes",
    types={classes_Element, classes_NamedElement, Element, classes_Namespace, classes_Package, NamedElement, Namespace, classes_Class, classes_Root},
    associations={ownedClasses0, ownedPackages2, superClass5, ownedPackages7},
    generalizations={gen_classes_NamedElement_Element, gen_classes_Namespace_Element, gen_classes_Package_NamedElement, gen_classes_Package_Namespace, gen_classes_Class_NamedElement, gen_classes_Root_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)