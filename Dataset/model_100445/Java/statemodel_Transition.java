





import java.util.List;
import java.util.ArrayList;

public class statemodel_Transition  {

    private String guard;
    private String action;





    private statemodel_State statemodel_state;




    private statemodel_TransitionBlock statemodel_transitionblock;


    public statemodel_Transition(
        String guard,        String action    ) {
        this.guard = guard;
        this.action = action;
    }


    public String getGuard() {
        return guard;
    }

    public void setGuard(String guard) {
        this.guard = guard;
    }
    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }

    public statemodel_State getStatemodel_state() {
        return statemodel_state;
    }

    public void setStatemodel_state(statemodel_State statemodel_state) {
        this.statemodel_state = statemodel_state;
    }
    public statemodel_TransitionBlock getStatemodel_transitionblock() {
        return statemodel_transitionblock;
    }

    public void setStatemodel_transitionblock(statemodel_TransitionBlock statemodel_transitionblock) {
        this.statemodel_transitionblock = statemodel_transitionblock;
    }

}