





import java.util.List;
import java.util.ArrayList;

public class UML_14_BehavioralFeature extends Feature {

    private boolean isQuery;





    private UML_14_Parameter uml_14_parameter;




    private List<UML_14_Parameter> uml_14_parameters;


    public UML_14_BehavioralFeature(
        boolean isQuery    ) {
        super(
        );
        this.isQuery = isQuery;
        this.uml_14_parameters = new ArrayList<>();
    }

    public UML_14_BehavioralFeature(
        boolean isQuery        ArrayList<UML_14_Parameter> uml_14_parameters    ) {
        this.isQuery = isQuery;
        this.uml_14_parameters = uml_14_parameters;
    }

    public boolean getIsquery() {
        return isQuery;
    }

    public void setIsquery(boolean isQuery) {
        this.isQuery = isQuery;
    }

    public UML_14_Parameter getUml_14_parameter() {
        return uml_14_parameter;
    }

    public void setUml_14_parameter(UML_14_Parameter uml_14_parameter) {
        this.uml_14_parameter = uml_14_parameter;
    }
    public List<UML_14_Parameter> getUml_14_parameters() {
        return uml_14_parameters;
    }

    public void addUml_14_parameter(Uml_14_parameter uml_14_parameter) {
        this.uml_14_parameters.add(uml_14_parameter);
    }

}