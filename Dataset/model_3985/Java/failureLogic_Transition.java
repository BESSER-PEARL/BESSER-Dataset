





import java.util.List;
import java.util.ArrayList;

public class failureLogic_Transition extends BaseElement {

    private float transition;





    private failureLogic_ProbDist failurelogic_probdist;


    public failureLogic_Transition(
        float transition    ) {
        super(
        );
        this.transition = transition;
    }


    public float getTransition() {
        return transition;
    }

    public void setTransition(float transition) {
        this.transition = transition;
    }

    public failureLogic_ProbDist getFailurelogic_probdist() {
        return failurelogic_probdist;
    }

    public void setFailurelogic_probdist(failureLogic_ProbDist failurelogic_probdist) {
        this.failurelogic_probdist = failurelogic_probdist;
    }

}