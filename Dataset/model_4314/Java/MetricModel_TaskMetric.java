





import java.util.List;
import java.util.ArrayList;

public class MetricModel_TaskMetric extends Metric {

    private String tasksBase;



    public MetricModel_TaskMetric(
        String tasksBase    ) {
        super(
        );
        this.tasksBase = tasksBase;
    }


    public String getTasksbase() {
        return tasksBase;
    }

    public void setTasksbase(String tasksBase) {
        this.tasksBase = tasksBase;
    }


}