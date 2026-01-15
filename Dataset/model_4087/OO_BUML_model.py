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
simpleuml_Class = Class(name="simpleuml::Class")
Classifier = Class(name="Classifier")
simpleuml_Classifier = Class(name="simpleuml::Classifier", is_abstract=True)

# simpleuml_Class class attributes and methods
simpleuml_Class_name: Property = Property(name="name", type=StringType)
simpleuml_Class.attributes={simpleuml_Class_name}

# Classifier class attributes and methods

# simpleuml_Classifier class attributes and methods

# Relationships
generalizationGeneral0: BinaryAssociation = BinaryAssociation(
    name="generalizationGeneral0",
    ends={
        Property(name="simpleuml_Classifier", type=simpleuml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleuml_Class", type=simpleuml_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_simpleuml_Class_Classifier = Generalization(general=Classifier, specific=simpleuml_Class)

# Domain Model
domain_model = DomainModel(
    name="simpleuml",
    types={simpleuml_Class, Classifier, simpleuml_Classifier},
    associations={generalizationGeneral0},
    generalizations={gen_simpleuml_Class_Classifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)