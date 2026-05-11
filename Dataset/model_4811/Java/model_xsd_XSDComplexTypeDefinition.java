





import java.util.List;
import java.util.ArrayList;

public class model_xsd_XSDComplexTypeDefinition extends xsd_XSDTypeDefinition, xsd_XSDScope {

    private boolean mixed;
    private String block;
    private String lexicalFinal;
    private String contentTypeCategory;
    private String derivationMethod;
    private boolean abstract;
    private String prohibitedSubstitutions;
    private String final;





    private XSDTypeDefinition xsdtypedefinition;




    private XSDTypeDefinition xsdtypedefinition;




    private XSDComplexTypeContent xsdcomplextypecontent;




    private XSDComplexTypeContent xsdcomplextypecontent;




    private XSDAnnotation xsdannotation;


    public model_xsd_XSDComplexTypeDefinition(
        boolean mixed,        String block,        String lexicalFinal,        String contentTypeCategory,        String derivationMethod,        boolean abstract,        String prohibitedSubstitutions,        String final    ) {
        super(
        );
        this.mixed = mixed;
        this.block = block;
        this.lexicalFinal = lexicalFinal;
        this.contentTypeCategory = contentTypeCategory;
        this.derivationMethod = derivationMethod;
        this.abstract = abstract;
        this.prohibitedSubstitutions = prohibitedSubstitutions;
        this.final = final;
    }


    public boolean getMixed() {
        return mixed;
    }

    public void setMixed(boolean mixed) {
        this.mixed = mixed;
    }
    public String getBlock() {
        return block;
    }

    public void setBlock(String block) {
        this.block = block;
    }
    public String getLexicalfinal() {
        return lexicalFinal;
    }

    public void setLexicalfinal(String lexicalFinal) {
        this.lexicalFinal = lexicalFinal;
    }
    public String getContenttypecategory() {
        return contentTypeCategory;
    }

    public void setContenttypecategory(String contentTypeCategory) {
        this.contentTypeCategory = contentTypeCategory;
    }
    public String getDerivationmethod() {
        return derivationMethod;
    }

    public void setDerivationmethod(String derivationMethod) {
        this.derivationMethod = derivationMethod;
    }
    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }
    public String getProhibitedsubstitutions() {
        return prohibitedSubstitutions;
    }

    public void setProhibitedsubstitutions(String prohibitedSubstitutions) {
        this.prohibitedSubstitutions = prohibitedSubstitutions;
    }
    public String getFinal() {
        return final;
    }

    public void setFinal(String final) {
        this.final = final;
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
    public XSDComplexTypeContent getXsdcomplextypecontent() {
        return xsdcomplextypecontent;
    }

    public void setXsdcomplextypecontent(XSDComplexTypeContent xsdcomplextypecontent) {
        this.xsdcomplextypecontent = xsdcomplextypecontent;
    }
    public XSDComplexTypeContent getXsdcomplextypecontent() {
        return xsdcomplextypecontent;
    }

    public void setXsdcomplextypecontent(XSDComplexTypeContent xsdcomplextypecontent) {
        this.xsdcomplextypecontent = xsdcomplextypecontent;
    }
    public XSDAnnotation getXsdannotation() {
        return xsdannotation;
    }

    public void setXsdannotation(XSDAnnotation xsdannotation) {
        this.xsdannotation = xsdannotation;
    }

}