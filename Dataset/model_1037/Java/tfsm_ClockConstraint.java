





import java.util.List;
import java.util.ArrayList;

public class tfsm_ClockConstraint extends ClockConstraintOperation {

    private int threshold;





    private tfsm_Clock tfsm_clock;


    public tfsm_ClockConstraint(
        int threshold    ) {
        super(
        );
        this.threshold = threshold;
    }


    public int getThreshold() {
        return threshold;
    }

    public void setThreshold(int threshold) {
        this.threshold = threshold;
    }

    public tfsm_Clock getTfsm_clock() {
        return tfsm_clock;
    }

    public void setTfsm_clock(tfsm_Clock tfsm_clock) {
        this.tfsm_clock = tfsm_clock;
    }

}