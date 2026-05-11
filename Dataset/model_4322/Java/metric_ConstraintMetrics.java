





import java.util.List;
import java.util.ArrayList;

public class metric_ConstraintMetrics extends ConstraintMetric {

    private String numberOfConstraintsByKind;



    public metric_ConstraintMetrics(
        String numberOfConstraintsByKind    ) {
        super(
        );
        this.numberOfConstraintsByKind = numberOfConstraintsByKind;
    }


    public String getNumberofconstraintsbykind() {
        return numberOfConstraintsByKind;
    }

    public void setNumberofconstraintsbykind(String numberOfConstraintsByKind) {
        this.numberOfConstraintsByKind = numberOfConstraintsByKind;
    }


}