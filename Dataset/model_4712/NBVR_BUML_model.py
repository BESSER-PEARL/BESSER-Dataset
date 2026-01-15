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
FormElementKind: Enumeration = Enumeration(
    name="FormElementKind",
    literals={
            EnumerationLiteral(name="SubjectRole"),
			EnumerationLiteral(name="ObjectRole"),
			EnumerationLiteral(name="ParticleRole"),
			EnumerationLiteral(name="ParticleElement"),
			EnumerationLiteral(name="ItemElement")
    }
)

KeywordKind: Enumeration = Enumeration(
    name="KeywordKind",
    literals={
            EnumerationLiteral(name="K_Than"),
			EnumerationLiteral(name="K_Exactly"),
			EnumerationLiteral(name="K_Many"),
			EnumerationLiteral(name="K_Not"),
			EnumerationLiteral(name="K_And"),
			EnumerationLiteral(name="K_Or"),
			EnumerationLiteral(name="K_If"),
			EnumerationLiteral(name="K_Then"),
			EnumerationLiteral(name="K_Else"),
			EnumerationLiteral(name="K_Only"),
			EnumerationLiteral(name="K_Unless"),
			EnumerationLiteral(name="K_Same"),
			EnumerationLiteral(name="K_Different"),
			EnumerationLiteral(name="K_Other"),
			EnumerationLiteral(name="K_Another"),
			EnumerationLiteral(name="K_Must"),
			EnumerationLiteral(name="K_May"),
			EnumerationLiteral(name="K_Always"),
			EnumerationLiteral(name="K_That"),
			EnumerationLiteral(name="K_Whose"),
			EnumerationLiteral(name="Anaphor"),
			EnumerationLiteral(name="Pronoun"),
			EnumerationLiteral(name="Genitive"),
			EnumerationLiteral(name="K_Self"),
			EnumerationLiteral(name="Adjunct"),
			EnumerationLiteral(name="K_An"),
			EnumerationLiteral(name="K_The"),
			EnumerationLiteral(name="K_All"),
			EnumerationLiteral(name="K_None"),
			EnumerationLiteral(name="K_No"),
			EnumerationLiteral(name="K_Any"),
			EnumerationLiteral(name="K_One"),
			EnumerationLiteral(name="K_At"),
			EnumerationLiteral(name="K_Least"),
			EnumerationLiteral(name="K_Less"),
			EnumerationLiteral(name="K_Most"),
			EnumerationLiteral(name="K_More"),
			EnumerationLiteral(name="K_Everything"),
			EnumerationLiteral(name="K_Something"),
			EnumerationLiteral(name="K_Anything"),
			EnumerationLiteral(name="K_Nothing"),
			EnumerationLiteral(name="K_Whether"),
			EnumerationLiteral(name="K_What"),
			EnumerationLiteral(name="K_Which"),
			EnumerationLiteral(name="K_Where"),
			EnumerationLiteral(name="K_When"),
			EnumerationLiteral(name="K_Why"),
			EnumerationLiteral(name="K_How"),
			EnumerationLiteral(name="K_This"),
			EnumerationLiteral(name="K_Both"),
			EnumerationLiteral(name="K_Either"),
			EnumerationLiteral(name="K_Neither"),
			EnumerationLiteral(name="K_Nor"),
			EnumerationLiteral(name="K_Together"),
			EnumerationLiteral(name="K_But"),
			EnumerationLiteral(name="K_Instead"),
			EnumerationLiteral(name="K_There"),
			EnumerationLiteral(name="K_For"),
			EnumerationLiteral(name="K_As"),
			EnumerationLiteral(name="K_Of"),
			EnumerationLiteral(name="Function")
    }
)

VocItemKind: Enumeration = Enumeration(
    name="VocItemKind",
    literals={
            EnumerationLiteral(name="NounConcept"),
			EnumerationLiteral(name="VerbConcept"),
			EnumerationLiteral(name="AdjectiveConcept"),
			EnumerationLiteral(name="PropertyConcept"),
			EnumerationLiteral(name="ProperName")
    }
)

QuantifierKind: Enumeration = Enumeration(
    name="QuantifierKind",
    literals={
            EnumerationLiteral(name="Q_An"),
			EnumerationLiteral(name="Q_The"),
			EnumerationLiteral(name="Q_All"),
			EnumerationLiteral(name="Q_No"),
			EnumerationLiteral(name="Q_Any"),
			EnumerationLiteral(name="AtLeast1"),
			EnumerationLiteral(name="AtMost1"),
			EnumerationLiteral(name="Exactly1"),
			EnumerationLiteral(name="AtLeastN"),
			EnumerationLiteral(name="AtMostN"),
			EnumerationLiteral(name="ExactlyN"),
			EnumerationLiteral(name="LessThanN"),
			EnumerationLiteral(name="MoreThanN")
    }
)

PhraseType: Enumeration = Enumeration(
    name="PhraseType",
    literals={
            EnumerationLiteral(name="Instance"),
			EnumerationLiteral(name="Group"),
			EnumerationLiteral(name="Query"),
			EnumerationLiteral(name="TypeNoun"),
			EnumerationLiteral(name="Property"),
			EnumerationLiteral(name="RoleNoun"),
			EnumerationLiteral(name="Pronoun"),
			EnumerationLiteral(name="Anaphor"),
			EnumerationLiteral(name="Interrogative"),
			EnumerationLiteral(name="LocalName")
    }
)

InstanceKind: Enumeration = Enumeration(
    name="InstanceKind",
    literals={
            EnumerationLiteral(name="Name"),
			EnumerationLiteral(name="Number"),
			EnumerationLiteral(name="String"),
			EnumerationLiteral(name="Quantity"),
			EnumerationLiteral(name="Statement"),
			EnumerationLiteral(name="Question"),
			EnumerationLiteral(name="Query"),
			EnumerationLiteral(name="Concept")
    }
)

Connective: Enumeration = Enumeration(
    name="Connective",
    literals={
            EnumerationLiteral(name="And"),
			EnumerationLiteral(name="Or"),
			EnumerationLiteral(name="Nor"),
			EnumerationLiteral(name="Xor"),
			EnumerationLiteral(name="If"),
			EnumerationLiteral(name="Unless"),
			EnumerationLiteral(name="OnlyIf"),
			EnumerationLiteral(name="Eqv")
    }
)

Modality: Enumeration = Enumeration(
    name="Modality",
    literals={
            EnumerationLiteral(name="Permission"),
			EnumerationLiteral(name="PermittedNot"),
			EnumerationLiteral(name="Possibility"),
			EnumerationLiteral(name="Impossibility"),
			EnumerationLiteral(name="Preference"),
			EnumerationLiteral(name="Antipreference"),
			EnumerationLiteral(name="Nonpreference"),
			EnumerationLiteral(name="None"),
			EnumerationLiteral(name="Negation"),
			EnumerationLiteral(name="Obligation"),
			EnumerationLiteral(name="Prohibition")
    }
)

SentenceType: Enumeration = Enumeration(
    name="SentenceType",
    literals={
            EnumerationLiteral(name="Other"),
			EnumerationLiteral(name="Simple"),
			EnumerationLiteral(name="Compound"),
			EnumerationLiteral(name="Implication"),
			EnumerationLiteral(name="Equivalence"),
			EnumerationLiteral(name="Domain"),
			EnumerationLiteral(name="Modal")
    }
)

GroupKind: Enumeration = Enumeration(
    name="GroupKind",
    literals={
            EnumerationLiteral(name="Joint"),
			EnumerationLiteral(name="All"),
			EnumerationLiteral(name="Choice"),
			EnumerationLiteral(name="Neither"),
			EnumerationLiteral(name="Instead")
    }
)

QueryKind: Enumeration = Enumeration(
    name="QueryKind",
    literals={
            EnumerationLiteral(name="Any"),
			EnumerationLiteral(name="What"),
			EnumerationLiteral(name="Whether"),
			EnumerationLiteral(name="Why"),
			EnumerationLiteral(name="How"),
			EnumerationLiteral(name="Where"),
			EnumerationLiteral(name="When"),
			EnumerationLiteral(name="HowMany")
    }
)

ElementKind: Enumeration = Enumeration(
    name="ElementKind",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="Sentence"),
			EnumerationLiteral(name="Qualifier"),
			EnumerationLiteral(name="Quantifier"),
			EnumerationLiteral(name="Condition"),
			EnumerationLiteral(name="Modifier"),
			EnumerationLiteral(name="Noun"),
			EnumerationLiteral(name="Group"),
			EnumerationLiteral(name="Query"),
			EnumerationLiteral(name="Instance"),
			EnumerationLiteral(name="Property"),
			EnumerationLiteral(name="Pronoun"),
			EnumerationLiteral(name="Role")
    }
)

PropositionKind: Enumeration = Enumeration(
    name="PropositionKind",
    literals={
            EnumerationLiteral(name="Relation"),
			EnumerationLiteral(name="Connection"),
			EnumerationLiteral(name="Implication"),
			EnumerationLiteral(name="Negation"),
			EnumerationLiteral(name="Quantification"),
			EnumerationLiteral(name="Modal")
    }
)

# Classes
NBVR_Vocabulary_Adjective = Class(name="NBVR::Vocabulary::Adjective")
Word = Class(name="Word")
NBVR_Vocabulary_Word = Class(name="NBVR::Vocabulary::Word", is_abstract=True)
NBVR_Vocabulary_Term = Class(name="NBVR::Vocabulary::Term")
VocabularyItem = Class(name="VocabularyItem")
VerbRole = Class(name="VerbRole")
Particle = Class(name="Particle")
ItemElement = Class(name="ItemElement")
NBVR_Vocabulary_VocabularyItem = Class(name="NBVR::Vocabulary::VocabularyItem", is_abstract=True)
WordForm = Class(name="WordForm")
Term = Class(name="Term")
NBVR_Vocabulary_WordForm = Class(name="NBVR::Vocabulary::WordForm")
NBVR_Vocabulary_Formulation = Class(name="NBVR::Vocabulary::Formulation")
Formulation = Class(name="Formulation")
NBVR_Vocabulary_VocNoun = Class(name="NBVR::Vocabulary::VocNoun")
Predicate = Class(name="Predicate")
NBVR_Vocabulary_VocVerb = Class(name="NBVR::Vocabulary::VocVerb")
SyntaxForm = Class(name="SyntaxForm")
FormulationForm = Class(name="FormulationForm")
ParseElement = Class(name="ParseElement")
NBVR_Vocabulary_FormulationForm = Class(name="NBVR::Vocabulary::FormulationForm", is_abstract=True)
NBVR_Vocabulary_VerbRole = Class(name="NBVR::Vocabulary::VerbRole")
VocNoun = Class(name="VocNoun")
VocVerb = Class(name="VocVerb")
NBVR_Vocabulary_NumberWord = Class(name="NBVR::Vocabulary::NumberWord")
NBVR_Vocabulary_VocUnit = Class(name="NBVR::Vocabulary::VocUnit")
VocName = Class(name="VocName")
NBVR_Vocabulary_VocName = Class(name="NBVR::Vocabulary::VocName")
NBVR_Vocabulary_VocAdjective = Class(name="NBVR::Vocabulary::VocAdjective")
NBVR_Vocabulary_SyntaxForm = Class(name="NBVR::Vocabulary::SyntaxForm")
FormElement = Class(name="FormElement")
VocProperty = Class(name="VocProperty")
NBVR_Vocabulary_FormElement = Class(name="NBVR::Vocabulary::FormElement", is_abstract=True)
NBVR_Vocabulary_VocProperty = Class(name="NBVR::Vocabulary::VocProperty")
NBVR_Vocabulary_RoleElement = Class(name="NBVR::Vocabulary::RoleElement")
NBVR_Vocabulary_Keyword = Class(name="NBVR::Vocabulary::Keyword")
NBVR_Vocabulary_ItemElement = Class(name="NBVR::Vocabulary::ItemElement")
NBVR_Vocabulary_Particle = Class(name="NBVR::Vocabulary::Particle")
RoleElement = Class(name="RoleElement")
NBVR_Vocabulary_Dictionary = Class(name="NBVR::Vocabulary::Dictionary")
NBVR_Vocabulary_StringWord = Class(name="NBVR::Vocabulary::StringWord")
NBVR_Vocabulary_Adjunct = Class(name="NBVR::Vocabulary::Adjunct")
NBVR_Vocabulary_Noun = Class(name="NBVR::Vocabulary::Noun")
NBVR_Vocabulary_Name = Class(name="NBVR::Vocabulary::Name")
NBVR_Vocabulary_Verb = Class(name="NBVR::Vocabulary::Verb")
Variable = Class(name="Variable")
NBVR_Vocabulary_Definition = Class(name="NBVR::Vocabulary::Definition")
NBVR_Vocabulary_DateTime = Class(name="NBVR::Vocabulary::DateTime")
NBVR_Vocabulary_Terminology = Class(name="NBVR::Vocabulary::Terminology")
NBVR_Vocabulary_IsVerb = Class(name="NBVR::Vocabulary::IsVerb")
Verb = Class(name="Verb")
NBVR_Grammar_GroupPhrase = Class(name="NBVR::Grammar::GroupPhrase")
RolePhrase = Class(name="RolePhrase")
SimpleNounPhrase = Class(name="SimpleNounPhrase")
NBVR_Grammar_RolePhrase = Class(name="NBVR::Grammar::RolePhrase", is_abstract=True)
Vocabulary_FormulationForm = Class(name="Vocabulary::FormulationForm")
Grammar_ParseElement = Class(name="Grammar::ParseElement")
NBVR_Grammar_Qualifier = Class(name="NBVR::Grammar::Qualifier", is_abstract=True)
NBVR_Grammar_QualifierChain = Class(name="NBVR::Grammar::QualifierChain")
NBVR_Grammar_Sentence = Class(name="NBVR::Grammar::Sentence", is_abstract=True)
NBVR_Grammar_SimpleNounPhrase = Class(name="NBVR::Grammar::SimpleNounPhrase", is_abstract=True)
NBVR_Grammar_Condition = Class(name="NBVR::Grammar::Condition")
SimpleQualifier = Class(name="SimpleQualifier")
Sentence = Class(name="Sentence")
NBVR_Grammar_SimpleQualifier = Class(name="NBVR::Grammar::SimpleQualifier")
Qualifier = Class(name="Qualifier")
QualifierChain = Class(name="QualifierChain")
Condition = Class(name="Condition")
Quantity = Class(name="Quantity")
NBVR_Grammar_Quantity = Class(name="NBVR::Grammar::Quantity")
Instance = Class(name="Instance")
NumberWord = Class(name="NumberWord")
Dimension = Class(name="Dimension")
NBVR_Grammar_Instance = Class(name="NBVR::Grammar::Instance", is_abstract=True)
NBVR_Grammar_Dimension = Class(name="NBVR::Grammar::Dimension")
VocUnit = Class(name="VocUnit")
NBVR_Grammar_Modifier = Class(name="NBVR::Grammar::Modifier")
VocAdjective = Class(name="VocAdjective")
NBVR_Grammar_TypeNoun = Class(name="NBVR::Grammar::TypeNoun")
ModifiedTerm = Class(name="ModifiedTerm")
NBVR_Grammar_ModifiedTerm = Class(name="NBVR::Grammar::ModifiedTerm", is_abstract=True)
Quantifier = Class(name="Quantifier")
Modifier = Class(name="Modifier")
NBVR_Grammar_Quantifier = Class(name="NBVR::Grammar::Quantifier")
NBVR_Grammar_VerbPhrase = Class(name="NBVR::Grammar::VerbPhrase")
NBVR_Grammar_PartPhrase = Class(name="NBVR::Grammar::PartPhrase")
NBVR_Grammar_SimpleForm = Class(name="NBVR::Grammar::SimpleForm")
VerbPhrase = Class(name="VerbPhrase")
NBVR_Grammar_PropertyNoun = Class(name="NBVR::Grammar::PropertyNoun")
TypeNoun = Class(name="TypeNoun")
NBVR_Grammar_RoleNoun = Class(name="NBVR::Grammar::RoleNoun")
NBVR_Grammar_CompoundForm = Class(name="NBVR::Grammar::CompoundForm")
NBVR_Grammar_LexicalInstance = Class(name="NBVR::Grammar::LexicalInstance")
NBVR_Grammar_Nominalization = Class(name="NBVR::Grammar::Nominalization", is_abstract=True)
NBVR_Grammar_Statement = Class(name="NBVR::Grammar::Statement")
Nominalization = Class(name="Nominalization")
NBVR_Grammar_Question = Class(name="NBVR::Grammar::Question")
QueryPhrase = Class(name="QueryPhrase")
PartPhrase = Class(name="PartPhrase")
NBVR_Grammar_ImplicationForm = Class(name="NBVR::Grammar::ImplicationForm")
NBVR_Grammar_Pronoun = Class(name="NBVR::Grammar::Pronoun")
Keyword = Class(name="Keyword")
NBVR_Grammar_Intension = Class(name="NBVR::Grammar::Intension")
NBVR_Grammar_Parse = Class(name="NBVR::Grammar::Parse")
NBVR_Grammar_DomainForm = Class(name="NBVR::Grammar::DomainForm")
NBVR_Grammar_QueryPhrase = Class(name="NBVR::Grammar::QueryPhrase")
Question = Class(name="Question")
NBVR_Grammar_ProperName = Class(name="NBVR::Grammar::ProperName")
NBVR_Logic_Variable = Class(name="NBVR::Logic::Variable")
Quantification = Class(name="Quantification")
Proposition = Class(name="Proposition")
Relation = Class(name="Relation")
Set = Class(name="Set")
NBVR_Grammar_LocalName = Class(name="NBVR::Grammar::LocalName")
LocalName = Class(name="LocalName")
NBVR_Grammar_ParseElement = Class(name="NBVR::Grammar::ParseElement", is_abstract=True)
Argument = Class(name="Argument")
NBVR_Logic_Argument = Class(name="NBVR::Logic::Argument")
Constant = Class(name="Constant")
NBVR_Logic_Quantification = Class(name="NBVR::Logic::Quantification")
NBVR_Logic_Proposition = Class(name="NBVR::Logic::Proposition", is_abstract=True)
NBVR_Logic_Relation = Class(name="NBVR::Logic::Relation")
NBVR_Logic_ExtentConstant = Class(name="NBVR::Logic::ExtentConstant")
NBVR_Logic_Connection = Class(name="NBVR::Logic::Connection")
NBVR_Logic_Implication = Class(name="NBVR::Logic::Implication")
NBVR_Logic_Constant = Class(name="NBVR::Logic::Constant", is_abstract=True)
NBVR_Logic_Set = Class(name="NBVR::Logic::Set")
ExtentConstant = Class(name="ExtentConstant")
NBVR_Logic_NominalConstant = Class(name="NBVR::Logic::NominalConstant")
NBVR_Logic_QuantityValue = Class(name="NBVR::Logic::QuantityValue")
NBVR_Logic_Predicate = Class(name="NBVR::Logic::Predicate")
RoleVariable = Class(name="RoleVariable")
NBVR_Logic_Modal = Class(name="NBVR::Logic::Modal")
NBVR_Logic_Negation = Class(name="NBVR::Logic::Negation")
NBVR_Logic_RoleVariable = Class(name="NBVR::Logic::RoleVariable")
NBVR_Logic_ValueConstant = Class(name="NBVR::Logic::ValueConstant")

# NBVR_Vocabulary_Adjective class attributes and methods

# Word class attributes and methods

# NBVR_Vocabulary_Word class attributes and methods
NBVR_Vocabulary_Word_m_isArticle: Method = Method(name="isArticle", parameters={}, type=BooleanType)
NBVR_Vocabulary_Word_m_isNumber: Method = Method(name="isNumber", parameters={}, type=BooleanType)
NBVR_Vocabulary_Word_m_isText: Method = Method(name="isText", parameters={}, type=BooleanType)
NBVR_Vocabulary_Word_m_isKeyword: Method = Method(name="isKeyword", parameters={Parameter(name='kind')}, type=BooleanType)
NBVR_Vocabulary_Word_m_isKeyword: Method = Method(name="isKeyword", parameters={}, type=BooleanType)
NBVR_Vocabulary_Word_m_isIs: Method = Method(name="isIs", parameters={}, type=BooleanType)
NBVR_Vocabulary_Word.methods={NBVR_Vocabulary_Word_m_isKeyword, NBVR_Vocabulary_Word_m_isIs, NBVR_Vocabulary_Word_m_isText, NBVR_Vocabulary_Word_m_isNumber, NBVR_Vocabulary_Word_m_isKeyword, NBVR_Vocabulary_Word_m_isArticle}

# NBVR_Vocabulary_Term class attributes and methods
NBVR_Vocabulary_Term_text: Property = Property(name="text", type=StringType)
NBVR_Vocabulary_Term.attributes={NBVR_Vocabulary_Term_text}

# VocabularyItem class attributes and methods

# VerbRole class attributes and methods

# Particle class attributes and methods

# ItemElement class attributes and methods

# NBVR_Vocabulary_VocabularyItem class attributes and methods
NBVR_Vocabulary_VocabularyItem_m_isPrimitive: Method = Method(name="isPrimitive", parameters={}, type=BooleanType)
NBVR_Vocabulary_VocabularyItem_m_getKind: Method = Method(name="getKind", parameters={}, type=StringType)
NBVR_Vocabulary_VocabularyItem.methods={NBVR_Vocabulary_VocabularyItem_m_getKind, NBVR_Vocabulary_VocabularyItem_m_isPrimitive}

# WordForm class attributes and methods

# Term class attributes and methods

# NBVR_Vocabulary_WordForm class attributes and methods
NBVR_Vocabulary_WordForm_text: Property = Property(name="text", type=StringType)
NBVR_Vocabulary_WordForm.attributes={NBVR_Vocabulary_WordForm_text}

# NBVR_Vocabulary_Formulation class attributes and methods
NBVR_Vocabulary_Formulation_text: Property = Property(name="text", type=StringType)
NBVR_Vocabulary_Formulation_language: Property = Property(name="language", type=StringType)
NBVR_Vocabulary_Formulation_m_isStructured: Method = Method(name="isStructured", parameters={}, type=BooleanType)
NBVR_Vocabulary_Formulation_m_addElement: Method = Method(name="addElement", parameters={Parameter(name='elt')})
NBVR_Vocabulary_Formulation.attributes={NBVR_Vocabulary_Formulation_language, NBVR_Vocabulary_Formulation_text}
NBVR_Vocabulary_Formulation.methods={NBVR_Vocabulary_Formulation_m_isStructured, NBVR_Vocabulary_Formulation_m_addElement}

# Formulation class attributes and methods

# NBVR_Vocabulary_VocNoun class attributes and methods
NBVR_Vocabulary_VocNoun_massNoun: Property = Property(name="massNoun", type=BooleanType)
NBVR_Vocabulary_VocNoun.attributes={NBVR_Vocabulary_VocNoun_massNoun}

# Predicate class attributes and methods

# NBVR_Vocabulary_VocVerb class attributes and methods
NBVR_Vocabulary_VocVerb_arity: Property = Property(name="arity", type=IntegerType)
NBVR_Vocabulary_VocVerb.attributes={NBVR_Vocabulary_VocVerb_arity}

# SyntaxForm class attributes and methods

# FormulationForm class attributes and methods

# ParseElement class attributes and methods

# NBVR_Vocabulary_FormulationForm class attributes and methods
NBVR_Vocabulary_FormulationForm_m_isStructured: Method = Method(name="isStructured", parameters={}, type=BooleanType)
NBVR_Vocabulary_FormulationForm.methods={NBVR_Vocabulary_FormulationForm_m_isStructured}

# NBVR_Vocabulary_VerbRole class attributes and methods
NBVR_Vocabulary_VerbRole_isRange: Property = Property(name="isRange", type=BooleanType)
NBVR_Vocabulary_VerbRole.attributes={NBVR_Vocabulary_VerbRole_isRange}

# VocNoun class attributes and methods

# VocVerb class attributes and methods

# NBVR_Vocabulary_NumberWord class attributes and methods
NBVR_Vocabulary_NumberWord_value: Property = Property(name="value", type=IntegerType)
NBVR_Vocabulary_NumberWord_decimal: Property = Property(name="decimal", type=BooleanType)
NBVR_Vocabulary_NumberWord.attributes={NBVR_Vocabulary_NumberWord_value, NBVR_Vocabulary_NumberWord_decimal}

# NBVR_Vocabulary_VocUnit class attributes and methods

# VocName class attributes and methods

# NBVR_Vocabulary_VocName class attributes and methods
NBVR_Vocabulary_VocName_m_isUnit: Method = Method(name="isUnit", parameters={}, type=BooleanType)
NBVR_Vocabulary_VocName.methods={NBVR_Vocabulary_VocName_m_isUnit}

# NBVR_Vocabulary_VocAdjective class attributes and methods

# NBVR_Vocabulary_SyntaxForm class attributes and methods
NBVR_Vocabulary_SyntaxForm_isAuxForm: Property = Property(name="isAuxForm", type=BooleanType)
NBVR_Vocabulary_SyntaxForm_text: Property = Property(name="text", type=StringType)
NBVR_Vocabulary_SyntaxForm.attributes={NBVR_Vocabulary_SyntaxForm_isAuxForm, NBVR_Vocabulary_SyntaxForm_text}

# FormElement class attributes and methods

# VocProperty class attributes and methods

# NBVR_Vocabulary_FormElement class attributes and methods
NBVR_Vocabulary_FormElement_kind: Property = Property(name="kind", type=StringType)
NBVR_Vocabulary_FormElement.attributes={NBVR_Vocabulary_FormElement_kind}

# NBVR_Vocabulary_VocProperty class attributes and methods

# NBVR_Vocabulary_RoleElement class attributes and methods
NBVR_Vocabulary_RoleElement_slot: Property = Property(name="slot", type=IntegerType)
NBVR_Vocabulary_RoleElement.attributes={NBVR_Vocabulary_RoleElement_slot}

# NBVR_Vocabulary_Keyword class attributes and methods
NBVR_Vocabulary_Keyword_kind: Property = Property(name="kind", type=StringType)
NBVR_Vocabulary_Keyword.attributes={NBVR_Vocabulary_Keyword_kind}

# NBVR_Vocabulary_ItemElement class attributes and methods

# NBVR_Vocabulary_Particle class attributes and methods

# RoleElement class attributes and methods

# NBVR_Vocabulary_Dictionary class attributes and methods

# NBVR_Vocabulary_StringWord class attributes and methods

# NBVR_Vocabulary_Adjunct class attributes and methods

# NBVR_Vocabulary_Noun class attributes and methods

# NBVR_Vocabulary_Name class attributes and methods

# NBVR_Vocabulary_Verb class attributes and methods
NBVR_Vocabulary_Verb_m_isProgressive: Method = Method(name="isProgressive", parameters={Parameter(name='wf')}, type=BooleanType)
NBVR_Vocabulary_Verb_m_isPast: Method = Method(name="isPast", parameters={Parameter(name='wf')}, type=BooleanType)
NBVR_Vocabulary_Verb_m_isPerfective: Method = Method(name="isPerfective", parameters={Parameter(name='wf')}, type=BooleanType)
NBVR_Vocabulary_Verb.methods={NBVR_Vocabulary_Verb_m_isProgressive, NBVR_Vocabulary_Verb_m_isPast, NBVR_Vocabulary_Verb_m_isPerfective}

# Variable class attributes and methods

# NBVR_Vocabulary_Definition class attributes and methods

# NBVR_Vocabulary_DateTime class attributes and methods

# NBVR_Vocabulary_Terminology class attributes and methods

# NBVR_Vocabulary_IsVerb class attributes and methods

# Verb class attributes and methods

# NBVR_Grammar_GroupPhrase class attributes and methods
NBVR_Grammar_GroupPhrase_kind: Property = Property(name="kind", type=StringType)
NBVR_Grammar_GroupPhrase.attributes={NBVR_Grammar_GroupPhrase_kind}

# RolePhrase class attributes and methods

# SimpleNounPhrase class attributes and methods

# NBVR_Grammar_RolePhrase class attributes and methods
NBVR_Grammar_RolePhrase_m_getType: Method = Method(name="getType", parameters={}, type=StringType)
NBVR_Grammar_RolePhrase.methods={NBVR_Grammar_RolePhrase_m_getType}

# Vocabulary_FormulationForm class attributes and methods

# Grammar_ParseElement class attributes and methods

# NBVR_Grammar_Qualifier class attributes and methods
NBVR_Grammar_Qualifier_m_isSimple: Method = Method(name="isSimple", parameters={}, type=BooleanType)
NBVR_Grammar_Qualifier.methods={NBVR_Grammar_Qualifier_m_isSimple}

# NBVR_Grammar_QualifierChain class attributes and methods

# NBVR_Grammar_Sentence class attributes and methods
NBVR_Grammar_Sentence_m_getType: Method = Method(name="getType", parameters={}, type=StringType)
NBVR_Grammar_Sentence.methods={NBVR_Grammar_Sentence_m_getType}

# NBVR_Grammar_SimpleNounPhrase class attributes and methods

# NBVR_Grammar_Condition class attributes and methods
NBVR_Grammar_Condition_otherwise: Property = Property(name="otherwise", type=BooleanType)
NBVR_Grammar_Condition.attributes={NBVR_Grammar_Condition_otherwise}

# SimpleQualifier class attributes and methods

# Sentence class attributes and methods

# NBVR_Grammar_SimpleQualifier class attributes and methods

# Qualifier class attributes and methods

# QualifierChain class attributes and methods

# Condition class attributes and methods

# Quantity class attributes and methods

# NBVR_Grammar_Quantity class attributes and methods

# Instance class attributes and methods

# NumberWord class attributes and methods

# Dimension class attributes and methods

# NBVR_Grammar_Instance class attributes and methods
NBVR_Grammar_Instance_m_getKind: Method = Method(name="getKind", parameters={}, type=StringType)
NBVR_Grammar_Instance.methods={NBVR_Grammar_Instance_m_getKind}

# NBVR_Grammar_Dimension class attributes and methods
NBVR_Grammar_Dimension_exponent: Property = Property(name="exponent", type=IntegerType)
NBVR_Grammar_Dimension.attributes={NBVR_Grammar_Dimension_exponent}

# VocUnit class attributes and methods

# NBVR_Grammar_Modifier class attributes and methods
NBVR_Grammar_Modifier_kind: Property = Property(name="kind", type=StringType)
NBVR_Grammar_Modifier.attributes={NBVR_Grammar_Modifier_kind}

# VocAdjective class attributes and methods

# NBVR_Grammar_TypeNoun class attributes and methods

# ModifiedTerm class attributes and methods

# NBVR_Grammar_ModifiedTerm class attributes and methods

# Quantifier class attributes and methods

# Modifier class attributes and methods

# NBVR_Grammar_Quantifier class attributes and methods
NBVR_Grammar_Quantifier_count: Property = Property(name="count", type=IntegerType)
NBVR_Grammar_Quantifier_kind: Property = Property(name="kind", type=StringType)
NBVR_Grammar_Quantifier.attributes={NBVR_Grammar_Quantifier_count, NBVR_Grammar_Quantifier_kind}

# NBVR_Grammar_VerbPhrase class attributes and methods
NBVR_Grammar_VerbPhrase_modality: Property = Property(name="modality", type=StringType)
NBVR_Grammar_VerbPhrase_negated: Property = Property(name="negated", type=BooleanType)
NBVR_Grammar_VerbPhrase.attributes={NBVR_Grammar_VerbPhrase_negated, NBVR_Grammar_VerbPhrase_modality}

# NBVR_Grammar_PartPhrase class attributes and methods

# NBVR_Grammar_SimpleForm class attributes and methods
NBVR_Grammar_SimpleForm_m_getModality: Method = Method(name="getModality", parameters={}, type=StringType)
NBVR_Grammar_SimpleForm_m_isNegated: Method = Method(name="isNegated", parameters={}, type=BooleanType)
NBVR_Grammar_SimpleForm.methods={NBVR_Grammar_SimpleForm_m_getModality, NBVR_Grammar_SimpleForm_m_isNegated}

# VerbPhrase class attributes and methods

# NBVR_Grammar_PropertyNoun class attributes and methods

# TypeNoun class attributes and methods

# NBVR_Grammar_RoleNoun class attributes and methods

# NBVR_Grammar_CompoundForm class attributes and methods
NBVR_Grammar_CompoundForm_kind: Property = Property(name="kind", type=StringType)
NBVR_Grammar_CompoundForm.attributes={NBVR_Grammar_CompoundForm_kind}

# NBVR_Grammar_LexicalInstance class attributes and methods

# NBVR_Grammar_Nominalization class attributes and methods

# NBVR_Grammar_Statement class attributes and methods

# Nominalization class attributes and methods

# NBVR_Grammar_Question class attributes and methods
NBVR_Grammar_Question_query: Property = Property(name="query", type=StringType)
NBVR_Grammar_Question.attributes={NBVR_Grammar_Question_query}

# QueryPhrase class attributes and methods

# PartPhrase class attributes and methods

# NBVR_Grammar_ImplicationForm class attributes and methods
NBVR_Grammar_ImplicationForm_kind: Property = Property(name="kind", type=StringType)
NBVR_Grammar_ImplicationForm.attributes={NBVR_Grammar_ImplicationForm_kind}

# NBVR_Grammar_Pronoun class attributes and methods

# Keyword class attributes and methods

# NBVR_Grammar_Intension class attributes and methods

# NBVR_Grammar_Parse class attributes and methods

# NBVR_Grammar_DomainForm class attributes and methods
NBVR_Grammar_DomainForm_modality: Property = Property(name="modality", type=StringType)
NBVR_Grammar_DomainForm.attributes={NBVR_Grammar_DomainForm_modality}

# NBVR_Grammar_QueryPhrase class attributes and methods
NBVR_Grammar_QueryPhrase_query: Property = Property(name="query", type=StringType)
NBVR_Grammar_QueryPhrase.attributes={NBVR_Grammar_QueryPhrase_query}

# Question class attributes and methods

# NBVR_Grammar_ProperName class attributes and methods

# NBVR_Logic_Variable class attributes and methods
NBVR_Logic_Variable_name: Property = Property(name="name", type=StringType)
NBVR_Logic_Variable.attributes={NBVR_Logic_Variable_name}

# Quantification class attributes and methods

# Proposition class attributes and methods

# Relation class attributes and methods

# Set class attributes and methods

# NBVR_Grammar_LocalName class attributes and methods

# LocalName class attributes and methods

# NBVR_Grammar_ParseElement class attributes and methods
NBVR_Grammar_ParseElement_m_isRolePhrase: Method = Method(name="isRolePhrase", parameters={}, type=BooleanType)
NBVR_Grammar_ParseElement_m_getElementKind: Method = Method(name="getElementKind", parameters={}, type=StringType)
NBVR_Grammar_ParseElement_m_isSentence: Method = Method(name="isSentence", parameters={}, type=BooleanType)
NBVR_Grammar_ParseElement_m_isInstance: Method = Method(name="isInstance", parameters={}, type=BooleanType)
NBVR_Grammar_ParseElement.methods={NBVR_Grammar_ParseElement_m_isRolePhrase, NBVR_Grammar_ParseElement_m_isSentence, NBVR_Grammar_ParseElement_m_getElementKind, NBVR_Grammar_ParseElement_m_isInstance}

# Argument class attributes and methods

# NBVR_Logic_Argument class attributes and methods
NBVR_Logic_Argument_m_hasNext: Method = Method(name="hasNext", parameters={}, type=BooleanType)
NBVR_Logic_Argument.methods={NBVR_Logic_Argument_m_hasNext}

# Constant class attributes and methods

# NBVR_Logic_Quantification class attributes and methods
NBVR_Logic_Quantification_kind: Property = Property(name="kind", type=StringType)
NBVR_Logic_Quantification_unique: Property = Property(name="unique", type=BooleanType)
NBVR_Logic_Quantification.attributes={NBVR_Logic_Quantification_unique, NBVR_Logic_Quantification_kind}

# NBVR_Logic_Proposition class attributes and methods
NBVR_Logic_Proposition_text: Property = Property(name="text", type=StringType)
NBVR_Logic_Proposition_m_getType: Method = Method(name="getType", parameters={}, type=StringType)
NBVR_Logic_Proposition.attributes={NBVR_Logic_Proposition_text}
NBVR_Logic_Proposition.methods={NBVR_Logic_Proposition_m_getType}

# NBVR_Logic_Relation class attributes and methods
NBVR_Logic_Relation_m_getArgument: Method = Method(name="getArgument", parameters={}, type=StringType)
NBVR_Logic_Relation.methods={NBVR_Logic_Relation_m_getArgument}

# NBVR_Logic_ExtentConstant class attributes and methods

# NBVR_Logic_Connection class attributes and methods
NBVR_Logic_Connection_kind: Property = Property(name="kind", type=StringType)
NBVR_Logic_Connection.attributes={NBVR_Logic_Connection_kind}

# NBVR_Logic_Implication class attributes and methods

# NBVR_Logic_Constant class attributes and methods
NBVR_Logic_Constant_kind: Property = Property(name="kind", type=StringType)
NBVR_Logic_Constant.attributes={NBVR_Logic_Constant_kind}

# NBVR_Logic_Set class attributes and methods

# ExtentConstant class attributes and methods

# NBVR_Logic_NominalConstant class attributes and methods

# NBVR_Logic_QuantityValue class attributes and methods
NBVR_Logic_QuantityValue_factor: Property = Property(name="factor", type=StringType)
NBVR_Logic_QuantityValue_unit: Property = Property(name="unit", type=StringType)
NBVR_Logic_QuantityValue.attributes={NBVR_Logic_QuantityValue_unit, NBVR_Logic_QuantityValue_factor}

# NBVR_Logic_Predicate class attributes and methods
NBVR_Logic_Predicate_name: Property = Property(name="name", type=StringType)
NBVR_Logic_Predicate.attributes={NBVR_Logic_Predicate_name}

# RoleVariable class attributes and methods

# NBVR_Logic_Modal class attributes and methods
NBVR_Logic_Modal_kind: Property = Property(name="kind", type=StringType)
NBVR_Logic_Modal.attributes={NBVR_Logic_Modal_kind}

# NBVR_Logic_Negation class attributes and methods

# NBVR_Logic_RoleVariable class attributes and methods

# NBVR_Logic_ValueConstant class attributes and methods
NBVR_Logic_ValueConstant_name: Property = Property(name="name", type=StringType)
NBVR_Logic_ValueConstant.attributes={NBVR_Logic_ValueConstant_name}

# Relationships
altWord10: BinaryAssociation = BinaryAssociation(
    name="altWord10",
    ends={
        Property(name="Word12", type=NBVR_Vocabulary_WordForm, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_WordForm11", type=Word, multiplicity=Multiplicity(0, 1))
    }
)
concept13: BinaryAssociation = BinaryAssociation(
    name="concept13",
    ends={
        Property(name="Vocabulary", type=NBVR_Vocabulary_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="VocabularyItem", type=VocabularyItem, multiplicity=Multiplicity(0, 1))
    }
)
role14: BinaryAssociation = BinaryAssociation(
    name="role14",
    ends={
        Property(name="Vocabulary15", type=NBVR_Vocabulary_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="VerbRole", type=VerbRole, multiplicity=Multiplicity(0, 1))
    }
)
particle16: BinaryAssociation = BinaryAssociation(
    name="particle16",
    ends={
        Property(name="Vocabulary17", type=NBVR_Vocabulary_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="Particle", type=Particle, multiplicity=Multiplicity(0, 1))
    }
)
words18: BinaryAssociation = BinaryAssociation(
    name="words18",
    ends={
        Property(name="Word19", type=NBVR_Vocabulary_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_Term", type=Word, multiplicity=Multiplicity(1, 9999))
    }
)
context20: BinaryAssociation = BinaryAssociation(
    name="context20",
    ends={
        Property(name="VocabularyItem22", type=NBVR_Vocabulary_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_Term21", type=VocabularyItem, multiplicity=Multiplicity(0, 1))
    }
)
element23: BinaryAssociation = BinaryAssociation(
    name="element23",
    ends={
        Property(name="Vocabulary24", type=NBVR_Vocabulary_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="ItemElement", type=ItemElement, multiplicity=Multiplicity(0, 9999))
    }
)
base0: BinaryAssociation = BinaryAssociation(
    name="base0",
    ends={
        Property(name="WordForm", type=NBVR_Vocabulary_Word, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_Word", type=WordForm, multiplicity=Multiplicity(1, 1))
    }
)
beginsTerm1: BinaryAssociation = BinaryAssociation(
    name="beginsTerm1",
    ends={
        Property(name="Term", type=NBVR_Vocabulary_Word, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_Word2", type=Term, multiplicity=Multiplicity(0, 9999))
    }
)
next3: BinaryAssociation = BinaryAssociation(
    name="next3",
    ends={
        Property(name="Word", type=NBVR_Vocabulary_Word, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_Word4", type=Word, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
next5: BinaryAssociation = BinaryAssociation(
    name="next5",
    ends={
        Property(name="WordForm6", type=NBVR_Vocabulary_WordForm, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_WordForm", type=WordForm, multiplicity=Multiplicity(0, 1))
    }
)
word7: BinaryAssociation = BinaryAssociation(
    name="word7",
    ends={
        Property(name="Word9", type=NBVR_Vocabulary_WordForm, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_WordForm8", type=Word, multiplicity=Multiplicity(1, 1))
    }
)
next29: BinaryAssociation = BinaryAssociation(
    name="next29",
    ends={
        Property(name="VocabularyItem31", type=NBVR_Vocabulary_VocabularyItem, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_VocabularyItem30", type=VocabularyItem, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
terms32: BinaryAssociation = BinaryAssociation(
    name="terms32",
    ends={
        Property(name="Vocabulary34", type=NBVR_Vocabulary_VocabularyItem, multiplicity=Multiplicity(1, 1)),
        Property(name="Term33", type=Term, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
formulations25: BinaryAssociation = BinaryAssociation(
    name="formulations25",
    ends={
        Property(name="Vocabulary26", type=NBVR_Vocabulary_VocabularyItem, multiplicity=Multiplicity(1, 1)),
        Property(name="Formulation", type=Formulation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
base27: BinaryAssociation = BinaryAssociation(
    name="base27",
    ends={
        Property(name="VocabularyItem28", type=NBVR_Vocabulary_VocabularyItem, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_VocabularyItem", type=VocabularyItem, multiplicity=Multiplicity(0, 9999))
    }
)
isAVerb50: BinaryAssociation = BinaryAssociation(
    name="isAVerb50",
    ends={
        Property(name="VocVerb51", type=NBVR_Vocabulary_VocNoun, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_VocNoun", type=VocVerb, multiplicity=Multiplicity(0, 1))
    }
)
predicate52: BinaryAssociation = BinaryAssociation(
    name="predicate52",
    ends={
        Property(name="Logic", type=NBVR_Vocabulary_VocNoun, multiplicity=Multiplicity(1, 1)),
        Property(name="Predicate", type=Predicate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
roles53: BinaryAssociation = BinaryAssociation(
    name="roles53",
    ends={
        Property(name="Vocabulary55", type=NBVR_Vocabulary_VocVerb, multiplicity=Multiplicity(1, 1)),
        Property(name="VerbRole54", type=VerbRole, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
form56: BinaryAssociation = BinaryAssociation(
    name="form56",
    ends={
        Property(name="Vocabulary57", type=NBVR_Vocabulary_VocVerb, multiplicity=Multiplicity(1, 1)),
        Property(name="SyntaxForm", type=SyntaxForm, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
predicate58: BinaryAssociation = BinaryAssociation(
    name="predicate58",
    ends={
        Property(name="Logic60", type=NBVR_Vocabulary_VocVerb, multiplicity=Multiplicity(1, 1)),
        Property(name="Predicate59", type=Predicate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
form35: BinaryAssociation = BinaryAssociation(
    name="form35",
    ends={
        Property(name="Vocabulary36", type=NBVR_Vocabulary_Formulation, multiplicity=Multiplicity(1, 1)),
        Property(name="FormulationForm", type=FormulationForm, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements37: BinaryAssociation = BinaryAssociation(
    name="elements37",
    ends={
        Property(name="ParseElement", type=NBVR_Vocabulary_Formulation, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_Formulation", type=ParseElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
concept38: BinaryAssociation = BinaryAssociation(
    name="concept38",
    ends={
        Property(name="Vocabulary40", type=NBVR_Vocabulary_Formulation, multiplicity=Multiplicity(1, 1)),
        Property(name="VocabularyItem39", type=VocabularyItem, multiplicity=Multiplicity(1, 1))
    }
)
formulation41: BinaryAssociation = BinaryAssociation(
    name="formulation41",
    ends={
        Property(name="Vocabulary43", type=NBVR_Vocabulary_FormulationForm, multiplicity=Multiplicity(1, 1)),
        Property(name="Formulation42", type=Formulation, multiplicity=Multiplicity(0, 1))
    }
)
range44: BinaryAssociation = BinaryAssociation(
    name="range44",
    ends={
        Property(name="VocNoun", type=NBVR_Vocabulary_VerbRole, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_VerbRole", type=VocNoun, multiplicity=Multiplicity(1, 1))
    }
)
verb45: BinaryAssociation = BinaryAssociation(
    name="verb45",
    ends={
        Property(name="Vocabulary46", type=NBVR_Vocabulary_VerbRole, multiplicity=Multiplicity(1, 1)),
        Property(name="VocVerb", type=VocVerb, multiplicity=Multiplicity(1, 1))
    }
)
term47: BinaryAssociation = BinaryAssociation(
    name="term47",
    ends={
        Property(name="Vocabulary49", type=NBVR_Vocabulary_VerbRole, multiplicity=Multiplicity(1, 1)),
        Property(name="Term48", type=Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
domain71: BinaryAssociation = BinaryAssociation(
    name="domain71",
    ends={
        Property(name="VocNoun72", type=NBVR_Vocabulary_VocProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_VocProperty", type=VocNoun, multiplicity=Multiplicity(1, 1))
    }
)
range73: BinaryAssociation = BinaryAssociation(
    name="range73",
    ends={
        Property(name="VocNoun75", type=NBVR_Vocabulary_VocProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_VocProperty74", type=VocNoun, multiplicity=Multiplicity(1, 1))
    }
)
verb76: BinaryAssociation = BinaryAssociation(
    name="verb76",
    ends={
        Property(name="VocVerb78", type=NBVR_Vocabulary_VocProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_VocProperty77", type=VocVerb, multiplicity=Multiplicity(1, 1))
    }
)
propertyForm79: BinaryAssociation = BinaryAssociation(
    name="propertyForm79",
    ends={
        Property(name="Vocabulary81", type=NBVR_Vocabulary_VocProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="SyntaxForm80", type=SyntaxForm, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
quantityKind82: BinaryAssociation = BinaryAssociation(
    name="quantityKind82",
    ends={
        Property(name="VocProperty83", type=NBVR_Vocabulary_VocUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_VocUnit", type=VocProperty, multiplicity=Multiplicity(0, 1))
    }
)
elements61: BinaryAssociation = BinaryAssociation(
    name="elements61",
    ends={
        Property(name="Vocabulary62", type=NBVR_Vocabulary_SyntaxForm, multiplicity=Multiplicity(1, 1)),
        Property(name="FormElement", type=FormElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
property63: BinaryAssociation = BinaryAssociation(
    name="property63",
    ends={
        Property(name="Vocabulary64", type=NBVR_Vocabulary_SyntaxForm, multiplicity=Multiplicity(1, 1)),
        Property(name="VocProperty", type=VocProperty, multiplicity=Multiplicity(0, 1))
    }
)
verb65: BinaryAssociation = BinaryAssociation(
    name="verb65",
    ends={
        Property(name="Vocabulary67", type=NBVR_Vocabulary_SyntaxForm, multiplicity=Multiplicity(1, 1)),
        Property(name="VocVerb66", type=VocVerb, multiplicity=Multiplicity(0, 1))
    }
)
form68: BinaryAssociation = BinaryAssociation(
    name="form68",
    ends={
        Property(name="Vocabulary70", type=NBVR_Vocabulary_FormElement, multiplicity=Multiplicity(1, 1)),
        Property(name="SyntaxForm69", type=SyntaxForm, multiplicity=Multiplicity(0, 1))
    }
)
domain84: BinaryAssociation = BinaryAssociation(
    name="domain84",
    ends={
        Property(name="VocNoun85", type=NBVR_Vocabulary_VocAdjective, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_VocAdjective", type=VocNoun, multiplicity=Multiplicity(0, 1))
    }
)
verb86: BinaryAssociation = BinaryAssociation(
    name="verb86",
    ends={
        Property(name="VocVerb88", type=NBVR_Vocabulary_VocAdjective, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_VocAdjective87", type=VocVerb, multiplicity=Multiplicity(1, 1))
    }
)
role89: BinaryAssociation = BinaryAssociation(
    name="role89",
    ends={
        Property(name="RoleElement", type=NBVR_Vocabulary_Particle, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_Particle", type=RoleElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
term90: BinaryAssociation = BinaryAssociation(
    name="term90",
    ends={
        Property(name="Vocabulary92", type=NBVR_Vocabulary_Particle, multiplicity=Multiplicity(1, 1)),
        Property(name="Term91", type=Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
role93: BinaryAssociation = BinaryAssociation(
    name="role93",
    ends={
        Property(name="VerbRole94", type=NBVR_Vocabulary_RoleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_RoleElement", type=VerbRole, multiplicity=Multiplicity(1, 1))
    }
)
term95: BinaryAssociation = BinaryAssociation(
    name="term95",
    ends={
        Property(name="Vocabulary97", type=NBVR_Vocabulary_ItemElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Term96", type=Term, multiplicity=Multiplicity(1, 1))
    }
)
singular103: BinaryAssociation = BinaryAssociation(
    name="singular103",
    ends={
        Property(name="WordForm104", type=NBVR_Vocabulary_Verb, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_Verb", type=WordForm, multiplicity=Multiplicity(1, 1))
    }
)
plural105: BinaryAssociation = BinaryAssociation(
    name="plural105",
    ends={
        Property(name="WordForm107", type=NBVR_Vocabulary_Verb, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_Verb106", type=WordForm, multiplicity=Multiplicity(1, 1))
    }
)
past108: BinaryAssociation = BinaryAssociation(
    name="past108",
    ends={
        Property(name="WordForm110", type=NBVR_Vocabulary_Verb, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_Verb109", type=WordForm, multiplicity=Multiplicity(1, 1))
    }
)
progressive111: BinaryAssociation = BinaryAssociation(
    name="progressive111",
    ends={
        Property(name="WordForm113", type=NBVR_Vocabulary_Verb, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_Verb112", type=WordForm, multiplicity=Multiplicity(1, 1))
    }
)
perfective114: BinaryAssociation = BinaryAssociation(
    name="perfective114",
    ends={
        Property(name="WordForm116", type=NBVR_Vocabulary_Verb, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_Verb115", type=WordForm, multiplicity=Multiplicity(1, 1))
    }
)
altPast117: BinaryAssociation = BinaryAssociation(
    name="altPast117",
    ends={
        Property(name="WordForm119", type=NBVR_Vocabulary_Verb, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_Verb118", type=WordForm, multiplicity=Multiplicity(0, 1))
    }
)
firstWord120: BinaryAssociation = BinaryAssociation(
    name="firstWord120",
    ends={
        Property(name="Word121", type=NBVR_Vocabulary_Dictionary, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_Dictionary", type=Word, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
plural98: BinaryAssociation = BinaryAssociation(
    name="plural98",
    ends={
        Property(name="WordForm99", type=NBVR_Vocabulary_Noun, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_Noun", type=WordForm, multiplicity=Multiplicity(1, 1))
    }
)
altPlural100: BinaryAssociation = BinaryAssociation(
    name="altPlural100",
    ends={
        Property(name="WordForm102", type=NBVR_Vocabulary_Noun, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_Noun101", type=WordForm, multiplicity=Multiplicity(0, 1))
    }
)
rolePlayed128: BinaryAssociation = BinaryAssociation(
    name="rolePlayed128",
    ends={
        Property(name="VerbRole129", type=NBVR_Grammar_RolePhrase, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_RolePhrase", type=VerbRole, multiplicity=Multiplicity(0, 1))
    }
)
variable130: BinaryAssociation = BinaryAssociation(
    name="variable130",
    ends={
        Property(name="Variable", type=NBVR_Grammar_RolePhrase, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_RolePhrase131", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
referent132: BinaryAssociation = BinaryAssociation(
    name="referent132",
    ends={
        Property(name="RolePhrase", type=NBVR_Grammar_RolePhrase, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_RolePhrase133", type=RolePhrase, multiplicity=Multiplicity(0, 1))
    }
)
firstItem122: BinaryAssociation = BinaryAssociation(
    name="firstItem122",
    ends={
        Property(name="VocabularyItem123", type=NBVR_Vocabulary_Terminology, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_Terminology", type=VocabularyItem, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lastItem124: BinaryAssociation = BinaryAssociation(
    name="lastItem124",
    ends={
        Property(name="VocabularyItem126", type=NBVR_Vocabulary_Terminology, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_Terminology125", type=VocabularyItem, multiplicity=Multiplicity(0, 1))
    }
)
members127: BinaryAssociation = BinaryAssociation(
    name="members127",
    ends={
        Property(name="SimpleNounPhrase", type=NBVR_Grammar_GroupPhrase, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_GroupPhrase", type=SimpleNounPhrase, multiplicity=Multiplicity(1, 9999))
    }
)
qualifiers142: BinaryAssociation = BinaryAssociation(
    name="qualifiers142",
    ends={
        Property(name="Grammar144", type=NBVR_Grammar_QualifierChain, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleQualifier143", type=SimpleQualifier, multiplicity=Multiplicity(1, 9999))
    }
)
domain145: BinaryAssociation = BinaryAssociation(
    name="domain145",
    ends={
        Property(name="RolePhrase146", type=NBVR_Grammar_Sentence, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_Sentence", type=RolePhrase, multiplicity=Multiplicity(0, 1))
    }
)
rewrites147: BinaryAssociation = BinaryAssociation(
    name="rewrites147",
    ends={
        Property(name="Sentence149", type=NBVR_Grammar_Sentence, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_Sentence148", type=Sentence, multiplicity=Multiplicity(0, 1))
    }
)
qualifier134: BinaryAssociation = BinaryAssociation(
    name="qualifier134",
    ends={
        Property(name="Grammar", type=NBVR_Grammar_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleQualifier", type=SimpleQualifier, multiplicity=Multiplicity(1, 1))
    }
)
antecedent135: BinaryAssociation = BinaryAssociation(
    name="antecedent135",
    ends={
        Property(name="Sentence", type=NBVR_Grammar_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_Condition", type=Sentence, multiplicity=Multiplicity(0, 1))
    }
)
chain136: BinaryAssociation = BinaryAssociation(
    name="chain136",
    ends={
        Property(name="Grammar137", type=NBVR_Grammar_SimpleQualifier, multiplicity=Multiplicity(1, 1)),
        Property(name="QualifierChain", type=QualifierChain, multiplicity=Multiplicity(0, 1))
    }
)
boundForm138: BinaryAssociation = BinaryAssociation(
    name="boundForm138",
    ends={
        Property(name="Sentence139", type=NBVR_Grammar_SimpleQualifier, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_SimpleQualifier", type=Sentence, multiplicity=Multiplicity(1, 1))
    }
)
condition140: BinaryAssociation = BinaryAssociation(
    name="condition140",
    ends={
        Property(name="Grammar141", type=NBVR_Grammar_SimpleQualifier, multiplicity=Multiplicity(1, 1)),
        Property(name="Condition", type=Condition, multiplicity=Multiplicity(0, 1))
    }
)
quantity157: BinaryAssociation = BinaryAssociation(
    name="quantity157",
    ends={
        Property(name="Quantity", type=NBVR_Grammar_Quantifier, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_Quantifier", type=Quantity, multiplicity=Multiplicity(0, 1))
    }
)
factor158: BinaryAssociation = BinaryAssociation(
    name="factor158",
    ends={
        Property(name="NumberWord", type=NBVR_Grammar_Quantity, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_Quantity", type=NumberWord, multiplicity=Multiplicity(1, 1))
    }
)
dimension159: BinaryAssociation = BinaryAssociation(
    name="dimension159",
    ends={
        Property(name="Dimension", type=NBVR_Grammar_Quantity, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_Quantity160", type=Dimension, multiplicity=Multiplicity(0, 9999))
    }
)
unit161: BinaryAssociation = BinaryAssociation(
    name="unit161",
    ends={
        Property(name="VocUnit", type=NBVR_Grammar_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_Dimension", type=VocUnit, multiplicity=Multiplicity(1, 1))
    }
)
noun150: BinaryAssociation = BinaryAssociation(
    name="noun150",
    ends={
        Property(name="VocNoun151", type=NBVR_Grammar_TypeNoun, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_TypeNoun", type=VocNoun, multiplicity=Multiplicity(1, 1))
    }
)
quantifier152: BinaryAssociation = BinaryAssociation(
    name="quantifier152",
    ends={
        Property(name="Quantifier", type=NBVR_Grammar_ModifiedTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_ModifiedTerm", type=Quantifier, multiplicity=Multiplicity(0, 1))
    }
)
modifiers153: BinaryAssociation = BinaryAssociation(
    name="modifiers153",
    ends={
        Property(name="Modifier", type=NBVR_Grammar_ModifiedTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_ModifiedTerm154", type=Modifier, multiplicity=Multiplicity(0, 9999))
    }
)
qualifiers155: BinaryAssociation = BinaryAssociation(
    name="qualifiers155",
    ends={
        Property(name="Qualifier", type=NBVR_Grammar_ModifiedTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_ModifiedTerm156", type=Qualifier, multiplicity=Multiplicity(0, 9999))
    }
)
verb175: BinaryAssociation = BinaryAssociation(
    name="verb175",
    ends={
        Property(name="VocVerb176", type=NBVR_Grammar_VerbPhrase, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_VerbPhrase", type=VocVerb, multiplicity=Multiplicity(1, 1))
    }
)
partRole177: BinaryAssociation = BinaryAssociation(
    name="partRole177",
    ends={
        Property(name="RolePhrase178", type=NBVR_Grammar_PartPhrase, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_PartPhrase", type=RolePhrase, multiplicity=Multiplicity(0, 1))
    }
)
particle179: BinaryAssociation = BinaryAssociation(
    name="particle179",
    ends={
        Property(name="Particle181", type=NBVR_Grammar_PartPhrase, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_PartPhrase180", type=Particle, multiplicity=Multiplicity(1, 1))
    }
)
verb182: BinaryAssociation = BinaryAssociation(
    name="verb182",
    ends={
        Property(name="VerbPhrase", type=NBVR_Grammar_SimpleForm, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_SimpleForm", type=VerbPhrase, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
adjective162: BinaryAssociation = BinaryAssociation(
    name="adjective162",
    ends={
        Property(name="VocAdjective", type=NBVR_Grammar_Modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_Modifier", type=VocAdjective, multiplicity=Multiplicity(0, 1))
    }
)
relative163: BinaryAssociation = BinaryAssociation(
    name="relative163",
    ends={
        Property(name="RolePhrase165", type=NBVR_Grammar_Modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_Modifier164", type=RolePhrase, multiplicity=Multiplicity(0, 1))
    }
)
property166: BinaryAssociation = BinaryAssociation(
    name="property166",
    ends={
        Property(name="VocProperty167", type=NBVR_Grammar_PropertyNoun, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_PropertyNoun", type=VocProperty, multiplicity=Multiplicity(1, 1))
    }
)
domain168: BinaryAssociation = BinaryAssociation(
    name="domain168",
    ends={
        Property(name="SimpleNounPhrase170", type=NBVR_Grammar_PropertyNoun, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_PropertyNoun169", type=SimpleNounPhrase, multiplicity=Multiplicity(1, 1))
    }
)
expansion171: BinaryAssociation = BinaryAssociation(
    name="expansion171",
    ends={
        Property(name="TypeNoun", type=NBVR_Grammar_PropertyNoun, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_PropertyNoun172", type=TypeNoun, multiplicity=Multiplicity(0, 1))
    }
)
role173: BinaryAssociation = BinaryAssociation(
    name="role173",
    ends={
        Property(name="VerbRole174", type=NBVR_Grammar_RoleNoun, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_RoleNoun", type=VerbRole, multiplicity=Multiplicity(0, 1))
    }
)
statements199: BinaryAssociation = BinaryAssociation(
    name="statements199",
    ends={
        Property(name="Sentence200", type=NBVR_Grammar_CompoundForm, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_CompoundForm", type=Sentence, multiplicity=Multiplicity(1, 9999))
    }
)
word201: BinaryAssociation = BinaryAssociation(
    name="word201",
    ends={
        Property(name="Word202", type=NBVR_Grammar_LexicalInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_LexicalInstance", type=Word, multiplicity=Multiplicity(1, 1))
    }
)
sentence203: BinaryAssociation = BinaryAssociation(
    name="sentence203",
    ends={
        Property(name="Sentence204", type=NBVR_Grammar_Nominalization, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_Nominalization", type=Sentence, multiplicity=Multiplicity(1, 1))
    }
)
partPhrases183: BinaryAssociation = BinaryAssociation(
    name="partPhrases183",
    ends={
        Property(name="PartPhrase", type=NBVR_Grammar_SimpleForm, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_SimpleForm184", type=PartPhrase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subject185: BinaryAssociation = BinaryAssociation(
    name="subject185",
    ends={
        Property(name="RolePhrase187", type=NBVR_Grammar_SimpleForm, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_SimpleForm186", type=RolePhrase, multiplicity=Multiplicity(1, 1))
    }
)
object188: BinaryAssociation = BinaryAssociation(
    name="object188",
    ends={
        Property(name="RolePhrase190", type=NBVR_Grammar_SimpleForm, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_SimpleForm189", type=RolePhrase, multiplicity=Multiplicity(0, 1))
    }
)
antecedent191: BinaryAssociation = BinaryAssociation(
    name="antecedent191",
    ends={
        Property(name="Sentence192", type=NBVR_Grammar_ImplicationForm, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_ImplicationForm", type=Sentence, multiplicity=Multiplicity(1, 1))
    }
)
consequent193: BinaryAssociation = BinaryAssociation(
    name="consequent193",
    ends={
        Property(name="Sentence195", type=NBVR_Grammar_ImplicationForm, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_ImplicationForm194", type=Sentence, multiplicity=Multiplicity(1, 1))
    }
)
alternative196: BinaryAssociation = BinaryAssociation(
    name="alternative196",
    ends={
        Property(name="Sentence198", type=NBVR_Grammar_ImplicationForm, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_ImplicationForm197", type=Sentence, multiplicity=Multiplicity(0, 1))
    }
)
name211: BinaryAssociation = BinaryAssociation(
    name="name211",
    ends={
        Property(name="VocName", type=NBVR_Grammar_ProperName, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_ProperName", type=VocName, multiplicity=Multiplicity(1, 1))
    }
)
keyword212: BinaryAssociation = BinaryAssociation(
    name="keyword212",
    ends={
        Property(name="Keyword", type=NBVR_Grammar_Pronoun, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_Pronoun", type=Keyword, multiplicity=Multiplicity(1, 1))
    }
)
concept213: BinaryAssociation = BinaryAssociation(
    name="concept213",
    ends={
        Property(name="RolePhrase214", type=NBVR_Grammar_Intension, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_Intension", type=RolePhrase, multiplicity=Multiplicity(0, 1))
    }
)
statement215: BinaryAssociation = BinaryAssociation(
    name="statement215",
    ends={
        Property(name="Sentence216", type=NBVR_Grammar_DomainForm, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_DomainForm", type=Sentence, multiplicity=Multiplicity(0, 1))
    }
)
queryPhrase205: BinaryAssociation = BinaryAssociation(
    name="queryPhrase205",
    ends={
        Property(name="Grammar206", type=NBVR_Grammar_Question, multiplicity=Multiplicity(1, 1)),
        Property(name="QueryPhrase", type=QueryPhrase, multiplicity=Multiplicity(0, 1))
    }
)
domain207: BinaryAssociation = BinaryAssociation(
    name="domain207",
    ends={
        Property(name="RolePhrase208", type=NBVR_Grammar_QueryPhrase, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_QueryPhrase", type=RolePhrase, multiplicity=Multiplicity(1, 1))
    }
)
question209: BinaryAssociation = BinaryAssociation(
    name="question209",
    ends={
        Property(name="Grammar210", type=NBVR_Grammar_QueryPhrase, multiplicity=Multiplicity(1, 1)),
        Property(name="Question", type=Question, multiplicity=Multiplicity(1, 1))
    }
)
parent221: BinaryAssociation = BinaryAssociation(
    name="parent221",
    ends={
        Property(name="ParseElement222", type=NBVR_Grammar_ParseElement, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_ParseElement", type=ParseElement, multiplicity=Multiplicity(0, 1))
    }
)
source223: BinaryAssociation = BinaryAssociation(
    name="source223",
    ends={
        Property(name="Logic224", type=NBVR_Logic_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="Quantification", type=Quantification, multiplicity=Multiplicity(0, 1))
    }
)
constraint225: BinaryAssociation = BinaryAssociation(
    name="constraint225",
    ends={
        Property(name="Proposition", type=NBVR_Logic_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Logic_Variable", type=Proposition, multiplicity=Multiplicity(0, 1))
    }
)
uses226: BinaryAssociation = BinaryAssociation(
    name="uses226",
    ends={
        Property(name="Relation", type=NBVR_Logic_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Logic_Variable227", type=Relation, multiplicity=Multiplicity(1, 9999))
    }
)
range228: BinaryAssociation = BinaryAssociation(
    name="range228",
    ends={
        Property(name="VocNoun230", type=NBVR_Logic_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Logic_Variable229", type=VocNoun, multiplicity=Multiplicity(1, 1))
    }
)
set231: BinaryAssociation = BinaryAssociation(
    name="set231",
    ends={
        Property(name="Logic232", type=NBVR_Logic_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="Set", type=Set, multiplicity=Multiplicity(0, 1))
    }
)
word217: BinaryAssociation = BinaryAssociation(
    name="word217",
    ends={
        Property(name="Word218", type=NBVR_Grammar_LocalName, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_LocalName", type=Word, multiplicity=Multiplicity(1, 1))
    }
)
next219: BinaryAssociation = BinaryAssociation(
    name="next219",
    ends={
        Property(name="LocalName", type=NBVR_Grammar_LocalName, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_LocalName220", type=LocalName, multiplicity=Multiplicity(0, 1))
    }
)
arguments240: BinaryAssociation = BinaryAssociation(
    name="arguments240",
    ends={
        Property(name="Logic241", type=NBVR_Logic_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="Argument", type=Argument, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
predicate242: BinaryAssociation = BinaryAssociation(
    name="predicate242",
    ends={
        Property(name="Predicate243", type=NBVR_Logic_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Logic_Relation", type=Predicate, multiplicity=Multiplicity(1, 1))
    }
)
next244: BinaryAssociation = BinaryAssociation(
    name="next244",
    ends={
        Property(name="Argument245", type=NBVR_Logic_Argument, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Logic_Argument", type=Argument, multiplicity=Multiplicity(0, 1))
    }
)
variable246: BinaryAssociation = BinaryAssociation(
    name="variable246",
    ends={
        Property(name="Variable248", type=NBVR_Logic_Argument, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Logic_Argument247", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
phrase249: BinaryAssociation = BinaryAssociation(
    name="phrase249",
    ends={
        Property(name="RolePhrase251", type=NBVR_Logic_Argument, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Logic_Argument250", type=RolePhrase, multiplicity=Multiplicity(1, 1))
    }
)
role252: BinaryAssociation = BinaryAssociation(
    name="role252",
    ends={
        Property(name="VerbRole254", type=NBVR_Logic_Argument, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Logic_Argument253", type=VerbRole, multiplicity=Multiplicity(0, 1))
    }
)
constant255: BinaryAssociation = BinaryAssociation(
    name="constant255",
    ends={
        Property(name="Constant", type=NBVR_Logic_Argument, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Logic_Argument256", type=Constant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scope233: BinaryAssociation = BinaryAssociation(
    name="scope233",
    ends={
        Property(name="Proposition234", type=NBVR_Logic_Quantification, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Logic_Quantification", type=Proposition, multiplicity=Multiplicity(1, 1))
    }
)
variable235: BinaryAssociation = BinaryAssociation(
    name="variable235",
    ends={
        Property(name="Logic237", type=NBVR_Logic_Quantification, multiplicity=Multiplicity(1, 1)),
        Property(name="Variable236", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
owner238: BinaryAssociation = BinaryAssociation(
    name="owner238",
    ends={
        Property(name="Proposition239", type=NBVR_Logic_Proposition, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Logic_Proposition", type=Proposition, multiplicity=Multiplicity(0, 1))
    }
)
variable262: BinaryAssociation = BinaryAssociation(
    name="variable262",
    ends={
        Property(name="Logic264", type=NBVR_Logic_Set, multiplicity=Multiplicity(1, 1)),
        Property(name="Variable263", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
set265: BinaryAssociation = BinaryAssociation(
    name="set265",
    ends={
        Property(name="Logic267", type=NBVR_Logic_ExtentConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="Set266", type=Set, multiplicity=Multiplicity(1, 1))
    }
)
operands268: BinaryAssociation = BinaryAssociation(
    name="operands268",
    ends={
        Property(name="Proposition269", type=NBVR_Logic_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Logic_Connection", type=Proposition, multiplicity=Multiplicity(1, 9999))
    }
)
antecedent270: BinaryAssociation = BinaryAssociation(
    name="antecedent270",
    ends={
        Property(name="Proposition271", type=NBVR_Logic_Implication, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Logic_Implication", type=Proposition, multiplicity=Multiplicity(1, 1))
    }
)
relation257: BinaryAssociation = BinaryAssociation(
    name="relation257",
    ends={
        Property(name="Logic259", type=NBVR_Logic_Argument, multiplicity=Multiplicity(1, 1)),
        Property(name="Relation258", type=Relation, multiplicity=Multiplicity(1, 1))
    }
)
extent260: BinaryAssociation = BinaryAssociation(
    name="extent260",
    ends={
        Property(name="Logic261", type=NBVR_Logic_Set, multiplicity=Multiplicity(1, 1)),
        Property(name="ExtentConstant", type=ExtentConstant, multiplicity=Multiplicity(0, 1))
    }
)
proposition284: BinaryAssociation = BinaryAssociation(
    name="proposition284",
    ends={
        Property(name="Proposition285", type=NBVR_Logic_NominalConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Logic_NominalConstant", type=Proposition, multiplicity=Multiplicity(1, 1))
    }
)
variables286: BinaryAssociation = BinaryAssociation(
    name="variables286",
    ends={
        Property(name="Logic287", type=NBVR_Logic_Predicate, multiplicity=Multiplicity(1, 1)),
        Property(name="RoleVariable", type=RoleVariable, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
noun288: BinaryAssociation = BinaryAssociation(
    name="noun288",
    ends={
        Property(name="Vocabulary290", type=NBVR_Logic_Predicate, multiplicity=Multiplicity(1, 1)),
        Property(name="VocNoun289", type=VocNoun, multiplicity=Multiplicity(0, 1))
    }
)
verb291: BinaryAssociation = BinaryAssociation(
    name="verb291",
    ends={
        Property(name="Vocabulary293", type=NBVR_Logic_Predicate, multiplicity=Multiplicity(1, 1)),
        Property(name="VocVerb292", type=VocVerb, multiplicity=Multiplicity(0, 1))
    }
)
consequent272: BinaryAssociation = BinaryAssociation(
    name="consequent272",
    ends={
        Property(name="Proposition274", type=NBVR_Logic_Implication, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Logic_Implication273", type=Proposition, multiplicity=Multiplicity(1, 1))
    }
)
scope275: BinaryAssociation = BinaryAssociation(
    name="scope275",
    ends={
        Property(name="Proposition276", type=NBVR_Logic_Modal, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Logic_Modal", type=Proposition, multiplicity=Multiplicity(1, 1))
    }
)
scope277: BinaryAssociation = BinaryAssociation(
    name="scope277",
    ends={
        Property(name="Proposition278", type=NBVR_Logic_Negation, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Logic_Negation", type=Proposition, multiplicity=Multiplicity(1, 1))
    }
)
predicate279: BinaryAssociation = BinaryAssociation(
    name="predicate279",
    ends={
        Property(name="Logic281", type=NBVR_Logic_RoleVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="Predicate280", type=Predicate, multiplicity=Multiplicity(0, 1))
    }
)
role282: BinaryAssociation = BinaryAssociation(
    name="role282",
    ends={
        Property(name="VerbRole283", type=NBVR_Logic_RoleVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Logic_RoleVariable", type=VerbRole, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_NBVR_Vocabulary_Adjective_Word = Generalization(general=Word, specific=NBVR_Vocabulary_Adjective)
gen_NBVR_Vocabulary_VocNoun_VocabularyItem = Generalization(general=VocabularyItem, specific=NBVR_Vocabulary_VocNoun)
gen_NBVR_Vocabulary_VocVerb_VocabularyItem = Generalization(general=VocabularyItem, specific=NBVR_Vocabulary_VocVerb)
gen_NBVR_Vocabulary_NumberWord_Word = Generalization(general=Word, specific=NBVR_Vocabulary_NumberWord)
gen_NBVR_Vocabulary_VocUnit_VocName = Generalization(general=VocName, specific=NBVR_Vocabulary_VocUnit)
gen_NBVR_Vocabulary_VocName_VocabularyItem = Generalization(general=VocabularyItem, specific=NBVR_Vocabulary_VocName)
gen_NBVR_Vocabulary_VocAdjective_VocabularyItem = Generalization(general=VocabularyItem, specific=NBVR_Vocabulary_VocAdjective)
gen_NBVR_Vocabulary_VocProperty_VocabularyItem = Generalization(general=VocabularyItem, specific=NBVR_Vocabulary_VocProperty)
gen_NBVR_Vocabulary_RoleElement_FormElement = Generalization(general=FormElement, specific=NBVR_Vocabulary_RoleElement)
gen_NBVR_Vocabulary_Keyword_Word = Generalization(general=Word, specific=NBVR_Vocabulary_Keyword)
gen_NBVR_Vocabulary_ItemElement_FormElement = Generalization(general=FormElement, specific=NBVR_Vocabulary_ItemElement)
gen_NBVR_Vocabulary_Particle_FormElement = Generalization(general=FormElement, specific=NBVR_Vocabulary_Particle)
gen_NBVR_Vocabulary_Adjunct_Word = Generalization(general=Word, specific=NBVR_Vocabulary_Adjunct)
gen_NBVR_Vocabulary_Noun_Word = Generalization(general=Word, specific=NBVR_Vocabulary_Noun)
gen_NBVR_Vocabulary_Name_Word = Generalization(general=Word, specific=NBVR_Vocabulary_Name)
gen_NBVR_Vocabulary_Verb_Word = Generalization(general=Word, specific=NBVR_Vocabulary_Verb)
gen_NBVR_Vocabulary_StringWord_Word = Generalization(general=Word, specific=NBVR_Vocabulary_StringWord)
gen_NBVR_Vocabulary_Definition_Formulation = Generalization(general=Formulation, specific=NBVR_Vocabulary_Definition)
gen_NBVR_Vocabulary_DateTime_Word = Generalization(general=Word, specific=NBVR_Vocabulary_DateTime)
gen_NBVR_Vocabulary_IsVerb_Verb = Generalization(general=Verb, specific=NBVR_Vocabulary_IsVerb)
gen_NBVR_Grammar_GroupPhrase_RolePhrase = Generalization(general=RolePhrase, specific=NBVR_Grammar_GroupPhrase)
gen_NBVR_Grammar_RolePhrase_Vocabulary_FormulationForm = Generalization(general=Vocabulary_FormulationForm, specific=NBVR_Grammar_RolePhrase)
gen_NBVR_Grammar_RolePhrase_Grammar_ParseElement = Generalization(general=Grammar_ParseElement, specific=NBVR_Grammar_RolePhrase)
gen_NBVR_Grammar_Qualifier_ParseElement = Generalization(general=ParseElement, specific=NBVR_Grammar_Qualifier)
gen_NBVR_Grammar_QualifierChain_Qualifier = Generalization(general=Qualifier, specific=NBVR_Grammar_QualifierChain)
gen_NBVR_Grammar_Sentence_Vocabulary_FormulationForm = Generalization(general=Vocabulary_FormulationForm, specific=NBVR_Grammar_Sentence)
gen_NBVR_Grammar_Sentence_Grammar_ParseElement = Generalization(general=Grammar_ParseElement, specific=NBVR_Grammar_Sentence)
gen_NBVR_Grammar_SimpleNounPhrase_RolePhrase = Generalization(general=RolePhrase, specific=NBVR_Grammar_SimpleNounPhrase)
gen_NBVR_Grammar_Condition_ParseElement = Generalization(general=ParseElement, specific=NBVR_Grammar_Condition)
gen_NBVR_Grammar_SimpleQualifier_Qualifier = Generalization(general=Qualifier, specific=NBVR_Grammar_SimpleQualifier)
gen_NBVR_Grammar_Quantity_Instance = Generalization(general=Instance, specific=NBVR_Grammar_Quantity)
gen_NBVR_Grammar_Instance_SimpleNounPhrase = Generalization(general=SimpleNounPhrase, specific=NBVR_Grammar_Instance)
gen_NBVR_Grammar_Modifier_ParseElement = Generalization(general=ParseElement, specific=NBVR_Grammar_Modifier)
gen_NBVR_Grammar_TypeNoun_ModifiedTerm = Generalization(general=ModifiedTerm, specific=NBVR_Grammar_TypeNoun)
gen_NBVR_Grammar_ModifiedTerm_SimpleNounPhrase = Generalization(general=SimpleNounPhrase, specific=NBVR_Grammar_ModifiedTerm)
gen_NBVR_Grammar_Quantifier_ParseElement = Generalization(general=ParseElement, specific=NBVR_Grammar_Quantifier)
gen_NBVR_Grammar_SimpleForm_Sentence = Generalization(general=Sentence, specific=NBVR_Grammar_SimpleForm)
gen_NBVR_Grammar_PropertyNoun_ModifiedTerm = Generalization(general=ModifiedTerm, specific=NBVR_Grammar_PropertyNoun)
gen_NBVR_Grammar_RoleNoun_SimpleNounPhrase = Generalization(general=SimpleNounPhrase, specific=NBVR_Grammar_RoleNoun)
gen_NBVR_Grammar_CompoundForm_Sentence = Generalization(general=Sentence, specific=NBVR_Grammar_CompoundForm)
gen_NBVR_Grammar_LexicalInstance_Instance = Generalization(general=Instance, specific=NBVR_Grammar_LexicalInstance)
gen_NBVR_Grammar_Nominalization_Instance = Generalization(general=Instance, specific=NBVR_Grammar_Nominalization)
gen_NBVR_Grammar_Statement_Nominalization = Generalization(general=Nominalization, specific=NBVR_Grammar_Statement)
gen_NBVR_Grammar_Question_Nominalization = Generalization(general=Nominalization, specific=NBVR_Grammar_Question)
gen_NBVR_Grammar_ImplicationForm_Sentence = Generalization(general=Sentence, specific=NBVR_Grammar_ImplicationForm)
gen_NBVR_Grammar_ProperName_Instance = Generalization(general=Instance, specific=NBVR_Grammar_ProperName)
gen_NBVR_Grammar_Pronoun_ModifiedTerm = Generalization(general=ModifiedTerm, specific=NBVR_Grammar_Pronoun)
gen_NBVR_Grammar_Intension_Instance = Generalization(general=Instance, specific=NBVR_Grammar_Intension)
gen_NBVR_Grammar_DomainForm_Sentence = Generalization(general=Sentence, specific=NBVR_Grammar_DomainForm)
gen_NBVR_Grammar_QueryPhrase_RolePhrase = Generalization(general=RolePhrase, specific=NBVR_Grammar_QueryPhrase)
gen_NBVR_Grammar_LocalName_SimpleNounPhrase = Generalization(general=SimpleNounPhrase, specific=NBVR_Grammar_LocalName)
gen_NBVR_Logic_Relation_Proposition = Generalization(general=Proposition, specific=NBVR_Logic_Relation)
gen_NBVR_Logic_Quantification_Proposition = Generalization(general=Proposition, specific=NBVR_Logic_Quantification)
gen_NBVR_Logic_Proposition_FormulationForm = Generalization(general=FormulationForm, specific=NBVR_Logic_Proposition)
gen_NBVR_Logic_ExtentConstant_Constant = Generalization(general=Constant, specific=NBVR_Logic_ExtentConstant)
gen_NBVR_Logic_Connection_Proposition = Generalization(general=Proposition, specific=NBVR_Logic_Connection)
gen_NBVR_Logic_Implication_Proposition = Generalization(general=Proposition, specific=NBVR_Logic_Implication)
gen_NBVR_Logic_NominalConstant_Constant = Generalization(general=Constant, specific=NBVR_Logic_NominalConstant)
gen_NBVR_Logic_QuantityValue_Constant = Generalization(general=Constant, specific=NBVR_Logic_QuantityValue)
gen_NBVR_Logic_Modal_Proposition = Generalization(general=Proposition, specific=NBVR_Logic_Modal)
gen_NBVR_Logic_Negation_Proposition = Generalization(general=Proposition, specific=NBVR_Logic_Negation)
gen_NBVR_Logic_RoleVariable_Variable = Generalization(general=Variable, specific=NBVR_Logic_RoleVariable)
gen_NBVR_Logic_ValueConstant_Constant = Generalization(general=Constant, specific=NBVR_Logic_ValueConstant)

# Domain Model
domain_model = DomainModel(
    name="NBVR",
    types={NBVR_Vocabulary_Adjective, Word, NBVR_Vocabulary_Word, NBVR_Vocabulary_Term, VocabularyItem, VerbRole, Particle, ItemElement, NBVR_Vocabulary_VocabularyItem, WordForm, Term, NBVR_Vocabulary_WordForm, NBVR_Vocabulary_Formulation, Formulation, NBVR_Vocabulary_VocNoun, Predicate, NBVR_Vocabulary_VocVerb, SyntaxForm, FormulationForm, ParseElement, NBVR_Vocabulary_FormulationForm, NBVR_Vocabulary_VerbRole, VocNoun, VocVerb, NBVR_Vocabulary_NumberWord, NBVR_Vocabulary_VocUnit, VocName, NBVR_Vocabulary_VocName, NBVR_Vocabulary_VocAdjective, NBVR_Vocabulary_SyntaxForm, FormElement, VocProperty, NBVR_Vocabulary_FormElement, NBVR_Vocabulary_VocProperty, NBVR_Vocabulary_RoleElement, NBVR_Vocabulary_Keyword, NBVR_Vocabulary_ItemElement, NBVR_Vocabulary_Particle, RoleElement, NBVR_Vocabulary_Dictionary, NBVR_Vocabulary_StringWord, NBVR_Vocabulary_Adjunct, NBVR_Vocabulary_Noun, NBVR_Vocabulary_Name, NBVR_Vocabulary_Verb, Variable, NBVR_Vocabulary_Definition, NBVR_Vocabulary_DateTime, NBVR_Vocabulary_Terminology, NBVR_Vocabulary_IsVerb, Verb, NBVR_Grammar_GroupPhrase, RolePhrase, SimpleNounPhrase, NBVR_Grammar_RolePhrase, Vocabulary_FormulationForm, Grammar_ParseElement, NBVR_Grammar_Qualifier, NBVR_Grammar_QualifierChain, NBVR_Grammar_Sentence, NBVR_Grammar_SimpleNounPhrase, NBVR_Grammar_Condition, SimpleQualifier, Sentence, NBVR_Grammar_SimpleQualifier, Qualifier, QualifierChain, Condition, Quantity, NBVR_Grammar_Quantity, Instance, NumberWord, Dimension, NBVR_Grammar_Instance, NBVR_Grammar_Dimension, VocUnit, NBVR_Grammar_Modifier, VocAdjective, NBVR_Grammar_TypeNoun, ModifiedTerm, NBVR_Grammar_ModifiedTerm, Quantifier, Modifier, NBVR_Grammar_Quantifier, NBVR_Grammar_VerbPhrase, NBVR_Grammar_PartPhrase, NBVR_Grammar_SimpleForm, VerbPhrase, NBVR_Grammar_PropertyNoun, TypeNoun, NBVR_Grammar_RoleNoun, NBVR_Grammar_CompoundForm, NBVR_Grammar_LexicalInstance, NBVR_Grammar_Nominalization, NBVR_Grammar_Statement, Nominalization, NBVR_Grammar_Question, QueryPhrase, PartPhrase, NBVR_Grammar_ImplicationForm, NBVR_Grammar_Pronoun, Keyword, NBVR_Grammar_Intension, NBVR_Grammar_Parse, NBVR_Grammar_DomainForm, NBVR_Grammar_QueryPhrase, Question, NBVR_Grammar_ProperName, NBVR_Logic_Variable, Quantification, Proposition, Relation, Set, NBVR_Grammar_LocalName, LocalName, NBVR_Grammar_ParseElement, Argument, NBVR_Logic_Argument, Constant, NBVR_Logic_Quantification, NBVR_Logic_Proposition, NBVR_Logic_Relation, NBVR_Logic_ExtentConstant, NBVR_Logic_Connection, NBVR_Logic_Implication, NBVR_Logic_Constant, NBVR_Logic_Set, ExtentConstant, NBVR_Logic_NominalConstant, NBVR_Logic_QuantityValue, NBVR_Logic_Predicate, RoleVariable, NBVR_Logic_Modal, NBVR_Logic_Negation, NBVR_Logic_RoleVariable, NBVR_Logic_ValueConstant, FormElementKind, KeywordKind, VocItemKind, QuantifierKind, PhraseType, InstanceKind, Connective, Modality, SentenceType, GroupKind, QueryKind, ElementKind, PropositionKind},
    associations={altWord10, concept13, role14, particle16, words18, context20, element23, base0, beginsTerm1, next3, next5, word7, next29, terms32, formulations25, base27, isAVerb50, predicate52, roles53, form56, predicate58, form35, elements37, concept38, formulation41, range44, verb45, term47, domain71, range73, verb76, propertyForm79, quantityKind82, elements61, property63, verb65, form68, domain84, verb86, role89, term90, role93, term95, singular103, plural105, past108, progressive111, perfective114, altPast117, firstWord120, plural98, altPlural100, rolePlayed128, variable130, referent132, firstItem122, lastItem124, members127, qualifiers142, domain145, rewrites147, qualifier134, antecedent135, chain136, boundForm138, condition140, quantity157, factor158, dimension159, unit161, noun150, quantifier152, modifiers153, qualifiers155, verb175, partRole177, particle179, verb182, adjective162, relative163, property166, domain168, expansion171, role173, statements199, word201, sentence203, partPhrases183, subject185, object188, antecedent191, consequent193, alternative196, name211, keyword212, concept213, statement215, queryPhrase205, domain207, question209, parent221, source223, constraint225, uses226, range228, set231, word217, next219, arguments240, predicate242, next244, variable246, phrase249, role252, constant255, scope233, variable235, owner238, variable262, set265, operands268, antecedent270, relation257, extent260, proposition284, variables286, noun288, verb291, consequent272, scope275, scope277, predicate279, role282},
    generalizations={gen_NBVR_Vocabulary_Adjective_Word, gen_NBVR_Vocabulary_VocNoun_VocabularyItem, gen_NBVR_Vocabulary_VocVerb_VocabularyItem, gen_NBVR_Vocabulary_NumberWord_Word, gen_NBVR_Vocabulary_VocUnit_VocName, gen_NBVR_Vocabulary_VocName_VocabularyItem, gen_NBVR_Vocabulary_VocAdjective_VocabularyItem, gen_NBVR_Vocabulary_VocProperty_VocabularyItem, gen_NBVR_Vocabulary_RoleElement_FormElement, gen_NBVR_Vocabulary_Keyword_Word, gen_NBVR_Vocabulary_ItemElement_FormElement, gen_NBVR_Vocabulary_Particle_FormElement, gen_NBVR_Vocabulary_Adjunct_Word, gen_NBVR_Vocabulary_Noun_Word, gen_NBVR_Vocabulary_Name_Word, gen_NBVR_Vocabulary_Verb_Word, gen_NBVR_Vocabulary_StringWord_Word, gen_NBVR_Vocabulary_Definition_Formulation, gen_NBVR_Vocabulary_DateTime_Word, gen_NBVR_Vocabulary_IsVerb_Verb, gen_NBVR_Grammar_GroupPhrase_RolePhrase, gen_NBVR_Grammar_RolePhrase_Vocabulary_FormulationForm, gen_NBVR_Grammar_RolePhrase_Grammar_ParseElement, gen_NBVR_Grammar_Qualifier_ParseElement, gen_NBVR_Grammar_QualifierChain_Qualifier, gen_NBVR_Grammar_Sentence_Vocabulary_FormulationForm, gen_NBVR_Grammar_Sentence_Grammar_ParseElement, gen_NBVR_Grammar_SimpleNounPhrase_RolePhrase, gen_NBVR_Grammar_Condition_ParseElement, gen_NBVR_Grammar_SimpleQualifier_Qualifier, gen_NBVR_Grammar_Quantity_Instance, gen_NBVR_Grammar_Instance_SimpleNounPhrase, gen_NBVR_Grammar_Modifier_ParseElement, gen_NBVR_Grammar_TypeNoun_ModifiedTerm, gen_NBVR_Grammar_ModifiedTerm_SimpleNounPhrase, gen_NBVR_Grammar_Quantifier_ParseElement, gen_NBVR_Grammar_SimpleForm_Sentence, gen_NBVR_Grammar_PropertyNoun_ModifiedTerm, gen_NBVR_Grammar_RoleNoun_SimpleNounPhrase, gen_NBVR_Grammar_CompoundForm_Sentence, gen_NBVR_Grammar_LexicalInstance_Instance, gen_NBVR_Grammar_Nominalization_Instance, gen_NBVR_Grammar_Statement_Nominalization, gen_NBVR_Grammar_Question_Nominalization, gen_NBVR_Grammar_ImplicationForm_Sentence, gen_NBVR_Grammar_ProperName_Instance, gen_NBVR_Grammar_Pronoun_ModifiedTerm, gen_NBVR_Grammar_Intension_Instance, gen_NBVR_Grammar_DomainForm_Sentence, gen_NBVR_Grammar_QueryPhrase_RolePhrase, gen_NBVR_Grammar_LocalName_SimpleNounPhrase, gen_NBVR_Logic_Relation_Proposition, gen_NBVR_Logic_Quantification_Proposition, gen_NBVR_Logic_Proposition_FormulationForm, gen_NBVR_Logic_ExtentConstant_Constant, gen_NBVR_Logic_Connection_Proposition, gen_NBVR_Logic_Implication_Proposition, gen_NBVR_Logic_NominalConstant_Constant, gen_NBVR_Logic_QuantityValue_Constant, gen_NBVR_Logic_Modal_Proposition, gen_NBVR_Logic_Negation_Proposition, gen_NBVR_Logic_RoleVariable_Variable, gen_NBVR_Logic_ValueConstant_Constant},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)