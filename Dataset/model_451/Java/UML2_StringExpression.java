





import java.util.List;
import java.util.ArrayList;

public class UML2_StringExpression extends TemplateableElement {






    private UML2_StringExpression uml2_stringexpression;




    private UML2_Comment uml2_comment;




    private List<UML2_StringExpression> uml2_stringexpressions;


    public UML2_StringExpression(
    ) {
        super(
        );
        this.uml2_stringexpressions = new ArrayList<>();
    }

    public UML2_StringExpression(
        ArrayList<UML2_StringExpression> uml2_stringexpressions    ) {
        this.uml2_stringexpressions = uml2_stringexpressions;
    }


    public UML2_StringExpression getUml2_stringexpression() {
        return uml2_stringexpression;
    }

    public void setUml2_stringexpression(UML2_StringExpression uml2_stringexpression) {
        this.uml2_stringexpression = uml2_stringexpression;
    }
    public UML2_Comment getUml2_comment() {
        return uml2_comment;
    }

    public void setUml2_comment(UML2_Comment uml2_comment) {
        this.uml2_comment = uml2_comment;
    }
    public List<UML2_StringExpression> getUml2_stringexpressions() {
        return uml2_stringexpressions;
    }

    public void addUml2_stringexpression(Uml2_stringexpression uml2_stringexpression) {
        this.uml2_stringexpressions.add(uml2_stringexpression);
    }

}