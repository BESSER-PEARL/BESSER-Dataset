





import java.util.List;
import java.util.ArrayList;

public class camel_requirement_OptimisationRequirement extends SoftRequirement {

    private String optimisationFunction;





    private Metric metric;




    private Property property;




    private requirement_camel_Application requirement_camel_application;




    private MetricContext metriccontext;




    private Component component;


    public camel_requirement_OptimisationRequirement(
        String optimisationFunction    ) {
        super(
        );
        this.optimisationFunction = optimisationFunction;
    }


    public String getOptimisationfunction() {
        return optimisationFunction;
    }

    public void setOptimisationfunction(String optimisationFunction) {
        this.optimisationFunction = optimisationFunction;
    }

    public Metric getMetric() {
        return metric;
    }

    public void setMetric(Metric metric) {
        this.metric = metric;
    }
    public Property getProperty() {
        return property;
    }

    public void setProperty(Property property) {
        this.property = property;
    }
    public requirement_camel_Application getRequirement_camel_application() {
        return requirement_camel_application;
    }

    public void setRequirement_camel_application(requirement_camel_Application requirement_camel_application) {
        this.requirement_camel_application = requirement_camel_application;
    }
    public MetricContext getMetriccontext() {
        return metriccontext;
    }

    public void setMetriccontext(MetricContext metriccontext) {
        this.metriccontext = metriccontext;
    }
    public Component getComponent() {
        return component;
    }

    public void setComponent(Component component) {
        this.component = component;
    }

}