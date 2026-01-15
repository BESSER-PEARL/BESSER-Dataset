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
oclstdlibcs_MetaclassNameCS = Class(name="oclstdlibcs::MetaclassNameCS")
oclstdlibcs_LibCoercionCS = Class(name="oclstdlibcs::LibCoercionCS")
OperationCS = Class(name="OperationCS")
JavaImplementationCS = Class(name="JavaImplementationCS")
oclstdlibcs_LibConstraintCS = Class(name="oclstdlibcs::LibConstraintCS")
ConstraintCS = Class(name="ConstraintCS")
oclstdlibcs_LibIterationCS = Class(name="oclstdlibcs::LibIterationCS")
oclstdlibcs_JavaClassCS = Class(name="oclstdlibcs::JavaClassCS")
NamedElementCS = Class(name="NamedElementCS")
oclstdlibcs_JavaImplementationCS = Class(name="oclstdlibcs::JavaImplementationCS", is_abstract=True)
ElementCS = Class(name="ElementCS")
oclstdlibcs_LibClassCS = Class(name="oclstdlibcs::LibClassCS")
StructuredClassCS = Class(name="StructuredClassCS")
oclstdlibcs_ParameterCS = Class(name="oclstdlibcs::ParameterCS")
oclstdlibcs_LibOperationCS = Class(name="oclstdlibcs::LibOperationCS")
oclstdlibcs_LibRootPackageCS = Class(name="oclstdlibcs::LibRootPackageCS")
RootPackageCS = Class(name="RootPackageCS")
Nameable = Class(name="Nameable")
oclstdlibcs_Precedence = Class(name="oclstdlibcs::Precedence")
oclstdlibcs_LibPackageCS = Class(name="oclstdlibcs::LibPackageCS")
PackageCS = Class(name="PackageCS")
oclstdlibcs_PrecedenceCS = Class(name="oclstdlibcs::PrecedenceCS")
oclstdlibcs_LibPropertyCS = Class(name="oclstdlibcs::LibPropertyCS")
AttributeCS = Class(name="AttributeCS")

# oclstdlibcs_MetaclassNameCS class attributes and methods
oclstdlibcs_MetaclassNameCS_name: Property = Property(name="name", type=StringType)
oclstdlibcs_MetaclassNameCS.attributes={oclstdlibcs_MetaclassNameCS_name}

# oclstdlibcs_LibCoercionCS class attributes and methods

# OperationCS class attributes and methods

# JavaImplementationCS class attributes and methods

# oclstdlibcs_LibConstraintCS class attributes and methods

# ConstraintCS class attributes and methods

# oclstdlibcs_LibIterationCS class attributes and methods
oclstdlibcs_LibIterationCS_isInvalidating: Property = Property(name="isInvalidating", type=StringType)
oclstdlibcs_LibIterationCS_isValidating: Property = Property(name="isValidating", type=StringType)
oclstdlibcs_LibIterationCS.attributes={oclstdlibcs_LibIterationCS_isInvalidating, oclstdlibcs_LibIterationCS_isValidating}

# oclstdlibcs_JavaClassCS class attributes and methods

# NamedElementCS class attributes and methods

# oclstdlibcs_JavaImplementationCS class attributes and methods

# ElementCS class attributes and methods

# oclstdlibcs_LibClassCS class attributes and methods

# StructuredClassCS class attributes and methods

# oclstdlibcs_ParameterCS class attributes and methods

# oclstdlibcs_LibOperationCS class attributes and methods
oclstdlibcs_LibOperationCS_isInvalidating: Property = Property(name="isInvalidating", type=StringType)
oclstdlibcs_LibOperationCS_isStatic: Property = Property(name="isStatic", type=StringType)
oclstdlibcs_LibOperationCS_isValidating: Property = Property(name="isValidating", type=StringType)
oclstdlibcs_LibOperationCS.attributes={oclstdlibcs_LibOperationCS_isValidating, oclstdlibcs_LibOperationCS_isStatic, oclstdlibcs_LibOperationCS_isInvalidating}

# oclstdlibcs_LibRootPackageCS class attributes and methods

# RootPackageCS class attributes and methods

# Nameable class attributes and methods

# oclstdlibcs_Precedence class attributes and methods

# oclstdlibcs_LibPackageCS class attributes and methods

# PackageCS class attributes and methods

# oclstdlibcs_PrecedenceCS class attributes and methods
oclstdlibcs_PrecedenceCS_isRightAssociative: Property = Property(name="isRightAssociative", type=BooleanType)
oclstdlibcs_PrecedenceCS.attributes={oclstdlibcs_PrecedenceCS_isRightAssociative}

# oclstdlibcs_LibPropertyCS class attributes and methods
oclstdlibcs_LibPropertyCS_isStatic: Property = Property(name="isStatic", type=StringType)
oclstdlibcs_LibPropertyCS.attributes={oclstdlibcs_LibPropertyCS_isStatic}

# AttributeCS class attributes and methods

# Relationships
metaclassName1: BinaryAssociation = BinaryAssociation(
    name="metaclassName1",
    ends={
        Property(name="oclstdlibcs_MetaclassNameCS", type=oclstdlibcs_LibClassCS, multiplicity=Multiplicity(1, 1)),
        Property(name="oclstdlibcs_LibClassCS", type=oclstdlibcs_MetaclassNameCS, multiplicity=Multiplicity(0, 1))
    }
)
implementation0: BinaryAssociation = BinaryAssociation(
    name="implementation0",
    ends={
        Property(name="oclstdlibcs_JavaClassCS", type=oclstdlibcs_JavaImplementationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="oclstdlibcs_JavaImplementationCS", type=oclstdlibcs_JavaClassCS, multiplicity=Multiplicity(0, 1))
    }
)
ownedAccumulators2: BinaryAssociation = BinaryAssociation(
    name="ownedAccumulators2",
    ends={
        Property(name="oclstdlibcs_ParameterCS", type=oclstdlibcs_LibIterationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="oclstdlibcs_LibIterationCS", type=oclstdlibcs_ParameterCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedIterators3: BinaryAssociation = BinaryAssociation(
    name="ownedIterators3",
    ends={
        Property(name="oclstdlibcs_ParameterCS5", type=oclstdlibcs_LibIterationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="oclstdlibcs_LibIterationCS4", type=oclstdlibcs_ParameterCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
precedence6: BinaryAssociation = BinaryAssociation(
    name="precedence6",
    ends={
        Property(name="oclstdlibcs_Precedence", type=oclstdlibcs_LibOperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="oclstdlibcs_LibOperationCS", type=oclstdlibcs_Precedence, multiplicity=Multiplicity(0, 1))
    }
)
ownedPrecedences7: BinaryAssociation = BinaryAssociation(
    name="ownedPrecedences7",
    ends={
        Property(name="oclstdlibcs_PrecedenceCS", type=oclstdlibcs_LibPackageCS, multiplicity=Multiplicity(1, 1)),
        Property(name="oclstdlibcs_LibPackageCS", type=oclstdlibcs_PrecedenceCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_oclstdlibcs_LibCoercionCS_OperationCS = Generalization(general=OperationCS, specific=oclstdlibcs_LibCoercionCS)
gen_oclstdlibcs_LibCoercionCS_JavaImplementationCS = Generalization(general=JavaImplementationCS, specific=oclstdlibcs_LibCoercionCS)
gen_oclstdlibcs_LibConstraintCS_ConstraintCS = Generalization(general=ConstraintCS, specific=oclstdlibcs_LibConstraintCS)
gen_oclstdlibcs_LibIterationCS_OperationCS = Generalization(general=OperationCS, specific=oclstdlibcs_LibIterationCS)
gen_oclstdlibcs_LibIterationCS_JavaImplementationCS = Generalization(general=JavaImplementationCS, specific=oclstdlibcs_LibIterationCS)
gen_oclstdlibcs_JavaClassCS_NamedElementCS = Generalization(general=NamedElementCS, specific=oclstdlibcs_JavaClassCS)
gen_oclstdlibcs_JavaImplementationCS_ElementCS = Generalization(general=ElementCS, specific=oclstdlibcs_JavaImplementationCS)
gen_oclstdlibcs_LibClassCS_StructuredClassCS = Generalization(general=StructuredClassCS, specific=oclstdlibcs_LibClassCS)
gen_oclstdlibcs_LibOperationCS_OperationCS = Generalization(general=OperationCS, specific=oclstdlibcs_LibOperationCS)
gen_oclstdlibcs_LibOperationCS_JavaImplementationCS = Generalization(general=JavaImplementationCS, specific=oclstdlibcs_LibOperationCS)
gen_oclstdlibcs_LibRootPackageCS_RootPackageCS = Generalization(general=RootPackageCS, specific=oclstdlibcs_LibRootPackageCS)
gen_oclstdlibcs_MetaclassNameCS_ElementCS = Generalization(general=ElementCS, specific=oclstdlibcs_MetaclassNameCS)
gen_oclstdlibcs_MetaclassNameCS_Nameable = Generalization(general=Nameable, specific=oclstdlibcs_MetaclassNameCS)
gen_oclstdlibcs_LibPackageCS_PackageCS = Generalization(general=PackageCS, specific=oclstdlibcs_LibPackageCS)
gen_oclstdlibcs_LibPropertyCS_AttributeCS = Generalization(general=AttributeCS, specific=oclstdlibcs_LibPropertyCS)
gen_oclstdlibcs_LibPropertyCS_JavaImplementationCS = Generalization(general=JavaImplementationCS, specific=oclstdlibcs_LibPropertyCS)
gen_oclstdlibcs_PrecedenceCS_NamedElementCS = Generalization(general=NamedElementCS, specific=oclstdlibcs_PrecedenceCS)

# Domain Model
domain_model = DomainModel(
    name="oclstdlibcs",
    types={oclstdlibcs_MetaclassNameCS, oclstdlibcs_LibCoercionCS, OperationCS, JavaImplementationCS, oclstdlibcs_LibConstraintCS, ConstraintCS, oclstdlibcs_LibIterationCS, oclstdlibcs_JavaClassCS, NamedElementCS, oclstdlibcs_JavaImplementationCS, ElementCS, oclstdlibcs_LibClassCS, StructuredClassCS, oclstdlibcs_ParameterCS, oclstdlibcs_LibOperationCS, oclstdlibcs_LibRootPackageCS, RootPackageCS, Nameable, oclstdlibcs_Precedence, oclstdlibcs_LibPackageCS, PackageCS, oclstdlibcs_PrecedenceCS, oclstdlibcs_LibPropertyCS, AttributeCS},
    associations={metaclassName1, implementation0, ownedAccumulators2, ownedIterators3, precedence6, ownedPrecedences7},
    generalizations={gen_oclstdlibcs_LibCoercionCS_OperationCS, gen_oclstdlibcs_LibCoercionCS_JavaImplementationCS, gen_oclstdlibcs_LibConstraintCS_ConstraintCS, gen_oclstdlibcs_LibIterationCS_OperationCS, gen_oclstdlibcs_LibIterationCS_JavaImplementationCS, gen_oclstdlibcs_JavaClassCS_NamedElementCS, gen_oclstdlibcs_JavaImplementationCS_ElementCS, gen_oclstdlibcs_LibClassCS_StructuredClassCS, gen_oclstdlibcs_LibOperationCS_OperationCS, gen_oclstdlibcs_LibOperationCS_JavaImplementationCS, gen_oclstdlibcs_LibRootPackageCS_RootPackageCS, gen_oclstdlibcs_MetaclassNameCS_ElementCS, gen_oclstdlibcs_MetaclassNameCS_Nameable, gen_oclstdlibcs_LibPackageCS_PackageCS, gen_oclstdlibcs_LibPropertyCS_AttributeCS, gen_oclstdlibcs_LibPropertyCS_JavaImplementationCS, gen_oclstdlibcs_PrecedenceCS_NamedElementCS},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)