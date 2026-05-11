





import java.util.List;
import java.util.ArrayList;

public class metrics_MetricSource extends Base {

    private String name;
    private String filterPattern;
    private String metricLocation;





    private metrics_Mapping metrics_mapping;


    public metrics_MetricSource(
        String name,        String filterPattern,        String metricLocation    ) {
        super(
        );
        this.name = name;
        this.filterPattern = filterPattern;
        this.metricLocation = metricLocation;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getFilterpattern() {
        return filterPattern;
    }

    public void setFilterpattern(String filterPattern) {
        this.filterPattern = filterPattern;
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