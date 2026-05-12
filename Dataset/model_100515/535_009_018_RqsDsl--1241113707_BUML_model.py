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
rqsDsl_Model = Class(name="rqsDsl_Model")
rqsDsl_TAnnotation = Class(name="rqsDsl_TAnnotation")
rqsDsl_Requirement = Class(name="rqsDsl_Requirement")
rqsDsl_EObject = Class(name="rqsDsl_EObject")
rqsDsl_RAnnotation = Class(name="rqsDsl_RAnnotation")

# rqsDsl_Model class attributes and methods

# rqsDsl_TAnnotation class attributes and methods
rqsDsl_TAnnotation_text: Property = Property(name="text", type=StringType)
rqsDsl_TAnnotation_num: Property = Property(name="num", type=IntegerType)
rqsDsl_TAnnotation_id: Property = Property(name="id", type=IntegerType)
rqsDsl_TAnnotation_type: Property = Property(name="type", type=StringType)
rqsDsl_TAnnotation_a: Property = Property(name="a", type=IntegerType)
rqsDsl_TAnnotation_b: Property = Property(name="b", type=IntegerType)
rqsDsl_TAnnotation.attributes={rqsDsl_TAnnotation_id, rqsDsl_TAnnotation_type, rqsDsl_TAnnotation_num, rqsDsl_TAnnotation_b, rqsDsl_TAnnotation_a, rqsDsl_TAnnotation_text}

# rqsDsl_Requirement class attributes and methods
rqsDsl_Requirement_text: Property = Property(name="text", type=StringType)
rqsDsl_Requirement.attributes={rqsDsl_Requirement_text}

# rqsDsl_EObject class attributes and methods

# rqsDsl_RAnnotation class attributes and methods
rqsDsl_RAnnotation_num: Property = Property(name="num", type=IntegerType)
rqsDsl_RAnnotation_id: Property = Property(name="id", type=IntegerType)
rqsDsl_RAnnotation_type: Property = Property(name="type", type=StringType)
rqsDsl_RAnnotation_aa: Property = Property(name="aa", type=IntegerType)
rqsDsl_RAnnotation_ab: Property = Property(name="ab", type=IntegerType)
rqsDsl_RAnnotation_ba: Property = Property(name="ba", type=IntegerType)
rqsDsl_RAnnotation_bb: Property = Property(name="bb", type=IntegerType)
rqsDsl_RAnnotation.attributes={rqsDsl_RAnnotation_id, rqsDsl_RAnnotation_ba, rqsDsl_RAnnotation_bb, rqsDsl_RAnnotation_ab, rqsDsl_RAnnotation_type, rqsDsl_RAnnotation_num, rqsDsl_RAnnotation_aa}

# Relationships
requirements0: BinaryAssociation = BinaryAssociation(
    name="requirements0",
    ends={
        Property(name="rqsDsl_Requirement", type=rqsDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="rqsDsl_Model", type=rqsDsl_Requirement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations1: BinaryAssociation = BinaryAssociation(
    name="annotations1",
    ends={
        Property(name="rqsDsl_EObject", type=rqsDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="rqsDsl_Model2", type=rqsDsl_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="rqsDsl",
    types={rqsDsl_Model, rqsDsl_TAnnotation, rqsDsl_Requirement, rqsDsl_EObject, rqsDsl_RAnnotation},
    associations={requirements0, annotations1},
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