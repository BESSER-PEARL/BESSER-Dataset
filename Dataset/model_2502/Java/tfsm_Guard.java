





import java.util.List;
import java.util.ArrayList;

public class tfsm_Guard  {

    private int time;





    private tfsm_Transition tfsm_transition;


    public tfsm_Guard(
        int time    ) {
        this.time = time;
    }


    public int getTime() {
        return time;
    }

    public void setTime(int time) {
        this.time = time;
    }

    public tfsm_Transition getTfsm_transition() {
        return tfsm_transition;
    }

    public void setTfsm_transition(tfsm_Transition tfsm_transition) {
        this.tfsm_transition = tfsm_transition;
    }

}