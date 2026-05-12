





import java.util.List;
import java.util.ArrayList;

public class stm_GuardCall  {

    private String parameters;





    private stm_Guard stm_guard;




    private stm_Transition stm_transition;




    private stm_SelfEvent stm_selfevent;


    public stm_GuardCall(
        String parameters    ) {
        this.parameters = parameters;
    }


    public String getParameters() {
        return parameters;
    }

    public void setParameters(String parameters) {
        this.parameters = parameters;
    }

    public stm_Guard getStm_guard() {
        return stm_guard;
    }

    public void setStm_guard(stm_Guard stm_guard) {
        this.stm_guard = stm_guard;
    }
    public stm_Transition getStm_transition() {
        return stm_transition;
    }

    public void setStm_transition(stm_Transition stm_transition) {
        this.stm_transition = stm_transition;
    }
    public stm_SelfEvent getStm_selfevent() {
        return stm_selfevent;
    }

    public void setStm_selfevent(stm_SelfEvent stm_selfevent) {
        this.stm_selfevent = stm_selfevent;
    }

}