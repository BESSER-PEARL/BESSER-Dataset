





import java.util.List;
import java.util.ArrayList;

public class uml_BehavioralFeature extends Feature, Namespace {

    private String isAbstract;





    private List<uml_Type> uml_types;




    private List<uml_Parameter> uml_parameters;


    public uml_BehavioralFeature(
        String isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.uml_types = new ArrayList<>();
        this.uml_parameters = new ArrayList<>();
    }

    public uml_BehavioralFeature(
        String isAbstract        ArrayList<uml_Type> uml_types,        ArrayList<uml_Parameter> uml_parameters    ) {
        this.isAbstract = isAbstract;
        this.uml_types = uml_types;
        this.uml_parameters = uml_parameters;
    }

    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }

    public List<uml_Type> getUml_types() {
        return uml_types;
    }

    public void addUml_type(Uml_type uml_type) {
        this.uml_types.add(uml_type);
    }
    public List<uml_Parameter> getUml_parameters() {
        return uml_parameters;
    }

    public void addUml_parameter(Uml_parameter uml_parameter) {
        this.uml_parameters.add(uml_parameter);
    }

}