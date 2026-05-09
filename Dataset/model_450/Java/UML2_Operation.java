





import java.util.List;
import java.util.ArrayList;

public class UML2_Operation extends TypedElement, MultiplicityElement, ParameterableElement, BehavioralFeature {

    private boolean isQuery;





    private List<UML2_Operation> uml2_operations;




    private UML2_Class uml2_class;




    private UML2_Class uml2_class;


    public UML2_Operation(
        boolean isQuery    ) {
        super(
        );
        this.isQuery = isQuery;
        this.uml2_operations = new ArrayList<>();
    }

    public UML2_Operation(
        boolean isQuery        ArrayList<UML2_Operation> uml2_operations    ) {
        this.isQuery = isQuery;
        this.uml2_operations = uml2_operations;
    }

    public boolean getIsquery() {
        return isQuery;
    }

    public void setIsquery(boolean isQuery) {
        this.isQuery = isQuery;
    }

    public List<UML2_Operation> getUml2_operations() {
        return uml2_operations;
    }

    public void addUml2_operation(Uml2_operation uml2_operation) {
        this.uml2_operations.add(uml2_operation);
    }
    public UML2_Class getUml2_class() {
        return uml2_class;
    }

    public void setUml2_class(UML2_Class uml2_class) {
        this.uml2_class = uml2_class;
    }
    public UML2_Class getUml2_class() {
        return uml2_class;
    }

    public void setUml2_class(UML2_Class uml2_class) {
        this.uml2_class = uml2_class;
    }

}