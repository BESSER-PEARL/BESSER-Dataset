





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Operation extends ParameterableElement, BehavioralFeature, MultiplicityElement, TypedElement {

    private boolean isQuery;





    private List<UML2WithID_Parameter> uml2withid_parameters;




    private List<UML2WithID_Operation> uml2withid_operations;




    private UML2WithID_Parameter uml2withid_parameter;


    public UML2WithID_Operation(
        boolean isQuery    ) {
        super(
        );
        this.isQuery = isQuery;
        this.uml2withid_parameters = new ArrayList<>();
        this.uml2withid_operations = new ArrayList<>();
    }

    public UML2WithID_Operation(
        boolean isQuery        ArrayList<UML2WithID_Parameter> uml2withid_parameters,        ArrayList<UML2WithID_Operation> uml2withid_operations    ) {
        this.isQuery = isQuery;
        this.uml2withid_parameters = uml2withid_parameters;
        this.uml2withid_operations = uml2withid_operations;
    }

    public boolean getIsquery() {
        return isQuery;
    }

    public void setIsquery(boolean isQuery) {
        this.isQuery = isQuery;
    }

    public List<UML2WithID_Parameter> getUml2withid_parameters() {
        return uml2withid_parameters;
    }

    public void addUml2withid_parameter(Uml2withid_parameter uml2withid_parameter) {
        this.uml2withid_parameters.add(uml2withid_parameter);
    }
    public List<UML2WithID_Operation> getUml2withid_operations() {
        return uml2withid_operations;
    }

    public void addUml2withid_operation(Uml2withid_operation uml2withid_operation) {
        this.uml2withid_operations.add(uml2withid_operation);
    }
    public UML2WithID_Parameter getUml2withid_parameter() {
        return uml2withid_parameter;
    }

    public void setUml2withid_parameter(UML2WithID_Parameter uml2withid_parameter) {
        this.uml2withid_parameter = uml2withid_parameter;
    }

}