





import java.util.List;
import java.util.ArrayList;

public class efsm_AbstractState  {

    private String name;





    private efsm_Transition efsm_transition;




    private efsm_Transition efsm_transition;


    public efsm_AbstractState(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public efsm_Transition getEfsm_transition() {
        return efsm_transition;
    }

    public void setEfsm_transition(efsm_Transition efsm_transition) {
        this.efsm_transition = efsm_transition;
    }
    public efsm_Transition getEfsm_transition() {
        return efsm_transition;
    }

    public void setEfsm_transition(efsm_Transition efsm_transition) {
        this.efsm_transition = efsm_transition;
    }

}