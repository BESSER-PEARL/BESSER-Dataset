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
classescstraces_RootCS = Class(name="classescstraces::RootCS")
classescstraces_PackageCS2Package = Class(name="classescstraces::PackageCS2Package")
classescstraces_PackageCS = Class(name="classescstraces::PackageCS")
classescstraces_Package = Class(name="classescstraces::Package")
classescstraces_ClassCS2Class = Class(name="classescstraces::ClassCS2Class")
classescstraces_ClassCS = Class(name="classescstraces::ClassCS")
classescstraces_Class = Class(name="classescstraces::Class")
classescstraces_RootCS2Root = Class(name="classescstraces::RootCS2Root")
classescstraces_Root = Class(name="classescstraces::Root")

# classescstraces_RootCS class attributes and methods

# classescstraces_PackageCS2Package class attributes and methods

# classescstraces_PackageCS class attributes and methods

# classescstraces_Package class attributes and methods

# classescstraces_ClassCS2Class class attributes and methods

# classescstraces_ClassCS class attributes and methods

# classescstraces_Class class attributes and methods

# classescstraces_RootCS2Root class attributes and methods

# classescstraces_Root class attributes and methods

# Relationships
packageCS0: BinaryAssociation = BinaryAssociation(
    name="packageCS0",
    ends={
        Property(name="classescstraces_PackageCS", type=classescstraces_PackageCS2Package, multiplicity=Multiplicity(1, 1)),
        Property(name="classescstraces_PackageCS2Package", type=classescstraces_PackageCS, multiplicity=Multiplicity(1, 1))
    }
)
package1: BinaryAssociation = BinaryAssociation(
    name="package1",
    ends={
        Property(name="classescstraces_Package", type=classescstraces_PackageCS2Package, multiplicity=Multiplicity(1, 1)),
        Property(name="classescstraces_PackageCS2Package2", type=classescstraces_Package, multiplicity=Multiplicity(1, 1))
    }
)
classCS3: BinaryAssociation = BinaryAssociation(
    name="classCS3",
    ends={
        Property(name="classescstraces_ClassCS", type=classescstraces_ClassCS2Class, multiplicity=Multiplicity(1, 1)),
        Property(name="classescstraces_ClassCS2Class", type=classescstraces_ClassCS, multiplicity=Multiplicity(1, 1))
    }
)
class4: BinaryAssociation = BinaryAssociation(
    name="class4",
    ends={
        Property(name="classescstraces_Class", type=classescstraces_ClassCS2Class, multiplicity=Multiplicity(1, 1)),
        Property(name="classescstraces_ClassCS2Class5", type=classescstraces_Class, multiplicity=Multiplicity(1, 1))
    }
)
rootCS6: BinaryAssociation = BinaryAssociation(
    name="rootCS6",
    ends={
        Property(name="classescstraces_RootCS", type=classescstraces_RootCS2Root, multiplicity=Multiplicity(1, 1)),
        Property(name="classescstraces_RootCS2Root", type=classescstraces_RootCS, multiplicity=Multiplicity(1, 1))
    }
)
root7: BinaryAssociation = BinaryAssociation(
    name="root7",
    ends={
        Property(name="classescstraces_Root", type=classescstraces_RootCS2Root, multiplicity=Multiplicity(1, 1)),
        Property(name="classescstraces_RootCS2Root8", type=classescstraces_Root, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="classescstraces",
    types={classescstraces_RootCS, classescstraces_PackageCS2Package, classescstraces_PackageCS, classescstraces_Package, classescstraces_ClassCS2Class, classescstraces_ClassCS, classescstraces_Class, classescstraces_RootCS2Root, classescstraces_Root},
    associations={packageCS0, package1, classCS3, class4, rootCS6, root7},
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