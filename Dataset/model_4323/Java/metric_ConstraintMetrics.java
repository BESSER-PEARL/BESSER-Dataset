





import java.util.List;
import java.util.ArrayList;

public class metric_ConstraintMetrics extends ConstraintMetric {

    private String numberOfConstraintsByKind;





    private List<metric_Constraint> metric_constraints;




    private List<metric_ConstraintMetric> metric_constraintmetrics;


    public metric_ConstraintMetrics(
        String numberOfConstraintsByKind    ) {
        super(
        );
        this.numberOfConstraintsByKind = numberOfConstraintsByKind;
        this.metric_constraints = new ArrayList<>();
        this.metric_constraintmetrics = new ArrayList<>();
    }

    public metric_ConstraintMetrics(
        String numberOfConstraintsByKind        ArrayList<metric_Constraint> metric_constraints,        ArrayList<metric_ConstraintMetric> metric_constraintmetrics    ) {
        this.numberOfConstraintsByKind = numberOfConstraintsByKind;
        this.metric_constraints = metric_constraints;
        this.metric_constraintmetrics = metric_constraintmetrics;
    }

    public String getNumberofconstraintsbykind() {
        return numberOfConstraintsByKind;
    }

    public void setNumberofconstraintsbykind(String numberOfConstraintsByKind) {
        this.numberOfConstraintsByKind = numberOfConstraintsByKind;
    }

    public List<metric_Constraint> getMetric_constraints() {
        return metric_constraints;
    }

    public void addMetric_constraint(Metric_constraint metric_constraint) {
        this.metric_constraints.add(metric_constraint);
    }
    public List<metric_ConstraintMetric> getMetric_constraintmetrics() {
        return metric_constraintmetrics;
    }

    public void addMetric_constraintmetric(Metric_constraintmetric metric_constraintmetric) {
        this.metric_constraintmetrics.add(metric_constraintmetric);
    }

}