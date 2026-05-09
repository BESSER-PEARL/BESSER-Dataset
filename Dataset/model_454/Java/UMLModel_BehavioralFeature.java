





import java.util.List;
import java.util.ArrayList;

public class UMLModel_BehavioralFeature extends Namespace, Feature {

    private String concurrency;
    private String raisedException;
    private String method;
    private String isAbstract;





    private List<UMLModel_ParameterSet> umlmodel_parametersets;




    private List<UMLModel_Parameter> umlmodel_parameters;


    public UMLModel_BehavioralFeature(
        String concurrency,        String raisedException,        String method,        String isAbstract    ) {
        super(
        );
        this.concurrency = concurrency;
        this.raisedException = raisedException;
        this.method = method;
        this.isAbstract = isAbstract;
        this.umlmodel_parametersets = new ArrayList<>();
        this.umlmodel_parameters = new ArrayList<>();
    }

    public UMLModel_BehavioralFeature(
        String concurrency,        String raisedException,        String method,        String isAbstract        ArrayList<UMLModel_ParameterSet> umlmodel_parametersets,        ArrayList<UMLModel_Parameter> umlmodel_parameters    ) {
        this.concurrency = concurrency;
        this.raisedException = raisedException;
        this.method = method;
        this.isAbstract = isAbstract;
        this.umlmodel_parametersets = umlmodel_parametersets;
        this.umlmodel_parameters = umlmodel_parameters;
    }

    public String getConcurrency() {
        return concurrency;
    }

    public void setConcurrency(String concurrency) {
        this.concurrency = concurrency;
    }
    public String getRaisedexception() {
        return raisedException;
    }

    public void setRaisedexception(String raisedException) {
        this.raisedException = raisedException;
    }
    public String getMethod() {
        return method;
    }

    public void setMethod(String method) {
        this.method = method;
    }
    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }

    public List<UMLModel_ParameterSet> getUmlmodel_parametersets() {
        return umlmodel_parametersets;
    }

    public void addUmlmodel_parameterset(Umlmodel_parameterset umlmodel_parameterset) {
        this.umlmodel_parametersets.add(umlmodel_parameterset);
    }
    public List<UMLModel_Parameter> getUmlmodel_parameters() {
        return umlmodel_parameters;
    }

    public void addUmlmodel_parameter(Umlmodel_parameter umlmodel_parameter) {
        this.umlmodel_parameters.add(umlmodel_parameter);
    }

}