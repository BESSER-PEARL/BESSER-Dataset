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

# Enumerations
Scale: Enumeration = Enumeration(
    name="Scale",
    literals={
            EnumerationLiteral(name="nothing"),
			EnumerationLiteral(name="one"),
			EnumerationLiteral(name="two"),
			EnumerationLiteral(name="three"),
			EnumerationLiteral(name="four")
    }
)

# Classes
relationworld_ThingB = Class(name="relationworld::ThingB")
TargetNode = Class(name="TargetNode")
relationworld_RelatedTo = Class(name="relationworld::RelatedTo")
Arrow = Class(name="Arrow")
relationworld_ThingA = Class(name="relationworld::ThingA")
SourceNode = Class(name="SourceNode")
NamedElement = Class(name="NamedElement")
relationworld_SourceNode = Class(name="relationworld::SourceNode", is_abstract=True)
relationworld_Arrow = Class(name="relationworld::Arrow", is_abstract=True)
relationworld_World = Class(name="relationworld::World")
Category = Class(name="Category")
relationworld_TargetNode = Class(name="relationworld::TargetNode", is_abstract=True)
relationworld_Category = Class(name="relationworld::Category", is_abstract=True)
relationworld_NamedElement = Class(name="relationworld::NamedElement")

# relationworld_ThingB class attributes and methods
relationworld_ThingB_step: Property = Property(name="step", type=StringType)
relationworld_ThingB_m_compare: Method = Method(name="compare", parameters={Parameter(name='role')}, type=IntegerType)
relationworld_ThingB_m_pred: Method = Method(name="pred", parameters={}, type=StringType)
relationworld_ThingB_m_succ: Method = Method(name="succ", parameters={}, type=StringType)
relationworld_ThingB.attributes={relationworld_ThingB_step}
relationworld_ThingB.methods={relationworld_ThingB_m_pred, relationworld_ThingB_m_compare, relationworld_ThingB_m_succ}

# TargetNode class attributes and methods

# relationworld_RelatedTo class attributes and methods
relationworld_RelatedTo_m_validate: Method = Method(name="validate", parameters={}, type=BooleanType)
relationworld_RelatedTo.methods={relationworld_RelatedTo_m_validate}

# Arrow class attributes and methods

# relationworld_ThingA class attributes and methods
relationworld_ThingA_since: Property = Property(name="since", type=DateType)
relationworld_ThingA_m_compare: Method = Method(name="compare", parameters={Parameter(name='personne')}, type=IntegerType)
relationworld_ThingA_m_pred: Method = Method(name="pred", parameters={}, type=StringType)
relationworld_ThingA_m_succ: Method = Method(name="succ", parameters={}, type=StringType)
relationworld_ThingA.attributes={relationworld_ThingA_since}
relationworld_ThingA.methods={relationworld_ThingA_m_succ, relationworld_ThingA_m_pred, relationworld_ThingA_m_compare}

# SourceNode class attributes and methods

# NamedElement class attributes and methods

# relationworld_SourceNode class attributes and methods
relationworld_SourceNode_m_compare: Method = Method(name="compare", parameters={Parameter(name='noeud')}, type=IntegerType)
relationworld_SourceNode_m_pred: Method = Method(name="pred", parameters={}, type=SourceNode)
relationworld_SourceNode_m_succ: Method = Method(name="succ", parameters={}, type=SourceNode)
relationworld_SourceNode.methods={relationworld_SourceNode_m_succ, relationworld_SourceNode_m_compare, relationworld_SourceNode_m_pred}

# relationworld_Arrow class attributes and methods
relationworld_Arrow_m_validate: Method = Method(name="validate", parameters={}, type=BooleanType)
relationworld_Arrow.methods={relationworld_Arrow_m_validate}

# relationworld_World class attributes and methods
relationworld_World_m_compare: Method = Method(name="compare", parameters={Parameter(name='role2'), Parameter(name='role1')}, type=IntegerType)
relationworld_World_m_compare: Method = Method(name="compare", parameters={Parameter(name='personne2'), Parameter(name='personne1')}, type=IntegerType)
relationworld_World_m_affectation: Method = Method(name="affectation", parameters={Parameter(name='personne'), Parameter(name='role')}, type=StringType)
relationworld_World.methods={relationworld_World_m_affectation, relationworld_World_m_compare, relationworld_World_m_compare}

# Category class attributes and methods

# relationworld_TargetNode class attributes and methods
relationworld_TargetNode_m_compare: Method = Method(name="compare", parameters={Parameter(name='noeud')}, type=IntegerType)
relationworld_TargetNode_m_pred: Method = Method(name="pred", parameters={}, type=TargetNode)
relationworld_TargetNode_m_succ: Method = Method(name="succ", parameters={}, type=TargetNode)
relationworld_TargetNode.methods={relationworld_TargetNode_m_pred, relationworld_TargetNode_m_compare, relationworld_TargetNode_m_succ}

# relationworld_Category class attributes and methods
relationworld_Category_nom: Property = Property(name="nom", type=StringType)
relationworld_Category_m_compare: Method = Method(name="compare", parameters={Parameter(name='n1'), Parameter(name='n2')}, type=IntegerType)
relationworld_Category_m_compare: Method = Method(name="compare", parameters={Parameter(name='n2'), Parameter(name='n1')}, type=IntegerType)
relationworld_Category_m_affectation: Method = Method(name="affectation", parameters={Parameter(name='source'), Parameter(name='cible')}, type=Arrow)
relationworld_Category.attributes={relationworld_Category_nom}
relationworld_Category.methods={relationworld_Category_m_compare, relationworld_Category_m_compare, relationworld_Category_m_affectation}

# relationworld_NamedElement class attributes and methods
relationworld_NamedElement_name: Property = Property(name="name", type=StringType)
relationworld_NamedElement.attributes={relationworld_NamedElement_name}

# Relationships
thingsa3: BinaryAssociation = BinaryAssociation(
    name="thingsa3",
    ends={
        Property(name="relationworld_ThingA4", type=relationworld_World, multiplicity=Multiplicity(1, 1)),
        Property(name="relationworld_World", type=relationworld_ThingA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thingsb5: BinaryAssociation = BinaryAssociation(
    name="thingsb5",
    ends={
        Property(name="relationworld_ThingB7", type=relationworld_World, multiplicity=Multiplicity(1, 1)),
        Property(name="relationworld_World6", type=relationworld_ThingB, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations8: BinaryAssociation = BinaryAssociation(
    name="relations8",
    ends={
        Property(name="relationworld_RelatedTo10", type=relationworld_World, multiplicity=Multiplicity(1, 1)),
        Property(name="relationworld_World9", type=relationworld_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thingA0: BinaryAssociation = BinaryAssociation(
    name="thingA0",
    ends={
        Property(name="relationworld_ThingA", type=relationworld_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="relationworld_RelatedTo", type=relationworld_ThingA, multiplicity=Multiplicity(0, 1))
    }
)
thingB1: BinaryAssociation = BinaryAssociation(
    name="thingB1",
    ends={
        Property(name="relationworld_ThingB", type=relationworld_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="relationworld_RelatedTo2", type=relationworld_ThingB, multiplicity=Multiplicity(0, 1))
    }
)
fleches16: BinaryAssociation = BinaryAssociation(
    name="fleches16",
    ends={
        Property(name="relationworld_Arrow18", type=relationworld_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="relationworld_Category17", type=relationworld_Arrow, multiplicity=Multiplicity(0, 9999))
    }
)
targets19: BinaryAssociation = BinaryAssociation(
    name="targets19",
    ends={
        Property(name="relationworld_TargetNode21", type=relationworld_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="relationworld_Category20", type=relationworld_TargetNode, multiplicity=Multiplicity(0, 9999))
    }
)
source11: BinaryAssociation = BinaryAssociation(
    name="source11",
    ends={
        Property(name="relationworld_SourceNode", type=relationworld_Arrow, multiplicity=Multiplicity(1, 1)),
        Property(name="relationworld_Arrow", type=relationworld_SourceNode, multiplicity=Multiplicity(0, 1))
    }
)
cible12: BinaryAssociation = BinaryAssociation(
    name="cible12",
    ends={
        Property(name="relationworld_TargetNode", type=relationworld_Arrow, multiplicity=Multiplicity(1, 1)),
        Property(name="relationworld_Arrow13", type=relationworld_TargetNode, multiplicity=Multiplicity(0, 1))
    }
)
sources14: BinaryAssociation = BinaryAssociation(
    name="sources14",
    ends={
        Property(name="relationworld_SourceNode15", type=relationworld_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="relationworld_Category", type=relationworld_SourceNode, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_relationworld_ThingB_TargetNode = Generalization(general=TargetNode, specific=relationworld_ThingB)
gen_relationworld_ThingB_NamedElement = Generalization(general=NamedElement, specific=relationworld_ThingB)
gen_relationworld_RelatedTo_Arrow = Generalization(general=Arrow, specific=relationworld_RelatedTo)
gen_relationworld_RelatedTo_NamedElement = Generalization(general=NamedElement, specific=relationworld_RelatedTo)
gen_relationworld_ThingA_SourceNode = Generalization(general=SourceNode, specific=relationworld_ThingA)
gen_relationworld_ThingA_NamedElement = Generalization(general=NamedElement, specific=relationworld_ThingA)
gen_relationworld_World_Category = Generalization(general=Category, specific=relationworld_World)

# Domain Model
domain_model = DomainModel(
    name="relationworld",
    types={relationworld_ThingB, TargetNode, relationworld_RelatedTo, Arrow, relationworld_ThingA, SourceNode, NamedElement, relationworld_SourceNode, relationworld_Arrow, relationworld_World, Category, relationworld_TargetNode, relationworld_Category, relationworld_NamedElement, Scale},
    associations={thingsa3, thingsb5, relations8, thingA0, thingB1, fleches16, targets19, source11, cible12, sources14},
    generalizations={gen_relationworld_ThingB_TargetNode, gen_relationworld_ThingB_NamedElement, gen_relationworld_RelatedTo_Arrow, gen_relationworld_RelatedTo_NamedElement, gen_relationworld_ThingA_SourceNode, gen_relationworld_ThingA_NamedElement, gen_relationworld_World_Category},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)