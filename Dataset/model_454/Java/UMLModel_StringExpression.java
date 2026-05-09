





import java.util.List;
import java.util.ArrayList;

public class UMLModel_StringExpression extends TemplateableElement, Expression {

    private String owningExpression;





    private UMLModel_NamedElement umlmodel_namedelement;




    private List<UMLModel_StringExpression> umlmodel_stringexpressions;


    public UMLModel_StringExpression(
        String owningExpression    ) {
        super(
        );
        this.owningExpression = owningExpression;
        this.umlmodel_stringexpressions = new ArrayList<>();
    }

    public UMLModel_StringExpression(
        String owningExpression        ArrayList<UMLModel_StringExpression> umlmodel_stringexpressions    ) {
        this.owningExpression = owningExpression;
        this.umlmodel_stringexpressions = umlmodel_stringexpressions;
    }

    public String getOwningexpression() {
        return owningExpression;
    }

    public void setOwningexpression(String owningExpression) {
        this.owningExpression = owningExpression;
    }

    public UMLModel_NamedElement getUmlmodel_namedelement() {
        return umlmodel_namedelement;
    }

    public void setUmlmodel_namedelement(UMLModel_NamedElement umlmodel_namedelement) {
        this.umlmodel_namedelement = umlmodel_namedelement;
    }
    public List<UMLModel_StringExpression> getUmlmodel_stringexpressions() {
        return umlmodel_stringexpressions;
    }

    public void addUmlmodel_stringexpression(Umlmodel_stringexpression umlmodel_stringexpression) {
        this.umlmodel_stringexpressions.add(umlmodel_stringexpression);
    }

}