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
syswb103_Workbench = Class(name="syswb103::Workbench")
NamedElement = Class(name="NamedElement")
syswb103_Thing = Class(name="syswb103::Thing")
syswb103_Thoughts = Class(name="syswb103::Thoughts")
syswb103_System = Class(name="syswb103::System")
syswb103_FunctionProperty = Class(name="syswb103::FunctionProperty")
syswb103_PatternCatalog = Class(name="syswb103::PatternCatalog")
syswb103_RelatedTo = Class(name="syswb103::RelatedTo")
syswb103_NamedElement = Class(name="syswb103::NamedElement", is_abstract=True)
syswb103_Component = Class(name="syswb103::Component")
syswb103_Function = Class(name="syswb103::Function")

# syswb103_Workbench class attributes and methods
syswb103_Workbench_aprop: Property = Property(name="aprop", type=StringType)
syswb103_Workbench.attributes={syswb103_Workbench_aprop}

# NamedElement class attributes and methods

# syswb103_Thing class attributes and methods
syswb103_Thing_id: Property = Property(name="id", type=IntegerType)
syswb103_Thing.attributes={syswb103_Thing_id}

# syswb103_Thoughts class attributes and methods

# syswb103_System class attributes and methods

# syswb103_FunctionProperty class attributes and methods
syswb103_FunctionProperty_description: Property = Property(name="description", type=StringType)
syswb103_FunctionProperty.attributes={syswb103_FunctionProperty_description}

# syswb103_PatternCatalog class attributes and methods
syswb103_PatternCatalog_id: Property = Property(name="id", type=StringType)
syswb103_PatternCatalog.attributes={syswb103_PatternCatalog_id}

# syswb103_RelatedTo class attributes and methods
syswb103_RelatedTo_since: Property = Property(name="since", type=StringType)
syswb103_RelatedTo.attributes={syswb103_RelatedTo_since}

# syswb103_NamedElement class attributes and methods
syswb103_NamedElement_name: Property = Property(name="name", type=StringType)
syswb103_NamedElement.attributes={syswb103_NamedElement_name}

# syswb103_Component class attributes and methods

# syswb103_Function class attributes and methods

# Relationships
things0: BinaryAssociation = BinaryAssociation(
    name="things0",
    ends={
        Property(name="syswb103_Thing", type=syswb103_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb103_Workbench", type=syswb103_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thoughts1: BinaryAssociation = BinaryAssociation(
    name="thoughts1",
    ends={
        Property(name="syswb103_Thoughts", type=syswb103_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb103_Workbench2", type=syswb103_Thoughts, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
systemView3: BinaryAssociation = BinaryAssociation(
    name="systemView3",
    ends={
        Property(name="syswb103_System", type=syswb103_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb103_Workbench4", type=syswb103_System, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
functionProperties5: BinaryAssociation = BinaryAssociation(
    name="functionProperties5",
    ends={
        Property(name="syswb103_FunctionProperty", type=syswb103_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb103_Workbench6", type=syswb103_FunctionProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
catalog7: BinaryAssociation = BinaryAssociation(
    name="catalog7",
    ends={
        Property(name="syswb103_PatternCatalog", type=syswb103_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb103_Workbench8", type=syswb103_PatternCatalog, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations9: BinaryAssociation = BinaryAssociation(
    name="relations9",
    ends={
        Property(name="RelatedTo", type=syswb103_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="fromThing", type=syswb103_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromThing10: BinaryAssociation = BinaryAssociation(
    name="fromThing10",
    ends={
        Property(name="Thing", type=syswb103_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="relations", type=syswb103_Thing, multiplicity=Multiplicity(0, 1))
    }
)
toThing11: BinaryAssociation = BinaryAssociation(
    name="toThing11",
    ends={
        Property(name="syswb103_Thing12", type=syswb103_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb103_RelatedTo", type=syswb103_Thing, multiplicity=Multiplicity(0, 1))
    }
)
relatedTo13: BinaryAssociation = BinaryAssociation(
    name="relatedTo13",
    ends={
        Property(name="syswb103_Thing15", type=syswb103_Thoughts, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb103_Thoughts14", type=syswb103_Thing, multiplicity=Multiplicity(0, 9999))
    }
)
parent17: BinaryAssociation = BinaryAssociation(
    name="parent17",
    ends={
        Property(name="syswb103_FunctionProperty18", type=syswb103_FunctionProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb103_FunctionProperty16", type=syswb103_FunctionProperty, multiplicity=Multiplicity(0, 1))
    }
)
decompositions20: BinaryAssociation = BinaryAssociation(
    name="decompositions20",
    ends={
        Property(name="syswb103_Component", type=syswb103_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb103_Component19", type=syswb103_Component, multiplicity=Multiplicity(0, 9999))
    }
)
associations22: BinaryAssociation = BinaryAssociation(
    name="associations22",
    ends={
        Property(name="syswb103_Component23", type=syswb103_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb103_Component21", type=syswb103_Component, multiplicity=Multiplicity(0, 9999))
    }
)
performs24: BinaryAssociation = BinaryAssociation(
    name="performs24",
    ends={
        Property(name="syswb103_Function", type=syswb103_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb103_Component25", type=syswb103_Function, multiplicity=Multiplicity(0, 9999))
    }
)
physicalArchitecture41: BinaryAssociation = BinaryAssociation(
    name="physicalArchitecture41",
    ends={
        Property(name="syswb103_Component43", type=syswb103_System, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb103_System42", type=syswb103_Component, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
decompositions27: BinaryAssociation = BinaryAssociation(
    name="decompositions27",
    ends={
        Property(name="syswb103_Function28", type=syswb103_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb103_Function26", type=syswb103_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property29: BinaryAssociation = BinaryAssociation(
    name="property29",
    ends={
        Property(name="syswb103_FunctionProperty31", type=syswb103_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb103_Function30", type=syswb103_FunctionProperty, multiplicity=Multiplicity(0, 9999))
    }
)
associations33: BinaryAssociation = BinaryAssociation(
    name="associations33",
    ends={
        Property(name="syswb103_Function34", type=syswb103_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb103_Function32", type=syswb103_Function, multiplicity=Multiplicity(0, 1))
    }
)
allocatedTo35: BinaryAssociation = BinaryAssociation(
    name="allocatedTo35",
    ends={
        Property(name="syswb103_Component37", type=syswb103_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb103_Function36", type=syswb103_Component, multiplicity=Multiplicity(0, 1))
    }
)
functionalArchitecture38: BinaryAssociation = BinaryAssociation(
    name="functionalArchitecture38",
    ends={
        Property(name="syswb103_Function40", type=syswb103_System, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb103_System39", type=syswb103_Function, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
patterns44: BinaryAssociation = BinaryAssociation(
    name="patterns44",
    ends={
        Property(name="syswb103_Function46", type=syswb103_PatternCatalog, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb103_PatternCatalog45", type=syswb103_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_syswb103_Workbench_NamedElement = Generalization(general=NamedElement, specific=syswb103_Workbench)
gen_syswb103_Thing_NamedElement = Generalization(general=NamedElement, specific=syswb103_Thing)
gen_syswb103_RelatedTo_NamedElement = Generalization(general=NamedElement, specific=syswb103_RelatedTo)
gen_syswb103_Thoughts_NamedElement = Generalization(general=NamedElement, specific=syswb103_Thoughts)
gen_syswb103_FunctionProperty_NamedElement = Generalization(general=NamedElement, specific=syswb103_FunctionProperty)
gen_syswb103_Component_NamedElement = Generalization(general=NamedElement, specific=syswb103_Component)
gen_syswb103_Function_NamedElement = Generalization(general=NamedElement, specific=syswb103_Function)
gen_syswb103_System_NamedElement = Generalization(general=NamedElement, specific=syswb103_System)

# Domain Model
domain_model = DomainModel(
    name="syswb103",
    types={syswb103_Workbench, NamedElement, syswb103_Thing, syswb103_Thoughts, syswb103_System, syswb103_FunctionProperty, syswb103_PatternCatalog, syswb103_RelatedTo, syswb103_NamedElement, syswb103_Component, syswb103_Function},
    associations={things0, thoughts1, systemView3, functionProperties5, catalog7, relations9, fromThing10, toThing11, relatedTo13, parent17, decompositions20, associations22, performs24, physicalArchitecture41, decompositions27, property29, associations33, allocatedTo35, functionalArchitecture38, patterns44},
    generalizations={gen_syswb103_Workbench_NamedElement, gen_syswb103_Thing_NamedElement, gen_syswb103_RelatedTo_NamedElement, gen_syswb103_Thoughts_NamedElement, gen_syswb103_FunctionProperty_NamedElement, gen_syswb103_Component_NamedElement, gen_syswb103_Function_NamedElement, gen_syswb103_System_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)