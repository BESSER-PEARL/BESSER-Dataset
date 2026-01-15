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
classescs_ElementCS = Class(name="classescs::ElementCS", is_abstract=True)
classescs_Element = Class(name="classescs::Element")
classescs_NamedElementCS = Class(name="classescs::NamedElementCS", is_abstract=True)
ElementCS = Class(name="ElementCS")
classescs_PackageCS = Class(name="classescs::PackageCS")
NamedElementCS = Class(name="NamedElementCS")
classescs_ClassCS = Class(name="classescs::ClassCS")
classescs_PathNameCS = Class(name="classescs::PathNameCS")
classescs_PathElementCS = Class(name="classescs::PathElementCS")
classescs_RootCS = Class(name="classescs::RootCS")

# classescs_ElementCS class attributes and methods

# classescs_Element class attributes and methods

# classescs_NamedElementCS class attributes and methods
classescs_NamedElementCS_name: Property = Property(name="name", type=StringType)
classescs_NamedElementCS.attributes={classescs_NamedElementCS_name}

# ElementCS class attributes and methods

# classescs_PackageCS class attributes and methods

# NamedElementCS class attributes and methods

# classescs_ClassCS class attributes and methods

# classescs_PathNameCS class attributes and methods

# classescs_PathElementCS class attributes and methods

# classescs_RootCS class attributes and methods

# Relationships
ast0: BinaryAssociation = BinaryAssociation(
    name="ast0",
    ends={
        Property(name="classescs_Element", type=classescs_ElementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="classescs_ElementCS", type=classescs_Element, multiplicity=Multiplicity(0, 1))
    }
)
ownedClasses1: BinaryAssociation = BinaryAssociation(
    name="ownedClasses1",
    ends={
        Property(name="classescs_ClassCS", type=classescs_PackageCS, multiplicity=Multiplicity(1, 1)),
        Property(name="classescs_PackageCS", type=classescs_ClassCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extends2: BinaryAssociation = BinaryAssociation(
    name="extends2",
    ends={
        Property(name="classescs_PathNameCS", type=classescs_ClassCS, multiplicity=Multiplicity(1, 1)),
        Property(name="classescs_ClassCS3", type=classescs_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
path4: BinaryAssociation = BinaryAssociation(
    name="path4",
    ends={
        Property(name="classescs_PathElementCS", type=classescs_PathNameCS, multiplicity=Multiplicity(1, 1)),
        Property(name="classescs_PathNameCS5", type=classescs_PathElementCS, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ownedPackages6: BinaryAssociation = BinaryAssociation(
    name="ownedPackages6",
    ends={
        Property(name="classescs_PackageCS7", type=classescs_RootCS, multiplicity=Multiplicity(1, 1)),
        Property(name="classescs_RootCS", type=classescs_PackageCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_classescs_NamedElementCS_ElementCS = Generalization(general=ElementCS, specific=classescs_NamedElementCS)
gen_classescs_PackageCS_NamedElementCS = Generalization(general=NamedElementCS, specific=classescs_PackageCS)
gen_classescs_ClassCS_NamedElementCS = Generalization(general=NamedElementCS, specific=classescs_ClassCS)
gen_classescs_PathNameCS_ElementCS = Generalization(general=ElementCS, specific=classescs_PathNameCS)
gen_classescs_PathElementCS_NamedElementCS = Generalization(general=NamedElementCS, specific=classescs_PathElementCS)
gen_classescs_RootCS_ElementCS = Generalization(general=ElementCS, specific=classescs_RootCS)

# Domain Model
domain_model = DomainModel(
    name="classescs",
    types={classescs_ElementCS, classescs_Element, classescs_NamedElementCS, ElementCS, classescs_PackageCS, NamedElementCS, classescs_ClassCS, classescs_PathNameCS, classescs_PathElementCS, classescs_RootCS},
    associations={ast0, ownedClasses1, extends2, path4, ownedPackages6},
    generalizations={gen_classescs_NamedElementCS_ElementCS, gen_classescs_PackageCS_NamedElementCS, gen_classescs_ClassCS_NamedElementCS, gen_classescs_PathNameCS_ElementCS, gen_classescs_PathElementCS_NamedElementCS, gen_classescs_RootCS_ElementCS},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)