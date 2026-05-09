





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Operation extends TypedElement, MultiplicityElement, BehavioralFeature, ParameterableElement {

    private boolean isQuery;





    private UML2WithID_Artifact uml2withid_artifact;




    private UML2WithID_Parameter uml2withid_parameter;




    private UML2WithID_DataType uml2withid_datatype;




    private UML2WithID_DataType uml2withid_datatype;




    private List<UML2WithID_Operation> uml2withid_operations;




    private UML2WithID_Interface uml2withid_interface;




    private List<UML2WithID_Parameter> uml2withid_parameters;


    public UML2WithID_Operation(
        boolean isQuery    ) {
        super(
        );
        this.isQuery = isQuery;
        this.uml2withid_operations = new ArrayList<>();
        this.uml2withid_parameters = new ArrayList<>();
    }

    public UML2WithID_Operation(
        boolean isQuery        ArrayList<UML2WithID_Operation> uml2withid_operations,        ArrayList<UML2WithID_Parameter> uml2withid_parameters    ) {
        this.isQuery = isQuery;
        this.uml2withid_operations = uml2withid_operations;
        this.uml2withid_parameters = uml2withid_parameters;
    }

    public boolean getIsquery() {
        return isQuery;
    }

    public void setIsquery(boolean isQuery) {
        this.isQuery = isQuery;
    }

    public UML2WithID_Artifact getUml2withid_artifact() {
        return uml2withid_artifact;
    }

    public void setUml2withid_artifact(UML2WithID_Artifact uml2withid_artifact) {
        this.uml2withid_artifact = uml2withid_artifact;
    }
    public UML2WithID_Parameter getUml2withid_parameter() {
        return uml2withid_parameter;
    }

    public void setUml2withid_parameter(UML2WithID_Parameter uml2withid_parameter) {
        this.uml2withid_parameter = uml2withid_parameter;
    }
    public UML2WithID_DataType getUml2withid_datatype() {
        return uml2withid_datatype;
    }

    public void setUml2withid_datatype(UML2WithID_DataType uml2withid_datatype) {
        this.uml2withid_datatype = uml2withid_datatype;
    }
    public UML2WithID_DataType getUml2withid_datatype() {
        return uml2withid_datatype;
    }

    public void setUml2withid_datatype(UML2WithID_DataType uml2withid_datatype) {
        this.uml2withid_datatype = uml2withid_datatype;
    }
    public List<UML2WithID_Operation> getUml2withid_operations() {
        return uml2withid_operations;
    }

    public void addUml2withid_operation(Uml2withid_operation uml2withid_operation) {
        this.uml2withid_operations.add(uml2withid_operation);
    }
    public UML2WithID_Interface getUml2withid_interface() {
        return uml2withid_interface;
    }

    public void setUml2withid_interface(UML2WithID_Interface uml2withid_interface) {
        this.uml2withid_interface = uml2withid_interface;
    }
    public List<UML2WithID_Parameter> getUml2withid_parameters() {
        return uml2withid_parameters;
    }

    public void addUml2withid_parameter(Uml2withid_parameter uml2withid_parameter) {
        this.uml2withid_parameters.add(uml2withid_parameter);
    }

}