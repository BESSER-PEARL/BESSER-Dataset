





import java.util.List;
import java.util.ArrayList;

public class rtsc_ClockConstraint  {

    private int bound;





    private rtsc_Transition rtsc_transition;




    private rtsc_Clock rtsc_clock;


    public rtsc_ClockConstraint(
        int bound    ) {
        this.bound = bound;
    }


    public int getBound() {
        return bound;
    }

    public void setBound(int bound) {
        this.bound = bound;
    }

    public rtsc_Transition getRtsc_transition() {
        return rtsc_transition;
    }

    public void setRtsc_transition(rtsc_Transition rtsc_transition) {
        this.rtsc_transition = rtsc_transition;
    }
    public rtsc_Clock getRtsc_clock() {
        return rtsc_clock;
    }

    public void setRtsc_clock(rtsc_Clock rtsc_clock) {
        this.rtsc_clock = rtsc_clock;
    }

}