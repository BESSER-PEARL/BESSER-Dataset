





import java.util.List;
import java.util.ArrayList;

public class tfsm_plaink3_TemporalGuard extends Guard {

    private int afterDuration;





    private tfsm_plaink3_FSMClock tfsm_plaink3_fsmclock;


    public tfsm_plaink3_TemporalGuard(
        int afterDuration    ) {
        super(
        );
        this.afterDuration = afterDuration;
    }


    public int getAfterduration() {
        return afterDuration;
    }

    public void setAfterduration(int afterDuration) {
        this.afterDuration = afterDuration;
    }

    public tfsm_plaink3_FSMClock getTfsm_plaink3_fsmclock() {
        return tfsm_plaink3_fsmclock;
    }

    public void setTfsm_plaink3_fsmclock(tfsm_plaink3_FSMClock tfsm_plaink3_fsmclock) {
        this.tfsm_plaink3_fsmclock = tfsm_plaink3_fsmclock;
    }

}