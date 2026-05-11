





import java.util.List;
import java.util.ArrayList;

public class Metrics_Metric  {

    private String name;





    private List<MetricValue> metricvalues;


    public Metrics_Metric(
        String name    ) {
        this.name = name;
        this.metricvalues = new ArrayList<>();
    }

    public Metrics_Metric(
        String name        ArrayList<MetricValue> metricvalues    ) {
        this.name = name;
        this.metricvalues = metricvalues;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<MetricValue> getMetricvalues() {
        return metricvalues;
    }

    public void addMetricvalue(Metricvalue metricvalue) {
        this.metricvalues.add(metricvalue);
    }

}