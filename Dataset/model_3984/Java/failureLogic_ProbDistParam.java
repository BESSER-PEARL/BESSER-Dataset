





import java.util.List;
import java.util.ArrayList;

public class failureLogic_ProbDistParam extends BaseElement {

    private String value;





    private failureLogic_ProbDist failurelogic_probdist;


    public failureLogic_ProbDistParam(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public failureLogic_ProbDist getFailurelogic_probdist() {
        return failurelogic_probdist;
    }

    public void setFailurelogic_probdist(failureLogic_ProbDist failurelogic_probdist) {
        this.failurelogic_probdist = failurelogic_probdist;
    }

}