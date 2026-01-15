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
simpleClass_NamedElement = Class(name="simpleClass::NamedElement", is_abstract=True)
simpleClass_ClassModel = Class(name="simpleClass::ClassModel")
simpleClass_Package = Class(name="simpleClass::Package")
NamedElement = Class(name="NamedElement")
simpleClass_Class = Class(name="simpleClass::Class")
simpleClass_Association = Class(name="simpleClass::Association")
simpleClass_Attribute = Class(name="simpleClass::Attribute")

# simpleClass_NamedElement class attributes and methods
simpleClass_NamedElement_name: Property = Property(name="name", type=StringType)
simpleClass_NamedElement.attributes={simpleClass_NamedElement_name}

# simpleClass_ClassModel class attributes and methods

# simpleClass_Package class attributes and methods

# NamedElement class attributes and methods

# simpleClass_Class class attributes and methods
simpleClass_Class_persistent: Property = Property(name="persistent", type=BooleanType)
simpleClass_Class.attributes={simpleClass_Class_persistent}

# simpleClass_Association class attributes and methods

# simpleClass_Attribute class attributes and methods

# Relationships
packages0: BinaryAssociation = BinaryAssociation(
    name="packages0",
    ends={
        Property(name="simpleClass_Package", type=simpleClass_ClassModel, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleClass_ClassModel", type=simpleClass_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subPackages2: BinaryAssociation = BinaryAssociation(
    name="subPackages2",
    ends={
        Property(name="simpleClass_Package3", type=simpleClass_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleClass_Package1", type=simpleClass_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classes4: BinaryAssociation = BinaryAssociation(
    name="classes4",
    ends={
        Property(name="simpleClass_Class", type=simpleClass_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleClass_Package5", type=simpleClass_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associations6: BinaryAssociation = BinaryAssociation(
    name="associations6",
    ends={
        Property(name="simpleClass_Association", type=simpleClass_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleClass_Package7", type=simpleClass_Association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes8: BinaryAssociation = BinaryAssociation(
    name="attributes8",
    ends={
        Property(name="simpleClass_Attribute", type=simpleClass_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleClass_Class9", type=simpleClass_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
super11: BinaryAssociation = BinaryAssociation(
    name="super11",
    ends={
        Property(name="simpleClass_Class12", type=simpleClass_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleClass_Class10", type=simpleClass_Class, multiplicity=Multiplicity(0, 9999))
    }
)
source13: BinaryAssociation = BinaryAssociation(
    name="source13",
    ends={
        Property(name="simpleClass_Class15", type=simpleClass_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleClass_Association14", type=simpleClass_Class, multiplicity=Multiplicity(1, 1))
    }
)
target16: BinaryAssociation = BinaryAssociation(
    name="target16",
    ends={
        Property(name="simpleClass_Class18", type=simpleClass_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleClass_Association17", type=simpleClass_Class, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_simpleClass_Package_NamedElement = Generalization(general=NamedElement, specific=simpleClass_Package)
gen_simpleClass_Class_NamedElement = Generalization(general=NamedElement, specific=simpleClass_Class)
gen_simpleClass_Attribute_NamedElement = Generalization(general=NamedElement, specific=simpleClass_Attribute)
gen_simpleClass_Association_NamedElement = Generalization(general=NamedElement, specific=simpleClass_Association)

# Domain Model
domain_model = DomainModel(
    name="simpleClass",
    types={simpleClass_NamedElement, simpleClass_ClassModel, simpleClass_Package, NamedElement, simpleClass_Class, simpleClass_Association, simpleClass_Attribute},
    associations={packages0, subPackages2, classes4, associations6, attributes8, super11, source13, target16},
    generalizations={gen_simpleClass_Package_NamedElement, gen_simpleClass_Class_NamedElement, gen_simpleClass_Attribute_NamedElement, gen_simpleClass_Association_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)