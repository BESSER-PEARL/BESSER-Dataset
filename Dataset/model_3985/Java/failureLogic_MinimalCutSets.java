





import java.util.List;
import java.util.ArrayList;

public class failureLogic_MinimalCutSets extends BaseElement {






    private List<failureLogic_Failure> failurelogic_failures;




    private List<failureLogic_MinimalCutset> failurelogic_minimalcutsets;




    private failureLogic_FailureModel failurelogic_failuremodel;


    public failureLogic_MinimalCutSets(
    ) {
        super(
        );
        this.failurelogic_failures = new ArrayList<>();
        this.failurelogic_minimalcutsets = new ArrayList<>();
    }

    public failureLogic_MinimalCutSets(
        ArrayList<failureLogic_Failure> failurelogic_failures,        ArrayList<failureLogic_MinimalCutset> failurelogic_minimalcutsets    ) {
        this.failurelogic_failures = failurelogic_failures;
        this.failurelogic_minimalcutsets = failurelogic_minimalcutsets;
    }


    public List<failureLogic_Failure> getFailurelogic_failures() {
        return failurelogic_failures;
    }

    public void addFailurelogic_failure(Failurelogic_failure failurelogic_failure) {
        this.failurelogic_failures.add(failurelogic_failure);
    }
    public List<failureLogic_MinimalCutset> getFailurelogic_minimalcutsets() {
        return failurelogic_minimalcutsets;
    }

    public void addFailurelogic_minimalcutset(Failurelogic_minimalcutset failurelogic_minimalcutset) {
        this.failurelogic_minimalcutsets.add(failurelogic_minimalcutset);
    }
    public failureLogic_FailureModel getFailurelogic_failuremodel() {
        return failurelogic_failuremodel;
    }

    public void setFailurelogic_failuremodel(failureLogic_FailureModel failurelogic_failuremodel) {
        this.failurelogic_failuremodel = failurelogic_failuremodel;
    }

}