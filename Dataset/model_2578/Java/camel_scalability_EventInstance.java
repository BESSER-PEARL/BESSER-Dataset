





import java.util.List;
import java.util.ArrayList;

public class camel_scalability_EventInstance  {

    private String status;
    private String layer;
    private String name;





    private SimpleEvent simpleevent;




    private MetricInstance metricinstance;


    public camel_scalability_EventInstance(
        String status,        String layer,        String name    ) {
        this.status = status;
        this.layer = layer;
        this.name = name;
    }


    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getLayer() {
        return layer;
    }

    public void setLayer(String layer) {
        this.layer = layer;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public SimpleEvent getSimpleevent() {
        return simpleevent;
    }

    public void setSimpleevent(SimpleEvent simpleevent) {
        this.simpleevent = simpleevent;
    }
    public MetricInstance getMetricinstance() {
        return metricinstance;
    }

    public void setMetricinstance(MetricInstance metricinstance) {
        this.metricinstance = metricinstance;
    }

}