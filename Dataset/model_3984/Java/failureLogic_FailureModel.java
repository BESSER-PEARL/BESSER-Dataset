





import java.util.List;
import java.util.ArrayList;

public class failureLogic_FailureModel extends BaseElement {






    private failureLogic_FailureModel failurelogic_failuremodel;




    private List<failureLogic_Failure> failurelogic_failures;




    private List<failureLogic_MinimalCutSets> failurelogic_minimalcutsetss;


    public failureLogic_FailureModel(
    ) {
        super(
        );
        this.failurelogic_failures = new ArrayList<>();
        this.failurelogic_minimalcutsetss = new ArrayList<>();
    }

    public failureLogic_FailureModel(
        ArrayList<failureLogic_Failure> failurelogic_failures,        ArrayList<failureLogic_MinimalCutSets> failurelogic_minimalcutsetss    ) {
        this.failurelogic_failures = failurelogic_failures;
        this.failurelogic_minimalcutsetss = failurelogic_minimalcutsetss;
    }


    public failureLogic_FailureModel getFailurelogic_failuremodel() {
        return failurelogic_failuremodel;
    }

    public void setFailurelogic_failuremodel(failureLogic_FailureModel failurelogic_failuremodel) {
        this.failurelogic_failuremodel = failurelogic_failuremodel;
    }
    public List<failureLogic_Failure> getFailurelogic_failures() {
        return failurelogic_failures;
    }

    public void addFailurelogic_failure(Failurelogic_failure failurelogic_failure) {
        this.failurelogic_failures.add(failurelogic_failure);
    }
    public List<failureLogic_MinimalCutSets> getFailurelogic_minimalcutsetss() {
        return failurelogic_minimalcutsetss;
    }

    public void addFailurelogic_minimalcutsets(Failurelogic_minimalcutsets failurelogic_minimalcutsets) {
        this.failurelogic_minimalcutsetss.add(failurelogic_minimalcutsets);
    }

}