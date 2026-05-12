





import java.util.List;
import java.util.ArrayList;

public class UML2_BehavioralFeature extends Namespace, Feature {

    private String concurrency;
    private boolean isAbstract;





    private UML2_Behavior uml2_behavior;




    private List<UML2_Type> uml2_types;




    private List<UML2_Parameter> uml2_parameters;




    private List<UML2_Parameter> uml2_parameters;




    private List<UML2_Parameter> uml2_parameters;




    private List<UML2_Behavior> uml2_behaviors;


    public UML2_BehavioralFeature(
        String concurrency,        boolean isAbstract    ) {
        super(
        );
        this.concurrency = concurrency;
        this.isAbstract = isAbstract;
        this.uml2_types = new ArrayList<>();
        this.uml2_parameters = new ArrayList<>();
        this.uml2_parameters = new ArrayList<>();
        this.uml2_parameters = new ArrayList<>();
        this.uml2_behaviors = new ArrayList<>();
    }

    public UML2_BehavioralFeature(
        String concurrency,        boolean isAbstract        ArrayList<UML2_Type> uml2_types,        ArrayList<UML2_Parameter> uml2_parameters,        ArrayList<UML2_Parameter> uml2_parameters,        ArrayList<UML2_Parameter> uml2_parameters,        ArrayList<UML2_Behavior> uml2_behaviors    ) {
        this.concurrency = concurrency;
        this.isAbstract = isAbstract;
        this.uml2_types = uml2_types;
        this.uml2_parameters = uml2_parameters;
        this.uml2_parameters = uml2_parameters;
        this.uml2_parameters = uml2_parameters;
        this.uml2_behaviors = uml2_behaviors;
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

    public UML2_Behavior getUml2_behavior() {
        return uml2_behavior;
    }

    public void setUml2_behavior(UML2_Behavior uml2_behavior) {
        this.uml2_behavior = uml2_behavior;
    }
    public List<UML2_Type> getUml2_types() {
        return uml2_types;
    }

    public void addUml2_type(Uml2_type uml2_type) {
        this.uml2_types.add(uml2_type);
    }
    public List<UML2_Parameter> getUml2_parameters() {
        return uml2_parameters;
    }

    public void addUml2_parameter(Uml2_parameter uml2_parameter) {
        this.uml2_parameters.add(uml2_parameter);
    }
    public List<UML2_Parameter> getUml2_parameters() {
        return uml2_parameters;
    }

    public void addUml2_parameter(Uml2_parameter uml2_parameter) {
        this.uml2_parameters.add(uml2_parameter);
    }
    public List<UML2_Parameter> getUml2_parameters() {
        return uml2_parameters;
    }

    public void addUml2_parameter(Uml2_parameter uml2_parameter) {
        this.uml2_parameters.add(uml2_parameter);
    }
    public List<UML2_Behavior> getUml2_behaviors() {
        return uml2_behaviors;
    }

    public void addUml2_behavior(Uml2_behavior uml2_behavior) {
        this.uml2_behaviors.add(uml2_behavior);
    }

}