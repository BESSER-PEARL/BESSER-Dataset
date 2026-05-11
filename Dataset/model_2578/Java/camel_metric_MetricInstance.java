





import java.util.List;
import java.util.ArrayList;

public class camel_metric_MetricInstance  {

    private String name;





    private MetricContext metriccontext;


    public camel_metric_MetricInstance(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public MetricContext getMetriccontext() {
        return metriccontext;
    }

    public void setMetriccontext(MetricContext metriccontext) {
        this.metriccontext = metriccontext;
    }

}