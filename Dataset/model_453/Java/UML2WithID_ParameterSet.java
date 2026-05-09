





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_ParameterSet extends NamedElement {






    private List<UML2WithID_Parameter> uml2withid_parameters;




    private UML2WithID_Parameter uml2withid_parameter;




    private UML2WithID_Behavior uml2withid_behavior;


    public UML2WithID_ParameterSet(
    ) {
        super(
        );
        this.uml2withid_parameters = new ArrayList<>();
    }

    public UML2WithID_ParameterSet(
        ArrayList<UML2WithID_Parameter> uml2withid_parameters    ) {
        this.uml2withid_parameters = uml2withid_parameters;
    }


    public List<UML2WithID_Parameter> getUml2withid_parameters() {
        return uml2withid_parameters;
    }

    public void addUml2withid_parameter(Uml2withid_parameter uml2withid_parameter) {
        this.uml2withid_parameters.add(uml2withid_parameter);
    }
    public UML2WithID_Parameter getUml2withid_parameter() {
        return uml2withid_parameter;
    }

    public void setUml2withid_parameter(UML2WithID_Parameter uml2withid_parameter) {
        this.uml2withid_parameter = uml2withid_parameter;
    }
    public UML2WithID_Behavior getUml2withid_behavior() {
        return uml2withid_behavior;
    }

    public void setUml2withid_behavior(UML2WithID_Behavior uml2withid_behavior) {
        this.uml2withid_behavior = uml2withid_behavior;
    }

}