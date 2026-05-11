





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedConstraint extends TracedPackageableElement {






    private uml_TracedValueSpecification uml_tracedvaluespecification;




    private List<uml_TracedElement> uml_tracedelements;




    private uml_TracedNamespace uml_tracednamespace;


    public umlTrace_uml_TracedConstraint(
    ) {
        super(
        );
        this.uml_tracedelements = new ArrayList<>();
    }

    public umlTrace_uml_TracedConstraint(
        ArrayList<uml_TracedElement> uml_tracedelements    ) {
        this.uml_tracedelements = uml_tracedelements;
    }


    public uml_TracedValueSpecification getUml_tracedvaluespecification() {
        return uml_tracedvaluespecification;
    }

    public void setUml_tracedvaluespecification(uml_TracedValueSpecification uml_tracedvaluespecification) {
        this.uml_tracedvaluespecification = uml_tracedvaluespecification;
    }
    public List<uml_TracedElement> getUml_tracedelements() {
        return uml_tracedelements;
    }

    public void addUml_tracedelement(Uml_tracedelement uml_tracedelement) {
        this.uml_tracedelements.add(uml_tracedelement);
    }
    public uml_TracedNamespace getUml_tracednamespace() {
        return uml_tracednamespace;
    }

    public void setUml_tracednamespace(uml_TracedNamespace uml_tracednamespace) {
        this.uml_tracednamespace = uml_tracednamespace;
    }

}