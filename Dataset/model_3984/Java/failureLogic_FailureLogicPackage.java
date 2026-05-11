





import java.util.List;
import java.util.ArrayList;

public class failureLogic_FailureLogicPackage  {






    private List<failureLogic_FailureModel> failurelogic_failuremodels;


    public failureLogic_FailureLogicPackage(
    ) {
        this.failurelogic_failuremodels = new ArrayList<>();
    }

    public failureLogic_FailureLogicPackage(
        ArrayList<failureLogic_FailureModel> failurelogic_failuremodels    ) {
        this.failurelogic_failuremodels = failurelogic_failuremodels;
    }


    public List<failureLogic_FailureModel> getFailurelogic_failuremodels() {
        return failurelogic_failuremodels;
    }

    public void addFailurelogic_failuremodel(Failurelogic_failuremodel failurelogic_failuremodel) {
        this.failurelogic_failuremodels.add(failurelogic_failuremodel);
    }

}