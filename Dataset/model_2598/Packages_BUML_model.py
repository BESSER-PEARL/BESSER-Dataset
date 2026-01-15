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
MainPackage_ClassInMainPackage = Class(name="MainPackage::ClassInMainPackage")
MainPackage_Model = Class(name="MainPackage::Model")
MainPackage_EObject = Class(name="MainPackage::EObject")
MainPackage_Subpackage_ClassInSubpackage = Class(name="MainPackage::Subpackage::ClassInSubpackage")
MainPackage_Subpackage_InheritingClass = Class(name="MainPackage::Subpackage::InheritingClass")
ClassInMainPackage = Class(name="ClassInMainPackage")

# MainPackage_ClassInMainPackage class attributes and methods
MainPackage_ClassInMainPackage_name: Property = Property(name="name", type=StringType)
MainPackage_ClassInMainPackage.attributes={MainPackage_ClassInMainPackage_name}

# MainPackage_Model class attributes and methods

# MainPackage_EObject class attributes and methods

# MainPackage_Subpackage_ClassInSubpackage class attributes and methods

# MainPackage_Subpackage_InheritingClass class attributes and methods

# ClassInMainPackage class attributes and methods

# Relationships
objects0: BinaryAssociation = BinaryAssociation(
    name="objects0",
    ends={
        Property(name="MainPackage_EObject", type=MainPackage_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="MainPackage_Model", type=MainPackage_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_MainPackage_Subpackage_InheritingClass_ClassInMainPackage = Generalization(general=ClassInMainPackage, specific=MainPackage_Subpackage_InheritingClass)

# Domain Model
domain_model = DomainModel(
    name="MainPackage",
    types={MainPackage_ClassInMainPackage, MainPackage_Model, MainPackage_EObject, MainPackage_Subpackage_ClassInSubpackage, MainPackage_Subpackage_InheritingClass, ClassInMainPackage},
    associations={objects0},
    generalizations={gen_MainPackage_Subpackage_InheritingClass_ClassInMainPackage},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)