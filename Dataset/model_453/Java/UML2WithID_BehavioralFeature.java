





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_BehavioralFeature extends Namespace, Feature {

    private String concurrency;
    private boolean isAbstract;





    private List<UML2WithID_Parameter> uml2withid_parameters;




    private List<UML2WithID_Parameter> uml2withid_parameters;




    private UML2WithID_Behavior uml2withid_behavior;




    private List<UML2WithID_Type> uml2withid_types;




    private List<UML2WithID_Behavior> uml2withid_behaviors;




    private List<UML2WithID_Parameter> uml2withid_parameters;


    public UML2WithID_BehavioralFeature(
        String concurrency,        boolean isAbstract    ) {
        super(
        );
        this.concurrency = concurrency;
        this.isAbstract = isAbstract;
        this.uml2withid_parameters = new ArrayList<>();
        this.uml2withid_parameters = new ArrayList<>();
        this.uml2withid_types = new ArrayList<>();
        this.uml2withid_behaviors = new ArrayList<>();
        this.uml2withid_parameters = new ArrayList<>();
    }

    public UML2WithID_BehavioralFeature(
        String concurrency,        boolean isAbstract        ArrayList<UML2WithID_Parameter> uml2withid_parameters,        ArrayList<UML2WithID_Parameter> uml2withid_parameters,        ArrayList<UML2WithID_Type> uml2withid_types,        ArrayList<UML2WithID_Behavior> uml2withid_behaviors,        ArrayList<UML2WithID_Parameter> uml2withid_parameters    ) {
        this.concurrency = concurrency;
        this.isAbstract = isAbstract;
        this.uml2withid_parameters = uml2withid_parameters;
        this.uml2withid_parameters = uml2withid_parameters;
        this.uml2withid_types = uml2withid_types;
        this.uml2withid_behaviors = uml2withid_behaviors;
        this.uml2withid_parameters = uml2withid_parameters;
    }

    public String getConcurrency() {
        return concurrency;
    }

    public void setConcurrency(String concurrency) {
        this.concurrency = concurrency;
    }
    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public List<UML2WithID_Parameter> getUml2withid_parameters() {
        return uml2withid_parameters;
    }

    public void addUml2withid_parameter(Uml2withid_parameter uml2withid_parameter) {
        this.uml2withid_parameters.add(uml2withid_parameter);
    }
    public List<UML2WithID_Parameter> getUml2withid_parameters() {
        return uml2withid_parameters;
    }

    public void addUml2withid_parameter(Uml2withid_parameter uml2withid_parameter) {
        this.uml2withid_parameters.add(uml2withid_parameter);
    }
    public UML2WithID_Behavior getUml2withid_behavior() {
        return uml2withid_behavior;
    }

    public void setUml2withid_behavior(UML2WithID_Behavior uml2withid_behavior) {
        this.uml2withid_behavior = uml2withid_behavior;
    }
    public List<UML2WithID_Type> getUml2withid_types() {
        return uml2withid_types;
    }

    public void addUml2withid_type(Uml2withid_type uml2withid_type) {
        this.uml2withid_types.add(uml2withid_type);
    }
    public List<UML2WithID_Behavior> getUml2withid_behaviors() {
        return uml2withid_behaviors;
    }

    public void addUml2withid_behavior(Uml2withid_behavior uml2withid_behavior) {
        this.uml2withid_behaviors.add(uml2withid_behavior);
    }
    public List<UML2WithID_Parameter> getUml2withid_parameters() {
        return uml2withid_parameters;
    }

    public void addUml2withid_parameter(Uml2withid_parameter uml2withid_parameter) {
        this.uml2withid_parameters.add(uml2withid_parameter);
    }

}