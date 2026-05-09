





import java.util.List;
import java.util.ArrayList;

public class UML2_BehavioralFeature extends Namespace, Feature {

    private boolean isAbstract;
    private String concurrency;





    private List<UML2_Parameter> uml2_parameters;




    private List<UML2_Parameter> uml2_parameters;




    private List<UML2_Parameter> uml2_parameters;




    private List<UML2_Type> uml2_types;


    public UML2_BehavioralFeature(
        boolean isAbstract,        String concurrency    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.concurrency = concurrency;
        this.uml2_parameters = new ArrayList<>();
        this.uml2_parameters = new ArrayList<>();
        this.uml2_parameters = new ArrayList<>();
        this.uml2_types = new ArrayList<>();
    }

    public UML2_BehavioralFeature(
        boolean isAbstract,        String concurrency        ArrayList<UML2_Parameter> uml2_parameters,        ArrayList<UML2_Parameter> uml2_parameters,        ArrayList<UML2_Parameter> uml2_parameters,        ArrayList<UML2_Type> uml2_types    ) {
        this.isAbstract = isAbstract;
        this.concurrency = concurrency;
        this.uml2_parameters = uml2_parameters;
        this.uml2_parameters = uml2_parameters;
        this.uml2_parameters = uml2_parameters;
        this.uml2_types = uml2_types;
    }

    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }
    public String getConcurrency() {
        return concurrency;
    }

    public void setConcurrency(String concurrency) {
        this.concurrency = concurrency;
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
    public List<UML2_Type> getUml2_types() {
        return uml2_types;
    }

    public void addUml2_type(Uml2_type uml2_type) {
        this.uml2_types.add(uml2_type);
    }

}