





import java.util.List;
import java.util.ArrayList;

public class uml_BehavioralFeature extends Feature, Namespace {






    private List<uml_Parameter> uml_parameters;


    public uml_BehavioralFeature(
    ) {
        super(
        );
        this.uml_parameters = new ArrayList<>();
    }

    public uml_BehavioralFeature(
        ArrayList<uml_Parameter> uml_parameters    ) {
        this.uml_parameters = uml_parameters;
    }


    public List<uml_Parameter> getUml_parameters() {
        return uml_parameters;
    }

    public void addUml_parameter(Uml_parameter uml_parameter) {
        this.uml_parameters.add(uml_parameter);
    }

}