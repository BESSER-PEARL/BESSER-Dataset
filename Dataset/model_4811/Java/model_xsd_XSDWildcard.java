





import java.util.List;
import java.util.ArrayList;

public class model_xsd_XSDWildcard extends XSDTerm {

    private String namespaceConstraintCategory;
    private String processContents;
    private String namespaceConstraint;
    private String lexicalNamespaceConstraint;





    private List<XSDAnnotation> xsdannotations;




    private XSDAnnotation xsdannotation;


    public model_xsd_XSDWildcard(
        String namespaceConstraintCategory,        String processContents,        String namespaceConstraint,        String lexicalNamespaceConstraint    ) {
        super(
        );
        this.namespaceConstraintCategory = namespaceConstraintCategory;
        this.processContents = processContents;
        this.namespaceConstraint = namespaceConstraint;
        this.lexicalNamespaceConstraint = lexicalNamespaceConstraint;
        this.xsdannotations = new ArrayList<>();
    }

    public model_xsd_XSDWildcard(
        String namespaceConstraintCategory,        String processContents,        String namespaceConstraint,        String lexicalNamespaceConstraint        ArrayList<XSDAnnotation> xsdannotations    ) {
        this.namespaceConstraintCategory = namespaceConstraintCategory;
        this.processContents = processContents;
        this.namespaceConstraint = namespaceConstraint;
        this.lexicalNamespaceConstraint = lexicalNamespaceConstraint;
        this.xsdannotations = xsdannotations;
    }

    public String getNamespaceconstraintcategory() {
        return namespaceConstraintCategory;
    }

    public void setNamespaceconstraintcategory(String namespaceConstraintCategory) {
        this.namespaceConstraintCategory = namespaceConstraintCategory;
    }
    public String getProcesscontents() {
        return processContents;
    }

    public void setProcesscontents(String processContents) {
        this.processContents = processContents;
    }
    public String getNamespaceconstraint() {
        return namespaceConstraint;
    }

    public void setNamespaceconstraint(String namespaceConstraint) {
        this.namespaceConstraint = namespaceConstraint;
    }
    public String getLexicalnamespaceconstraint() {
        return lexicalNamespaceConstraint;
    }

    public void setLexicalnamespaceconstraint(String lexicalNamespaceConstraint) {
        this.lexicalNamespaceConstraint = lexicalNamespaceConstraint;
    }

    public List<XSDAnnotation> getXsdannotations() {
        return xsdannotations;
    }

    public void addXsdannotation(Xsdannotation xsdannotation) {
        this.xsdannotations.add(xsdannotation);
    }
    public XSDAnnotation getXsdannotation() {
        return xsdannotation;
    }

    public void setXsdannotation(XSDAnnotation xsdannotation) {
        this.xsdannotation = xsdannotation;
    }

}