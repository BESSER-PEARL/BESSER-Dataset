





import java.util.List;
import java.util.ArrayList;

public class failureLogic_MinimalCutset extends BaseElement {






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


    public List<failureLogic_Failure> getFailurelogic_failures() {
        return failurelogic_failures;
    }

    public void addFailurelogic_failure(Failurelogic_failure failurelogic_failure) {
        this.failurelogic_failures.add(failurelogic_failure);
    }

}