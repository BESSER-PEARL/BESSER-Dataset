





import java.util.List;
import java.util.ArrayList;

public class failureLogic_FailureModel extends BaseElement {






    private List<failureLogic_FailureModel> failurelogic_failuremodels;




    private failureLogic_FailureLogicPackage failurelogic_failurelogicpackage;


    public failureLogic_FailureModel(
    ) {
        super(
        );
        this.failurelogic_failuremodels = new ArrayList<>();
    }

    public failureLogic_FailureModel(
        ArrayList<failureLogic_FailureModel> failurelogic_failuremodels    ) {
        this.failurelogic_failuremodels = failurelogic_failuremodels;
    }


    public List<failureLogic_FailureModel> getFailurelogic_failuremodels() {
        return failurelogic_failuremodels;
    }

    public void addFailurelogic_failuremodel(Failurelogic_failuremodel failurelogic_failuremodel) {
        this.failurelogic_failuremodels.add(failurelogic_failuremodel);
    }
    public failureLogic_FailureLogicPackage getFailurelogic_failurelogicpackage() {
        return failurelogic_failurelogicpackage;
    }

    public void setFailurelogic_failurelogicpackage(failureLogic_FailureLogicPackage failurelogic_failurelogicpackage) {
        this.failurelogic_failurelogicpackage = failurelogic_failurelogicpackage;
    }

}