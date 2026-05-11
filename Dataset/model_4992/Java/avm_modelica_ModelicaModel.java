





import java.util.List;
import java.util.ArrayList;

public class avm_modelica_ModelicaModel extends DomainModel_ {

    private String Class;





    private List<Redeclare> redeclares;




    private List<Connector> connectors;




    private List<Parameter> parameters;




    private List<Metric> metrics;




    private List<Limit> limits;


    public avm_modelica_ModelicaModel(
        String Class    ) {
        super(
        );
        this.Class = Class;
        this.redeclares = new ArrayList<>();
        this.connectors = new ArrayList<>();
        this.parameters = new ArrayList<>();
        this.metrics = new ArrayList<>();
        this.limits = new ArrayList<>();
    }

    public avm_modelica_ModelicaModel(
        String Class        ArrayList<Redeclare> redeclares,        ArrayList<Connector> connectors,        ArrayList<Parameter> parameters,        ArrayList<Metric> metrics,        ArrayList<Limit> limits    ) {
        this.Class = Class;
        this.redeclares = redeclares;
        this.connectors = connectors;
        this.parameters = parameters;
        this.metrics = metrics;
        this.limits = limits;
    }

    public String getClass() {
        return Class;
    }

    public void setClass(String Class) {
        this.Class = Class;
    }

    public List<Redeclare> getRedeclares() {
        return redeclares;
    }

    public void addRedeclare(Redeclare redeclare) {
        this.redeclares.add(redeclare);
    }
    public List<Connector> getConnectors() {
        return connectors;
    }

    public void addConnector(Connector connector) {
        this.connectors.add(connector);
    }
    public List<Parameter> getParameters() {
        return parameters;
    }

    public void addParameter(Parameter parameter) {
        this.parameters.add(parameter);
    }
    public List<Metric> getMetrics() {
        return metrics;
    }

    public void addMetric(Metric metric) {
        this.metrics.add(metric);
    }
    public List<Limit> getLimits() {
        return limits;
    }

    public void addLimit(Limit limit) {
        this.limits.add(limit);
    }

}