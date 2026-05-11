





import java.util.List;
import java.util.ArrayList;

public class failureLogic_ProbDist extends BaseElement {

    private String type;





    private List<failureLogic_ProbDistParam> failurelogic_probdistparams;




    private failureLogic_Failure failurelogic_failure;


    public failureLogic_ProbDist(
        String type    ) {
        super(
        );
        this.type = type;
        this.failurelogic_probdistparams = new ArrayList<>();
    }

    public failureLogic_ProbDist(
        String type        ArrayList<failureLogic_ProbDistParam> failurelogic_probdistparams    ) {
        this.type = type;
        this.failurelogic_probdistparams = failurelogic_probdistparams;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<failureLogic_ProbDistParam> getFailurelogic_probdistparams() {
        return failurelogic_probdistparams;
    }

    public void addFailurelogic_probdistparam(Failurelogic_probdistparam failurelogic_probdistparam) {
        this.failurelogic_probdistparams.add(failurelogic_probdistparam);
    }
    public failureLogic_Failure getFailurelogic_failure() {
        return failurelogic_failure;
    }

    public void setFailurelogic_failure(failureLogic_Failure failurelogic_failure) {
        this.failurelogic_failure = failurelogic_failure;
    }

}