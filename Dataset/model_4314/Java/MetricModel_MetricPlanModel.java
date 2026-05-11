





import java.util.List;
import java.util.ArrayList;

public class MetricModel_MetricPlanModel  {

    private String name;





    private List<MetricModel_Metric> metricmodel_metrics;


    public MetricModel_MetricPlanModel(
        String name    ) {
        this.name = name;
        this.metricmodel_metrics = new ArrayList<>();
    }

    public MetricModel_MetricPlanModel(
        String name        ArrayList<MetricModel_Metric> metricmodel_metrics    ) {
        this.name = name;
        this.metricmodel_metrics = metricmodel_metrics;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<MetricModel_Metric> getMetricmodel_metrics() {
        return metricmodel_metrics;
    }

    public void addMetricmodel_metric(Metricmodel_metric metricmodel_metric) {
        this.metricmodel_metrics.add(metricmodel_metric);
    }

}