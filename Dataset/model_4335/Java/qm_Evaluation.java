





import java.util.List;
import java.util.ArrayList;

public class qm_Evaluation extends NamedElement {

    private int maximumPoints;
    private int completeness;





    private qm_Factor qm_factor;


    public qm_Evaluation(
        int maximumPoints,        int completeness    ) {
        super(
        );
        this.maximumPoints = maximumPoints;
        this.completeness = completeness;
    }


    public int getMaximumpoints() {
        return maximumPoints;
    }

    public void setMaximumpoints(int maximumPoints) {
        this.maximumPoints = maximumPoints;
    }
    public int getCompleteness() {
        return completeness;
    }

    public void setCompleteness(int completeness) {
        this.completeness = completeness;
    }

    public qm_Factor getQm_factor() {
        return qm_factor;
    }

    public void setQm_factor(qm_Factor qm_factor) {
        this.qm_factor = qm_factor;
    }

}