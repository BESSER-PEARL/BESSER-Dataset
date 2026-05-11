





import java.util.List;
import java.util.ArrayList;

public class failureLogic_FaultTree extends FailureModel {






    private List<failureLogic_Cause> failurelogic_causes;


    public failureLogic_FaultTree(
    ) {
        super(
        );
        this.failurelogic_causes = new ArrayList<>();
    }

    public failureLogic_FaultTree(
        ArrayList<failureLogic_Cause> failurelogic_causes    ) {
        this.failurelogic_causes = failurelogic_causes;
    }


    public List<failureLogic_Cause> getFailurelogic_causes() {
        return failurelogic_causes;
    }

    public void addFailurelogic_cause(Failurelogic_cause failurelogic_cause) {
        this.failurelogic_causes.add(failurelogic_cause);
    }

}