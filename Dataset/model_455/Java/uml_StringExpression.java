





import java.util.List;
import java.util.ArrayList;

public class uml_StringExpression extends Expression, TemplateableElement {






    private uml_StringExpression uml_stringexpression;




    private uml_NamedElement uml_namedelement;




    private List<uml_StringExpression> uml_stringexpressions;


    public uml_StringExpression(
    ) {
        super(
        );
        this.uml_stringexpressions = new ArrayList<>();
    }

    public uml_StringExpression(
        ArrayList<uml_StringExpression> uml_stringexpressions    ) {
        this.uml_stringexpressions = uml_stringexpressions;
    }


    public uml_StringExpression getUml_stringexpression() {
        return uml_stringexpression;
    }

    public void setUml_stringexpression(uml_StringExpression uml_stringexpression) {
        this.uml_stringexpression = uml_stringexpression;
    }
    public uml_NamedElement getUml_namedelement() {
        return uml_namedelement;
    }

    public void setUml_namedelement(uml_NamedElement uml_namedelement) {
        this.uml_namedelement = uml_namedelement;
    }
    public List<uml_StringExpression> getUml_stringexpressions() {
        return uml_stringexpressions;
    }

    public void addUml_stringexpression(Uml_stringexpression uml_stringexpression) {
        this.uml_stringexpressions.add(uml_stringexpression);
    }

}