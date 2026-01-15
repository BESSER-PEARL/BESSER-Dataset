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
classescs_EObject = Class(name="classescs::EObject")
classescs_NamedElementCS = Class(name="classescs::NamedElementCS", is_abstract=True)
ElementCS = Class(name="ElementCS")
classescs_OperationCS = Class(name="classescs::OperationCS")
classescs_PathElementCS = Class(name="classescs::PathElementCS")
classescs_RootCS = Class(name="classescs::RootCS")
classescs_NameExpCS = Class(name="classescs::NameExpCS")
classescs_PackageCS = Class(name="classescs::PackageCS")
NamedElementCS = Class(name="NamedElementCS")
classescs_RoundedBracketClause = Class(name="classescs::RoundedBracketClause")
classescs_ClassCS = Class(name="classescs::ClassCS")
classescs_PathNameCS = Class(name="classescs::PathNameCS")
classescs_PropertyCS = Class(name="classescs::PropertyCS")
classescs_ArgumentCS = Class(name="classescs::ArgumentCS")

# classescs_ElementCS class attributes and methods

# classescs_EObject class attributes and methods

# classescs_NamedElementCS class attributes and methods
classescs_NamedElementCS_name: Property = Property(name="name", type=StringType)
classescs_NamedElementCS.attributes={classescs_NamedElementCS_name}

# ElementCS class attributes and methods

# classescs_OperationCS class attributes and methods
classescs_OperationCS_params: Property = Property(name="params", type=StringType)
classescs_OperationCS.attributes={classescs_OperationCS_params}

# classescs_PathElementCS class attributes and methods

# classescs_RootCS class attributes and methods

# classescs_NameExpCS class attributes and methods

# classescs_PackageCS class attributes and methods

# NamedElementCS class attributes and methods

# classescs_RoundedBracketClause class attributes and methods

# classescs_ClassCS class attributes and methods

# classescs_PathNameCS class attributes and methods

# classescs_PropertyCS class attributes and methods

# classescs_ArgumentCS class attributes and methods

# Relationships
ast0: BinaryAssociation = BinaryAssociation(
    name="ast0",
    ends={
        Property(name="classescs_EObject", type=classescs_ElementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="classescs_ElementCS", type=classescs_EObject, multiplicity=Multiplicity(0, 1))
    }
)
operations9: BinaryAssociation = BinaryAssociation(
    name="operations9",
    ends={
        Property(name="classescs_OperationCS", type=classescs_ClassCS, multiplicity=Multiplicity(1, 1)),
        Property(name="classescs_ClassCS10", type=classescs_OperationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
path11: BinaryAssociation = BinaryAssociation(
    name="path11",
    ends={
        Property(name="classescs_PathElementCS", type=classescs_PathNameCS, multiplicity=Multiplicity(1, 1)),
        Property(name="classescs_PathNameCS12", type=classescs_PathElementCS, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ownedPackages13: BinaryAssociation = BinaryAssociation(
    name="ownedPackages13",
    ends={
        Property(name="classescs_PackageCS14", type=classescs_RootCS, multiplicity=Multiplicity(1, 1)),
        Property(name="classescs_RootCS", type=classescs_PackageCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeRef15: BinaryAssociation = BinaryAssociation(
    name="typeRef15",
    ends={
        Property(name="classescs_PathNameCS17", type=classescs_PropertyCS, multiplicity=Multiplicity(1, 1)),
        Property(name="classescs_PropertyCS16", type=classescs_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bodyExps18: BinaryAssociation = BinaryAssociation(
    name="bodyExps18",
    ends={
        Property(name="classescs_NameExpCS", type=classescs_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="classescs_OperationCS19", type=classescs_NameExpCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resultRef20: BinaryAssociation = BinaryAssociation(
    name="resultRef20",
    ends={
        Property(name="classescs_PathNameCS22", type=classescs_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="classescs_OperationCS21", type=classescs_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name23: BinaryAssociation = BinaryAssociation(
    name="name23",
    ends={
        Property(name="classescs_PathNameCS25", type=classescs_NameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="classescs_NameExpCS24", type=classescs_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedClasses1: BinaryAssociation = BinaryAssociation(
    name="ownedClasses1",
    ends={
        Property(name="classescs_ClassCS", type=classescs_PackageCS, multiplicity=Multiplicity(1, 1)),
        Property(name="classescs_PackageCS", type=classescs_ClassCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedPackages3: BinaryAssociation = BinaryAssociation(
    name="ownedPackages3",
    ends={
        Property(name="classescs_PackageCS4", type=classescs_PackageCS, multiplicity=Multiplicity(1, 1)),
        Property(name="classescs_PackageCS2", type=classescs_PackageCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extends5: BinaryAssociation = BinaryAssociation(
    name="extends5",
    ends={
        Property(name="classescs_PathNameCS", type=classescs_ClassCS, multiplicity=Multiplicity(1, 1)),
        Property(name="classescs_ClassCS6", type=classescs_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties7: BinaryAssociation = BinaryAssociation(
    name="properties7",
    ends={
        Property(name="classescs_PropertyCS", type=classescs_ClassCS, multiplicity=Multiplicity(1, 1)),
        Property(name="classescs_ClassCS8", type=classescs_PropertyCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
roundedBrackets26: BinaryAssociation = BinaryAssociation(
    name="roundedBrackets26",
    ends={
        Property(name="classescs_RoundedBracketClause", type=classescs_NameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="classescs_NameExpCS27", type=classescs_RoundedBracketClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedNameExp29: BinaryAssociation = BinaryAssociation(
    name="ownedNameExp29",
    ends={
        Property(name="classescs_NameExpCS30", type=classescs_NameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="classescs_NameExpCS28", type=classescs_NameExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args31: BinaryAssociation = BinaryAssociation(
    name="args31",
    ends={
        Property(name="classescs_ArgumentCS", type=classescs_RoundedBracketClause, multiplicity=Multiplicity(1, 1)),
        Property(name="classescs_RoundedBracketClause32", type=classescs_ArgumentCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_classescs_NamedElementCS_ElementCS = Generalization(general=ElementCS, specific=classescs_NamedElementCS)
gen_classescs_PathNameCS_ElementCS = Generalization(general=ElementCS, specific=classescs_PathNameCS)
gen_classescs_PathElementCS_NamedElementCS = Generalization(general=NamedElementCS, specific=classescs_PathElementCS)
gen_classescs_RootCS_ElementCS = Generalization(general=ElementCS, specific=classescs_RootCS)
gen_classescs_PropertyCS_NamedElementCS = Generalization(general=NamedElementCS, specific=classescs_PropertyCS)
gen_classescs_OperationCS_NamedElementCS = Generalization(general=NamedElementCS, specific=classescs_OperationCS)
gen_classescs_NameExpCS_ElementCS = Generalization(general=ElementCS, specific=classescs_NameExpCS)
gen_classescs_PackageCS_NamedElementCS = Generalization(general=NamedElementCS, specific=classescs_PackageCS)
gen_classescs_ClassCS_NamedElementCS = Generalization(general=NamedElementCS, specific=classescs_ClassCS)
gen_classescs_RoundedBracketClause_ElementCS = Generalization(general=ElementCS, specific=classescs_RoundedBracketClause)
gen_classescs_ArgumentCS_NamedElementCS = Generalization(general=NamedElementCS, specific=classescs_ArgumentCS)

# Domain Model
domain_model = DomainModel(
    name="classescs",
    types={classescs_ElementCS, classescs_EObject, classescs_NamedElementCS, ElementCS, classescs_OperationCS, classescs_PathElementCS, classescs_RootCS, classescs_NameExpCS, classescs_PackageCS, NamedElementCS, classescs_RoundedBracketClause, classescs_ClassCS, classescs_PathNameCS, classescs_PropertyCS, classescs_ArgumentCS},
    associations={ast0, operations9, path11, ownedPackages13, typeRef15, bodyExps18, resultRef20, name23, ownedClasses1, ownedPackages3, extends5, properties7, roundedBrackets26, ownedNameExp29, args31},
    generalizations={gen_classescs_NamedElementCS_ElementCS, gen_classescs_PathNameCS_ElementCS, gen_classescs_PathElementCS_NamedElementCS, gen_classescs_RootCS_ElementCS, gen_classescs_PropertyCS_NamedElementCS, gen_classescs_OperationCS_NamedElementCS, gen_classescs_NameExpCS_ElementCS, gen_classescs_PackageCS_NamedElementCS, gen_classescs_ClassCS_NamedElementCS, gen_classescs_RoundedBracketClause_ElementCS, gen_classescs_ArgumentCS_NamedElementCS},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)