





import java.util.List;
import java.util.ArrayList;

public class model_xsd_XSDFacet extends XSDComponent {

    private String lexicalValue;
    private String effectiveValue;
    private String facetName;





    private XSDSimpleTypeDefinition xsdsimpletypedefinition;




    private XSDAnnotation xsdannotation;


    public model_xsd_XSDFacet(
        String lexicalValue,        String effectiveValue,        String facetName    ) {
        super(
        );
        this.lexicalValue = lexicalValue;
        this.effectiveValue = effectiveValue;
        this.facetName = facetName;
    }


    public String getLexicalvalue() {
        return lexicalValue;
    }

    public void setLexicalvalue(String lexicalValue) {
        this.lexicalValue = lexicalValue;
    }
    public String getEffectivevalue() {
        return effectiveValue;
    }

    public void setEffectivevalue(String effectiveValue) {
        this.effectiveValue = effectiveValue;
    }
    public String getFacetname() {
        return facetName;
    }

    public void setFacetname(String facetName) {
        this.facetName = facetName;
    }

    public XSDSimpleTypeDefinition getXsdsimpletypedefinition() {
        return xsdsimpletypedefinition;
    }

    public void setXsdsimpletypedefinition(XSDSimpleTypeDefinition xsdsimpletypedefinition) {
        this.xsdsimpletypedefinition = xsdsimpletypedefinition;
    }
    public XSDAnnotation getXsdannotation() {
        return xsdannotation;
    }

    public void setXsdannotation(XSDAnnotation xsdannotation) {
        this.xsdannotation = xsdannotation;
    }

}