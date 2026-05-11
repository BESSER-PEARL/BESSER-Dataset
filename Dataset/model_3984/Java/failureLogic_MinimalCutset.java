





import java.util.List;
import java.util.ArrayList;

public class failureLogic_MinimalCutset extends BaseElement {






    private failureLogic_MinimalCutSets failurelogic_minimalcutsets;




    private List<failureLogic_Failure> failurelogic_failures;


    public failureLogic_MinimalCutset(
    ) {
        super(
        );
        this.failurelogic_failures = new ArrayList<>();
    }

    public failureLogic_MinimalCutset(
        ArrayList<failureLogic_Failure> failurelogic_failures    ) {
        this.failurelogic_failures = failurelogic_failures;
    }


    public failureLogic_MinimalCutSets getFailurelogic_minimalcutsets() {
        return failurelogic_minimalcutsets;
    }

    public void setFailurelogic_minimalcutsets(failureLogic_MinimalCutSets failurelogic_minimalcutsets) {
        this.failurelogic_minimalcutsets = failurelogic_minimalcutsets;
    }
    public List<failureLogic_Failure> getFailurelogic_failures() {
        return failurelogic_failures;
    }

    public void addFailurelogic_failure(Failurelogic_failure failurelogic_failure) {
        this.failurelogic_failures.add(failurelogic_failure);
    }

}