





import java.util.List;
import java.util.ArrayList;

public class metricDSL_StepwiseMetric extends MetricDefinition {






    private List<metricDSL_BoundAndWeight> metricdsl_boundandweights;




    private metricDSL_Metric metricdsl_metric;


    public metricDSL_StepwiseMetric(
    ) {
        super(
        );
        this.metricdsl_boundandweights = new ArrayList<>();
    }

    public metricDSL_StepwiseMetric(
        ArrayList<metricDSL_BoundAndWeight> metricdsl_boundandweights    ) {
        this.metricdsl_boundandweights = metricdsl_boundandweights;
    }


    public List<metricDSL_BoundAndWeight> getMetricdsl_boundandweights() {
        return metricdsl_boundandweights;
    }

    public void addMetricdsl_boundandweight(Metricdsl_boundandweight metricdsl_boundandweight) {
        this.metricdsl_boundandweights.add(metricdsl_boundandweight);
    }
    public metricDSL_Metric getMetricdsl_metric() {
        return metricdsl_metric;
    }

    public void setMetricdsl_metric(metricDSL_Metric metricdsl_metric) {
        this.metricdsl_metric = metricdsl_metric;
    }

}