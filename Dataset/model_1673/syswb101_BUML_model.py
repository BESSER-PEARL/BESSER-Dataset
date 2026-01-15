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
syswb101_Thoughts = Class(name="syswb101::Thoughts")
syswb101_System = Class(name="syswb101::System")
syswb101_FunctionProperty = Class(name="syswb101::FunctionProperty")
syswb101_PatternCatalog = Class(name="syswb101::PatternCatalog")
NamedElement = Class(name="NamedElement")
syswb101_Workbench = Class(name="syswb101::Workbench")
Named = Class(name="Named")
syswb101_Thing = Class(name="syswb101::Thing")
syswb101_Component = Class(name="syswb101::Component")
syswb101_RelatedTo = Class(name="syswb101::RelatedTo")
syswb101_NamedElement = Class(name="syswb101::NamedElement", is_abstract=True)
syswb101_Named = Class(name="syswb101::Named", is_abstract=True)
syswb101_Function = Class(name="syswb101::Function")

# syswb101_Thoughts class attributes and methods

# syswb101_System class attributes and methods

# syswb101_FunctionProperty class attributes and methods
syswb101_FunctionProperty_description: Property = Property(name="description", type=StringType)
syswb101_FunctionProperty.attributes={syswb101_FunctionProperty_description}

# syswb101_PatternCatalog class attributes and methods
syswb101_PatternCatalog_id: Property = Property(name="id", type=StringType)
syswb101_PatternCatalog.attributes={syswb101_PatternCatalog_id}

# NamedElement class attributes and methods

# syswb101_Workbench class attributes and methods
syswb101_Workbench_aprop: Property = Property(name="aprop", type=StringType)
syswb101_Workbench.attributes={syswb101_Workbench_aprop}

# Named class attributes and methods

# syswb101_Thing class attributes and methods
syswb101_Thing_id: Property = Property(name="id", type=IntegerType)
syswb101_Thing.attributes={syswb101_Thing_id}

# syswb101_Component class attributes and methods

# syswb101_RelatedTo class attributes and methods
syswb101_RelatedTo_since: Property = Property(name="since", type=StringType)
syswb101_RelatedTo.attributes={syswb101_RelatedTo_since}

# syswb101_NamedElement class attributes and methods
syswb101_NamedElement_name: Property = Property(name="name", type=StringType)
syswb101_NamedElement.attributes={syswb101_NamedElement_name}

# syswb101_Named class attributes and methods
syswb101_Named_ident: Property = Property(name="ident", type=StringType)
syswb101_Named.attributes={syswb101_Named_ident}

# syswb101_Function class attributes and methods

# Relationships
thoughts1: BinaryAssociation = BinaryAssociation(
    name="thoughts1",
    ends={
        Property(name="syswb101_Thoughts", type=syswb101_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb101_Workbench2", type=syswb101_Thoughts, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
systemView3: BinaryAssociation = BinaryAssociation(
    name="systemView3",
    ends={
        Property(name="syswb101_System", type=syswb101_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb101_Workbench4", type=syswb101_System, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
functionProperties5: BinaryAssociation = BinaryAssociation(
    name="functionProperties5",
    ends={
        Property(name="syswb101_FunctionProperty", type=syswb101_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb101_Workbench6", type=syswb101_FunctionProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
catalog7: BinaryAssociation = BinaryAssociation(
    name="catalog7",
    ends={
        Property(name="syswb101_PatternCatalog", type=syswb101_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb101_Workbench8", type=syswb101_PatternCatalog, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
things0: BinaryAssociation = BinaryAssociation(
    name="things0",
    ends={
        Property(name="syswb101_Thing", type=syswb101_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb101_Workbench", type=syswb101_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromThing10: BinaryAssociation = BinaryAssociation(
    name="fromThing10",
    ends={
        Property(name="Thing", type=syswb101_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="relations", type=syswb101_Thing, multiplicity=Multiplicity(0, 1))
    }
)
toThing11: BinaryAssociation = BinaryAssociation(
    name="toThing11",
    ends={
        Property(name="syswb101_Thing12", type=syswb101_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb101_RelatedTo", type=syswb101_Thing, multiplicity=Multiplicity(0, 1))
    }
)
relatedTo13: BinaryAssociation = BinaryAssociation(
    name="relatedTo13",
    ends={
        Property(name="syswb101_Thing15", type=syswb101_Thoughts, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb101_Thoughts14", type=syswb101_Thing, multiplicity=Multiplicity(0, 9999))
    }
)
relations9: BinaryAssociation = BinaryAssociation(
    name="relations9",
    ends={
        Property(name="RelatedTo", type=syswb101_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="fromThing", type=syswb101_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent17: BinaryAssociation = BinaryAssociation(
    name="parent17",
    ends={
        Property(name="syswb101_FunctionProperty18", type=syswb101_FunctionProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb101_FunctionProperty16", type=syswb101_FunctionProperty, multiplicity=Multiplicity(0, 1))
    }
)
associations33: BinaryAssociation = BinaryAssociation(
    name="associations33",
    ends={
        Property(name="syswb101_Function34", type=syswb101_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb101_Function32", type=syswb101_Function, multiplicity=Multiplicity(0, 1))
    }
)
allocatedTo35: BinaryAssociation = BinaryAssociation(
    name="allocatedTo35",
    ends={
        Property(name="syswb101_Component37", type=syswb101_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb101_Function36", type=syswb101_Component, multiplicity=Multiplicity(0, 1))
    }
)
decompositions20: BinaryAssociation = BinaryAssociation(
    name="decompositions20",
    ends={
        Property(name="syswb101_Component", type=syswb101_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb101_Component19", type=syswb101_Component, multiplicity=Multiplicity(0, 9999))
    }
)
associations22: BinaryAssociation = BinaryAssociation(
    name="associations22",
    ends={
        Property(name="syswb101_Component23", type=syswb101_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb101_Component21", type=syswb101_Component, multiplicity=Multiplicity(0, 9999))
    }
)
performs24: BinaryAssociation = BinaryAssociation(
    name="performs24",
    ends={
        Property(name="syswb101_Function", type=syswb101_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb101_Component25", type=syswb101_Function, multiplicity=Multiplicity(0, 9999))
    }
)
decompositions27: BinaryAssociation = BinaryAssociation(
    name="decompositions27",
    ends={
        Property(name="syswb101_Function28", type=syswb101_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb101_Function26", type=syswb101_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property29: BinaryAssociation = BinaryAssociation(
    name="property29",
    ends={
        Property(name="syswb101_FunctionProperty31", type=syswb101_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb101_Function30", type=syswb101_FunctionProperty, multiplicity=Multiplicity(0, 9999))
    }
)
functionalArchitecture38: BinaryAssociation = BinaryAssociation(
    name="functionalArchitecture38",
    ends={
        Property(name="syswb101_Function40", type=syswb101_System, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb101_System39", type=syswb101_Function, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
physicalArchitecture41: BinaryAssociation = BinaryAssociation(
    name="physicalArchitecture41",
    ends={
        Property(name="syswb101_Component43", type=syswb101_System, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb101_System42", type=syswb101_Component, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
patterns44: BinaryAssociation = BinaryAssociation(
    name="patterns44",
    ends={
        Property(name="syswb101_Function46", type=syswb101_PatternCatalog, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb101_PatternCatalog45", type=syswb101_Function, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_syswb101_Thing_NamedElement = Generalization(general=NamedElement, specific=syswb101_Thing)
gen_syswb101_Workbench_Named = Generalization(general=Named, specific=syswb101_Workbench)
gen_syswb101_Thoughts_NamedElement = Generalization(general=NamedElement, specific=syswb101_Thoughts)
gen_syswb101_FunctionProperty_Named = Generalization(general=Named, specific=syswb101_FunctionProperty)
gen_syswb101_RelatedTo_NamedElement = Generalization(general=NamedElement, specific=syswb101_RelatedTo)
gen_syswb101_Component_Named = Generalization(general=Named, specific=syswb101_Component)
gen_syswb101_Function_Named = Generalization(general=Named, specific=syswb101_Function)
gen_syswb101_System_Named = Generalization(general=Named, specific=syswb101_System)

# Domain Model
domain_model = DomainModel(
    name="syswb101",
    types={syswb101_Thoughts, syswb101_System, syswb101_FunctionProperty, syswb101_PatternCatalog, NamedElement, syswb101_Workbench, Named, syswb101_Thing, syswb101_Component, syswb101_RelatedTo, syswb101_NamedElement, syswb101_Named, syswb101_Function},
    associations={thoughts1, systemView3, functionProperties5, catalog7, things0, fromThing10, toThing11, relatedTo13, relations9, parent17, associations33, allocatedTo35, decompositions20, associations22, performs24, decompositions27, property29, functionalArchitecture38, physicalArchitecture41, patterns44},
    generalizations={gen_syswb101_Thing_NamedElement, gen_syswb101_Workbench_Named, gen_syswb101_Thoughts_NamedElement, gen_syswb101_FunctionProperty_Named, gen_syswb101_RelatedTo_NamedElement, gen_syswb101_Component_Named, gen_syswb101_Function_Named, gen_syswb101_System_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)