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
Module = Class(name="Module")
ea_automata_State = Class(name="ea::automata::State")
Automaton = Class(name="Automaton")
ea_automata_Automaton = Class(name="ea::automata::Automaton")
ExtendibleElement = Class(name="ExtendibleElement")
State = Class(name="State")
Transition = Class(name="Transition")
ea_automata_Module = Class(name="ea::automata::Module")
ea_extensions_IExtendible = Class(name="ea::extensions::IExtendible", is_abstract=True)
IExtension = Class(name="IExtension")
ea_automata_Transition = Class(name="ea::automata::Transition")
ea_extensions_StringListExtension = Class(name="ea::extensions::StringListExtension")
ea_extensions_BooleanExtension = Class(name="ea::extensions::BooleanExtension")
ea_extensions_IExtension = Class(name="ea::extensions::IExtension", is_abstract=True)
IExtendible = Class(name="IExtendible")
ea_extensions_ExtendibleElement = Class(name="ea::extensions::ExtendibleElement", is_abstract=True)
ea_extensions_ExtensionElement = Class(name="ea::extensions::ExtensionElement", is_abstract=True)
ea_extensions_IntegerExtension = Class(name="ea::extensions::IntegerExtension")
ExtensionElement = Class(name="ExtensionElement")
ea_extensions_StringExtension = Class(name="ea::extensions::StringExtension")

# Module class attributes and methods

# ea_automata_State class attributes and methods
ea_automata_State_id: Property = Property(name="id", type=StringType)
ea_automata_State_name: Property = Property(name="name", type=StringType)
ea_automata_State.attributes={ea_automata_State_name, ea_automata_State_id}

# Automaton class attributes and methods

# ea_automata_Automaton class attributes and methods
ea_automata_Automaton_id: Property = Property(name="id", type=StringType)
ea_automata_Automaton_name: Property = Property(name="name", type=StringType)
ea_automata_Automaton_usedExtensionIds: Property = Property(name="usedExtensionIds", type=StringType)
ea_automata_Automaton.attributes={ea_automata_Automaton_name, ea_automata_Automaton_id, ea_automata_Automaton_usedExtensionIds}

# ExtendibleElement class attributes and methods

# State class attributes and methods

# Transition class attributes and methods

# ea_automata_Module class attributes and methods

# ea_extensions_IExtendible class attributes and methods
ea_extensions_IExtendible_m_findExtension: Method = Method(name="findExtension", parameters={Parameter(name='id')}, type=StringType)
ea_extensions_IExtendible_m_updateExtension: Method = Method(name="updateExtension", parameters={Parameter(name='extension')})
ea_extensions_IExtendible.methods={ea_extensions_IExtendible_m_findExtension, ea_extensions_IExtendible_m_updateExtension}

# IExtension class attributes and methods

# ea_automata_Transition class attributes and methods
ea_automata_Transition_id: Property = Property(name="id", type=StringType)
ea_automata_Transition.attributes={ea_automata_Transition_id}

# ea_extensions_StringListExtension class attributes and methods
ea_extensions_StringListExtension_values: Property = Property(name="values", type=StringType)
ea_extensions_StringListExtension.attributes={ea_extensions_StringListExtension_values}

# ea_extensions_BooleanExtension class attributes and methods
ea_extensions_BooleanExtension_value: Property = Property(name="value", type=BooleanType)
ea_extensions_BooleanExtension.attributes={ea_extensions_BooleanExtension_value}

# ea_extensions_IExtension class attributes and methods
ea_extensions_IExtension_id: Property = Property(name="id", type=StringType)
ea_extensions_IExtension.attributes={ea_extensions_IExtension_id}

# IExtendible class attributes and methods

# ea_extensions_ExtendibleElement class attributes and methods

# ea_extensions_ExtensionElement class attributes and methods

# ea_extensions_IntegerExtension class attributes and methods
ea_extensions_IntegerExtension_value: Property = Property(name="value", type=IntegerType)
ea_extensions_IntegerExtension.attributes={ea_extensions_IntegerExtension_value}

# ExtensionElement class attributes and methods

# ea_extensions_StringExtension class attributes and methods
ea_extensions_StringExtension_value: Property = Property(name="value", type=StringType)
ea_extensions_StringExtension.attributes={ea_extensions_StringExtension_value}

# Relationships
module3: BinaryAssociation = BinaryAssociation(
    name="module3",
    ends={
        Property(name="automata4", type=ea_automata_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="Module", type=Module, multiplicity=Multiplicity(0, 1))
    }
)
automaton5: BinaryAssociation = BinaryAssociation(
    name="automaton5",
    ends={
        Property(name="automata6", type=ea_automata_State, multiplicity=Multiplicity(1, 1)),
        Property(name="Automaton", type=Automaton, multiplicity=Multiplicity(0, 1))
    }
)
incoming7: BinaryAssociation = BinaryAssociation(
    name="incoming7",
    ends={
        Property(name="automata9", type=ea_automata_State, multiplicity=Multiplicity(1, 1)),
        Property(name="Transition8", type=Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing10: BinaryAssociation = BinaryAssociation(
    name="outgoing10",
    ends={
        Property(name="automata12", type=ea_automata_State, multiplicity=Multiplicity(1, 1)),
        Property(name="Transition11", type=Transition, multiplicity=Multiplicity(0, 9999))
    }
)
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="automata", type=ea_automata_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="State", type=State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="automata2", type=ea_automata_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="Transition", type=Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
automata22: BinaryAssociation = BinaryAssociation(
    name="automata22",
    ends={
        Property(name="automata24", type=ea_automata_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="Automaton23", type=Automaton, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensions25: BinaryAssociation = BinaryAssociation(
    name="extensions25",
    ends={
        Property(name="extensions", type=ea_extensions_IExtendible, multiplicity=Multiplicity(1, 1)),
        Property(name="IExtension", type=IExtension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
automaton13: BinaryAssociation = BinaryAssociation(
    name="automaton13",
    ends={
        Property(name="automata15", type=ea_automata_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="Automaton14", type=Automaton, multiplicity=Multiplicity(0, 1))
    }
)
source16: BinaryAssociation = BinaryAssociation(
    name="source16",
    ends={
        Property(name="automata18", type=ea_automata_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="State17", type=State, multiplicity=Multiplicity(0, 1))
    }
)
target19: BinaryAssociation = BinaryAssociation(
    name="target19",
    ends={
        Property(name="automata21", type=ea_automata_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="State20", type=State, multiplicity=Multiplicity(0, 1))
    }
)
owner26: BinaryAssociation = BinaryAssociation(
    name="owner26",
    ends={
        Property(name="extensions27", type=ea_extensions_IExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="IExtendible", type=IExtendible, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_ea_automata_State_ExtendibleElement = Generalization(general=ExtendibleElement, specific=ea_automata_State)
gen_ea_automata_Automaton_ExtendibleElement = Generalization(general=ExtendibleElement, specific=ea_automata_Automaton)
gen_ea_automata_Transition_ExtendibleElement = Generalization(general=ExtendibleElement, specific=ea_automata_Transition)
gen_ea_extensions_StringExtension_ExtensionElement = Generalization(general=ExtensionElement, specific=ea_extensions_StringExtension)
gen_ea_extensions_StringListExtension_ExtensionElement = Generalization(general=ExtensionElement, specific=ea_extensions_StringListExtension)
gen_ea_extensions_BooleanExtension_ExtensionElement = Generalization(general=ExtensionElement, specific=ea_extensions_BooleanExtension)
gen_ea_extensions_ExtendibleElement_IExtendible = Generalization(general=IExtendible, specific=ea_extensions_ExtendibleElement)
gen_ea_extensions_ExtensionElement_IExtension = Generalization(general=IExtension, specific=ea_extensions_ExtensionElement)
gen_ea_extensions_IntegerExtension_ExtensionElement = Generalization(general=ExtensionElement, specific=ea_extensions_IntegerExtension)

# Domain Model
domain_model = DomainModel(
    name="ea",
    types={Module, ea_automata_State, Automaton, ea_automata_Automaton, ExtendibleElement, State, Transition, ea_automata_Module, ea_extensions_IExtendible, IExtension, ea_automata_Transition, ea_extensions_StringListExtension, ea_extensions_BooleanExtension, ea_extensions_IExtension, IExtendible, ea_extensions_ExtendibleElement, ea_extensions_ExtensionElement, ea_extensions_IntegerExtension, ExtensionElement, ea_extensions_StringExtension},
    associations={module3, automaton5, incoming7, outgoing10, states0, transitions1, automata22, extensions25, automaton13, source16, target19, owner26},
    generalizations={gen_ea_automata_State_ExtendibleElement, gen_ea_automata_Automaton_ExtendibleElement, gen_ea_automata_Transition_ExtendibleElement, gen_ea_extensions_StringExtension_ExtensionElement, gen_ea_extensions_StringListExtension_ExtensionElement, gen_ea_extensions_BooleanExtension_ExtensionElement, gen_ea_extensions_ExtendibleElement_IExtendible, gen_ea_extensions_ExtensionElement_IExtension, gen_ea_extensions_IntegerExtension_ExtensionElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)