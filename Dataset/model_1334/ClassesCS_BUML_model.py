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
classescs_NamedElementCS = Class(name="classescs::NamedElementCS", is_abstract=True)
classescs_PackageCS = Class(name="classescs::PackageCS")
NamedElementCS = Class(name="NamedElementCS")
classescs_ClassCS = Class(name="classescs::ClassCS")
classescs_PathNameCS = Class(name="classescs::PathNameCS")
classescs_PathElementCS = Class(name="classescs::PathElementCS")
classescs_RootCS = Class(name="classescs::RootCS")

# classescs_NamedElementCS class attributes and methods
classescs_NamedElementCS_name: Property = Property(name="name", type=StringType)
classescs_NamedElementCS.attributes={classescs_NamedElementCS_name}

# classescs_PackageCS class attributes and methods

# NamedElementCS class attributes and methods

# classescs_ClassCS class attributes and methods

# classescs_PathNameCS class attributes and methods

# classescs_PathElementCS class attributes and methods

# classescs_RootCS class attributes and methods

# Relationships
ownedClasses0: BinaryAssociation = BinaryAssociation(
    name="ownedClasses0",
    ends={
        Property(name="classescs_ClassCS", type=classescs_PackageCS, multiplicity=Multiplicity(1, 1)),
        Property(name="classescs_PackageCS", type=classescs_ClassCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extends1: BinaryAssociation = BinaryAssociation(
    name="extends1",
    ends={
        Property(name="classescs_PathNameCS", type=classescs_ClassCS, multiplicity=Multiplicity(1, 1)),
        Property(name="classescs_ClassCS2", type=classescs_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
path3: BinaryAssociation = BinaryAssociation(
    name="path3",
    ends={
        Property(name="classescs_PathElementCS", type=classescs_PathNameCS, multiplicity=Multiplicity(1, 1)),
        Property(name="classescs_PathNameCS4", type=classescs_PathElementCS, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ownedPackages5: BinaryAssociation = BinaryAssociation(
    name="ownedPackages5",
    ends={
        Property(name="classescs_PackageCS6", type=classescs_RootCS, multiplicity=Multiplicity(1, 1)),
        Property(name="classescs_RootCS", type=classescs_PackageCS, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_classescs_PackageCS_NamedElementCS = Generalization(general=NamedElementCS, specific=classescs_PackageCS)
gen_classescs_ClassCS_NamedElementCS = Generalization(general=NamedElementCS, specific=classescs_ClassCS)
gen_classescs_PathElementCS_NamedElementCS = Generalization(general=NamedElementCS, specific=classescs_PathElementCS)

# Domain Model
domain_model = DomainModel(
    name="classescs",
    types={classescs_NamedElementCS, classescs_PackageCS, NamedElementCS, classescs_ClassCS, classescs_PathNameCS, classescs_PathElementCS, classescs_RootCS},
    associations={ownedClasses0, extends1, path3, ownedPackages5},
    generalizations={gen_classescs_PackageCS_NamedElementCS, gen_classescs_ClassCS_NamedElementCS, gen_classescs_PathElementCS_NamedElementCS},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)