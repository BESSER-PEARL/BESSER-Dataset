





import java.util.List;
import java.util.ArrayList;

public class metrics_MetricSource extends Base {

    private String name;
    private String metricLocation;
    private String filterPattern;





    private metrics_Mapping metrics_mapping;




    private List<metrics_MappingStatistic> metrics_mappingstatistics;




    private metrics_Metric metrics_metric;


    public metrics_MetricSource(
        String name,        String metricLocation,        String filterPattern    ) {
        super(
        );
        this.name = name;
        this.metricLocation = metricLocation;
        this.filterPattern = filterPattern;
        this.metrics_mappingstatistics = new ArrayList<>();
    }

    public metrics_MetricSource(
        String name,        String metricLocation,        String filterPattern        ArrayList<metrics_MappingStatistic> metrics_mappingstatistics    ) {
        this.name = name;
        this.metricLocation = metricLocation;
        this.filterPattern = filterPattern;
        this.metrics_mappingstatistics = metrics_mappingstatistics;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMetriclocation() {
        return metricLocation;
    }

    public void setMetriclocation(String metricLocation) {
        this.metricLocation = metricLocation;
    }
    public String getFilterpattern() {
        return filterPattern;
    }

    public void setFilterpattern(String filterPattern) {
        this.filterPattern = filterPattern;
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
    public metrics_Metric getMetrics_metric() {
        return metrics_metric;
    }

    public void setMetrics_metric(metrics_Metric metrics_metric) {
        this.metrics_metric = metrics_metric;
    }

}