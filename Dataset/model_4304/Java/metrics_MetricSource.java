





import java.util.List;
import java.util.ArrayList;

public class metrics_MetricSource extends Base {

    private String filterPattern;
    private String name;
    private String metricLocation;





    private metrics_Mapping metrics_mapping;


    public metrics_MetricSource(
        String filterPattern,        String name,        String metricLocation    ) {
        super(
        );
        this.filterPattern = filterPattern;
        this.name = name;
        this.metricLocation = metricLocation;
    }


    public String getFilterpattern() {
        return filterPattern;
    }

    public void setFilterpattern(String filterPattern) {
        this.filterPattern = filterPattern;
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

    public metrics_Mapping getMetrics_mapping() {
        return metrics_mapping;
    }

    public void setMetrics_mapping(metrics_Mapping metrics_mapping) {
        this.metrics_mapping = metrics_mapping;
    }

}