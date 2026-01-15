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
systemworkbench102_Workbench = Class(name="systemworkbench102::Workbench")
Named = Class(name="Named")
systemworkbench102_Thing = Class(name="systemworkbench102::Thing")
systemworkbench102_System = Class(name="systemworkbench102::System")
systemworkbench102_FunctionProperty = Class(name="systemworkbench102::FunctionProperty")
systemworkbench102_PatternCatalog = Class(name="systemworkbench102::PatternCatalog")
NamedElement = Class(name="NamedElement")
systemworkbench102_Thoughts = Class(name="systemworkbench102::Thoughts")
systemworkbench102_RelatedTo = Class(name="systemworkbench102::RelatedTo")
systemworkbench102_NamedElement = Class(name="systemworkbench102::NamedElement", is_abstract=True)
systemworkbench102_Named = Class(name="systemworkbench102::Named")
systemworkbench102_Component = Class(name="systemworkbench102::Component")
systemworkbench102_Function = Class(name="systemworkbench102::Function")

# systemworkbench102_Workbench class attributes and methods
systemworkbench102_Workbench_aprop: Property = Property(name="aprop", type=StringType)
systemworkbench102_Workbench.attributes={systemworkbench102_Workbench_aprop}

# Named class attributes and methods

# systemworkbench102_Thing class attributes and methods
systemworkbench102_Thing_id: Property = Property(name="id", type=IntegerType)
systemworkbench102_Thing.attributes={systemworkbench102_Thing_id}

# systemworkbench102_System class attributes and methods

# systemworkbench102_FunctionProperty class attributes and methods
systemworkbench102_FunctionProperty_description: Property = Property(name="description", type=StringType)
systemworkbench102_FunctionProperty.attributes={systemworkbench102_FunctionProperty_description}

# systemworkbench102_PatternCatalog class attributes and methods
systemworkbench102_PatternCatalog_id: Property = Property(name="id", type=IntegerType)
systemworkbench102_PatternCatalog.attributes={systemworkbench102_PatternCatalog_id}

# NamedElement class attributes and methods

# systemworkbench102_Thoughts class attributes and methods

# systemworkbench102_RelatedTo class attributes and methods
systemworkbench102_RelatedTo_since: Property = Property(name="since", type=StringType)
systemworkbench102_RelatedTo.attributes={systemworkbench102_RelatedTo_since}

# systemworkbench102_NamedElement class attributes and methods
systemworkbench102_NamedElement_name: Property = Property(name="name", type=StringType)
systemworkbench102_NamedElement.attributes={systemworkbench102_NamedElement_name}

# systemworkbench102_Named class attributes and methods
systemworkbench102_Named_ident: Property = Property(name="ident", type=StringType)
systemworkbench102_Named.attributes={systemworkbench102_Named_ident}

# systemworkbench102_Component class attributes and methods

# systemworkbench102_Function class attributes and methods

# Relationships
things0: BinaryAssociation = BinaryAssociation(
    name="things0",
    ends={
        Property(name="systemworkbench102_Thing", type=systemworkbench102_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="systemworkbench102_Workbench", type=systemworkbench102_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
systemView3: BinaryAssociation = BinaryAssociation(
    name="systemView3",
    ends={
        Property(name="systemworkbench102_System", type=systemworkbench102_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="systemworkbench102_Workbench4", type=systemworkbench102_System, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
functionProperties5: BinaryAssociation = BinaryAssociation(
    name="functionProperties5",
    ends={
        Property(name="systemworkbench102_FunctionProperty", type=systemworkbench102_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="systemworkbench102_Workbench6", type=systemworkbench102_FunctionProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
catalog7: BinaryAssociation = BinaryAssociation(
    name="catalog7",
    ends={
        Property(name="systemworkbench102_PatternCatalog", type=systemworkbench102_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="systemworkbench102_Workbench8", type=systemworkbench102_PatternCatalog, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thoughts1: BinaryAssociation = BinaryAssociation(
    name="thoughts1",
    ends={
        Property(name="systemworkbench102_Thoughts", type=systemworkbench102_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="systemworkbench102_Workbench2", type=systemworkbench102_Thoughts, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations9: BinaryAssociation = BinaryAssociation(
    name="relations9",
    ends={
        Property(name="RelatedTo", type=systemworkbench102_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="fromThing", type=systemworkbench102_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromThing10: BinaryAssociation = BinaryAssociation(
    name="fromThing10",
    ends={
        Property(name="Thing", type=systemworkbench102_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="relations", type=systemworkbench102_Thing, multiplicity=Multiplicity(0, 1))
    }
)
toThing11: BinaryAssociation = BinaryAssociation(
    name="toThing11",
    ends={
        Property(name="systemworkbench102_RelatedTo", type=systemworkbench102_Thing, multiplicity=Multiplicity(0, 1)),
        Property(name="systemworkbench102_Thing12", type=systemworkbench102_RelatedTo, multiplicity=Multiplicity(1, 1))
    }
)
relatedTo13: BinaryAssociation = BinaryAssociation(
    name="relatedTo13",
    ends={
        Property(name="systemworkbench102_Thing15", type=systemworkbench102_Thoughts, multiplicity=Multiplicity(1, 1)),
        Property(name="systemworkbench102_Thoughts14", type=systemworkbench102_Thing, multiplicity=Multiplicity(0, 9999))
    }
)
parent17: BinaryAssociation = BinaryAssociation(
    name="parent17",
    ends={
        Property(name="systemworkbench102_FunctionProperty18", type=systemworkbench102_FunctionProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="systemworkbench102_FunctionProperty16", type=systemworkbench102_FunctionProperty, multiplicity=Multiplicity(0, 1))
    }
)
decompositions20: BinaryAssociation = BinaryAssociation(
    name="decompositions20",
    ends={
        Property(name="systemworkbench102_Component", type=systemworkbench102_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="systemworkbench102_Component19", type=systemworkbench102_Component, multiplicity=Multiplicity(0, 9999))
    }
)
associations22: BinaryAssociation = BinaryAssociation(
    name="associations22",
    ends={
        Property(name="systemworkbench102_Component23", type=systemworkbench102_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="systemworkbench102_Component21", type=systemworkbench102_Component, multiplicity=Multiplicity(0, 9999))
    }
)
performs24: BinaryAssociation = BinaryAssociation(
    name="performs24",
    ends={
        Property(name="systemworkbench102_Function", type=systemworkbench102_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="systemworkbench102_Component25", type=systemworkbench102_Function, multiplicity=Multiplicity(0, 9999))
    }
)
decompositions27: BinaryAssociation = BinaryAssociation(
    name="decompositions27",
    ends={
        Property(name="systemworkbench102_Function28", type=systemworkbench102_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="systemworkbench102_Function26", type=systemworkbench102_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property29: BinaryAssociation = BinaryAssociation(
    name="property29",
    ends={
        Property(name="systemworkbench102_FunctionProperty31", type=systemworkbench102_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="systemworkbench102_Function30", type=systemworkbench102_FunctionProperty, multiplicity=Multiplicity(0, 9999))
    }
)
associations33: BinaryAssociation = BinaryAssociation(
    name="associations33",
    ends={
        Property(name="systemworkbench102_Function34", type=systemworkbench102_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="systemworkbench102_Function32", type=systemworkbench102_Function, multiplicity=Multiplicity(0, 1))
    }
)
allocatedTo35: BinaryAssociation = BinaryAssociation(
    name="allocatedTo35",
    ends={
        Property(name="systemworkbench102_Component37", type=systemworkbench102_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="systemworkbench102_Function36", type=systemworkbench102_Component, multiplicity=Multiplicity(0, 1))
    }
)
functionalArchitecture38: BinaryAssociation = BinaryAssociation(
    name="functionalArchitecture38",
    ends={
        Property(name="systemworkbench102_Function40", type=systemworkbench102_System, multiplicity=Multiplicity(1, 1)),
        Property(name="systemworkbench102_System39", type=systemworkbench102_Function, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
physicalArchitecture41: BinaryAssociation = BinaryAssociation(
    name="physicalArchitecture41",
    ends={
        Property(name="systemworkbench102_Component43", type=systemworkbench102_System, multiplicity=Multiplicity(1, 1)),
        Property(name="systemworkbench102_System42", type=systemworkbench102_Component, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
patterns44: BinaryAssociation = BinaryAssociation(
    name="patterns44",
    ends={
        Property(name="systemworkbench102_Function46", type=systemworkbench102_PatternCatalog, multiplicity=Multiplicity(1, 1)),
        Property(name="systemworkbench102_PatternCatalog45", type=systemworkbench102_Function, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_systemworkbench102_Workbench_Named = Generalization(general=Named, specific=systemworkbench102_Workbench)
gen_systemworkbench102_Thing_NamedElement = Generalization(general=NamedElement, specific=systemworkbench102_Thing)
gen_systemworkbench102_RelatedTo_NamedElement = Generalization(general=NamedElement, specific=systemworkbench102_RelatedTo)
gen_systemworkbench102_Thoughts_NamedElement = Generalization(general=NamedElement, specific=systemworkbench102_Thoughts)
gen_systemworkbench102_FunctionProperty_Named = Generalization(general=Named, specific=systemworkbench102_FunctionProperty)
gen_systemworkbench102_Component_Named = Generalization(general=Named, specific=systemworkbench102_Component)
gen_systemworkbench102_Function_Named = Generalization(general=Named, specific=systemworkbench102_Function)
gen_systemworkbench102_System_Named = Generalization(general=Named, specific=systemworkbench102_System)

# Domain Model
domain_model = DomainModel(
    name="systemworkbench102",
    types={systemworkbench102_Workbench, Named, systemworkbench102_Thing, systemworkbench102_System, systemworkbench102_FunctionProperty, systemworkbench102_PatternCatalog, NamedElement, systemworkbench102_Thoughts, systemworkbench102_RelatedTo, systemworkbench102_NamedElement, systemworkbench102_Named, systemworkbench102_Component, systemworkbench102_Function},
    associations={things0, systemView3, functionProperties5, catalog7, thoughts1, relations9, fromThing10, toThing11, relatedTo13, parent17, decompositions20, associations22, performs24, decompositions27, property29, associations33, allocatedTo35, functionalArchitecture38, physicalArchitecture41, patterns44},
    generalizations={gen_systemworkbench102_Workbench_Named, gen_systemworkbench102_Thing_NamedElement, gen_systemworkbench102_RelatedTo_NamedElement, gen_systemworkbench102_Thoughts_NamedElement, gen_systemworkbench102_FunctionProperty_Named, gen_systemworkbench102_Component_Named, gen_systemworkbench102_Function_Named, gen_systemworkbench102_System_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)