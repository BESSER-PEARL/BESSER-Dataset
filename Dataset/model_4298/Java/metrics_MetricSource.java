





import java.util.List;
import java.util.ArrayList;

public class metrics_MetricSource  {

    private String metricLocation;
    private String name;





    private metrics_Mapping metrics_mapping;




    private List<metrics_MappingStatistic> metrics_mappingstatistics;




    private List<metrics_Metric> metrics_metrics;




    private metrics_Metric metrics_metric;


    public metrics_MetricSource(
        String metricLocation,        String name    ) {
        this.metricLocation = metricLocation;
        this.name = name;
        this.metrics_mappingstatistics = new ArrayList<>();
        this.metrics_metrics = new ArrayList<>();
    }

    public metrics_MetricSource(
        String metricLocation,        String name        ArrayList<metrics_MappingStatistic> metrics_mappingstatistics,        ArrayList<metrics_Metric> metrics_metrics    ) {
        this.metricLocation = metricLocation;
        this.name = name;
        this.metrics_mappingstatistics = metrics_mappingstatistics;
        this.metrics_metrics = metrics_metrics;
    }

    public String getMetriclocation() {
        return metricLocation;
    }

    public void setMetriclocation(String metricLocation) {
        this.metricLocation = metricLocation;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public metrics_Mapping getMetrics_mapping() {
        return metrics_mapping;
    }

    public void setMetrics_mapping(metrics_Mapping metrics_mapping) {
        this.metrics_mapping = metrics_mapping;
    }
    public List<metrics_MappingStatistic> getMetrics_mappingstatistics() {
        return metrics_mappingstatistics;
    }

    public void addMetrics_mappingstatistic(Metrics_mappingstatistic metrics_mappingstatistic) {
        this.metrics_mappingstatistics.add(metrics_mappingstatistic);
    }
    public List<metrics_Metric> getMetrics_metrics() {
        return metrics_metrics;
    }

    public void addMetrics_metric(Metrics_metric metrics_metric) {
        this.metrics_metrics.add(metrics_metric);
    }
    public metrics_Metric getMetrics_metric() {
        return metrics_metric;
    }

    public void setMetrics_metric(metrics_Metric metrics_metric) {
        this.metrics_metric = metrics_metric;
    }

}