





import java.util.List;
import java.util.ArrayList;

public class RefOntoUML_StringExpression extends Expression {






    private RefOntoUML_NamedElement refontouml_namedelement;




    private RefOntoUML_StringExpression refontouml_stringexpression;




    private List<RefOntoUML_StringExpression> refontouml_stringexpressions;


    public RefOntoUML_StringExpression(
    ) {
        super(
        );
        this.refontouml_stringexpressions = new ArrayList<>();
    }

    public RefOntoUML_StringExpression(
        ArrayList<RefOntoUML_StringExpression> refontouml_stringexpressions    ) {
        this.refontouml_stringexpressions = refontouml_stringexpressions;
    }


    public RefOntoUML_NamedElement getRefontouml_namedelement() {
        return refontouml_namedelement;
    }

    public void setRefontouml_namedelement(RefOntoUML_NamedElement refontouml_namedelement) {
        this.refontouml_namedelement = refontouml_namedelement;
    }
    public RefOntoUML_StringExpression getRefontouml_stringexpression() {
        return refontouml_stringexpression;
    }

    public void setRefontouml_stringexpression(RefOntoUML_StringExpression refontouml_stringexpression) {
        this.refontouml_stringexpression = refontouml_stringexpression;
    }
    public List<RefOntoUML_StringExpression> getRefontouml_stringexpressions() {
        return refontouml_stringexpressions;
    }

    public void addRefontouml_stringexpression(Refontouml_stringexpression refontouml_stringexpression) {
        this.refontouml_stringexpressions.add(refontouml_stringexpression);
    }

}