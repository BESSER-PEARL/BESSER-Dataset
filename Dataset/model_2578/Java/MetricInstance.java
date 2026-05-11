





import java.util.List;
import java.util.ArrayList;

public class MetricInstance  {






    private camel_execution_Measurement camel_execution_measurement;




    private camel_metric_MetricModel camel_metric_metricmodel;




    private camel_metric_CompositeMetricInstance camel_metric_compositemetricinstance;


    public MetricInstance(
    ) {
    }



    public camel_execution_Measurement getCamel_execution_measurement() {
        return camel_execution_measurement;
    }

    public void setCamel_execution_measurement(camel_execution_Measurement camel_execution_measurement) {
        this.camel_execution_measurement = camel_execution_measurement;
    }
    public camel_metric_MetricModel getCamel_metric_metricmodel() {
        return camel_metric_metricmodel;
    }

    public void setCamel_metric_metricmodel(camel_metric_MetricModel camel_metric_metricmodel) {
        this.camel_metric_metricmodel = camel_metric_metricmodel;
    }
    public camel_metric_CompositeMetricInstance getCamel_metric_compositemetricinstance() {
        return camel_metric_compositemetricinstance;
    }

    public void setCamel_metric_compositemetricinstance(camel_metric_CompositeMetricInstance camel_metric_compositemetricinstance) {
        this.camel_metric_compositemetricinstance = camel_metric_compositemetricinstance;
    }

}