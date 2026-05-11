





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedNamedElement extends TracedElement {






    private uml_TracedNamespace uml_tracednamespace;




    private uml_TracedStringExpression uml_tracedstringexpression;




    private List<uml_TracedDependency> uml_traceddependencys;


    public umlTrace_uml_TracedNamedElement(
    ) {
        super(
        );
        this.uml_traceddependencys = new ArrayList<>();
    }

    public umlTrace_uml_TracedNamedElement(
        ArrayList<uml_TracedDependency> uml_traceddependencys    ) {
        this.uml_traceddependencys = uml_traceddependencys;
    }


    public uml_TracedNamespace getUml_tracednamespace() {
        return uml_tracednamespace;
    }

    public void setUml_tracednamespace(uml_TracedNamespace uml_tracednamespace) {
        this.uml_tracednamespace = uml_tracednamespace;
    }
    public uml_TracedStringExpression getUml_tracedstringexpression() {
        return uml_tracedstringexpression;
    }

    public void setUml_tracedstringexpression(uml_TracedStringExpression uml_tracedstringexpression) {
        this.uml_tracedstringexpression = uml_tracedstringexpression;
    }
    public List<uml_TracedDependency> getUml_traceddependencys() {
        return uml_traceddependencys;
    }

    public void addUml_traceddependency(Uml_traceddependency uml_traceddependency) {
        this.uml_traceddependencys.add(uml_traceddependency);
    }

}