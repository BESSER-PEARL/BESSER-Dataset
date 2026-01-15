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
oclstdlib_Collection = Class(name="oclstdlib::Collection", is_abstract=True)
OclAny = Class(name="OclAny")
oclstdlib_Bag = Class(name="oclstdlib::Bag", is_abstract=True)
oclstdlib_OclAny = Class(name="oclstdlib::OclAny", is_abstract=True)
oclstdlib_OclComparable = Class(name="oclstdlib::OclComparable", is_abstract=True)
oclstdlib_OclElement = Class(name="oclstdlib::OclElement", is_abstract=True)
oclstdlib_OclInvalid = Class(name="oclstdlib::OclInvalid", is_abstract=True)
OclVoid = Class(name="OclVoid")
oclstdlib_OclLambda = Class(name="oclstdlib::OclLambda", is_abstract=True)
oclstdlib_OclMessage = Class(name="oclstdlib::OclMessage", is_abstract=True)
oclstdlib_OclState = Class(name="oclstdlib::OclState", is_abstract=True)
oclstdlib_OclSummable = Class(name="oclstdlib::OclSummable", is_abstract=True)
oclstdlib_OclTuple = Class(name="oclstdlib::OclTuple", is_abstract=True)
oclstdlib_OclType = Class(name="oclstdlib::OclType", is_abstract=True)
OclElement = Class(name="OclElement")
oclstdlib_OclVoid = Class(name="oclstdlib::OclVoid", is_abstract=True)
oclstdlib_OrderedCollection = Class(name="oclstdlib::OrderedCollection", is_abstract=True)
oclstdlib_OrderedSet = Class(name="oclstdlib::OrderedSet", is_abstract=True)
oclstdlib_Sequence = Class(name="oclstdlib::Sequence", is_abstract=True)
oclstdlib_Set = Class(name="oclstdlib::Set", is_abstract=True)
oclstdlib_UniqueCollection = Class(name="oclstdlib::UniqueCollection", is_abstract=True)

# oclstdlib_Collection class attributes and methods
oclstdlib_Collection_lower: Property = Property(name="lower", type=StringType)
oclstdlib_Collection_upper: Property = Property(name="upper", type=StringType)
oclstdlib_Collection.attributes={oclstdlib_Collection_upper, oclstdlib_Collection_lower}

# OclAny class attributes and methods

# oclstdlib_Bag class attributes and methods

# oclstdlib_OclAny class attributes and methods

# oclstdlib_OclComparable class attributes and methods

# oclstdlib_OclElement class attributes and methods

# oclstdlib_OclInvalid class attributes and methods

# OclVoid class attributes and methods

# oclstdlib_OclLambda class attributes and methods

# oclstdlib_OclMessage class attributes and methods

# oclstdlib_OclState class attributes and methods

# oclstdlib_OclSummable class attributes and methods

# oclstdlib_OclTuple class attributes and methods

# oclstdlib_OclType class attributes and methods

# OclElement class attributes and methods

# oclstdlib_OclVoid class attributes and methods

# oclstdlib_OrderedCollection class attributes and methods

# oclstdlib_OrderedSet class attributes and methods

# oclstdlib_Sequence class attributes and methods

# oclstdlib_Set class attributes and methods

# oclstdlib_UniqueCollection class attributes and methods

# Relationships
oclContents3: BinaryAssociation = BinaryAssociation(
    name="oclContents3",
    ends={
        Property(name="oclstdlib_OclElement4", type=oclstdlib_OclElement, multiplicity=Multiplicity(1, 1)),
        Property(name="oclstdlib_OclElement2", type=oclstdlib_OclElement, multiplicity=Multiplicity(0, 9999))
    }
)
oclContainer1: BinaryAssociation = BinaryAssociation(
    name="oclContainer1",
    ends={
        Property(name="oclstdlib_OclElement", type=oclstdlib_OclElement, multiplicity=Multiplicity(1, 1)),
        Property(name="oclstdlib_OclElement0", type=oclstdlib_OclElement, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_oclstdlib_Collection_OclAny = Generalization(general=OclAny, specific=oclstdlib_Collection)
gen_oclstdlib_OclComparable_OclAny = Generalization(general=OclAny, specific=oclstdlib_OclComparable)
gen_oclstdlib_OclElement_OclAny = Generalization(general=OclAny, specific=oclstdlib_OclElement)
gen_oclstdlib_OclInvalid_OclVoid = Generalization(general=OclVoid, specific=oclstdlib_OclInvalid)
gen_oclstdlib_OclLambda_OclAny = Generalization(general=OclAny, specific=oclstdlib_OclLambda)
gen_oclstdlib_OclMessage_OclAny = Generalization(general=OclAny, specific=oclstdlib_OclMessage)
gen_oclstdlib_OclState_OclAny = Generalization(general=OclAny, specific=oclstdlib_OclState)
gen_oclstdlib_OclSummable_OclAny = Generalization(general=OclAny, specific=oclstdlib_OclSummable)
gen_oclstdlib_OclTuple_OclAny = Generalization(general=OclAny, specific=oclstdlib_OclTuple)
gen_oclstdlib_OclType_OclElement = Generalization(general=OclElement, specific=oclstdlib_OclType)
gen_oclstdlib_OclVoid_OclAny = Generalization(general=OclAny, specific=oclstdlib_OclVoid)

# Domain Model
domain_model = DomainModel(
    name="oclstdlib",
    types={oclstdlib_Collection, OclAny, oclstdlib_Bag, oclstdlib_OclAny, oclstdlib_OclComparable, oclstdlib_OclElement, oclstdlib_OclInvalid, OclVoid, oclstdlib_OclLambda, oclstdlib_OclMessage, oclstdlib_OclState, oclstdlib_OclSummable, oclstdlib_OclTuple, oclstdlib_OclType, OclElement, oclstdlib_OclVoid, oclstdlib_OrderedCollection, oclstdlib_OrderedSet, oclstdlib_Sequence, oclstdlib_Set, oclstdlib_UniqueCollection},
    associations={oclContents3, oclContainer1},
    generalizations={gen_oclstdlib_Collection_OclAny, gen_oclstdlib_OclComparable_OclAny, gen_oclstdlib_OclElement_OclAny, gen_oclstdlib_OclInvalid_OclVoid, gen_oclstdlib_OclLambda_OclAny, gen_oclstdlib_OclMessage_OclAny, gen_oclstdlib_OclState_OclAny, gen_oclstdlib_OclSummable_OclAny, gen_oclstdlib_OclTuple_OclAny, gen_oclstdlib_OclType_OclElement, gen_oclstdlib_OclVoid_OclAny},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)