





import java.util.List;
import java.util.ArrayList;

public class tsm_TimeEvent  {

    private int time;





    private tsm_Transition tsm_transition;


    public tsm_TimeEvent(
        int time    ) {
        this.time = time;
    }


    public int getTime() {
        return time;
    }

    public void setTime(int time) {
        this.time = time;
    }

    public tsm_Transition getTsm_transition() {
        return tsm_transition;
    }

    public void setTsm_transition(tsm_Transition tsm_transition) {
        this.tsm_transition = tsm_transition;
    }

}