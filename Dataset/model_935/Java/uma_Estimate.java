





import java.util.List;
import java.util.ArrayList;

public class uma_Estimate extends Guidance {

    private String group2;
    private String estimationMetric;
    private String estimationConsiderations;



    public uma_Estimate(
        String group2,        String estimationMetric,        String estimationConsiderations    ) {
        super(
        );
        this.group2 = group2;
        this.estimationMetric = estimationMetric;
        this.estimationConsiderations = estimationConsiderations;
    }


    public String getGroup2() {
        return group2;
    }

    public void setGroup2(String group2) {
        this.group2 = group2;
    }
    public String getEstimationmetric() {
        return estimationMetric;
    }

    public void setEstimationmetric(String estimationMetric) {
        this.estimationMetric = estimationMetric;
    }
    public String getEstimationconsiderations() {
        return estimationConsiderations;
    }

    public void setEstimationconsiderations(String estimationConsiderations) {
        this.estimationConsiderations = estimationConsiderations;
    }


}