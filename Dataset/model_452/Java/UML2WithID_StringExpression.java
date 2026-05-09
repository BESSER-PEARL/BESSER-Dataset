





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_StringExpression extends TemplateableElement {






    private UML2WithID_NamedElement uml2withid_namedelement;




    private UML2WithID_StringExpression uml2withid_stringexpression;




    private List<UML2WithID_StringExpression> uml2withid_stringexpressions;


    public UML2WithID_StringExpression(
    ) {
        super(
        );
        this.uml2withid_stringexpressions = new ArrayList<>();
    }

    public UML2WithID_StringExpression(
        ArrayList<UML2WithID_StringExpression> uml2withid_stringexpressions    ) {
        this.uml2withid_stringexpressions = uml2withid_stringexpressions;
    }


    public UML2WithID_NamedElement getUml2withid_namedelement() {
        return uml2withid_namedelement;
    }

    public void setUml2withid_namedelement(UML2WithID_NamedElement uml2withid_namedelement) {
        this.uml2withid_namedelement = uml2withid_namedelement;
    }
    public UML2WithID_StringExpression getUml2withid_stringexpression() {
        return uml2withid_stringexpression;
    }

    public void setUml2withid_stringexpression(UML2WithID_StringExpression uml2withid_stringexpression) {
        this.uml2withid_stringexpression = uml2withid_stringexpression;
    }
    public List<UML2WithID_StringExpression> getUml2withid_stringexpressions() {
        return uml2withid_stringexpressions;
    }

    public void addUml2withid_stringexpression(Uml2withid_stringexpression uml2withid_stringexpression) {
        this.uml2withid_stringexpressions.add(uml2withid_stringexpression);
    }

}