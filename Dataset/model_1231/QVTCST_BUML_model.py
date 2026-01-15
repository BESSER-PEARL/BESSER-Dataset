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
qvt_cst_ErrorNode = Class(name="qvt::cst::ErrorNode")
qvt_cst_IdentifiedCS = Class(name="qvt::cst::IdentifiedCS")
cst_CSTNode = Class(name="cst::CSTNode")
cst_IHasName = Class(name="cst::IHasName")
IdentifierCS = Class(name="IdentifierCS")
cst_qvt_EObject = Class(name="cst::qvt::EObject")
qvt_cst_IdentifierCS = Class(name="qvt::cst::IdentifierCS")
qvt_cst_IHasName = Class(name="qvt::cst::IHasName", is_abstract=True)

# qvt_cst_ErrorNode class attributes and methods
qvt_cst_ErrorNode_message: Property = Property(name="message", type=StringType)
qvt_cst_ErrorNode.attributes={qvt_cst_ErrorNode_message}

# qvt_cst_IdentifiedCS class attributes and methods

# cst_CSTNode class attributes and methods

# cst_IHasName class attributes and methods

# IdentifierCS class attributes and methods

# cst_qvt_EObject class attributes and methods

# qvt_cst_IdentifierCS class attributes and methods
qvt_cst_IdentifierCS_value: Property = Property(name="value", type=StringType)
qvt_cst_IdentifierCS.attributes={qvt_cst_IdentifierCS_value}

# qvt_cst_IHasName class attributes and methods

# Relationships
identifier0: BinaryAssociation = BinaryAssociation(
    name="identifier0",
    ends={
        Property(name="IdentifierCS", type=qvt_cst_IdentifiedCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvt_cst_IdentifiedCS", type=IdentifierCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
astNode1: BinaryAssociation = BinaryAssociation(
    name="astNode1",
    ends={
        Property(name="cst_qvt_EObject", type=qvt_cst_IdentifiedCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvt_cst_IdentifiedCS2", type=cst_qvt_EObject, multiplicity=Multiplicity(0, 1))
    }
)
astNode3: BinaryAssociation = BinaryAssociation(
    name="astNode3",
    ends={
        Property(name="cst_qvt_EObject4", type=qvt_cst_IdentifierCS, multiplicity=Multiplicity(1, 1)),
        Property(name="qvt_cst_IdentifierCS", type=cst_qvt_EObject, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_qvt_cst_IdentifiedCS_cst_CSTNode = Generalization(general=cst_CSTNode, specific=qvt_cst_IdentifiedCS)
gen_qvt_cst_IdentifiedCS_cst_IHasName = Generalization(general=cst_IHasName, specific=qvt_cst_IdentifiedCS)
gen_qvt_cst_IdentifierCS_cst_CSTNode = Generalization(general=cst_CSTNode, specific=qvt_cst_IdentifierCS)
gen_qvt_cst_IdentifierCS_cst_IHasName = Generalization(general=cst_IHasName, specific=qvt_cst_IdentifierCS)

# Domain Model
domain_model = DomainModel(
    name="qvt",
    types={qvt_cst_ErrorNode, qvt_cst_IdentifiedCS, cst_CSTNode, cst_IHasName, IdentifierCS, cst_qvt_EObject, qvt_cst_IdentifierCS, qvt_cst_IHasName},
    associations={identifier0, astNode1, astNode3},
    generalizations={gen_qvt_cst_IdentifiedCS_cst_CSTNode, gen_qvt_cst_IdentifiedCS_cst_IHasName, gen_qvt_cst_IdentifierCS_cst_CSTNode, gen_qvt_cst_IdentifierCS_cst_IHasName},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)