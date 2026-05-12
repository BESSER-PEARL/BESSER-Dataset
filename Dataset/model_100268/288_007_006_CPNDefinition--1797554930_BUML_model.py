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
cpndefinition_CPN = Class(name="cpndefinition_CPN")
PetriNetType = Class(name="PetriNetType")
cpndefinition_Place = Class(name="cpndefinition_Place")
Place = Class(name="Place")
cpndefinition_InitialMarking = Class(name="cpndefinition_InitialMarking")
cpndefinition_Arc = Class(name="cpndefinition_Arc")
Arc = Class(name="Arc")
cpndefinition_ArcExpression = Class(name="cpndefinition_ArcExpression")
cpndefinition_Transition = Class(name="cpndefinition_Transition")
Transition = Class(name="Transition")
cpndefinition_Guard = Class(name="cpndefinition_Guard")
cpndefinition_Page = Class(name="cpndefinition_Page")
Page = Class(name="Page")
CPNInscription = Class(name="CPNInscription")
cpndefinition_CPNInscription = Class(name="cpndefinition_CPNInscription")
Label = Class(name="Label")
cpndefinition_Sort = Class(name="cpndefinition_Sort")

# cpndefinition_CPN class attributes and methods

# PetriNetType class attributes and methods

# cpndefinition_Place class attributes and methods

# Place class attributes and methods

# cpndefinition_InitialMarking class attributes and methods

# cpndefinition_Arc class attributes and methods

# Arc class attributes and methods

# cpndefinition_ArcExpression class attributes and methods

# cpndefinition_Transition class attributes and methods

# Transition class attributes and methods

# cpndefinition_Guard class attributes and methods

# cpndefinition_Page class attributes and methods

# Page class attributes and methods

# CPNInscription class attributes and methods

# cpndefinition_CPNInscription class attributes and methods
cpndefinition_CPNInscription_text: Property = Property(name="text", type=StringType)
cpndefinition_CPNInscription.attributes={cpndefinition_CPNInscription_text}

# Label class attributes and methods

# cpndefinition_Sort class attributes and methods

# Relationships
expression3: BinaryAssociation = BinaryAssociation(
    name="expression3",
    ends={
        Property(name="cpndefinition_ArcExpression", type=cpndefinition_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="cpndefinition_Arc", type=cpndefinition_ArcExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
guard4: BinaryAssociation = BinaryAssociation(
    name="guard4",
    ends={
        Property(name="cpndefinition_Guard", type=cpndefinition_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="cpndefinition_Transition", type=cpndefinition_Guard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initialMarking0: BinaryAssociation = BinaryAssociation(
    name="initialMarking0",
    ends={
        Property(name="cpndefinition_InitialMarking", type=cpndefinition_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="cpndefinition_Place", type=cpndefinition_InitialMarking, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sort1: BinaryAssociation = BinaryAssociation(
    name="sort1",
    ends={
        Property(name="cpndefinition_Sort", type=cpndefinition_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="cpndefinition_Place2", type=cpndefinition_Sort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_cpndefinition_CPN_PetriNetType = Generalization(general=PetriNetType, specific=cpndefinition_CPN)
gen_cpndefinition_Place_Place = Generalization(general=Place, specific=cpndefinition_Place)
gen_cpndefinition_Arc_Arc = Generalization(general=Arc, specific=cpndefinition_Arc)
gen_cpndefinition_Transition_Transition = Generalization(general=Transition, specific=cpndefinition_Transition)
gen_cpndefinition_Page_Page = Generalization(general=Page, specific=cpndefinition_Page)
gen_cpndefinition_ArcExpression_CPNInscription = Generalization(general=CPNInscription, specific=cpndefinition_ArcExpression)
gen_cpndefinition_CPNInscription_Label = Generalization(general=Label, specific=cpndefinition_CPNInscription)
gen_cpndefinition_Guard_CPNInscription = Generalization(general=CPNInscription, specific=cpndefinition_Guard)
gen_cpndefinition_InitialMarking_CPNInscription = Generalization(general=CPNInscription, specific=cpndefinition_InitialMarking)
gen_cpndefinition_Sort_CPNInscription = Generalization(general=CPNInscription, specific=cpndefinition_Sort)

# Domain Model
domain_model = DomainModel(
    name="cpndefinition",
    types={cpndefinition_CPN, PetriNetType, cpndefinition_Place, Place, cpndefinition_InitialMarking, cpndefinition_Arc, Arc, cpndefinition_ArcExpression, cpndefinition_Transition, Transition, cpndefinition_Guard, cpndefinition_Page, Page, CPNInscription, cpndefinition_CPNInscription, Label, cpndefinition_Sort},
    associations={expression3, guard4, initialMarking0, sort1},
    generalizations={gen_cpndefinition_CPN_PetriNetType, gen_cpndefinition_Place_Place, gen_cpndefinition_Arc_Arc, gen_cpndefinition_Transition_Transition, gen_cpndefinition_Page_Page, gen_cpndefinition_ArcExpression_CPNInscription, gen_cpndefinition_CPNInscription_Label, gen_cpndefinition_Guard_CPNInscription, gen_cpndefinition_InitialMarking_CPNInscription, gen_cpndefinition_Sort_CPNInscription},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)