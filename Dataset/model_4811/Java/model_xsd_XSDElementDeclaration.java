





import java.util.List;
import java.util.ArrayList;

public class model_xsd_XSDElementDeclaration extends xsd_XSDSchemaContent, xsd_XSDTerm, xsd_XSDFeature {

    private boolean abstract;
    private boolean nillable;
    private boolean circular;
    private String disallowedSubstitutions;
    private boolean elementDeclarationReference;
    private String lexicalFinal;
    private String block;
    private String substitutionGroupExclusions;





    private XSDElementDeclaration xsdelementdeclaration;




    private XSDTypeDefinition xsdtypedefinition;




    private XSDTypeDefinition xsdtypedefinition;




    private XSDElementDeclaration xsdelementdeclaration;




    private List<XSDElementDeclaration> xsdelementdeclarations;


    public model_xsd_XSDElementDeclaration(
        boolean abstract,        boolean nillable,        boolean circular,        String disallowedSubstitutions,        boolean elementDeclarationReference,        String lexicalFinal,        String block,        String substitutionGroupExclusions    ) {
        super(
        );
        this.abstract = abstract;
        this.nillable = nillable;
        this.circular = circular;
        this.disallowedSubstitutions = disallowedSubstitutions;
        this.elementDeclarationReference = elementDeclarationReference;
        this.lexicalFinal = lexicalFinal;
        this.block = block;
        this.substitutionGroupExclusions = substitutionGroupExclusions;
        this.xsdelementdeclarations = new ArrayList<>();
    }

    public model_xsd_XSDElementDeclaration(
        boolean abstract,        boolean nillable,        boolean circular,        String disallowedSubstitutions,        boolean elementDeclarationReference,        String lexicalFinal,        String block,        String substitutionGroupExclusions        ArrayList<XSDElementDeclaration> xsdelementdeclarations    ) {
        this.abstract = abstract;
        this.nillable = nillable;
        this.circular = circular;
        this.disallowedSubstitutions = disallowedSubstitutions;
        this.elementDeclarationReference = elementDeclarationReference;
        this.lexicalFinal = lexicalFinal;
        this.block = block;
        this.substitutionGroupExclusions = substitutionGroupExclusions;
        this.xsdelementdeclarations = xsdelementdeclarations;
    }

    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }
    public boolean getNillable() {
        return nillable;
    }

    public void setNillable(boolean nillable) {
        this.nillable = nillable;
    }
    public boolean getCircular() {
        return circular;
    }

    public void setCircular(boolean circular) {
        this.circular = circular;
    }
    public String getDisallowedsubstitutions() {
        return disallowedSubstitutions;
    }

    public void setDisallowedsubstitutions(String disallowedSubstitutions) {
        this.disallowedSubstitutions = disallowedSubstitutions;
    }
    public boolean getElementdeclarationreference() {
        return elementDeclarationReference;
    }

    public void setElementdeclarationreference(boolean elementDeclarationReference) {
        this.elementDeclarationReference = elementDeclarationReference;
    }
    public String getLexicalfinal() {
        return lexicalFinal;
    }

    public void setLexicalfinal(String lexicalFinal) {
        this.lexicalFinal = lexicalFinal;
    }
    public String getBlock() {
        return block;
    }

    public void setBlock(String block) {
        this.block = block;
    }
    public String getSubstitutiongroupexclusions() {
        return substitutionGroupExclusions;
    }

    public void setSubstitutiongroupexclusions(String substitutionGroupExclusions) {
        this.substitutionGroupExclusions = substitutionGroupExclusions;
    }

    public XSDElementDeclaration getXsdelementdeclaration() {
        return xsdelementdeclaration;
    }

    public void setXsdelementdeclaration(XSDElementDeclaration xsdelementdeclaration) {
        this.xsdelementdeclaration = xsdelementdeclaration;
    }
    public XSDTypeDefinition getXsdtypedefinition() {
        return xsdtypedefinition;
    }

    public void setXsdtypedefinition(XSDTypeDefinition xsdtypedefinition) {
        this.xsdtypedefinition = xsdtypedefinition;
    }
    public XSDTypeDefinition getXsdtypedefinition() {
        return xsdtypedefinition;
    }

    public void setXsdtypedefinition(XSDTypeDefinition xsdtypedefinition) {
        this.xsdtypedefinition = xsdtypedefinition;
    }
    public XSDElementDeclaration getXsdelementdeclaration() {
        return xsdelementdeclaration;
    }

    public void setXsdelementdeclaration(XSDElementDeclaration xsdelementdeclaration) {
        this.xsdelementdeclaration = xsdelementdeclaration;
    }
    public List<XSDElementDeclaration> getXsdelementdeclarations() {
        return xsdelementdeclarations;
    }

    public void addXsdelementdeclaration(Xsdelementdeclaration xsdelementdeclaration) {
        this.xsdelementdeclarations.add(xsdelementdeclaration);
    }

}