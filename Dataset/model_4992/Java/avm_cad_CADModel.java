





import java.util.List;
import java.util.ArrayList;

public class avm_cad_CADModel extends DomainModel_ {

    private String Format;





    private List<Metric> metrics;




    private List<Parameter> parameters;


    public avm_cad_CADModel(
        String Format    ) {
        super(
        );
        this.Format = Format;
        this.metrics = new ArrayList<>();
        this.parameters = new ArrayList<>();
    }

    public avm_cad_CADModel(
        String Format        ArrayList<Metric> metrics,        ArrayList<Parameter> parameters    ) {
        this.Format = Format;
        this.metrics = metrics;
        this.parameters = parameters;
    }

    public String getFormat() {
        return Format;
    }

    public void setFormat(String Format) {
        this.Format = Format;
    }

    public List<Metric> getMetrics() {
        return metrics;
    }

    public void addMetric(Metric metric) {
        this.metrics.add(metric);
    }
    public List<Parameter> getParameters() {
        return parameters;
    }

    public void addParameter(Parameter parameter) {
        this.parameters.add(parameter);
    }

}