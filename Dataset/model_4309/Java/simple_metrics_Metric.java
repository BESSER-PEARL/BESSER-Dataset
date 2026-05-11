





import java.util.List;
import java.util.ArrayList;

public class simple_metrics_Metric  {

    private String name;
    private String value;





    private simple_metrics_MetricsSet simple_metrics_metricsset;


    public simple_metrics_Metric(
        String name,        String value    ) {
        this.name = name;
        this.value = value;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public simple_metrics_MetricsSet getSimple_metrics_metricsset() {
        return simple_metrics_metricsset;
    }

    public void setSimple_metrics_metricsset(simple_metrics_MetricsSet simple_metrics_metricsset) {
        this.simple_metrics_metricsset = simple_metrics_metricsset;
    }

}