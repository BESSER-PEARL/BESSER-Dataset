





import java.util.List;
import java.util.ArrayList;

public class UML2_StructuredActivityNode extends Namespace, Action, ActivityGroup {

    private boolean mustIsolate;





    private UML2_Variable uml2_variable;




    private List<UML2_Variable> uml2_variables;


    public UML2_StructuredActivityNode(
        boolean mustIsolate    ) {
        super(
        );
        this.mustIsolate = mustIsolate;
        this.uml2_variables = new ArrayList<>();
    }

    public UML2_StructuredActivityNode(
        boolean mustIsolate        ArrayList<UML2_Variable> uml2_variables    ) {
        this.mustIsolate = mustIsolate;
        this.uml2_variables = uml2_variables;
    }

    public boolean getMustisolate() {
        return mustIsolate;
    }

    public void setMustisolate(boolean mustIsolate) {
        this.mustIsolate = mustIsolate;
    }

    public UML2_Variable getUml2_variable() {
        return uml2_variable;
    }

    public void setUml2_variable(UML2_Variable uml2_variable) {
        this.uml2_variable = uml2_variable;
    }
    public List<UML2_Variable> getUml2_variables() {
        return uml2_variables;
    }

    public void addUml2_variable(Uml2_variable uml2_variable) {
        this.uml2_variables.add(uml2_variable);
    }

}