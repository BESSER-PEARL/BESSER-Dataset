





import java.util.List;
import java.util.ArrayList;

public class tfsm_TemporalGuard extends Guard {

    private String afterDuration;





    private tfsm_FSMClock tfsm_fsmclock;


    public tfsm_TemporalGuard(
        String afterDuration    ) {
        super(
        );
        this.afterDuration = afterDuration;
    }


    public String getAfterduration() {
        return afterDuration;
    }

    public void setAfterduration(String afterDuration) {
        this.afterDuration = afterDuration;
    }

    public tfsm_FSMClock getTfsm_fsmclock() {
        return tfsm_fsmclock;
    }

    public void setTfsm_fsmclock(tfsm_FSMClock tfsm_fsmclock) {
        this.tfsm_fsmclock = tfsm_fsmclock;
    }

}