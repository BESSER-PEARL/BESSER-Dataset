





import java.util.List;
import java.util.ArrayList;

public class failureLogic_State extends BaseElement {

    private boolean isFailState;
    private boolean isInitialState;





    private failureLogic_Transition failurelogic_transition;




    private failureLogic_Transition failurelogic_transition;




    private failureLogic_Failure failurelogic_failure;


    public failureLogic_State(
        boolean isFailState,        boolean isInitialState    ) {
        super(
        );
        this.isFailState = isFailState;
        this.isInitialState = isInitialState;
    }


    public boolean getIsfailstate() {
        return isFailState;
    }

    public void setIsfailstate(boolean isFailState) {
        this.isFailState = isFailState;
    }
    public boolean getIsinitialstate() {
        return isInitialState;
    }

    public void setIsinitialstate(boolean isInitialState) {
        this.isInitialState = isInitialState;
    }

    public failureLogic_Transition getFailurelogic_transition() {
        return failurelogic_transition;
    }

    public void setFailurelogic_transition(failureLogic_Transition failurelogic_transition) {
        this.failurelogic_transition = failurelogic_transition;
    }
    public failureLogic_Transition getFailurelogic_transition() {
        return failurelogic_transition;
    }

    public void setFailurelogic_transition(failureLogic_Transition failurelogic_transition) {
        this.failurelogic_transition = failurelogic_transition;
    }
    public failureLogic_Failure getFailurelogic_failure() {
        return failurelogic_failure;
    }

    public void setFailurelogic_failure(failureLogic_Failure failurelogic_failure) {
        this.failurelogic_failure = failurelogic_failure;
    }

}