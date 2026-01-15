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
systemworkbench101_Function = Class(name="systemworkbench101::Function")
systemworkbench101_Component = Class(name="systemworkbench101::Component")
systemworkbench101_Workbench = Class(name="systemworkbench101::Workbench")
systemworkbench101_FunctionProperty = Class(name="systemworkbench101::FunctionProperty")
systemworkbench101_System = Class(name="systemworkbench101::System")
Named = Class(name="Named")
systemworkbench101_PatternCatalog = Class(name="systemworkbench101::PatternCatalog")
systemworkbench101_Thing = Class(name="systemworkbench101::Thing")
systemworkbench101_Thoughts = Class(name="systemworkbench101::Thoughts")
systemworkbench101_Named = Class(name="systemworkbench101::Named", is_abstract=True)
systemworkbench101_RelatedTo = Class(name="systemworkbench101::RelatedTo")
NamedElement = Class(name="NamedElement")
systemworkbench101_NamedElement = Class(name="systemworkbench101::NamedElement")

# systemworkbench101_Function class attributes and methods

# systemworkbench101_Component class attributes and methods

# systemworkbench101_Workbench class attributes and methods
systemworkbench101_Workbench_foobar: Property = Property(name="foobar", type=StringType)
systemworkbench101_Workbench.attributes={systemworkbench101_Workbench_foobar}

# systemworkbench101_FunctionProperty class attributes and methods
systemworkbench101_FunctionProperty_description: Property = Property(name="description", type=StringType)
systemworkbench101_FunctionProperty.attributes={systemworkbench101_FunctionProperty_description}

# systemworkbench101_System class attributes and methods

# Named class attributes and methods

# systemworkbench101_PatternCatalog class attributes and methods
systemworkbench101_PatternCatalog_id: Property = Property(name="id", type=IntegerType)
systemworkbench101_PatternCatalog.attributes={systemworkbench101_PatternCatalog_id}

# systemworkbench101_Thing class attributes and methods
systemworkbench101_Thing_id: Property = Property(name="id", type=IntegerType)
systemworkbench101_Thing.attributes={systemworkbench101_Thing_id}

# systemworkbench101_Thoughts class attributes and methods

# systemworkbench101_Named class attributes and methods
systemworkbench101_Named_ident: Property = Property(name="ident", type=StringType)
systemworkbench101_Named.attributes={systemworkbench101_Named_ident}

# systemworkbench101_RelatedTo class attributes and methods
systemworkbench101_RelatedTo_since: Property = Property(name="since", type=StringType)
systemworkbench101_RelatedTo.attributes={systemworkbench101_RelatedTo_since}

# NamedElement class attributes and methods

# systemworkbench101_NamedElement class attributes and methods
systemworkbench101_NamedElement_name: Property = Property(name="name", type=StringType)
systemworkbench101_NamedElement.attributes={systemworkbench101_NamedElement_name}

# Relationships
functionalArchitecture0: BinaryAssociation = BinaryAssociation(
    name="functionalArchitecture0",
    ends={
        Property(name="systemworkbench101_Function", type=systemworkbench101_System, multiplicity=Multiplicity(1, 1)),
        Property(name="systemworkbench101_System", type=systemworkbench101_Function, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
physicalArchitecture1: BinaryAssociation = BinaryAssociation(
    name="physicalArchitecture1",
    ends={
        Property(name="systemworkbench101_Component", type=systemworkbench101_System, multiplicity=Multiplicity(1, 1)),
        Property(name="systemworkbench101_System2", type=systemworkbench101_Component, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
systemView3: BinaryAssociation = BinaryAssociation(
    name="systemView3",
    ends={
        Property(name="systemworkbench101_System4", type=systemworkbench101_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="systemworkbench101_Workbench", type=systemworkbench101_System, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
associations23: BinaryAssociation = BinaryAssociation(
    name="associations23",
    ends={
        Property(name="systemworkbench101_Function24", type=systemworkbench101_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="systemworkbench101_Function22", type=systemworkbench101_Function, multiplicity=Multiplicity(0, 1))
    }
)
allocatedTo25: BinaryAssociation = BinaryAssociation(
    name="allocatedTo25",
    ends={
        Property(name="Component", type=systemworkbench101_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="performs", type=systemworkbench101_Component, multiplicity=Multiplicity(0, 1))
    }
)
decompositions27: BinaryAssociation = BinaryAssociation(
    name="decompositions27",
    ends={
        Property(name="systemworkbench101_Component28", type=systemworkbench101_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="systemworkbench101_Component26", type=systemworkbench101_Component, multiplicity=Multiplicity(0, 9999))
    }
)
functionProperties5: BinaryAssociation = BinaryAssociation(
    name="functionProperties5",
    ends={
        Property(name="systemworkbench101_FunctionProperty", type=systemworkbench101_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="systemworkbench101_Workbench6", type=systemworkbench101_FunctionProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
catalog7: BinaryAssociation = BinaryAssociation(
    name="catalog7",
    ends={
        Property(name="systemworkbench101_PatternCatalog", type=systemworkbench101_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="systemworkbench101_Workbench8", type=systemworkbench101_PatternCatalog, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
things9: BinaryAssociation = BinaryAssociation(
    name="things9",
    ends={
        Property(name="systemworkbench101_Thing", type=systemworkbench101_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="systemworkbench101_Workbench10", type=systemworkbench101_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thoughts11: BinaryAssociation = BinaryAssociation(
    name="thoughts11",
    ends={
        Property(name="systemworkbench101_Thoughts", type=systemworkbench101_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="systemworkbench101_Workbench12", type=systemworkbench101_Thoughts, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent14: BinaryAssociation = BinaryAssociation(
    name="parent14",
    ends={
        Property(name="systemworkbench101_FunctionProperty15", type=systemworkbench101_FunctionProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="systemworkbench101_FunctionProperty13", type=systemworkbench101_FunctionProperty, multiplicity=Multiplicity(0, 1))
    }
)
decompositions17: BinaryAssociation = BinaryAssociation(
    name="decompositions17",
    ends={
        Property(name="systemworkbench101_Function18", type=systemworkbench101_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="systemworkbench101_Function16", type=systemworkbench101_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property19: BinaryAssociation = BinaryAssociation(
    name="property19",
    ends={
        Property(name="systemworkbench101_FunctionProperty21", type=systemworkbench101_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="systemworkbench101_Function20", type=systemworkbench101_FunctionProperty, multiplicity=Multiplicity(0, 9999))
    }
)
associations30: BinaryAssociation = BinaryAssociation(
    name="associations30",
    ends={
        Property(name="systemworkbench101_Component31", type=systemworkbench101_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="systemworkbench101_Component29", type=systemworkbench101_Component, multiplicity=Multiplicity(0, 9999))
    }
)
performs32: BinaryAssociation = BinaryAssociation(
    name="performs32",
    ends={
        Property(name="Function", type=systemworkbench101_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="allocatedTo", type=systemworkbench101_Function, multiplicity=Multiplicity(0, 9999))
    }
)
patterns33: BinaryAssociation = BinaryAssociation(
    name="patterns33",
    ends={
        Property(name="systemworkbench101_Function35", type=systemworkbench101_PatternCatalog, multiplicity=Multiplicity(1, 1)),
        Property(name="systemworkbench101_PatternCatalog34", type=systemworkbench101_Function, multiplicity=Multiplicity(0, 9999))
    }
)
toThing38: BinaryAssociation = BinaryAssociation(
    name="toThing38",
    ends={
        Property(name="systemworkbench101_Thing40", type=systemworkbench101_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="systemworkbench101_RelatedTo39", type=systemworkbench101_Thing, multiplicity=Multiplicity(0, 1))
    }
)
fromThing36: BinaryAssociation = BinaryAssociation(
    name="fromThing36",
    ends={
        Property(name="systemworkbench101_Thing37", type=systemworkbench101_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="systemworkbench101_RelatedTo", type=systemworkbench101_Thing, multiplicity=Multiplicity(0, 1))
    }
)
relations41: BinaryAssociation = BinaryAssociation(
    name="relations41",
    ends={
        Property(name="systemworkbench101_RelatedTo43", type=systemworkbench101_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="systemworkbench101_Thing42", type=systemworkbench101_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relatedTo44: BinaryAssociation = BinaryAssociation(
    name="relatedTo44",
    ends={
        Property(name="systemworkbench101_Thing46", type=systemworkbench101_Thoughts, multiplicity=Multiplicity(1, 1)),
        Property(name="systemworkbench101_Thoughts45", type=systemworkbench101_Thing, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_systemworkbench101_Workbench_Named = Generalization(general=Named, specific=systemworkbench101_Workbench)
gen_systemworkbench101_System_Named = Generalization(general=Named, specific=systemworkbench101_System)
gen_systemworkbench101_Component_Named = Generalization(general=Named, specific=systemworkbench101_Component)
gen_systemworkbench101_FunctionProperty_Named = Generalization(general=Named, specific=systemworkbench101_FunctionProperty)
gen_systemworkbench101_Function_Named = Generalization(general=Named, specific=systemworkbench101_Function)
gen_systemworkbench101_RelatedTo_NamedElement = Generalization(general=NamedElement, specific=systemworkbench101_RelatedTo)
gen_systemworkbench101_Thing_NamedElement = Generalization(general=NamedElement, specific=systemworkbench101_Thing)
gen_systemworkbench101_Thoughts_NamedElement = Generalization(general=NamedElement, specific=systemworkbench101_Thoughts)

# Domain Model
domain_model = DomainModel(
    name="systemworkbench101",
    types={systemworkbench101_Function, systemworkbench101_Component, systemworkbench101_Workbench, systemworkbench101_FunctionProperty, systemworkbench101_System, Named, systemworkbench101_PatternCatalog, systemworkbench101_Thing, systemworkbench101_Thoughts, systemworkbench101_Named, systemworkbench101_RelatedTo, NamedElement, systemworkbench101_NamedElement},
    associations={functionalArchitecture0, physicalArchitecture1, systemView3, associations23, allocatedTo25, decompositions27, functionProperties5, catalog7, things9, thoughts11, parent14, decompositions17, property19, associations30, performs32, patterns33, toThing38, fromThing36, relations41, relatedTo44},
    generalizations={gen_systemworkbench101_Workbench_Named, gen_systemworkbench101_System_Named, gen_systemworkbench101_Component_Named, gen_systemworkbench101_FunctionProperty_Named, gen_systemworkbench101_Function_Named, gen_systemworkbench101_RelatedTo_NamedElement, gen_systemworkbench101_Thing_NamedElement, gen_systemworkbench101_Thoughts_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)