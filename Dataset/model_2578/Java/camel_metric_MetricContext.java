





import java.util.List;
import java.util.ArrayList;

public class camel_metric_MetricContext extends ConditionContext {






    private Metric metric;




    private Schedule schedule;




    private Window window;


    public camel_metric_MetricContext(
    ) {
        super(
        );
    }



    public Metric getMetric() {
        return metric;
    }

    public void setMetric(Metric metric) {
        this.metric = metric;
    }
    public Schedule getSchedule() {
        return schedule;
    }

    public void setSchedule(Schedule schedule) {
        this.schedule = schedule;
    }
    public Window getWindow() {
        return window;
    }

    public void setWindow(Window window) {
        this.window = window;
    }

}