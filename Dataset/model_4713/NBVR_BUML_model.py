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
            EnumerationLiteral(name="K_Something"),
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
			EnumerationLiteral(name="K_Anything"),
			EnumerationLiteral(name="Pronoun"),
			EnumerationLiteral(name="K_Nothing"),
			EnumerationLiteral(name="Genitive"),
			EnumerationLiteral(name="K_Whether"),
			EnumerationLiteral(name="K_Self"),
			EnumerationLiteral(name="K_What"),
			EnumerationLiteral(name="K_Everything"),
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
			EnumerationLiteral(name="Q_Any"),
			EnumerationLiteral(name="Q_All"),
			EnumerationLiteral(name="AtLeast1"),
			EnumerationLiteral(name="Q_No"),
			EnumerationLiteral(name="AtMost1"),
			EnumerationLiteral(name="Exactly1"),
			EnumerationLiteral(name="AtLeastN"),
			EnumerationLiteral(name="AtMostN"),
			EnumerationLiteral(name="ExactlyN"),
			EnumerationLiteral(name="LessThanN"),
			EnumerationLiteral(name="MoreThanN")
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
            EnumerationLiteral(name="None_"),
			EnumerationLiteral(name="Negation"),
			EnumerationLiteral(name="Obligation"),
			EnumerationLiteral(name="Prohibition"),
			EnumerationLiteral(name="Permission"),
			EnumerationLiteral(name="PermittedNot"),
			EnumerationLiteral(name="Possibility"),
			EnumerationLiteral(name="Impossibility"),
			EnumerationLiteral(name="Preference"),
			EnumerationLiteral(name="Antipreference"),
			EnumerationLiteral(name="Nonpreference")
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

SentenceType: Enumeration = Enumeration(
    name="SentenceType",
    literals={
            EnumerationLiteral(name="Compound"),
			EnumerationLiteral(name="Implication"),
			EnumerationLiteral(name="Equivalence"),
			EnumerationLiteral(name="Domain"),
			EnumerationLiteral(name="Modal"),
			EnumerationLiteral(name="Other"),
			EnumerationLiteral(name="Simple")
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
            EnumerationLiteral(name="Group"),
			EnumerationLiteral(name="Query"),
			EnumerationLiteral(name="Instance"),
			EnumerationLiteral(name="Property"),
			EnumerationLiteral(name="Pronoun"),
			EnumerationLiteral(name="Role"),
			EnumerationLiteral(name="None_"),
			EnumerationLiteral(name="Sentence"),
			EnumerationLiteral(name="Qualifier"),
			EnumerationLiteral(name="Quantifier"),
			EnumerationLiteral(name="Condition"),
			EnumerationLiteral(name="Modifier"),
			EnumerationLiteral(name="Noun")
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
NBVR_Vocabulary_Adjective = Class(name="NBVR_Vocabulary_Adjective")
Word = Class(name="Word")
NBVR_Vocabulary_Word = Class(name="NBVR_Vocabulary_Word", is_abstract=True)
WordForm = Class(name="WordForm")
Term = Class(name="Term")
NBVR_Vocabulary_WordForm = Class(name="NBVR_Vocabulary_WordForm")
ParseElement = Class(name="ParseElement")
NBVR_Vocabulary_Term = Class(name="NBVR_Vocabulary_Term")
VocabularyItem = Class(name="VocabularyItem")
VerbRole = Class(name="VerbRole")
Particle = Class(name="Particle")
ItemElement = Class(name="ItemElement")
NBVR_Vocabulary_VocabularyItem = Class(name="NBVR_Vocabulary_VocabularyItem", is_abstract=True)
Formulation = Class(name="Formulation")
NBVR_Vocabulary_Formulation = Class(name="NBVR_Vocabulary_Formulation")
FormulationForm = Class(name="FormulationForm")
VocProperty = Class(name="VocProperty")
NBVR_Vocabulary_FormulationForm = Class(name="NBVR_Vocabulary_FormulationForm", is_abstract=True)
NBVR_Vocabulary_VerbRole = Class(name="NBVR_Vocabulary_VerbRole")
VocNoun = Class(name="VocNoun")
VocVerb = Class(name="VocVerb")
NBVR_Vocabulary_VocNoun = Class(name="NBVR_Vocabulary_VocNoun")
Predicate = Class(name="Predicate")
NBVR_Vocabulary_VocVerb = Class(name="NBVR_Vocabulary_VocVerb")
SyntaxForm = Class(name="SyntaxForm")
NBVR_Vocabulary_SyntaxForm = Class(name="NBVR_Vocabulary_SyntaxForm")
FormElement = Class(name="FormElement")
NBVR_Vocabulary_FormElement = Class(name="NBVR_Vocabulary_FormElement", is_abstract=True)
NBVR_Vocabulary_VocProperty = Class(name="NBVR_Vocabulary_VocProperty")
NBVR_Vocabulary_NumberWord = Class(name="NBVR_Vocabulary_NumberWord")
NBVR_Vocabulary_VocUnit = Class(name="NBVR_Vocabulary_VocUnit")
VocName = Class(name="VocName")
NBVR_Vocabulary_VocName = Class(name="NBVR_Vocabulary_VocName")
NBVR_Vocabulary_VocAdjective = Class(name="NBVR_Vocabulary_VocAdjective")
NBVR_Vocabulary_Noun = Class(name="NBVR_Vocabulary_Noun")
NBVR_Vocabulary_Particle = Class(name="NBVR_Vocabulary_Particle")
RoleElement = Class(name="RoleElement")
NBVR_Vocabulary_RoleElement = Class(name="NBVR_Vocabulary_RoleElement")
NBVR_Vocabulary_Keyword = Class(name="NBVR_Vocabulary_Keyword")
NBVR_Vocabulary_ItemElement = Class(name="NBVR_Vocabulary_ItemElement")
NBVR_Vocabulary_Adjunct = Class(name="NBVR_Vocabulary_Adjunct")
NBVR_Vocabulary_StringWord = Class(name="NBVR_Vocabulary_StringWord")
NBVR_Vocabulary_Definition = Class(name="NBVR_Vocabulary_Definition")
NBVR_Vocabulary_Name = Class(name="NBVR_Vocabulary_Name")
NBVR_Vocabulary_Verb = Class(name="NBVR_Vocabulary_Verb")
NBVR_Vocabulary_Dictionary = Class(name="NBVR_Vocabulary_Dictionary")
NBVR_Vocabulary_DateTime = Class(name="NBVR_Vocabulary_DateTime")
NBVR_Vocabulary_Terminology = Class(name="NBVR_Vocabulary_Terminology")
NBVR_Vocabulary_IsVerb = Class(name="NBVR_Vocabulary_IsVerb")
Verb = Class(name="Verb")
NBVR_Grammar_GroupPhrase = Class(name="NBVR_Grammar_GroupPhrase")
RolePhrase = Class(name="RolePhrase")
SimpleNounPhrase = Class(name="SimpleNounPhrase")
NBVR_Grammar_RolePhrase = Class(name="NBVR_Grammar_RolePhrase", is_abstract=True)
Vocabulary_FormulationForm = Class(name="Vocabulary_FormulationForm")
Grammar_ParseElement = Class(name="Grammar_ParseElement")
Variable = Class(name="Variable")
NBVR_Grammar_SimpleNounPhrase = Class(name="NBVR_Grammar_SimpleNounPhrase", is_abstract=True)
NBVR_Grammar_TypeNoun = Class(name="NBVR_Grammar_TypeNoun")
ModifiedTerm = Class(name="ModifiedTerm")
NBVR_Grammar_Condition = Class(name="NBVR_Grammar_Condition")
SimpleQualifier = Class(name="SimpleQualifier")
Sentence = Class(name="Sentence")
NBVR_Grammar_SimpleQualifier = Class(name="NBVR_Grammar_SimpleQualifier")
Qualifier = Class(name="Qualifier")
QualifierChain = Class(name="QualifierChain")
Condition = Class(name="Condition")
NBVR_Grammar_Qualifier = Class(name="NBVR_Grammar_Qualifier", is_abstract=True)
NBVR_Grammar_QualifierChain = Class(name="NBVR_Grammar_QualifierChain")
NBVR_Grammar_Sentence = Class(name="NBVR_Grammar_Sentence", is_abstract=True)
NBVR_Grammar_PropertyNoun = Class(name="NBVR_Grammar_PropertyNoun")
NBVR_Grammar_ModifiedTerm = Class(name="NBVR_Grammar_ModifiedTerm", is_abstract=True)
Quantifier = Class(name="Quantifier")
Modifier = Class(name="Modifier")
NBVR_Grammar_Quantifier = Class(name="NBVR_Grammar_Quantifier")
Quantity = Class(name="Quantity")
NBVR_Grammar_Quantity = Class(name="NBVR_Grammar_Quantity")
Instance = Class(name="Instance")
NumberWord = Class(name="NumberWord")
Dimension = Class(name="Dimension")
NBVR_Grammar_Instance = Class(name="NBVR_Grammar_Instance", is_abstract=True)
NBVR_Grammar_Dimension = Class(name="NBVR_Grammar_Dimension")
VocUnit = Class(name="VocUnit")
NBVR_Grammar_Modifier = Class(name="NBVR_Grammar_Modifier")
VocAdjective = Class(name="VocAdjective")
TypeNoun = Class(name="TypeNoun")
NBVR_Grammar_RoleNoun = Class(name="NBVR_Grammar_RoleNoun")
NBVR_Grammar_VerbPhrase = Class(name="NBVR_Grammar_VerbPhrase")
NBVR_Grammar_PartPhrase = Class(name="NBVR_Grammar_PartPhrase")
NBVR_Grammar_SimpleForm = Class(name="NBVR_Grammar_SimpleForm")
VerbPhrase = Class(name="VerbPhrase")
PartPhrase = Class(name="PartPhrase")
NBVR_Grammar_ImplicationForm = Class(name="NBVR_Grammar_ImplicationForm")
NBVR_Grammar_CompoundForm = Class(name="NBVR_Grammar_CompoundForm")
NBVR_Grammar_LexicalInstance = Class(name="NBVR_Grammar_LexicalInstance")
NBVR_Grammar_Nominalization = Class(name="NBVR_Grammar_Nominalization", is_abstract=True)
NBVR_Grammar_Statement = Class(name="NBVR_Grammar_Statement")
Nominalization = Class(name="Nominalization")
NBVR_Grammar_Question = Class(name="NBVR_Grammar_Question")
QueryPhrase = Class(name="QueryPhrase")
NBVR_Grammar_QueryPhrase = Class(name="NBVR_Grammar_QueryPhrase")
NBVR_Grammar_ParseElement = Class(name="NBVR_Grammar_ParseElement", is_abstract=True)
Question = Class(name="Question")
NBVR_Grammar_ProperName = Class(name="NBVR_Grammar_ProperName")
NBVR_Grammar_Pronoun = Class(name="NBVR_Grammar_Pronoun")
Keyword = Class(name="Keyword")
NBVR_Grammar_Intension = Class(name="NBVR_Grammar_Intension")
NBVR_Grammar_Parse = Class(name="NBVR_Grammar_Parse")
NBVR_Grammar_DomainForm = Class(name="NBVR_Grammar_DomainForm")
NBVR_Grammar_LocalName = Class(name="NBVR_Grammar_LocalName")
LocalName = Class(name="LocalName")
NBVR_Logic_Variable = Class(name="NBVR_Logic_Variable")
Quantification = Class(name="Quantification")
Proposition = Class(name="Proposition")
Relation = Class(name="Relation")
Set = Class(name="Set")
NBVR_Logic_Quantification = Class(name="NBVR_Logic_Quantification")
NBVR_Logic_Proposition = Class(name="NBVR_Logic_Proposition", is_abstract=True)
NBVR_Logic_Implication = Class(name="NBVR_Logic_Implication")
NBVR_Logic_Relation = Class(name="NBVR_Logic_Relation")
Argument = Class(name="Argument")
NBVR_Logic_Argument = Class(name="NBVR_Logic_Argument")
Constant = Class(name="Constant")
NBVR_Logic_Constant = Class(name="NBVR_Logic_Constant", is_abstract=True)
NBVR_Logic_Set = Class(name="NBVR_Logic_Set")
ExtentConstant = Class(name="ExtentConstant")
NBVR_Logic_ExtentConstant = Class(name="NBVR_Logic_ExtentConstant")
NBVR_Logic_Connection = Class(name="NBVR_Logic_Connection")
RoleVariable = Class(name="RoleVariable")
NBVR_Logic_Modal = Class(name="NBVR_Logic_Modal")
NBVR_Logic_Negation = Class(name="NBVR_Logic_Negation")
NBVR_Logic_RoleVariable = Class(name="NBVR_Logic_RoleVariable")
NBVR_Logic_ValueConstant = Class(name="NBVR_Logic_ValueConstant")
NBVR_Logic_NominalConstant = Class(name="NBVR_Logic_NominalConstant")
NBVR_Logic_QuantityValue = Class(name="NBVR_Logic_QuantityValue")
NBVR_Logic_Predicate = Class(name="NBVR_Logic_Predicate")

# NBVR_Vocabulary_Adjective class attributes and methods

# Word class attributes and methods

# NBVR_Vocabulary_Word class attributes and methods
NBVR_Vocabulary_Word_m_isArticle: Method = Method(name="isArticle", parameters={}, type=BooleanType)
NBVR_Vocabulary_Word_m_isNumber: Method = Method(name="isNumber", parameters={}, type=BooleanType)
NBVR_Vocabulary_Word_m_isText: Method = Method(name="isText", parameters={}, type=BooleanType)
NBVR_Vocabulary_Word_m_isKeyword: Method = Method(name="isKeyword", parameters={Parameter(name='NBVR_kind', type=StringType)}, type=BooleanType)
NBVR_Vocabulary_Word_m_isKeyword: Method = Method(name="isKeyword", parameters={}, type=BooleanType)
NBVR_Vocabulary_Word_m_isIs: Method = Method(name="isIs", parameters={}, type=BooleanType)
NBVR_Vocabulary_Word.methods={NBVR_Vocabulary_Word_m_isKeyword, NBVR_Vocabulary_Word_m_isKeyword, NBVR_Vocabulary_Word_m_isIs, NBVR_Vocabulary_Word_m_isNumber, NBVR_Vocabulary_Word_m_isArticle, NBVR_Vocabulary_Word_m_isText}

# WordForm class attributes and methods

# Term class attributes and methods

# NBVR_Vocabulary_WordForm class attributes and methods
NBVR_Vocabulary_WordForm_text: Property = Property(name="text", type=StringType)
NBVR_Vocabulary_WordForm.attributes={NBVR_Vocabulary_WordForm_text}

# ParseElement class attributes and methods

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
NBVR_Vocabulary_VocabularyItem.methods={NBVR_Vocabulary_VocabularyItem_m_isPrimitive, NBVR_Vocabulary_VocabularyItem_m_getKind}

# Formulation class attributes and methods

# NBVR_Vocabulary_Formulation class attributes and methods
NBVR_Vocabulary_Formulation_text: Property = Property(name="text", type=StringType)
NBVR_Vocabulary_Formulation_language: Property = Property(name="language", type=StringType)
NBVR_Vocabulary_Formulation_m_isStructured: Method = Method(name="isStructured", parameters={}, type=BooleanType)
NBVR_Vocabulary_Formulation_m_addElement: Method = Method(name="addElement", parameters={Parameter(name='NBVR_elt', type=StringType)})
NBVR_Vocabulary_Formulation.attributes={NBVR_Vocabulary_Formulation_language, NBVR_Vocabulary_Formulation_text}
NBVR_Vocabulary_Formulation.methods={NBVR_Vocabulary_Formulation_m_addElement, NBVR_Vocabulary_Formulation_m_isStructured}

# FormulationForm class attributes and methods

# VocProperty class attributes and methods

# NBVR_Vocabulary_FormulationForm class attributes and methods
NBVR_Vocabulary_FormulationForm_m_isStructured: Method = Method(name="isStructured", parameters={}, type=BooleanType)
NBVR_Vocabulary_FormulationForm.methods={NBVR_Vocabulary_FormulationForm_m_isStructured}

# NBVR_Vocabulary_VerbRole class attributes and methods
NBVR_Vocabulary_VerbRole_isRange: Property = Property(name="isRange", type=BooleanType)
NBVR_Vocabulary_VerbRole.attributes={NBVR_Vocabulary_VerbRole_isRange}

# VocNoun class attributes and methods

# VocVerb class attributes and methods

# NBVR_Vocabulary_VocNoun class attributes and methods
NBVR_Vocabulary_VocNoun_massNoun: Property = Property(name="massNoun", type=BooleanType)
NBVR_Vocabulary_VocNoun.attributes={NBVR_Vocabulary_VocNoun_massNoun}

# Predicate class attributes and methods

# NBVR_Vocabulary_VocVerb class attributes and methods
NBVR_Vocabulary_VocVerb_arity: Property = Property(name="arity", type=IntegerType)
NBVR_Vocabulary_VocVerb.attributes={NBVR_Vocabulary_VocVerb_arity}

# SyntaxForm class attributes and methods

# NBVR_Vocabulary_SyntaxForm class attributes and methods
NBVR_Vocabulary_SyntaxForm_text: Property = Property(name="text", type=StringType)
NBVR_Vocabulary_SyntaxForm_isAuxForm: Property = Property(name="isAuxForm", type=BooleanType)
NBVR_Vocabulary_SyntaxForm.attributes={NBVR_Vocabulary_SyntaxForm_text, NBVR_Vocabulary_SyntaxForm_isAuxForm}

# FormElement class attributes and methods

# NBVR_Vocabulary_FormElement class attributes and methods
NBVR_Vocabulary_FormElement_kind: Property = Property(name="kind", type=StringType)
NBVR_Vocabulary_FormElement.attributes={NBVR_Vocabulary_FormElement_kind}

# NBVR_Vocabulary_VocProperty class attributes and methods

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

# NBVR_Vocabulary_Noun class attributes and methods

# NBVR_Vocabulary_Particle class attributes and methods

# RoleElement class attributes and methods

# NBVR_Vocabulary_RoleElement class attributes and methods
NBVR_Vocabulary_RoleElement_slot: Property = Property(name="slot", type=IntegerType)
NBVR_Vocabulary_RoleElement.attributes={NBVR_Vocabulary_RoleElement_slot}

# NBVR_Vocabulary_Keyword class attributes and methods
NBVR_Vocabulary_Keyword_kind: Property = Property(name="kind", type=StringType)
NBVR_Vocabulary_Keyword.attributes={NBVR_Vocabulary_Keyword_kind}

# NBVR_Vocabulary_ItemElement class attributes and methods

# NBVR_Vocabulary_Adjunct class attributes and methods

# NBVR_Vocabulary_StringWord class attributes and methods

# NBVR_Vocabulary_Definition class attributes and methods

# NBVR_Vocabulary_Name class attributes and methods

# NBVR_Vocabulary_Verb class attributes and methods
NBVR_Vocabulary_Verb_m_isProgressive: Method = Method(name="isProgressive", parameters={Parameter(name='NBVR_wf', type=StringType)}, type=BooleanType)
NBVR_Vocabulary_Verb_m_isPast: Method = Method(name="isPast", parameters={Parameter(name='NBVR_wf', type=StringType)}, type=BooleanType)
NBVR_Vocabulary_Verb_m_isPerfective: Method = Method(name="isPerfective", parameters={Parameter(name='NBVR_wf', type=StringType)}, type=BooleanType)
NBVR_Vocabulary_Verb.methods={NBVR_Vocabulary_Verb_m_isPast, NBVR_Vocabulary_Verb_m_isPerfective, NBVR_Vocabulary_Verb_m_isProgressive}

# NBVR_Vocabulary_Dictionary class attributes and methods

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

# Variable class attributes and methods

# NBVR_Grammar_SimpleNounPhrase class attributes and methods

# NBVR_Grammar_TypeNoun class attributes and methods

# ModifiedTerm class attributes and methods

# NBVR_Grammar_Condition class attributes and methods
NBVR_Grammar_Condition_otherwise: Property = Property(name="otherwise", type=BooleanType)
NBVR_Grammar_Condition.attributes={NBVR_Grammar_Condition_otherwise}

# SimpleQualifier class attributes and methods

# Sentence class attributes and methods

# NBVR_Grammar_SimpleQualifier class attributes and methods

# Qualifier class attributes and methods

# QualifierChain class attributes and methods

# Condition class attributes and methods

# NBVR_Grammar_Qualifier class attributes and methods
NBVR_Grammar_Qualifier_m_isSimple: Method = Method(name="isSimple", parameters={}, type=BooleanType)
NBVR_Grammar_Qualifier.methods={NBVR_Grammar_Qualifier_m_isSimple}

# NBVR_Grammar_QualifierChain class attributes and methods

# NBVR_Grammar_Sentence class attributes and methods
NBVR_Grammar_Sentence_m_getType: Method = Method(name="getType", parameters={}, type=StringType)
NBVR_Grammar_Sentence.methods={NBVR_Grammar_Sentence_m_getType}

# NBVR_Grammar_PropertyNoun class attributes and methods

# NBVR_Grammar_ModifiedTerm class attributes and methods

# Quantifier class attributes and methods

# Modifier class attributes and methods

# NBVR_Grammar_Quantifier class attributes and methods
NBVR_Grammar_Quantifier_kind: Property = Property(name="kind", type=StringType)
NBVR_Grammar_Quantifier_count: Property = Property(name="count", type=IntegerType)
NBVR_Grammar_Quantifier.attributes={NBVR_Grammar_Quantifier_kind, NBVR_Grammar_Quantifier_count}

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

# TypeNoun class attributes and methods

# NBVR_Grammar_RoleNoun class attributes and methods

# NBVR_Grammar_VerbPhrase class attributes and methods
NBVR_Grammar_VerbPhrase_modality: Property = Property(name="modality", type=StringType)
NBVR_Grammar_VerbPhrase_negated: Property = Property(name="negated", type=BooleanType)
NBVR_Grammar_VerbPhrase.attributes={NBVR_Grammar_VerbPhrase_negated, NBVR_Grammar_VerbPhrase_modality}

# NBVR_Grammar_PartPhrase class attributes and methods

# NBVR_Grammar_SimpleForm class attributes and methods
NBVR_Grammar_SimpleForm_m_getModality: Method = Method(name="getModality", parameters={}, type=StringType)
NBVR_Grammar_SimpleForm_m_isNegated: Method = Method(name="isNegated", parameters={}, type=BooleanType)
NBVR_Grammar_SimpleForm.methods={NBVR_Grammar_SimpleForm_m_isNegated, NBVR_Grammar_SimpleForm_m_getModality}

# VerbPhrase class attributes and methods

# PartPhrase class attributes and methods

# NBVR_Grammar_ImplicationForm class attributes and methods
NBVR_Grammar_ImplicationForm_kind: Property = Property(name="kind", type=StringType)
NBVR_Grammar_ImplicationForm.attributes={NBVR_Grammar_ImplicationForm_kind}

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

# NBVR_Grammar_QueryPhrase class attributes and methods
NBVR_Grammar_QueryPhrase_query: Property = Property(name="query", type=StringType)
NBVR_Grammar_QueryPhrase.attributes={NBVR_Grammar_QueryPhrase_query}

# NBVR_Grammar_ParseElement class attributes and methods
NBVR_Grammar_ParseElement_m_getElementKind: Method = Method(name="getElementKind", parameters={}, type=StringType)
NBVR_Grammar_ParseElement_m_isSentence: Method = Method(name="isSentence", parameters={}, type=BooleanType)
NBVR_Grammar_ParseElement_m_isInstance: Method = Method(name="isInstance", parameters={}, type=BooleanType)
NBVR_Grammar_ParseElement_m_isRolePhrase: Method = Method(name="isRolePhrase", parameters={}, type=BooleanType)
NBVR_Grammar_ParseElement.methods={NBVR_Grammar_ParseElement_m_isRolePhrase, NBVR_Grammar_ParseElement_m_getElementKind, NBVR_Grammar_ParseElement_m_isSentence, NBVR_Grammar_ParseElement_m_isInstance}

# Question class attributes and methods

# NBVR_Grammar_ProperName class attributes and methods

# NBVR_Grammar_Pronoun class attributes and methods

# Keyword class attributes and methods

# NBVR_Grammar_Intension class attributes and methods

# NBVR_Grammar_Parse class attributes and methods

# NBVR_Grammar_DomainForm class attributes and methods
NBVR_Grammar_DomainForm_modality: Property = Property(name="modality", type=StringType)
NBVR_Grammar_DomainForm.attributes={NBVR_Grammar_DomainForm_modality}

# NBVR_Grammar_LocalName class attributes and methods

# LocalName class attributes and methods

# NBVR_Logic_Variable class attributes and methods
NBVR_Logic_Variable_name: Property = Property(name="name", type=StringType)
NBVR_Logic_Variable.attributes={NBVR_Logic_Variable_name}

# Quantification class attributes and methods

# Proposition class attributes and methods

# Relation class attributes and methods

# Set class attributes and methods

# NBVR_Logic_Quantification class attributes and methods
NBVR_Logic_Quantification_kind: Property = Property(name="kind", type=StringType)
NBVR_Logic_Quantification_unique: Property = Property(name="unique", type=BooleanType)
NBVR_Logic_Quantification.attributes={NBVR_Logic_Quantification_kind, NBVR_Logic_Quantification_unique}

# NBVR_Logic_Proposition class attributes and methods
NBVR_Logic_Proposition_text: Property = Property(name="text", type=StringType)
NBVR_Logic_Proposition_m_getType: Method = Method(name="getType", parameters={}, type=StringType)
NBVR_Logic_Proposition.attributes={NBVR_Logic_Proposition_text}
NBVR_Logic_Proposition.methods={NBVR_Logic_Proposition_m_getType}

# NBVR_Logic_Implication class attributes and methods

# NBVR_Logic_Relation class attributes and methods
NBVR_Logic_Relation_m_getArgument: Method = Method(name="getArgument", parameters={}, type=StringType)
NBVR_Logic_Relation.methods={NBVR_Logic_Relation_m_getArgument}

# Argument class attributes and methods

# NBVR_Logic_Argument class attributes and methods
NBVR_Logic_Argument_m_hasNext: Method = Method(name="hasNext", parameters={}, type=BooleanType)
NBVR_Logic_Argument.methods={NBVR_Logic_Argument_m_hasNext}

# Constant class attributes and methods

# NBVR_Logic_Constant class attributes and methods
NBVR_Logic_Constant_kind: Property = Property(name="kind", type=StringType)
NBVR_Logic_Constant.attributes={NBVR_Logic_Constant_kind}

# NBVR_Logic_Set class attributes and methods

# ExtentConstant class attributes and methods

# NBVR_Logic_ExtentConstant class attributes and methods

# NBVR_Logic_Connection class attributes and methods
NBVR_Logic_Connection_kind: Property = Property(name="kind", type=StringType)
NBVR_Logic_Connection.attributes={NBVR_Logic_Connection_kind}

# RoleVariable class attributes and methods

# NBVR_Logic_Modal class attributes and methods
NBVR_Logic_Modal_kind: Property = Property(name="kind", type=StringType)
NBVR_Logic_Modal.attributes={NBVR_Logic_Modal_kind}

# NBVR_Logic_Negation class attributes and methods

# NBVR_Logic_RoleVariable class attributes and methods

# NBVR_Logic_ValueConstant class attributes and methods
NBVR_Logic_ValueConstant_name: Property = Property(name="name", type=StringType)
NBVR_Logic_ValueConstant.attributes={NBVR_Logic_ValueConstant_name}

# NBVR_Logic_NominalConstant class attributes and methods

# NBVR_Logic_QuantityValue class attributes and methods
NBVR_Logic_QuantityValue_factor: Property = Property(name="factor", type=StringType)
NBVR_Logic_QuantityValue_unit: Property = Property(name="unit", type=StringType)
NBVR_Logic_QuantityValue.attributes={NBVR_Logic_QuantityValue_factor, NBVR_Logic_QuantityValue_unit}

# NBVR_Logic_Predicate class attributes and methods
NBVR_Logic_Predicate_name: Property = Property(name="name", type=StringType)
NBVR_Logic_Predicate.attributes={NBVR_Logic_Predicate_name}

# Relationships
word7: BinaryAssociation = BinaryAssociation(
    name="word7",
    ends={
        Property(name="Word9", type=NBVR_Vocabulary_WordForm, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_WordForm8", type=Word, multiplicity=Multiplicity(1, 1))
    }
)
altWord10: BinaryAssociation = BinaryAssociation(
    name="altWord10",
    ends={
        Property(name="Word12", type=NBVR_Vocabulary_WordForm, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_WordForm11", type=Word, multiplicity=Multiplicity(0, 1))
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
elements34: BinaryAssociation = BinaryAssociation(
    name="elements34",
    ends={
        Property(name="ParseElement", type=NBVR_Vocabulary_Formulation, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_Formulation", type=ParseElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
concept35: BinaryAssociation = BinaryAssociation(
    name="concept35",
    ends={
        Property(name="VocabularyItem36", type=NBVR_Vocabulary_Formulation, multiplicity=Multiplicity(1, 1)),
        Property(name="formulations", type=VocabularyItem, multiplicity=Multiplicity(1, 1))
    }
)
concept13: BinaryAssociation = BinaryAssociation(
    name="concept13",
    ends={
        Property(name="VocabularyItem", type=NBVR_Vocabulary_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="terms", type=VocabularyItem, multiplicity=Multiplicity(0, 1))
    }
)
role14: BinaryAssociation = BinaryAssociation(
    name="role14",
    ends={
        Property(name="VerbRole", type=NBVR_Vocabulary_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="term", type=VerbRole, multiplicity=Multiplicity(0, 1))
    }
)
particle15: BinaryAssociation = BinaryAssociation(
    name="particle15",
    ends={
        Property(name="Particle", type=NBVR_Vocabulary_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="term16", type=Particle, multiplicity=Multiplicity(0, 1))
    }
)
words17: BinaryAssociation = BinaryAssociation(
    name="words17",
    ends={
        Property(name="Word18", type=NBVR_Vocabulary_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_Term", type=Word, multiplicity=Multiplicity(1, 9999))
    }
)
context19: BinaryAssociation = BinaryAssociation(
    name="context19",
    ends={
        Property(name="VocabularyItem21", type=NBVR_Vocabulary_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_Term20", type=VocabularyItem, multiplicity=Multiplicity(0, 1))
    }
)
element22: BinaryAssociation = BinaryAssociation(
    name="element22",
    ends={
        Property(name="ItemElement", type=NBVR_Vocabulary_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="term23", type=ItemElement, multiplicity=Multiplicity(0, 9999))
    }
)
formulations24: BinaryAssociation = BinaryAssociation(
    name="formulations24",
    ends={
        Property(name="Formulation", type=NBVR_Vocabulary_VocabularyItem, multiplicity=Multiplicity(1, 1)),
        Property(name="concept", type=Formulation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
base25: BinaryAssociation = BinaryAssociation(
    name="base25",
    ends={
        Property(name="VocabularyItem26", type=NBVR_Vocabulary_VocabularyItem, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_VocabularyItem", type=VocabularyItem, multiplicity=Multiplicity(0, 9999))
    }
)
next27: BinaryAssociation = BinaryAssociation(
    name="next27",
    ends={
        Property(name="VocabularyItem29", type=NBVR_Vocabulary_VocabularyItem, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_VocabularyItem28", type=VocabularyItem, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
terms30: BinaryAssociation = BinaryAssociation(
    name="terms30",
    ends={
        Property(name="Term32", type=NBVR_Vocabulary_VocabularyItem, multiplicity=Multiplicity(1, 1)),
        Property(name="concept31", type=Term, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
form33: BinaryAssociation = BinaryAssociation(
    name="form33",
    ends={
        Property(name="FormulationForm", type=NBVR_Vocabulary_Formulation, multiplicity=Multiplicity(1, 1)),
        Property(name="formulation", type=FormulationForm, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
property55: BinaryAssociation = BinaryAssociation(
    name="property55",
    ends={
        Property(name="VocProperty", type=NBVR_Vocabulary_SyntaxForm, multiplicity=Multiplicity(1, 1)),
        Property(name="propertyForm", type=VocProperty, multiplicity=Multiplicity(0, 1))
    }
)
formulation37: BinaryAssociation = BinaryAssociation(
    name="formulation37",
    ends={
        Property(name="Formulation38", type=NBVR_Vocabulary_FormulationForm, multiplicity=Multiplicity(1, 1)),
        Property(name="form", type=Formulation, multiplicity=Multiplicity(0, 1))
    }
)
range39: BinaryAssociation = BinaryAssociation(
    name="range39",
    ends={
        Property(name="VocNoun", type=NBVR_Vocabulary_VerbRole, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_VerbRole", type=VocNoun, multiplicity=Multiplicity(1, 1))
    }
)
verb40: BinaryAssociation = BinaryAssociation(
    name="verb40",
    ends={
        Property(name="VocVerb", type=NBVR_Vocabulary_VerbRole, multiplicity=Multiplicity(1, 1)),
        Property(name="roles", type=VocVerb, multiplicity=Multiplicity(1, 1))
    }
)
term41: BinaryAssociation = BinaryAssociation(
    name="term41",
    ends={
        Property(name="Term42", type=NBVR_Vocabulary_VerbRole, multiplicity=Multiplicity(1, 1)),
        Property(name="role", type=Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
isAVerb43: BinaryAssociation = BinaryAssociation(
    name="isAVerb43",
    ends={
        Property(name="VocVerb44", type=NBVR_Vocabulary_VocNoun, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_VocNoun", type=VocVerb, multiplicity=Multiplicity(0, 1))
    }
)
predicate45: BinaryAssociation = BinaryAssociation(
    name="predicate45",
    ends={
        Property(name="Predicate", type=NBVR_Vocabulary_VocNoun, multiplicity=Multiplicity(1, 1)),
        Property(name="noun", type=Predicate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
roles46: BinaryAssociation = BinaryAssociation(
    name="roles46",
    ends={
        Property(name="VerbRole47", type=NBVR_Vocabulary_VocVerb, multiplicity=Multiplicity(1, 1)),
        Property(name="verb", type=VerbRole, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
form48: BinaryAssociation = BinaryAssociation(
    name="form48",
    ends={
        Property(name="SyntaxForm", type=NBVR_Vocabulary_VocVerb, multiplicity=Multiplicity(1, 1)),
        Property(name="verb49", type=SyntaxForm, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
predicate50: BinaryAssociation = BinaryAssociation(
    name="predicate50",
    ends={
        Property(name="Predicate52", type=NBVR_Vocabulary_VocVerb, multiplicity=Multiplicity(1, 1)),
        Property(name="verb51", type=Predicate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements53: BinaryAssociation = BinaryAssociation(
    name="elements53",
    ends={
        Property(name="FormElement", type=NBVR_Vocabulary_SyntaxForm, multiplicity=Multiplicity(1, 1)),
        Property(name="form54", type=FormElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
domain73: BinaryAssociation = BinaryAssociation(
    name="domain73",
    ends={
        Property(name="VocNoun74", type=NBVR_Vocabulary_VocAdjective, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_VocAdjective", type=VocNoun, multiplicity=Multiplicity(0, 1))
    }
)
verb75: BinaryAssociation = BinaryAssociation(
    name="verb75",
    ends={
        Property(name="VocVerb77", type=NBVR_Vocabulary_VocAdjective, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_VocAdjective76", type=VocVerb, multiplicity=Multiplicity(1, 1))
    }
)
verb56: BinaryAssociation = BinaryAssociation(
    name="verb56",
    ends={
        Property(name="VocVerb58", type=NBVR_Vocabulary_SyntaxForm, multiplicity=Multiplicity(1, 1)),
        Property(name="form57", type=VocVerb, multiplicity=Multiplicity(0, 1))
    }
)
form59: BinaryAssociation = BinaryAssociation(
    name="form59",
    ends={
        Property(name="SyntaxForm60", type=NBVR_Vocabulary_FormElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=SyntaxForm, multiplicity=Multiplicity(0, 1))
    }
)
domain61: BinaryAssociation = BinaryAssociation(
    name="domain61",
    ends={
        Property(name="VocNoun62", type=NBVR_Vocabulary_VocProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_VocProperty", type=VocNoun, multiplicity=Multiplicity(1, 1))
    }
)
range63: BinaryAssociation = BinaryAssociation(
    name="range63",
    ends={
        Property(name="VocNoun65", type=NBVR_Vocabulary_VocProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_VocProperty64", type=VocNoun, multiplicity=Multiplicity(1, 1))
    }
)
verb66: BinaryAssociation = BinaryAssociation(
    name="verb66",
    ends={
        Property(name="VocVerb68", type=NBVR_Vocabulary_VocProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_VocProperty67", type=VocVerb, multiplicity=Multiplicity(1, 1))
    }
)
propertyForm69: BinaryAssociation = BinaryAssociation(
    name="propertyForm69",
    ends={
        Property(name="SyntaxForm70", type=NBVR_Vocabulary_VocProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="property", type=SyntaxForm, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
quantityKind71: BinaryAssociation = BinaryAssociation(
    name="quantityKind71",
    ends={
        Property(name="VocProperty72", type=NBVR_Vocabulary_VocUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_VocUnit", type=VocProperty, multiplicity=Multiplicity(0, 1))
    }
)
plural85: BinaryAssociation = BinaryAssociation(
    name="plural85",
    ends={
        Property(name="WordForm86", type=NBVR_Vocabulary_Noun, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_Noun", type=WordForm, multiplicity=Multiplicity(1, 1))
    }
)
role78: BinaryAssociation = BinaryAssociation(
    name="role78",
    ends={
        Property(name="RoleElement", type=NBVR_Vocabulary_Particle, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_Particle", type=RoleElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
term79: BinaryAssociation = BinaryAssociation(
    name="term79",
    ends={
        Property(name="Term80", type=NBVR_Vocabulary_Particle, multiplicity=Multiplicity(1, 1)),
        Property(name="particle", type=Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
role81: BinaryAssociation = BinaryAssociation(
    name="role81",
    ends={
        Property(name="VerbRole82", type=NBVR_Vocabulary_RoleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_RoleElement", type=VerbRole, multiplicity=Multiplicity(1, 1))
    }
)
term83: BinaryAssociation = BinaryAssociation(
    name="term83",
    ends={
        Property(name="Term84", type=NBVR_Vocabulary_ItemElement, multiplicity=Multiplicity(1, 1)),
        Property(name="element", type=Term, multiplicity=Multiplicity(1, 1))
    }
)
altPlural87: BinaryAssociation = BinaryAssociation(
    name="altPlural87",
    ends={
        Property(name="WordForm89", type=NBVR_Vocabulary_Noun, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_Noun88", type=WordForm, multiplicity=Multiplicity(0, 1))
    }
)
singular90: BinaryAssociation = BinaryAssociation(
    name="singular90",
    ends={
        Property(name="WordForm91", type=NBVR_Vocabulary_Verb, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_Verb", type=WordForm, multiplicity=Multiplicity(1, 1))
    }
)
plural92: BinaryAssociation = BinaryAssociation(
    name="plural92",
    ends={
        Property(name="WordForm94", type=NBVR_Vocabulary_Verb, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_Verb93", type=WordForm, multiplicity=Multiplicity(1, 1))
    }
)
past95: BinaryAssociation = BinaryAssociation(
    name="past95",
    ends={
        Property(name="WordForm97", type=NBVR_Vocabulary_Verb, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_Verb96", type=WordForm, multiplicity=Multiplicity(1, 1))
    }
)
progressive98: BinaryAssociation = BinaryAssociation(
    name="progressive98",
    ends={
        Property(name="WordForm100", type=NBVR_Vocabulary_Verb, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_Verb99", type=WordForm, multiplicity=Multiplicity(1, 1))
    }
)
perfective101: BinaryAssociation = BinaryAssociation(
    name="perfective101",
    ends={
        Property(name="WordForm103", type=NBVR_Vocabulary_Verb, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_Verb102", type=WordForm, multiplicity=Multiplicity(1, 1))
    }
)
altPast104: BinaryAssociation = BinaryAssociation(
    name="altPast104",
    ends={
        Property(name="WordForm106", type=NBVR_Vocabulary_Verb, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_Verb105", type=WordForm, multiplicity=Multiplicity(0, 1))
    }
)
firstWord107: BinaryAssociation = BinaryAssociation(
    name="firstWord107",
    ends={
        Property(name="Word108", type=NBVR_Vocabulary_Dictionary, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_Dictionary", type=Word, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
firstItem109: BinaryAssociation = BinaryAssociation(
    name="firstItem109",
    ends={
        Property(name="VocabularyItem110", type=NBVR_Vocabulary_Terminology, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_Terminology", type=VocabularyItem, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lastItem111: BinaryAssociation = BinaryAssociation(
    name="lastItem111",
    ends={
        Property(name="VocabularyItem113", type=NBVR_Vocabulary_Terminology, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Vocabulary_Terminology112", type=VocabularyItem, multiplicity=Multiplicity(0, 1))
    }
)
members114: BinaryAssociation = BinaryAssociation(
    name="members114",
    ends={
        Property(name="SimpleNounPhrase", type=NBVR_Grammar_GroupPhrase, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_GroupPhrase", type=SimpleNounPhrase, multiplicity=Multiplicity(1, 9999))
    }
)
rolePlayed115: BinaryAssociation = BinaryAssociation(
    name="rolePlayed115",
    ends={
        Property(name="VerbRole116", type=NBVR_Grammar_RolePhrase, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_RolePhrase", type=VerbRole, multiplicity=Multiplicity(0, 1))
    }
)
variable117: BinaryAssociation = BinaryAssociation(
    name="variable117",
    ends={
        Property(name="Variable", type=NBVR_Grammar_RolePhrase, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_RolePhrase118", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
referent119: BinaryAssociation = BinaryAssociation(
    name="referent119",
    ends={
        Property(name="RolePhrase", type=NBVR_Grammar_RolePhrase, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_RolePhrase120", type=RolePhrase, multiplicity=Multiplicity(0, 1))
    }
)
qualifier121: BinaryAssociation = BinaryAssociation(
    name="qualifier121",
    ends={
        Property(name="SimpleQualifier", type=NBVR_Grammar_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="condition", type=SimpleQualifier, multiplicity=Multiplicity(1, 1))
    }
)
antecedent122: BinaryAssociation = BinaryAssociation(
    name="antecedent122",
    ends={
        Property(name="Sentence", type=NBVR_Grammar_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_Condition", type=Sentence, multiplicity=Multiplicity(0, 1))
    }
)
chain123: BinaryAssociation = BinaryAssociation(
    name="chain123",
    ends={
        Property(name="QualifierChain", type=NBVR_Grammar_SimpleQualifier, multiplicity=Multiplicity(1, 1)),
        Property(name="qualifiers", type=QualifierChain, multiplicity=Multiplicity(0, 1))
    }
)
boundForm124: BinaryAssociation = BinaryAssociation(
    name="boundForm124",
    ends={
        Property(name="Sentence125", type=NBVR_Grammar_SimpleQualifier, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_SimpleQualifier", type=Sentence, multiplicity=Multiplicity(1, 1))
    }
)
condition126: BinaryAssociation = BinaryAssociation(
    name="condition126",
    ends={
        Property(name="Condition", type=NBVR_Grammar_SimpleQualifier, multiplicity=Multiplicity(1, 1)),
        Property(name="qualifier", type=Condition, multiplicity=Multiplicity(0, 1))
    }
)
qualifiers127: BinaryAssociation = BinaryAssociation(
    name="qualifiers127",
    ends={
        Property(name="SimpleQualifier128", type=NBVR_Grammar_QualifierChain, multiplicity=Multiplicity(1, 1)),
        Property(name="chain", type=SimpleQualifier, multiplicity=Multiplicity(1, 9999))
    }
)
domain129: BinaryAssociation = BinaryAssociation(
    name="domain129",
    ends={
        Property(name="RolePhrase130", type=NBVR_Grammar_Sentence, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_Sentence", type=RolePhrase, multiplicity=Multiplicity(0, 1))
    }
)
rewrites131: BinaryAssociation = BinaryAssociation(
    name="rewrites131",
    ends={
        Property(name="Sentence133", type=NBVR_Grammar_Sentence, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_Sentence132", type=Sentence, multiplicity=Multiplicity(0, 1))
    }
)
relative147: BinaryAssociation = BinaryAssociation(
    name="relative147",
    ends={
        Property(name="RolePhrase149", type=NBVR_Grammar_Modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_Modifier148", type=RolePhrase, multiplicity=Multiplicity(0, 1))
    }
)
noun134: BinaryAssociation = BinaryAssociation(
    name="noun134",
    ends={
        Property(name="VocNoun135", type=NBVR_Grammar_TypeNoun, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_TypeNoun", type=VocNoun, multiplicity=Multiplicity(1, 1))
    }
)
quantifier136: BinaryAssociation = BinaryAssociation(
    name="quantifier136",
    ends={
        Property(name="Quantifier", type=NBVR_Grammar_ModifiedTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_ModifiedTerm", type=Quantifier, multiplicity=Multiplicity(0, 1))
    }
)
modifiers137: BinaryAssociation = BinaryAssociation(
    name="modifiers137",
    ends={
        Property(name="Modifier", type=NBVR_Grammar_ModifiedTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_ModifiedTerm138", type=Modifier, multiplicity=Multiplicity(0, 9999))
    }
)
qualifiers139: BinaryAssociation = BinaryAssociation(
    name="qualifiers139",
    ends={
        Property(name="Qualifier", type=NBVR_Grammar_ModifiedTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_ModifiedTerm140", type=Qualifier, multiplicity=Multiplicity(0, 9999))
    }
)
quantity141: BinaryAssociation = BinaryAssociation(
    name="quantity141",
    ends={
        Property(name="Quantity", type=NBVR_Grammar_Quantifier, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_Quantifier", type=Quantity, multiplicity=Multiplicity(0, 1))
    }
)
factor142: BinaryAssociation = BinaryAssociation(
    name="factor142",
    ends={
        Property(name="NumberWord", type=NBVR_Grammar_Quantity, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_Quantity", type=NumberWord, multiplicity=Multiplicity(1, 1))
    }
)
dimension143: BinaryAssociation = BinaryAssociation(
    name="dimension143",
    ends={
        Property(name="Dimension", type=NBVR_Grammar_Quantity, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_Quantity144", type=Dimension, multiplicity=Multiplicity(0, 9999))
    }
)
unit145: BinaryAssociation = BinaryAssociation(
    name="unit145",
    ends={
        Property(name="VocUnit", type=NBVR_Grammar_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_Dimension", type=VocUnit, multiplicity=Multiplicity(1, 1))
    }
)
adjective146: BinaryAssociation = BinaryAssociation(
    name="adjective146",
    ends={
        Property(name="VocAdjective", type=NBVR_Grammar_Modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_Modifier", type=VocAdjective, multiplicity=Multiplicity(0, 1))
    }
)
antecedent175: BinaryAssociation = BinaryAssociation(
    name="antecedent175",
    ends={
        Property(name="Sentence176", type=NBVR_Grammar_ImplicationForm, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_ImplicationForm", type=Sentence, multiplicity=Multiplicity(1, 1))
    }
)
consequent177: BinaryAssociation = BinaryAssociation(
    name="consequent177",
    ends={
        Property(name="Sentence179", type=NBVR_Grammar_ImplicationForm, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_ImplicationForm178", type=Sentence, multiplicity=Multiplicity(1, 1))
    }
)
property150: BinaryAssociation = BinaryAssociation(
    name="property150",
    ends={
        Property(name="VocProperty151", type=NBVR_Grammar_PropertyNoun, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_PropertyNoun", type=VocProperty, multiplicity=Multiplicity(1, 1))
    }
)
domain152: BinaryAssociation = BinaryAssociation(
    name="domain152",
    ends={
        Property(name="SimpleNounPhrase154", type=NBVR_Grammar_PropertyNoun, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_PropertyNoun153", type=SimpleNounPhrase, multiplicity=Multiplicity(1, 1))
    }
)
expansion155: BinaryAssociation = BinaryAssociation(
    name="expansion155",
    ends={
        Property(name="TypeNoun", type=NBVR_Grammar_PropertyNoun, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_PropertyNoun156", type=TypeNoun, multiplicity=Multiplicity(0, 1))
    }
)
role157: BinaryAssociation = BinaryAssociation(
    name="role157",
    ends={
        Property(name="VerbRole158", type=NBVR_Grammar_RoleNoun, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_RoleNoun", type=VerbRole, multiplicity=Multiplicity(0, 1))
    }
)
verb159: BinaryAssociation = BinaryAssociation(
    name="verb159",
    ends={
        Property(name="VocVerb160", type=NBVR_Grammar_VerbPhrase, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_VerbPhrase", type=VocVerb, multiplicity=Multiplicity(1, 1))
    }
)
partRole161: BinaryAssociation = BinaryAssociation(
    name="partRole161",
    ends={
        Property(name="RolePhrase162", type=NBVR_Grammar_PartPhrase, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_PartPhrase", type=RolePhrase, multiplicity=Multiplicity(0, 1))
    }
)
particle163: BinaryAssociation = BinaryAssociation(
    name="particle163",
    ends={
        Property(name="Particle165", type=NBVR_Grammar_PartPhrase, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_PartPhrase164", type=Particle, multiplicity=Multiplicity(1, 1))
    }
)
verb166: BinaryAssociation = BinaryAssociation(
    name="verb166",
    ends={
        Property(name="VerbPhrase", type=NBVR_Grammar_SimpleForm, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_SimpleForm", type=VerbPhrase, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
partPhrases167: BinaryAssociation = BinaryAssociation(
    name="partPhrases167",
    ends={
        Property(name="PartPhrase", type=NBVR_Grammar_SimpleForm, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_SimpleForm168", type=PartPhrase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subject169: BinaryAssociation = BinaryAssociation(
    name="subject169",
    ends={
        Property(name="RolePhrase171", type=NBVR_Grammar_SimpleForm, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_SimpleForm170", type=RolePhrase, multiplicity=Multiplicity(1, 1))
    }
)
object172: BinaryAssociation = BinaryAssociation(
    name="object172",
    ends={
        Property(name="RolePhrase174", type=NBVR_Grammar_SimpleForm, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_SimpleForm173", type=RolePhrase, multiplicity=Multiplicity(0, 1))
    }
)
domain190: BinaryAssociation = BinaryAssociation(
    name="domain190",
    ends={
        Property(name="RolePhrase191", type=NBVR_Grammar_QueryPhrase, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_QueryPhrase", type=RolePhrase, multiplicity=Multiplicity(1, 1))
    }
)
alternative180: BinaryAssociation = BinaryAssociation(
    name="alternative180",
    ends={
        Property(name="Sentence182", type=NBVR_Grammar_ImplicationForm, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_ImplicationForm181", type=Sentence, multiplicity=Multiplicity(0, 1))
    }
)
statements183: BinaryAssociation = BinaryAssociation(
    name="statements183",
    ends={
        Property(name="Sentence184", type=NBVR_Grammar_CompoundForm, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_CompoundForm", type=Sentence, multiplicity=Multiplicity(1, 9999))
    }
)
word185: BinaryAssociation = BinaryAssociation(
    name="word185",
    ends={
        Property(name="Word186", type=NBVR_Grammar_LexicalInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_LexicalInstance", type=Word, multiplicity=Multiplicity(1, 1))
    }
)
sentence187: BinaryAssociation = BinaryAssociation(
    name="sentence187",
    ends={
        Property(name="Sentence188", type=NBVR_Grammar_Nominalization, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_Nominalization", type=Sentence, multiplicity=Multiplicity(1, 1))
    }
)
queryPhrase189: BinaryAssociation = BinaryAssociation(
    name="queryPhrase189",
    ends={
        Property(name="QueryPhrase", type=NBVR_Grammar_Question, multiplicity=Multiplicity(1, 1)),
        Property(name="question", type=QueryPhrase, multiplicity=Multiplicity(0, 1))
    }
)
question192: BinaryAssociation = BinaryAssociation(
    name="question192",
    ends={
        Property(name="Question", type=NBVR_Grammar_QueryPhrase, multiplicity=Multiplicity(1, 1)),
        Property(name="queryPhrase", type=Question, multiplicity=Multiplicity(1, 1))
    }
)
name193: BinaryAssociation = BinaryAssociation(
    name="name193",
    ends={
        Property(name="VocName", type=NBVR_Grammar_ProperName, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_ProperName", type=VocName, multiplicity=Multiplicity(1, 1))
    }
)
keyword194: BinaryAssociation = BinaryAssociation(
    name="keyword194",
    ends={
        Property(name="Keyword", type=NBVR_Grammar_Pronoun, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_Pronoun", type=Keyword, multiplicity=Multiplicity(1, 1))
    }
)
concept195: BinaryAssociation = BinaryAssociation(
    name="concept195",
    ends={
        Property(name="RolePhrase196", type=NBVR_Grammar_Intension, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_Intension", type=RolePhrase, multiplicity=Multiplicity(0, 1))
    }
)
statement197: BinaryAssociation = BinaryAssociation(
    name="statement197",
    ends={
        Property(name="Sentence198", type=NBVR_Grammar_DomainForm, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_DomainForm", type=Sentence, multiplicity=Multiplicity(0, 1))
    }
)
word199: BinaryAssociation = BinaryAssociation(
    name="word199",
    ends={
        Property(name="Word200", type=NBVR_Grammar_LocalName, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_LocalName", type=Word, multiplicity=Multiplicity(1, 1))
    }
)
next201: BinaryAssociation = BinaryAssociation(
    name="next201",
    ends={
        Property(name="LocalName", type=NBVR_Grammar_LocalName, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_LocalName202", type=LocalName, multiplicity=Multiplicity(0, 1))
    }
)
parent203: BinaryAssociation = BinaryAssociation(
    name="parent203",
    ends={
        Property(name="ParseElement204", type=NBVR_Grammar_ParseElement, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Grammar_ParseElement", type=ParseElement, multiplicity=Multiplicity(0, 1))
    }
)
source205: BinaryAssociation = BinaryAssociation(
    name="source205",
    ends={
        Property(name="Quantification", type=NBVR_Logic_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="variable", type=Quantification, multiplicity=Multiplicity(0, 1))
    }
)
constraint206: BinaryAssociation = BinaryAssociation(
    name="constraint206",
    ends={
        Property(name="Proposition", type=NBVR_Logic_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Logic_Variable", type=Proposition, multiplicity=Multiplicity(0, 1))
    }
)
uses207: BinaryAssociation = BinaryAssociation(
    name="uses207",
    ends={
        Property(name="Relation", type=NBVR_Logic_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Logic_Variable208", type=Relation, multiplicity=Multiplicity(1, 9999))
    }
)
range209: BinaryAssociation = BinaryAssociation(
    name="range209",
    ends={
        Property(name="VocNoun211", type=NBVR_Logic_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Logic_Variable210", type=VocNoun, multiplicity=Multiplicity(1, 1))
    }
)
set212: BinaryAssociation = BinaryAssociation(
    name="set212",
    ends={
        Property(name="Set", type=NBVR_Logic_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="variable213", type=Set, multiplicity=Multiplicity(0, 1))
    }
)
scope214: BinaryAssociation = BinaryAssociation(
    name="scope214",
    ends={
        Property(name="Proposition215", type=NBVR_Logic_Quantification, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Logic_Quantification", type=Proposition, multiplicity=Multiplicity(1, 1))
    }
)
variable216: BinaryAssociation = BinaryAssociation(
    name="variable216",
    ends={
        Property(name="Variable217", type=NBVR_Logic_Quantification, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
owner218: BinaryAssociation = BinaryAssociation(
    name="owner218",
    ends={
        Property(name="Proposition219", type=NBVR_Logic_Proposition, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Logic_Proposition", type=Proposition, multiplicity=Multiplicity(0, 1))
    }
)
operands244: BinaryAssociation = BinaryAssociation(
    name="operands244",
    ends={
        Property(name="NBVR_Logic_Connection", type=Proposition, multiplicity=Multiplicity(1, 9999)),
        Property(name="Proposition245", type=NBVR_Logic_Connection, multiplicity=Multiplicity(1, 1))
    }
)
arguments220: BinaryAssociation = BinaryAssociation(
    name="arguments220",
    ends={
        Property(name="Argument", type=NBVR_Logic_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="relation", type=Argument, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
predicate221: BinaryAssociation = BinaryAssociation(
    name="predicate221",
    ends={
        Property(name="Predicate222", type=NBVR_Logic_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Logic_Relation", type=Predicate, multiplicity=Multiplicity(1, 1))
    }
)
next223: BinaryAssociation = BinaryAssociation(
    name="next223",
    ends={
        Property(name="Argument224", type=NBVR_Logic_Argument, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Logic_Argument", type=Argument, multiplicity=Multiplicity(0, 1))
    }
)
variable225: BinaryAssociation = BinaryAssociation(
    name="variable225",
    ends={
        Property(name="Variable227", type=NBVR_Logic_Argument, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Logic_Argument226", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
phrase228: BinaryAssociation = BinaryAssociation(
    name="phrase228",
    ends={
        Property(name="RolePhrase230", type=NBVR_Logic_Argument, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Logic_Argument229", type=RolePhrase, multiplicity=Multiplicity(1, 1))
    }
)
role231: BinaryAssociation = BinaryAssociation(
    name="role231",
    ends={
        Property(name="VerbRole233", type=NBVR_Logic_Argument, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Logic_Argument232", type=VerbRole, multiplicity=Multiplicity(0, 1))
    }
)
constant234: BinaryAssociation = BinaryAssociation(
    name="constant234",
    ends={
        Property(name="Constant", type=NBVR_Logic_Argument, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Logic_Argument235", type=Constant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
relation236: BinaryAssociation = BinaryAssociation(
    name="relation236",
    ends={
        Property(name="Relation237", type=NBVR_Logic_Argument, multiplicity=Multiplicity(1, 1)),
        Property(name="arguments", type=Relation, multiplicity=Multiplicity(1, 1))
    }
)
extent238: BinaryAssociation = BinaryAssociation(
    name="extent238",
    ends={
        Property(name="ExtentConstant", type=NBVR_Logic_Set, multiplicity=Multiplicity(1, 1)),
        Property(name="set", type=ExtentConstant, multiplicity=Multiplicity(0, 1))
    }
)
variable239: BinaryAssociation = BinaryAssociation(
    name="variable239",
    ends={
        Property(name="Variable241", type=NBVR_Logic_Set, multiplicity=Multiplicity(1, 1)),
        Property(name="set240", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
set242: BinaryAssociation = BinaryAssociation(
    name="set242",
    ends={
        Property(name="Set243", type=NBVR_Logic_ExtentConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="extent", type=Set, multiplicity=Multiplicity(1, 1))
    }
)
variables261: BinaryAssociation = BinaryAssociation(
    name="variables261",
    ends={
        Property(name="RoleVariable", type=NBVR_Logic_Predicate, multiplicity=Multiplicity(1, 1)),
        Property(name="predicate", type=RoleVariable, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
antecedent246: BinaryAssociation = BinaryAssociation(
    name="antecedent246",
    ends={
        Property(name="Proposition247", type=NBVR_Logic_Implication, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Logic_Implication", type=Proposition, multiplicity=Multiplicity(1, 1))
    }
)
consequent248: BinaryAssociation = BinaryAssociation(
    name="consequent248",
    ends={
        Property(name="Proposition250", type=NBVR_Logic_Implication, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Logic_Implication249", type=Proposition, multiplicity=Multiplicity(1, 1))
    }
)
scope251: BinaryAssociation = BinaryAssociation(
    name="scope251",
    ends={
        Property(name="Proposition252", type=NBVR_Logic_Modal, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Logic_Modal", type=Proposition, multiplicity=Multiplicity(1, 1))
    }
)
scope253: BinaryAssociation = BinaryAssociation(
    name="scope253",
    ends={
        Property(name="Proposition254", type=NBVR_Logic_Negation, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Logic_Negation", type=Proposition, multiplicity=Multiplicity(1, 1))
    }
)
predicate255: BinaryAssociation = BinaryAssociation(
    name="predicate255",
    ends={
        Property(name="Predicate256", type=NBVR_Logic_RoleVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="variables", type=Predicate, multiplicity=Multiplicity(0, 1))
    }
)
role257: BinaryAssociation = BinaryAssociation(
    name="role257",
    ends={
        Property(name="VerbRole258", type=NBVR_Logic_RoleVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Logic_RoleVariable", type=VerbRole, multiplicity=Multiplicity(0, 1))
    }
)
proposition259: BinaryAssociation = BinaryAssociation(
    name="proposition259",
    ends={
        Property(name="Proposition260", type=NBVR_Logic_NominalConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="NBVR_Logic_NominalConstant", type=Proposition, multiplicity=Multiplicity(1, 1))
    }
)
noun262: BinaryAssociation = BinaryAssociation(
    name="noun262",
    ends={
        Property(name="VocNoun264", type=NBVR_Logic_Predicate, multiplicity=Multiplicity(1, 1)),
        Property(name="predicate263", type=VocNoun, multiplicity=Multiplicity(0, 1))
    }
)
verb265: BinaryAssociation = BinaryAssociation(
    name="verb265",
    ends={
        Property(name="VocVerb267", type=NBVR_Logic_Predicate, multiplicity=Multiplicity(1, 1)),
        Property(name="predicate266", type=VocVerb, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_NBVR_Vocabulary_Adjective_Word = Generalization(general=Word, specific=NBVR_Vocabulary_Adjective)
gen_NBVR_Vocabulary_VocNoun_VocabularyItem = Generalization(general=VocabularyItem, specific=NBVR_Vocabulary_VocNoun)
gen_NBVR_Vocabulary_VocVerb_VocabularyItem = Generalization(general=VocabularyItem, specific=NBVR_Vocabulary_VocVerb)
gen_NBVR_Vocabulary_VocProperty_VocabularyItem = Generalization(general=VocabularyItem, specific=NBVR_Vocabulary_VocProperty)
gen_NBVR_Vocabulary_NumberWord_Word = Generalization(general=Word, specific=NBVR_Vocabulary_NumberWord)
gen_NBVR_Vocabulary_VocUnit_VocName = Generalization(general=VocName, specific=NBVR_Vocabulary_VocUnit)
gen_NBVR_Vocabulary_VocName_VocabularyItem = Generalization(general=VocabularyItem, specific=NBVR_Vocabulary_VocName)
gen_NBVR_Vocabulary_VocAdjective_VocabularyItem = Generalization(general=VocabularyItem, specific=NBVR_Vocabulary_VocAdjective)
gen_NBVR_Vocabulary_Noun_Word = Generalization(general=Word, specific=NBVR_Vocabulary_Noun)
gen_NBVR_Vocabulary_Particle_FormElement = Generalization(general=FormElement, specific=NBVR_Vocabulary_Particle)
gen_NBVR_Vocabulary_RoleElement_FormElement = Generalization(general=FormElement, specific=NBVR_Vocabulary_RoleElement)
gen_NBVR_Vocabulary_Keyword_Word = Generalization(general=Word, specific=NBVR_Vocabulary_Keyword)
gen_NBVR_Vocabulary_ItemElement_FormElement = Generalization(general=FormElement, specific=NBVR_Vocabulary_ItemElement)
gen_NBVR_Vocabulary_Adjunct_Word = Generalization(general=Word, specific=NBVR_Vocabulary_Adjunct)
gen_NBVR_Vocabulary_StringWord_Word = Generalization(general=Word, specific=NBVR_Vocabulary_StringWord)
gen_NBVR_Vocabulary_Definition_Formulation = Generalization(general=Formulation, specific=NBVR_Vocabulary_Definition)
gen_NBVR_Vocabulary_Name_Word = Generalization(general=Word, specific=NBVR_Vocabulary_Name)
gen_NBVR_Vocabulary_Verb_Word = Generalization(general=Word, specific=NBVR_Vocabulary_Verb)
gen_NBVR_Vocabulary_DateTime_Word = Generalization(general=Word, specific=NBVR_Vocabulary_DateTime)
gen_NBVR_Vocabulary_IsVerb_Verb = Generalization(general=Verb, specific=NBVR_Vocabulary_IsVerb)
gen_NBVR_Grammar_GroupPhrase_RolePhrase = Generalization(general=RolePhrase, specific=NBVR_Grammar_GroupPhrase)
gen_NBVR_Grammar_RolePhrase_Vocabulary_FormulationForm = Generalization(general=Vocabulary_FormulationForm, specific=NBVR_Grammar_RolePhrase)
gen_NBVR_Grammar_RolePhrase_Grammar_ParseElement = Generalization(general=Grammar_ParseElement, specific=NBVR_Grammar_RolePhrase)
gen_NBVR_Grammar_SimpleNounPhrase_RolePhrase = Generalization(general=RolePhrase, specific=NBVR_Grammar_SimpleNounPhrase)
gen_NBVR_Grammar_Condition_ParseElement = Generalization(general=ParseElement, specific=NBVR_Grammar_Condition)
gen_NBVR_Grammar_SimpleQualifier_Qualifier = Generalization(general=Qualifier, specific=NBVR_Grammar_SimpleQualifier)
gen_NBVR_Grammar_Qualifier_ParseElement = Generalization(general=ParseElement, specific=NBVR_Grammar_Qualifier)
gen_NBVR_Grammar_QualifierChain_Qualifier = Generalization(general=Qualifier, specific=NBVR_Grammar_QualifierChain)
gen_NBVR_Grammar_Sentence_Vocabulary_FormulationForm = Generalization(general=Vocabulary_FormulationForm, specific=NBVR_Grammar_Sentence)
gen_NBVR_Grammar_Sentence_Grammar_ParseElement = Generalization(general=Grammar_ParseElement, specific=NBVR_Grammar_Sentence)
gen_NBVR_Grammar_TypeNoun_ModifiedTerm = Generalization(general=ModifiedTerm, specific=NBVR_Grammar_TypeNoun)
gen_NBVR_Grammar_ModifiedTerm_SimpleNounPhrase = Generalization(general=SimpleNounPhrase, specific=NBVR_Grammar_ModifiedTerm)
gen_NBVR_Grammar_Quantifier_ParseElement = Generalization(general=ParseElement, specific=NBVR_Grammar_Quantifier)
gen_NBVR_Grammar_Quantity_Instance = Generalization(general=Instance, specific=NBVR_Grammar_Quantity)
gen_NBVR_Grammar_Instance_SimpleNounPhrase = Generalization(general=SimpleNounPhrase, specific=NBVR_Grammar_Instance)
gen_NBVR_Grammar_Modifier_ParseElement = Generalization(general=ParseElement, specific=NBVR_Grammar_Modifier)
gen_NBVR_Grammar_PropertyNoun_ModifiedTerm = Generalization(general=ModifiedTerm, specific=NBVR_Grammar_PropertyNoun)
gen_NBVR_Grammar_RoleNoun_SimpleNounPhrase = Generalization(general=SimpleNounPhrase, specific=NBVR_Grammar_RoleNoun)
gen_NBVR_Grammar_SimpleForm_Sentence = Generalization(general=Sentence, specific=NBVR_Grammar_SimpleForm)
gen_NBVR_Grammar_ImplicationForm_Sentence = Generalization(general=Sentence, specific=NBVR_Grammar_ImplicationForm)
gen_NBVR_Grammar_CompoundForm_Sentence = Generalization(general=Sentence, specific=NBVR_Grammar_CompoundForm)
gen_NBVR_Grammar_LexicalInstance_Instance = Generalization(general=Instance, specific=NBVR_Grammar_LexicalInstance)
gen_NBVR_Grammar_Nominalization_Instance = Generalization(general=Instance, specific=NBVR_Grammar_Nominalization)
gen_NBVR_Grammar_Statement_Nominalization = Generalization(general=Nominalization, specific=NBVR_Grammar_Statement)
gen_NBVR_Grammar_Question_Nominalization = Generalization(general=Nominalization, specific=NBVR_Grammar_Question)
gen_NBVR_Grammar_QueryPhrase_RolePhrase = Generalization(general=RolePhrase, specific=NBVR_Grammar_QueryPhrase)
gen_NBVR_Grammar_ProperName_Instance = Generalization(general=Instance, specific=NBVR_Grammar_ProperName)
gen_NBVR_Grammar_Pronoun_ModifiedTerm = Generalization(general=ModifiedTerm, specific=NBVR_Grammar_Pronoun)
gen_NBVR_Grammar_Intension_Instance = Generalization(general=Instance, specific=NBVR_Grammar_Intension)
gen_NBVR_Grammar_DomainForm_Sentence = Generalization(general=Sentence, specific=NBVR_Grammar_DomainForm)
gen_NBVR_Grammar_LocalName_SimpleNounPhrase = Generalization(general=SimpleNounPhrase, specific=NBVR_Grammar_LocalName)
gen_NBVR_Logic_Quantification_Proposition = Generalization(general=Proposition, specific=NBVR_Logic_Quantification)
gen_NBVR_Logic_Proposition_FormulationForm = Generalization(general=FormulationForm, specific=NBVR_Logic_Proposition)
gen_NBVR_Logic_Implication_Proposition = Generalization(general=Proposition, specific=NBVR_Logic_Implication)
gen_NBVR_Logic_Relation_Proposition = Generalization(general=Proposition, specific=NBVR_Logic_Relation)
gen_NBVR_Logic_ExtentConstant_Constant = Generalization(general=Constant, specific=NBVR_Logic_ExtentConstant)
gen_NBVR_Logic_Connection_Proposition = Generalization(general=Proposition, specific=NBVR_Logic_Connection)
gen_NBVR_Logic_Modal_Proposition = Generalization(general=Proposition, specific=NBVR_Logic_Modal)
gen_NBVR_Logic_Negation_Proposition = Generalization(general=Proposition, specific=NBVR_Logic_Negation)
gen_NBVR_Logic_RoleVariable_Variable = Generalization(general=Variable, specific=NBVR_Logic_RoleVariable)
gen_NBVR_Logic_ValueConstant_Constant = Generalization(general=Constant, specific=NBVR_Logic_ValueConstant)
gen_NBVR_Logic_NominalConstant_Constant = Generalization(general=Constant, specific=NBVR_Logic_NominalConstant)
gen_NBVR_Logic_QuantityValue_Constant = Generalization(general=Constant, specific=NBVR_Logic_QuantityValue)

# Domain Model
domain_model = DomainModel(
    name="NBVR",
    types={NBVR_Vocabulary_Adjective, Word, NBVR_Vocabulary_Word, WordForm, Term, NBVR_Vocabulary_WordForm, ParseElement, NBVR_Vocabulary_Term, VocabularyItem, VerbRole, Particle, ItemElement, NBVR_Vocabulary_VocabularyItem, Formulation, NBVR_Vocabulary_Formulation, FormulationForm, VocProperty, NBVR_Vocabulary_FormulationForm, NBVR_Vocabulary_VerbRole, VocNoun, VocVerb, NBVR_Vocabulary_VocNoun, Predicate, NBVR_Vocabulary_VocVerb, SyntaxForm, NBVR_Vocabulary_SyntaxForm, FormElement, NBVR_Vocabulary_FormElement, NBVR_Vocabulary_VocProperty, NBVR_Vocabulary_NumberWord, NBVR_Vocabulary_VocUnit, VocName, NBVR_Vocabulary_VocName, NBVR_Vocabulary_VocAdjective, NBVR_Vocabulary_Noun, NBVR_Vocabulary_Particle, RoleElement, NBVR_Vocabulary_RoleElement, NBVR_Vocabulary_Keyword, NBVR_Vocabulary_ItemElement, NBVR_Vocabulary_Adjunct, NBVR_Vocabulary_StringWord, NBVR_Vocabulary_Definition, NBVR_Vocabulary_Name, NBVR_Vocabulary_Verb, NBVR_Vocabulary_Dictionary, NBVR_Vocabulary_DateTime, NBVR_Vocabulary_Terminology, NBVR_Vocabulary_IsVerb, Verb, NBVR_Grammar_GroupPhrase, RolePhrase, SimpleNounPhrase, NBVR_Grammar_RolePhrase, Vocabulary_FormulationForm, Grammar_ParseElement, Variable, NBVR_Grammar_SimpleNounPhrase, NBVR_Grammar_TypeNoun, ModifiedTerm, NBVR_Grammar_Condition, SimpleQualifier, Sentence, NBVR_Grammar_SimpleQualifier, Qualifier, QualifierChain, Condition, NBVR_Grammar_Qualifier, NBVR_Grammar_QualifierChain, NBVR_Grammar_Sentence, NBVR_Grammar_PropertyNoun, NBVR_Grammar_ModifiedTerm, Quantifier, Modifier, NBVR_Grammar_Quantifier, Quantity, NBVR_Grammar_Quantity, Instance, NumberWord, Dimension, NBVR_Grammar_Instance, NBVR_Grammar_Dimension, VocUnit, NBVR_Grammar_Modifier, VocAdjective, TypeNoun, NBVR_Grammar_RoleNoun, NBVR_Grammar_VerbPhrase, NBVR_Grammar_PartPhrase, NBVR_Grammar_SimpleForm, VerbPhrase, PartPhrase, NBVR_Grammar_ImplicationForm, NBVR_Grammar_CompoundForm, NBVR_Grammar_LexicalInstance, NBVR_Grammar_Nominalization, NBVR_Grammar_Statement, Nominalization, NBVR_Grammar_Question, QueryPhrase, NBVR_Grammar_QueryPhrase, NBVR_Grammar_ParseElement, Question, NBVR_Grammar_ProperName, NBVR_Grammar_Pronoun, Keyword, NBVR_Grammar_Intension, NBVR_Grammar_Parse, NBVR_Grammar_DomainForm, NBVR_Grammar_LocalName, LocalName, NBVR_Logic_Variable, Quantification, Proposition, Relation, Set, NBVR_Logic_Quantification, NBVR_Logic_Proposition, NBVR_Logic_Implication, NBVR_Logic_Relation, Argument, NBVR_Logic_Argument, Constant, NBVR_Logic_Constant, NBVR_Logic_Set, ExtentConstant, NBVR_Logic_ExtentConstant, NBVR_Logic_Connection, RoleVariable, NBVR_Logic_Modal, NBVR_Logic_Negation, NBVR_Logic_RoleVariable, NBVR_Logic_ValueConstant, NBVR_Logic_NominalConstant, NBVR_Logic_QuantityValue, NBVR_Logic_Predicate, FormElementKind, KeywordKind, VocItemKind, QuantifierKind, GroupKind, InstanceKind, Connective, Modality, PhraseType, SentenceType, QueryKind, ElementKind, PropositionKind},
    associations={word7, altWord10, base0, beginsTerm1, next3, next5, elements34, concept35, concept13, role14, particle15, words17, context19, element22, formulations24, base25, next27, terms30, form33, property55, formulation37, range39, verb40, term41, isAVerb43, predicate45, roles46, form48, predicate50, elements53, domain73, verb75, verb56, form59, domain61, range63, verb66, propertyForm69, quantityKind71, plural85, role78, term79, role81, term83, altPlural87, singular90, plural92, past95, progressive98, perfective101, altPast104, firstWord107, firstItem109, lastItem111, members114, rolePlayed115, variable117, referent119, qualifier121, antecedent122, chain123, boundForm124, condition126, qualifiers127, domain129, rewrites131, relative147, noun134, quantifier136, modifiers137, qualifiers139, quantity141, factor142, dimension143, unit145, adjective146, antecedent175, consequent177, property150, domain152, expansion155, role157, verb159, partRole161, particle163, verb166, partPhrases167, subject169, object172, domain190, alternative180, statements183, word185, sentence187, queryPhrase189, question192, name193, keyword194, concept195, statement197, word199, next201, parent203, source205, constraint206, uses207, range209, set212, scope214, variable216, owner218, operands244, arguments220, predicate221, next223, variable225, phrase228, role231, constant234, relation236, extent238, variable239, set242, variables261, antecedent246, consequent248, scope251, scope253, predicate255, role257, proposition259, noun262, verb265},
    generalizations={gen_NBVR_Vocabulary_Adjective_Word, gen_NBVR_Vocabulary_VocNoun_VocabularyItem, gen_NBVR_Vocabulary_VocVerb_VocabularyItem, gen_NBVR_Vocabulary_VocProperty_VocabularyItem, gen_NBVR_Vocabulary_NumberWord_Word, gen_NBVR_Vocabulary_VocUnit_VocName, gen_NBVR_Vocabulary_VocName_VocabularyItem, gen_NBVR_Vocabulary_VocAdjective_VocabularyItem, gen_NBVR_Vocabulary_Noun_Word, gen_NBVR_Vocabulary_Particle_FormElement, gen_NBVR_Vocabulary_RoleElement_FormElement, gen_NBVR_Vocabulary_Keyword_Word, gen_NBVR_Vocabulary_ItemElement_FormElement, gen_NBVR_Vocabulary_Adjunct_Word, gen_NBVR_Vocabulary_StringWord_Word, gen_NBVR_Vocabulary_Definition_Formulation, gen_NBVR_Vocabulary_Name_Word, gen_NBVR_Vocabulary_Verb_Word, gen_NBVR_Vocabulary_DateTime_Word, gen_NBVR_Vocabulary_IsVerb_Verb, gen_NBVR_Grammar_GroupPhrase_RolePhrase, gen_NBVR_Grammar_RolePhrase_Vocabulary_FormulationForm, gen_NBVR_Grammar_RolePhrase_Grammar_ParseElement, gen_NBVR_Grammar_SimpleNounPhrase_RolePhrase, gen_NBVR_Grammar_Condition_ParseElement, gen_NBVR_Grammar_SimpleQualifier_Qualifier, gen_NBVR_Grammar_Qualifier_ParseElement, gen_NBVR_Grammar_QualifierChain_Qualifier, gen_NBVR_Grammar_Sentence_Vocabulary_FormulationForm, gen_NBVR_Grammar_Sentence_Grammar_ParseElement, gen_NBVR_Grammar_TypeNoun_ModifiedTerm, gen_NBVR_Grammar_ModifiedTerm_SimpleNounPhrase, gen_NBVR_Grammar_Quantifier_ParseElement, gen_NBVR_Grammar_Quantity_Instance, gen_NBVR_Grammar_Instance_SimpleNounPhrase, gen_NBVR_Grammar_Modifier_ParseElement, gen_NBVR_Grammar_PropertyNoun_ModifiedTerm, gen_NBVR_Grammar_RoleNoun_SimpleNounPhrase, gen_NBVR_Grammar_SimpleForm_Sentence, gen_NBVR_Grammar_ImplicationForm_Sentence, gen_NBVR_Grammar_CompoundForm_Sentence, gen_NBVR_Grammar_LexicalInstance_Instance, gen_NBVR_Grammar_Nominalization_Instance, gen_NBVR_Grammar_Statement_Nominalization, gen_NBVR_Grammar_Question_Nominalization, gen_NBVR_Grammar_QueryPhrase_RolePhrase, gen_NBVR_Grammar_ProperName_Instance, gen_NBVR_Grammar_Pronoun_ModifiedTerm, gen_NBVR_Grammar_Intension_Instance, gen_NBVR_Grammar_DomainForm_Sentence, gen_NBVR_Grammar_LocalName_SimpleNounPhrase, gen_NBVR_Logic_Quantification_Proposition, gen_NBVR_Logic_Proposition_FormulationForm, gen_NBVR_Logic_Implication_Proposition, gen_NBVR_Logic_Relation_Proposition, gen_NBVR_Logic_ExtentConstant_Constant, gen_NBVR_Logic_Connection_Proposition, gen_NBVR_Logic_Modal_Proposition, gen_NBVR_Logic_Negation_Proposition, gen_NBVR_Logic_RoleVariable_Variable, gen_NBVR_Logic_ValueConstant_Constant, gen_NBVR_Logic_NominalConstant_Constant, gen_NBVR_Logic_QuantityValue_Constant},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)