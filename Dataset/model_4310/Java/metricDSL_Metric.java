





import java.util.List;
import java.util.ArrayList;

public class metricDSL_Metric  {

    private String name;





    private metricDSL_MetricModel metricdsl_metricmodel;


    public metricDSL_Metric(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public metricDSL_MetricModel getMetricdsl_metricmodel() {
        return metricdsl_metricmodel;
    }

    public void setMetricdsl_metricmodel(metricDSL_MetricModel metricdsl_metricmodel) {
        this.metricdsl_metricmodel = metricdsl_metricmodel;
    }

}