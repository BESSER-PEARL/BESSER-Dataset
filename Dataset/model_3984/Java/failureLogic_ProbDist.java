





import java.util.List;
import java.util.ArrayList;

public class failureLogic_ProbDist extends BaseElement {

    private String type;





    private failureLogic_Failure failurelogic_failure;


    public failureLogic_ProbDist(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public failureLogic_Failure getFailurelogic_failure() {
        return failurelogic_failure;
    }

    public void setFailurelogic_failure(failureLogic_Failure failurelogic_failure) {
        this.failurelogic_failure = failurelogic_failure;
    }

}