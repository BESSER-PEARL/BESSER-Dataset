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
relationworld_ThingA = Class(name="relationworld_ThingA")
SourceNode = Class(name="SourceNode")
NamedElement = Class(name="NamedElement")
relationworld_ThingB = Class(name="relationworld_ThingB")
TargetNode = Class(name="TargetNode")
relationworld_RelatedTo = Class(name="relationworld_RelatedTo")
Arrow = Class(name="Arrow")
relationworld_SourceNode = Class(name="relationworld_SourceNode", is_abstract=True)
relationworld_Arrow = Class(name="relationworld_Arrow", is_abstract=True)
relationworld_TargetNode = Class(name="relationworld_TargetNode", is_abstract=True)
relationworld_Category = Class(name="relationworld_Category", is_abstract=True)
relationworld_World = Class(name="relationworld_World")
Category = Class(name="Category")
relationworld_NamedElement = Class(name="relationworld_NamedElement", is_abstract=True)

# relationworld_ThingA class attributes and methods
relationworld_ThingA_since: Property = Property(name="since", type=DateType)
relationworld_ThingA_m_compare: Method = Method(name="compare", parameters={Parameter(name='relationworld_personne', type=StringType)}, type=IntegerType)
relationworld_ThingA_m_pred: Method = Method(name="pred", parameters={}, type=StringType)
relationworld_ThingA_m_succ: Method = Method(name="succ", parameters={}, type=StringType)
relationworld_ThingA.attributes={relationworld_ThingA_since}
relationworld_ThingA.methods={relationworld_ThingA_m_succ, relationworld_ThingA_m_compare, relationworld_ThingA_m_pred}

# SourceNode class attributes and methods

# NamedElement class attributes and methods

# relationworld_ThingB class attributes and methods
relationworld_ThingB_step: Property = Property(name="step", type=StringType)
relationworld_ThingB_m_compare: Method = Method(name="compare", parameters={Parameter(name='relationworld_role', type=StringType)}, type=IntegerType)
relationworld_ThingB_m_pred: Method = Method(name="pred", parameters={}, type=StringType)
relationworld_ThingB_m_succ: Method = Method(name="succ", parameters={}, type=StringType)
relationworld_ThingB.attributes={relationworld_ThingB_step}
relationworld_ThingB.methods={relationworld_ThingB_m_compare, relationworld_ThingB_m_pred, relationworld_ThingB_m_succ}

# TargetNode class attributes and methods

# relationworld_RelatedTo class attributes and methods
relationworld_RelatedTo_m_validate: Method = Method(name="validate", parameters={}, type=BooleanType)
relationworld_RelatedTo.methods={relationworld_RelatedTo_m_validate}

# Arrow class attributes and methods

# relationworld_SourceNode class attributes and methods
relationworld_SourceNode_m_compare: Method = Method(name="compare", parameters={Parameter(name='relationworld_noeud', type=StringType)}, type=IntegerType)
relationworld_SourceNode_m_pred: Method = Method(name="pred", parameters={}, type=SourceNode)
relationworld_SourceNode_m_succ: Method = Method(name="succ", parameters={}, type=SourceNode)
relationworld_SourceNode.methods={relationworld_SourceNode_m_pred, relationworld_SourceNode_m_succ, relationworld_SourceNode_m_compare}

# relationworld_Arrow class attributes and methods
relationworld_Arrow_m_validate: Method = Method(name="validate", parameters={}, type=BooleanType)
relationworld_Arrow.methods={relationworld_Arrow_m_validate}

# relationworld_TargetNode class attributes and methods
relationworld_TargetNode_m_compare: Method = Method(name="compare", parameters={Parameter(name='relationworld_noeud', type=StringType)}, type=IntegerType)
relationworld_TargetNode_m_pred: Method = Method(name="pred", parameters={}, type=TargetNode)
relationworld_TargetNode_m_succ: Method = Method(name="succ", parameters={}, type=TargetNode)
relationworld_TargetNode.methods={relationworld_TargetNode_m_pred, relationworld_TargetNode_m_compare, relationworld_TargetNode_m_succ}

# relationworld_Category class attributes and methods
relationworld_Category_nom: Property = Property(name="nom", type=StringType)
relationworld_Category_m_compare: Method = Method(name="compare", parameters={Parameter(name='relationworld_n1', type=StringType), Parameter(name='relationworld_n2', type=StringType)}, type=IntegerType)
relationworld_Category_m_compare: Method = Method(name="compare", parameters={Parameter(name='relationworld_n2', type=StringType), Parameter(name='relationworld_n1', type=StringType)}, type=IntegerType)
relationworld_Category_m_affectation: Method = Method(name="affectation", parameters={Parameter(name='relationworld_cible', type=StringType), Parameter(name='relationworld_source', type=StringType)}, type=Arrow)
relationworld_Category.attributes={relationworld_Category_nom}
relationworld_Category.methods={relationworld_Category_m_compare, relationworld_Category_m_affectation, relationworld_Category_m_compare}

# relationworld_World class attributes and methods
relationworld_World_m_compare: Method = Method(name="compare", parameters={Parameter(name='relationworld_role1', type=StringType), Parameter(name='relationworld_role2', type=StringType)}, type=IntegerType)
relationworld_World_m_compare: Method = Method(name="compare", parameters={Parameter(name='relationworld_personne2', type=StringType), Parameter(name='relationworld_personne1', type=StringType)}, type=IntegerType)
relationworld_World_m_affectation: Method = Method(name="affectation", parameters={Parameter(name='relationworld_role', type=StringType), Parameter(name='relationworld_personne', type=StringType)}, type=StringType)
relationworld_World.methods={relationworld_World_m_compare, relationworld_World_m_compare, relationworld_World_m_affectation}

# Category class attributes and methods

# relationworld_NamedElement class attributes and methods
relationworld_NamedElement_name: Property = Property(name="name", type=StringType)
relationworld_NamedElement.attributes={relationworld_NamedElement_name}

# Relationships
relations8: BinaryAssociation = BinaryAssociation(
    name="relations8",
    ends={
        Property(name="relationworld_RelatedTo10", type=relationworld_World, multiplicity=Multiplicity(1, 1)),
        Property(name="relationworld_World9", type=relationworld_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
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

# Generalizations
gen_relationworld_ThingA_SourceNode = Generalization(general=SourceNode, specific=relationworld_ThingA)
gen_relationworld_ThingA_NamedElement = Generalization(general=NamedElement, specific=relationworld_ThingA)
gen_relationworld_ThingB_TargetNode = Generalization(general=TargetNode, specific=relationworld_ThingB)
gen_relationworld_ThingB_NamedElement = Generalization(general=NamedElement, specific=relationworld_ThingB)
gen_relationworld_RelatedTo_Arrow = Generalization(general=Arrow, specific=relationworld_RelatedTo)
gen_relationworld_RelatedTo_NamedElement = Generalization(general=NamedElement, specific=relationworld_RelatedTo)
gen_relationworld_World_Category = Generalization(general=Category, specific=relationworld_World)

# Domain Model
domain_model = DomainModel(
    name="relationworld",
    types={relationworld_ThingA, SourceNode, NamedElement, relationworld_ThingB, TargetNode, relationworld_RelatedTo, Arrow, relationworld_SourceNode, relationworld_Arrow, relationworld_TargetNode, relationworld_Category, relationworld_World, Category, relationworld_NamedElement, Scale},
    associations={relations8, source11, cible12, sources14, thingA0, thingB1, thingsa3, thingsb5, fleches16, targets19},
    generalizations={gen_relationworld_ThingA_SourceNode, gen_relationworld_ThingA_NamedElement, gen_relationworld_ThingB_TargetNode, gen_relationworld_ThingB_NamedElement, gen_relationworld_RelatedTo_Arrow, gen_relationworld_RelatedTo_NamedElement, gen_relationworld_World_Category},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)